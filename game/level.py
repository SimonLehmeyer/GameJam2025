"""Simple tile-based level layout for the Balance prototype."""

import os
import pygame
import pytmx


TILE_SIZE = 40
MAP_ROWS = 16
MAP_COLS = 100
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")


def _image_loader(filename, colorkey, **kwargs):
    """Load tile images, providing a gray fallback if missing."""
    path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(path):
        return pygame.image.load(path).convert_alpha()
    img = pygame.Surface((TILE_SIZE, TILE_SIZE))
    img.fill((130, 130, 130))
    return img


class Level:
    """Tilemap driven collection of platforms for the demo level."""

    def __init__(self, map_file=os.path.join(ASSETS_DIR, "level1.tmx")):
        """Load the tilemap from ``map_file`` and build collision rectangles."""
        self.map_file = map_file
        self._load_map()

    def _load_map(self):
        loader = lambda fname, colorkey, **_: _image_loader(fname, colorkey)
        self.tmx = pytmx.util_pygame.load_pygame(self.map_file, pixelalpha=True, image_loader=loader)

        assert self.tmx.width == MAP_COLS and self.tmx.height == MAP_ROWS, (
            f"Map must be {MAP_ROWS}x{MAP_COLS}")

        self.surface = pygame.Surface(
            (self.tmx.width * self.tmx.tilewidth, self.tmx.height * self.tmx.tileheight),
            pygame.SRCALPHA,
        )
        self.platforms = []
        for layer in self.tmx.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmx.get_tile_image_by_gid(gid)
                    if tile:
                        self.surface.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))
                        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                        self.platforms.append(rect)

    def reset(self):
        """Reload the map so external edits show up immediately."""
        self._load_map()

    @property
    def width(self):
        return self.surface.get_width()

    def draw(self, surface, offset_x=0):
        """Draw the map to the screen applying a horizontal offset."""
        surface.blit(self.surface, (-offset_x, 0))


