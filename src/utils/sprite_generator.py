"""
Programmatic sprite generator for creating better-looking placeholder graphics.
Creates actual shapes and designs instead of simple colored rectangles.
"""

import pygame
import math
import random
from config import *


def draw_player_idle(width, height):
    """Draw a player character in idle pose."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Colors
    skin = (255, 220, 177)
    shirt = (70, 130, 180)
    pants = (50, 50, 100)
    shoes = (60, 40, 20)

    # Body proportions
    head_size = width // 3
    body_height = height // 2
    leg_height = height // 4

    # Head
    pygame.draw.circle(surface, skin, (width // 2, head_size), head_size - 2)

    # Eyes
    eye_y = head_size - 2
    pygame.draw.circle(surface, BLACK, (width // 2 - 4, eye_y), 2)
    pygame.draw.circle(surface, BLACK, (width // 2 + 4, eye_y), 2)

    # Smile
    pygame.draw.arc(surface, BLACK, (width // 3, head_size - 2, width // 3, 8), 0, 3.14, 1)

    # Body (shirt)
    body_rect = pygame.Rect(width // 4, head_size * 2 - 4, width // 2, body_height)
    pygame.draw.rect(surface, shirt, body_rect)
    pygame.draw.rect(surface, (50, 100, 150), body_rect, 1)

    # Arms
    arm_y = head_size * 2
    pygame.draw.line(surface, shirt, (width // 4, arm_y), (2, arm_y + 8), 3)
    pygame.draw.line(surface, shirt, (width * 3 // 4, arm_y), (width - 2, arm_y + 8), 3)

    # Legs (pants)
    leg_start = head_size * 2 + body_height
    leg_width = width // 5
    pygame.draw.rect(surface, pants, (width // 3, leg_start, leg_width, leg_height))
    pygame.draw.rect(surface, pants, (width // 2, leg_start, leg_width, leg_height))

    # Shoes
    pygame.draw.rect(surface, shoes, (width // 3 - 2, leg_start + leg_height - 4, leg_width + 2, 4))
    pygame.draw.rect(surface, shoes, (width // 2 - 2, leg_start + leg_height - 4, leg_width + 2, 4))

    return surface


def draw_player_run(width, height, frame):
    """Draw a player character in running pose."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Colors
    skin = (255, 220, 177)
    shirt = (70, 130, 180)
    pants = (50, 50, 100)
    shoes = (60, 40, 20)

    # Animation offset
    bob = int(math.sin(frame * math.pi / 3) * 2)
    leg_offset = int(math.sin(frame * math.pi / 3) * 5)

    # Body proportions
    head_size = width // 3
    body_height = height // 2
    leg_height = height // 4

    # Head (bobbing)
    pygame.draw.circle(surface, skin, (width // 2, head_size + bob), head_size - 2)

    # Eyes
    eye_y = head_size - 2 + bob
    pygame.draw.circle(surface, BLACK, (width // 2 - 4, eye_y), 2)
    pygame.draw.circle(surface, BLACK, (width // 2 + 4, eye_y), 2)

    # Body (shirt)
    body_rect = pygame.Rect(width // 4, head_size * 2 - 4 + bob, width // 2, body_height)
    pygame.draw.rect(surface, shirt, body_rect)

    # Arms (swinging)
    arm_y = head_size * 2 + bob
    arm_swing = leg_offset
    pygame.draw.line(surface, shirt, (width // 4, arm_y), (2, arm_y + 8 - arm_swing), 3)
    pygame.draw.line(surface, shirt, (width * 3 // 4, arm_y), (width - 2, arm_y + 8 + arm_swing), 3)

    # Legs (running)
    leg_start = head_size * 2 + body_height + bob
    leg_width = width // 5
    pygame.draw.rect(surface, pants, (width // 3, leg_start + leg_offset, leg_width, leg_height - abs(leg_offset)))
    pygame.draw.rect(surface, pants, (width // 2, leg_start - leg_offset, leg_width, leg_height - abs(leg_offset)))

    return surface


def draw_player_jump(width, height):
    """Draw a player character in jump pose."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Colors
    skin = (255, 220, 177)
    shirt = (70, 130, 180)
    pants = (50, 50, 100)

    # Body proportions
    head_size = width // 3
    body_height = height // 2

    # Head
    pygame.draw.circle(surface, skin, (width // 2, head_size), head_size - 2)

    # Eyes (surprised)
    eye_y = head_size - 2
    pygame.draw.circle(surface, BLACK, (width // 2 - 4, eye_y), 3)
    pygame.draw.circle(surface, BLACK, (width // 2 + 4, eye_y), 3)

    # Body (shirt)
    body_rect = pygame.Rect(width // 4, head_size * 2 - 4, width // 2, body_height)
    pygame.draw.rect(surface, shirt, body_rect)

    # Arms (up)
    arm_y = head_size * 2
    pygame.draw.line(surface, shirt, (width // 4, arm_y), (2, arm_y - 10), 3)
    pygame.draw.line(surface, shirt, (width * 3 // 4, arm_y), (width - 2, arm_y - 10), 3)

    # Legs (tucked)
    leg_start = head_size * 2 + body_height
    pygame.draw.rect(surface, pants, (width // 3, leg_start, width // 3, 8))

    return surface


def draw_pigeon(width, height):
    """Draw a pigeon enemy."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Colors
    body_color = (150, 150, 150)
    wing_color = (120, 120, 120)
    beak_color = (200, 150, 50)

    # Body
    pygame.draw.ellipse(surface, body_color, (5, height // 3, width - 10, height // 2))

    # Head
    pygame.draw.circle(surface, body_color, (width - 8, height // 3 + 5), 6)

    # Beak
    beak_points = [(width - 3, height // 3 + 5), (width - 1, height // 3 + 3), (width - 1, height // 3 + 7)]
    pygame.draw.polygon(surface, beak_color, beak_points)

    # Eye
    pygame.draw.circle(surface, BLACK, (width - 7, height // 3 + 4), 1)

    # Wing
    pygame.draw.ellipse(surface, wing_color, (8, height // 3 + 3, width // 2, height // 3))

    # Tail
    tail_points = [(5, height // 2), (2, height // 2 + 5), (5, height // 2 + 8)]
    pygame.draw.polygon(surface, wing_color, tail_points)

    return surface


def draw_taxi(width, height):
    """Draw a taxi enemy."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Colors
    body_color = (255, 215, 0)
    window_color = (100, 150, 200)
    tire_color = (40, 40, 40)

    # Car body
    car_rect = pygame.Rect(5, height // 3, width - 10, height // 2)
    pygame.draw.rect(surface, body_color, car_rect, border_radius=3)
    pygame.draw.rect(surface, (200, 170, 0), car_rect, 2, border_radius=3)

    # Roof
    roof_rect = pygame.Rect(width // 4, height // 6, width // 2, height // 3)
    pygame.draw.rect(surface, body_color, roof_rect, border_radius=2)

    # Windows
    pygame.draw.rect(surface, window_color, (width // 4 + 3, height // 6 + 2, width // 4 - 3, height // 4))
    pygame.draw.rect(surface, window_color, (width // 2 + 2, height // 6 + 2, width // 4 - 5, height // 4))

    # Wheels
    pygame.draw.circle(surface, tire_color, (width // 4, height * 3 // 4), 5)
    pygame.draw.circle(surface, tire_color, (width * 3 // 4, height * 3 // 4), 5)
    pygame.draw.circle(surface, (80, 80, 80), (width // 4, height * 3 // 4), 3)
    pygame.draw.circle(surface, (80, 80, 80), (width * 3 // 4, height * 3 // 4), 3)

    # Headlight
    pygame.draw.circle(surface, WHITE, (width - 8, height // 2), 2)

    return surface


def draw_rat(width, height):
    """Draw a rat enemy."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Colors
    body_color = (80, 60, 60)
    ear_color = (100, 80, 80)

    # Body
    pygame.draw.ellipse(surface, body_color, (3, height // 3, width - 8, height // 2))

    # Head
    pygame.draw.circle(surface, body_color, (width - 6, height // 2), 5)

    # Ears
    pygame.draw.circle(surface, ear_color, (width - 8, height // 3), 3)
    pygame.draw.circle(surface, ear_color, (width - 4, height // 3), 3)

    # Eye
    pygame.draw.circle(surface, (200, 50, 50), (width - 5, height // 2), 1)

    # Tail
    tail_points = [(3, height // 2), (1, height * 2 // 3), (2, height - 3)]
    pygame.draw.lines(surface, body_color, False, tail_points, 2)

    # Feet
    pygame.draw.line(surface, body_color, (width // 2, height * 2 // 3), (width // 2 - 2, height - 2), 2)
    pygame.draw.line(surface, body_color, (width * 2 // 3, height * 2 // 3), (width * 2 // 3 + 2, height - 2), 2)

    return surface


def draw_cyclist(width, height):
    """Draw a cyclist enemy."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Colors
    skin = (255, 220, 177)
    shirt = (200, 100, 50)

    # Head
    pygame.draw.circle(surface, skin, (width * 2 // 3, height // 4), 6)

    # Eye
    pygame.draw.circle(surface, BLACK, (width * 2 // 3 + 2, height // 4), 1)

    # Body
    pygame.draw.line(surface, shirt, (width * 2 // 3, height // 4 + 6), (width // 2, height // 2), 4)

    # Arms (on handlebars)
    pygame.draw.line(surface, shirt, (width * 2 // 3, height // 3), (width // 3, height // 2), 3)

    # Bike frame
    bike_color = (100, 100, 100)
    pygame.draw.line(surface, bike_color, (width // 4, height * 3 // 4), (width * 3 // 4, height * 3 // 4), 2)
    pygame.draw.line(surface, bike_color, (width // 2, height // 2), (width // 4, height * 3 // 4), 2)
    pygame.draw.line(surface, bike_color, (width // 2, height // 2), (width * 3 // 4, height * 3 // 4), 2)

    # Wheels
    pygame.draw.circle(surface, BLACK, (width // 4, height * 3 // 4), 8, 2)
    pygame.draw.circle(surface, BLACK, (width * 3 // 4, height * 3 // 4), 8, 2)

    return surface


def draw_vendor(width, height):
    """Draw a street vendor enemy."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Colors
    skin = (200, 150, 100)
    apron = (100, 180, 100)
    cart = (139, 90, 60)

    # Head
    pygame.draw.circle(surface, skin, (width // 3, height // 4), 7)

    # Hat
    pygame.draw.rect(surface, (80, 80, 80), (width // 3 - 8, height // 4 - 10, 16, 4))
    pygame.draw.ellipse(surface, (80, 80, 80), (width // 3 - 6, height // 4 - 8, 12, 6))

    # Body (apron)
    pygame.draw.rect(surface, apron, (width // 3 - 8, height // 4 + 7, 16, height // 3))

    # Cart
    pygame.draw.rect(surface, cart, (width // 2, height // 2, width // 2 - 5, height // 3))

    # Umbrella
    umbrella_points = [(width // 2, height // 4), (width - 5, height // 3), (width // 2 + 5, height // 3)]
    pygame.draw.polygon(surface, (200, 50, 50), umbrella_points)

    # Wheels
    pygame.draw.circle(surface, BLACK, (width * 2 // 3, height * 4 // 5), 4)

    return surface


def draw_flying_paper(width, height):
    """Draw a flying paper enemy."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Paper
    paper_color = (240, 240, 240)
    pygame.draw.rect(surface, paper_color, (2, 2, width - 4, height - 4), border_radius=2)
    pygame.draw.rect(surface, (180, 180, 180), (2, 2, width - 4, height - 4), 1, border_radius=2)

    # Text lines
    line_color = (100, 100, 100)
    for i in range(3):
        y = 6 + i * 5
        pygame.draw.line(surface, line_color, (5, y), (width - 5, y), 1)

    # Wind lines
    wind_color = (200, 220, 255)
    pygame.draw.line(surface, wind_color, (0, height // 3), (5, height // 3), 1)
    pygame.draw.line(surface, wind_color, (0, height * 2 // 3), (5, height * 2 // 3), 1)

    return surface


def draw_collectible_pizza(width, height):
    """Draw a pizza slice collectible."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Crust color
    crust = (255, 200, 100)
    cheese = (255, 230, 150)
    sauce = (200, 50, 50)

    # Pizza slice triangle
    points = [(width // 2, 2), (width - 2, height - 2), (2, height - 2)]
    pygame.draw.polygon(surface, cheese, points)
    pygame.draw.polygon(surface, crust, points, 2)

    # Sauce spots
    pygame.draw.circle(surface, sauce, (width // 2, height // 2), 2)
    pygame.draw.circle(surface, sauce, (width // 3, height * 2 // 3), 2)
    pygame.draw.circle(surface, sauce, (width * 2 // 3, height * 2 // 3), 2)

    # Pepperoni
    pygame.draw.circle(surface, (180, 30, 30), (width // 2, height * 3 // 5), 3)

    return surface


def draw_collectible_teacup(width, height):
    """Draw a teacup collectible."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Cup colors
    cup_color = (200, 100, 150)

    # Cup body
    cup_points = [(6, height * 2 // 3), (width - 6, height * 2 // 3), (width - 4, height - 4), (4, height - 4)]
    pygame.draw.polygon(surface, cup_color, cup_points)
    pygame.draw.polygon(surface, (180, 80, 130), cup_points, 2)

    # Handle
    pygame.draw.arc(surface, cup_color, (width - 10, height // 2, 8, height // 3), -1.5, 1.5, 2)

    # Saucer
    pygame.draw.ellipse(surface, cup_color, (2, height - 6, width - 4, 4))

    # Steam
    steam_color = (200, 200, 220)
    pygame.draw.line(surface, steam_color, (width // 3, height // 3), (width // 3 - 2, height // 6), 1)
    pygame.draw.line(surface, steam_color, (width // 2, height // 3), (width // 2, height // 6), 1)
    pygame.draw.line(surface, steam_color, (width * 2 // 3, height // 3), (width * 2 // 3 + 2, height // 6), 1)

    return surface


def draw_collectible_hot_dog(width, height):
    """Draw a hot dog collectible."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Colors
    bun = (210, 180, 140)
    sausage = (180, 100, 80)
    mustard = (255, 215, 0)

    # Bottom bun
    pygame.draw.ellipse(surface, bun, (2, height // 2, width - 4, height // 2 - 2))

    # Sausage
    pygame.draw.ellipse(surface, sausage, (4, height // 3, width - 8, height // 3))

    # Top bun
    pygame.draw.ellipse(surface, bun, (2, 2, width - 4, height // 2))

    # Mustard zigzag
    pygame.draw.line(surface, mustard, (6, height // 2), (width // 3, height // 2 - 2), 2)
    pygame.draw.line(surface, mustard, (width // 3, height // 2 - 2), (width * 2 // 3, height // 2 + 2), 2)
    pygame.draw.line(surface, mustard, (width * 2 // 3, height // 2 + 2), (width - 6, height // 2), 2)

    return surface


def draw_collectible_book(width, height):
    """Draw a book collectible."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Book cover
    cover = (139, 69, 19)
    pygame.draw.rect(surface, cover, (4, 2, width - 8, height - 4), border_radius=2)
    pygame.draw.rect(surface, (100, 50, 10), (4, 2, width - 8, height - 4), 2, border_radius=2)

    # Pages (white edge)
    pygame.draw.rect(surface, WHITE, (width - 6, 4, 2, height - 8))

    # Title lines
    pygame.draw.line(surface, (200, 150, 100), (8, height // 3), (width - 10, height // 3), 1)
    pygame.draw.line(surface, (200, 150, 100), (8, height // 2), (width - 10, height // 2), 1)

    return surface


def draw_collectible_bagel(width, height):
    """Draw a bagel collectible."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Bagel color
    bagel = (210, 180, 140)

    # Outer circle
    pygame.draw.circle(surface, bagel, (width // 2, height // 2), width // 2 - 2)
    pygame.draw.circle(surface, (180, 150, 110), (width // 2, height // 2), width // 2 - 2, 2)

    # Inner circle (hole)
    pygame.draw.circle(surface, BLACK, (width // 2, height // 2), width // 4)
    pygame.draw.circle(surface, (180, 150, 110), (width // 2, height // 2), width // 4, 1)

    # Sesame seeds
    seed_color = (230, 200, 150)
    for angle in range(0, 360, 45):
        x = width // 2 + int(width // 3 * math.cos(math.radians(angle)))
        y = height // 2 + int(height // 3 * math.sin(math.radians(angle)))
        pygame.draw.circle(surface, seed_color, (x, y), 1)

    return surface


def draw_collectible_metrocard(width, height):
    """Draw a metrocard collectible."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Card
    card_color = (255, 215, 0)
    pygame.draw.rect(surface, card_color, (2, 4, width - 4, height - 8), border_radius=2)
    pygame.draw.rect(surface, (200, 170, 0), (2, 4, width - 4, height - 8), 1, border_radius=2)

    # Magnetic stripe
    pygame.draw.rect(surface, BLACK, (2, height // 2 - 2, width - 4, 3))

    # "M" logo
    pygame.draw.circle(surface, (0, 100, 200), (width // 2, height // 3), 4)
    pygame.draw.line(surface, WHITE, (width // 2 - 2, height // 3), (width // 2 + 2, height // 3), 1)

    return surface


def draw_collectible_jazz_note(width, height):
    """Draw a jazz note collectible."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Note color
    note_color = (138, 43, 226)

    # Note head
    pygame.draw.ellipse(surface, note_color, (4, height * 2 // 3, 8, 6))

    # Note stem
    pygame.draw.rect(surface, note_color, (11, height // 4, 2, height // 2))

    # Note flag
    flag_points = [(13, height // 4), (width - 4, height // 3), (13, height // 3 + 4)]
    pygame.draw.polygon(surface, note_color, flag_points)

    # Musical staff lines
    staff_color = (180, 140, 220)
    for i in range(3):
        y = height // 2 + i * 4
        pygame.draw.line(surface, staff_color, (0, y), (width, y), 1)

    return surface


def create_boston_background(width, height):
    """Create a highly detailed Boston autumn background."""
    surface = pygame.Surface((width, height))

    # Autumn sky gradient (warm peachy tones)
    top_color = (244, 200, 180)
    mid_color = (248, 220, 195)
    bottom_color = (244, 232, 208)

    # Draw sky gradient with smoother transition
    for y in range(height):
        if y < height // 2:
            progress = y / (height // 2)
            r = int(top_color[0] + (mid_color[0] - top_color[0]) * progress)
            g = int(top_color[1] + (mid_color[1] - top_color[1]) * progress)
            b = int(top_color[2] + (mid_color[2] - top_color[2]) * progress)
        else:
            progress = (y - height // 2) / (height // 2)
            r = int(mid_color[0] + (bottom_color[0] - mid_color[0]) * progress)
            g = int(mid_color[1] + (bottom_color[1] - mid_color[1]) * progress)
            b = int(mid_color[2] + (bottom_color[2] - mid_color[2]) * progress)
        pygame.draw.line(surface, (r, g, b), (0, y), (width, y))

    # Add clouds
    cloud_color = (255, 240, 230, 128)
    cloud_positions = [(150, 80), (400, 120), (700, 60), (950, 100), (1100, 85)]
    for cx, cy in cloud_positions:
        for i in range(5):
            x_offset = (i - 2) * 20
            radius = 15 + (2 - abs(i - 2)) * 5
            temp_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(temp_surf, cloud_color, (radius, radius), radius)
            surface.blit(temp_surf, (cx + x_offset - radius, cy - radius))

    # Distant hills/treeline
    hill_color = (150, 120, 100)
    hill_points = [(0, 450), (200, 420), (400, 440), (600, 410), (800, 435), (1000, 415), (1280, 430), (1280, 720), (0, 720)]
    pygame.draw.polygon(surface, hill_color, hill_points)

    # Historic buildings (varied heights and styles)
    buildings = [
        # Old brick buildings
        {'x': 50, 'y': 480, 'w': 90, 'h': 240, 'color': (160, 70, 58), 'style': 'brick'},
        {'x': 150, 'y': 450, 'w': 110, 'h': 270, 'color': (180, 85, 65), 'style': 'brick'},
        {'x': 270, 'y': 490, 'w': 85, 'h': 230, 'color': (170, 75, 60), 'style': 'brick'},
        {'x': 365, 'y': 420, 'w': 100, 'h': 300, 'color': (165, 80, 62), 'style': 'church'},
        {'x': 475, 'y': 460, 'w': 95, 'h': 260, 'color': (175, 78, 63), 'style': 'brick'},
        {'x': 580, 'y': 440, 'w': 105, 'h': 280, 'color': (158, 72, 55), 'style': 'brick'},
        {'x': 695, 'y': 470, 'w': 88, 'h': 250, 'color': (172, 82, 64), 'style': 'brick'},
        {'x': 793, 'y': 435, 'w': 115, 'h': 285, 'color': (168, 76, 60), 'style': 'tall'},
        {'x': 918, 'y': 455, 'w': 92, 'h': 265, 'color': (163, 73, 58), 'style': 'brick'},
        {'x': 1020, 'y': 475, 'w': 98, 'h': 245, 'color': (177, 84, 66), 'style': 'brick'},
        {'x': 1128, 'y': 445, 'w': 105, 'h': 275, 'color': (161, 74, 59), 'style': 'brick'},
    ]

    for building in buildings:
        x, y, w, h = building['x'], building['y'], building['w'], building['h']
        color = building['color']

        # Building body
        pygame.draw.rect(surface, color, (x, y, w, h))
        # Darker outline
        pygame.draw.rect(surface, (color[0] - 30, color[1] - 20, color[2] - 15), (x, y, w, h), 2)

        # Special features
        if building['style'] == 'church':
            # Church steeple
            steeple_points = [(x + w // 2 - 15, y), (x + w // 2 + 15, y), (x + w // 2, y - 50)]
            pygame.draw.polygon(surface, color, steeple_points)
            pygame.draw.circle(surface, (200, 180, 150), (x + w // 2, y - 20), 8)

        # Windows (Colonial style - more frequent on upper floors)
        window_lit = (255, 245, 200)
        window_dark = (100, 80, 60)
        window_cream = (240, 230, 200)

        for row in range(4, h - 10, 18):
            for col in range(8, w - 8, 16):
                wx = x + col
                wy = y + row

                # Vary window colors (some lit, some dark, some cream curtains)
                import random
                random.seed(wx + wy)  # Consistent random
                choice = random.random()
                if choice < 0.3:
                    win_color = window_lit
                elif choice < 0.6:
                    win_color = window_cream
                else:
                    win_color = window_dark

                # Window frame
                pygame.draw.rect(surface, win_color, (wx, wy, 9, 12))
                pygame.draw.rect(surface, (80, 60, 50), (wx, wy, 9, 12), 1)
                # Window cross divider
                pygame.draw.line(surface, (80, 60, 50), (wx + 4, wy), (wx + 4, wy + 12), 1)
                pygame.draw.line(surface, (80, 60, 50), (wx, wy + 6), (wx + 9, wy + 6), 1)

        # Roof details
        roof_color = (90, 70, 65)
        if building['style'] == 'tall':
            # Flat roof with decorative top
            pygame.draw.rect(surface, roof_color, (x - 3, y - 5, w + 6, 5))
        else:
            # Slanted roof
            roof_points = [(x - 3, y), (x + w + 3, y), (x + w + 8, y - 12), (x - 8, y - 12)]
            pygame.draw.polygon(surface, roof_color, roof_points)

    # Add autumn trees (colorful leaves)
    tree_positions = [(120, 600), (340, 610), (560, 605), (780, 608), (950, 602), (1150, 606)]
    for tx, ty in tree_positions:
        # Trunk
        trunk_color = (80, 60, 50)
        pygame.draw.rect(surface, trunk_color, (tx - 4, ty, 8, 120))

        # Leaves (autumn colors - red, orange, yellow mix)
        leaf_colors = [(200, 50, 40), (230, 120, 30), (255, 180, 50), (180, 90, 40)]
        for i, leaf_color in enumerate(leaf_colors):
            offset_x = (i % 2) * 15 - 7
            offset_y = (i // 2) * 12 - 12
            pygame.draw.circle(surface, leaf_color, (tx + offset_x, ty - 15 + offset_y), 18)

        # Some falling leaves
        for i in range(3):
            import random
            random.seed(tx + i)
            leaf_x = tx + random.randint(-30, 30)
            leaf_y = ty + random.randint(20, 100)
            leaf_c = random.choice(leaf_colors)
            # Small leaf shape
            pygame.draw.ellipse(surface, leaf_c, (leaf_x, leaf_y, 4, 6))

    # Lamp posts
    lamp_positions = [220, 520, 820, 1050]
    for lx in lamp_positions:
        # Post
        pygame.draw.rect(surface, (40, 40, 40), (lx - 2, 560, 4, 160))
        # Top horizontal bar
        pygame.draw.rect(surface, (40, 40, 40), (lx - 2, 560, 25, 3))
        # Lamp (old gas lamp style)
        pygame.draw.rect(surface, (60, 50, 45), (lx + 18, 563, 14, 20), border_radius=3)
        # Lamp glow
        glow_surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (255, 240, 180, 80), (15, 15), 15)
        surface.blit(glow_surf, (lx + 10, 558))
        # Light beam down
        beam_surf = pygame.Surface((40, 160), pygame.SRCALPHA)
        for i in range(160):
            alpha = int(60 * (1 - i / 160))
            pygame.draw.line(beam_surf, (255, 240, 180, alpha), (20 - i // 8, i), (20 + i // 8, i))
        surface.blit(beam_surf, (lx + 5, 580))

    # Birds in the sky
    bird_color = (80, 60, 50)
    bird_positions = [(300, 150), (450, 180), (650, 140), (900, 170)]
    for bx, by in bird_positions:
        # Simple V-shaped birds
        pygame.draw.line(surface, bird_color, (bx, by), (bx - 4, by - 3), 1)
        pygame.draw.line(surface, bird_color, (bx, by), (bx + 4, by - 3), 1)

    # Multi-layered ground with varied colors

    # Brick sidewalk on left (reddish)
    sidewalk_left_color = (140, 90, 80)
    pygame.draw.rect(surface, sidewalk_left_color, (0, 650, 280, 70))
    # Brick pattern
    for bx in range(0, 280, 20):
        for by in range(650, 720, 10):
            brick_var = random.randint(-15, 15)
            brick_color = (sidewalk_left_color[0] + brick_var,
                          sidewalk_left_color[1] + brick_var,
                          sidewalk_left_color[2] + brick_var)
            pygame.draw.rect(surface, brick_color, (bx, by, 18, 8))
            pygame.draw.rect(surface, (100, 60, 50), (bx, by, 18, 8), 1)

    # Cobblestone street in middle (gray-brown)
    street_base = (110, 105, 95)
    pygame.draw.rect(surface, street_base, (280, 650, 720, 70))
    # Cobblestone texture
    for sx in range(280, 1000, 12):
        for sy in range(650, 720, 12):
            stone_color = (street_base[0] + random.randint(-12, 12),
                          street_base[1] + random.randint(-12, 12),
                          street_base[2] + random.randint(-10, 10))
            pygame.draw.circle(surface, stone_color, (sx + 5, sy + 5), 5)
            pygame.draw.circle(surface, (70, 65, 60), (sx + 5, sy + 5), 5, 1)

    # Granite sidewalk on right (lighter gray)
    sidewalk_right_color = (130, 125, 120)
    pygame.draw.rect(surface, sidewalk_right_color, (1000, 650, 280, 70))
    # Granite tiles
    for gx in range(1000, 1280, 35):
        for gy in range(650, 720, 35):
            tile_var = random.randint(-10, 10)
            tile_color = (sidewalk_right_color[0] + tile_var,
                         sidewalk_right_color[1] + tile_var,
                         sidewalk_right_color[2] + tile_var)
            pygame.draw.rect(surface, tile_color, (gx, gy, 33, 33))
            pygame.draw.rect(surface, (90, 85, 80), (gx, gy, 33, 33), 1)
            # Speckles for granite texture
            for _ in range(5):
                speck_x = gx + random.randint(2, 30)
                speck_y = gy + random.randint(2, 30)
                pygame.draw.circle(surface, (100, 95, 90), (speck_x, speck_y), 1)

    # Add some grates and manholes
    manhole_positions = [450, 750]
    for mx in manhole_positions:
        # Manhole cover
        pygame.draw.circle(surface, (60, 55, 50), (mx, 685), 20)
        pygame.draw.circle(surface, (40, 35, 30), (mx, 685), 18)
        # Pattern on manhole
        for angle in range(0, 360, 45):
            x_end = mx + int(12 * math.cos(math.radians(angle)))
            y_end = 685 + int(12 * math.sin(math.radians(angle)))
            pygame.draw.line(surface, (50, 45, 40), (mx, 685), (x_end, y_end), 1)

    # Curbs between sections
    pygame.draw.rect(surface, (90, 85, 80), (278, 645, 4, 75))  # Left curb
    pygame.draw.rect(surface, (90, 85, 80), (998, 645, 4, 75))  # Right curb

    # Add chimneys with smoke to some buildings
    chimney_positions = [(170, 445), (390, 415), (600, 435), (930, 450), (1050, 470)]
    for chim_x, chim_y in chimney_positions:
        # Chimney brick
        pygame.draw.rect(surface, (140, 70, 60), (chim_x, chim_y, 12, 35))
        pygame.draw.rect(surface, (100, 50, 40), (chim_x, chim_y, 12, 35), 1)
        # Chimney cap
        pygame.draw.rect(surface, (80, 60, 55), (chim_x - 2, chim_y - 3, 16, 3))

        # Smoke (wispy)
        smoke_surf = pygame.Surface((30, 40), pygame.SRCALPHA)
        for i in range(3):
            smoke_y = i * 12
            smoke_alpha = int(60 - i * 15)
            smoke_radius = 4 + i * 2
            pygame.draw.circle(smoke_surf, (200, 200, 210, smoke_alpha),
                             (15 + i * 2, smoke_y), smoke_radius)
        surface.blit(smoke_surf, (chim_x - 5, chim_y - 38))

    # Window flower boxes on some buildings
    flower_box_positions = [
        (65, 520), (95, 540), (165, 490), (195, 510), (285, 530),
        (490, 500), (520, 520), (600, 480), (710, 510), (800, 475),
        (935, 495), (1035, 515), (1145, 485)
    ]
    for fb_x, fb_y in flower_box_positions:
        # Box
        pygame.draw.rect(surface, (101, 67, 33), (fb_x, fb_y, 20, 6))
        # Flowers (small colored dots)
        flower_colors = [(255, 100, 120), (255, 180, 50), (200, 100, 200), (255, 150, 150)]
        random.seed(fb_x + fb_y)
        for i in range(4):
            f_x = fb_x + 3 + i * 4
            f_color = random.choice(flower_colors)
            pygame.draw.circle(surface, f_color, (f_x, fb_y - 2), 2)

    # Store signs and awnings
    store_signs = [
        {'x': 60, 'y': 475, 'text': 'BAKERY', 'color': (220, 180, 140)},
        {'x': 275, 'y': 485, 'text': 'BOOKS', 'color': (180, 140, 100)},
        {'x': 485, 'y': 455, 'text': 'CAFE', 'color': (200, 150, 120)},
        {'x': 705, 'y': 465, 'text': 'PIZZA', 'color': (210, 160, 130)},
        {'x': 925, 'y': 450, 'text': 'DELI', 'color': (190, 150, 110)},
    ]

    for sign in store_signs:
        # Sign background
        sign_width = len(sign['text']) * 8 + 8
        pygame.draw.rect(surface, sign['color'], (sign['x'], sign['y'], sign_width, 18))
        pygame.draw.rect(surface, (100, 70, 50), (sign['x'], sign['y'], sign_width, 18), 1)

        # Simple text representation (dots pattern for letters)
        # Just decorative pattern since we can't render text easily
        for i in range(len(sign['text'])):
            letter_x = sign['x'] + 6 + i * 8
            pygame.draw.rect(surface, (80, 60, 40), (letter_x, sign['y'] + 5, 5, 8))

    # Fire hydrants
    hydrant_positions = [180, 410, 640, 880, 1100]
    for hyd_x in hydrant_positions:
        # Hydrant body
        pygame.draw.rect(surface, (200, 50, 50), (hyd_x, 635, 12, 20))
        # Top cap
        pygame.draw.circle(surface, (180, 45, 45), (hyd_x + 6, 633), 7)
        # Side nozzles
        pygame.draw.circle(surface, (160, 40, 40), (hyd_x + 2, 642), 3)
        pygame.draw.circle(surface, (160, 40, 40), (hyd_x + 10, 642), 3)
        # Base
        pygame.draw.rect(surface, (150, 35, 35), (hyd_x - 1, 655, 14, 3))

    # Parking meters
    meter_positions = [310, 540, 770, 1010]
    for meter_x in meter_positions:
        # Post
        pygame.draw.rect(surface, (80, 80, 85), (meter_x, 620, 3, 35))
        # Meter head
        pygame.draw.rect(surface, (100, 100, 105), (meter_x - 3, 615, 9, 8), border_radius=2)
        # Display (small rectangle)
        pygame.draw.rect(surface, (200, 220, 220), (meter_x - 1, 617, 5, 3))

    # Newspaper boxes
    newsbox_positions = [250, 690, 1150]
    for nb_x in newsbox_positions:
        # Box body
        pygame.draw.rect(surface, (220, 40, 40), (nb_x, 630, 18, 25))
        pygame.draw.rect(surface, (180, 30, 30), (nb_x, 630, 18, 25), 1)
        # Coin slot
        pygame.draw.rect(surface, (100, 100, 100), (nb_x + 7, 635, 4, 1))
        # Window (top half)
        pygame.draw.rect(surface, (240, 240, 250), (nb_x + 2, 632, 14, 10))

    # Trash cans
    trash_positions = [140, 470, 850, 1180]
    for trash_x in trash_positions:
        # Can body
        pygame.draw.rect(surface, (60, 90, 60), (trash_x, 635, 16, 22))
        pygame.draw.circle(surface, (70, 100, 70), (trash_x + 8, 633), 9)
        # Lid
        pygame.draw.ellipse(surface, (50, 80, 50), (trash_x + 2, 630, 12, 5))

    # Bike rack
    bike_rack_positions = [380, 950]
    for rack_x in bike_rack_positions:
        # Rack (inverted U shapes)
        for i in range(3):
            u_x = rack_x + i * 15
            pygame.draw.line(surface, (100, 100, 105), (u_x, 655), (u_x, 640), 2)
            pygame.draw.arc(surface, (100, 100, 105), (u_x - 5, 635, 10, 10), 0, 3.14, 2)

    # Street vendor cart
    cart_x, cart_y = 590, 625
    # Cart body
    pygame.draw.rect(surface, (180, 120, 80), (cart_x, cart_y, 40, 30))
    # Umbrella/canopy
    pygame.draw.polygon(surface, (220, 180, 60), [
        (cart_x - 5, cart_y),
        (cart_x + 45, cart_y),
        (cart_x + 40, cart_y - 15),
        (cart_x, cart_y - 15)
    ])
    # Wheels
    pygame.draw.circle(surface, (60, 60, 60), (cart_x + 8, cart_y + 32), 4)
    pygame.draw.circle(surface, (60, 60, 60), (cart_x + 32, cart_y + 32), 4)
    # Cart items (pretzel stand)
    for i in range(3):
        item_x = cart_x + 8 + i * 10
        pygame.draw.circle(surface, (200, 150, 80), (item_x, cart_y + 10), 3)

    # More falling leaves scattered in air
    random.seed(42)  # Consistent pattern
    for _ in range(25):
        leaf_air_x = random.randint(0, width)
        leaf_air_y = random.randint(200, 600)
        leaf_air_color = random.choice([(200, 50, 40), (230, 120, 30), (255, 180, 50), (180, 90, 40)])
        # Tilted leaf
        angle = random.randint(0, 360)
        if angle % 2 == 0:
            pygame.draw.ellipse(surface, leaf_air_color, (leaf_air_x, leaf_air_y, 5, 3))
        else:
            pygame.draw.ellipse(surface, leaf_air_color, (leaf_air_x, leaf_air_y, 3, 5))

    # Window shutters on some windows
    shutter_positions = [(75, 500), (105, 520), (280, 510), (500, 480), (715, 490), (940, 475)]
    for shut_x, shut_y in shutter_positions:
        # Left shutter
        pygame.draw.rect(surface, (100, 120, 80), (shut_x - 8, shut_y, 3, 12))
        # Right shutter
        pygame.draw.rect(surface, (100, 120, 80), (shut_x + 13, shut_y, 3, 12))
        # Slats (horizontal lines)
        for slat_i in range(3):
            slat_y = shut_y + 2 + slat_i * 4
            pygame.draw.line(surface, (80, 100, 60), (shut_x - 8, slat_y), (shut_x - 5, slat_y), 1)
            pygame.draw.line(surface, (80, 100, 60), (shut_x + 13, slat_y), (shut_x + 16, slat_y), 1)

    # Add decorative ironwork on some balconies
    ironwork_positions = [(420, 595), (720, 585), (1070, 590)]
    for iron_x, iron_y in ironwork_positions:
        # Base rail
        pygame.draw.line(surface, (40, 40, 40), (iron_x, iron_y), (iron_x + 30, iron_y), 2)
        # Vertical bars
        for bar_i in range(5):
            bar_x = iron_x + 5 + bar_i * 6
            pygame.draw.line(surface, (40, 40, 40), (bar_x, iron_y), (bar_x, iron_y + 12), 1)
        # Top rail
        pygame.draw.line(surface, (40, 40, 40), (iron_x, iron_y + 12), (iron_x + 30, iron_y + 12), 2)
        # Decorative curls
        pygame.draw.circle(surface, (40, 40, 40), (iron_x + 15, iron_y + 6), 3, 1)

    # Add some pigeons on the ground
    pigeon_ground_positions = [(200, 660), (360, 663), (520, 661), (810, 662), (1020, 664)]
    for pig_x, pig_y in pigeon_ground_positions:
        # Body (gray oval)
        pygame.draw.ellipse(surface, (120, 120, 130), (pig_x, pig_y, 8, 5))
        # Head
        pygame.draw.circle(surface, (110, 110, 120), (pig_x + 2, pig_y - 1), 2)
        # Beak
        pygame.draw.line(surface, (200, 150, 100), (pig_x, pig_y), (pig_x - 1, pig_y), 1)

    # Add street crossing lines (white stripes)
    crossing_positions = [400, 900]
    for cross_x in crossing_positions:
        for stripe_i in range(8):
            stripe_y = 660 + stripe_i * 8
            pygame.draw.rect(surface, (240, 240, 245), (cross_x, stripe_y, 35, 4))

    # Add autumn leaf piles in corners
    leaf_pile_positions = [(100, 655), (440, 658), (780, 656), (1200, 657)]
    for pile_x, pile_y in leaf_pile_positions:
        random.seed(pile_x)
        for _ in range(15):
            pile_leaf_x = pile_x + random.randint(-12, 12)
            pile_leaf_y = pile_y + random.randint(-3, 5)
            pile_color = random.choice([(200, 50, 40), (230, 120, 30), (255, 180, 50), (180, 90, 40)])
            pygame.draw.ellipse(surface, pile_color, (pile_leaf_x, pile_leaf_y, 3, 2))

    return surface


def create_nyc_background(width, height):
    """Create a highly detailed NYC nighttime background."""
    surface = pygame.Surface((width, height))

    # Night sky gradient (dark purple to dark blue)
    top_color = (15, 15, 35)
    mid_color = (25, 20, 45)
    bottom_color = (35, 25, 50)

    # Draw sky gradient
    for y in range(height):
        if y < height // 2:
            progress = y / (height // 2)
            r = int(top_color[0] + (mid_color[0] - top_color[0]) * progress)
            g = int(top_color[1] + (mid_color[1] - top_color[1]) * progress)
            b = int(top_color[2] + (mid_color[2] - top_color[2]) * progress)
        else:
            progress = (y - height // 2) / (height // 2)
            r = int(mid_color[0] + (bottom_color[0] - mid_color[0]) * progress)
            g = int(mid_color[1] + (bottom_color[1] - mid_color[1]) * progress)
            b = int(mid_color[2] + (bottom_color[2] - mid_color[2]) * progress)
        pygame.draw.line(surface, (r, g, b), (0, y), (width, y))

    # Stars
    random.seed(999)
    for _ in range(40):
        star_x = random.randint(0, width)
        star_y = random.randint(0, 300)
        star_brightness = random.randint(150, 255)
        pygame.draw.circle(surface, (star_brightness, star_brightness, star_brightness),
                         (star_x, star_y), 1)

    # Moon
    pygame.draw.circle(surface, (240, 240, 250), (1100, 100), 35)
    pygame.draw.circle(surface, (220, 220, 235), (1090, 95), 30)

    # Distant water (Hudson River)
    water_color = (20, 30, 50)
    pygame.draw.rect(surface, water_color, (0, 550, width, 170))
    # Water reflections
    for i in range(0, width, 40):
        pygame.draw.line(surface, (30, 40, 60), (i, 560), (i + 20, 580), 2)

    # Skyscrapers (varied heights - Art Deco and modern)
    buildings = [
        # Far left - shorter buildings
        {'x': 20, 'y': 420, 'w': 70, 'h': 300, 'color': (35, 40, 55), 'style': 'modern'},
        {'x': 100, 'y': 380, 'w': 85, 'h': 340, 'color': (40, 45, 60), 'style': 'modern'},
        {'x': 195, 'y': 450, 'w': 65, 'h': 270, 'color': (38, 43, 58), 'style': 'deco'},

        # Empire State Building (tallest in center)
        {'x': 270, 'y': 200, 'w': 90, 'h': 520, 'color': (45, 50, 65), 'style': 'empire'},

        # Mid buildings
        {'x': 370, 'y': 350, 'w': 75, 'h': 370, 'color': (42, 47, 62), 'style': 'modern'},
        {'x': 455, 'y': 300, 'w': 95, 'h': 420, 'color': (38, 43, 58), 'style': 'deco'},
        {'x': 560, 'y': 390, 'w': 80, 'h': 330, 'color': (40, 45, 60), 'style': 'modern'},

        # Chrysler-style building
        {'x': 650, 'y': 250, 'w': 85, 'h': 470, 'color': (43, 48, 63), 'style': 'chrysler'},

        # Right side buildings
        {'x': 745, 'y': 370, 'w': 70, 'h': 350, 'color': (37, 42, 57), 'style': 'modern'},
        {'x': 825, 'y': 320, 'w': 90, 'h': 400, 'color': (41, 46, 61), 'style': 'deco'},
        {'x': 925, 'y': 410, 'w': 75, 'h': 310, 'color': (39, 44, 59), 'style': 'modern'},
        {'x': 1010, 'y': 360, 'w': 85, 'h': 360, 'color': (36, 41, 56), 'style': 'modern'},
        {'x': 1105, 'y': 430, 'w': 70, 'h': 290, 'color': (40, 45, 60), 'style': 'deco'},
        {'x': 1185, 'y': 380, 'w': 95, 'h': 340, 'color': (38, 43, 58), 'style': 'modern'},
    ]

    for building in buildings:
        x, y, w, h = building['x'], building['y'], building['w'], building['h']
        color = building['color']
        style = building['style']

        # Building body
        pygame.draw.rect(surface, color, (x, y, w, h))

        # Special architectural features
        if style == 'empire':
            # Empire State Building spire
            spire_points = [(x + w//2 - 8, y), (x + w//2 + 8, y), (x + w//2, y - 60)]
            pygame.draw.polygon(surface, (50, 55, 70), spire_points)
            # Top lights
            for i in range(3):
                light_y = y - 20 - i * 15
                pygame.draw.circle(surface, (255, 230, 150, 180), (x + w//2, light_y), 3)

        elif style == 'chrysler':
            # Chrysler Building art deco top
            for i in range(5):
                tier_y = y + i * 8
                tier_width = w - i * 8
                pygame.draw.rect(surface, (55, 60, 75), (x + i * 4, tier_y, tier_width, 8))
            # Spire
            pygame.draw.polygon(surface, (60, 65, 80), [
                (x + w//2 - 5, y), (x + w//2 + 5, y), (x + w//2, y - 40)
            ])

        elif style == 'deco':
            # Art deco stepped top
            pygame.draw.rect(surface, (color[0] + 10, color[1] + 10, color[2] + 10),
                           (x + 8, y - 10, w - 16, 10))

        # Windows (lit and dark - NYC never sleeps)
        window_lit = (255, 245, 180)
        window_dark = (25, 30, 40)

        for row in range(5, h - 5, 12):
            for col in range(6, w - 6, 10):
                wx = x + col
                wy = y + row

                # 70% of windows are lit at night
                random.seed(wx + wy)
                if random.random() < 0.7:
                    win_color = window_lit
                else:
                    win_color = window_dark

                pygame.draw.rect(surface, win_color, (wx, wy, 6, 8))
                pygame.draw.rect(surface, (50, 55, 65), (wx, wy, 6, 8), 1)

        # Building edge highlighting
        pygame.draw.line(surface, (color[0] + 15, color[1] + 15, color[2] + 15),
                        (x, y), (x, y + h), 1)

    # Water towers on some rooftops
    water_tower_positions = [(110, 375), (385, 345), (575, 385), (835, 315), (1020, 355)]
    for wt_x, wt_y in water_tower_positions:
        # Support
        pygame.draw.rect(surface, (60, 55, 50), (wt_x, wt_y, 3, 20))
        pygame.draw.rect(surface, (60, 55, 50), (wt_x + 12, wt_y, 3, 20))
        # Tank
        pygame.draw.rect(surface, (80, 70, 60), (wt_x - 3, wt_y - 15, 20, 15))
        pygame.draw.circle(surface, (70, 60, 50), (wt_x + 7, wt_y - 15), 10)

    # Neon signs (Times Square style)
    neon_signs = [
        {'x': 280, 'y': 480, 'w': 70, 'h': 25, 'color': (255, 50, 100)},
        {'x': 465, 'y': 520, 'w': 80, 'h': 30, 'color': (50, 200, 255)},
        {'x': 660, 'y': 500, 'w': 65, 'h': 28, 'color': (255, 230, 50)},
        {'x': 835, 'y': 540, 'w': 75, 'h': 26, 'color': (150, 50, 255)},
    ]

    for sign in neon_signs:
        # Sign glow
        glow_surf = pygame.Surface((sign['w'] + 20, sign['h'] + 20), pygame.SRCALPHA)
        pygame.draw.rect(glow_surf, (*sign['color'], 60), (10, 10, sign['w'], sign['h']))
        surface.blit(glow_surf, (sign['x'] - 10, sign['y'] - 10))
        # Sign itself
        pygame.draw.rect(surface, sign['color'], (sign['x'], sign['y'], sign['w'], sign['h']))
        pygame.draw.rect(surface, (sign['color'][0]//2, sign['color'][1]//2, sign['color'][2]//2),
                        (sign['x'], sign['y'], sign['w'], sign['h']), 2)

    # Street level (dark asphalt)
    street_color = (30, 32, 35)
    pygame.draw.rect(surface, street_color, (0, 650, width, 70))

    # Street lane markings
    for lane_x in range(0, width, 60):
        pygame.draw.rect(surface, (200, 200, 180), (lane_x + 25, 685, 15, 3))

    # Sidewalks
    sidewalk_color = (45, 47, 50)
    pygame.draw.rect(surface, sidewalk_color, (0, 640, width, 12))

    # Street lamps (NYC style)
    lamp_positions = [150, 380, 610, 840, 1070]
    for lamp_x in lamp_positions:
        # Pole
        pygame.draw.rect(surface, (70, 70, 75), (lamp_x, 580, 4, 70))
        # Curved top
        pygame.draw.arc(surface, (70, 70, 75), (lamp_x - 12, 570, 25, 20), 0, 3.14, 3)
        # Light
        pygame.draw.circle(surface, (255, 245, 200), (lamp_x + 2, 575), 6)
        # Glow
        glow_surf = pygame.Surface((40, 80), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (255, 245, 200, 40), (20, 10), 20)
        surface.blit(glow_surf, (lamp_x - 18, 570))

    # Yellow cabs (iconic NYC)
    cab_positions = [(220, 655), (560, 657), (920, 656)]
    for cab_x, cab_y in cab_positions:
        # Cab body
        pygame.draw.rect(surface, (255, 215, 0), (cab_x, cab_y, 35, 18))
        # Windows
        pygame.draw.rect(surface, (100, 140, 180), (cab_x + 5, cab_y + 3, 12, 8))
        pygame.draw.rect(surface, (100, 140, 180), (cab_x + 20, cab_y + 3, 10, 8))
        # Wheels
        pygame.draw.circle(surface, (30, 30, 30), (cab_x + 8, cab_y + 20), 4)
        pygame.draw.circle(surface, (30, 30, 30), (cab_x + 28, cab_y + 20), 4)
        # Taxi light
        pygame.draw.rect(surface, (255, 100, 100), (cab_x + 12, cab_y - 3, 12, 3))

    # Fire escapes
    fire_escape_positions = [(50, 500), (230, 440), (410, 460), (595, 480), (780, 450), (970, 490)]
    for fe_x, fe_y in fire_escape_positions:
        # Zigzag pattern
        for i in range(4):
            platform_y = fe_y + i * 35
            pygame.draw.rect(surface, (60, 50, 45), (fe_x, platform_y, 25, 3))
            if i < 3:
                # Ladder
                pygame.draw.line(surface, (60, 50, 45), (fe_x + 12, platform_y + 3),
                               (fe_x + 5, platform_y + 35), 2)

    # Steam vents (NYC characteristic)
    steam_positions = [(300, 650), (700, 652), (1100, 651)]
    for steam_x, steam_y in steam_positions:
        # Grate
        for i in range(5):
            pygame.draw.line(surface, (60, 60, 65), (steam_x + i * 4, steam_y),
                           (steam_x + i * 4, steam_y + 8), 1)
        # Steam cloud
        steam_surf = pygame.Surface((30, 60), pygame.SRCALPHA)
        for i in range(4):
            alpha = int(80 - i * 15)
            radius = 8 + i * 3
            pygame.draw.circle(steam_surf, (220, 220, 230, alpha), (15 + i * 2, i * 12), radius)
        surface.blit(steam_surf, (steam_x - 8, steam_y - 55))

    # Pedestrians (small silhouettes)
    pedestrian_positions = [(100, 645), (340, 646), (580, 645), (820, 646), (1050, 645)]
    for ped_x, ped_y in pedestrian_positions:
        # Head
        pygame.draw.circle(surface, (40, 40, 45), (ped_x, ped_y), 3)
        # Body
        pygame.draw.rect(surface, (40, 40, 45), (ped_x - 2, ped_y + 3, 4, 8))

    # Traffic lights
    traffic_light_positions = [480, 980]
    for tl_x in traffic_light_positions:
        # Pole
        pygame.draw.rect(surface, (50, 50, 55), (tl_x, 600, 3, 50))
        # Light box
        pygame.draw.rect(surface, (40, 40, 45), (tl_x - 4, 595, 11, 18))
        # Red light (on)
        pygame.draw.circle(surface, (255, 50, 50), (tl_x + 2, 598), 3)
        # Yellow light
        pygame.draw.circle(surface, (80, 80, 60), (tl_x + 2, 604), 3)
        # Green light
        pygame.draw.circle(surface, (60, 80, 60), (tl_x + 2, 610), 3)

    # Delivery trucks
    truck_positions = [(440, 655)]
    for truck_x, truck_y in truck_positions:
        # Truck body
        pygame.draw.rect(surface, (180, 180, 185), (truck_x, truck_y, 50, 20))
        # Cab
        pygame.draw.rect(surface, (160, 160, 165), (truck_x, truck_y + 10, 15, 10))
        # Wheels
        pygame.draw.circle(surface, (30, 30, 30), (truck_x + 10, truck_y + 22), 4)
        pygame.draw.circle(surface, (30, 30, 30), (truck_x + 42, truck_y + 22), 4)

    # === TIMES SQUARE ENHANCEMENTS ===

    # Large digital billboards (animated-style with bright colors)
    billboards = [
        {'x': 150, 'y': 350, 'w': 100, 'h': 60, 'color': (255, 100, 150), 'text_color': (255, 255, 255)},
        {'x': 370, 'y': 320, 'w': 110, 'h': 70, 'color': (50, 150, 255), 'text_color': (255, 255, 100)},
        {'x': 555, 'y': 340, 'w': 95, 'h': 65, 'color': (100, 255, 100), 'text_color': (255, 100, 255)},
        {'x': 740, 'y': 330, 'w': 105, 'h': 68, 'color': (255, 200, 50), 'text_color': (0, 0, 0)},
        {'x': 920, 'y': 360, 'w': 90, 'h': 55, 'color': (255, 50, 255), 'text_color': (255, 255, 255)},
        {'x': 1080, 'y': 345, 'w': 98, 'h': 62, 'color': (255, 150, 0), 'text_color': (255, 255, 255)},
    ]

    for billboard in billboards:
        # Main billboard screen
        pygame.draw.rect(surface, billboard['color'],
                        (billboard['x'], billboard['y'], billboard['w'], billboard['h']))
        # Screen border (metallic frame)
        pygame.draw.rect(surface, (80, 80, 90),
                        (billboard['x'], billboard['y'], billboard['w'], billboard['h']), 3)
        # Glowing effect around billboard
        glow_surface = pygame.Surface((billboard['w'] + 10, billboard['h'] + 10), pygame.SRCALPHA)
        glow_color = (*billboard['color'][:3], 30)
        pygame.draw.rect(glow_surface, glow_color, (0, 0, billboard['w'] + 10, billboard['h'] + 10))
        surface.blit(glow_surface, (billboard['x'] - 5, billboard['y'] - 5))
        # Simulated text lines (bright rectangles)
        for line_offset in range(3):
            line_y = billboard['y'] + 15 + line_offset * 15
            pygame.draw.rect(surface, billboard['text_color'],
                           (billboard['x'] + 10, line_y, billboard['w'] - 20, 8))

    # Broadway theater marquees
    marquees = [
        {'x': 200, 'y': 580, 'w': 85, 'h': 35, 'name': 'BROADWAY'},
        {'x': 500, 'y': 575, 'w': 90, 'h': 38, 'name': 'THEATER'},
        {'x': 800, 'y': 578, 'w': 82, 'h': 36, 'name': 'MUSICAL'},
    ]

    for marquee in marquees:
        # Marquee canopy
        pygame.draw.rect(surface, (200, 20, 20),
                        (marquee['x'], marquee['y'], marquee['w'], marquee['h']))
        # Gold/yellow lights around border
        for light_x in range(0, marquee['w'], 8):
            pygame.draw.circle(surface, (255, 220, 0),
                             (marquee['x'] + light_x, marquee['y'] + 2), 2)
            pygame.draw.circle(surface, (255, 220, 0),
                             (marquee['x'] + light_x, marquee['y'] + marquee['h'] - 2), 2)
        # Title area
        pygame.draw.rect(surface, (255, 255, 200),
                        (marquee['x'] + 5, marquee['y'] + 10, marquee['w'] - 10, 15))
        # Support posts
        pygame.draw.rect(surface, (150, 20, 20),
                        (marquee['x'], marquee['y'] + marquee['h'], 4, 35))
        pygame.draw.rect(surface, (150, 20, 20),
                        (marquee['x'] + marquee['w'] - 4, marquee['y'] + marquee['h'], 4, 35))

    # News ticker (running text display)
    ticker_x, ticker_y = 400, 450
    pygame.draw.rect(surface, (0, 0, 0), (ticker_x, ticker_y, 200, 18))
    pygame.draw.rect(surface, (255, 100, 0), (ticker_x + 2, ticker_y + 2, 196, 14))
    # Moving text effect (white blocks)
    for tick_pos in [10, 40, 70, 100, 130, 160]:
        pygame.draw.rect(surface, (255, 255, 255), (ticker_x + tick_pos, ticker_y + 5, 20, 8))

    # TKTS booth (iconic red steps)
    tkts_x, tkts_y = 600, 620
    # Red steps
    for step in range(3):
        step_y = tkts_y + step * 8
        pygame.draw.rect(surface, (200, 0, 0), (tkts_x, step_y, 60, 8))
        pygame.draw.rect(surface, (180, 0, 0), (tkts_x, step_y, 60, 8), 1)
    # TKTS sign
    pygame.draw.rect(surface, (255, 255, 255), (tkts_x + 15, tkts_y - 20, 30, 15))
    pygame.draw.rect(surface, (200, 0, 0), (tkts_x + 17, tkts_y - 18, 26, 11))

    # Times Square Ball (iconic New Year's ball)
    ball_x, ball_y = 300, 150
    # Ball structure
    pygame.draw.circle(surface, (200, 200, 220), (ball_x, ball_y), 15)
    # Crystalline panels (lighter spots)
    for angle in range(0, 360, 60):
        import math
        offset_x = int(math.cos(math.radians(angle)) * 8)
        offset_y = int(math.sin(math.radians(angle)) * 8)
        pygame.draw.circle(surface, (230, 230, 255), (ball_x + offset_x, ball_y + offset_y), 4)
    # Glow effect
    glow_surface = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.circle(glow_surface, (255, 255, 255, 40), (20, 20), 20)
    surface.blit(glow_surface, (ball_x - 20, ball_y - 20))
    # Support pole
    pygame.draw.rect(surface, (100, 100, 110), (ball_x - 2, ball_y + 15, 4, 50))

    # Street performers (silhouettes)
    performers = [
        {'x': 250, 'y': 645, 'type': 'statue'},  # Living statue
        {'x': 680, 'y': 643, 'type': 'musician'},  # Musician
        {'x': 1100, 'y': 646, 'type': 'dancer'},  # Dancer
    ]

    for performer in performers:
        if performer['type'] == 'statue':
            # Person standing still with top hat
            pygame.draw.circle(surface, (180, 180, 185), (performer['x'], performer['y'] - 8), 4)  # Head
            pygame.draw.rect(surface, (180, 180, 185), (performer['x'] - 3, performer['y'] - 4, 6, 12))  # Body
            # Top hat
            pygame.draw.rect(surface, (50, 50, 55), (performer['x'] - 3, performer['y'] - 14, 6, 6))
            pygame.draw.rect(surface, (50, 50, 55), (performer['x'] - 4, performer['y'] - 8, 8, 2))
        elif performer['type'] == 'musician':
            # Person with guitar
            pygame.draw.circle(surface, (120, 100, 90), (performer['x'], performer['y'] - 8), 3)  # Head
            pygame.draw.rect(surface, (80, 60, 120), (performer['x'] - 2, performer['y'] - 4, 4, 10))  # Body
            # Guitar
            pygame.draw.circle(surface, (160, 120, 80), (performer['x'] + 4, performer['y'] - 2), 4)
            pygame.draw.line(surface, (100, 80, 60), (performer['x'] + 4, performer['y'] - 6),
                           (performer['x'] + 4, performer['y'] + 4), 2)
        else:  # dancer
            # Person in motion
            pygame.draw.circle(surface, (140, 120, 110), (performer['x'], performer['y'] - 9), 3)  # Head
            pygame.draw.polygon(surface, (200, 100, 150), [
                (performer['x'] - 3, performer['y'] - 5),
                (performer['x'] + 4, performer['y'] - 3),
                (performer['x'] + 2, performer['y'] + 6),
                (performer['x'] - 4, performer['y'] + 5)
            ])  # Dancing pose body

    # Police presence (NYPD cars and officers)
    # Police car
    police_car_x, police_car_y = 900, 660
    pygame.draw.rect(surface, (30, 50, 120), (police_car_x, police_car_y, 45, 18))  # Car body
    pygame.draw.rect(surface, (100, 150, 200), (police_car_x + 10, police_car_y + 3, 10, 8))  # Window
    pygame.draw.rect(surface, (100, 150, 200), (police_car_x + 25, police_car_y + 3, 10, 8))  # Window
    # Police lights (red and blue)
    pygame.draw.rect(surface, (255, 0, 0), (police_car_x + 15, police_car_y - 2, 6, 3))
    pygame.draw.rect(surface, (0, 100, 255), (police_car_x + 24, police_car_y - 2, 6, 3))
    # Wheels
    pygame.draw.circle(surface, (30, 30, 30), (police_car_x + 10, police_car_y + 20), 4)
    pygame.draw.circle(surface, (30, 30, 30), (police_car_x + 37, police_car_y + 20), 4)
    # "NYPD" text
    pygame.draw.rect(surface, (255, 255, 255), (police_car_x + 12, police_car_y + 10, 20, 5))

    # Police officers
    officer_positions = [(875, 645), (950, 646)]
    for off_x, off_y in officer_positions:
        # Head
        pygame.draw.circle(surface, (180, 150, 130), (off_x, off_y), 3)
        # Cap
        pygame.draw.rect(surface, (30, 50, 120), (off_x - 3, off_y - 4, 6, 3))
        # Body (dark blue uniform)
        pygame.draw.rect(surface, (30, 50, 120), (off_x - 2, off_y + 3, 4, 10))
        # Badge (gold)
        pygame.draw.circle(surface, (255, 215, 0), (off_x, off_y + 6), 1)

    # Tourist crowds (more dense pedestrians)
    tourist_positions = [
        (180, 648), (220, 647), (260, 649), (300, 646), (380, 648),
        (420, 647), (460, 646), (540, 649), (620, 647), (660, 648),
        (720, 646), (760, 649), (840, 647), (1020, 648), (1060, 646),
        (1140, 647), (1180, 649), (1220, 646)
    ]

    tourist_colors = [
        (200, 100, 100), (100, 150, 200), (150, 200, 150), (200, 200, 100),
        (180, 120, 180), (100, 180, 180), (220, 150, 100), (150, 150, 150)
    ]

    random.seed(42)  # Consistent randomization
    for tour_x, tour_y in tourist_positions:
        color = random.choice(tourist_colors)
        # Head
        pygame.draw.circle(surface, (180, 150, 130), (tour_x, tour_y), 2)
        # Body (random colored clothing)
        pygame.draw.rect(surface, color, (tour_x - 2, tour_y + 2, 4, 7))
        # Some with cameras
        if random.random() < 0.3:
            pygame.draw.rect(surface, (50, 50, 55), (tour_x + 2, tour_y + 4, 3, 2))

    # Additional large neon signs (iconic brands style)
    large_signs = [
        {'x': 100, 'y': 420, 'w': 70, 'h': 50, 'color': (255, 0, 0)},  # Coca-Cola style
        {'x': 850, 'y': 410, 'w': 75, 'h': 55, 'color': (0, 100, 255)},  # Samsung style
        {'x': 1050, 'y': 425, 'w': 65, 'h': 48, 'color': (255, 200, 0)},  # McDonald's style
    ]

    for sign in large_signs:
        # Sign background
        pygame.draw.rect(surface, sign['color'], (sign['x'], sign['y'], sign['w'], sign['h']))
        # Border lights
        pygame.draw.rect(surface, (255, 255, 255), (sign['x'], sign['y'], sign['w'], sign['h']), 2)
        # Glow effect
        glow_surface = pygame.Surface((sign['w'] + 20, sign['h'] + 20), pygame.SRCALPHA)
        glow_color = (*sign['color'][:3], 50)
        pygame.draw.rect(glow_surface, glow_color, (0, 0, sign['w'] + 20, sign['h'] + 20))
        surface.blit(glow_surface, (sign['x'] - 10, sign['y'] - 10))
        # Logo placeholder (white circle/shape)
        pygame.draw.circle(surface, (255, 255, 255),
                          (sign['x'] + sign['w']//2, sign['y'] + sign['h']//2),
                          min(sign['w'], sign['h'])//3)

    # Electronic news zipper/ticker on building
    zipper_x, zipper_y = 50, 500
    pygame.draw.rect(surface, (255, 140, 0), (zipper_x, zipper_y, 1200, 12))
    # Moving text blocks
    for zip_pos in range(0, 1200, 30):
        block_color = (255, 255, 255) if (zip_pos // 30) % 2 == 0 else (0, 0, 0)
        pygame.draw.rect(surface, block_color, (zipper_x + zip_pos, zipper_y + 2, 20, 8))

    return surface


def create_chicago_background(width, height):
    """Create a highly detailed Chicago daytime background."""
    surface = pygame.Surface((width, height))

    # Bright blue sky gradient (The Windy City)
    top_color = (120, 180, 240)
    mid_color = (150, 200, 250)
    bottom_color = (180, 220, 255)

    # Draw sky gradient
    for y in range(height):
        if y < height // 2:
            progress = y / (height // 2)
            r = int(top_color[0] + (mid_color[0] - top_color[0]) * progress)
            g = int(top_color[1] + (mid_color[1] - top_color[1]) * progress)
            b = int(top_color[2] + (mid_color[2] - top_color[2]) * progress)
        else:
            progress = (y - height // 2) / (height // 2)
            r = int(mid_color[0] + (bottom_color[0] - mid_color[0]) * progress)
            g = int(mid_color[1] + (bottom_color[1] - mid_color[1]) * progress)
            b = int(mid_color[2] + (bottom_color[2] - mid_color[2]) * progress)
        pygame.draw.line(surface, (r, g, b), (0, y), (width, y))

    # Fluffy white clouds
    cloud_positions = [(200, 100), (500, 80), (800, 120), (1050, 90)]
    for cx, cy in cloud_positions:
        for i in range(6):
            x_offset = (i - 2.5) * 18
            radius = 12 + (2.5 - abs(i - 2.5)) * 4
            pygame.draw.circle(surface, (255, 255, 255), (int(cx + x_offset), cy), int(radius))

    # Lake Michigan (distant)
    lake_color = (100, 160, 210)
    pygame.draw.rect(surface, lake_color, (0, 480, width, 100))
    # Lake waves
    for i in range(0, width, 50):
        pygame.draw.arc(surface, (90, 150, 200), (i, 490, 40, 20), 0, 3.14, 1)

    # Chicago skyline - mix of modern and classic architecture
    buildings = [
        # Willis (Sears) Tower - tallest
        {'x': 580, 'y': 180, 'w': 100, 'h': 540, 'color': (90, 100, 115), 'style': 'willis'},

        # Left side buildings
        {'x': 40, 'y': 400, 'w': 75, 'h': 320, 'color': (110, 120, 135), 'style': 'modern'},
        {'x': 125, 'y': 360, 'w': 85, 'h': 360, 'color': (100, 110, 125), 'style': 'deco'},
        {'x': 220, 'y': 330, 'w': 90, 'h': 390, 'color': (105, 115, 130), 'style': 'modern'},
        {'x': 320, 'y': 380, 'w': 80, 'h': 340, 'color': (95, 105, 120), 'style': 'glass'},
        {'x': 410, 'y': 300, 'w': 95, 'h': 420, 'color': (108, 118, 133), 'style': 'modern'},
        {'x': 515, 'y': 340, 'w': 70, 'h': 380, 'color': (102, 112, 127), 'style': 'deco'},

        # Right side buildings
        {'x': 690, 'y': 320, 'w': 85, 'h': 400, 'color': (98, 108, 123), 'style': 'glass'},
        {'x': 785, 'y': 280, 'w': 95, 'h': 440, 'color': (112, 122, 137), 'style': 'modern'},

        # John Hancock Center
        {'x': 890, 'y': 220, 'w': 88, 'h': 500, 'color': (85, 95, 110), 'style': 'hancock'},

        {'x': 988, 'y': 360, 'w': 78, 'h': 360, 'color': (105, 115, 130), 'style': 'modern'},
        {'x': 1076, 'y': 390, 'w': 82, 'h': 330, 'color': (100, 110, 125), 'style': 'glass'},
        {'x': 1168, 'y': 340, 'w': 92, 'h': 380, 'color': (95, 105, 120), 'style': 'modern'},
    ]

    for building in buildings:
        x, y, w, h = building['x'], building['y'], building['w'], building['h']
        color = building['color']
        style = building['style']

        # Building body
        pygame.draw.rect(surface, color, (x, y, w, h))

        # Special features
        if style == 'willis':
            # Willis Tower's distinctive tubes
            pygame.draw.line(surface, (color[0] - 10, color[1] - 10, color[2] - 10),
                           (x + w//3, y), (x + w//3, y + h), 2)
            pygame.draw.line(surface, (color[0] - 10, color[1] - 10, color[2] - 10),
                           (x + 2*w//3, y), (x + 2*w//3, y + h), 2)
            # Antennas
            pygame.draw.rect(surface, (120, 130, 140), (x + w//2 - 2, y - 40, 4, 40))

        elif style == 'hancock':
            # John Hancock's X-bracing
            for brace_y in range(y + 50, y + h, 80):
                pygame.draw.line(surface, (color[0] + 15, color[1] + 15, color[2] + 15),
                               (x + 10, brace_y), (x + w - 10, brace_y + 40), 2)
                pygame.draw.line(surface, (color[0] + 15, color[1] + 15, color[2] + 15),
                               (x + w - 10, brace_y), (x + 10, brace_y + 40), 2)
            # Antennas
            pygame.draw.rect(surface, (120, 130, 140), (x + w//2 - 2, y - 35, 4, 35))

        elif style == 'glass':
            # Reflective glass effect
            for reflect_y in range(y + 10, y + h - 10, 30):
                pygame.draw.rect(surface, (color[0] + 20, color[1] + 25, color[2] + 30),
                               (x + 5, reflect_y, w - 10, 15))

        # Windows (reflective daytime glass)
        window_color = (150, 180, 200)
        window_reflect = (180, 210, 230)

        for row in range(8, h - 8, 14):
            for col in range(8, w - 8, 12):
                wx = x + col
                wy = y + row

                # Alternating reflection pattern
                random.seed(wx + wy)
                if random.random() < 0.4:
                    win_color = window_reflect
                else:
                    win_color = window_color

                pygame.draw.rect(surface, win_color, (wx, wy, 8, 10))
                pygame.draw.rect(surface, (color[0] + 10, color[1] + 10, color[2] + 10),
                               (wx, wy, 8, 10), 1)

        # Building highlights
        pygame.draw.line(surface, (color[0] + 20, color[1] + 20, color[2] + 20),
                        (x, y), (x, y + h), 1)

    # The Bean (Cloud Gate) - simplified version
    bean_x, bean_y = 250, 600
    pygame.draw.ellipse(surface, (180, 180, 190), (bean_x, bean_y, 80, 50))
    # Reflections on the bean
    pygame.draw.ellipse(surface, (200, 210, 220), (bean_x + 10, bean_y + 10, 30, 20))
    pygame.draw.ellipse(surface, (160, 170, 180), (bean_x + 45, bean_y + 15, 25, 18))

    # Chicago River
    river_color = (95, 155, 195)
    pygame.draw.polygon(surface, river_color, [
        (0, 580), (400, 590), (800, 585), (1280, 592), (1280, 610), (0, 610)
    ])
    # River boats
    boat_positions = [(180, 590), (650, 587)]
    for boat_x, boat_y in boat_positions:
        pygame.draw.rect(surface, (255, 255, 255), (boat_x, boat_y, 35, 12))
        pygame.draw.polygon(surface, (200, 200, 210), [
            (boat_x, boat_y), (boat_x + 35, boat_y), (boat_x + 30, boat_y + 12), (boat_x + 5, boat_y + 12)
        ])

    # Street level
    street_color = (70, 75, 80)
    pygame.draw.rect(surface, street_color, (0, 650, width, 70))

    # Chicago's grid pattern streets
    for grid_x in range(0, width, 80):
        pygame.draw.rect(surface, (180, 180, 170), (grid_x + 35, 685, 10, 3))

    # Sidewalks (gray)
    sidewalk_color = (100, 105, 110)
    pygame.draw.rect(surface, sidewalk_color, (0, 640, width, 12))

    # L Train elevated tracks
    track_y = 610
    # Support columns
    for col_x in range(100, width, 120):
        pygame.draw.rect(surface, (80, 70, 65), (col_x, track_y, 8, 40))
    # Track platform
    pygame.draw.rect(surface, (90, 80, 75), (0, track_y, width, 6))
    # Train
    train_x = 500
    pygame.draw.rect(surface, (190, 60, 70), (train_x, track_y - 18, 100, 16))
    # Train windows
    for tw_x in range(train_x + 8, train_x + 92, 20):
        pygame.draw.rect(surface, (220, 220, 235), (tw_x, track_y - 14, 12, 8))

    # Hot dog stands (Chicago style)
    stand_positions = [(320, 635), (900, 635)]
    for stand_x, stand_y in stand_positions:
        # Cart
        pygame.draw.rect(surface, (220, 50, 50), (stand_x, stand_y, 40, 18))
        # Umbrella
        pygame.draw.polygon(surface, (255, 200, 50), [
            (stand_x - 5, stand_y - 5), (stand_x + 45, stand_y - 5),
            (stand_x + 42, stand_y - 20), (stand_x - 2, stand_y - 20)
        ])
        # Wheels
        pygame.draw.circle(surface, (40, 40, 40), (stand_x + 8, stand_y + 20), 4)
        pygame.draw.circle(surface, (40, 40, 40), (stand_x + 32, stand_y + 20), 4)

    # Wind effects (Chicago is the Windy City!)
    random.seed(777)
    for _ in range(15):
        wind_x = random.randint(0, width)
        wind_y = random.randint(300, 600)
        # Motion lines
        pygame.draw.line(surface, (200, 210, 220, 100), (wind_x, wind_y), (wind_x + 20, wind_y + 3), 1)

    # Street signs
    sign_positions = [200, 600, 1000]
    for sign_x in sign_positions:
        # Pole
        pygame.draw.rect(surface, (70, 70, 75), (sign_x, 600, 3, 50))
        # Sign
        pygame.draw.rect(surface, (50, 100, 50), (sign_x - 15, 595, 33, 12))
        pygame.draw.rect(surface, (255, 255, 255), (sign_x - 13, 597, 29, 8))

    # People on street
    people_positions = [(150, 645), (400, 646), (720, 645), (1050, 646)]
    for person_x, person_y in people_positions:
        # Head
        pygame.draw.circle(surface, (120, 100, 90), (person_x, person_y), 3)
        # Body
        random.seed(person_x)
        clothing_color = random.choice([(80, 80, 120), (120, 60, 60), (60, 100, 60)])
        pygame.draw.rect(surface, clothing_color, (person_x - 3, person_y + 3, 6, 10))

    # Newspaper boxes
    newsbox_positions = [270, 820]
    for nb_x in newsbox_positions:
        pygame.draw.rect(surface, (80, 100, 180), (nb_x, 635, 18, 20))
        pygame.draw.rect(surface, (220, 220, 230), (nb_x + 2, 638, 14, 10))
        # "Tribune" text representation
        pygame.draw.rect(surface, (40, 40, 40), (nb_x + 4, 640, 10, 6))

    # Bike lanes (green)
    for bike_x in range(0, width, 100):
        pygame.draw.rect(surface, (100, 180, 100), (bike_x, 670, 30, 8))

    # Cyclists
    cyclist_positions = [(480, 665), (1100, 667)]
    for cyc_x, cyc_y in cyclist_positions:
        # Bike
        pygame.draw.circle(surface, (60, 60, 65), (cyc_x, cyc_y + 6), 4, 1)
        pygame.draw.circle(surface, (60, 60, 65), (cyc_x + 15, cyc_y + 6), 4, 1)
        pygame.draw.line(surface, (60, 60, 65), (cyc_x + 7, cyc_y), (cyc_x + 7, cyc_y + 6), 2)
        # Rider
        pygame.draw.circle(surface, (140, 120, 100), (cyc_x + 7, cyc_y - 2), 3)

    # Jazz club signs (Chicago jazz heritage)
    jazz_sign_x, jazz_sign_y = 750, 630
    pygame.draw.rect(surface, (100, 40, 120), (jazz_sign_x, jazz_sign_y, 45, 22))
    pygame.draw.rect(surface, (150, 100, 180), (jazz_sign_x + 2, jazz_sign_y + 2, 41, 18), 2)
    # Musical note decoration
    pygame.draw.circle(surface, (200, 180, 100), (jazz_sign_x + 10, jazz_sign_y + 10), 3)

    # Cars (various colors)
    car_data = [
        (120, 657, (180, 50, 50)),
        (550, 656, (50, 100, 180)),
        (980, 658, (100, 100, 100)),
    ]
    for car_x, car_y, car_color in car_data:
        pygame.draw.rect(surface, car_color, (car_x, car_y, 40, 18))
        # Windows
        pygame.draw.rect(surface, (140, 180, 200), (car_x + 8, car_y + 3, 10, 8))
        pygame.draw.rect(surface, (140, 180, 200), (car_x + 22, car_y + 3, 10, 8))
        # Wheels
        pygame.draw.circle(surface, (30, 30, 30), (car_x + 8, car_y + 20), 4)
        pygame.draw.circle(surface, (30, 30, 30), (car_x + 32, car_y + 20), 4)

    # === CHICAGO LANDMARK ENHANCEMENTS ===

    # Enhanced Cloud Gate (The Bean) - larger and more detailed
    bean_center_x, bean_center_y = 280, 610
    # Main Bean body (larger ellipse)
    pygame.draw.ellipse(surface, (190, 195, 205), (bean_center_x - 50, bean_center_y - 25, 100, 50))
    # Reflective highlights (sky reflection)
    pygame.draw.ellipse(surface, (220, 230, 245), (bean_center_x - 35, bean_center_y - 18, 35, 20))
    pygame.draw.ellipse(surface, (200, 210, 230), (bean_center_x + 5, bean_center_y - 15, 30, 18))
    # Dark reflection (ground/people reflection)
    pygame.draw.ellipse(surface, (140, 150, 165), (bean_center_x - 30, bean_center_y + 5, 60, 18))
    # Metallic shine spots (bright white highlights)
    pygame.draw.ellipse(surface, (245, 250, 255), (bean_center_x - 20, bean_center_y - 10, 15, 8))
    pygame.draw.ellipse(surface, (235, 240, 250), (bean_center_x + 15, bean_center_y - 5, 12, 7))
    # Shadow beneath Bean
    shadow_surface = pygame.Surface((120, 15), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow_surface, (0, 0, 0, 40), (0, 0, 120, 15))
    surface.blit(shadow_surface, (bean_center_x - 60, bean_center_y + 25))

    # Millennium Park Crown Fountain (interactive fountain)
    fountain_x, fountain_y = 180, 630
    # Fountain tower/screen (LED display tower)
    pygame.draw.rect(surface, (80, 90, 100), (fountain_x, fountain_y - 50, 25, 50))
    # LED screen effect (blue glow)
    pygame.draw.rect(surface, (50, 150, 255), (fountain_x + 3, fountain_y - 45, 19, 35))
    # Face outline on screen (iconic feature)
    pygame.draw.circle(surface, (100, 200, 255), (fountain_x + 12, fountain_y - 28), 6)
    # Water stream from mouth
    for water_y in range(fountain_y - 15, fountain_y + 15, 3):
        pygame.draw.circle(surface, (150, 200, 255), (fountain_x + 12, water_y), 2)
    # Water pool
    pygame.draw.rect(surface, (100, 180, 240), (fountain_x - 10, fountain_y + 15, 45, 8))
    # Splashing water effect
    for splash_x in range(fountain_x - 5, fountain_x + 35, 8):
        pygame.draw.circle(surface, (180, 220, 255), (splash_x, fountain_y + 16), 2)

    # Navy Pier Ferris Wheel (in the distance on lake)
    wheel_x, wheel_y = 1100, 480
    # Wheel structure
    pygame.draw.circle(surface, (200, 210, 220), (wheel_x, wheel_y), 35, 3)
    # Spokes
    for angle in range(0, 360, 45):
        import math
        end_x = wheel_x + int(math.cos(math.radians(angle)) * 32)
        end_y = wheel_y + int(math.sin(math.radians(angle)) * 32)
        pygame.draw.line(surface, (180, 190, 200), (wheel_x, wheel_y), (end_x, end_y), 2)
    # Gondolas (passenger cars)
    for angle in range(0, 360, 45):
        gondola_x = wheel_x + int(math.cos(math.radians(angle)) * 32)
        gondola_y = wheel_y + int(math.sin(math.radians(angle)) * 32)
        pygame.draw.rect(surface, (255, 100, 100), (gondola_x - 4, gondola_y - 3, 8, 6))
        pygame.draw.rect(surface, (255, 150, 150), (gondola_x - 3, gondola_y - 2, 6, 4))
    # Support structure
    pygame.draw.rect(surface, (150, 160, 170), (wheel_x - 3, wheel_y + 35, 6, 30))
    # Pier extending into lake
    pygame.draw.rect(surface, (120, 100, 80), (wheel_x - 60, wheel_y + 65, 120, 15))

    # Buckingham Fountain (iconic fountain)
    buckingham_x, buckingham_y = 450, 625
    # Main fountain basin
    pygame.draw.ellipse(surface, (100, 110, 120), (buckingham_x - 30, buckingham_y, 60, 20))
    # Water in basin
    pygame.draw.ellipse(surface, (120, 180, 220), (buckingham_x - 26, buckingham_y + 3, 52, 14))
    # Center water jet (tall)
    for jet_y in range(buckingham_y - 60, buckingham_y, 2):
        alpha = int(255 * (1 - (buckingham_y - jet_y) / 60))
        water_color = (150 + alpha // 10, 200 + alpha // 10, 240)
        pygame.draw.circle(surface, water_color, (buckingham_x, jet_y), 2)
    # Surrounding water jets (smaller)
    for angle in range(0, 360, 90):
        import math
        jet_x = buckingham_x + int(math.cos(math.radians(angle)) * 20)
        for offset_y in range(0, 25, 3):
            pygame.draw.circle(surface, (160, 210, 240), (jet_x, buckingham_y - offset_y), 1)
    # Fountain lights (pink/purple - evening mode)
    light_surface = pygame.Surface((70, 70), pygame.SRCALPHA)
    pygame.draw.circle(light_surface, (255, 180, 200, 60), (35, 35), 35)
    surface.blit(light_surface, (buckingham_x - 35, buckingham_y - 35))

    # Chicago Flag (iconic 4-star flag)
    flag_x, flag_y = 950, 580
    # Flag pole
    pygame.draw.rect(surface, (120, 120, 130), (flag_x, flag_y, 3, 50))
    # Flag (white with blue stripes and red stars)
    flag_width, flag_height = 40, 25
    # White background
    pygame.draw.rect(surface, (255, 255, 255), (flag_x + 3, flag_y + 10, flag_width, flag_height))
    # Blue stripes (top and bottom)
    pygame.draw.rect(surface, (100, 180, 220), (flag_x + 3, flag_y + 10, flag_width, 5))
    pygame.draw.rect(surface, (100, 180, 220), (flag_x + 3, flag_y + 30, flag_width, 5))
    # Four red stars (6-pointed Chicago stars)
    star_y = flag_y + 20
    for star_i, star_x_offset in enumerate([8, 17, 26, 35]):
        star_x = flag_x + star_x_offset
        # Simplified 6-pointed star (two triangles)
        pygame.draw.polygon(surface, (200, 50, 50), [
            (star_x, star_y - 3),
            (star_x - 2, star_y + 1),
            (star_x + 2, star_y + 1)
        ])
        pygame.draw.polygon(surface, (200, 50, 50), [
            (star_x, star_y + 3),
            (star_x - 2, star_y - 1),
            (star_x + 2, star_y - 1)
        ])

    # More boats on Chicago River
    boat_positions = [
        (840, 563, (255, 255, 255)),  # White boat
        (960, 565, (100, 150, 200)),  # Blue boat
        (1020, 562, (200, 180, 160)),  # Tan boat
    ]
    for boat_x, boat_y, boat_color in boat_positions:
        # Boat hull
        pygame.draw.polygon(surface, boat_color, [
            (boat_x, boat_y),
            (boat_x + 25, boat_y),
            (boat_x + 22, boat_y + 8),
            (boat_x + 3, boat_y + 8)
        ])
        # Cabin/deck
        pygame.draw.rect(surface, (240, 240, 245), (boat_x + 5, boat_y - 5, 15, 5))
        # Wake/waves
        pygame.draw.line(surface, (255, 255, 255), (boat_x - 5, boat_y + 4), (boat_x, boat_y + 6), 1)

    # Art Institute Lions (iconic bronze lions)
    lion_positions = [380, 430]
    for lion_x in lion_positions:
        lion_y = 650
        # Lion body (bronze color)
        bronze = (140, 120, 80)
        # Base pedestal
        pygame.draw.rect(surface, (180, 180, 190), (lion_x - 8, lion_y + 8, 16, 12))
        # Lion body (sitting pose)
        pygame.draw.ellipse(surface, bronze, (lion_x - 6, lion_y, 12, 10))
        # Lion head
        pygame.draw.circle(surface, bronze, (lion_x - 2, lion_y + 2), 4)
        # Mane
        pygame.draw.circle(surface, (120, 100, 60), (lion_x - 2, lion_y + 2), 5, 2)
        # Front paws
        pygame.draw.rect(surface, bronze, (lion_x - 5, lion_y + 8, 3, 5))
        pygame.draw.rect(surface, bronze, (lion_x + 2, lion_y + 8, 3, 5))

    # Chicago Theater marquee (iconic State Street theater)
    theater_x, theater_y = 650, 590
    # Theater building
    pygame.draw.rect(surface, (120, 40, 40), (theater_x, theater_y, 70, 70))
    # Vertical "CHICAGO" sign
    pygame.draw.rect(surface, (255, 220, 100), (theater_x + 25, theater_y - 30, 20, 80))
    pygame.draw.rect(surface, (220, 180, 60), (theater_x + 25, theater_y - 30, 20, 80), 2)
    # Bulb lights around sign
    for bulb_y in range(theater_y - 25, theater_y + 45, 8):
        pygame.draw.circle(surface, (255, 255, 200), (theater_x + 24, bulb_y), 2)
        pygame.draw.circle(surface, (255, 255, 200), (theater_x + 46, bulb_y), 2)
    # Theater marquee
    pygame.draw.rect(surface, (200, 50, 50), (theater_x, theater_y + 60, 70, 12))
    # Marquee lights
    for light_x in range(theater_x + 5, theater_x + 65, 8):
        pygame.draw.circle(surface, (255, 240, 180), (light_x, theater_y + 66), 2)

    # Additional architectural details on Willis Tower
    willis_tower_x = 630  # From earlier building definition
    # Antenna spires on top
    pygame.draw.rect(surface, (60, 70, 85), (willis_tower_x + 45, 160, 3, 25))
    pygame.draw.rect(surface, (60, 70, 85), (willis_tower_x + 52, 155, 3, 30))
    # Skydeck observation windows (bright)
    for deck_y in [600, 610, 620]:
        pygame.draw.rect(surface, (255, 200, 100), (willis_tower_x + 35, deck_y, 30, 3))

    # More street vendors (diverse Chicago food)
    vendor_positions = [
        (500, 655, 'italian_beef'),
        (850, 653, 'popcorn'),
    ]
    for vendor_x, vendor_y, vendor_type in vendor_positions:
        # Cart
        pygame.draw.rect(surface, (200, 50, 50) if vendor_type == 'italian_beef' else (220, 180, 100),
                        (vendor_x, vendor_y, 30, 15))
        # Umbrella
        pygame.draw.arc(surface, (255, 200, 0), (vendor_x - 5, vendor_y - 18, 40, 20), 0, 3.14, 2)
        # Vendor person
        pygame.draw.circle(surface, (180, 140, 120), (vendor_x + 15, vendor_y - 5), 3)
        pygame.draw.rect(surface, (255, 255, 255), (vendor_x + 13, vendor_y, 4, 8))
        # Cart wheels
        pygame.draw.circle(surface, (40, 40, 40), (vendor_x + 8, vendor_y + 17), 3)
        pygame.draw.circle(surface, (40, 40, 40), (vendor_x + 22, vendor_y + 17), 3)

    # More diverse pedestrians (Chicago style)
    chicago_pedestrians = [
        (350, 648, (30, 50, 120)),  # Business suit (blue)
        (410, 647, (200, 100, 100)),  # Red jacket
        (520, 649, (100, 100, 100)),  # Gray coat
        (780, 646, (50, 100, 50)),  # Green shirt
        (920, 648, (150, 120, 80)),  # Brown jacket
        (1050, 647, (80, 80, 200)),  # Purple shirt
    ]
    for ped_x, ped_y, clothing_color in chicago_pedestrians:
        # Head
        pygame.draw.circle(surface, (200, 170, 150), (ped_x, ped_y), 3)
        # Body
        pygame.draw.rect(surface, clothing_color, (ped_x - 3, ped_y + 3, 6, 10))
        # Legs
        pygame.draw.rect(surface, (50, 50, 80), (ped_x - 2, ped_y + 13, 2, 8))
        pygame.draw.rect(surface, (50, 50, 80), (ped_x + 1, ped_y + 13, 2, 8))

    # Chicago "L" train station sign
    l_sign_x, l_sign_y = 1000, 515
    # Sign pole
    pygame.draw.rect(surface, (100, 100, 110), (l_sign_x, l_sign_y + 20, 3, 30))
    # CTA sign (blue background with white circle and "L")
    pygame.draw.circle(surface, (0, 80, 160), (l_sign_x + 1, l_sign_y + 10), 10)
    pygame.draw.circle(surface, (255, 255, 255), (l_sign_x + 1, l_sign_y + 10), 6)
    pygame.draw.circle(surface, (0, 80, 160), (l_sign_x + 1, l_sign_y + 10), 4)

    # More clouds (Chicago windy sky)
    extra_clouds = [
        (300, 140), (500, 110), (700, 130), (900, 120), (1100, 125)
    ]
    for cloud_x, cloud_y in extra_clouds:
        pygame.draw.ellipse(surface, (240, 250, 255), (cloud_x, cloud_y, 50, 18))
        pygame.draw.ellipse(surface, (240, 250, 255), (cloud_x + 15, cloud_y - 5, 35, 18))
        pygame.draw.ellipse(surface, (240, 250, 255), (cloud_x + 25, cloud_y + 3, 30, 15))

    # Wind effect lines (animated wind streaks)
    wind_lines = [
        (50, 200), (150, 250), (280, 180), (400, 220), (550, 190),
        (680, 240), (800, 210), (950, 230), (1050, 195), (1180, 215)
    ]
    for wind_x, wind_y in wind_lines:
        # Multiple streaks for wind effect
        pygame.draw.line(surface, (220, 235, 250), (wind_x, wind_y), (wind_x + 25, wind_y - 5), 1)
        pygame.draw.line(surface, (230, 240, 252), (wind_x + 5, wind_y + 8), (wind_x + 30, wind_y + 3), 1)

    return surface


def create_city_background(width, height, city_name):
    """Create a detailed background with cityscape."""
    if city_name == 'boston':
        return create_boston_background(width, height)
    elif city_name == 'nyc':
        return create_nyc_background(width, height)
    elif city_name == 'chicago':
        return create_chicago_background(width, height)
    else:
        # Fallback for unknown cities
        surface = pygame.Surface((width, height))
        surface.fill((100, 150, 200))
        return surface
