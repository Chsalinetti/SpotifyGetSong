import io
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen
import tkinter.font as font
import time
from get_credentials import get_credentials
from get_song import get_current_track
import requests
from client_id import *
import json
from threading import Thread
'''
Updates the display with new song information
'''
def display_update(root,image_frame, title_button, line_button, artists_button, album_button, access_token, url, refresh_token, counter):
    #loop forever
    while (True):
        #run counter, after 1500 seconds token will refresh. Token expires after 3600 seconds.
        if (counter > 1500):
            print("Refreshing Token...")
            try :
                #refresh tokens
                request_body_params = {'grant_type':'refresh_token', 'refresh_token' : refresh_token, 'client_id' : CLIENT_ID , 'client_secret' : CLIENT_SECRET}
                response = requests.post(
                    url='https://accounts.spotify.com/api/token',
                    data = request_body_params
                )
                resp_json = response.json()
                access_token = resp_json['access_token']
                counter = 0
                print("Token Refreshed!")
            except :
                print("Unable to refresh!")
        #get current info
        current_track_name = title_button['text']
        current_artist = artists_button['text']
        current_album = album_button['text']
        #get current track info
        track_name, artists, album, year, artwork_url, line = get_current_track(access_token, url)
        #check to see if update is needed
        if (current_track_name != track_name or current_artist != artists or current_album != (album + " - " + year)):
            #image
            try:
                image_bytes = urlopen(artwork_url).read()
                data_stream = io.BytesIO(image_bytes)
                pil_image = Image.open(data_stream)
                pil_image = pil_image.resize((400, 400), Image.ANTIALIAS)
                tk_image = ImageTk.PhotoImage(pil_image)
                image_frame['image'] = tk_image
            except:
                print ("Image Error!")
            #title
            if (len(track_name) > 40):
                track_name = track_name[:40] + "..."
            title_button['text'] = track_name
            #line
            line_button['text'] = line
            #artists
            artists_button['text'] = artists
            #albums
            if (album == ""):
                album_button['text'] = ""
            else:
                album_button['text'] = album + " - " + year
        #increase counter
        time.sleep(1)
        counter += 1
'''
Display current song using Tkinter
'''
def display_song():
    #get credentials
    access_token, url, refresh_token = get_credentials()
    #get current song
    track_name, artists, album, year, artwork_url, line = get_current_track(access_token, url)
    #Initilize Tkinter
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg='black')
    #top border
    line_font = font.Font(family='Segoe', size=20, weight='normal')
    line_button = tk.Button(master=root, text=" ", bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white", borderwidth=0, highlightbackground="black")
    line_button['font'] = line_font
    line_button.pack(fill=tk.X)
    #Album Art
    image_bytes = urlopen(artwork_url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((400, 400), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image)
    image_frame = tk.Label(master=root, image = tk_image, height=400, width = 400, bg="black", borderwidth=0, highlightbackground="black")
    image_frame.pack()
    #Song Title
    if (len(track_name) > 40):
        track_name = track_name[:40] + "..."
    title_font = font.Font(family='Copperplate Gothic Bold', size=35, weight='normal')
    title_button = tk.Button(master=root, text=(track_name), bg='black', height=0, activebackground='black', bd=-2, state='disabled', disabledforeground="white", borderwidth=0, highlightbackground="black")
    title_button['font'] = title_font
    title_button.pack(fill=tk.X)
    #Underscore
    line_font = font.Font(family='Segoe', size=10, weight='normal')
    line_button = tk.Button(master=root, text=line, bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white", borderwidth=0, highlightbackground="black")
    line_button['font'] = line_font
    line_button.pack(fill=tk.X)
    #Artist
    artists_font = font.Font(family='Bahnschrift SemiLight SemiCondensed', size=25, weight='normal')
    artists_button = tk.Button(master=root, text=artists, bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white", borderwidth=0, highlightbackground="black")
    artists_button['font'] = artists_font
    artists_button.pack(fill=tk.X)
    #Album - Years
    #blank checker
    if (album == ""):
            album_button_text = ""
    else:
        album_button_text = album + " - " + year

    album_font = font.Font(family='Bahnschrift Light SemiCondensed', size=10, weight='normal')
    album_button = tk.Button(master=root, text=(album_button_text), bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white", borderwidth=0, highlightbackground="black")
    album_button['font'] = album_font
    album_button.pack(fill=tk.X)
    #create thread to update display constatly
    Thread(target=display_update, args=(root, image_frame ,title_button, line_button, artists_button, album_button, access_token, url, refresh_token, 0)).start()
    root.mainloop()