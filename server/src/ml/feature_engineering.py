import numpy
import cv2

def bilateral_filter(img: numpy.ndarray):
    try:
        im = cv2.bilateralFilter(img, 5, 55, 60)
        return im
    except Exception as e:
        print(str(e))
        return img


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

