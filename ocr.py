import easyocr
import re
import cv2
import logging

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
        self.hp_bbox = None
        self.boss_bbox = None
        self.fail_safe_hp = 0
        self.fail_safe_gate = 0
        self.hp = 0
        self.gate = ''
        
    def calibrate(self, hp_bbox=None, boss_bbox=None):
        logging.warning("Calibrating")
        
        self.screenshot()
        
        image = cv2.imread(CURRENT)
        
        res = self.reader.readtext(image)
        
        self.hp_bbox = hp_bbox
        self.boss_bbox = boss_bbox
        
        for r in res:
            text = r[1].lower().replace(" ", "")
            
            if re.match(HP_PATTERN, text) and not self.hp_bbox:
                coordinates = r[0]
                
                top_right = coordinates[1]
                bottom_left = coordinates[3]

                left = (bottom_left[0] - PADDING) * self.screenshot_ratio
                top = (top_right[1] - PADDING) * self.screenshot_ratio
                right = (top_right[0] + PADDING) * self.screenshot_ratio
                bottom = (bottom_left[1] + PADDING) * self.screenshot_ratio
                
                self.hp_bbox = (left, top, right, bottom)
                
            if self.match_monster(text) and not self.boss_bbox:
                coordinates = r[0]
                
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
        
        elif not self.hp_bbox:
            logging.warning("HP not found")
            return self.calibrate(boss_bbox=self.boss_bbox)
        
        elif not self.boss_bbox:
            logging.warning("Boss not found")
            return self.calibrate(hp_bbox=self.hp_bbox)
        
        if self.hp_bbox and self.boss_bbox:
            logging.warning("Calibration complete")
            self.fail_safe_gate = 0
            self.fail_safe_hp = 0
        
    def get_hp(self):
        self.screenshot(bbox=self.hp_bbox)
        
        image = cv2.imread(CURRENT)
        
        res = self.reader.readtext(image)
        
        for r in res:
            text = r[1].lower().replace(" ", "")
            
            if self.match_hp(text):
                self.fail_safe_hp = 0
                return self.hp
        
        self.fail_safe_hp += 1
        
        if self.fail_safe_hp > FAIL_SAFE:
            self.calibrate(boss_bbox=self.boss_bbox)
            
        return self.hp
    
    def get_gate(self):
        self.screenshot(bbox=self.boss_bbox)
        
        image = cv2.imread(CURRENT)
        
        res = self.reader.readtext(image)
        
        for r in res:
            text = r[1].lower().replace(" ", "")
            
            if self.match_monster(text):
                self.fail_safe_gate = 0
                return self.gate
            
        self.fail_safe_gate += 1
        
        if self.fail_safe_gate > FAIL_SAFE:
            self.calibrate(hp_bbox=self.hp_bbox)
            
        return self.gate
        
                
    
    def screenshot(self, bbox=None):
        image = ImageGrab.grab(bbox)
        image.save(CURRENT)
        
        # Downscale image to RESOLUTION in order to improve performance
        if bbox is None:
            image = cv2.imread(CURRENT)
            self.screenshot_ratio = image.shape[1] / RESOLUTION
            dim = (RESOLUTION, int(image.shape[0] / self.screenshot_ratio))
            image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            cv2.imwrite(CURRENT, image)
            
    def match_hp(self, text):
        if re.match(HP_PATTERN, text):
                
                hp = text.split("x")[1]
                try:
                    self.hp = int(hp)
                    self.fail_safe = 0
                    
                    return True
                
                except ValueError:
                    return False
        
        return False
    
    def match_monster(self, text):
        raids = Raids()
        
        for boss in raids.bosses:
            
            for gate in boss.gates:
                
                for name in gate.names:
                    if text == name.lower().replace(" ", ""):
                        self.gate = gate
                        return True
        
        return False
            