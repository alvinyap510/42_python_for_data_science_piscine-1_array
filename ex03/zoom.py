from PIL import Image
import numpy as np
from load_image import ft_load


def main():
    img_array = ft_load("animal.jpeg")
    print(img_array)
    img_array = img_array[70:470]
    new_img_array = []
    for i in img_array:
        new_img_array.append(i[500:900])
    new_img_array = np.array(new_img_array, dtype=np.uint8)
    new_img = Image.fromarray(new_img_array)
    if (new_img.mode != "L"):
        new_img = new_img.convert("L")
    print(new_img)
    new_array = np.array(new_img)
    print(new_array)
    three_d_array = np.array([[[element] for element in row]
                             for row in new_array])
    print(three_d_array)

    new_img.save("processed_animal.jpeg")


if __name__ == "__main__":
    main()
