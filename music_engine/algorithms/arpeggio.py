"""
An arpeggio generator, given a chord or set of notes (possible later a scale), play each note in sequence.
"""

import random

from music_engine.core.chord import Chord

class Arpeggio:
    def __init__(self):
        pass

    def generate_from_chord(self, chord_symbol, octave=4, note_duration=0.5, direction="up"):
        """
        Generate an arpeggio sequence from a chord symbol.
        
        Parameters:
        - chord_symbol: String representing the chord (e.g., "Cmaj", "Am", "G7")
        - octave: Octave number for the root note (default 4)
        - note_duration: Duration of each note in beats (default 0.5)
        - direction: Direction to order the arpeggio: "up", "down", or "random" (default "up")
        
        Returns:
        - List of (pitch, duration) tuples representing the arpeggio
        """
        chord = Chord(chord_symbol, octave=octave)
        pitches = chord.get_chord_pitches()
        return self.order_arpeggio_notes(direction, pitches, note_duration)
    
    def order_arpeggio_notes(self, direction, pitch, note_duration):
        """
        Order the arpeggio notes in a specific direction.
        
        Parameters:
        - direction: "up", "down", or "random"
        - pitch: List of MIDI pitches to order
        - note_duration: Duration of each note in beats
        
        Returns:
        - List of (pitch, duration) tuples representing the ordered arpeggio
        """
        if direction == "up":
            ordered_pitches = sorted(pitch)
        elif direction == "down":
            ordered_pitches = sorted(pitch, reverse=True)
        elif direction == "random":
            ordered_pitches = pitch[:]
            random.shuffle(ordered_pitches)
        else:
            raise ValueError("Invalid direction. Choose 'up', 'down', or 'random'.")
        
        return [(p, note_duration) for p in ordered_pitches]
