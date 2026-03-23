import pygame as PG

# Engeguem Pygame aquí mateix perquè no ens peti res al crear finestres o lletres
PG.init()

# Constants Globals de la Pantalla
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1100
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PG.display.set_caption("Dino_game")

game_speed = 120

# Colors
WHITE = (247, 247, 247)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)  
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
clock = PG.time.Clock()
font = PG.font.Font("freesansbold.ttf", 36) 
