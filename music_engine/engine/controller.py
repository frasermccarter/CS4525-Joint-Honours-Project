from core.note import Note
from core.sequence import Sequence

class Controller:
    def __init__(self):
        self.sequence = Sequence()

    #----------------
    #User-API Methods
    #----------------

    def note(self, pitch: int, duration: float, velocity: int = 80):
        """
        Add a note to the current sequence.

        Parameters:
        - pitch: Can be a MIDI note number (0-127), a frequency in Hz (e.g., 440), or a note name (e.g., 'C4').
        - duration: Duration of the note in beats (must be positive).
        - velocity: Intensity of the note (0-100, default is 80).
        """

        new_note = Note(pitch, duration, velocity)
        self.sequence.add_note(new_note)

    def get_sequence(self) -> Sequence:
        return self.sequence
    
    def clear(self):
        self.sequence.clear()

    def show(self):
        #Debug method to print the current sequence of notes
        print(self.sequence)
        for note in self.sequence.get_notes():
            print(note)
    

    