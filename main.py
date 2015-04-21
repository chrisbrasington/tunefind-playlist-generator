import requests, pprint, json, time
from keys import api

# debug output
def debug(text):
	pprint.pprint(text)

# get json
def get(url):
	print
	print url
	response = requests.get(url, auth=(api.username, api.password))
	data = response.json()
	return data

# get entire show
def get_show(show):

	# get show's season information
	base_url = 'https://www.tunefind.com/api/v1/show/' #supernatural/season-1/5239
	url = base_url + show
	data = get(url)

	# count the number seasons
	seasons = int(data['seasons'][-1]['number'])

	# for each season
	for season in range(1,seasons+1):
		season_url = url + '/season-' + str(season)
		data = get(season_url)

		# get each episode id
		episodes = []
		for episode in data['episodes']:
			print episode['name'], '(', episode['id'], ')', ' songs: ', episode['song_count']
			episodes.append(episode['id'])

		raw_input('\nEnter to continue..')

		# for each episode, get songs
		for episode in episodes:
			data = get(season_url+'/'+episode)

			for song in data['songs']:
				print song['name'], '-', song['artist']['name'], '(', song['confidence'], ')'
			print
		break

# main
if __name__ == '__main__':	

	# test show
	get_show('supernatural')
	
	# user input
	'''
	show = ''
	while show != 'quit':
		show = raw_input('Input show: ')
		get_show(show)
	'''