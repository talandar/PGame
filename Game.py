import sys
import math

import pygame

import input_manager
import map.zone as zone
import player

pygame.init()
Clock = pygame.time.Clock()

max_framerate = 240

draw_size = width, height = 320, 240
window_size = window_width, window_height = 640, 480
draw_ratio = width / height
draw_scale_width, draw_scale_height = 1, 1
draw_translate_x, draw_translate_y = 0, 0
black = 0, 0, 0

# these two lines get a screen of draw_size, to get something to draw on without needing to scale 16x16
# sized tiles.
display_screen = pygame.display.set_mode(draw_size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
draw_screen = display_screen.copy()

# re-init display_screen to size based on monitor, etc
display_screen = pygame.display.set_mode(window_size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

print('found ', pygame.joystick.get_count(), 'joystick(s)')
input_manager = input_manager.manager

current_zone = zone.Zone(None)

character = player.Player(pygame.Vector2(64, 64))

while 1:
    last_frame_mil = Clock.tick(240)
    global_timer = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            display_screen = pygame.display.set_mode(event.dict['size'],
                                                     pygame.HWSURFACE |
                                                     pygame.DOUBLEBUF |
                                                     pygame.RESIZABLE)
            current_ratio = display_screen.get_width() / display_screen.get_height()
            if current_ratio > draw_ratio:
                # black bars left and right
                draw_translate_y = 0
                draw_scale_height = display_screen.get_height()
                draw_scale_width = math.floor(draw_scale_height * draw_ratio)
                draw_translate_x = (display_screen.get_width() - draw_scale_width) / 2
            else:
                # black bars top and bottom
                draw_translate_x = 0
                draw_scale_width = display_screen.get_width()
                draw_scale_height = math.floor(draw_scale_width / draw_ratio)
                draw_translate_y = (display_screen.get_height() - draw_scale_height) / 2

    input_manager.update_keys()

    """block: player movement and level collision."""
    player_mov_vector = pygame.Vector2(0, 0)
    if input_manager.MOV_RIGHT:
        player_mov_vector.x += 1
    if input_manager.MOV_DOWN:
        player_mov_vector.y += 1
    if input_manager.MOV_UP:
        player_mov_vector.y -= 1
    if input_manager.MOV_LEFT:
        player_mov_vector.x -= 1

    if player_mov_vector.magnitude_squared() > 0:
        player_mov_vector.scale_to_length(character.get_speed())
        character.move(player_mov_vector, current_zone.get_unwalkable_rects())
    """end player movement/level collision block"""

    draw_screen.fill(black)
    current_zone.draw(draw_screen, 0, 0, global_timer)

    character.draw(draw_screen)

    # handle scaling and drawing game
    display_screen.blit(pygame.transform.scale(draw_screen, (draw_scale_width, draw_scale_height)),
                        (draw_translate_x, draw_translate_y))
    pygame.display.flip()
