import vlc

class MusicPlayer:
    def __init__(self, folder):
        self._folder = folder
        self.player = vlc.MediaPlayer()

    def playsong(self, songpath):
        self.player.set_mrl(mrl=self._folder / songpath)
        self.player.play()
