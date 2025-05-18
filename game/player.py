"""Player entity used in the Balance prototype without pygame."""

from .utils import Rect

GRAVITY = 1000
JUMP_SPEED = -400
SPEED = 200


class Player:
    """Controlled character with basic platformer physics."""

    def __init__(self, x, y):
        self.spawn_pos = (x, y)
        self.rect = Rect(x, y, 40, 60)
        self.vel_y = 0

    def reset(self, pos=None):
        if pos:
            self.rect.x, self.rect.y = pos
        else:
            self.rect.x, self.rect.y = self.spawn_pos
        self.vel_y = 0

    def update(self, dt, platforms):
        self.vel_y += GRAVITY * dt
        self.rect.y += self.vel_y * dt

        for p in platforms:
            if self.rect.colliderect(p) and self.vel_y > 0:
                if self.rect.bottom >= p.top:
                    self.rect.bottom = p.top
                    self.vel_y = 0

    def on_ground(self, platforms):
        self.rect.y += 1
        grounded = any(self.rect.colliderect(p) for p in platforms)
        self.rect.y -= 1
        return grounded
