import sys
import os
from pygame.math import Vector2


def resourcePath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.getcwd())
    return os.path.join(base_path, "assets", relative_path)


GAME_TITLE = "Jogo da Cobrinha"
FPS = 60
# SCREEN SIZE
CELL_SIZE = 40
CELL_NUMBER = 20
DISPLAY_SIZE = (CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER)

# SNAKE MOVIMENTS
SNAKE_UP = Vector2(0, -1)
SNAKE_DOWN = Vector2(0, 1)
SNAKE_LEFT = Vector2(-1, 0)
SNAKE_RIGHT = Vector2(1, 0)

# PATH ASSETS
PATH_FONT = resourcePath("Fonts/IHATCS__.TTF")
PATH_GRAPHIC_APPLE = resourcePath("Graphics/apple.png")
PATH_GRAPHIC_PAUSE = resourcePath("Graphics/pause.png")
PATH_GRAPHIC_BACKGROUND = resourcePath("Graphics/background.jpg")
PATH_GRAPHIC_LOGO = resourcePath("Graphics/snake-logo.png")
