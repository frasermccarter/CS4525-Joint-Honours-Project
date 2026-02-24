"""
Main entry point for the music engine.
Exports Controller, Track, Sequence, and Note for user convenience.
"""

from music_engine.engine.controller import Controller
from music_engine.core.track import Track
from music_engine.core.sequence import Sequence
from music_engine.core.note import Note

__all__ = ['Controller', 'Track', 'Sequence', 'Note']
