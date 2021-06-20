# Microphone

Provides a simple interface for configuring and utilizing a microphone in Python.

This package has been tested using Python 3.7, using conda 4.7.5, on both Mac and Windows 10.

# Installing pyaudio (required dependency)
```shell
conda install pyaudio
```

# Installing this package
Once you have installed the dependencies, clone this repository, navigate to it, and run

```shell
pip install -e .
```
It is important that you use this `develop` install option, as the microphone configuration requires that
this package is installed in-place.

# Configuring Your Microphone
Navigate to Microphone/microphone and run:
```shell
python configure_input.py
```
and follow the selection prompt. This will save your microphone preference for future use. The resulting configuration file will be saved to `Microphone/microphone/config.ini`. You can edit [this file](https://github.com/CogWorksBWSI/Microphone/blob/master/microphone/config.py) to change the recording settings (e.g. the sampling rate) used to sampled audio from your microphone.

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
