def get_config(environment = 'DEV'):
    """
    Get configuration values for the application based on the environment parameter.
    Args:
        environment: The environment to get configurations for.

    Returns:
        dict - Dictionary with key value pairs required to run the application.
    """
    try:
        # TODO: Make the paths work across paltforms
        if environment == 'DEV':
            import os
            from pathlib import Path

            tesseract_home = Path(str(os.getenv("TESSERACT_HOME")))
            tesseract_cmd_path = tesseract_home / 'tesseract.exe'
            tesseract_cmd = str(tesseract_cmd_path)

            return {
                'image_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\server\\uploaded_images',
                'feature_image_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\server\\feature_images',
                'log_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\server\\logs',
                'tesseract_cmd': f'{tesseract_cmd}',
                'tesseract_config': "--oem 3 --psm 1 -c tessedit_char_whitelist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.$/ '",
                'text_output_path': 'C:\\Users\\dhama\\Projects\\image-text-detection-app\\server\\output'
            }
        if environment == 'DOCKER-DEV':
            return {
                'image_path': '/server/uploaded_images',
                'feature_image_path': '/server/feature_images',
                'log_path': '/server/logs',
                'tesseract_cmd': 'tesseract',
                'tesseract_config': "--oem 3 --psm 1 -c tessedit_char_whitelist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.$/ '",
                'text_output_path': '/server/output'
            }
        else:
            return None
    except Exception as e:
        print(str(e))
        raise e