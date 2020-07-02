import math

import graphics.image_store as image_store


class Tile_Meta(object):
    def __init__(self, map_x, map_y, variant):
        self.map_x = map_x
        self.map_y = map_y
        self.variant = variant


class Simple_Tile(object):

    def __init__(self, image_surfaces, walkable):
        self._surfaces = image_surfaces
        self.walkable = walkable

    def draw(self, level_x_offset, level_y_offset, meta, dest_surface):
        dest_surface.blit(self._surfaces[meta.variant], self.calculate_offset(meta, level_x_offset, level_y_offset))

    def count_variants(self):
        return len(self._surfaces)

    def calculate_offset(self, meta, level_x, level_y):
        return ((16 * meta.map_x) + level_x, (16 * meta.map_y) + level_y)


class Layered_Tile(Simple_Tile):

    def __init__(self, surface_layers, walkable):
        self.walkable = walkable
        self._surface_layers = surface_layers

    def draw(self, level_x_offset, level_y_offset, meta, dest_surface):
        variant_remainder = meta.variant
        for layer_surfaces in self._surface_layers:
            selector = variant_remainder % len(layer_surfaces)
            variant_remainder = math.floor((variant_remainder - selector) / len(layer_surfaces))
            dest_surface.blit(layer_surfaces[selector], self.calculate_offset(meta, level_x_offset, level_y_offset))

    def count_variants(self):
        count = 1
        for layer_surfaces in self._surface_layers:
            count = count * len(layer_surfaces)
        return count


class forest_tiles(object):
    grass = Simple_Tile([image_store.forest_bg_tiles.get_sprite(5, 2),
                         image_store.forest_bg_tiles.get_sprite(6, 2),
                         image_store.forest_bg_tiles.get_sprite(7, 2),
                         image_store.forest_bg_tiles.get_sprite(8, 2)],
                        True)
    dirt = Simple_Tile([image_store.forest_bg_tiles.get_sprite(1, 1),
                        image_store.forest_bg_tiles.get_sprite(7, 0),
                        image_store.forest_bg_tiles.get_sprite(7, 1),
                        image_store.forest_bg_tiles.get_sprite(8, 0),
                        image_store.forest_bg_tiles.get_sprite(8, 1)],
                       True)
    left_cliff_grass = Layered_Tile([grass._surfaces,
                                    [image_store.forest_bg_tiles.get_sprite(15, 1),
                                     image_store.forest_bg_tiles.get_sprite(15, 2)]],
                                    False)
    left_cliff_dirt = Layered_Tile([dirt._surfaces,
                                    [image_store.forest_bg_tiles.get_sprite(15, 1),
                                     image_store.forest_bg_tiles.get_sprite(15, 2)]],
                                   False)

    rock = Simple_Tile([image_store.forest_bg_tiles.get_sprite(0, 5)], False)
