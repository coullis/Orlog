import pygame
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

#for x in p1cup:
#    print(random.choice(x))
#
#print(random.choice(d1))

pygame.init()
environ['SDL_VIDEO_WINDOW_POS'] = f"{973},{-1200}"
screen = pygame.display.set_mode((1920, 1200), pygame.SCALED)
pygame.display.set_caption("Orlog")
clock = pygame.time.Clock()

# GRAPHICS ===========================================================================================================
bg_img = pygame.image.load("graphics/bg.jpg").convert_alpha()
exit_img = pygame.image.load("graphics/exit.png").convert_alpha()

# CLASSES =============================================================================================================


class Button():
    def __init__(self, x, y, image, s):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image = pygame.transform.scale_by(self.image, s)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# BUTTON INSTANCES ====================================================================================================


exit_button = Button(1800, 100, exit_img, 0.2)


# GAME LOOP ===========================================================================================================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    pygame.display.update()
    clock.tick(60)

    screen.blit(bg_img, (0, 0))

    exit_button.draw()
