"""
This module defines the Sequence class, which represents a sequence of musical notes.

A Sequence is essentially a list of Note objects, along with some metadata such as tempo and time signature.
"""

from typing import List
from music_engine.core.note import Note

class Sequence:
    def __init__(self, name: str = None):
        self.name = name
        self.notes: List[Note] = []

    def add_note(self, pitch=None, duration: float = None, velocity: int = 80) -> Note:
        """
        Add a note to the sequence.
        
        Parameters:
        - pitch: MIDI number, frequency in Hz, or note name (e.g., 'C4')
        - duration: Duration in beats
        - velocity: Velocity (0-100, default 80)
        
        If called with a Note object, adds that note directly.
        If called with pitch and duration, creates and adds a new Note.
        
        Returns:
        - The Note object that was added
        """
        #Supports both passing Note object and passing pitch, duration, velocity
        if isinstance(pitch, Note):
            note = pitch
        else:
            #Creates Note from pitch, duration, velocity
            if pitch is None or duration is None:
                raise ValueError("pitch and duration are required when not passing a Note object")
            note = Note(pitch, duration, velocity)
        
        if not isinstance(note, Note):
            raise TypeError("Only Note objects can be added to the sequence.")
        self.notes.append(note)
        return note

    def get_notes(self) -> List[Note]:
        return list(self.notes)
    
    def total_duration(self) -> float:
        return sum(note.duration for note in self.notes)
    
    def clear(self):
        self.notes.clear()

    def __len__(self):
        return len(self.notes)
    
    def __repr__(self):
        name_part = f"'{self.name}' " if self.name else ""
        return f"Sequence {name_part}(num_notes={len(self.notes)}, total_duration={self.total_duration():.2f} beats)"

    def play(self, tempo=120):
        """
        Play this sequence using the computer's audio output.
        
        Parameters:
        - tempo: Tempo in BPM (default 120)
        """
        from music_engine.output.playback import PlaybackEngine
        engine = PlaybackEngine(tempo=tempo)
        engine.play_sequence(self)
        engine.close()