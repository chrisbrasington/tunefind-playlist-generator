# tunefind-playlist-generator

Uses [tunefind API](http://tunefind.com/api/) to find all music included in a television show. This code loops through all seasons and episodes of the TV show building a music playlist. It creates a google music playlist of the show name on found songs.

*Currently only working with television shows, movies pending.*

*Contacting tunefind because unverified (low confidence) songs are suspected as not being returned by the API. The episode will have song_count, but return an empty string of songs.*

###gmusicapi
Uses [gmusicapi](https://github.com/simon-weber/Unofficial-Google-Music-API) to authenticate and create a playlist on google-music. [Further documentation here](https://unofficial-google-music-api.readthedocs.org/en/latest/). **gmusicapi is not supported nor endorsed by Google,** but it is actively maintained.

###keys.py 
Not included in repository, but add your API keys to a python file as such..

```
# tunefind API keys
# populate these with your API key values
class tunefind:
    username = ''
    password = ''
```
