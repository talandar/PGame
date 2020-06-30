import sys
import pygame
import math
import Tile

pygame.init()
Clock = pygame.time.Clock()

target_framerate = 60
target_frametime = math.floor(1000 / target_framerate)

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

print('found ', pygame.joystick.get_count(), 'joystick(s)')

map = []
for x in range(20):
    column = []
    for y in range(15):
        column.append(Tile.randGrass())
    map.append(column)

while 1:
    last_frame_mil = Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    for x in range(20):
        for y in range(15):
            screen.blit(map[x][y].surface, (32*x, 32*y))
    pygame.display.flip()
