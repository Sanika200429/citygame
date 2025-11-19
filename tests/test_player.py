"""
Unit tests for Player class.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame
from src.player import Player
from config import *


class TestPlayer(unittest.TestCase):
    """Test cases for the Player class."""

    @classmethod
    def setUpClass(cls):
        """Set up pygame for all tests."""
        pygame.init()

    def setUp(self):
        """Set up a fresh player instance for each test."""
        self.player = Player(100, 100)

    def test_player_initialization(self):
        """Test that player initializes with correct values."""
        self.assertEqual(self.player.x, 100)
        self.assertEqual(self.player.y, 100)
        self.assertEqual(self.player.width, PLAYER_WIDTH)
        self.assertEqual(self.player.height, PLAYER_HEIGHT)
        self.assertEqual(self.player.health, PLAYER_MAX_HEALTH)
        self.assertEqual(self.player.score, 0)

    def test_player_movement(self):
        """Test basic player movement."""
        # Directly set velocity to simulate right movement
        self.player.vel_x = self.player.speed
        self.player.facing_right = True

        # Player should have positive velocity (moving right)
        self.assertGreater(self.player.vel_x, 0)
        self.assertTrue(self.player.facing_right)

    def test_player_jump(self):
        """Test player jump mechanics."""
        # Player starts on ground
        self.player.on_ground = True

        # Simulate jump
        self.player.jump()

        # Velocity should be negative (upward)
        self.assertLess(self.player.vel_y, 0)
        self.assertFalse(self.player.on_ground)
        self.assertTrue(self.player.is_jumping)

    def test_player_health(self):
        """Test player health system."""
        initial_health = self.player.health

        # Take damage
        self.player.take_damage(1)

        # Health should decrease
        self.assertEqual(self.player.health, initial_health - 1)

    def test_player_score(self):
        """Test score collection."""
        initial_score = self.player.score

        # Collect item (teacup worth 10 points)
        points = self.player.collect_item('teacup')

        # Score should increase
        self.assertEqual(self.player.score, initial_score + 10)
        self.assertEqual(points, 10)

    def test_player_death(self):
        """Test player death when health reaches zero."""
        # Reduce health to zero
        self.player.health = 0

        # Player should be considered dead
        self.assertTrue(self.player.is_dead())

    def test_player_bounds(self):
        """Test that player rect is correctly positioned."""
        rect = self.player.rect

        self.assertEqual(rect.x, int(self.player.x))
        self.assertEqual(rect.y, int(self.player.y))
        self.assertEqual(rect.width, self.player.width)
        self.assertEqual(rect.height, self.player.height)


if __name__ == '__main__':
    unittest.main()
