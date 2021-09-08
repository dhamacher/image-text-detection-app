from ..config.config import get_config
from werkzeug.datastructures import FileStorage
from pathlib import Path

import os

ENV = os.getenv('APP_ENV')

def save_image(image_file: FileStorage) -> Path:
    """
    Saves an image file to disk.
    Args:
        file: The image file to write to disk

    Returns:
        None

    """
    try:
        path = Path(get_config(ENV)['image_path'])
        filename = str(image_file.filename)
        dest = path / filename
        image_file.save(dest)
        return dest
    except Exception as e:
        print(str(e))
        raise(e)


def save_text_to_file(path: Path, content: str) -> Path:
    try:
        with open(path, 'w') as f:
            f.write(content)
    except Exception as e:
        raise(e)
