import requests
import time
import json
from client_id import *

def get_current_track(access_token, url):
    response = requests.get(
        url,
        headers={
            "Authorization" : f"Bearer {access_token}"
        }
    )
    try:
        resp_json = response.json()
        track_name = resp_json['item']['name']
        artists = resp_json['item']['artists'][0]['name']
        album = resp_json['item']['album']['name']
        date = resp_json['item']['album']['release_date']
        date = date.split("-")
        year = date[0]
        artwork = resp_json['item']['album']['images'][0]['url']
    except:
        print("Error Recieving Song Data!")
        track_name = "No Song Playing"
        artists = "No Current Artist"
        album = "No Current Album"
        year = "0000"
        artwork = "https://static.wikia.nocookie.net/impracticaljokers/images/d/d2/Sal.png/revision/latest/scale-to-width-down/250?cb=20190604013345"

    return track_name, artists, album, year, artwork

def song_checker(current_track_info, access_token, url):
    t = 0
    while (True):
        t += 1
        if (current_track_info != get_current_track(access_token, url) or t > 3400):
            time.sleep(1)
            break
        else:
            time.sleep(1)
    return t

def loop_current_track(access_token, url, refresh_token):
    while True:
        t = 0
        while (t < 1000):
            current_track_info = get_current_track(access_token, url)
            if (current_track_info == "invalid token!"):
                print("Error! invalid user or token!")
                break
            print(current_track_info)
            t_inc = song_checker(current_track_info, access_token, url)
            t += t_inc
            
        #refresh token
        request_body_params = {'grant_type':'refresh_token', 'refresh_token' : refresh_token, 'client_id' : CLIENT_ID , 'client_secret' : CLIENT_SECRET}
        response = requests.post(
            url='https://accounts.spotify.com/api/token',
            data = request_body_params
        )
        resp_json = response.json()
        access_token = resp_json['access_token']
