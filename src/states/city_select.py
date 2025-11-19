"""
City selection menu state.
"""

import pygame
from src.states.state import State
from config import *


class CitySelect(State):
    """City selection menu with unlock progression."""

    def __init__(self, game):
        super().__init__(game)
        self.title_font = pygame.font.Font(None, 60)
        self.city_font = pygame.font.Font(None, 50)
        self.info_font = pygame.font.Font(None, 30)

        self.selected_city = 0
        self.unlocked_cities = self.game.unlocked_cities if hasattr(self.game, 'unlocked_cities') else ['boston']

        self.city_info = {
            'boston': {
                'name': 'Boston',
                'theme': 'Fall Leaves & Brick Streets',
                'landmark': 'Fenway Park',
                'color': BOSTON_COLORS['autumn_orange']
            },
            'nyc': {
                'name': 'New York City',
                'theme': 'Neon Nights & Skyscrapers',
                'landmark': 'Times Square',
                'color': NYC_COLORS['electric_blue']
            },
            'chicago': {
                'name': 'Chicago',
                'theme': 'Windy Lakefront',
                'landmark': 'The Chicago Bean',
                'color': CHICAGO_COLORS['cool_blue']
            }
        }

    def handle_events(self, events):
        """Handle city selection input."""
        super().handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.selected_city = (self.selected_city - 1) % len(CITIES)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.selected_city = (self.selected_city + 1) % len(CITIES)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.start_selected_city()
                elif event.key == pygame.K_ESCAPE:
                    self.next_state = 'menu'
                    self.done = True

    def start_selected_city(self):
        """Start the selected city level."""
        city_key = CITIES[self.selected_city]

        if city_key in self.unlocked_cities:
            self.game.current_city = city_key
            self.next_state = 'gameplay'
            self.done = True
        # else: show "locked" message (could add visual feedback)

    def update(self, dt):
        """Update city selection menu."""
        pass

    def draw(self, screen):
        """Draw city selection menu."""
        screen.fill((30, 30, 50))

        # Title
        title_text = self.title_font.render('Select Your City', True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 80))
        screen.blit(title_text, title_rect)

        # City cards
        card_width = 300
        card_height = 400
        card_spacing = 50
        total_width = len(CITIES) * card_width + (len(CITIES) - 1) * card_spacing
        start_x = (SCREEN_WIDTH - total_width) // 2

        for i, city_key in enumerate(CITIES):
            x = start_x + i * (card_width + card_spacing)
            y = 180
            is_selected = i == self.selected_city
            is_unlocked = city_key in self.unlocked_cities

            self.draw_city_card(screen, x, y, card_width, card_height, city_key, is_selected, is_unlocked)

        # Instructions
        instructions = self.info_font.render('Arrow Keys to Select | Enter to Play | ESC to Back', True, (180, 180, 180))
        instructions_rect = instructions.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40))
        screen.blit(instructions, instructions_rect)

    def draw_city_card(self, screen, x, y, width, height, city_key, is_selected, is_unlocked):
        """Draw an individual city card."""
        info = self.city_info[city_key]

        # Card background
        card_rect = pygame.Rect(x, y, width, height)
        border_color = info['color'] if is_selected else (100, 100, 100)
        border_width = 5 if is_selected else 2

        # Background
        bg_color = (50, 50, 70) if is_unlocked else (30, 30, 30)
        pygame.draw.rect(screen, bg_color, card_rect)
        pygame.draw.rect(screen, border_color, card_rect, border_width)

        # City name
        name_text = self.city_font.render(info['name'], True, info['color'] if is_unlocked else (80, 80, 80))
        name_rect = name_text.get_rect(center=(x + width // 2, y + 60))
        screen.blit(name_text, name_rect)

        # Theme
        theme_text = self.info_font.render(info['theme'], True, WHITE if is_unlocked else (100, 100, 100))
        theme_rect = theme_text.get_rect(center=(x + width // 2, y + 150))
        screen.blit(theme_text, theme_rect)

        # Landmark
        landmark_label = self.info_font.render('Landmark:', True, (150, 150, 150))
        landmark_text = self.info_font.render(info['landmark'], True, info['color'] if is_unlocked else (80, 80, 80))
        label_rect = landmark_label.get_rect(center=(x + width // 2, y + 220))
        text_rect = landmark_text.get_rect(center=(x + width // 2, y + 250))
        screen.blit(landmark_label, label_rect)
        screen.blit(landmark_text, text_rect)

        # Lock status
        if not is_unlocked:
            lock_text = self.city_font.render('LOCKED', True, RED)
            lock_rect = lock_text.get_rect(center=(x + width // 2, y + 320))
            screen.blit(lock_text, lock_rect)
        elif is_selected:
            play_text = self.info_font.render('Press ENTER to Play', True, info['color'])
            play_rect = play_text.get_rect(center=(x + width // 2, y + 320))
            screen.blit(play_text, play_rect)
