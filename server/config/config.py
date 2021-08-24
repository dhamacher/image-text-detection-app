def get_config(environment = 'dev'):
    configuration = {
        'dev': {
            'image_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\uploaded_images',
            'log_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\logs',
            'tesseract_config': "--oem 3 --psm 1 -c tessedit_char_whitelist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.$/ '",
            'text_output_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\output',
            'test_image_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\data\\alt text.jpg'
        }
    }
    return configuration[environment]