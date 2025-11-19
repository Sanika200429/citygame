"""
Flying Paper enemy - blown by wind at various heights.
"""

import random
import math
from src.entities.enemies.enemy import Enemy
from config import *


class FlyingPaper(Enemy):
    """Paper blown by wind in diagonal patterns."""

    def __init__(self, x, y):
        super().__init__(x, y, 'flying_paper')
        self.wind_strength = random.uniform(0.5, 1.5)
        self.vertical_speed = random.uniform(-1, 1)
        self.wobble = 0

    def update(self, dt, platforms=None):
        """Update flying paper wind movement."""
        if not self.active:
            return

        # Horizontal wind movement
        self.x += self.speed * self.wind_strength * self.direction

        # Vertical wobble
        self.wobble += 0.1
        self.y += math.sin(self.wobble) * 0.5 + self.vertical_speed

        # Keep in reasonable bounds
        if self.y < 100:
            self.vertical_speed = abs(self.vertical_speed)
        elif self.y > SCREEN_HEIGHT - 200:
            self.vertical_speed = -abs(self.vertical_speed)

        # Update rect
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        # Reset if too far off screen
        if self.x < -100 or self.x > LEVEL_WIDTH + 100:
            self.active = False
