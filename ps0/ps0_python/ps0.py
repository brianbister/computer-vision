import argparse

import cv2
import numpy as np


BLUE = 0
GREEN = 1
RED = 2


def basic_input(images):
    """Copies images to an output folder.

    images: A list of strings containing the location of images.
    """
    for i, image_name in enumerate(images):
        img = cv2.imread(image_name)
        cv2.imwrite("output/ps0-1-a-{}.png".format(i + 1), img)


def color_planes(image):
    """Given an image, create 3 new images with the following:
    1) The red and blue pixels swapped.
    2) Green monochrome image.
    3) Red monochrome image.

    image: The location of the image.
    """
    img = cv2.imread(image)

    # Swap red and blue pixel values.
    swap_img = np.copy(img)
    red_pixels = np.copy(swap_img[:, :, RED])
    swap_img[:, :, RED] = swap_img[:, :, BLUE]
    swap_img[:, :, BLUE] = red_pixels
    cv2.imwrite("output/ps0-2-a-1.png", swap_img)

    # Green monochrome.
    green_img = np.copy(img)
    green_img[:, :, BLUE] = 0
    green_img[:, :, RED] = 0
    cv2.imwrite("output/ps0-2-b-1.png", green_img)

    # Red monochrome.
    red_img = np.copy(img)
    red_img[:, :, BLUE] = 0
    red_img[:, :, GREEN] = 0
    cv2.imwrite("output/ps0-2-c-1.png", red_img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run some basic computer "
                                                 "vision operations.")
    parser.add_argument("question_num", type=int, help="The question # to "
                        "run.")
    parser.add_argument("-img", "--images", action="store", dest="images",
                        help="The list of images to process.", nargs="+")
    args = parser.parse_args()
    if args.question_num == 0:
        basic_input(args.images)
    if args.question_num == 1:
        if len(args.images) != 1:
            raise ValueError("Requires only one image.")
        color_planes(args.images[0])
