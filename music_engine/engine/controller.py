"""
This class is the main interface through which users interact with the engine.

It currently provides methods for adding notes to a sequence, getting the current sequence, and clearing the sequence, adding and managing tracks.
"""

from music_engine.core.note import Note
from music_engine.core.sequence import Sequence
from music_engine.core.track import Track

class Controller:
    def __init__(self):
        self.tracks = []
        self._sequences = {}  #Registry of sequences by name for sharing across tracks

    #-------------------
    #Track Management
    #-------------------

    def new_track(self, name: str = None) -> Track:
        """
        Create a new track and add it to the controller.
        
        Parameters:
        - name: Optional name for the track
        
        Returns:
        - The created Track object
        """
        track = Track(name=name, controller=self)
        self.tracks.append(track)
        return track

    def add_track(self, track: Track):
        """
        Add a track to the controller.
        
        Parameters:
        - track: A Track object containing sequences.
        """
        if not isinstance(track, Track):
            raise TypeError("Only Track objects can be added.")
        self.tracks.append(track)

    #-------------------
    #Utility Methods    
    #-------------------

    def get_tracks(self) -> list:
        return self.tracks

    def register_sequence(self, sequence: Sequence):
        """
        Register a sequence by name for sharing across tracks.
        
        Parameters:
        - sequence: The Sequence object to register
        """
        if sequence.name:
            self._sequences[sequence.name] = sequence

    def get_sequence(self, name: str) -> Sequence:
        """
        Get a registered sequence by name.
        
        Parameters:
        - name: The name of the sequence
        
        Returns:
        - The Sequence object if found, None otherwise
        """
        return self._sequences.get(name)

    def show(self):
        #Debug method to print all tracks and their sequences
        for track in self.tracks:
            print(track)
            for i, seq in enumerate(track.get_sequences()):
                print(f"  Sequence {i}: {seq}")
                for note in seq.get_notes():
                    print(f"    Note: MIDI Pitch={note.midi_pitch}, Duration={note.duration}, Velocity={note.velocity}")

    