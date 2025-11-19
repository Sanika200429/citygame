"""
Landmark celebration animation state.
"""

import pygame
from src.states.state import State
from config import *


class LandmarkCelebration(State):
    """Landmark arrival celebration animation."""

    def __init__(self, game):
        super().__init__(game)
        self.animation_timer = 0
        self.animation_duration = 5000  # 5 seconds
        self.big_font = pygame.font.Font(None, 80)
        self.medium_font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 36)
        self.city = None
        self.landmark = None

    def enter_state(self):
        """Initialize celebration for current city."""
        self.city = self.game.current_city if hasattr(self.game, 'current_city') else 'boston'
        self.landmark = CITY_LANDMARKS.get(self.city, 'Landmark')
        self.animation_timer = 0

        # Unlock next city
        if hasattr(self.game, 'unlocked_cities'):
            city_index = CITIES.index(self.city)
            if city_index < len(CITIES) - 1:
                next_city = CITIES[city_index + 1]
                if next_city not in self.game.unlocked_cities:
                    self.game.unlocked_cities.append(next_city)

    def handle_events(self, events):
        """Handle input during celebration."""
        super().handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    # Skip to city select
                    self.next_state = 'city_select'
                    self.done = True

    def update(self, dt):
        """Update celebration animation."""
        self.animation_timer += dt

        if self.animation_timer >= self.animation_duration:
            # Auto-advance to city select
            self.next_state = 'city_select'
            self.done = True

    def draw(self, screen):
        """Draw celebration animation."""
        # Background color based on city
        bg_colors = {
            'boston': BOSTON_COLORS['deep_green'],
            'nyc': NYC_COLORS['hot_pink'],
            'chicago': CHICAGO_COLORS['cool_blue']
        }
        screen.fill(bg_colors.get(self.city, BLACK))

        # Calculate animation phase
        phase = self.animation_timer / self.animation_duration

        # Victory text (fade in)
        if phase < 0.3:
            alpha = int((phase / 0.3) * 255)
        else:
            alpha = 255

        victory_text = self.big_font.render('VICTORY!', True, WHITE)
        victory_text.set_alpha(alpha)
        victory_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        screen.blit(victory_text, victory_rect)

        # Landmark reached (fade in after victory)
        if phase > 0.2:
            landmark_alpha = int(min((phase - 0.2) / 0.3, 1.0) * 255)
            landmark_text = self.medium_font.render(f'You reached {self.landmark}!', True, WHITE)
            landmark_text.set_alpha(landmark_alpha)
            landmark_rect = landmark_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(landmark_text, landmark_rect)

        # City specific celebration elements
        if self.city == 'boston':
            # Baseball confetti
            if phase > 0.4:
                self.draw_confetti(screen, (50, 200, 50))  # Green for Green Monster

        elif self.city == 'nyc':
            # Neon lights effect
            if phase > 0.4:
                self.draw_neon_flash(screen)

        elif self.city == 'chicago':
            # Reflective shine effect
            if phase > 0.4:
                self.draw_shine_effect(screen)

        # Continue prompt (fade in at end)
        if phase > 0.6:
            prompt_alpha = int(min((phase - 0.6) / 0.4, 1.0) * 255)
            prompt_text = self.small_font.render('Press ENTER to continue', True, WHITE)
            prompt_text.set_alpha(prompt_alpha)
            prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
            screen.blit(prompt_text, prompt_rect)

    def draw_confetti(self, screen, color):
        """Draw confetti particles."""
        import random
        for _ in range(20):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            size = random.randint(3, 8)
            pygame.draw.circle(screen, color, (x, y), size)

    def draw_neon_flash(self, screen):
        """Draw neon flashing effect."""
        flash_intensity = int((pygame.time.get_ticks() % 500) / 500 * 100)
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(NYC_COLORS['electric_blue'])
        overlay.set_alpha(flash_intensity)
        screen.blit(overlay, (0, 0))

    def draw_shine_effect(self, screen):
        """Draw reflective shine effect."""
        shine_width = 100
        shine_x = (pygame.time.get_ticks() % 3000) / 3000 * (SCREEN_WIDTH + shine_width * 2) - shine_width
        for i in range(shine_width):
            alpha = int((1 - abs(i - shine_width // 2) / (shine_width // 2)) * 100)
            pygame.draw.line(screen, (255, 255, 255, alpha), (shine_x + i, 0), (shine_x + i, SCREEN_HEIGHT), 1)
