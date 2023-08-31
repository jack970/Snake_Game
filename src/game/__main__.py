import pygame

from src.config import Colors
from src.config.global_var import *
from src.objects import Fruit, Snake
from src.widgets import Text


class Game:
    def __init__(self, display, main):
        self.display = display
        self.main_app = main

        self.game_font = pygame.font.Font(PATH_FONT, 30)
        self.menu_pressed = False

        self.pause_img = pygame.image.load(PATH_GRAPHIC_PAUSE)
        self.pause_img = pygame.transform.scale(
            self.pause_img, (CELL_SIZE, CELL_SIZE))

        self.fruit = Fruit(self.display)
        self.snake = Snake(self.display, self.fruit,
                           lambda: self.main_app.run_game_over())

    def draw_grass(self):
        for x in range(CELL_NUMBER):
            if x % 2 == 0:
                for y in range(CELL_NUMBER):
                    if y % 2 == 0:
                        grass_rect = pygame.Rect(
                            y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(
                            self.display, Colors.GREEN_DARK, grass_rect)
            else:
                for yy in range(CELL_NUMBER):
                    if yy % 2 != 0:
                        grass_rect = pygame.Rect(
                            yy * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(
                            self.display, Colors.GREEN_DARK, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_x = int(CELL_SIZE * CELL_NUMBER - 60)
        score_y = int(CELL_SIZE * CELL_NUMBER - 40)
        pos = (score_x, score_y)
        Text(self.display, f"Pontos {score_text}",
             pos, color=(56, 74, 12)).draw()

    def draw_menu_button(self):
        menu_x = int(CELL_SIZE * 18 - 20)
        menu_y = int(CELL_SIZE)
        menu_rect = pygame.Rect(int(menu_x), int(menu_y), CELL_SIZE, CELL_SIZE)
        self.display.blit(self.pause_img, menu_rect)

        mouse_pos = pygame.mouse.get_pos()
        if menu_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.menu_pressed = True
            else:
                if self.menu_pressed:
                    self.main_app.run_pause()
                    self.menu_pressed = False
        else:
            pass

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw()
        self.fruit.draw()
        self.draw_score()
        self.draw_menu_button()

    def update(self):
        self.snake.move()
