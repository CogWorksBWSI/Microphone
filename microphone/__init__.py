""" This package contains utilities for configuring, saving, and testing a microphone.

    Running the script `configure_input.py` will prompt a user to choose their microphone.
    This will save a file to songfp/mic_config/config.ini

    `configure_input.load_ini()` will return the name of the saved device from the config.ini file"""


from .context_managers import open_input_device as _open_input_device
from .context_managers import open_output_device as _open_output_device

""" Provides basic functionality for recording audio from a saved device, and
    playing the audio back."""

__all__ = ["record_audio",
           "play_audio"]

# buffer size
_CHUNK = 1024

# 16-bit audio
_WIDTH = 2

# mono
_CHANNELS = 1

_RATE = 44100


def record_audio(time, device=None):
    """ Record input stream to in-memory list.

        Parameters
        ----------
        time : float
            The amount of time, in seconds, to record for.

        device : Optional[Dict[str, str]]
            {name : device name,
            index: device index from config prompt}

        Returns
        -------
        Tuple[List[bytes], int]
            The bytes from the recorded signal, and the sample rate."""
    with _open_input_device(device) as mic:
        frames = []
        for i in range(0, int(_RATE / _CHUNK * time)):
            data = mic.read(_CHUNK)
            frames.append(data)
    return frames, _RATE


def play_audio(frames, time):
    """ Play an audio stream.

        Parameters
        ----------
        stream : pyaudio.Stream
            The output stream.

        frames : List[bytes]
            The bytes to write to the output stream.

        time : float
            The amount of time to play back (in seconds)"""
    with _open_output_device() as stream:
        for i in range(0, int(_RATE / _CHUNK * time)):
            stream.write(frames[i], _CHUNK)
