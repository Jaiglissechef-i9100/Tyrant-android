#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. Time Location - Featured - Scenes
#----- End List -----

label showerup7look:
    hide screen locations
    povi "Maybe I can see something."
    scene showerupstairs 7am shower up
    povi "Oh my god. I can see her. She's so hot."
    povi "But the angle is wrong. I can't see anymore."
    povi "I need to do something! Maybe a second mirror? Or a way to get in?"
    jump showerup

label showerup7talk:
    hide screen locations
    pov "Who's in there?"
    ls "Go away! I'm showering right now."
    pov "..."
    #----- Added in 0.75 Part 2 ----- Done
    if basealefirst == True: #----- added basealefirst == True and removed Love and Corruption points check -----
        jump showerup7extlanding
    else:
        jump showerup

label showerup7extlanding:
    call screen showerup7extlovocormenu

screen showerup7extlovocormenu:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('showerup7extlovocormenu'), Jump('showerup7extlove')) hovered tt.Action ("Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('showerup7extlovocormenu'), Jump('showerup7extcor')) hovered tt.Action ("Corruption [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7listen:
    hide screen locations
    "You listen through the door."
    povi "Someone is showering."
    jump showerup

label showerup20talk:
    hide screen locations
    pov "Who's in there?"
    ls "Go away! The bathroom is occupied."
    pov "..."
    jump showerup

label showerup20listen:
    hide screen locations
    "You listen through the door."
    povi "Someone is in the bathroom. But it's very quiet in there."
    jump showerup

label showerup20look:
    hide screen locations
    povi "Maybe I can see something."
    scene showerupstairs 8pm shower upstairs 002
    povi "[ls] is in there. Is she checking herself out?"
    ls "Fine... very well..."
    scene showerupstairs 8pm shower upstairs 003
    povi "Oh my god! These panties are cute. And her ass too."
    ls "Lalala..."
    $ dtime += 1
    jump showerup

label showerup22talk:
    hide screen locations
    pov "Who's in there?"
    bs "Go away! The bathroom is occupied."
    pov "..."
    jump showerup

label showerup22listen:
    hide screen locations
    "You listen through the door."
    povi "Someone is in the bathroom. But it's very quiet in there."
    jump showerup

label showerup22look:
    hide screen locations
    povi "Maybe I can see something."
    scene showerupstairs 10pm shower upstairs 002
    povi "[bs] is in there. Is she checking herself out?"
    povi "Her nipples are hard too and her tits are so hot."
    scene showerupstairs 10pm shower upstairs 003
    bs "Hmm... hmm..."
    povi "Is she? Oh yeah. She's playing with herself. So hot."
    povi "I wonder where she was before?"
    povi "Maybe with her boyfriend?"
    scene showerupstairs 10pm shower upstairs 004
    bs "Yes... yes, do me harder!"
    povi "She's getting herself off and I can watch. Perfect!"
    if bigsislove or bigsiscorruption >= 30:
        bs "[pov]... Don't stop!"
        povi "Did she just say my name?"
    bs "Hah... hmm... yes!"
    povi "Damn it! She's already done..."
    $ dtime += 1
    jump showerup

label showerup15listen:
    hide screen locations
    "You listen through the door."
    ls "Hah... Hmm..."
    povi "She's in here. But what is she doing?"
    jump showerup

label showerup15look:
    hide screen locations
    povi "Maybe I can see something."
    if lsispronBDSM >= 4:
        scene showerupstairs 3pm 001b
        ls "Hmm... slap me..."
        povi "Damn, she's getting into the BDSM stuff."
        "<slap>"
        ls "Hng..."
        povi "Nice to see that I get her so horny."
        scene showerupstairs 3pm 002b
        ls "Hm... it feels so good... hah... master."
        povi "Damn, she's masturbating and slapping herself."
        ls "Au... hah... <slap>"
        povi "I'm curious if she can get herself off with this stuff."
        scene showerupstairs 3pm 003b
        ls "Aaaahh... hah... hah..."
        if inc == True:
            povi "So hot. My innocent little sister came up with that stuff."
        else:
            povi "So hot. Innocent [ls] came up with that stuff."
        povi "And I got her into it."
        ls "Hnngg..."
        $ lsispronBDSM += 1
        $ su15masBDSM = True
        jump showerup15end
    elif lsispronanal >= 4:
        scene showerupstairs 3pm 001a
        ls "If it slowly gets in..."
        povi "Damn, is she trying to do anal on herself?"
        ls "Hng... careful..."
        povi "I can't believe it!"
        ls "Hmm..."
        scene showerupstairs 3pm 002a
        ls "Ohh... I feel it inside... ah..."
        povi "Damn, she's masturbating and fingering her asshole."
        ls "It feels weird... and... hah... so good."
        povi "I'm curious if she can get herself off with this stuff."
        scene showerupstairs 3pm 003a
        ls "Hah... Aaaahh... Hmm..."
        "She's shaking wildly."
        if inc == True:
            povi "So hot. My innocent little sister came up with that stuff."
        else:
            povi "So hot. Innocent [ls] came up with that stuff."
        povi "And I got her into it."
        ls "Hnngg..."
        $ lsispronanal += 1
        $ su15masanal = True
        jump showerup15end
    elif lsisproninterracial >= 4:
        scene showerupstairs 3pm 001
        ls "Your black dick is rubbing me there, hah..."
        povi "Damn, is she fantasizing about interracial sex?"
        ls "When he sticks it in... hmm..."
        povi "I wonder with whom she's fantasizing?"
        scene showerupstairs 3pm 002
        ls "You're inside! Hmm... so big, hah..."
        povi "Damn, she's masturbating and fantasizing about black men."
        ls "It's so good... hah... deeper..."
        povi "I'm curious if she can get herself off with this stuff."
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            povi "So hot. My innocent little sister came up with that stuff."
        else:
            povi "So hot. Innocent [ls] came up with that stuff."
        povi "And I got her into it."
        ls "Hah... hah... hah..."
        $ lsisproninterracial += 1
        $ su15masinterracial = True
        jump showerup15end
    elif lsisproninc >= 4:
        scene showerupstairs 3pm 001
        ls "Your dick is rubbing me there, hah... big brother..."
        povi "Damn, is she fantasizing about me?"
        ls "When he sticks it in... hmm..."
        povi "I can't believe it! She wants me!"
        scene showerupstairs 3pm 002
        ls "You're inside! Hmm... so big, hah..."
        povi "Damn, she's masturbating and fantasizing about me."
        ls "It's forbidden, but so good... hah... deeper..."
        povi "I'm curious if she can get herself off with this stuff."
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        povi "So hot. My innocent little sister came with that stuff."
        povi "And I got her into it."
        ls "Hah... hah... hah..."
        $ lsisproninc += 1
        $ su15masinc = True
        jump showerup15end
    elif lsispronlesbian >= 4:
        scene showerupstairs 3pm 001
        ls "Yes... hah... lick me there..."
        povi "Damn, who is she thinking of?"
        ls "You're always my best friend... hmm..."
        povi "She has a boyfriend?"
        scene showerupstairs 3pm 002
        ls "Yes, hah... play with your breasts too... ahh..."
        povi "Damn, she's masturbating and fantasizing about another girl."
        ls "Your tongue is so... hah... hah... amazing!"
        povi "I'm curious if she can get herself off with this stuff."
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            povi "So hot. My innocent little sister came up with that stuff."
        else:
            povi "So hot. Innocent [ls] came up with that stuff."
        povi "And I got her into it."
        ls "Hah... hah... hah..."
        $ lsispronlesbian += 1
        $ su15maslesbian = True
        jump showerup15end
    elif lsispronntr >= 4:
        scene showerupstairs 3pm 001
        ls "Yes... hah... look at him, he'll stick it in me... hah..."
        povi "Damn, I don't get it."
        ls "He'll fuck me and you have to watch... hmm..."
        povi "She's fantasizing about ntr'ing someone!"
        scene showerupstairs 3pm 002
        ls "Yes, hah... he's so good and you're the loser [pov]... ahh..."
        povi "Damn, she's masturbating and fantasizing about ntr'ing me. I wonder who fucks her in this?"
        ls "Please stick it deeper... hah... hah..."
        povi "I'm curious if she can get herself off with this stuff."
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            povi "So hot. My innocent little sister came up with that stuff."
        else:
            povi "So hot. Innocent [ls] came up with that stuff."
        povi "And I got her into it."
        ls "Hah... hah... hah..."
        $ lsispronntr += 1
        $ su15masntr = True
        jump showerup15end
    elif lsispronfemdom >= 4:
        scene showerupstairs 3pm 001
        ls "Yes... hah... lick me, slave... hah..."
        povi "Slave? What's going on?"
        ls "Lick me faster... hah or I'll spank you... hmm..."
        povi "She's fantasizing about dominating someone!"
        scene showerupstairs 3pm 002
        ls "No, hah... you aren't allowed to touch your dick... ahh..."
        povi "Damn, she's masturbating and fantasizing about femdom. I wonder who's the slave?"
        ls "Yes, good boy... hah... hah..."
        povi "I'm curious if she can get herself off with this stuff."
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            povi "So hot. My innocent little sister came up with that stuff."
        else:
            povi "So hot. Innocent [ls] came up with that stuff."
        povi "And I got her into it."
        ls "Hah... hah... hah..."
        $ lsispronfemdom += 1
        $ su15masfemdom = True
        jump showerup15end
    elif lsisprongangbang >= 4:
        scene showerupstairs 3pm 001
        ls "Yes... hah... stick it in... hah..."
        povi "What's going on?"
        ls "Go on, the others are waiting... hah... hmm..."
        povi "She's fantasizing about getting gangbanged!"
        scene showerupstairs 3pm 002
        ls "No, hah... wait a second... hm... when he's done... ahh..."
        povi "Damn, she's masturbating and fantasizing about group sex."
        ls "Yes, another one? Hah... hah..."
        povi "I'm curious if she can get herself off with this stuff."
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            povi "So hot. My innocent little sister came up with that stuff."
        else:
            povi "So hot. Innocent [ls] came up with that stuff."
        povi "And I got her into it."
        ls "Hah... hah... hah..."
        $ lsisprongangbang += 1
        $ su15masgangbang = True
        jump showerup15end
    else:
        scene showerupstairs 3pm 001
        ls "Yes... hah... your dick is rubbing me there... hah..."
        povi "She's masturbating."
        ls "Please stick it in... hah... hmm..."
        povi "She's fantasizing about getting fucked!"
        scene showerupstairs 3pm 002
        ls "Yes, hah... deeper... ahh..."
        povi "Damn, she's masturbating and fantasizing about getting fucked."
        ls "You're so big, hah... faster..."
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            povi "So hot. My innocent little sister came up with that stuff."
        else:
            povi "So hot. Innocent [ls] came up with that stuff."
        ls "Hah... hah... hah..."
        $ su15masnormal = True
        jump showerup15end

label showerup15end:
    povi "It's better if I leave now. I can use this \"secret\" another time."
    scene black
    $ lilsisrelationship += 1
    $ dtime += 1
    jump showerup
