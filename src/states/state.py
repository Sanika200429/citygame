"""
Base State class for game state management.
"""

import pygame
from config import *


class State:
    """Base class for all game states."""

    def __init__(self, game):
        self.game = game
        self.next_state = None
        self.done = False

    def handle_events(self, events):
        """Handle input events. Override in subclasses."""
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False

    def update(self, dt):
        """Update state logic. Override in subclasses."""
        pass

    def draw(self, screen):
        """Draw state to screen. Override in subclasses."""
        screen.fill(BLACK)

    def enter_state(self):
        """Called when entering this state."""
        pass

    def exit_state(self):
        """Called when exiting this state."""
        pass
