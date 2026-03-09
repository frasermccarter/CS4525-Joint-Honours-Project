"""
This file contains tests for the export functionality of the music engine.
"""

import unittest
import os
from music_engine.core.note import Note
from music_engine.core.sequence import Sequence
from music_engine.core.track import Track
from music_engine.engine.controller import Controller
from music_engine.output.midi_export import MIDIExporter

class TestMIDIExport(unittest.TestCase):
    """Test MIDI export functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.controller = Controller()
    
    def test_export_single_track_to_midi(self):
        """Test exporting a single track to MIDI."""
        #Create a simple track with one sequence
        track = self.controller.new_track("Test Track")
        seq = Sequence("Test Sequence")
        seq.add_note(60, 1.0)  # C4, quarter note
        seq.add_note(62, 1.0)  # D4, quarter note
        seq.add_note(64, 1.0)  # E4, quarter note
        track.add_sequence(seq)
        
        #Export to MIDI
        exporter = MIDIExporter()
        midi_data = exporter.export_tracks_to_midi(self.controller.get_tracks())
        
        #Check that MIDI data is not empty
        self.assertTrue(midi_data)
    
    def test_export_multiple_tracks_to_midi(self):
        """Test exporting multiple tracks to MIDI."""
        #Create first track
        track1 = self.controller.new_track("Track 1")
        seq1 = Sequence("Sequence 1")
        seq1.add_note(60, 1.0)  # C4
        seq1.add_note(62, 1.0)  # D4
        track1.add_sequence(seq1)
        
        #Create second track
        track2 = self.controller.new_track("Track 2")
        seq2 = Sequence("Sequence 2")
        seq2.add_note(48, 1.0)  # C3
        seq2.add_note(50, 1.0)  # D3
        track2.add_sequence(seq2)
        
        #Export to MIDI
        exporter = MIDIExporter()
        midi_data = exporter.export_tracks_to_midi(self.controller.get_tracks())
        
        #Check that MIDI data is not empty
        self.assertTrue(midi_data)

    def test_export_midi_file_creation(self):
        """Test that exporting creates a MIDI file."""
        #Create a simple track
        track = self.controller.new_track("File Test Track")
        seq = Sequence("File Test Sequence")
        seq.add_note(60, 1.0)  # C4
        track.add_sequence(seq)
        
        #Export to MIDI file
        exporter = MIDIExporter()
        filename = "test_output.mid"
        exporter.export(track, filename)
        
        #Check that the file was created
        self.assertTrue(os.path.exists(filename))
        
        #Clean up test file
        os.remove(filename)

    if __name__ == '__main__':
        unittest.main()

    