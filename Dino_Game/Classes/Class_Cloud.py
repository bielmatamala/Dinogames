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
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = PG.image.load(os.path.join('Assets', 'Cloud.png')).convert_alpha()
        self.image = PG.transform.scale(self.image, (60, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def update(self):
        self.rect.x -= 5  # Moure a la esquerra a velocitat constant
        if self.rect.right < 0:  # Si el nuvol va fora, reinicia la posicio
            self.rect.left = 800  # assumint que screen width es 800
    
    
