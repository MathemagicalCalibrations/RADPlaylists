from cfg import cfg
from mdm import MusicDataManager

dbpath = cfg.get('path_settings', 'db_path')
mdm = MusicDataManager(dbpath)
del mdm
