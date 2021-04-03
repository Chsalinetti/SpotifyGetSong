from pprint import pprint
import requests
import time

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/mktnd699x5xqklxc1c2tvx1bi/player'
SPOTIFY_ACCESS_TOKEN = 'BQC_7eezCE_C8mi9OyNinKB2k3l9HCvWM2odN_wwvlRyA7shDOTVCvsfJcFrubTx54U-0ywAsaUBXa-W-mLAyQETGZ38KXsSMolJkAYVKhXnpxhO8V4x22509eFG6cSfeIuuT6TRTP9m_gT0vRtLVA2H5I2zq0SSCd7VvYqhzvlFqXPutl68npq_BNRO4nzR88HiWNuTNzW4SKXuGbvgTSYYvU9dygZxWTuT34mCZFWXMpGHrELjnwXfk8AKtibOkquA889CME1itm2-P-2Xs9xu0HAtf-QIIhLt2s67BxRw'

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization" : f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join(
        artists['name'] for artist in artists
    )
    link = resp_json['item']['external_urls']['spotify']


    current_track_info = {
        "id" : track_id,
        "name": track_name,
        "artists" : artists_names,
        "link" : link
    }

    return current_track_info

def main():
    while True:
        current_track_info = get_current_track(
            SPOTIFY_ACCESS_TOKEN
        )

        pprint(current_track_info, indent = 4)

        time.sleep(2)

if __name__ == '__main__':
    main()