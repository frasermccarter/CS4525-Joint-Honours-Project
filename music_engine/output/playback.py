import numpy as np
import sounddevice as sd


class PlaybackEngine:
    """
    Audio playback using the computer's audio output via sounddevice.
    Supports both monophonic (sequential) and polyphonic (simultaneous) playback.
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
        Play all sequences in a track sequentially (monophonic).
        
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

    def play_polyphonic(self, tracks):
        """
        Play multiple tracks simultaneously with polyphonic mixing.
        
        Parameters:
        - tracks: A list of Track objects or a single Track object to play polyphonically
        """
        if isinstance(tracks, list):
            track_list = tracks
        else:
            track_list = [tracks]
        
        seconds_per_beat = 60 / self.tempo
        
        #Render all tracks to audio
        all_audio = []
        max_duration = 0
        
        for track in track_list:
            audio = self._render_track(track, seconds_per_beat)
            all_audio.append(audio)
            max_duration = max(max_duration, len(audio))
        
        #Pad all audio to the same length
        for i in range(len(all_audio)):
            if len(all_audio[i]) < max_duration:
                all_audio[i] = np.pad(all_audio[i], (0, max_duration - len(all_audio[i])), mode='constant')
        
        #Mix all tracks together
        mixed_audio = np.sum(all_audio, axis=0)
        
        # Normalize to prevent clipping
        max_amplitude = np.max(np.abs(mixed_audio))
        if max_amplitude > 1.0:
            mixed_audio /= max_amplitude
        
        #Play the mixed audio
        sd.play(mixed_audio, self.sample_rate, blocking=True)

    def _render_track(self, track, seconds_per_beat):
        """
        Render all sequences in a track to audio without playing.
        
        Parameters:
        - track: A Track object to render
        - seconds_per_beat: Duration of one beat in seconds
        
        Returns:
        - A numpy array containing the rendered audio
        """
        all_audio = []
        
        for sequence in track.get_sequences():
            audio = self._render_sequence(sequence, seconds_per_beat)
            all_audio.append(audio)
        
        if not all_audio:
            return np.array([])
        
        #Concatenate all sequences
        return np.concatenate(all_audio)

    def _render_sequence(self, sequence, seconds_per_beat):
        """
        Render a sequence to audio without playing.
        
        Parameters:
        - sequence: A Sequence object to render
        - seconds_per_beat: Duration of one beat in seconds
        
        Returns:
        - A numpy array containing the rendered audio
        """
        all_audio = []
        
        for note in sequence.get_notes():
            duration_seconds = note.duration * seconds_per_beat
            audio = self._render_note(note, duration_seconds)
            all_audio.append(audio)
        
        if not all_audio:
            return np.array([])
        
        return np.concatenate(all_audio)

    def _render_note(self, note, duration_seconds):
        """
        Render a single note to audio without playing.
        
        Parameters:
        - note: A Note object to render
        - duration_seconds: Duration of the note in seconds
        
        Returns:
        - A numpy array containing the rendered audio
        """
        # Envelope timings
        attack_time = 0.01   # 10ms
        release_time = 0.02  # 20ms
        
        # Account for envelope in the tone duration
        # The requested duration_seconds should be the total time INCLUDING envelope
        # So the tone itself should be shorter to leave room for the release
        tone_duration = max(0.001, duration_seconds - release_time)  # Ensure minimum duration
        
        #Calculate frequency from MIDI pitch
        frequency = 440 * (2 ** ((note.midi_pitch - 69) / 12))

        #Generate time array
        t = np.linspace(0, tone_duration, int(self.sample_rate * tone_duration), False)

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

        return waveform

    def _play_sequence(self, sequence, seconds_per_beat):
        """
        Internal method to play a sequence with a given tempo.
        
        Parameters:
        - sequence: A Sequence object
        - seconds_per_beat: Duration of one beat in seconds
        """
        audio = self._render_sequence(sequence, seconds_per_beat)
        sd.play(audio, self.sample_rate, blocking=True)

    def _play_note(self, note, duration_seconds):
        """
        Internal method to play a single note (deprecated).
        Use _render_note() instead to render audio without playing.
        
        Parameters:
        - note: A Note object to play
        - duration_seconds: Duration of the note in seconds
        """
        audio = self._render_note(note, duration_seconds)
        sd.play(audio, self.sample_rate, blocking=True)

    def close(self):
        """
        Stop playback and close the audio device.
        """
        sd.stop()
