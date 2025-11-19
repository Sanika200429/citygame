# base enemy class all enemies inherit from

import pygame
from src.entities.entity import Entity
from src.utils.asset_loader import asset_loader
from config import *


class Enemy(Entity):

    def __init__(self, x, y, enemy_type):
        config = ENEMY_TYPES.get(enemy_type, {})
        width = config.get('width', 32)
        height = config.get('height', 32)
        super().__init__(x, y, width, height)

        self.enemy_type = enemy_type
        self.speed = config.get('speed', 2)
        self.health = config.get('health', 1)
        self.points = config.get('points', 10)

        # patrol bounds
        self.patrol_left_bound = x - 200
        self.patrol_right_bound = x + 200
        self.direction = 1  # 1 = right, -1 = left

        self.load_sprite()

    def load_sprite(self):
        # placeholder colors for each enemy
        color_map = {
            'cyclist': (200, 100, 50),
            'pigeon': (150, 150, 150),
            'taxi': (255, 215, 0),
            'rat': (80, 60, 60),
            'vendor': (100, 180, 100),
            'flying_paper': (240, 240, 240)
        }
        fallback_color = color_map.get(self.enemy_type, RED)

        sprite_path = f"enemies/{self.enemy_type}/{self.enemy_type}.png"
        self.image = asset_loader.load_sprite(
            sprite_path,
            (self.width, self.height),
            fallback_color
        )

    def update(self, dt, platforms=None):
        # override this in subclasses
        pass

    def take_damage(self, amount=1):
        self.health -= amount
        if self.health <= 0:
            self.active = False

    def is_defeated(self):
        return not self.active

    def patrol(self):
        # basic back and forth movement
        self.vel_x = self.speed * self.direction

        # turn around at bounds
        if self.direction > 0 and self.x >= self.patrol_right_bound:
            self.direction = -1
            self.facing_right = False
        elif self.direction < 0 and self.x <= self.patrol_left_bound:
            self.direction = 1
            self.facing_right = True

        self.x += self.vel_x
        self.rect.x = int(self.x)
