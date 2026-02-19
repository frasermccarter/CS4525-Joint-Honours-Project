"""
Tests for the Note class in music_engine.core.note.
"""

import pytest
from music_engine.core.note import Note


def test_valid_midi_pitch():
    n = Note(60, 1.0, velocity=50)
    assert n.midi_pitch == 60
    assert n.duration == 1.0
    assert n.velocity == 50
    assert n.midi_velocity == int((50 / 100) * 127)


def test_valid_hz_pitch():
    n = Note(440.0, 0.5)
    #440 Hz should map to MIDI note 69 (A4)
    assert n.midi_pitch == 69


def test_valid_note_name():
    n = Note("C4", 2.0, velocity=100)
    #C4 should map to 60 in MIDI
    assert n.midi_pitch == 60
    assert n.midi_velocity == 127


def test_invalid_pitch_type():
    with pytest.raises(TypeError):
        Note([60], 1.0)


def test_invalid_midi_range():
    with pytest.raises(ValueError):
        Note(200, 1.0)


def test_invalid_hz_range():
    #frequency that maps outside 0-127
    with pytest.raises(ValueError):
        Note(100000.0, 1.0)


def test_invalid_note_name_format():
    with pytest.raises(ValueError):
        Note("H#", 1.0)


def test_negative_duration():
    with pytest.raises(ValueError):
        Note(60, -1)


def test_velocity_out_of_bounds():
    with pytest.raises(ValueError):
        Note(60, 1.0, velocity=200)


def test_repr():
    n = Note(60, 1.5, velocity=30)
    r = repr(n)
    assert "Note(midi=60" in r
    assert "duration=1.5" in r
    assert "velocity=30" in r
