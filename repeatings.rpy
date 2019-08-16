#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label droom7momcorrepeat:
    scene diningroom 7am 014a
    mom "..."
    pov "Good girl!"
    mom "Hnn..."
    pov "I love to look at your big boobs!"
    mom "Please..."
    pov "Ssshh..."
    "You stare a while longer at her breasts."
    jump droom7momtalk2

label droom7momloverepeat:
    mom "Oh, you want to hold my hand again?"
    pov "Yes it's a good way to start the morning."
    scene diningroom 7am 009
    mom "Oh that's so sweet [pov]."
    if inc == True:
        pov "You're welcome, mom."
    else:
        pov "You're welcome [mother]."
    "You silently look at each other, just enjoying the moment."
    jump droom7momtalk2

label lroom8momfondle:
    hide screen locations
    $ momcorruption += 1
    scene livingroom 8am 012
    povi "I need to fondle that ass!"
    mom "Huh?"
    "You knead her ass-cheek."
    scene livingroom 8am 013
    mom "Please stop. That's going to far."
    pov "No, I need to fondle your hot ass."
    pov "It's also your fault for bending over like that."
    scene livingroom 8am 014
    mom "Hnn..."
    "She lets you fondle her ass for some time."
    $ lroom8fondlefirst = True
    jump lroom8momtalk

#----- Custom reaction Corrupton to Love -----
label lroom8momfondle_love:
    hide screen locations
    $ momlove += 1
    scene livingroom 8am 012
    mom "Huh?"
    "You knead her ass-cheek."
    scene livingroom 8am 013
    mom "Oh Sweetie, that's nice."
    pov "You have the perfect ass."
    scene livingroom 8am 014
    mom "Hnn..."
    "She lets you fondle her ass for some time before asking you to stop so she can finish cleaning."
    $ lroom8fondlefirst = True
    jump lroom8momtalk

label bsis142look:
    hide screen locations
    scene bigsisroom 2pm 002
    povi "Oh, they're fighting again. Better leave."
    $ bigsisrelationship += 1
    $ dtime += 1
    jump bsisroom

label bsis142listen:
    hide screen locations
    povi "Oh, they're fighting again. Better leave."
    $ bigsisrelationship += 1
    $ dtime += 1
    jump bsisroom

label kitchen11repeat:
    pov "Urg! Not again!"
    if momcorruption > momlove:
        if nicolereddresswear == True:
            scene kitchen 11am 011ancc1
        elif nicolebabydollwear == True:
            scene kitchen 11am 011ancc2
        elif nicolesweaterpantswear == True:
            scene kitchen 11am 011ancl1
        elif nicolerobewear == True:
            scene kitchen 11am 011ancl2
        else:
            scene kitchen 11am 011a
        mom "I'm sorry."
    else:
        if nicolereddresswear == True:
            scene kitchen 11am 011bncc1
        elif nicolebabydollwear == True:
            scene kitchen 11am 011bncc2
        elif nicolesweaterpantswear == True:
            scene kitchen 11am 011bncl1
        elif nicolerobewear == True:
            scene kitchen 11am 011bncl2
        else:
            scene kitchen 11am 011b
        mom "Oh come on. It isn't that bad."
    povi "This needs to change..."
    call screen k11h2

screen k11h2():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('k11h2'), Jump('kitchen11momhelprepeat')) hovered tt.Action ("Help her with the dinner[lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('k11h2'), Jump('kitchen11momnohelprepeat')) hovered tt.Action ("Don't help her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen11momhelprepeat:
    $ momlove += 1
    pov "I'll help you again with the dinner."
    if nicolereddresswear == True:
        scene kitchen 11am 007ancc1
    elif nicolebabydollwear == True:
        scene kitchen 11am 007ancc2
    elif nicolesweaterpantswear == True:
        scene kitchen 11am 007ancl1
    elif nicolerobewear == True:
        scene kitchen 11am 007ancl2
    else:
        scene kitchen 11am 007a
    mom "Thank you so much!"
    pov "You're welcome."
    "You help her."
    $ dtime += 1
    jump kitchen

label kitchen11momnohelprepeat:
    $ momcorruption += 1
    pov "No, I won't help you."
    if nicolereddresswear == True:
        scene kitchen 11am 007bncc1
    elif nicolebabydollwear == True:
        scene kitchen 11am 007bncc2
    elif nicolesweaterpantswear == True:
        scene kitchen 11am 007bncl1
    elif nicolerobewear == True:
        scene kitchen 11am 007bncl2
    else:
        scene kitchen 11am 007b
    mom "But I didn't want to..."
    pov "Because it's a woman's job."
    $ dtime += 1
    jump kitchen

label kitchen8amrepeat1:
    pov "I wonder if she's doing that on purpose. No way she smells an orange every morning."
    pov "Or is she just a bit crazy?"
    jump kitchen

label kitchen8amrepeat2:
    pov "Damn, I can't get enough of this view. But it would be even better with some cleavage."
    jump kitchen

label kitchen8amrepeat3:
    scene kitchen 8am 012
    ls "You got me again <giggle>."
    ls "But next time I'll be ready."
    jump kitchen8lsistalk

label kitchen8amrepeat4:
    scene kitchen 8am 006
    ls "I need to go to school soon. But can we do something together this afternoon?"
    if inc == True:
        pov "We'll see if I have time for my lovely little sister."
    else:
        pov "We'll see if I have time for my lovely girl."
    ls "Please... It's so boring all alone."
    pov "Hmm..."
    if gangmember == True and lilsisrelationship >= 6 and lilsislove >= 50 or gangmember == True and lilsisrelationship >= 6 and lilsiscorruption >= 30:
        pov "I have also something else for you. Meet me at 4am tomorrow in the kitchen."
        scene kitchen 8am 007
        ls "Why? You want to show me something special?"
        pov "Yes, very special. But I won't tell you now, you'll see it then. And be quiet so no one else knows."
        ls "Oh, now I'm very interested."
        $ meet4am = True
    jump kitchen8lsistalk2

label proom8repeat1:
    scene main 8pm parents room
    povi "She's changing again."
    call screen proom8rep

screen proom8rep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if momlove >= 30:
            imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('proom8rep'), Jump('proom8repeat2')) hovered tt.Action ("Say Hello [lv1]") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('proom8rep'), Jump('proom8repeat2')) hovered tt.Action ("Leave her alone [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('proom8rep'), Jump('proom8repeat3')) hovered tt.Action ("Stay and watch [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Edited Scene -----
label proom8repeat2:
    povi "I should leave her alone while she's changing."
    if momlove >= 30:
        povi "Well on second thought... maybe I'll say hello."
        scene parentsroom 8pm 008a
        mom "[pov]!"
        if inc == True:
            pov "Hi mom."
        else:
            pov "Hi [mother]."
        mom "Are you watch me change?"
        pov "No... Well yes... I mean I was about to leave..."
        scene parentsroom 8pm 009a
        mom "Haha, relax [pov]. I'm not mad."
        pov "Really? You do know I can see your boobs, right?"
        mom "I said I'm not mad. <giggle>"
        scene parentsroom 8pm 010a
        mom "What do you think about these stockings?"
        mom "Aren't they beautiful?"
        pov "Y... yes. And they look even better on your legs."
        mom "Oh, thank you [pov]."
        scene parentsroom 8pm 011a
        pov "Can I feel them?"
        mom "Huh?"
        pov "It's so soft and warm..."
        mom "[pov]!"
        pov "Huh?"
        if momlove >= 40:
            mom "Your hand... feels nice."
            "She turns around, your hand brush past her skin until it lands on her ass."
            scene parentsroom 8pm 011c
            mom "Hnnn... How does that feel?"
            pov "Wow, so soft but still really firm!"
            mom "Haha..."
            "She presses herself against your chest, pressing her ass into your crotch. You're embrace her, your arms wraping around her as your hands find her breasts."
            scene parentsroom 8pm 011d
            mom "<giggle> How about those?!"
            pov "..."
            mom "Cat got your tongue sweetie?"
            pov "Sorry, they are just... Awesome."
            mom "I'm glad!"
            "You feel her up for a while, before all too soon, she turns around to face you."
            scene parentsroom 8pm 012a
            mom "That was nice..."
            povi "Holy shit! That was amazing! She let be feel her up. No she practically invited me to feel her body."
            if inc == True:
                pov "Wow mom! That was amazing! But I didn't think..."
            else:
                pov "Wow [mother]! That was amazing! But I didn't think..."
            scene parentsroom 8pm 013a
            mom "It's alright [pov]. I liked it too. So what did you think about the stockings?"
            povi "Stockings?! Oh yeah, that's how this all started."
            if inc == True:
                pov "They are really soft, I like them a lot mom."
            else:
                pov "They are really soft, I like them a lot [mother]."
            mom "I was hoping you'd like them. Looks like I made the right choice."
            povi "What's with her today? Standing there half naked and letting me touch her? Not that I'm complaining."
            mom "[pov]? Are you alright?"
            jump proom8poster
        else:
            scene parentsroom 8pm 012a
            mom "Your hand..."
            if inc == True:
                pov "I'm sorry mom. I just wanted to feel it, I didn't think..."
            else:
                pov "I'm sorry [mother]. I just wanted to feel it, I didn't think..."
            scene parentsroom 8pm 013a
            mom "It's alright [pov]. Just warn me next time. I was just surprised was all."
            if inc == True:
                pov "Oh, okay, mom. They are really soft, I like them."
            else:
                pov "Oh, okay, [mother]. They are really soft, I like them."
            mom "I was hoping you'd like them. Looks like I made the right choice."
            povi "What's with her today? Standing there half naked and letting me touch her? Not that I'm complaining."
            mom "[pov]? Are you alright?"
        pov "Oh... yeah. I'll go now."
        mom "Thank you for helping me out."
    $ momlove += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

#----- Added label -----
label proom8poster:
    scene parentsroom 8pm 013a
    call screen proom8posterquestion

#----- Added screen -----
screen proom8posterquestion():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('proom8posterquestion'), Jump('proom8posterask')) hovered tt.Action ("Ask her about the poster") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('proom8posterquestion'), Jump('proom8posterleave')) hovered tt.Action ("Leave") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Added label -----
label proom8posterask:
    scene parentsroom 8pm 013a
    if inc == True:
        pov "Hey mom... can I ask you something?"
    else:
        pov "Hey [pov]... can I ask you something?"
    mom "Hmm... sure."
    pov "Are those pictures around the house with the woman in red..."
    pov "...really just pictures of you?"
    scene parentsroom 8pm 005
    mom "Oh... you think I look like her?"
    pov "Well we've gotten know know each other better since I have returned and..."
    pov "...well, yeah. I think that's you in those pictures."
    mom "Well sweetie... can you keep a secret?"
    if inc == True:
        pov "Did you seriously just ask me that Mom?"
        pov "Of course I can! Half my life is now secrets! Haha!"
        scene parentsroom 8pm 009a
        mom "True! Don't tell your father I told you this... but yes, those are pictures of me."
        pov "I knew it! Seriously mom, you could be a model! They are so sexy!"
    else:
        pov "Did you seriously just ask me that [pov]?"
        pov "Of course I can, half my life is now secrets! Haha!"
        scene parentsroom 8pm 009a
        mom "True! Don't tell Bruce I told you this... but yes, those are pictures of me."
        pov "I knew it! Seriously [pov], you could be a model! They are so sexy!"
    scene parentsroom 8pm 012a
    mom "You really think so?"
    pov "Of course I do! You look even better in person. You body is smokin hot!"
    pov "Why don't you turn around again for me?"
    scene parentsroom 8pm 010b
    mom "...like this?"
    pov "That's perfect!"
    scene parentsroom 8pm 011c
    pov "Seriously can't get enough of this ass!"
    mom "Hnnn..."
    "You slide your hand around and up to her breasts."
    scene parentsroom 8pm 011d
    "You press your body against her back and whisper in her ear."
    pov "I'm having a hard time not just ravishing you right now!"
    mom "Hnng... Hnnn..."
    "She presses her backside against your crotch as she moans."
    "You two grind against each other for a hot minute or so."
    povi "Wow, she seems interested in the idea!"
    "Suddenly she just stops for a momemnt, as if deep in thought."
    scene parentsroom 8pm 012d
    povi "Oh, I think I have her flustered a bit. She's just staring off into space."
    pov "...anyway."
    pov "That's exactly the kind of feelings a sexy model should envoke!"
    "She turns around to face you. Pulling herself back to here and now."
    scene parentsroom 8pm 013a
    mom "Well... I guess I did a good job then!"
    pov "That's for sure! Maybe one day you'll let me take a picture like just for me to have!"
    scene parentsroom 8pm 012a
    mom "I'd... like that... Hnnn..."
    pov "Cool, well I better let you finish."
    mom "...oh yeah. Getting dressed..."
    pov "See ya."
    scene parentsroom 8pm 013a
    mom "Bye sweetie."
    scene black
    povi "Maybe I should have made a move? Next time!"
    $ momlove += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

#----- Added label -----
label proom8posterleave:
    pov "Oh... yeah. I'll go now."
    mom "Thank you for helping me out."
    $ momlove += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

label proom8repeat3:
    povi "I'm going to watch her change some more."
    if inc == True:
        pov "Hi mom!"
    else:
        pov "Hi [mother]!"
    scene parentsroom 8pm 003
    mom "Eh?"
    mom "What are you doing here [pov]? You know that I'm changing!"
    pov "I know. I came to see you half-naked again!"
    scene parentsroom 8pm 004
    mom "..."
    pov "I need to see your hot body more often!"
    mom "Hmm..."
    if droom7momlookcor == True:
        scene parentsroom 8pm 007b
        pov "Good girl, you remembered."
        scene parentsroom 8pm 008b
        pov "You have such amazing tits you know!"
        pov "I need to play with them soon!"
        mom "But..."
        if gangmember == True:
            if inc == True:
                pov "No but's, mom! I'm a gang-member now, so I can do what I want to!"
            else:
                pov "No but's, [mother]! I'm a gang-member now, so I can do what I want to!"
            pov "So now I need you to turn around."
            mom "Turn around?"
            pov "Yes, turn around now!"
            scene parentsroom 8pm 010b
            povi "It's time to cash in on my gang-member status some more."
            call screen proom8chless
        else:
            pov "And remember, no complaints. Good girls enjoy their masters playing with them."
            mom "..."
        pov "They're already waiting for me!"
        mom "Hnn..."
    scene parentsroom 8pm 009b
    pov "It's too bad you're almost done changing, maybe I'll need to come by sooner next time!"
    mom "No you mustn't."
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    pov "We just talked about this. No more complaints! Say it!"
    mom "...No more complaints..."
    pov "Good slave."
    mom "Hnnn..."
    $ momcorruption += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

screen proom8chless():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom8chless'), Jump('proom8lesstits')) hovered tt.Action ("Grope her tits") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom8chless'), Jump('proom8lessass')) hovered tt.Action ("Grope her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom8chless'), Jump('proom8lessslap')) hovered tt.Action ("Slap her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom8lesstits:
    povi "She's get this in time."
    scene parentsroom 8pm 011d
    mom "Hah..."
    pov "I love your big, soft tits!"
    scene parentsroom 8pm 012d
    mom "Why are you doing this?"
    pov "Because I want to! You need to accept that I have claimed you now. You're mine."
    mom "Hnng..."
    pov "We'll have so much fun together."
    pov "I really do need to come by sooner next time! I need to see you nude."
    mom "No... you shouldn't..."
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    pov "We just talked about this. No more complaints! Say it!"
    mom "...No more complaints..."
    pov "Good slave."
    mom "Hnnn..."
    $ momcorruption += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

label proom8lessass:
    povi "She's get this in time."
    scene parentsroom 8pm 011c
    mom "Hah..."
    pov "I love your hot, firm ass!"
    scene parentsroom 8pm 012b
    mom "Why are you doing this?"
    pov "Because I want to! You need to accept that I have claimed you now. You're mine."
    mom "Hnng..."
    pov "We'll have so much fun together."
    pov "I really do need to come by sooner next time! I need to see you nude."
    mom "No... you shouldn't..."
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    pov "We just talked about this. No more complaints! Say it!"
    mom "...No more complaints..."
    pov "Good slave."
    mom "Hnnn..."
    $ momcorruption += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

label proom8lessslap:
    povi "She's get this in time."
    scene parentsroom 8pm 011b
    with vpunch
    mom "Hah..."
    pov "I love slapping that hot, firm ass!"
    scene parentsroom 8pm 012b
    mom "Why are you doing this?"
    pov "Because I want to! You need to accept that I have claimed you now. You're mine."
    mom "Hnng..."
    pov "We'll have so much fun together."
    pov "I really do need to come by sooner next time! I need to see you nude."
    mom "No... you shouldn't..."
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    pov "We just talked about this. No more complaints! Say it!"
    mom "...No more complaints..."
    pov "Good slave."
    mom "Hnnn..."
    $ momcorruption += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

label droom6pmrepeat:
    pov "Yeah! ...another dinner with sandwiches."
    if nicolereddresswear == True:
        scene diningroom 6pm 006ncc1
    elif nicolebabydollwear == True:
        scene diningroom 6pm 006ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 6pm 006ncl1
    elif nicolerobewear == True:
        scene diningroom 6pm 006ncl2
    else:
        scene diningroom 6pm 006
    "You eat dinner together and listen to the girls gossip."
    $ dtime += 1
    jump droom

label droom12pmrepeat:
    if nicolereddresswear == True:
        scene diningroom 12pm 003ncc1
    elif nicolebabydollwear == True:
        scene diningroom 12pm 003ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 12pm 003ncl1
    elif nicolerobewear == True:
        scene diningroom 12pm 003ncl2
    else:
        scene diningroom 12pm 003
    "You eat dinner together and listen to the girls gossip."
    "[ls] is still teasing you."
    if nicolereddress == 3 or nicolebabydoll == 3 or nicolesweaterpants == 3 or nicolerobe == 3:
        jump droom12pmclothreactions
    $ dtime += 1
    jump droom

label lroom15repeat:
    $ bigsisrelationship += 1
    $ irinarelationship += 1
    "You get closer to her."
    scene livingroom 3pm 003
    pov "Hey [irina]!"
    scene livingroom 3pm 004b
    irina "Oh, hello [pov]."
    if inc == True:
        pov "You're here to meet with my sister again?"
    else:
        pov "You're here to mee with [bs] again?"
    scene livingroom 3pm 006
    irina "Yes we were outside and now she's taking her time again."
    pov "Haha, I know."
    call screen lroom15repchoice

screen lroom15repchoice():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lroom15repchoice'), Jump('lroom15repirinalove')) hovered tt.Action ("Greet her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lroom15repchoice'), Jump('lroom15repirinacor')) hovered tt.Action ("Greet her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom15repirinalove:
    scene livingroom 3pm 002d
    $ irinalove += 1
    $ irinalroom15love = True
    pov "Looks like you need another hug. Come here!"
    irina "Again you're so nice to me."
    pov "Well, that's because I really like you."
    irina "Then just hold me tight."
    "You hold her a few moments longer."
    scene livingroom 3pm 003d
    irina "That was something I never want to miss."
    pov "Me too."
    irina "I still can't believe that you are so nice to me and not trying to get in my pants."
    pov "Haha, maybe I still want to get in there."
    irina "Maybe, but I like the way you do it slowly. <giggle>"
    scene livingroom 3pm 004d
    irina "And I'm also totally lost in the way you look at me."
    "She comes closer."
    pov "Then I'll look at you more."
    irina "I... can't... stop..."
    scene livingroom 3pm 005d
    irina "<kiss>"
    pov "Hm... what a nice surprise."
    irina "I'm glad you like it, hmm."
    irina "<kiss more>"
    scene livingroom 3pm 006d
    irina "That was so wonderful, we should continue this sometime."
    pov "Now?"
    irina "<giggle> Not now, [bs] would kill us and you know that."
    pov "You're worth it!"
    irina "Ohh... <giggle>"
    scene livingroom 3pm 010
    bs "Oh here you are again [pov]!"
    pov "Hmm, yes!"
    bs "Want to try your perverted things on her again?"
    jump lroom15repboth

label lroom15repirinacor:
    scene livingroom 3pm 002d
    $ irinacorruption += 1
    $ irinalroom15cor = True
    pov "Come here!"
    irina "Oh, so nice."
    pov "Then let's enjoy it more."
    scene livingroom 3pm 003c
    "You grope her ass."
    irina "Hnn...?"
    pov "That's a firm ass."
    irina "Hmm..."
    scene livingroom 3pm 004c
    pov "So you liked your hug?"
    irina "..."
    pov "I had to do it after you teased me with that hot ass in a short skirt."
    irina "Hnn..."
    pov "And while we are talking about teasing."
    scene livingroom 3pm 005c
    pov "That cleavage you're showing is another good reason why I chose you."
    irina "You... chose me..."
    pov "Yes, I'm sure I told you that before and you should stop teasing me like that."
    irina "Stop teasing...?"
    scene livingroom 3pm 005cb
    pov "Yes and the best way is to show me your tits now, so I don't have to fantasize about them any more."
    irina "You want me to show you my boobs right now?"
    pov "Right. Prove to me you're wortht of being my girl."
    irina "But [bs] will be coming any moment."
    pov "Oh I don't care about her, only about your tits at the moment."
    irina "Hmm... OK."
    scene livingroom 3pm 005cc
    pov "Oh, these are some hot tits, you should be glad!"
    irina "T... Thank you..."
    pov "I can't wait to lay my hands on them and play with them."
    irina "But... you... can't do it now."
    pov "Hm... we'll see."
    scene livingroom 3pm 005cd
    irina "Please... [bs] is coming."
    pov "Haha, OK. You're my good girl, you can get dressed again."
    irina "T... Thank you..."
    pov "I'll play with them another time."
    scene livingroom 3pm 010
    bs "Oh you're here again [pov]!"
    pov "Hmm, yes!"
    bs "Want to try your perverted things on her again?"
    jump lroom15repboth

label lroom15repboth:
    call screen lroom15repbothchoice

screen lroom15repbothchoice:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if irinalroom15love == True:
            imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lroom15repbothchoice'), Jump('lroom15repirinalove2')) hovered tt.Action ("Show her more love [lv1]/[irina]") focus_mask True
            imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lroom15repbothchoice'), Jump('lroom15repirinacor2')) hovered tt.Action ("Play with her [cr1]/[irina]") focus_mask True
        if irinalroom15cor == True:
            imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lroom15repbothchoice'), Jump('lroom15repirinalove2')) hovered tt.Action ("Show her some love [lv1]/[irina]") focus_mask True
            imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lroom15repbothchoice'), Jump('lroom15repirinacor2')) hovered tt.Action ("Play with her more [cr1]/[irina]") focus_mask True
        if d5love == True:
            imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lroom15repbothchoice'), Jump('lroom15repcaslove')) hovered tt.Action ("Go for her [lv1]/[bs]") focus_mask True
        if d5corruption == True:
            imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lroom15repbothchoice'), Jump('lroom15repcascor')) hovered tt.Action ("Have some fun with her [cr1]/[bs]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom15repirinalove2:
    scene livingroom 3pm 007d
    $ irinalove += 1
    pov "Yes, but I wouldn't call it perverted."
    irina "Hnn... <giggle>"
    pov "I wouldn't do such things to her."
    irina "More. <giggle>"
    scene livingroom 3pm 008d
    bs "What...?"
    irina "He's so sweet. Isn't he?"
    bs "Are you drunk? Letting him touch you like that?!"
    pov "Oh this isn't all."
    scene livingroom 3pm 009d
    bs "Wha...?"
    pov "<kiss>"
    irina "Hmm!"
    "[irina] is returning your kiss eagerly."
    pov "You waited for this, didn't you?"
    irina "Hmm... yes..."
    bs "..."
    scene livingroom 3pm 010d
    bs "You two are fucking crazy! I'm out of here!"
    pov "Calm down, I just had to do it."
    irina "<giggle>"
    bs "Idiots!"
    scene livingroom 3pm 011d
    irina "Haha, that was too much for her. But not for me, thank you for kissing me."
    pov "I couldn't withstand it, I had to kiss you and prove to her that we're good together."
    irina "I can't wait to prove that to her some more. <giggle>"
    if irinalroom15love == True:
        irina "I would love to stay here with you now and kiss some more, but I think I should go after her."
        irina "She does stupid things when she's angry and she's still my friend after all."
        pov "Yes, you should follow her, we'll have more time to know each other better."
        irina "Oh, I can't wait. See you later my gentleman."
        $ irinalroom15love = False
        $ lroom15extendfirst = True
        $ dtime += 1
        jump lroom
    else:
        irina "I was surprised when you suddenly kissed me like that after you were so demanding before."
        irina "But it was a very nice surprise and I would love to get more of that from you, but I think I should now go after her."
        irina "She does stupid things when she's angry and she's still my friend after all."
        pov "Yes, you should follow her and maybe I'll surprise you more often."
        irina "Oh, I can't wait. See you [pov]."
        $ irinalroom15cor = False
        $ lroom15extendfirst = True
        $ dtime += 1
        jump lroom

label lroom15repirinacor2:
    scene livingroom 3pm 006c
    $ irinacorruption += 1
    pov "Yes, maybe that's my plan."
    "You get closer to [irina]."
    irina "<giggle>"
    bs "What's going on here?"
    povi "Oh it seems [irina] likes it when she's charmed while [bs] around."
    scene livingroom 3pm 007c
    "You grope her secretly."
    irina "Hnn..."
    scene livingroom 3pm 008c
    irina "Hnn..."
    povi "Oh [irina] is lightly shaking. But I'm sure she'll do everything to prevent getting caught."
    bs "Just forget it [pov]. [irina] won't fell for your attempts. She isn't like the sluts you're always wishing for."
    pov "Oh, you're so sure about it?"
    irina "Hmm!"
    bs "Oh yes, I am!"
    povi "Time for more fun."
    scene livingroom 3pm 009c
    "You probe her asshole with your finger."
    povi "She's already mine, haha."
    scene livingroom 3pm 010c
    "Your finger enters her."
    irina "Aaah..."
    if irinalroom15love == True:
        "She's obviously shocked that you're taking advantage of her when you started out so nice."
        povi "Hah, I'm full of surprises."
    bs "What is it [irina]?"
    irina "Hnn..."
    scene livingroom 3pm 011c
    irina "I... I just bit my tongue."
    povi "A good answer, haha."
    bs "Everything alright, you look confused."
    irina "Yes, yes. Everything is alright."
    "You feel her asshole getting tight, so you let go of her."
    povi "No need to overdo it now. I made my point."
    bs "Come on we should go now and leave that looser so he can play with himself."
    povi "Oh that's not nice. But I'm not even mad, haha."
    irina "O... OK."
    "They leave and [irina] walks somewhat uncomfortably."
    $ irinalroom15cor = False
    $ irinalroom15love = False
    $ lroom15extendfirst = True
    $ dtime += 1
    jump lroom

label lroom15repcaslove:
    scene livingroom 3pm 006e
    $ bigsislove += 1
    "You move closer to [bs]."
    irina "Hah, you're still so mad at him?"
    bs "Of course, he's just a silly pervert."
    if cdate5bj == True or cdate5fuck == True or cdate5hj == True:
        povi "Wow, talking like that after we had so much fun at the mall."
    povi "I'll show her that she's wrong."
    scene livingroom 3pm 011b
    if inc == True:
        "You hug your sister."
    else:
        "You hug her."
    bs "Huh?"
    irina "Oh..."
    pov "<whisper> I want to talk to you alone."
    scene livingroom 3pm 003f
    irina "What's happening?"
    bs "Everything is alright, I think."
    if inc == True:
        bs "Can you go first? I need to talk to my brother."
    else:
        bs "Can you go first? I need to talk to [pov]."
    irina "Oh... sure."
    "[irina] leaves you."
    scene livingroom 3pm 004f
    bs "What's the problem, [pov]?"
    pov "I just wanted to see you alone."
    bs "Hm... for a special reason?"
    pov "I'm still thinking about what happened at the mall all the time."
    bs "I told you about that..."
    scene livingroom 3pm 005f
    pov "I know but I can't pretend anymore."
    bs "What? You can't..."
    pov "But when we're alone, I don't have to anymore."
    if inc == True:
        pov "I love you big sis."
    else:
        pov "I love you [bs]."
    scene livingroom 3pm 006f
    pov "<kiss>"
    bs "Oh... hah..."
    pov "I don't want wait anymore."
    bs "Don't S...stop... you're kissing me there."
    pov "Yes, I'm at the perfect spot. <kiss>"
    bs "Hah... but I told you..."
    pov "I know you love getting kissed."
    bs "Hah... [pov]."
    scene livingroom 3pm 007f
    bs "You... kissed me..."
    pov "Yes and I'll do it more and more until you admit that I'm a better boyfriend for you."
    bs "But... you won't stop even after I told you it was a mistake?"
    pov "No, I won't It wasn't a mistake. You loved it too."
    pov "It's a mistake that you want to stop just because of what others might think."
    scene livingroom 3pm 008f
    pov "You know that I'm right, just think about it some more."
    bs "Hmm..."
    pov "I'm willing to make it our secret if you'll be with me!"
    bs "Hmm..."
    pov "You won't find anyone that loves you like I have all my life. I won't abandon you."
    if inc == True:
        pov "You're my sister, we should stay together forever."
    else:
        pov "You're my childhood friend, we shgould stay together forever."
    bs "I want... I..."
    bs "You're confusing me very much right now."
    pov "But you'll think about it?"
    bs "Yes..."
    bs "I must go after [irina] now."
    "She leaves you."
    $ irinalroom15cor = False
    $ irinalroom15love = False
    $ lroom15extendcaslove = True
    $ dtime += 1
    jump lroom

label lroom15repcascor:
    scene livingroom 3pm 006e
    $ bigsiscorruption += 1
    "You move closer to [bs]."
    irina "Hah, you're still so mad at him?"
    bs "Of course, he's just a silly pervert."
    povi "Wow, talking like that after we had so much fun at the mall."
    povi "I'll teach her a lesson."
    scene livingroom 3pm 007e
    "You grope her secretly."
    bs "Huh?"
    scene livingroom 3pm 008e
    povi "Haha, she's looks so confused."
    irina "What's wrong [bs]?"
    bs "No... nothing, it's just..."
    if inc == True:
        povi "She won't fight back, she won't risk getting caught while her little brother gropes her ass so shamelessly."
    else:
        povi "She won't fight back, she won't risk getting caught while I grope her ass so shamelessly."
    povi "And especially not when I could tell her friend what we did together, haha."
    scene livingroom 3pm 009e
    irina "I'm talking to you [bs]!"
    bs "Oh, hnn..."
    "You knead her ass more."
    bs "Every... thing is alright. My thoughts just flew away."
    irina "Haha, you're really crazy sometimes."
    irina "Let's go?"
    scene livingroom 3pm 010e
    pov "You can go first [irina], I have to talk with [bs]."
    if inc == True:
        pov "Siblings-talk."
    bs "Hnn..."
    irina "You sure?"
    bs "Yes, go first. I'll come soon."
    irina "Haha, OK. See you [pov]."
    scene livingroom 3pm 011e
    bs "Are you fucking crazy? Groping me like that in front of my friend!"
    pov "Shhh... you better stop talking now."
    bs "What's wrong with you!"
    pov "Maybe I should tell [irina] what happened at the mall?"
    scene livingroom 3pm 012e
    bs "...no... you can't."
    pov "Oh you're learning fast. But don't worry, I wont do it."
    pov "Not until you're my girl!"
    bs "I can't be your girl."
    pov "Says the girl that loves to be dominated, even when her best friend is around."
    bs "I... I..."
    pov "Stop denying it. I already decided that I'm going to make you mine."
    bs "..."
    if inc == True:
        pov "We'll have a secret relationship as lovers, brother and sister lovers, just as it should be!"
    else:
        pov "We'll have a secret relationship as lovers, childhood friends and lovers, just as it should be!"
    bs "Hnn... I... have to go..."
    pov "Sure, but remember my words, lovers!"
    "She's leaves in a hurry. More than a little flustered."
    $ irinalroom15cor = False
    $ irinalroom15love = False
    $ lroom15extendcascor  = True
    $ dtime += 1
    jump lroom
