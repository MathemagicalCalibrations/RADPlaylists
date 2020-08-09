from configparser import ConfigParser

cfg = ConfigParser()

#verifies that settings.ini exists, if not creates it
try:
    t = open('settings.ini', 'r')
    t.close()
except Exception as e:
    print(e)
    print("Attempting to create settings.ini")
    try:
        cfg.add_section('path_settings')
        cfg.set('path_settings', 'db_path', "music.db")
        i = input("Where are the music files?")
        cfg.set('path_settings', 'music_path', i)
        with open('settings.ini', 'w+') as cfgfile:
            cfg.write(cfgfile)
    except Exception as e:
        print(e)

cfg.read('settings.ini')
