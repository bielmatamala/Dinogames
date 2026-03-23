from Dino_Game.Classes.Class_Obstacle import Obstacle
import pygame as PG
import random
import os
from Styles.Style import SCREEN, inicialitzar

LARGE_CACTUS = [PG.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                PG.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                PG.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

# Classe del cactus gran que hereta de Obstacle
class LargeCactus(Obstacle):
    def __init__(self, image):
        # Selecciona aleatòriament una de les tres variants del cactus
        self.type = random.randint(0, 2)
        # Crida el constructor del pare (Obstacle)
        super().__init__(image, self.type)
        # Posiciona el cactus verticalment en terra (més amunt que el petit)
        self.rect.y = 300