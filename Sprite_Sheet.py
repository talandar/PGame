import pygame.image
import pygame


class Sprite_Sheet(object):

    """Sprite Sheet is a set of square images in a grid.  This class stores
    the full grid, allowing sub-images to be extracted."""

    def __init__(self, path, tile_size):
        self.path = path
        self.tile_size = tile_size
        self.surface = pygame.image.load(path)
        self.tiles_x = self.surface.get_width() / tile_size
        self.tiles_y = self.surface.get_height() / tile_size
        print("loaded ", self.path, " with ", self.tiles_x, "x", self.tiles_y,
              " tiles of size", self.tile_size)

    def get_sprite(self, x, y):
        if x < 0 | y < 0 | x >= self.tiles_x | y >= self.tiles_y:
            print("invalid tile selection: asked for (", x, ", ", y,
                  "), max tile is (", self.tiles_x, ", ", self.tiles_y, ").")
            return None
        bounding_rect = pygame.rect.Rect(self.tile_size*x, self.tile_size*y,
                                         self.tile_size, self.tile_size)
        tile = self.surface.subsurface(bounding_rect)
        return pygame.transform.scale(tile, (32, 32))
