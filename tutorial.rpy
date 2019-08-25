
label tutorial:
    window hide
    nvl clear
    scene black
    "You lay in bed with your thoughts."
    if gamemusic == True:
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
    pov "Or I try to get them back to their purity like they was in the past."
    pov "For that I need to collect love points and also have good relationships with them."
    if NTR == True:
        scene tut NTR
        pov "But I must also be aware or I could loose them to other men."
        pov "Or maybe is that something I want or I just don't care?"
        pov "Or even take the option to take benefits from their relationships?"
    scene tut death
    pov "I can also make plans to get rid of my rivals or people I just don't like."
    pov "Kill everyone until I'm all alone with all the women, haha."
    pov "And when it gets even worse can I endure this situation?"
    pov "Maybe just Bruce gets punishment and they'll leave us alone."
    pov "I'll have to find out more before I decide what to do with him."
    pov "When I play along it's fine for him, but when I don't I'll have to stay patient so he doesn't find out."

    $ dtime = 7
    $ persistent.end = "intro"
    show screen hud
    show screen phone
    show screen dlhs
    hide black
    jump lroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
