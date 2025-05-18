"""Entry point for the Balance demo."""

import pygame
from pygame.locals import (
    K_a,
    K_d,
    K_w,
    K_e,
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_RCTRL,
    QUIT,
)
from .player import Player
from .level import Level

WIDTH, HEIGHT = 800, 600
FPS = 60
BALANCE_TIME = 40.0  # seconds each player can hold the debuff


def main():
    """Run the demo game loop."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    player1 = Player(100, HEIGHT - 150, (255, 0, 0), controls={'left':K_a, 'right':K_d, 'jump':K_w, 'pass':K_e})
    player2 = Player(200, HEIGHT - 150, (0, 0, 255), controls={'left':K_LEFT, 'right':K_RIGHT, 'jump':K_UP, 'pass':K_RCTRL})

    level = Level()

    balance_holder = player1
    balance_timer = BALANCE_TIME

    camera_x = 0
    running = True
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # handle passing debuff
        keys = pygame.key.get_pressed()
        if balance_holder is player1 and keys[player1.controls['pass']] and player1.rect.colliderect(player2.rect):
            balance_holder = player2
            balance_timer = BALANCE_TIME
        elif balance_holder is player2 and keys[player2.controls['pass']] and player1.rect.colliderect(player2.rect):
            balance_holder = player1
            balance_timer = BALANCE_TIME

        balance_timer -= dt
        if balance_timer <= 0:
            print("Balance timer expired! Restarting...")
            balance_holder = player1
            balance_timer = BALANCE_TIME
            level.reset()
            player1.reset((100, HEIGHT - 150))
            player2.reset((200, HEIGHT - 150))

        player1.update(dt, level.platforms)
        player2.update(dt, level.platforms)

        # camera follows the balance holder
        camera_x = balance_holder.rect.centerx - WIDTH // 2
        camera_x = max(0, min(camera_x, level.width - WIDTH))

        screen.fill((30, 30, 30))
        level.draw(screen, camera_x)
        player1.draw(screen, camera_x)
        player2.draw(screen, camera_x)
        timer_surf = font.render(f"{balance_timer:.1f}", True, (255, 255, 255))
        screen.blit(timer_surf, (WIDTH // 2 - timer_surf.get_width() // 2, 10))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

