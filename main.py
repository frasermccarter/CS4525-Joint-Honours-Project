"""
This file is currently used for composing music, this will be abstracted slighlty when sandboxed.
Users format their scripts by defining track functions decorated with @register_track.
"""

from music_engine.engine import Controller

#Global controller instance
controller = Controller()

from music_engine.core.chord import Chord

c = Chord("C")
print(c.get_chord_pitches()) #Expect something like [60, 64, 67]

a = Chord("Amaj7")
print(a.get_chord_pitches())



#Track registration decorator
def register_track(func):
    """Decorator to register a track setup function"""
    controller._track_functions.append(func)
    return func


#User efined tracks
@register_track
def track(piano):
    intro = piano.add_sequence("intro")
    for pitch in a.get_chord_pitches():
        intro.add_note(pitch, 0.5)

    # intro.add_note('C4', 0.5)
    # intro.add_note(64, 0.5, velocity=20)
    # intro.add_note(440.0, 1.0)
    
    # verse = piano.add_sequence("verse")
    # verse.add_note('G3', 1)
    # verse.add_note('G3', 1)
    # verse.add_note('G3', 1)


# @register_track
# def track(guitar):
#     intro2 = guitar.add_sequence("intro2")
#     intro2.add_note('C4', 0.5)
#     intro2.add_note('E4', 0.5)
#     intro2.add_note('G4', 1.0)

#     verse2 = guitar.add_sequence("verse2")
#     verse2.generate_random_walk(start_pitch='C4', num_notes=16, max_step=2, duration=0.5, scale_type='major')

#     verse2.wait(2)  #Add a rest before the next part

#     intro3 = guitar.add_sequence("intro3")
#     intro3.add_note('C4', 0.5)
#     intro3.add_note('Eb4', 0.5)
#     intro3.add_note('G4', 1.0)

#     verse3 = guitar.add_sequence("verse3")
#     verse3.generate_random_walk(start_pitch='C4', num_notes=16, max_step=2, duration=0.5, scale_type='minor')

# #test for melodic rhythm generation
# @register_track
# def track(bass):
#     bass_seq = bass.add_sequence("bassline")
#     bass_seq.generate_melodic_rhythm(start_pitch=60, num_notes=16, allowed_durations=[0.25, 0.5, 1.0, 1.5, 2, 3], total_beats=8.0, scale_type='major', velocity=90)

# #test for just rhythm generation
# @register_track
# def track(drum):
#     drum_seq = drum.add_sequence("drum_pattern")
#     drum_seq.generate_rhythm_sequence(pitch=36, allowed_durations=[0.25, 0.5, 1.0, 1.5, 2, 3], total_beats=8.0, velocity=100)


def main():
    #Create tracks for each registered track function
    track_functions = controller._track_functions
    tracks_by_name = {}
    
    for i, track_func in enumerate(track_functions):
        #Get the track name from the function parameter name
        import inspect
        params = inspect.signature(track_func).parameters
        track_name = list(params.keys())[0] if params else f"track_{i}"
        
        #Create the track and call the function
        track_obj = controller.new_track(track_name)
        track_func(track_obj)
        tracks_by_name[track_name] = track_obj

    #Display structure (debug)
    controller.show()

    #playback test
    print("\n--- Playing piano track ---")
    piano = tracks_by_name['piano']
    piano.play(tempo=120)
    #controller.export_midi("test_output.mid", tempo=120)


if __name__ == "__main__":
    main()