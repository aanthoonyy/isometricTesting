import pygame

class Camera:
    def __init__(self, player_pos, screen_width, screen_height):
        self.camera = pygame.math.Vector2(player_pos.x, player_pos.y)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def apply(self, entity):
        return entity.rect.move(-self.camera.x + self.screen_width / 2, -self.camera.y + self.screen_height / 2)

    def update(self, player_pos):
        self.camera.x = player_pos.x
        self.camera.y = player_pos.y
