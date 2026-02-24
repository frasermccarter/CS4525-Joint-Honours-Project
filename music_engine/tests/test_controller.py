"""
Tests for the Controller class in music_engine.engine.controller.
"""

from music_engine.engine.controller import Controller
from music_engine.core.track import Track
from music_engine.core.sequence import Sequence
from music_engine.core.note import Note


def test_controller_add_track():
    c = Controller()
    assert len(c.get_tracks()) == 0
    track = Track(name="test_track")
    c.add_track(track)
    assert len(c.get_tracks()) == 1
    assert c.get_tracks()[0] is track


def test_controller_add_track_invalid_type():
    c = Controller()
    try:
        c.add_track("not a track")
        assert False, "Should raise TypeError"
    except TypeError:
        pass


def test_show_prints_tracks(capsys):
    c = Controller()
    track = Track(name="piano")
    seq = Sequence(name="intro")
    seq.add_note(Note(60, 1.0))
    seq.add_note(Note(62, 2.0, velocity=10))
    track.add(seq)
    c.add_track(track)
    c.show()
    captured = capsys.readouterr()
    assert "<Track 'piano'" in captured.out
    assert "Sequence 'intro'" in captured.out
    assert "MIDI Pitch=60" in captured.out
    assert "MIDI Pitch=62" in captured.out


def test_controller_new_track():
    c = Controller()
    assert len(c.get_tracks()) == 0
    track = c.new_track("piano")
    assert len(c.get_tracks()) == 1
    assert track.name == "piano"
    assert c.get_tracks()[0] is track


def test_chainable_api():
    c = Controller()
    piano = c.new_track("piano")
    intro = piano.add_sequence("intro")
    note = intro.add_note('C4', 1.0)
    
    assert len(c.get_tracks()) == 1
    assert len(piano.get_sequences()) == 1
    assert len(intro.get_notes()) == 1
    assert note.midi_pitch == 60


def test_chainable_api_multiple():
    c = Controller()
    piano = c.new_track("piano")
    
    intro = piano.add_sequence("intro")
    intro.add_note('C4', 0.5)
    intro.add_note(64, 0.5, velocity=20)
    intro.add_note(440.0, 1.0)
    
    verse = piano.add_sequence("verse")
    verse.add_note('G3', 1)
    verse.add_note('G3', 1)
    verse.add_note('G3', 1)
    
    assert len(piano.get_sequences()) == 2
    assert len(intro.get_notes()) == 3
    assert len(verse.get_notes()) == 3


def test_sequence_sharing_across_tracks():
    c = Controller()
    
    #Create piano track with intro sequence
    piano = c.new_track("piano")
    intro = piano.add_sequence("intro")
    intro.add_note('C4', 0.5)
    intro.add_note(64, 0.5, velocity=20)
    
    #Create guitar track and add the same intro sequence by name
    guitar = c.new_track("guitar")
    guitar_intro = guitar.add_sequence("intro")
    
    #They should be the same object
    assert piano.get_sequences()[0] is guitar.get_sequences()[0]
    assert intro is guitar_intro
    assert len(guitar_intro.get_notes()) == 2  #Has the notes from piano's intro


def test_register_and_get_sequence():
    c = Controller()
    seq = Sequence(name="test_seq")
    
    c.register_sequence(seq)
    retrieved = c.get_sequence("test_seq")
    
    assert retrieved is seq
    assert c.get_sequence("nonexistent") is None
