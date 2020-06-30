import sys
import pygame
import math
import Tile
import Input_Manager

pygame.init()
Clock = pygame.time.Clock()

target_framerate = 60
target_frametime = math.floor(1000 / target_framerate)

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

print('found ', pygame.joystick.get_count(), 'joystick(s)')
input_manager = Input_Manager.manager

map = []
for x in range(20):
    column = []
    for y in range(15):
        column.append(Tile.randGrass())
    map.append(column)

player_pos = player_x, player_y = 0, 0

while 1:
    last_frame_mil = Clock.tick(60)
    input_manager.update_keys()

    if input_manager.MOV_RIGHT:
        player_x = player_x + 1
    if input_manager.MOV_DOWN:
        player_y = player_y + 1
    if input_manager.MOV_UP:
        player_y = player_y - 1
    if input_manager.MOV_LEFT:
        player_x = player_x - 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    for x in range(20):
        for y in range(15):
            screen.blit(map[x][y].surface, (32*x, 32*y))

    screen.blit(Tile.dirt.surface, (player_x, player_y))
    pygame.display.flip()
