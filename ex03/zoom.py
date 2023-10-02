import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    '''
    Load an image, prints out its size, zoom in the image,
    converts it to grayscale and use matplotlib to plot it.

    Parameters:

    Returns:

    '''

    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)

        start_height = 70
        end_height = 470
        start_column = 450
        end_column = 850

        new_img_array = img_array[start_height:end_height,
                                  start_column:end_column, :]
        new_img = Image.fromarray(new_img_array)
        new_img = new_img.convert("L")
        new_gray_array = np.array(new_img)
        print(
            "TNew shape after slicing: " +
            f"{new_gray_array.reshape(400,400,1).shape} or " +
            f"{new_gray_array.shape} ")
        new_gray_array = new_gray_array.reshape(400, 400, 1)
        print(new_gray_array)
        plt.imshow(new_img, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interupted, exiting...")


if __name__ == "__main__":
    main()
