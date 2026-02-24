"""
This file is currently used for testing the basic functionality of the engine. Later it will change to a more sandboxed experience where users don't have to import or define a main function.
"""

from music_engine.engine import Controller

def main():
    controller = Controller()

    #Create a track and add sequences
    piano = controller.new_track("piano")
    
    intro = piano.add_sequence("intro")
    intro.add_note('C4', 0.5)
    intro.add_note(64, 0.5, velocity=20)
    intro.add_note(440.0, 1.0)

    verse = piano.add_sequence("verse")
    verse.add_note('G3', 1)
    verse.add_note('G3', 1)
    verse.add_note('G3', 1)

    guitar = controller.new_track("guitar")
    guitar.add_sequence("intro")

    # Display structure
    controller.show()

    #Play individual sequences
    print("\n--- Playing intro sequence ---")
    intro.play(tempo=120)
    
    print("\n--- Playing verse sequence ---")
    verse.play(tempo=120)

    #Play individual tracks
    print("\n--- Playing piano track ---")
    piano.play(tempo=120)
    
    print("\n--- Playing guitar track ---")
    guitar.play(tempo=120)

    #Play and export all tracks
    print("\n--- Playing all tracks ---")
    controller.play(tempo=120)

if __name__ == "__main__":
    main()