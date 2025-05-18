"""Simplified game loop utilities for Balance prototype."""

from .player import Player
from .level import Level

WIDTH, HEIGHT = 800, 600
BALANCE_TIME = 40.0  # seconds each player can hold the debuff


def update_game_state(balance_holder, balance_timer, level, player1, player2, dt):
    """Advance timer and reset when it expires."""
    balance_timer -= dt
    if balance_timer <= 0:
        balance_holder = player1
        balance_timer = BALANCE_TIME
        level.reset()
        player1.reset((100, HEIGHT - 150))
        player2.reset((200, HEIGHT - 150))
    return balance_holder, balance_timer
