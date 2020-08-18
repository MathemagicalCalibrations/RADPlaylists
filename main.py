from cfg import cfg
from mdm import MusicDataManager
from player import MusicPlayer
import threading
from pathlib import Path

mdm = MusicDataManager(Path(cfg.get('path_settings', 'db_path')))
dj = MusicPlayer(Path(cfg.get('path_settings', 'music_path')))

def simple(e, s, g, m, d, a):
    return mdm.simpleq(e, s, g, m, d, a)

def marked():
    return mdm.marked()

def mark(id):
    mdm.mark(id)

def update(id, e, s, g, m, d):
    mdm.update(id, e, s, g, m, d)

def addsong(path, length, e, s, g, m, d):
    mdm.add(path, length, e, s, g, m, d)

def deletesong(id):
    mdm.delete(id)

def index():
    return dj.getindex()

def play(q = None):
    if q != None:
        dj.setqueue(q)
    dj.start()

def pause():
    dj.pause()

def stop():
    dj.stop()

def skip():
    dj.stop()
    dj.play(1)
