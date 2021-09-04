from .feature_engineering import binarization, apply_grayscale, bilateral_filter, remove_alpha_channel
from ..utils.files import save_image, save_text_to_file
from ..config.config import get_config

from werkzeug.datastructures import FileStorage
from PIL import Image
from pathlib import Path

import pytesseract
import numpy as np
import os
import matplotlib.pyplot as plt

ENV = os.getenv('APP_ENV')

def _get_image_array(image_file: FileStorage) -> np.ndarray:
    try:
        image_path = save_image(image_file)
        image_file = Image.open(image_path)
        image_array = np.array(image_file)
        return image_array
    except Exception as e:
        raise(e)


def _save_feature_image(img_array: np.ndarray, path: Path):
    try:
        plt.figure(figsize=(10, 10))
        plt.imshow(img_array)
        plt.xticks([])
        plt.yticks([])
        plt.savefig(path, bbox_inches='tight')
    except Exception as e:
        raise(e)


def _get_features(image_file: FileStorage) -> np.ndarray:
    try:
        output_path = Path(get_config(ENV)['feature_image_path'])
        image_array = _get_image_array(image_file)
        # TODO: Study other image feature engineering techniques to improve performance.

        featured_image_array1 = bilateral_filter(image_array)
        feature_filename = f'bilateral_filter_{Path(image_file.filename).name}'
        _save_feature_image(featured_image_array1, output_path / feature_filename)

        featured_image_array2 = apply_grayscale(featured_image_array1)
        feature_filename = f'grayscale_{Path(image_file.filename).name}'
        _save_feature_image(featured_image_array2, output_path / feature_filename)

        featured_image_array3 = binarization(featured_image_array2)
        feature_filename = f'binarization_{Path(image_file.filename).name}'
        _save_feature_image(featured_image_array3, output_path / feature_filename)

        final_image_array = featured_image_array3
        return final_image_array
    except Exception as e:
        print(str(e))
        raise(e)


def _valid_output(value: str) -> bool:
    try:
        if value == ' \n\f':
            return False
        else:
            return True
    except Exception as e:
        raise(e)


def _image_preprocessing(image_file: FileStorage):
    try:
        output_path = Path(get_config(ENV)['feature_image_path'])
        feature_filename = f'alpha_channel_removed_{Path(image_file.filename).name}'
        img = _get_image_array(image_file)
        if Path(image_file.filename).suffix == '.png':
            im = remove_alpha_channel(img)
            _save_feature_image(im, output_path / feature_filename)
            mod_image_file = FileStorage(output_path / feature_filename)
            return mod_image_file
        return image_file
    except Exception as e:
        print(str(e))


def get_text_from_image(image_file: FileStorage):
    try:
        config = get_config(ENV)
        output_filename = f'{Path(image_file.filename).stem}.txt'
        output_path = Path(config['text_output_path'])
        full_path = output_path / output_filename
        tess_exec = Path(config['tesseract_cmd'])
        pytesseract.pytesseract.tesseract_cmd = tess_exec
        custom_config = config['tesseract_config']

        mod_image_file = _image_preprocessing(image_file)
        feature_image_array = _get_features(mod_image_file)

        output = pytesseract.image_to_string(feature_image_array, config=custom_config)
        if not _valid_output(output):
            output = '=== NO TEXT DETECTED ==='

        text_file_path = save_text_to_file(full_path, output)

        return output
    except Exception as e:
        raise(e)
