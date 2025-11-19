# collectible items you pick up for points

import pygame
from src.entities.entity import Entity
from src.utils.asset_loader import asset_loader
from config import *


class Collectible(Entity):

    def __init__(self, x, y, collectible_type):
        super().__init__(x, y, 24, 24)  # smaller hitbox

        self.collectible_type = collectible_type
        self.collected = False
        self.value = COLLECTIBLE_VALUES.get(collectible_type, 10)

        # bobbing animation
        self.bob_offset = 0
        self.bob_speed = 0.05
        self.base_y = y

        self.load_sprite()

    def load_sprite(self):
        # colors for each collectible type
        color_map = {
            # Boston
            'teacup': (200, 100, 150),
            'book': (139, 69, 19),
            # NYC
            'pizza': (255, 140, 0),
            'metrocard': (255, 215, 0),
            'bagel': (210, 180, 140),
            # Chicago
            'deep_dish': (178, 34, 34),
            'hot_dog': (255, 160, 122),
            'jazz_note': (138, 43, 226)
        }

        fallback_color = color_map.get(self.collectible_type, BLUE)

        sprite_path = f"collectibles/{self.collectible_type}.png"
        self.image = asset_loader.load_sprite(
            sprite_path,
            (self.width, self.height),
            fallback_color
        )

    def update(self, dt, platforms=None):
        if self.collected:
            return

        # make it bob up and down
        self.bob_offset += self.bob_speed
        import math
        self.y = self.base_y + math.sin(self.bob_offset) * 5
        self.rect.y = int(self.y)

    def collect(self):
        self.collected = True
        self.active = False
        return self.value

    def draw(self, screen, camera_offset=0):
        if not self.collected:
            super().draw(screen, camera_offset)


# helper function to spawn a bunch of collectibles
def create_city_collectibles(city, x, y, count=10):
    collectibles = []

    city_types = {
        'boston': ['teacup', 'book'],
        'nyc': ['pizza', 'metrocard', 'bagel'],
        'chicago': ['deep_dish', 'hot_dog', 'jazz_note']
    }

    types = city_types.get(city, ['teacup'])

    import random
    for i in range(count):
        ctype = random.choice(types)
        offset_x = x + i * 40 + random.randint(-10, 10)
        offset_y = y + random.randint(-20, 20)
        collectibles.append(Collectible(offset_x, offset_y, ctype))

    return collectibles
