from distutils.core import setup
from setuptools import find_packages

try:
    import pyaudio
except ImportError:
      print("Warning: `pyaudio` must be installed in order to use `microphone`")

setup(name='microphone',
      version='1.0',
      description='Provides simple interface for recording audio',
      author='Ryan Soklaski (@LLrsokl)',
      author_email="ry26099@mit.edu",
      packages=find_packages(),
      license="MIT"
      )
