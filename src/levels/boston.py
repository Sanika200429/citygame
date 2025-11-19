# boston level - fall theme with brick streets

from src.levels.level import Level
from src.entities.enemies.cyclist import Cyclist
from src.entities.enemies.pigeon import Pigeon
from src.entities.enemies.taxi import Taxi
from src.entities.collectible import Collectible, create_city_collectibles
from config import *
import pygame
import random


class BostonLevel(Level):

    def __init__(self):
        super().__init__('boston', LEVEL_WIDTH)
        self.platform_data = []
        self.setup_level()

    def setup_level(self):
        self.create_platforms()
        self.create_enemies()
        self.create_collectibles()

        self.checkpoints = [1000, 2000, 3000]
        self.landmark_position = LEVEL_WIDTH - 300  # fenway park

    def create_platforms(self):
        ground_y = SCREEN_HEIGHT - 100

        # the ground
        ground_rect = pygame.Rect(0, ground_y, self.level_width, 100)
        self.platforms.append(ground_rect)
        self.platform_data.append({'rect': ground_rect, 'type': 'ground'})

        # brownstone stoops
        stoop_positions = [
            (250, ground_y - 40, 80),
            (600, ground_y - 35, 90),
            (950, ground_y - 45, 85),
            (1300, ground_y - 40, 75),
            (1650, ground_y - 38, 95),
            (2100, ground_y - 42, 80),
            (2550, ground_y - 45, 90),
            (2900, ground_y - 40, 85),
            (3300, ground_y - 35, 100),
        ]

        for x, y, width in stoop_positions:
            rect = pygame.Rect(x, y, width, 15)
            self.platforms.append(rect)
            self.platform_data.append({'rect': rect, 'type': 'stoop'})

        # awnings and balconies
        awning_positions = [
            (400, ground_y - 120, 200),
            (700, ground_y - 140, 150),
            (1050, ground_y - 125, 180),
            (1450, ground_y - 135, 160),
            (1850, ground_y - 130, 190),
            (2250, ground_y - 145, 170),
            (2650, ground_y - 125, 185),
            (3050, ground_y - 140, 175),
        ]

        for x, y, width in awning_positions:
            rect = pygame.Rect(x, y, width, 12)
            self.platforms.append(rect)
            self.platform_data.append({'rect': rect, 'type': 'awning'})

        # fire escapes
        fire_escape_positions = [
            (500, ground_y - 200, 120),
            (900, ground_y - 240, 110),
            (1400, ground_y - 220, 130),
            (1800, ground_y - 250, 115),
            (2200, ground_y - 230, 125),
            (2700, ground_y - 245, 120),
            (3100, ground_y - 210, 140),
        ]

        for x, y, width in fire_escape_positions:
            rect = pygame.Rect(x, y, width, 10)
            self.platforms.append(rect)
            self.platform_data.append({'rect': rect, 'type': 'fire_escape'})

        # rooftops
        rooftop_positions = [
            (800, ground_y - 300, 180),
            (1200, ground_y - 280, 160),
            (1600, ground_y - 320, 150),
            (2000, ground_y - 290, 200),
            (2400, ground_y - 310, 170),
            (2800, ground_y - 285, 180),
            (3200, ground_y - 295, 190),
        ]

        for x, y, width in rooftop_positions:
            rect = pygame.Rect(x, y, width, 18)
            self.platforms.append(rect)
            self.platform_data.append({'rect': rect, 'type': 'rooftop'})

        # park benches
        bench_positions = [
            (350, ground_y - 25, 50),
            (1100, ground_y - 25, 55),
            (1750, ground_y - 25, 50),
            (2350, ground_y - 25, 60),
            (3000, ground_y - 25, 50),
        ]

        for x, y, width in bench_positions:
            rect = pygame.Rect(x, y, width, 8)
            self.platforms.append(rect)
            self.platform_data.append({'rect': rect, 'type': 'bench'})

    def draw_platforms(self, screen, camera_offset):
        for platform_info in self.platform_data:
            platform = platform_info['rect']
            platform_type = platform_info['type']

            # where to draw it on screen
            screen_rect = pygame.Rect(
                platform.x - camera_offset,
                platform.y,
                platform.width,
                platform.height
            )

            # draw different styles for each platform type
            if platform_type == 'ground':
                pygame.draw.rect(screen, (80, 70, 60), screen_rect)

            elif platform_type == 'stoop':
                # red brick stoops
                base_color = (120, 50, 45)
                pygame.draw.rect(screen, base_color, screen_rect)
                # Brick texture
                for bx in range(0, screen_rect.width, 16):
                    pygame.draw.line(screen, (100, 40, 35),
                                   (screen_rect.x + bx, screen_rect.y),
                                   (screen_rect.x + bx, screen_rect.bottom), 1)
                # Top edge highlight
                pygame.draw.line(screen, (140, 70, 65),
                               (screen_rect.x, screen_rect.y),
                               (screen_rect.right, screen_rect.y), 2)

            elif platform_type == 'awning':
                # striped awnings
                stripe_width = 12
                for i in range(0, screen_rect.width, stripe_width):
                    color = (180, 40, 40) if (i // stripe_width) % 2 == 0 else (220, 200, 200)
                    stripe_rect = pygame.Rect(
                        screen_rect.x + i,
                        screen_rect.y,
                        min(stripe_width, screen_rect.width - i),
                        screen_rect.height
                    )
                    pygame.draw.rect(screen, color, stripe_rect)
                # Bottom edge (fabric fold)
                pygame.draw.line(screen, (120, 20, 20),
                               (screen_rect.x, screen_rect.bottom - 1),
                               (screen_rect.right, screen_rect.bottom - 1), 2)

            elif platform_type == 'fire_escape':
                # metal fire escapes
                base_color = (70, 75, 80)
                pygame.draw.rect(screen, base_color, screen_rect)
                # Metal grid
                for gx in range(0, screen_rect.width, 8):
                    pygame.draw.line(screen, (50, 55, 60),
                                   (screen_rect.x + gx, screen_rect.y),
                                   (screen_rect.x + gx, screen_rect.bottom), 1)
                # Highlight edge (metallic shine)
                pygame.draw.line(screen, (100, 105, 110),
                               (screen_rect.x, screen_rect.y),
                               (screen_rect.right, screen_rect.y), 1)
                # Bolts
                for bolt_x in range(8, screen_rect.width - 8, 24):
                    pygame.draw.circle(screen, (50, 50, 55),
                                     (screen_rect.x + bolt_x, screen_rect.y + screen_rect.height // 2), 2)

            elif platform_type == 'rooftop':
                # tar paper roofs
                base_color = (45, 45, 50)
                pygame.draw.rect(screen, base_color, screen_rect)
                # Tar paper texture (random dark spots)
                random.seed(platform.x + platform.y)  # Consistent random for each platform
                for _ in range(screen_rect.width // 20):
                    spot_x = screen_rect.x + random.randint(0, screen_rect.width)
                    spot_y = screen_rect.y + random.randint(0, screen_rect.height)
                    pygame.draw.circle(screen, (35, 35, 40), (spot_x, spot_y), 2)
                # Edge (rooftop border)
                pygame.draw.rect(screen, (60, 55, 50), screen_rect, 2)

            elif platform_type == 'bench':
                # wooden benches
                wood_color = (101, 67, 33)
                pygame.draw.rect(screen, wood_color, screen_rect)
                # Wood slats (vertical lines)
                for slat_x in range(0, screen_rect.width, 10):
                    pygame.draw.line(screen, (85, 55, 25),
                                   (screen_rect.x + slat_x, screen_rect.y),
                                   (screen_rect.x + slat_x, screen_rect.bottom), 1)
                # Top highlight
                pygame.draw.line(screen, (120, 85, 50),
                               (screen_rect.x, screen_rect.y),
                               (screen_rect.right, screen_rect.y), 1)

    def create_enemies(self):
        ground_y = SCREEN_HEIGHT - 148

        # cyclists riding around
        cyclist_positions = [500, 1100, 1900, 2600]
        for x in cyclist_positions:
            self.enemies.append(Cyclist(x, ground_y, patrol_distance=200))

        # pigeons flying around
        pigeon_positions = [(700, 300), (1400, 250), (2200, 280), (3000, 260)]
        for x, y in pigeon_positions:
            self.enemies.append(Pigeon(x, y, flight_height=80))

        # taxis zoom through
        self.enemies.append(Taxi(100, ground_y + 8))

    def create_collectibles(self):
        ground_y = SCREEN_HEIGHT - 100

        # tea cups everywhere
        for i in range(30):
            x = random.randint(200, self.level_width - 200)
            y = ground_y - 50
            self.collectibles.append(Collectible(x, y, 'teacup'))

        # books on platforms (worth more)
        book_positions = [
            (450, ground_y - 150),
            (850, ground_y - 210),
            (1250, ground_y - 180),
            (1650, ground_y - 230),
            (2050, ground_y - 170),
            (2450, ground_y - 220),
            (2850, ground_y - 190),
            (3250, ground_y - 160),
        ]

        for x, y in book_positions:
            self.collectibles.append(Collectible(x, y, 'book'))

        # more tea cups on some platforms
        for platform in self.platforms[1:]:
            if random.random() < 0.6:
                x = platform.x + platform.width // 2
                y = platform.y - 30
                self.collectibles.append(Collectible(x, y, 'teacup'))
