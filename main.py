import pygame, sys, time, random
from pygame.locals import *
from playerClass import Player
from camera import Camera

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('game base')
screen = pygame.display.set_mode((900, 900), RESIZABLE)
display = pygame.Surface((300, 300))

grass_img = pygame.image.load('grass.png').convert()
#grass_img = pygame.transform.scale(grass_img, (10, 10))
grass_img.set_colorkey((0, 0, 0))

f = open('map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

player = Player()
playerGroup = pygame.sprite.Group(player)
frames = 0
start_time = 0

while True:
    display.fill((0, 0, 0))
    clock.tick(60)
    dt = clock.get_time() / 1000.0

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

    playerGroup.draw(screen)
    playerGroup.update(dt)

    pygame.display.update()
