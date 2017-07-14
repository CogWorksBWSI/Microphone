# Microphone

Provides a simple interface for configuring and utilizing a microphone in Python.

# Installation

Clone this repository, navigate to it, and run

```shell
python setup.py develop
```

# Configuring Your Microphone
Navigate to Microphone/microphone and run:
```shell
python configure_input.py
```
and follow the selection prompt. This will save your microphone preference for furture use.

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