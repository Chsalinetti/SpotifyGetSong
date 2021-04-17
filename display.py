import io
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen
import tkinter.font as font

def display_song(track_name, artists, album, year, artwork_url):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg='black')
    #Album Art
    image_bytes = urlopen(artwork_url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((450, 450), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image)
    image_frame = tk.Label(master=root, image = tk_image, height=450, width = 450, bg="black")
    image_frame.pack()
    #Song Title
    if (len(track_name) > 30):
        track_name = track_name[:30] + "..."
    title_font = font.Font(family='Segoe', size=40, weight='bold')
    title_button = tk.Button(master=root, text=track_name, bg='black', height=0, activebackground='black', bd=-2, state='disabled', disabledforeground="white")
    title_button['font'] = title_font
    title_button.pack(fill=tk.X)
    #Artist
    artists_font = font.Font(family='Segoe', size=30, weight='normal')
    artists_button = tk.Button(master=root, text=artists, bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white")
    artists_button['font'] = artists_font
    artists_button.pack(fill=tk.X)
    #Album - Year
    album_font = font.Font(family='Segoe', size=10, weight='normal')
    album_button = tk.Button(master=root, text=(album + " - " + year), bg='black', height=0, activebackground='black', bd=0, state='disabled', disabledforeground="white")
    album_button['font'] = album_font
    album_button.pack(fill=tk.X)

    root.mainloop()


def main():
    url = "https://i.scdn.co/image/ab67616d0000b2731b2a9188ac775e16998eb78d"
    display_song("Wheel in the Sky", "Journey", "Infinity", "1978", url)


if __name__ == '__main__':
    main()  