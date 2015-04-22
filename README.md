# tunefind-playlist-generator

Uses [tunefind API](http://tunefind.com/api/) to find all music included in a television show. This code loops through all seasons and episodes of the TV show building a music playlist. It creates a google music playlist of the show name on found songs.

*The free TuneFind API restricts getting results less than a year old. There is a verification process to be granted access to real-time data.*

*Currently only working with television shows, movies pending.*

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
