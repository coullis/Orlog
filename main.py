import pygame
import myLib as ml
from os import environ
from sys import exit
import random

d1 = ["axe", "axe", "arrow", "shield", "felmet", "fteal"]
d2 = ["axe", "axe", "farrow", "shield", "felmet", "steal"]
d3 = ["axe", "axe", "farrow", "shield", "helmet", "fteal"]
d4 = ["axe", "axe", "arrow", "field", "felmet", "steal"]
d5 = ["axe", "axe", "arrow", "field", "helmet", "fteal"]
d6 = ["axe", "axe", "farrow", "field", "helmet", "steal"]

p1cup = ["d1", "d2", "d3", "d4", "d5", "d6"]

pygame.init()
environ['SDL_VIDEO_WINDOW_POS'] = f"{990},{-1200}"
screen = pygame.display.set_mode((1920, 1200), pygame.FULLSCREEN)
pygame.display.set_caption("Orlog")
clock = pygame.time.Clock()

# GAME LOOP ===========================================================================================================

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    screen.blit(ml.bg_img, (0, 0))

    if ml.exit_button.draw():
        exit()

    if ml.play_button.draw():
        ml.play_button.active = False

    if not ml.play_button.active:
        ml.roll()

    pygame.display.update()
    clock.tick(60)
