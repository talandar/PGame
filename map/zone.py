import random

import pygame

import map.tile as tiles


class Zone(object):

    def __init__(self, zone_data):
        self._map = []
        self._all_tiles = []
        self._unwalkable = []
        self._zone_x_offset = 0
        self._zone_y_offset = 0

        self._load_map(zone_data)
        for column in self._map:
            for tile_data in column:
                self._all_tiles.append(tile_data)
                tile_type = tile_data[0]
                tile_meta = tile_data[1]
                if not tile_type.walkable:
                    self._unwalkable.append(tile_meta)

    def _load_map(self, zone_data):
        for x in range(20):
            column = []
            for y in range(15):
                if x == 0:
                    tile = tiles.forest_tiles.left_cliff_grass
                    column.append([tile,
                                   tiles.Tile_Meta(x,
                                                   y,
                                                   random.randint(0, tile.count_variants()-1))])
                else:
                    tile = tiles.forest_tiles.grass
                    column.append([tile,
                                   tiles.Tile_Meta(x,
                                                   y,
                                                   random.randint(0, tile.count_variants()-1))])
            self._map.append(column)
        self._map[10][7] = [tiles.forest_tiles.rock, tiles.Tile_Meta(10, 7, 0)]

    def draw(self, screen, x_offset, y_offset, animation_timer):
        for x in range(20):
            for y in range(15):
                self._map[x][y][0].draw(self._zone_x_offset + x_offset,
                                        self._zone_y_offset + y_offset,
                                        self._map[x][y][1],  # meta
                                        screen)

    def get_unwalkable_rects(self):
        rects = []
        for tile_meta in self._unwalkable:
            rects.append(pygame.rect.Rect((16*tile_meta.map_x, 16*tile_meta.map_y), (16, 16)))
        return rects
