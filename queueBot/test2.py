from pantheon import pantheon
import asyncio
server = "na1"
api_key = Rito Api Key
data = {
  "mapType": "SUMMONERS_RIFT",
  "pickType": "TOURNAMENT_DRAFT",
  "spectatorType": "ALL",
  "teamSize": 5
}


def requestsLog(url, status, headers):
    # print(url)
    # print(status)
    # print(headers)
    pass

provider_id = 0
tournament_id = 0

panth = pantheon.Pantheon(server=server, api_key=api_key, auto_retry=True, requests_logging_function=requestsLog, debug=True)


async def create_provider():
    global provider_id
    provider_id = await panth.register_provider("NA", "https://microboxmedia.github.io", stub=True)


async def create_tournament(provider):
    global tournament_id
    tournament_id = await panth.register_tournament(provider, "Name is funny", stub=True)


async def create_tournament_code(tournament_id):
    return await panth.create_tournament_code(tournament_id, data=data, nb_codes=1, stub=True)


async def output_tournament():
    tournament_code = await create_tournament_code(tournament_id)
    code = tournament_code[0]
    return code

