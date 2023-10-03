from PIL import Image
import numpy as np


def ft_invert(array) -> np.array:
    '''
    Inverts the color of the image received.

    Parameters:
    array (np.array): A 3D numpy array representing an RGB image.

    Returns:
    np.array: The inverse-colored image array.
    '''
    try:
        if not isinstance(array, np.ndarray) or not array.ndim == 3:
            raise ValueError("Input must be a 3d numpy array")
        inverted_array = 255 - array
        inverted_array = inverted_array.astype(np.uint8)
        img = Image.fromarray(inverted_array)
        img.show()
        return inverted_array
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interupted, exiting...")


def ft_red(array) -> np.array:
    '''
    Convert an image into red scale.

    Parameters:
    array (np.array): A 3D numpy array representing an RGB image.

    Returns:
    np.array: The red-scaled image array.
    '''
    try:
        if not isinstance(array, np.ndarray) or not array.ndim == 3:
            raise ValueError("Input must be a 3d numpy array")
        red_scale_array = array.copy()
        red_scale_array[:, :, 1] = 0
        red_scale_array[:, :, 2] = 0
        img = Image.fromarray(red_scale_array)
        img.show()
        return red_scale_array
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interupted, exiting...")


def ft_green(array) -> np.array:
    '''
    Convert an image into green scale.

    Parameters:
    array (np.array): A 3D numpy array representing an RGB image.

    Returns:
    np.array: The green-scaled image array.
    '''
    try:
        if not isinstance(array, np.ndarray) or not array.ndim == 3:
            raise ValueError("Input must be a 3d numpy array")
        green_scale_array = array.copy()
        green_scale_array[:, :, 0] = 0
        green_scale_array[:, :, 2] = 0
        img = Image.fromarray(green_scale_array)
        img.show()
        return green_scale_array
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interupted, exiting...")


def ft_blue(array) -> np.array:
    '''
    Convert an image into blue scale.

    Parameters:
    array (np.array): A 3D numpy array representing an RGB image.

    Returns:
    np.array: The blue-scaled image array.
    '''
    try:
        if not isinstance(array, np.ndarray) or not array.ndim == 3:
            raise ValueError("Input must be a 3d numpy array")
        blue_scale_array = array.copy()
        blue_scale_array[:, :, 0] = 0
        blue_scale_array[:, :, 1] = 0
        img = Image.fromarray(blue_scale_array)
        img.show()
        return blue_scale_array
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interupted, exiting...")


def ft_grey(array) -> np.array:
    '''
    Convert an image into gray scale.

    Parameters:
    array (np.array): A 3D numpy array representing an RGB image.

    Returns:
    np.array: The gray-scaled image array.
    '''
    try:
        if not isinstance(array, np.ndarray) or not array.ndim == 3:
            raise ValueError("Input must be a 3d numpy array")
        # img = Image.fromarray(array)
        # img = img.convert("L")
        # grayscale_array = np.array(img)
        # NTSC formula: 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue
        grayscale_array = 0.299 * \
            array[:, :, 0] + 0.587 * array[:, :, 1] + 0.114 * array[:, :, 2]
        img = Image.fromarray(grayscale_array)
        img.show()
        return grayscale_array
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interupted, exiting...")
