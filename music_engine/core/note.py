"""
This module defines the Note class, which represents a musical note with its pitch, velocity, and duration.

Pitch can be defined in multiple ways:
- MIDI note number (0-127)
- Frequency in Hz (e.g., 440.0 for A4)
- Note name (e.g., "C4", "A#3")

Velocity is user-defined on a scale of 0-100 and internally scaled to the MIDI standard of 0-100.

Duration is defined in beats.
"""

import math

class Note:
    # Note map for converting note names to MIDI numbers
    NOTE_MAP = {
        "C": 0, "C#": 1, "Db": 1,
        "D": 2, "D#": 3, "Eb": 3,
        "E": 4,
        "F": 5, "F#": 6, "Gb": 6,
        "G": 7, "G#": 8, "Ab": 8,
        "A": 9, "A#": 10, "Bb": 10,
        "B": 11
    }


    def __init__(self, pitch, duration: float, velocity: int = 80):
        self.midi_pitch = self._parse_pitch(pitch)

        if duration <= 0:
            raise ValueError("Duration must be a positive number.")
        self.duration = duration

        if not (0 <= velocity <= 100):
            raise ValueError("Velocity must be between 0 and 100.")
        self.velocity = velocity

        #Scale the velocity to MIDI standard (0-127)
        self.midi_velocity = int((velocity / 100) * 127)


    def _parse_pitch(self, pitch):
        if isinstance(pitch, int): #When pitch is given as MIDI note number (Assumed asume MIDI note number)
            #Check validity
            if not (0 <= pitch <= 127):
                raise ValueError("MIDI pitch must be between 0 and 127.")
            return pitch
        
        elif isinstance(pitch, float): #When pitch is given as frequency in Hz
            return self._hz_to_midi(pitch)
        
        elif isinstance(pitch, str): #When pitch is given as note name
            return self._note_name_to_midi(pitch)
        
        else:
            raise TypeError("Pitch must be a MIDI number (0-127), Hz (e.g., 440.0), or the note name (e.g., 'C4').")
        
    #--------------------------------------    
    #Convert given type to MIDI note number
    #--------------------------------------

    def _hz_to_midi(self, hz):
        if hz <= 0:
            raise ValueError("Frequency must be a positive number.")
        
        midi_number = 69 + 12 * math.log2(hz / 440.0)
        midi_number = int(round(midi_number))

        if not (0 <= midi_number <= 127):
            raise ValueError("Frequency is out of MIDI range (0-127).")
        
        return midi_number
    
    
    def _note_name_to_midi(self, note_name):
        note_name = note_name.strip().upper()

        #Split the note name into pitch and octave
        if len(note_name) < 2:
            raise ValueError("Invalid note name format. Expected a format like 'C4' or 'A#3'.")
        
        #Handle sharp and flat notes
        if note_name[1] in ['#', 'B']:
            pitch = note_name[:2]
            octave = note_name[2:]
        else:
            pitch = note_name[0]
            octave = note_name[1:]

        if pitch not in self.NOTE_MAP:
            raise ValueError(f"Invalid pitch '{pitch}' in note name. Expected a note from C, C#, D, D#, E, F, F#, G, G#, A, A#, B.")
        
        semitone = self.NOTE_MAP[pitch]
        midi_number = (int(octave) + 1) * 12 + semitone

        if not (0 <= midi_number <= 127):
            raise ValueError("Frequency is out of MIDI range (0-127).")
        
        return midi_number
    
    #--------------
    #Representation
    #--------------

    def __repr__(self):
        return (
            f"Note(midi={self.midi_pitch}), "
            f"duration={self.duration}, "
            f"velocity={self.velocity})"
        )