import pygame
import keypresses as k
import saver
import loader
import numpy as np
from model import Model
from collections import deque

TIMESTEP = 5

def init():
    pygame.init()
    screen = pygame.display.set_mode((650, 400))
    pygame.display.set_caption("mimickAI")
    k.setup()
    m = Model()
    sav = saver.Saver()

    image_stream = deque()

    running = True

    inputs = np.zeros(shape=(10,))

    i = 0

    while running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

        #generate image stream

        '''if k.get_ai_or_player():
            # player active, dont record
            sav.record(False, k.get_bits())

        else:
            sav.record(True, k.get_bits())

        update(screen, k.get_bits())

        '''

        sav.record(False, k.get_bits())

        if i == TIMESTEP:
            inputs = m.predict(np.expand_dims(np.array(image_stream), axis=0))

            image_stream.popleft()
            image_stream.append(sav.get_current_img())

        else:
            i += 1
            image_stream.append(sav.get_current_img())

        if k.get_ai_or_player():
            # player active, record
            k.send_bits(inputs)
            update(screen, inputs)
        else:
            update(screen, k.get_bits())

        pygame.display.update()

    sav.close()


def update(screen, keys):
    screen.fill((255, 255, 255))

    draw_controller(screen, keys)
    draw_player_or_ai(screen, k.get_ai_or_player())


def draw_controller(screen, key_bits):
    #up
    if key_bits[0] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, 200, 40, 40))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, 200, 40, 40), 3)
    #down
    if key_bits[1] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, 300, 40, 40))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, 300, 40, 40), 3)
    #left
    if key_bits[2] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 250, 40, 40))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 250, 40, 40), 3)
    #right
    if key_bits[3] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(150, 250, 40, 40))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(150, 250, 40, 40), 3)

    # x
    if key_bits[7] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 200, 40, 40))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 200, 40, 40), 3)
    # b
    if key_bits[4] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 300, 40, 40))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 300, 40, 40), 3)
    # y
    if key_bits[6] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(450, 250, 40, 40))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(450, 250, 40, 40), 3)
    # a
    if key_bits[5] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(550, 250, 40, 40))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(550, 250, 40, 40), 3)

    if key_bits[8] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 100, 140, 30))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 100, 140, 30), 3)

    if key_bits[9] == 1:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(450, 100, 140, 30))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(450, 100, 140, 30), 3)


def draw_player_or_ai(screen, key):
    rect = pygame.Rect(270, 300, 80, 80)

    if key:
        pygame.draw.rect(screen, (0, 255, 0), rect)
    else:
        pygame.draw.rect(screen, (255, 0, 0), rect)


if __name__ == '__main__':
    init()
