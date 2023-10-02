from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        # Open the image
        img = Image.open(path)

        # Ensure the image is in RGB format
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Convert image to numpy array
        img_array = np.array(img)

        # Print image details
        print(f"The shape of the image is: {img_array.shape}")

        return img_array

    except IOError:
        raise ValueError(
            f"Error: Unable to load image at '{path}'. Ensure the file exists and is a valid JPG/JPEG image.")
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")


# Tester
if __name__ == "__main__":
    from load_image import ft_load
    img_content = ft_load("landscape.jpg")
    print(img_content)
