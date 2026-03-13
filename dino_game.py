import pygame
import random
import sys
import math

# Inicializar Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
GROUND_HEIGHT = 120
FPS = 60

# Colors
WHITE = (247, 247, 247)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game - Sense Connexió")
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

class Dino(pygame.sprite.Sprite):
    """Classe pel dinosaure T-Rex"""
    def __init__(self):
        super().__init__()
        self.width = 60
        self.height = 60
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.draw_dino()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
        
        self.vel_y = 0
        self.is_jumping = False
        self.gravity = 0.7
        self.jump_power = 16
        self.leg_cycle = 0  # Per a animació de les potes
        
    def draw_dino(self):
        """Dibuixar el dinosaure T-Rex"""
        self.image.fill((0, 0, 0, 0))  # Transparent
        
        # Cos (rectangle arrodonit)
        pygame.draw.ellipse(self.image, BLACK, (15, 25, 35, 25))
        
        # Cap (mé gran)
        pygame.draw.circle(self.image, BLACK, (42, 20), 12)
        
        # Cua (triangle)
        tail_points = [(50, 30), (55, 20), (50, 35)]
        pygame.draw.polygon(self.image, BLACK, tail_points)
        
        # Ull
        pygame.draw.circle(self.image, WHITE, (46, 18), 2)
        
        # Potes davanteres
        pygame.draw.rect(self.image, BLACK, (25, 48, 4, 12))
        pygame.draw.rect(self.image, BLACK, (32, 48, 4, 12))
        
        # Potes posteriors
        pygame.draw.rect(self.image, BLACK, (42, 48, 4, 12))
        pygame.draw.rect(self.image, BLACK, (50, 48, 4, 12))
        
        # Braços (més petits)
        pygame.draw.rect(self.image, BLACK, (30, 35, 3, 8))
        pygame.draw.rect(self.image, BLACK, (45, 35, 3, 8))
    
    def jump(self):
        """Fer saltar el dinosaure"""
        if not self.is_jumping:
            self.is_jumping = True
            self.vel_y = -self.jump_power
    
    def update(self):
        """Actualitzar la posició del dinosaure"""
        # Aplicar gravetat
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        
        # Detectar col·lisió amb el sòl
        if self.rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
            self.is_jumping = False
            self.vel_y = 0
        
        self.leg_cycle += 1
    
    def draw(self, surface):
        """Dibuixar el dinosaure"""
        surface.blit(self.image, self.rect)


class Obstacle(pygame.sprite.Sprite):
    """Classe pels obstacles (cactus)"""
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 60
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
        self.speed = 8
    
    def update(self):
        """Actualitzar la posició de l'obstacle"""
        self.rect.x -= self.speed
    
    def draw(self, surface):
        """Dibuixar l'obstacle"""
        surface.blit(self.image, self.rect)


class Cloud(pygame.sprite.Sprite):
    """Classe pels núvols (decoració)"""
    def __init__(self, x, y):
        super().__init__()
        self.width = 60
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
    
    def update(self):
        """Actualitzar la posició del núvol"""
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH
    
    def draw(self, surface):
        """Dibuixar el núvol"""
        surface.blit(self.image, self.rect)


def main():
    """Funció principal del joc"""
    # Crear sprites
    dino = Dino()
    clouds = [Cloud(random.randint(0, SCREEN_WIDTH), random.randint(20, 100)) for _ in range(3)]
    obstacles = []
    
    # Variables del joc
    score = 0
    game_over = False
    obstacle_spawn_timer = 0
    obstacle_spawn_rate = 60  # Spawnar obstacle cada 60 frames
    
    running = True
    while running:
        clock.tick(FPS)
        
        # Gestionar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_over:
                        dino.jump()
                    else:
                        # Reiniciar el joc
                        return main()
        
        if not game_over:
            # Actualitzar dinosaure
            dino.update()
            
            # Actualitzar núvols
            for cloud in clouds:
                cloud.update()
            
            # Spawnar obstacles
            obstacle_spawn_timer += 1
            if obstacle_spawn_timer >= obstacle_spawn_rate:
                obstacles.append(Obstacle())
                obstacle_spawn_timer = 0
                # Augmentar dificultat
                if obstacle_spawn_rate > 30:
                    obstacle_spawn_rate -= 2
            
            # Actualitzar obstacles
            for obstacle in obstacles:
                obstacle.update()
                
                # Detectar col·lisió
                if pygame.sprite.spritecollide(dino, [obstacle], False):
                    game_over = True
                
                # Incrementar puntuació si l'obstacle ha passat
                if obstacle.rect.right < dino.rect.left and not hasattr(obstacle, 'counted'):
                    score += 10
                    obstacle.counted = True
            
            # Eliminar obstacles que han sortit de la pantalla
            obstacles = [obs for obs in obstacles if obs.rect.right > 0]
        
        # Dibuixar
        screen.fill(WHITE)
        
        # Dibuixar sòl
        pygame.draw.line(screen, BLACK, (0, SCREEN_HEIGHT - GROUND_HEIGHT), 
                        (SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT), 2)
        
        # Dibuixar núvols
        for cloud in clouds:
            cloud.draw(screen)
        
        # Dibuixar obstacles
        for obstacle in obstacles:
            obstacle.draw(screen)
        
        # Dibuixar dinosaure
        dino.draw(screen)
        
        # Dibuixar puntuació
        score_text = font.render(f"Punts: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        # Dibuixar missatge de Game Over
        if game_over:
            game_over_font = pygame.font.Font(None, 48)
            game_over_text = game_over_font.render("GAME OVER", True, BLACK)
            restart_text = font.render("Prem ESPAI per reiniciar", True, BLACK)
            
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 20))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
