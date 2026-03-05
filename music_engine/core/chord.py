from music_engine.core.sequence import Note

MAJOR_TRIAD_INTERVALS = [0, 4, 7]
MINOR_TRIAD_INTERVALS = [0, 3, 7]
DOMINANT_SEVENTH_INTERVALS = [0, 4, 7, 10]
DIMINISHED_SEVENTH_INTERVALS = [0, 3, 6, 9]
AUGMENTED_TRIAD_INTERVALS = [0, 4, 8]
MAJOR_SEVENTH_INTERVALS = [0, 4, 7, 11]
ADD_SIX_INTERVALS = [0, 4, 7, 9]
ADD_NINE_INTERVALS = [0, 4, 7, 14]

class Chord:
    """
    Represents a chord, which is a collection of notes played together.
    """

    def __init__(self, symbol, octave=4):
        """
        Symbol: A string representing the chord symbol.
        
        Valid chord symbols include:
        - Major triads: "C", "Cmaj"
        - Minor triads: "Cm", "Cmin"
        - Dominant sevenths: "C7"
        - Diminished sevenths: "Cdim7", "Cdim"
        - Augmented triads: "Caug", "C+"
        - Major sevenths: "Cmaj7", "CM7"
        - Add six: "Cadd6"
        - Add nine: "Cadd9", "Cadd2"
        
        Examples: "C", "Am", "G7", "Cmaj7", "Dm", "D7", "Edim7", "Caug"
        
        Octave: The octave in which to place the chord (default 4)
        """

        self.symbol = symbol
        self.octave = octave

        self.root_name, self.quality = self._parse_symbol(symbol)
        self.root_midi = self._get_root_midi()

    def _parse_symbol(self, symbol):
        symbol = symbol.strip()

        #Check for major seventh chords (maj7, M7)
        if symbol.endswith('maj7') or symbol.endswith('M7'):
            suffix = 'maj7' if symbol.endswith('maj7') else 'M7'
            return symbol[:-len(suffix)], 'major_seventh'
        
        #Check for dominant seventh chords (7)
        if symbol.endswith('7'):
            return symbol[:-1], 'dominant_seventh'

        #Check for diminished seventh chords (dim7, °7)
        if symbol.endswith('dim7'):
            return symbol[:-4], 'diminished_seventh'

        #Check for diminished triads (dim, °)
        if symbol.endswith('dim') or symbol.endswith('°'):
            suffix = 'dim' if symbol.endswith('dim') else '°'
            return symbol[:-len(suffix)], 'diminished_seventh'

        #Check for augmented chords (aug, +)
        if symbol.endswith('aug') or symbol.endswith('+'):
            suffix = 'aug' if symbol.endswith('aug') else '+'
            return symbol[:-len(suffix)], 'augmented'

        #Check for add6 chords
        if symbol.endswith('add6'):
            return symbol[:-4], 'add_six'

        #Check for add9/add2 chords
        if symbol.endswith('add9') or symbol.endswith('add2'):
            suffix = 'add9' if symbol.endswith('add9') else 'add2'
            return symbol[:-len(suffix)], 'add_nine'

        #Check for minor chords (m, min)
        if symbol.endswith('m') and not symbol.endswith('maj'):
            return symbol[:-1], 'minor'

        if symbol.endswith('min'):
            return symbol[:-3], 'minor'
        
        #Check for major chords (maj)
        if symbol.endswith('maj'):
            return symbol[:-3], 'major'
        
        #Default to major chord
        return symbol, 'major'
    
    def _get_root_midi(self):
        note_string = f"{self.root_name}{self.octave}"
        try:
            note = Note(note_string, duration=1)  #Duration doesn't matter here
            return note.midi_pitch
        except ValueError as e:
            raise ValueError(f"Unknown chord symbol. '{self.root_name}' is not a valid note. {str(e)}")
    
    def get_chord_pitches(self):
        if self.quality == 'major':
            intervals = MAJOR_TRIAD_INTERVALS
        elif self.quality == 'minor':
            intervals = MINOR_TRIAD_INTERVALS
        elif self.quality == 'dominant_seventh':
            intervals = DOMINANT_SEVENTH_INTERVALS
        elif self.quality == 'diminished_seventh':
            intervals = DIMINISHED_SEVENTH_INTERVALS
        elif self.quality == 'augmented':
            intervals = AUGMENTED_TRIAD_INTERVALS
        elif self.quality == 'major_seventh':
            intervals = MAJOR_SEVENTH_INTERVALS
        elif self.quality == 'add_six':
            intervals = ADD_SIX_INTERVALS
        elif self.quality == 'add_nine':
            intervals = ADD_NINE_INTERVALS
        else:
            raise ValueError(f"Unsupported chord quality: {self.quality}")

        return [self.root_midi + interval for interval in intervals]
        