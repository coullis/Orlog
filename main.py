import pygame
import myLib as ml
from sys import exit

d1 = ["axe", "axe", "arrow", "shield", "felmet", "fteal"]
d2 = ["axe", "axe", "farrow", "shield", "felmet", "steal"]
d3 = ["axe", "axe", "farrow", "shield", "helmet", "fteal"]
d4 = ["axe", "axe", "arrow", "field", "felmet", "steal"]
d5 = ["axe", "axe", "arrow", "field", "helmet", "fteal"]
d6 = ["axe", "axe", "farrow", "field", "helmet", "steal"]

p1cup = [d1, d2, d3, d4, d5, d6]

skipRoll = 0

# GAME LOOP ===========================================================================================================

while True:
    drawAll = [[ml.bg_img, (0, 0)], [ml.exit_button.image, (ml.width * 0.97, ml.height * 0.01)]]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                skipRoll = 1

    ml.exit_button.draw()
    if ml.exit_button.clicked:
        exit()

    if not ml.play_button.clicked:
        drawAll.append(ml.play_button.draw())
        skipRoll = 0
    else:
        if not skipRoll:
            drawAll.append(ml.rollmsg.draw())
            drawAll.append(ml.roll())
        else:
            print(ml.chooseDice(p1cup))
            #need to print only once after roll

    ml.updateScreen(drawAll)
