from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton, QProgressBar


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("panel")
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(14)

        section_folder = QLabel("📂 Carpeta")
        section_folder.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.folder_label = QLabel("Ninguna carpeta seleccionada")
        self.folder_label.setWordWrap(True)
        self.folder_label.setStyleSheet("""
            color: #cbd5e1;
            background-color: #1e293b;
            border-radius: 10px;
            padding: 10px;
        """)

        self.select_button = QPushButton("Seleccionar carpeta")

        self.scan_button = QPushButton("Escanear")
        self.scan_button.setObjectName("secondary")

        section_stats = QLabel("📊 Estadísticas")
        section_stats.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.image_count = QLabel("📷 Imágenes: 0")
        self.video_count = QLabel("🎥 Videos: 0")
        self.group_count = QLabel("🧩 Grupos: 0")
        self.space_label = QLabel("💾 Recuperable: 0 MB")

        section_progress = QLabel("Progreso")
        section_progress.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.status_label = QLabel("Estado: listo")
        self.status_label.setStyleSheet("color: #94a3b8; font-size: 12px;")

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.delete_button = QPushButton("Eliminar seleccionados")
        self.delete_button.setObjectName("danger")

        layout.addWidget(section_folder)
        layout.addWidget(self.folder_label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.scan_button)

        layout.addSpacing(20)
        layout.addWidget(section_stats)
        layout.addWidget(self.image_count)
        layout.addWidget(self.video_count)
        layout.addWidget(self.group_count)
        layout.addWidget(self.space_label)

        layout.addSpacing(20)
        layout.addWidget(section_progress)
        layout.addWidget(self.progress)
        layout.addWidget(self.status_label)

        layout.addStretch()
        layout.addWidget(self.delete_button)