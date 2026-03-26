import pygame as PG
import random
import os
from Styles.Style import SCREEN, WHITE
from Variables_Globals import RUNNING, JUMPING, DOWNING, SMALL_CACTUS, LARGE_CACTUS, BIRD, CLOUD, BG
from Classes.Class_Dino import Dinosaur
from Classes.Class_Obstacle import Obstacle
from Classes.Class_Cloud import Cloud
from Classes.Class_Bird import Bird
from Classes.Class_Cactus.Class_SmallCactus import SmallCactus
from Classes.Class_Cactus.Class_LargeCacuts import LargeCactus


# Inicializar Pygame
PG.init()


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
    x_pos_bg = 0
    y_pos_bg = 380

    while run:
        PG.mixer.music.load(r"C:\Users\AppJT\Dinogames\Dino_Game\GAME\Assets\Sons\43861138-jurassic-park-210987.mp3")
        PG.mixer.music.play(-1)
        for event in PG.event.get():
            if event.type == PG.QUIT:
                run = False

        SCREEN.fill(WHITE)
        userInput = PG.key.get_pressed()
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg)) # Dibuixa una segona imatge darrere
        
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0 # Torna a començar el bucle d'imatges
        x_pos_bg -= game_speed

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
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obstacle_tipus == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            else:
                obstacles.append(Bird(BIRD))
        # Crida a les classes dels obstacles
        for obstacle in obstacles[:]:
            obstacle.draw(SCREEN)
            if not obstacle.update(game_speed):
                obstacles.remove(obstacle)
        
        if userInput[PG.KSCAN_EURO]: #Si el jugador prem la tecla de reiniciar el joc, es reinicia
            main() # Reinicia el joc
            
        #Comporvar col·lisions
        if Dino.dino_rect.colliderect(obstacle.rect):
                PG.time.delay(100) # El joc es congela 2 segons (2000 mil·lisegons) perquè vegis el xoc

                run = False
        
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

if __name__ == "__main__":
    
    main()