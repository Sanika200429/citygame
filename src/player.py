# the player character class

import pygame
from src.entities.entity import Entity
from src.utils.asset_loader import asset_loader
from config import *


class Player(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

        # movement stuff
        self.speed = PLAYER_SPEED
        self.jump_strength = PLAYER_JUMP_STRENGTH
        self.is_jumping = False
        self.can_double_jump = False
        self.has_double_jumped = False

        # health and points
        self.health = PLAYER_MAX_HEALTH
        self.score = 0
        self.invincible = False
        self.invincibility_timer = 0

        # animation state tracking
        self.animation_state = 'idle'
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 100  # ms per frame

        # powerups currently active
        self.active_powerups = {}

        self.load_sprites()

    def load_sprites(self):
        # load all the animation frames
        self.animations = {
            'idle': asset_loader.load_animation_frames(
                'player/idle', 'idle_', 4, (self.width, self.height), BLUE
            ),
            'run': asset_loader.load_animation_frames(
                'player/run', 'run_', 6, (self.width, self.height), BLUE
            ),
            'jump': asset_loader.load_animation_frames(
                'player/jump', 'jump_', 3, (self.width, self.height), BLUE
            ),
            'hurt': asset_loader.load_animation_frames(
                'player/hurt', 'hurt_', 2, (self.width, self.height), RED
            ),
        }

        # start with idle animation
        self.image = self.animations['idle'][0]

    def handle_input(self, keys, dt):
        # check what keys are pressed
        moving = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
            self.facing_right = False
            moving = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
            self.facing_right = True
            moving = True
        else:
            # slow down when not moving
            self.vel_x *= PLAYER_FRICTION
            if abs(self.vel_x) < 0.1:
                self.vel_x = 0

        # sprint when holding shift
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            if moving:
                self.vel_x *= PLAYER_SPRINT_MULTIPLIER

        # jump controls
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            self.jump()

        # figure out which animation to show
        if not self.on_ground:
            self.animation_state = 'jump'
        elif moving:
            self.animation_state = 'run'
        else:
            self.animation_state = 'idle'

    def jump(self):
        # jump from ground
        if self.on_ground and not self.is_jumping:
            self.vel_y = self.jump_strength
            self.is_jumping = True
            self.on_ground = False
            self.has_double_jumped = False
        elif self.can_double_jump and not self.has_double_jumped and not self.on_ground:
            # double jump if we have the powerup
            self.vel_y = self.jump_strength * 0.8
            self.has_double_jumped = True

    def update(self, dt, platforms):
        # apply gravity
        self.apply_gravity(PLAYER_GRAVITY)

        # move the player
        self.x += self.vel_x
        self.y += self.vel_y

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        # check if hitting platforms
        self.check_platform_collision(platforms)

        # don't go off left side of screen
        if self.rect.left < 0:
            self.rect.left = 0
            self.x = self.rect.x
            self.vel_x = 0

        # handle invincibility timer
        if self.invincible:
            self.invincibility_timer -= dt
            if self.invincibility_timer <= 0:
                self.invincible = False

        self.update_powerups(dt)
        self.update_animation(dt)

    def check_platform_collision(self, platforms):
        if platforms is None:
            # just use ground if no platforms
            if self.rect.bottom >= SCREEN_HEIGHT - 100:
                self.rect.bottom = SCREEN_HEIGHT - 100
                self.y = self.rect.y
                self.vel_y = 0
                self.on_ground = True
                self.is_jumping = False
            else:
                self.on_ground = False
            return

        # check all platforms
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform):
                # landing on top
                if self.vel_y > 0 and self.rect.bottom <= platform.top + 15:
                    self.rect.bottom = platform.top
                    self.y = self.rect.y
                    self.vel_y = 0
                    self.on_ground = True
                    self.is_jumping = False
                # bonk your head on ceiling
                elif self.vel_y < 0 and self.rect.top >= platform.bottom - 15:
                    self.rect.top = platform.bottom
                    self.y = self.rect.y
                    self.vel_y = 0

    def take_damage(self, amount=1):
        if self.invincible:
            return

        self.health -= amount
        if self.health < 0:
            self.health = 0

        # can't get hit again for a bit
        self.invincible = True
        self.invincibility_timer = PLAYER_INVINCIBILITY_TIME

        # knock back a little
        self.vel_y = -5

    def collect_item(self, item_type):
        points = COLLECTIBLE_VALUES.get(item_type, 10)

        # double points if we have the multiplier
        if 'score_multiplier' in self.active_powerups:
            points *= 2

        self.score += points
        return points

    def activate_powerup(self, powerup_type):
        duration = POWERUP_DURATION.get(powerup_type, 10000)
        self.active_powerups[powerup_type] = duration

        if powerup_type == 'double_jump':
            self.can_double_jump = True

    def update_powerups(self, dt):
        """Update active power-up timers."""
        expired = []
        for powerup_type, remaining_time in self.active_powerups.items():
            remaining_time -= dt
            if remaining_time <= 0:
                expired.append(powerup_type)
            else:
                self.active_powerups[powerup_type] = remaining_time

        # Remove expired power-ups
        for powerup_type in expired:
            del self.active_powerups[powerup_type]
            if powerup_type == 'double_jump':
                self.can_double_jump = False

    def update_animation(self, dt):
        """Update animation frame."""
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_frame += 1

            # Get current animation frames
            current_anim = self.animations.get(self.animation_state, self.animations['idle'])

            # Reset frame based on animation length
            if self.animation_frame >= len(current_anim):
                if self.animation_state == 'jump':
                    self.animation_frame = len(current_anim) - 1  # Hold on last frame
                else:
                    self.animation_frame = 0

            # Update image
            self.image = current_anim[self.animation_frame]

            # Flip image if facing left
            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, screen, camera_offset=0):
        """Draw player with invincibility flashing."""
        if self.invincible:
            # Flash by only drawing on even frames
            if (pygame.time.get_ticks() // 100) % 2 == 0:
                return

        super().draw(screen, camera_offset)

        # Draw health
        self.draw_health(screen)

    def draw_health(self, screen):
        """Draw health hearts in top-left corner."""
        heart_size = 30
        spacing = 35
        start_x = 20
        start_y = 20

        for i in range(PLAYER_MAX_HEALTH):
            x = start_x + i * spacing
            color = RED if i < self.health else (100, 100, 100)
            # Draw simple heart shape (placeholder)
            pygame.draw.circle(screen, color, (x, start_y), heart_size // 3)
            pygame.draw.circle(screen, color, (x + heart_size // 3, start_y), heart_size // 3)
            pygame.draw.polygon(screen, color, [
                (x - heart_size // 3, start_y),
                (x + heart_size // 1.5, start_y),
                (x + heart_size // 6, start_y + heart_size // 2)
            ])

    def reset_position(self, x, y):
        """Reset player to a checkpoint position."""
        self.x = x
        self.y = y
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.vel_x = 0
        self.vel_y = 0

    def is_dead(self):
        """Check if player is dead."""
        return self.health <= 0
