#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 8pm Front Door - Bruce, Davide, MC - Good, Bad
# 2. 1pm Front Door - Cassandra, Martin, MC - Good, Bad, Love, Corruption
# 3. 9pm Front Door - Cassandra, Irina, MC - Love, Corruption
#----- End List -----

label frontdoorcloser:
    hide screen locations
    povi "Let's see what's going on."
    scene frontdoor 8pm 002
    davide "Oh, it's you."
    dad "Hey [pov]."
    pov "What's going on here? Something bad happened?"
    if inc == True:
        davide "Yes, your dad ruined it!"
    else:
        davide "Yes, Bruce ruined it!"
    pov "What...?"
    scene frontdoor 8pm 003
    dad "We're running from the cops and decided to split up."
    dad "Davide took the short cut and Steve and I should've lured the cops the long way."
    pov "Okay..."
    dad "We had to carry the loot away fast, but I tripped..."
    povi " Accidentally or get this undercover shit to an end?"
    dad "And then Steve stopped to helped me. I got away and the cops caught him instead of me."
    pov "And now you're afraid he could snitch on you!"
    scene frontdoor 8pm 004
    davide "No. That won't be a problem. He's loyal to us and won't snitch on us."
    davide "But someone will need to care for his mother. She's ill and can't take care of herself all alone."
    davide "He knows we'll take care of her so that is not the problem."
    dad "We have to carry the loot to several people and it's very hard with one man down."
    povi "What idiots, haha."
    jump fda

label fda:
    call screen fda1

screen fda1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('fda1'), Jump('frontdoorapprove')) hovered tt.Action ("Help them [gd1]/both") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('fda1'), Jump('frontdoordisapprove')) hovered tt.Action ("Don't care [bd1]/both") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdoordisapprove:
    scene frontdoor 8pm 005a
    pov "I don't care about your shit!"
    davide "What did you say?"
    if inc == True:
        pov "You heard me. It's your problem and maybe dad's. So don't get me involved after you already fucked up!"
        dad "No, wait son..."
        davide "Your son's an asshole!"
    else:
        pov "You heard me. It's your problem and maybe Bruce's. So don't get me involved after you already fucked up!"
        dad "No, wait [pov]..."
        davide "He's an asshole!"
    pov "Whatever..."
    $ frontdoorddfirst = True
    $ dadbad += 1
    $ davidebad += 1
    $ dtime += 1
    jump frontdoor

label frontdoorapprove:
    scene frontdoor 8pm 005b
    pov "I don't get why that is such a problem?"
    dad "We already told you."
    davide "I don't get it! Did we miss something?"
    povi "No wonder that undercover thing took so long. They're so stupid and slow."
    pov "You lost one member, so get another member."
    davide "Eh?"
    scene frontdoor 8pm 006b
    davide "Oh, you want to take his place?"
    pov "Obviously."
    if inc == True:
        dad "That's my son!"
    davide "Very good idea. So you in for now. I'm interested to see how you'll work out."
    povi "Now I'm in their gang. Let's see what I can do to fuck with Davide."
    $ frontdoorddfirst = True
    #$ gangmember = True ----- Removed in 0.6.5 -----
    $ gangmemberaccept = 1 # ----- Added in 0.6.5 -----
    $ dadgood += 1
    $ davidegood += 1
    $ dtime += 1
    jump frontdoor

label frontdoor13closer:
    hide screen locations
    scene frontdoor 1pm 002
    if inc == True:
        povi "Big sis is making out with that guy?"
    else:
        povi "[bs] is making out with that guy?"
    povi "So this must be her boyfriend. But that guy looks weird."
    jump fd1pmcl

label fd1pmcl:
    hide screen locations
    scene frontdoor 1pm 002
    call screen fd1pmcl1

screen fd1pmcl1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('fd1pmcl1'), Jump('frontdoor1tits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('fd1pmcl1'), Jump('frontdoor1ass')) hovered tt.Action ("Look at ass") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('fd1pmcl1'), Jump('frontdoor1talk')) hovered tt.Action ("Talk") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdoor1tits:
    hide screen locations
    scene frontdoor 1pm 002a
    if inc == True:
        povi "That lucky bastard motorboatin' my big sister's tits."
    else:
        povi "That lucky bastard motorboatin' [bs]'s tits."
    povi "Soon I'll be the one doing that."
    jump fd1pmcl

label frontdoor1ass:
    hide screen locations
    scene frontdoor 1pm 002b
    povi "He gets to grope that hot ass."
    povi "That's my job pal!"
    jump fd1pmcl

#----- edited scene -----
label frontdoor1talk:
    hide screen locations
    pov "Ahem..."
    scene frontdoor 1pm 003
    #----- Removed and bigsisntr == True to expand random options for both ntr paths -----
    if bigsisrelationship < 30:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump cassandrashakyfd
        elif randomnum == 2:
            " "
    $ martinfirstmeet = True
    bs "Eh?"
    "Guy" "Hmm...?"
    bs "Oh damn it!"
    scene frontdoor 1pm 004
    if inc == True:
        bs "This is my stupid little brother."
    else:
        bs "This is stupid [pov]."
    bs "And this is my boyfriend Martin."
    martin "Hello, nice to meet you."
    if inc == True:
        martin "I finally get to meet my girlfriends brother for the first time. She's told me much about you."
        povi "This is my big sister's boyfriend?"
    else:
        martin "I finally get to meet you for the first time. She's told me much about you."
        povi "This is my [bs]'s boyfriend?"
    povi "An emo? That's not what I expected..."
    pov "Well I'm sure only half of what she said was true!"
    jump fd1pmemo

label fd1pmemo:
    call screen fd1pmemo1

screen fd1pmemo1:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('fd1pmemo1'), Jump('frontdoor1emoapprove')) hovered tt.Action ("Greet him nice [gd1]") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('fd1pmemo1'), Jump('frontdoor1emodisapprove')) hovered tt.Action ("Greet him rude [bd1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdoor1emoapprove:
    $ frontd1approve = True
    pov "It's nice to meet you too."
    pov "It seems like you're a nice enough guy."
    scene frontdoor 1pm 005
    if inc == True:
        martin "I'm surprised. Your brother seems to be a nice guy. He's nothing like you told me."
    else:
        martin "I'm surprised. He seems to be a nice guy. He's nothing like you told me."
    bs "He's just acting."
    martin "I'm not sure. Maybe you're just wrong."
    $ martingood += 1
    jump fd1pmwatch

label frontdoor1emodisapprove:
    $ frontd1disapprove = True
    pov "Oh shit, are you're an emo, hahaha."
    pov "What the fuck happened to you [bs]?"
    scene frontdoor 1pm 007
    if inc == True:
        martin "You're right! You're brother isn't a nice guy."
    else:
        martin "You're right! He isn't a nice guy."
    bs "I told you so."
    $ martinbad += 1
    jump fd1pmwatch

label fd1pmwatch:
    if frontd1approve == True:
        scene frontdoor 1pm 005
    else:
        scene frontdoor 1pm 007
    call screen fd1pmwatch1

screen fd1pmwatch1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('fd1pmwatch1'), Jump('frontdoor1lookemo')) hovered tt.Action ("Look at him") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('fd1pmwatch1'), Jump('frontdoor1talk2')) hovered tt.Action ("Stop looking") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('fd1pmwatch1'), Jump('frontdoor1lookbstits')) hovered tt.Action ("Look at tits") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdoor1lookbstits:
    scene frontdoor 1pm 006
    povi "Damn, I can't get enough of her tits. Seeing them through that transparent top is great."
    jump fd1pmwatch

label frontdoor1lookemo:
    scene frontdoor 1pm 006a
    povi "Is he really wearing make up?"
    povi "And that silly ass look. A true emo?"
    jump fd1pmwatch

label frontdoor1talk2:
    scene frontdoor 1pm 008
    pov "So you two are together. Surprising."
    bs "Is that so?"
    pov "So what do you for a living Martin?"
    martin "I'm a famous singer with my band."
    pov "Band?"
    scene frontdoor 1pm 009
    martin "We're \"The Chosen\"!"
    bs "His band is really famous. And I'm his girlfriend."
    jump fd1pmband

label fd1pmband:
    call screen fd1pmband1

screen fd1pmband1:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('fd1pmemo1'), Jump('frontdoor1bandapprove')) hovered tt.Action ("Congratulate them [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('fd1pmemo1'), Jump('frontdoor1banddisapprove')) hovered tt.Action ("Make fun of them [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdoor1bandapprove:
    pov "Wow congratulations. You found a great boyfriend, [bs]."
    scene frontdoor 1pm 010a
    if inc == True:
        martin "Thank you man! It's good to hear it from her brother."
    else:
        martin "Thank you man! It's good to hear it from you."
    bs "Yes, isn't he sweet?"
    martin "You're always welcome at our concerts!"
    pov "You're welcome."
    $ frontd1approve = False
    $ frontd1disapprove = False
    $ bigsislove += 1
    $ bigsisrelationship += 1
    $ dtime += 1
    $ frontdoor1pmfirst = True # ----- added in 0.6.5 -----
    jump frontdoor

label frontdoor1banddisapprove:
    pov "Is that the music about \"sucking dicks\" that [bs] is listening to all the time?"
    scene frontdoor 1pm 010b
    martin "Sucking what?"
    bs "What...? That's not true!"
    martin "What does he mean?"
    bs "He's lying! I don't listen to music like that!"
    povi "Hahaha..."
    $ frontd1approve = False
    $ frontd1disapprove = False
    $ bigsiscorruption += 1
    $ bigsisrelationship += 1
    $ dtime += 1
    $ frontdoor1pmfirst = True # ----- added in 0.6.5 -----
    jump frontdoor

label frontdoor21closer:
    hide screen locations
    scene frontdoor 9pm 002
    povi "Damn, their clothes are so revealing. It's hot! And [irina]!"
    povi "It would be damn nice if they took me with them once in a while. Especially wherever they go in those outfits."
    jump fd21la

label fd21la:
    hide screen locations
    scene frontdoor 9pm 002
    call screen fd21la1

screen fd21la1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('fd21la1'), Jump('frontdoor21look')) hovered tt.Action ("Look at ass") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('fd21la1'), Jump('frontdoor21talk')) hovered tt.Action ("Talk") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdoor21look:
    scene frontdoor 9pm 002a
    povi "That dress is so wonderfully transparent. It covers just in all the right places."
    povi "Her ass is so firm."
    jump fd21la

label frontdoor21talk:
    pov "Hello Ladies!"
    $ bigsisrelationship += 1
    $ irinarelationship += 1
    scene frontdoor 9pm 003
    bs "It's you again!"
    irina "Oh hi [pov]!"
    pov "Wow, nice outfits!"
    irina "Thank you."
    bs "The little perv wants to stare."
    pov "No...I..."
    jump frontdoor21talk2

label frontdoor21talk2:
    call screen fd21talk3

screen fd21talk3():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_gift_%s.png" action (Hide('fd21talk3'), Show('giftfd21icon', transition=None)) hovered tt.Action ("Give someone a gift") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('fd21talk3'), Jump('frontdoor21talk4')) hovered tt.Action ("Don't give anyone a gift") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdoor21talk4:
    scene frontdoor 9pm 004
    bs "I'm going inside now. See you tomorrow [irina]."
    irina "Okay, see you."
    povi "Oh she wants to stay with me."
    scene frontdoor 9pm 005
    irina "It's nice to see you again."
    pov "Totally."
    irina "So... you really like my outfit?"
    pov "Hmm..."
    pov "Maybe I can see the back too?"
    scene frontdoor 9pm 005a
    irina "And...?"
    povi "That transparency is killing me. It's Like she's almost naked."
    pov "Hmm..."
    scene frontdoor 9pm 006
    irina "Come on! Don't make me wait any longer. Let me know what you think."
    irina "It's sexy, isn't it?"
    jump fd21dc

label fd21dc:
    call screen fd21dc1

screen fd21dc1:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('fd21dc1'), Jump('frontdoor21love')) hovered tt.Action ("Answer to improve Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('fd21dc1'), Jump('frontdoor21cor')) hovered tt.Action ("Answer to improve Corruption [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdoor21cor:
    pov "It's really sexy and just the right thing a girl like you should be wearing."
    scene frontdoor 9pm 007c
    pov "A girl who wants to drive the men crazy and show off that she's willing to earn her gifts."
    irina "Like a prostitute?"
    pov "No! You're not a prostitute. More like a hot chick that knows exactly what to do to get what she wants."
    irina "So you like me in this outfit then."
    pov "Yes! Of course I do. So what should we do to celebrate that you got what you wanted?"
    irina "Oh, so I have you now do I?"
    pov "Yup, so what are you going to do to keep me?"
    scene frontdoor 9pm 008c
    irina "I could start by showing off more skin maybe?"
    pov "Right. That's a good idea to begin with."
    pov "Showing off your smokin' hot body."
    irina "Okay..."
    pov "Play more with me and we can come together."
    scene frontdoor 9pm 009c
    irina "Like that...?"
    pov "Holy shit! That's hot."
    pov "And especially the opening at the just the right place in your dress."
    irina "Thank you..."
    scene frontdoor 9pm 010c
    pov "And I'm very sure you show yourself off in that outfit because your waiting for someone to advantage of it!"
    pov "You're not that type of girl who would dress like this because others like [bs] do."
    irina "Hmm..."
    pov "You're soft skin. And you're shivering."
    irina "Hmm..."
    pov "So am I correct with my assumption?"
    scene frontdoor 9pm 011c
    irina "Hmm..."
    pov "So that sounds like a \"yes\" to me."
    pov "I'm glad I got to meet a sexy girl like you."
    pov "I'll call you soon and then we can go out together!"
    irina "Hmm... okay..."
    $ irinacorruption += 1
    $ dtime += 1
    $ frontdoor9pmfirst = True # ----- added in 0.6.5 -----
    jump frontdoor

label frontdoor21love:
    pov "I think it looks wonderful."
    pov "But you could wear anything and still be the most beautiful girl in the world."
    scene frontdoor 9pm 007a
    irina "Oh my goodness! That's the most beautiful thing someone has ever said to me!"
    pov "You're welcome."
    irina "You're really quiet a bit different than all the other men around."
    irina "And you're so polite."
    pov "Oh and there is more. Come here."
    scene frontdoor 9pm 008a
    irina "Oh wow, another hug."
    pov "Yes, I see you needed that."
    scene frontdoor 9pm 009a
    irina "You can do that anytime you want. No one ever just hugs me without asking for a reward."
    pov "Hmm..."
    irina "I feel like someone actually cares about me while I'm in your arms."
    $ irinalove += 1
    jump fd21ga

label fd21ga:
    call screen fd21ga1

screen fd21ga1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_abort_love_%s.png" action (Hide('fd21ga1'), Jump('frontdoor21nogrope')) hovered tt.Action ("Don't [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" action (Hide('fd21ga1'), Jump('frontdoor21grope')) hovered tt.Action ("Grope her ass [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdoor21grope:
    scene frontdoor 9pm 009b
    pov "Of course a hug grants some privileges too."
    irina "Eh?"
    pov "Like also enjoying the firm ass of a nice girl."
    "You knead her ass-cheeks."
    scene frontdoor 9pm 010b
    irina "Hmm..."
    pov "That sort of hug is nice too, isn't it?"
    irina "Hmm... I don't know..."
    scene frontdoor 9pm 011b
    irina "So we'll meet again?"
    povi "Hmm... maybe groping her ass was too much. She's not as happy as she was before."
    pov "Yes, I would like that."
    irina "Then please call me. You're still a better man then the others here."
    povi "Still? Yup, it was too much."
    pov "Sure, I will."
    $ irinacorruption += 1
    $ dtime += 1
    $ frontdoor9pmfirst = True
    jump frontdoor

label frontdoor21nogrope:
    scene frontdoor 9pm 011a
    irina "I still can't believe it. Such a wonderful guy showing an interest in me."
    pov "And I can't believe that such an amazing girl like you doesn't have a boyfriend already. You don't have one, do you?"
    irina "No. But I hope that will change soon."
    pov "Oh, so you're interested in a normal guy like me?"
    scene frontdoor 9pm 012a
    irina "Oh, you're playing with me? <giggle>"
    irina "Please call me so we can go out soon. I would love to hang out more with a good man like you."
    pov "It would be my pleasure."
    irina "Oh my god. You make me blush."
    irina "Don't make me wait too long or I'll go crazy."
    pov "Haha, okay."
    $ irinalove += 1
    $ dtime += 1
    $ frontdoor9pmfirst = True
    jump frontdoor
