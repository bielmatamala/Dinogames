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
pygame.init()
PG = pygame
inicialitzar() #Styles


#Programa principal
def main():
    run = True
    player = Dinosaur()
    clock = PG.time.Clock()
    cloud = Cloud()
    game_speed = 20
    points = 0
    obstacles = []
    font = PG.font.Font('freesansbold.ttf', 20)

    while run: 
    

#Marc -> class: Bird i catctus
#Biel -> Class: Dino
#Despres -> cloud, obstacle
#fer un ftx per a les calsses un atre per les imategs... i un per cada clsse(dino, nubol, ...)

def main_2():
    # Versió completa amb obstacles i col·lisió
    run = True
    clock = PG.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 20
    points = 0
    obstacles = []
    font = PG.font.Font('freesansbold.ttf', 20)
    
    while run:
        for event in PG.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()
        
        # Crida a les classes del dinosaure
        player.draw(SCREEN)
        player.update(userInput)
        
        # Crida a la classe del núvol
        cloud.draw(SCREEN)
        cloud.update(game_speed)
        
        # Crear obstacles aleatòriament
        if len(obstacles) == 0:
            obstacle_type = random.randint(0, 2)
            if obstacle_type == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obstacle_type == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            else:
                obstacles.append(Bird(BIRD))
        
        # Crida a les classes dels obstacles
        for obstacle in obstacles[:]:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed)
        
        # Puntuació
        points += 1
        if points % 100 == 0:
            game_speed += 1
        
        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1100 // 2, 40)
        SCREEN.blit(text, textRect)
        
        clock.tick(30)
        pygame.display.update()
    