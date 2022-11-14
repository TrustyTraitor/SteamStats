import requests
import json

from auth import AUTH_TOKEN
from auth import MY_STEAM_ID


def __get_friends_list(steam_id):
	address = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={AUTH_TOKEN}&steamid={steam_id}&relationship=friend'

	result = requests.get(address).text
	result = json.loads(result)['friendslist']['friends']

	return result


def get_account_names():
	friends_list = __get_friends_list(MY_STEAM_ID)

	friend_ids = []
	for friend in friends_list:
		friend_ids.append(friend['steamid'])

	friend_ids = ','.join(friend_ids)

	address = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={AUTH_TOKEN}&steamids={friend_ids}'

	result = requests.get(address).text
	result = json.loads(result)['response']['players']

	friends = []
	for friend in result:
		friends.append( (friend['steamid'], friend['personaname']) )

	return friends
