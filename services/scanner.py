from pathlib import Path
from PIL import Image

from services.hashing import calculate_sha256
from models.file_info import FileInfo
from services.image_hashing import calculate_phash

VALID_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
    ".heic",
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
}


def get_file_type(extension):
    image_extensions = {
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".webp",
        ".heic",
    }

    video_extensions = {
        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
    }

    if extension in image_extensions:
        return "Imagen"

    if extension in video_extensions:
        return "Video"

    return "Desconocido"


def get_image_dimensions(file_path):
    try:
        with Image.open(file_path) as img:
            return img.width, img.height
    except Exception:
        return None, None


def scan_folder(folder_path):
    folder = Path(folder_path)
    files = []

    for file in folder.rglob("*"):
        if file.is_file() and file.suffix.lower() in VALID_EXTENSIONS:
            file_size = file.stat().st_size
            file_type = get_file_type(file.suffix.lower())

            width = None
            height = None
            phash = None

            if file_type == "Imagen":
                width, height = get_image_dimensions(file)
            phash = calculate_phash(file)

            files.append(
                FileInfo(
                    name=file.name,
                    path=str(file),
                    size=round(file_size / (1024 * 1024), 2),
                    file_type=file_type,
                    sha256=calculate_sha256(file),
                    width=width,
                    height=height,
                    phash=phash,
                )
            )

    return files