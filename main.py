from cfg import cfg
from mdm import MusicDataManager
from player import MusicPlayer
import threading
from pathlib import Path

mdm = MusicDataManager(Path(cfg.get('path_settings', 'db_path')))
dj = MusicPlayer(Path(cfg.get('path_settings', 'music_path')))

queue = mdm.defaultq(1,1,1,1,1,5)

dj.playsong(queue[1][1])
input()
