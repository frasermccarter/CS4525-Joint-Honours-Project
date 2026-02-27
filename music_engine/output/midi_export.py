import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage


class MIDIExporter:
    """
    Exports Track objects to MIDI files.
    """

    def __init__(self, tempo=120, ticks_per_beat=480):
        self.tempo = tempo
        self.ticks_per_beat = ticks_per_beat

    def export(self, track, filename):
        """
        Export a single track to a MIDI file.
        
        Parameters:
        - track: A Track object to export
        - filename: Output MIDI file path
        """
        mid = MidiFile(ticks_per_beat=self.ticks_per_beat)
        self._add_track_to_midi(mid, track)
        mid.save(filename)

    def export_multiple(self, tracks, filename):
        """
        Export multiple tracks to a single MIDI file, each as a separate MIDI track.
        
        Parameters:
        - tracks: A list of Track objects to export
        - filename: Output MIDI file path
        """
        mid = MidiFile(ticks_per_beat=self.ticks_per_beat)
        for track in tracks:
            self._add_track_to_midi(mid, track)
        mid.save(filename)

    def _add_track_to_midi(self, midi_file, track):
        """
        Add a track's sequences and notes to the MIDI file as a separate MIDI track.
        
        Parameters:
        - midi_file: The MidiFile object to add to
        - track: The Track object to add
        """
        midi_track = MidiTrack()
        midi_file.tracks.append(midi_track)

        # Set tempo once per MIDI track
        tempo_microseconds = mido.bpm2tempo(self.tempo)
        midi_track.append(
            MetaMessage("set_tempo", tempo=tempo_microseconds)
        )

        # Add track name if it exists
        if track.name:
            midi_track.append(
                MetaMessage("track_name", name=track.name)
            )

        current_time = 0

        # Add all sequences and their notes in order
        for sequence in track.get_sequences():
            for note in sequence.get_notes():
                duration_ticks = int(note.duration * self.ticks_per_beat)

                # Note ON
                midi_track.append(
                    Message(
                        "note_on",
                        note=note.midi_pitch,
                        velocity=note.velocity,
                        time=current_time,
                    )
                )

                # Note OFF
                midi_track.append(
                    Message(
                        "note_off",
                        note=note.midi_pitch,
                        velocity=0,
                        time=duration_ticks,
                    )
                )

                current_time = 0
