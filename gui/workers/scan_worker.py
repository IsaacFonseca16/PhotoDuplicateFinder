from PySide6.QtCore import QThread, Signal

from services.scanner import scan_folder
from services.similar_image_detector import find_similar_images


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

            groups = find_similar_images(files, max_difference=5)

            self.progress.emit(100)

            self.finished.emit(files, groups)

        except Exception as e:
            self.error.emit(str(e))