import io
from PIL import Image, ImageTk

try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
def resize(w, h, w_box, h_box, pil_image):
    f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)
root = tk.Tk()
# size of image display box you want
# Size of desired image display
w_box = 560
h_box = 160

url = "https://i.scdn.co/image/ab67616d0000b2731b2a9188ac775e16998eb78d"

image_bytes = urlopen(url).read()
data_stream = io.BytesIO(image_bytes)

# Open as a PIL image object
pil_image = Image.open(data_stream)

# Get the original size of the image
w, h = pil_image.size

# Scale the image to keep it in scale and within a rectangle
pil_image_resized = resize(w, h, w_box, h_box, pil_image)

# You can also display the zoomed image information to get the size
wr, hr = pil_image_resized.size

# Title block display: zoomed image file name and size
fname = url.split('/')[-1]
sf = "resized {} ({}x{})".format(fname, wr, hr)
root.title(sf)

# Convert PIL image object to Tkinter's PhotoImage object
tk_image = ImageTk.PhotoImage(pil_image_resized)

# Label: this gadget is a display box, a small window, which displays the image size to the specified display box
label = tk.Label(root, image=tk_image, width=w_box, height=h_box)
# padx,pady is the distance between the image and the edge of the window
label.pack(padx=5, pady=5)
root.mainloop()