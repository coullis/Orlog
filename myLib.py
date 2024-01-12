import pygame
import random

pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Orlog")
clock = pygame.time.Clock()
cup = 1

# GRAPHICS ===========================================================================================================
bg_img = pygame.image.load("graphics/bg.jpg").convert_alpha()
exit_img = pygame.image.load("graphics/exit.png").convert_alpha()
play_img = pygame.image.load("graphics/play.png").convert_alpha()
cup_img = pygame.image.load("graphics/cup.png").convert_alpha()
fcup_img = pygame.image.load("graphics/fcup.png").convert_alpha()
rollmsg_img = pygame.image.load("graphics/rollmsg.png").convert_alpha()


class Button:
    def __init__(self, x, y, image, s=1.0):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image = pygame.transform.scale_by(self.image, s)
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return [self.image, (self.rect.x, self.rect.y)]


# BUTTON INSTANCES ====================================================================================================
exit_button = Button(width * 0.97, height * 0.01, exit_img, s=0.1)
play_button = Button(width * 0.01, height * 0.01, play_img, s=0.5)
cup_sprite = Button(width * 0.4, height * 0.3, cup_img, s=0.7)
fcup_sprite = Button(width * 0.4, height * 0.4, fcup_img, s=0.7)
rollmsg = Button(width * 0.3, height * 0.9, rollmsg_img, s=0.7)


# FUNCTIONS ===========================================================================================================

def roll():
    global cup
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if cup == 1:
            pygame.time.wait(200)
            cup = 2
            return cup_sprite.draw()
        else:
            pygame.time.wait(200)
            cup = 1
            return fcup_sprite.draw()

    return exit_button.draw()


def updateScreen(drawAll):
    for x in drawAll:
        screen.blit(x[0], x[1])
    pygame.display.update()
    clock.tick(60)


def chooseDice(p1cup):
    currentDFaces = []
    for x in p1cup:
        currentDFaces.append(x[random.randint(0, 5)])
    return currentDFaces
