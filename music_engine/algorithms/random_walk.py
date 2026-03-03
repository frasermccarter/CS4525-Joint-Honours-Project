"""
This module implements a random walk algorithm for generating musical notes based on a specified scale (major or minor) or unspecified (chromatically).
"""

import random

#scale intervals defied in semitones from the root note
MAJOR_SCALE_INTERVALS = [0, 2, 4, 5, 7, 9, 11]
MINOR_SCALE_INTERVALS = [0, 2, 3, 5, 7, 8, 10]

class RandomWalk:
    def __init__(self, scale_type="major"):
        if scale_type == "major":
            self.intervals = MAJOR_SCALE_INTERVALS
        elif scale_type == "minor":
            self.intervals = MINOR_SCALE_INTERVALS
        else:
            raise ValueError("Unsupported scale type. Please choose between 'major' or 'minor'. For chromatic walk, use the generate_chromatic method or leave scale unspecified.")
        
    def generate(self, root_midi, steps, step_duration):
        """
        Generate notes using scale-based random walk.
        
        Parameters:
        - root_midi: Starting MIDI pitch
        - steps: Number of notes to generate
        - step_duration: Duration of each note in beats
        
        Returns:
        - List of (pitch, duration) tuples
        """
        notes = []
        current_degree = 0  #Start at the root note

        for _ in range(steps):
            interval = self.intervals[current_degree]
            pitch = root_midi + interval
            notes.append((pitch, step_duration))

            #Randomly decide to move up, down, or stay
            move = random.choice([-1, 0, 1])
            next_degree = (current_degree + move) % len(self.intervals) #Wrap around the scale degrees

            current_degree = next_degree

        return notes
    
    def generate_chromatic(self, start_pitch, num_notes, max_step=2, duration=0.5):
        """
        Generate notes using chromatic random walk (unrestricted by scale).
        
        Parameters:
        - start_pitch: Starting MIDI pitch
        - num_notes: Number of notes to generate
        - max_step: Maximum semitone step (+ or - max_step)
        - duration: Duration of each note in beats
        
        Returns:
        - List of (pitch, duration) tuples
        """
        notes = []
        current_pitch = start_pitch
        
        for _ in range(num_notes):
            notes.append((current_pitch, duration))
            #Randomly step up, down, or stay within max_step range
            step = random.randint(-max_step, max_step)
            current_pitch = max(0, current_pitch + step)  #Ensure pitch doesn't go below 0
        
        return notes
    

