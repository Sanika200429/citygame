"""
NYC level configuration.
"""

from src.levels.level import Level
from src.entities.enemies.rat import Rat
from src.entities.enemies.taxi import Taxi
from src.entities.enemies.vendor import Vendor
from src.entities.collectible import Collectible
from config import *
import pygame
import random


class NYCLevel(Level):
    """NYC level - neon night theme."""

    def __init__(self):
        super().__init__('nyc', LEVEL_WIDTH)
        self.setup_level()

    def setup_level(self):
        """Set up NYC-specific elements."""
        self.create_platforms()
        self.create_enemies()
        self.create_collectibles()

        self.checkpoints = [1000, 2000, 3000]
        self.landmark_position = LEVEL_WIDTH - 300

    def create_platforms(self):
        """Create NYC platforms (fire escapes, building ledges)."""
        ground_y = SCREEN_HEIGHT - 100

        # Main ground
        self.platforms.append(pygame.Rect(0, ground_y, self.level_width, 100))

        # Fire escape platforms (staggered)
        for i in range(12):
            x = 350 + i * 300
            y = ground_y - 120 - (i % 4) * 40
            width = 120 + random.randint(-20, 20)
            self.platforms.append(pygame.Rect(x, y, width, 15))

    def create_enemies(self):
        """Create NYC enemies (rats, taxis, vendors)."""
        ground_y = SCREEN_HEIGHT - 115

        # Rats
        for i in range(8):
            x = 600 + i * 450
            self.enemies.append(Rat(x, ground_y))

        # Street vendors
        vendor_positions = [800, 1600, 2400]
        for x in vendor_positions:
            self.enemies.append(Vendor(x, ground_y))

        # Taxis
        self.enemies.append(Taxi(100, ground_y + 15))

    def create_collectibles(self):
        """Create NYC collectibles (pizza, metrocards, bagels)."""
        ground_y = SCREEN_HEIGHT - 100

        types = ['pizza', 'metrocard', 'bagel']

        # Ground collectibles
        for i in range(40):
            x = random.randint(200, self.level_width - 200)
            y = ground_y - 50
            ctype = random.choice(types)
            self.collectibles.append(Collectible(x, y, ctype))

        # Platform collectibles
        for platform in self.platforms[1:]:
            if random.random() < 0.7:
                x = platform.x + platform.width // 2
                y = platform.y - 30
                ctype = random.choice(types)
                self.collectibles.append(Collectible(x, y, ctype))
