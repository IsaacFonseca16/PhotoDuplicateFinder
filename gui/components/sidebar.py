from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QLabel, QPushButton, QProgressBar
)


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("panel")
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(14)

        title = QLabel("📸 Photo Duplicate Finder")
        title.setStyleSheet("font-size: 22px; font-weight: bold;")

        subtitle = QLabel("Detector de fotos y videos duplicados")
        subtitle.setStyleSheet("color: #94a3b8; font-size: 13px;")

        self.folder_label = QLabel("Ninguna carpeta seleccionada")
        self.folder_label.setWordWrap(True)
        self.folder_label.setStyleSheet("""
            color: #cbd5e1;
            background-color: #1e293b;
            border-radius: 8px;
            padding: 10px;
        """)

        self.select_button = QPushButton("Seleccionar carpeta")

        self.scan_button = QPushButton("Escanear")
        self.scan_button.setObjectName("secondary")

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.image_count = QLabel("📷 Imágenes: 0")
        self.video_count = QLabel("🎥 Videos: 0")
        self.group_count = QLabel("🧩 Grupos: 0")
        self.space_label = QLabel("💾 Recuperable: 0 MB")

        self.delete_button = QPushButton("Eliminar seleccionados")
        self.delete_button.setObjectName("danger")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(QLabel("Carpeta seleccionada"))
        layout.addWidget(self.folder_label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.scan_button)
        layout.addSpacing(20)
        layout.addWidget(QLabel("Progreso"))
        layout.addWidget(self.progress)
        layout.addSpacing(15)
        layout.addWidget(self.image_count)
        layout.addWidget(self.video_count)
        layout.addWidget(self.group_count)
        layout.addWidget(self.space_label)
        layout.addStretch()
        layout.addWidget(self.delete_button)