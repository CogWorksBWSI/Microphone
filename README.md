# Microphone

Provides a simple interface for configuring and utilizing a microphone in Python.

# Installation Requirements
Anaconda with Python 3.{5, 6}, portaudio (Mac & Ubuntu only) & pyaudio. See following sections for installation instructions.

### Installing Required Packages (Windows)
```shell
pip install pyaudio
```


### Installing Required Packages (Mac OSX)
There are a few things to consider when installing this project for OS X.

First, the `portaudio` library must be installed before running `pip install pyaudio`.

This can be done with [Homebrew](https://brew.sh/) using
 - `brew install portaudio`

or MacPorts using
  - `sudo port install portaudio`

it may also be available through conda, although this is not verified (there seems to be issues with this method..)
  - `conda install -c anaconda portaudio=19`

Having installed `portaudio`, proceed as follows:
```shell
pip install pyaudio
```

### Installing Required Packages (Debian/Ubuntu)
```shell
sudo apt-get install python-pyaudio python3-pyaudio
```


# Installing this package
Once you have installed the dependencies, clone this repository, navigate to it, and run

```shell
python setup.py develop
```

# Configuring Your Microphone
Navigate to Microphone/microphone and run:
```shell
python configure_input.py
```
and follow the selection prompt. This will save your microphone preference for future use.

# Testing Your Microphone
Navigate to Microphone and run:
```shell
python test_input.py
```
This should record and play back a brief audio clip using the microphone selected during configuration.

# Recording Audio
```python
from microphone import record_audio

# Record 10 seconds of audio
byte_encoded_signal, sampling_rate = record_audio(10)
```

# Playing Audio
```python
from microphone import play_audio

# Play 10 seconds of audio
play_audio(byte_encoded_signal, 10)
```
