import argparse

import cv2


def basic_input(images):
    """Copies images to an output folder.

    images: A list of strings containing the location of images.
    """
    for i, image_name in enumerate(images):
        image = cv2.imread(image_name)
        cv2.imwrite("output/ps0-1-a-{}.png".format(i + 1), image)


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
