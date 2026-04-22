"""
Example file showing how to use the THREE in-built algorithms to generate and assist music creation.  
These algorithms are designed to be flexible and can be used in a variety of ways to create different styles of music.

The algorithms are accessed through the Sequence class, and can be used to generate sequences of notes based on different parameters.

The three algorithms currently implemented are:
1.  Random Walk: 
        Generates a sequence of notes by taking random steps from a starting pitch.  
        The step size can be controlled to create more or less variation in the melody.

2. Rhythm Pattern:
        Generates a rhythmic pattern based on the inputed, allowed note durations.
        The pattern is defined as a list of durations (in beats) that repeat throughout the sequence

3. Scale Arpeggio:
        Generates an arpeggio based on a given scale (major, minor, or chromatic if left unspecified) and root note.
        Appegios can also be generated from chords, where the arpeggio notes are derived from the chord tones.
        The arpeggio can be generated in different orders (e.g. ascending, descending, random).

These algorithms can be used in combination with the basic note adding functionality to create more complex and interesting musical ideas.
"""

from runner import *                                    #Runner provides the necessary imports and setup for the music engine.  It must be imported before any user code.

"""Random Walk Examples"""
@register_track                                         #This decorator registers the track function with the engine controller. 
def track(randomWalk):                                  #To create a track, simply define a function that takes a single argument (the track name) and decorate it with @register_track.
    majorWalk = randomWalk.add_sequence("majorWalk")    #Within the track function, you can create sequences by calling add_sequence on the track object.  Sequences are used to organise notes and can be thought of as sections of a song (e.g. intro, verse, chorus).
    majorWalk.generate_random_walk(start_pitch='C4', num_notes=16, max_step=2, duration=0.5, scale_type="major")  #This generates a random walk starting from C4, with a maximum step size of 2 semitones, and a total of 16 notes.  The notes will be generated within the C major scale.
    
    majorWalk.play(tempo=120)                           #Finally, to play the track, call the play method on the track object with the desired tempo (in BPM).  This will play all sequences in the track in order.  You can also export the track to a MIDI file using the export_midi method.

    minorWalk = randomWalk.add_sequence("minorWalk")
    minorWalk.generate_random_walk(start_pitch=440.0, num_notes=16, max_step=2, duration=0.5, scale_type="minor")

#     minorWalk.play(120)


"""Rhythm Generator Example"""
@register_track
def track(rhythm):
    rhythmEx = rhythm.add_sequence("rhythmEx")
    rhythmEx.generate_rhythm_sequence(pitch='C3', total_beats=4)    #This generates a rhythm pattern that fills a 4 beat bar with notes of pitch C3.  The durations of the notes are generated randomly but will always add up to 4 beats.
    
#     rhythm.play(tempo=120)


"""Arpeggio Examples"""
"""
Valid chord symbols include:
- Major triads: "C", "Cmaj"
- Minor triads: "Cm", "Cmin"
- Dominant sevenths: "C7"
- Diminished sevenths: "Cdim7", "Cdim"
- Augmented triads: "Caug", "C+"
- Major sevenths: "Cmaj7", "CM7"
- Add six: "Cadd6"
- Add nine: "Cadd9", "Cadd2"

Examples: "C", "Am", "G7", "Cmaj7", "Dm", "D7", "Edim7", "Caug"

Octave: The octave in which to place the chord (default 4)
"""
@register_track
def track(arpeggio):
    arpUp = arpeggio.add_sequence("arpUp")
    arpUp.generate_arpeggio(chord_symbol="Cmaj7", octave=4, note_duration=0.5, direction="up")   #This generates an arpeggio based on the C major chord, starting from the root note (C4) and ascending through the chord tones (E4, G4).  Each note has a duration of 0.5 beats.

    arpDown = arpeggio.add_sequence("arpDown")
    arpDown.generate_arpeggio(chord_symbol="Am", octave=4, note_duration=0.5, direction="down") #This generates an arpeggio based on the A minor chord, starting from the root note (A4) and descending through the chord tones (E4, C4).  Each note has a duration of 0.5 beats.
    
#     arpUp.play(tempo=120)
#     arpDown.play(120)
