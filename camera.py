import pygame
import math
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.scroll = pygame.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.speed = 25
    def update(self, target):
        self.dx = -target.rect.x + self.width / 2
        self.dy = -target.rect.y + self.height / 2

    def apply(self, entity):
        return entity.rect.move(self.dx, self.dy)