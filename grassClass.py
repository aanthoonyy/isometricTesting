import pygame
class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        grass_img = pygame.image.load('grass.png').convert()
        grass_img = pygame.transform.scale(grass_img, (20 * 5, 24 * 5))
        grass_img.set_colorkey((0, 0, 0))
        self.image = grass_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


def load_map(map_data, grassGroup, screen):
    grassGroup.empty()
    map_width = len(map_data[0]) * 50
    map_height = len(map_data) * 25
    offset_x = (screen.get_width() - map_width) // 2
    offset_y = (screen.get_height() - map_height) // 2

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                grass = Grass(offset_x + x * 50 - y * 50, offset_y + x * 25 + y * 25)
                grassGroup.add(grass)

def get_clicked_tile(mouse_x, mouse_y, map_data, screen):
    map_width = len(map_data[0]) * 50
    map_height = len(map_data) * 25
    offset_x = (screen.get_width() - map_width) // 2
    offset_y = (screen.get_height() - map_height) // 2
    relative_x = mouse_x - offset_x
    relative_y = mouse_y - offset_y
    tile_x = (relative_x + 2 * relative_y) // 100
    tile_y = (2 * relative_y - relative_x) // 100

    if 0 <= tile_x < len(map_data[0]) and 0 <= tile_y < len(map_data):
        map_data[tile_y][tile_x] = 0

        return (tile_x, tile_y, map_data[tile_y][tile_x])
    else:
        return None
