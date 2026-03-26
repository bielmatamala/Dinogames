from Classes.Class_Obstacle import Obstacle
import pygame as PG
import random
import os
from Styles.Style import SCREEN
from Variables_Globals import SMALL_CACTUS

# Classe del cactus petit que hereta de Obstacle
class SmallCactus(Obstacle):
    def __init__(self, image):
        # Selecciona aleatòriament una de les tres variants del cactus
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        # Posiciona el cactus verticalment en terra
        self.rect.y = 325
