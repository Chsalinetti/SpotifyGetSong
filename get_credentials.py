from client_id import *
import webbrowser

AUTH_URL = 'https://accounts.spotify.com/api/token'

def get_credentials():

    webbrowser.open('https://accounts.spotify.com/authorize?client_id=' + CLIENT_ID +'&response_type=code&redirect_uri=https://api.spotify.com/v1/me/player/currently-playing&scope=user-read-currently-playing', new = 2)







    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    print(access_token)
    url = 'https://api.spotify.com/v1/me/player/currently-playing'

    return access_token, url