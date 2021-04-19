import requests
import time
import json
'''
Returns information on the current playing track given the access token and url
'''
def get_current_track(access_token, url):
    #get response from Spotify
    response = requests.get(
        url,
        headers={
            "Authorization" : f"Bearer {access_token}"
        }
    )
    try:
        #try to get info for current song
        resp_json = response.json()
        track_name = resp_json['item']['name']
        artists = resp_json['item']['artists'][0]['name']
        album = resp_json['item']['album']['name']
        date = resp_json['item']['album']['release_date']
        date = date.split("-")
        year = date[0]
        artwork = resp_json['item']['album']['images'][0]['url']
        line = "──────────────────────────────"
    except:
        #if current song can't be found, displays blank info
        track_name = ""
        artists = ""
        album = ""
        year = ""
        #artwork = "https://static.wikia.nocookie.net/impracticaljokers/images/d/d2/Sal.png/revision/latest/scale-to-width-down/250?cb=20190604013345"
        artwork = "https://upload.wikimedia.org/wikipedia/commons/7/71/Black.png"
        line = ""

    return track_name, artists, album, year, artwork, line
