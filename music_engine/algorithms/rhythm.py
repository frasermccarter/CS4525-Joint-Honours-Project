import random

class RhythmGenerator:
    def __init__(self, allowed_durations=None):
        """
        Initialise the RhythmGenerator with allowed note durations.
        
        Parameters:
        - allowed_durations: List of positive durations (in beats). If None, defaults to [0.25, 0.5, 1].
        
        Raises:
        - ValueError: If durations are not positive or list is empty.
        """
        if allowed_durations is None:
            #Default to simple common subdivisions (in beats)
            self.allowed_durations = [0.25, 0.5, 1]  #semiquaver, quaver, crotchet
        else:
            if not allowed_durations:
                raise ValueError("allowed_durations list cannot be empty.")
            if not all(d > 0 for d in allowed_durations):
                raise ValueError("All allowed durations must be positive numbers.")
            self.allowed_durations = allowed_durations

    def generate_bar(self, total_beats=4):
        """
        Generate a list of durations that sum to exactly total_beats.
        
        Parameters:
        - total_beats: Total duration of the bar in beats (default 4)
        
        Returns:
        - List of durations that sum to total_beats
        
        Raises:
        - ValueError: If total_beats is invalid or impossible to fill with given durations.
        """
        if total_beats < 0:
            raise ValueError("total_beats must be a non-negative number.")
        
        if total_beats == 0:
            return []
        
        rhythm = []
        current_sum = 0.0
        epsilon = 1e-9  # Floating-point tolerance to handle precision errors
        
        while current_sum < total_beats - epsilon:
            remaining = total_beats - current_sum
            
            # Only choose durations that fit (with epsilon tolerance)
            valid_durations = [d for d in self.allowed_durations if d <= remaining + epsilon]
            
            if not valid_durations:
                raise ValueError(
                    f"Cannot fill a bar of {total_beats} beats with allowed durations {self.allowed_durations}. "
                    f"Remaining: {remaining:.4f} beats. Consider adding smaller duration values."
                )
            
            next_duration = random.choice(valid_durations)
            rhythm.append(next_duration)
            current_sum += next_duration
            # Round to avoid floating point accumulation errors
            current_sum = round(current_sum, 10)
        
        return rhythm
    
