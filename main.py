from dbm import Manager

dbpath = 'music.db'

dbm = Manager(dbpath)
del dbm
