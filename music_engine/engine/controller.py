"""
This class is the main interface through which users interact with the engine.

It currently provides methods for adding notes to a sequence, getting the current sequence, and clearing the sequence.
"""

from music_engine.core.note import Note
from music_engine.core.sequence import Sequence
from music_engine.core.track import Track

class Controller:
    def __init__(self):
        self.track = Track()
        # current_sequence holds the active Sequence object
        self.current_sequence = Sequence()
        self.track.add_sequence(self.current_sequence)

    #-------------------
    #Note API
    #-------------------

    def note(self, pitch: int, duration: float, velocity: int = 80):
        """
        Add a note to the current sequence.

        Parameters:
        - pitch: Can be a MIDI note number (0-127), a frequency in Hz (e.g., 440), or a note name (e.g., 'C4').
        - duration: Duration of the note in beats (must be positive).
        - velocity: Intensity of the note (0-100, default is 80).
        """

        new_note = Note(pitch, duration, velocity)
        self.current_sequence.add_note(new_note)

    #-------------------
    #Sequence Management
    #-------------------

    def new_sequence(self):
        #Start a new sequence and add it to the track
        self.current_sequence = Sequence()
        self.track.add_sequence(self.current_sequence)

    def clear_sequence(self):
        #Clear the current sequence
        self.current_sequence.clear()

    def get_current_sequence(self) -> Sequence:
        return self.current_sequence

    #-------------------
    #Utility Methods    
    #-------------------

    def get_track(self) -> Track:
        return self.track

    def show(self):
        #Debug method to print the current sequence of notes
        print(self.track)
        for i, seq in enumerate(self.track.get_sequences()):
            print(f"Sequence {i}: {seq}")
            for note in seq.get_notes():
                print(f"  Note: MIDI Pitch={note.midi_pitch}, Duration={note.duration}, Velocity={note.velocity}")
    

    