"""
Chicago level configuration.
"""

from src.levels.level import Level
from src.entities.enemies.pigeon import Pigeon
from src.entities.enemies.flying_paper import FlyingPaper
from src.entities.collectible import Collectible
from config import *
import pygame
import random


class ChicagoLevel(Level):
    """Chicago level - windy, modern theme."""

    def __init__(self):
        super().__init__('chicago', LEVEL_WIDTH)
        self.setup_level()

    def setup_level(self):
        """Set up Chicago-specific elements."""
        self.create_platforms()
        self.create_enemies()
        self.create_collectibles()

        self.checkpoints = [1000, 2000, 3000]
        self.landmark_position = LEVEL_WIDTH - 300

    def create_platforms(self):
        """Create Chicago platforms (elevated train tracks, buildings)."""
        ground_y = SCREEN_HEIGHT - 100

        # Main ground
        self.platforms.append(pygame.Rect(0, ground_y, self.level_width, 100))

        # Elevated train platforms
        for i in range(10):
            x = 300 + i * 350
            y = ground_y - 180 - (i % 3) * 30
            width = 180
            self.platforms.append(pygame.Rect(x, y, width, 20))

    def create_enemies(self):
        """Create Chicago enemies (pigeons, flying papers)."""
        # Aggressive pigeons
        for i in range(6):
            x = 500 + i * 600
            y = 200 + random.randint(-50, 50)
            self.enemies.append(Pigeon(x, y, flight_height=100))

        # Flying papers (wind effect)
        for i in range(15):
            x = random.randint(300, self.level_width - 300)
            y = random.randint(150, 400)
            self.enemies.append(FlyingPaper(x, y))

    def create_collectibles(self):
        """Create Chicago collectibles (deep-dish, hot dogs, jazz notes)."""
        ground_y = SCREEN_HEIGHT - 100

        types = ['deep_dish', 'hot_dog', 'jazz_note']

        # Ground collectibles
        for i in range(35):
            x = random.randint(200, self.level_width - 200)
            y = ground_y - 50
            ctype = random.choice(types)
            self.collectibles.append(Collectible(x, y, ctype))

        # Platform collectibles
        for platform in self.platforms[1:]:
            if random.random() < 0.65:
                x = platform.x + platform.width // 2
                y = platform.y - 30
                ctype = random.choice(types)
                self.collectibles.append(Collectible(x, y, ctype))
