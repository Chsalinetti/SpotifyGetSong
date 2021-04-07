from info import *
from get_credentials import *
from get_song import *

def play_current():
    test = input("!!!Enter test for testing!!! ")

    if (test == "test"):
        access_token = SPOTIFY_ACCESS_TOKEN
        url = SPOTIFY_GET_CURRENT_TRACK_URL
    else:
        access_token, url = get_credentials()
    
    loop_current_track(access_token, url )

def main():
    play_current()

if __name__ == '__main__':
    main()  