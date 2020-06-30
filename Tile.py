import Image_Store
import random


class Tile(object):

    def __init__(self, image_surface, walkable):
        self.surface = image_surface
        self.walkable = walkable


def randGrass():
    return grass[random.randrange(4)]


grass0 = Tile(Image_Store.forest_bg_tiles.get_sprite(5, 2), True)
grass1 = Tile(Image_Store.forest_bg_tiles.get_sprite(6, 2), True)
grass2 = Tile(Image_Store.forest_bg_tiles.get_sprite(7, 2), True)
grass3 = Tile(Image_Store.forest_bg_tiles.get_sprite(8, 2), True)
grass = [grass0, grass1, grass2, grass3]

dirt = Tile(Image_Store.forest_bg_tiles.get_sprite(1, 1), True)