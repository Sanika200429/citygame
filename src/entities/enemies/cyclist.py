"""
Cyclist enemy - patrols back and forth on ground.
"""

from src.entities.enemies.enemy import Enemy
from config import *


class Cyclist(Enemy):
    """Cyclist that patrols horizontally on platforms."""

    def __init__(self, x, y, patrol_distance=200):
        super().__init__(x, y, 'cyclist')
        self.patrol_left_bound = x - patrol_distance
        self.patrol_right_bound = x + patrol_distance

    def update(self, dt, platforms=None):
        """Update cyclist patrol behavior."""
        if not self.active:
            return

        # Simple patrol
        self.patrol()

        # Apply gravity and ground collision
        self.apply_gravity()
        self.y += self.vel_y
        self.rect.y = int(self.y)

        # Simple ground check
        if platforms:
            for platform in platforms:
                if self.rect.colliderect(platform) and self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.y = self.rect.y
                    self.vel_y = 0
        else:
            # Default ground
            if self.rect.bottom >= SCREEN_HEIGHT - 100:
                self.rect.bottom = SCREEN_HEIGHT - 100
                self.y = self.rect.y
                self.vel_y = 0
