from runner import *

@register_track
def track(guitar):
    intro = guitar.add_sequence("intro")
    intro.generate_random_walk(start_pitch='C4', num_notes=16, max_step=2, duration=0.5, scale_type='major')

    guitar.play(tempo=120)

@register_track
def track(piano):
    intro2 = piano.add_sequence("intro2")
    intro2.add_note('C4', 0.5)
    intro2.add_note('E4', 0.5)
    intro2.add_note('G4', 1.0)

    piano.export_midi("piano_output.mid", tempo=120)