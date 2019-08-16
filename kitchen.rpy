#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 8am Kitchen - Alexis, MC - Love, Corruption
# 2. 9am Kitchen - Cassandra, MC - Love, Corruption
# 3. 11am Kitchen - MC, Nicole - Love, Corruption
# 4. 7pm Kitchen - Alexis, MC - Love, Corruption
# 5. 2am Kitchen - Bruce, Davide, MC, Nicole - Darker Paths
#----- End List -----

label kitchen8lsislookface:
    hide screen locations
    scene kitchen 8am 003
    if kitchen8am == True:
        jump kitchen8amrepeat1
    else:
        povi "She's so beautiful. Even when she's just smelling an orange."
        jump kitchen

label kitchen8lsislooktits:
    hide screen locations
    scene kitchen 8am 003a
    if kitchen8am == True:
        jump kitchen8amrepeat2
    else:
        povi "She's just wearing an old shirt that has grown too tight as she has developed."
        povi "Are her nipples stiff too?"
        jump kitchen

label kitchen8lsisscare:
    hide screen locations
    scene main 8am kitchen
    $ vkitchen8scare = True
    pov "Boo!"
    scene kitchen 8am 004
    ls "Waaah...?"
    pov "Hahaha..."
    scene kitchen 8am 005
    ls "Hmpf..."
    if lilsisrelationship < 40 and lilsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump alexisshakykitchen
        elif randomnum == 2:
            " "
    if kitchen8am == True:
        jump kitchen8amrepeat3
    else:
        scene kitchen 8am 005
        pov "Oh come on, it was funny."
        povi "Oh shit. Was it too much?"
        scene kitchen 8am 006
        ls "Haha, look at your face. You really thought that would make me angry!"
        pov "You think so?"
        jump kitchen8lsistalk

label kitchen8lsistalk:
    hide screen locations
    if vkitchen8scare == False:
        scene kitchen 8am 004a
        pov "Hey [ls]!"
        ls "Oh, hi [pov]!"
    if lilsisrelationship < 40 and lilsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump alexisshakykitchen
        elif randomnum == 2:
            " "
    if adatekiss == True and lilsislove >= 30:
        jump kitchen8kiss
    else:
        jump kitchen8lsistalk4

label kitchen8lsistalk4:
    scene kitchen 8am 006
    if kitchen8am == True:
        jump kitchen8amrepeat4
    ls "And, did you enjoyed your boring meeting with dad's friends?"
    $ vkitchen8lsistalknight = True
    $ lilsisrelationship += 1
    pov "Hmm it wasn't quite as boring as you think."
    ls "Sure, just keep thinking that. After hearing mom's stories about it, its gotta be the most boring thing ever."
    jump k8a1

label k8a1:
    call screen k8a1s

screen k8a1s():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('k8a1s'), Jump('kitchen8lsistalklove')) hovered tt.Action ("Answer to improve Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('k8a1s'), Jump('kitchen8lsistalkcor')) hovered tt.Action ("Answer to improve Corruption [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen8lsistalklove:
    if inc == True:
        pov "Yeah it was pretty boring. It's would be better to hang out with my annoying little sister more!"
    else:
        pov "Yeah it was pretty boring. It's would be better to hang out with my annoying friend more!"
    $ lilsislove += 1
    povi "It's better to keep her away from those assholes."
    scene kitchen 8am 007
    if inc == True:
        ls "Haha, you liar. I know you enjoy your time with the greatest little sister ever!"
    else:
        ls "Haha, you liar. I know you enjoy your time with the greatest girl ever!"
    pov "Riiight, are you on drugs?"
    ls "Hahahaha..."
    jump kitchen8lsistalk2

label kitchen8lsistalkcor:
    if inc == True:
        pov "Well, mom lied to you. It's probably the greatest party ever."
    else:
        pov "Well, your mom lied to you. It's probably the greatest party ever."
    $ lilsiscorruption += 1
    scene kitchen 8am 007b
    ls "What...?"
    pov "I don't know why she wouldn't want to have you there with us, but I'm sure you deserve it, haha."
    ls "But... I don't remember doing something wrong..."
    pov "Too bad. And I'm pretty sure she won't allow you there in the future too."
    ls "But... that's not fair!"
    if inc == True:
        pov "Haha, maybe your big brother can do something about. Maybe...!"
    else:
        pov "Haha, maybe I can do something about it. Maybe...!"
    jump kitchen8lsistalk2

label kitchen8lsistalk2:
    call screen k8a2s

screen k8a2s():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('k8a2s'), Jump('kitchen8lsistickle')) hovered tt.Action ("Tickle her [lv1] or [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('k8a2s'), Jump('kitchen8lsistalk3')) hovered tt.Action ("Don't tickle her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen8lsistickle:
    scene kitchen 8am 009
    $ vkitchen8lsistickle = True
    pov "Come here, hehehe..."
    ls "Aaahh..."
    if inc == True:
        pov "My naughty little sister needs her punishment, haha..."
    else:
        pov "My naughty little friend needs her punishment, haha..."
    ls "Hahahaha..."
    scene kitchen 8am 010
    ls "Stop it, I need to go to school soon."
    jump k8a3

label k8a3:
    call screen k8a3s

screen k8a3s():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" action (Hide('k8a3s'), Jump('kitchen8lsisrubass')) hovered tt.Action ("Tickle her more [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_love_%s.png" action (Hide('k8a3s'), Jump('kitchen8lsistalk3')) hovered tt.Action ("Stop it [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen8lsisrubass:
    pov "We're not done yet!"
    $ vkitchen8lsisrubass = True
    $ lilsiscorruption += 1
    ls "Huh?"
    scene kitchen 8am 011
    "You turn her around and rub your dick against her ass."
    ls "Hnn..."
    povi "I hope she can feel my boner."
    ls "What are you doing...?"
    pov "Just tickling you like adults do, hahaha..."
    ls "Hnn..."
    povi "I think I better not overdo it."
    jump kitchen8lsistalk3

label kitchen8lsistalk3:
    if vkitchen8lsisrubass == True:
        scene kitchen 8am 007c
        ls "Why did... you do that?"
        pov "I just tickled you like the grown up you want to be."
        ls "But you... you rubbed..."
        if inc == True:
            pov "And what's wrong with that? We were just fooling around. Like siblings do."
        else:
            pov "And what's wrong with that? We were just fooling around. Like childhood friends do."
        ls "Hnn..."
        pov "Or you are not as much of a grown up as I thought?"
        pov "You're not getting frightened right, haha?"
        scene kitchen 8am 008c
        ls "No! I'm not. I've grown up!"
        pov "Oh, is that so...?"
        ls "Yes, I just felt something there and I was surprised for a moment."
        povi "Good, she felt my boner."
        ls "I have to go to school now!"
        pov "Oh sure..."
        povi "Hehehe..."
        $ kitchen8am = True
        $ dtime = 9
        jump kitchen
    elif vkitchen8lsistickle == False:
        scene kitchen 8am 008
        ls "I have to go to school now!"
        pov "Okay, then see you later, \"little\" girl, haha."
        ls "You wish, looser, haha."
        $ kitchen8am = True
        $ dtime = 9
        jump kitchen
    else:
        scene kitchen 8am 008
        $ lilsislove += 1
        ls "Hahaha, that was fun. You got me there."
        pov "Yes it was. The \"bad\" girl needed her punishment alright, haha."
        pov "It's good that this part of you stayed childish."
        ls "I have to go to school now!"
        pov "Okay, then see you later, \"little\" girl, haha."
        ls "You wish, looser, haha."
        $ kitchen8am = True
        $ dtime = 9
        jump kitchen

label kitchen8kiss:
    scene kitchen 8am 005kiss
    if inc == True:
        ls "Come here, big brother."
    else:
        ls "Come here, [pov]."
    pov "Sure thing."
    povi "I'm getting a hug from her? What a nice surprise."
    scene kitchen 8am 006kiss
    ls "Muah!"
    povi "Wow!"
    "[ls] kisses you on the mouth."
    scene kitchen 8am 007kiss
    pov "What was that for?"
    ls "Nothing! I just wanted to do it."
    pov "Oh, thank you, I liked it."
    povi "Maybe our date went better than I thought?"
    $ lsiskiss += 1
    $ lilsislove += 1
    jump kitchen8lsistalk4

label kitchen9bsisscare:
    hide screen locations
    pov "Whaaaa...!"
    scene kitchen 9am 002
    bs "Hiiii...!"
    povi "Haha, oh shit..."
    scene kitchen 9am 003
    if bigsisrelationship < 30 and bigsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump cassandrashakykitchen
        elif randomnum == 2:
            " "
    bs "Aaah... It's all over me!"
    povi "Hahaha, who thought this would have happened?"
    povi "Shit that looks hot. I want to do that sometime... with my juice!"
    scene kitchen 9am 004
    bs "YOU!"
    bs "Look what you did you asshole. Scaring me so much!"
    pov "I... I thought there was someone outside..."
    bs "Liar! You did this on purpose!"
    pov "No?"
    bs "Grrr..."
    $ bigsisrelationship += 1
    $ bigsiscorruption += 1
    $ kitchen9meet = True
    jump k9s

label k9s:
    scene kitchen 9am 004
    call screen k9s1

screen k9s1():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('k9s1'), Jump('kitchen9bsissperm')) hovered tt.Action ("Say something kinky [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('k9s1'), Jump('kitchen9bsissorry')) hovered tt.Action ("Say sorry [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen9bsissperm:
    pov "It looks like someone came on you, hahaha."
    $ bigsiscorruption += 1
    scene kitchen 9am 005
    bs "You're so dead asshole. First you started this and now you're making bad jokes."
    pov "But it's true. Sticky, white stuff, hahaha..."
    bs "You wish it was yours, don't you? You pervert!"
    pov "Maybe, hahaha..."
    if bigsiscorruption > 30 or bigsislove > 30:
        bs "Hnnn..."
    pov "Not! What's wrong with you?"
    bs "Fuck you!"
    scene kitchen 9am 006
    bs "Now I have to go wash myself! And miss breakfast!"
    bs "You better not try to peek perv!"
    $ kitchen9mix = True
    $ kitchen9mixfirst = True
    $ dtime = 10
    jump kitchen

label kitchen9bsissorry:
    pov "I'm really sorry, [bs]! I didn't think that would happen."
    $ bigsislove += 1
    bs "Liar! You're still angry that I got made at you that time when we were kids!"
    pov "What? Are you serious? I was very young then."
    if inc == True:
        bs "And still a pervert! Wanking while watching your big sister!"
    else:
        bs "And you still a pervert! Wanking while watching your childhood friend!"
    pov "I was young and stupid then. It was all new to me."
    if bigsiscorruption > 30 or bigsislove > 30:
        bs "I guess..."
    else:
        bs "Grrr..."
    scene kitchen 9am 006
    bs "Look now I have to wash myself. And miss breakfast."
    bs "You better not try to peek perv!"
    $ kitchen9mix = True
    $ kitchen9mixfirst = True
    $ dtime = 10
    jump kitchen

label kitchen9bsiswait:
    hide screen locations
    scene kitchen 9am 002a
    $ bigsislove += 1
    $ bigsisrelationship += 1
    $ kitchen9meet = True
    povi "Oh she's drinking something, a smoothie or breakfast drink?"
    povi "Looks like she's taking care of herself well."
    scene kitchen 9am 003a
    if bigsisrelationship < 30 and bigsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump cassandrashakykitchen
        elif randomnum == 2:
            " "
    bs "Oh [pov], I didn't hear you coming."
    pov "Yeah I came a few seconds before and waited until you finished your drink."
    bs "Oh, it's my breakfast everyday. A health food drink that gives me vitamins and power for the day."
    pov "Ah, so you're on a healthy diet now?"
    bs "Yes."
    pov "Does that stuff taste good?"
    bs "Hmm... it's very good."
    scene kitchen 9am 004a
    bs "<gulp> <gulp>"
    povi "Damn, she's exercising too, just look at her abs."
    jump k9wl1


label k9wl2:
    scene kitchen 9am 005a
    bs "Wow... that was so good."
    povi "Should i tell her, haha?"
    jump k9sf

label k9sf:
    scene kitchen 9am 005a
    call screen k9sf1

screen k9sf1():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('k9sf1'), Jump('kitchen9bsisjoke')) hovered tt.Action ("Make a joke [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('k9sf1'), Jump('kitchen9bsisperv')) hovered tt.Action ("Say something kinky [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen9bsisjoke:
    pov "I'm ready to serve, mine führer!"
    $ bigsislove += 1
    bs "What...?"
    pov "Hahahaha..."
    bs "Oh..."
    scene kitchen 9am 006c
    bs "Hahaha..."
    pov "Not bad?"
    bs "Yes that one wasn't that bad, haha..."
    jump k9wl3

label kitchen9bsisperv:
    pov "A great update to your makeup. You should do that more often!"
    $ bigsiscorruption += 1
    bs "What do you mean?"
    pov "Something men like to do, haha."
    bs "Oh...!"
    scene kitchen 9am 006b
    bs "You're such a perverted idiot."
    pov "I'm just being honest, haha."
    bs "But you won't be getting to me that easily. My mood is too good now."
    pov "Must be all that gooey white stuff."
    jump k9wl3

label k9wl3:
    scene kitchen 9am 007
    bs "So look now that you're back we will be seeing much more of eachother."
    pov "Yes, haha..."
    bs "Just don't get on my nerves and we won't have any problems okay?"
    povi "Wow, for her that was actually kind of nice. Maybe there are drugs in her drink?"
    scene kitchen 9am 008
    bs "I have to do some training now. This body takes hard work."
    bs "I'll see you later."
    pov "Don't worry, I'll try not to bother you."
    bs "Good."
    $ kitchen9mix = False
    $ dtime = 10
    jump kitchen

label k9wl1:
    scene kitchen 9am 004a
    call screen k9wl

screen k9wl():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('k9wl'), Jump('kitchen9bsisface')) hovered tt.Action ("Look at face") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('k9wl'), Jump('kitchen9bsistits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('k9wl'), Jump('kitchen9bsiscrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('k9wl'), Jump('k9wl2')) hovered tt.Action ("Stop looking") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen9bsisface:
    scene kitchen 9am 003ac
    povi "Damn I want to give her something else white and sticky to drink!"
    hide kitchen 9am 003ac
    jump k9wl1

label kitchen9bsistits:
    scene kitchen 9am 003ab
    povi "They're so damn big. They are like all the porn star's breasts! I wouldn't mind trying a few of those things out with her..."
    jump k9wl1

label kitchen9bsiscrotch:
    scene kitchen 9am 003aa
    povi "What a sexy belly piercing! Her panties aren't hiding much either. Looks like she's shaves!"
    jump k9wl1

label kitchen11momslap:
    hide screen locations
    if vlroom8momslap >= 1:
        povi "Let's slap that ass again!"
    else:
        povi "Let's slap that ass!"
    if nicolereddresswear == True:
        scene kitchen 11am 002ancc1
    elif nicolebabydollwear == True:
        scene kitchen 11am 002ancc2
    elif nicolesweaterpantswear == True:
        scene kitchen 11am 002ancl1
    elif nicolerobewear == True:
        scene kitchen 11am 002ancl2
    else:
        scene kitchen 11am 002a
    with vpunch
    mom "Ahh..."
    if momrelationship < 30 and momntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            mom "Cut it out!"
            jump nicoleshakykitchen
        elif randomnum == 2:
            " "
    if vlroom8momslap >= 1:
        if nicolereddresswear == True:
            scene kitchen 11am 003ancc1
        elif nicolebabydollwear == True:
            scene kitchen 11am 003ancc2
        elif nicolesweaterpantswear == True:
            scene kitchen 11am 003ancl1
        elif nicolerobewear == True:
            scene kitchen 11am 003ancl2
        else:
            scene kitchen 11am 003a
        mom "Hnnn..."
        pov "You needed that, didn't you?"
        if momrelationship > 5 and momlove >= 50 or momrelationship > 5 and momcorruption >= 50:
            mom "Yes... maybe... you want to give a little squeeze too."
            "You squeeze ass hard massaging the flesh with your hand."
            if nicolereddresswear == True:
                scene kitchen 11am 003xncc1
            elif nicolebabydollwear == True:
                scene kitchen 11am 003xncc2
            elif nicolesweaterpantswear == True:
                scene kitchen 11am 003xncl1
            elif nicolerobewear == True:
                scene kitchen 11am 003xncl2
            else:
                scene kitchen 11am 003x
            mom "You call that a little squeeze dear?"
            pov "No, but I know you wanted that"
            if nicolereddresswear == True:
                scene kitchen 11am 003ancc1
            elif nicolebabydollwear == True:
                scene kitchen 11am 003ancc2
            elif nicolesweaterpantswear == True:
                scene kitchen 11am 003ancl1
            elif nicolerobewear == True:
                scene kitchen 11am 003ancl2
            else:
                scene kitchen 11am 003a
            mom "Yes... hnnn... feels nice..."
            "You play with her ass for a while longer before finally giving it one last squeeze and let go."
    else:
        if nicolereddresswear == True:
            scene kitchen 11am 003xncc1
        elif nicolebabydollwear == True:
            scene kitchen 11am 003xncc2
        elif nicolesweaterpantswear == True:
            scene kitchen 11am 003xncl1
        elif nicolerobewear == True:
            scene kitchen 11am 003xncl2
        else:
            scene kitchen 11am 003x
        mom "You slapped me! Are you insane?"
        pov "It needed to be done, I'm trying to play the bad boy remember?"
        mom "Oh... but do you need to slap me like that?"
        pov "Yes, especially when you're sticking your ass out like that. It's exactly what a bad boy would do!"
        if inc == True:
            mom "But I'm your mother!"
        else:
            mom "You can't do that to me!"
        pov "No, while in this play, you're just another bitch."
        mom "But..."
        pov "I'm just trying to play my part well."
        mom "..."
    $ momcorruption += 1
    $ vlroom8momslap += 1
    $ kitchen11momslap = True
    jump kitchen11momtalk

label kitchen11momtalk:
    hide screen locations
    $ momrelationship +=1
    if kitchen11momslap == True:
        if nicolereddresswear == True:
            scene kitchen 11am 002ncc1
        elif nicolebabydollwear == True:
            scene kitchen 11am 002ncc2
        elif nicolesweaterpantswear == True:
            scene kitchen 11am 002ncl1
        elif nicolerobewear == True:
            scene kitchen 11am 002ncl2
        else:
            scene kitchen 11am 002
        pov "And what are you making for dinner?"
        mom "I'm making some stew for dinner."
        if kitchen11am == True:
            jump kitchen11repeat
        pov "Stew huh?"
        mom "Yes, it's cheap and filling."
        pov "Okay... if you say so."
        povi "I don't really like stew much, ugh!"
        jump kitchen11help
    else:
        if nicolereddresswear == True:
            scene kitchen 11am 002ncc1
        elif nicolebabydollwear == True:
            scene kitchen 11am 002ncc2
        elif nicolesweaterpantswear == True:
            scene kitchen 11am 002ncl1
        elif nicolerobewear == True:
            scene kitchen 11am 002ncl2
        else:
            scene kitchen 11am 002
        if inc == True:
            pov "Hi mom."
        else:
            pov "Hi [mother]"
        if momrelationship < 30 and momntr == True:
            $ randomnum = renpy.random.randint(1,2)
            if randomnum == 1:
                jump nicoleshakykitchen
            elif randomnum == 2:
                " "
        mom "Oh hello [pov]."
        pov "What are you making for dinner?"
        mom "I'm making some stew for dinner."
        if kitchen11am == True:
            jump kitchen11repeat
        pov "Stew huh?"
        mom "Yes, it's cheap and filling."
        pov "Okay... if you say so."
        povi "I don't really like stew much, ugh!"
        jump kitchen11help

label kitchen11help:
    mom "Oh, can you help me with something?"
    scene kitchen 11am 004
    pov "Probably, what is it?"
    mom "Can you set the table? The dishes are over there."
    pov "Hmm..."
    scene kitchen 11am 006
    jump k11h

label k11h:
    scene kitchen 11am 006
    call screen k11h1

screen k11h1():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('k11h1'), Jump('kitchen11momhelp')) hovered tt.Action ("Help her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('k11h1'), Jump('kitchen11momnohelp')) hovered tt.Action ("Don't help her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen11momhelp:
    pov "Of course, I'll help you with that."
    scene kitchen 11am 007a
    mom "That's so nice of you, thank you."
    if inc == True:
        pov "It's okay mom. You work all day for us and you're making dinner too. It's the least I can do."
    else:
        pov "It's okay [mother]. You work all day for us and you're making dinner too. It's the least I can do."
    scene kitchen 11am 008a
    "You walk over and gather the dishes."
    scene black
    "Then you set the table."
    scene kitchen 11am 007a
    pov "I'm done mom."
    mom "It's good to have some real help around here."
    $ momlove += 1
    $ kitchen11am = True
    jump k11hu

label k11hu:
    scene kitchen 11am 007a
    call screen k11hu1

screen k11hu1():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_hug_%s.png" action (Hide('k11hu1'), Jump('kitchen11momhug')) hovered tt.Action ("Hug [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('k11hu1'), Jump('kitchen11momtalk2')) hovered tt.Action ("Don't hug") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen11momhug:
    if inc == True:
        pov "Come here mom!"
    else:
        pov "Come here [mother]!"
    scene kitchen 11am 009
    mom "Huh?"
    pov "Incoming hug..."
    scene kitchen 11am 010
    if vlroom8momhug == 0:
        mom "What is that for?"
        if inc == True:
            pov "I just want to hug my mom in the morning."
        else:
            pov "I just want to hug you in the morning."
        mom "That's so sweet, [pov]!"
    else:
        mom "Another hug?"
        if inc == True:
            pov "Yes mom."
        else:
            pov "Yes [mother]."
        mom "I could get used to that."
        pov "You better now that I'm home! Haha!"
    jump kitchen11momtalk2

label kitchen11momtalk2:
    scene kitchen 11am 006
    mom "Now I need to get lunch ready."
    pov "When is it?"
    mom "At noon. It would be nice if you can eat with us."
    $ momlove += 1
    $ dtime = 12
    jump kitchen

label kitchen11momnohelp:
    if inc == True:
        pov "No mom that's your job!"
    else:
        pov "No [mother] that's your job!"
    scene kitchen 11am 007b
    mom "But..."
    pov "It's women's work, so you should do it yourself. The men bring home the money, the women keep the home in order!"
    mom "Hmm... okay..."
    $ momcorruption += 1
    $ kitchen11am = True
    $ dtime = 12
    jump kitchen

label kitchen19talk:
    hide screen locations
    pov "Hey [ls]."
    scene kitchen 7pm 002c
    if lilsisrelationship < 40 and lilsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump alexisshakykitchen
        elif randomnum == 2:
            " "
    ls "Hi [pov]."
    pov "You're doing the dishes?"
    ls "Yeah, mom is busy."
    if proom19fuck == True:
        pov "I know."
    else:
        pov "Ah, where is she?"
    scene kitchen 7pm 003c
    if basement10pmnicoleouting == True: #----- Custom Reaction -----
        ls "Mom and dad are arguing."
        povi "Yeah and I know why too!"
        mom "[pov] is my lover... You're weak!"
        povi "Wow, [mother] isn't being quiet about us being together now. I wonder if she knows that [ls] can hear her?"
        scene kitchen 7pm 004c
        ls "Did mom just say you're her lover?!"
        pov "It's just the truth."
        pov "We're really close and care about each other a lot."
        ls "But isn't... isn't that wrong?"
        pov "I don't think so, we're both consenting adults, that's all that matters."
        if inc == True:
            pov "And mom really likes it!"
        else:
            pov "And [mother] really likes it!"
        scene kitchen 7pm 005c
        ls "This isn't something we should be discussing anyway."
        pov "Why not? We're just talking."
        if inc == True:
            ls "But I'm your sister."
        pov "Then again, you are pretty young, haha."
        ls "No I'm not..."
    else:
        ls "Mom and dad are making love."
        povi "Making love. How cute!"
        mom "Ahh... hah... hah..."
        pov "Oh I think they're fucking each other too hard to be calling \"making love\" though."
        scene kitchen 7pm 004c
        ls "Don't say that!"
        pov "Why not, it's just the truth."
        pov "It's totally normal that they just really go at it from time to time."
        ls "They make love every day at this time."
        pov "Oh, sounds like a decent sex life."
        mom "Ahh... harder... harder!"
        if inc == True:
            pov "And it seems that mom really likes it!"
        else:
            pov "And it seems that [mother] really likes it!"
        scene kitchen 7pm 005c
        ls "Don't! This isn't something we should be discussing anyway."
        pov "Why not? We're just talking."
        if inc == True:
            ls "But I'm your sister."
        pov "Then again, you are pretty young, haha."
        mom "Hmm... hah..."
        pov "At least she's enjoying it up there, haha."
        ls "..."
    $ lilsisrelationship += 1
    $ kitchen19 = True
    $ dtime += 1
    jump kitchen

label kitchen19closer:
    hide screen locations
    scene kitchen 7pm 002
    if inc == True:
        "You grab your sister from behind."
    else:
        "You grab her from behind."
    pov "Gotcha!"
    scene kitchen 7pm 003
    if lilsisrelationship < 40 and lilsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump alexisshakykitchen
        elif randomnum == 2:
            " "
    ls "Eh?"
    pov "It's really easy to sneak up on you, haha."
    scene kitchen 7pm 004
    ls "Oh, it's you, lazy bones!"
    ls "Hey! I'm working hard here. It's not easy being as awesome as I am 24/7 you know!"
    povi "Something else is starting to work hard too is seems."
    pov "Why are you doing the dishes?"
    scene kitchen 7pm 005
    ls "Mom is busy."
    if basement10pmnicoleouting == True: #----- Custom Reaction -----
        pov "Mother and I are fucking now you know?"
        ls "Yes..."
        pov "It feels so good, being inside her. Making her feel great too."
        ls "Hmm..."
        "You begin to rub your dick against her ass."
        pov "We really get into it. We just can't get enough."
        scene kitchen 7pm 006
        ls "Hmm..."
        pov "Don't you want to do that with me too?"
        "[ls] is pressing her ass into you now, you just don't know if it's because she likes it or is trying to get you to stop."
        ls "Ahh... hah... hmm..."
        pov "We could you know. Anytime you want to."
        ls "Hmm..."
    else:
        if proom19fuck == True:
            pov "They're fucking, you know?"
            ls "Yes..."
        else:
            pov "Where is she?"
            ls "Mom and dad are making love."
            povi "Making love. How cute!"
        mom "Ahh... hah... hah..."
        pov "Oh I think they're fucking each other too hard to be calling \"making love\" though."
        ls "Hmm..."
        "You begin to rub your dick against her ass."
        pov "They are really getting into it. Probably don't do often enough."
        scene kitchen 7pm 006
        ls "Hmm..."
        ls "Wait, no! They do this every day around this time."
        pov "Fucking like animals in heat?"
        "[ls] is pressing her ass into you now, you just don't know if it's because she likes it or is trying to get you to stop."
        mom "Ahh... hah... hmm..."
        pov "So you hear them fucking every day when you do the dishes?"
        ls "Hmm..."
    scene kitchen 7pm 007
    ls "[pov], you should probably stop that..."
    pov "What do you mean?"
    ls "I can feel your \"thing\" rubbing against me. It makes me feel... uncomfortable... kinda..."
    pov "Oh..."
    jump k19rub

label k19rub:
    call screen k19rub1

screen k19rub1():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('k19rub1'), Jump('kitchen19stop')) hovered tt.Action ("Stop [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('k19rub1'), Jump('kitchen19nostop')) hovered tt.Action ("Don't stop [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen19stop:
    scene kitchen 7pm 009a
    if basement10pmnicoleouting == True: #----- Custom Reaction -----
        pov "Oh, I'm so sorry [ls]. I got a bit too excited I guess."
    else:
        pov "Oh, I'm so sorry [ls]. The load moaning got me excited a bit I guess."
    ls "Yeah I could tell, dummy."
    pov "Anyway, I'm sorry about that."
    pov "I don't want to make you feel uncomfortable."
    pov "Let me make it up to you?"
    scene kitchen 7pm 010a
    ls "Eh?"
    if inc == True:
        pov "Let your big brother give you a hug."
    else:
        pov "Let me give you a hug."
    ls "Oh..."
    if inc == True:
        pov "No need to feel uncomfortable anymore. We're a family."
        scene kitchen 7pm 011a
        ls "Hmm... that feels so good brother."
    else:
        pov "No need to feel uncomfortable anymore. We're live together."
        scene kitchen 7pm 011a
        ls "Hmm... that feels so good [pov]."
    pov "Are you feeling better now?"
    pov "I don't want to do anything bad to you, or that you don't want me to."
    povi "Hopefully she doesnt feel the raging boner that is now against her stomach... Dude calm the fuck down..."
    ls "You're such a sweet dummy. <giggle>"
    scene kitchen 7pm 012a
    pov "Are we good still?"
    ls "Of course silly. You're like a wizard sometime you know, haha."
    ls "I magically feel so relaxed now."
    ls "I don't get many hugs lately."
    pov "Well, you should. It's good for the soul and it's an easy way to show that you care for someone. Hugs for everyone!"
    povi "Ok, now I'm the uncomfortable one. Did I just get dumped out from an afternoon kid's special here? Geez."
    ls "I'm sorry that I felt uncomfortable around you."
    pov "No need to. Everything is alright now, cutie."
    ls "Hahaha..."
    if adatekiss == True and lilsislove >= 30:
        jump kitchen19kiss
    else:
        jump kitchen19talk2

label kitchen19talk2:
    $ lilsisrelationship += 1
    $ lilsislove += 1
    $ kitchen19 = True
    $ dtime += 1
    jump kitchen

label kitchen19nostop:
    scene kitchen 7pm 008
    if basement10pmnicoleouting == True: #----- Custom Reaction -----
        pov "Thinking about us together got me excited. It happens when you grow up more."
        pov "Seems like you're feeling it too."
        "She's squirming against you more, but not enough to get away, just pressing her ass closer to you."
        ls "No... you're... hah... wrong."
        pov "We're just two consenting adults, nothing wrong with that right?"
        ls "Ohh... Hmm..."
        scene kitchen 7pm 010b
        pov "See? There is no reason we shouldn't enjoy themselves."
        ls "Hmm... hah..."
    else:
        pov "The loud moaning got me excited. It happens when you grow up more."
        pov "Seems like you're feeling it too."
        "She's squirming against you more, but not enough to get away, just pressing her ass closer to you."
        ls "No... you're... hah... wrong."
        pov "Let us just listen and enjoy the situation some more, nothing wrong with that right?"
        mom "Ohh... harder... please harder..."
        scene kitchen 7pm 010b
        pov "See? Why should they be the only ones enjoy themselves."
        ls "Hmm... hah..."
    if inc == True:
        "Your sister isn't protesting anymore and goes with your rhythm."
    else:
        "She isn't protesting anymore and goes with your rhythm."
    pov "Oh [ls] that feels real nice, do you feel it too?"
    ls "Hmm... hah... hah..."
    scene kitchen 7pm 009b
    if inc == True:
        ls "Yes... feels nice... Oh please brother, we should stop."
        pov "It's ok to feel good sis. Trust your brother, you won't regret it."
    else:
        ls "Yes... feels nice... Oh please [pov], we should stop."
        pov "It's ok to feel good [ls]. Trust me, you won't regret it."
    ls "Oh... hah... it's... hmm..."
    pov "I know you like it too, I can feel you grinding against me more."
    scene kitchen 7pm 011b
    ls "No we should stop this, we can't be doing this here!"
    pov "But why? You enjoying it too. You're even moaning."
    if inc == True:
        ls "I don't know, isn't it wrong? We're brother and sister. This sort of thing isn't allowed."
    else:
        ls "I don't know, isn't it wrong? We're living together. This sort of thing isn't allowed."
    povi "Hmm, interesting. She doesn't dislike it, she's just against it because it's forbidden."
    pov "Hey hey, it's alright. We didn't do anything wrong. It can be our secret if you want?"
    ls "Well, ok. That would be nice to be the one wth a secret for a change."
    pov "Ok then. It's our secret. See you tomorrow then?"
    ls "...yes..."
    $ lilsisrelationship += 1
    $ kitchen19 = True
    $ lilsiscorruption += 1
    $ dtime += 1
    jump kitchen

label kitchen19kiss:
    scene kitchen 7pm 012akiss
    if inc == True:
        ls "Come here, big brother."
    else:
        ls "Come here, [pov]."
    pov "Sure thing."
    povi "I'm getting a hug from her? What a nice surprise."
    scene kitchen 7pm 013akiss
    ls "Muah!"
    povi "Wow!"
    "[ls] kisses you on the mouth."
    scene kitchen 7pm 014akiss
    pov "What was that for?"
    ls "Nothing! I just wanted to do it."
    pov "Oh, thank you, I liked it."
    povi "Maybe our date went better than I thought?"
    $ lsiskiss += 1
    $ lilsislove += 1
    jump kitchen19talk2

label kitchen2am:
    hide screen locations
    $ dtime = 2
    scene black
    "After some time sleeping, you wake up."
    povi "What's that noise? Its coming from downstairs."
    jump kitchen2am2

label kitchen2am2:
    scene black
    call screen kitchen2am3

screen kitchen2am3():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('kitchen2am3'), Jump('kitchen2amntrchoice')) hovered tt.Action ("Check it out(Dark Paths)") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('kitchen2am3'), Jump('kitchen2am2sleep')) hovered tt.Action ("Go to sleep") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen2am2sleep:
    scene black
    pov "No, I don't care!"
    "You go to sleep again."
    if meet4am == True:
        $ dtime = 4
        scene black
        "You woke up."
        povi "It's 4am. I should meet with [ls]."
        jump base4amal
    elif hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard
    else:
        jump stats

label kitchen2amntrchoice:
    scene black
    call screen checkdarkerpaths_nicole
    if k2amntr == False:
        jump kitchen2am5
    else:
        jump kitchen2amrepeat

label kitchen2am5:
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    povi "Something going on down there, but it doesn't sound like the girls."
    povi "I don't think it's from the basement either, you can't hear anything from down there all the way up here."
    povi "Better go check it out..."
    "You walk downstairs."
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 001
        mom "Oh Davide, slow down! You're too big..."
    else:
        scene edited kitchen 2am 001cry
        mom "Please Davide, don't do this... I did what you asked..."
    davide "No! You need to get punished more! You're a very bad slut!"
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            mom "Oh my god! Yes, I'm... hah... a bad slut... hah..."
            povi "Wow! Their doing it up here too. What if they get caught?"
            if inc == True:
                povi "And where's dad? He needs to stop this!"
            else:
                povi "And where's Bruce? He needs to stop this!"
        else:
            mom "Oh my god! Yes, I'm... hah... a bad slut... hah..."
            povi "What? No! They're doing it here now too!"
            if inc == True:
                povi "And where's dad? He needs to stop this!"
            else:
                povi "And where's Bruce? He needs to stop this!"
    else:
        if nicole_revenge == True:
            mom "Fuck you Davide! Ho... Oww... hah..."
            povi "What? No! He's forcing her! What if the girls saw this, it would break their hearts."
            if inc == True:
                povi "And where's dad? He needs to stop this!"
            else:
                povi "And where's Bruce? He needs to stop this!"
        else:
            mom "Fuck you Davide! Ho... Oww... hah..."
            povi "Wow, raping her in her own kitchen... Can't say I blame him. She so fucking hot!"
            if inc == True:
                povi "And where's dad? I don't see him around."
            else:
                povi "And where's Bruce? I don't see him around."
    if nicole_voyeur == True or nicole_ntr == True:
        mom "You're tearing my ass apart... god... yes!"
        scene kitchen 2am 002
    else:
        mom "You're tearing my ass apart... please... stop..."
        scene edited kitchen 2am 002cry
    davide "Yes! And that's the way you love it. Getting pierced and being helpless!"
    mom "Hmm... hah... aaahhh..."
    davide "Your hot ass is made for my big dick!"
    davide "And you even can take all of it!"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "So... hah... deep..."
    else:
        mom "Too... hah... deep..."
    davide "I'm about to cum! Take every drop of my sperm in your ass!"
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            mom "Yes! Give it to me!"
            mom "Haaah... Aaahhh... so... hot..."
            povi "Yeah you dirty fucker! Do it!"
        else:
            mom "Yes! Give it to me!"
            mom "Haaah... Aaahhh... so... hot..."
            povi "Stop it Davide! Just stop!"
    else:
        if nicole_revenge == True:
            mom "Nooo! Get the fuck out of me!"
            mom "Haaah... Owww! Asshole!"
            povi "Nooo...!"
        else:
            mom "Nooo! Get the fuck out of me!"
            mom "Haaah... Owww! Asshole!"
            povi "Geez, she's all sorts of feisty tonight!"
    scene kitchen 2am 003
    mom "Hah... hah... hah..."
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            if inc == True:
                povi "That lucky bastard! Fucking my mom's fine ass and cumming so much in her. I want to be doing that!"
            else:
                povi "That lucky bastard! Fucking [mother]'s fine ass and cumming so much in her. I want to be doing that!"
            povi "And now he's grinning at me, celebrating his victory..."
        else:
            if inc == True:
                povi "That asshole! Fucking my mom's fine ass and cumming so much in her. And she wants it!"
            else:
                povi "That asshole! Fucking [mother]'s fine ass and cumming so much in her. And she wants it!"
            povi "And now he's grinning at me, celebrating his victory..."
    else:
        if nicole_revenge == True:
            if inc == True:
                povi "That asshole! Defiling my mom's ass and even cumming in her."
            else:
                povi "That asshole! Defiling [mother]'s ass and even cumming in her."
            povi "And now he's grinning at me, celebrating his victory..."
        else:
            if inc == True:
                povi "Wow, he's filling my mom's ass up."
            else:
                povi "Wow, he's filling her ass up."
            povi "And now he's grinning at me? Fuck dude, focus on that bitch in front of you..."
    davide "You liked that, slut?"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hah... hah... yes!"
        davide "You're not the only one!"
    else:
        mom "Hah... hah... no... never!"
        if inc == True:
            davide "Well I did! Oh, just so you know... I let your bitch ass son watch as well."
        else:
            davide "Well I did! Oh, just so you know... I let that bitch ass [pov] watch as well."
    mom "Wait..."
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 004
    else:
        scene edited kitchen 2am 004cry
    mom "Huh?"
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            if inc == True:
                povi "I can't believe it! Mom's enjoying getting fucked by this prick, what a slut!"
                mom "What's he doing here?"
                davide "He's enjoying seeing his mom getting fucked like a slut!"
                pov "That's just what I was thinking..."
                davide "So why are you here?"
            else:
                povi "I can't believe it! [mother]'s enjoying getting fucked by this prick, what a slut!"
                mom "What's he doing here?"
                davide "He's enjoying seeing you getting fucked like a slut!"
                pov "That's just what I was thinking..."
                davide "So why are you here?"
        else:
            if inc == True:
                povi "I can't believe it! Mom's enjoying getting fucked by this prick?"
                mom "What's he doing here?"
                davide "He's enjoying seeing his mom getting fucked like a slut!"
                pov "Maybe, maybe not..."
                davide "So why you here then?"
            else:
                povi "I can't believe it! [mother]'s enjoying getting fucked by this prick?"
                mom "What's he doing here?"
                davide "He's enjoying seeing you getting fucked like a slut!"
                pov "Maybe, maybe not..."
                davide "So why you here then?"
    else:
        if nicole_revenge == True:
            if inc == True:
                povi "I can't believe it! He's acting like Mom was enjoying getting fucked by him."
                mom "Why are you here son?!?"
                mom "You shouldn't have to see this!"
                davide "He's enjoying seeing his mom getting fucked like a slut!"
                pov "That's not true."
                davide "So why you here then?"
            else:
                povi "I can't believe it! He's acting like [mother] was enjoying getting fucked by him."
                mom "Why are you here [pov]?!?"
                mom "You shouldn't have to see this!"
                davide "He's enjoying seeing you getting fucked like a slut!"
                pov "That's not true."
                davide "So why you here then?"
        else:
            if inc == True:
                pov "Hey there! I have to say, I don't believe you either, seemed like you wanted it the whole time!"
                mom "Why are you here son?!?"
                mom "You shouldn't talk to me like that!"
                davide "He's enjoying seeing his mom getting fucked like a slut!"
                pov "That's true."
                davide "See I told you!"
            else:
                pov "Hey there! I have to say I don't believe you, seemed like you wanted it the whole time!"
                mom "Why are you here [pov]?!?"
                mom "You shouldn't talk to me like that!"
                davide "He's enjoying seeing you getting fucked like a slut!"
                pov "That's true."
                davide "See I told you!"
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 005
    else:
        scene edited kitchen 2am 005cry
    mom "That doesn't matter! You shouldn't be here!"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Sneaking in on us!"
    else:
        if nicole_revenge == True:
            "She's super pissed, but you see a flash of something in her eyes... what is she trying to tell you?"
        else:
            "She's pissed, but it is at you or herself?"
    if inc == True:
        davide "But he like to watch, just like his father, hahaha..."
    else:
        davide "But he likes to watch, just like Bruce, hahaha..."
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 006
        mom "But Bruce is allowed and he isn't."
        davide "Oh, I like your touch slut."
        mom "Maybe we should go for another round."
        mom "But let's go down in the basement."
        scene kitchen 2am 007
        if inc == True:
            davide "Now you'll get an even harder punishment for having such an idiotic son!"
            mom "Even harder...?"
            davide "You're body will be drowning in my sperm!"
            mom "Hmm..."
        else:
            davide "Now you'll get an even harder punishment for hosting such an idiot!"
            mom "Even harder...?"
            davide "You're body will be drowning in my sperm!"
            mom "Hmm..."
        mom "But he's not allowed to join us."
        if nicole_voyeur == True:
            povi "Nooo...! I wanted a turn!"
        else:
            povi "I don't want to join him!"
    else:
        if nicole_revenge == True:
            "Once more here eyes plead with you for just a moment. Asking for you to understand something."
            scene edited kitchen 2am 006cry
            mom "I don't want him to see this..."
            davide "Does it look like I give a fuck?"
            mom "If you promise to leave the girls alone like you said..."
            mom "...we can go down to the basement and continue this."
            scene edited kitchen 2am 007cry
            if inc == True:
                davide "Well, now you'll get an even harder punishment for having such an idiotic son!"
                mom "Even harder...?"
                davide "You're body will be drowning in my sperm!"
                mom "..."
            else:
                davide "Well, now you'll get an even harder punishment for hosting such an idiot!"
                mom "Even harder...?"
                davide "You're body will be drowning in my sperm!"
                mom "..."
            povi "Nooo...! That's it! She's trying to protect the girls. God damn Davide! I need to stop him!"
            mom "But please don't let him watch us..."
            davide "I can do that... But if you don't start acting like you want this dick, then I might have to just look for something better upstairs..."
            mom "No! I... I want your... your dick inside me..."
            povi "She's trying her best to make him believe it, but I can still see the pain in her eyes. She doesn't want this."
            davide "Better slut!"
        else:
            "Her eyes plead with you for just a moment. Maybe she wants you to help her..."
            povi "That's not likely, I might join in though."
            scene edited kitchen 2am 006cry
            mom "I don't want him to see this..."
            davide "Does it look like I give a fuck?"
            mom "If you promise to leave the girls alone like you said..."
            mom "...we can go down to the basement and continue this."
            scene edited kitchen 2am 007cry
            if inc == True:
                davide "Well, now you'll get an even harder punishment for having such an idiotic son!"
                mom "Even harder...?"
                davide "You're body will be drowning in my sperm!"
                mom "..."
            else:
                davide "Well, now you'll get an even harder punishment for hosting such an idiot!"
                mom "Even harder...?"
                davide "You're body will be drowning in my sperm!"
                mom "..."
            pov "Ah come on! I want to see that!"
            mom "Please don't let him watch us..."
            davide "I can do that... But if you don't start acting like you want this dick, then I might have to just look for something better upstairs..."
            mom "No! I... I want your... your dick inside me..."
            povi "That makes sense. if they aren't going to let me watch, I'll use the girls as leverage to fuck her later on my own."
            davide "Better slut!"
    if gangmember == True:
        pov "But I'm a gang member too..."
    else:
        pov "But..."
    if nicole_revenge == True:
        povi "I don't want her all alone with this bastard... what if he hurts her?!"
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 008
        if inc == True:
            davide "Sorry bro. As much I would like to show you how hard your mom needs to get pounded..."
        else:
            davide "Sorry bro. As much I would like to show you how hard [mother] needs to get pounded..."
        davide "If she says she doesn't want you there, then that's that."
        mom "And I'll make sure that you won't regret it."
        scene black
        if nicole_voyeur == True:
            povi "Who does she think she is, humiliating me like that? I'll show her!"
        else:
            povi "Damn it, why is she humiliating me like that?"
        "You go back to your bed."
        "Thinking about whether or not this was happening the whole time you were gone."
    else:
        if nicole_revenge == True:
            scene edited kitchen 2am 008cry
            if inc == True:
                davide "Sorry bro. As much I would like to show you how hard your mom needs to get pounded..."
            else:
                davide "Sorry bro. As much I would like to show you how hard [mother] needs to get pounded..."
            davide "If she says she doesn't want you there, then that's that."
            mom "..."
            scene black
            if inc == True:
                povi "Damn it, stop trying to protect me mom! You're the one that needs help!"
            else:
                povi "Damn it, stop trying to protect me [mother]! You're the one that needs help!"
            "You go back to your bed."
            "Thinking about a way to stop this once and for all!"
        else:
            scene edited kitchen 2am 008cry
            if inc == True:
                davide "Sorry bro. As much I would like to show you how hard your mom needs to get pounded..."
            else:
                davide "Sorry bro. As much I would like to show you how hard [mother] needs to get pounded..."
            davide "If she says she doesn't want you there, then that's that."
            mom "..."
            scene black
            povi "Damn it, I need to get that ass for myself. Davide keeps cramping my style."
            "You go back to your bed."
            "Thinking about ways to fuck her when you get your turn."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ k2amntr = True
    $ k2amon = True
    if meet4am == True:
        $ dtime = 4
        scene black
        "You woke up."
        povi "It's 4am. I should meet with [ls]."
        jump base4amal
    elif hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard
    else:
        jump stats

label kitchen2amrepeat:
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene black
    "You walk downstairs."
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 001
        mom "Oh Davide, slow down! You're too big..."
    else:
        scene edited kitchen 2am 001cry
        mom "Please Davide, don't do this... I did what you asked..."
    davide "No! You need to get punished more! You're a very bad slut!"
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            mom "Oh my god! Yes, I'm... hah... a bad slut... hah..."
            povi "Wow! Their doing it up here again. What if they get caught?"
        else:
            mom "Oh my god! Yes, I'm... hah... a bad slut... hah..."
            povi "What? No! They're doing it here again!"
    else:
        if nicole_revenge == True:
            mom "Fuck you Davide! Ho... Oww... hah..."
            povi "Again?! No! He's forcing her to do this again! This is just like last time!"
        else:
            mom "Fuck you Davide! Ho... Oww... hah..."
            povi "Again?! And I still didn't get an invite! That's cold"
    if inc == True:
        povi "And still no dad!"
    else:
        povi "And still no Bruce!"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "You're tearing my ass apart... god... yes!"
        scene kitchen 2am 002
    else:
        mom "You're tearing my ass apart... please... stop..."
        scene edited kitchen 2am 002cry
    davide "Yes! And that's the way you love it. Getting pierced and being helpless!"
    mom "Hmm... hah... aaahhh..."
    davide "Your hot ass is made for my big dick!"
    davide "And you even can take all of it!"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "So... hah... deep..."
    else:
        mom "Too... hah... deep..."
    davide "I'm about to cum! Take every drop of my sperm in your ass!"
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            mom "Yes! Give it to me!"
            mom "Haaah... Aaahhh... so... hot..."
            povi "Yeah you dirty fucker! Do it!"
        else:
            mom "Yes! Give it to me!"
            mom "Haaah... Aaahhh... so... hot..."
            povi "Stop it Davide! Just stop!"
    else:
        if nicole_revenge == True:
            mom "Nooo! Get the fuck out of me!"
            mom "Haaah... Owww! Asshole!"
            povi "Nooo...!"
        else:
            mom "Nooo! Get the fuck out of me!"
            mom "Haaah... Owww! Asshole!"
            povi "Geez, she's all sorts of feisty tonight!"
    scene kitchen 2am 003
    mom "Hah... hah... hah..."
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            if inc == True:
                povi "That lucky bastard! Fucking my mom's fine ass and cumming so much in her. I want to be doing that!"
            else:
                povi "That lucky bastard! Fucking [mother]'s fine ass and cumming so much in her. I want to be doing that!"
            povi "And now he's grinning at me, celebrating his victory..."
        else:
            if inc == True:
                povi "That asshole! Fucking my mom's fine ass and cumming so much in her. And she wants it!"
            else:
                povi "That asshole! Fucking [mother]'s fine ass and cumming so much in her. And she wants it!"
            povi "And now he's grinning at me, celebrating his victory..."
    else:
        if nicole_revenge == True:
            if inc == True:
                povi "That asshole! Defiling my mom's ass and even cumming in her."
            else:
                povi "That asshole! Defiling [mother]'s ass and even cumming in her."
            povi "And now he's grinning at me, celebrating his victory..."
        else:
            if inc == True:
                povi "Wow, he's filling my mom's ass up."
            else:
                povi "Wow, he's filling her ass up."
            povi "And now he's grinning at me? Fuck dude, focus on that bitch in front of you..."
    davide "You liked that, slut?"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hah... hah... yes!"
        davide "You're not the only one!"
    else:
        mom "Hah... hah... no... never!"
        if inc == True:
            davide "Well I did! Oh, just so you know... I let your bitch ass son watch as well."
        else:
            davide "Well I did! Oh, just so you know... I let that bitch ass [pov] watch as well."
    mom "Wait..."
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 004
    else:
        scene edited kitchen 2am 004cry
    mom "Huh?"
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            if inc == True:
                povi "I can't believe it! Mom's enjoying getting fucked by this prick, what a slut!"
                mom "What's he doing here?"
                davide "He's enjoying seeing his mom getting fucked like a slut!"
                pov "That's just what I was thinking..."
                davide "So why are you here?"
            else:
                povi "I can't believe it! [mother]'s enjoying getting fucked by this prick, what a slut!"
                mom "What's he doing here?"
                davide "He's enjoying seeing you getting fucked like a slut!"
                pov "That's just what I was thinking..."
                davide "So why are you here?"
        else:
            if inc == True:
                povi "I can't believe it! Mom's enjoying getting fucked by this prick?"
                mom "What's he doing here?"
                davide "He's enjoying seeing his mom getting fucked like a slut!"
                pov "Maybe, maybe not..."
                davide "So why you here then?"
            else:
                povi "I can't believe it! [mother]'s enjoying getting fucked by this prick?"
                mom "What's he doing here?"
                davide "He's enjoying seeing you getting fucked like a slut!"
                pov "Maybe, maybe not..."
                davide "So why you here then?"
    else:
        if nicole_revenge == True:
            if inc == True:
                povi "I can't believe it! He's acting like Mom was enjoying getting fucked by him."
                mom "Why are you here son?!?"
                mom "You shouldn't have to see this!"
                davide "He's enjoying seeing his mom getting fucked like a slut!"
                pov "That's not true."
                davide "So why you here then?"
            else:
                povi "I can't believe it! He's acting like [mother] was enjoying getting fucked by him."
                mom "Why are you here [pov]?!?"
                mom "You shouldn't have to see this!"
                davide "He's enjoying seeing you getting fucked like a slut!"
                pov "That's not true."
                davide "So why you here then?"
        else:
            if inc == True:
                pov "Hey there! I have to say, I don't believe you either, seemed like you wanted it the whole time!"
                mom "Why are you here son?!?"
                mom "You shouldn't talk to me like that!"
                davide "He's enjoying seeing his mom getting fucked like a slut!"
                pov "That's true."
                davide "See I told you!"
            else:
                pov "Hey there! I have to say I don't believe you, seemed like you wanted it the whole time!"
                mom "Why are you here [pov]?!?"
                mom "You shouldn't talk to me like that!"
                davide "He's enjoying seeing you getting fucked like a slut!"
                pov "That's true."
                davide "See I told you!"
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 005
    else:
        scene edited kitchen 2am 005cry
    mom "That doesn't matter! You shouldn't be here!"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Sneaking in on us!"
        if inc == True:
            davide "But he like to watch just like his father, hahaha..."
            mom "Speaking of him, where is he? BRUCE!"
            dad "Hmm...?"
            mom "Our son is spying on us again!"
            povi "Is he just in the other room, watching this?"
            pov "But..."
        else:
            davide "But he likes to watch just like Bruce, hahaha..."
            mom "Speaking of him, where is he? BRUCE!"
            dad "Hmm...?"
            mom "This pervert is spying on us again!"
            povi "Is he just in the other room, watching this?"
            pov "But..."
    else:
        if nicole_revenge == True:
            "She's super pissed, but you see a flash of something in her eyes... what is she trying to tell you?"
        else:
            "She's pissed, but it is at you or herself?"
        if inc == True:
            davide "But he like to watch just like his father, hahaha..."
            mom "I'm so sorry, Bruce! I know you don't..."
            dad "<sobs>"
            mom "Please just get out of here son!"
            povi "Is he just in the other room, watching this?"
            pov "But..."
        else:
            davide "But he likes to watch just like Bruce, hahaha..."
            mom "I'm so sorry, Bruce! I know you don't..."
            dad "<sobs>"
            mom "Please just get out of here [pov]!"
            povi "Is that little fucker just in the other room, watching this?"
            pov "But..."
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 006
        mom "But Bruce is allowed and he isn't."
        davide "Oh, I like your touch slut."
        mom "Maybe we should go for another round."
        mom "But let's go down in the basement."
        scene kitchen 2am 007
        if inc == True:
            davide "Now you'll get an even harder punishment for having such an idiotic son!"
            mom "Even harder...?"
            davide "You're body will be drowning in my sperm!"
            mom "Hmm..."
        else:
            davide "Now you'll get an even harder punishment for hosting such an idiot!"
            mom "Even harder...?"
            davide "You're body will be drowning in my sperm!"
            mom "Hmm..."
        mom "But he's not allowed to join."
        if nicole_voyeur == True:
            povi "Nooo...! I wanted a turn!"
        else:
            povi "I don't want to join him!"
    else:
        if nicole_revenge == True:
            "Once more here eyes plead with you for just a moment. Asking for you to understand something."
            scene edited kitchen 2am 006cry
            mom "I don't want him to see this..."
            davide "Does it look like I give a fuck?"
            mom "If you promise to leave the girls alone like you said..."
            mom "...we can go down to the basement and continue this."
            scene edited kitchen 2am 007cry
            if inc == True:
                davide "Well, now you'll get an even harder punishment for having such an idiotic son!"
                mom "Even harder...?"
                davide "You're body will be drowning in my sperm!"
                mom "..."
            else:
                davide "Well, now you'll get an even harder punishment for hosting such an idiot!"
                mom "Even harder...?"
                davide "You're body will be drowning in my sperm!"
                mom "..."
            povi "Nooo...! That's it! She's trying to protect the girls. God damn Davide! I need to stop him!"
            mom "But please don't let him watch us..."
            davide "I can do that... But if you don't start acting like you want this dick, then I might have to just look for something better upstairs..."
            mom "No! I... I want your... your dick inside me..."
            povi "She's trying her best to make him believe it, but I can still see the pain in her eyes. She doesn't want this."
            davide "Better slut!"
        else:
            "Her eyes plead with you for just a moment. Maybe she wants you to help her..."
            povi "That's not likely, I might join in though."
            scene edited kitchen 2am 006cry
            mom "I don't want him to see this..."
            davide "Does it look like I give a fuck?"
            mom "If you promise to leave the girls alone like you said..."
            mom "...we can go down to the basement and continue this."
            scene edited kitchen 2am 007cry
            if inc == True:
                davide "Well, now you'll get an even harder punishment for having such an idiotic son!"
                mom "Even harder...?"
                davide "You're body will be drowning in my sperm!"
                mom "..."
            else:
                davide "Well, now you'll get an even harder punishment for hosting such an idiot!"
                mom "Even harder...?"
                davide "You're body will be drowning in my sperm!"
                mom "..."
            pov "Ah come on! I want to see that!"
            mom "Please don't let him watch us..."
            davide "I can do that... But if you don't start acting like you want this dick, then I might have to just look for something better upstairs..."
            mom "No! I... I want your... your dick inside me..."
            povi "That makes sense. if they aren't going to let me watch, I'll use the girls as leverage to fuck her later on my own."
            davide "Better slut!"
    if gangmember == True:
        pov "But I'm a gang member too..."
    else:
        pov "But..."
    if nicole_ntr == True:
        povi "I don't want her all alone with this bastard... what if he hurts her?!"
    if nicole_voyeur == True or nicole_ntr == True:
        scene kitchen 2am 008
        if inc == True:
            davide "Sorry bro. As much I would like to show you how hard your mom needs to get pounded..."
        else:
            davide "Sorry bro. As much I would like to show you how hard [mother] needs to get pounded..."
        davide "But if she says she doesn't want you there, then that's that."
        mom "And I'll make sure that you won't regret it."
        scene black
        if nicole_voyeur == True:
            povi "Who does she think she is, humiliating me like that? I'll show her!"
        else:
            povi "Damn it, why is she humiliating me like that?"
        "You go back to your bed."
        "Thinking about whether or not this was happening the whole time you were gone."
    else:
        if nicole_revenge == True:
            scene edited kitchen 2am 008cry
            if inc == True:
                davide "Sorry bro. As much I would like to show you how hard your mom needs to get pounded..."
            else:
                davide "Sorry bro. As much I would like to show you how hard [mother] needs to get pounded..."
            davide "If she says she doesn't want you there, then that's that."
            mom "..."
            scene black
            if inc == True:
                povi "Damn it, stop trying to protect me mom! You're the one that needs help!"
            else:
                povi "Damn it, stop trying to protect me [mother]! You're the one that needs help!"
            "You go back to your bed."
            "Thinking about a way to stop this once and for all!"
        else:
            scene edited kitchen 2am 008cry
            if inc == True:
                davide "Sorry bro. As much I would like to show you how hard your mom needs to get pounded..."
            else:
                davide "Sorry bro. As much I would like to show you how hard [mother] needs to get pounded..."
            davide "If she says she doesn't want you there, then that's that."
            mom "..."
            scene black
            povi "Damn it, I need to get that ass for myself. Davide keeps cramping my style."
            "You go back to your bed."
            "Thinking about ways to fuck her when you get your turn."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ k2amntr = True
    $ k2amon = True
    if meet4am == True:
        $ dtime = 4
        scene black
        "You woke up."
        povi "It's 4am. I should meet with [ls]."
        jump base4amal
    elif hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard
    else:
        jump stats
