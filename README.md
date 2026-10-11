# QueueBot

A Discord bot that queues players for League of Legends custom games, splits them into
Blue/Red teams, and generates a tournament code via the Riot API.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in DISCORD_TOKEN and RIOT_API_KEY
cd queueBot && python test.py
```

Commands: `$queue` to join, `$matchmake` to build teams.
