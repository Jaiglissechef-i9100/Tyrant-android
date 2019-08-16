




label lroom8momslap:
    hide screen locations
    scene livingroom 8am 002
    pov "{i} Let's slap that ass!{/i}"
    with vpunch
    $ momcorruption += 1
    scene livingroom 8am 003
    mom "Aaaahh..."
    pov "{i}Damn, that was hot.{/i}"
    $ vlroom8momslap += 1
    jump lroom8momtalk

label lroom8momlook:
    hide screen locations
    if nicolereddresswear == True:
        scene livingroom 8am 001acc1
    elif nicolebabydollwear == True:
        scene livingroom 8am 001acc2
    elif nicolesweaterpantswear == True:
        scene livingroom 8am 001acl1
    elif nicolerobewear == True:
        scene livingroom 8am 001acl2
    else:
        scene livingroom 8am 001a
    pov "{i}Her ass is so damn hot, I can't stop looking.{/i}"
    jump lroom



label lroom8momtalk:
    hide screen locations
    $ momrelationship +=1
    if vlroom8momslap == 1:
        scene livingroom 8am 004
        if momrelationship < 30 and momntr == True:
            $ randomnum = renpy.random.randint(1,2)
            if randomnum == 1:
                jump nicoleshakylroom
            elif randomnum == 2:
                " "
        mom "Why did you do that?"
        pov "Calm down!"
        mom "You slapped me! Are you insane?"
        pov "It has to be done. I'm trying to play the bad ass."
        scene livingroom 8am 005
        mom "Oh... but is there a need for you to slap me?"
        pov "Yes when your sticking your ass out like that I slap it like a bad boy would do!"
        if inc == True:
            mom "But I'm your mother!"
        else:
            mom "You can't do that to me!"
        pov "No, in this bad play you're just another bitch."
        mom "But..."
        pov "I'm just trying to play my role good."
        mom "..."
        if vlroom8momtalknight2 == True:
            jump lroom8momtalk3
        if NTR == True and inc == True:
            pov "By the way, you were in the basement that night with dad's friends?"
            mom "Y... yes, but why are you asking?"
            pov "What did you do there without dad?"
            mom "We... we just talked and waited for your dad there."
            pov "Can I join you next time?"
            scene livingroom 8am 005a
            mom "No!"
            scene livingroom 8am 005b
            mom "I mean it's not possible yet. It's like their secret hideout and only trusted ones can join in."
            pov "{i}She lied to me. I must find out what she's hiding and what they do down there.{/i}"
            pov "Okay, I understand."
        if NTR == True and inc == False:
            pov "By the way, you were in the basement that night with Bruce's friends?"
            mom "Y... yes, but why are you asking?"
            pov "What did you do there without Bruce?"
            mom "We... we just talked and waited for him there."
            pov "Can I join you next time?"
            scene livingroom 8am 005a
            mom "No!"
            scene livingroom 8am 005b
            mom "I mean it's not possible yet. It's like their secret hideout and only trusted ones can join in."
            pov "{i}She lied to me. I must find out what she's hiding and what they do down there.{/i}"
            pov "Okay, I understand."

    elif vlroom8momslap > 1:
        if momrelationship < 30 and momntr == True:
            $ randomnum = renpy.random.randint(1,2)
            if randomnum == 1:
                jump nicoleshakylroom
            elif randomnum == 2:
                " "
        scene livingroom 8am 005
        mom "Hnnn..."
        pov "You needed that, didn't you?"


        if vlroom8momtalknight2 == True:
            jump lroom8momtalk3
        if NTR == True and inc == True:
            pov "By the way, you were in the basement that night with dad's friends?"
            mom "Y... yes, but why are you asking?"
            pov "What did you do there without dad?"
            mom "We... we just talked and waited for your dad there."
            pov "Can I join you next time?"
            scene livingroom 8am 005a
            mom "No!"
            scene livingroom 8am 005b
            mom "I mean it's not possible yet. It's like their secret hideout and only trusted ones can join in."
            pov "{i}She lied to me. I must find out what she's hiding and what they do down there.{/i}"
            pov "Okay, I understand."
        if NTR == True and inc == False:
            pov "By the way, you were in the basement that night with Bruce's friends?"
            mom "Y... yes, but why are you asking?"
            pov "What did you do there without Bruce?"
            mom "We... we just talked and waited for him there."
            pov "Can I join you next time?"
            scene livingroom 8am 005a
            mom "No!"
            scene livingroom 8am 005b
            mom "I mean it's not possible yet. It's like their secret hideout and only trusted ones can join in."
            pov "{i}She lied to me. I must find out what she's hiding and what they do down there.{/i}"
            pov "Okay, I understand."
    else:
        scene livingroom 8am 004lo
        if momrelationship < 30 and momntr == True:
            $ randomnum = renpy.random.randint(1,2)
            if randomnum == 1:
                jump nicoleshakylroom
            elif randomnum == 2:
                " "
        mom "Oh hey [pov]."
        pov "What are you doing?"
        mom "Removing the alcohol from them last night."
        if vlroom8momtalknight2 == True:
            jump lroom8momtalk3
        pov "Oh I thought it was yours?"
        mom "Haha, no."
        pov "I'm already a little confused about the things that happened yesterday."
        mom "You'll get used to it fast, I know it."
        pov "Yes..."

        if NTR == True and inc == True:
            pov "By the way, you were in the basement that night with dad's friends?"
            mom "Y... yes, but why are you asking?"
            pov "What did you do there without dad?"
            mom "We... we just talked and waited for your dad there."
            pov "Can I join you next time?"
            scene livingroom 8am 004alo
            mom "No!"
            scene livingroom 8am 004blo
            mom "I mean it's not possible yet. It's like their secret hideout and only trusted ones can join in."
            pov "{i}She lied to me. I must find out what she's hiding and what they do down there.{/i}"
            pov "Okay, I understand."
        if NTR == True and inc == False:
            pov "By the way, you were in the basement that night with Bruce's friends?"
            mom "Y... yes, but why are you asking?"
            pov "What did you do there without Bruce?"
            mom "We... we just talked and waited for him there."
            pov "Can I join you next time?"
            scene livingroom 8am 005a
            mom "No!"
            scene livingroom 8am 005b
            mom "I mean it's not possible yet. It's like their secret hideout and only trusted ones can join in."
            pov "{i}She lied to me. I must find out what she's hiding and what they do down there.{/i}"
            pov "Okay, I understand."

    pov "I liked your playing of your role when you were sitting there in that slutty dress yesterday night."
    if inc == True:
        mom "Your dad choose it for me. He thinks it fits better around his \"friends\"."
    else:
        mom "Bruce choose it for me. He thinks it fits better around his \"friends\"."
    jump l8a1

label l8a1:
    call screen l8a1s

screen l8a1s():
    default tt = Tooltip (" ")

    fixed:
        if vlroom8momslap == 1:
            add "images/livingroom/8am 005.jpg"
        else:
            add "images/livingroom/8am 004lo.jpg"
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 669 ypos 216 action (Hide('l8a1s'), Jump('lroom8momtalklove')) hovered tt.Action ("Answer to improve Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1139 ypos 216 action (Hide('l8a1s'), Jump('lroom8momtalkcor')) hovered tt.Action ("Answer to improve Corruption [cr1]") focus_mask True

    frame:
        xalign .5
        text tt.value

label lroom8momtalklove:
    mom "And I thought it would help too."
    $ momlove += 1
    if vlroom8momslap == 1:
        scene livingroom 8am 006
    else:
        scene livingroom 8am 005lo
    pov "So you're good with this style of clothing?"
    mom "Of course it's not my favorite, but it could be worse."
    pov "You're right. You're doing good."
    mom "Thank you..."
    jump lroom8momtalk2

label lroom8momtalkcor:
    pov "Yes I like that slutty dress too. It shows your assets better."
    $ momcorruption += 1
    if vlroom8momslap == 1:
        scene livingroom 8am 007
    else:
        scene livingroom 8am 006lo
    mom "You shouldn't look at me that way. It's needed for our cover."
    if droom7momlookcor == True:
        pov "You remember what we talked about before? I'll have to get used to it."
        mom "Yes..."
    else:
        if inc == True:
            pov "Sure! You should take it as a compliment! Not everyone's mom look so hot in a short dress."
            mom "But... please stop it."
            pov "Come on mom. No need to be embarrassed. I know this isn't your usual style of clothing."
        else:
            pov "Sure! You should take it as a compliment! You look so hot in a short dress."
            mom "But... please stop it."
            pov "Come on [mother]. No need to be embarrassed. I know this isn't your usual style of clothing."
        mom "O... okay..."
    jump lroom8momtalk2


label lroom8momtalk2:
    if vlroom8momslap == 1:
        scene livingroom 8am 010
    else:
        scene livingroom 8am 010lo
    pov "What else are you going to do today?"
    mom "I'm going out with a friend. I'll be back about midday."
    pov "A male friend?"
    mom "No. Getting a manicure to stay beautiful for this role."
    pov "Oh, have fun there."
    mom "Thank you [pov]!"
    jump l8a2

label l8a2:
    call screen l8a2s

screen l8a2s():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_hug_%s.png" xpos 675 ypos 216 action (Hide('l8a2s'), Jump('lroom8momtalklove2')) hovered tt.Action ("Hug [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1185 ypos 216 action (Hide('l8a2s'), Jump('lroom8momtalkcor2')) hovered tt.Action ("Don't hug") focus_mask True

    frame:
        xalign .5
        text tt.value

label lroom8momtalklove2:
    if inc == True:
        pov "Come here mom."
    else:
        pov "Come here [mother]."
    mom "Oh..."
    if vlroom8momslap == 1:
        scene livingroom 8am 008
    else:
        scene livingroom 8am 008lo
    if vlroom8momhug >= 1:
        mom "Another hug?"
        pov "Yes."
        mom "I could get used to this."
    else:
        mom "What is that for?"
        if inc == True:
            pov "I just want to hug my mom in the morning."
        else:
            pov "I just want to hug you in the morning."
        mom "That's so sweet, [pov]!"
    $ vlroom8momhug += 1
    $ momlove += 1
    pov "You're welcome."


label lroom8momtalkcor2:
    if vlroom8momslap == 1:
        scene livingroom 8am 009
    else:
        scene livingroom 8am 009lo
    mom "Then see you later. And you could try to find a job or do anything else around the house."
    pov "And if I want to go in town?"
    mom "Please don't do that yet. It's better if someone accompanies you there the first time."
    mom "Thru this playing there are some people who don't like us."
    pov "Oh, gang enemies?"
    mom "Yes, something like that."
    pov "Ok. See you later."
    $ vlroom8momtalknight2 = True
    $ dtime = 9
    jump lroom




label lroom10bsistits:
    hide screen locations
    scene livingroom 10am 002b
    pov "{i}Damn she's so hot right now. Her fine boobs and she's so beautiful concentrating at staying in shape.{/i}"
    jump lroom

label lroom10bsiscrotch:
    hide screen locations
    scene livingroom 10am 002a
    pov "{i}Only those little panties are hiding her pussy from me. And I'm sure her asshole is tight and sexy too.{/i}"
    jump lroom

label lroom10bsisfeet:
    hide screen locations
    scene livingroom 10am 002c
    pov "{i}Her cute little feet.{/i}"
    jump lroom

label lroom10bsistalk:
    hide screen locations
    scene livingroom 10am 003
    if bigsisrelationship < 30 and bigsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump cassandrashakylroom
        elif randomnum == 2:
            " "
    $ bigsisrelationship += 1
    pov "Hey [bs]."
    bs "Oh you... What you're looking for, little perv?"
    pov "Oh I'm just seeing what's going on over the day here in my new home."
    pov "What are you doing?"
    scene livingroom 10am 004
    if vlroom10trainfirst == True:
        bs "I'm training again, dummy."
    else:
        bs "I'm training, can't you see?"
    pov "Oh yeah, sure."
    bs "I do my best to stay in shape, not like ordinary girls."
    scene livingroom 10am 005
    pov "Oh and with a personal trainer."
    bs "Yes there are always new lessons and they're very good."
    scene livingroom 10am 006
    bs "It's sometimes a little hard but it's necessary."
    pov "{i}I know something else what is also getting hard right now.{/i}"
    pov "Yeah these lessons seem to be a good thing."
    scene livingroom 10am 007
    if vlroom10trainfirst == True:
        bs "Can you help me again?"
        if vlroom10firstposcor == True:
            bs "But this time do it right please."
            pov "Hmm... sure."
    else:
        bs "When you're here you could help me!"
        pov "Help you?"
        pov "{i}Yes let me help you!{/i}"
        bs "Count on that I know when I have to change position."
        pov "Hmm...?"
        bs "Sit down I'll tell you."
        scene livingroom 10am 008
        pov "{i}Damn fucking god!{/i}"
        bs "There will be a counter going down at the show, but I can't see it from here. So count down for me."
        scene livingroom 10am 009b
        pov "{i}But then I won't see you anymore...{/i}"
        bs "Can you do this for me?"
    $ vlroom10trainfirst = True
    jump lroom10ft

label lroom10ft:
    scene livingroom 10am 009b
    call screen lroom10ft1

screen lroom10ft1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 590 ypos 750 action (Hide('lroom10ft1'), Jump('lroom10bsisfirsttrainlove')) hovered tt.Action ("Help her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1161 ypos 750 action (Hide('lroom10ft1'), Jump('lroom10bsisfirsttraincor')) hovered tt.Action ("Help her [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value


label lroom10bsisfirsttrainlove:
    pov "Okay, I'll do it."
    bs "Great, let's get started."
    pov "5"
    bs "..."
    pov "4"
    bs "Hnn..."
    pov "{i}Just a quick look.{/i}"
    scene livingroom 10am 009a
    bs "Hmm..."
    pov "{i}Damn I'm missing the best show. But I told her I would help.{/i}"
    scene livingroom 10am 009b
    pov "3"
    pov "At least the girl on the TV isn't that bad either."
    bs "Hmm..."
    pov "2"
    bs "Hah..."
    pov "{i}She's moaning from the effort. So hot.{/i}"
    pov "1"
    bs "Hah..."
    pov "Done."
    scene livingroom 10am 010b
    bs "You did good. At least something you can, haha."
    pov "You're welcome."
    pov "{i}Interesting. When she wants something she isn't a bitch.{/i}"
    $ vlroom10firstposlove = True
    $ vlroom10firstposcor = False
    $ bigsislove += 1
    scene livingroom 10am 011b
    if vlroom10trainfirst == True:
        bs "Could you help again?"
        if vlroom10secposcor == True:
            bs "But don't dare to grope my tits again!"
            pov "Okay..."
        else:
            bs "You were such a good help last time."
            pov "Okay..."
    else:
        bs "Oh, that lesson is good, but I could never do it."
        pov "Why?"
        bs "There are two people needed and normally I'm all alone at this time."
        scene livingroom 10am 012
        bs "But you can help me out again, can you?"
        pov "Again?"
        bs "Yes please! The lesson will affect your fitness too."
        pov "But I'm in good shape?"
        bs "Come on, please!"
    jump lroom10ft2

label lroom10ft2:
    scene livingroom 10am 012
    call screen l10ft3

screen l10ft3():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 590 ypos 750 action (Hide('lroom10ft1'), Jump('lroom10bsissectrainlove')) hovered tt.Action ("Help her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1161 ypos 750 action (Hide('lroom10ft1'), Jump('lroom10bsissectraincor')) hovered tt.Action ("Help her [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom10bsissectrainlove:
    pov "Okay, I can do that."
    bs "Good stay there."
    scene livingroom 10am 013
    pov "{i}Wow, she's pressing her ass on my dick. I wonder what will happen when she notices my boner.{/i}"
    bs "I will fall now slowly forward and you have to hold me."
    pov "Okay...?"
    pov "{i}Then she'll press her hot body on me, damn. And her soft skin.{/i}"
    bs "It's good for most of the body parts especially for the ass."
    pov "Okay!"
    pov "{i}Then I'll love that too.{/i}"
    bs "Ready?"
    pov "Sure."
    scene livingroom 10am 014
    bs "Don't let me fall over."
    pov "Sure, I can hold you, don't worry."
    pov "{i}Oh my god her ass is killing me. I want to fuck her now!{/i}"
    bs "Oh this is good, I can feel it stretching my muscles."
    pov "Hell yeah."
    bs "Hmm...?"
    pov "Oh nothing, it's alright."
    scene livingroom 10am 015
    bs "You're doing good as a training partner. Just a moment longer."
    pov "{i}I could hold you all my life in this position.{/i}"
    pov "Sure."
    bs "Hmm..."
    pov "{i}Did she notice my boner? But she's not stopping? Or does she want to do this training position that badly?{/i}"
    bs "O... okay, that's it."
    pov "{i}Nooo...{/i}"
    scene livingroom 10am 016
    if vlroom10secposlove == True:
        bs "Wow! You did as good as last time. You could be my personal trainer, haha."
        pov "..."
        pov "{i}You have no idea.{/i}"
        bs "Relax, I'm just kidding, haha."
    else:
        bs "Wow I'm surprised. You didn't act like a jerk and really helped me."
        pov "Okay..."
        bs "And you didn't try pervy things. Maybe you really learned manners overseas."
        pov "If you say so."
        pov "{i}Then she didn't notice my boner, but is this good?{/i}"
        if inc == True:
            bs "Well... thank you very much little brother."
        else:
            bs "Well... thank you very much [pov]."
    pov "Alright, no problem. Feel free to ask again."
    $ vlroom10secposlove = True
    $ vlroom10secposcor = False
    $ bigsislove += 1
    $ dtime = 11
    jump lroom

label lroom10bsisfirsttraincor:
    pov "Okay, I'll do it."
    bs "Great, let's get started."
    pov "5"
    pov "{i}I don't care about this shit, I must see her.{/i}"
    scene livingroom 10am 009a
    bs "..."
    pov "{i}Such a hot position. Maybe she can do some naked training some time for me, haha?{/i}"
    bs "What's wrong?"
    pov "Oh, 4..."
    scene livingroom 10am 008
    pov "{i}Relax... Calm down...{/i}"
    bs "Hmm..."
    bs "..."
    pov "Ahem... 3"
    scene livingroom 10am 009a
    pov "{i}That's more enduring for me then for her.{/i}"
    bs "Hnn..."
    bs "..."
    scene livingroom 10am 010a
    if vlroom10firstposcor == True:
        bs "You did it again!"
        pov "But..."
        bs "You're no help to me!"
    else:
        bs "What are you doing you idiot?"
        pov "{i}Oh... oh...{/i}"
        bs "Your counting is totally wrong!"
        pov "I... I just..."
        bs "I should've known you would suck at helping, you jerk!"
    pov "..."
    $ vlroom10firstposlove = False
    $ vlroom10firstposcor = True
    $ bigsiscorruption += 1
    $ dtime = 11
    jump lroom

label lroom10bsissectraincor:
    pov "Okay, I can do that."
    bs "Good stay there."
    scene livingroom 10am 013
    pov "{i}Wow, she's pressing her ass on my dick. I wonder what would happen if she noticed my boner.{/i}"
    bs "I will fall now slowly forward and you have to hold me."
    pov "Okay...?"
    pov "{i}Then she'll press her hot body on me, damn. And her soft skin.{/i}"
    bs "It's good for most of the body parts especially for the ass."
    pov "Okay!"
    pov "{i}Then I'll love that too.{/i}"
    bs "Ready?"
    pov "Sure."
    scene livingroom 10am 014
    bs "Don't let me fall over."
    pov "Sure, I can hold you, don't worry."
    pov "{i}Oh my god her ass is killing me. I want to fuck her now!{/i}"
    bs "Oh this is good, I can feel it stretching my muscles."
    pov "Hell yeah."
    bs "Hmm...?"
    pov "{i}Maybe it's time to rescue her from falling over.{/i}"
    scene livingroom 10am 015a
    bs "Huh? What?"
    if inc == True:
        pov "It's okay big sis, I'm holding you, you won't fall over."
    else:
        pov "It's okay [bs], I'm holding you, you won't fall over."
    bs "Stop it!"
    pov "No! You'll fall over. I'm preventing that."
    pov "{i}I'll never get my hands off these firm boobs.{/i}"
    scene livingroom 10am 016a
    if vlroom10secposcor == True:
        bs "You groped me again, you jerk!"
        pov "No I just wanted to rescue you like last time."
        bs "Are you that stupid you think I'm too dumb to not fall over?"
        pov "No... but..."
        bs "Fuck you!"
    else:
        bs "You damn asshole. I should have known that you take the chance to grope me."
        pov "No. I just wanted to prevent that you from falling over."
        bs "Sure! You're still a pervert!"
        pov "But you wanted me to do that. I was just trying to help."
        bs "..."
        bs "Maybe... but I don't think so..."
        pov "I'm telling the truth."
        pov "{i}I would say anything for those boobs.{/i}"
    $ vlroom10secposlove = False
    $ vlroom10secposcor = True
    $ bigsiscorruption += 1
    $ dtime = 11
    jump lroom



label lroom15tits:
    hide screen locations
    hide screen townl
    scene livingroom 3pm 002a
    pov "{i}Wow what a nice rack. And those lips too.{/i}"
    jump lroom

label lroom15crotch:
    hide screen locations
    hide screen townl
    scene livingroom 3pm 002b
    pov "{i}That flat belly. I wonder if she's shaved and what her ass looks like.{/i}"
    jump lroom

label lroom15talk:
    hide screen locations
    hide screen townl
    if irinafirstmeet == True:
        jump lroom15repeat
    "You get closer to her."
    $ bigsisrelationship += 1
    $ irinarelationship += 1
    scene livingroom 3pm 003
    pov "{i}I wonder who she is? Maybe a friend of a family member?{/i}"
    pov "{i}Time to find out.{/i}"
    pov "Hi!"
    "Girl" "Eh?"
    scene livingroom 3pm 004a
    pov "{i}Wow, she's checking me out.{/i}"
    scene livingroom 3pm 004b
    "Girl" "Oh, hello."
    pov "Hello, I'm [pov]. I live here."
    "Girl" "Really? I didn't see you before."
    pov "I was overseas for a year. And you are?"
    "Girl" "Oh how rude of me."
    if irinafirstmeet == False:
        $ irina = renpy.input(_("My name is...")) or _("Irina")
    scene livingroom 3pm 005
    pov "Nice to meet you [irina]!"
    irina "Oh... I mean nice to meet you too."
    pov "Did I do something wrong?"
    scene livingroom 3pm 006
    irina "No! But it doesn't happen often here, that someone shakes hands."
    pov "No?"
    irina "Most people here are rude or egoists."
    irina "So that was a very nice surprise."
    pov "Oh then you're welcome."
    scene livingroom 3pm 007
    if inc == True:
        irina "So you're the little brother of [bs]?"
    else:
        irina "So you're living with the family of [bs]?"
    pov "Oh she told you about me?"
    irina "Some things. But not how cute you are. <giggle>"
    pov "Oh you're also a very sexy girl."
    scene livingroom 3pm 008
    bs "I'm done! We can go [irina]."
    irina "Maybe I'm good here."
    bs "What do you..."
    scene livingroom 3pm 009
    if inc == True:
        bs "Oh! It's my little brother!"
    else:
        bs "Oh! It's him!"
    bs "Did you try to do your pervy things to my friend?"
    irina "<giggle>"
    bs "Be aware of him. He's a pervert!"
    scene livingroom 3pm 010
    bs "So it's time to go [pov]. You saw my friend and now it's time for your business."
    pov "But maybe I want to hang out with you."
    bs "Cut it out! I have no time for your games."
    irina "I think I like him."
    bs "No you don't. He must have tricked you."
    jump lr3gf

label lr3gf:
    call screen lr3gf1

screen lr3gf1:
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1077 ypos 153 action (Hide('lr3gf1'), Jump('lroom15love')) hovered tt.Action ("Answer to improve Love [lv1]/[bs]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 807 ypos 153 action (Hide('lr3gf1'), Jump('lroom15cor')) hovered tt.Action ("Answer to improve Corruption [cr1]/[bs]") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom15love:
    pov "Don't worry [irina]. She isn't always so mad."
    pov "It's just time for a hug!"
    scene livingroom 3pm 011b
    bs "What are you..."
    pov "Come here! No one is mad at you, calm down."
    irina "Oh..."
    bs "What..."
    scene livingroom 3pm 012b
    bs "Are you fucking crazy? Hugging me out of nowhere!"
    pov "You're welcome!"
    bs "I'll kill you. Doing that in front of my friend!"
    irina "Wow. That was so sweet of you."
    irina "Maybe... I can have a hug too?"
    $ bigsislove += 1
    jump lr3irina

label lroom15cor:
    pov "I'm sorry [irina], but [bs] wants me all alone to be her lover."
    pov "She tell everyone that I'm a pervert to isolate me for her."
    scene livingroom 3pm 012a
    bs "Are you fucking crazy? What the hell are you talking about?"
    irina "Hahahaha..."
    pov "Don't be mad, I'm sure [irina] will keep the secret."
    bs "How dare you..."
    irina "I've never laughed that hard. Wonderful!"
    bs "And you're on his side. You crazy bitch."
    irina "Hahahaha..."
    bs "Fuck you two..."
    $ bigsiscorruption += 1
    jump lroom15bend

label lr3irina:
    call screen lr3irina1

screen lr3irina1:
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1077 ypos 153 action (Hide('lr3irina1'), Jump('lroom15mlove')) hovered tt.Action ("Answer to improve Love [lv1]/[irina]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 807 ypos 153 action (Hide('lr3irina1'), Jump('lroom15mcor')) hovered tt.Action ("Answer to improve Corruption [cr1]/[irina]") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom15mcor:
    pov "No, not now. That's something you have to earn."
    irina "Oh, but it looked so nice."
    pov "As I said, maybe sometime you earned it for yourself."
    irina "<giggle> Now I'm curious."
    bs "He's just a pervert like I said."
    $ irinacorruption += 1
    jump lroom15gend

label lroom15mlove:
    pov "Sure, come here [irina]!"
    scene livingroom 3pm 013b
    irina "Hmm..."
    pov "Everyone loves to get hugged."
    irina "That's such a sweet idea. It's been a long time since someone hugged me."
    bs "What are..."
    bs "I'm out of here! You can't be serious!"
    $ irinalove += 1
    jump lroom15gend

label lroom15bend:
    scene livingroom 3pm 013a
    irina "Haha, that was amazing. I never saw [bs] her so raging."
    pov "Oh I thought it was fun too."
    irina "You're an interesting guy, maybe we can meet sometime again?"
    pov "Oh sure why not."
    irina "See you [pov]."
    pov "Bye [irina]."
    $ dtime += 1
    $ irinafirstmeet = True
    jump lroom

label lroom15gend:
    scene livingroom 3pm 014
    irina "Wow, you're full of surprises [pov]."
    pov "What do you mean?"
    irina "You're like a true gentleman in that slum. Almost all the men here are jerks against women."
    pov "Maybe you're worth it."
    irina "Oh my god. You're so sweet."
    irina "Can we meet up again, please?"
    pov "Sure, I would be pleased too."
    irina "Oh... <giggle>"
    $ dtime += 1
    $ irinafirstmeet = True
    jump lroom




label lroom14momcloser:
    hide screen locations
    if nicolereddresswear == True:
        scene livingroom 2pm 002ncc1
    elif nicolebabydollwear == True:
        scene livingroom 2pm 002ncc2
    elif nicolesweaterpantswear == True:
        scene livingroom 2pm 002ncl1
    elif nicolerobewear == True:
        scene livingroom 2pm 002ncl2
    else:
        scene livingroom 2pm 002
    if inc == True:
        pov "{i}Oh mom's sleeping. She's so tired all the time.{/i}"
    else:
        pov "{i}Oh [mother]'s sleeping. She's so tired all the time.{/i}"
    jump lroom14momcloser2

label lroom14momcloser2:
    if NTR == True and momrelationship < 6 and momntr == True:
        mom "Ohh..."
        pov "{i}She's dreaming?{/i}"
        mom "Fuck me harder!"
        pov "{i}...{/i}"
        mom "Punish my pussy more with your black rod."
        pov "{i}What, black...? So Davide is fucking her in the basement!{/i}"
        if inc == True:
            pov "{i}That asshole. Fucking my mom. I'll get rid of him and make mom mine again.{/i}"
        else:
            pov "{i}That asshole. Fucking [mother]. I'll get rid of him and make her mine again.{/i}"
        jump lroom14momcloser3
    elif NTR == True and momrelationship >= 6:
        pov "{i}I wonder if what they do in the basement is the reason?{/i}"
        jump lroom14momcloser3
    else:
        pov "{i}I wonder if what they do in the basement is the reason?{/i}"
        jump lroom14momcloser3

label lroom14momcloser3:
    if nicolereddresswear == True:
        scene livingroom 2pm 002ncc1
    elif nicolebabydollwear == True:
        scene livingroom 2pm 002ncc2
    elif nicolesweaterpantswear == True:
        scene livingroom 2pm 002ncl1
    elif nicolerobewear == True:
        scene livingroom 2pm 002ncl2
    else:
        scene livingroom 2pm 002
    jump l14l

label l14l:
    if nicolereddresswear == True:
        scene livingroom 2pm 002ncc1
    elif nicolebabydollwear == True:
        scene livingroom 2pm 002ncc2
    elif nicolesweaterpantswear == True:
        scene livingroom 2pm 002ncl1
    elif nicolerobewear == True:
        scene livingroom 2pm 002ncl2
    else:
        scene livingroom 2pm 002
    call screen l14l1

screen l14l1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 266 ypos 389 action (Hide('l14l1'), Jump('lroom14legs')) hovered tt.Action ("Look at legs") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 14 ypos 389 action (Hide('l14l1'), Jump('lroom14feet')) hovered tt.Action ("Look at feet") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1077 ypos 152 action (Hide('l14l1'), Jump('lroom14momcloser4')) hovered tt.Action ("Stop looking") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom14legs:
    if nicolereddresswear == True:
        scene livingroom 2pm 005ncc1
    elif nicolebabydollwear == True:
        scene livingroom 2pm 005ncc2
    elif nicolesweaterpantswear == True:
        scene livingroom 2pm 005ncl1
    elif nicolerobewear == True:
        scene livingroom 2pm 005ncl2
    else:
        scene livingroom 2pm 005
    pov "{i}Her beautiful legs. And her crotch so near. Wrapped tight in those leggings.{/i}"
    jump l14l

label lroom14feet:
    if nicolereddresswear == True:
        scene livingroom 2pm 002ancl1
    elif nicolebabydollwear == True:
        scene livingroom 2pm 002ancl1
    elif nicolesweaterpantswear == True:
        scene livingroom 2pm 002ancl1
    elif nicolerobewear == True:
        scene livingroom 2pm 002ancl1
    else:
        scene livingroom 2pm 002a
    pov "{i}Her cute feet. All ready to rub on my dick. I wonder if she has ever given a footjob?{/i}"
    jump l14l

label lroom14momcloser4:
    if nicolereddresswear == True:
        scene livingroom 2pm 002ncc1
    elif nicolebabydollwear == True:
        scene livingroom 2pm 002ncc2
    elif nicolesweaterpantswear == True:
        scene livingroom 2pm 002ncl1
    elif nicolerobewear == True:
        scene livingroom 2pm 002ncl2
    else:
        scene livingroom 2pm 002
    pov "{i}Let's have some fun to make her love me more.{/i}"
    pov "{i}So she can get used to my touching.{/i}"
    jump l14grope

label l14grope:
    call screen l14grope1

screen l14grope1():
    default tt = Tooltip (" ")

    fixed:
        if nicolereddresswear == True or nicolerobewear == True or nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
            imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 944 ypos 150 action (Hide('l14grope1'), Jump('lroom14gtits')) hovered tt.Action ("Grope tits [lv1]/[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 266 ypos 389 action (Hide('l14grope1'), Jump('lroom14gcrotch')) hovered tt.Action ("Grope crotch [lv1]/[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1077 ypos 152 action (Hide('l14grope1'), Jump('lroom14abort')) hovered tt.Action ("Let her sleep") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom14gtits:
    if momcorruption < 20 and momlove < 20:
        if inc == True:
            pov "{i}Damn I'm so horny. Mom's sleeping and I want to give her and myself a good time.{/i}"
        else:
            pov "{i}Damn I'm so horny. [mother]'s sleeping and I want to give her and myself a good time.{/i}"
        pov "{i}I need to see them. Her big tits.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 003ncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 003ncl2
        else:
            scene livingroom 2pm 003
        pov "{i}Oh my god! Yes, yes, yes...{/i}"
        pov "{i}More!{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 004ncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 004ncl2
        else:
            scene livingroom 2pm 004
        pov "{i}Ohh... I'm so close. And they are so beautiful. I want to lick them!{/i}"
        mom "Hmm..."
        pov "{i}Shit. She's about to wake up. Better redress her and get out.{/i}"
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

    elif momcorruption > 20 and momcorruption < 40 or momlove > 20 and momlove < 40:
        pov "{i}Damn I'm so horny. She's sleeping and I want to give her and myself a good time.{/i}"
        pov "{i}I need to play with her tits.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 005bncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 005bncl2
        else:
            scene livingroom 2pm 005b
        pov "{i}Yes, they're so soft and warm.{/i}"
        mom "Hmm..."
        pov "{i}Oh yes, she's feeling it in her dream.{/i}"
        if inc == True:
            pov "{i}It's me, your son. Giving you a good time.{/i}"
        else:
            pov "{i}It's me, [pov]. Giving you a good time.{/i}"
        pov "{i}But it's better to stop now. No need for her to catch me.{/i}"
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

    elif momcorruption > 40 or momlove > 40:
        pov "{i}Damn I'm so horny. She's sleeping and I want to give her and myself a good time.{/i}"
        pov "{i}I need to play with her tits again. But this time I want to feel her flesh.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 006bncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 006bncl2
        else:
            scene livingroom 2pm 006b
        pov "{i}Even better! Feel my hand kneading your breast.{/i}"
        if momlove > 40:
            pov "{i}Soon you'll love me.{/i}"
        else:
            pov "{i}Soon you'll be mine.{/i}"
        mom "Hmm... hah..."
        pov "{i}She's moaning, so she likes it. I bet she's dreaming about it.{/i}"
        pov "{i}Time for more.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 007bncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 007bncl2
        else:
            scene livingroom 2pm 007b
        mom "Hah... hah..."
        pov "{i}Damn, is she waking up or is she getting off.{/i}"
        mom "Hmm... hah..."
        if inc == True:
            pov "{i}Wow more like the second one. Enjoy my touching, mom.{/i}"
        else:
            pov "{i}Wow more like the second one. Enjoy my touching, [mother].{/i}"
        if NTR == True and momrelationship < 6 and momntr == True:
            mom "Ohh... hah... yes..."
            mom "Punish me more, my black master!"
            pov "{i}Nooo! It's me [pov]! I'm giving you the good feeling.{/i}"
        mom "Hah... eh...?"
        pov "{i}Oh shit. Now she's about to wake up. I need to stop it fast.{/i}"
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

label lroom14gcrotch:
    if momcorruption < 20 and momlove < 20:
        pov "{i}Damn I'm so horny. She's sleeping and I want to give her and myself a good time.{/i}"
        pov "{i}Let's caress her beautiful legs.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 005cncc1
        elif nicolebabydollwear == True:
            scene livingroom 2pm 005cncc2
        elif nicolesweaterpantswear == True:
            scene livingroom 2pm 005cncl1
        elif nicolerobewear == True:
            scene livingroom 2pm 005cncl2
        else:
            scene livingroom 2pm 005c
        pov "{i}So firm and warm. I wonder if she works out?{/i}"
        pov "{i}But I need to get closer to her pussy!{/i}"
        mom "Hmm..."
        pov "{i}Shit. She's about to wake up. Maybe I'll have another chance.{/i}"
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

    elif momcorruption > 20 and momcorruption < 40 or momlove > 20 and momlove < 40:
        pov "{i}Damn I'm so horny. She's sleeping and I want to give her and myself a good time.{/i}"
        pov "{i}Let's caress her beautiful legs again.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 005cncc1
        elif nicolebabydollwear == True:
            scene livingroom 2pm 005cncc2
        elif nicolesweaterpantswear == True:
            scene livingroom 2pm 005cncl1
        elif nicolerobewear == True:
            scene livingroom 2pm 005cncl2
        else:
            scene livingroom 2pm 005c
        pov "{i}Starting slowly. Maybe I can reach her pussy this time?{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 006cncc1
        elif nicolebabydollwear == True:
            scene livingroom 2pm 006cncc2
        elif nicolesweaterpantswear == True:
            scene livingroom 2pm 006cncl1
        elif nicolerobewear == True:
            scene livingroom 2pm 006cncl2
        else:
            scene livingroom 2pm 006c
        pov "{i}Oh yes, that's good.{/i}"
        pov "{i}Is she having a wet dream? I can feel her pussy so good through the leggings.{/i}"
        mom "Hmm..."
        pov "{i}Oh yes, she's feeling it in her dream.{/i}"
        pov "{i}It's me, [pov]. Giving you a good time.{/i}"
        pov "{i}But it's better to stop now. No need for her to catch me.{/i}"
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

    elif momcorruption > 40 or momlove > 40:
        pov "{i}Damn I'm so horny. She's sleeping and I want to give her and myself a good time.{/i}"
        pov "{i}I think now it's time to play with her pussy.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 005ancc1
        elif nicolebabydollwear == True:
            scene livingroom 2pm 005ancc2
        elif nicolesweaterpantswear == True:
            scene livingroom 2pm 005ancl1
        elif nicolerobewear == True:
            scene livingroom 2pm 005ancl2
        else:
            scene livingroom 2pm 005a
        pov "{i}Yes, yes, yes. I'm rubbing her pussy.{/i}"
        pov "{i}And she's already a little wet. She must be dreaming something good.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 006ancc1
        elif nicolebabydollwear == True:
            scene livingroom 2pm 006ancc2
        elif nicolesweaterpantswear == True:
            scene livingroom 2pm 006ancl1
        elif nicolerobewear == True:
            scene livingroom 2pm 006ancl2
        else:
            scene livingroom 2pm 006a
        mom "Hmm... hah... hah..."
        pov "{i}Very nice. She's enjoying my touch.{/i}"
        if inc == True:
            pov "{i}You're so damn sexy mom. I'll give you an even better time.{/i}"
        else:
            pov "{i}You're so damn sexy [mother]. I'll give you an even better time.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 007ancc1
        elif nicolebabydollwear == True:
            scene livingroom 2pm 007ancc2
        elif nicolesweaterpantswear == True:
            scene livingroom 2pm 007ancl1
        elif nicolerobewear == True:
            scene livingroom 2pm 007ancl2
        else:
            scene livingroom 2pm 007a
        mom "Hah... ahh..."
        pov "{i}Wow, she spread her legs. She's really enjoying it.{/i}"
        if inc == True:
            pov "{i}Yes mom, enjoy yourself while your son is getting you off.{/i}"
        else:
            pov "{i}Yes [mother], enjoy yourself while I'm getting you off.{/i}"
        if nicolereddresswear == True:
            scene livingroom 2pm 008ancc1
        elif nicolebabydollwear == True:
            scene livingroom 2pm 008ancc2
        elif nicolesweaterpantswear == True:
            scene livingroom 2pm 008ancl1
        elif nicolerobewear == True:
            scene livingroom 2pm 008ancl2
        else:
            scene livingroom 2pm 008a
        mom "Hmm... hah... hah..."
        pov "{i}Damn, is she waking up or is she getting off.{/i}"
        mom "Hmm... hah..."
        if inc == True:
            pov "{i}Wow more like the second one. Enjoy my touch, mom.{/i}"
        else:
            pov "{i}Wow more like the second one. Enjoy my touch, [mother].{/i}"
        if NTR == True and momrelationship < 6 and momntr == True:
            mom "Ohh... hah... yes..."
            mom "Ram your hard dick in your slut, Davide!"
            pov "{i}Nooo! It's me [pov]! I'm giving you this good feeling.{/i}"
        mom "Hah... eh...?"
        pov "{i}Oh shit. Now she's about to wake up. I need to stop it fast.{/i}"
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

label lroom14abort:
    if nicolereddresswear == True:
        scene livingroom 2pm 002ncc1
    elif nicolebabydollwear == True:
        scene livingroom 2pm 002ncc2
    elif nicolesweaterpantswear == True:
        scene livingroom 2pm 002ncl1
    elif nicolerobewear == True:
        scene livingroom 2pm 002ncl2
    else:
        scene livingroom 2pm 002
    pov "{i}No, I'll let her sleep.{/i}"
    $ momrelationship += 1
    $ dtime += 1
    jump lroom


label lroom21talk:
    hide screen locations
    scene livingroom 9pm 002
    davide "Hey bro!"
    if inc == True:
        dad "Son!"
    else:
        dad "[pov]!"
    if jobdone >= 2:
        $ jobgang = False
        jump basementgo
    if frontdoorddfirst == True and gangmember == False:
        davide "I know we had a bad start, but I'll give you a second chance."
    else:
        davide "Good to see you!"
    scene livingroom 9pm 004
    davide "We could use your help!"
    pov "What do you want?"
    davide "You need to deliver something for me."
    pov "Deliver? And what is it?"
    scene livingroom 9pm 005
    if gangmember == True:
        davide "A good chance to become a full gang member with some benefits."
        pov "Some benefits?"
        davide "When you do this for me you'll be trustworthy."
        davide "And can help our preparations in the basement."
        pov "{i}The basement, huh? Then I'd know what happens there.{/i}"
        pov "And what would I have to do?"
        davide "I'll tell you then, but first I want your decision."
        dad "Do it! It's a good chance."
    else:
        davide "A second chance to become a full gang member with some benefits."
        pov "Some benefits?"
        davide "When you do this for me you'll be trustworthy."
        davide "And can help our preparations in the basement."
        pov "{i}The basement, huh? Then I'd know what happens there.{/i}"
        pov "And what would I have to do?"
        davide "I'll tell you then, but first I want your decision."
        dad "Do it! It's a good chance."
    pov "{i}A chance to get in the basement. But I'm sure I'll have to do something criminal too.{/i}"
    pov "{i}So becoming a criminal too or don't and find another way into the basement?{/i}"
    call screen lroom21decide

screen lroom21decide:
    default tt = Tooltip (" ")

    fixed:

        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 605 ypos 193 action (Hide('lroom21decide'), Jump('lroom21yes')) hovered tt.Action ("Take the job [gd1]/both") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1286 ypos 193 action (Hide('lroom21decide'), Jump('lroom21no')) hovered tt.Action ("Don't take the job [bd1]/both") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom21no:
    pov "No, I don't want to do this criminal shit."
    scene livingroom 9pm 006n
    davide "Another disappointment..."
    if inc == True:
        dad "You made a mistake, son."
    else:
        dad "You made a mistake, [pov]."
    dad "We could really use your help."
    $ dadbad += 1
    $ davidebad += 1
    $ dtime += 1
    jump lroom

label lroom21yes:
    pov "Sure, I'm in."
    scene livingroom 9pm 006j
    davide "Yes, a good decision bro."
    if inc == True:
        dad "That's my son!"
    else:
        dad "Great, [pov]!"
    pov "You didn't tell me what to do so far."
    scene livingroom 9pm 007j
    davide "I need you to deliver a package."
    pov "{i}Oh sure. The typical delivery job.{/i}"
    pov "Ok, that's easy."
    if inc == True:
        davide "Your dad has it."
    else:
        davide "Bruce has it."
    scene livingroom 9pm 008j
    pov "That small red one?"
    davide "Yes. Go in the old subway station on Tuesday or Thursday."
    davide "Between 7am and 8am you'll find someone there."
    davide "Deliver the package and you can keep what you get."
    scene livingroom 9pm 009j
    pov "What I get?"
    davide "Yes, a criminal's life is a good life, haha."
    davide "And don't open it."
    dad "You can't open it anyway, so don't try it."
    pov "Ok."
    $ package += 1
    "You receive the package."
    scene livingroom 9pm 010j
    davide "Do this for us and it'll pay for you too."
    pov "Yes, I hope so."
    $ dadgood += 1
    $ davidegood += 1
    $ dtime += 1
    $ jobgang = True
    jump lroom


label basementgo:
    scene livingroom 9pm 006j
    $ gangmember = True
    davide "You did a good job delivering the packages!"
    davide "So you can be trusted with more and become a permanent member of our gang."
    dad "Yes! I knew it!"
    davide "Then I'll explain you some things, but first..."
    scene livingroom 9pm 006b
    davide "I need you to take care of our bags, Bruce."
    dad "But I thought..."
    davide "No! Bring them to our other place. I'll need the basement clean today."
    dad "But..."
    davide "You remember what we talked about?"
    scene livingroom 9pm 007b
    dad "Yes, sorry. I'm your man for this. I'll do it as fast as possible!"
    davide "That's my man! Show me that we don't need to miss Steve."
    dad "Aye! See you later [pov]!"
    scene livingroom 9pm 008b
    davide "Good. I love it when everything turns out as planned."
    pov "What do you mean with permanent member? What are the privileges?"
    davide "Wait a moment."
    "Bruce leaves with the first bags."
    scene livingroom 9pm 009b
    davide "I need him to leave because he shouldn't know what I have to explain."
    davide "Steve was my right hand in the gang and Bruce thought he would gain that position."
    davide "But I think you'd fit better!"
    pov "Oh... And what's special about that?"
    if inc == True:
        davide "He and your mother have to follow our orders."
    else:
        davide "He and [mother] have to follow our orders."
    scene livingroom 9pm 010b
    davide "I think this way we can be more productive."
    pov "But what are we doing?"
    davide "Follow me and you'll see."
    pov "{i}They have to do what I say? This could be a lot of fun!{/i}"
    scene livingroom 9pm 011b
    davide "You now get access to the basement. Our operations base."
    "Davide gives you a key."
    $ basementkey = True
    $ lroom21pdone = True
    pov "{i}Finally!{/i}"
    davide "Go on! Enter the door to success, haha."
    scene black
    "You go down."
    scene basement 001
    pov "{i}Wow! This place looks somewhat perverted. I wonder what happens here?{/i}"
    davide "Come. I'll show you everything."
    scene basement 002
    davide "This is our bar. Where we make our drinks so the evenings will not be so boring, haha."
    pov "And many different drinks. But isn't that a bit too much for 4 people?"
    davide "We often have guests here, so we need fine drinks."
    scene basement 003
    pov "And this stuff?"
    davide "Haha, for personal use. When some girls come by and guests too."
    pov "When are guests coming by?"
    scene basement 004
    davide "Soon to get some of our drugs we prepare here."
    davide "The guests are men and women and after some drinks and drugs we usually have fun here."
    pov "Fun?"
    davide "Haha, you know exactly what that means!"
    scene basement 005
    davide "Here's our place to chill or make deals."
    pov "Not bad what's down here in the basement."
    scene basement 006
    pov "And what's here?"
    davide "The right one is the toilet, so we don't need to leave the basement for that."
    davide "The left one is the changing room, mostly for the girls."
    pov "Why a changing room? Isn't naked enough?"
    davide "Haha, not bad. But you should see what hot costumes girls can wear!"
    if inc == True:
        "Does that include my mom? Wearing costumes and participate at the party's?"
    else:
        "Does that include [mother]? Wearing costumes and participate at the party's?"
    if NTR == True:
        davide "Yeah, sure! I'd bet you'd love to see her here too!"
    else:
        davide "No. Wearing costumes sometimes, but having real fun isn't her thing."
        davide "Maybe she is too much in love with Bruce..."
    pov "Hmm..."
    scene basement 002
    davide "You can't wait to see the action, can you?"
    pov "I'm a little surprised, because I wasn't sure what to expect here."
    davide "Haha..."
    davide "Oh look who's here. Guests!"
    scene basement 9pm 010
    if vivianfirstmeet == True:
        pov "This is the bartender from the \"sleazy weasel\", [vivian]."
        pov "But who's the women?"
    else:
        pov "Who are they?"
        scene basement 9pm 011
        davide "So you can't wait any longer? Good to hear, haha."
        if vivianfirstmeet == True:
            vivian "Yes she was stubborn, so I took her here. She's yours to deal with now."
        else:
            "Woman" "Yes she was stubborn, so I took her here. She's yours to deal with now."
    scene basement 9pm 012
    davide "Then follow me, I'll take care of you."
    "woman" "Yes please."
    if vivianfirstmeet == True:
        vivian "And you're now part of the gang [pov]?"
        pov "Yes."
        vivian "Good. So you can play with us too."
    else:
        "Woman" "Hi, I'm..."
        $ vivian = renpy.input(_("Her name is...")) or _("Vivian")
        $ vivianfirstmeet = True
        pov "Hello, I'm..."
        vivian "I know exactly who you are [pov]."
        if inc == True:
            vivian "You're [mother]'s son."
        else:
            vivian "You're the guy who lives with [mother]'s family."
            vivian "And you're now part of the gang [pov]?"
            pov "Yes."
            vivian "Good. So you can play with us too."
    scene basement 9pm 013
    vivian "But I hope you can do better then these wannabe \"gangsters\"."
    vivian "I would prefer a strong leader and I'm sure you can be one!"
    pov "{i}Wow...{/i}"
    vivian "So don't make me wait, haha!"
    scene basement 9pm 014
    vivian "I'll go back! See you guys!"
    davide "See you [vivian]."
    pov "{i}So she's taking a role in the gang-activities.{/i}"
    davide "Come here [pov]!"
    scene basement 9pm 015
    davide "This is ..."
    if mirandafirstmeet == False:
        $ miranda = renpy.input(_("Her name is...")) or _("Miranda")
        $ mirandafirstmeet = True
    davide "[miranda], this is [pov]. The newest member of our gang."
    miranda "Nice to meet you."
    pov "Nice to meet you too."
    davide "[pov] is here to learn what we do here."
    miranda "So he'll join us?"
    davide "Haha, maybe."
    scene basement 9pm 016
    davide "Look, this one is for you. For the hot \"pussy cat\" that you are."
    miranda "Then please give it to me! Don't make me wait every time like Davide."
    pov "{i}These drugs look like candy.{/i}"
    davide "But it's our ritual. You know what you've to do to get it."
    scene basement 9pm 017
    miranda "Satisfied now?"
    davide "Good, open your mouth."
    miranda "Hmm..."
    pov "{i}So he loves to humiliate her?{/i}"
    scene basement 9pm 018
    miranda "Hnn...!"
    davide "See? She loves it!"
    pov "And what's the drug she's doing now?"
    davide "Wait a second!"
    scene basement 9pm 019
    davide "How about you prepare yourself and I'll be ready in a few moments?"
    miranda "Ok. But please don't make me wait."
    scene basement 9pm 020
    davide "This is really good stuff that we got here."
    pov "And let me guess, it gives good feelings?"
    davide "Haha yes. And like other drugs you can get addicted, but..."
    davide "This shit is not normal, it has the strongest effect I ever knew."
    davide "And it's specialty is that it works for everything that gives you pleasure, individually."
    pov "Everything?"
    davide "Haha yes. If you like to eat you'll get the maximum pleasure out of it and could eat until you die."
    davide "The effect works around 1 day and has no bad effects, so win-win. Except that you want more to keep that good feelings."
    pov "Wow. Did you try it?"
    davide "Sadly not. It only works on females. We males have no luck with that."
    pov "If it has no bad effects why can't you sale it officially. This isn't a real bad drug then."
    davide "We tried. But there was an accident. Someone used the drug on a girl without her knowing ..."
    davide "And she thought she got the pleasure from the things she drank and she tried to get that feeling again and she drunk herself to death."
    pov "Oh..."
    davide "That's the reason why we sell this secretly."
    miranda "Are you done? I don't want to wait anymore..."
    scene basement 9pm 021
    davide "Come, let's enjoy the drug as males."
    pov "{i}Holy...{/i}"
    miranda "I want to enjoy my drug now!"
    davide "Haha, relax. You'll get real pleasure soon enough."
    scene basement 9pm 022
    miranda "Can he join us? He looks hot, I want to taste him too!"
    davide "Haha, he can join if he wants to. But now prepare yourself so we can start."
    pov "So she enjoys this kind of pleasure?"
    miranda "Oh yes! You poor men have no idea what you're missing."
    scene basement 9pm 023
    "Davide helped her to get ready."
    davide "See? This is her chosen pleasure. Of course she doesn't have to pay for it then."
    davide "But she'll pay in an other way, haha."
    miranda "Don't stand there looking at me, boy! Get your dick out too!"
    davide "Oh, [miranda] is in love, haha."
    scene basement 9pm 024
    davide "You can have her mouth while I use the other side!"
    miranda "Ohhh..."
    miranda "Please let me taste you, hah..."
    call screen base9mirbj

screen base9mirbj():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1170 ypos 95 action (Hide('base9mirbj'), Jump('base9mirbjy')) hovered tt.Action ("Let her suck you") focus_mask True

        frame:
            xalign .5
            text tt.value

label base9mirbjn:
    pov "No sorry [miranda]. I won't participate."
    davide "You're serious?"
    miranda "What a shame. You're loss boy!"
    scene black
    "not finished yet."

label base9mirbjy:
    scene basement 9pm 025b
    "You get your dick out and go to her."
    pov "Now I'm curious what you can do?"
    miranda "Oh you won't regret it!"
    scene basement 9pm 026b
    davide "Oh and don't forget. You can choose how you use your mouth, after she's restrained here, haha."
    pov "I don't rape girls!"
    davide "That wouldn't be like that, she'll love both ways because of the drug, ain't I right?"
    "Davide fucks her rougher."
    miranda "Hah... hah... you animal!"
    pov "Hmm..."
    miranda "Please let me... hah... pleasure you..."
    scene basement 9pm 027b
    "She catches your dick as you came to near."
    pov "Oh... someone can't wait..."
    miranda "<suck> <suck>"
    davide "A nice surprise, isn't it?"
    pov "Oh yes!"
    dad "WHAT THE FUCK !?"
    scene basement 9pm 029
    davide "Oh hey Bruce, you found us!"
    if inc == True:
        pov "Hey dad."
    else:
        pov "Hey Bruce."
    dad "You can't bring him here, I told you! [mother] would not be amused."
    davide "Haha, I don't care!"
    dad "But I do!"
    scene basement 9pm 030
    dad "I'm serious. She'll go totally crazy! You know her!"
    davide "Yeah I know. But we need a third person for the gang and I think he fits in good."
    davide "And I wouldn't want to get her angry."
    dad "Oh, sure! But I still think we could find another solution."
    pov "Him?"
    davide "The boss, I'll explain it later to you."
    pov "{i}There's also another one, the boss of them? But who is it?{/i}"
    scene basement 9pm 031
    dad "Well, I'm out of here. He's your problem now!"
    davide "Hahaha, don't cry. I don't fear [mother]'s anger."
    pov "Can she really be that bad?"
    davide "Oh you have no idea. But let us enjoy [miranda] for now."
    scene basement 9pm 028b
    "You two have your fun with [miranda]."
    davide "But now you still have to choose what you'll do."
    miranda "Hmm..."
    davide "Let yourself have pleasure by this naughty woman or give her throat a good fuck."
    davide "And as I explained before, she'll get pleasure from both through the drug. even if she only favors one of them."
    call screen base9mirbj2

screen base9mirbj2():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1170 ypos 95 action (Hide('base9mirbj2'), Jump('base9mirbjc')) hovered tt.Action ("Fuck her throat [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 569 ypos 95 action (Hide('base9mirbj2'), Jump('base9mirbjl')) hovered tt.Action ("Let her pleasure you [lv1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label base9mirbjc:
    $ mirandacorruption += 1
    scene basement 9pm 032br
    miranda "Bllggrhh...!"
    pov "I'll choose to fuck her hot mouth! And shut her up, haha."
    davide "A good choice. You'll love it!"
    pov "Oh I hope so."
    miranda "Hnng...!"
    pov "Come on give your best, you made me so hard with your body!"
    scene basement 9pm 033br
    "You stick your dick deeper in her throat."
    miranda "Hnn... Hnn..."
    pov "Wow she's really good."
    davide "As I told you, haha."
    davide "And she's enjoying it also, she's tightening up on my side like hell."
    pov "Oh this is too good, I'll cum soon and feed you well."
    miranda "Hmm..."
    scene basement 9pm 034bri
    pov "Oh yes... hnng..."
    miranda "Bllggrhh...! HNNG..."
    "You cum deep in her throat."
    davide "Haha, yes impregnate her stomach!"
    pov "Damn, [miranda]!"
    scene basement 9pm 035bri
    miranda "Hnn... <gulp> <gulp>"
    davide "Don't pout you got your meal, haha!"
    pov "That was very good [miranda]!"
    miranda "So you had your fun."
    jump base9nic

label base9mirbjl:
    $ mirandalove += 1
    scene basement 9pm 032bg
    pov "Let's see what you can do [miranda]."
    miranda "Oh you'll love it. <lick>"
    davide "She's like a pro, you'll be in heaven."
    pov "Ohh... that tongue."
    scene basement 9pm 033bg
    "She's licking faster with her tongue over your tip."
    pov "Oh yes!"
    miranda "I like your dick. It's good and lickable, hah..."
    davide "As I said before, she's in love with you, haha."
    pov "Now I'm already at my limit. You're doing too good [miranda]."
    miranda "I'll let you choose where you want your sperm on me!"
    pov "Perfect!"
    call screen base9mirbj3

screen base9mirbj3():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1170 ypos 95 action (Hide('base9mirbj3'), Jump('base9mirbjlm')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 569 ypos 95 action (Hide('base9mirbj3'), Jump('base9mirbjlf')) hovered tt.Action ("Cum on her face") focus_mask True
        frame:
            xalign .5
            text tt.value

label base9mirbjlm:
    pov "I want you to taste my sperm!"
    scene basement 9pm 034bgi
    pov "Hnng..."
    "You cum in her mouth."
    miranda "Hmm..."
    pov "Damn, she's like sucking it out of me."
    miranda "<gulp> <gulp>"
    scene basement 9pm 035bgi
    miranda "Ohh... that tasted good. Young men sperm!"
    pov "Wow, really like a pro!"
    miranda "So you liked my treatment?"
    pov "Yes! Your mouth is wonderful!"
    davide "Then you should try her other holes too!"
    jump base9nic

label base9mirbjlf:
    pov "I want to spray it over your beautiful face!"
    $ mirandacumface = True
    scene basement 9pm 034bgo
    pov "Hnng..."
    "You cum on her face."
    miranda "Hmm..."
    pov "Yes, let me paint on you."
    scene basement 9pm 035bgo
    miranda "So much sperm came out all over my face."
    pov "Wow what a fantastic view."
    miranda "It's like youth-cream for my skin, coming from a young boy."
    pov "Wow, really like a pro!"
    miranda "So you liked my treatment?"
    pov "Yes! Your mouth is wonderful!"
    davide "Then you should try her other holes too!"
    jump base9nic


label base9nic:
    scene basement 9pm 036b
    miranda "Ohh... hah..."
    davide "Good, you shut up now and enjoy my hard ride."
    miranda "Hah... you horndog!"
    if mirandacumface == True:
        scene basement 9pm 037b
    else:
        scene basement 9pm 037a
    davide "Oh hell yeah! That tight hole!"
    pov "You're still not done?"
    davide "I go slower from time to time to enjoy her wet hole longer."
    davide "And she can enjoy my hard dick longer too. You like that don't you [miranda]."
    miranda "Hah... yes... but continue fucking me now!"
    mom "YOU'RE SO DEAD, DAVIDE!"
    scene basement 9pm 038
    davide "Wow, she's really angry, haha."
    miranda "Hi [mother]."
    mom "Shut the fuck up you whore!"
    davide "Hahaha, shit..."
    scene basement 9pm 039
    mom "I forbid you to let him down there."
    if inc == True:
        pov "But I want this too, mom."
    else:
        pov "But I want this too."
    mom "You shut up!"
    davide "Hahaha..."
    mom "And you stop laughing. This isn't funny anymore."
    davide "Oh yes it its. It wasn't my decision alone to get him there."
    scene basement 9pm 041n
    mom "You can't be serious!"
    davide "Oh yes I am. He choose him and has given him Steve's rank in the gang."
    mom "So he's your right hand out of nothing?"
    davide "Yes and as a good boss I show him all the goods, haha."
    if inc == True:
        pov "So I have a higher rank then my mom?"
    else:
        pov "So I have a higher rank then [mom]?"
    davide "Yes you have."
    scene basement 9pm 040n
    davide "And it's time that you get punished for being so rude!"
    mom "But..."
    davide "No! Talking to a higher gang member like that! You know the rules!"
    mom "..."
    pov "{i}Punishment, hm...{/i}"
    if NTR == True and momrelationship <= 5:
        jump base9ntr
    else:
        scene basement 9pm 042nn
        davide "Go on! You can now choose how you'll punish her."
    pov "I should punish her?"
    davide "Yes, she insulted you too and I'm not stop fucking [miranda] right now!"
    pov "Haha, I understand."
    if inc == True:
        "You go over to your mom."
    else:
        "You go over to [mom]."
    scene basement 9pm 043n
    pov "So... so..."
    mom "Hnn..."
    davide "Show her her place."
    pov "I can choose what ever I want?"
    davide "Yes of course, it's your punishment."
    mom "[pov], please..."
    jump base9nicpunish


label base9nicpunish:
    scene basement 9pm 043n
    call screen base9nicpunish1

screen base9nicpunish1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1170 ypos 95 action (Hide('base9nicpunish1'), Jump('base9nicpunc')) hovered tt.Action ("Punish her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 569 ypos 95 action (Hide('base9nicpunish1'), Jump('base9nicpunl')) hovered tt.Action ("Punish her [lv1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label base9nicpunc:
    pov "Come with me, punishment time!"
    $ momcorruption += 1
    scene basement 9pm 043nnc
    mom "Huh?"
    "You grab her arm and pull her your way."
    mom "What do you want to do with me?"
    pov "You'll see it soon!"
    "She's so confused she realizes too late what you will do with her."
    scene basement 9pm 044nnc
    mom "No! You can't be serious!"
    davide "Haha, nice one! I'm curious what you're up to."
    if inc == True:
        mom "I don't know what you're up to but don't forget that I'm your mother."
    else:
        mom "I don't know what you're up to but don't forget that I'm your mother's best friend."
    pov "Yes and that's the reason why that rude talking must be punished."
    scene basement 9pm 045nnc
    mom "Oh no! Don't look at me!"
    if inc == True:
        davide "Wow bro. You ain't gonna fuck your mom?"
    else:
        davide "Wow bro. You ain't gonna fuck her?"
    miranda "Oh I think that naughty bitch would love it, haha."
    mom "Shut the fuck up [miranda]!"
    pov "No, I'll do something else. She earned herself a good spanking."
    scene basement 9pm 046nnc
    mom "Stop! You can't be serious!"
    miranda "Hahaha... hah... hah..."
    davide "What a nice idea."
    mom "You shut up too, davide! It's all your fault!"
    scene basement 9pm 047nnc
    pov "{i}Hmm... what should I choose for her?{/i}"
    call screen base9nicpunch

screen base9nicpunch():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1170 ypos 95 action (Hide('base9nicpunch'), Jump('base9nicpunp')) hovered tt.Action ("Choose the ping-pong paddle [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 569 ypos 95 action (Hide('base9nicpunch'), Jump('base9nicpunch1')) hovered tt.Action ("Use your hand") focus_mask True
        frame:
            xalign .5
            text tt.value

label base9nicpunp:
    $ mompaddle = True
    $ momcorruption += 1
    pov "{i}It has to be a good punishment!{/i}"
    jump base9nicpunch1

label base9nicpunch1:
    pov "{i}A good spanking with my hand is enough!{/i}"
    if mompaddle == True:
        scene basement 9pm 048nncp
    else:
        scene basement 9pm 048nnch
    if inc == True:
        mom "Please listen to me [pov]. You're my son, you shouldn't do this!"
        pov "You decided it yourself, mom. So be a good mom and endure your punishment."
    else:
        mom "Please listen to me [pov]. You're like a son, you shouldn't do this!"
        pov "You decided it yourself, [mother]. So be a good girl and endure your punishment."
    mom "Wait...!"
    with vpunch
    "Slap"
    mom "Ahhh..."
    davide "Hah you're really doing it."
    mom "Don't think..."
    with vpunch
    "Slap"
    mom "Ahhh..."
    pov "Sshhh...! No more talking!"
    miranda "I can be a bad girl too!"
    mom "Don't you dare [miranda]! You're so de..."
    with vpunch
    "Slap"
    mom "Ahhh..."
    if mompaddle == True:
        scene basement 9pm 049nncp
    else:
        scene basement 9pm 049nnch
    pov "The fine red ass from a good punishment..."
    mom "Red? Oh god! Stop it please!"
    with vpunch
    "Slap"
    mom "Hnng..."
    dad "What the hell?"
    pov "Huh?"
    scene basement 9pm 050nnc
    if inc == True:
        dad "What are you doing with your mother?"
    else:
        dad "What are you doing with [mother]?"
    davide "She's receiving her punishment for being rude to a higher gang-member."
    dad "Hmm..."
    dad "But I need her now! There's a call for her, it's urgent!"
    davide "This seems to be serious. You should let her go."
    pov "Ok."
    "You free her."
    scene basement 9pm 051nnc
    mom "..."
    pov "..."
    dad "Are you coming [mother]?"
    scene basement 9pm 052nnc
    pov "Stop!"
    mom "Hnng..."
    pov "You didn't accept that your punishment was necessary!"
    mom "..."
    pov "Then you're free to go."
    scene basement 9pm 053nnc
    mom "I... I was a bad girl and needed to be punished by you."
    if inc == True:
        pov "Good mom! I hope you learned your lesson."
    else:
        pov "Good girl! I hope you learned your lesson."
    mom "Yes I have. Can I go now?"
    pov "Yes, you're free to go."
    scene basement 9pm 054nnc
    "[mother] is shaking while she goes."
    davide "Wow, you're taming her good."
    pov "She needs to feel humiliated too."
    miranda "You have no idea how bad I'll be next time <giggle>"
    davide "Shut up [miranda]!"
    miranda "Aaah... hah..."
    scene black
    "After she left and you enjoyed your new power and leave the basement."
    $ dtime += 2
    $ b9rncor = True
    jump mcroom



label base9ntr:
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene basement 9pm 040n
    davide "I'll take care of it!"
    if inc == True:
        pov "{i}He'll punish mom?{/i}"
    else:
        pov "{i}He'll punish [mother]?{/i}"
    pov "{i}Do I want him to punish her?{/i}"
    call screen base9ntrpun

screen base9ntrpun():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1170 ypos 95 action (Hide('base9ntrpun'), Jump('base9ntrpund')) hovered tt.Action ("Let him") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 569 ypos 95 action (Hide('base9ntrpun'), Jump('base9ntrpunm')) hovered tt.Action ("Interfere") focus_mask True
        frame:
            xalign .5
            text tt.value


label base9ntrpunm:
    pov "{i}No, I don't want him to lay a hand on her.{/i}"
    pov "Wait!"
    scene basement 9pm 042nn
    davide "Huh?"
    pov "I want to punish her myself!"
    davide "Oh...?"
    pov "She insulted me, also should I be the one do it."
    davide "Ok. Then do it yourself."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    jump base9nicpunish


label base9ntrpund:
    scene basement 9pm 043n
    mom "Please... Davide..."
    davide "Now! I know you'll like it too."
    mom "But..."
    davide "..."
    mom "Ok."
    scene basement 9pm 044n
    davide "What are you waiting for? Get naked and bend over."
    mom "Please, he must not see this!"
    davide "Oh I'm sure he won't care. He's part of the gang now, so he'll stay with us often."
    if inc == True:
        mom "But he's my son."
    else:
        mom "But he's the son of my best friend."
    davide "Bla.. bla... bla..."
    mom "I... I understand..."
    scene basement 9pm 045n
    mom "Please... don't look."
    davide "Oh I'm sure he wants to take a glimpse. You're damn hot."
    if inc == True:
        pov "He's right. You're damn hot, mom."
    else:
        pov "He's right. You're damn hot, [mother]."
    mom "Hnng..."
    scene basement 9pm 046n
    "[mother] gets herself into position."
    mom "I can't believe you want to do this."
    davide "It's your punishment and you love this, you're flooding."
    mom "Nooo!"
    if inc == True:
        davide "Letting your son see how you get screwed up and love it."
    else:
        davide "Letting him see how you get screwed up and love it."
    mom "That's not true. He knows why I have to do this."
    davide "Because you're a slut!"
    scene basement 9pm 047n
    mom "Aaah..."
    davide "Good. You're sucking me already."
    mom "Hmm..."
    davide "What's with you [pov]? [miranda] needs to be fucked too!"
    miranda "Oh yes, please do me boy. My pussy wants to taste your dick!"
    mom "No [pov]! You can't do this."
    scene basement 9pm 048n
    davide "Go on, have your fun [pov]! There's no need to only watch."
    if inc == True:
        davide "Your mom has to accept this because there's nothing she can do, except moan, haha."
    else:
        davide "[mother] has to accept this because there's nothing she can do, except moan, haha."
    mom "No... hah... hah... she's a whore..."
    miranda "Haha, shut up [mother]."
    if inc == True:
        miranda "Telling your son that's bad while getting fucked and enjoying it. Bad mom!"
    else:
        miranda "Telling him that's bad while getting fucked and enjoying it. Bad [mother]!"
    pov "{i}Hm... what a good question. [miranda] is free now and ready to get fucked too.{/i}"
    scene basement 9pm 049n
    miranda "Please [pov]. I want your dick. Please fuck me too!"
    mom "Hah... hah..."
    davide "Come on. Let give [miranda] some fun too!"
    mom "Don't... hah.. stick it... in her... hah..."
    miranda "Why should you be the only one who has fun?"
    mom "I... hah... ahh..."
    davide "Haha, she's still trying to deny it."
    if inc == True:
        pov "{i}Should I fuck [miranda]? Or should I follow mom's wish and just watch her getting fucked?{/i}"
    else:
        pov "{i}Should I fuck [miranda]? Or should I follow [mother]'s wish and just watch her getting fucked?{/i}"
    call screen base9ntrmir

screen base9ntrmir():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1170 ypos 95 action (Hide('base9ntrmir'), Jump('base9ntrmiry')) hovered tt.Action ("Fuck [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 569 ypos 95 action (Hide('base9ntrmir'), Jump('base9ntrmirn')) hovered tt.Action ("Just watch") focus_mask True
        frame:
            xalign .5
            text tt.value

label base9ntrmirn:
    if inc == True:
        pov "{i}I don't want to fuck [miranda]. I don't want to make mom any more angry.{/i}"
        davide "Haha, you really regret her? So you're a good boy, doing what your mom wants."
    else:
        pov "{i}I don't want to fuck [miranda]. I don't want to make [mother] any more angry.{/i}"
        davide "Haha, you really regret her? So you're a good boy, doing what [mother] wants."
    davide "Or do you just enjoy it, seeing her getting fucked by other men, haha?"
    mom "Don't talk... hah... like that... hah... with him!"
    call screen base9ntrnicch

screen base9ntrnicch():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1170 ypos 95 action (Hide('base9ntrnicch'), Jump('base9ntrnicapp')) hovered tt.Action ("You like it seeing her get fucked") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 569 ypos 95 action (Hide('base9ntrnicch'), Jump('base9ntrnic2')) hovered tt.Action ("You don't like it") focus_mask True
        frame:
            xalign .5
            text tt.value

label base9ntrnicapp:
    $ momgetfucked = True
    pov "I like it. I want to see it how she's betraying everyone while getting fucked."
    davide "Oh you're a pervert? Good for me, haha."
    if inc == True:
        mom "You can't be serious? You like it seeing your mother getting fucked by other men?"
    else:
        mom "You can't be serious? You like it seeing me getting fucked by other men?"
    jump base9ntrnic2

label base9ntrnic2:
    if momgetfucked == False:
        if inc == True:
            pov "{i}I don't like it. But I can't win a fight against him. And mom doesn't fight against it either.{/i}"
        else:
            pov "{i}I don't like it. But I can't win a fight against him. And [mother] doesn't fight against it either.{/i}"
    davide "So you decided, haha. See how much she likes it, getting fucked by my big black dick."
    scene basement 9pm 051n
    mom "No... don't watch us! Hah..."
    davide "He decided so we'll give him a good show!"
    if momgetfucked == False:
        pov "{i}That damn asshole! But why does she only complain that I shouldn't watch?{/i}"
    else:
        pov "Yes, do it. I want to see her cum!"
    mom "No... hah... hah..."
    if inc == True:
        davide "How about you tell your son how much you love it?"
    else:
        davide "How about you tell him how much you love it?"
    scene basement 9pm 054n
    mom "I... hah... have to... do this..."
    davide "Because you're a slut?"
    mom "Please... hah... [pov] you know it..."
    if momgetfucked == False:
        pov "{i}Yes sure. She \"must\" do it for her cover. But I'm not sure anymore.{/i}"
    else:
        pov "Yeah I know. So you need to please everyone and cum hard on their dicks!"
        mom "No... It's not... hah... like that..."
    davide "Time to cum, slut!"
    mom "Wait... hah.. hah..."
    scene basement 9pm 052n
    mom "Hnng... Hnn..."
    davide "Look! She hates it so much that she's about to cum!"
    mom "Hah... yes..."
    if momgetfucked == True:
        pov "{i}No! I can't believe it! She's cumming from that assholes dick.{/i}"
    else:
        if inc == True:
            pov "Yes! Show me your cum-face, mom!"
        else:
            pov "Yes! Show me your cum-face, [mother]!"
    mom "Aaaahhhh... Hnnnng..."
    scene basement 9pm 053n
    davide "I came hard! But I need more. So time for another round?"
    mom "Hah... yes... more please... hah..."
    davide "So you had enough fun, [pov]! I'll have more fun without you, haha."
    if inc == True:
        davide "Time to stop your watching time seeing your mom get fucked!"
    else:
        davide "Time to stop your watching time seeing [mother] get fucked!"
    if momgetfucked == True:
        pov "{i}No... I have to do something. I must help her or she's get corrupted.{/i}"
    else:
        pov "Yeah have fun fucking that slut!"
    scene black
    "You leave the basement hearing them start another round."
    $ dtime += 2
    $ b9rnntr = True
    if momgetfucked == True:
        $ ntrhatenic = True
        $ ntrlovenic = False
    else:
        $ ntrlovenic = False
        $ ntrhatenic = True
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    jump mcroom

label base9ntrmiry:
    pov "{i}It's my chance. I'll fuck her too.{/i}"
    scene basement 9pm 050nf
    miranda "Yes! Please take care of me [pov]!"
    pov "{i}What a nice view.{/i}"
    davide "What's wrong [pov]. Can't decide which hole you should use?"
    mom "Stop! Hah... don't give him these ideas..."
    miranda "I don't care, just fuck me. I want to feel your young dick!"
    pov "{i}So which one will it be?{/i}"
    call screen base9ntrmirch

screen base9ntrmirch():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1170 ypos 95 action (Hide('base9ntrmirch'), Jump('base9ntrmira')) hovered tt.Action ("Fuck her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 569 ypos 95 action (Hide('base9ntrmirch'), Jump('base9ntrmirp')) hovered tt.Action ("Fuck her pussy") focus_mask True
        frame:
            xalign .5
            text tt.value

label base9ntrmira:
    pov "{i}I need to fuck that tight asshole.{/i}"
    $ mirandass = True
    jump base9ntrmirfuck

label base9ntrmirp:
    pov "{i}I need to fuck her wet pussy.{/i}"
    jump base9ntrmirfuck


label base9ntrmirfuck:
    scene basement 9pm 052nf
    if mirandass == True:
        "You stick you dick in her asshole."
    else:
        "You stick your dick in her pussy."
    miranda "Ahhh... so big."
    mom "Hah... no... [pov]"
    davide "See? As I told you before, her holes are damn good."
    pov "Yes, especially the one I'm in now!"
    davide "And which did you choose?"
    if mirandass == True:
        miranda "He's in my asshole."
        if inc == True:
            miranda "Your son is fucking me in my asshole, [mother]!"
        else:
            miranda "[pov] is fucking me in my asshole, [mother]!"
    else:
        miranda "He's in my pussy."
        if inc == True:
            miranda "Your son is fucking me in my pussy, [mother]!"
        else:
            miranda "[pov] is fucking me in my pussy, [mother]!"
    mom "No... don't tell me... hah... that..."
    miranda "But he's really good. That young stud riding me hard."
    mom "Shut up you... damn whore... hah..."
    if inc == True:
        mom "Talking like that... about my son... hah..."
    else:
        mom "Talking like that... about him... hah..."
    davide "Enough talking [mother]."
    scene basement 9pm 053nf
    mom "Hnng...!"
    davide "Time for some harder fucking!"
    miranda "Go on [pov]! We can't get left behind them. Fuck me harder!"
    if inc == True:
        davide "Damn, your mom is getting tight. She likes to get a hard pounding when her son is watching."
    else:
        davide "Damn, [mother]'s is getting tight. She like to get a hard pounding when you're watching."
    mom "Hnng... hnng..."
    davide "No more fighting. Just accept it!"
    if inc == True:
        miranda "See? Your mom is a whore too!"
    else:
        miranda "See? [mother] is a whore too!"
    pov "You shouldn't talk so much either!"
    "You fuck her harder!"
    scene basement 9pm 054nf
    miranda "Hah... ahhh... yes..."
    mom "Hnn... hah... hah..."
    davide "Good. She gave up and is just enjoying it."
    pov "Mine too, haha."
    davide "Good to see you're also able to shut the slut's up, haha."
    pov "Yes! But she's really a hot ride!"
    miranda "Hah... ahhh... yes..."
    mom "Hnn... hah... hah..."
    scene basement 9pm 055nf
    "You two fucked them for a while until they're done and you leave the basement."
    $ dtime += 2
    $ b9rnntrmir = True
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    jump mcroom


label base9nicpunl:
    scene basement 9pm 042
    $ base9nickiss = False
    if inc == True:
        pov "<whisper> Relax mom! I won't punish you!"
    else:
        pov "<whisper> Relax [mother]! I won't punish you!"
    mom "Hmm...?"
    pov "<whisper> Why are you so scared. You know that I won't hurt you!"
    mom "<whisper> But you're in the gang now."
    pov "<whisper> Yes but that doesn't mean I have to do everything they do."
    scene basement 9pm 043
    mom "Oh..."
    pov "<whisper> But I'm still confused why you're so angry seeing me down here?"
    pov "<whisper> I thought you might need my help?"
    if inc == True:
        mom "<whisper> That's something I've wanted to hide from you and your siblings."
    else:
        mom "<whisper> That's something I've wanted to hide from you and my daughters."
    mom "<whisper> Bad things happen down here."
    pov "<whisper> Yes and that's the reason why I want to stay with you here. So that no more bad things happen."
    scene basement 9pm 044
    mom "<whisper> But we already did unforgivable things..."
    pov "<whisper> You mean the drugs?"
    mom "<whisper> Yes..."
    mom "<whisper> I was so proud of you and now I have failed you..."
    if inc == True:
        mom "<whisper> I failed as a mother..."
        pov "<whisper> Oh, mom..."
        pov "<whisper> Mom!"
    else:
        pov "<whisper> Oh, [mother]..."
        pov "<whisper> [mother]!"
    scene basement 9pm 045
    pov "<whisper> I'll not be the one that judges you! I know why you had to do it."
    pov "<whisper> I love you and you know that and I'm pretty sure that [ls] and [bs] would understand it too."
    if inc == True:
        pov "<whisper> You sacrificed yourself for the family."
        pov "<whisper> And I'll do everything needed to get my old mom back!"
    else:
        pov "<whisper> You sacrificed yourself for us."
        pov "<whisper> And I'll do everything needed to get the old [mother] back!"
    pov "<whisper> The one I loved all the time."
    scene basement 9pm 046
    mom "<whisper> You're saying such nice things to me..."
    pov "<whisper> Yes and it brought your wonderful smile back."
    mom "<whisper> I was so trapped, with dark feelings that I forgot how positive you could be."
    pov "<whisper> See? So it isn't a bad thing when I'm down here with you."
    if inc == True:
        mom "<whisper> My son want to rescue my fallen soul..."
    else:
        mom "<whisper> You want to rescue my fallen soul..."
    if momlove >= 30:
        scene basement 9pm 047
        $ base9nickiss = True
        mom "<kiss>"
        pov "{i}What...?{/i}"
        if inc == True:
            pov "{i}Mom is kissing me!{/i}"
        else:
            pov "{i}[mother] is kissing me!{/i}"
        scene basement 9pm 048
        mom "<whisper> Oh no...! What have I done?"
        mom "<whisper> I... I... it was a mistake..."
        if inc == True:
            pov "<whisper> Calm down, mom!"
        else:
            pov "<whisper> Calm down, [mother]!"
    davide "What's up? Less talking, more punishing!"
    mom "<whisper> Oh no, that's not good."
    pov "<whisper> What is it? I don't understand..."
    mom "<whisper> Let me think..."
    scene basement 9pm 049
    mom "<whisper> Come here [pov]."
    pov "<whisper> What? Why?"
    davide "What's the matter? Do I need to do it myself?"
    mom "<whisper> You need to punish me, Davide needs his drama, so we have to play along."
    pov "<whisper> But..."
    scene basement 9pm 050
    mom "<whisper> Just go ahead and spank me a little, so he won't get suspicious."
    pov "<whisper> Spank..."
    if inc == True:
        pov "{i}Did my mom really ask me to spank her naked ass?{/i}"
    else:
        pov "{i}Did she really ask me to spank her naked ass?{/i}"
    scene basement 9pm 051
    mom "<whisper> Please... just a little. You must show him that you're a worthy gang member."
    if inc == True:
        pov "Ok. So it's time that you need to get spanked for being a bad mom!"
    else:
        pov "Ok. So it's time that you need to get spanked for being a bad girl!"
    mom "Please be gentle!"
    davide "You have chosen spanking? A good choice!"
    scene basement 9pm 052
    if inc == True:
        davide "I bet you waited a long time to do this with your mom!"
    else:
        davide "I bet you waited a long time to do this with [mother]!"
    miranda "Yes! She needs a hard spanki... Hah!"
    davide "Shut up slut! No talking while I'm fucking you!"
    miranda "Hah... hah..."
    if inc == True:
        pov "{i}Mom is right. I should do it. It's still better than Davide doing something.{/i}"
    else:
        pov "{i}[mother] is right. I should do it. It's still better than Davide doing something.{/i}"
    pov "{i}So then let's do it.{/i}"
    call screen base9splove

screen base9splove():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1170 ypos 95 action (Hide('base9splove'), Jump('base9splvh')) hovered tt.Action ("Spank her hard") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 569 ypos 95 action (Hide('base9splove'), Jump('base9splvn')) hovered tt.Action ("Spank her gentle") focus_mask True
        frame:
            xalign .5
            text tt.value

label base9splvh:
    $ base9spankh = True
    jump base9splvn

label base9splvn:
    scene basement 9pm 054
    with vpunch
    "<slap>"
    if base9spankh == True:
        mom "HAH!"
    else:
        mom "Hah!"
    scene basement 9pm 053
    if base9spankh == True:
        if inc == True:
            pov "<whisper> Sorry mom. I need to spank you hard to pretend it's a real punishment."
        else:
            pov "<whisper> Sorry [mother]. I need to spank you hard to pretend it's a real punishment."
    else:
        if inc == True:
            pov "<whisper> Is this really ok for you, mom?"
        else:
            pov "<whisper> Is this really ok for you, [mother]?"
    mom "<whisper> It's fine, just a few more!"
    scene basement 9pm 054
    with vpunch
    "<slap>"
    if base9spankh == True:
        mom "HNN!"
    else:
        mom "Hnn!"
    with vpunch
    "<slap>"
    if base9spankh == True:
        scene basement 9pm 055
        mom "HAH!"
    else:
        mom "Hah!"
    davide "You're doing good bro!"
    mom "I'm sorry that I was so rude with you [pov]!"
    dad "What the hell?"
    scene basement 9pm 056
    mom "Oh, hey darling."
    davide "She's receiving her punishment for being rude to a higher gang-member."
    dad "Hmm..."
    dad "But I need her now! There's a call for her, it's urgent!"
    davide "This seems to be serious. You should let her go."
    scene basement 9pm 057
    mom "I'm coming darling, don't get mad."
    davide "Oh she looks chastened. You made your position clear."
    if inc == True:
        pov "<whisper> Mom, I'm not with Davide..."
    else:
        pov "<whisper> [mother], I'm not with Davide..."
    scene basement 9pm 058
    mom "<whisper> Don't worry [pov]. You did it perfect."
    mom "<whisper> And I'm happy about what you said before, that lifts a great burden from my shoulders."
    pov "Hmm..."
    if inc == True:
        mom "<whisper> You're the best son!"
    else:
        mom "<whisper> You're like the son I wished to have!"
    scene basement 9pm 059
    mom "<whisper> Relax, darling. We just set up a show for Davide."
    mom "<whisper> He didn't spank me as a punishment. We can still be proud of him."
    "Bruce looks at you with relief."
    scene basement 9pm 060
    if inc == True:
        pov "{i}Mom looks really happy. So I did good.{/i}"
    else:
        pov "{i}[mother] looks really happy. So I did good.{/i}"
    if base9nickiss == True:
        pov "{i}But I still need to know why she kissed me. I have to ask her when we're alone again.{/i}"
    scene black
    "After she left and you enjoyed your new agreement with her you leave the basement too."
    $ dtime += 2
    $ b9rnlove = True
    jump mcroom






label lroom22ass:
    hide screen locations
    scene livingroom 10pm 002a
    pov "{i}Damn, her ass is even hotter in that dress!{/i}"
    jump lroom

label lroom22talk:
    hide screen locations
    scene livingroom 10pm 002
    $ momrelationship += 1
    dad "Look who's here."
    mom "Oh, [pov] You found us."
    davide "Hi bro."
    mom "I was about to ask them what they wanted to do with all these bags."
    davide "And I told her that's new stuff we \"found\"."
    pov "Found?"
    if inc == True:
        dad "Yes the less you know the better, son."
    else:
        dad "Yes the less you know the better, [pov]."
    pov "Okay..."
    if NTR == True and momrelationship < 6 and momntr == True:
        jump lroom22hardntr
    scene livingroom 10pm 003
    davide "How about you bring us some drinks, [mother]?"
    mom "Hmm... okay, I can do that."
    dad "Yes my throat is all dry."
    pov "{i}Hmm...{/i}"
    scene livingroom 10pm 004
    mom "I'll get you something too, [pov]. So you can drink with us."
    davide "Yes he could use a drink too."
    if inc == True:
        dad "My son will beat us all at drinking, be aware."
        pov "Wait mom!"
    else:
        dad "He'll beat us all at drinking, be aware."
        pov "Wait [mother]!"
    jump lr22nontr

label lr22nontr:
    call screen lr22nontr1

screen lr22nontr1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1100 ypos 158 action (Hide('lr22nontr1'), Jump('lroom22love')) hovered tt.Action ("Help her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1271 ypos 158 action (Hide('lr22nontr1'), Jump('lroom22cor')) hovered tt.Action ("Slap her ass [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom22love:
    scene livingroom 10pm 005a
    pov "Let me help you get the drinks."
    mom "Eh?"
    davide "What...?"
    dad "Huh?"
    mom "You mean..."
    if inc == True:
        pov "Yes it's easier when you don't have to do it all alone, mom."
    else:
        pov "Yes it's easier when you don't have to do it all alone, [mother]."
    scene livingroom 10pm 006a
    davide "You can't be serious helping a woman!"
    pov "Oh yes I am."
    mom "Oh thank you."
    if inc == True:
        davide "What's with your son, bro?"
    else:
        davide "What's with him, bro?"
    dad "I don't know, I'm sorry."
    scene livingroom 10pm 007a
    mom "I appreciate that you'll help me but you must be aware."
    pov "Why?"
    mom "This isn't a behavior that fits in your role."
    mom "You have to be a bad boy like them."
    scene livingroom 10pm 008a
    pov "I don't care about these idiots."
    mom "But..."
    pov "And I don't want you to participate in this shit any longer."
    if inc == True:
        pov "Dad's friends are scum and you deserve better then them."
    else:
        pov "Bruce's friends are scum and you deserve better then them."
    mom "..."
    scene livingroom 10pm 009a
    pov "And I want you to stay with me now."
    pov "They'll get their business done without you. I haven't seen you in such a long time."
    if inc == True:
        pov "I want to spend more time with my mom."
        mom "Oh..."
        pov "Please mom. You deserve better."
    else:
        pov "I want to spend more time with you, [mother]."
        mom "Oh..."
        pov "Please. You deserve better."
    scene livingroom 10pm 010a
    mom "You're so sweet, but I'm not sure if they'll get angry at you and something bad could happen."
    if inc == True:
        pov "Please trust me. Only one time won't make them suspicious. Also dad will talk to them, I'm sure."
    else:
        pov "Please trust me. Only one time won't make them suspicious. Also Bruce will talk to them, I'm sure."
    pov "I'll participate more in this role-play, but for this evening I'll spend time only with you."
    scene livingroom 10pm 011a
    mom "You're right! One evening won't hurt them to much."
    mom "And I love you for being such a brave young man. The time overseas was good for you."
    pov "Thank you. So we'll stay together?"
    mom "Yes, [pov]."
    scene livingroom 10pm 012a
    pov "We have something to announce!"
    dad "Eh?"
    davide "Huh?"
    if inc == True:
        pov "Mom will stay with me this evening!"
    else:
        pov "[mother] will stay with me this evening!"
    scene livingroom 10pm 013a
    mom "Yes we talked about it. After he was gone so long, I'll spend this evening with him."
    mom "But I'm sure you'll can handle your stuff yourself."
    davide "..."
    scene livingroom 10pm 014a
    davide "But I thought you would help us get this stuff prepared."
    if inc == True:
        pov "Not today! As my mom said we'll spend time together without you."
    else:
        pov "Not today! As [mother] said we'll spend time together without you."
    pov "You're two strong men, you can handle this without us."
    dad "Wait, [pov]..."
    scene livingroom 10pm 015a
    davide "Are you fucking kidding me?"
    pov "No! I decided so."
    dad "..."
    mom "Calm down Davide. After that long time it's his right to spend some time with me."
    davide "..."
    if inc == True:
        davide "We'll talk later about this. And about your son too."
    else:
        davide "We'll talk later about this. And about him too."
    scene livingroom 10pm 016a
    mom "Can you help them carry their stuff out?"
    pov "Why?"
    mom "Then they'll be out sooner and we'll have more time."
    if inc == True:
        pov "Oh, mom. Sure, I'll be done in no time."
    else:
        pov "Oh, [mother]. Sure, I'll be done in no time."
    $ momlove += 1
    $ lroom10mcwin = True
    $ dtime += 1
    jump lroom

label lroom22cor:
    scene livingroom 10pm 005b
    with vpunch
    mom "Hah..."
    scene livingroom 10pm 006b
    mom "Hmm..."
    davide "Wow, hahaha..."
    if inc == True:
        pov "Appreciation for your decision to get us drinks as ordered, mom."
    else:
        pov "Appreciation for your decision to get us drinks as ordered, [mother]."
    mom "Okay..."
    scene livingroom 10pm 007b
    davide "Haha, a good one bro. You'll fit good with us here."
    if inc == True:
        dad "That's my son."
    pov "She needs to learn her place."
    if inc == True:
        davide "You're so right bro. I see that you're your father's son!"
    else:
        davide "You're so right bro. I see that you're like Bruce!"
    dad "Yes, he's a bad boy too, haha."
    scene livingroom 10pm 008b
    mom "Here are your drinks."
    davide "Good, that was fast."
    pov "When I think about it, I have another idea."
    dad "Another idea?"
    if inc == True:
        pov "Yes, I'll spend the rest of the evening with my mom alone, there's much to discuss."
    else:
        pov "Yes, I'll spend the rest of the evening with [mother] alone, there's much to discuss."
    scene livingroom 10pm 009b
    davide "What?"
    mom "Eh?"
    dad "You mean...?"
    davide "But we need her help with this stuff!"
    pov "Our help?"
    dad "No, just hers. You can't help us, you're not part of the gang."
    if inc == True:
        davide "Yes, your dad is right."
    else:
        davide "Yes, Bruce is right."
    pov "Haha, no! When I can't participate I'll spend the evening with her after that long time away."
    davide "But..."
    pov "The \"bad boy\" decided. And when you're ready to let me join you we can help you out then."
    scene livingroom 10pm 010b
    dad "He's a true \"bad boy\", hah..."
    davide "Okay, it seems you're brave enough to stand on your point. So you can spend the evening with her, this time."
    davide "Our stuff is to important to discuss longer about that now."
    dad "So we'll go somewhere else?"
    davide "Yes."
    if inc == True:
        pov "Good. And we'll stay here together, mom!"
    else:
        pov "Good. And we'll stay here together, [mother]!"
    mom "Okay..."
    dad "Can you help us at least to get this stuff outside...?"
    pov "Sure! You wait here."
    $ momcorruption += 1
    $ lroom10mcwin = True
    $ dtime += 1
    jump lroom


label lroom22hardntr:
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene livingroom 10pm 003
    davide "How about you come here and sit on my lap, [mother]?"
    mom "Huh?"
    dad "I don't know Davide."
    jump lr22hntrd

label lr22hntrd:
    scene livingroom 10pm 003
    call screen lr22hntrd1

screen lr22hntrd1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1100 ypos 158 action (Hide('lr22hntrd1'), Jump('lroom22hardntrdec')) hovered tt.Action ("Don't let her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1271 ypos 158 action (Hide('lr22hntrd1'), Jump('lroom22hardntrdec')) hovered tt.Action ("Don't let her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1271 ypos 158 action (Hide('lr22hntrd1'), Jump('lroom22hardntrdec')) hovered tt.Action ("Do nothing") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom22hardntrdec:
    davide "I won't wait all day. Come here!"
    mom "Okay Davide."
    pov "But..."
    scene livingroom 10pm 004c
    davide "Good girl!"
    mom "Hmm..."
    pov "{i}Oh no! Why did she do that?{/i}"
    davide "What's with you?"
    if inc == True:
        mom "Please calm down Davide. My son's still here with us."
        davide "And why's that a problem? Seeing his sexy mom sitting on another guys lap?"
    else:
        mom "Please calm down Davide. [pov]'s still here with us."
        davide "And why's that a problem? Seeing his sexy friend sitting on another guys lap?"
    mom "Hmm..."
    davide "So how about you show him a little bit more?"
    scene livingroom 10pm 005c
    mom "You... you can't be serious, haha..."
    davide "Here take a good look, [pov]! You won't see it every day."
    mom "Don't [pov]. He's just joking."
    if inc == True:
        pov "{i}Are you serious mom?{/i}"
        scene livingroom 10pm 006c
        pov "{i}I can even see her thong. And I'm sure dad can see that too.{/i}"
        pov "{i}But why doesn't he do anything. Letting mom sit on this asshole's lap.{/i}"
    else:
        pov "{i}Are you serious [mother]?{/i}"
        scene livingroom 10pm 006c
        pov "{i}I can even see her thong. And I'm sure Bruce can see that too.{/i}"
        pov "{i}But why doesn't he do anything. Letting her sit on this asshole's lap.{/i}"
    scene livingroom 10pm 007c
    pov "{i}I can't believe it! He's doing nothing, not even saying something.{/i}"
    if inc == True:
        pov "{i}Just staring at her crotch. Damn dad what's wrong with you?{/i}"
    else:
        pov "{i}Just staring at her crotch. Damn Bruce what's wrong with you?{/i}"
    davide "Come on let's go!"
    mom "So soon?"
    scene livingroom 10pm 008c
    with vpunch
    davide "Move your ass, sexy slut."
    mom "Ouch, Davide. <giggle>"
    if gangmember == False:
        if inc == True:
            pov "{i}No way! Do something dad! He's too strong for me but you work out, you should stop him.{/i}"
            davide "You're coming to, bro? What a pity your son can't join us too."
            pov "What...?"
            dad "Sorry, son. Gang members only."
            pov "Dad! Really?"
            dad "That's the rule, sorry son."
        else:
            pov "{i}No way! Do something Bruce! He's too strong for me but you work out, you should stop him.{/i}"
            davide "You're coming to, bro? What a pity [pov] can't join us too."
            pov "What...?"
            dad "Sorry, [pov]. Gang members only."
            pov "Bruce! Really?"
            dad "That's the rule, sorry."
    scene livingroom 10pm 009c
    davide "I won't wait any longer. Downstairs, now!"
    mom "Haha, calm down Davide. No need to hurry, we have enough time."
    pov "{i}This can't happen! I must stop him!{/i}"
    davide "Let's give him a good show!"
    mom "Okay. You're coming too, honey?"
    dad "Y... yes..."
    if gangmember == True:
        jump base10pmnicntr
    if inc == True:
        pov "{i}No! Dad!{/i}"
    else:
        pov "{i}No! Bruce!{/i}"
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    $ dtime += 1
    jump basement


label lroom11pmtalk:
    hide screen locations
    scene livingroom 11pm 001
    mom "There you are... Come sit with me..."
    $ momrelationship += 1
    mom "You took so long I bored myself."
    mom "So I started to drink alone, but you don't mind, do you? <giggle>"
    if inc == True:
        pov "Sure mom."
    else:
        pov "Sure, [mother]."
    scene livingroom 11pm 002
    mom "It was a very good idea to have some time for us."
    pov "I'm glad you like it too."
    mom "You're such a strong man when you stand up against Davide!"
    pov "I just explained to him that I'd rather stay with you, alone."
    mom "And that's why I'm so proud of you!"
    if inc == True:
        pov "Oh mom."
    else:
        pov "Oh, [mother]."
    scene livingroom 11pm 003
    mom "And I'd forgot how good looking you are."
    if inc == True:
        pov "Mom?"
    else:
        pov "[mother]?"
    pov "{i}What's she talking about?{/i}"
    mom "I missed you for so long and now you here with me all alone."
    pov "{i}Wait? Is she into me? Or maybe she drank a little to much?{/i}"
    pov "{i}But that makes no sense. Even when she's drunk she doesn't behave like that.{/i}"
    mom "I Just can't remember clearly when we met the last time."
    pov "What? It was like 20 minutes before?"
    scene livingroom 11pm 004
    mom "Your smell, like the way your looking at me and your masculine face."
    pov "{i}Damn. I don't get it.{/i}"
    mom "Don't make me wait any longer, since you were away such a long time."
    pov "{i}1 year? What...?{/i}"
    scene livingroom 11pm 005
    mom "<kiss>"
    pov "{i}Oh my god. Am I dreaming?{/i}"
    mom "I missed you so much, Adam!"
    pov "Adam? Wait...!"
    if inc == True:
        pov "{i}She's thinking I'm her husband, my real dad.{/i}"
    else:
        pov "{i}She's thinking I'm my dad? So he betrayed mom with her?{/i}"
    pov "{i}But that makes sense now! So I must look like dad when he was younger.{/i}"
    mom "You taste so good."
    pov "{i}This is wrong because she doesn't realize it. She must be very drunk. But on the other hand...{/i}"
    pov "{i}When she's thinking about doing this with my dad maybe it isn't a bad thing either.{/i}"
    $ lroom11part1 = True
    jump lr11pmkiss

label lr11pmkiss:
    scene livingroom 11pm 005
    call screen lr11pmkiss1

screen lr11pmkiss1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1360 ypos 188 action (Hide('lroom11pmkiss1'), Jump('lroom11pmkiss2')) hovered tt.Action ("Go further [lv1] or [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1520 ypos 188 action (Hide('lroom11pmkiss1'), Jump('lroom11pmstop')) hovered tt.Action ("Stop her") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom11pmkiss2:
    if inc == True:
        pov "{i}Screw it! I can't stop now. I won't get another chance at making out with mom soon.{/i}"
    else:
        pov "{i}Screw it! I can't stop now. I won't get another chance [mother] making out with me soon.{/i}"
    scene livingroom 11pm 006
    pov "Come here [mother]. Let me kiss you more."
    mom "Oh yes..."
    pov "{i}Better just call her by her name. I won't ruin this chance now.{/i}"
    mom "Yes show me that you missed me too."
    pov "{i}Wow, her tongue is getting more aggressive!{/i}"
    scene livingroom 11pm 007
    mom "Here, I know you love to play with them."
    pov "{i}Shit, I'm just like my father. Leeching her sexy boobs.{/i}"
    if inc == False:
        pov "{i}So I can fully understand now, why dad started an affair with her.{/i}"
    else:
        pov "{i}Shit, dad was so lucky.{/i}"
    mom "Play with them, they're yours."
    pov "{i}But it's good to know that she seems to get drunk so fast. No wonder she doesn't like to drink often.{/i}"
    scene livingroom 11pm 008
    pov "{i}She must get really excited that someone stood up against that scum and used that as a reason to drink.{/i}"
    pov "{i}Oh what's she doing now?{/i}"
    mom "Hmm..."
    pov "Everything alright, [mother]?"
    mom "You're really excited to be with me, aren't you. I bet I find something hard right now."
    pov "What...?"
    scene livingroom 11pm 009
    mom "I knew it!"
    if inc == True:
        pov "{i}Oh shit, mom's touching my crotch!{/i}"
    else:
        pov "{i}Oh shit, [mother]'s touching in my crotch!{/i}"
    mom "I missed him so much too!"
    if inc == True:
        pov "{i}Oh shit, maybe this is going a little to far. Kissing was like a little bit innocent stuff, but mom's groping my dick?{/i}"
    else:
        pov "{i}Oh shit, maybe this is going a little to far. Kissing was like a little bit innocent stuff, but [mother]'s groping my dick?{/i}"
    pov "{i}When she realizes what she did she'll get really mad.{/i}"
    $ momdrunktimes += 1
    jump lroom11pmkiss3

label lroom11pmkiss3:
    scene livingroom 11pm 009
    call screen lroom11pmkiss4

screen lroom11pmkiss4():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 764 ypos 255 action (Hide('lroom11pmkiss4'), Jump('lroom11pmhj')) hovered tt.Action ("Let her continue [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 960 ypos 255 action (Hide('lroom11pmkiss4'), Jump('lroom11pmstop2')) hovered tt.Action ("Stop her [lv1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom11pmhj:
    scene livingroom 11pm 010
    pov "Then how about you show me how much you missed me?"
    pov "{i}I won't let her stop now.{/i}"
    mom "You want me to play with you? I'm so glad Adam."
    pov "{i}I wonder if I could get her to say my real name some time?{/i}"
    "She start to unpack your dick."
    scene livingroom 11pm 011b
    if inc == True:
        pov "{i}Oh my god. What a view! Mom's sexy hand on my dick.{/i}"
    else:
        pov "{i}Oh my god. What a view! [mother]'s sexy hand on my dick.{/i}"
    mom "So big and warm..."
    pov "It's good you like it."
    if inc == True:
        pov "{i}This is heaven. Don't stop here mom!{/i}"
    else:
        pov "{i}This is heaven. Don't stop here [mother]!{/i}"
    mom "Let's make it hard after not seeing him for so long."
    pov "{i}I wonder what time she became such a prude and if I can get her real naughty side back forever.{/i}"
    scene livingroom 11pm 012b
    mom "It's getting bigger and bigger."
    pov "Because it's you touching it. You're hands are like magic."
    mom "<giggle> I'm so happy."
    pov "Me too."
    pov "{i}Damn. You have no idea.{/i}"
    mom "But something... is wrong..."
    pov "{i}What...? No, no, no...{/i}"
    scene livingroom 11pm 013b
    mom "It's bigger then the old times. My hand looks so small suddenly."
    pov "{i}Oh! So is my penis bigger than my dad's?{/i}"
    mom "Could a penis grew up so much?"
    pov "You're right! It never was that big before. But we have never been separated so long before."
    pov "I'm so hard because I desired you for so long!"
    mom "Oh... you got so big because of me?"
    if inc == True:
        pov "{i}Getting a hand-job from my hot mom? He should get even bigger!{/i}"
    else:
        pov "{i}Getting a hand-job from you? He should get even bigger!{/i}"
    pov "{i}Let me make you feel god too.{/i}"
    scene livingroom 11pm 014b
    image hjnic_lroom = Movie(channel="hjnic_lroom", play="images/anim/hjnic_lroom.webm")
    scene hjnic_lroom with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    mom "Hmm..."
    pov "{i}Yes! Finally. I can touch her boobs and she wants me to do it.{/i}"
    mom "You always loved to grope my breasts, don't you?"
    pov "You have no idea how I missed your big tits."
    pov "{i}And how often I dreamed about that!{/i}"
    mom "Don't leave me alone for such a long time again. I missed your firm touches."
    pov "{i}My dick won't last long if you talk to me like that!{/i}"
    pov "You can bet on that, [mother]!"
    pov "I love playing with your nipples."
    mom "Hnng... hah..."
    pov "Pulling them to see your nice reactions."
    mom "They are yours always."
    pov "{i}I wonder why dad ever left us? It had to be very import to leave such a hot woman.{/i}"
    mom "I love how your dick pulsates. I can even remember how it pulsated in me."
    pov "{i}Hell! How should I endure this until then?{/i}"
    scene livingroom 11pm 016b
    mom "Hiii..."
    pov "Such a nice reaction."
    mom "Hmm..."
    pov "{i}Oh shit. She's squeezing my dick like crazy. I can't hold it any longer!{/i}"
    pov "{i}Her dirty talking, that view, her big and soft boobs and her firm grip. I'll come so hard!{/i}"
    scene livingroom 11pm 017b
    pov "Argghh...! Yes... more..."
    mom "You're about to cum already?"
    mom "Was my touching that good? <giggle>"
    pov "{i}If this is a dream don't let me wake up now!{/i}"
    if inc == True:
        pov "Yes, yes... YES! MOM!"
    else:
        pov "Yes, yes... YES! [mother]!"
    pov "Hmm..."
    mom "Wow so warm..."
    scene livingroom 11pm 018b
    mom "That much came out..."
    if inc == True:
        pov "{i}That's so damn hot. Mom's staring at my cum after she released me!{/i}"
    else:
        pov "{i}That's so damn hot. [mother]'s staring at my cum after she released me!{/i}"
    pov "It has to be that amount after your pressing was so wonderful!"
    mom "Did I make you felt that good? But still that much...?"
    pov "{i}Damn she must really have loved him. And now I'm his replacement!{/i}"
    pov "{i}I would love it when she would lick it from her fingers right now, or smear it over her tits.{/i}"
    pov "{i}But I must see how she reacts tomorrow first. It's to soon now!{/i}"
    mom "So warm..."
    if inc == True:
        pov "{i}Drunk mom is staring at my cum...{/i}"
    else:
        pov "{i}Drunk [mother] is staring at my cum...{/i}"
    pov "{i}I better leave her now. I'm sure she'll sleep good tonight, haha.{/i}"
    $ momcorruption += 1
    $ lroom11hj = True
    $ dtime += 1
    jump lroom

label lroom11pmstop2:
    $ lroom11makeout = True
    jump lroom11pmstop


label lroom11pmstop:
    scene livingroom 11pm 011a
    pov "Stop it! I'm not Adam!"
    mom "What...? Why?"
    if inc == True:
        pov "It's enough and it's wrong, mom!"
    else:
        pov "It's enough and it's wrong, [mother]!"
    mom "..."
    scene livingroom 11pm 012a
    mom "Did I do something wrong? Why are you mad at me, Adam?"
    pov "{i}Damn, she don't get it.{/i}"
    if inc == True:
        pov "I'm not Adam! I'm your son, [pov]!"
        mom "What are you talking about, Adam?"
        pov "{i}Shit, drunk mom is a stupid mom...{/i}"
        pov "You're my mother and I'm your son and I'm sure this Isn't something we should do."
        pov "{i}At least not now and especially not when you're drunk.{/i}"
    else:
        pov "I'm not Adam! I'm his son, [pov]!"
        mom "What are you talking about, Adam?"
        pov "{i}Shit, drunk [mother] is a stupid [mother]...{/i}"
        pov "I know you and we have such a good relationship so I'm sure this Isn't something we should do."
        pov "{i}At least not now and especially not when you're drunk.{/i}"
    mom "Oh, so..."
    scene livingroom 11pm 013a
    mom "Oh my god! [pov]!"
    pov "That's what I'm trying to tell you!"
    mom "It's you! I thought of were someone else!"
    mom "What have I done...?"
    pov "Calm down. It's not so bad. No need to freak out because of that."
    mom "But... Oh... no...!"
    scene livingroom 11pm 014a
    if inc == True:
        mom "I made out with my own son! This is so wrong!"
    else:
        mom "I made out with you! This is so wrong!"
    pov "Relax! I won't take any damage from it. And you're drunk. Things like that can happen."
    mom "I put my tongue in your mouth!"
    if inc == True:
        mom "Bring my own son in a make-out with me..."
        mom "..."
        pov "Please mom. Don't take it that seriously."
    else:
        mom "Bring you in a make-out with me..."
        mom "..."
        pov "Please [mother]. Don't take it that seriously."
    mom "Nooo...!"
    scene livingroom 11pm 015a
    mom "I'm so sorry...!"
    pov "Please calm down. It's my fault too..."
    mom "No! I was the one. I can't... so... sorry..."
    pov "{i}Damn, but it's no use. Hopefully I can have a normal conversation with her about that tomorrow when she's sober again.{/i}"
    pov "{i}But her kissing was so damn good.{/i}"
    $ momlove += 1
    $ lroom11kiss = True
    $ dtime += 1
    jump lroom