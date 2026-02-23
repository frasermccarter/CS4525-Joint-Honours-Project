"""
Tests for the Controller class in music_engine.engine.controller.
"""

from music_engine.engine.controller import Controller


def test_controller_add_notes():
    c = Controller()
    assert len(c.get_current_sequence()) == 0
    c.note(60, 1.0)
    c.note("C4", 0.5, velocity=100)
    assert len(c.get_current_sequence()) == 2
    notes = c.get_current_sequence().get_notes()
    assert notes[0].midi_pitch == 60
    assert notes[1].midi_pitch == 60


def test_clear_sequence():
    c = Controller()
    c.note(60, 1.0)
    c.clear_sequence()
    assert len(c.get_current_sequence()) == 0


def test_show_prints_sequence(capsys):
    c = Controller()
    c.note(60, 1.0)
    c.note(62, 2.0, velocity=10)
    c.show()
    captured = capsys.readouterr()
    assert "Sequence(num_notes=2" in captured.out
    assert "MIDI Pitch=60" in captured.out
    assert "MIDI Pitch=62" in captured.out
