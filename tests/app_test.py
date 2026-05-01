import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import Qt
from kuqirui import KuqirApp, KuqirButton, KuqirSidebar
from kuqirui.widgets import KuqirBrowser # Yeni eklediğimiz bileşen

def main():
    app = QApplication(sys.argv)
    
    # Pencere başlığı verilmezse otomatik "KuqirUI" olacak
    window = KuqirApp() 
    window.resize(1200, 800)

    # --- SIDEBAR ---
    sidebar = KuqirSidebar()
    window.main_layout.addWidget(sidebar)
    
    sidebar.layout.addWidget(KuqirButton("Favoriler"))
    sidebar.layout.addWidget(KuqirButton("Geçmiş"))
    sidebar.layout.addStretch()

    # --- ANA TARAYICI ALANI ---
    browser_container = QWidget()
    browser_layout = QVBoxLayout(browser_container)
    browser_layout.setContentsMargins(5, 5, 5, 5)

    # Adres Çubuğu Paneli
    nav_bar = QHBoxLayout()
    
    address_bar = QLineEdit()
    address_bar.setPlaceholderText("URL yazın veya arama yapın...")
    address_bar.setStyleSheet("""
        QLineEdit {
            background-color: #3c3c3c;
            color: white;
            border: 1px solid #555;
            padding: 8px;
            border-radius: 4px;
            font-family: 'Segoe UI';
        }
    """)
    
    go_btn = KuqirButton("Git")
    
    nav_bar.addWidget(address_bar)
    nav_bar.addWidget(go_btn)
    
    # Tarayıcı Motoru
    web_view = KuqirBrowser()
    
    # Fonksiyonlar
    def load_url():
        web_view.navigate_to(address_bar.text())

    go_btn.clicked.connect(load_url)
    address_bar.returnPressed.connect(load_url) # Enter tuşuna basınca git

    # Layout'a ekle
    browser_layout.addLayout(nav_bar)
    browser_layout.addWidget(web_view)

    window.main_layout.addWidget(browser_container, 1)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
