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
RUNNING = [PG.image.load(os.path.join("Assets/Dino", r"DinoRun1.png")),
           PG.image.load(os.path.join("Assets/Dino", r"DinoRun2.png"))]

JUMPING = PG.image.load(os.path.join("Assets/Dino", r"DinoJump.png"))

DOWNING = [PG.image.load(os.path.join("Assets/Dino", r"DinoDuck1.png")),
           PG.image.load(os.path.join("Assets/Dino", r"DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


#Classes
class Dinosarure:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.down = DOWNING
        self.run_img = RUNNING
        self.jump = JUMPING
        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    
    def avançar(self):
        self.run = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1


#fer un ftx per a les calsses un atre per les imategs... i un per cada clsse(dino, nubol,...)