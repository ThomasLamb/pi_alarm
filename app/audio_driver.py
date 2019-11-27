import os

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from app import app

class AudioDriver(object):
    """
    Class for controlling audio playback.
    """

    def __init__(self, audiofile=None):
        if not audiofile:
            self.audiofile = app.config['AUDIOFILE']

    def get_audiofile(self):
        return self.audiofile

    def set_audiofile(self, audiofile):
        try:
            self.audiofile = audiofile
            return True
        except Exception as exc:
            print("Failed to set audiofile: %s" % exc)
            return False

    def on(self):
        print("Turning audio on")
        os.system("mpg123 %s" % self.audiofile)

    def off(self):
        print("Turning audio off... um...")

