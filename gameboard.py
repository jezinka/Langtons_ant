import os
import pygame
import random

import ant

__author__ = 'jezinka'

os.environ['SDL_VIDEO_CENTERED'] = '1'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
CYAN = (0, 255, 255, 255)
PURPLE = (255, 0, 255, 255)

colors = [RED, GREEN, BLUE, CYAN, PURPLE]


def start_ants(ants, height, width):
    pygame.init()
    pygame.display.set_caption("Langton's ants")

    size = int(width), int(height)
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    step_counter = 0

    screen.fill(WHITE)
    pygame.display.flip()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255, 255))

    font = pygame.font.Font(None, 24)

    my_ant = []
    ant_count = int(ants)

    for i in range(ant_count):
        my_ant.append(ant.Ant(random.randint(0, size[0] - 1), random.randint(0, size[1] - 1), colors[i % len(colors)]))

    # -------- Main Program Loop -----------
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                elif event.key == pygame.K_ESCAPE:
                    pygame.display.set_mode(size)

        step_counter += 1
        for i in range(len(my_ant)):
            clockwise = background.get_at(my_ant[i].position) == WHITE
            background.set_at(my_ant[i].position, my_ant[i].color if clockwise else WHITE)
            my_ant[i].position = my_ant[i].move(clockwise, size)

        text = font.render("Step:" + str(step_counter), True, BLACK)
        screen.blit(text, (0, 0))
        pygame.display.update()

        background = background.convert()
        screen.blit(background, (0, 0))

        clock.tick(120)

    pygame.quit()


def init_program():
    try:
        ants_count = int(raw_input('Choose number of ants:'))
        height = int(raw_input('Choose height of screen:'))
        width = int(raw_input('Choose width of screen:'))

        start_ants(ants_count, height, width)

    except ValueError:
        print '\nWrong format of input data, should be numbers. Try again.'
        init_program()


init_program()
