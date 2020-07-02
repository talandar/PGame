import math

import pygame

import map.tile as tiles


class Player(object):

    def __init__(self, init_pos):
        self._health = 3
        self._position = init_pos
        self._size = 12
        self._calc_hitbox()

    def move(self, movement, blocking_rects):
        if not math.isclose(movement.x, 0, abs_tol=1e-5):
            self.move_single_axis(movement.x, 0, blocking_rects)
        if not math.isclose(movement.y, 0, abs_tol=1e-5):
            self.move_single_axis(0, movement.y, blocking_rects)
        self._calc_hitbox()

    def hitbox(self):
        return self._hitbox

    def draw(self, screen):
        tiles.forest_tiles.dirt.draw(self._position.x, self._position.y, tiles.Tile_Meta(0, 0, 0), screen)

    def get_speed(self):
        return 1

    def get_position(self):
        return self._position

    def _calc_hitbox(self):
        self._hitbox = pygame.rect.Rect(self._position, (self._size, self._size))
        return self._hitbox

    def move_single_axis(self, dx, dy, blocking_rects):
        self._position.x += dx
        self._position.y += dy
        hitbox = self._calc_hitbox()

        # If you collide with a wall, move out based on velocity
        for wall in blocking_rects:
            if hitbox.colliderect(wall):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self._position.x = wall.left - self._size
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self._position.x = wall.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self._position.y = wall.top - self._size
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self._position.y = wall.bottom
