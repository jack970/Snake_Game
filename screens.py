from global_var import CELL_SIZE, CELL_NUMBER
from widgets import Button, Text
from colors import Colors


class Screens:
    def __init__(self, display, main):
        self.display = display
        self.main = main

        self.title_x = (CELL_SIZE * CELL_NUMBER // 2)
        self.title_y = (CELL_SIZE * CELL_NUMBER // 6)

        self.start_game_button = Button(
            self.display, "Iniciar",
            self.title_x, self.title_y // 2,
            (200, 250), 6, lambda: self.main.run_game())

        self.start_new_game_btn = Button(
            self.display, "Novo Jogo",
            self.title_x, self.title_y // 2,
            (200, 250), 6, lambda: self.main.reset())

        self.quit_button = Button(
            self.display, "Sair",
            self.title_x, self.title_y // 2,
            (200, self.title_y * 3), 6, lambda: self.main.quit_())

    def home_screen(self):
        self.display.fill(Colors.WHITE)

        # título
        title = Text(self.display, "Snake Game", (self.title_x, self.title_y), color=Colors.BLACK, size=40)
        title.draw()

        self.start_game_button.draw()

        self.quit_button.draw()

    def game_over_screen(self):
        self.display.fill(Colors.WHITE)

        title = Text(self.display, "Game Over", (self.title_x, self.title_y), color=Colors.RED, size=40)
        title.draw()

        self.start_new_game_btn.draw()
        self.quit_button.draw()
