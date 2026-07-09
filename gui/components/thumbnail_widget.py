from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QCheckBox,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal


class ThumbnailWidget(QFrame):
    double_clicked = Signal(object)

    def __init__(self, file_info):
        super().__init__()

        self.file_info = file_info
        self.setObjectName("thumbnailWidget")
        self.setFixedWidth(210)

        self.setStyleSheet("""
            QFrame#thumbnailWidget {
                background-color: #0f172a;
                border: 1px solid #334155;
                border-radius: 16px;
            }

            QFrame#thumbnailWidget:hover {
                border: 1px solid #60a5fa;
                background-color: #111c33;
            }

            QLabel {
                color: #e5e7eb;
                font-family: Segoe UI;
            }

            QCheckBox {
                color: #e5e7eb;
                font-family: Segoe UI;
                font-size: 12px;
            }
        """)

        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        self.checkbox = QCheckBox("Marcar para eliminar")

        image_label = QLabel()
        image_label.setFixedSize(190, 135)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setStyleSheet("""
            background-color: #020617;
            border-radius: 12px;
            color: #64748b;
        """)

        pixmap = QPixmap(self.file_info.path)

        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                190,
                135,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            image_label.setPixmap(pixmap)
        else:
            image_label.setText("Sin vista")

        name = self.shorten_name(self.file_info.name)
        name_label = QLabel(name)
        name_label.setToolTip(self.file_info.name)
        name_label.setWordWrap(True)
        name_label.setStyleSheet("font-size: 13px; font-weight: bold;")

        details_label = QLabel(
            f"{self.file_info.width} × {self.file_info.height}\n"
            f"{self.file_info.size} MB"
        )
        details_label.setStyleSheet("color: #94a3b8; font-size: 12px;")

        layout.addWidget(self.checkbox)
        layout.addWidget(image_label)
        layout.addWidget(name_label)
        layout.addWidget(details_label)

    def shorten_name(self, name, max_length=26):
        if len(name) <= max_length:
            return name

        return name[:max_length - 3] + "..."

    def is_selected_for_delete(self):
        return self.checkbox.isChecked()

    def mouseDoubleClickEvent(self, event):
        self.double_clicked.emit(self.file_info)
        super().mouseDoubleClickEvent(event)