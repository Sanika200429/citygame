# loads sprites and backgrounds, creates placeholders if files are missing

import pygame
import os
from config import SPRITES_DIR, BACKGROUNDS_DIR
from src.utils import sprite_generator


class AssetLoader:

    def __init__(self):
        self.sprite_cache = {}
        self.background_cache = {}

    def load_sprite(self, path, size=None, fallback_color=(255, 0, 255)):
        cache_key = f"{path}_{size}"

        # check if we already loaded this
        if cache_key in self.sprite_cache:
            return self.sprite_cache[cache_key]

        full_path = os.path.join(SPRITES_DIR, path)

        # try to load from file
        if os.path.exists(full_path):
            try:
                image = pygame.image.load(full_path).convert_alpha()
                if size:
                    image = pygame.transform.scale(image, size)
                self.sprite_cache[cache_key] = image
                return image
            except pygame.error as e:
                print(f"Warning: Could not load sprite {path}: {e}")

        # if file doesn't exist, generate a placeholder
        if size:
            width, height = size
        else:
            width, height = 32, 32

        placeholder = self._generate_sprite(path, width, height, fallback_color)
        self.sprite_cache[cache_key] = placeholder
        return placeholder

    def _generate_sprite(self, path, width, height, fallback_color):
        # generate sprites based on name
        path_lower = path.lower()

        # enemies
        if 'pigeon' in path_lower:
            return sprite_generator.draw_pigeon(width, height)
        elif 'taxi' in path_lower:
            return sprite_generator.draw_taxi(width, height)
        elif 'rat' in path_lower:
            return sprite_generator.draw_rat(width, height)
        elif 'cyclist' in path_lower:
            return sprite_generator.draw_cyclist(width, height)
        elif 'vendor' in path_lower:
            return sprite_generator.draw_vendor(width, height)
        elif 'flying_paper' in path_lower or 'paper' in path_lower:
            return sprite_generator.draw_flying_paper(width, height)

        # collectibles
        elif 'pizza' in path_lower or 'deep_dish' in path_lower:
            return sprite_generator.draw_collectible_pizza(width, height)
        elif 'teacup' in path_lower:
            return sprite_generator.draw_collectible_teacup(width, height)
        elif 'hot_dog' in path_lower:
            return sprite_generator.draw_collectible_hot_dog(width, height)
        elif 'book' in path_lower:
            return sprite_generator.draw_collectible_book(width, height)
        elif 'bagel' in path_lower:
            return sprite_generator.draw_collectible_bagel(width, height)
        elif 'metrocard' in path_lower:
            return sprite_generator.draw_collectible_metrocard(width, height)
        elif 'jazz' in path_lower:
            return sprite_generator.draw_collectible_jazz_note(width, height)

        # just a colored box if we don't know what it is
        else:
            placeholder = pygame.Surface((width, height), pygame.SRCALPHA)
            placeholder.fill(fallback_color)
            return placeholder

    def load_spritesheet(self, path, frame_width, frame_height, num_frames, fallback_color=(255, 0, 255)):
        """
        Load a sprite sheet and split it into frames.

        Args:
            path: Path to sprite sheet relative to sprites directory
            frame_width: Width of each frame
            frame_height: Height of each frame
            num_frames: Number of frames to extract
            fallback_color: Color for placeholder if image not found

        Returns:
            List of pygame.Surface objects (one per frame)
        """
        full_path = os.path.join(SPRITES_DIR, path)
        frames = []

        if os.path.exists(full_path):
            try:
                sheet = pygame.image.load(full_path).convert_alpha()
                for i in range(num_frames):
                    frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
                    frame.blit(sheet, (0, 0), (i * frame_width, 0, frame_width, frame_height))
                    frames.append(frame)
                return frames
            except pygame.error as e:
                print(f"Warning: Could not load spritesheet {path}: {e}")

        # Fallback to colored rectangles
        for _ in range(num_frames):
            placeholder = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
            placeholder.fill(fallback_color)
            frames.append(placeholder)

        return frames

    def load_animation_frames(self, directory, frame_prefix, num_frames, size=None, fallback_color=(255, 0, 255)):
        """
        Load animation frames from individual files.

        Args:
            directory: Directory containing frames (relative to sprites dir)
            frame_prefix: Prefix for frame files (e.g., "idle_")
            num_frames: Number of frames to load
            size: Tuple (width, height) to scale frames, or None
            fallback_color: Color for placeholder if images not found

        Returns:
            List of pygame.Surface objects (animation frames)
        """
        frames = []

        for i in range(num_frames):
            # Try common naming patterns
            possible_names = [
                f"{frame_prefix}{i}.png",
                f"{frame_prefix}{i:02d}.png",
                f"{frame_prefix}{i+1}.png",
                f"{frame_prefix}{i+1:02d}.png",
            ]

            loaded = False
            for name in possible_names:
                path = os.path.join(directory, name)
                full_path = os.path.join(SPRITES_DIR, path)

                if os.path.exists(full_path):
                    try:
                        image = pygame.image.load(full_path).convert_alpha()
                        if size:
                            image = pygame.transform.scale(image, size)
                        frames.append(image)
                        loaded = True
                        break
                    except pygame.error:
                        continue

            # Fallback if frame not found
            if not loaded:
                if size:
                    width, height = size
                else:
                    width, height = 32, 32

                # Generate player animation frames
                if 'player' in directory.lower():
                    if 'idle' in directory.lower():
                        placeholder = sprite_generator.draw_player_idle(width, height)
                    elif 'run' in directory.lower():
                        placeholder = sprite_generator.draw_player_run(width, height, i)
                    elif 'jump' in directory.lower():
                        placeholder = sprite_generator.draw_player_jump(width, height)
                    else:
                        placeholder = sprite_generator.draw_player_idle(width, height)
                else:
                    placeholder = pygame.Surface((width, height), pygame.SRCALPHA)
                    placeholder.fill(fallback_color)

                frames.append(placeholder)

        return frames

    def load_background(self, path, size=None, fallback_color=(50, 50, 80)):
        """
        Load a background image.

        Args:
            path: Path relative to backgrounds directory
            size: Tuple (width, height) to scale the background, or None
            fallback_color: Color for placeholder if image not found

        Returns:
            pygame.Surface with the background
        """
        cache_key = f"bg_{path}_{size}"

        # Check cache
        if cache_key in self.background_cache:
            return self.background_cache[cache_key]

        full_path = os.path.join(BACKGROUNDS_DIR, path)

        # Try to load the image
        if os.path.exists(full_path):
            try:
                image = pygame.image.load(full_path).convert()
                if size:
                    image = pygame.transform.scale(image, size)
                self.background_cache[cache_key] = image
                return image
            except pygame.error as e:
                print(f"Warning: Could not load background {path}: {e}")

        # Fallback to generated city background
        if size:
            width, height = size
        else:
            width, height = 1280, 720

        # Extract city name from path
        city_name = 'boston'  # default
        if 'nyc' in path.lower():
            city_name = 'nyc'
        elif 'chicago' in path.lower():
            city_name = 'chicago'
        elif 'boston' in path.lower():
            city_name = 'boston'

        background = sprite_generator.create_city_background(width, height, city_name)
        self.background_cache[cache_key] = background
        return background

    def clear_cache(self):
        """Clear all cached assets."""
        self.sprite_cache.clear()
        self.background_cache.clear()


# Global asset loader instance
asset_loader = AssetLoader()
