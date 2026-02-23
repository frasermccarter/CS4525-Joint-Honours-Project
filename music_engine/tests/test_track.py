"""
Test for the Track class in the music engine.
"""

import pytest
from music_engine.core.track import Track
from music_engine.core.sequence import Sequence


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
        track.add_sequence("not a sequence")

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
    assert repr(track) == "<Track: 0 sequences>"
    track.add_sequence(Sequence())
    assert repr(track) == "<Track: 1 sequences>"