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
image_x = math.floor(img_x / rows) * rows
image_y = math.floor(img_y / cols) * cols
img = img.resize((image_x, image_y))
img = np.array(img)
image_x = np.shape(img)[1]
tile_size = (math.ceil(image_x / rows), math.ceil(image_y / cols))
num_cols = (img.shape[0] + tile_size[1] - 1) // tile_size[1]
num_rows = (img.shape[1] + tile_size[0] - 1) // tile_size[0]
padded_size = (num_rows * tile_size[0], num_cols * tile_size[1])
padded_image = Image.new("RGB", padded_size, color=(0, 0, 0))
padded_image.paste(Image.fromarray(img), box=(0, 0))
padded_array = np.array(padded_image)
tiled_array = np.tile(padded_array, (num_cols, num_rows, 1))
image_padded = Image.new('RGB', (tile_size[0], tile_size[1]))
path = filedialog.askdirectory()
for i in range(num_cols):
    for j in range(num_rows):
        img = tiled_array[i*tile_size[1]:(i+1)*tile_size[1], j*tile_size[0]:(j+1)*tile_size[0], :]
        tile_image = Image.fromarray(img)
        x_offset = j * tile_size[0]
        y_offset = i * tile_size[1]
        tile_array = tile_image
        image_padded.paste(tile_array, (x_offset, y_offset))
        tile_array.save(os.path.join(path, f'tile_{i}{j}.png'))
