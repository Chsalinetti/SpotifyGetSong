from client_id import *
import webbrowser
import requests

AUTH_URL = 'https://accounts.spotify.com/api/token'
'''
Gets credentials from Spotify
'''
def get_credentials():
    #Open website
    webbrowser.open('https://accounts.spotify.com/authorize?client_id=' + CLIENT_ID +'&response_type=code&redirect_uri=https://api.spotify.com/v1/me/player/currently-playing&scope=user-read-currently-playing', new=1)
    #get url from site to get code
    cred_url = input("Enter URL: ")
    tokens = cred_url.split('=')
    code = tokens[1]
    #get credentials
    request_body_params = {'grant_type':'authorization_code', 'code' : code, 'redirect_uri' : 'https://api.spotify.com/v1/me/player/currently-playing' , 'client_id' : CLIENT_ID , 'client_secret' : CLIENT_SECRET}
    response = requests.post(
        url='https://accounts.spotify.com/api/token',
        data = request_body_params
    )
    #get access_token and refresh_token
    resp_json = response.json()
    access_token = resp_json['access_token']
    refresh_token= resp_json['refresh_token']
    #url for currently playing song
    url = 'https://api.spotify.com/v1/me/player/currently-playing'
    #return information
    return access_token, url, refresh_token