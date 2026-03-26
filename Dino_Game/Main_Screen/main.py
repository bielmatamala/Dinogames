#pantalla principal abans de començar el joc, on es mostra els contols i el nonms del joc
import pygame as PG
from Styles.Style import SCREEN, WHITE, font

def main_screen():
    PG.init()
    PG.display.set_caption("Dino Game")
    screen = SCREEN
    