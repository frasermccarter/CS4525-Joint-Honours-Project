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
            self.allowed_durations = sorted(allowed_durations, reverse=True)  # Sort largest first

    def generate_bar(self, total_beats=4):
        """
        Generate a list of durations that sum to exactly total_beats.
        
        Uses a backtracking algorithm to find a valid combination of durations
        that sum to the target total_beats.
        
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
        
        epsilon = 1e-9
        #Try to find a valid combination using backtracking
        result = self._find_rhythm(total_beats, [], epsilon)
        
        if result is None:
            raise ValueError(
                f"Cannot fill a bar of {total_beats} beats with allowed durations {sorted(self.allowed_durations, reverse=True)}. "
                f"Consider adding smaller duration values or adjusting total_beats."
            )
        
        return result

    def _find_rhythm(self, remaining, current_rhythm, epsilon):
        """
        Recursively find a valid rhythm combination using backtracking.
        
        Parameters:
        - remaining: Remaining beats to fill
        - current_rhythm: Current list of durations selected
        - epsilon: Floating-point tolerance
        
        Returns:
        - A valid rhythm list if found, None otherwise
        """
        #Base case: we've filled the total
        if remaining < epsilon:
            return current_rhythm if remaining < epsilon else None
        
        #Try each duration, starting with largest for efficiency
        durations_to_try = [d for d in self.allowed_durations if d <= remaining + epsilon]
        
        if not durations_to_try:
            return None
        
        #Shuffle to add randomness while still guaranteeing we find a solution
        random.shuffle(durations_to_try)
        
        for duration in durations_to_try:
            new_remaining = remaining - duration
            #Round to avoid floating point accumulation errors
            new_remaining = round(new_remaining, 10)
            
            result = self._find_rhythm(new_remaining, current_rhythm + [duration], epsilon)
            if result is not None:
                return result
        
        return None
    

