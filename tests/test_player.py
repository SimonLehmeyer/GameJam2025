import unittest
from game.player import Player
from game.utils import Rect


class TestPlayerCollision(unittest.TestCase):
    def test_player_collision_stops_fall(self):
        platform = Rect(0, 50, 100, 10)
        player = Player(10, 0)
        player.vel_y = 100
        dt = 0.1
        player.update(dt, [platform])
        self.assertEqual(player.rect.bottom, platform.top)
        self.assertEqual(player.vel_y, 0)


if __name__ == "__main__":
    unittest.main()
