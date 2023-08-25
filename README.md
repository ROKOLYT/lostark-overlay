# Lost Ark Overlay

⚠️ **Warning:** This repo is in active developement and it's contents are subject to change.

Simple overlay written in python that shows the next boss mechanic using OCR

- [Features](#features)
- [How it works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)

# Features
* Fully automated mechanic detection
    - Support automatic boss, gate and phase detection.
    - Mechanic detection is based on the current boss HP.
* Currently implemented raids
    - Valtan [Hard]
    - Brelshaza [Normal] Gate 1-2
    - Kakul-Saydon [Normal]

# How it works
+ The program calibrates itself and tries to detect both the boss and the HP using OCR.
+ It then remembers where those 2 elements are and updates the values only by scanning those areas which massively improves performance.
+ Finally, based on the boss and the current HP it displays the next mechanic.

# Installation
```bash

# Clone this repo
git clone https://github.com/ROKOLYT/lostark-overlay.git ; cd lostark-overlay
```
Install pytorch-cuda to enable GPU acceleration if you have an NVIDIA GPU

```bash
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
```
```bash
# Install requirements
pip install -r requirements.txt
```

# Usage
```bash
# Run main.py
python main.py
```