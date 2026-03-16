"""
Users format their scripts by defining track functions decorated with @register_track.
"""

from music_engine.engine import Controller
import inspect
import atexit

#Global controller instance
controller = Controller()

track_proxies = {}
_finalised = False
_last_track_count = 0  # Track where we left off

class TrackProxy:
    def __init__(self, name):
        self.name = name
        self.play_requests = []
        self.export_requests = []
        self.track_obj = None

    def play(self, tempo=120):
        self.play_requests.append(tempo)

    def export_midi(self, filename="output.mid", tempo=120):
        self.export_requests.append((filename, tempo))

#Track registration decorator
def register_track(func):
    """Decorator to register a track setup function"""
    params = inspect.signature(func).parameters
    track_name = list(params.keys())[0]

    controller._track_functions.append(func)

    proxy = TrackProxy(track_name)
    track_proxies[track_name] = proxy

    globals()[track_name] = proxy

    return func


def _finalise():
    """Handle any remaining track operations at program exit"""
    global _last_track_count
    
    #Only finalize tracks that haven't been played yet
    track_functions = controller._track_functions[_last_track_count:]
    
    if not track_functions:
        return  # All tracks already handled
    
    #Clear state for remaining tracks
    controller.tracks = []
    controller._sequences = {}
    
    for i, track_func in enumerate(track_functions):
        params = inspect.signature(track_func).parameters
        track_name = list(params.keys())[0] if params else f"track_{i}"

        track_obj = controller.new_track(track_name)
        track_func(track_obj)

        if track_name in track_proxies:
            track_proxies[track_name].track_obj = track_obj

    for name, proxy in track_proxies.items():
        track = proxy.track_obj
        if track is None:
            continue

        for tempo in proxy.play_requests:
            controller.play(track=track, tempo=tempo)

        for filename, tempo in proxy.export_requests:
            controller.export_midi(filename, tempo=tempo, track=track)
        
        #Clear requests after execution
        proxy.play_requests.clear()
        proxy.export_requests.clear()


def play_polyphonic(tempo=120):
    """Play only tracks registered in this section polyphonically (simultaneously)"""
    global _last_track_count
    
    #Only finalize newly registered tracks since the last call
    track_functions = controller._track_functions[_last_track_count:]
    _last_track_count = len(controller._track_functions)
    
    if not track_functions:
        return  # No new tracks to play
    
    #Clear state for this section's tracks only
    controller.tracks = []
    controller._sequences = {}
    
    tracks_by_name = {}
    
    for i, track_func in enumerate(track_functions):
        params = inspect.signature(track_func).parameters
        track_name = list(params.keys())[0] if params else f"track_{i}"

        track_obj = controller.new_track(track_name)
        track_func(track_obj)

        tracks_by_name[track_name] = track_obj

        if track_name in track_proxies:
            track_proxies[track_name].track_obj = track_obj

    #Play the newly registered tracks
    controller.play_polyphonic(tempo=tempo)


def export_midi(filename="output.mid", tempo=120):
    """Export all tracks to a MIDI file"""
    # Add .mid extension if not present
    if not filename.endswith('.mid'):
        filename += '.mid'
    
    controller.export_midi(filename=filename, tempo=tempo)


atexit.register(_finalise)
