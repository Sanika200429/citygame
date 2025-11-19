"""
Camera system for smooth side-scrolling.
"""

import pygame
from config import *


class Camera:
    """Camera that follows the player with smooth scrolling."""

    def __init__(self, level_width):
        self.offset_x = 0
        self.offset_y = 0
        self.level_width = level_width
        self.target_offset_x = 0

    def update(self, player):
        """Update camera position to follow player."""
        # Calculate ideal camera position (player at 1/3 from left)
        ideal_offset = player.rect.x - CAMERA_PLAYER_OFFSET_X

        # Add lookahead in movement direction
        if player.vel_x > 0:
            ideal_offset += CAMERA_LOOKAHEAD
        elif player.vel_x < 0:
            ideal_offset -= CAMERA_LOOKAHEAD

        # Smooth camera movement (lerp)
        self.target_offset_x = ideal_offset
        smoothing = 0.1
        self.offset_x += (self.target_offset_x - self.offset_x) * smoothing

        # Clamp camera to level boundaries
        self.offset_x = max(0, self.offset_x)
        max_offset = self.level_width - SCREEN_WIDTH
        if max_offset > 0:
            self.offset_x = min(self.offset_x, max_offset)

        # Keep y offset at 0 for side-scroller (can modify for vertical movement)
        self.offset_y = 0

    def apply(self, entity):
        """Apply camera offset to an entity's position."""
        return entity.rect.x - self.offset_x, entity.rect.y - self.offset_y

    def apply_rect(self, rect):
        """Apply camera offset to a rectangle."""
        return pygame.Rect(rect.x - self.offset_x, rect.y - self.offset_y, rect.width, rect.height)

    def get_offset(self):
        """Get current camera offset."""
        return int(self.offset_x), int(self.offset_y)
