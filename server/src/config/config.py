def get_config(environment = 'DEV'):
    # TODO: Make the paths work across paltforms
    if environment == 'DEV':
        import os
        from pathlib import Path

        tesseract_home = Path(str(os.getenv("TESSERACT_HOME")))
        tesseract_cmd_path = tesseract_home / 'tesseract.exe'
        tesseract_cmd = str(tesseract_cmd_path)

        return {
            'image_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\server\\uploaded_images',
            'log_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\server\\logs',
            'tesseract_cmd': f'{tesseract_cmd}',
            'tesseract_config': "--oem 3 --psm 1 -c tessedit_char_whitelist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.$/ '",
            'text_output_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\server\\output',
            'test_image_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\data\\alt text.jpg'
        }
    if environment == 'DOCKER-DEV':
        return {
            'image_path': './server/uploaded_images',
            'log_path': './server/logs',
            'tesseract_cmd': 'tesseract',
            'tesseract_config': "--oem 3 --psm 1 -c tessedit_char_whitelist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.$/ '",
            'text_output_path': './server/output',
            'test_image_path': './server/data/alt text.jpg'
        }
    else:
        return None