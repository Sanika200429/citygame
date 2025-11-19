"""
Base Entity class for all game objects.
Provides common functionality for player, enemies, and collectibles.
"""

import pygame
from config import *


class Entity(pygame.sprite.Sprite):
    """Base class for all entities in the game."""

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x = float(x)  # Float for smooth movement
        self.y = float(y)
        self.width = width
        self.height = height

        # Physics
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False

        # Visual
        self.image = None
        self.facing_right = True

        # State
        self.active = True
        self.visible = True

    def update(self, dt, platforms=None):
        """Update entity state. Override in subclasses."""
        pass

    def draw(self, screen, camera_offset=0):
        """Draw entity to screen with camera offset."""
        if not self.visible or self.image is None:
            return

        # Draw sprite
        screen_x = self.rect.x - camera_offset
        screen_y = self.rect.y

        # Flip sprite if facing left
        if self.facing_right:
            screen.blit(self.image, (screen_x, screen_y))
        else:
            flipped = pygame.transform.flip(self.image, True, False)
            screen.blit(flipped, (screen_x, screen_y))

        # Debug hitbox
        if DEBUG_MODE and SHOW_HITBOXES:
            debug_rect = pygame.Rect(screen_x, screen_y, self.width, self.height)
            pygame.draw.rect(screen, RED, debug_rect, 2)

    def apply_gravity(self, gravity=GRAVITY):
        """Apply gravity to entity."""
        self.vel_y += gravity
        if self.vel_y > TERMINAL_VELOCITY:
            self.vel_y = TERMINAL_VELOCITY

    def check_collision(self, other):
        """Check if this entity collides with another."""
        return self.rect.colliderect(other.rect)

    def get_hitbox(self):
        """Return the entity's hitbox."""
        return self.rect
