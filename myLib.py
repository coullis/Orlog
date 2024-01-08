import pygame

screen = pygame.display.set_mode((1920, 1200), pygame.FULLSCREEN)


class Button():
    def __init__(self, x, y, image, s):
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

def roll():
    pressed = pygame.key.get_pressed()
    cup_img = pygame.image.load("graphics/cup.png").convert_alpha()
    run = True
    while run:
        if pressed[pygame.K_SPACE]:
            screen.blit(cup_img, (100, 100))





