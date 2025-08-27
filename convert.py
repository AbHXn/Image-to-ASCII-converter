import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from os import system
from PIL import Image
import sys

ASCII_CODES = [' ', '.', '_', '~', '"', '=', 
                '*', '>', '?', '|', ']', '#', 
                '$', '@','A', 'B', 'C', 'X', 'W', 'M']
MAX_SIZE = len(ASCII_CODES)

def image_to_ascii(img_file, save_file):
    try:
        image = mpimg.imread(img_file)
        gray_image_255 = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
        if gray_image_255.max() <= 1.0:
            gray_image_255 = (gray_image_255 * 255).astype("int32")
        pil_img = Image.fromarray(gray_image_255)
        new_width, new_height = 256, 256
        resized = pil_img.resize((new_width, new_height), Image.LANCZOS)
        resized = np.clip(np.array(resized), 0, 255).astype("uint8")
        with open(save_file, "w") as file:
            for row in range(len(resized)):
                for col in range(len(resized[0])):
                    pixel = resized[row][col]
                    a_index = int((pixel / 255) * MAX_SIZE)
                    if a_index >= MAX_SIZE:
                        a_index -= 1
                    final_code = ASCII_CODES[a_index]
                    file.write(final_code)
                file.write('\n')
        print("DONE!")
        system(f"xdg-open {save_file}")
    except Exception as error:
        print(error)

if len(sys.argv) != 2:
    print("provied image file")
    sys.exit(0)

img_file = sys.argv[1]
save_file = img_file.split(".")[0]+".txt"
image_to_ascii(img_file, save_file)

