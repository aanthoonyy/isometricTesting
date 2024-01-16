import pygame
import math
class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        grass_img = pygame.image.load('grass.png').convert()
        grass_img = pygame.transform.scale(grass_img, (20 * 5, 24 * 5))
        grass_img.set_colorkey((0, 0, 0))
        self.image = grass_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Store the isometric coordinates of the grass block
        self.isometric_x, self.isometric_y = cartesianToIsometric(pygame.math.Vector2(x, y))
        print(self.isometric_x, self.isometric_y)
    def remove(self):
        self.kill()

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
    pygame.display.update()


def delete_tile(grassGroup, mouse_x, mouse_y):
    clicked_grass = get_clicked_tile(mouse_x, mouse_y, grassGroup)
    if clicked_grass:

        clicked_grass.remove()



def point_in_triangle(p, p0, p1, p2):
    # Calculate barycentric coordinates
    denom = (p1[1] - p2[1]) * (p0[0] - p2[0]) + (p2[0] - p1[0]) * (p0[1] - p2[1])
    a = ((p1[1] - p2[1]) * (p[0] - p2[0]) + (p2[0] - p1[0]) * (p[1] - p2[1])) / denom
    b = ((p2[1] - p0[1]) * (p[0] - p2[0]) + (p0[0] - p2[0]) * (p[1] - p2[1])) / denom
    c = 1 - a - b

    # Check if point is inside the triangle
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1
def is_point_in_triangle(p, p0, p1, p2):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    d1 = sign(p, p0, p1)
    d2 = sign(p, p1, p2)
    d3 = sign(p, p2, p0)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


def get_clicked_tile(mouse_x, mouse_y, grassGroup):
    for grass in grassGroup.sprites():
        tile_rect = grass.rect
        p0 = (tile_rect.left, tile_rect.top + tile_rect.height // 2)
        p1 = (tile_rect.left + tile_rect.width // 2, tile_rect.top)
        p2 = (tile_rect.right, tile_rect.top + tile_rect.height // 2)


        if is_point_in_triangle((mouse_x, mouse_y), p0, p1, p2):
            print("printing grass", grass)
            return grass
    return None




def updateTile(map_data, grassGroup, screen, x, y):
    if 0 <= x < len(map_data) and 0 <= y < len(map_data[0]):
        # Update the map_data with the new value (0 in this case)
        map_data[x][y] = 0

        # Find the corresponding Grass sprite in grassGroup and remove it
        for grass in grassGroup.sprites():
            if grass.isometric_x == x and grass.isometric_y == y:
                grass.kill()  # Remove the existing Grass sprite
                break


def cartesianToIsometric(cartesian):
    iso_x = (cartesian.x - cartesian.y) * 50
    iso_y = (cartesian.x + cartesian.y) * 25
    return pygame.math.Vector2(iso_x, iso_y)



