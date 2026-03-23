import pygame as PG
from Styles.Style import SCREEN_WIDTH

# Classe base per a tots els obstacles
class Obstacle:
    def __init__(self, image, type):
        # Emmagatzema la imatge i el tipus de l'obstacle
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect() # Crea el rectangle de col·lisió a partir de la imatge
        self.rect.x = SCREEN_WIDTH # Posiciona l'obstacle a la dreta de la pantalla

    def update(self, game_speed):
        self.rect.x -= game_speed # Mou l'obstacle cap a l'esquerra depenent la velocitat del joc
        if self.rect.x < -self.rect.width: 
            return False # Retorna False si l'obstacle surt de la pantalla (per a eliminar-lo)
        return True

    def draw(self, SCREEN):
        # Dibuixa l'obstacle a la pantalla
        SCREEN.blit(self.image[self.type], self.rect)