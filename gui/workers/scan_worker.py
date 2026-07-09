from PySide6.QtCore import QThread, Signal

from services.scanner import scan_folder
from services.similar_image_detector import find_similar_images
from services.video_duplicate_detector import find_duplicate_videos

class ScanWorker(QThread):
    finished = Signal(list, list)
    progress = Signal(int)
    error = Signal(str)

    def __init__(self, folder_path):
        super().__init__()
        self.folder_path = folder_path

    def run(self):
        try:
            self.progress.emit(10)

            files = scan_folder(self.folder_path)

            self.progress.emit(70)

            image_groups = find_similar_images(files, max_difference=5)
            video_groups_dict = find_duplicate_videos(files)

            video_groups = list(video_groups_dict.values())

            groups = image_groups + video_groups

            self.progress.emit(100)

            self.finished.emit(files, groups)

        except Exception as e:
            self.error.emit(str(e))