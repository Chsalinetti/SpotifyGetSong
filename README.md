# Improved Spotify Current Song Display

This program displays information about a Spotify user's currently playing song in a Tkinter GUI.

Charlie Salinetti
@sultanofswing
2021

## GitHub Page

The program can be found [here](https://github.com/Chsalinetti/SpotifyGetSong).

## Usage

The program authenticates the user through Spotify's API, which opens a webpage where the user approves the program,
and is directed to a website. When the link to the website is copied into the Python program, a code is recieved and sent
back to Spotify. The JSON response is parced to recieve a user token, which allows requests to be made about the user's
currently playing song.

Using the Python GUI Tkinter, a display is created. Using more API requests, the program is able recieve information about
the current song being played and update the user's token which will expire after an hour. Using threading, the display is
updated every second to check info about the current song being played, and the information in the Tkinter GUI is updated.
The program will also stop displaying the song if none are being played at that moment, in the event that Spotify is closed
or the program temorarily loses internet connection.

A Raspberry PI can be used to have this program displayed by itself on a monitor.

## Implementation
This program requires the following libraries to be impemented:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

This program requires a client_id.py file with the following implementation:

```python
import requests

CLIENT_ID = '41da94c0f5f94c14927a75b502c9d21d'
CLIENT_SECRET = '<client secret>'
```

Email me at chsalinetti@gmail.com if you would like the program for personal use and need the CLIENT_SECRET.
