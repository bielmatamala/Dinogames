import pygame as PG
import os
 

# Variables Globals
RUNNING = [PG.image.load(os.path.join("Assets/Dino", r"DinoRun1.png")),
        PG.image.load(os.path.join("Assets/Dino", r"DinoRun2.png"))]

JUMPING = PG.image.load(os.path.join("Assets/Dino", r"DinoJump.png"))

DOWNING = [PG.image.load(os.path.join("Assets/Dino", r"DinoDuck1.png")),
        PG.image.load(os.path.join("Assets/Dino", r"DinoDuck2.png"))]

SMALL_CACTUS = [PG.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                PG.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                PG.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [PG.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                PG.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                PG.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [PG.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        PG.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = PG.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = PG.image.load(os.path.join("Assets/Other", "Track.png"))

