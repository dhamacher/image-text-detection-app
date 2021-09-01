from .feature_engineering import binarization, apply_grayscale
from ..utils.files import save_image, save_text_to_file
import numpy
from werkzeug.datastructures import FileStorage
import pytesseract
from PIL import Image
import numpy as np
import os
from pathlib import Path
import logging

ENV = os.getenv('APP_ENV')

from ..config.config import get_config

_image_path = Path(get_config(ENV)['image_path'])
_logger = logging.getLogger(__name__)


def _logging_setup():
    try:
        log_path = Path(get_config(ENV)['log_path'])
        filename = 'logs.txt'
        dest = log_path / filename
        _logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.FileHandler(dest, mode='a', encoding=None, delay=False)
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to _logger
        _logger.addHandler(ch)
        return _logger
    except Exception as e:
        print(str(e))
        raise(e)


def _get_features(image_array: numpy.ndarray):
    try:
        # TODO: Study other image feature engineering techniques to improve performance.
        # featured_image_array1 = bilateral_filter(image_array)
        featured_image_array2 = apply_grayscale(image_array)
        featured_image_array3 = binarization(featured_image_array2)

        final_image_array = featured_image_array3
        return final_image_array
    except Exception as e:
        print(str(e))


def get_text_from_image(image_file: FileStorage):
    log = None
    try:
        log = _logging_setup()
        tess_exec = Path(get_config(ENV)['tesseract_cmd'])
        pytesseract.pytesseract.tesseract_cmd = tess_exec

        image_path = save_image(image_file)
        image_file = Image.open(image_path)
        image_array = np.array(image_file)
        processed_image_array = _get_features(image_array)

        custom_config = get_config(ENV)['tesseract_config']
        output = pytesseract.image_to_string(processed_image_array, config=custom_config)
        output_path = Path(get_config(ENV)['text_output_path'])
        text_file_path = save_text_to_file(output_path, output)

        return output
    except Exception as e:
        log.exception(f'{str(e)}')

