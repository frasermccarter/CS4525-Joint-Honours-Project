"""
This module defines the Sequence class, which represents a sequence of musical notes.

A Sequence is essentially a list of Note objects, along with some metadata such as tempo and time signature.
"""

from typing import List
from music_engine.core.note import Note

class Sequence:
    def __init__(self):
        self.notes: List[Note] = []

    def add_note(self, note: Note):
        if not isinstance(note, Note):
            raise TypeError("Only Note objects can be added to the sequence.")
        self.notes.append(note)

    def get_notes(self) -> List[Note]:
        return list(self.notes)
    
    def total_duration(self) -> float:
        return sum(note.duration for note in self.notes)
    
    def clear(self):
        self.notes.clear()

    def __len__(self):
        return len(self.notes)
    
    def __repr__(self):
        return f"Sequence(num_notes={len(self.notes)}, total_duration={self.total_duration():.2f} beats)"