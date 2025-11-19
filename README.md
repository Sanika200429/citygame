# City Runner: Coast to Coast

A charming side-scrolling platformer adventure through three iconic American cities!

## Overview

Run, jump, and collect your way through Boston, New York City, and Chicago. Each city features unique collectibles, quirky enemies, and ends at a famous landmark. Unlock cities progressively and master the art of urban parkour!

## Features

- **3 Unique Cities**: Boston, NYC, and Chicago - each with distinct art style and atmosphere
- **City-Specific Collectibles**: Tea cups in Boston, pizza slices in NYC, hot dogs in Chicago
- **Diverse Enemies**: Cyclists, pigeons, taxis, rats, vendors, and flying papers
- **Smooth Platforming**: Responsive controls with jump, sprint, and double-jump mechanics
- **Progressive Unlocking**: Beat one city to unlock the next
- **Landmark Celebrations**: Special animations when reaching iconic landmarks
- **Checkpoint System**: Never lose too much progress
- **Score Tracking**: Compete for high scores

## Installation

### Requirements
- Python 3.8 or higher
- Pygame 2.5+

### Setup

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd CityRunner_CoastToCoast
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the game:
   ```bash
   python main.py
   ```

## Controls

| Action | Keys |
|--------|------|
| Move Left/Right | Arrow Keys or A/D |
| Jump | Space, W, or Up Arrow |
| Sprint | Hold Shift while moving |
| Pause | ESC |
| Select/Continue | Enter |
| Restart (when dead) | R |

## Game Progression

1. **Start**: Begin at the main menu
2. **City Selection**: Choose from unlocked cities (Boston is always available)
3. **Play Through Level**: Collect items, avoid enemies, reach the landmark
4. **Celebrate**: Watch the landmark celebration animation
5. **Unlock Next City**: The next city becomes available
6. **Repeat**: Continue through all three cities!

## Cities Guide

### Boston
- **Theme**: Fall leaves, brick streets, cozy colonial architecture
- **Collectibles**: Tea Cups (10 pts), Books (25 pts)
- **Enemies**: Cyclists, Pigeons, Taxis, Traffic Cones
- **Landmark**: Fenway Park (Green Monster)
- **Atmosphere**: Warm, academic, nostalgic

### New York City
- **Theme**: Neon nights, skyscrapers, urban energy
- **Collectibles**: Pizza Slices (15 pts), MetroCards (20 pts), Bagels (10 pts)
- **Enemies**: Rats, Taxis, Street Vendors
- **Landmark**: Times Square
- **Atmosphere**: Energetic, bustling, electric

### Chicago
- **Theme**: Windy lakefront, modern skyline
- **Collectibles**: Deep-Dish Pizza (20 pts), Hot Dogs (15 pts), Jazz Notes (25 pts)
- **Enemies**: Aggressive Pigeons, Flying Papers, Snow Piles
- **Landmark**: The Chicago Bean (Cloud Gate)
- **Atmosphere**: Breezy, sophisticated, dynamic

## Project Structure

```
CityRunner_CoastToCoast/
├── main.py                 # Entry point
├── config.py               # Game constants
├── requirements.txt        # Dependencies
├── src/
│   ├── game.py            # Main game manager
│   ├── player.py          # Player character
│   ├── camera.py          # Camera system
│   ├── entities/          # Game entities
│   │   ├── entity.py      # Base entity class
│   │   ├── collectible.py # Collectible items
│   │   └── enemies/       # Enemy classes
│   ├── levels/            # Level definitions
│   │   ├── level.py       # Base level
│   │   ├── boston.py      # Boston level
│   │   ├── nyc.py         # NYC level
│   │   └── chicago.py     # Chicago level
│   ├── states/            # Game states
│   │   ├── menu.py        # Main menu
│   │   ├── city_select.py # City selection
│   │   ├── gameplay.py    # Active gameplay
│   │   └── landmark.py    # Celebration
│   └── utils/             # Utility functions
├── assets/                # Game assets (you'll add these)
│   ├── sprites/
│   ├── backgrounds/
│   ├── audio/
│   └── data/
└── docs/
    └── GAME_DESIGN_DOCUMENT.md
```

## Customization & Extension

### Adding Your Own Art

The game currently uses placeholder graphics. To add your own pixel art:

1. **Player Sprites**: Place in `assets/sprites/player/`
   - Idle animation frames
   - Run animation frames
   - Jump frames
   - Hurt frames

2. **Enemy Sprites**: Place in `assets/sprites/enemies/[enemy_name]/`

3. **Collectibles**: Place in `assets/sprites/collectibles/`

4. **Backgrounds**: Place in `assets/backgrounds/[city_name]/`
   - Use multiple layers for parallax effect

### Modifying Levels

Edit the level files in `src/levels/`:
- `boston.py`
- `nyc.py`
- `chicago.py`

Each level has methods to customize:
- `create_platforms()` - Add/modify platform positions
- `create_enemies()` - Change enemy placement
- `create_collectibles()` - Adjust collectible distribution

### Tweaking Game Feel

Modify values in [config.py](config.py):
- `PLAYER_SPEED` - Running speed
- `PLAYER_JUMP_STRENGTH` - Jump height
- `PLAYER_GRAVITY` - Fall speed
- `PLAYER_MAX_HEALTH` - Starting health
- Enemy speeds and behaviors

## Development Roadmap

### Current Features (v1.0)
- [x] Three playable cities
- [x] Player movement and physics
- [x] Enemy AI behaviors
- [x] Collectibles system
- [x] Progressive unlocking
- [x] Checkpoint system
- [x] Landmark celebrations

### Planned Features (v2.0)
- [ ] Custom pixel art assets
- [ ] Background music for each city
- [ ] Sound effects
- [ ] Power-ups (speed boost, shield, magnet)
- [ ] Achievements system
- [ ] High score leaderboard
- [ ] Additional cities
- [ ] Time trial mode

## Debugging

Enable debug mode in [config.py](config.py):

```python
DEBUG_MODE = True
SHOW_HITBOXES = True
SHOW_FPS = True
```

This will show:
- FPS counter
- Entity hitboxes
- Additional debug information

## Credits

**Game Design**: Based on the "City Runner: Coast to Coast" concept
**Engine**: Pygame
**Programming**: Python 3

## License

This project is provided as-is for educational and entertainment purposes.

## Contributing

Feel free to fork this project and add your own features! Some ideas:
- New cities (San Francisco, Miami, Seattle, etc.)
- New enemy types
- Boss battles at landmarks
- Multiplayer mode
- Level editor

## Troubleshooting

### Game won't start
- Ensure Python 3.8+ is installed: `python --version`
- Install Pygame: `pip install pygame`
- Check for error messages in the console

### Low FPS
- Reduce window size in [config.py](config.py)
- Disable debug mode
- Close other applications

### Controls not responding
- Make sure the game window is in focus
- Try clicking on the window first
- Check keyboard layout (use arrow keys if WASD doesn't work)

## Have Fun!

Enjoy your coast-to-coast journey through America's greatest cities!

For the complete game design details, see [GAME_DESIGN_DOCUMENT.md](GAME_DESIGN_DOCUMENT.md)
