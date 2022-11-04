import sys
import pygame

import function as func

if __name__ == '__main__':
    pygame.init()
    pygame.display.init()

    DISPLAY = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
    print(DISPLAY)
    pygame.display.set_caption("Chess in Pygame")

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        DISPLAY.fill((0, 0, 0))

        func.gridrender()

        pygame.display.update()
