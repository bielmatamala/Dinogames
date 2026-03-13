import pygame
import random
import os
import math
# Inicializar Pygame

pygame.init()
PG = pygame

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1100
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 120

# Colors
WHITE = (247, 247, 247)
BLACK = (0, 0, 0)
GARY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

#crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino_game")
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Variables Globals 
RUNNING = [PG.image.load(os.path.join(r"dinogames\dino-master\Assets\Dino", r"DinoRun1.png")),
           PG.image.load(os.path.join(r"dinogames\dino-master\Assets\Dino", r"DinoRun2.png"))]

#Classes
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
