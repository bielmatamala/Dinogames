import pygame as PG


# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1100
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_speed = 120

# Colors
WHITE = (247, 247, 247)
BLACK = (0, 0, 0)
GARY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

#crear la pantalla
screen = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PG.display.set_caption("Dino_game")
clock = PG.time.Clock()

# Font
font = PG.font.Font(None, 36)


def inicialitzar():
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
    screen = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PG.display.set_caption("Dino_game")
    clock = PG.time.Clock()

    # Font
    font = PG.font.Font(None, 36)
