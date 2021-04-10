import requests
import time
import json

def get_current_track(access_token, url):
    response = requests.get(
        url,
        headers={
            "Authorization" : f"Bearer {access_token}"
        }
    )
    resp_json = response.json()
    try:
        track_name = resp_json['item']['name']
        artists = resp_json['item']['artists'][0]['name']
        album = resp_json['item']['album']['name']
    except:
        return "invalid token!"

    return "\n" + track_name + "\n" + artists + "\n[" + album + "]"

def loop_current_track(access_token, url):
    while True:
        current_track_info = get_current_track(access_token, url)
        if (current_track_info == "invalid token!"):
            print("Error! invalid user or token!")
            break
        print(current_track_info)
        while True:
            if (current_track_info != get_current_track(access_token, url)):
                break
            else:
                time.sleep(5)