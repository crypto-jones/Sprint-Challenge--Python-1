import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *
# from paddle import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE,
                       Vector2(random.randint(
                           20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                       Vector2(6, -6),
                       [255, 10, 0], 10)
    object_list.append(kinetic)

    block = BreakableBlock(Vector2(200, 200), 100, 100, [0, 0, 255])
    object_list.append(block)

    paddle = Paddle(
        Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1] - 50), 100, 25, [128, 128, 128])
    object_list.append(paddle)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_objects(object_list)

    while len(object_list) > 2:  # TODO:  Create more elegant condition for loop
        left = False
        right = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # Do something
            left = True
            pass
        if keys[pygame.K_RIGHT]:
            # Do something
            right = True
            pass

        for object in object_list:
            object.update(left=left, right=right, pygame=pygame)
            object.check_collision()

        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
