"""
Example of how to export created tracks to MIDI files.
"""

from runner import *

@register_track
def track(piano):
    intro = piano.add_sequence("intro")
    intro.add_note(pitch='C4', duration=1.0, velocity=90)
    intro.add_note(pitch='Eb4', duration=1.0)
    intro.add_note(pitch='G4', duration=1.0)

    verse = piano.add_sequence("verse")
    verse.add_note(pitch=440.0, duration=0.5)
    verse.add_note(pitch=72, duration=0.5)
    verse.add_note(pitch='E5', duration=2.0)

    #Export the track to a MIDI file called "piano_track.mid" with a tempo of 120 BPM
    piano.export_midi("piano_track.mid", tempo=120)


@register_track
def track(guitar):
    intro2 = guitar.add_sequence("intro2")
    intro2.add_note(pitch='E4', duration=1.0, velocity=80)
    intro2.add_note(pitch='G4', duration=1.0)
    intro2.add_note(pitch='B4', duration=1.0)

    #Export the guitar track to a MIDI file called "guitar_track.mid" with a tempo of 120 BPM
    guitar.export_midi("guitar_track.mid", tempo=120)


controller.export_midi("full_song.mid", tempo=120)  #Calling export on the controller exports all tracks (to a single MIDI file called "full_song.mid" with a tempo of 120 BPM)

