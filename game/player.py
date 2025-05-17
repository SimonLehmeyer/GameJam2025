import pygame

GRAVITY = 1000
JUMP_SPEED = -400
SPEED = 200


class Player:
    def __init__(self, x, y, color, controls):
        self.controls = controls
        self.color = color
        self.spawn_pos = (x, y)
        self.rect = pygame.Rect(x, y, 40, 60)
        self.vel = pygame.Vector2(0, 0)

    def reset(self, pos=None):
        if pos:
            self.rect.topleft = pos
        else:
            self.rect.topleft = self.spawn_pos
        self.vel.update(0, 0)

    def update(self, dt, platforms):
        keys = pygame.key.get_pressed()
        if keys[self.controls['left']]:
            self.rect.x -= SPEED * dt
        if keys[self.controls['right']]:
            self.rect.x += SPEED * dt
        if keys[self.controls['jump']] and self.on_ground(platforms):
            self.vel.y = JUMP_SPEED

        self.vel.y += GRAVITY * dt
        self.rect.y += self.vel.y * dt

        # simple collision with ground/platforms
        for p in platforms:
            if self.rect.colliderect(p):
                if self.vel.y > 0:
                    self.rect.bottom = p.top
                    self.vel.y = 0

    def on_ground(self, platforms):
        self.rect.y += 1
        grounded = any(self.rect.colliderect(p) for p in platforms)
        self.rect.y -= 1
        return grounded

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
