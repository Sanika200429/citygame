"""
Pigeon enemy - flies in sine wave pattern.
"""

import math
from src.entities.enemies.enemy import Enemy
from config import *


class Pigeon(Enemy):
    """Pigeon that flies in a sine wave pattern."""

    def __init__(self, x, y, flight_height=150):
        super().__init__(x, y, 'pigeon')
        self.base_y = y
        self.flight_height = flight_height
        self.wave_offset = 0
        self.wave_speed = 0.05

    def update(self, dt, platforms=None):
        """Update pigeon sine wave flight."""
        if not self.active:
            return

        # Horizontal movement
        self.patrol()

        # Sine wave vertical movement
        self.wave_offset += self.wave_speed
        wave_y = math.sin(self.wave_offset) * self.flight_height
        self.y = self.base_y + wave_y
        self.rect.y = int(self.y)
