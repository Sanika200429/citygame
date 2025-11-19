"""
Audio manager for music and sound effects.
Handles loading, playing, and volume control for all game audio.
"""

import pygame
import os
from config import AUDIO_DIR, MUSIC_VOLUME, SFX_VOLUME, AMBIENT_VOLUME


class AudioManager:
    """Manages all game audio including music, SFX, and ambient sounds."""

    def __init__(self):
        """Initialize the audio manager."""
        pygame.mixer.init()

        # Storage for loaded sounds
        self.music = {}
        self.sfx = {}
        self.ambient = {}

        # Current playing track
        self.current_music = None

        # Volume levels
        self.music_volume = MUSIC_VOLUME
        self.sfx_volume = SFX_VOLUME
        self.ambient_volume = AMBIENT_VOLUME

        # Load audio files
        self.load_audio()

    def load_audio(self):
        """Load all audio files from assets directory."""
        # Load music (if files exist)
        music_dir = os.path.join(AUDIO_DIR, 'music')
        if os.path.exists(music_dir):
            for filename in os.listdir(music_dir):
                if filename.endswith(('.ogg', '.mp3', '.wav')):
                    name = os.path.splitext(filename)[0]
                    self.music[name] = os.path.join(music_dir, filename)

        # Load SFX (if files exist)
        sfx_dir = os.path.join(AUDIO_DIR, 'sfx')
        if os.path.exists(sfx_dir):
            for filename in os.listdir(sfx_dir):
                if filename.endswith('.wav'):
                    name = os.path.splitext(filename)[0]
                    try:
                        self.sfx[name] = pygame.mixer.Sound(os.path.join(sfx_dir, filename))
                        self.sfx[name].set_volume(self.sfx_volume)
                    except pygame.error:
                        pass  # Skip if file can't be loaded

        # Load ambient sounds (if files exist)
        ambient_dir = os.path.join(AUDIO_DIR, 'ambient')
        if os.path.exists(ambient_dir):
            for filename in os.listdir(ambient_dir):
                if filename.endswith(('.ogg', '.wav')):
                    name = os.path.splitext(filename)[0]
                    try:
                        self.ambient[name] = pygame.mixer.Sound(os.path.join(ambient_dir, filename))
                        self.ambient[name].set_volume(self.ambient_volume)
                    except pygame.error:
                        pass  # Skip if file can't be loaded

    def play_music(self, track_name, loops=-1, fade_ms=1000):
        """
        Play background music.

        Args:
            track_name: Name of the music track (without extension)
            loops: Number of times to loop (-1 for infinite)
            fade_ms: Fade in time in milliseconds
        """
        if track_name in self.music and track_name != self.current_music:
            try:
                pygame.mixer.music.load(self.music[track_name])
                pygame.mixer.music.set_volume(self.music_volume)
                pygame.mixer.music.play(loops, fade_ms=fade_ms)
                self.current_music = track_name
            except pygame.error:
                pass  # Silently fail if music can't be played

    def stop_music(self, fade_ms=1000):
        """
        Stop currently playing music.

        Args:
            fade_ms: Fade out time in milliseconds
        """
        if fade_ms > 0:
            pygame.mixer.music.fadeout(fade_ms)
        else:
            pygame.mixer.music.stop()
        self.current_music = None

    def play_sfx(self, sfx_name):
        """
        Play a sound effect.

        Args:
            sfx_name: Name of the sound effect (without extension)
        """
        if sfx_name in self.sfx:
            self.sfx[sfx_name].play()

    def play_ambient(self, ambient_name, loops=-1):
        """
        Play ambient sound.

        Args:
            ambient_name: Name of the ambient sound (without extension)
            loops: Number of times to loop (-1 for infinite)
        """
        if ambient_name in self.ambient:
            self.ambient[ambient_name].play(loops=loops)

    def stop_ambient(self, ambient_name):
        """
        Stop ambient sound.

        Args:
            ambient_name: Name of the ambient sound to stop
        """
        if ambient_name in self.ambient:
            self.ambient[ambient_name].stop()

    def set_music_volume(self, volume):
        """
        Set music volume (0.0 to 1.0).

        Args:
            volume: Volume level from 0.0 (silent) to 1.0 (max)
        """
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)

    def set_sfx_volume(self, volume):
        """
        Set sound effects volume (0.0 to 1.0).

        Args:
            volume: Volume level from 0.0 (silent) to 1.0 (max)
        """
        self.sfx_volume = max(0.0, min(1.0, volume))
        for sound in self.sfx.values():
            sound.set_volume(self.sfx_volume)

    def set_ambient_volume(self, volume):
        """
        Set ambient sounds volume (0.0 to 1.0).

        Args:
            volume: Volume level from 0.0 (silent) to 1.0 (max)
        """
        self.ambient_volume = max(0.0, min(1.0, volume))
        for sound in self.ambient.values():
            sound.set_volume(self.ambient_volume)

    def pause_music(self):
        """Pause currently playing music."""
        pygame.mixer.music.pause()

    def unpause_music(self):
        """Resume paused music."""
        pygame.mixer.music.unpause()
