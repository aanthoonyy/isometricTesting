import pygame

class SelectionBox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("selection.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.visible = True






def transform(p, mat2x2):
    x = p[0] * mat2x2[0][0] + p[1] * mat2x2[1][0]
    y = p[0] * mat2x2[0][1] + p[1] * mat2x2[1][1]
    return pygame.math.Vector2(x, y)

def inverseMat2x2(x_axis, y_axis):
    a, b, c, d = x_axis.x, x_axis.y, y_axis.x, y_axis.y
    det = 1 / (a * d - b * c)
    return [(d * det, -b * det), (-c * det, a * det)]

def tileRect(column, row, tile_size):
    x = (column - row) * tile_size[0] // 2
    y = (column + row) * tile_size[1] // 2
    return pygame.Rect(x, y, *tile_size)

