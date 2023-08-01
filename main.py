import pygame, sys, time, random
from pygame.locals import *
from playerClass import Player
from grassClass import *
pygame.init()



clock = pygame.time.Clock()

pygame.display.set_caption('game base')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
display = pygame.Surface((1920, 1080))

f = open('map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

grassGroup = pygame.sprite.Group()

player = Player()
playerGroup = pygame.sprite.Group()
playerGroup.add(player)

load_map(map_data, grassGroup, screen)
while True:
    dt = clock.get_time() / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_tile = get_clicked_tile(mouse_x, mouse_y, map_data, screen)
                if clicked_tile is not None:
                    print("Clicked Tile:", clicked_tile)
                    load_map(map_data, grassGroup, screen)
    screen.fill((0, 0, 0))
    screen.blit(display, (0, 0))


    grassGroup.draw(screen)

    player.update()
    playerGroup.update()


    playerGroup.draw(screen)

    pygame.display.update()
    #print("Player Position:", player.pos)

    clock.tick(60)



