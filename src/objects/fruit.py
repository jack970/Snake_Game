import random

import pygame
from pygame.math import Vector2

from src.config import CELL_SIZE, CELL_NUMBER, PATH_GRAPHIC_APPLE


class Fruit:
    def __init__(self, display):
        self.pos = None
        self.y = None
        self.x = None
        self.display = display

        self.apple_image = pygame.image.load(PATH_GRAPHIC_APPLE)
        self.apple_image = pygame.transform.scale(
            self.apple_image, (CELL_SIZE, CELL_SIZE))
        self.randomized()

    def draw(self):
        if self.pos:
            fruit_rect = pygame.Rect(
                int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
            self.display.blit(self.apple_image, fruit_rect)

    def randomized(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
