from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ImagePreviewDialog(QDialog):
    def __init__(self, file_info):
        super().__init__()

        self.file_info = file_info

        self.setWindowTitle(file_info.name)
        self.resize(900, 650)

        self.setStyleSheet("""
            QDialog {
                background-color: #0f172a;
            }

            QLabel {
                color: #e5e7eb;
                font-family: Segoe UI;
            }

            QPushButton {
                background-color: #334155;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }
        """)

        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(self.file_info.path)

        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                820,
                480,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            image_label.setPixmap(pixmap)
        else:
            image_label.setText("No se pudo cargar la imagen")

        info_label = QLabel(
            f"{self.file_info.name}\n"
            f"{self.file_info.width}x{self.file_info.height} | "
            f"{self.file_info.size} MB"
        )
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setStyleSheet("font-size: 14px; color: #cbd5e1;")

        close_button = QPushButton("Cerrar")
        close_button.clicked.connect(self.close)

        layout.addWidget(image_label)
        layout.addWidget(info_label)
        layout.addWidget(close_button)