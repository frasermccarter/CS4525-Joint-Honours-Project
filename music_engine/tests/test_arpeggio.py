"""
Tets for the Arpeggio algorithm.
"""

from music_engine.algorithms.arpeggio import Arpeggio

def test_arpeggio_generate_from_chord():
    arp = Arpeggio()
    arpeggio_notes = arp.generate_from_chord("Cmaj", octave=4, note_duration=0.5, direction="up")
    
    expected_pitches = [60, 64, 67]  # C4, E4, G4
    expected_durations = [0.5, 0.5, 0.5]
    
    assert len(arpeggio_notes) == len(expected_pitches)
    for (pitch, duration), expected_pitch in zip(arpeggio_notes, expected_pitches):
        assert pitch == expected_pitch
        assert duration == 0.5

def test_arpeggio_ordering():
    arp = Arpeggio()
    
    # Test ascending order (tested through public API)
    ordered_up = arp.generate_from_chord("Cmaj", octave=4, note_duration=0.5, direction="up")
    pitches_up = [p for p, d in ordered_up]
    assert pitches_up == sorted(pitches_up), "Ascending order should be sorted"
    
    # Test descending order (tested through public API)
    ordered_down = arp.generate_from_chord("Cmaj", octave=4, note_duration=0.5, direction="down")
    pitches_down = [p for p, d in ordered_down]
    assert pitches_down == sorted(pitches_down, reverse=True), "Descending order should be reverse sorted"
    
    # Test random order (just check that all pitches are present)
    ordered_random = arp.generate_from_chord("Cmaj", octave=4, note_duration=0.5, direction="random")
    random_pitches = [p for p, d in ordered_random]
    assert sorted(random_pitches) == sorted(pitches_up), "Random order should contain same pitches"

def test_arpeggio_invalid_direction():
    arp = Arpeggio()
    try:
        arp.generate_from_chord("Cmaj", octave=4, note_duration=0.5, direction="invalid_direction")
        assert False, "Expected ValueError for invalid direction"
    except ValueError as e:
        assert str(e) == "Invalid direction. Choose 'up', 'down', or 'random'."

def test_arpeggio_invalid_chord():
    arp = Arpeggio()
    try:
        arp.generate_from_chord("InvalidChord", octave=4, note_duration=0.5, direction="up")
        assert False, "Expected ValueError for invalid chord"
    except ValueError as e:
        assert "Unknown chord symbol" in str(e)

def test_arpeggio_different_chords():
    arp = Arpeggio()
    
    # Test Cmaj
    cmaj_notes = arp.generate_from_chord("Cmaj", octave=4, note_duration=0.5, direction="up")
    assert [p for p, d in cmaj_notes] == [60, 64, 67]
    
    # Test Am
    am_notes = arp.generate_from_chord("Am", octave=4, note_duration=0.5, direction="up")
    assert [p for p, d in am_notes] == [69, 72, 76]  # A4, C5, E5
    
    # Test G7
    g7_notes = arp.generate_from_chord("G7", octave=4, note_duration=0.5, direction="up")
    assert [p for p, d in g7_notes] == [67, 71, 74, 77]  # G4, B4, D5, F5

def test_arpeggio_different_durations():
    arp = Arpeggio()
    
    # Test with different note durations
    cmaj_half_notes = arp.generate_from_chord("Cmaj", octave=4, note_duration=1.0, direction="up")
    assert all(d == 1.0 for p, d in cmaj_half_notes)
    
    cmaj_quarter_notes = arp.generate_from_chord("Cmaj", octave=4, note_duration=0.25, direction="up")
    assert all(d == 0.25 for p, d in cmaj_quarter_notes)

def test_arpeggio_different_octaves():
    arp = Arpeggio()
    
    # Test with different octaves
    cmaj_octave_3 = arp.generate_from_chord("Cmaj", octave=3, note_duration=0.5, direction="up")
    assert [p for p, d in cmaj_octave_3] == [48, 52, 55]  # C3, E3, G3
    
    cmaj_octave_5 = arp.generate_from_chord("Cmaj", octave=5, note_duration=0.5, direction="up")
    assert [p for p, d in cmaj_octave_5] == [72, 76, 79]  # C5, E5, G5

def test_arpeggio_different_directions():
    arp = Arpeggio()
    
    # Test ascending order
    cmaj_up = arp.generate_from_chord("Cmaj", octave=4, note_duration=0.5, direction="up")
    assert [p for p, d in cmaj_up] == [60, 64, 67]
    
    # Test descending order
    cmaj_down = arp.generate_from_chord("Cmaj", octave=4, note_duration=0.5, direction="down")
    assert [p for p, d in cmaj_down] == [67, 64, 60]
    
    # Test random order (just check that all pitches are present)
    cmaj_random = arp.generate_from_chord("Cmaj", octave=4, note_duration=0.5, direction="random")
    random_pitches = [p for p, d in cmaj_random]
    assert sorted(random_pitches) == [60, 64, 67]

def test_arpeggio_empty_chord():
    arp = Arpeggio()
    try:
        arp.generate_from_chord("", octave=4, note_duration=0.5, direction="up")
        assert False, "Expected ValueError for empty chord symbol"
    except ValueError as e:
        assert "Unknown chord symbol" in str(e)