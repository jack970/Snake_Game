import pygame
from pygame.math import Vector2
from src.config import *


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
            if self.body[0] == block:
                snake_rect = pygame.Rect(
                    int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.display, Colors.BLACK, snake_rect)
            else:
                snake_rect = pygame.Rect(
                    int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
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

    def commands(self):
        pressed = pygame.key.get_pressed()

        k_up, k_down, k_left, k_right = pressed[KEY_UP], pressed[KEY_DOWN], pressed[KEY_LEFT], pressed[KEY_RIGHT]

        k_w, k_s, k_a, k_d = pressed[KEY_W], pressed[KEY_S], pressed[KEY_A], pressed[KEY_D]

        if (k_up or k_w) and self.direction != SNAKE_DOWN:
            self.direction = SNAKE_UP

        elif (k_down or k_s) and self.direction != SNAKE_UP:
            self.direction = SNAKE_DOWN

        elif (k_left or k_a) and self.direction != SNAKE_RIGHT:
            self.direction = SNAKE_LEFT

        elif (k_right or k_d) and self.direction != SNAKE_LEFT:
            self.direction = SNAKE_RIGHT

    def eat(self):
        if self.body[0] == self.fruit.pos:
            self.fruit.randomized()
            self.add_block()

    def screen_collision(self):
        snake_x = self.body[0].x
        snake_y = self.body[0].y

        if snake_x < 0 or snake_x >= CELL_NUMBER or snake_y >= CELL_NUMBER or snake_y < 0:
            self.game_over()

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
