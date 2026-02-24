import numpy as np
import sounddevice as sd


class PlaybackEngine:
    """
    Audio playback using the computer's audio output via sounddevice.
    """
    
    def __init__(self, tempo=120, sample_rate=44100):
        """
        Initialise the playback engine.
        
        Parameters:
        - tempo: Tempo in BPM (default 120)
        - sample_rate: Sample rate in Hz (default 44100)
        """
        self.tempo = tempo
        self.sample_rate = sample_rate

    def play_track(self, track):
        """
        Play all sequences in a track.
        
        Parameters:
        - track: A Track object to play
        """
        seconds_per_beat = 60 / self.tempo

        for sequence in track.get_sequences():
            self._play_sequence(sequence, seconds_per_beat)

    def play_sequence(self, sequence):
        """
        Play a single sequence.
        
        Parameters:
        - sequence: A Sequence object to play
        """
        seconds_per_beat = 60 / self.tempo
        self._play_sequence(sequence, seconds_per_beat)

    def _play_sequence(self, sequence, seconds_per_beat):
        """
        Internal method to play a sequence with a given tempo.
        
        Parameters:
        - sequence: A Sequence object
        - seconds_per_beat: Duration of one beat in seconds
        """
        for note in sequence.get_notes():
            duration_seconds = note.duration * seconds_per_beat
            self._play_note(note, duration_seconds)

    def _play_note(self, note, duration_seconds):
        """
        Internal method to play a single note.
        
        Parameters:
        - note: A Note object to play
        - duration_seconds: Duration of the note in seconds
        """
        #Calculate frequency from MIDI pitch
        frequency = 440 * (2 ** ((note.midi_pitch - 69) / 12))

        #Generate time array
        t = np.linspace(0, duration_seconds, int(self.sample_rate * duration_seconds), False)

        #Generate sine wave
        waveform = np.sin(2 * np.pi * frequency * t)

        # Apply velocity scaling (normalize to 0-1 range)
        amplitude = note.velocity / 100.0
        waveform *= amplitude

        # Apply envelope (Attack + Release)
        attack_time = 0.01   # 10ms
        release_time = 0.02  # 20ms

        attack_samples = int(self.sample_rate * attack_time)
        release_samples = int(self.sample_rate * release_time)

        #Create envelope, this is used to avoid clicks at the start and end of the note by ramping the amplitude up and down
        envelope = np.ones_like(waveform)

        #Attack phase (ramp from 0 to 1)
        if attack_samples > 0 and len(envelope) > attack_samples:
            envelope[:attack_samples] = np.linspace(0, 1, attack_samples)

        #Release phase (ramp from 1 to 0)
        if release_samples > 0 and len(envelope) > release_samples:
            envelope[-release_samples:] = np.linspace(1, 0, release_samples)

        #Apply envelope to waveform
        waveform *= envelope

        #Play the note
        sd.play(waveform, self.sample_rate, blocking=True)

    def close(self):
        """
        Stop playback and close the audio device.
        """
        sd.stop()
