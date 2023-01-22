
import pygame
pygame.init()

import game

game.initialize([1280, 720], 60, "assets/save.json", title="CPT Game", icon="assets/icon.jpg")

# ------------------------------ #



# ------------------------------ #

while game.RUNNING:
    # updating the window

    # drawing to window
    game.WINDOW.fill((255, 255, 255))


    # update inputs etc
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game.RUNNING = False

    # updating window + fps stuff
    pygame.display.update()
    game.CLOCK.tick(game.FPS)

# close pygame
pygame.quit()
