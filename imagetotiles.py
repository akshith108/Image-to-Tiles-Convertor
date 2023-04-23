from PIL import Image
import numpy as np
import math
from tkinter import filedialog
import os

rows = int(input("Enter number of rows image should be divided:"))
cols = int(input("Enter number of columns image should be divided:"))

img = Image.open(filedialog.askopenfilename())
img_x = np.shape(img)[1]
img_y = np.shape(img)[0]
reimg_x = math.floor(img_x / rows) * rows
reimg_y = math.floor(img_y / cols) * cols
reimg = np.array(img.resize((reimg_x, reimg_y)))
tile_size = (int(reimg_x / rows), int(reimg_y / cols))
path = filedialog.askdirectory()
for i in range(cols):
    for j in range(rows):
        tiled_array = reimg[i*tile_size[1]:(i+1)*tile_size[1], j*tile_size[0]:(j+1)*tile_size[0], :]
        tile_image = Image.fromarray(tiled_array)
        tile_image.save(os.path.join(path, f'tile_{i}{j}.png'))
