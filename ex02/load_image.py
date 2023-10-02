from PIL import Image
import numpy as np


def ft_load(path: str):
    img = Image.open(path)
    width, height = img.size
    if img.mode != "RGB":
        img = img.convert("RGB")

    img_array = np.array(img)
    print(
        f"The shape of image is: ({height}, {width}, {len(img_array[0][0])})")
    return img_array
