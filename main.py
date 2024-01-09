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

# GRAPHICS ===========================================================================================================
bg_img = pygame.image.load("graphics/bg.jpg").convert_alpha()
exit_img = pygame.image.load("graphics/exit.png").convert_alpha()
play_img = pygame.image.load("graphics/play.png").convert_alpha()
cup_img = pygame.image.load("graphics/cup.png").convert_alpha()

# BUTTON INSTANCES ====================================================================================================
exit_button = ml.Button(1870, 10, exit_img, 0.1)
play_button = ml.Button(40, 40, play_img, 0.5)
cup_sprite = ml.Button(100, 500, cup_img, 0.5)


# FUNCTIONS ===========================================================================================================

#def roll():
    #TODO


# GAME LOOP ===========================================================================================================
screen.blit(bg_img, (0, 0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    if exit_button.draw():
        exit()

    if play_button.draw():
        play_button.active = False
        #roll()

    pygame.display.update()
    clock.tick(60)





