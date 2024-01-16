import pygame, sys, time, random
from pygame.locals import *

import grassClass
from playerClass import Player
from grassClass import *
from selectionBoxClass import *
from camera import *
pygame.init()

clock = pygame.time.Clock()
#setup
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
display = pygame.Surface((1920, 1080))

#set mouse visible
pygame.mouse.set_visible(True)
#read map file
f = open('map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()
columns, rows = len(map_data[0]), len(map_data)
print(columns, rows) #put into rows and collums

# group stuff
grassGroup = pygame.sprite.Group()

player = Player()
playerGroup = pygame.sprite.Group()
playerGroup.add(player)
selection_box = SelectionBox()

load_map(map_data, grassGroup, screen) # load the map

#general variables
clicked_grass = None
tile_width = 20
tile_height = 24
isometric_size = tile_width
x_axis = pygame.math.Vector2(tile_width, 0)
y_axis = pygame.math.Vector2(0, tile_height)
origin = pygame.math.Vector2(columns * isometric_size / 2, columns * isometric_size / 4)
point_to_grid = inverseMat2x2(x_axis, y_axis)
tile_size = (tile_width, tile_height)
map_width = columns * isometric_size
map_height = rows * isometric_size // 2
map_rect = pygame.Rect(0, 0, map_width, map_height)
camera = Camera(1920, 1080)

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                delete_tile(grassGroup, mouse_x, mouse_y)

    camera.update(player)
    screen.fill((0, 0, 0))
    #screen.blit(display, (0, 0))
    for grass in grassGroup:
        screen.blit(grass.image, camera.apply(grass))

    #grassGroup.draw(screen)

    player.update()
    playerGroup.update()


    #playerGroup.draw(screen)
    for player in playerGroup:
        screen.blit(player.image, camera.apply(player))
    mouse_x, mouse_y = pygame.mouse.get_pos()



    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)



