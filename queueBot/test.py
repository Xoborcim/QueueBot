import discord
from discord.ext import commands

import matchmaking
import test2

import os
import sys

from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
if not token:
    sys.exit("DISCORD_TOKEN is not set. Copy .env.example to .env and fill it in.")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    await test2.create_provider()
    await test2.create_tournament(test2.provider_id)
    print("The bot is ready")


@bot.command()
async def matchmake(ctx):
    matchmaking.matchmake()
    teams = "**Blue Side**\n"
    for playerb in matchmaking.blue:
        teams += playerb[1] +  " " + str(playerb[2]) + "\n"
    teams += "**Red Side**\n"
    for playerr in matchmaking.red:
        teams += playerr[1] +  " " + str(playerr[2]) + "\n"
    embed = discord.Embed(title="Match Code: " + await test2.output_tournament(),
                          color=discord.Colour.blue(),
                          description=teams)
    await ctx.channel.send(embed=embed)
    matchmaking.clear_teams()


@bot.command()
async def queue(ctx):
    player_data = [0, ctx.author.name, 800]
    matchmaking.players.append(player_data)
    print(matchmaking.players)
    await ctx.channel.send(player_data)


bot.run(token)
