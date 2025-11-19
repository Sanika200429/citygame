"""
Rat enemy - scurries with erratic movement.
"""

import random
from src.entities.enemies.enemy import Enemy
from config import *


class Rat(Enemy):
    """Rat that scurries with unpredictable turns."""

    def __init__(self, x, y):
        super().__init__(x, y, 'rat')
        self.direction_change_timer = 0
        self.direction_change_interval = random.randint(1000, 3000)

    def update(self, dt, platforms=None):
        """Update rat erratic movement."""
        if not self.active:
            return

        # Erratic direction changes
        self.direction_change_timer += dt
        if self.direction_change_timer >= self.direction_change_interval:
            self.direction_change_timer = 0
            self.direction_change_interval = random.randint(1000, 3000)
            # Randomly change direction
            if random.random() < 0.5:
                self.direction *= -1
                self.facing_right = self.direction > 0

        # Move
        self.vel_x = self.speed * self.direction
        self.x += self.vel_x
        self.rect.x = int(self.x)

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
