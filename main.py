from cfg import cfg
from mdm import MusicDataManager
from player import MusicPlayer
import threading
from pathlib import Path

mdm = MusicDataManager(Path(cfg.get('path_settings', 'db_path')))
dj = MusicPlayer(Path(cfg.get('path_settings', 'music_path')))

queue = mdm.defaultq(1,4,1,1,1,2)

dj.makelist(queue)
dj.play()
input()
