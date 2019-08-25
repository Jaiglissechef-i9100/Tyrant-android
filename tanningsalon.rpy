
label tanningenter:
    hide screen townl
    pov "{i}Let's see what I can do here.{/i}"
    scene town tanning desk
    if momrelationship < 6 and momntr == True and NTR == True and frankfirstmeet == False and vipntrfrank == True:
        pov "{i}That's the asshole that spanked mom!{/i}"
        jump frankunknown
    if frankfirstmeet == False:
        pov "{i}Oh this guy looks mad.{/i}"
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
    pov "I don't have any money, can I maybe get a job here?"
    "NOTE: This scene isn't written properly and will get finished in the next version"
    "NOTE:, but you can take the job, because you need money to access the tanning salon scenes."
    "NOTE: It's the only available job right now, so you'll take it automatically, but you can work when you want to."
    "Man" "Yes, you'll get 20$ per hour."
    pov "Good."
    "Man" "My name is Frank."
    pov "I'm [pov]."
    frank "OK. You can start work when you want to."
    $ tanningjob = True
    jump frankknown


label frankunknown:
    scene town tanning desk
    "Man" "What do you want?"
    pov "Oh wow. No Need to be so mad at me."
    "Man" "I have no time for idiots strolling around in my studio."
    pov "Maybe I want to spent some money here?"
    pov "{i}What an asshole!{/i}"
    "Man" "It's 20$ per hour!"
    pov "Oh, okay."
    jump getatan

label tanningwork1:
    scene town tanning ts work
    "You work one hour cleaning the sunbeds and rooms."
    "NOTE: Working scenes are also available in the next version."
    $ money += 20
    $ dtime += 1
    jump town

label getatan:
    scene town tanning desk2
    call screen getatan1

screen getatan1():
    default tt = Tooltip (" ")

    fixed:
        if money >= 20:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1280 ypos 213 action (Hide ('getatan1'), Jump('getatanyes')) hovered tt.Action ("Buy one hour") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1376 ypos 213 action (Hide ('getatan1'), Jump('getatanno')) hovered tt.Action ("Don't buy") focus_mask True
        if tanningjob == False:
            imagebutton auto "gui/icons/icon_question_%s.png" xpos 864 ypos 213 action (Hide ('getatan1'), Jump('tanningwork')) hovered tt.Action ("Ask for a job") focus_mask True
        if tanningjob == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 741 ypos 213 action (Hide ('getatan1'), Jump('tanningwork1')) hovered tt.Action ("Work (+1 hour/+20$)") focus_mask True

    frame:
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
    pov "I've reconsidered. I won't do anything."
    frank "Then how about you leave my studio now?"
    pov "..."
    jump town


label tanning4pm:
    scene town tanning 4pm 001
    irina "Can I have the sunscreen with the orange flavor please?"
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
        irina "Haha yes. I barely know your younger one."
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
        pov "{i}So this is Frank.{/i}"
        $ frankfirstmeet = True
    frank "You got what you want, so don't tell me how to live my life!"
    irina "Okay, if you say so."
    scene town tanning 4pm 006
    irina "Always a bad mood, haha."
    irina "..."
    irina "I... I need to go now. I have to put this on."
    pov "Okay..."
    irina "See you [pov]."
    pov "Bye."
    scene town tanning 4pm 007
    irina "<giggle>"
    pov "{i}Oh, she's teasing me.{/i}"
    $ tanning4pmfirst = True
    if irinarelationship >= 6 or NTR == False:
        jump tan1
    scene town tanning 4pm 008
    frank "Are you two done yet?"
    pov "Oh sure."
    frank "Good then how about you get your tan now and excuse me."
    pov "..."
    scene town tanning 4pm 009 ntr
    pov "{i}What? Where's he going? Isn't that [irina]'s room?{/i}"
    "You follow him."
    pov "{i}I Have a really bad feeling.{/i}"
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene town tanning 4pm 010 ntr
    pov "{i}No...{/i}"
    frank "Now my mood is getting much better with your mouth stuffed."
    irina "Hmm... <suck>"
    pov "{i}No! Not with that old prick.{/i}"
    frank "Yes, earn your tanning sessions, little slut."
    irina "Hmm... hmm..."
    frank "Argh! Let me mark you!"
    scene town tanning 4pm 011 ntr
    frank "Ahh... hah..."
    irina "Hmm..."
    frank "You did good. Now you can enjoy your tanning."
    irina "Thank you, daddy."
    pov "{i}No! He isn't her real dad, is he? But it's still so wrong!{/i}"
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    $ dtime += 1
    $ tanning4pmntrfirst = True
    jump town


label tanning5pm:
    mom "So I explained it to him."
    "Woman" "Oh yes, he's so stupid sometimes."
    pov "{i}Wait, isn't that...?{/i}"
    scene town tanning 5pm 001
    jump t5pm

label t5pm:
    scene town tanning 5pm 001
    call screen t5pm1

screen t5pm1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_talk_%s.png" xpos 713 ypos 245 action (Hide ('t5pm1'), Jump('t5pmtalk')) hovered tt.Action ("Talk to them") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 996 ypos 245 action (Hide ('t5pm1'), Jump('t5pmignore')) hovered tt.Action ("Ignore them") focus_mask True


    frame:
        xalign .5
        text tt.value

label t5pmignore:
    if inc == True:
        pov "{i}I don't want to talk to mom right now.{/i}"
    else:
        pov "{i}I don't want to talk to [mother] right now.{/i}"
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
        $ susan = renpy.input(_("Her name is...")) or _("Susan")
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
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1103 ypos 207 action (Hide ('t5pmsm1'), Jump('t5pmlove')) hovered tt.Action ("Shake her hand [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1595 ypos 207 action (Hide ('t5pmsm1'), Jump('t5pmcor')) hovered tt.Action ("Hug her [cr1]") focus_mask True


    frame:
        xalign .5
        text tt.value

label t5pmlove:
    scene town tanning 5pm 004a
    if inc == True:
        pov "I'm [pov]. It's nice to meet a friend of mom."
    else:
        pov "I'm [pov]. It's nice to meet a friend of [mother]."
    susan "Me too."
    $ susanlove += 1
    scene town tanning 5pm 005a
    if inc == True:
        susan "You're right, your son really has some manners."
    else:
        susan "You're right, he has really some manners."
    pov "Thank you."
    mom "Yes, I'm so proud of him."
    susan "Maybe we should have tea some time together?"
    mom "Oh sure. That would be nice."
    mom "Excuse me a moment."
    scene town tanning 5pm 006a
    susan "I really meant it. You should come over some time so we can have fun."
    susan "Fun for adults. I know you want too."
    pov "{i}What?{/i}"
    "You look away to escape the weird talk."
    jump t5pmmf

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
    pov "Oh so you liked it."
    mom "Excuse me a moment."
    scene town tanning 5pm 006b
    susan "I liked it very much."
    susan "And you did it on purpose, hoping my towel would fall, so you can see my tits, didn't you?"
    pov "..."
    susan "Maybe you should come over some time to play with them."
    pov "<gulp>"
    "You look away to escape the weird talk."
    jump t5pmmf


label t5pmmf:
    if momrelationship < 6 and momntr == True and NTR == True:
        if gamemusic == True:
            stop music fadeout 2
            play music "music/NTR.mp3"
        scene town tanning 5pm 008 ntr
        mom "Forgive me, I was a bad girl again."
        pov "{i}What...?{/i}"
        frank "Yes you were. Take that damn towel off!"
        scene town tanning 5pm 009 ntr
        pov "..."
        frank "Much better!"
        frank "Tanning here in my studio is making you very sexy!"
        mom "Thank you!"
        frank "Let me cop a feel."
        scene town tanning 5pm 010 ntr
        if inc == True:
            pov "{i}Why can he do this with mom?{/i}"
        else:
            pov "{i}Why can he do this with her?{/i}"
        frank "That ass is so firm because of the many spanks I gave you."
        mom "Yes..."
        pov "{i}Argh...{/i}"
        frank "Davide is lucky to have you!"
        pov "{i}Don't talk about that asshole too.{/i}"
        scene town tanning 5pm 011 ntr
        with vpunch
        mom "Hah..."
        frank "Your ass is made for spanking!"
        mom "Thank you..."
        frank "Now get your tan girl. Davide is paying me good."
        mom "Alright."
        pov "{i}No...{/i}"
        scene town tanning 5pm 012 ntr
        frank "Where you looking boy?"
        frank "Wish you had such a hot girlfriend too, hahaha..."
        pov "..."
        if gamemusic == True:
            stop music fadeout 2
            play music "music/default.mp3"
        $ tanning5pmntrfirst = True
        jump tan1
    else:
        scene town tanning 5pm 007
        mom "No that's not okay! It needs to be repaired soon or I won't pay you."
        frank "O...okay..."
        mom "Don't just agree, do it!"
        frank "..."
        scene town tanning 5pm 008
        if inc == True:
            pov "{i}Wow mom.{/i}"
        else:
            pov "{i}Wow [mother].{/i}"
        mom "You do it better quickly!"
        susan "You heard her."
        $ tanning5pmfirst = True
        jump tan1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
