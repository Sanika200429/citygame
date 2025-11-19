"""
Main menu state.
"""

import pygame
from src.states.state import State
from config import *


class MainMenu(State):
    """Main menu with title and play button."""

    def __init__(self, game):
        super().__init__(game)
        self.title_font = pygame.font.Font(None, 80)
        self.menu_font = pygame.font.Font(None, 50)
        self.selected_option = 0
        self.options = ['Start Game', 'Quit']

    def handle_events(self, events):
        """Handle menu input."""
        super().handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.select_option()

    def select_option(self):
        """Execute selected menu option."""
        if self.selected_option == 0:  # Start Game
            self.next_state = 'city_select'
            self.done = True
        elif self.selected_option == 1:  # Quit
            self.game.running = False

    def update(self, dt):
        """Update menu (animations, etc.)."""
        pass

    def draw(self, screen):
        """Draw main menu."""
        screen.fill((20, 30, 50))  # Dark blue background

        # Title
        title_text = self.title_font.render('City Runner', True, WHITE)
        subtitle_text = self.menu_font.render('Coast to Coast', True, (200, 200, 200))

        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, 270))

        screen.blit(title_text, title_rect)
        screen.blit(subtitle_text, subtitle_rect)

        # Menu options
        y_start = 400
        y_spacing = 70

        for i, option in enumerate(self.options):
            color = BOSTON_COLORS['autumn_orange'] if i == self.selected_option else WHITE
            text = self.menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_start + i * y_spacing))
            screen.blit(text, text_rect)

            # Selection indicator
            if i == self.selected_option:
                indicator = self.menu_font.render('>', True, color)
                screen.blit(indicator, (text_rect.left - 50, text_rect.top))

        # Instructions
        small_font = pygame.font.Font(None, 30)
        instructions = small_font.render('Use Arrow Keys and Enter', True, (150, 150, 150))
        instructions_rect = instructions.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(instructions, instructions_rect)
