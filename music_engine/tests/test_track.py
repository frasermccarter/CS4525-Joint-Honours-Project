"""
Test for the Track class in the music engine.
"""

import pytest
from music_engine.core.track import Track
from music_engine.core.sequence import Sequence
from music_engine.core.note import Note


def test_add_and_get_sequences():
    track = Track()
    seq1 = Sequence()
    seq2 = Sequence()
    track.add_sequence(seq1)
    track.add_sequence(seq2)
    sequences = track.get_sequences()
    assert len(sequences) == 2
    assert sequences[0] is seq1
    assert sequences[1] is seq2

def test_add_invalid_type():
    track = Track()
    with pytest.raises(TypeError):
        track.add_sequence(123)  # Invalid type

def test_add_sequence_with_string_name():
    track = Track()
    seq = track.add_sequence("verse")
    assert len(track) == 1
    assert seq.name == "verse"
    assert track.get_sequences()[0] is seq
    assert isinstance(seq, Sequence)

def test_len_and_clear():
    track = Track()
    seq1 = Sequence()
    seq2 = Sequence()
    track.add_sequence(seq1)
    track.add_sequence(seq2)
    assert len(track) == 2
    track.clear()
    assert len(track) == 0

def test_repr():
    track = Track()
    assert repr(track) == "<Track : 0 sequences>"
    track.add_sequence(Sequence())
    assert repr(track) == "<Track : 1 sequences>"


def test_repr_with_name():
    track = Track(name="piano")
    assert repr(track) == "<Track 'piano' : 0 sequences>"
    track.add_sequence(Sequence())
    assert repr(track) == "<Track 'piano' : 1 sequences>"


def test_add_sequence_method():
    track = Track()
    seq = Sequence()
    result = track.add_sequence(seq)
    assert len(track) == 1
    assert track.get_sequences()[0] is seq
    

def test_track_has_play_method():
    track = Track(name="test")
    seq = Sequence(name="seq1")
    seq.add_note(Note(60, 1.0))
    track.add_sequence(seq)
    # Just verify the method exists and is callable
    assert hasattr(track, 'play')
    assert callable(getattr(track, 'play'))