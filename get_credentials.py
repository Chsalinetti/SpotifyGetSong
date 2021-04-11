from client_id import *
import webbrowser
import requests

AUTH_URL = 'https://accounts.spotify.com/api/token'

def get_credentials():

    webbrowser.open('https://accounts.spotify.com/authorize?client_id=' + CLIENT_ID +'&response_type=code&redirect_uri=https://api.spotify.com/v1/me/player/currently-playing&scope=user-read-currently-playing')
    cred_url = input("Enter URL: ")
    tokens = cred_url.split('=')
    code = tokens[1]
    
    



    url = 'https://api.spotify.com/v1/me/player/currently-playing'


    access_token = 0
    return access_token, url