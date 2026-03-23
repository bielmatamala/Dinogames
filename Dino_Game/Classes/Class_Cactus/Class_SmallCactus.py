from Classes.Class_Obstacle import Obstacle
import pygame as PG
import random
import os
from Styles.Style import SCREEN

SMALL_CACTUS = [PG.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                PG.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                PG.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

# Classe del cactus petit que hereta de Obstacle
class SmallCactus(Obstacle):
    def __init__(self, image):
        # Selecciona aleatòriament una de les tres variants del cactus
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        # Posiciona el cactus verticalment en terra
        self.rect.y = 325
