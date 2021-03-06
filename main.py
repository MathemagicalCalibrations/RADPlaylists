from cfg import cfg
from mdm import MusicDataManager
from player import MusicPlayer
import threading
from pathlib import Path

mdm = MusicDataManager(Path(cfg.get('path_settings', 'db_path')))
dj = MusicPlayer(Path(cfg.get('path_settings', 'music_path')))
q = []

def writequeue(queue):
    global q
    q = queue

def queue(amount, et, st, gt, mt, dt, en = 0, ex = 5, ew = 1, sn = 0, sx = 5, sw = 1, gn = 0, gx = 5, gw = 1, mn = 0, mx = 5, mw = 1, dn = 0, dx = 5, dw = 1):
    writequeue(mdm.queue(et, en, ex, ew, st, sn, sx, sw, gt, gn, gx, gw, mt, mn, mx, mw, dt, dn, dx, dw, amount))

def marked():
    writequeue(q = mdm.marked())

def getqueue():
    for song in q:
        print(song)

def mark(id = None):
    if id == None:
        id = q[index()][0]
    mdm.mark(id)

def update(id, e, s, g, m, d):
    mdm.update(id, e, s, g, m, d)

def addsong(path, e, s, g, m, d):
    mdm.add(path, e, s, g, m, d)

def deletesong(id):
    confirm = input("".join(("Are you sure you want to delete song entry #", str(id), "? (y/N) ")))
    if confirm == 'y' or confirm == 'Y':
        mdm.delete(id)
    else:
        print("Aborted")

def index():
    return dj.getindex()

def current():
    i = index()
    if i == None:
        print("No song is playing \n")
        return
    return q[index()]

def play():
    dj.setqueue(q)
    dj.start()

def restart():
    dj.start()

def pause():
    dj.pause()

def stop():
    dj.stop()

def skip(i = 1):
    dj.stop()
    dj.play(i)

def loop():
    if dj.looptoggle():
        print("Queue looping enabled")
    else:
        print("Queue looping disabled")

def length(i = None):
    if i == None:
        i = dj.getindex()
    return dj.getlength(i)
