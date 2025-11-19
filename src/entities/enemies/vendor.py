"""
Street Vendor enemy - pushes cart slowly with wide hitbox.
"""

from src.entities.enemies.enemy import Enemy
from config import *


class Vendor(Enemy):
    """Street vendor pushing a cart."""

    def __init__(self, x, y, patrol_distance=150):
        super().__init__(x, y, 'vendor')
        self.patrol_left_bound = x - patrol_distance
        self.patrol_right_bound = x + patrol_distance
        self.speed = 1  # Slow movement

    def update(self, dt, platforms=None):
        """Update vendor movement."""
        if not self.active:
            return

        # Slow patrol
        self.patrol()

        # Apply gravity
        self.apply_gravity()
        self.y += self.vel_y
        self.rect.y = int(self.y)

        # Ground check
        if platforms:
            for platform in platforms:
                if self.rect.colliderect(platform) and self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.y = self.rect.y
                    self.vel_y = 0
        else:
            if self.rect.bottom >= SCREEN_HEIGHT - 100:
                self.rect.bottom = SCREEN_HEIGHT - 100
                self.y = self.rect.y
                self.vel_y = 0
