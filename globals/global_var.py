from pygame.math import Vector2

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

#PATH ASSETS
PATH_FONT = "assets/Fonts/IHATCS__.TTF"
PATH_GRAPHIC_APPLE = "assets/Graphics/apple.png"
PATH_GRAPHIC_PAUSE = "assets/Graphics/pause.png"