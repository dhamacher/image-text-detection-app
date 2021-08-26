from werkzeug.datastructures import FileStorage
from pathlib import Path
import server.src.config.config as cfg


def save_image(file: FileStorage) -> Path:
    """
    Saves an image file to disk.
    Args:
        file: The image file to write to disk

    Returns:
        None

    """
    try:
        path = Path(cfg.get_config('DEV')['image_path'])
        filename = str(file.filename)
        dest = path / filename
        file.save(dest)
        return dest
    except Exception as e:
        print(str(e))


def save_text_to_file(path: Path, content: str, filename = "output.txt") -> Path:
    try:
        dest = path / filename
        with open(dest, 'w') as f:
            f.write(content)
    except Exception as e:
        print(str(e))

