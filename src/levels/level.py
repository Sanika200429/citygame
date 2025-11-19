"""
Base Level class with platforms, enemies, and collectibles.
"""

import pygame
from src.utils.asset_loader import asset_loader
from config import *


class Level:
    """Base class for game levels."""

    def __init__(self, city_name, level_width=LEVEL_WIDTH):
        self.city_name = city_name
        self.level_width = level_width
        self.level_height = SCREEN_HEIGHT

        # Level elements
        self.platforms = []
        self.enemies = []
        self.collectibles = []
        self.checkpoints = []
        self.landmark_position = level_width - 200

        # Background layers (parallax)
        self.bg_layers = []
        self.load_backgrounds()

        # Level state
        self.completed = False
        self.current_checkpoint = 0

    def load_backgrounds(self):
        """Load background layers for parallax effect."""
        # Try to load background layers
        # Layer 0: Far background (slowest parallax)
        # Layer 1: Mid background
        # Layer 2: Near background (fastest parallax)
        for i in range(3):
            bg_path = f"{self.city_name}/layer_{i}.png"
            bg_image = asset_loader.load_background(
                bg_path,
                (SCREEN_WIDTH, SCREEN_HEIGHT),
                self.get_sky_color()
            )
            self.bg_layers.append(bg_image)

    def update(self, dt):
        """Update all level entities."""
        # Update enemies
        for enemy in self.enemies:
            if enemy.active:
                enemy.update(dt, self.platforms)

        # Update collectibles
        for collectible in self.collectibles:
            if not collectible.collected:
                collectible.update(dt, self.platforms)

    def draw(self, screen, camera_offset):
        """Draw level elements."""
        # Draw background layers (parallax)
        self.draw_background(screen, camera_offset)

        # Draw platforms
        self.draw_platforms(screen, camera_offset)

        # Draw collectibles
        for collectible in self.collectibles:
            if not collectible.collected:
                collectible.draw(screen, camera_offset)

        # Draw enemies
        for enemy in self.enemies:
            if enemy.active:
                enemy.draw(screen, camera_offset)

    def draw_background(self, screen, camera_offset):
        """Draw parallax background layers."""
        # Fill with sky color as base
        screen.fill(self.get_sky_color())

        # Draw each parallax layer
        for i, layer in enumerate(self.bg_layers):
            # Different parallax speeds for each layer
            parallax_factor = 0.1 + (i * 0.15)
            offset = int(camera_offset * parallax_factor)

            # Draw layer
            screen.blit(layer, (-offset, 0))

            # Draw second copy for seamless scrolling if needed
            if offset > 0:
                screen.blit(layer, (layer.get_width() - offset, 0))

    def draw_platforms(self, screen, camera_offset):
        """Draw all platforms."""
        for platform in self.platforms:
            screen_rect = pygame.Rect(
                platform.x - camera_offset,
                platform.y,
                platform.width,
                platform.height
            )
            # Simple colored rectangles for now
            pygame.draw.rect(screen, self.get_platform_color(), screen_rect)

    def get_sky_color(self):
        """Get the sky background color for this city."""
        sky_colors = {
            'boston': (244, 232, 208),  # Warm cream
            'nyc': (25, 25, 50),  # Dark blue (night)
            'chicago': (135, 206, 235)  # Sky blue
        }
        return sky_colors.get(self.city_name, (135, 206, 235))

    def get_platform_color(self):
        """Get the platform color for this city."""
        platform_colors = {
            'boston': (180, 70, 58),  # Brick red
            'nyc': (112, 128, 144),  # Steel gray
            'chicago': (192, 192, 192)  # Silver
        }
        return platform_colors.get(self.city_name, (100, 100, 100))

    def check_collectible_collision(self, player):
        """Check if player collected any items."""
        collected_points = 0
        for collectible in self.collectibles:
            if not collectible.collected and player.check_collision(collectible):
                points = collectible.collect()
                player.collect_item(collectible.collectible_type)
                collected_points += points
        return collected_points

    def check_enemy_collision(self, player):
        """Check if player hit any enemies."""
        for enemy in self.enemies:
            if enemy.active and player.check_collision(enemy):
                # Check if player is jumping on enemy
                if player.vel_y > 0 and player.rect.bottom <= enemy.rect.centery:
                    # Player jumped on enemy
                    if enemy.health < 999:  # Only defeat if not invincible
                        enemy.take_damage(1)
                        player.vel_y = -8  # Bounce
                        return True, enemy.points
                else:
                    # Player hit enemy
                    player.take_damage(1)
                    return False, 0
        return False, 0

    def check_checkpoint(self, player):
        """Check if player reached a checkpoint."""
        for i, checkpoint_x in enumerate(self.checkpoints):
            if i > self.current_checkpoint and player.rect.x >= checkpoint_x:
                self.current_checkpoint = i
                return i, checkpoint_x
        return None, None

    def check_landmark_reached(self, player):
        """Check if player reached the landmark."""
        if player.rect.x >= self.landmark_position:
            self.completed = True
            return True
        return False

    def get_respawn_position(self):
        """Get the respawn position for current checkpoint."""
        if self.current_checkpoint == 0:
            return 100, SCREEN_HEIGHT - 200
        else:
            checkpoint_x = self.checkpoints[self.current_checkpoint - 1]
            return checkpoint_x + 50, SCREEN_HEIGHT - 200

    def create_ground_platforms(self):
        """Create basic ground platforms for testing."""
        # Create continuous ground
        ground_y = SCREEN_HEIGHT - 100
        self.platforms.append(pygame.Rect(0, ground_y, self.level_width, 100))

        # Add some floating platforms
        for i in range(5):
            x = 300 + i * 600
            y = ground_y - 100 - (i % 3) * 50
            self.platforms.append(pygame.Rect(x, y, 150, 20))
