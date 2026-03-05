"""
This module defines the Sequence class, which represents a sequence of musical notes.

A Sequence is essentially a list of Note objects, along with some metadata such as tempo and time signature.
"""

from typing import List
from music_engine.core.note import Note

class Sequence:
    def __init__(self, name: str = None):
        self.name = name
        self.notes: List[Note] = []

    def add_note(self, pitch=None, duration: float = None, velocity: int = 80) -> Note:
        """
        Add a note to the sequence.
        
        Parameters:
        - pitch: MIDI number, frequency in Hz, or note name (e.g., 'C4')
        - duration: Duration in beats
        - velocity: Velocity (0-100, default 80)
        
        If called with a Note object, adds that note directly.
        If called with pitch and duration, creates and adds a new Note.
        
        Returns:
        - The Note object that was added
        """
        #Supports both passing Note object and passing pitch, duration, velocity
        if isinstance(pitch, Note):
            note = pitch
        else:
            #Creates Note from pitch, duration, velocity
            if pitch is None or duration is None:
                raise ValueError("pitch and duration are required when not passing a Note object")
            note = Note(pitch, duration, velocity)
        
        if not isinstance(note, Note):
            raise TypeError("Only Note objects can be added to the sequence.")
        self.notes.append(note)
        return note

    def wait(self, duration: float) -> Note:
        """
        Add silence/rest to the sequence.
        
        Parameters:
        - duration: Duration of the rest in beats
        
        Returns:
        - The silent Note object that was added
        """
        if duration <= 0:
            raise ValueError("Wait duration must be a positive number.")
        
        # Create a silent note with velocity 0 (will not produce sound)
        silent_note = Note(0, duration, velocity=0)
        self.notes.append(silent_note)
        return silent_note

    def generate_random_walk(self, start_pitch, num_notes, max_step=2, duration=0.5, velocity=80, scale_type=None):
        """
        Generate notes using a random walk algorithm and add them to the sequence.
        
        Parameters:
        - start_pitch: Starting pitch (MIDI number, frequency, or note name like 'C3')
        - num_notes: Number of notes to generate
        - max_step: Maximum semitone step (±max_step). Default: 2
        - duration: Duration of each note in beats. Default: 0.5
        - velocity: Velocity of each note (0-127). Default: 80
        - scale_type: If set to 'major' or 'minor', uses scale-constrained walk. If None, uses chromatic walk.
        
        Returns:
        - List of Note objects that were added
        """
        from music_engine.algorithms.random_walk import RandomWalk
        from music_engine.core.note import Note as NoteClass
        
        #Convert start_pitch to MIDI if needed
        start_note = NoteClass(start_pitch, 0.1)  #Temporary note to get MIDI pitch
        start_midi = start_note.midi_pitch
        
        #Generate notes using the appropriate random walk method
        if scale_type in ['major', 'minor']:
            #Use scale-constrained random walk
            generator = RandomWalk(scale_type=scale_type)
            generated_pitches = generator.generate(start_midi, num_notes, duration)
        elif scale_type is None:
            #Use chromatic random walk
            generator = RandomWalk()
            generated_pitches = generator.generate_chromatic(start_midi, num_notes, max_step, duration)
        
        #Add the generated notes to the sequence
        added_notes = []
        for pitch, dur in generated_pitches:
            note = self.add_note(int(pitch), dur, velocity=velocity)
            added_notes.append(note)
        
        return added_notes

    def generate_rhythm_sequence(self, pitch, total_beats=4, velocity=80, allowed_durations=None):
        """
        Generate notes using a rhythm generator and add them to the sequence.
        
        Parameters:
        - pitch: The pitch for all generated notes (MIDI number, frequency, or note name like 'C4')
        - total_beats: Total duration of the rhythmic sequence in beats. Default: 4
        - velocity: Velocity for all notes (0-100, default 80)
        - allowed_durations: List of allowed note durations. If None, uses default [0.25, 0.5, 1]
        
        Returns:
        - List of Note objects that were added
        """
        from music_engine.algorithms.rhythm import RhythmGenerator
        
        rhythm_gen = RhythmGenerator(allowed_durations=allowed_durations)
        durations = rhythm_gen.generate_bar(total_beats)
        
        added_notes = []
        for duration in durations:
            note = self.add_note(pitch, duration, velocity=velocity)
            added_notes.append(note)
        
        return added_notes

    def generate_melodic_rhythm(self, start_pitch, num_notes, total_beats=4, 
                               max_step=2, scale_type=None, velocity=80, allowed_durations=None):
        """
        Generate notes with both random pitches AND variable rhythms.
        
        Combines random walk (for pitch variation) with rhythm generation (for duration variation)
        to create more expressive melodic sequences.
        
        Parameters:
        - start_pitch: Starting pitch (MIDI number, frequency, or note name like 'C4')
        - num_notes: Number of notes to generate
        - total_beats: Total duration of the sequence in beats. Default: 4
        - max_step: Maximum semitone step for chromatic walk (±max_step). Default: 2
        - scale_type: If 'major' or 'minor', uses scale-constrained walk. If None, uses chromatic walk.
        - velocity: Velocity for all notes (0-100, default 80)
        - allowed_durations: List of allowed note durations. If None, uses default [0.25, 0.5, 1]
        
        Returns:
        - List of Note objects that were added
        """
        from music_engine.algorithms.random_walk import RandomWalk
        from music_engine.algorithms.rhythm import RhythmGenerator
        
        #Convert start_pitch to MIDI if needed
        start_note = Note(start_pitch, 0.1)
        start_midi = start_note.midi_pitch
        
        #Generate pitches using random walk
        if scale_type in ['major', 'minor']:
            walk = RandomWalk(scale_type=scale_type)
            pitches_with_temp_dur = walk.generate(start_midi, num_notes, 0.5)
            pitches = [int(p[0]) for p in pitches_with_temp_dur]
        else:
            walk = RandomWalk()
            pitches_with_temp_dur = walk.generate_chromatic(start_midi, num_notes, max_step, 0.5)
            pitches = [int(p[0]) for p in pitches_with_temp_dur]
        
        #Generate rhythms
        rhythm_gen = RhythmGenerator(allowed_durations=allowed_durations)
        durations = rhythm_gen.generate_bar(total_beats)
        
        #Combine pitches and rhythms
        #If there are more pitches than durations, cycle through the durations
        #If there are more durations than pitches, only use as many as needed
        added_notes = []
        for i, pitch in enumerate(pitches):
            duration = durations[i % len(durations)]
            note = self.add_note(pitch, duration, velocity=velocity)
            added_notes.append(note)
        
        return added_notes

    def generate_arpeggio(self, chord_symbol, octave=4, note_duration=0.5, direction="up", velocity=80):
        """
        Generate an arpeggio from a chord and add notes to the sequence.
        
        Parameters:
        - chord_symbol: String representing the chord (e.g., "Cmaj", "Am", "G7")
        - octave: Octave number for the root note (default 4)
        - note_duration: Duration of each note in beats (default 0.5)
        - direction: Direction to order the arpeggio: "up", "down", or "random" (default "up")
        - velocity: Velocity for all notes (0-100, default 80)
        
        Returns:
        - List of Note objects that were added
        """
        from music_engine.algorithms.arpeggio import Arpeggio
        
        arp_gen = Arpeggio()
        arpeggio_notes = arp_gen.generate_from_chord(chord_symbol, octave, note_duration, direction)
        
        added_notes = []
        for pitch, duration in arpeggio_notes:
            note = self.add_note(pitch, duration, velocity=velocity)
            added_notes.append(note)
        
        return added_notes

    def get_notes(self) -> List[Note]:
        return list(self.notes)
    
    def total_duration(self) -> float:
        return sum(note.duration for note in self.notes)
    
    def clear(self):
        self.notes.clear()

    def __len__(self):
        return len(self.notes)
    
    def __repr__(self):
        name_part = f"'{self.name}' " if self.name else ""
        return f"Sequence {name_part}(num_notes={len(self.notes)}, total_duration={self.total_duration():.2f} beats)"

    def play(self, tempo=120):
        """
        Play this sequence using the computer's audio output.
        
        Parameters:
        - tempo: Tempo in BPM (default 120)
        """
        from music_engine.output.playback import PlaybackEngine
        engine = PlaybackEngine(tempo=tempo)
        engine.play_sequence(self)
        engine.close()