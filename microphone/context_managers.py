import pyaudio
from contextlib import contextmanager
from typing import Optional

from microphone.configure_input import load_ini
from microphone.config import settings


@contextmanager
def open_input_device(saved_device: Optional[dict] = None) -> pyaudio.Stream:
    """ Open an input audio stream from the saved mic as a context.
    Leaving the context will close the input stream and the device.

    Parameters
    ----------
    saved_device : Optional[dict]
        The log for the saved recording device.

    Yields
    ------
    pyaudio.Stream
        Input stream of bytes."""
    p = pyaudio.PyAudio()

    # try loading from config file
    if saved_device is None:
        saved_device = load_ini()

    # use portaudio to detect default device
    if saved_device is None:
        print("No microphone configuration file found, attempting to find default device..")
        defaultInfo = p.get_default_input_device_info()
        deviceIndex = defaultInfo['index']
        devicename = defaultInfo['name']
    else:
        deviceIndex = int(saved_device['index'])
        devicename = saved_device['name']

    stream = p.open(format=p.get_format_from_width(settings.width),
                    channels=settings.channels,
                    rate=settings.rate,
                    input=True,
                    input_device_index=deviceIndex,
                    frames_per_buffer=settings.chunk)

    print("Using input device '{}'".format(devicename))
    try:
        yield stream
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Recording ended")


@contextmanager
def open_output_device() -> pyaudio.Stream:
    """ Open an output audio stream as a context.
    Leaving the context will close the output stream and the device.

    Yields
    ------
    pyaudio.Stream
        Output stream to write to."""
    p = pyaudio.PyAudio()
    output_stream = p.open(format=p.get_format_from_width(settings.width),
                           channels=settings.channels,
                           rate=settings.rate,
                           output=True,
                           frames_per_buffer=settings.chunk)
    try:
        yield output_stream
    finally:
        output_stream.stop_stream()
        output_stream.close()
        p.terminate()
