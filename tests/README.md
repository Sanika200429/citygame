# City Runner: Coast to Coast - Tests

This directory contains unit tests for the City Runner game.

## Running Tests

To run all tests:

```bash
python -m unittest discover tests
```

To run a specific test file:

```bash
python -m unittest tests.test_player
```

To run a specific test case:

```bash
python -m unittest tests.test_player.TestPlayer.test_player_initialization
```

## Test Coverage

Current test modules:

- `test_config.py` - Tests for game configuration constants
- `test_player.py` - Tests for Player class functionality

## Writing Tests

When adding new tests, follow these guidelines:

1. Create test files with the naming pattern `test_*.py`
2. Inherit test classes from `unittest.TestCase`
3. Name test methods starting with `test_`
4. Use descriptive test names that explain what is being tested
5. Add docstrings to test methods explaining the test purpose

Example:

```python
import unittest
from src.module import ClassToTest

class TestClassName(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.instance = ClassToTest()

    def test_specific_behavior(self):
        """Test that specific behavior works correctly."""
        result = self.instance.method()
        self.assertEqual(result, expected_value)
```

## Test Requirements

Make sure pygame is initialized before running tests that require it:

```python
@classmethod
def setUpClass(cls):
    """Set up pygame for all tests."""
    pygame.init()
```

## Future Test Areas

Areas that need test coverage:

- Enemy classes
- Collectibles
- Level generation
- Collision detection
- Game states (menu, gameplay, etc.)
- Camera system
- Audio manager
