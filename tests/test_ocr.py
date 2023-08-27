import sys
import os

# Add the directory containing ocr.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ocr import OCR

images = ["brel_g1.png", "brel_g2.png", "valtan_g1_1.png", "valtan_g1_2.png", "valtan_g1_3.png", "valtan_g2_1.png", "valtan_g2_2.png"]
images = ["examples/" + image for image in images]

def test_ocr_calibrate():
    for image in images:
        ocr = OCR()
        ocr.current = image
        result = ocr.calibrate()
        assert result is True
