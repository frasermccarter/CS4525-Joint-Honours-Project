"""
Track class is made to hold multiple sequences. It provides methods to add, retrieve, and manage sequences within a track.
"""

from typing import List
from music_engine.core.sequence import Sequence

class Track:
    def __init__(self):
        self._sequences: List[Sequence] = []

    def add_sequence(self, sequence: Sequence):
        if not isinstance(sequence, Sequence):
            raise TypeError("Only Sequence objects can be added to a Track.")
        self._sequences.append(sequence)

    def get_sequences(self) -> List[Sequence]:
        return list(self._sequences)
    
    def __len__(self):
        return len(self._sequences)
    
    def clear(self):
        self._sequences.clear()

    def __repr__(self):
        return f"<Track: {len(self)} sequences>"
    

