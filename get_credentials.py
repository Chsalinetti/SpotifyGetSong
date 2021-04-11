from client_id import *
import requests

AUTH_URL = 'https://accounts.spotify.com/api/token'

def get_credentials():
    response = requests.get('https://accounts.spotify.com/authorize?client_id=' + CLIENT_ID +'&response_type=code&redirect_uri=https://api.spotify.com/v1/me/player/currently-playing&scope=user-read-currently-playing')
    print(response)
    print(response.text)
    access_token = input()
    url = 'https://api.spotify.com/v1/me/player/currently-playing'

    return access_token, url