from PIL import Image
import imagehash


def calculate_phash(file_path):
    try:
        with Image.open(file_path) as img:
            return imagehash.phash(img)

    except Exception:
        return None
    