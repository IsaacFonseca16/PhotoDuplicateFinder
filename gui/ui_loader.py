from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


def load_ui(ui_path):
    ui_file = QFile(ui_path)
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)

    ui_file.close()
    return window
