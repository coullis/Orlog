import pygame
import time

screen = pygame.display.set_mode((1920, 1200), pygame.FULLSCREEN)
clock = pygame.time.Clock()

# GRAPHICS ===========================================================================================================
bg_img = pygame.image.load("graphics/bg.jpg").convert_alpha()
exit_img = pygame.image.load("graphics/exit.png").convert_alpha()
play_img = pygame.image.load("graphics/play.png").convert_alpha()
cup_img = pygame.image.load("graphics/cup.png").convert_alpha()
fcup_img = pygame.image.load("graphics/fcup.png").convert_alpha()


class Button:
    def __init__(self, x, y, image, s=1.0):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image = pygame.transform.scale_by(self.image, s)
        self.clicked = False
        self.active = True

    def draw(self):
        action = False
        if self.active:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# BUTTON INSTANCES ====================================================================================================
exit_button = Button(1870, 10, exit_img, s=0.1)
play_button = Button(40, 40, play_img, s=0.5)
cup_sprite = Button(100, 500, cup_img, s=0.5)
fcup_sprite = Button(100, 500, fcup_img, s=0.5)

# FUNCTIONS ===========================================================================================================


def roll():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        cup_sprite.draw()
        pygame.display.update()
        pygame.time.wait(500)
        screen.blit(bg_img, (0, 0))
        exit_button.draw()
        fcup_sprite.draw()
        pygame.display.update()
        pygame.time.wait(500)



