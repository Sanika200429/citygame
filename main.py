"""
City Runner: Coast to Coast
Main entry point for the game.

A side-scrolling platformer journey through iconic American cities.
Run through Boston, New York City, and Chicago collecting items,
avoiding enemies, and reaching famous landmarks!

Controls:
- Arrow Keys / WASD: Move
- Space / W / Up: Jump
- Shift: Sprint
- ESC: Pause
- Enter: Select/Continue
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.game import Game


def main():
    """Main entry point."""
    print("=" * 60)
    print("CITY RUNNER: COAST TO COAST")
    print("=" * 60)
    print("\nStarting game...")
    print("\nControls:")
    print("  Movement: Arrow Keys or WASD")
    print("  Jump: Space or W or Up Arrow")
    print("  Sprint: Hold Shift")
    print("  Pause: ESC")
    print("  Select: Enter")
    print("\n" + "=" * 60 + "\n")

    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        return 1

    print("\nThanks for playing City Runner: Coast to Coast!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
