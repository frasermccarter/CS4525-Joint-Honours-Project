"""
Task One
- Find the Eb note and change it to an E, then run the code to play the result.
- Now change the octave of the G note from an G3 to a G4, then run the code to play the result.
- Change the duration of the C note from 1 to 0.5, then run the code to play the result.
- Create a new A4 note (with a duration and velocity of your choosing) that plays after the G note, then run the code to play the result.
"""

from runner import *

@register_track
def track1(track):
    sequence = track.add_sequence("sequence1")
    sequence.add_note(pitch='C4', duration=1, velocity=50)
    sequence.add_note(pitch='Eb4', duration=1, velocity=75)
    sequence.add_note(pitch='G3', duration=1, velocity=100)


    sequence.play(tempo=120)  # Play the sequence at 120 BPM