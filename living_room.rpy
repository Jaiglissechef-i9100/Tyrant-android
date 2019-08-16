#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 8am Living Room - MC, Nicole - love, Corruption
# 2. 10am Lving Room - Cassandra, MC - Love, Corruption
# 3. 3pm Living Room - Cassandra, Irina - Love, Corruption
# 4. 2pm Living Room - MC, Nicole - Love, Corruption
# 5. 9pm Living Room - Bruce, Davide, MC - Good, Bad (Drug Delivery)
# 6. 9pm Living Room - Bruce, Davide, Miranda, MC, Nicole, Vivian - Love, Corruption, Darker Paths (Join Gang)
# 7. 10pm Living Room, Basement - Bruce, Davide, MC, Nicole - Love, Corruption, Darker Paths
# 8. 11pm Living Room, Basement - MC, Nicole - Love, Corruption

#----- End List -----

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
    povi "Her ass is so damn hot, I can't stop looking."
    jump lroom

label lroom8momslap:
    hide screen locations
    scene livingroom 8am 002
    povi " Let's slap that ass!"
    with vpunch
    $ momcorruption += 1
    scene livingroom 8am 003
    mom "Aaaahh..."
    povi "Damn, that was hot."
    $ vlroom8momslap += 1
    jump lroom8momtalk

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
        pov "It needed to be done. I need to play the bad boy remember."
        scene livingroom 8am 005
        mom "Oh... but did you need to slap me?"
        pov "Yes when you're sticking your ass out like that! I did what any bad boy would do!"
        if inc == True:
            mom "But I'm your mother!"
        else:
            mom "You can't do that to me!"
        pov "No, in this house you're supposed to be just another gang bitch."
        mom "But..."
        pov "I'm just trying to play my part well..."
        mom "..."
        #if vlroom8momtalknight2 == True: ----- Added in 0.6.5
            #jump lroom8momtalk3 ----- Added in 0.6.5
        if NTR == True:
            if inc == True:
                pov "By the way, you were in the basement that night with dad's friends, right?"
            else:
                pov "By the way, you were in the basement that night with Bruce's friends, right?"
            mom "Y... yes, but why are you asking?"
            if inc == True:
                pov "What were you doing there without dad?"
                mom "We... we just talked and waited for your dad."
            else:
                pov "What were you doing there without Bruce?"
                mom "We... we just talked and waited for him."
            pov "Oh in that case, can I join you next time?"
            if basementkey == False:
                scene livingroom 8am 005a
                mom "No!"
                scene livingroom 8am 005b
                mom "I mean it's not possible yet. It's like their secret hideout and only trusted members can go down there."
                povi "She lying to me. I need to find out what she's hiding. And why she doesn't feel like she can tell me about it."
                pov "Okay, I understand."
            else:
                scene livingroom 8am 005a
                mom "No!"
                scene livingroom 8am 005b
                mom "I mean... Well you are member of the gang now, so I guess you can."
                povi "She's really nervous about me being down there with them in the basement. I wonder why?"
                pov "Sounds good then."
    elif vlroom8momslap > 1:
        if momrelationship < 30 and momntr == True:
            $ randomnum = renpy.random.randint(1,2)
            if randomnum == 1:
                jump nicoleshakylroom
            elif randomnum == 2:
                " "
        scene livingroom 8am 005
        mom "Hnnn..."
        pov "Starting to enjoy that, aren't you?"
        #if vlroom8momtalknight2 == True: ----- Added in 0.6.5
            #jump lroom8momtalk3 ----- Added in 0.6.5
        if NTR == True:
            if inc == True:
                pov "By the way, you were in the basement that night with dad's friends, right?"
            else:
                pov "By the way, you were in the basement that night with Bruce's friends, right?"
            mom "Y... yes, but why are you asking?"
            if inc == True:
                pov "What were you doing there without dad?"
                mom "We... we just talked and waited for your dad."
            else:
                pov "What were you doing there without Bruce?"
                mom "We... we just talked and waited for him."
            pov "Oh in that case, can I join you next time?"
            if basementkey == False:
                scene livingroom 8am 005a
                mom "No!"
                scene livingroom 8am 005b
                mom "I mean it's not possible yet. It's like their secret hideout and only trusted members can go down there."
                povi "She lying to me. I need to find out what she's hiding. And why she doesn't feel like she can tell me about it."
                pov "Okay, I understand."
            else:
                scene livingroom 8am 005a
                mom "No!"
                scene livingroom 8am 005b
                mom "I mean... Well you are member of the gang now, so I guess you can."
                povi "She's really nervous about me being down there with them in the basement. I wonder why?"
                pov "Sounds good then."
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
        mom "Cleaning up the alcohol bottles from last night."
        #if vlroom8momtalknight2 == True: ----- Added in 0.6.5
            #jump lroom8momtalk3 ----- Added in 0.6.5
        pov "Oh, I thought they were yours."
        mom "Haha, no."
        if lroom8momtalkfirst == True:
            pov "I'm already a little confused about the things that happened yesterday."
            mom "You'll get used to it fast. I know that for sure."
            pov "Oh..."
            $ lroom8momtalkfirst = False
        if NTR == True:
            if inc == True:
                pov "By the way, you were in the basement that night with dad's friends, right?"
            else:
                pov "By the way, you were in the basement that night with Bruce's friends, right?"
            mom "Y... yes, but why are you asking?"
            if inc == True:
                pov "What were you doing there without dad?"
                mom "We... we just talked and waited for your dad."
            else:
                pov "What were you doing there without Bruce?"
                mom "We... we just talked and waited for him."
            pov "Oh in that case, can I join you next time?"
            if basementkey == False:
                scene livingroom 8am 005a
                mom "No!"
                scene livingroom 8am 005b
                mom "I mean it's not possible yet. It's like their secret hideout and only trusted members can go down there."
                povi "She lying to me. I need to find out what she's hiding. And why she doesn't feel like she can tell me about it."
                pov "Okay, I understand."
            else:
                scene livingroom 8am 005a
                mom "No!"
                scene livingroom 8am 005b
                mom "I mean... Well you are member of the gang now, so I guess you can."
                povi "She's really nervous about me being down there with them in the basement. I wonder why?"
                pov "Sounds good then."
    pov "I didn't mind you playing your part last night though. Sitting there in that slutty dress."
    if inc == True:
        mom "Your dad chose it for me. He thinks it suits me when I'm around his \"friends\"."
    else:
        mom "Bruce chose it for me. He thinks it suits me when I'm around his \"friends\"."
    jump l8a1

label l8a1:
    if vlroom8momslap == 1:
        scene livingroom 8am 005
    else:
        scene livingroom 8am 004lo
    call screen l8a1s

screen l8a1s():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('l8a1s'), Jump('lroom8momtalklove')) hovered tt.Action ("Answer to improve Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('l8a1s'), Jump('lroom8momtalkcor')) hovered tt.Action ("Answer to improve Corruption [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
    pov "You're right. You're doing the best you can in a bad situation."
    mom "Thank you..."
    jump lroom8momtalk2

label lroom8momtalkcor:
    pov "Yes I like that slutty dress too. It shows your body better."
    $ momcorruption += 1
    if vlroom8momslap == 1:
        scene livingroom 8am 007
    else:
        scene livingroom 8am 006lo
    mom "You shouldn't look at me that way. It's just for our cover."
    if droom7momlookcor == True:
        pov "You remember what we talked about before? I'm just trying to get used to it."
        mom "Yes..."
    else:
        if inc == True:
            pov "Sure! You should take it as a compliment! Not everyone's mom look so hots in a short dress."
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
    pov "Oh, is she anyone I know?"
    mom "No. You don't know her. We're just getting manicures. I need to stay beautiful for this role."
    pov "Right, well have fun then."
    mom "Thank you [pov]!"
    jump l8a2

label l8a2:
    call screen l8a2s

screen l8a2s():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_hug_%s.png" action (Hide('l8a2s'), Jump('lroom8momtalklove2')) hovered tt.Action ("Hug [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('l8a2s'), Jump('lroom8momtalkcor2')) hovered tt.Action ("Don't hug") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
        mom "What is it for?"
        if inc == True:
            pov "I just want a hug from my mom in the morning."
        else:
            pov "I just want a hug from you in the morning."
        mom "That's so sweet, [pov]!"
    $ vlroom8momhug += 1
    $ momlove += 1
    pov "You're welcome."
    $ vlroom8momtalknight2 = True
    $ dtime = 9
    jump lroom

label lroom8momtalkcor2:
    if vlroom8momslap == 1:
        scene livingroom 8am 009
    else:
        scene livingroom 8am 009lo
    mom "Okay then, see you later. And you could try to find a job or feel free to do anything else around the house."
    pov "And if I want to go in to town?"
    mom "Please don't do that yet. It's better if someone goes with you there the first time."
    mom "This role has created enemies out of some people who don't like us."
    pov "Oh, gang enemies?"
    mom "Yes, something like that."
    pov "Ok. See you later."
    $ vlroom8momtalknight2 = True
    $ dtime = 9
    jump lroom

label lroom10bsistits:
    hide screen locations
    scene livingroom 10am 002b
    povi "Damn she's so hot right now. She's stacked! She's so beautiful while concentrating on staying in shape."
    jump lroom

label lroom10bsiscrotch:
    hide screen locations
    scene livingroom 10am 002a
    povi "There isn't much covering her pussy and asshole, just those tiny panties."
    jump lroom

label lroom10bsisfeet:
    hide screen locations
    scene livingroom 10am 002c
    povi "She has some cute little feet."
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
    bs "Oh hey... What you're looking for, little perv?"
    pov "Oh I'm just seeing what's going on in here."
    pov "What are you doing?"
    scene livingroom 10am 004
    if vlroom10trainfirst == True:
        bs "I'm training, can't you see?"
    else:
        bs "I'm training again, dummy."
    pov "Oh yeah, sure."
    bs "I do my best to stay in shape, unlike the other girls around town."
    scene livingroom 10am 005
    pov "Oh, is that a personal trainer channel."
    bs "Yes. There are always new lessons being released and they're very good."
    scene livingroom 10am 006
    bs "It's sometimes a little harder than the previous lessons but it's necessary."
    povi "I know something else getting a little hard right now."
    pov "Yeah these lessons seem to be a good thing."
    scene livingroom 10am 007
    if vlroom10trainfirst == True:
        bs "Can you help me again?"
        if vlroom10firstposcor == True:
            bs "But this time do it right please."
            pov "Hmm... sure."
    else:
        bs "Hey do you think you can help me out?!"
        pov "Help you?"
        povi "Yes!!! Let me help you!"
        bs "Can you count off my reps so I know when to change positions?"
        pov "Hmm...?"
        bs "Sit down, I'll explain."
        scene livingroom 10am 008
        povi "Thank you God! I don't know if you approve of this sort of thing... but fucking thank you!"
        bs "There will be a counter going down on the show, but I can't see it from here. So can you count down for me?"
        scene livingroom 10am 009b
        povi "But then I won't be able to watch you..."
        bs "Can you do that for me?"
    $ vlroom10trainfirst = True
    jump lroom10ft

label lroom10ft:
    scene livingroom 10am 009b
    call screen lroom10ft1

screen lroom10ft1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lroom10ft1'), Jump('lroom10bsisfirsttrainlove')) hovered tt.Action ("Help her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lroom10ft1'), Jump('lroom10bsisfirsttraincor')) hovered tt.Action ("Help her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom10bsisfirsttrainlove:
    pov "Okay, I'll do it."
    bs "Great, let's get started."
    pov "5"
    bs "..."
    pov "4"
    bs "Hnn..."
    povi "Just a quick look."
    scene livingroom 10am 009a
    bs "Hmm..."
    povi "Damn I'm missing the best show. But I told her I would help."
    scene livingroom 10am 009b
    pov "3"
    pov "At least the girl on the TV isn't that bad either."
    bs "Hmm..."
    pov "2"
    bs "Hah..."
    povi "She's moaning from the effort. So hot."
    pov "1"
    bs "Hah..."
    pov "Done."
    scene livingroom 10am 010b
    bs "You did good. Looks like we finally found something you're good at, haha."
    pov "You're welcome."
    povi "Interesting. When she wants something she doesn't act like an angry bitch."
    $ vlroom10firstposlove = True
    $ vlroom10firstposcor = False
    $ bigsislove += 1
    scene livingroom 10am 011b
    if vlroom10trainfirst == True:
        bs "Could you help me again?"
        if vlroom10secposcor == True:
            bs "But you better not grope my tits again!"
            pov "Okay..."
        else:
            bs "You were such a good help last time."
            pov "Okay..."
    else:
        bs "Oh, that lesson is good, but I can never do it."
        pov "Why?"
        bs "There are two people needed and normally I'm all alone in the mornings."
        scene livingroom 10am 012
        bs "Do you got time to help me with this one?"
        pov "Again?"
        bs "Yes please! The lesson will be good for you too."
        pov "But I'm in good shape?"
        bs "Come on, please!"
    jump lroom10ft2

label lroom10ft2:
    scene livingroom 10am 012
    call screen l10ft3

screen l10ft3():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lroom10ft1'), Jump('lroom10bsissectrainlove')) hovered tt.Action ("Help her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lroom10ft1'), Jump('lroom10bsissectraincor')) hovered tt.Action ("Help her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom10bsissectrainlove:
    pov "Okay, I can do that."
    bs "Good stay right there."
    scene livingroom 10am 013
    povi "Wow, she's pressing her ass against my dick. I wonder what will happen when she notices my boner."
    bs "I will fall now slowly forward and you have to hold me."
    pov "Okay...?"
    povi "And now she's pressing her hot body against me. She has such soft skin."
    bs "It's good all around exercise, but is especially good for the ass."
    pov "Okay!"
    povi "Then I will love that too."
    bs "Ready?"
    pov "Sure."
    scene livingroom 10am 014
    bs "Don't let me fall over."
    pov "Sure, I can hold you, don't worry."
    povi "Oh my god! Her ass is killing me. I just want to fuck her right now!"
    bs "Oh this is good, I can feel it stretching my muscles."
    pov "Hell yeah."
    bs "Hmm...?"
    pov "Oh nothing, it's alright."
    scene livingroom 10am 015
    bs "You're being such a good training partner. Just a moment longer."
    povi "I could hold you all my life in this position."
    pov "Sure."
    bs "Hmm..."
    povi "Did she notice my boner? But she's not stopping? Maybe she just wants to do this training position that badly?"
    bs "O... okay, that's it."
    povi "Nooo..."
    scene livingroom 10am 016
    if vlroom10secposlove == True:
        bs "Wow! You did great again. You could be my personal trainer, haha."
        pov "..."
        povi "You have no idea."
        bs "Relax, I'm just kidding, haha."
    else:
        bs "Wow I'm surprised. You didn't act like a jerk and actually helped me."
        pov "Of course..."
        bs "And you didn't try pervy things. Maybe you really learned manners at that overseas school of yours."
        pov "If you say so."
        povi "Then she didn't notice my boner, but is this good?"
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
    povi "I don't care about this shit, I must see her."
    scene livingroom 10am 009a
    bs "..."
    povi "Such a hot position. Maybe she can do some naked training some time for me, haha?"
    bs "What's wrong?"
    pov "Oh, 4..."
    scene livingroom 10am 008
    povi "Relax... Calm down..."
    bs "Hmm..."
    bs "..."
    pov "Ahem... 3"
    scene livingroom 10am 009a
    povi "This is tougher on me than it is on her!"
    bs "Hnn..."
    bs "..."
    scene livingroom 10am 010a
    if vlroom10firstposcor == True:
        bs "You did it again!"
        pov "But..."
        bs "You're no help to me!"
    else:
        bs "What are you doing you idiot?"
        povi "Oh... oh..."
        bs "Your counting is completely off!"
        pov "I... I just..."
        bs "I should've known you would suck at this, thanks for nothing jerk!"
    pov "..."
    $ vlroom10firstposlove = False
    $ vlroom10firstposcor = True
    $ bigsiscorruption += 1
    $ dtime = 11
    jump lroom

label lroom10bsissectraincor:
    pov "Okay, I can do that."
    bs "Good stay right there."
    scene livingroom 10am 013
    povi "Wow, she's pressing her ass against my dick. I wonder what will happen when she notices my boner."
    bs "I will fall now slowly forward and you have to hold me."
    pov "Okay...?"
    povi "And now she's pressing her hot body against me. She has such soft skin."
    bs "It's good all around exercise, but is especially good for the ass."
    pov "Okay!"
    povi "Then I will love that too."
    bs "Ready?"
    pov "Sure."
    scene livingroom 10am 014
    bs "Don't let me fall over."
    pov "Sure, I can hold you, don't worry."
    povi "Oh my god! Her ass is killing me. I just want to fuck her right now!"
    bs "Oh this is good, I can feel it stretching my muscles."
    pov "Hell yeah."
    bs "Hmm...?"
    povi "Maybe it's time to rescue her from falling over."
    scene livingroom 10am 015a
    bs "Huh? What?"
    if inc == True:
        pov "It's okay big sis, I'm just holding you so you won't fall over."
    else:
        pov "It's okay [bs], I'm just holding you so you won't fall over."
    bs "Come on! Stop it!"
    pov "No! You'll fall over. I'm here to prevent that. I'm taking my job seriously!"
    povi "I'll never take my hands off these firm breats."
    scene livingroom 10am 016a
    if vlroom10secposcor == True:
        bs "You groped me again, you jerk!"
        pov "No I just wanted to save you like last time."
        bs "Are you that stupid you think I dumb enough to fall that excuse?"
        pov "No... but..."
        bs "Fuck you!"
    else:
        bs "You damn asshole. I should have known that you would take the chance to grope me."
        pov "No. I just wanted to prevent you from falling over."
        bs "Sure! You're still a pervert!"
        pov "But you wanted me to do that. I was just trying to help."
        bs "..."
        bs "Maybe... but I don't know for sure..."
        pov "I'm telling the truth."
        povi "I would and will say anything for boob grabs, anything..."
    $ vlroom10secposlove = False
    $ vlroom10secposcor = True
    $ bigsiscorruption += 1
    $ dtime = 11
    jump lroom

label lroom15tits:
    hide screen locations
    hide screen townl
    scene livingroom 3pm 002a
    povi "Wow what a nice rack. And those lips too."
    jump lroom

label lroom15crotch:
    hide screen locations
    hide screen townl
    scene livingroom 3pm 002b
    povi "That flat belly. I wonder if she's shaved and what her ass looks like."
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
    povi "I wonder who she is? Maybe a friend of a family member?"
    povi "Time to find out."
    pov "Hi!"
    "Girl" "Eh?"
    scene livingroom 3pm 004a
    povi "Wow, she's checking me out."
    scene livingroom 3pm 004b
    "Girl" "Oh, hello."
    pov "Hello, I'm [pov]. I live here."
    "Girl" "Really? I haven't seen you before."
    pov "I was overseas for a year. And you are?"
    "Girl" "Oh how rude of me."
    if irinafirstmeet == False:
        $ irinaname = renpy.input(_("My name is...")) or _("Irina")
        $ irinaname = irinaname.strip()
        if irinaname == "":
            $ irinaname = "Irina"
    scene livingroom 3pm 005
    pov "Nice to meet you [irina]!"
    irina "Oh... yeah it's nice to meet you too."
    pov "Did I do something wrong?"
    scene livingroom 3pm 006
    irina "No! It's just that doesn't happen often here. Someone wanting to shakes hands."
    pov "No?"
    irina "Most people here are rude or egoists."
    irina "So that was a very nice surprise."
    pov "Oh then you're welcome I guess. Haha."
    scene livingroom 3pm 007
    if inc == True:
        irina "So you're [bs]'s little brother of?"
    else:
        irina "So you're living with [bs]'s family?"
    pov "Yeah I am. Has she told you about me?"
    irina "Some things. But not how cute you are. <giggle>"
    pov "Thanks! Not as cute as you are though."
    scene livingroom 3pm 008
    bs "I'm done! We can go now [irina]."
    irina "Maybe I'm good to stay here awhile."
    bs "What do you..."
    scene livingroom 3pm 009
    if inc == True:
        bs "Oh! It's my little brother!"
    else:
        bs "Oh! It's you!"
    bs "Did you try to do pervy things to my friend?"
    pov "Well not yet, we just met!"
    irina "<giggle>"
    bs "Watch this one [irina]. He's a pervert!"
    scene livingroom 3pm 010
    bs "So it's time to go [pov]. You met my friend and now it's time for you to go about your own business."
    pov "I wanted to hang out with you though, remember how you promised to hold my hand as we cross the street."
    bs "Cut it out! We have no time for your games."
    irina "I think, I like him."
    bs "No you don't. He must have tricked you [irina]."
    jump lr3gf

label lr3gf:
    call screen lr3gf1

screen lr3gf1:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lr3gf1'), Jump('lroom15love')) hovered tt.Action ("Answer to improve Love [lv1]/[bs]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lr3gf1'), Jump('lroom15cor')) hovered tt.Action ("Answer to improve Corruption [cr1]/[bs]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom15love:
    pov "Don't worry [irina]. She isn't always so crazy angry."
    pov "Let me give ya a hug before you go!"
    scene livingroom 3pm 011b
    bs "What are you..."
    pov "Come here! I love ya [bs], calm down."
    irina "Oh..."
    bs "What..."
    scene livingroom 3pm 012b
    bs "Are you fucking crazy? Hugging me out of nowhere!"
    pov "You're welcome!"
    bs "I swear I'm going to kill you one day!"
    irina "Wow. That was so sweet of you."
    irina "Maybe... I can have a hug too?"
    $ bigsislove += 1
    jump lr3irina

label lroom15cor:
    pov "I'm sorry [irina], but [bs] wants me all to herself, we're lover you know."
    pov "She tell everyone that I'm a pervert to keep the competition away."
    scene livingroom 3pm 012a
    bs "Are you fucking crazy? What the hell are you talking about?"
    irina "Hahahaha..."
    pov "Don't be mad, I'm sure [irina] will keep our secret."
    bs "How dare you..."
    pov "Our love is eternal!!!"
    irina "I've never laughed that hard. Wonderful!"
    bs "And you're on his side now. You're as crazy as he is!"
    pov "Oh come on [bs]! I will never leave you! Get back here and hug me lover!"
    irina "Hahahaha..."
    bs "Fuck you two..."
    $ bigsiscorruption += 1
    jump lroom15bend

label lr3irina:
    call screen lr3irina1

screen lr3irina1:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lr3irina1'), Jump('lroom15mlove')) hovered tt.Action ("Answer to improve Love [lv1]/[irina]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lr3irina1'), Jump('lroom15mcor')) hovered tt.Action ("Answer to improve Corruption [cr1]/[irina]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom15mcor:
    pov "No, not yet. That's something you have to earn."
    irina "Oooh, but it looked so nice."
    pov "Well once you've earned it for yourself, I'll hug you all you want."
    irina "<giggle> Now I'm curious."
    bs "He's just a pervert like I said."
    $ irinacorruption += 1
    jump lroom15gend

label lroom15mlove:
    pov "Sure, come here [irina]!"
    scene livingroom 3pm 013b
    irina "Hmm..."
    pov "Everyone loves to get hugged."
    irina "That's such a sweet idea. It's been a long time since someone's hugged me."
    bs "What are..."
    bs "I'm out of here! You can't be serious!"
    $ irinalove += 1
    jump lroom15gend

label lroom15bend:
    scene livingroom 3pm 013a
    irina "Haha, that was amazing. I never saw [bs] so angry!"
    pov "I thought it was fun too."
    irina "You're an interesting guy, maybe we can meet up sometime later?"
    pov "Sure why not."
    irina "See you [pov]."
    pov "Bye [irina]."
    $ dtime += 1
    $ irinafirstmeet = True
    jump lroom

label lroom15gend:
    scene livingroom 3pm 014
    irina "Wow, you're full of surprises [pov]."
    pov "What do you mean?"
    irina "You're like a true gentleman in a slum. Almost all the men here are jerks to women."
    pov "Well it's becuase you're worth it."
    irina "Oh my god. You're so sweet."
    irina "Can we meet up again, please?"
    pov "Sure, I would like that too."
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
        povi "Oh mom's sleeping. She's so tired all the time."
    else:
        povi "Oh [mother]'s sleeping. She's so tired all the time."
    jump lroom14momcloser2

label lroom14momcloser2:
    if NTR == True and momrelationship < 6 and momntr == True or hardntr == True:
        mom "Ohh..."
        povi "She's dreaming?"
        mom "Fuck me harder!"
        povi "..."
        mom "Punish my pussy more with your black rod."
        povi "What, black...? So Davide is fucking her in the basement!"
        if inc == True:
            povi "That asshole. Fucking my mom. I'll get rid of him and make her mine again."
        else:
            povi "That asshole. Fucking [mother]. I'll get rid of him and make her mine again."
        jump lroom14momcloser3
    elif momrelationship >= 6 and momlove >= 50:
        mom "Ohh..."
        povi "She's dreaming?"
        mom "Fuck me harder!"
        povi "..."
        mom "Punish my pussy more [pov]."
        povi "She's dreaming about fucking me?!?"
        povi "We should make this dream a reality soon!"
        jump lroom14momcloser3
    elif momrelationship >= 6 and momlove < 50:
        povi "I wonder if what they do in the basement is the reason she's so tired?"
    else:
        povi "I wonder if what they do in the basement is the reason she's so tired?"
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
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('l14l1'), Jump('lroom14legs')) hovered tt.Action ("Look at legs") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('l14l1'), Jump('lroom14feet')) hovered tt.Action ("Look at feet") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('l14l1'), Jump('lroom14momcloser4')) hovered tt.Action ("Stop looking") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
    povi "She has such beautiful legs. You can see the outline of her pussy, wrapped tightly in those leggings."
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
    povi "I wonder if she has ever given a footjob?"
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
    povi "Let's have some fun to make enjoy that dream even more."
    povi "And I can enjoy it too."
    jump l14grope

label l14grope:
    call screen l14grope1

screen l14grope1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if nicolereddresswear == True or nicolerobewear == True or nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
            imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('l14grope1'), Jump('lroom14gtits')) hovered tt.Action ("Grope tits [lv1]/[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('l14grope1'), Jump('lroom14gcrotch')) hovered tt.Action ("Grope crotch [lv1]/[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('l14grope1'), Jump('lroom14abort')) hovered tt.Action ("Let her sleep") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom14gtits:
    if momcorruption < 20 and momlove < 20:
        if inc == True:
            povi "Damn I'm so horny. Mom's sleeping, I'm sure she won't mind if I have a little fun."
        else:
            povi "Damn I'm so horny. [mother]'s sleeping, I'm sure she won't mind if I have a little fun."
        povi "I need to see her big tits."
        if nicolereddresswear == True:
            scene livingroom 2pm 003ncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 003ncl2
        else:
            scene livingroom 2pm 003
        povi "Oh my god! Yes, yes, yes..."
        povi "Maybe a little bit more!"
        if nicolereddresswear == True:
            scene livingroom 2pm 004ncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 004ncl2
        else:
            scene livingroom 2pm 004
        povi "Ohh... I'm so close to them, I just want to lick them!"
        mom "Hmm..."
        povi "Shit. She's about to wake up. Better cover her back up and get out."
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

    elif momcorruption > 20 and momcorruption < 40 or momlove > 20 and momlove < 40:
        if inc == True:
            povi "Damn I'm so horny. Mom's sleeping, I'm sure she won't mind if I have a little fun."
        else:
            povi "Damn I'm so horny. [mother]'s sleeping, I'm sure she won't mind if I have a little fun."
        povi "I need to play with her tits."
        if nicolereddresswear == True:
            scene livingroom 2pm 005bncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 005bncl2
        else:
            scene livingroom 2pm 005b
        povi "Yes, they're so soft and warm."
        mom "Hmm..."
        povi "Oh yes, she's feeling it in her dream."
        if inc == True:
            povi "It's me, your son giving you a good time."
        else:
            povi "It's me, [pov] giving you a good time."
        povi "It's probably better to stop now. No need for her to catch me now."
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

    elif momcorruption > 40 or momlove > 40:
        if inc == True:
            povi "Damn I'm so horny. Mom's sleeping, I'm sure she won't mind if I have a little fun."
        else:
            povi "Damn I'm so horny. [mother]'s sleeping, I'm sure she won't mind if I have a little fun."
        povi "I need to play with her tits again. But this time I want to feel her flesh."
        if nicolereddresswear == True:
            scene livingroom 2pm 006bncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 006bncl2
        else:
            scene livingroom 2pm 006b
        povi "Even better! I hope you can feel my hand kneading your breast."
        if momlove > momcorruption:
            povi "Soon you'll love only me."
        elif momlove < momcorruption:
            povi "Sooo you'll beg for me to touch you!"
        else:
            povi "Soon you'll be mine."
        mom "Hmm... hah..."
        povi "She's moaning, so she likes it. I bet she's dreaming about it."
        povi "Time for more."
        if nicolereddresswear == True:
            scene livingroom 2pm 007bncc1
        elif nicolerobewear == True:
            scene livingroom 2pm 007bncl2
        else:
            scene livingroom 2pm 007b
        mom "Hah... hah..."
        povi "Damn, is she waking up or is she getting off."
        mom "Hmm... hah..."
        if inc == True:
            povi "Wow more like the second one. Enjoy my touching, mom."
        else:
            povi "Wow more like the second one. Enjoy my touching, [mother]."
        if NTR == True and momrelationship < 6 and momntr == True:
            mom "Ohh... hah... yes..."
            mom "Punish me more, my black master!"
            povi "Nooo! It's me [pov]! I'm giving you the good feeling."
        mom "Hah... eh...?"
        povi "Oh shit. Now she's about to wake up. I need to stop it fast."
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

label lroom14gcrotch:
    if momcorruption < 20 and momlove < 20:
        if inc == True:
            povi "Damn I'm so horny. Mom's sleeping, I'm sure she won't mind if I have a little fun."
        else:
            povi "Damn I'm so horny. [mother]'s sleeping, I'm sure she won't mind if I have a little fun."
        povi "Let's caress those beautiful legs."
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
        povi "So firm and warm. I wonder if she works out?"
        povi "But what I really need is to get closer to that pussy!"
        mom "Hmm..."
        povi "Shit. She's about to wake up. Maybe I'll have another chance later."
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

    elif momcorruption > 20 and momcorruption < 40 or momlove > 20 and momlove < 40:
        if inc == True:
            povi "Damn I'm so horny. Mom's sleeping, I'm sure she won't mind if I have a little fun."
        else:
            povi "Damn I'm so horny. [mother]'s sleeping, I'm sure she won't mind if I have a little fun."
        povi "Let's caress those beautiful legs."
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
        povi "Maybe I can touch her pussy this time?"
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
        povi "Oh yes, that's nice."
        povi "Is she having a naughty dream? I can feel her wet pussy through the leggings."
        mom "Hmm..."
        povi "Oh wow, is she's feeling it in her dreams?"
        povi "It's me, [pov]. Giving you a good time."
        povi "It's probably better to stop now. No need for her to catch me now."
        $ momrelationship += 1
        $ momlove += 1
        $ momcorruption += 1
        $ dtime += 1
        jump lroom

    elif momcorruption > 40 or momlove > 40:
        if inc == True:
            povi "Damn I'm so horny. Mom's sleeping, I'm sure she won't mind if I have a little fun."
        else:
            povi "Damn I'm so horny. [mother]'s sleeping, I'm sure she won't mind if I have a little fun."
        povi "I think now it's time to play with her pussy."
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
        povi "Yes, yes, yes. I'm rubbing her pussy."
        povi "And she's already wet. She must be dreaming about something good."
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
        povi "Very nice. She's enjoying it."
        if inc == True:
            povi "You're so damn sexy mom. I'll help you have an even better time now."
        else:
            povi "You're so damn sexy [mother]. I'll help you have an even better time now."
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
        povi "Wow, she spread her legs. She's really enjoying it."
        if inc == True:
            povi "Yes mom, enjoy yourself while your son is getting you off."
        else:
            povi "Yes [mother], enjoy yourself while I'm getting you off."
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
        povi "Damn, is she waking up or is she getting close to cumming."
        mom "Hmm... hah..."
        if inc == True:
            povi "Wow more like the later. Enjoy my touch, mom."
        else:
            povi "Wow more like the later. Enjoy my touch, [mother]."
        if momrelationship >= 6 and momlove or momcorruption >= 75:
            mom "Ohh... hah... yes..."
            if momcorruption > momlove:
                mom "Ram your hard dick into your slut, [pov]!"
            elif momcorruption < momlove:
                mom "Go ahead [pov], push it inside further. I want you to."
            else:
                mom "Go ahead [pov], you earned this!"
            if inc == True:
                povi "That's right mom it's me making you feel so good this time."
            else:
                povi "That's right [mother] it's me making you feel so good this time."
            mom "Hah... eh...?"
            povi "Oh shit. Now she's about to wake up. I need to get out fast!"
            scene black
            "You scrabble towards the dining room"
            scene main day dining room
            mom "Wait! Sweetie! Come back!!!"
            povi "Shit... "
            povi "Well, I better go back and face the music."
            povi "I wonder if my cell will be a 3 by 5 prison cell or a padded one with a straight jacket at the nut house."
            if nicolereddresswear == True:
                scene livingroom 8am 015cc1
            elif nicolebabydollwear == True:
                scene livingroom 8am 015cc2
            elif nicolesweaterpantswear == True:
                scene livingroom 8am 015cl1
            elif nicolerobewear == True:
                scene livingroom 8am 015cl2
            else:
                scene livingroom 8am 015
            povi "God, I'm an idiot."
            mom "Look [pov]... I know you what you were doing."
            povi "I don't even know what so say."
            povi "I'm just going to wait for it to be over first."
            mom "I'm not mad sweetie."
            pov "Mom I'm sorr..."
            if inc == True:
                povi "Wait what?!?"
                povi "I was just molesting mom in her sleep... and she's not mad?"
            else:
                povi "Wait what?!?"
                povi "I was just molesting [mother] in her sleep... and she's not mad?"
            mom "Its a tough situation we are in now and we have all been a bit tense."
            if nicolereddresswear == True:
                scene edited lroom 8am 015cc1
            elif nicolebabydollwear == True:
                scene edited lroom 8am 015cc2
            elif nicolesweaterpantswear == True:
                scene edited lroom 8am 015cl1
            elif nicolerobewear == True:
                scene edited lroom 8am 015cl2
            else:
                scene edited lroom 8am 015
            povi "She's smiling now? What is she thinking?"
            mom "Do you think... you could... give me a kiss, maybe?"
            pov "Oh...ok."
            "You step forward and embrace her, pulling her into a kiss. She surprises you by leaning into your arms letting you hold her to you."
            if nicolereddresswear == True:
                scene livingroom 8am 025acc1
            elif nicolebabydollwear == True:
                scene livingroom 8am 025acc2
            elif nicolesweaterpantswear == True:
                scene livingroom 8am 025acl1
            elif nicolerobewear == True:
                scene livingroom 8am 025acl2
            else:
                scene livingroom 8am 025a
            povi "I can't believe this is what she meant by kiss... This is fantastic!"
            mom "Hmmm..."
            "You can feel little moans escape her lips as you two kiss passionately."
            "After a while she gently breaks the kiss."
            if nicolereddresswear == True:
                scene livingroom 8am 015cc1
            elif nicolebabydollwear == True:
                scene livingroom 8am 015cc2
            elif nicolesweaterpantswear == True:
                scene livingroom 8am 015cl1
            elif nicolerobewear == True:
                scene livingroom 8am 015cl2
            else:
                scene livingroom 8am 015
            if inc == True:
                pov "Mom, what is this? I know what I was doing was wrong but..."
            else:
                pov "[mother], what is this? I know what I was doing was wrong but..."
            mom "Shhhhh... It's really ok baby, I promise."
            if momlove > momcorruption:
                mom "I just wanted you to know how much I love you."
                pov "I love you too."
            elif momcorruption > momlove:
                mom "I just wanted to tell you how much I need you... here at home."
                pov "I need you too."
            else:
                mom "I just wanted to tell you how proud I am of you."
                pov "Thank you, but I know that, you tell me all the time."
            mom "Sweetie, will you do something for me?"
            povi "This is getting a little weird..."
            pov "Of course I will, anything you want."
            mom "Meet me in your room shortly. I need a couple minutes to get ready."
            pov "Sure thing."
            if nicolereddresswear == True:
                scene edited lroom 8am 015cc1
            elif nicolebabydollwear == True:
                scene edited lroom 8am 015cc2
            elif nicolesweaterpantswear == True:
                scene edited lroom 8am 015cl1
            elif nicolerobewear == True:
                scene edited lroom 8am 015cl2
            else:
                scene edited lroom 8am 015
            mom "Great. I'll see you soon baby."
            pov "Yeah, I'll see you soon."
            scene main day living room
            povi "What does she need to get ready for?"
            povi "Is she going to really let me have in there?"
            povi "She probably just doesn't what my sister to hear as she chews me out."
            povi "Well, it's been a couple minutes. I should head up there."
            scene main mc room day
            if inc == True:
                pov "Mom I'm here."
            else:
                pov "[mother] I'm here."
            mom "Turn around baby."
            scene edited mcroom mombed 01
            mom "Surpised [pov]?"
            povi "Oh... My... God..."
            povi "Am I dead? I have to be dead!"
            povi "I never thought I would go to heaven. But clearly I was wrong."
            if inc == True:
                povi "Heaven is your sexy mother naked in your bed and I am there now!"
            else:
                povi "Heaven is [mother] naked in your bed and I am there now!"
            mom "I'm going to take your stunned silence as a yes."
            "You can only bring yourself nod, afraid that if you look away, she will disappear and you'll wake up."
            povi "God she's so sexy!"
            scene edited mcroom mombed 02
            if momlove > momcorruption:
                mom "If you wanted to play with me all you had to do as ask."
                mom "Is this what you want to see, love?"
            elif momcorruption > momlove:
                mom "So my little boy likes to play with things he shouldn't it seems."
                mom "Such a naughty little boy! Is this what you wanted to see?"
            else:
                mom "I think you deserve a reward for working so hard to keep us all safe at home."
                mom "Would you like to see my pussy?"
            scene edited mcroom mombed 03
            mom "Well now you can look all you want."
            povi "Her skin is so smooth. Her pussy lips are still wet from downstairs."
            mom "Is it everything you hoped it would be?"
            if momlove > momcorruption:
                pov "YES! I really love it!"
                scene edited mcroom mombed 04
                mom "Look how wet I've gotten from you playing with me earlier."
                povi "God that's so hot!"
                mom "I really loved that baby."
                mom "I was dreaming about you making love to me in the basement."
                if inc == True:
                    pov "Mom, I wish I was making love with you right now!"
                else:
                    pov "[mother], I wish I was making love with you right now!"
            elif momcorruption > momlove:
                pov "YES! It's fucking amazing! I love how wet you are!"
                scene edited mcroom mombed 04
                mom "It's all from you playing with me earlier. You dirty bad boy!"
                povi "God that's so hot!"
                mom "I really needed that baby. I've been all pent up inside."
                mom "I was dreaming about you fucking me in the basement."
                if inc == True:
                    pov "Mom, I wish I was fucking you right now!"
                else:
                    pov "[mother], I wish I was fucking you right now!"
            else:
                pov "Wow, this is the greatest reward I have ever recieved!"
                scene edited mcroom mombed 04
                pov "Looks like you got me wet already from our little \"incident\" downstairs."
                povi "God that's so hot!"
                mom "That fels so nice..."
                mom "I was dreaming about you and I having sex in the basement."
                if inc == True:
                    pov "Mom, I wish we were having sex right now!"
                else:
                    pov "[mother], I wish we were having sex right now!"
            mom "Well that would be getting ahead of ourselves."
            if inc == True:
                mom "You're my son."
                mom "We just can't do that..."
                povi "Mother fucker!"
                povi "Well... I wish I was!"
            else:
                mom "It's just too much."
                mom "We just can't do that..."
                povi "At least she'd letting me watch her play with herself."
            povi "I wonder if she'd let me..."
            povi "Screw it, I'm going to play with myself too."
            mom "Hmmm... you want to play too sweetie."
            mom "Ok, but no touching. Just watch and enjoy."
            scene edited mcroom mombed 05
            mom "Come here baby, have a better look!"
            pov "God you're so fucking sexy!"
            pov "I can see the sides squeezing togther!"
            if momlove > momcorruption:
                mom "Yes baby, I'm imagining you pushing your hard cock deep inside me."
            elif momcorruption > momlove:
                mom "Yes baby, I'm imagining you fucking me with your hard cock right now."
            else:
                mom "Yes baby, I'm imagining you inside me. In and out, in and out."
            povi "Fuck! My cock is rock hard right now."
            "You start jacking it while watching her do kegels with her pussy."
            pov "You have great control down there, you must practice a lot!"
            povi "Shit, did I just say that out loud?"
            scene edited mcroom mombed 06
            if momlove > momcorruption:
                if inc == True:
                    mom "Hmmm... does my son think about his mother having sex a lot?!?"
                else:
                    mom "Hmmm... do you think about me having sex a lot?!?"
                mom "Well I think about you too sweetie."
                if inc == True:
                    pov "Yes mom, I do! I just can't get you out of my mind."
                else:
                    pov "Yes [mother], I do! I just can't get you out of my mind."
                mom "I don't want you to. Watch me baby, please! Tell me what will make you happy."
                pov "Yeah, ok!"
                pov "Rub your clit for me."
                pov "I want you to do while watching me too."
                povi "She's doing it!"
                mom "Hnng... Oh yes... hmmm..."
                povi "She's really jilling herself while watcing me!"
                pov "Now look at my dick!"
                mom "Hnnn... Yes sweetie, I'm watching you."
                pov "Look at how swollen it is for you!"
                pov "Don't you wish it was thrusting inside you right now?! Tell me..."
                mom "Oh baby... Hah... yes I do! I wish my hot wet pussy was filled with you deep inside me! Huunn...."
            elif momcorruption > momlove:
                if inc == True:
                    mom "Hmmm... does my son think his mommy is a slut?!?"
                else:
                    mom "Hmmm... do you think I'm a great big slut?!?"
                mom "Well sweetie, for you I can be a slut! I'll be your slut!"
                if inc == True:
                    pov "Fuck yes mom! You my slut now!"
                else:
                    pov "Fuck yes [mother]! You my slut now!"
                pov "You better do everything I tell you slut!"
                mom "Hnng... Yes... fuck yes... I'll do what ever you say!"
                if inc == True:
                    pov "Rub your swollen clit faster mom!"
                else:
                    pov "Rub your swollen clit faster [pov]!"
                pov "I know you want to, you wet dirty whore!"
                mom "Oh god! Hmmm... Hah... Hnnn..."
                povi "She's doing it!"
                povi "She's really jilling herself harder!"
                pov "Look at my cock slut!"
                pov "Look at how swollen it is for you!"
                mom "Hnnn... Yes! I'm watching you... Hgn..."
                pov "Don't you wish it was thrusting inside your filthy cunt right now?!"
                mom "Oh yes, fuck yes, I wish my wet slutty pussy was filled with your big hard cock right now!"
            else:
                mom "Hmmm... of course I do. Otherwise my rewards may not motivate you like I want them to!"
                mom "Well sweetie, do you like it, do you like what I'm doing for you!"
                pov "Fuck, yes I do! I really like it!"
                mom "Do you want me to rub my swollen clit faster now."
                pov "Yes, I want that so bad."
                mom "Hmmm... yes... that's so nice... hnn..."
                povi "She's doing it!"
                povi "She's really jilling herself harder for me!"
                mom "I'm looking at your cock sweetie."
                mom "Look at how swollen it has become. Is that from watching me?"
                if inc == True:
                    pov "Oh yes, its because of you mom!"
                else:
                    pov "Oh yes, its because of you [mother]!"
                mom "Don't you wish you were thrusting inside me right now?!"
                mom "Hnng... huhh... hmmm..."
                pov "Oh god yes! I wish I was deep inside you so badly!"
            mom "hmmm... huh.... hhhm..."
            scene edited mcroom mombed 07
            povi "She's fingering herself now and timing her fingers with my fist pumps."
            if momlove > momcorruption:
                if inc == True:
                    pov "Yes I like that. Keep pretending your son is deep inside you!"
                    mom "Oh baby.... hmmm... yes son... I want it so badly!"
                    pov "Can you feel my hips pressing into your thighs mother as we make love?"
                else:
                    pov "Yes I like that. Keep pretending I'm deep inside you!"
                    mom "Oh baby.... hmmm... yes [pov]... I want it so badly!"
                    pov "Can you feel my hips pressing into your thighs [pov] as we make love?"
                pov "As I press harder inside you, my hands caressing your sides."
                povi "Oh I can see her tensing up."
                povi "I think she's about to cum."
                if inc == True:
                    pov "Are you going to cum, mom?"
                    pov "Do you want to cum while your son rubs his cock in front of you?"
                    mom "God yes!!!"
                    mom "Mommy wants to cum so bad baby."
                    mom "Can I cum please? Gah... fuck.... yes..."
                    mom "Yesss... make love to me!"
                    mom "Do me baby. Ravish your mother!"
                    mom "Can I cum now for you son?!?"
                else :
                    pov "Are you going to cum, [pov]?"
                    pov "Do you want to cum while I rub my cock in front of you?"
                    mom "God yes!!!"
                    mom "I want to cum so bad baby."
                    mom "Can I cum please? Gah... fuck.... yes..."
                    mom "Yesss... make love to me!"
                    mom "Do me baby. Ravish me!!!"
                    mom "Can I cum now for you [pov]?!?"
                mom "Aaaah, hah... hah... fuckkk... gah.... I'm close... sweetie I'm so close..."
                povi "Her fingers are a blur right now and her breathing is so heavy! God this is an amazing sight!"
                povi "I leaned in closer."
                povi "I can smell her wet cunt and hear the sloppy sound of her fingers pistoning in and out."
                if inc == True:
                    pov "Ok Mother."
                    pov "You've been such a good girl for your son."
                else:
                    pov "Ok [mother]."
                    pov "You've been such a good girl for me."
                pov "I want you to cum now."
                pov "I need you to cum for me!"
                mom "Yesbabyyesbabyyesbaby!"
                mom "OHHHHHhhhhhh Fuck!!!"
                mom "gahhhhhh!"
                povi "She's staring right at me as she cums."
                povi "Her eyes are filled with lust and desire."
                povi "She keeps plunging her finger in and out for a while."
                povi "Is she going for another orgasm?!?"
                mom "oh... gah... mmmmmm... here it comes baby!"
            elif momcorruption > momlove:
                if inc == True:
                    pov "Yes slut, do it. Pretend your son is fucking your brains out!"
                    mom "Oh baby.... fuck... yes son... I want it so badly!"
                    pov "Can you feel my hips slapping hard against your thighs mother?!"
                else:
                    pov "Yes slut, do it. Pretend I'm fucking your brains out!"
                    mom "Oh baby.... fuck... yes [pov]... I want it so badly!"
                    pov "Can you feel my hips slapping hard against your thighs [pov]?!"
                pov "As my fucking cock rams inside you."
                povi "Oh I can see her tensing up."
                povi "I think she's about to cum."
                if inc == True:
                    pov "Does slut mommy want to cum?"
                    pov "Does the whore want to cum while her son rubs his cock in front of her?"
                    mom "God yes!!!"
                    mom "Slut mommy wants to cum so hard baby."
                    mom "Can I cum baby? Gah... fuck.... yes..."
                    mom "Yesss... fuck mommy!"
                    mom "Fuck me baby. Fuck your personal whore!"
                    mom "Can I cum for you son?!?"
                else :
                    pov "Does the slut want to cum?"
                    pov "Does she want to cum while she watched me rubs my cock in front of her?"
                    mom "God yes!!!"
                    mom "Your slut wants to cum so hard baby!"
                    mom "Can I cum baby? Gah... fuck.... yes..."
                    mom "Yesss... fuck meeee!"
                    mom "Fuck me baby. Fuck your personal whore!"
                    mom "Can I cum for you [pov]?!?"
                mom "Aaaah, hah... hah... fuckkk... gah.... I'm close... sweetie I'm so close..."
                povi "Her fingers are a blur right now and her breathing is so heavy! God this is an amazing sight!"
                povi "I leaned in closer."
                povi "I can smell her wet cunt and hear the sloppy sound of her fingers pistoning in and out."
                if inc == True:
                    pov "Ok Mother."
                    pov "You've been such a good slut for your son."
                else:
                    pov "Ok [mother]."
                    pov "You've been such a good slut for me."
                pov "I want you to cum now whore."
                pov "I need you to cum for me!"
                mom "Yesbabyyesbabyyesbaby!"
                mom "OHHHHHhhhhhh Fuck!!!"
                mom "gahhhhhh!"
                povi "She's staring right at me as she cums."
                povi "Her eyes are filled with lust and desire."
                povi "She keeps plunging her finger in and out for a while."
                povi "Is she going for another orgasm?!?"
                mom "oh... gah... mmmmmm... here it comes baby!"
            else:
                if inc == True:
                    mom "Do you like this baby, I'm pretending your cock is sliding in and out me again and again!"
                    pov "Oh yeah mom. I am imagining it too!"
                    mom "Haa... aah..."
                    mom "I can feel your hips slapping hard against my thighs!"
                else:
                    pmom "Do you like this baby, I'm pretending your cock is sliding in and out me again and again!"
                    pov "Oh yeah [pov]. I am imagining it too!"
                    mom "Haa... aah..."
                    mom "I can feel your hips slapping hard against my thighs!"
                mom "As your cock rams inside me."
                povi "Oh I can see her tensing up."
                povi "I think she's about to cum."
                if inc == True:
                    mom "Do you want mommy to cum?"
                    mom "Do you want me to cum while my son rubs his cock in front of me?"
                    pov "God yes!!!"
                    mom "Oh baby, mommy wants to cum so hard baby."
                    mom "Can I cum baby? Gah... fuck.... yes..."
                    mom "Yesss... fuck mommy!"
                    mom "Fuck me baby. Fuck your personal reward!"
                    mom "Can I cum for you son?!?"
                else :
                    mom "Do you want me to cum?"
                    mom "Do you want me to cum while you rub your cock in front of me?"
                    pov "God yes!!!"
                    mom "Oh baby, I want to cum so hard baby."
                    mom "Can I cum baby? Gah... fuck.... yes..."
                    mom "Yesss... fuck me!!!"
                    mom "Fuck me baby. Fuck your personal reward!"
                    mom "Can I cum for you [pov]?!?"
                mom "Aaaah, hah... hah... fuckkk... gah.... I'm close... sweetie. I'm so close..."
                povi "Her fingers are a blur right now and her breathing is so heavy! God this is an amazing sight!"
                povi "I leaned in closer."
                povi "I can smell her wet cunt and hear the sloppy sound of her fingers pistoning in and out."
                if inc == True:
                    pov "You've the best reward mother!"
                else:
                    pov "You've the best reward [pov]!"
                mom "I want to cum now..."
                mom "I need to cum for you!"
                mom "Yesbabyyesbabyyesbaby!"
                mom "OHHHHHhhhhhh Fuck!!!"
                mom "gahhhhhh!"
                povi "She's staring right at me as she cums."
                povi "Her eyes are filled with lust and desire."
                povi "She keeps plunging her finger in and out for a while."
                povi "Is she going for another orgasm?!?"
                mom "oh... gah... mmmmmm... here it comes baby!"
            scene edited mcroom mombed 08
            povi "Holy shit, I had not idea she could squirt like that!?!"
            povi "But she sure can."
            povi "The bed sheets and my face are soaked!"
            scene edited mcroom mombed 07a
            if inc == True:
                mom "Oh baby, that was soooo good. Mommy needed that."
                pov "Mom, I can't believe we did that! You are so fucking hot. Seriously!"
            else:
                mom "Oh baby, that was soooo good. I really needed that."
                pov "[pov], I can't believe we did that! You are so fucking hot. Seriously!"
            scene edited mcroom mombed 03a
            mom "Your pretty hot yourself baby."
            mom "But listen, uou can't tell anyone about this right?"
            if momlove > momcorruption:
                mom "It because I love you so much for being such a great man and the others just woudn't understand."
            elif momcorruption > momlove:
                mom "We both needed this so badly. No one else needs to know about this."
            else:
                mom "It was a reward for being such a great young man and helping us with all this."
            pov "Of course! I know that."
            pov "I'm just glad you wanted to do that with me."
            povi "She's still looking at my stiff cock. In the excitement I never got to finish."
            mom "Oh, you didn't get to cum yet?"
            mom "Why didn't you tell me?"
            if momlove > momcorruption:
                if inc == True:
                    mom "Do you want your mommy to help you with that?"
                else:
                    mom "Do you want me to help you with that?"
            elif momcorruption > momlove:
                if inc == True:
                    mom "Do you want your slutty mom to help you with that?"
                else:
                    mom "Do you want your slut to help you with that?"
            else:
                if inc == True:
                    mom "Do you want an extra reward from your mom to help you with that?"
                else:
                    mom "Do you want an extra reward from me to help you with that?"
            scene edited mcroom mombed 02a
            if inc == True:
                pov "That's ok mom. You look exausted."
            else:
                pov "That's ok [pov]. You look exausted."
            pov "It was so hot watching you get off like that."
            pov "I think I want to wait until later tonight when we go in the basement."
            povi "Wait?!?!"
            povi "What am I saying?"
            povi "Maybe I have gone crazy?!"
            mom "Well ok sweetie."
            mom "I think we can work somethiing out to help you with that tonight then."
            mom "Oh no, it's getting late."
            mom "I need to get dinner started."
            mom "Could you be a lamb and clean this up?"
            mom "Can't have anyone finding out about our fun, right?"
            pov "Uh... yeah. I can do that."
            pov "I'll see you downstairs."
            mom "Thanks honey."
            mom "Love you baby."
            if inc == True:
                pov "Love you too mom."
            else:
                pov "Love you too [pov]."
            scene main mc room day
            povi "Did that just happen?"
            povi "Holy shit that was fucking hot!!!"
            povi "I think the floor is still wet where she squirted all over."
            povi "I fucking love that woman!"
            povi "Shit... where is the freaking laundry room anyway?"
            $ momrelationship += 1
            $ momlove += 1
            $ momcorruption += 1
            $ dtime += 1
            jump mcroom
        else:
            mom "Ohh... hah... yes..."
            mom "Ram your hard dick in your slut, Davide!"
            povi "Nooo! It's me [pov]! I'm giving you this good feeling."
            mom "Hah... eh...?"
            povi "Oh shit. Now she's about to wake up. I need to stop it fast."
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
    povi "No, I'll let her sleep."
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
        davide "A chance to become a full gang member with some benefits."
        pov "Benefits?"
        davide "You do this for me and I'll know you're trustworthy."
        davide "And then you can help with our preparations in the basement."
        povi "The basement, huh? Then I'd finally know what happens there."
        pov "And what would I have to do?"
        davide "I'll tell you then, but first I want your decision."
        dad "Do it! It's a good gig."
    else:
        davide "A second chance to become a full gang member with some benefits."
        pov "Some benefits?"
        davide "You do this for me and I'll know you're trustworthy."
        davide "And then you can help with our preparations in the basement."
        povi "The basement, huh? Then I'd finally know what happens there."
        pov "And what would I have to do?"
        davide "I'll tell you then, but first I want your decision."
        dad "Do it! It's a good gig."
    povi "A chance to get in the basement. But I'm sure I'll have to do something criminal as well."
    povi "So should I become a criminal or not? If I don't I'll have to find another way into the basement."
    call screen lroom21decide

screen lroom21decide:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('lroom21decide'), Jump('lroom21yes')) hovered tt.Action ("Take the job [gd1]/both") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('lroom21decide'), Jump('lroom21no')) hovered tt.Action ("Don't take the job [bd1]/both") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
    pov "You haven't told me what to do so far."
    scene livingroom 9pm 007j
    davide "I need you to deliver a package."
    povi "A typical delivery job. Should be easy enough."
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
    pov "I'm not stupid."
    povi "Now I just want to open the damn thing! Don't you guys understand the concept of reverse psychology?"
    $ package += 1
    "You receive the package."
    scene livingroom 9pm 010j
    davide "Do this well and we'll see about that promotion."
    pov "No problem. I got this."
    $ dadgood += 1
    $ davidegood += 1
    $ dtime += 1
    $ jobgang = True # ----- Added in 0.6.5 -----
    jump lroom

label basementgo_landing:
    hide screen locations
    jump basementgo

label basementgo:
    scene livingroom 9pm 006j
    $ gangmember = True
    #$ gangmemberaccept += 1
    davide "You did a good job delivering those packages!"
    davide "So now I now you can be trusted it's time to become a permanent member of our gang."
    dad "Yes! I knew it!"
    davide "Then I'll explain some things to you, but first..."
    scene livingroom 9pm 006b
    davide "I need you to take care of our bags, Bruce."
    dad "But I thought..."
    davide "No! Bring them to our other place. I'll need the basement clean today."
    dad "But..."
    davide "You remember what we talked about?"
    scene livingroom 9pm 007b
    dad "Yes, sorry. I got this. I'll do it as fast as possible!"
    davide "That's my man! Show me that we don't need Steve."
    dad "Aye! See you later [pov]!"
    scene livingroom 9pm 008b
    davide "Good. I love it when everything turns out as planned."
    pov "What do you mean a permanent member? What are these privileges?"
    davide "Wait a moment."
    "Bruce leaves with the first bags."
    scene livingroom 9pm 009b
    davide "I need him to leave because he shouldn't know what I have to explain."
    davide "Steve was my right hand in the gang and Bruce thought he would gain that position."
    davide "But I think you're a better fit!"
    pov "Oh... And what's special about that?"
    if inc == True:
        davide "Your father and mother have to follow our orders."
    else:
        davide "Bruce and [mother] have to follow our orders."
    scene livingroom 9pm 010b
    davide "I think we can be more productive this way."
    pov "But what are we doing?"
    davide "Follow me and you'll see."
    povi "They have to do what I say? This could be a lot of fun!"
    povi "They made me hold a bar of soap in my mouth for swearing as a child!"
    povi "Now I can punish them! This is better than pretending to be blind from soap poisoning!"
    scene livingroom 9pm 011b
    davide "You now get access to the basement. Our base of operations."
    "Davide gives you a key."
    if basementkey == False:
        $ basementkey = True
    $ lroom21pdone = True
    povi "Finally!"
    davide "Go on! Enter the door to success, haha."
    scene black
    "You go down."
    scene basement 001
    povi "Wow! This place looks like a mini sex dungeon. I \"wonder\" what happens here?"
    davide "Come. I'll show you everything."
    scene basement 002
    davide "This is our bar. Where we make our drinks so the evenings won't be so boring, haha."
    pov "So many different drinks. Isn't that a bit too much for 4 people?"
    davide "We often have guests here, so we need plenty of drinks."
    scene basement 003
    pov "And this stuff?"
    davide "Haha, for personal use. When some of the girls come by or guests even."
    pov "When are guests coming by?"
    scene basement 004
    davide "Soon, to get some of our drugs we prepare here."
    davide "The guests are men and women and after some drinks and drugs we usually have fun here."
    pov "Fun?"
    davide "Haha, you know exactly what that means!"
    scene basement 005
    davide "Here's our place to chill or make deals."
    pov "Not bad down here in the basement."
    scene basement 006
    pov "And what's over there?"
    davide "The right one is the toilet, so we don't need to leave the basement for that."
    davide "The left one is the changing room, mostly for the girls."
    pov "Why a changing room? Isn't naked enough?"
    davide "Haha, not bad! But you should see what hot costumes the girls girls like to wear!"
    if inc == True:
        "Does that include my mom? Wearing costumes and participate at the party's?"
    else:
        "Does that include [mother]? Wearing costumes and participate at the party's?"
    if NTR == True:
        davide "Yeah, sure. If you want! I'd bet you'd love to see her down here too!"
    else:
        davide "No. Wearing costumes sometimes, but having real fun isn't her thing."
        davide "Maybe she loves Bruce too much..."
    pov "Hmm..."
    scene basement 002
    davide "You can't wait to see the action, can you?"
    pov "I'm a little surprised, because I wasn't sure what to expect."
    davide "Haha..."
    davide "Oh look who's here. Guests!"
    scene basement 9pm 010
    if vivianfirstmeet == True:
        pov "This is the bartender from the \"sleazy weasel\", [vivian]."
        pov "But who's the other women?"
    else:
        pov "Who are they?"
        scene basement 9pm 011
        davide "So you can't wait any longer? Good to hear, haha."
        if vivianfirstmeet == True:
            vivian "She was being stubborn, so I brought her here. She's yours to deal with now."
        else:
            "Woman" "She was being stubborn, so I brought her here. She's yours to deal with now."
    scene basement 9pm 012
    davide "Then follow me, I'll take care of you."
    "woman" "Yes please."
    if vivianfirstmeet == True:
        vivian "And you're now part of the gang [pov]?"
        pov "Yes."
        vivian "Good. So now you can play with us too."
    else:
        "Woman" "Hi, I'm..."
        $ vivianname = renpy.input(_("Her name is...")) or _("Vivian")
        $ vivianname = vivianname.strip()
        if vivianname == "":
            $ vivianname = "Vivian"
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
    povi "Wow..."
    vivian "So don't make me wait, haha!"
    scene basement 9pm 014
    vivian "I'm heading back! See you guys soon!"
    davide "See you [vivian]."
    povi "So she's part of the gang-activities too, interesting."
    davide "Come here [pov]!"
    scene basement 9pm 015
    davide "This is ..."
    if mirandafirstmeet == False:
        $ mirandaname = renpy.input(_("Her name is...")) or _("Miranda")
        $ mirandaname = mirandaname.strip()
        if mirandaname == "":
            $ mirandaname = "Miranda"
        $ mirandafirstmeet = True
    davide "[miranda], this is [pov]. The newest member of our gang."
    miranda "Nice to meet you."
    pov "Nice to meet you too."
    davide "[pov] is here to learn about what we do here."
    miranda "So he'll join us?"
    davide "Haha, maybe."
    scene basement 9pm 016
    davide "Look, this one is for you. For the hot \"pussy cat\" that you are."
    miranda "Please give it to me! Don't make me wait like Davide does every time!"
    povi "These drugs look like candy."
    davide "But that's our ritual. You know what you've to do to get it."
    scene basement 9pm 017
    miranda "Satisfied now?"
    davide "Good, open your mouth."
    miranda "Hmm..."
    povi "So he loves to humiliate her?"
    scene basement 9pm 018
    miranda "Hnn...!"
    davide "See? She loves it!"
    pov "And what's the drug she's doing now?"
    davide "Wait a second!"
    scene basement 9pm 019
    davide "How about you go prepare yourself and I'll be ready in a few moments?"
    miranda "Ok. But please don't make me wait."
    scene basement 9pm 020
    davide "This is really good stuff that we got here."
    pov "And let me guess, it gives you a great high?"
    davide "Haha yes. And like other drugs you can get addicted, but..."
    davide "This shit is not normal, it has the strongest effect I have ever seen."
    davide "And it's specialty is that it works for everything that gives you pleasure, individually."
    pov "Everything?"
    davide "Haha yes. If you like to eat you'll get the maximum pleasure out of it and could keep on eating until you die."
    davide "The effects last about a day and has no bad side effects, so win-win. Except that you want more to keep those good feelings going."
    pov "Wow. Did you try it?"
    davide "Sadly no. It only works on females so far."
    pov "If it has no bad effects why can't you sell it officially. Doesn't seem like it would be illegal."
    davide "We tried. But there was an accident. Someone used the drug on a girl without her knowing it."
    davide "She thought the pleasure she got from drinking was just from that, drinking. While trying to find that high again, she drank herself to death."
    pov "Oh..."
    davide "That's the reason why we have to sell this secretly."
    miranda "Are you done? I don't want to wait anymore..."
    scene basement 9pm 021
    davide "Come, let me show you how men can enjoy this drug too."
    povi "Holy..."
    miranda "I want to enjoy my high too now!"
    davide "Haha, relax. You'll get some real pleasure soon enough."
    scene basement 9pm 022
    miranda "Can he join us? He looks hot, I want to taste him too!"
    davide "Haha, he can join if he wants to. But now you better prepare yourself so we can start."
    pov "So she enjoys sex? Well, I mean... yeah she enjoys sex, everyone does. But this is her favorite high?"
    miranda "Oh yes! You poor men have no idea what you're missing."
    scene basement 9pm 023
    "Davide helped her to get ready."
    davide "See? This is her favorite pleasure. Of course she doesn't have to pay for the drugs if she's doing this for us."
    davide "But she'll pay in other ways, haha."
    miranda "Don't stand there looking at me, boy! Get your dick out too!"
    davide "Oh, I think [miranda] is in love, haha."
    scene basement 9pm 024
    davide "You can have her mouth while I use the other side!"
    miranda "Ohhh..."
    miranda "Please let me taste you, hah..."
    call screen base9mirbj

screen base9mirbj():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('base9mirbj'), Jump('base9mirbjy')) hovered tt.Action ("Let her suck you") focus_mask True
        #----- added -----
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('base9mirbj'), Jump('base9mirbjn')) hovered tt.Action ("Politely decline") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base9mirbjn:
    scene basement 9pm 024
    pov "No sorry [miranda]. I think I'm sitting this one out."
    davide "You're serious?"
    miranda "What a shame. Your loss boy!"
    scene black
    "Davide fucks [miranda] for a while"
    scene basement 9pm 037a
    jump base9nic

label base9mirbjy:
    scene basement 9pm 025b
    "You get your dick out and go to her."
    pov "Now I'm curious about what you can do."
    miranda "Oh you won't regret it!"
    scene basement 9pm 026b
    davide "Oh and don't forget. You can choose how you use your mouth, after she is restrained, haha."
    pov "I don't rape girls!"
    davide "It wouldn't be like that, she'll love it both ways because of the drug, ain't I right?"
    "Davide fucks her rougher."
    miranda "Hah... hah... you animal!"
    pov "Hmm..."
    miranda "Please let me... hah... pleasure you..."
    scene basement 9pm 027b
    "She catches your dick as you came to near."
    pov "Oh... someone can't wait."
    miranda "<suck> <suck>"
    davide "A nice surprise, isn't it?"
    pov "Oh yes!"
    dad "WHAT THE FUCK!?"
    scene basement 9pm 029
    davide "Oh hey Bruce, you found us!"
    if inc == True:
        pov "Hey dad."
    else:
        pov "Hey Bruce."
    dad "You can't bring him down here, I told you! [mother] would not be happy about that."
    davide "Haha, I don't care!"
    dad "But I do!"
    scene basement 9pm 030
    dad "I'm serious. She'll go totally crazy! You know her!"
    davide "Yeah I know. But we need a third person for the gang and I think he fits in good."
    davide "And I wouldn't want to get him angry."
    dad "Oh, sure! But I still think we could find another solution."
    pov "Him?"
    davide "The boss, I'll explain it to you later."
    povi "So there's another one. The boss over all of them? But who is it?"
    scene basement 9pm 031
    dad "Well, I'm out of here. He's your problem now!"
    davide "Hahaha, don't cry. I not afraid of [mother] anyway."
    pov "Can she really be that bad?"
    davide "Oh you have no idea. But let's enjoy [miranda] for now."
    scene basement 9pm 028b
    "You two have your fun with [miranda]."
    davide "But you still have to choose what you'll do now."
    miranda "Hmm..."
    davide "Let yourself get pleasured by this naughty woman or give her throat a good fuck."
    davide "And as I explained before, she'll enjoy it either way, even if she favors one over the other."
    call screen base9mirbj2

screen base9mirbj2():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('base9mirbj2'), Jump('base9mirbjc')) hovered tt.Action ("Fuck her throat [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('base9mirbj2'), Jump('base9mirbjl')) hovered tt.Action ("Let her pleasure you [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base9mirbjc:
    $ mirandacorruption += 1
    scene basement 9pm 032br
    miranda "Bllggrhh...!"
    pov "I choose to fuck her hot mouth! And shut her up, haha."
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
    miranda "So you had your fun!"
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
    pov "Damn, I'm already at my limit. You're doing too good [miranda]."
    miranda "I'll let you choose where you want your sperm on me!"
    pov "Perfect!"
    call screen base9mirbj3

screen base9mirbj3():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base9mirbj3'), Jump('base9mirbjlm')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base9mirbj3'), Jump('base9mirbjlf')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base9mirbjlm:
    pov "I want you to taste it!"
    scene basement 9pm 034bgi
    pov "Hnng..."
    "You cum in her mouth."
    miranda "Hmm..."
    pov "Damn, she's like sucking it out of me."
    miranda "<gulp> <gulp>"
    scene basement 9pm 035bgi
    miranda "Ohh... that tasted so good. I love young men's sperm!"
    pov "Wow, just like a pro!"
    miranda "So you liked it baby?"
    pov "Yes! Your mouth is wonderful!"
    davide "Then you should try her other holes too!"
    scene basement 9pm 036b
    miranda "Ohh... hah..."
    davide "Good, that shut you up, now enjoy my hard ride."
    miranda "Hah... you horndog!"
    scene basement 9pm 037a
    jump base9nic

label base9mirbjlf:
    pov "I want to spray it over your beautiful face!"
    $ mirandacumface = True
    scene basement 9pm 034bgo
    pov "Hnng..."
    "You cum on her face."
    miranda "Hmm..."
    pov "Yes, let me paint it on you."
    scene basement 9pm 035bgo
    miranda "So much sperm came out all over my face."
    pov "Wow what a fantastic view."
    miranda "It's like anti-aging cream for my skin, coming from a young boy."
    pov "Wow, just like a pro!"
    miranda "So you liked it baby?"
    pov "Yes! Your mouth is wonderful!"
    davide "Then you should try her other holes too!"
    scene basement 9pm 036b
    miranda "Ohh... hah..."
    davide "Good, that shut you up, now enjoy my hard ride."
    miranda "Hah... you horndog!"
    scene basement 9pm 037b
    jump base9nic

#----- Edited -----
label base9nic:
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
    mom "I told you to not let him down here."
    if inc == True:
        pov "But I wanted this, mom."
    else:
        pov "But I wanted this."
    mom "You shut up!"
    davide "Hahaha..."
    mom "And you stop laughing. This isn't funny anymore."
    davide "Oh yes it its. It wasn't my just my decision to get him down here."
    scene basement 9pm 041n
    mom "You can't be serious!"
    davide "Oh yes I am. The boss choose him and gave him Steve's rank in the gang."
    mom "So he's your right hand now, over a kingdom of nothing?"
    davide "Yes and his superior, I intend to show him all the goods, haha."
    if inc == True:
        pov "So I have a higher rank then my mom?"
    else:
        pov "So I have a higher rank then [mom]?"
    davide "Yes you do."
    scene basement 9pm 040n
    davide "And it's about time that you get punished for being so rude!"
    mom "But..."
    davide "No! Talking to a higher gang member like that! You know the rules!"
    mom "..."
    povi "Punishment, hm..."
    if NTR == True and momrelationship <= 5:
        jump base9ntr
    else:
        scene basement 9pm 042nn
        davide "Go on! You can now choose how you'll punish her."
    pov "I should punish her?"
    davide "Yes, she insulted you and I'm not going to stop fucking [miranda] right now to do it myself!"
    pov "Haha, I understand."
    if inc == True:
        "You go over to your mom."
    else:
        "You go over to [mom]."
    scene basement 9pm 043n
    pov "So..."
    mom "Hnn..."
    davide "Show her where her place is!"
    pov "I can choose whatever I want?"
    davide "Yes of course, it's your punishment."
    mom "[pov], please..."
    jump base9nicpunish

label base9nicpunish:
    scene basement 9pm 043n
    call screen base9nicpunish1

screen base9nicpunish1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('base9nicpunish1'), Jump('base9nicpunc')) hovered tt.Action ("Punish her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('base9nicpunish1'), Jump('base9nicpunl')) hovered tt.Action ("Punish her [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base9nicpunc:
    pov "Come with me [mother], it's punishment time!"
    $ momcorruption += 1
    scene basement 9pm 043nnc
    mom "Huh?"
    "You grab her arm and pull her with you."
    mom "What do you want to do with me?"
    pov "You'll see it soon!"
    "She's so confused she doesn't realizes until it's too late what you're going to do with her."
    scene basement 9pm 044nnc
    mom "No! You can't be serious!"
    davide "Haha, nice one! I'm curious about what you're up to."
    if inc == True:
        mom "I don't know what you're think you're doing but don't forget that I'm your mother."
    else:
        mom "I don't know what you're think you're doing but don't forget that I'm your mother's best friend."
    pov "Yes and that's the reason why talk to me like that must be punished."
    scene basement 9pm 045nnc
    mom "Oh no! Don't look at me!"
    if inc == True:
        davide "Wow bro. You ain't gonna fuck your mom?"
    else:
        davide "Wow bro. You ain't gonna fuck her?"
    miranda "Oh I think that naughty bitch would love it, haha."
    mom "Shut the fuck up [miranda]!"
    pov "No, I'll do something else first. She earned herself a good spanking."
    scene basement 9pm 046nnc
    mom "Stop! You can't be serious!"
    miranda "Hahaha... hah... hah..."
    davide "What a nice idea."
    mom "You shut up too, Davide! It's all your fault!"
    scene basement 9pm 047nnc
    povi "Hmm... what should I choose for her?"
    call screen base9nicpunch

screen base9nicpunch():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('base9nicpunch'), Jump('base9nicpunp')) hovered tt.Action ("Choose the ping-pong paddle [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base9nicpunch'), Jump('base9nicpunch1')) hovered tt.Action ("Use your hand") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base9nicpunp:
    $ mompaddle = True
    $ momcorruption += 1
    povi "It has to be a good punishment!"
    jump base9nicpunch1

label base9nicpunch1:
    povi "A good spanking with my hand is enough!"
    if mompaddle == True:
        scene basement 9pm 048nncp
    else:
        scene basement 9pm 048nnch
    if inc == True:
        mom "Please listen to me [pov]. You're my son, you shouldn't do this!"
        pov "You did this to yourself, mom. So be a good mom and endure your punishment."
    else:
        mom "Please listen to me [pov]. You're like a son, you shouldn't do this!"
        pov "You did this to yourself, [mother]. So be a good girl and endure your punishment."
    mom "Wait...!"
    with vpunch
    "Slap"
    mom "Ahhh..."
    davide "Hah! You're really doing it."
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
    pov "That's a fine red ass from a good punishment..."
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
    dad "But I need her now! There's an urgent call for her!"
    davide "That seems serious. You should let her go [pov]."
    pov "Ok."
    "You free her."
    scene basement 9pm 051nnc
    mom "..."
    pov "..."
    dad "Are you coming [mother]?"
    scene basement 9pm 052nnc
    pov "Stop!"
    mom "Hnng..."
    pov "You didn't apologize!"
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
    davide "Wow, you're taming her nice and good."
    pov "She needed to feel humiliated too."
    miranda "You have no idea how bad I'll be next time <giggle>"
    davide "Shut up [miranda]!"
    miranda "Aaah... hah..."
    scene black
    "Having enjoyed your new power, you leave the basement."
    $ dtime += 2
    $ b9rncor = True
    $ mompaddle = False
    jump mcroom

label base9ntr:
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene basement 9pm 040n
    davide "I'll take care of it!"
    if inc == True:
        povi "He'll punish mom?"
    else:
        povi "He'll punish [mother]?"
    povi "Do I want him to punish her?"
    call screen base9ntrpun

screen base9ntrpun():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('base9ntrpun'), Jump('base9ntrpuncont')) hovered tt.Action ("Darker Paths") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('base9ntrpun'), Jump('base9ntrpunm')) hovered tt.Action ("Interfere") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base9ntrpunm:
    povi "No, I don't want him to lay a hand on her."
    pov "Wait!"
    scene basement 9pm 042nn
    davide "Huh?"
    pov "I want to punish her myself!"
    davide "Oh...?"
    pov "She insulted me, also should I be the one do it."
    davide "Ok. Then do it yourself."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump base9nicpunish

label base9ntrpuncont:
    call screen checkdarkerpaths_nicole
    jump base9ntrpund

label base9ntrpund:
    scene basement 9pm 043n
    mom "Please... Davide..."
    davide "Now that's enought of that! I know you'll like it too."
    mom "But..."
    davide "..."
    if nicole_ntr == True or nicole_voyeur == True:
        mom "Ok."
    else:
        mom "Please don't..."
    scene basement 9pm 044n
    davide "What are you waiting for? Get naked and bend over."
    mom "Please, he must not see this!"
    davide "Oh I'm sure he won't care. He's part of the gang now, so he'll be down here with us often."
    if inc == True:
        mom "But he's my son."
    else:
        mom "But he's the son of my best friend."
    davide "Bla.. bla... bla..."
    if nicole_ntr == True or nicole_voyeur == True:
        mom "I... I understand..."
    else:
        mom "I... You can't do this..."
    scene basement 9pm 045n
    mom "Please... don't look."
    davide "Oh I'm sure he wants to look. You're damn hot."
    if nicole_voyeur == True:
        if inc == True:
            pov "He's right. You're damn hot, mom."
        else:
            pov "He's right. You're damn hot, [mother]."
        mom "Hnng..."
    elif nicole_ntr == True:
        pov "You don't know what I want Davide."
        povi "If I could stop you, I would. I'm just too weak."
        mom "Hnng..."
    elif nicole_revenge == True:
        mom "Please, I'm sorry..."
        if inc == True:
            pov "Davide, that is enough, my mom said she was sorry already!"
        else:
            pov "Davide, that is enough, [mother] said she was sorry already!"
    else:
        mom "Please, I'm sorry..."
        if inc == True:
            pov "Yeah, David. Did you hear my mom said she was sorry already. Haha!"
        else:
            pov "Yeah, David. Did you hear [mother] said she was sorry already. Haha!"
    davide "Bitch, I said get into position!"
    if nicole_revenge == True:
        povi "I need to find a way to stop Davide for good!"
    scene basement 9pm 046n
    "[mother] gets herself into position."
    if nicole_voyeur == True or nicole_ntr == True:
        mom "I can't believe you want to do this."
        davide "It's your punishment and you love it, you're flooding."
    else:
        mom "I can't believe your making me do this."
        davide "It's your punishment and you're gonna love it, you whore."
    mom "Nooo!"
    if inc == True:
        davide "Letting your son see how you get fucked and loving it."
    else:
        davide "Letting him see how you get fucked and loving it."
    mom "That's not true. He knows why I have to do this."
    davide "Because you're a slut!"
    scene basement 9pm 047n
    mom "Aaah..."
    if nicole_voyeur == True or nicole_ntr == True:
        davide "Good. You're sucking me already."
        mom "Hmm..."
    else:
        davide "That's it, take it you slut!"
        mom "Stop! It hurts!"
    davide "What's with you [pov]? [miranda] needs to be fucked too!"
    miranda "Oh yes, please do me boy. My pussy wants to taste your dick!"
    mom "No [pov]! You can't do this."
    scene basement 9pm 048n
    davide "Go on, have your fun [pov]! There's no need to only watch."
    if inc == True:
        davide "Your mom has to accept this because there's nothing she can do, except moan, haha."
    else:
        davide "[mother] has to accept this because there's nothing she can do, except moan, haha."
    if nicole_voyeur == True or nicole_ntr == True:
        mom "No... hah... hah... she's a whore..."
    else:
        mom "No... ow... ha... You're better than that..."
    miranda "Haha, shut up [mother]."
    if inc == True:
        miranda "Telling your son that's bad while getting fucked and enjoying it. Bad mom!"
    else:
        miranda "Telling him that's bad while getting fucked and enjoying it. Bad [mother]!"
    if nicole_voyeur == True:
        povi "Hm... what a good question. [miranda] is free now and ready to get fucked too."
    elif nicole_ntr == True:
        povi "I don't think I should do this. [mother] doesn't want me too."
    elif nicole_revenge == True:
        povi "Hm... what will Davide do if I don't fuck her. He could get angry and hurt [mother] more."
    else:
        "Hm... That is a good question. [miranda] is free now and ready to get fucked too."
    scene basement 9pm 049n
    miranda "Please [pov]. I want your dick. Please fuck me too!"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hah... hah..."
    else:
        mom "Please.... let us go!"
    davide "Come on. Let give [miranda] some fun too!"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Don't... hah.. stick it... in her... hah..."
        miranda "Why should you be the only one who has fun?"
        mom "I... hah... ahh..."
    else:
        mom "Don't... hah.. [pov]... I'm... sorry..."
        miranda "Why should you be the only one who has fun?"
        mom "I... am... not..."
    davide "Haha, she's still trying to deny it."
    if inc == True:
        povi "Should I fuck [miranda]? Or should I do what my mom wants and just stand by and watch while she gets fucked?"
    else:
        povi "Should I fuck [miranda]? Or should I do what [mother] wants and just stand by and watch while she gets fucked?"
    call screen base9ntrmir

screen base9ntrmir():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base9ntrmir'), Jump('base9ntrmiry')) hovered tt.Action ("Fuck [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base9ntrmir'), Jump('base9ntrmirn')) hovered tt.Action ("Just watch") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base9ntrmirn:
    if inc == True:
        povi "I don't want to fuck [miranda]. I don't want to make mom any more angry."
        davide "Haha, you're really going to turn her down? So you're a good boy, doing what your mom wants."
    else:
        povi "I don't want to fuck [miranda]. I don't want to make [mother] any more angry."
        davide "Haha, you're really going to turn her down? So you're a good boy, doing what [mother] wants."
    davide "Or do you just enjoy seeing her getting fucked by other men, haha?"
    mom "Don't talk... hah... like that... hah... with him!"
    jump base9ntrnic2

label base9ntrnic2: #S
    if nicole_voyeur == True or nicole_sadist == True:
        pov "I like it. I want to see it how she enjoys being fucked by someone other than her husband."
        davide "Oh so you're a pervert? Good for me, haha."
        if inc == True:
            mom "You can't be serious? You like it seeing your mother getting fucked by other men?"
        else:
            mom "You can't be serious? You like it seeing me getting fucked by other men?"
    elif nicole_ntr == True:
        if inc == True:
            povi "I don't like it. But I can't win a fight against him. And it doesn't look like mom will stop it."
        else:
            povi "I don't like it. But I can't win a fight against him. And it doesn't look like [mother] will stop it."
    else:
        if inc == True:
            povi "I don't like it. But I can't win a fight against him. And mom can't fight against it either. Go big or go home..."
        else:
            povi "I don't like it. But I can't win a fight against him. And [mother] can't fight against it either. Go big or go home..."
    davide "So you decided, haha. See how much she likes it, getting fucked by my big black dick."
    scene basement 9pm 051n
    mom "No... please don't watch us [pov]! Hah..."
    davide "He decided already, so we're give him a good show!"
    if nicole_voyeur == True:
        pov "Yes, do it. I want to see her cum!"
    elif nicole_ntr == True:
        povi "That damn asshole! He's just too strong!"
    elif nicole_revenge == True:
        povi "That damn asshole! We're going to make him pay one day!"
    else:
        pov "Yeah, you're giving a great show [mother]!"
    mom "No... hah... hah..."
    if inc == True:
        davide "How about you tell your son how much you love it?"
    else:
        davide "How about you tell him how much you love it?"
    scene basement 9pm 054n
    mom "I... hah... have to... do this..."
    davide "Because you're a slut?"
    mom "Please... hah... [pov] you know it..."
    if nicole_voyeur == True or nicole_sadist == True:
        pov "Yeah I know. You need to please everyone and cum hard on their dicks!"
        mom "No... It's not... hah... like that..."
    else:
        if nicole_ntr == True:
            pov "Yeah I know..."
            mom "Please... believe me. It's not... hah... like that..."
        else:
            pov "Yeah I know. I'm so sorry!"
            povi "She \"must\" do it for her cover."
    davide "Time to cum, slut!"
    mom "Wait... hah.. no..."
    scene basement 9pm 052n
    mom "Hnng... Hnn..."
    davide "Look! She loves it so much that she's about to cum!"
    if nicole_voyeur == True:
        mom "Hah... yes..."
        if inc == True:
            pov "Yes! Show me your cum-face, mom!"
        else:
            pov "Yes! Show me your cum-face, [mother]!"
    elif nicole_ntr == True:
        mom "Hah... yes..."
        if inc == True:
            povi "Yes?! I can't believe you like this, mom!"
        else:
            povi "Yes?! I can't believe you like this, [mother]!"
    elif nicole_revenge == True:
        mom "Fuck you... Davide!"
        povi "No! I can't believe it! She's cumming from that assholes dick."
    else:
        mom "Fuck you... Davide!"
        if inc == True:
            pov "Haha, yes! Show me your o-face, mom!"
        else:
            pov "Haha, yes! Show me your o-face, [mother]!"
    mom "Aaaahhhh... Hnnnng..."
    scene basement 9pm 053n
    davide "I came hard too! But I need more. So time for another round?"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hah... yes... more please... hah..."
    else:
        mom "Noo... no... please... no more..."
    davide "I think you've had enough fun, [pov]! I think I'll have more fun without you, haha."
    if inc == True:
        davide "Time to stop watching your mom getting fucked!"
    else:
        davide "Time to stop watching [mother] getting fucked!"
    if nicole_revenge == True:
        povi "No... I have to do something. I need to help her!"
        pov "Davide, look. You did what you wanted. You punished her. Let her go. I'll owe you one. Anything you want!"
        davide "Fuck... She's used anyway now. I'll use [miranda] for a while."
        davide "You can take her... but don't forget. You owe me one now!"
        scene black
        "You help her get out of the stocks and get dressed, you leave the basement together."
    elif nicole_ntr == True:
        povi "I couldn't anything! I'm useless..."
        scene black
        "You leave the basement hearing them start another round."
    else:
        pov "Yeah have fun fucking that slut!"
        scene black
        "You leave the basement hearing them start another round."
    $ dtime += 2
    $ b9rnntr = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump mcroom

label base9ntrmiry:
    if nicole_voyeur == True:
        povi "It's my chance. I'll fuck [miranda] too."
    elif nicole_ntr == True:
        povi "I don't know what else I can do..."
    else:
        povi "He might make me leave if I don't do this, and I want to make sure he doesn't hurt anyone."
    scene basement 9pm 050nf
    miranda "Yes! Please take care of me [pov]!"
    if nicole_voyeur == True:
        povi "What a nice view."
    else:
        povi "Ok, this is a messed up situation, but what a nice view."
    davide "What's wrong [pov]. Can't decide which hole you should use?"
    mom "Stop! Hah... don't give him those kind of ideas..."
    miranda "I don't care, just fuck me. I want to feel your young dick!"
    povi "So which one will it be?"
    call screen base9ntrmirch

screen base9ntrmirch():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base9ntrmirch'), Jump('base9ntrmira')) hovered tt.Action ("Fuck her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base9ntrmirch'), Jump('base9ntrmirp')) hovered tt.Action ("Fuck her pussy") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base9ntrmira:
    povi "I need to fuck that tight asshole."
    $ mirandass = True
    jump base9ntrmirfuck

label base9ntrmirp:
    povi "I need to fuck her wet pussy."
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
    if nicole_ntr == True:
        povi "I'm sorry mom, I just couldn't help myself!"
    if nicole_revenge == True:
        povi "I'm sorry mom, I need to play along now!"
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
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hnng...!"
    else:
        mom "Oouch!!!"
    davide "Time for some harder fucking!"
    miranda "Go on [pov]! We can't get left behind them. Fuck me harder!"
    if inc == True:
        davide "Damn, your mom is getting tight. She likes to get a hard pounding when her son is watching."
    else:
        davide "Damn, [mother]'s is getting tight. She like to get a hard pounding when you're watching."
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hnng... hnng..."
    else:
        mom "Stop... just stop!"
    davide "No more fighting. Just accept it!"
    if inc == True:
        miranda "See? Your mom is a whore too!"
    else:
        miranda "See? [mother] is a whore too!"
    if nicole_revenge == True:
        povi "Shut up Miranda, I'm only doing this to be here to protect her if Davide gets violent."
    pov "You shouldn't talk so much either!"
    "You fuck her harder!"
    scene basement 9pm 054nf
    miranda "Hah... ahhh... yes..."
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hnn... hah... hah..."
        davide "Good. She gave up and is just enjoying it."
        pov "Mine too, haha."
        davide "Good to see you're also able to shut the sluts up, haha."
    else:
        mom "Fucking stop Davide! I... hah... hate you!"
        davide "She's not going to give in to this! I need to tame this bitch more!"
        if nicole_revenge == True:
            povi "Fuck you Davide. Maybe I'll tame your ass with a baseball bat covered in barbed wire sometime!"
        else:
            pov "Mine too, haha."
        davide "Good to see you're also able to shut the sluts up, haha."
    pov "Yes! She's a really hot ride!"
    if nicole_revenge == True:
        povi "I'm sorry! I need to keep Davide happy long enough to think of something"
    miranda "Hah... ahhh... yes..."
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hnn... hah... hah..."
        scene basement 9pm 055nf
        "You two fuck them for a while until they're done and you leave the basement."
    elif nicole_revenge == True:
        scene basement 9pm 052nf
        pov "Hey Davide, seeing how I'm doing such a good job taming this bitch..."
        if inc == True:
            pov "Why don't you let me tame my mother for you?"
            davide "God damn son! You want to fuck your mom!"
        else:
            pov "Why don't you let me tame my mother for you?"
            davide "God damn son! You want to fuck [pov]!"
        mom "But... [pov]..."
        "You cut her off intentionally"
        pov "I just figured you might enjoy something hot and wet, [miranda] is flooding over here!"
        miranda "Please Davide! Fuck me! Fuck me until I pass out filled with your cum!"
        povi "Holy shit [miranda], you are a whore! But this can work!"
        "You pull out of [miranda] and the juices flow out of her. David seems interested."
        scene basement 9pm 051n
        davide "Fuck it, yeah. I done with this dry as shit over here. You can do what you want with it!"
        miranda "Yay!!! Get that fat black cock inside me right now!"
        "Davide walks over to here and shoves his dick deep inside her."
        scene basement 9pm 026b
        davide "You weren't kidding kid! She's a sopping mess! I love it!"
        davide "Way to look out for your superiors! I think you're going to go far kid!"
        pov "Thank Davide! I think I'm going give this whore a spray down in the shower before I figure out how to tame her!"
        davide "Haha, good thinking! Get something wet down there!"
        scene black
        "You help her get out of the stocks and get dressed, she's trembling."
        scene basement 9pm 053nnc
        if inc == True:
            pov "<whisper> Don't worry mom, I'm getting you out of here."
            mom "..."
            pov "<whisper> I promise. I only said and did those things so I could make sure he didn't hurt you even more."
            mom "<whisper> Ok... Thank you son."
        else:
            pov "<whisper> Don't worry [mother], I'm getting you out of here."
            mom "..."
            pov "<whisper> I promise. I only said and did those things so I could make sure he didn't hurt you even more."
            mom "<whisper> Ok... Thank you [pov]."
        "You walk with her towards the stairs. She stops and turns around to face you."
        scene basement 9pm 045
        mom "<whisper> I'm so sorry. I keep failing you. I didn't want this. I never wanted this."
        pov "<whisper> I know that. I really do."
        if inc == True:
            pov "<whisper> You're my mother. I love you know matter what. And I learn more and more how strong you've had to be while I was gone."
        else:
            pov "<whisper> You're like a mother to me. I love you know matter what. And I learn more and more how strong you've had to be while I was gone."
        pov "<whisper> Well you're not alone now. I am here for you. And I promise that very soon, we're going to get our lives back."
        pov "<whisper> And Davide and anyone else responsible of this mess... They are going to pay dearly."
        if inc == True:
            "Suddenly your mother moves very close to you, her hands on your chest. You wrap your arms around her. Holding her tightly."
        else:
            "Suddenly [pov] moves very close to you, her hands on your chest. You wrap your arms around her. Holding her tightly."
        scene basement 9pm 047
        mom "<whisper> You know... You actually make me believe you. Believe in something better after all of this."
        mom "<whisper> It's one of the many reasons I love you. And I'm proud of you."
        "She leans in and kisses you. It's a passionate moment that takes you by surprise."
        scene basement 9pm 046
        mom "<whisper> Thank you for saving me..."
        scene black
        "You two leave the basement together."
    else:
        mom "Nooo... hah... stop..."
        scene basement 9pm 055nf
        "You two fuck them for a while until they're done and you leave the basement."
    $ dtime += 2
    $ b9rnntrmir = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump mcroom

label base9nicpunl:
    scene basement 9pm 042
    $ base9nickiss = False
    if inc == True:
        pov "<whisper> Relax mom! I won't actually punish you!"
    else:
        pov "<whisper> Relax [mother]! I won't actually punish you!"
    mom "Hmm...?"
    pov "<whisper> You don't need to be scared now. You know that I won't hurt you!"
    mom "<whisper> But you're in the gang now."
    pov "<whisper> Yes but that doesn't mean I have to do everything they do."
    scene basement 9pm 043
    mom "Oh..."
    pov "<whisper> But I'm still confused why you're so angry seeing me down here?"
    pov "<whisper> I thought you might need my help down here?"
    if inc == True:
        mom "<whisper> This is something I've wanted to hide from you and your siblings."
    else:
        mom "<whisper> This is something I've wanted to hide from you and my daughters."
    mom "<whisper> Bad things happen down here."
    pov "<whisper> Yes and that's the reason why I want to be down here with you. So that no more bad things happen to you."
    scene basement 9pm 044
    mom "<whisper> But we've already done unforgivable things..."
    pov "<whisper> You mean the drugs?"
    mom "<whisper> Yes..."
    mom "<whisper> I'm so proud of you. You're such a good person and now I have failed you..."
    if inc == True:
        mom "<whisper> I failed as a mother..."
        pov "<whisper> Oh, mom..."
        pov "<whisper> Mom!"
    else:
        pov "<whisper> Oh, [mother]..."
        pov "<whisper> [mother]!"
    scene basement 9pm 045
    pov "<whisper> I'll never judge you like that! I know why you had to do it."
    pov "<whisper> I love you. And I'm pretty sure that [ls] and [bs] would understand it too."
    if inc == True:
        pov "<whisper> You sacrificed yourself for the family."
        pov "<whisper> And I'll do everything needed to get my old mom back!"
    else:
        pov "<whisper> You sacrificed yourself for us."
        pov "<whisper> And I'll do everything needed to get the old [mother] back!"
    pov "<whisper> The woman I know and love."
    scene basement 9pm 046
    mom "<whisper> You're saying such nice things to me..."
    pov "<whisper> I'm just glad I could bring your wonderful smile back."
    mom "<whisper> I was so trapped under all these dark feelings that I forgot how positive you could be."
    pov "<whisper> See? So it isn't a bad thing when I'm down here with you."
    if inc == True:
        mom "<whisper> My son want to rescue my fallen soul..."
    else:
        mom "<whisper> You want to rescue my fallen soul..."
    if momlove >= 30:
        scene basement 9pm 047
        $ base9nickiss = True
        mom "<kiss>"
        povi "What...?"
        if inc == True:
            povi "Mom is kissing me!"
        else:
            povi "[mother] is kissing me!"
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
    mom "<whisper> You need to punish me, Davide need drama all the time or he's just not happy, so we have to play along."
    pov "<whisper> But..."
    scene basement 9pm 050
    mom "<whisper> Just go ahead and spank me a little, so he won't get suspicious."
    pov "<whisper> Spank..."
    if inc == True:
        povi "Did my mom really ask me to spank her naked ass?"
    else:
        povi "Did she really ask me to spank her naked ass?"
    scene basement 9pm 051
    mom "<whisper> Please... just a little. You must show him that you're a worthy gang member."
    if inc == True:
        pov "Ok. So it's time that you need to get spanked for being a bad mom!"
    else:
        pov "Ok. So it's time that you need to get spanked for being a bad girl!"
    mom "Please be gentle!"
    davide "So you've decided to give the bitch a spanking huh? A good choice!"
    scene basement 9pm 052
    if inc == True:
        davide "I bet you waited a long time to do this to your mom!"
    else:
        davide "I bet you waited a long time to do this to [mother]!"
    miranda "Yes! She needs a hard spanki... Hah!"
    davide "Shut up slut! No talking while I'm fucking you!"
    miranda "Hah... hah..."
    if inc == True:
        povi "Mom is right. I should do it. It's still better than Davide doing something."
    else:
        povi "[mother] is right. I should do it. It's still better than Davide doing something."
    povi "So then, let's do it."
    call screen base9splove

screen base9splove():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base9splove'), Jump('base9splvh')) hovered tt.Action ("Spank her hard") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base9splove'), Jump('base9splvn')) hovered tt.Action ("Spank her gentle") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
            pov "<whisper> Sorry mom. I need to spank you hard to sell this as a real punishment."
        else:
            pov "<whisper> Sorry [mother]. I need to spank you hard to sell this as a real punishment."
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
    dad "But I need her now! There's an urgent call for her!"
    davide "Ok, ok, that seems serious. You should let her go [pov]."
    scene basement 9pm 057
    mom "I'm coming darling, don't get mad."
    davide "Oh she looks chastened. You did a good job!"
    if inc == True:
        pov "<whisper> Mom, I'm not with Davide..."
    else:
        pov "<whisper> [mother], I'm not with Davide..."
    scene basement 9pm 058
    mom "<whisper> Don't worry [pov]. You did it perfectly."
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
        povi "Mom looks really happy. So I did good I guess."
    else:
        povi "[mother] looks really happy. So I did good I guess."
    if base9nickiss == True:
        povi "But I still need to know why she kissed me. I'll have to ask her about it when we're alone again."
    scene black
    "You leave the basement shortly after they do."
    $ dtime += 2
    $ b9rnlove = True
    jump mcroom

label lroom22ass:
    hide screen locations
    scene livingroom 10pm 002a
    povi "Damn, her ass is even hotter in that dress!"
    jump lroom

label lroom22talk:
    hide screen locations
    scene livingroom 10pm 002
    $ lroom10mcwin = False
    $ momrelationship += 1
    dad "Look who's here."
    mom "Oh, [pov] You found us."
    davide "Hi bro."
    mom "I was about to ask them what they wanted to do with all these bags."
    davide "And I told her that's the new stuff we \"found\"."
    pov "Found?"
    if inc == True:
        dad "Yes the less you know the better, son."
    else:
        dad "Yes the less you know the better, [pov]."
    pov "Okay..."
    if NTR == True and momrelationship < 6 or hardntr == True:
        jump lroom22hardntr
    scene livingroom 10pm 003
    davide "How about you bring us some drinks, [mother]?"
    mom "Hmm... okay, I can do that."
    dad "Yeah, my throat is all dry."
    povi "Hmm..."
    scene livingroom 10pm 004
    mom "I'll get you something too, [pov]. So you can drink with us."
    davide "Ya, he could use a drink too."
    if inc == True:
        dad "Careful, my son will drink us all under the table if we let him!"
        pov "Wait mom!"
    else:
        dad "Careful, he'll drink us all under the table if we let him!"
        pov "Wait [mother]!"
    jump lr22nontr

label lr22nontr:
    call screen lr22nontr1

screen lr22nontr1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lr22nontr1'), Jump('lroom22love')) hovered tt.Action ("Help her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lr22nontr1'), Jump('lroom22cor')) hovered tt.Action ("Slap her ass [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
    davide "You can't be serious, helping a woman!"
    pov "Oh yes, I am."
    mom "Oh, thank you."
    if inc == True:
        davide "What's with your son, bro?"
    else:
        davide "What's with him, bro?"
    dad "I don't know, I'm sorry."
    scene livingroom 10pm 007a
    mom "I appreciate that you'll help me but you need to be careful."
    pov "Why?"
    mom "This isn't the behavior that fits in your role."
    mom "You have to be a bad boy like them."
    scene livingroom 10pm 008a
    pov "I don't care about these idiots."
    mom "But..."
    pov "And I don't want you to have to participate in this shit any longer."
    if inc == True:
        pov "Dad's friends are scum and you deserve better then them."
    else:
        pov "Bruce's friends are scum and you deserve better then them."
    mom "..."
    scene livingroom 10pm 009a
    pov "I want you to stay with me now."
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
    mom "You're so sweet, but I'm not sure if they'll get angry with you. And what if something bad happens?"
    if inc == True:
        pov "Please trust me. One time won't make them suspicious. Also dad will talk to them, I'm sure."
    else:
        pov "Please trust me. One time won't make them suspicious. Also Bruce will talk to them, I'm sure."
    pov "I'll participate more in this farce later, but for this evening I only want to spend time with you."
    scene livingroom 10pm 011a
    mom "You're right! One evening won't hurt them."
    mom "And I love you for being such a brave young man. The time overseas was good for you."
    pov "Thank you. So we'll stay here together?"
    mom "Yes, [pov]."
    scene livingroom 10pm 012a
    pov "We have a change of plans!"
    dad "Eh?"
    davide "Huh?"
    if inc == True:
        pov "Mom will stay with me this evening!"
    else:
        pov "[mother] will stay with me this evening!"
    scene livingroom 10pm 013a
    mom "Yes we talked about it and after he has been gone for so long, I want to spend this evening with him."
    mom "I'm sure you'll can handle this stuff yourself."
    davide "..."
    scene livingroom 10pm 014a
    davide "But I thought you would help us get this stuff prepared."
    if inc == True:
        pov "Not today! As my mom said we'll be spending some time together without you."
    else:
        pov "Not today! As [mother] said we'll be spending some time together without you."
    pov "You're two strong men, I'm sure you can handle this without us."
    dad "Wait, [pov]..."
    scene livingroom 10pm 015a
    davide "Are you fucking kidding me?"
    pov "No! I 'm fucking not."
    dad "..."
    mom "Calm down Davide. After so long time, he has the right to spend some time with me."
    davide "..."
    if inc == True:
        davide "We'll talk about this later. And about your son too."
    else:
        davide "We'll talk about this later. And about him too."
    scene livingroom 10pm 016a
    mom "Will you help them carry their stuff out?"
    pov "Why?"
    mom "They'll be out sooner and we'll have more time together."
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
        pov "Appreciation for getting us drinks as ordered, mom."
    else:
        pov "Appreciation for getting us drinks as ordered, [pov]."
    mom "Okay..."
    scene livingroom 10pm 007b
    davide "Haha, good one bro. You'll fit in good with us here."
    if inc == True:
        dad "That's my son."
    pov "She needed to learn her place."
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
        pov "Yes, I'll be spending the rest of the evening with my mom alone, there's much to discuss."
    else:
        pov "Yes, I'll be spending the rest of the evening with [mother] alone, there's much to discuss."
    scene livingroom 10pm 009b
    davide "What?"
    mom "Eh?"
    dad "You mean...?"
    davide "But we need her help with this stuff!"
    pov "Our help or just hers?"
    dad "No, just hers. You can't help us, you're not part of the gang."
    if inc == True:
        davide "Ya, your dad is right."
    else:
        davide "Ya, Bruce is right."
    pov "Haha, no! If I can't participate then neither can she. We'll spend the evening together after being gone for so long I need us to catch up."
    davide "But..."
    pov "The \"bad boy\" decided. And when you're ready to let me join you, then we can discuss helping you out then."
    scene livingroom 10pm 010b
    dad "He's a true \"bad boy\", hah..."
    davide "Okay, it seems you're brave enough to stand your ground. So you can spend the evening with her, this time."
    davide "We need to get this shit taken care now, anyway. Its not worth taking the time to argue with you boy."
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
    scene livingroom 10pm 003
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    davide "How about you come here and sit on my lap, [mother]?"
    mom "Huh?"
    dad "I don't know Davide."
    jump lr22hntrd

label lr22hntrd:
    scene livingroom 10pm 003
    call screen lr22hntrd1

screen lr22hntrd1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('lr22hntrd1'), Jump('lroom22hardntrdark')) hovered tt.Action ("Darker Paths") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('lr22hntrd1'), Jump('lroom22hardntrdec')) hovered tt.Action ("Get out of here") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label lroom22hardntrdark:
    call screen checkdarkerpaths_nicole
    if nicole_voyeur == True or nicole_ntr == True:
        jump lroom22hardntrscene
    else:
        jump lroom22nicrevenge

#----- Custom -----
label lroom22hardntrscene:
    davide "I won't wait all day. Come here!"
    mom "Okay Davide."
    pov "But..."
    scene livingroom 10pm 004c
    davide "Good girl!"
    mom "Hmm..."
    if nicole_voyeur == True:
        povi "Wow! Why did she do that?"
    else:
        povi "Oh no! Why did she do that?"
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
    if nicole_voyeur == True:
        if inc == True:
            povi "And yet you're doing it mom..."
            scene livingroom 10pm 006c
            povi "I can even see her thong. And I'm sure dad can see that too."
            povi "But why doesn't he do anything. Mom is sitting on another dude's lap. Does he like this?"
        else:
            povi "And yet you're doing it [mother]..."
            scene livingroom 10pm 006c
            povi "I can even see her thong. And I'm sure Bruce can see that too."
            povi "But why doesn't he do anything. [mother] is sitting on another dude's lap. Does he like this?"
        scene livingroom 10pm 007c
        povi "i think he does like it! He's doing nothing, not even saying anything about it."
        if inc == True:
            povi "Just staring at her crotch. Damn dad, are you just a perv in the end?"
        else:
            povi "Just staring at her crotch. Damn Bruce, are you just a perv in the end?"
    else:
        if inc == True:
            povi "Are you serious mom?"
            scene livingroom 10pm 006c
            povi "I can even see her thong. And I'm sure dad can see that too."
            povi "But why doesn't he do anything. Letting mom sit on this asshole's lap. Does he like this?"
        else:
            povi "Are you serious [mother]?"
            scene livingroom 10pm 006c
            povi "I can even see her thong. And I'm sure Bruce can see that too."
            povi "But why doesn't he do anything. Letting her sit on this asshole's lap. Does he like this?"
        scene livingroom 10pm 007c
        povi "I can't believe it! He's doing nothing, not even saying something."
        if inc == True:
            povi "Just staring at her crotch. Damn dad what's wrong with you?"
        else:
            povi "Just staring at her crotch. Damn Bruce what's wrong with you?"
    davide "Come on let's go!"
    mom "So soon?"
    scene livingroom 10pm 008c
    with vpunch
    davide "Move your ass, sexy slut."
    mom "Ouch, Davide. <giggle>"
    if gangmember == False:
        if nicole_voyeur == True:
            if inc == True:
                povi "He's not even going to try to stop him. Completely useless."
                davide "You're coming to, bro? What a pity your son can't join us too."
                pov "What...?"
                dad "Sorry, son. Gang members only."
                pov "Dad! Really?"
                dad "That's the rule, sorry son."
            else:
                povi "No way! Do something Bruce! He's too strong for me but you work out, you should stop him."
                davide "You're coming to, bro? What a pity [pov] can't join us too."
                pov "What...?"
                dad "Sorry, [pov]. Gang members only."
                pov "Bruce! Really?"
                dad "That's the rule, sorry."
        else:
            if inc == True:
                povi "No way! Do something dad! He's too strong for me but you work out, you should stop him."
                davide "You're coming to, bro? What a pity your son can't join us too."
                pov "What...?"
                dad "Sorry, son. Gang members only."
                pov "Dad! Really?"
                dad "That's the rule, sorry son."
            else:
                povi "No way! Do something Bruce! He's too strong for me but you work out, you should stop him."
                davide "You're coming to, bro? What a pity [pov] can't join us too."
                pov "What...?"
                dad "Sorry, [pov]. Gang members only."
                pov "Bruce! Really?"
                dad "That's the rule, sorry."
    scene livingroom 10pm 009c
    davide "I won't wait any longer. Downstairs, now!"
    mom "Haha, calm down Davide. No need to hurry, we have enough time."
    if nicole_voyeur == True:
        povi "Davide is an asshole, but he does have good taste in bitches!"
    else:
        povi "This can't happen! I need to stop him!"
    davide "Let's give him a good show!"
    mom "Okay. You're coming too, honey?"
    dad "Y... yes..."
    if gangmember == True:
        jump base10pmnicntr
    if nicole_voyeur == True:
        if inc == True:
            povi "Dad is pretty much spineless!"
        else:
            povi "Bruce is pretty much spineless!"
    else:
        if inc == True:
            povi "No! Dad!"
        else:
            povi "No! Bruce!"
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ dtime += 1
    jump basement

#----- Custom -----
label lroom22nicrevenge:
    davide "I won't wait all day. Come here!"
    mom "Okay Davide... just calm down..."
    if nicole_revenge == True:
        pov "But..."
    else:
        pov "Hmm..."
    scene livingroom 10pm 004c
    davide "Good girl!"
    mom "..."
    if nicole_revenge == True:
        povi "Oh no!"
    else:
        povi "Hehe!"
    davide "What's with you?"
    if inc == True:
        mom "Please calm down Davide. My son is here with us."
        davide "And why's that a problem? Seeing his sexy mom sitting on another guys lap?"
    else:
        mom "Please calm down Davide. [pov] is here with us."
        davide "And why's that a problem? Seeing his sexy friend sitting on another guys lap?"
    mom "Please don't..."
    davide "So how about you show him a little bit more?"
    scene livingroom 10pm 005c
    mom "You... you can't be serious..."
    davide "Here take a good look, [pov]! You won't see this every day."
    mom "Don't [pov]. He's just joking..."
    if nicole_revenge == True:
        povi "She's doing her best to play along. I'm sure she's doing to it to protect me."
        povi "Fucking Davide. I'm going to get rid of him one way or another..."
        if inc == True:
            povi "I'm sorry mom."
            scene livingroom 10pm 006c
            povi "I can see her thong. And I'm sure dad can see that too."
            povi "But why doesn't he do anything. Letting mom sit on this asshole's lap."
        else:
            povi "I'm sorry [mother]."
            scene livingroom 10pm 006c
            povi "I can see her thong. And I'm sure Bruce can see that too."
            povi "But why doesn't he do anything. Letting her sit on this asshole's lap."
        scene livingroom 10pm 007c
        povi "I can't believe it! He's doing nothing, not even saying something."
        if inc == True:
            povi "Just staring at her crotch. Damn dad what's wrong with you?"
        else:
            povi "Just staring at her crotch. Damn Bruce what's wrong with you?"
    else:
        if inc == True:
            povi "Looking good mom!"
            scene livingroom 10pm 006c
            povi "I can see her thong. And I'm sure dad can see that too."
            povi "Why isn't he doing anything though? Maybe he's into this sort of thing."
        else:
            povi "Looking good [mother]!"
            scene livingroom 10pm 006c
            povi "I can see her thong. And I'm sure Bruce can see that too."
            povi "But why doesn't he do anything. Maybe he's into this sort of thing."
        scene livingroom 10pm 007c
        povi "Seriously, he's doing whatever he can to avoid looking at them."
        if inc == True:
            povi "I guess he's not into this as much as I thought. Damn dad what's wrong with you?"
        else:
            povi "I guess he's not into this as much as I thought. Damn Bruce what's wrong with you?"
    davide "Come on let's go!"
    mom "Do we have too?"
    scene livingroom 10pm 008c
    with vpunch
    davide "Move your ass, slut."
    mom "Ouch, Davide. <forced giggle>..."
    if nicole_revenge == True:
        povi "Davide is so fucking dense. He can't even tell she's pretending. He actually believes she likes this crap."
        if gangmember == False:
            if inc == True:
                povi "No way! Do something dad! He's too strong for me but you work out, you should stop him."
                davide "You're coming to, bro? What a pity your son can't join us too."
                pov "What...?"
                dad "Sorry, son. Gang members only."
                pov "Dad! Really?"
                dad "That's the rule, sorry son."
            else:
                povi "No way! Do something Bruce! He's too strong for me but you work out, you should stop him."
                davide "You're coming to, bro? What a pity [pov] can't join us too."
                pov "What...?"
                dad "Sorry, [pov]. Gang members only."
                pov "Bruce! Really?"
                dad "That's the rule, sorry."
    else:
        povi "She doesn't seem that into it. She's joking around, but it all feels forced. Her voice is really tense."
        if gangmember == False:
            if inc == True:
                povi "I wonder how long this have been going on? Dad seems to have pretty much given up."
                davide "You're coming to, bro? What a pity your son can't join us too."
                pov "What...?"
                dad "Sorry, son. Gang members only."
                pov "Dad! Really?"
                dad "That's the rule, sorry son."
            else:
                povi "I wonder how long this have been going on? Bruce seems to have pretty much given up."
                davide "You're coming to, bro? What a pity [pov] can't join us too."
                pov "What...?"
                dad "Sorry, [pov]. Gang members only."
                pov "Bruce! Really?"
                dad "That's the rule, sorry."
    scene livingroom 10pm 009c
    davide "I won't wait any longer. Downstairs, now!"
    mom "Haha... calm down Davide."
    if nicole_revenge == True:
        povi "Seriously, she's giving me the look again. That defeated look in her eyes. I breaks my fucking heart."
        povi "I need to see what I can do to join in."
    else:
        povi "Seriously, you can tell she doesn't want to go down there with him. That defeated look in her eyes. Kind of turns me on!"
        povi "I need to see what I can do to join in."
    davide "Let's give him a good show!"
    mom "..."
    if gangmember == True:
        jump base10pmnicntr
    if nicole_revenge == True:
        povi "No!!!"
    else:
        povi "Next time..."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ dtime += 1
    jump basement

label lroom22hardntrdec:
    pov "Fuck this, I'm out!"
    if inc == True:
        mom "Son, don't go..."
    else:
        mom "[pov], don't go..."
    davide "Nah, the little bitch doesn't want to be here then he doesn't have to be."
    davide "[mother] and I will have our own fun!"
    povi "I'm going to fucking kill that guy one day, such an asshole!"
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ dtime += 1
    jump mcroom

label lroom11pmtalk:
    hide screen locations
    scene livingroom 11pm 001
    mom "There you are... Come sit with me..."
    $ momrelationship += 1
    mom "You took so long I got a bit bored."
    mom "So I started to drink alone, but you don't mind, do you? <giggle>"
    if inc == True:
        pov "Sure mom."
    else:
        pov "Sure, [mother]."
    scene livingroom 11pm 002
    mom "It was a very good idea to have some time together."
    pov "I'm glad you liked it too."
    mom "You're such a strong man when you stand up against Davide!"
    pov "Davide is just a coward, if I was stronger he wouldn't even try to stand up to me."
    mom "And that's why I'm so proud of you!"
    if inc == True:
        pov "Oh mom."
    else:
        pov "Oh, [mother]."
    if momdrunktimes >= 1 and momlove >= 50 or momdrunktimes >= 1 and momcorruption >= 30:
        jump lr11pmkissremembermepause
    else:
        jump lroom11pmtalkcontinued

label lr11pmkissremembermepause:
    scene livingroom 11pm 002
    call screen lr11pmkissrememberme

screen lr11pmkissrememberme():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        #----- Added -----
        if momlove >= 50:
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('lr11pmkissrememberme'), Jump('lroom11pmkissrememberyes')) hovered tt.Action ("Remember Me") focus_mask True
        #----- Added -----
        if momcorruption >= 30:
            imagebutton auto "gui/icons/icon_question_%s.png" action (Hide('lr11pmkissrememberme'), Jump('lroom11pmkissrememberno')) hovered tt.Action ("Doesn't Remember Me") focus_mask True
        if lroom10mcwin == True and gangmember == True and momlove >=50 or lroom10mcwin == True and gangmember == True and momcorruption >= 30:
            #----- imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('basement1'), Jump('base10pmnic')) hovered tt.Action ("Enter the basement") focus_mask True -----
            imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('lr11pmkissrememberme'), Jump('basement10pmlanding')) hovered tt.Action ("Enter the basement") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label basement10pmlanding:
    mom "I have an idea! Let's go down to the basement!"
    scene livingroom 11pm 002
    mom "You are a gang member now, so you should be able to enjoy some of the amenities memberships provides."
    pov "You don't have to talk me into it! Let's go."
    "[mother] gets up and leads to the way to basement."
    scene livingroom 10pm 017ab
    mom "I really think you're going to like this..."
    povi "I believe it."
    scene black
    "You fall behind for a moment, lost in thoughts about how this all started and wondering where it could all lead."
    jump base10pmnic

label lroom11pmkissrememberyes:
    $ lroom11pmkissremember = True
    jump lroom11pmtalkcontinued

label lroom11pmkissrememberno:
    $ lroom11pmkissremember = False
    jump lroom11pmtalkcontinued

label lroom11pmtalkcontinued:
    scene livingroom 11pm 003
    mom "And I'd forgot how good looking you are."
    if inc == True:
        pov "Mom?"
    else:
        pov "[mother]?"
    povi "What's she talking about?"
    mom "I missed you for so long and now you here with me all alone."
    povi "Wait? Is she into me? Or maybe she drank a little to much?"
    povi "But that makes no sense. Even when she's drunk she doesn't behave like that."
    mom "I Just can't remember clearly when we met the last time."
    pov "What? It was like 20 minutes before?"
    scene livingroom 11pm 004
    mom "Your smell, like the way your looking at me and your masculine face."
    povi "Damn. I don't get it."
    mom "Don't make me wait any longer, since you were away such a long time."
    povi "1 year? What...?"
    scene livingroom 11pm 005
    mom "<kiss>"
    povi "Oh my god. Am I dreaming?"
    mom "I missed you so much, Adam!"
    pov "Adam? Wait...!"
    if lroom11pmkissremember == True:
        scene livingroom 11pm 004
        if inc == True:
            pov "Don't you remmeber, it's me [pov], your son."
            mom "Oh son. I'm so sorry. I just got lost a little bit there."
            pov "Are you okay mom? Do you need to lay down or something?"
        else:
            pov "Don't you remmeber, it's me [pov], Adam's son."
            mom "Oh sweeite! I'm so sorry. I just got lost a little bit there."
            pov "Are you okay [mother]? Do you need to lay down or something?"
        mom "No please, I'm ok. Besides..."
        scene livingroom 11pm 005
        mom "You taste so good."
        povi "Should I stop this? She is drunk, but then again she does seem to remember who I am now."
    else:
        if inc == True:
            povi "She's thinking I'm her late husband, my biologcial dad."
        else:
            povi "She's thinking I'm my dad? Did they have a thing before my parent's got married?"
        povi "But that makes sense now! So I must look like dad when he was younger."
        mom "You taste so good."
        povi "This is wrong because she doesn't realize it. She must be very drunk. But on the other hand..."
        povi "When she's thinking about doing this with my dad maybe it isn't a bad thing either."
    $ lroom11part1 = True
    jump lr11pmkiss

label lr11pmkiss:
    scene livingroom 11pm 005
    call screen lr11pmkiss1

screen lr11pmkiss1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('lroom11pmkiss1'), Jump('lroom11pmkiss2')) hovered tt.Action ("Go further [lv1] or [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('lroom11pmkiss1'), Jump('lroom11pmstop')) hovered tt.Action ("Stop her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom11pmkiss2:
    if lroom11pmkissremember == True:
        if inc == True:
            povi "Screw it! I can't stop now. I probably won't get another chance to make out with mom."
            scene livingroom 11pm 006
            pov "Come here mom. Let me kiss you more."
        else:
            povi "Screw it! I can't stop now. I probably won't get another chance to make out with [mother]."
            scene livingroom 11pm 006
            pov "Come here [mother]. Let me kiss you more."
        mom "Oh yes..."
        povi "I can't believe this is happening."
        mom "Yes! Show me that you missed me too when you were overseas."
        povi "Wow, her tongue is getting more aggressive!"
        scene livingroom 11pm 007
        mom "Here, I know you'll love playing with them."
        povi "Wow, I'm holding my mother's breast."
        if inc == True:
            pov "Oh mom, this feels so good."
        else:
            pov "Oh [pov], this feels so good."
        mom "Play with them, they're yours."
        povi "Wow, she's really getting into this. Is it because she's drunk or really likes it?"
        scene livingroom 11pm 008
        povi "She may be really excited that someone actually stood up against that scum too."
        povi "Oh what's she doing now?"
        mom "Hmm..."
        if inc == True:
            pov "Everything alright, mom?"
        else:
            pov "Everything alright, [mother]?"
        mom "You're really excited to be with me too, aren't you? I bet I'm going find something hard right now."
        pov "What...?"
        scene livingroom 11pm 009
        mom "I knew it!"
        if inc == True:
            povi "Oh shit, mom's touching my cock!"
            mom "I missed you so much, let me show you what it means to me that you stood up to those assholes!"
            povi "Oh shit, maybe this is going a little to far. Kissing was probably already pushing it, but now mom's groping my dick?"
        else:
            povi "Oh shit, [mother]'s touching in my cock!"
            mom "I missed you so much, let me show you what it means to me that you stood up to those assholes!"
            povi "Oh shit, maybe this is going a little to far. Kissing was probably already pushing it, but now [mother]'s groping my dick?"
        povi "If this is just because she's drunk, she'll get really mad if we continue."
        $ momdrunktimes += 1
        jump lroom11pmkiss3
    else:
        if inc == True:
            povi "Screw it! I can't stop now. I probably won't get another chance to make out with mom."
        else:
            povi "Screw it! I can't stop now. I probably won't get another chance to make out with [mother]."
        scene livingroom 11pm 006
        pov "Come here [mother]. Let me kiss you more."
        mom "Oh yes..."
        povi "Better just call her by her name. I don't want to ruin this chance now."
        mom "Yes! Show me that you missed me too."
        povi "Wow, her tongue is getting more aggressive!"
        scene livingroom 11pm 007
        mom "Here, I know you love to play with them."
        povi "Shit, I'm just like my father. Leeching her sexy boobs."
        if inc == False:
            povi "I understand why my dad started an affair with her."
        else:
            povi "Shit, dad was so lucky."
        mom "Play with them, they're yours."
        povi "But it's good to know that she seems to get drunk so fast. No wonder she doesn't like to drink often."
        scene livingroom 11pm 008
        povi "She must get really excited that someone stood up against that scum and used that as a reason to drink."
        povi "Oh what's she doing now?"
        mom "Hmm..."
        pov "Everything alright, [mother]?"
        mom "You're really excited to be with me, aren't you. I bet I find something hard right now."
        pov "What...?"
        scene livingroom 11pm 009
        mom "I knew it!"
        if inc == True:
            povi "Oh shit, mom's touching my crotch!"
        else:
            povi "Oh shit, [mother]'s touching in my crotch!"
        mom "I missed him so much too!"
        if inc == True:
            povi "Oh shit, maybe this is going a little to far. Kissing was like a little bit innocent stuff, but mom's groping my dick?"
        else:
            povi "Oh shit, maybe this is going a little to far. Kissing was like a little bit innocent stuff, but [mother]'s groping my dick?"
        povi "When she realizes what she did she'll get really mad."
        $ momdrunktimes += 1
        jump lroom11pmkiss3

label lroom11pmkiss3:
    scene livingroom 11pm 009
    if lroom11pmkissremember == True:
        call screen lroom11pmkiss4b
    else:
        call screen lroom11pmkiss4

screen lroom11pmkiss4():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lroom11pmkiss4'), Jump('lroom11pmhj')) hovered tt.Action ("Let her continue [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lroom11pmkiss4'), Jump('lroom11pmstop2')) hovered tt.Action ("Stop her [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

screen lroom11pmkiss4b():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lroom11pmkiss4b'), Jump('lroom11pmhjcor')) hovered tt.Action ("[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lroom11pmkiss4b'), Jump('lroom11pmhj')) hovered tt.Action ("[lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom11pmhj:
    if lroom11pmkissremember == True:
        scene livingroom 11pm 010
        pov "Then how about you show me how much you missed me?"
        povi "I won't let her stop now."
        if inc == True:
            mom "You want me to play with you? I'm so glad son."
        else:
            mom "You want me to play with you? I'm so glad [pov]."
        povi "I'm so glad she remembered who I was. It would have awkward is she still though I was Adam."
        "She starts to pull out your dick."
        scene livingroom 11pm 011b
        if inc == True:
            povi "Oh my god. What a view! Mom's sexy hand on my dick."
        else:
            povi "Oh my god. What a view! [mother]'s sexy hand on my dick."
        mom "So big and warm..."
        pov "It's good you like it."
        if inc == True:
            povi "This is heaven. Don't stop here mom!"
        else:
            povi "This is heaven. Don't stop here [mother]!"
        mom "Let's make it hard now, see how much you've grown."
        povi "I never knew she had such a naughty side. I wonder if was this whole mess that brought it out."
        scene livingroom 11pm 012b
        mom "It's getting bigger and bigger."
        pov "Because it's you touching it. You're hands are like magic."
        mom "<giggle> I'm so happy."
        pov "Me too."
        povi "Damn. You have no idea."
        mom "Oh wow... it's so big..."
        povi "That's never a bad thing to hear!"
        scene livingroom 11pm 013b
        mom "My hand looks so small suddenly. <giggles>"
        if inc == True:
            povi "Oh! So is my penis bigger than dad's?"
        else:
            povi "Oh! So is my penis bigger than Bruce's?"
        mom "I had no idea you grew up so much in just a year?"
        pov "Well I did! But we have never been separated so long before."
        pov "I'm so hard because I've desired you for so long!"
        mom "Oh... you got so big because of me?"
        if inc == True:
            povi "Getting a hand-job from my hot mom? I'm surprised it hasn't burst!"
        else:
            povi "Getting a hand-job from you? I'm surprised it hasn't burst!"
        pov "Let me make you feel good too."
        scene livingroom 11pm 014b
        image hjnic_lroom = Movie(channel="hjnic_lroom", play="images/anim/hjnic_lroom.webm")
        scene hjnic_lroom with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        mom "Hmm..."
        povi "Yes! Finally. I can touch her boobs and she wants me to do it."
        mom "You've always wanted to grope my breasts, haven't you?"
        pov "You have no idea how I've wanted to feel you big tits."
        povi "And how often I dreamed about it!"
        mom "Don't leave me alone for such a long time again. I miss feeling like the person touching me actually want me, not a dressed up slut."
        povi "My dick won't last long if you talk to me like that!"
        if inc == True:
            pov "You can bet on that, mom!"
        else:
            pov "You can bet on that, [mother]!"
        pov "I love playing with your nipples."
        scene livingroom 11pm 015b
        mom "Hnng... hah..."
        pov "Pulling them and seeing your nice reactions."
        mom "They are yours always now."
        if inc == True:
            povi "I wonder why dad ever leaves this woman with Davide? He's an idiot! She deserves better."
        else:
            povi "I wonder why Bruce ever leaves this woman with Davide? He's an idiot! She deserves better."
        mom "I love how your dick pulsates in my hand. I can almost imagine how it would pulsated inside me."
        povi "Holy fuck! I almost just came just from that!"
        scene livingroom 11pm 016b
        mom "Hiii..."
        pov "I love your little moans."
        mom "Hmm..."
        povi "Oh shit. She's squeezing my dick like crazy. I can't hold it any longer!"
        povi "Her dirty talking, that view, her glorious boobs and that firm grip. I'm going to cum so hard!"
        scene livingroom 11pm 017b
        pov "Argghh...! Yes... more..."
        mom "You're about to cum sweetie?"
        mom "Was my touching that good? <giggle>"
        povi "If this is a dream don't let me wake up now!"
        if inc == True:
            pov "Yes, yes... YES! MOM!"
        else:
            pov "Yes, yes... YES! [mother]!"
        pov "Hmm..."
        mom "Wow so warm..."
        scene livingroom 11pm 018b
        mom "So much came out..."
        if inc == True:
            povi "That's so damn hot. Mom's staring at my cum after she released me!"
        else:
            povi "That's so damn hot. [mother]'s staring at my cum after she released me!"
        pov "Well you did have me pretty damn worked up there with your naughty talk!"
        mom "Did I make you felt that good? But still that much...?"
        povi "I would love to see if she would lick it from her fingers right now, or smear it over her tits."
        povi "But I should see how she reacts tomorrow first."
        mom "So warm..."
        if inc == True:
            povi "Mom is just staring at my cum..."
        else:
            povi "[mother] is just staring at my cum..."
        scene livingroom 11pm 012a
        if inc == True:
            mom "That was really nice, son."
            mom "We should probably get cleaned up though. Your dad will be home soon."
            pov "Oh ok, mom. Thanks. That was really nice to spend some private time with you."
            mom "You too, son. Love you sweetie."
            pov "Love you too."
        else:
            mom "That was really nice, [pov]."
            mom "We should probably get cleaned up though. Bruce will be home soon."
            pov "Oh ok, [mother]. Thanks. That was really nice to spend some private time with you."
            mom "You too, [pov]. Love you sweetie."
            pov "Love you too."
        povi "I better leave her now. I'm sure she'll sleep as good as I will tonight, haha."
        $ momlove += 1
        $ lroom11hj = True
        $ dtime += 1
        jump lroom
    else:
        scene livingroom 11pm 010
        pov "Then how about you show me how much you missed me?"
        povi "I won't let her stop now."
        mom "You want me to play with you? I'm so glad Adam."
        povi "I wonder if I could get her to say my real name some time?"
        "She starts to unpack your dick."
        scene livingroom 11pm 011b
        if inc == True:
            povi "Oh my god. What a view! Mom's sexy hand on my dick."
        else:
            povi "Oh my god. What a view! [mother]'s sexy hand on my dick."
        mom "So big and warm..."
        pov "It's good you like it."
        if inc == True:
            povi "This is heaven. Don't stop here mom!"
        else:
            povi "This is heaven. Don't stop here [mother]!"
        mom "Let's make it hard after not seeing him for so long."
        povi "I wonder what time she became such a prude and if I can get her real naughty side back forever."
        scene livingroom 11pm 012b
        mom "It's getting bigger and bigger."
        pov "Because it's you touching it. You're hands are like magic."
        mom "<giggle> I'm so happy."
        pov "Me too."
        povi "Damn. You have no idea."
        mom "But something... is wrong..."
        povi "What...? No, no, no..."
        scene livingroom 11pm 013b
        mom "It's bigger then the old times. My hand looks so small suddenly."
        povi "Oh! So is my penis bigger than my dad's?"
        mom "Could a penis grew up so much?"
        pov "You're right! It never was that big before. But we have never been separated so long before."
        pov "I'm so hard because I desired you for so long!"
        mom "Oh... you got so big because of me?"
        if inc == True:
            povi "Getting a hand-job from my hot mom? He should get even bigger!"
        else:
            povi "Getting a hand-job from you? He should get even bigger!"
        povi "Let me make you feel god too."
        scene livingroom 11pm 014b
        image hjnic_lroom = Movie(channel="hjnic_lroom", play="images/anim/hjnic_lroom.webm")
        scene hjnic_lroom with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        mom "Hmm..."
        povi "Yes! Finally. I can touch her boobs and she wants me to do it."
        mom "You always loved to grope my breasts, don't you?"
        pov "You have no idea how I missed your big tits."
        povi "And how often I dreamed about that!"
        mom "Don't leave me alone for such a long time again. I missed your firm touches."
        povi "My dick won't last long if you talk to me like that!"
        pov "You can bet on that, [mother]!"
        pov "I love playing with your nipples."
        scene livingroom 11pm 015b
        mom "Hnng... hah..."
        pov "Pulling them to see your nice reactions."
        mom "They are yours always."
        povi "I wonder why dad ever left us? It had to be very import to leave such a hot woman."
        mom "I love how your dick pulsates. I can even remember how it pulsated in me."
        povi "Hell! How should I endure this until then?"
        scene livingroom 11pm 016b
        mom "Hiii..."
        pov "Such a nice reaction."
        mom "Hmm..."
        povi "Oh shit. She's squeezing my dick like crazy. I can't hold it any longer!"
        povi "Her dirty talking, that view, her big and soft boobs and her firm grip. I'll come so hard!"
        scene livingroom 11pm 017b
        pov "Argghh...! Yes... more..."
        mom "You're about to cum already?"
        mom "Was my touching that good? <giggle>"
        povi "If this is a dream don't let me wake up now!"
        if inc == True:
            pov "Yes, yes... YES! MOM!"
        else:
            pov "Yes, yes... YES! [mother]!"
        pov "Hmm..."
        mom "Wow so warm..."
        scene livingroom 11pm 018b
        mom "That much came out..."
        if inc == True:
            povi "That's so damn hot. Mom's staring at my cum after she released me!"
        else:
            povi "That's so damn hot. [mother]'s staring at my cum after she released me!"
        pov "It has to be that amount after your pressing was so wonderful!"
        mom "Did I make you felt that good? But still that much...?"
        povi "Damn she must really have loved him. And now I'm his replacement!"
        povi "I would love it when she would lick it from her fingers right now, or smear it over her tits."
        povi "But I must see how she reacts tomorrow first. It's to soon now!"
        mom "So warm..."
        if inc == True:
            povi "Drunk mom is staring at my cum..."
        else:
            povi "Drunk [mother] is staring at my cum..."
        povi "I better leave her now. I'm sure she'll sleep good tonight, haha."
        $ momcorruption += 1
        $ lroom11hj = True
        $ dtime += 1
        jump lroom

label lroom11pmhjcor:
    if lroom11pmkissremember == True:
        scene livingroom 11pm 010
        pov "Then how about you show me how much you missed me?"
        povi "I won't let her stop now."
        if inc == True:
            mom "You want me to play with you? You want me to be your mommy slut?"
        else:
            mom "You want me to play with you? You want me to be your personal slut."
        povi "I'm so glad she remembered who I was. It would have awkward is she still though I was Adam."
        "She starts to pull out your dick."
        scene livingroom 11pm 011b
        if inc == True:
            pov "Oh my god. What a view! I love seeing my mom's sexy hand on my dick."
        else:
            pov "Oh my god. What a view! I love seeing your sexy hand on my dick."
        mom "So big and warm..."
        pov "It's good you like it, slut."
        if inc == True:
            povi "This is heaven. Don't stop here mom!"
        else:
            povi "This is heaven. Don't stop here [mother]!"
        mom "Let's make it hard now, this slut needs to do her job."
        povi "I never knew she had such a naughty side. I wonder if was this whole mess that brought it out."
        scene livingroom 11pm 012b
        mom "It's getting bigger and bigger."
        pov "Because it's you touching it. You're naughty hands are like magic."
        mom "<giggle> I'm so happy I can serve you so well."
        pov "Me too, that's a good whore."
        povi "Damn. You have no idea."
        mom "Oh wow... it's so big..."
        povi "That's never a bad thing to hear!"
        scene livingroom 11pm 013b
        mom "My hand looks so small suddenly. <giggles>"
        if inc == True:
            povi "Oh! So is my penis bigger than dad's?"
        else:
            povi "Oh! So is my penis bigger than Bruce's?"
        mom "Do you like me jacking you off in our living room?"
        pov "Just think, they could be back any moment now! They could see how naughty you are!"
        pov "They will see how hard you made me!"
        mom "Oh... you got so big because of me, am I being a good whore then?"
        if inc == True:
            povi "Getting a hand-job from my hot mom? I'm surprised it hasn't burst!"
        else:
            povi "Getting a hand-job from you? I'm surprised it hasn't burst!"
        pov "Yes you are, now let me make my slut feel good too."
        scene livingroom 11pm 014b
        image hjnic_lroom = Movie(channel="hjnic_lroom", play="images/anim/hjnic_lroom.webm")
        scene hjnic_lroom with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        mom "Hmm..."
        povi "Yes! Finally. I can touch her boobs and she wants me to do it."
        mom "You've always wanted to grope my breasts, haven't you?"
        pov "Of course, a slut's breasts are begging for it!"
        povi "And how often I dreamed about it!"
        mom "Never you leave you whore for so long again! I need someone that know what their doing with thier hands to make me hot and wet."
        povi "My dick won't last long if you talk to me like that!"
        pov "You can bet on that!"
        pov "Do you like me playing with your nipples. Pinching and pulling them?"
        scene livingroom 11pm 015b
        mom "Hnng... hah..."
        pov "That's right, a whore know how I want her to react. Good slut."
        mom "They are yours always now. Squeeze and pull them to pieces if you want!"
        if inc == True:
            povi "I wonder why dad ever leaves this woman with Davide? He's an idiot! She deserves better."
        else:
            povi "I wonder why Bruce ever leaves this woman with Davide? He's an idiot! She deserves better."
        mom "I love how your dick pulsates in my hand. I can almost imagine how it would pulsated inside me."
        povi "Holy fuck! I almost just came just from that!"
        scene livingroom 11pm 016b
        mom "Hiii..."
        pov "I love your little moans."
        mom "Hmm..."
        povi "Oh shit. She's squeezing my dick like crazy. I can't hold it any longer!"
        povi "Her dirty talking, that view, her glorious boobs and that firm grip. I'm going to cum so hard!"
        scene livingroom 11pm 017b
        pov "Argghh...! Yes... more..."
        mom "You're about to cum?"
        mom "Was my touching that good? <giggle>"
        povi "If this is a dream don't let me wake up now!"
        if inc == True:
            pov "Yes, yes... YES! MOM!"
        else:
            pov "Yes, yes... YES! [mother]!"
        pov "Hmm..."
        mom "Wow so warm..."
        scene livingroom 11pm 018b
        mom "So much came out..."
        if inc == True:
            povi "That's so damn hot. Mom's staring at my cum after she released me!"
        else:
            povi "That's so damn hot. [mother]'s staring at my cum after she released me!"
        pov "Well you did have me pretty damn worked up there with your naughty talk!"
        mom "Did I make you felt that good? But still that much...?"
        povi "I would love to see if she would lick it from her fingers right now, or smear it over her tits."
        povi "But I should see how she reacts tomorrow first."
        mom "So warm..."
        if inc == True:
            povi "Mom is just staring at my cum..."
        else:
            povi "[mother] is just staring at my cum..."
        scene livingroom 11pm 014a
        if inc == True:
            mom "That felt so good, son."
            mom "We should probably get cleaned up though. Your dad will be home soon."
            pov "Yeah, we don't want him seeing what a whore you are for your son when he's gone!"
        else:
            mom "That felt so good, [pov]."
            mom "We should probably get cleaned up though. Bruce will be home soon."
            pov "Yeah, we don't want him seeing what a whore you are for me when he's gone!"
        scene livingroom 11pm 012a
        mom "Hnng..."
        pov "Love you too, slut."
        povi "I better leave her now. I'm sure she'll sleep as good as I will tonight, haha."
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
    povi "Damn, she don't get it."
    if inc == True:
        pov "I'm not Adam! I'm your son, [pov]!"
        mom "What are you talking about, Adam?"
        povi "Shit, drunk mom is a stupid mom..."
        pov "You're my mother and I'm your son and I'm sure this Isn't something we should do."
        povi "At least not now and especially not when you're drunk."
    else:
        pov "I'm not Adam! I'm his son, [pov]!"
        mom "What are you talking about, Adam?"
        povi "Shit, drunk [mother] is a stupid [mother]..."
        pov "I know you and we have such a good relationship so I'm sure this Isn't something we should do."
        povi "At least not now and especially not when you're drunk."
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
    povi "Damn, but it's no use. Hopefully I can have a normal conversation with her about that tomorrow when she's sober again."
    povi "But her kissing was so damn good."
    $ momlove += 1
    $ lroom11kiss = True
    $ dtime += 1
    jump lroom
