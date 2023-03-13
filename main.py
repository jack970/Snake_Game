import sys

import pygame

from globals.colors import Colors
from globals.global_var import *
from objs import Fruit, Snake
from screens.screens import Screens
from screens.widgets import Button, Text


class Game:
    def __init__(self, display, main):
        self.display = display
        self.main_app = main

        self.game_font = pygame.font.Font(PATH_FONT, 30)
        self.menu_pressed = False

        self.pause_img = pygame.image.load(PATH_GRAPHIC_PAUSE)
        self.pause_img = pygame.transform.scale(self.pause_img, (CELL_SIZE, CELL_SIZE))

        self.fruit = Fruit(self.display)
        self.snake = Snake(self.display, self.fruit, lambda: self.main_app.run_game_over())

    def draw_grass(self):
        for x in range(CELL_NUMBER):
            if x % 2 == 0:
                for y in range(CELL_NUMBER):
                    if y % 2 == 0:
                        grass_rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.display, Colors.GREEN_DARK, grass_rect)
            else:
                for yy in range(CELL_NUMBER):
                    if yy % 2 != 0:
                        grass_rect = pygame.Rect(yy * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.display, Colors.GREEN_DARK, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_x = int(CELL_SIZE * CELL_NUMBER - 60)
        score_y = int(CELL_SIZE * CELL_NUMBER - 40)
        pos = (score_x, score_y)
        Text(self.display, f"Pontos {score_text}", pos, color=(56, 74, 12)).draw()

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


class App:
    def __init__(self):
        pygame.init()
        self.running = False
        self.paused = False

        self.display = pygame.display.set_mode(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()

        self.SCREEN_UPDATE = pygame.USEREVENT

        pygame.time.set_timer(self.SCREEN_UPDATE, 100)

        self.game = Game(self.display, self)
        self.screens = Screens(self.display, self)

    def run_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_()
                else:
                    pass

            self.screens.home_screen()

            pygame.display.update()
            self.clock.tick(FPS)

    def run_pause(self):
        self.paused = True

        center_x = (CELL_SIZE * CELL_NUMBER // 2)
        center_y = (CELL_SIZE * CELL_NUMBER // 6)

        title = Text(self.display, "Pause", (center_x, center_y), size=60)

        continue_btn = Button(
            self.display, "Continuar",
            center_x, center_y // 2,
            (200, center_y * 2.5), 6, lambda: self.run_game())

        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = False
                else:
                    pass

            title.draw()
            continue_btn.draw()
            pygame.display.update()
            self.clock.tick(FPS)

    def run_game_over(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_()
                else:
                    pass
            
            score = len(self.game.snake.body) - 3
            self.screens.game_over_screen(str(score))
            pygame.display.update()
            self.clock.tick(FPS)

    def run_game(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_()
                elif event.type == self.SCREEN_UPDATE:
                    self.game.update()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run_pause()
                else:
                    pass

            self.display.fill(Colors.GREEN)
            self.game.draw_elements()

            pygame.display.update()
            self.clock.tick(FPS)

    def reset(self):
        App().run_game()

    def quit_(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    app = App()
    app.run_menu()
