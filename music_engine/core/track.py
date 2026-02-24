"""
Track class is made to hold multiple sequences. It provides methods to add, retrieve, and manage sequences within a track.
"""

from typing import List
from music_engine.core.sequence import Sequence

class Track:
    def __init__(self, name: str = None, controller=None):
        self.name = name
        self._sequences: List[Sequence] = []
        self.controller = controller

    def add(self, sequence: Sequence) -> Sequence:
        #Alias for add_sequence to make the API more user-friendly
        return self.add_sequence(sequence)

    def add_sequence(self, sequence) -> Sequence:
        """
        Add a sequence to this track.
        
        Parameters:
        - sequence: Can be a Sequence object or a string name
                   If a string, tries to find existing sequence in controller first,
                   otherwise creates a new one
        
        Returns:
        - The Sequence object that was added
        """
        if isinstance(sequence, str):
            #Try to get existing sequence from controller
            if self.controller:
                existing = self.controller.get_sequence(sequence)
                if existing:
                    sequence = existing
                else:
                    #Create new sequence and register it
                    sequence = Sequence(name=sequence)
                    self.controller.register_sequence(sequence)
            else:
                #No controller, create new sequence
                sequence = Sequence(name=sequence)
        elif not isinstance(sequence, Sequence):
            raise TypeError("Only Sequence objects can be added to a Track.")
        
        #Register sequence if it has a name and controller exists
        if self.controller and sequence.name:
            self.controller.register_sequence(sequence)
        
        self._sequences.append(sequence)
        return sequence

    def get_sequences(self) -> List[Sequence]:
        return list(self._sequences)
    
    def __len__(self):
        return len(self._sequences)
    
    def clear(self):
        self._sequences.clear()

    def __repr__(self):
        name_part = f"'{self.name}' " if self.name else ""
        return f"<Track {name_part}: {len(self)} sequences>"

    def play(self, tempo=120):
        """
        Play this track.
        
        Parameters:
        - tempo: Tempo in BPM (default 120)
        """
        from music_engine.output.playback import PlaybackEngine
        engine = PlaybackEngine(tempo=tempo)
        engine.play_track(self)
        engine.close()

