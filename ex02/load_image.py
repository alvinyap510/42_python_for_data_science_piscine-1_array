from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    '''
    Load an image, prints out its size, and convert it
    into numpy array.

    Parameters:
    param1 (path: str): Path to the file to be converted.

    Returns:
    np.ndarray: Numpy array that represents the image
    '''
    try:
        img = Image.open(path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)
        print(
            f"The shape of image is: {img_array.shape}")
        return img_array
    except Exception as e:
        print(f"Error: {e}")
