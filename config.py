# game config stuff
# all the constants and settings go here

# screen stuff
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "City Runner: Coast to Coast"

# basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# each city has its own vibe
BOSTON_COLORS = {
    'brick_red': (180, 70, 58),
    'autumn_orange': (232, 155, 60),
    'deep_green': (47, 82, 51),
    'cream': (244, 232, 208)
}

NYC_COLORS = {
    'electric_blue': (0, 191, 255),
    'hot_pink': (255, 20, 147),
    'taxi_yellow': (255, 215, 0),
    'steel_gray': (112, 128, 144)
}

CHICAGO_COLORS = {
    'cool_blue': (70, 130, 180),
    'silver_gray': (192, 192, 192),
    'deep_purple': (102, 51, 153),
    'icy_white': (240, 248, 255)
}

# player character settings
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 48
PLAYER_SPEED = 5
PLAYER_SPRINT_MULTIPLIER = 1.5
PLAYER_JUMP_STRENGTH = -15  # negative means up
PLAYER_GRAVITY = 0.8
PLAYER_MAX_FALL_SPEED = 15
PLAYER_ACCELERATION = 0.5
PLAYER_FRICTION = 0.85  # makes movement feel smoother
PLAYER_MAX_HEALTH = 5
PLAYER_INVINCIBILITY_TIME = 2000  # ms after getting hit

# camera follows the player
CAMERA_SPEED = 5
CAMERA_PLAYER_OFFSET_X = SCREEN_WIDTH // 3  # keep player left of center
CAMERA_LOOKAHEAD = 100

# physics stuff
GRAVITY = 0.8
TERMINAL_VELOCITY = 15

# how much each collectible is worth
COLLECTIBLE_VALUES = {
    # Boston
    'teacup': 10,
    'book': 25,
    # NYC
    'pizza': 15,
    'metrocard': 20,
    'bagel': 10,
    # Chicago
    'deep_dish': 20,
    'hot_dog': 15,
    'jazz_note': 25
}

# enemy types and their stats
ENEMY_TYPES = {
    'cyclist': {
        'speed': 2,
        'health': 1,
        'points': 50,
        'width': 40,
        'height': 50
    },
    'pigeon': {
        'speed': 1.5,
        'health': 1,
        'points': 25,
        'width': 30,
        'height': 20
    },
    'taxi': {
        'speed': 8,
        'health': 999,  # can't kill taxis lol
        'points': 0,
        'width': 80,
        'height': 40
    },
    'rat': {
        'speed': 3,
        'health': 1,
        'points': 30,
        'width': 25,
        'height': 15
    },
    'vendor': {
        'speed': 1,
        'health': 999,  # vendors are friendly
        'points': 0,
        'width': 60,
        'height': 50
    },
    'flying_paper': {
        'speed': 2.5,
        'health': 1,
        'points': 20,
        'width': 20,
        'height': 20
    }
}

# powerup durations in ms
POWERUP_DURATION = {
    'speed_sneakers': 10000,
    'shield': 15000,
    'magnet': 12000,
    'score_multiplier': 15000
}

# level dimensions
LEVEL_WIDTH = 4000
CHECKPOINT_POSITIONS = [1000, 2000, 3000]
TILE_SIZE = 32

# the three cities you run through
CITIES = ['boston', 'nyc', 'chicago']
CITY_NAMES = {
    'boston': 'Boston',
    'nyc': 'New York City',
    'chicago': 'Chicago'
}

CITY_LANDMARKS = {
    'boston': 'Fenway Park',
    'nyc': 'Times Square',
    'chicago': 'The Chicago Bean'
}

# sound volumes
MUSIC_VOLUME = 0.7
SFX_VOLUME = 0.8
AMBIENT_VOLUME = 0.3

# where all the assets are stored
ASSETS_DIR = 'assets'
SPRITES_DIR = f'{ASSETS_DIR}/sprites'
BACKGROUNDS_DIR = f'{ASSETS_DIR}/backgrounds'
AUDIO_DIR = f'{ASSETS_DIR}/audio'
DATA_DIR = f'{ASSETS_DIR}/data'

# debug stuff - turn off for release
DEBUG_MODE = True
SHOW_HITBOXES = False
SHOW_FPS = True
