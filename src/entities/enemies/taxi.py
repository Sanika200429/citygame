"""
Taxi enemy - rushes from off-screen periodically.
"""

from src.entities.enemies.enemy import Enemy
from config import *
import random


class Taxi(Enemy):
    """Taxi that rushes across the screen with warning."""

    def __init__(self, x, y):
        super().__init__(x, y, 'taxi')
        self.warning_time = 1000  # milliseconds
        self.warning_timer = 0
        self.is_warning = False
        self.is_rushing = False
        self.reset_position = x - SCREEN_WIDTH - 100
        self.x = self.reset_position

    def update(self, dt, platforms=None):
        """Update taxi rush behavior."""
        if not self.active:
            return

        if self.is_rushing:
            # Rush across screen
            self.x += self.speed
            self.rect.x = int(self.x)

            # Reset when off-screen
            if self.x > self.reset_position + SCREEN_WIDTH * 2:
                self.is_rushing = False
                self.x = self.reset_position
                self.rect.x = int(self.x)
        else:
            # Wait for next rush (handled by level manager)
            pass

    def trigger_warning(self):
        """Start the warning before rushing."""
        self.is_warning = True
        self.warning_timer = self.warning_time

    def start_rush(self):
        """Begin the taxi rush."""
        self.is_warning = False
        self.is_rushing = True
