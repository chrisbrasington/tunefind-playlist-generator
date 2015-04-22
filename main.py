import requests, json, sys, getpass
from gmusicapi import Mobileclient
# must load tunefind api keys
try:
	from keys import tunefind
except:
	print 'unable to load tunefind keys'
	sys.exit()
try:
	from keys import google
except:
	print '',

api = Mobileclient()

# get json
def get(url):
	response = requests.get(url, auth=(tunefind.username, tunefind.password))
	data = response.json()
	return data

# get entire show
def get_show(show):

	# get show's season information
	base_url = 'https://www.tunefind.com/api/v1/show/'
	url = base_url + show 
	return get(url)

# get individual song ID for google musc
def get_song_id(song):
	try:
		result = api.search_all_access(song,10)
	# occasionally creating bad search
	except:
		return False

	# take first song hit
	if len(result['song_hits']) > 0:
		found_song = result['song_hits'][0]
		id = found_song['track']['nid']
		print '\t', song.encode("utf-8")
		return id
	else:
		return False

# authenticate with google music
def login():
	global api

	logged_in = False

	# ask user for credentials if not loaded
	if 'google' not in globals():
		username = raw_input('google email: ')
		password = getpass.getpass('password: ')
		logged_in = api.login(username, password)	
	else:
		logged_in = api.login(google.username, google.password)

	if logged_in:
		return True
	else:
		print 'unable to login to google music'
		return False
	
# main
if __name__ == '__main__':	

	# input show name
	show = raw_input('Input show: ').lower()

	# authenticate to google music
	if login():
		
		# create playlist
		playlist_id = api.create_playlist(show)

		# load seasons in show
		data = get_show(show.replace(' ', '-'))
		
		# song id array (added per season to single playlist)
		song_ids = []

		# for each season
		for season in data['seasons']:
			season_url = season['tunefind_api_url']
			season_number = season['number']

			print show + ' Season: ' + season_number, '\n'

			data = get(season_url)

			# for each episode
			for episode in data['episodes']:
				
				data = get(season_url+'/'+episode['id'])

				# mismatch between sound count and data returned by API?
				print episode['name'].encode("utf-8"), ' songs: ', len(data['songs']), '/', episode['song_count']

				# for each song
				for song in data['songs']:
					#if(song['confidence'] == 'high'):
					search_song = song['artist']['name'] + ' - ' + song['name']

					# get song ID
					id = get_song_id(search_song)
					if(id):
						song_ids.append(id)
					#else:
					#	print search_song + ' (not found)'
				print
				
			# add season of music to playlist 
			print 'Adding to playlist: ' + show
			api.add_songs_to_playlist(playlist_id, song_ids)

			# clear song list
			song_ids[:] = []
	