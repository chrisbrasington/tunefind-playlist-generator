import requests, json, sys, getpass
from gmusicapi import Mobileclient

# must load tunefind api keys
try:
    from keys import tunefind
except:
    print("Unable to load tunefind keys")
    sys.exit()
try:
    from keys import google
except ImportError as e:
    print("Could not find google keys in keys.py")

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
        result = api.search(song,10)
    # occasionally creating bad search
    except Exception as e:
        print(e)
        return False

    # take first song hit
    if len(result['song_hits']) > 0:
        found_song = result['song_hits'][0]
        song_id = found_song['track']['nid']
        print '\t', song 
        return song_id
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
        logged_in = api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)	
    else:
        logged_in = api.login(google.username, google.password, Mobileclient.FROM_MAC_ADDRESS)

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
                    artist_name = song['artist']['name']
                    song_name = song['name']

                    if not artist_name or not song_name:
                        continue
                    else:
                        artist_name = artist_name.encode("utf-8")
                        song_name = song_name.encode("utf-8")

                    search_song = "{} - {}".format(artist_name, song_name)

                    # get song ID
                    song_id = get_song_id(search_song)
                    if song_id:
                        song_ids.append(song_id)

                    print
                        
                # add season of music to playlist 
                print 'Adding to playlist: ' + show
                api.add_songs_to_playlist(playlist_id, song_ids)

                # clear song list
                song_ids[:] = []
