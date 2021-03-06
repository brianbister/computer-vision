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


def arithmetic_and_geometric_ops(image, color):
    """Prints the min, max, mean, and standard deviation
    of the image.

    image: The location of the image.
    """

    # Get an array of just the color specfied.
    img = cv2.imread(image)
    mono_pixels = img[:, :, color]

    minimum = np.amin(mono_pixels)
    maximum = np.amax(mono_pixels)
    mean = np.mean(mono_pixels)
    std_dev = np.std(mono_pixels)
    print("Min: {}\n"
          "Max: {}\n"
          "Mean: {}\n"
          "Standard Deviation: {}".format(minimum, maximum, mean, std_dev))

    # Do some basic operations.
    mono_img = _create_monochrome_image(img, color)
    mono_img[:, :, color] = mono_img[:, :, color] - mean
    mono_img[:, :, color] = mono_img[:, :, color] / std_dev
    mono_img[:, :, color] = mono_img[:, :, color] * 10
    mono_img[:, :, color] = mono_img[:, :, color] + mean
    cv2.imwrite("output/ps0-4-b-1.png", mono_img)

    # Shift by 2 pixels.
    mono_img = _create_monochrome_image(img, color)
    shifted_mono_img = mono_img[:, 2:, :]
    cv2.imwrite("output/ps0-4-c-1.png", shifted_mono_img)

    # Subtract shifted image from original
    diff_img = mono_img[:, :-2, :] - shifted_mono_img
    diff_img = diff_img.clip(min=0)
    cv2.imwrite("output/ps0-4-d-1.png", diff_img[:, :, color])


def add_noise(image):
    """Add noise to an image.

    image: The location of the image.
    """
    img = cv2.imread(image)
    height, width, _ = img.shape
    sigma = 8

    noise = np.random.randn(height, width) * sigma
    img[:, :, GREEN] = img[:, :, GREEN] + noise
    cv2.imwrite("output/ps0-5-a-1.png", img)

    img = cv2.imread(image)
    img[:, :, BLUE] = img[:, :, BLUE] + noise
    cv2.imwrite("output/ps0-5-b-1.png", img)


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
        arithmetic_and_geometric_ops(args.images[0], GREEN)
    if args.question_num == 5:
        if len(args.images) != 1:
            raise ValueError("Requires only one image.")
        add_noise(args.images[0])
