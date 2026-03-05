"""
Tests for the rhythm algorithm
"""

from music_engine.algorithms.rhythm import RhythmGenerator
from music_engine.core.sequence import Sequence
from music_engine.core.note import Note

def test_rhythm_basic():
    allowed_durations = [0.25, 0.5, 1.0]
    total_beats = 4
    rhythm_gen = RhythmGenerator(allowed_durations=allowed_durations)
    durations = rhythm_gen.generate_bar(total_beats)
    
    assert sum(durations) == total_beats
    for dur in durations:
        assert dur in allowed_durations

def test_rhythm_default_durations():
    total_beats = 4
    rhythm_gen = RhythmGenerator()  # Use default durations
    durations = rhythm_gen.generate_bar(total_beats)
    
    assert sum(durations) == total_beats
    for dur in durations:
        assert dur in [0.25, 0.5, 1.0]

def test_rhythm_invalid_total_beats():
    rhythm_gen = RhythmGenerator()
    try:
        rhythm_gen.generate_bar(total_beats=-1)
        assert False, "Should raise ValueError for negative total_beats"
    except ValueError:
        pass

def test_rhythm_zero_total_beats():
    rhythm_gen = RhythmGenerator()
    durations = rhythm_gen.generate_bar(total_beats=0)
    
    assert durations == []  # Should return an empty list for zero total beats

def test_rhythm_non_divisible_total_beats():
    allowed_durations = [0.3, 0.7]
    total_beats = 1
    rhythm_gen = RhythmGenerator(allowed_durations=allowed_durations)
    durations = rhythm_gen.generate_bar(total_beats)
    
    assert sum(durations) == total_beats
    for dur in durations:
        assert dur in allowed_durations

def test_rhythm_large_total_beats():
    allowed_durations = [0.5, 1.0]
    total_beats = 16
    rhythm_gen = RhythmGenerator(allowed_durations=allowed_durations)
    durations = rhythm_gen.generate_bar(total_beats)
    
    assert sum(durations) == total_beats
    for dur in durations:
        assert dur in allowed_durations

def test_rhythm_impossible_total_beats():
    allowed_durations = [0.3, 0.7]
    total_beats = 0.5
    rhythm_gen = RhythmGenerator(allowed_durations=allowed_durations)
    try:
        rhythm_gen.generate_bar(total_beats)
        assert False, "Should raise ValueError when total_beats cannot be filled with allowed durations"
    except ValueError:
        pass

def test_rhythm_empty_allowed_durations():
    try:
        RhythmGenerator(allowed_durations=[])
        assert False, "Should raise ValueError for empty allowed_durations list"
    except ValueError:
        pass

def test_rhythm_negative_allowed_durations():
    try:
        RhythmGenerator(allowed_durations=[0.5, -1.0])
        assert False, "Should raise ValueError for negative allowed duration"
    except ValueError:
        pass

def test_rhythm_zero_allowed_durations():
    try:
        RhythmGenerator(allowed_durations=[0.5, 0.0])
        assert False, "Should raise ValueError for zero allowed duration"
    except ValueError:
        pass