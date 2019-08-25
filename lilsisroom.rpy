


label lsislook:
    hide screen locations
    pov "{i}Maybe I can see something?{/i}"
    scene black
    pov "{i}Damn it. It's no use.{/i}"
    jump lsisroom

label lsisopen:
    hide screen locations
    "You try to open the door."
    pov "{i}Damn, it's locked.{/i}"
    jump lsisroom

label lsislisten:
    hide screen locations
    "You listen through the door."
    pov "{i}Nothing. She must still be sleeping.{/i}"
    jump lsisroom



label lsis21talk:
    hide screen locations
    scene lilsisroom 9pm 002
    mom "Oh hello [pov]."
    $ lilsisrelationship += 1
    $ momrelationship += 1
    ls "Hi dummy <giggle>."
    if lilsisroom9pmfirst == True:
        show blur
        "You can skip the event, because it'll repeat as you seen before."
        "When you achieve the requirements for something new, you'll get noticed, so you won't miss anything."
        "But you'll still collect points."
        "Do you want to skip this event?"
        call screen skiplsis21

        screen skiplsis21():
            default tt = Tooltip (" ")

            fixed:
                imagebutton auto "gui/icons/icon_approve_%s.png" xpos 348 ypos 550 action (Hide('skiplsis21'), Jump('skiplsis21yes')) hovered tt.Action ("Yes") focus_mask True
                imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 348 ypos 750 action (Hide('skiplsis21'), Jump('skiplsis21con')) hovered tt.Action ("No") focus_mask True

                frame:
                    xalign .5
                    text tt.value

        label skiplsis21yes:
            "Would you collect corruption or love points?"
            call screen lsis21points

            screen lsis21points():
                default tt = Tooltip (" ")

                fixed:
                    imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 348 ypos 550 action (Hide('lsis21points'), Jump('lsis21cpoints')) hovered tt.Action ("Collect [cr1] points") focus_mask True
                    imagebutton auto "gui/icons/icon_love_%s.png" xpos 348 ypos 750 action (Hide('lsis21points'), Jump('lsis21lpoints')) hovered tt.Action ("Collect [lv1] points") focus_mask True

                    frame:
                        xalign .5
                        text tt.value

        label lsis21cpoints:
            $ momcorruption += 1
            $ lilsiscorruption += 1
            $ dtime += 1
            jump lsisroom

        label lsis21lpoints:
            $ momlove += 1
            $ lilsislove += 1
            $ dtime += 1
            jump lsisroom



label skiplsis21con:
    hide blur
    mom "[ls]!"
    pov "Hi you two."
    pov "What you're doing?"
    mom "Just some chit-chat."
    ls "<giggle>"
    pov "Sure."
    pov "{i}That wasn't at all honest.{/i}"
    pov "Can I join?"
    mom "Sure."
    jump ls21lay

label ls21lay:
    call screen ls21lay1

screen ls21lay1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 266 ypos 389 action (Hide('ls21lay1'), Jump('lsis21slay')) hovered tt.Action ("Let [ls] lay in the middle") focus_mask True
        if inc == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1274 ypos 389 action (Hide('ls21lay1'), Jump('lsis21mlay')) hovered tt.Action ("Let mom lay in the middle") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1274 ypos 389 action (Hide('ls21lay1'), Jump('lsis21mlay')) hovered tt.Action ("Let [mother] lay in the middle") focus_mask True
        frame:
            xalign .5
            text tt.value



label lsis21mlay:
    pov "Lay yourself in the middle please."
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
    pov "Lay yourself in the middle please."
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
    default tt = Tooltip (" ")

    fixed:
        if ls21mmiddle == True:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1251 ypos 732 action (Hide('ls21mlook1'), Jump('lsis21mtits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 200 ypos 612 action (Hide('ls21mlook1'), Jump('lsis21mlegs')) hovered tt.Action ("Look at legs") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1143 ypos 443 action (Hide('ls21mlook1'), Jump('lsis21lstits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_abort_%s.png" xpos 684 ypos 266 action (Hide('ls21mlook1'), Jump('ls21mlay2')) hovered tt.Action ("Stop looking") focus_mask True
        elif ls21smiddle == True:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 818 ypos 507 action (Hide('ls21mlook1'), Jump('lsis21mtits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1431 ypos 458 action (Hide('ls21mlook1'), Jump('lsis21mlegs')) hovered tt.Action ("Look at legs") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 818 ypos 801 action (Hide('ls21mlook1'), Jump('lsis21lstits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1100 ypos 158 action (Hide('ls21mlook1'), Jump('ls21mlay2')) hovered tt.Action ("Stop looking") focus_mask True

        frame:
            xalign .5
            text tt.value

label lsis21mtits:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 004a
    else:
        scene lilsisroom 9pm 005b
    pov "{i}Her big tits, so near me.{/i}"
    jump ls21mlook

label lsis21mlegs:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 005a
    else:
        scene lilsisroom 9pm 006b
    pov "{i}Her beautiful legs. Wrapped like gifts in these stockings.{/i}"
    jump ls21mlook

label lsis21lstits:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 006a
    else:
        scene lilsisroom 9pm 007b
    pov "{i}[ls] little tits. I can't wait to play with them some time.{/i}"
    jump ls21mlook

label ls21mlay2:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 007a
    else:
        scene lilsisroom 9pm 008b
    mom "Knock! Knock!"
    ls "Wake up, dummy!"
    pov "Oh, sorry..."
    ls "We're talking about you."
    pov "About me...?"
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
    ls "Me too, also when you are a dummy. <giggle>"
    if ls21mmiddle == True:
        scene lilsisroom 9pm 009a
    else:
        scene lilsisroom 9pm 010b
    if inc == True:
        ls "And what do you think about mom's dress. It's beautiful, isn't it?"
        mom "[ls]..."
        ls "No mom. You're looking so much better since we started living here, I want to know big brothers opinion."
    else:
        ls "And what do you think about [mother]'s dress. It's beautiful, isn't it?"
        mom "[ls]..."
        ls "No [mother]. You're looking so much better since we started living here, I want to know his opinion."
    pov "Hmm..."
    jump ls21decide

label ls21decide:
    call screen ls21decide1

screen ls21decide1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 944 ypos 150 action (Hide('ls21decide1'), Jump('ls21love')) hovered tt.Action ("Answer to improve Love [lv1]/both") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 684 ypos 150 action (Hide('ls21decide1'), Jump('ls21cor')) hovered tt.Action ("Answer to improve Corruption [cr1]/both") focus_mask True
        frame:
            xalign .5
            text tt.value

label ls21love:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 010a
    else:
        scene lilsisroom 9pm 011b
    pov "[ls] is right. You look much more beautiful with your new style then before."
    pov "And you're more confident then before. That undercover-quest seems to make you more lively."
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
    pov "And [ls] is doing fine too. She grew up into a fine young adult."
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
    $ lilsisroom9pmfirst = True
    jump lsisroom

label ls21cor:
    if ls21mmiddle == True:
        scene lilsisroom 9pm 010ab
    else:
        scene lilsisroom 9pm 011bc
    pov "[ls] is right. You look much more beautiful with your new style then before."
    pov "The slutty look makes you damn sexy. You show yourself off like there is no need to hide something."
    ls "I didn't mean it that way."
    mom "Eh?"
    if ls21mmiddle == True:
        scene lilsisroom 9pm 011ab
    else:
        scene lilsisroom 9pm 012bc
    pov "But I mean it that way!"
    pov "You show off your assets like you don't know the word \"prude\"."
    mom "But..."
    pov "That's the way women should act and dress and I love it."
    pov "And it would be also really great if [ls] start to dress up like an adult woman too."
    if ls21mmiddle == True:
        scene lilsisroom 9pm 012ab
    else:
        scene lilsisroom 9pm 013bc
    ls "What... You mean...?"
    if inc == True:
        pov "Prove that you're proud of your grown boobs and your other assets like mom."
    else:
        pov "Prove that you're proud of your grown boobs and your other assets like your mother."
    mom "..."
    ls "Dress more slutty...?"
    pov "Yes, don't be afraid to be an adult like the other women!"
    ls "I'm not afraid..."
    pov "Then don't be shy and show it..."
    mom "..."
    ls "..."
    $ lilsiscorruption += 1
    $ momcorruption += 1
    $ dtime += 1
    $ ls21mmiddle = False
    $ ls21smiddle = False
    $ lilsisroom9pmfirst = True
    jump lsisroom


label lsis22lookass:
    hide screen locations
    scene lilsisroom 10pm 002a
    pov "{i}Her small but firm ass. I bet it looks cute too.{/i}"
    jump lsisroom

label lsis22lookfeet:
    hide screen locations
    scene lilsisroom 10pm 003a
    pov "{i}Those cute feet.{/i}"
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
        pov "{i}Her face is so close. I could kiss her right now.{/i}"
    pov "Let me show you something. I know some good stuff too."
    ls "Okay let me see it."
    jump l22v

label l22v:
    call screen l22v1

screen l22v1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1484 ypos 152 action (Hide('ls22v1'), Jump('ls22love')) hovered tt.Action ("Show her more funny videos [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1484 ypos 390 action (Hide('ls22v1'), Jump('ls22cor')) hovered tt.Action ("Show her some porn [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label ls22cor:
    pov "So look at this."
    scene lilsisroom 10pm 006a
    call screen ls22cor1

screen ls22cor1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1433 ypos 300 action (Hide('ls22cor1'), Jump('ls22cor2gb')) hovered tt.Action ("Gang Bang") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1272 ypos 390 action (Hide('ls22cor1'), Jump('ls22cor2bdsm')) hovered tt.Action ("BDSM") focus_mask True
        if inc == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1517 ypos 140 action (Hide('ls22cor1'), Jump('ls22cor2inc')) hovered tt.Action ("Incest") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1287 ypos 125 action (Hide('ls22cor1'), Jump('ls22cor2int')) hovered tt.Action ("Interracial") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1131 ypos 218 action (Hide('ls22cor1'), Jump('ls22cor2les')) hovered tt.Action ("Lesbian") focus_mask True
        if NTR == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1002 ypos 98 action (Hide('ls22cor1'), Jump('ls22cor2ntr')) hovered tt.Action ("NTR") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1007 ypos 306 action (Hide('ls22cor1'), Jump('ls22cor2anal')) hovered tt.Action ("Anal") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1587 ypos 488 action (Hide('ls22cor1'), Jump('ls22cor2femdom')) hovered tt.Action ("Femdom") focus_mask True
        frame:
            xalign .5
            text tt.value



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
    ls "Haha, I bet you'd wish, dummy."
    pov "Haha, that was fun."
    ls "Oh yes, it was. I missed that when you were away."
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
    pov "And? Is there a problem? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yes it's not a funny video but porn can put one in a good mood."
    ls "Hmm..."
    scene lilsisroom 10pm 008gb2
    "Girl" "Hnng... Yesshh! More..."
    pov "See! She's getting a good ride!"
    ls "Hm..."
    pov "Just enjoy it longer. You'll get used to it."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you can have nice dreams tonight."
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
    pov "And? Is there a problem? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yes it's not a funny video but porn can give you a good mood."
    ls "Hmm..."
    scene lilsisroom 10pm 008bdsm2
    "Girl" "Please master! I can't... hah... longer... hnng..."
    pov "Look! The bad girl enjoys her punishment."
    ls "Hm..."
    pov "Just enjoy it longer. You'll get used to it."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you can have nice dreams tonight."
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
    pov "And? Is there a problem? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yes it's not a funny video but porn can give you a good mood."
    ls "Hmm..."
    scene lilsisroom 10pm 008inc2
    "Girl" "Please come inside me, big brother! I want to be your wife!"
    pov "Look, the little sister loves her brother so much."
    ls "Hm..."
    pov "Just enjoy it longer. You'll get used to it."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you can have nice dreams tonight."
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
    pov "And? Is there a problem? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yes it's not a funny video but porn can give you a good mood."
    ls "Hmm..."
    scene lilsisroom 10pm 008int2
    "Girl" "Hah... yes! I want to cum more from your... hah... dick!"
    pov "Look the girl's getting addicted to the black man."
    ls "Hm..."
    pov "Just enjoy it longer. You'll get used to it."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you can have nice dreams tonight."
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
    pov "And? Is there a problem? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yes it's not a funny video but porn can give you a good mood."
    ls "Hmm..."
    scene lilsisroom 10pm 008les2
    "Girl" "More! Lick... me more... hah... so gentle!"
    pov "Look! The girlfriends getting naughtier."
    ls "Hm..."
    pov "Just enjoy it longer. You'll get used to it."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you can have nice dreams tonight."
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
    pov "And? Is there a problem? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yes it's not a funny video but porn can give you a good mood."
    ls "Hmm..."
    scene lilsisroom 10pm 008ntr2
    "Boy" "Nooo! He came inside you. You're not on the pill!"
    pov "Haha... the boy is a cucky!"
    ls "Hm..."
    pov "Just enjoy it longer. You'll get used to it."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you can have nice dreams tonight."
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
    pov "And? Is there a problem? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yes it's not a funny video but porn can give you a good mood."
    ls "Hmm..."
    scene lilsisroom 10pm 008anal2
    "Girl" "Hnng... you're hah... all in..."
    pov "Look! She's taking it all in her ass!"
    ls "Hm..."
    pov "Just enjoy it longer. You'll get used to it."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you can have nice dreams tonight."
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
    pov "And? Is there a problem? We're just watching, not doing it."
    ls "But..."
    pov "And do you like it?"
    ls "It's porn..."
    pov "Yes it's not a funny video but porn can give you a good mood."
    ls "Hmm..."
    scene lilsisroom 10pm 008femdom2
    "Man" "Hah... yes... harder, mistress!"
    pov "He's so obedient!"
    ls "Hm..."
    pov "Just enjoy it longer. You'll get used to it."
    scene lilsisroom 10pm 011a
    ls "Hmmmmm..."
    pov "I knew you would like it. So you can have nice dreams tonight."
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
    pov "Oh, what is it?"
    pov "{i}What does she want to do? Revenge?{/i}"
    scene lilsisroom 10pm 013b
    ls "Muah!"
    pov "{i}Wow!{/i}"
    "[ls] kisses you on the mouth."
    scene lilsisroom 10pm 014b
    pov "What was that for?"
    ls "Nothing! I just wanted to do it."
    pov "Oh, thank you, I liked it."
    pov "{i}Maybe my advice at the date motivated her?{/i}"
    $ lsiskiss += 1
    $ lilsislove += 1
    $ lilsisroom10pmfirst = True
    jump ls22love2