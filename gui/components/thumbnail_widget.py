from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QLabel, QCheckBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ThumbnailWidget(QFrame):
    def __init__(self, file_info):
        super().__init__()

        self.file_info = file_info

        self.setObjectName("thumbnailWidget")
        self.setFixedWidth(170)

        self.setStyleSheet("""
            QFrame#thumbnailWidget {
                background-color: #0f172a;
                border: 1px solid #334155;
                border-radius: 12px;
            }

            QLabel {
                color: #e5e7eb;
                font-family: Segoe UI;
            }

            QCheckBox {
                color: #e5e7eb;
                font-family: Segoe UI;
            }
        """)

        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        image_label = QLabel()
        image_label.setFixedSize(150, 110)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setStyleSheet("""
            background-color: #020617;
            border-radius: 8px;
            color: #64748b;
        """)

        pixmap = QPixmap(self.file_info.path)

        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                150,
                110,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            image_label.setPixmap(pixmap)
        else:
            image_label.setText("Sin vista")

        name_label = QLabel(self.file_info.name)
        name_label.setWordWrap(True)
        name_label.setStyleSheet("font-size: 12px; font-weight: bold;")

        details_label = QLabel(
            f"{self.file_info.width}x{self.file_info.height}\n"
            f"{self.file_info.size} MB"
        )
        details_label.setStyleSheet("color: #94a3b8; font-size: 11px;")

        self.checkbox = QCheckBox("Eliminar")

        layout.addWidget(image_label)
        layout.addWidget(name_label)
        layout.addWidget(details_label)
        layout.addWidget(self.checkbox)
        
    def is_selected_for_delete(self):
        return self.checkbox.isChecked()