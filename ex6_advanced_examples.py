"""
Advanced creative examples showcasing interesting ways to use the music engine.
Each example demonstrates a different compositional technique or algorithmic approach.

Uncomment an example to hear how it sounds.
"""

from runner import *
from music_engine.core.chord import Chord

# ============================================================================
# 1. THEME AND VARIATIONS
# ============================================================================
# Generate a simple theme, then create variations with different algorithms
# @register_track
# def track(theme_variations):
#     # Original theme
#     theme = theme_variations.add_sequence("theme")
#     theme.add_note('C4', 0.5)
#     theme.add_note('E4', 0.5)
#     theme.add_note('G4', 1.0)
    
#     # Variation 1: Same theme with random walk for variation
#     var1 = theme_variations.add_sequence("variation1")
#     var1.generate_random_walk(start_pitch='C4', num_notes=8, max_step=2, duration=0.5, scale_type='major')
    
#     # Variation 2: Arpeggio of same chords
#     var2 = theme_variations.add_sequence("variation2")
#     var2.generate_arpeggio("Cmaj", octave=4, note_duration=0.5, direction="up")

#     theme_variations.play(tempo=120)


# ============================================================================
# 2. CHORD PROGRESSION WITH COUNTERPOINT
# ============================================================================
# Create a bass line over a chord progression, with melody on top
# @register_track
# def track(bass):
#     # Bass line (root movements)
#     bass = bass.add_sequence("bass")
#     chords_seq = ['Cmaj', 'Fmaj', 'Gmaj', 'Cmaj']
#     for chord_symbol in chords_seq:
#         chord = Chord(chord_symbol, octave=2)
#         root = chord.get_chord_pitches()[0]
#         bass.add_note(root, 2.0)

# @register_track
# def track(harmony):
#     # Harmony with rhythm pattern
#     harmony = harmony.add_sequence("harmony")
#     harmony.generate_rhythm_sequence(pitch='E4', total_beats=8, allowed_durations=[0.25, 0.5])

# @register_track
# def track(melody): 
#     # Melody in random walk on C major scale
#     melody = melody.add_sequence("melody")
#     melody.generate_random_walk(start_pitch='G4', num_notes=16, max_step=2, duration=0.5, scale_type='major')

# play_polyphonic(tempo=100)


# ============================================================================
# 3. POLYRHYTHMIC COMPOSITION
# ============================================================================
# Create multiple sequences with different rhythmic patterns that interlock
# @register_track
# def track(fast):
#     # Pattern 1: Fast sixteenths on kick drum-like pitch
#     fast = fast.add_sequence("fast_rhythm")
#     for _ in range(16):
#         fast.add_note('C4', 0.25)

# @register_track
# def track(syncopated):  
#     # Pattern 2: Syncopated rhythm (3 against 4)
#     syncopated = syncopated.add_sequence("syncopated")
#     durations = [0.33, 0.33, 0.34] * 4  # 3 beats repeated, creating polyrhythm
#     for dur in durations:
#         syncopated.add_note('G4', dur)

# @register_track
# def track(sustained):  
#     # Pattern 3: Long sustained notes
#     sustained = sustained.add_sequence("sustained")
#     sustained.add_note('E4', 4.0)

# play_polyphonic(tempo=120)


# ============================================================================
# 4. GENERATIVE AMBIENT COMPOSITION
# ============================================================================
# Create evolving, ambient textures using multiple random walks
# @register_track
# def track(pad1):
#     # Low pad layer
#     pad1 = pad1.add_sequence("pad1")
#     pad1.generate_random_walk(start_pitch='C3', num_notes=20, max_step=1, 
#                               duration=0.5, scale_type='major')

# @register_track
# def track(pad2): 
#     # Mid melody layer with larger steps
#     melody_layer = pad2.add_sequence("melody_layer")
#     melody_layer.generate_random_walk(start_pitch='G4', num_notes=20, max_step=3, 
#                                       duration=0.5, scale_type='major')
    
# @register_track
# def track(pad3):
#     # High arpeggio layer (static chord)
#     high_layer = pad3.add_sequence("high_layer")
#     for _ in range(5):
#         high_layer.generate_arpeggio("Cmaj7", octave=5, note_duration=0.5, direction="up")

# play_polyphonic(tempo=80)


# ============================================================================
# 5. CALL AND RESPONSE PATTERN
# ============================================================================
# Create a musical conversation between two voices
# @register_track
# def track(call_response):
#     # Call: A simple melodic phrase in C major
#     call = call_response.add_sequence("call")
#     call.add_note('C4', 0.5)
#     call.add_note('E4', 0.5)
#     call.add_note('G4', 1.0)
#     call.wait(0.5)  # Silence for response
  
#     # Response: Shifted version of the call
#     response = call_response.add_sequence("response")
#     response.wait(2.5)  # Wait for the call
#     response.add_note('E4', 0.5)
#     response.add_note('G4', 0.5)
#     response.add_note('C5', 1.0)

#     call_response.play(tempo=100)


# ============================================================================
# 6. RHYTHMIC DIMINUTION
# ============================================================================
# Start with slow notes, gradually speed up (diminution)
# @register_track
# def track(diminution):
#     intro = diminution.add_sequence("intro")
    
#     # Slow section
#     intro.add_note('C4', 2.0)
#     intro.add_note('D4', 2.0)
    
#     # Acceleration: halving durations
#     intro.add_note('E4', 1.0)
#     intro.add_note('F4', 1.0)
#     intro.add_note('G4', 0.5)
#     intro.add_note('A4', 0.5)
#     intro.add_note('B4', 0.25)
#     intro.add_note('C5', 0.25)

#     diminution.play(tempo=120)


# ============================================================================
# 7. ALGORITHMIC HARMONY FROM MELODY
# ============================================================================
# Generate a melody, then create harmony using chord arpeggios beneath it
# @register_track
# def track(melody):
#     # Main melody
#     melody = melody.add_sequence("melody")
#     melody.generate_random_walk(start_pitch='E4', num_notes=12, max_step=2, 
#                                 duration=0.5, scale_type='major')
    
# @register_track
# def track(harmony):
#     # Harmony: Root position of C major chord underneath
#     harmony = harmony.add_sequence("harmony")
#     for _ in range(4):  # Match melody length
#         harmony.generate_arpeggio("Cmaj", octave=3, note_duration=0.5, direction="up")
#           # Just play once; in real app you'd repeat or vary

# play_polyphonic(tempo=120)


# ============================================================================
# 8. MINIMALIST REPETITION WITH SLIGHT VARIATION
# ============================================================================
# Repeat a pattern but with small random variations (minimalism technique)
# @register_track
# def track(minimalist):
#     import random
#     pattern = minimalist.add_sequence("pattern")
    
#     # Repeat a simple 4-note motif 8 times
#     base_notes = ['C4', 'E4', 'G4', 'E4']
#     for rep in range(8):
#         for note_name in base_notes:
#             # Slight rhythmic variation: add a small random duration offset
#             duration_offset = random.uniform(-0.1, 0.1)
#             pattern.add_note(note_name, 0.5 + duration_offset)
#         pattern.wait(1.0)  # Breath between repetitions

#     minimalist.play(tempo=140)


# ============================================================================
# 9. MELODIC INVERSION AND RETROGRADE
# ============================================================================
# Create a melody, then add its inversion and retrograde
# @register_track
# def track(inversion):
#     notes = ['C4', 'E4', 'G4', 'A4']

#     # Original melody (ascending)
#     original = inversion.add_sequence("original")
#     for note in notes:
#         # Inversion (mirror around C4)
#         original.add_note(note, 0.5)  # Add original notes to get pitches
    
#     # Retrograde (backwards)
#     retrograde = inversion.add_sequence("retrograde")
#     for note in reversed(notes):
#         retrograde.add_note(note, 0.5)

#     inversion.play(tempo=120)


# ============================================================================
# 10. FUGAL STAGGERED ENTRIES (Canon)
# ============================================================================
# Voices enter one at a time with the same motif (canon technique)
# motif_notes = [60, 62, 64, 67] #Midi
# @register_track
# def track(voice1):
#     # Voice 1: Starts immediately
#     voice1 = voice1.add_sequence("voice1")
#     for note in motif_notes:
#         voice1.add_note(note, 1.0)
#     voice1.wait(2)
#     for note in motif_notes:
#         voice1.add_note(note+5, 1)  # Repeat motif for longer duration
    
# @register_track
# def track(voice2):
#     # Voice 2: Enters after voice1 starts
#     voice2 = voice2.add_sequence("voice2")
#     voice2.wait(2)  # Wait 2 beats (4 notes * 0.5)
#     for note in motif_notes:
#         voice2.add_note(note, 1.0)
#     voice2.wait(2)
#     for note in motif_notes:
#         voice2.add_note(note+5, 1)  # Repeat motif for longer duration
    
# @register_track
# def track(voice3):
#     # Voice 3: Enters later (lower octave)
#     voice3 = voice3.add_sequence("voice3")
#     voice3.wait(4)
#     for note in motif_notes:
#         voice3.add_note(note-12, 1)  # Lower octave
#     voice3.wait(2)
#     for note in motif_notes:
#         voice3.add_note(note-7, 1)  # Repeat motif for longer duration

# play_polyphonic(tempo=100)


# ============================================================================
# 11. RANDOM WALK WITH CONSTRAINED OCTAVE RANGE
# ============================================================================
# Create wandering melodies that stay within a range
# @register_track
# def track(constrained_walk):
#     # Wander within C3-C5 range
#     melody = constrained_walk.add_sequence("constrained_melody")
#     melody.generate_random_walk(start_pitch='C4', num_notes=20, max_step=2, 
#                                 duration=0.5, scale_type='major')

#     constrained_walk.play(tempo=120)


# ============================================================================
# 12. STOCHASTIC RHYTHM WITH CHROMATIC MELODY
# ============================================================================
#This example shows how the chord helper utility can be imported to generate chord tones for a given chord.  
#In this case, we generate the pitches for a C major chord and then use those pitches to generate a rhythm sequence in the intro sequence of the ideaOne track.

# @register_track
# def track(ideaOne):
#     seq1 = ideaOne.add_sequence("seq1")

#     from music_engine.core.chord import Chord

#     chord = Chord("Cmaj")
#     for note in chord.get_chord_pitches():
#         seq1.generate_rhythm_sequence(pitch=note, total_beats=4)

#     seq1.play(tempo=120)


# ============================================================================
# Example to run:
# Uncomment one of the play_polyphonic() or track.play() calls above to hear it!
# Or export them all:
# ============================================================================

# Export all defined tracks to a single MIDI file
controller.export_midi("advanced_examples.mid", tempo=120)
