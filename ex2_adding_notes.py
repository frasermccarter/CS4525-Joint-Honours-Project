"""
Example file showing how to add notes to sequences and how to add sequences to tracks. 
This is the most basic way to create music with the engine, and is a good starting point for users new to music programming.

tracks are created by using the @register_track decorator to define a function that takes a single argument (the track name).  
Within the track function, you can create sequences by calling add_sequence on the track object.  
Sequences are used to organise notes and can be thought of as sections of a song (e.g. intro, verse, chorus).  

To add a note to a sequence, call add_note with the desired parameters.  
Note can be specified as a string (e.g. 'C4'), MIDI number (e.g. 60), or frequency in Hz (e.g. 440.0).  
Duration is specified in beats, and velocity is an optional parameter that controls the volume of the note (default is 80).  

Finally, to play the track, call the play method on the track object with the desired tempo (in BPM).  
This will play all sequences in the track in order.  You can also export the track to a MIDI file using the export_midi method.
"""

from runner import *                                #Runner provides the necessary imports and setup for the music engine.  It must be imported before any user code.

@register_track                                     #This decorator registers the track function with the engine controller. 
def track(piano):                                   #To create a track, simply define a function that takes a single argument (the track name) and decorate it with @register_track.
    intro = piano.add_sequence("intro")             #Within the track function, you can create sequences by calling add_sequence on the track object.  Sequences are used to organise notes and can be thought of as sections of a song (e.g. intro, verse, chorus).
    
    #intro.add_note(pitch, duration, velocity=100)  #To add a note to a sequence, call add_note with the desired parameters.  Note can be specified as a string (e.g. 'C4'), MIDI number (e.g. 60), or frequency in Hz (e.g. 440.0).  Duration is specified in beats, and velocity is an optional parameter that controls the volume of the note (default is 80).
    intro.add_note(pitch='C4', duration=1.0, velocity=90)
    intro.add_note(pitch='Eb4', duration=1.0)
    intro.add_note(pitch='G4', duration=1.0)

    verse = piano.add_sequence("verse")             #A new secquence in the piano track is created called verse.
    verse.add_note(pitch=440.0, duration=0.5)       #You can also specify the pitch as a frequency in Hz.  In this case, 440.0 Hz corresponds to A4.
    verse.add_note(pitch=72, duration=0.5)
    verse.add_note(pitch='E5', duration=2.0)

    intro.play(tempo=120)                           #Playback can be called either on sequences or on the track itself.  Calling play on a sequence will play only that sequence, while calling play on the track will play all sequences in order.
    verse.play(tempo=120)

    # piano.play(tempo=120)                         #Finally, to play the track, call the play method on the track object with the desired tempo (in BPM).  This will play all sequences in the track in order.  You can also export the track to a MIDI file using the export_midi method.


@register_track
def track(guitar):
    intro = guitar.add_sequence("intro")            #A sequence names are not unique across tracks, so we can also create an intro sequence in the guitar track.  This allows us to have different sections of the song that are specific to each instrument.
    #guitar.play(tempo=120)                         #Uncomment this line to see that the guitar track will play the same intro sequence as the piano track.



