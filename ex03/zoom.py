import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)

        start_height = 70
        end_height = 470
        start_column = 450
        end_column = 850

        # new_img_array = img_array[70:470, 500:900, 2]
        # # new_img = Image.fromarray(new_img_array)
        # # new_img.save("processed_animal.jpeg")
        # plt.imshow(new_img_array, cmap="gray")
        # plt.show()

        new_img_array = img_array[70:470, 500:900, :]
        new_img = Image.fromarray(new_img_array)
        if (new_img.mode != "L"):
            new_img = new_img.convert("L")
        new_img.save("processed_animal.jpeg")
        plt.imshow(new_img)
        plt.show()






    # img_array = img_array[70:470]
    # new_img_array = []
    # for i in img_array:
    #     new_img_array.append(i[500:900])
    # new_img_array = np.array(new_img_array, dtype=np.uint8)
    # new_img = Image.fromarray(new_img_array)
    # if (new_img.mode != "L"):
    #     new_img = new_img.convert("L")
    # print(new_img)
    # new_array = np.array(new_img)
    # print(new_array)
    # three_d_array = np.array([[[element] for element in row]
    #                          for row in new_array])
    # print(three_d_array)

    # new_img.save("processed_animal.jpeg")
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("K thanks bye")


if __name__ == "__main__":
    main()
