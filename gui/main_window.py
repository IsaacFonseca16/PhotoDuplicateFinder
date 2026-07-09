from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QScrollArea,
    QFileDialog,
)
from PySide6.QtCore import Qt

from gui.styles import APP_STYLE
from gui.components.sidebar import Sidebar
from gui.components.duplicate_card import DuplicateCard

from services.scanner import scan_folder
from services.similar_image_detector import find_similar_images


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Photo Duplicate Finder")
        self.resize(1100, 720)

        self.selected_folder = None
        self.setStyleSheet(APP_STYLE)

        self.build_ui()

    def build_ui(self):
        main = QWidget()
        main_layout = QHBoxLayout(main)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(18)

        self.sidebar = Sidebar()
        content = self.create_content()

        self.sidebar.select_button.clicked.connect(self.select_folder)
        self.sidebar.scan_button.clicked.connect(self.scan_folder)

        main_layout.addWidget(self.sidebar, 1)
        main_layout.addWidget(content, 4)

        self.setCentralWidget(main)

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

        self.empty_label = QLabel(
            "No hay resultados todavía.\nSelecciona una carpeta y presiona Escanear."
        )
        self.empty_label.setAlignment(Qt.AlignCenter)
        self.empty_label.setStyleSheet(
            "color: #64748b; font-size: 18px; padding: 120px;"
        )

        self.results_layout.addWidget(self.empty_label)
        self.results_area.setWidget(self.results_container)

        layout.addWidget(header)
        layout.addWidget(description)
        layout.addWidget(self.results_area)

        return content

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta")

        if folder:
            self.selected_folder = folder
            self.sidebar.folder_label.setText(folder)

    def scan_folder(self):
        if not self.selected_folder:
            return

        files = scan_folder(self.selected_folder)
        groups = find_similar_images(files, max_difference=5)

        self.clear_results()

        image_count = len([f for f in files if f.file_type == "Imagen"])
        video_count = len([f for f in files if f.file_type == "Video"])

        self.sidebar.image_count.setText(f"📷 Imágenes: {image_count}")
        self.sidebar.video_count.setText(f"🎥 Videos: {video_count}")
        self.sidebar.group_count.setText(f"🧩 Grupos: {len(groups)}")
        self.sidebar.progress.setValue(100)

        if not groups:
            self.results_layout.addWidget(self.empty_label)
            return

        for index, group in enumerate(groups, start=1):
            card = DuplicateCard(index, group)
            self.results_layout.addWidget(card)

    def clear_results(self):
        while self.results_layout.count():
            item = self.results_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.setParent(None)