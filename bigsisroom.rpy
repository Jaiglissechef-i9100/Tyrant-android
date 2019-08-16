#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 2pm BigSisRoom - Cassandra, Martin - Look, Listen
#----- End List -----

label bsis78look:
    hide screen locations
    if dtime == 14:
        jump bsis14look
    else:
        povi "Maybe I can see something?"
        scene black
        povi "Damn, it's no use."
        jump bsisroom

label bsis78open:
    hide screen locations
    "You try to open the door."
    povi "Damn, it's locked."
    jump bsisroom

label bsis78listen:
    hide screen locations
    if bigsisroom2pm == False:
        "You listen through the door."
        povi "Are they fighting?"
        martin "You're way off base here! There is no other girl!"
        bs "Liar!"
        martin "There maybe other groupies, but you're my only girlfriend!"
        bs "I don't believe that shit!"
        povi "This might be useful later."
        povi "I better leave, if she catches me spying on her she'll turn that anger on me."
        $ bigsisroom2pm = True
        jump bsisroom
    else:
        jump bsis142listen

label bsis14look:
    hide screen locations
    if bigsisroom2pm == False:
        scene bigsisroom 2pm 002
        povi "Oh, I can see her. But what are they doing? Are they fighting?"
        martin "You're way off base here! There is no other girl!"
        bs "Liar!"
        martin "There maybe other groupies, but you're my only girlfriend!"
        bs "I don't believe that shit!"
        povi "This might be useful later."
        povi "I better leave, if she catches me spying on her she'll turn that anger on me."
        $ bigsisroom2pm = True
        jump bsisroom
    else:
        jump bsis142look
