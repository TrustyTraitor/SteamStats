import matplotlib.pyplot as plt
import get_stats

from auth import MY_STEAM_ID


def create_plot(json_data):
	plt.style.use('ggplot')
	plt.rcParams['toolbar'] = 'None'

	num_of_games = len(json_data['response']['games'])
	playtimes = []
	for item in json_data['response']['games']:
		playtimes.append(item['playtime_forever']/60)

	playtimes.sort(reverse=True)
	plt.plot(range(0,num_of_games), playtimes)

	plt.title("Hours spent in games owned on Steam")
	plt.ylabel("Hours Played")
	plt.xlabel("Games")

	total_playtime = sum(playtimes)

	plt.text(num_of_games/2, playtimes[0]/2, f'Total PlayTime (Hrs): {round(total_playtime)}')

	playtimes_without_zeros = list(filter(lambda a: a != 0, playtimes))
	num_of_games = len(playtimes_without_zeros)

	twenty_percent_count = (num_of_games * 0.2)+1

	twenty_percent_playtime = sum(playtimes[0:round(twenty_percent_count)])
	eighty_percent_playtime = sum(playtimes[round(twenty_percent_count):num_of_games])
	total_playtime = twenty_percent_playtime + eighty_percent_playtime
	print(f'Twenty Percent of Games playtime: {round(twenty_percent_playtime)}Hrs which is {round((twenty_percent_playtime/total_playtime)*100)} percent of total playtime')
	print(f'Eighty Percent of Games playtime: {round(eighty_percent_playtime)}Hrs which is {round((eighty_percent_playtime/total_playtime)*100)} percent of total playtime')

	plt.show()


if __name__ == '__main__':
	json_data = get_stats.get_json(MY_STEAM_ID)
	create_plot(json_data)
