


label bsis78look:
    hide screen locations
    if dtime == 14:
        jump bsis14look
    else:
        pov "{i}Maybe I can see something?{/i}"
        scene black
        pov "{i}Damn it's no use.{/i}"
        jump bsisroom

label bsis78open:
    hide screen locations
    "You try to open the door."
    pov "{i}Damn, it's locked.{/i}"
    jump bsisroom

label bsis78listen:
    hide screen locations
    "You listen through the door."
    pov "{i}Nothing. She must still be sleeping.{/i}"
    jump bsisroom



label bsis14look:
    hide screen locations
    if bigsisroom2pm == False:
        scene bigsisroom 2pm 002
        pov "{i}Oh, I can see her. But what are they doing? Are they fighting?{/i}"
        martin "You're wrong! There is no other girl!"
        bs "Liar!"
        martin "There maybe other groupies, but you're my only groupie!"
        bs "I don't believe that shit!"
        pov "{i}Oh, good to know about that.{/i}"
        pov "{i}But I better leave, if she catches me now spying on her, uh... oh...{/i}"
        $ dtime += 1
        $ bigsisroom2pm = True
        jump bsisroom
    else:
        jump bsis142look
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
