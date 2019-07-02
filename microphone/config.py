from argparse import Namespace
from pathlib import Path

path = Path(__file__).resolve().parent

settings = Namespace()

# buffer size
settings.chunk = 1024

# 16-bit audio
settings.width = 2


# mono
settings.channels = 1

# sampling rate
settings.rate = 44100
