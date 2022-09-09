import pygame
import random
from pygame.math import Vector2

from colors import Colors
from global_var import CELL_SIZE, CELL_NUMBER, SNAKE_RIGHT, SNAKE_DOWN, SNAKE_UP, SNAKE_LEFT


class Fruit:
    def __init__(self, display):
        self.pos = None
        self.y = None
        self.x = None
        self.display = display

        self.apple_image = pygame.image.load('Graphics/apple.png')
        self.apple_image = pygame.transform.scale(self.apple_image, (CELL_SIZE, CELL_SIZE))
        self.randomized()

    def draw(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        self.display.blit(self.apple_image, fruit_rect)

    def randomized(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)


class Snake:
    def __init__(self, display, fruit, game_over):
        super().__init__()
        self.display = display
        self.game_over = game_over

        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = SNAKE_RIGHT
        self.fruit = fruit
        self.new_block = False

    def draw(self):
        for block in self.body:
            # create rectangle
            snake_rect = pygame.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.display, Colors.WHITE, snake_rect)

    def move(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

        self.update()

    def screen_collision(self):
        if self.body[0].x < 0:
            print("colisao")

    def commands(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.direction != SNAKE_DOWN:
            self.direction = SNAKE_UP
        elif pressed[pygame.K_DOWN] and self.direction != SNAKE_UP:
            self.direction = SNAKE_DOWN
        elif pressed[pygame.K_LEFT] and self.direction != SNAKE_RIGHT:
            self.direction = SNAKE_LEFT
        elif pressed[pygame.K_RIGHT] and self.direction != SNAKE_LEFT:
            self.direction = SNAKE_RIGHT

    def eat(self):
        if self.body[0] == self.fruit.pos:
            self.fruit.randomized()
            self.add_block()

    def self_eat(self):
        if self.body[0] in self.body[1:]:
            self.game_over()

    def add_block(self):
        self.new_block = True

    def update(self):
        self.commands()
        self.screen_collision()
        self.self_eat()
        self.eat()
