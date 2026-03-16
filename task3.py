"""
Task Three
- Run the code and listen to its musical output.
- Export the musical output of the Python script as a MIDI file using: export_midi("task3_output", tempo=120)
- Once exported, upload the MIDI file to the online MIDI editor / player linked below:
https://signalmidi.app/edit

Please listen and compare the results to what you expect based on the code input and whether the MIDI output is an accurate representation of the code."""

from runner import *

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


# Play all tracks polyphonically
play_polyphonic(tempo=120)

# Export the MIDI file (your code below)


