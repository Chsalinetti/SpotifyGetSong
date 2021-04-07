from get_song import *
from info import *

def loop_current_track(token, url):
    while True:
        current_track_info = get_current_track(token, url)
        pprint(current_track_info, indent = 4)
        while True:
            if (current_track_info != get_current_track(token, url)):
                break
            else:
                time.sleep(5)

def main():
    loop_current_track(SPOTIFY_ACCESS_TOKEN, SPOTIFY_GET_CURRENT_TRACK_URL)    

if __name__ == '__main__':
    main()  