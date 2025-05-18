import unittest
import os
from game.level import Level, TILE_SIZE


class TestLevelLoading(unittest.TestCase):
    def test_load_map(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "map.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write("..#\n###\n")
            lvl = Level(map_file=path)
            self.assertEqual(lvl.grid, ["..#", "###"])
            self.assertEqual(len(lvl.platforms), 4)
            first = lvl.platforms[0]
            self.assertEqual(first.x, TILE_SIZE * 2)
            self.assertEqual(first.y, 0)


if __name__ == "__main__":
    unittest.main()
