import logging
import re
import easyocr
import cv2

from PIL import ImageGrab
from raid import Raids

RESOLUTION = 1920
CURRENT = "data/current.png"
HP_PATTERN = r"x\d{1,3}" # match x followed by 1 - 3 digits
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

PADDING = 15
FAIL_SAFE = 10

class OCR():
    def __init__(self):
        self.reader = easyocr.Reader(["en"], gpu=True)
        self.screenshot_ratio = 1 # required for monitors with resolutions other than 1080p
        self.current = "data/current.png"
        self.hp_bbox = None
        self.boss_bbox = None
        self.fail_safe_hp = 0
        self.fail_safe_gate = 0
        self.hp = 0
        self.gate = ''

    def calibrate(self, hp_bbox=None, boss_bbox=None):
        logging.warning("Calibrating")

        if self.current == CURRENT:
            self.screenshot()

        result = self.reader.readtext(self.current)

        self.hp_bbox = hp_bbox
        self.boss_bbox = boss_bbox

        for res in result:
            text = res[1].lower().replace(" ", "")

            if re.match(HP_PATTERN, text) and not self.hp_bbox:
                coordinates = res[0]

                top_right = coordinates[1]
                bottom_left = coordinates[3]

                left = (bottom_left[0] - PADDING) * self.screenshot_ratio
                top = (top_right[1] - PADDING) * self.screenshot_ratio
                right = (top_right[0] + PADDING) * self.screenshot_ratio
                bottom = (bottom_left[1] + PADDING) * self.screenshot_ratio

                self.hp_bbox = (left, top, right, bottom)

            if self.match_monster(text) and not self.boss_bbox:
                coordinates = res[0]

                top_right = coordinates[1]
                bottom_left = coordinates[3]

                left = (bottom_left[0] - PADDING) * self.screenshot_ratio
                top = (top_right[1] - PADDING) * self.screenshot_ratio
                right = (top_right[0] + PADDING) * self.screenshot_ratio
                bottom = (bottom_left[1] + PADDING) * self.screenshot_ratio

                self.boss_bbox = (left, top, right, bottom)

        if not self.hp_bbox and not self.boss_bbox:
            logging.warning("HP and Boss not found")
            return self.calibrate()

        if not self.hp_bbox:
            logging.warning("HP not found")
            return self.calibrate(boss_bbox=self.boss_bbox)

        if not self.boss_bbox:
            logging.warning("Boss not found")
            return self.calibrate(hp_bbox=self.hp_bbox)

        logging.warning("Calibration complete")
        self.fail_safe_gate = 0
        self.fail_safe_hp = 0
        return True

    def get_hp(self) -> int:
        if self.current == CURRENT:
            self.screenshot(bbox=self.hp_bbox)

        result = self.reader.readtext(self.current)

        for res in result:
            text = res[1].lower().replace(" ", "")

            if self.match_hp(text):
                self.fail_safe_hp = 0
                return self.hp

        self.fail_safe_hp += 1

        if self.fail_safe_hp > FAIL_SAFE:
            self.calibrate(boss_bbox=self.boss_bbox)

        return self.hp

    def get_gate(self):
        if self.current == CURRENT:
            self.screenshot(bbox=self.boss_bbox)

        result = self.reader.readtext(self.current)

        for res in result:
            text = res[1].lower().replace(" ", "")

            if self.match_monster(text):
                self.fail_safe_gate = 0
                return self.gate

        self.fail_safe_gate += 1

        if self.fail_safe_gate > FAIL_SAFE:
            self.calibrate(hp_bbox=self.hp_bbox)

        return self.gate

    def screenshot(self, bbox=None):
        image = ImageGrab.grab(bbox)
        image.save(self.current)

        # Downscale image to RESOLUTION in order to improve performance
        if bbox is None:
            image = cv2.imread(self.current)
            self.screenshot_ratio = image.shape[1] / RESOLUTION
            dim = (RESOLUTION, int(image.shape[0] / self.screenshot_ratio))
            image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            cv2.imwrite(self.current, image)

    def match_hp(self, text: str) -> bool:
        if re.match(HP_PATTERN, text):

            hp = text.split("x")[1]
            try:
                self.hp = int(hp)
                self.fail_safe_hp = 0

                return True

            except ValueError:
                return False

        return False

    def match_monster(self, text: str) -> bool:
        raids = Raids()

        for boss in raids.bosses:

            for gate in boss.gates:

                for name in gate.names:
                    if text == name.lower().replace(" ", ""):
                        self.gate = gate
                        self.fail_safe_gate = 0

                        return True

        return False
            