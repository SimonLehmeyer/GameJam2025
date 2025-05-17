"""Simple level layout for the Balance prototype."""

import pygame


class Level:
    """Static collection of platforms for the demo level."""

    def __init__(self):
        """Create rectangles representing each platform."""
        self.platforms = [
            pygame.Rect(0, 550, 800, 50),
            pygame.Rect(150, 450, 200, 20),
            pygame.Rect(400, 350, 200, 20),
            pygame.Rect(100, 250, 200, 20),
            pygame.Rect(300, 150, 200, 20),
        ]

    def reset(self):
        """Reset any dynamic state (none yet)."""
        pass

    def draw(self, surface):
        """Draw platforms to the given surface."""
        for p in self.platforms:
            pygame.draw.rect(surface, (100, 100, 100), p)

