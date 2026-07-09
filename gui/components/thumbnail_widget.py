import cv2

from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QCheckBox, QHBoxLayout
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, Signal


class ThumbnailWidget(QFrame):
    double_clicked = Signal(object)
    selection_changed = Signal()

    def __init__(self, file_info):
        super().__init__()

        self.file_info = file_info
        self.is_recommended = False

        self.setObjectName("thumbnailWidget")
        self.setFixedWidth(210)

        self.apply_default_style()
        self.build_ui()

    def apply_default_style(self):
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

            QLabel#badge {
                border-radius: 10px;
                padding: 4px 8px;
                font-size: 11px;
                font-weight: bold;
            }
        """)

    def apply_recommended_style(self):
        self.setStyleSheet("""
            QFrame#thumbnailWidget {
                background-color: #0f172a;
                border: 2px solid #22c55e;
                border-radius: 16px;
            }

            QFrame#thumbnailWidget:hover {
                border: 2px solid #86efac;
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

            QLabel#badge {
                border-radius: 10px;
                padding: 4px 8px;
                font-size: 11px;
                font-weight: bold;
            }
        """)

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        top_row = QHBoxLayout()

        self.badge = QLabel(
            "🎥 Video" if self.file_info.file_type == "Video" else "🖼️ Imagen"
        )
        self.badge.setObjectName("badge")

        if self.file_info.file_type == "Video":
            self.badge.setStyleSheet("background-color: #7c2d12; color: #fed7aa;")
        else:
            self.badge.setStyleSheet("background-color: #1e3a8a; color: #bfdbfe;")

        self.checkbox = QCheckBox()
        self.checkbox.stateChanged.connect(lambda _: self.selection_changed.emit())

        top_row.addWidget(self.badge)
        top_row.addStretch()
        top_row.addWidget(self.checkbox)

        image_label = QLabel()
        image_label.setFixedSize(190, 135)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setStyleSheet("""
            background-color: #020617;
            border-radius: 12px;
            color: #64748b;
        """)

        if self.file_info.file_type == "Video":
            pixmap = self.get_video_thumbnail()
        else:
            pixmap = QPixmap(self.file_info.path)

        if pixmap and not pixmap.isNull():
            pixmap = pixmap.scaled(
                190,
                135,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            image_label.setPixmap(pixmap)
        else:
            image_label.setText("Sin vista")

        name_label = QLabel(self.shorten_name(self.file_info.name))
        name_label.setToolTip(self.file_info.name)
        name_label.setWordWrap(True)
        name_label.setStyleSheet("font-size: 13px; font-weight: bold;")

        details_text = (
            f"{self.file_info.width} × {self.file_info.height}\n"
            f"💾 {self.file_info.size} MB"
        )

        if self.file_info.file_type == "Video" and self.file_info.duration:
            minutes = int(self.file_info.duration // 60)
            seconds = int(self.file_info.duration % 60)
            details_text += f"\n⏱ {minutes:02d}:{seconds:02d}"

        if self.file_info.file_type == "Video" and self.file_info.fps:
            details_text += f"\n🎬 {round(self.file_info.fps, 1)} FPS"

        details_label = QLabel(details_text)
        details_label.setStyleSheet("color: #94a3b8; font-size: 12px;")

        self.recommended_label = QLabel("")
        self.recommended_label.setStyleSheet(
            "color: #86efac; font-size: 12px; font-weight: bold;"
        )

        layout.addLayout(top_row)
        layout.addWidget(image_label)
        layout.addWidget(name_label)
        layout.addWidget(details_label)
        layout.addWidget(self.recommended_label)

    def get_video_thumbnail(self):
        video = cv2.VideoCapture(self.file_info.path)

        if not video.isOpened():
            return None

        success, frame = video.read()
        video.release()

        if not success:
            return None

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        height, width, channels = frame.shape
        bytes_per_line = channels * width

        image = QImage(
            frame.data,
            width,
            height,
            bytes_per_line,
            QImage.Format_RGB888,
        )

        return QPixmap.fromImage(image)

    def shorten_name(self, name, max_length=26):
        if len(name) <= max_length:
            return name

        return name[:max_length - 3] + "..."

    def is_selected_for_delete(self):
        return self.checkbox.isChecked()

    def set_checked_for_delete(self, checked):
        self.checkbox.setChecked(checked)

    def set_recommended(self, recommended):
        self.is_recommended = recommended

        if recommended:
            self.apply_recommended_style()
            self.recommended_label.setText("⭐ Recomendado conservar")
            self.checkbox.setChecked(False)
        else:
            self.apply_default_style()
            self.recommended_label.setText("")

    def mouseDoubleClickEvent(self, event):
        self.double_clicked.emit(self.file_info)
        super().mouseDoubleClickEvent(event)