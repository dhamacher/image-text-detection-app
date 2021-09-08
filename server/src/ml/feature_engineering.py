import numpy
import cv2


def remove_alpha_channel(img: numpy.ndarray):
    try:
        # # make mask of where the transparent bits are
        # trans_mask = img[:, :, 3] == 0
        #
        # # replace areas of transparency with white and not transparent
        # img[trans_mask] = [255, 255, 255, 255]

        # new image without alpha channel...
        im = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return im
    except Exception as e:
        print(str(e))
        return img


def bilateral_filter(img: numpy.ndarray):
    try:
        im = cv2.bilateralFilter(img, 5, 55, 60)
        return im
    except Exception as e:
        print(str(e))
        return img


def invert_image(img):
    """
    Use dark text on light background.
    Args:
        img:

    Returns:

    """
    try:
        pass
    except Exception as e:
        print(str(e))


def rescale_image(img):
    """
    Tesseract works best on images which have a DPI of at least 300 dpi, so it may be beneficial to resize images
    Args:
        img:

    Returns:

    """
    try:
        pass
    except Exception as e:
        print(str(e))


def apply_grayscale(img: numpy.ndarray):
    try:
        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return im
    except Exception as e:
        print(str(e))
        return img


def binarization(img: numpy.ndarray):
    try:
        _, im = cv2.threshold(img, 190, 255, 1)  # 2nd param affects outcome of text recognition
        return im
    except Exception as e:
        print(str(e))
        return img

