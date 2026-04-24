WIDTH = 800
HEIGHT = 600

PLAYER_SPEED = 4
SPRINT_SPEED = 7

MONSTER_SPEED = 2

SANITY_DECAY = 0.05

import pygame
from settings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 40, 40)
        self.speed = PLAYER_SPEED
        self.stamina = 100

    def move(self, keys):
        if keys[pygame.K_LSHIFT] and self.stamina > 0:
            self.speed = SPRINT_SPEED
            self.stamina -= 0.5
        else:
            self.speed = PLAYER_SPEED
            self.stamina += 0.2

        self.stamina = max(0, min(100, self.stamina))

        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed

        import pygame
from settings import *

class Monster:
    def __init__(self):
        self.rect = pygame.Rect(500, 300, 40, 40)

    def update(self, player):
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y

        dist = max(1, (dx**2 + dy**2) ** 0.5)

        self.rect.x += MONSTER_SPEED * dx / dist
        self.rect.y += MONSTER_SPEED * dy / dist

        import pygame

def draw_map(screen):
    screen.fill((10, 10, 10))  # dark background

    import pygame

def draw_ui(screen, player, sanity):
    font = pygame.font.SysFont(None, 30)

    stamina_text = font.render(f"Stamina: {int(player.stamina)}", True, (255,255,255))
    sanity_text = font.render(f"Sanity: {int(sanity)}", True, (255,100,100))

    screen.blit(stamina_text, (10,10))
    screen.blit(sanity_text, (10,40))

    import pygame
from player import Player
from monster import Monster
from map import draw_map
from ui import draw_ui
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player()
monster = Monster()

sanity = 100
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move(keys)
    monster.update(player)

    sanity -= SANITY_DECAY

    # DRAW
    draw_map(screen)

    pygame.draw.rect(screen, (0,255,0), player.rect)
    pygame.draw.rect(screen, (255,0,0), monster.rect)

    draw_ui(screen, player, sanity)

    pygame.display.flip()

pygame.quit()

