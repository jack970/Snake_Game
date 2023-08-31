import pygame

from ..config import Colors
from ..config.global_var import PATH_FONT


class Text:
    def __init__(self, display, text, pos, size=30, color=Colors.BLACK):
        self.game_font = pygame.font.Font(PATH_FONT, size)
        self.display = display
        self.text = text
        self.color = color
        self.pos = pos

    def draw(self):
        surface = self.game_font.render(self.text, True, self.color)
        rect = surface.get_rect(center=self.pos)
        self.display.blit(surface, rect)
