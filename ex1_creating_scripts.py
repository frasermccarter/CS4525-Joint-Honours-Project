"""
An example file for how to create scripts using the music scripting language.

1. Create a .py file with any chosen name (e.g. my_script.py) and place it in the same (root) directory as runner.py.

2. In the script file, import everything from runner.py using the line "from runner import *".  
   This will give you access to the necessary functions and classes to create music with the engine.  
   Runner.py must be imported before any user code.

3. Define track functions using the @register_track decorator.

4. Within each track function, create sequences and add notes to those sequences using the provided methods.

5. Call the play method on the track or on individual sequences to play the music, or use export_midi to save it as a MIDI file.

6. Run the script file to execute the code and create music with the engine.

7. You can create as many track functions as you like, and they will all be registered with the engine and can be played together or separately as desired.

8. The engine will automatically handle the timing and synchronization of the tracks and sequences when playing or exporting to MIDI.

9. You can also use the provided algorithms to generate notes and rhythms, or create your own custom algorithms to generate musical ideas.

10. For more advanced usage, you can also use the polyphonic playback feature to play multiple tracks together at the same time, allowing for more complex and layered musical compositions.

11. See the example files for more specific examples of how to use the various features of the engine and the scripting language.
"""