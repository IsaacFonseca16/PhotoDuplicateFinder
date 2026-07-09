from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel
)

from gui.components.thumbnail_widget import ThumbnailWidget


class DuplicateCard(QFrame):
    def __init__(self, group_number, files):
        super().__init__()

        self.group_number = group_number
        self.files = files
        self.thumbnails = []

        self.setObjectName("duplicateCard")

        self.setStyleSheet("""
            QFrame#duplicateCard {
                background-color: #1e293b;
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
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(10)

        title = QLabel(f"Grupo #{self.group_number}")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        thumbnails_row = QHBoxLayout()
        thumbnails_row.setSpacing(12)

        for file in self.files:
            thumbnail = ThumbnailWidget(file)
            self.thumbnails.append(thumbnail)
            thumbnails_row.addWidget(thumbnail)

        thumbnails_row.addStretch()
        layout.addLayout(thumbnails_row)

    def get_selected_files(self):
        selected = []

        for thumbnail in self.thumbnails:
            if thumbnail.is_selected_for_delete():
                selected.append(thumbnail.file_info)

        return selected