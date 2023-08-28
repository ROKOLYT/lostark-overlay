import sys
import os

# Add the directory containing ocr.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PyQt5.QtWidgets import QApplication
from app import OverlayWidget

def test_app_show_event():
    app = QApplication(sys.argv)
    overlay = OverlayWidget()
    overlay.show()
    assert overlay.isVisible()