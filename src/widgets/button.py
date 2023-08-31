import pygame

from src.config import Colors
from src.config.global_var import PATH_FONT


class Button:
    def __init__(self, display, text, width, height, pos, elevation, target):
        self.display = display

        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.target = target

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = Colors.BLUE

        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = (75, 145, 50)

        game_font = pygame.font.Font(PATH_FONT, 40)

        self.text_surf = game_font.render(text, True, Colors.WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.display, self.bottom_color,
                         self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.display, self.top_color,
                         self.top_rect, border_radius=12)
        self.display.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (75, 145, 50)
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    self.target()
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = Colors.GREEN
