import numpy as np
import random

TOTAL_SLOTS = 20

def detect_parking_slots():
    # Simulated occupancy detection (replace with real OpenCV later)
    occupancy = [random.choice([0, 1]) for _ in range(TOTAL_SLOTS)]
    return occupancy
