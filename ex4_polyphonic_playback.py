"""
Example file for how to use polyphonic playback.

In this example, we create three tracks: melody, harmony, and bass.
Each track has its own sequence of notes, and we use the play_polyphonic function to play all tracks together at the same time.

This allows us to create a simple piece of music with multiple parts that play together.

Polyphonic playback is dependent on the function calls placement in the code.  
It will play all tracks that have been defined between where the play_polyphonic function is called and where it was previously called.  
This means that if you define a track after the play_polyphonic function, it will not be included in the polyphonic playback.
"""

from runner import *

@register_track
def track(melody):
    melody = melody.add_sequence("melody")
    melody.add_note('C4', 1)
    melody.add_note('D4', 1)
    melody.add_note('E4', 1)
    melody.add_note('F4', 1)

#Plays just melody track polyphonically (only one track, so it will sound the same as normal playback)
play_polyphonic(tempo=120)


@register_track
def track(harmony):
    harmony = harmony.add_sequence("harmony")
    harmony.add_note('F3', 1)
    harmony.add_note('G3', 1)
    harmony.add_note('A3', 1)
    harmony.add_note('Bb3', 1)


@register_track
def track(bass):
    bass = bass.add_sequence("bass")
    bass.add_note('C3', 2)
    bass.add_note('F3', 2)

#Play all tracks polyphonically since last call so both harmony and bass will play.
play_polyphonic(tempo=120)


@register_track
def track(melody):
    melody = melody.add_sequence("melody")
    melody.add_note('C4', 1)
    melody.add_note('D4', 1)
    melody.add_note('E4', 1)
    melody.add_note('F4', 1)


@register_track
def track(harmony):
    harmony = harmony.add_sequence("harmony")
    harmony.add_note('F3', 1)
    harmony.add_note('G3', 1)
    harmony.add_note('A3', 1)
    harmony.add_note('Bb3', 1)


@register_track
def track(bass):
    bass = bass.add_sequence("bass")
    bass.add_note('C3', 2)
    bass.add_note('F3', 2)

#Play all tracks polyphonically
play_polyphonic(tempo=120)

