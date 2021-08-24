import numpy
import matplotlib.pyplot as plt
import cv2
import logging

logger = logging.getLogger(__name__)

def bilateral_filter(img: numpy.ndarray):
    try:
        im = cv2.bilateralFilter(img, 5, 55, 60)
        # plt.figure(figsize=(10, 10))
        # plt.title('BILATERAL FILTER')
        # plt.imshow(im)
        # plt.xticks([])
        # plt.yticks([])
        # plt.savefig('..\\images\\02_filtered_img.png', bbox_inches='tight')
        return im
    except Exception as e:
        logger.exception(str(e))
    return None


def apply_grayscale(img: numpy.ndarray):
    im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # plt.figure(figsize=(10,10))
    # plt.title('GRAYSCALE IMAGE')
    # plt.imshow(im, cmap='gray'); plt.xticks([]); plt.yticks([])
    # plt.savefig('..\\images\\03_grayscale_img.png', bbox_inches='tight')
    return im


def binarization(img: numpy.ndarray):
    _, im = cv2.threshold(img, 190, 255, 1)  # 2nd param affects outcome of text recognition
    # plt.figure(figsize=(10, 10))
    # plt.title('IMMAGINE BINARIA')
    # plt.imshow(im, cmap='gray')
    # plt.xticks([])
    # plt.yticks([])
    # plt.savefig('..\\images\\04_binarization_img.png', bbox_inches='tight')
    return im


