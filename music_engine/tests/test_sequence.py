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
    # "not a note" will be treated as a pitch name and fail during Note creation
    with pytest.raises(ValueError):
        seq.add_note("not a note")  # Invalid note name


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
    assert "Sequence" in r
    assert "num_notes=1" in r


def test_repr_with_name():
    seq = Sequence(name="verse")
    seq.add_note(Note(60, 1.0))
    r = repr(seq)
    assert "Sequence 'verse'" in r
    assert "num_notes=1" in r


def test_add_note_with_pitch_duration():
    seq = Sequence()
    note = seq.add_note('C4', 1.0)
    assert len(seq) == 1
    assert note.midi_pitch == 60
    assert note.duration == 1.0
    assert note.velocity == 80  # default


def test_add_note_with_velocity():
    seq = Sequence()
    note = seq.add_note(64, 0.5, velocity=50)
    assert len(seq) == 1
    assert note.midi_pitch == 64
    assert note.duration == 0.5
    assert note.velocity == 50


def test_add_note_returns_note_object():
    seq = Sequence()
    returned_note = seq.add_note('G3', 1.0)
    assert isinstance(returned_note, Note)
    assert returned_note.midi_pitch == 55


def test_sequence_has_play_method():
    seq = Sequence()
    seq.add_note('C4', 1.0)
    # Just verify the method exists and is callable
    assert hasattr(seq, 'play')
    assert callable(getattr(seq, 'play'))
