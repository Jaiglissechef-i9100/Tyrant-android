#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. Time Location - Featured - Scenes
#----- End List -----

label tanningenter:
    hide screen townl
    povi "Let's see what I can do here."
    scene town tanning desk
    if momrelationship < 6 and momntr == True and NTR == True and frankfirstmeet == False and vipntrfrank == True:
        povi "That's the asshole that spanked mom!"
        jump frankunknown
    if frankfirstmeet == False:
        povi "Great, this guy looks like he's mad."
        jump frankunknown
    else:
        pov "Hello Frank."
        jump frankknown

label frankknown:
    scene town tanning desk
    frank "So ready to work or get a tan?"
    jump getatan

label tanningwork:
    hide screen townl
    scene town tanning desk
    pov "I'm looking to earn some money. Could I get a job here?"
    povi "Not much of a choice here, I need money and I haven't found anything better yet..."
    "Man" "Yes you can boy, you'll get 50$ per hour."
    "Man" "I'll give you the premium wage... if you can keep your mouth shut while you work!"
    pov "Yes sir..."
    povi "What an asshole!"
    "Man" "My name is Frank."
    pov "I'm [pov]."
    frank "OK. You can start work immediately if you want to."
    $ tanningjob = True
    jump frankknown

label frankunknown:
    scene town tanning desk
    "Man" "What do you want?"
    pov "Oh wow. No need to be so angry all the time."
    "Man" "I have no time for idiots strolling around in my studio."
    pov "Maybe I want to spent some money here?"
    povi "What an asshole!"
    "Man" "It's 20$ per hour to tan!"
    pov "Oh, okay."
    jump getatan

label tanningwork1:
    scene town tanning ts work
    "You work for one hour cleaning the sunbeds and rooms."
    $ money += 50
    $ dtime += 1
    jump town

label getatan:
    scene town tanning desk2
    call screen getatan1

screen getatan1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if money >= 20:
            imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('getatan1'), Jump('getatanyes')) hovered tt.Action ("Buy one hour") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('getatan1'), Jump('getatanno')) hovered tt.Action ("Don't buy") focus_mask True
        if tanningjob == False:
            imagebutton auto "gui/icons/icon_question_%s.png" action (Hide('getatan1'), Jump('tanningwork')) hovered tt.Action ("Ask for a job") focus_mask True
        if tanningjob == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('getatan1'), Jump('tanningwork1')) hovered tt.Action ("Work (+1 hour/+50$)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label getatanyes:
    pov "I want to buy an hour."
    frank "Okay. You can choose a room. The ones with open doors are not occupied."
    pov "Good. Thank you."
    frank "..."
    $ money -= 20
    if dtime == 16 and irinafirstmeet == True:
        jump tanning4pm
    if dtime == 17:
        jump tanning5pm
    else:
        jump tan1

label tan1:
    scene black
    "You get yourself a tan for an hour."
    $ dtime += 1
    jump town

label getatanno:
    pov "I've reconsidered. I won't be doing business today with angry ass men, good day sir!"
    frank "Then how about you leave my studio now?"
    pov "...fine, you win this time..."
    jump town

label tanning4pm:
    scene town tanning 4pm 001
    irina "Can I have the sunscreen with the orange scent please?"
    $ irinarelationship += 1
    if frankfirstmeet == True:
        frank "Sure."
    else:
        "Man" "Sure."
    scene town tanning 4pm 002
    irina "Oh hi [pov]!"
    pov "Hello, [irina]"
    irina "What are you doing here?"
    pov "The same as your doing. Getting some more sun."
    scene town tanning 4pm 003
    irina "Oh, then we have something in common, that's great."
    pov "Yes."
    if inc == True:
        irina "Your sister is also here."
        pov "[bs]?"
        irina "Haha yes. I barely know your little sister."
    else:
        irina "[bs] is also here."
    if frankfirstmeet == True:
        frank "Hey!"
    else:
        "Man" "Hey!"
    scene town tanning 4pm 004
    irina "Huh?"
    if frankfirstmeet == True:
        frank "Your sunscreen."
    else:
        "Man" "Your sunscreen."
    irina "Oh sure."
    scene town tanning 4pm 005
    irina "You should really calm down, Frank. You'll get heart problems with all your stress."
    if frankfirstmeet == False:
        povi "So this is Frank."
        $ frankfirstmeet = True
    frank "You got what you want, so don't tell me how to live my life!"
    irina "Okay, if you say so."
    scene town tanning 4pm 006
    irina "Always a bad mood, haha."
    irina "..."
    irina "I... I need to go now. I have to put this on."
    pov "Okay... sure you don't want any help? I wouldn't want you to miss a spot."
    irina "Maybe..."
    povi "Please oh please oh please oh please!"
    irina "See you [pov]."
    povi "Damn it!"
    pov "Bye."
    scene town tanning 4pm 007
    irina "<giggle>"
    povi "Oh, she's teasing me."
    if irinarelationship >= 6 or NTR == False:
        jump tan1
    scene town tanning 4pm 008
    frank "Are you two done yet?"
    pov "Oh sure."
    frank "Good then how about you get your tan now and excuse me."
    pov "..."
    scene town tanning 4pm 009 ntr
    povi "What? Where's he going? Isn't that [irina]'s room?"
    "You follow him."
    povi "I Have a really bad feeling about this."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    jump tanningsalon4pmntrlanding

label tanningsalon4pmntrlanding:
    scene town tanning 4pm 009 ntr
    call screen checkdarkerpaths_irina
    jump tanning4pmcont

label tanning4pmcont:
    scene town tanning 4pm 010 ntr
    povi "No..."
    frank "Now my mood is getting much better with your mouth stuffed."
    irina "Hmm... <suck>"
    povi "No! Not with that old prick."
    frank "Yes, earn your tanning sessions, little slut."
    irina "Hmm... hmm..."
    frank "Argh! Let me mark you!"
    scene town tanning 4pm 011 ntr
    frank "Ahh... hah..."
    irina "Hmm..."
    frank "You did good. Now you can enjoy your tanning."
    if irina_voyeur == True:
        irina "Thank you, daddy. <giggle>"
        povi "Wait! He isn't her real dad, is he? Either way it's still hot!"
    elif irina_ntr == True:
        irina "Thank you, daddy. <giggle>"
        povi "Wait! He isn't her real dad, is he? This is horrible!"
    elif irina_revenge == True:
        irina "Yes... sir."
        povi "That asshole! He's forcing her!"
    else:
        irina "Thank you, daddy."
        povi "He isn't her real dad, is he? I mean either way, I'd hit that."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ dtime += 1
    $ tanning4pmntrfirst = True # ----- Added in 0.6.5 -----
    jump town

label tanning5pm:
    mom "So I explained it to him."
    "Woman" "Oh yes, he's so stupid sometimes."
    povi "Wait, isn't that...?"
    scene town tanning 5pm 001
    jump t5pm

label t5pm:
    scene town tanning 5pm 001
    call screen t5pm1

screen t5pm1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('t5pm1'), Jump('t5pmtalk')) hovered tt.Action ("Talk to them") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('t5pm1'), Jump('t5pmignore')) hovered tt.Action ("Ignore them") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label t5pmignore:
    if inc == True:
        povi "I don't want to talk to mom right now."
    else:
        povi "I don't want to talk to [mother] right now."
    jump tan1

label t5pmtalk:
    if inc == True:
        pov "Hi mom!"
    else:
        pov "Hi, [mother]!"
    scene town tanning 5pm 002
    mom "Oh hey [pov]!"
    if susanfirstmeet == True:
        susan "Hmm..."
    else:
        "Woman" "Hmm..."
    mom "What a surprise to meet you here."
    pov "Why, I'm here to get a tan too."
    mom "Haha, sure."
    scene town tanning 5pm 003
    mom "Oh, this is my good friend..."
    if susanfirstmeet == False:
        $ susanname = renpy.input(_("Her name is...")) or _("Susan")
        $ susanname = susanname.strip()
        if susanname == "":
            $ susanname = "Susan"
    $ susanfirstmeet = True
    susan "Hello."
    if inc == True:
        mom "This is my son, [pov]."
    else:
        mom "This is my [pov], he's living with us."
    mom "And [susan] is our neighbor and a very good friend."
    pov "Hello, nice to meet you."
    $ momrelationship += 1
    $ susanrelationship += 1
    jump t5pmsm

label t5pmsm:
    scene town tanning 5pm 003
    call screen t5pmsm1

screen t5pmsm1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('t5pmsm1'), Jump('t5pmlove')) hovered tt.Action ("Shake her hand [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('t5pmsm1'), Jump('t5pmcor')) hovered tt.Action ("Hug her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label t5pmlove:
    scene town tanning 5pm 004a
    if inc == True:
        pov "I'm [pov]. It's nice to meet a friend of mom's."
    else:
        pov "I'm [pov]. It's nice to meet a friend of [mother]'s."
    susan "Me too."
    $ susanlove += 1
    scene town tanning 5pm 005a
    if inc == True:
        susan "You're right, your son really has some good manners."
    else:
        susan "You're right, he has really some good manners."
    pov "Thank you."
    mom "Yes, I'm so proud of him."
    susan "Maybe we should have tea some time together?"
    mom "Oh sure. That would be nice."
    mom "Excuse me a moment."
    scene town tanning 5pm 006a
    susan "I really meant it. You should come over some time so we can have fun."
    susan "Fun for adults. I know you want too."
    povi "What?"
    "You look away to escape the weird talk."
    if momrelationship < 6 and momntr == True and NTR == True:
        jump tanningsalonntrlanding2
    else:
        jump t5pmmfnontr

label t5pmcor:
    scene town tanning 5pm 004b
    pov "Come here."
    susan "Huh?"
    mom "[pov]!"
    pov "You need a good hug."
    susan "Hmm..."
    $ susancorruption += 1
    scene town tanning 5pm 005b
    mom "Sorry, [susan]. He really shouldn't hug you when your only wearing a towel."
    if inc == True:
        pov "Calm down mom. It was just a hug."
        susan "Your son is right. No harm done. And a new experience to say hello."
    else:
        pov "Calm down [mother]. It was just a hug."
        susan "He's is right. No harm done. And a new experience to say hello."
    pov "Oh so you liked it?"
    mom "Excuse me a moment."
    scene town tanning 5pm 006b
    susan "I liked it very much."
    susan "And you did it on purpose, hoping my towel would fall, so you can see my tits, didn't you?"
    pov "..."
    susan "Maybe you should come over some time to play with them."
    pov "<gulp>"
    "You look away to escape the weird talk."
    if momrelationship < 6 and momntr == True and NTR == True:
        jump tanningsalonntrlanding2
    else:
        jump t5pmmfnontr

label tanningsalonntrlanding2:
    scene town tanning 5pm 008 ntr
    call screen checkdarkerpaths_irina
    jump t5pmmf

label t5pmmf:
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    if nicole_voyeur == True:
        scene town tanning 5pm 008 ntr
        mom "Forgive me, I was a bad girl again."
        povi "What is going on over here...?"
        frank "Yes you were. Take that damn towel off!"
        scene town tanning 5pm 009 ntr
        pov "..."
        frank "Much better!"
        frank "Tanning here in my studio is making you very sexy!"
        mom "Thank you!"
        frank "Let me cop a feel."
        scene town tanning 5pm 010 ntr
        if inc == True:
            povi "Why does this lucky bastard get to do this to mom?"
        else:
            povi "Why does this lucky bastard get to do this to her?"
        frank "That ass is so firm because of the many spanks I give you."
        mom "Yes..."
        povi "Nice..."
        frank "Davide is lucky to have you!"
        povi "Geez, that fucker gets around in town."
        scene town tanning 5pm 011 ntr
        with vpunch
        mom "Hah..."
        frank "Your ass is made for spanking!"
        mom "Thank you..."
        frank "Now get your tan girl. Davide is paying me good money for this."
        mom "Alright."
        povi "Figures..."
        scene town tanning 5pm 012 ntr
        frank "What are you looking at boy?"
        frank "Wish you had such a hot girlfriend too, hahaha..."
        pov "..."
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        $ tanning5pmfirst = True # ----- Added in 0.6.5 -----
        jump tan1

    elif nicole_ntr == True:
        scene town tanning 5pm 008 ntr
        mom "Forgive me, I was a bad girl again."
        povi "What...?"
        frank "Yes you were. Take that damn towel off!"
        scene town tanning 5pm 009 ntr
        pov "..."
        frank "Much better!"
        frank "Tanning here in my studio is making you very sexy!"
        mom "Thank you!"
        frank "Let me cop a feel."
        scene town tanning 5pm 010 ntr
        if inc == True:
            povi "Why can he do this to mom?"
        else:
            povi "Why can he do this to her?"
        frank "That ass is so firm because of the many spanks I give you."
        mom "Yes..."
        povi "Argh..."
        frank "Davide is lucky to have you!"
        povi "Don't talk about that asshole too."
        scene town tanning 5pm 011 ntr
        with vpunch
        mom "Hah..."
        frank "Your ass is made for spanking!"
        mom "Thank you..."
        frank "Now get your tan girl. Davide is paying me good money for this."
        mom "Alright."
        povi "No..."
        scene town tanning 5pm 012 ntr
        frank "What are you looking at boy?"
        frank "Wish you had such a hot girlfriend too, hahaha..."
        pov "..."
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        $ tanning5pmfirst = True # ----- Added in 0.6.5 -----
        jump tan1

    elif nicole_revenge == True:
        scene town tanning 5pm 008 ntr
        mom "Forgive me, please..."
        povi "What...?"
        frank "You were a bad girl! Take that damn towel off!"
        scene town tanning 5pm 009 ntr
        pov "..."
        frank "Much better!"
        frank "Tanning here in my studio is making you very sexy!"
        mom "Fuck you!"
        frank "Let me cop a feel."
        scene town tanning 5pm 010 ntr
        if inc == True:
            povi "Why the fuck is he doing this to mom?"
        else:
            povi "Why the fuck is he doing this to her?"
        frank "That ass is so firm because of the many spanks I gave you."
        mom "I'm only doing this because I have to..."
        povi "Argh..."
        frank "Davide is lucky to have you!"
        povi "Don't talk about that asshole too."
        scene town tanning 5pm 011 ntr
        with vpunch
        mom "Ouch..."
        frank "Your ass is made for spanking!"
        mom "..."
        frank "Now get your tan girl. Davide is paying me good money for this."
        mom "..."
        povi "No..."
        scene town tanning 5pm 012 ntr
        frank "What are you looking at boy?"
        frank "Wish you had such a hot girlfriend too, hahaha..."
        pov "..."
        povi "This fucker just made the list. He's fucking dead!"
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        $ tanning5pmfirst = True # ----- Added in 0.6.5 -----
        jump tan1

    else:
        scene town tanning 5pm 008 ntr
        mom "Forgive me, please..."
        povi "What...?"
        frank "You were a bad girl! Take that damn towel off!"
        scene town tanning 5pm 009 ntr
        pov "..."
        frank "Much better!"
        frank "Tanning here in my studio is making you very sexy!"
        mom "Fuck you!"
        frank "Let me cop a feel."
        scene town tanning 5pm 010 ntr
        if inc == True:
            povi "Wow! What kind of deal does he have with my mom?"
        else:
            povi "Wow! What kind of deal does he have with [mother]?"
        frank "That ass is so firm because of the many spanks I gave you."
        mom "I'm only doing this because I have to..."
        povi "Right... I've heard that before"
        frank "Davide is lucky to have you!"
        povi "Not if I take her from him..."
        scene town tanning 5pm 011 ntr
        with vpunch
        mom "Ouch..."
        frank "Your ass is made for spanking!"
        mom "..."
        frank "Now get your tan girl. Davide is paying me good money for this."
        mom "..."
        povi "Interesting..."
        scene town tanning 5pm 012 ntr
        frank "What are you looking at boy?"
        frank "Wish you had such a hot girlfriend too, hahaha..."
        pov "..."
        povi "Seriously, that fat fuck is an idiot. But he's got the right idea."
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        $ tanning5pmfirst = True # ----- Added in 0.6.5 -----
        jump tan1

label t5pmmfnontr:
    scene town tanning 5pm 007
    mom "No that's not okay! It needs to be repaired soon or I won't pay you."
    frank "O...okay..."
    mom "Don't just agree, do it!"
    frank "..."
    scene town tanning 5pm 008
    if inc == True:
        povi "Wow mom."
    else:
        povi "Wow [mother]."
    mom "You do it better quickly!"
    susan "You heard her."
    $ tanning5pmfirst = True # ----- Added in 0.6.5 -----
    jump tan1
