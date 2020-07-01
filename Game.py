import sys
import math

import pygame

import map.tile as tiles
import input_manager
import map.zone as zone

pygame.init()
Clock = pygame.time.Clock()

target_framerate = 60
target_frametime = math.floor(1000 / target_framerate)

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

print('found ', pygame.joystick.get_count(), 'joystick(s)')
input_manager = input_manager.manager

current_zone = zone.Zone(None)


player_pos = player_x, player_y = 64, 64

while 1:
    last_frame_mil = Clock.tick(target_framerate)
    global_timer = pygame.time.get_ticks()
    input_manager.update_keys()

    if input_manager.MOV_RIGHT:
        player_x = player_x + 2
    if input_manager.MOV_DOWN:
        player_y = player_y + 2
    if input_manager.MOV_UP:
        player_y = player_y - 2
    if input_manager.MOV_LEFT:
        player_x = player_x - 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    current_zone.draw(screen, 0, 0, global_timer)

    tiles.forest_tiles.dirt.draw(player_x, player_y, tiles.Tile_Meta(0, 0, 0), screen)
    pygame.display.flip()
