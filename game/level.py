"""Simple tile-based level layout for the Balance prototype."""

import os
from .utils import Rect

TILE_SIZE = 40
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")


class Level:
    """Tilemap driven collection of platforms for the demo level."""

    def __init__(self, map_file=os.path.join(ASSETS_DIR, "level1.txt")):
        self.map_file = map_file
        self._load_map()

    def _load_map(self):
        with open(self.map_file, "r", encoding="utf-8") as f:
            self.grid = [line.rstrip("\n") for line in f]

        self.platforms = []
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                if tile == "#":
                    rect = Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    self.platforms.append(rect)

    def reset(self):
        self._load_map()
