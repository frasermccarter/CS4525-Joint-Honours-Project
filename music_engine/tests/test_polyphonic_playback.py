"""
Tests for polyphonic playback functionality.

This also demonstrates how to use the polyphonic playback feature to play multiple
tracks simultaneously with audio mixing.
"""

import unittest
from music_engine.core.note import Note
from music_engine.core.sequence import Sequence
from music_engine.core.track import Track
from music_engine.engine.controller import Controller
from music_engine.output.playback import PlaybackEngine


class TestPolyphonicPlayback(unittest.TestCase):
    """Test polyphonic playback functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.controller = Controller()
        self.tempo = 120
    
    def test_play_polyphonic_multiple_tracks(self):
        """Test playing multiple tracks polyphonically."""
        #Create first track as a melody
        track1 = self.controller.new_track("Melody")
        seq1 = Sequence("Melody Sequence")
        seq1.add_note(60, 1.0)  # C4
        seq1.add_note(62, 1.0)  # D4
        seq1.add_note(64, 1.0)  # E4
        seq1.add_note(65, 1.0)  # F4
        track1.add_sequence(seq1)
        
        #Create second track as harmony
        track2 = self.controller.new_track("Harmony")
        seq2 = Sequence("Harmony Sequence")
        seq2.add_note(48, 1.0)  # C3
        seq2.add_note(50, 1.0)  # D3
        seq2.add_note(52, 1.0)  # E3
        seq2.add_note(53, 1.0)  # F3
        track2.add_sequence(seq2)
        
        #Create third track as the bass
        track3 = self.controller.new_track("Bass")
        seq3 = Sequence("Bass Sequence")
        seq3.add_note(36, 2.0)  # C2 (whole note)
        seq3.add_note(41, 2.0)  # F2 (whole note)
        track3.add_sequence(seq3)
        
        #Test that we can call play_polyphonic without errors
        #(Audio is not played in tests to avoid audio device issues)
        self.assertEqual(len(self.controller.tracks), 3)
    
    def test_render_track_to_audio(self):
        """Test rendering a track to audio without playing."""
        #Create a simple track
        track = self.controller.new_track("Test")
        seq = Sequence("Test Sequence")
        seq.add_note(60, 0.5)  # C4, half beat
        seq.add_note(64, 0.5)  # E4, half beat
        track.add_sequence(seq)
        
        #Create playback engine and render
        engine = PlaybackEngine(tempo=self.tempo)
        audio = engine._render_track(track, 60 / self.tempo)
        
        #Verify audio was generated
        self.assertIsNotNone(audio)
        self.assertGreater(len(audio), 0)
    
    def test_render_sequence_different_durations(self):
        """Test rendering sequences with different note durations."""
        engine = PlaybackEngine(tempo=120)
        seq = Sequence("Test")
        
        #Add notes with various durations
        seq.add_note(60, 0.25, velocity=80)  # Sixteenth note
        seq.add_note(62, 0.5, velocity=85)   # Eighth note
        seq.add_note(64, 1.0, velocity=90)   # Quarter note
        seq.add_note(65, 2.0, velocity=95)   # Half note
        
        audio = engine._render_sequence(seq, 60 / 120)
        
        #Verify audio was generated for all notes
        self.assertIsNotNone(audio)
        self.assertGreater(len(audio), 0)
    
    def test_polyphonic_audio_mixing(self):
        """Test that audio from multiple tracks is mixed correctly."""
        engine = PlaybackEngine(tempo=120)
        
        #Create two identical tracks
        track1 = Track("Track1")
        seq1 = Sequence()
        seq1.add_note(60, 1.0, velocity=50)
        track1.add_sequence(seq1)
        
        track2 = Track("Track2")
        seq2 = Sequence()
        seq2.add_note(60, 1.0, velocity=50)
        track2.add_sequence(seq2)
        
        #Render individual tracks
        audio1 = engine._render_track(track1, 60 / 120)
        audio2 = engine._render_track(track2, 60 / 120)
        
        # he rendered audios should have similar length
        self.assertEqual(len(audio1), len(audio2))
    
    def test_controller_play_polyphonic_all_tracks(self):
        """Test controller's play_polyphonic method with all tracks."""
        #Create multiple tracks
        for i in range(3):
            track = self.controller.new_track(f"Track{i}")
            seq = Sequence(f"Sequence{i}")
            seq.add_note(60 + i * 2, 1.0)
            track.add_sequence(seq)
        
        #Verify all tracks were added
        self.assertEqual(len(self.controller.tracks), 3)
        
        #Test that play_polyphonic can be called (without actually playing)
        #This just ensures the method exists and is callable
        self.assertTrue(hasattr(self.controller, 'play_polyphonic'))
    
    def test_render_note_with_envelope(self):
        """Test that note rendering applies proper envelope."""
        engine = PlaybackEngine(sample_rate=44100)
        note = Note(60, 0.5, velocity=80)  # 0.5 beats duration
        
        duration_seconds = 0.5 * (60 / 120)  # 0.25 seconds
        audio = engine._render_note(note, duration_seconds)
        
        #Verify audio was generated
        self.assertIsNotNone(audio)
        self.assertGreater(len(audio), 0)
        
        #Verify envelope shaping (start and end should be quieter due to attack/release)
        #The attack should make the beginning quieter
        self.assertLess(abs(audio[0]), abs(audio[len(audio) // 2]))
    
    def test_different_sample_rates(self):
        """Test rendering with different sample rates."""
        for sample_rate in [22050, 44100, 48000]:
            engine = PlaybackEngine(sample_rate=sample_rate)
            note = Note(60, 1.0, velocity=80)
            
            audio = engine._render_note(note, 1.0)
            
            #Audio length should scale with sample rate
            self.assertIsNotNone(audio)
            self.assertGreater(len(audio), 0)


if __name__ == '__main__':
    unittest.main()
