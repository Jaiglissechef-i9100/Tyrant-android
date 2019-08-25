
init -2:
    $ renpy.music.register_channel("bgm", "music", True, True, True, "bgm/", ".ogg", ".mp3")


init python:
    mr = MusicRoom(channel='bgm', fadeout=0.5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
