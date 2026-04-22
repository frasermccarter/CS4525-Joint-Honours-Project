"""
Presentation Demo: Polyphonic Mary Had a Little Lamb

This demonstration showcases several key features of the music engine:
- Multiple tracks with polyphonic playback
- Various note durations and velocities
- Sequence organization (intro, verse, chorus)
- Dynamic control through velocity
- Use of chords and harmony

The arrangement features:
- Melody: Main theme in the treble
- Harmony: Chord accompaniment providing harmonic support
- Bass: Root note progression providing rhythmic foundation
"""

from runner import *


@register_track
def track(melody):
    """Main melody line - the classic 'Mary Had a Little Lamb' tune"""
    melody = melody.add_sequence("melody")
    
    # "Mary had a little lamb,"
    melody.add_note('E4', 1, velocity=100)  # Ma
    melody.add_note('D4', 1, velocity=100)  # ry
    melody.add_note('C4', 1, velocity=100)  # had
    melody.add_note('D4', 1, velocity=100)  # a
    melody.add_note('E4', 1, velocity=100)  # lit
    melody.add_note('E4', 1, velocity=100)  # tle
    melody.add_note('E4', 2, velocity=100)  # lamb
    
    # "Little lamb, little lamb,"
    melody.add_note('D4', 1, velocity=100)  # lit
    melody.add_note('D4', 1, velocity=100)  # tle
    melody.add_note('D4', 2, velocity=100)  # lamb
    melody.add_note('E4', 1, velocity=100)  # lit
    melody.add_note('E4', 1, velocity=100)  # tle
    melody.add_note('E4', 2, velocity=100)  # lamb
    
    # "Mary had a little lamb"
    melody.add_note('E4', 1, velocity=100)  # Ma
    melody.add_note('D4', 1, velocity=100)  # ry
    melody.add_note('C4', 1, velocity=100)  # had
    melody.add_note('D4', 1, velocity=100)  # a
    melody.add_note('E4', 1, velocity=100)  # lit
    melody.add_note('E4', 1, velocity=100)  # tle
    melody.add_note('E4', 1, velocity=100)  # lamb
    
    # "Whose fleece was white as snow"
    melody.add_note('E4', 1, velocity=100)  # whose
    melody.add_note('D4', 1, velocity=100)  # fleece
    melody.add_note('D4', 1, velocity=100)  # was
    melody.add_note('E4', 1, velocity=100)  # white
    melody.add_note('D4', 1, velocity=100)  # as
    melody.add_note('C4', 3, velocity=100)  # snow


@register_track
def track(harmony):
    """Harmonic accompaniment with chord tones"""
    harmony = harmony.add_sequence("harmony")
    
    # "Mary had a little lamb,"
    harmony.add_note('G3', 1, velocity=80)
    harmony.add_note('E3', 1, velocity=80)
    harmony.add_note('C3', 1, velocity=80)
    harmony.add_note('E3', 1, velocity=80)
    harmony.add_note('G3', 1, velocity=80)
    harmony.add_note('G3', 1, velocity=80)
    harmony.add_note('C4', 2, velocity=80)
    
    # "Little lamb, little lamb,"
    harmony.add_note('G3', 1, velocity=80)
    harmony.add_note('A3', 1, velocity=80)
    harmony.add_note('B3', 2, velocity=80)
    harmony.add_note('C4', 1, velocity=80)
    harmony.add_note('B3', 1, velocity=80)
    harmony.add_note('C4', 2, velocity=80)
    
    # "Mary had a little lamb"
    harmony.add_note('G3', 1, velocity=80)
    harmony.add_note('E3', 1, velocity=80)
    harmony.add_note('C3', 1, velocity=80)
    harmony.add_note('E3', 1, velocity=80)
    harmony.add_note('G3', 1, velocity=80)
    harmony.add_note('G3', 1, velocity=80)
    harmony.add_note('C4', 1, velocity=80)
    
    # "Whose fleece was white as snow"
    harmony.add_note('G3', 1, velocity=80)
    harmony.add_note('A3', 1, velocity=80)
    harmony.add_note('A3', 1, velocity=80)
    harmony.add_note('G3', 1, velocity=80)
    harmony.add_note('A3', 1, velocity=80)
    harmony.add_note('G3', 3, velocity=80)


@register_track
def track(bass):
    """Bass line providing rhythmic and harmonic foundation"""
    bass = bass.add_sequence("bass")
    
    # "Mary had a little lamb,"
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 2, velocity=90)
    
    # "Little lamb, little lamb,"
    bass.add_note('G2', 1, velocity=90)
    bass.add_note('G2', 1, velocity=90)
    bass.add_note('G2', 2, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 2, velocity=90)
    
    # "Mary had a little lamb"
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    
    # "Whose fleece was white as snow"
    bass.add_note('G1', 0.5, velocity=90)
    bass.add_note('C1', 0.5, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('C2', 1, velocity=90)
    bass.add_note('G2', 1, velocity=90)
    bass.add_note('G2', 1, velocity=90)
    bass.add_note('C2', 2, velocity=90)
    bass.add_note('C3', 1, velocity=90)


# Play all three tracks together polyphonically

play_polyphonic(tempo=180)
export_midi("presentation_demo.mid")