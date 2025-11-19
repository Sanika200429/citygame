"""
Main gameplay state - active level play.
"""

import pygame
from src.states.state import State
from src.player import Player
from src.camera import Camera
from src.levels.boston import BostonLevel
from src.levels.nyc import NYCLevel
from src.levels.chicago import ChicagoLevel
from config import *


class Gameplay(State):
    """Active gameplay state."""

    def __init__(self, game):
        super().__init__(game)
        self.player = None
        self.camera = None
        self.level = None
        self.paused = False

        # UI
        self.ui_font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 60)

    def enter_state(self):
        """Set up the level when entering gameplay."""
        # Load appropriate level
        city = self.game.current_city if hasattr(self.game, 'current_city') else 'boston'

        if city == 'boston':
            self.level = BostonLevel()
        elif city == 'nyc':
            self.level = NYCLevel()
        elif city == 'chicago':
            self.level = ChicagoLevel()
        else:
            self.level = BostonLevel()

        # Create player
        self.player = Player(100, SCREEN_HEIGHT - 200)

        # Create camera
        self.camera = Camera(self.level.level_width)

    def handle_events(self, events):
        """Handle gameplay input."""
        super().handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and self.player.is_dead():
                    # Restart level
                    self.enter_state()

    def update(self, dt):
        """Update gameplay."""
        if self.paused or self.player.is_dead():
            return

        # Get player input
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys, dt)

        # Update player
        self.player.update(dt, self.level.platforms)

        # Update level
        self.level.update(dt)

        # Check collectibles
        self.level.check_collectible_collision(self.player)

        # Check enemy collisions
        self.level.check_enemy_collision(self.player)

        # Check checkpoints
        checkpoint_idx, checkpoint_x = self.level.check_checkpoint(self.player)
        if checkpoint_idx is not None:
            print(f"Checkpoint {checkpoint_idx + 1} reached!")

        # Check landmark
        if self.level.check_landmark_reached(self.player):
            self.next_state = 'landmark'
            self.done = True

        # Update camera
        self.camera.update(self.player)

        # Check if player fell off map
        if self.player.rect.y > SCREEN_HEIGHT + 100:
            self.respawn_player()

    def respawn_player(self):
        """Respawn player at last checkpoint."""
        x, y = self.level.get_respawn_position()
        self.player.reset_position(x, y)
        self.player.take_damage(1)

    def draw(self, screen):
        """Draw gameplay."""
        camera_x, camera_y = self.camera.get_offset()

        # Draw level
        self.level.draw(screen, camera_x)

        # Draw player
        self.player.draw(screen, camera_x)

        # Draw UI
        self.draw_ui(screen)

        # Draw pause overlay
        if self.paused:
            self.draw_pause_overlay(screen)

        # Draw death overlay
        if self.player.is_dead():
            self.draw_death_overlay(screen)

    def draw_ui(self, screen):
        """Draw HUD elements."""
        # Score
        score_text = self.ui_font.render(f'Score: {self.player.score}', True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH - 220, 20))

        # City name
        city_name = CITY_NAMES.get(self.game.current_city if hasattr(self.game, 'current_city') else 'boston', 'Boston')
        city_text = self.ui_font.render(city_name, True, WHITE)
        city_rect = city_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
        screen.blit(city_text, city_rect)

        # Progress bar (simple)
        progress = self.player.rect.x / self.level.level_width
        bar_width = 300
        bar_height = 20
        bar_x = SCREEN_WIDTH // 2 - bar_width // 2
        bar_y = 60

        pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, int(bar_width * progress), bar_height))
        pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)

    def draw_pause_overlay(self, screen):
        """Draw pause menu overlay."""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(180)
        screen.blit(overlay, (0, 0))

        # Pause text
        pause_text = self.big_font.render('PAUSED', True, WHITE)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(pause_text, pause_rect)

        # Instructions
        continue_text = self.ui_font.render('Press ESC to Continue', True, WHITE)
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(continue_text, continue_rect)

    def draw_death_overlay(self, screen):
        """Draw death/game over overlay."""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(200)
        screen.blit(overlay, (0, 0))

        # Game over text
        game_over_text = self.big_font.render('GAME OVER', True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(game_over_text, game_over_rect)

        # Score
        score_text = self.ui_font.render(f'Final Score: {self.player.score}', True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(score_text, score_rect)

        # Restart instruction
        restart_text = self.ui_font.render('Press R to Restart', True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
        screen.blit(restart_text, restart_rect)
