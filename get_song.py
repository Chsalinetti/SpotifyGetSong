from pprint import pprint
import requests
import time

def get_current_track(access_token, url):
    response = requests.get(
        url,
        headers={
            "Authorization" : f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists'][0]['name']

    return track_name + " - " + artists

