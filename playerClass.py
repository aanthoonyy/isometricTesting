import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        vec = pygame.math.Vector2

        original_image = pygame.image.load("knight.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (450, 450)
        self.pos = vec(450, 450)
        self.speed = 0.1

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:

            self.pos += (0, 10)
        if keys[pygame.K_d]:
            self.pos += (0, -10)

        if keys[pygame.K_w]:
            self.pos += (-10, 0)

        if keys[pygame.K_s]:
            self.pos += (10, 0)




        self.rect.center = cartesianToIsometric(self.pos)

def cartesianToIsometric(cartesian):
    iso_x = cartesian.x - cartesian.y
    iso_y = cartesian.x / 2 + cartesian.y / 2
    return pygame.math.Vector2(iso_x, iso_y)
