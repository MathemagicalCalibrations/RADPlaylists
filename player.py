import vlc

class MusicPlayer:
    def __init__(self, folder):
        self._folder = folder
        self._list = None
        self._index = None
        self._player = None
        self._events = None
        self._is_playing = False

    def makelist(self, queue):
        self._list = vlc.MediaList()
        for song in queue:
            print(song)
            self._list.add_media(self._folder / song[1])

    def next(self):
        self._index += 1
        if self._index < self._list.count():
            print(self._index)
            self._player = vlc.MediaPlayer()
            self._player.set_media(self._list.item_at_index(self._index))
            self._events = self._player.event_manager()
            self._events.event_attach(vlc.EventType.MediaPlayerEndReached, self.done)
            print(self._player.get_length())
            self._player.play()
        else:
            print("all done")

    def done(self, a):
        print(self._player.is_playing())
        self.next()

    def play(self):
        self._index = -1
        print(self._list.count())
        self.next()

    def playsong(self, songpath):
        self._player.set_mrl(mrl=self._folder / songpath)
        self._player.play()
