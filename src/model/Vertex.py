import pygame
from .GraphObject import *


def render_text(text, family, size, color=(0, 0, 0), aa=False):
    font = pygame.font.SysFont(family, size)
    return font.render(text, aa, color)

def near(p, center, radius):
    d2 = (p[0] - center[0])**2 + (p[1] - center[1])**2
    return d2 <= radius**2
 

class Vertex (GraphObject):
    def __init__(self, name, x, y, size=15, color=(0, 0, 0), width=1):
        self.__name, self.__name_surface = "", None
        self.set_name(name)
        self.x, self.y = x, y
        self.size, self.width, self.color = size, width, color
        self.__edges = []
        self.selected = False
        self.selection_color = (255, 0, 0)
 
    @property
    def edges(self):
        return self.__edges
 
    @property
    def name(self):
        return self.__name
 
    @property
    def pos(self):
        return self.x, self.y
 
    def set_name(self, name):
        self.__name = name
        self.__name_surface = render_text(name, "Arial", 16)
 
    def get_event(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN and near(self.pos, ev.pos, self.size):
            self.select()
        elif ev.type == pygame.MOUSEMOTION and self.selected:
            self.x, self.y = ev.pos
        elif ev.type == pygame.MOUSEBUTTONUP and self.selected:
            self.deselect()
 
    def select(self, color=(255, 0, 0)):
        self.selected = True
        self.selection_color = color
 
    def deselect(self):
        self.selected = False
 
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.size, self.width)  # draw vertex circle
        if self.__name_surface:  # draw name
            x, y, w, h = self.__name_surface.get_rect()
            surface.blit(self.__name_surface, (self.x-w//2, self.y-h//2))
        if self.selected:  # draw selection
            pygame.draw.circle(surface, self.selection_color, self.pos, self.size-self.width)
 