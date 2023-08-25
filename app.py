import threading
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from time import sleep
from ocr import OCR

PADX, PADY = 150, 150

class OverlayWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | 
            Qt.FramelessWindowHint |
            # Hide program from taskbar
            Qt.Tool
        )
        
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.layout = QVBoxLayout(self)
        
        pixmap = QPixmap("data/empty.png")
        
        self.image = QLabel(self)
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setPixmap(pixmap)
        
        self.layout.addWidget(self.image)
        
        self.label = QLabel("Hello Overlay!", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white; font-size: 50px; border-style: outset; border-width: 5px; border-radius: 20px; border-color: black")
        
        self.layout.addWidget(self.label)
        
        self.setGeometry(100, 100, 400, 200)
        
        updateBossData_thread = threading.Thread(target=self.updateBossData)
        updateBossData_thread.start()
        
    def showEvent(self, event):
        super().showEvent(event)
        
        super().showEvent(event)
        
        # Get the screen's geometry
        screen_geometry = QApplication.primaryScreen().geometry()
        
        # Set the position of the top-left corner of the widget to the bottom right corner
        self.move(screen_geometry.width() - self.width() - PADX, screen_geometry.height() - self.height() - PADY)
        
    def changeContent(self, text, image_path=None):
        
        if image_path:
            pixmap = QPixmap(image_path)
            self.image.setPixmap(pixmap)
        
        self.label.setText(text)
        
    def updateBossData(self):
        ocr = OCR()
        ocr.calibrate()
        
        while True:
            hp = ocr.get_hp()
            gate = ocr.get_gate()
            
            if hp and gate:
                mechanic = gate.get_next_mechanic(hp).description
                self.changeContent(mechanic)
                
            sleep(1)