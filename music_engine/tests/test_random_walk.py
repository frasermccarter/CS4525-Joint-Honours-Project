"""
Tests for the random walk algorithm
"""

from music_engine.algorithms.random_walk import RandomWalk
from music_engine.core.sequence import Sequence
from music_engine.core.note import Note

def test_random_walk_basic():
    seq = Sequence()
    seq.generate_random_walk(start_pitch=60, num_notes=5, max_step=2, duration=0.5, velocity=80, scale_type='major')
    
    assert len(seq.notes) == 5
    for note in seq.notes:
        assert isinstance(note, Note)
        assert 48 <= note.midi_pitch <= 72  # Check that pitches are within a reasonable range
        assert note.duration == 0.5
        assert note.velocity == 80

def test_random_walk_chromatic():
    seq = Sequence()
    seq.generate_random_walk(start_pitch=60, num_notes=5, max_step=2, duration=0.5, velocity=80, scale_type=None)
    
    assert len(seq.notes) == 5
    for note in seq.notes:
        assert isinstance(note, Note)
        assert 48 <= note.midi_pitch <= 72  # Check that pitches are within a reasonable range
        assert note.duration == 0.5
        assert note.velocity == 80

def test_random_walk_invalid_scale():
    seq = Sequence()
    try:
        seq.generate_random_walk(start_pitch=60, num_notes=5, max_step=2, duration=0.5, velocity=80, scale_type='invalid_scale')
        assert False, "Should raise ValueError for invalid scale type"
    except ValueError:
        pass

def test_random_walk_negative_steps():
    seq = Sequence()
    try:
        seq.generate_random_walk(start_pitch=60, num_notes=-5, max_step=2, duration=0.5, velocity=80, scale_type='major')
        assert False, "Should raise ValueError for negative number of notes"
    except ValueError:
        pass

def test_random_walk_zero_steps():
    seq = Sequence()
    seq.generate_random_walk(start_pitch=60, num_notes=0, max_step=2, duration=0.5, velocity=80, scale_type='major')
    
    assert len(seq.notes) == 0  # No notes should be generated for zero steps

def test_random_walk_large_max_step():
    seq = Sequence()
    seq.generate_random_walk(start_pitch=60, num_notes=5, max_step=12, duration=0.5, velocity=80, scale_type=None)
    
    assert len(seq.notes) == 5
    for note in seq.notes:
        assert isinstance(note, Note)
        assert 0 <= note.midi_pitch <= 127  # Check pitches are valid MIDI range
        assert note.duration == 0.5
        assert note.velocity == 80

def test_random_walk_invalid_start_pitch():
    seq = Sequence()
    try:
        seq.generate_random_walk(start_pitch='invalid_pitch', num_notes=5, max_step=2, duration=0.5, velocity=80, scale_type='major')
        assert False, "Should raise ValueError for invalid start pitch"
    except ValueError:
        pass