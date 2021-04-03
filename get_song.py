from pprint import pprint
import requests

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/mktnd699x5xqklxc1c2tvx1bi/player'
SPOTIFY_ACCESS_TOKEN = 'BQC_7eezCE_C8mi9OyNinKB2k3l9HCvWM2odN_wwvlRyA7shDOTVCvsfJcFrubTx54U-0ywAsaUBXa-W-mLAyQETGZ38KXsSMolJkAYVKhXnpxhO8V4x22509eFG6cSfeIuuT6TRTP9m_gT0vRtLVA2H5I2zq0SSCd7VvYqhzvlFqXPutl68npq_BNRO4nzR88HiWNuTNzW4SKXuGbvgTSYYvU9dygZxWTuT34mCZFWXMpGHrELjnwXfk8AKtibOkquA889CME1itm2-P-2Xs9xu0HAtf-QIIhLt2s67BxRw'

def get_current_track(access_token):
    respone = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
    )

def main():
    current_track_info = get_current_track(
        SPOTIFY_ACCESS_TOKEN
    )

    pprint(current_track_info, indent = 4)

if __main__ == '__main__':
    main()