import vlc

class MusicPlayer:
    def __init__(self, folder):
        self._folder = folder
        self._queue = None
        self._index = None
        self._player = vlc.MediaPlayer()
        self._events = None
        self._is_playing = False

    def.getindex(self):
        return self._index

    def setqueue(self, queue):
        self._queue = []
        for song in queue:
            self._queue.append(self._folder / song[1])

    def next(self):
        self._index += 1
        if self._index < len(self._queue):
            self._player = vlc.MediaPlayer(self._queue[self._index])
            self._events = self._player.event_manager()
            self._events.event_attach(vlc.EventType.MediaPlayerEndReached, self.done)
            print(self._player.get_length())
            self._player.play()
        else:
            print("The queue has ended. You can play it again or change it.")

    def done(self, a):
        self.next()

    def play(self):
        self._index = -1
        self.next()

    def pause(self):
        self._player.pause()

    def stop(self):
        self._player.stop()
