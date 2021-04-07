from pprint import pprint
import requests
import time

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'BQAmk3Qwz0uFUI2OkiqbfeW-pZveBRElfFKsr3mGBS2xjwQ2-M8-at34_ojzVkE_ChB3-SGTXsdZIprqtkiW9nyS2dWE9LHXxqp77cBnqqJFGiROcxJQOZRHHfpPz_ylwcORdIi5lG7IWNZDjM3fmC7uzgqXOZu0Mihu6eMjRLGEQeT3mlltme8wfhZQu5lqTFLrK2foA8Kos46JIVQ77Oqz-hAHC1Tg-S3W6fAi2Z5vm_3SZFT6Vd2-wgWBXWmEN7pVeX9hyUIBhBtF1-Ae6QL87k3l7x38i459Ndva98NB'
def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization" : f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists'][0]['name']

    return track_name + " - " + artists

def main():
    while True:
        current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
        pprint(current_track_info, indent = 4)
        time.sleep(10)

if __name__ == '__main__':
    main()