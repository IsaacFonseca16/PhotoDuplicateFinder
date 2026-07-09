from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Signal

from services.recommendation_service import get_recommended_file
from gui.components.thumbnail_widget import ThumbnailWidget
from gui.dialogs.image_preview_dialog import ImagePreviewDialog


class DuplicateCard(QFrame):
    selection_changed = Signal()

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
                border-radius: 16px;
            }

            QLabel {
                color: #e5e7eb;
                font-family: Segoe UI;
            }
        """)

        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(14)

        header = QHBoxLayout()

        title = QLabel(f"Grupo #{self.group_number}")
        title.setStyleSheet("font-size: 19px; font-weight: bold;")

        similarity = QLabel("Similitud alta")
        similarity.setStyleSheet("""
            color: #86efac;
            background-color: #14532d;
            border-radius: 10px;
            padding: 5px 10px;
            font-size: 12px;
            font-weight: bold;
        """)

        header.addWidget(title)
        header.addStretch()
        header.addWidget(similarity)

        layout.addLayout(header)

        thumbnails_row = QHBoxLayout()
        thumbnails_row.setSpacing(14)

        recommended_file = get_recommended_file(self.files)

        for file in self.files:
            thumbnail = ThumbnailWidget(file)
            thumbnail.double_clicked.connect(self.open_preview)
            thumbnail.selection_changed.connect(self.selection_changed)

            if recommended_file and file.path == recommended_file.path:
                thumbnail.set_recommended(True)
            else:
                thumbnail.set_checked_for_delete(True)

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

    def open_preview(self, file_info):
        dialog = ImagePreviewDialog(file_info)
        dialog.exec()

    def matches_search(self, text):
        text = text.lower().strip()

        if not text:
            return True

        for file in self.files:
            if text in file.name.lower():
                return True

        return False