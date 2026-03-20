from Dino_Game.Classes.Class_Obstacle import Obstacle
import pygame as PG
import os
from Styles.Style import SCREEN, inicialitzar

BIRD = [PG.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        PG.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

# Classe de l'ocell que hereta de Obstacle
class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0 # Tipus 0 significa que és un ocell
        super().__init__(image, self.type)

        self.rect.y = 250 #Posiciona l'ocell en altura
        self.index = 0 #Índex per a l'animació de l'ocell

    def draw(self, SCREEN):
        # Anima l'ocell canviant entre les dues imatges
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)  # Dibuixa la imatge corresponent a l'animació
        self.index += 1 # Incrementa l'índex per a la següent frame d'animació
