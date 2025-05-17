import pygame


class Level:
    def __init__(self):
        self.platforms = [
            pygame.Rect(0, 550, 800, 50),
            pygame.Rect(150, 450, 200, 20),
            pygame.Rect(400, 350, 200, 20),
            pygame.Rect(100, 250, 200, 20),
            pygame.Rect(300, 150, 200, 20),
        ]

    def reset(self):
        # For now nothing dynamic
        pass

    def draw(self, surface):
        for p in self.platforms:
            pygame.draw.rect(surface, (100, 100, 100), p)
