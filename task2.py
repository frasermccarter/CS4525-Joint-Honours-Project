"""
Task Two
- Locate the arpeggio function and change the chord from a C major (Cmaj) to a C minor (Cmin), then run the code to play the result.
- Change the arpeggio from playing an ascending sequence (up) to a descending sequence (down), then run the code to play the result.
- Fill in the parameters for the random walk function, then run the code to play the result.
"""

from runner import *

@register_track
def track1(track):
    arpeggio = track.add_sequence("arpeggio")
    arpeggio.generate_arpeggio(chord_symbol='Cmaj', octave='4', note_duration=0.5, direction='up')


    arpeggio.play(tempo=120)

"""
Uncomment the line below and fill in the blanks to complete the random walk example. 
You can experiment with different parameters to create different musical results.

You must fill in:
- start_pitch: The starting pitch of the random walk (e.g. 'C4', 60 (midi), 440.0 (hz) etc.).
- num_notes: The total number of notes to generate in the random walk (e.g. 4, 5, 16 etc.).
- max_step: The maximum step size (in semitones) for the random walk.  A max_step of 2 means that each note can be at most 2 semitones apart from each other.
- duration: The duration of each note in beats (e.g. 0.5 for quaver, 1 for crochet, etc.)
- scale_type: The scale to constrain the random walk to (e.g. "major", "minor", "chromatic").  If left unspecified (scale_type=None), the random walk will be generated without any scale constraints, meaning it can include any pitch.
"""
@register_track
def track3(track):
    randomWalk = track.add_sequence("randomWalk")
    # randomWalk.generate_random_walk(start_pitch='', num_notes=, max_step=, duration=, scale_type="")
    
    
    randomWalk.play(tempo=120)