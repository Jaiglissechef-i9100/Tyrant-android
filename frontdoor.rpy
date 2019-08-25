

label frontdoorcloser:
    hide screen locations
    pov "{i}Let's see what's going on.{/i}"
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
    pov "{i} Accidentally or get that undercover shit to an end?{/i}"
    dad "And then Steve stopped and helped me. But then I got away and the cops caught him instead of me."
    pov "And now you're afraid he could snitch on you!"
    scene frontdoor 8pm 004
    davide "No. That won't be a problem. He's loyal to us and won't snitch on us."
    davide "And someone must take care of is his mother. She's ill and can't take care of herself all alone."
    davide "He knows we'll take care of her so that is not the problem."
    dad "We have to carry the loot to several people and it's very hard with one man less."
    pov "{i}What idiots, haha.{/i}"
    jump fda

label fda:
    call screen fda1

screen fda1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1664 ypos 162 action (Hide('fda1'), Jump('frontdoorapprove')) hovered tt.Action ("Help them [gd1]/both") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1664 ypos 293 action (Hide('fda1'), Jump('frontdoordisapprove')) hovered tt.Action ("Don't care [bd1]/both") focus_mask True
        frame:
            xalign .5
            text tt.value

label frontdoordisapprove:
    scene frontdoor 8pm 005a
    pov "I don't care about your shit!"
    davide "What did you say?"
    if inc == True:
        pov "You heard me. It's your problem and maybe dad's. So don't get me involved after you already fucked up!"
        dad "No, wait son..."
        davide "Your son is an asshole!"
    else:
        pov "You heard me. It's your problem and maybe Bruce's. So don't get me involved after you already fucked up!"
        dad "No, wait [pov]..."
        davide "He is an asshole!"
    pov "Whatever..."
    $ frontdoorddfirst = True
    $ dadbad += 1
    $ davidebad += 1
    $ dtime += 1
    jump frontdoor

label frontdoorapprove:
    scene frontdoor 8pm 005b
    pov "I don't understand why you make such a problem out of that?"
    dad "We already told you."
    davide "I don't get it! Did we miss something?"
    pov "{i}No wonder that undercover thing took so long. They're so stupid and slow.{/i}"
    pov "You lost one member and another joined in?"
    davide "Eh?"
    scene frontdoor 8pm 006b
    davide "Oh, you want to take his place?"
    pov "Obviously."
    if inc == True:
        dad "That's my son!"
    davide "Very good idea. So you in for now. I'm curious how you'll work out."
    pov "{i}Now I'm in their gang. Let's see what we can do then.{/i}"
    $ frontdoorddfirst = True
    $ gangmemberaccept = 1
    $ dadgood += 1
    $ davidegood += 1
    $ dtime += 1
    jump frontdoor


label frontdoor13closer:
    hide screen locations
    scene frontdoor 1pm 002
    if inc == True:
        pov "{i}Big sis is making out with that guy?{/i}"
    else:
        pov "{i}[bs] is making out with that guy?{/i}"
    pov "{i}So this must be her boyfriend. But that guy looks weird.{/i}"
    jump fd1pmcl

label fd1pmcl:
    hide screen locations
    scene frontdoor 1pm 002
    call screen fd1pmcl1

screen fd1pmcl1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 881 ypos 301 action (Hide('fd1pmcl1'), Jump('frontdoor1tits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1241 ypos 543 action (Hide('fd1pmcl1'), Jump('frontdoor1ass')) hovered tt.Action ("Look at ass") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1308 ypos 165 action (Hide('fd1pmcl1'), Jump('frontdoor1talk')) hovered tt.Action ("Talk") focus_mask True
        frame:
            xalign .5
            text tt.value

label frontdoor1tits:
    hide screen locations
    scene frontdoor 1pm 002a
    if inc == True:
        pov "{i}That lucky bastard motorboatin' my big sister's tits.{/i}"
    else:
        pov "{i}That lucky bastard motorboatin' [bs]'s tits.{/i}"
    pov "{i}Soon I'll do that.{/i}"
    jump fd1pmcl

label frontdoor1ass:
    hide screen locations
    scene frontdoor 1pm 002b
    pov "{i}And he can grope that hot ass.{/i}"
    pov "{i}That should be my duty only.{/i}"
    jump fd1pmcl

label frontdoor1talk:
    hide screen locations
    pov "Ahem..."
    scene frontdoor 1pm 003
    if bigsisrelationship < 30 and bigsisntr == True:
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
        martin "Now I get meet my girlfriends brother for the first time. She told me much about you."
        pov "{i}This is my big sister's boyfriend?{/i}"
    else:
        martin "Now I get meet my you for the first time. She told me much about you."
        pov "{i}This is my [bs]'s boyfriend?{/i}"
    pov "{i}An emo? That's not what I expected...{/i}"
    jump fd1pmemo

label fd1pmemo:
    call screen fd1pmemo1

screen fd1pmemo1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 939 ypos 174 action (Hide('fd1pmemo1'), Jump('frontdoor1emoapprove')) hovered tt.Action ("Greet him nice [gd1]") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1142 ypos 174 action (Hide('fd1pmemo1'), Jump('frontdoor1emodisapprove')) hovered tt.Action ("Greet him rude [bd1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label frontdoor1emoapprove:
    $ frontd1approve = True
    pov "Hi, i'm [pov]. Nice to meet you."
    pov "It seems you're a nice guy with some manners."
    scene frontdoor 1pm 005
    if inc == True:
        martin "I'm surprised. Your brother seems to be a nice guy, not like you told me."
    else:
        martin "I'm surprised. He seems to be a nice guy, not like you told me."
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
    bs "I told you before."
    $ martinbad += 1
    jump fd1pmwatch

label fd1pmwatch:
    if frontd1approve == True:
        scene frontdoor 1pm 005
    else:
        scene frontdoor 1pm 007
    call screen fd1pmwatch1

screen fd1pmwatch1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 990 ypos 107 action (Hide('fd1pmwatch1'), Jump('frontdoor1lookemo')) hovered tt.Action ("Look at him") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1139 ypos 107 action (Hide('fd1pmwatch1'), Jump('frontdoor1talk2')) hovered tt.Action ("Stop looking") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1086 ypos 485 action (Hide('fd1pmwatch1'), Jump('frontdoor1lookbstits')) hovered tt.Action ("Look at tits") focus_mask True
        frame:
            xalign .5
            text tt.value

label frontdoor1lookbstits:
    scene frontdoor 1pm 006
    pov "{i}Damn, I can't get enough of her tits. Seeing them through that transparent top.{/i}"
    jump fd1pmwatch

label frontdoor1lookemo:
    scene frontdoor 1pm 006a
    pov "{i}Is he really wearing make up?{/i}"
    pov "{i}And that silly look. A true emo?{/i}"
    jump fd1pmwatch

label frontdoor1talk2:
    scene frontdoor 1pm 008
    pov "So you two are together. Surprising."
    bs "Is that so?"
    pov "And what are you doing with your life, Martin? Wearing that stuff?"
    martin "I'm a famous singer with my band."
    pov "Band?"
    scene frontdoor 1pm 009
    martin "We're \"The Chosen\"!"
    bs "His band is really famous. And i'm his groupie."
    jump fd1pmband

label fd1pmband:
    call screen fd1pmband1

screen fd1pmband1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1100 ypos 158 action (Hide('fd1pmemo1'), Jump('frontdoor1bandapprove')) hovered tt.Action ("Congratulate them [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1271 ypos 158 action (Hide('fd1pmemo1'), Jump('frontdoor1banddisapprove')) hovered tt.Action ("Make fun of them [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label frontdoor1bandapprove:
    pov "Wow congratulations. You found a great boyfriend, [bs]."
    scene frontdoor 1pm 010a
    if inc == True:
        martin "Thank you man! It's good to her it from her brother."
    else:
        martin "Thank you man! It's good to her it from you."
    bs "Yes, isn't he sweet?"
    martin "You're always welcome at our concerts!"
    pov "You're welcome."
    $ frontd1approve = False
    $ frontd1disapprove = False
    $ bigsislove += 1
    $ bigsisrelationship += 1
    $ dtime += 1
    $ frontdoor1pmfirst = True
    jump frontdoor

label frontdoor1banddisapprove:
    pov "Is that the music about \"sucking dicks\" that [bs] hearing all the time?"
    scene frontdoor 1pm 010b
    martin "Sucking what?"
    bs "What...? That's not true!"
    martin "What does he mean?"
    bs "He's lying! I don't hear such music!"
    pov "{i}Hahaha...{/i}"
    $ frontd1approve = False
    $ frontd1disapprove = False
    $ bigsiscorruption += 1
    $ bigsisrelationship += 1
    $ dtime += 1
    $ frontdoor1pmfirst = True
    jump frontdoor


label frontdoor21closer:
    hide screen locations
    scene frontdoor 9pm 002
    pov "{i}Damn, it's so hot what they're wearing. And [irina]!{/i}"
    pov "{i}It would be damn nice if they took me with them, wherever they go in those outfits.{/i}"
    jump fd21la

label fd21la:
    hide screen locations
    scene frontdoor 9pm 002
    call screen fd21la1

screen fd21la1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 840 ypos 605 action (Hide('fd21la1'), Jump('frontdoor21look')) hovered tt.Action ("Look at ass") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1271 ypos 158 action (Hide('fd21la1'), Jump('frontdoor21talk')) hovered tt.Action ("Talk") focus_mask True
        frame:
            xalign .5
            text tt.value

label frontdoor21look:
    scene frontdoor 9pm 002a
    pov "{i}That dress is so wonderfully transparent. And it hides only the right places.{/i}"
    pov "{i}Her ass is so firm.{/i}"
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
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_gift_%s.png" xpos 905 ypos 104 action (Hide ('fd21talk3'), Show('giftfd21icon', transition=None)) hovered tt.Action ("Give someone a gift") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 905 ypos 231 action (Hide('fd21talk3'), Jump('frontdoor21talk4')) hovered tt.Action ("Don't give anyone a gift") focus_mask True
        frame:
            xalign .5
            text tt.value






label frontdoor21talk4:
    scene frontdoor 9pm 004
    bs "I'll go inside now. See you tomorrow [irina]."
    irina "Okay, see you."
    pov "{i}Oh she wants to stay with me.{/i}"
    scene frontdoor 9pm 005
    irina "It's nice to meet you again."
    pov "Oh yes."
    irina "So... you really like my outfit?"
    pov "Hmm..."
    pov "Maybe I can see the back too?"
    scene frontdoor 9pm 005a
    irina "And...?"
    pov "{i}That transparency is killing me. Like she is almost naked.{/i}"
    pov "Hmm..."
    scene frontdoor 9pm 006
    irina "Don't make me wait any longer. Let me know what you think."
    irina "It's sexy, isn't it?"
    jump fd21dc

label fd21dc:
    call screen fd21dc1

screen fd21dc1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 560 ypos 158 action (Hide('fd21dc1'), Jump('frontdoor21love')) hovered tt.Action ("Answer to improve Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1100 ypos 158 action (Hide('fd21dc1'), Jump('frontdoor21cor')) hovered tt.Action ("Answer to improve Corruption [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label frontdoor21cor:
    pov "It's really sexy and the right thing a girl like you should wear."
    scene frontdoor 9pm 007c
    pov "A girl who wants to drive the men crazy and show off that she's willing to earn her stuff."
    irina "Like a prostitute?"
    pov "No! You're not a prostitute. More like a hot chick that knows exactly what to do to get what you want."
    irina "So you like me in this outfit."
    pov "Yes! And I think you should reward me more for my approval."
    scene frontdoor 9pm 008c
    irina "Like showing off more of me?"
    pov "Right. That's a good idea to begin."
    pov "Show off your smokin' hot body."
    irina "Okay..."
    pov "Play more with me and we can come together."
    scene frontdoor 9pm 009c
    irina "Like that...?"
    pov "Holy shit! That's hot."
    pov "And especially that hole at the right place of your dress."
    irina "Thank you..."
    scene frontdoor 9pm 010c
    pov "And I'm very sure you show yourself off in that outfit because your waiting for someone who takes advantage!"
    pov "You're not that type of girl who dress like this because the others like [bs] do."
    irina "Hmm..."
    pov "You're soft skin. And you're shivering."
    irina "Hmm..."
    pov "So I am right with my assumption?"
    scene frontdoor 9pm 011c
    irina "Hmm..."
    pov "So that sound much like a \"yes\" to me."
    pov "I'm glad that I found a sexy girl like you."
    pov "I'll call you soon and then we can go out together!"
    irina "Hmm... okay..."
    $ irinacorruption += 1
    $ dtime += 1
    $ frontdoor9pmfirst = True
    jump frontdoor

label frontdoor21love:
    pov "I think it could be more conservative. A beautiful girl like you doesn't need to show off so much."
    pov "You can wear anything and would look like the most beautiful girl in the world."
    scene frontdoor 9pm 007a
    irina "Oh my god! That's the most beautiful thing that someone has said to me ever!"
    pov "You're welcome."
    irina "You're really so much different to all the other men around."
    irina "With such good manners."
    pov "Oh and there is more. Come here."
    scene frontdoor 9pm 008a
    irina "Oh wow, another hug again."
    pov "Yes, I see you need that."
    scene frontdoor 9pm 009a
    irina "You can do that anytime you want. No one ever does that before without asking for a reward."
    pov "Hmm..."
    irina "I feel myself with so much worth in your arms."
    $ irinalove += 1
    jump fd21ga

label fd21ga:
    call screen fd21ga1

screen fd21ga1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_abort_love_%s.png" xpos 438 ypos 447 action (Hide('fd21ga1'), Jump('frontdoor21nogrope')) hovered tt.Action ("Don't [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 438 ypos 636 action (Hide('fd21ga1'), Jump('frontdoor21grope')) hovered tt.Action ("Grope her ass [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label frontdoor21grope:
    scene frontdoor 9pm 009b
    pov "And a hug grants some privileges too."
    irina "Eh?"
    pov "Enjoying the firm ass of a nice girl."
    "You knead her ass-cheeks."
    scene frontdoor 9pm 010b
    irina "Hmm..."
    pov "That sort of hug is even nicer, isn't it?"
    irina "Hmm... I don't know..."
    scene frontdoor 9pm 011b
    irina "So we'll meet again?"
    pov "{i}Hmm... maybe was that groping to much. She's not to happy anymore like before.{/i}"
    pov "Yes, I'm very interested."
    irina "Then please call me. You're still a better mate then the others here."
    pov "{i}Still? Oh I'll show you.{/i}"
    pov "Sure, I will."
    $ irinacorruption += 1
    $ dtime += 1
    $ frontdoor9pmfirst = True
    jump frontdoor

label frontdoor21nogrope:
    scene frontdoor 9pm 011a
    irina "I still can't believe it. That such a wonderful man shows interest in me."
    pov "And I can't believe that such an amazing girl like you doesn't have a boyfriend. You don't have one, do you?"
    irina "No. But I hope that will change soon."
    pov "Oh so you're really interested in such a normal guy like me?"
    scene frontdoor 9pm 012a
    irina "Oh, you're playing with me? <giggle>"
    irina "Please call me so we can get out soon. I want to hang out more with a nice person like you."
    pov "Okay, then I'll do that, my lady."
    irina "Oh my god. You make me blush so much."
    irina "Don't make me wait to long or I'll go crazy."
    pov "Haha, okay.."
    $ irinalove += 1
    $ dtime += 1
    $ frontdoor9pmfirst = True
    jump frontdoor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
