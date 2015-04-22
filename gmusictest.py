from gmusicapi import Mobileclient
from keys import google
import pprint, json

# debug output
def debug(text):
	pprint.pprint(text)

if __name__ == '__main__':	

	artist = 'Kansas'
	title = 'Carry On My Wayward Son'

	search = title + ' - ' + artist
	print search

	api = Mobileclient()
	logged_in = api.login(google.username, google.password)

	print logged_in

	result = api.search_all_access(search,10)

	f = open('result.json', 'w')
	f.write(json.dumps(result))

	song = result['song_hits'][0]
	id = song['track']['nid']

	playlist_id = api.create_playlist('Playlist Test')
	api.add_songs_to_playlist(playlist_id, id)

	print 'done'
