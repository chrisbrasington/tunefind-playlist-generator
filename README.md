# tunefind-playlist-generator

Uses [tunefind API](http://tunefind.com/api/) to find all music included in a television show. This code loops through all seasons and episodes of the TV show building a music playlist. It creates a google music playlist of the show name on found songs.

Currently only working with television shows, movies pending.

###keys.py 
Not included in repository, but add your API keys to a python file as such..

```
# tunefind API keys
# populate these with your API key values
class tunefind:
    username = ''
    password = ''
```