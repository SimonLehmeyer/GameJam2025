import unittest
from game.main import update_game_state, BALANCE_TIME
from game.player import Player
from game.level import Level


class DummyLevel(Level):
    def __init__(self):
        super().__init__()
        self.reset_called = 0

    def reset(self):
        self.reset_called += 1
        super().reset()


class DummyPlayer(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.reset_called = 0

    def reset(self, pos=None):
        self.reset_called += 1
        super().reset(pos)


class TestTimer(unittest.TestCase):
    def test_timer_expiration(self):
        level = DummyLevel()
        p1 = DummyPlayer(100, 0)
        p2 = DummyPlayer(200, 0)
        holder = p1
        timer = 0.1

        holder, timer = update_game_state(holder, timer, level, p1, p2, dt=0.2)

        self.assertIs(holder, p1)
        self.assertEqual(timer, BALANCE_TIME)
        self.assertEqual(level.reset_called, 1)
        self.assertEqual(p1.reset_called, 1)
        self.assertEqual(p2.reset_called, 1)


if __name__ == "__main__":
    unittest.main()
