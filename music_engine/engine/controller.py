"""
This class is the main interface through which users interact with the engine.

It currently provides methods for adding notes to a sequence, getting the current sequence, and clearing the sequence, adding and managing tracks.
"""

import random

from music_engine.core.note import Note
from music_engine.core.sequence import Sequence
from music_engine.core.track import Track

from music_engine.output.playback import PlaybackEngine
from music_engine.output.midi_export import MIDIExporter

from music_engine.algorithms.random_walk import RandomWalk
from music_engine.algorithms.rhythm import RhythmGenerator
from music_engine.algorithms.arpeggio import Arpeggio

class Controller:
    def __init__(self):
        self.tracks = []
        self._sequences = {}  #Registry of sequences by name for sharing across tracks
        self._track_functions = []  #Registry for track setup functions

    #-------------------
    #Track Management
    #-------------------

    def new_track(self, name: str = None) -> Track:
        """
        Create a new track and add it to the controller.
        
        Parameters:
        - name: Optional name for the track
        
        Returns:
        - The created Track object
        """
        track = Track(name=name, controller=self)
        self.tracks.append(track)
        return track

    def add_track(self, track: Track):
        """
        Add a track to the controller.
        
        Parameters:
        - track: A Track object containing sequences.
        """
        if not isinstance(track, Track):
            raise TypeError("Only Track objects can be added.")
        self.tracks.append(track)

    #-------------------
    #Utility Methods    
    #-------------------

    def get_tracks(self) -> list:
        return self.tracks

    def register_sequence(self, sequence: Sequence):
        """
        Register a sequence by name for sharing across tracks.
        
        Parameters:
        - sequence: The Sequence object to register
        """
        if sequence.name:
            self._sequences[sequence.name] = sequence

    def get_sequence(self, name: str) -> Sequence:
        """
        Get a registered sequence by name.
        
        Parameters:
        - name: The name of the sequence
        
        Returns:
        - The Sequence object if found, None otherwise
        """
        return self._sequences.get(name)

    def show(self):
        #Debug method to print all tracks and their sequences
        for track in self.tracks:
            print(track)
            for i, seq in enumerate(track.get_sequences()):
                print(f"  Sequence {i}: {seq}")
                for note in seq.get_notes():
                    print(f"    Note: MIDI Pitch={note.midi_pitch}, Duration={note.duration}, Velocity={note.velocity}")

    #-------------------
    #Algorithmic Composition
    #-------------------

    def generate_random_walk(self, root: int, steps: int, step_duration: float, scale_type="major"):
        generator = RandomWalk(scale_type=scale_type)
        
        root_note = Note(root, 1)
        root_midi = root_note.midi_pitch  # Ensure we have the MIDI pitch value

        generated = generator.generate(root_midi, steps, step_duration)

        for pitch, duration in generated:
            self.note(pitch, duration)

    def generate_rhythm_sequence(self, pitch=60, total_beats=4):
        rhythm_gen = RhythmGenerator()
        durations = rhythm_gen.generate_bar(total_beats)

        sequence = Sequence()

        for dur in durations:
            note = Note(pitch=pitch, duration=dur, velocity=80)
            sequence.add_note(note)

        return sequence
    
    def generate_arpeggio(self, chord_symbol, octave=4, note_duration=0.5, direction="up"):
        arp_gen = Arpeggio()
        arpeggio_notes = arp_gen.generate_from_chord(chord_symbol, octave, note_duration, direction)
        
        sequence = Sequence()
        for pitch, duration in arpeggio_notes:
            note = Note(pitch, duration, velocity=80)
            sequence.add_note(note)
        
        return sequence

    #-------------------
    #Playback
    #-------------------

    def play(self, tempo=120, track: Track = None):
        """
        Play one or all tracks.
        
        Parameters:
        - tempo: Tempo in BPM (default 120)
        - track: Specific track to play. If None, plays all tracks.
        """
        engine = PlaybackEngine(tempo=tempo)
        if track:
            engine.play_track(track)
        else:
            for t in self.tracks:
                engine.play_track(t)
        engine.close()

    def play_polyphonic(self, tempo=120, tracks=None):
        """
        Play one or more tracks simultaneously with polyphonic mixing.
        
        Parameters:
        - tempo: Tempo in BPM (default 120)
        - tracks: List of specific tracks to play, or None to play all tracks polyphonically.
        """
        engine = PlaybackEngine(tempo=tempo)
        if tracks:
            if isinstance(tracks, list):
                engine.play_polyphonic(tracks)
            else:
                engine.play_polyphonic(tracks)
        else:
            engine.play_polyphonic(self.tracks)
        engine.close()

    #-------------------
    #MIDI Export
    #-------------------

    def export_midi(self, filename, tempo=120, track: Track = None):
        """
        Export tracks to a MIDI file.
        
        Parameters:
        - filename: Output MIDI file path
        - tempo: Tempo in BPM (default 120)
        - track: Specific track to export. If None, exports all tracks as separate MIDI tracks in one file.
        """
        exporter = MIDIExporter(tempo=tempo)
        if track:
            # Export single track
            exporter.export(track, filename)
        else:
            # Export all tracks as separate MIDI tracks in one file
            exporter.export_multiple(self.tracks, filename)
    

    