#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 9pm Lil Sis Room - Alexis, MC, Nicole - Love, Corruption
# 2. 10pm Lil Sis Room - Alexis, MC - Love, Corruption, Fetish Training
#----- End List -----

label lsislook:
    hide screen locations
    povi "Maybe I can see something?"
    scene black
    povi "Damn it. It's no use."
    jump lsisroom

label lsisopen:
    hide screen locations
    "You try to open the door."
    povi "It's locked."
    jump lsisroom

label lsislisten:
    hide screen locations
    "You listen through the door."
    povi "Nothing. Maybe she's sleeping?"
    jump lsisroom

label lsis21talk:
    hide screen locations
    if momlove > 40 and lilsislove > 40 or momcorruption > 30 and lilsiscorruption > 30:
        scene edited main room upstairs listen
        mom "Yeah I do too."
        ls "He's just so cute now, you know..."
        mom "I know right!"
        mom "He's really grown up."
        ls "I love when he just randomly hugs me!"
        mom "I do too. I just want him to hold me forever sometimes."
        povi "Are they talking about me?"
        mom "Don't tell him any of this..."
        if momlove > momcorruption:
            mom "...but I sometime wish he could just take us all away together."
        else:
            mom "...but I sometimes wish he would just take me right then and there."
        povi "Now I really hope they are talking about me!"
    scene lilsisroom 9pm 002
    if momrelationship < 30 and momntr == True or lilsisrelationship < 40 and lilsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump nicoleshakylilsisroom
        elif randomnum == 2:
            " "
    mom "Oh hello [pov]."
    $ lilsisrelationship += 1
    $ momrelationship += 1
    ls "Hi dummy <giggle>."
    mom "[ls]!"
    pov "Hi you two."
    pov "So whatcha doing?"
    mom "Just girl talk..."
    ls "<giggle>"
    pov "Sure."
    povi "That was convincing. Not!"
    pov "Well, I didn't take a class on girl talk while I was away, so I might not be very good at it. But, can I join you guys?"
    mom "Sure."
    jump ls21lay

label ls21lay:
    call screen ls21lay1

screen ls21lay1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls21lay1'), Jump('lsis21slay')) hovered tt.Action ("Let [ls] lay in the middle") focus_mask True
        if inc == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls21lay1'), Jump('lsis21mlay')) hovered tt.Action ("Let mom lay in the middle") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls21lay1'), Jump('lsis21mlay')) hovered tt.Action ("Let [mother] lay in the middle") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lsis21mlay:
    pov "Could you move to the middle please?"
    $ ls21mmiddle = True
    mom "Okay."
    scene lilsisroom 9pm 003a
    if inc == True:
        ls "So you really think so mom?"
    else:
        ls "So you really think so [mother]?"
    mom "Hahaha... yes..."
    jump ls21mlook

label lsis21slay:
    pov "Scoot on over to the middle please."
    $ ls21smiddle = True
    ls "Okay."
    scene lilsisroom 9pm 004b
    if inc == True:
        ls "So you really think so mom?"
    else:
        ls "So you really think so [mother]?"
    mom "Hahaha... yes..."
    jump ls21mlook

label ls21mlook:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 003a
    else:
        scene lilsisroom 9pm 004b
    call screen ls21mlook1

screen ls21mlook1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if ls21mmiddle == True:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('ls21mlook1'), Jump('lsis21mtits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('ls21mlook1'), Jump('lsis21mlegs')) hovered tt.Action ("Look at legs") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('ls21mlook1'), Jump('lsis21lstits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('ls21mlook1'), Jump('ls21mlay2')) hovered tt.Action ("Stop looking") focus_mask True
        elif ls21smiddle == True:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('ls21mlook1'), Jump('lsis21mtits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('ls21mlook1'), Jump('lsis21mlegs')) hovered tt.Action ("Look at legs") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('ls21mlook1'), Jump('lsis21lstits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('ls21mlook1'), Jump('ls21mlay2')) hovered tt.Action ("Stop looking") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lsis21mtits:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 004a
    else:
        scene lilsisroom 9pm 005b
    povi "Seriously, it's not fair. Those enormous breats are so near me and I don't do anthing about it!"
    jump ls21mlook

label lsis21mlegs:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 005a
    else:
        scene lilsisroom 9pm 006b
    povi "Her beautiful legs. Wrapped up like gifts in those stockings."
    jump ls21mlook

label lsis21lstits:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 006a
    else:
        scene lilsisroom 9pm 007b
    povi "[ls] perky tits are just amazing. Maybe I can convince her to let me play with them some time."
    jump ls21mlook

label ls21mlay2:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 007a
    else:
        scene lilsisroom 9pm 008b
    mom "Hello! Earth to [pov]!"
    ls "Wake up, dummy!"
    pov "Oh, sorry..."
    ls "We're talking about you."
    pov "About me...?"
    povi "I knew it!"
    if inc == True:
        ls "Mom is still so happy that you're back home with us."
    else:
        ls "[mother] is still so happy that you're back home with us."
    pov "Oh..."
    if ls21mmiddle == True:
        scene lilsisroom 9pm 008a
    else:
        scene lilsisroom 9pm 009b
        if inc == True:
            ls "Aren't you mom?"
            mom "Yes... I'm so happy that you're here and can support us."
            pov "Me too, mom."
        else:
            ls "Aren't you [mother]?"
            mom "Yes... I'm so happy that you're here and can support us."
            pov "Me too, [mother]."
    ls "Me too, even though you are a big dummy. <giggle>"
    if ls21mmiddle == True:
        scene lilsisroom 9pm 009a
    else:
        scene lilsisroom 9pm 010b
    if inc == True:
        ls "And what do you think about mom's dress. It's beautiful, isn't it?"
        mom "[ls]..."
        ls "No really mom. You're looking so much better since we started living here and I want to know big brothers opinion."
    else:
        ls "And what do you think about [mother]'s dress. It's beautiful, isn't it?"
        mom "[ls]..."
        ls "No really [mother]. You're looking so much better since we started living here and I want to know his opinion."
    pov "Hmm..."
    jump ls21decide

label ls21decide:
    call screen ls21decide1

screen ls21decide1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('ls21decide1'), Jump('ls21love')) hovered tt.Action ("Answer to improve Love [lv1]/both") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('ls21decide1'), Jump('ls21cor')) hovered tt.Action ("Answer to improve Corruption [cr1]/both") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ls21love:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 010a
    else:
        scene lilsisroom 9pm 011b
    pov "[ls] is right. You look even more beautiful with your new style then before."
    pov "And you're more confident than before. This undercover-quest seems to have made you more lively."
    mom "Really, you think so?"
    if inc == True:
        ls "I told you mom."
    else:
        ls "I told you [mother]."
    if ls21mmiddle == True:
        scene lilsisroom 9pm 011a
    else:
        scene lilsisroom 9pm 012b
    if inc == True:
        pov "Yes mom. The new you is really amazing."
        mom "Thank you so much my son."
    else:
        pov "Yes [mother]. The new you is really amazing."
        mom "Thank you so much."
    mom "That makes me even happier."
    pov "And [ls] is doing fine too. She grew up into a beautiful young woman."
    if ls21mmiddle == True:
        scene lilsisroom 9pm 012a
    else:
        scene lilsisroom 9pm 013b
    ls "You really think so?"
    mom "And I told you that... <giggle>"
    if inc == True:
        pov "Yes, little sister."
    else:
        pov "Yes, [ls]."
    ls "Oh thank you so much [pov]."
    pov "You're welcome, both of you."
    mom "<giggle>"
    ls "<giggle>"
    $ lilsislove += 1
    $ momlove += 1
    $ dtime += 1
    $ ls21mmiddle = False
    $ ls21smiddle = False
    $ lilsisroom9pmfirst = True # ----- Added in 0.6.5 -----
    jump lsisroom

label ls21cor:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 010ab
    else:
        scene lilsisroom 9pm 011bc
    pov "[ls] is right. You look way more beautiful with your new style then before."
    pov "The slutty look makes you look so damn sexy. You show yourself off like there is nothing too bold to show the world!"
    ls "I didn't mean it that way."
    mom "Eh?"
    if ls21mmiddle == True:
        scene lilsisroom 9pm 011ab
    else:
        scene lilsisroom 9pm 012bc
    pov "But I mean it that way!"
    pov "You show off your assets like you don't know the meaning of the word \"slut\"."
    mom "But..."
    pov "That's the way women should act and dress and I love it."
    pov "And it would be also really great if [ls] started to dress up like an adult too."
    if ls21mmiddle == True:
        scene lilsisroom 9pm 012ab
    else:
        scene lilsisroom 9pm 013bc
    ls "What... You mean...?"
    if inc == True:
        pov "Prove that you're proud of your growing breast and your other assets like mom."
    else:
        pov "Prove that you're proud of your growing breast and your other assets like your mother."
    mom "..."
    ls "Dress more, slutty...?"
    pov "Yes, don't be afraid to be an adult, like the other women!"
    ls "I'm not afraid..."
    pov "Then don't be shy and show it..."
    mom "..."
    ls "..."
    $ lilsiscorruption += 1
    $ momcorruption += 1
    $ dtime += 1
    $ ls21mmiddle = False
    $ ls21smiddle = False
    $ lilsisroom9pmfirst = True # ----- Added in 0.6.5 -----
    jump lsisroom

label lsis22lookass:
    hide screen locations
    scene lilsisroom 10pm 002a
    povi "Her small but firm ass. I bet it looks cute too."
    jump lsisroom

label lsis22lookfeet:
    hide screen locations
    scene lilsisroom 10pm 003a
    povi "Those cute feet."
    jump lsisroom

label lsis22talk:
    hide screen locations
    pov "Hey [ls]."
    scene lilsisroom 10pm 004
    if lilsisrelationship < 40 and lilsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump alexisshakylilsisroom
        elif randomnum == 2:
            " "
    if inc == True:
        ls "Oh hey big brother."
    else:
        ls "Oh hey [pov]."
    pov "What are you doing?"
    ls "I'm watching funny videos."
    pov "Ah. Can I join you?"
    scene lilsisroom 10pm 005
    ls "Sure..."
    pov "Good. Just move a little bit."
    ls "Sshhh..."
    pov "Let me see too."
    scene lilsisroom 10pm 006
    pov "What's happening?"
    ls "Sshh... just wait a little bit longer."
    pov "..."
    scene lilsisroom 10pm 006a
    ls "See?"
    pov "Oh yes, hahaha..."
    scene lilsisroom 10pm 007
    ls "Hahaha... that was so funny."
    pov "Hahaha, you're right."
    if inc == True:
        povi "Her face is so close. I could kiss her right now."
    pov "Let me show you something. I know some good stuff too."
    ls "Okay let me see it."
    jump l22v

label l22v:
    call screen l22v1

screen l22v1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('ls22v1'), Jump('ls22love')) hovered tt.Action ("Show her more funny videos [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('ls22v1'), Jump('ls22cor')) hovered tt.Action ("Show her some porn [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ls22cor:
    pov "So look at this."
    scene lilsisroom 10pm 006a
    call screen ls22cor1

screen ls22cor1():
    modal True
    default tt = Tooltip ("Select Porn")
    tag ls22cortIag

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls22cor1'), Jump('ls22cor2anal')) hovered tt.Action ("Anal") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls22cor1'), Jump('ls22cor2bdsm')) hovered tt.Action ("BDSM") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls22cor1'), Jump('ls22cor2femdom')) hovered tt.Action ("Femdom") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls22cor1'), Jump('ls22cor2gb')) hovered tt.Action ("Gang Bang") focus_mask True
        if inc == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls22cor1'), Jump('ls22cor2inc')) hovered tt.Action ("Incest") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls22cor1'), Jump('ls22cor2int')) hovered tt.Action ("Interracial") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls22cor1'), Jump('ls22cor2les')) hovered tt.Action ("Lesbian") focus_mask True
        if NTR == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ls22cor1'), Jump('ls22cor2ntr')) hovered tt.Action ("NTR") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('ls22cor1'), Jump('ls22love')) hovered tt.Action ("Nevermind") focus_mask True

        frame:
            if tt.value == "" or tt.value ==" ":
                background None
            xalign .5
            yalign .23
            xanchor .5
            yanchor .23
            xfill True
            yfill True
            xmaximum 252
            ymaximum 63
            text tt.value at center

label ls22love:
    pov "So look at this."
    scene lilsisroom 10pm 008b
    ls "Hmm... oh..."
    pov "It's some good stuff, isn't it?"
    ls "Haha..."
    pov "Wait...!"
    scene lilsisroom 10pm 008bb
    ls "Oh my god, hahahaha..."
    scene lilsisroom 10pm 009b
    ls "That was so funny!"
    pov "I'm glad you liked it."
    ls "Hahaha... I can't stop laughing."
    pov "Good. That's my chance."
    ls "What do you mean...?"
    scene lilsisroom 10pm 010b
    ls "Oh that's not fair, I'm already dying from laughing."
    pov "Then I'll make sure you'll really die, hahaha."
    ls "Oh no stop... hahaha..."
    pov "There is no mercy."
    scene lilsisroom 10pm 011b
    ls "Hahahaha... you're really trying to kill me."
    pov "Oh yes, hahaha..."
    ls "I just can't stop..."
    pov "I'd love to see you laughing all day, that's really cute."
    ls "Haha, I bet you do, dummy."
    pov "Haha, that was fun."
    ls "Yeah, it was. I missed that when you were away."
    if adatekiss == True and lilsislove >= 30:
        jump ls22kiss
    else:
        jump ls22love2

label ls22love2:
    $ lilsisrelationship += 1
    $ lilsislove += 1
    $ dtime += 1
    $ lilsisroom10pmfirst = True
    jump lsisroom

label ls22cor2gb:
    scene lilsisroom 10pm 008gb1
    "Girl" "Oh yes fuck me harder! Give me all your dicks!"
    pov "Oh, this a good one."
    ls "..."
    scene lilsisroom 10pm 009a
    if inc == True:
        ls "Why are you showing me porn brother?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with my brother..."
    else:
        ls "Why are you showing me porn [pov]?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with you..."
    pov "Is there a problem with that? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yeah it's not a funny video but porn can put you in a good mood too."
    ls "Hmm..."
    scene lilsisroom 10pm 008gb2
    "Girl" "Hnng... Yesshh! More..."
    pov "See! She's getting a good ride!"
    ls "Hm..."
    pov "Just watch it a bit longer. You'll start to like it, I'm sure."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you now can have nice dreams tonight."
    ls "..."
    $ lsisprongangbang += 1
    $ lilsisrelationship += 1
    $ lilsiscorruption += 1
    $ dtime += 1
    $ lilsisroom10pmfirst = True
    jump lsisroom

label ls22cor2bdsm:
    scene lilsisroom 10pm 008bdsm1
    "Girl" "Please master! I'll be obedient!"
    pov "Oh, this a good one."
    ls "..."
    scene lilsisroom 10pm 009a
    if inc == True:
        ls "Why are you showing me porn brother?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with my brother..."
    else:
        ls "Why are you showing me porn [pov]?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with you..."
    pov "Is there a problem with that? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yeah it's not a funny video but porn can put you in a good mood too."
    ls "Hmm..."
    scene lilsisroom 10pm 008bdsm2
    "Girl" "Please master! I can't... hah... longer... hnng..."
    pov "Look! The bad girl enjoys her punishment."
    ls "Hm..."
    pov "Just watch it a bit longer. You'll start to like it, I'm sure."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you now can have nice dreams tonight."
    ls "..."
    $ lsispronBDSM += 1
    $ lilsisrelationship += 1
    $ lilsiscorruption += 1
    $ dtime += 1
    $ lilsisroom10pmfirst = True
    jump lsisroom

label ls22cor2inc:
    scene lilsisroom 10pm 008inc1
    "Girl" "I love you brother! I know it's forbidden but please fuck me more!"
    pov "Oh, this a good one."
    ls "..."
    scene lilsisroom 10pm 009a
    if inc == True:
        ls "Why are you showing me porn brother?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with my brother..."
    else:
        ls "Why are you showing me porn [pov]?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with you..."
    pov "Is there a problem with that? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yeah it's not a funny video but porn can put you in a good mood too."
    ls "Hmm..."
    scene lilsisroom 10pm 008inc2
    "Girl" "Please come inside me, big brother! I want to be your wife!"
    pov "Look, the little sister loves her brother so much."
    ls "Hm..."
    pov "Just watch it a bit longer. You'll start to like it, I'm sure."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you now can have nice dreams tonight."
    ls "..."
    $ lsisproninc += 1
    $ lilsisrelationship += 1
    $ lilsiscorruption += 1
    $ dtime += 1
    $ lilsisroom10pmfirst = True
    jump lsisroom

label ls22cor2int:
    scene lilsisroom 10pm 008int1
    "Girl" "Oh my god! You're so big!"
    pov "Oh, this a good one."
    ls "..."
    scene lilsisroom 10pm 009a
    if inc == True:
        ls "Why are you showing me porn brother?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with my brother..."
    else:
        ls "Why are you showing me porn [pov]?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with you..."
    pov "Is there a problem with that? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yeah it's not a funny video but porn can put you in a good mood too."
    ls "Hmm..."
    scene lilsisroom 10pm 008int2
    "Girl" "Hah... yes! I want to cum more from your... hah... dick!"
    pov "Look the girl's getting addicted to the black man."
    ls "Hm..."
    pov "Just watch it a bit longer. You'll start to like it, I'm sure."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you now can have nice dreams tonight."
    ls "..."
    $ lsisproninterracial += 1
    $ lilsisrelationship += 1
    $ lilsiscorruption += 1
    $ dtime += 1
    $ lilsisroom10pmfirst = True
    jump lsisroom

label ls22cor2les:
    scene lilsisroom 10pm 008les1
    "Girl" "You taste so good! I won't ever stop!"
    pov "Oh, this a good one."
    ls "..."
    scene lilsisroom 10pm 009a
    if inc == True:
        ls "Why are you showing me porn brother?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with my brother..."
    else:
        ls "Why are you showing me porn [pov]?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with you..."
    pov "Is there a problem with that? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yeah it's not a funny video but porn can put you in a good mood too."
    ls "Hmm..."
    scene lilsisroom 10pm 008les2
    "Girl" "More! Lick... me more... hah... so gentle!"
    pov "Look! The girlfriends getting naughtier."
    ls "Hm..."
    pov "Just watch it a bit longer. You'll start to like it, I'm sure."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you now can have nice dreams tonight."
    ls "..."
    $ lsispronlesbian += 1
    $ lilsisrelationship += 1
    $ lilsiscorruption += 1
    $ dtime += 1
    $ lilsisroom10pmfirst = True
    jump lsisroom

label ls22cor2ntr:
    scene lilsisroom 10pm 008ntr1
    "Boy" "Oh no Tracy, why you do this with him? I thought you loved me."
    pov "Oh, this a good one."
    ls "..."
    scene lilsisroom 10pm 009a
    if inc == True:
        ls "Why are you showing me porn brother?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with my brother..."
    else:
        ls "Why are you showing me porn [pov]?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with you..."
    pov "Is there a problem with that? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yeah it's not a funny video but porn can put you in a good mood too."
    ls "Hmm..."
    scene lilsisroom 10pm 008ntr2
    "Boy" "Nooo! He came inside you. You're not on the pill!"
    pov "Haha... the boy is a cucky!"
    ls "Hm..."
    pov "Just watch it a bit longer. You'll start to like it, I'm sure."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you now can have nice dreams tonight."
    ls "..."
    $ lsispronntr += 1
    $ lilsisrelationship += 1
    $ lilsiscorruption += 1
    $ dtime += 1
    $ lilsisroom10pmfirst = True
    jump lsisroom

label ls22cor2anal:
    scene lilsisroom 10pm 008anal1
    "Girl" "Oh my god! You're in my asshole!"
    pov "Oh, this a good one."
    ls "..."
    scene lilsisroom 10pm 009a
    if inc == True:
        ls "Why are you showing me porn brother?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with my brother..."
    else:
        ls "Why are you showing me porn [pov]?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with you..."
    pov "Is there a problem with that? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yeah it's not a funny video but porn can put you in a good mood too."
    ls "Hmm..."
    scene lilsisroom 10pm 008anal2
    "Girl" "Hnng... you're hah... all in..."
    pov "Look! She's taking it all in her ass!"
    ls "Hm..."
    pov "Just watch it a bit longer. You'll start to like it, I'm sure."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you now can have nice dreams tonight."
    ls "..."
    $ lsispronanal += 1
    $ lilsisrelationship += 1
    $ lilsiscorruption += 1
    $ dtime += 1
    $ lilsisroom10pmfirst = True
    jump lsisroom

label ls22cor2femdom:
    scene lilsisroom 10pm 008femdom1
    "Girl" "Yes, be a good slave!"
    pov "Oh, this a good one."
    ls "..."
    scene lilsisroom 10pm 009a
    if inc == True:
        ls "Why are you showing me porn brother?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with my brother..."
    else:
        ls "Why are you showing me porn [pov]?"
        pov "Adults watch this stuff, so I thought I would show you."
        ls "But watching porn with you..."
    pov "Is there a problem with that? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yeah it's not a funny video but porn can put you in a good mood too."
    ls "Hmm..."
    scene lilsisroom 10pm 008femdom2
    "Man" "Hah... yes... harder, mistress!"
    pov "He's so obedient!"
    ls "Hm..."
    pov "Just watch it a bit longer. You'll start to like it, I'm sure."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you now can have nice dreams tonight."
    ls "..."
    $ lsispronfemdom += 1
    $ lilsisrelationship += 1
    $ lilsiscorruption += 1
    $ dtime += 1
    $ lilsisroom10pmfirst = True
    jump lsisroom

label ls22kiss:
    scene lilsisroom 10pm 012b
    if inc == True:
        ls "Come here, big brother."
    else:
        ls "Come here, [pov]."
    pov "Why...?"
    povi "What does she want to do? Get revenge?"
    scene lilsisroom 10pm 013b
    ls "Muah!"
    povi "Wow!"
    "[ls] kisses you on the mouth."
    scene lilsisroom 10pm 014b
    pov "What was that for?"
    ls "Nothing! I just wanted to do it."
    pov "Oh, thank you, I liked it."
    povi "Maybe our date went better than I thought?"
    $ lsiskiss += 1
    $ lilsislove += 1
    $ lilsisroom10pmfirst = True
    jump ls22love2
