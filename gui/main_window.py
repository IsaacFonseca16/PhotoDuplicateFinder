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
from gui.components.toolbar import Toolbar
from gui.components.duplicate_card import DuplicateCard
from gui.workers.scan_worker import ScanWorker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Photo Duplicate Finder")
        self.resize(1200, 760)

        self.selected_folder = None
        self.duplicate_cards = []
        self.worker = None

        self.setStyleSheet(APP_STYLE)
        self.build_ui()

    def build_ui(self):
        main = QWidget()
        root_layout = QVBoxLayout(main)
        root_layout.setContentsMargins(18, 18, 18, 18)
        root_layout.setSpacing(16)

        self.toolbar = Toolbar()

        body_layout = QHBoxLayout()
        body_layout.setSpacing(16)

        self.sidebar = Sidebar()
        content = self.create_content()

        self.sidebar.select_button.clicked.connect(self.select_folder)
        self.sidebar.scan_button.clicked.connect(self.scan_folder)
        self.sidebar.delete_button.clicked.connect(self.delete_selected)

        body_layout.addWidget(self.sidebar, 1)
        body_layout.addWidget(content, 4)

        root_layout.addWidget(self.toolbar)
        root_layout.addLayout(body_layout)

        self.setCentralWidget(main)

    def create_content(self):
        content = QFrame()
        content.setObjectName("panel")

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
        self.results_layout.setSpacing(16)

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

        self.sidebar.scan_button.setEnabled(False)
        self.sidebar.scan_button.setText("Escaneando...")
        self.sidebar.progress.setValue(0)

        self.clear_results()

        self.worker = ScanWorker(self.selected_folder)
        self.worker.progress.connect(self.sidebar.progress.setValue)
        self.worker.finished.connect(self.on_scan_finished)
        self.worker.error.connect(self.on_scan_error)
        self.worker.start()

    def on_scan_finished(self, files, groups):
        image_count = len([f for f in files if f.file_type == "Imagen"])
        video_count = len([f for f in files if f.file_type == "Video"])

        self.sidebar.image_count.setText(f"📷 Imágenes: {image_count}")
        self.sidebar.video_count.setText(f"🎥 Videos: {video_count}")
        self.sidebar.group_count.setText(f"🧩 Grupos: {len(groups)}")
        self.sidebar.progress.setValue(100)

        self.sidebar.scan_button.setEnabled(True)
        self.sidebar.scan_button.setText("Escanear")

        if not groups:
            self.results_layout.addWidget(self.empty_label)
            return

        for index, group in enumerate(groups, start=1):
            card = DuplicateCard(index, group)
            self.duplicate_cards.append(card)
            self.results_layout.addWidget(card)

    def on_scan_error(self, message):
        self.sidebar.scan_button.setEnabled(True)
        self.sidebar.scan_button.setText("Escanear")
        self.sidebar.progress.setValue(0)

        print("Error durante el escaneo:", message)

    def clear_results(self):
        while self.results_layout.count():
            item = self.results_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.setParent(None)

        self.duplicate_cards.clear()

    def delete_selected(self):
        selected_files = []

        for card in self.duplicate_cards:
            selected_files.extend(card.get_selected_files())

        print("\nArchivos seleccionados:\n")

        for file in selected_files:
            print(file.path)