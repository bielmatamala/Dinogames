import os
import sys
from pathlib import Path
import pygame as PG

# Ensure imports work when running this file directly (Python sets cwd to Classes/)
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Styles.Style import inicialitzar
from Variables_Globals import RUNNING, JUMPING, DOWNING
from Classes.Class_Obstacle import Obstacle

inicialitzar()

class Cloud(Obstacle):


