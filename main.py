import sys

from PyQt5.QtWidgets import QApplication
from app import OverlayWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = OverlayWidget()
    overlay.show()
    sys.exit(app.exec_())
    