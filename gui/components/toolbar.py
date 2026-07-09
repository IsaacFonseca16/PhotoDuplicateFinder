from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton


class Toolbar(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("toolbar")
        self.build_ui()

    def build_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(18, 12, 18, 12)
        layout.setSpacing(12)

        title = QLabel("📸 Photo Duplicate Finder")
        title.setStyleSheet("font-size: 22px; font-weight: bold;")

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar archivo...")
        self.search_input.setFixedWidth(260)

        self.theme_button = QPushButton("🌙")
        self.settings_button = QPushButton("⚙️")

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(self.search_input)
        layout.addWidget(self.theme_button)
        layout.addWidget(self.settings_button)
        