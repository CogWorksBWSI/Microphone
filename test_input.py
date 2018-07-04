from microphone.context_managers import open_input_device, open_output_device
from microphone.configure_input import load_ini
from microphone.__init__ import record_audio, play_audio

""" Running this script will test the configured microphone - it will record
    audio using the device for RECORD_SECONDS amount of time, and then play back
    the audio. """

RECORD_SECONDS = 5

print('Recording audio for {} seconds... (if this hangs, choose a different input device)'.format(RECORD_SECONDS))
frames, _RATE = record_audio(RECORD_SECONDS)
print('Finished recording')

# Playback the recorded digital signal
print('Playing back recording...')
play_audio(frames, RECORD_SECONDS)
print('Finished playback')
