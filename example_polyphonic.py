"""
Example: Polyphonic Playback

This example demonstrates how to use the polyphonic playback feature
to play multiple tracks simultaneously with audio mixing.

The engine will:
1. Create three tracks: melody, harmony, and bass
2. Add notes to each track
3. Play all tracks together polyphonically (simultaneously)

The audio from all tracks is mixed together and played at the same time,
creating a polyphonic arrangement.
"""

from music_engine.engine.controller import Controller
from music_engine.core.sequence import Sequence


def main():
    # Create a controller
    controller = Controller()
    
    # ===== Track 1: Melody =====
    melody_track = controller.new_track("Melody")
    melody_seq = Sequence("Melody Notes")
    
    # Add a simple melody (C major scale)
    melody_notes = [
        (60, 1),   # C4, quarter note
        (62, 1),   # D4, quarter note
        (64, 1),   # E4, quarter note
        (65, 1),   # F4, quarter note
    ]
    
    for pitch, duration in melody_notes:
        melody_seq.add_note(pitch, duration, velocity=85)
    
    melody_track.add_sequence(melody_seq)
    
    # ===== Track 2: Harmony =====
    harmony_track = controller.new_track("Harmony")
    harmony_seq = Sequence("Harmony Notes")
    
    # Add harmony notes (a third below the melody)
    harmony_notes = [
        (53, 1),   # F3, quarter note
        (55, 1),   # G3, quarter note
        (57, 1),   # A3, quarter note
        (58, 1),   # Bb3, quarter note
    ]
    
    for pitch, duration in harmony_notes:
        harmony_seq.add_note(pitch, duration, velocity=80)
    
    harmony_track.add_sequence(harmony_seq)
    
    # ===== Track 3: Bass =====
    bass_track = controller.new_track("Bass")
    bass_seq = Sequence("Bass Notes")
    
    # Add bass notes (whole notes)
    bass_notes = [
        (48, 2),   # C3, half note
        (53, 2),   # F3, half note
    ]
    
    for pitch, duration in bass_notes:
        bass_seq.add_note(pitch, duration, velocity=90)
    
    bass_track.add_sequence(bass_seq)
    
    # ===== Play Polyphonically =====
    print("Playing tracks polyphonically (all at once)...")
    print(f"Melody track: {len(melody_seq.get_notes())} notes")
    print(f"Harmony track: {len(harmony_seq.get_notes())} notes")
    print(f"Bass track: {len(bass_seq.get_notes())} notes")
    
    # Play all tracks simultaneously
    controller.play_polyphonic(tempo=120)
    
    print("Playback complete!")
    
    # ===== Alternative: Play specific tracks =====
    # You can also play specific tracks polyphonically:
    # controller.play_polyphonic(tempo=120, tracks=[melody_track, harmony_track])
    
    # ===== Alternative: Sequential playback (original behavior) =====
    # To play tracks one after another, use the original play() method:
    # controller.play(tempo=120)


if __name__ == "__main__":
    main()
