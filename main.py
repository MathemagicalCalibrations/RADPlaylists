from cfgm import cfg
from dbm import Manager

dbpath = cfg.get('path_settings', 'db_path')
dbm = Manager(dbpath)
del dbm
