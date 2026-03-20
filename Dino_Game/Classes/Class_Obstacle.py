import os
import sys
from pathlib import Path
import pygame as PG
from Styles.Style import inicialitzar, SCREEN_WIDTH

# Ensure the project root (Dino_Game) is on sys.path so imports work when running this file directly.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Styles.Style import inicialitzar
from Variables_Globals import RUNNING, JUMPING, DOWNING

inicialitzar()

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)