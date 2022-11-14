import requests
import json

from auth import AUTH_TOKEN


def get_json(steam_id):
	address = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={AUTH_TOKEN}&steamid={steam_id}&format=json'

	result = requests.get(address).text
	result = json.loads(result)

	return result
