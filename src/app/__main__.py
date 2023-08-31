import sys
import pygame
from src.widgets import Button, Text
from src.config.global_var import *
from src.config import Colors
from src.game import Game
from src.screens import Screens


class App:
    def __init__(self):
        pygame.init()

        self.running = False
        self.paused = False

        pygame.display.set_caption(GAME_TITLE)
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
            self.screens.game_over_screen(score)
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
