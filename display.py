import io
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen
import tkinter.font as font
import time

def display_song(track_name, artists, album, year, artwork_url):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg='black')
    #top
    line_font = font.Font(family='Segoe', size=20, weight='normal')
    line_button = tk.Button(master=root, text=" ", bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white")
    line_button['font'] = line_font
    line_button.pack(fill=tk.X)
    #Album Art
    image_bytes = urlopen(artwork_url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((400, 400), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image)
    image_frame = tk.Label(master=root, image = tk_image, height=400, width = 400, bg="black")
    image_frame.pack()
    #Song Title
    if (len(track_name) > 30):
        track_name = track_name[:30] + "..."
    title_font = font.Font(family='Segoe', size=40, weight='bold')
    title_button = tk.Button(master=root, text=(track_name), bg='black', height=0, activebackground='black', bd=-2, state='disabled', disabledforeground="white")
    title_button['font'] = title_font
    title_button.pack(fill=tk.X)
    #Underscore
    line_font = font.Font(family='Segoe', size=10, weight='normal')
    line_button = tk.Button(master=root, text="──────────────────────────────", bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white")
    line_button['font'] = line_font
    line_button.pack(fill=tk.X)
    #Artist
    artists_font = font.Font(family='Segoe', size=25, weight='normal')
    artists_button = tk.Button(master=root, text=artists, bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white")
    artists_button['font'] = artists_font
    artists_button.pack(fill=tk.X)
    #Album - Years
    album_font = font.Font(family='Segoe', size=10, weight='normal')
    album_button = tk.Button(master=root, text=(album + " - " + year), bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white")
    album_button['font'] = album_font
    album_button.pack(fill=tk.X)

    root.mainloop()


def main():
    url = "https://i.scdn.co/image/ab67616d0000b2731b2a9188ac775e16998eb78d"
    display_song("Wheel in the Sky", "Journey", "Infinity", "1978", url)
    time.sleep(5)
    url = "https://i.scdn.co/image/ab67616d0000b27398260c528e6eec9dd431c1d7"
    display_song("Sunday Morning", "The Velvet Underground", "Nico", "1967", url)


if __name__ == '__main__':
    main()  