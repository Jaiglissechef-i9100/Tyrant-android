
init -2:
    $ renpy.music.register_channel("bgm", "music", True, True, True, "bgm/")


init python:
    mr = MusicRoom(channel='bgm', fadeout=0.5)