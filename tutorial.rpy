#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label tutorial:
    window hide
    nvl clear
    scene black
    "You lay in bed with your thoughts."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    pov "Should I play along? Or should I rebel against it?"
    if inc == True:
        pov "And what if I get pleasure out of it. Being the king when dad is away and taking what I want."
        pov "Even from mom or my sisters! They have to play along."
    else:
        pov "And what if I get pleasure out of it. Being the king when Bruce is away and taking what I want."
        pov "Even from [mother] or her daughters! They have to play along."
    scene tut corruption
    pov "I could corrupt them in every way I want."
    pov "I just need to collect corruption points and have a good relationship with them."
    scene tut love
    pov "Or I try to help them get back their purity like they was in the past."
    pov "For that I need to collect love points and also have good relationships with them."
    if NTR == True:
        scene tut NTR
        pov "But I must also be careful or I could lose them to other men."
        pov "Or maybe that is something I want or I just don't care?"
        pov "Or I could even take advantage of their illicit affairs?"
    scene tut death
    pov "I can also make plans to get rid of my rivals or people I just don't like."
    pov "Kill everyone! Until I'm all alone with all the women, haha."
    pov "As things get worse will I be able to endure?"
    pov "Maybe I'll just punish Bruce and they'll leave us alone."
    pov "I'll have to find out more before I decide what to do with him."
    pov "When I play along it benefits him, but I'll need to wait for the right time to stop playing along."
    hide black
    $ dtime = 7
    $ persistent.end = "intro"
    show screen hud
    show screen phone
    show screen dlhs
    jump lroom
