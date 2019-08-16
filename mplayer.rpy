#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

init -2:
    #$ renpy.music.register_channel("bgm", "music", True, True, True, "bgm/", ".ogg", ".mp3") - Original
    $ renpy.music.register_channel("bgm", "music", True, True, True, "bgm/", ".mp3")

init python:
    mr = MusicRoom(channel='bgm', fadeout=0.5)
