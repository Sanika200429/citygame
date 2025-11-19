"""
Main Game class with state management.
"""

import pygame
import asyncio
from config import *
from src.states.menu import MainMenu
from src.states.city_select import CitySelect
from src.states.gameplay import Gameplay
from src.states.landmark import LandmarkCelebration


class Game:
    """Main game manager with state machine."""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        # Screen setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # Game state
        self.current_state = None
        self.states = {}
        self.current_city = 'boston'
        self.unlocked_cities = ['boston']  # Start with Boston unlocked

        # FPS tracking
        self.font = pygame.font.Font(None, 30)

        # Initialize states
        self.setup_states()

    def setup_states(self):
        """Create all game states."""
        self.states = {
            'menu': MainMenu(self),
            'city_select': CitySelect(self),
            'gameplay': Gameplay(self),
            'landmark': LandmarkCelebration(self)
        }

        # Start with main menu
        self.current_state = self.states['menu']
        self.current_state.enter_state()

    async def run(self):
        """Main game loop - async for web compatibility."""
        while self.running:
            dt = self.clock.tick(FPS)

            # Handle events
            events = pygame.event.get()
            self.current_state.handle_events(events)

            # Update current state
            self.current_state.update(dt)

            # Check for state transition
            if self.current_state.done:
                self.change_state(self.current_state.next_state)

            # Draw
            self.current_state.draw(self.screen)

            # Debug info
            if DEBUG_MODE and SHOW_FPS:
                self.draw_fps()

            pygame.display.flip()

            # yield control to browser for web builds
            await asyncio.sleep(0)

        pygame.quit()

    def change_state(self, new_state_name):
        """Change to a new state."""
        if new_state_name in self.states:
            self.current_state.exit_state()
            self.current_state = self.states[new_state_name]
            self.current_state.done = False
            self.current_state.next_state = None
            self.current_state.enter_state()

    def draw_fps(self):
        """Draw FPS counter."""
        fps = int(self.clock.get_fps())
        fps_text = self.font.render(f'FPS: {fps}', True, WHITE)
        self.screen.blit(fps_text, (10, SCREEN_HEIGHT - 40))
