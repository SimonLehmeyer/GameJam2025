"""Simple tile-based level layout for the Balance prototype."""

import os
import pygame


TILE_SIZE = 40
MAP_ROWS = 16
MAP_COLS = 100
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")


def _load_tile_image(name, default_color=(100, 100, 100)):
    """Return a square surface for the given tile name.

    If a PNG with the given name exists under ``assets/tiles`` it will be
    loaded and scaled to ``TILE_SIZE``. Otherwise a plain colored surface is
    returned so projects can easily drop in custom artwork later on.
    """
    path = os.path.join(ASSETS_DIR, "tiles", name)
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        if img.get_size() != (TILE_SIZE, TILE_SIZE):
            img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    else:
        img = pygame.Surface((TILE_SIZE, TILE_SIZE))
        img.fill(default_color)
    return img


class Level:
    """Tilemap driven collection of platforms for the demo level."""

    def __init__(self, map_file=os.path.join(ASSETS_DIR, "level1.txt")):
        """Load the tilemap from ``map_file`` and build collision rectangles."""
        self.map_file = map_file
        self.tiles = {"#": _load_tile_image("ground.png")}
        self.width = MAP_COLS * TILE_SIZE
        self.height = MAP_ROWS * TILE_SIZE
        self._load_map()

    def _load_map(self):
        with open(self.map_file, "r", encoding="utf-8") as f:
            self.grid = [line.rstrip("\n") for line in f]

        if len(self.grid) != MAP_ROWS or any(len(row) != MAP_COLS for row in self.grid):
            raise ValueError(
                f"Map must be {MAP_ROWS}x{MAP_COLS} characters (got {len(self.grid)}x{max(len(r) for r in self.grid) if self.grid else 0})"
            )

        self.platforms = []
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                if tile == "#":
                    rect = pygame.Rect(
                        x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    )
                    self.platforms.append(rect)

    def reset(self):
        """Reload the map so external edits show up immediately."""
        self._load_map()

    def draw(self, surface, offset_x=0):
        """Draw tiles to the given surface with an optional horizontal offset."""
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                img = self.tiles.get(tile)
                if img:
                    surface.blit(img, (x * TILE_SIZE - offset_x, y * TILE_SIZE))


