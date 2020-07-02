import pygame.image
import pygame


class Sprite_Sheet(object):

    """Sprite Sheet is a set of square images in a grid.  This class stores
    the full grid, allowing sub-images to be extracted.  Sprites are of size 16x16"""

    def __init__(self, path):
        self.path = path
        self.input_size = 16
        self.surface = pygame.image.load(path)
        self.tiles_x = self.surface.get_width() / self.input_size
        self.tiles_y = self.surface.get_height() / self.input_size
        print("loaded ", self.path, " with ", self.tiles_x, "x", self.tiles_y,
              " tiles of size", self.input_size)

    def get_sprite(self, x, y):
        if x < 0 | y < 0 | x >= self.tiles_x | y >= self.tiles_y:
            print("invalid tile selection: asked for (", x, ", ", y,
                  "), max tile is (", self.tiles_x, ", ", self.tiles_y, ").")
            return None
        bounding_rect = pygame.rect.Rect(self.input_size*x, self.input_size*y,
                                         self.input_size, self.input_size)
        tile = self.surface.subsurface(bounding_rect)
        return tile
