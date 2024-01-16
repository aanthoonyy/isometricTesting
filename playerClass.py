import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        vec = pygame.math.Vector2

        original_image = pygame.image.load("knight.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (1570, 360)
        self.pos = vec(1570, 360)
        self.speed = 0.1
        self.velocity = vec(20, 20)
        self.camera_offset_x = 0
        self.camera_offset_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.pos += (0, 1)
        if keys[pygame.K_d]:
            self.pos += (0, -1)
        if keys[pygame.K_w]:
            self.pos += (-1, 0)
        if keys[pygame.K_s]:
            self.pos += (1, 0)

        self.rect.center = cartesianToIsometric(self.pos)
        self.camera_offset_x = -self.rect.x + (1920 // 2)
        self.camera_offset_y = -self.rect.y + (1080 // 2)

def draw_crosshair(window, position, tile_size):
    crosshair_color = (255, 255, 255)
    crosshair_width = 2

    crosshair_rect = pygame.Rect(position[0] - tile_size[0] // 4, position[1], tile_size[0] // 2, tile_size[1])
    pygame.draw.rect(window, crosshair_color, crosshair_rect, crosshair_width)

    crosshair_rect = pygame.Rect(position[0], position[1] - tile_size[1] // 4, tile_size[0], tile_size[1] // 2)
    pygame.draw.rect(window, crosshair_color, crosshair_rect, crosshair_width)



def cartesianToIsometric(cartesian):
    iso_x = cartesian.x - cartesian.y
    iso_y = cartesian.x / 2 + cartesian.y / 2
    return pygame.math.Vector2(iso_x, iso_y)

