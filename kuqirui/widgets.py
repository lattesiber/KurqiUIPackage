from PySide6.QtWidgets import QPushButton, QFrame, QVBoxLayout, QLineEdit
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QCursor

# --- 1. MODERN KUQIR BUTON ---
class KuqirButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: #0e639c;
                color: white;
                border: none;
                padding: 10px 15px;
                font-size: 13px;
                font-weight: bold;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #1177bb;
            }
            QPushButton:pressed {
                background-color: #094771;
            }
        """)

# --- 2. MODERN YAN PANEL (SIDEBAR) ---
class KuqirSidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(220)
        self.setStyleSheet("""
            QFrame {
                background-color: #252526; 
                border-right: 1px solid #333333;
            }
            QLabel {
                color: #858585;
                font-weight: bold;
                font-size: 11px;
                padding: 5px;
            }
        """)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 20, 10, 20)
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignTop)

# --- 3. MODERN ADRES ÇUBUĞU ---
class KuqirAddressBar(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText("URL yazın veya arama yapın...")
        self.setStyleSheet("""
            QLineEdit {
                background-color: #3c3c3c;
                color: #cccccc;
                border: 1px solid #555555;
                padding: 8px 12px;
                border-radius: 5px;
                font-size: 13px;
                selection-background-color: #264f78;
            }
            QLineEdit:focus {
                border: 1px solid #007acc;
                color: white;
            }
        """)

# --- 4. KUQIR WEB TARAYICI MOTORU ---
class KuqirBrowser(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setUrl(QUrl("https://www.google.com"))
        self.setStyleSheet("background-color: #1e1e1e;")

    def navigate_to(self, url):
        # URL temizleme: http yoksa ekle
        q_url = QUrl(url)
        if q_url.scheme() == "":
            q_url.setScheme("https")
        
        # Eğer bir kelimeyse Google'da ara
        if "." not in url:
            self.setUrl(QUrl(f"https://www.google.com/search?q={url}"))
        else:
            self.setUrl(q_url)
