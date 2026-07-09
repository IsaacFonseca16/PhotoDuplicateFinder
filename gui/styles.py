APP_STYLE = """
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
    padding: 10px 16px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1d4ed8;
}

QPushButton#secondary {
    background-color: #334155;
}

QPushButton#danger {
    background-color: #dc2626;
}

QFrame#panel {
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

QScrollArea {
    border: none;
    background-color: transparent;
}
"""