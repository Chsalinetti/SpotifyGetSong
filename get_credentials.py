def get_credentials():
    access_token = input("Enter Access Token: ")
    username = input("Enter Username: ")
    url = 'https://api.spotify.com/v1/'+ username +'/player/currently-playing'

    return access_token, url