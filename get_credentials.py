from client_id import *
import webbrowser
import requests

AUTH_URL = 'https://accounts.spotify.com/api/token'

def get_credentials():

    webbrowser.open('https://accounts.spotify.com/authorize?client_id=' + CLIENT_ID +'&response_type=code&redirect_uri=https://api.spotify.com/v1/me/player/currently-playing&scope=user-read-currently-playing')
    cred_url = input("Enter URL: ")
    tokens = cred_url.split('=')
    code = tokens[1]
    
    request_body_params = {'grant_type':'authorization_code', 'code' : code, 'redirect_uri' : 'https://api.spotify.com/v1/me/player/currently-playing' , 'client_id' : CLIENT_ID , 'client_secret' : CLIENT_SECRET}
    response = requests.post(
        url='https://accounts.spotify.com/api/token',
        data = request_body_params
    )
    resp_json = response.json()
    access_token = resp_json['access_token']
    expires_in = resp_json['expires_in']
    refresh_token= resp_json['refresh_token']
    
    url = 'https://api.spotify.com/v1/me/player/currently-playing'
    return access_token, url