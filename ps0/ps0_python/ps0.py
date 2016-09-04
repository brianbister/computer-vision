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


def _create_monochrome_image(image, color):
    """Given an image and color, create the monochrome version of it.

    image: The location of the image.
    color: The color to create a monochrome version of.
    """
    mono_img = np.copy(image)
    mono_img[:, :, (color + 1) % 3] = 0
    mono_img[:, :, (color + 2) % 3] = 0
    return mono_img


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
    green_img = _create_monochrome_image(img, GREEN)
    cv2.imwrite("output/ps0-2-b-1.png", green_img)

    # Red monochrome.
    red_img = _create_monochrome_image(img, RED)
    cv2.imwrite("output/ps0-2-c-1.png", red_img)


def replace_pixels(image_1, image_2, color):
    """Creates a monochrome version of both images then places the 100x100
    center of image_1 into the center of image_2

    image_1: The location of image_1
    image_2: The locatino of image_2
    color: The color to create the monochrome version.
    """
    img_1 = cv2.imread(image_1)
    img_2 = cv2.imread(image_2)
    mono_1 = _create_monochrome_image(img_1, color)
    mono_2 = _create_monochrome_image(img_2, color)

    # Get center of green_1
    height_1, width_1, _ = mono_1.shape
    print height_1, width_1
    center_1 = mono_1[height_1 / 2 - 50:height_1 / 2 + 50,
                      width_1 / 2 - 50:width_1 / 2 + 50]

    # Replace center of green_2
    height_2, width_2, _ = mono_2.shape
    mono_2[height_2 / 2 - 50:height_2 / 2 + 50,
           width_2 / 2 - 50:width_2 / 2 + 50] = center_1
    cv2.imwrite("output/ps0-3-a-1.png", mono_2)


def arithmetic_and_geometric_ops(image):
    """Prints the min, max, mean, and standard deviation
    of the image.

    image: The location of the image.
    """

    # Get an array of just the green pixels.
    img = cv2.imread(image)
    green_pixels = img[:, :, GREEN]

    minimum = np.amin(green_pixels)
    maximum = np.amax(green_pixels)
    mean = np.mean(green_pixels)
    std_dev = np.std(green_pixels)
    print("Min: {}\n"
          "Max: {}\n"
          "Mean: {}\n"
          "Standard Deviation: {}".format(minimum, maximum, mean, std_dev))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run some basic computer "
                                                 "vision operations.")
    parser.add_argument("question_num", type=int, help="The question # to "
                        "run.")
    parser.add_argument("-img", "--images", action="store", dest="images",
                        help="The list of images to process.", nargs="+")
    args = parser.parse_args()
    if args.question_num == 1:
        basic_input(args.images)
    if args.question_num == 2:
        if len(args.images) != 1:
            raise ValueError("Requires only one image.")
        color_planes(args.images[0])
    if args.question_num == 3:
        if len(args.images) != 2:
            raise ValueError("Requires two images.")
        replace_pixels(args.images[0], args.images[1], GREEN)
    if args.question_num == 4:
        if len(args.images) != 1:
            raise ValueError("Requires only one image.")
        arithmetic_and_geometric_ops(args.images[0])
