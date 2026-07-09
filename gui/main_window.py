from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QFrame, QProgressBar, QScrollArea, QFileDialog
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Photo Duplicate Finder")
        self.resize(1100, 720)

        self.selected_folder = None

        self.setStyleSheet("""
            QMainWindow {
                background-color: #0f172a;
            }

            QLabel {
                color: #e5e7eb;
                font-family: Segoe UI;
            }

            QPushButton {
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 18px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }

            QPushButton#secondaryButton {
                background-color: #334155;
            }

            QPushButton#dangerButton {
                background-color: #dc2626;
            }

            QFrame#card {
                background-color: #111827;
                border: 1px solid #334155;
                border-radius: 14px;
            }

            QProgressBar {
                border: 1px solid #334155;
                border-radius: 8px;
                background-color: #1e293b;
                color: white;
                text-align: center;
                height: 18px;
            }

            QProgressBar::chunk {
                background-color: #22c55e;
                border-radius: 8px;
            }
        """)

        self.build_ui()

    def build_ui(self):
        main = QWidget()
        main_layout = QHBoxLayout(main)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(18)

        sidebar = self.create_sidebar()
        content = self.create_content()

        main_layout.addWidget(sidebar, 1)
        main_layout.addWidget(content, 4)

        self.setCentralWidget(main)

    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setObjectName("card")

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(16)

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
        self.select_button.clicked.connect(self.select_folder)

        self.scan_button = QPushButton("Escanear")
        self.scan_button.setObjectName("secondaryButton")

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.image_count = QLabel("📷 Imágenes: 0")
        self.video_count = QLabel("🎥 Videos: 0")
        self.group_count = QLabel("🧩 Grupos: 0")
        self.space_label = QLabel("💾 Recuperable: 0 MB")

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

        delete_button = QPushButton("Eliminar seleccionados")
        delete_button.setObjectName("dangerButton")
        layout.addWidget(delete_button)

        return sidebar

    def create_content(self):
        content = QFrame()
        content.setObjectName("card")

        layout = QVBoxLayout(content)
        layout.setContentsMargins(22, 22, 22, 22)
        layout.setSpacing(16)

        header = QLabel("Resultados")
        header.setStyleSheet("font-size: 26px; font-weight: bold;")

        description = QLabel("Aquí aparecerán los grupos de archivos duplicados o similares.")
        description.setStyleSheet("color: #94a3b8; font-size: 14px;")

        self.results_area = QScrollArea()
        self.results_area.setWidgetResizable(True)
        self.results_area.setStyleSheet("border: none;")

        self.results_container = QWidget()
        self.results_layout = QVBoxLayout(self.results_container)
        self.results_layout.setAlignment(Qt.AlignTop)

        empty_label = QLabel("No hay resultados todavía.\nSelecciona una carpeta y presiona Escanear.")
        empty_label.setAlignment(Qt.AlignCenter)
        empty_label.setStyleSheet("color: #64748b; font-size: 18px; padding: 120px;")

        self.results_layout.addWidget(empty_label)
        self.results_area.setWidget(self.results_container)

        layout.addWidget(header)
        layout.addWidget(description)
        layout.addWidget(self.results_area)

        return content

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta")

        if folder:
            self.selected_folder = folder
            self.folder_label.setText(folder)