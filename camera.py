import pygame


class CameraClass(pygame.sprite.Group):
    def __init__(self):
        self.displaySurface = pygame.display.get_surface()
        self.halfWidth = self.displaySurface.get_size()[0] // 2
        self.halfHeight = self.displaySurface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)

    def customDraw(self):
        self.offset.x = player.rect.centerx - screen.get_width() // 2
        self.offset.y = player.rect.centery - screen.get_height() // 2

        for sprite in playerGroup:
            offset_pos = sprite.rect.topleft + self.offset
            self.displaySurface.blit(sprite.image, offset_pos)
            playerGroup.draw(screen)