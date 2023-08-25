import sys

from app import OverlayWidget
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = OverlayWidget()
    overlay.show()
    sys.exit(app.exec_())