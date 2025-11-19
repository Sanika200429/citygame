"""
Unit tests for game configuration.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import *


class TestConfig(unittest.TestCase):
    """Test cases for game configuration constants."""

    def test_screen_dimensions(self):
        """Test that screen dimensions are valid."""
        self.assertGreater(SCREEN_WIDTH, 0)
        self.assertGreater(SCREEN_HEIGHT, 0)
        self.assertIsInstance(SCREEN_WIDTH, int)
        self.assertIsInstance(SCREEN_HEIGHT, int)

    def test_fps(self):
        """Test that FPS is a positive integer."""
        self.assertGreater(FPS, 0)
        self.assertIsInstance(FPS, int)

    def test_player_constants(self):
        """Test player configuration values."""
        self.assertGreater(PLAYER_WIDTH, 0)
        self.assertGreater(PLAYER_HEIGHT, 0)
        self.assertGreater(PLAYER_SPEED, 0)
        self.assertGreater(PLAYER_MAX_HEALTH, 0)

    def test_cities_list(self):
        """Test that cities are properly configured."""
        self.assertEqual(len(CITIES), 3)
        self.assertIn('boston', CITIES)
        self.assertIn('nyc', CITIES)
        self.assertIn('chicago', CITIES)

    def test_city_names(self):
        """Test city name mappings."""
        for city_id in CITIES:
            self.assertIn(city_id, CITY_NAMES)
            self.assertIsInstance(CITY_NAMES[city_id], str)

    def test_city_landmarks(self):
        """Test city landmark mappings."""
        for city_id in CITIES:
            self.assertIn(city_id, CITY_LANDMARKS)
            self.assertIsInstance(CITY_LANDMARKS[city_id], str)

    def test_enemy_types(self):
        """Test enemy configuration."""
        self.assertGreater(len(ENEMY_TYPES), 0)

        for enemy_name, enemy_config in ENEMY_TYPES.items():
            self.assertIn('speed', enemy_config)
            self.assertIn('health', enemy_config)
            self.assertIn('points', enemy_config)
            self.assertIn('width', enemy_config)
            self.assertIn('height', enemy_config)

    def test_collectible_values(self):
        """Test collectible point values."""
        self.assertGreater(len(COLLECTIBLE_VALUES), 0)

        for collectible, value in COLLECTIBLE_VALUES.items():
            self.assertGreater(value, 0)
            self.assertIsInstance(value, int)

    def test_colors(self):
        """Test that colors are valid RGB tuples."""
        colors = [WHITE, BLACK, RED, GREEN, BLUE]

        for color in colors:
            self.assertIsInstance(color, tuple)
            self.assertEqual(len(color), 3)
            for component in color:
                self.assertGreaterEqual(component, 0)
                self.assertLessEqual(component, 255)

    def test_volume_settings(self):
        """Test that volume settings are valid."""
        self.assertGreaterEqual(MUSIC_VOLUME, 0.0)
        self.assertLessEqual(MUSIC_VOLUME, 1.0)
        self.assertGreaterEqual(SFX_VOLUME, 0.0)
        self.assertLessEqual(SFX_VOLUME, 1.0)


if __name__ == '__main__':
    unittest.main()
