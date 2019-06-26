from argparse import Namespace
from pathlib import Path
import os

path = Path(os.path.dirname(os.path.abspath( __file__ )))

settings = Namespace()

# buffer size
settings.chunk = 1024

# 16-bit audio
settings.width = 2


# mono
settings.channels = 1

# sampling rate
settings.rate = 44100