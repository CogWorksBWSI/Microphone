import pyaudio
from contextlib import contextmanager
import configparser
import os
from pathlib import Path


_path = Path(os.path.dirname(os.path.abspath( __file__ )))
# buffer size
CHUNK = 1024

# 16-bit audio
WIDTH = 2

# mono
CHANNELS = 1

RATE = 44100


def load_ini():
    """ Returns the saved device from config.ini or `None`

            Returns
            -------
            Union[dict, None]
                {name : device name,
                 index: device index from config prompt}"""
    config = configparser.ConfigParser()

    # This returns an empty array if no config file was found
    if config.read(str(_path / 'config.ini')) != []:
        return config['input device']
    else:
        return None


@contextmanager
def open_input_device(savedDevice=None):
    """ Open an input audio stream from the saved mic as a context.
        Leaving the context will close the input stream and the device.

        Parameters
        ----------
        savedDevice : Optional[dict]
            The log for the saved recording device.

        Yields
        ------
        pyaudio.Stream
            Input stream of bytes.
        """
    p = pyaudio.PyAudio()

    # try loading from config file
    if savedDevice is None:
        savedDevice = load_ini()

    # use portaudio to detect default device
    if savedDevice is None:
        print("No microphone configuration file found, attempting to find default device..")
        defaultInfo = p.get_default_input_device_info()
        deviceIndex = defaultInfo['index']
        devicename = defaultInfo['name']
    else:
        deviceIndex = int(savedDevice['index'])
        devicename = savedDevice['name']

    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=deviceIndex,
                    frames_per_buffer=CHUNK)

    print("Using input device '{}'".format(devicename))
    try:
        yield stream
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Recording ended")


@contextmanager
def open_output_device():
    """ Open an output audio stream as a context.
        Leaving the context will close the output stream and the device.

        Yields
        ------
        pyaudio.Stream
            Output stream to write to.
        """
    p = pyaudio.PyAudio()
    outputStream = p.open(format=p.get_format_from_width(WIDTH),
                          channels=CHANNELS,
                          rate=RATE,
                          output=True,
                          frames_per_buffer=CHUNK)

    try:
        yield outputStream
    finally:
        outputStream.stop_stream()
        outputStream.close()
        p.terminate()
