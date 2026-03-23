import pygame as PG
import random
import os
from Styles.Style import SCREEN, inicialitzar
from Variables_Globals import RUNNING, JUMPING, DOWNING
from Classes.Class_Dino import Dinosaur
from Classes.Class_Obstacle import Obstacle
from Classes.Class_Cloud import Cloud
from Classes.Class_Bird import Bird
from Classes.Class_Cactus.Class_SmallCactus import SmallCactus
from Classes.Class_Cactus.Class_LargeCacuts import LargeCactus

# Inicializar Pygame
PG.init()
PG = PG
inicialitzar() #Styles


#Programa principal
def main():
    run = True
    Dino = Dinosaur()
    clock = PG.time.Clock()
    cloud = Cloud()
    game_speed = 20
    points = 0
    obstacles = []
    font = PG.font.Font('freesansbold.ttf', 20)

    while run:
        PG.mixer.music.load("")
        PG.mixer.music.play(-1)
        for event in PG.event.get():
            if event.type == PG.QUIT:
                run = False

        SCREEN.fill((255,255,255))
        userInput = PG.key.get_pressed()

        # Cridar calsse del dinosuare
        Dino.draw(SCREEN)
        Dino.update(userInput)

        # Cridar calsse del núvol
        cloud.draw(SCREEN)
        cloud.update(game_speed)

        # Crear obstacles aleatòriament
        if len(obstacles) == 0:
            obstacle_tipus = random.randint(0,2)
            if obstacle_tipus == 0:
                obstacles.append(SmallCactus)
            elif obstacle_tipus == 1:
                obstacles.append(LargeCactus)
            else:
                obstacles.append(Bird)
        
        # Crida a les classes dels obstacles
        for obstacle in obstacles[:]:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed)
        
        # Puntuació
        points += 1
        if points % 100 == 0:
            game_speed += 1
        # Ensenyaqr els punts per pantalla
        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1100 // 2, 40)
        SCREEN.blit(text, textRect)
        
        clock.tick(30)
        PG.display.update()

if __name__ == "main":
    main()
