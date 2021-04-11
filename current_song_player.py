from get_credentials import get_credentials
from get_song import get_current_track
from get_song import loop_current_track

def play_current():
    access_token, url = get_credentials()  
    loop_current_track(access_token, url)

def main():
    play_current()

if __name__ == '__main__':
    main()  