import sys
import os

# Add the directory containing ocr.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from raid import Raids

def test_raids_get_next_mechanic():
    raids = Raids()
    for boss in raids.bosses:
        for gate in boss.gates:
            result = gate.get_next_mechanic(50)
            assert isinstance(result.description, str)
        