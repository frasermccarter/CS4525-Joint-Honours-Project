"""
Tests for the Sequence class in music_engine.core.sequence.
"""

import pytest
from music_engine.core.note import Note
from music_engine.core.sequence import Sequence


def test_add_and_len():
    seq = Sequence()
    assert len(seq) == 0
    seq.add_note(Note(60, 1.0))
    assert len(seq) == 1


def test_add_invalid_type():
    seq = Sequence()
    with pytest.raises(TypeError):
        seq.add_note("not a note")


def test_total_duration_and_clear():
    seq = Sequence()
    seq.add_note(Note(60, 1.0))
    seq.add_note(Note(62, 0.5))
    assert seq.total_duration() == 1.5
    seq.clear()
    assert len(seq) == 0
    assert seq.total_duration() == 0


def test_get_notes_returns_copy():
    seq = Sequence()
    n = Note(60, 1.0)
    seq.add_note(n)
    notes = seq.get_notes()
    assert notes == [n]
    # modifying returned list should not alter internal list
    notes.append(Note(62, 1.0))
    assert len(seq) == 1


def test_repr():
    seq = Sequence()
    seq.add_note(Note(60, 1.0))
    r = repr(seq)
    assert "Sequence(num_notes=1" in r
