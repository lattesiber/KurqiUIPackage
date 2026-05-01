# kuqirui/core.py
import os
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon

class KuqirApp(QMainWindow):
    def __init__(self, title=None): # Varsayılan None yapıyoruz
        super().__init__()
        
        # Eğer title yoksa veya boşsa "KuqirUI" ismini ver
        if not title:
            self.setWindowTitle("KuqirUI")
        else:
            self.setWindowTitle(title)
            
        self.resize(1100, 700)
        self.handle_logo()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e1e; }
            QWidget { color: #cccccc; font-family: 'Segoe UI'; }
        """)

    def handle_logo(self):
        # Logo arama mantığı
        paths = ["logo.png", "kuqirui/logo.png"]
        for p in paths:
            if os.path.exists(p):
                self.setWindowIcon(QIcon(p))
                return
