"""
This is a script to verify the contents of the generated MIDI files by printing out the number of tracks and messages in each track. It checks the individual test piano and guitar MIDI files, as well as the combined MIDI file, just to ensure that they contain the expected data.
"""

import mido

#Check piano track
piano_mid = mido.MidiFile('piano_output.mid')
print('piano_output.mid:')
print(f'  Tracks: {len(piano_mid.tracks)}')
for i, track in enumerate(piano_mid.tracks):
    print(f'  Track {i}: {len(track)} messages')

#Check guitar track
guitar_mid = mido.MidiFile('guitar_output.mid')
print('\nguitar_output.mid:')
print(f'  Tracks: {len(guitar_mid.tracks)}')
for i, track in enumerate(guitar_mid.tracks):
    print(f'  Track {i}: {len(track)} messages')

#Check combined file
combined_mid = mido.MidiFile('test_output.mid')
print('\ntest_output.mid (combined):')
print(f'  Tracks: {len(combined_mid.tracks)}')
for i, track in enumerate(combined_mid.tracks):
    track_name = 'Unknown'
    for msg in track:
        if msg.type == 'track_name':
            track_name = msg.name
            break
    print(f'  Track {i} ({track_name}): {len(track)} messages')
