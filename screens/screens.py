from globals.colors import Colors
from globals.global_var import *
from screens.widgets import Button, Text
import pygame

class Screens:
    def __init__(self, display, main):
        self.display = display
        self.main = main

        self.title_x = (CELL_SIZE * CELL_NUMBER // 2)
        self.title_y = (CELL_SIZE * CELL_NUMBER // 6)

        self.start_game_button = Button(
            self.display, "Iniciar",
            self.title_x, self.title_y // 2,
            (200, (self.title_y * 2) + 50), 6, lambda: self.main.run_game())

        self.start_new_game_btn = Button(
            self.display, "Novo Jogo",
            self.title_x, self.title_y // 2,
            (200, (self.title_y * 2) + 50), 6, lambda: self.main.reset())

        self.quit_button = Button(
            self.display, "Sair",
            self.title_x, self.title_y // 2,
            (200, (self.title_y * 3) + 50), 6, lambda: self.main.quit_())
        
        self.background = self.load_background()

    def load_background(self):
        background = pygame.image.load(PATH_GRAPHIC_BACKGROUND).convert()
        background = pygame.transform.scale(background, DISPLAY_SIZE)
        background.set_alpha(150)
        
        return background
    
    def home_screen(self):
        self.display.fill(Colors.WHITE)
        self.display.blit(self.background, (0, 0))


        # logo snake
        logo_snake = pygame.image.load(PATH_GRAPHIC_LOGO)
        logo_snake = pygame.transform.scale(logo_snake, (150, 150))
        self.display.blit(logo_snake, (self.title_x - 80, self.title_y - 70))

        # título
        title = Text(self.display, "Snake Game", (self.title_x, self.title_y + 120), color=Colors.BLACK, size=60)
        title.draw()

        self.start_game_button.draw()

        self.quit_button.draw()

    def game_over_screen(self, score=10):
        self.display.fill(Colors.WHITE)
        self.display.blit(self.background, (0, 0))

        title = Text(self.display, "Game Over", (self.title_x, self.title_y), color=Colors.RED, size=40)
        title.draw()

        score = Text(self.display, f"Pontos: {score}", (self.title_x, self.title_y//2))
        score.draw()

        self.start_new_game_btn.draw()
        self.quit_button.draw()