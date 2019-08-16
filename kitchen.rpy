




label kitchen8lsislookface:
    hide screen locations
    scene kitchen 8am 003
    if kitchen8am == True:
        jump kitchen8amrepeat1
    else:
        pov "{i}She's so beautiful. Even when she's smelling that orange.{/i}"
        jump kitchen

label kitchen8lsislooktits:
    hide screen locations
    scene kitchen 8am 003a
    if kitchen8am == True:
        jump kitchen8amrepeat2
    else:
        pov "{i}She's wearing her old shirt. But with her grown up tits it's a pleasure to view.{/i}"
        pov "{i}Are her nipples stiff too?{/i}"
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
        pov "{i}Oh shit. Was it too much?{/i}"
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
    pov "Hmm it wasn't as boring as you think."
    ls "Sure, just keep thinking that. After mom's stories it must be the most boring meetings ever."
    jump k8a1

label k8a1:
    call screen k8a1s

screen k8a1s():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 725 ypos 191 action (Hide('k8a1s'), Jump('kitchen8lsistalklove')) hovered tt.Action ("Answer to improve Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1169 ypos 191 action (Hide('k8a1s'), Jump('kitchen8lsistalkcor')) hovered tt.Action ("Answer to improve Corruption [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label kitchen8lsistalklove:
    if inc == True:
        pov "Yes, maybe. But it's better to stay all the time with my annoying little sister!"
    else:
        pov "Yes, maybe. But it's better to stay all the time with you!"
    $ lilsislove += 1
    pov "{i}It's better to keep her away from those assholes.{/i}"
    scene kitchen 8am 007
    if inc == True:
        ls "Haha, you liar. I know you enjoy the time with the greatest little sister ever!"
    else:
        ls "Haha, you liar. I know you enjoy the time with the greatest girl ever!"
    pov "Haha, are you on drugs?"
    ls "Hahahaha..."
    jump kitchen8lsistalk2

label kitchen8lsistalkcor:
    if inc == True:
        pov "Hahaha, mom lied to you. It's like the greatest party ever."
    else:
        pov "Hahaha, your mom lied to you. It's like the greatest party ever."
    $ lilsiscorruption += 1
    scene kitchen 8am 007b
    ls "What...?"
    pov "I don't know why she won't have you there with us, but I'm sure you deserve it, haha."
    ls "But... I don't remember doing something wrong..."
    pov "Too bad. And I'm sure she won't allow you in the future too."
    ls "But... that's not fair!"
    if inc == True:
        pov "Haha, maybe your big brother can do something. Maybe...!"
    else:
        pov "Haha, maybe I can do something. Maybe...!"
    jump kitchen8lsistalk2

label kitchen8lsistalk2:
    call screen k8a2s

screen k8a2s():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1169 ypos 191 action (Hide('k8a2s'), Jump('kitchen8lsistickle')) hovered tt.Action ("Tickle her [lv1] or [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 725 ypos 191 action (Hide('k8a2s'), Jump('kitchen8lsistalk3')) hovered tt.Action ("Don't tickle her") focus_mask True
        frame:
            xalign .5
            text tt.value

label kitchen8lsistickle:
    scene kitchen 8am 009
    $ vkitchen8lsistickle = True
    pov "Come here, hehehe..."
    ls "Aaahh..."
    if inc == True:
        pov "My bad sister needs her punishment, haha..."
    else:
        pov "You need your punishment, haha..."
    ls "Hahahaha..."
    scene kitchen 8am 010
    ls "Stop it, I need to go to school soon."
    jump k8a3


label k8a3:
    call screen k8a3s

screen k8a3s():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 1241 ypos 174 action (Hide('k8a3s'), Jump('kitchen8lsisrubass')) hovered tt.Action ("Tickle her more [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_love_%s.png" xpos 1286 ypos 300 action (Hide('k8a3s'), Jump('kitchen8lsistalk3')) hovered tt.Action ("Stop it [lv1]") focus_mask True
        frame:
            xalign .5
            text tt.value


label kitchen8lsisrubass:
    pov "We're not done yet!"
    $ vkitchen8lsisrubass = True
    $ lilsiscorruption += 1
    ls "Huh?"
    scene kitchen 8am 011
    "You move her around and rub your crotch on her ass."
    ls "Hnn..."
    pov "{i}I hope she's feeling my boner.{/i}"
    ls "What are you doing...?"
    pov "Just tickling you like adults do, hahaha..."
    ls "Hnn..."
    pov "{i}I think it's better if I don't overdo it.{/i}"
    jump kitchen8lsistalk3

label kitchen8lsistalk3:
    if vkitchen8lsisrubass == True:
        scene kitchen 8am 007c
        ls "Why did... you do that?"
        pov "I just tickled you like the grown up you want to be."
        ls "But you... you rub..."
        if inc == True:
            pov "And what's wrong with that? We just fooled around. Like siblings do."
        else:
            pov "And what's wrong with that? We just fooled around. Like childhood friends do."
        ls "Hnn..."
        pov "Or you aren't so much a grown up as I thought?"
        pov "Getting frightened, haha?"
        scene kitchen 8am 008c
        ls "No that's not true. I'm a big girl now."
        pov "Oh, is that so...?"
        ls "Yes, I just felt there was something and I was surprised for a moment."
        pov "{i}Good, she felt my boner.{/i}"
        ls "I have to go to school now!"
        pov "Oh sure..."
        pov "{i}Hehehe...{/i}"
        $ kitchen8am = True
        $ dtime = 9
        jump kitchen
    elif vkitchen8lsistickle == False:
        scene kitchen 8am 008
        ls "I have to go to school now!"
        pov "Okay, then see you later, number two, haha."
        ls "You wish, looser, haha."
        $ kitchen8am = True
        $ dtime = 9
        jump kitchen
    else:
        scene kitchen 8am 008
        $ lilsislove += 1
        ls "Hahaha, that was fun. You got me there."
        pov "Yes it was. The \"bad\" punishment, haha."
        pov "It's good that this part of you stayed childish."
        ls "I have to go to school now!"
        pov "Okay, then see you later, number two, haha."
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
    pov "Oh, what is it?"
    pov "{i}I'll get a hug from her? What a nice surprise?{/i}"
    scene kitchen 8am 006kiss
    ls "Muah!"
    pov "{i}Wow!{/i}"
    "[ls] kisses you on the mouth."
    scene kitchen 8am 007kiss
    pov "What was that for?"
    ls "Nothing! I just wanted to do it."
    pov "Oh, thank you, I liked it."
    pov "{i}Maybe my advice at the date motivated her?{/i}"
    $ lsiskiss += 1
    $ lilsislove += 1
    jump kitchen8lsistalk4



label kitchen9bsisscare:
    hide screen locations
    pov "Whaaaa...!"
    scene kitchen 9am 002
    bs "Hiiii...!"
    pov "{i}Haha, oh shit...{/i}"
    scene kitchen 9am 003
    if bigsisrelationship < 30 and bigsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump cassandrashakykitchen
        elif randomnum == 2:
            " "
    bs "Aaah... It's all over me!"
    pov "{i}Hahaha, who thought this could happen?{/i}"
    pov "{i}Shit this is hot. I want to do that sometime... with my juice!{/i}"
    scene kitchen 9am 004
    bs "YOU!"
    bs "Look what you did you asshole. Scaring me that much!"
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
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1289 ypos 273 action (Hide('k9s1'), Jump('kitchen9bsissperm')) hovered tt.Action ("Say something kinky [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 816 ypos 273 action (Hide('k9s1'), Jump('kitchen9bsissorry')) hovered tt.Action ("Say sorry [lv1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label kitchen9bsissperm:
    pov "It looks like someone came on you, hahaha."
    $ bigsiscorruption += 1
    scene kitchen 9am 005
    bs "You're so dead asshole. Getting me in this situation and then making your bad jokes."
    pov "But it's true. Sticky, slimy white stuff, hahaha..."
    bs "You wish it was yours, don't you? You pervert!"
    pov "Maybe, hahaha..."
    pov "No! What's wrong with you?"
    bs "Fuck you!"
    scene kitchen 9am 006
    bs "Now I have to wash myself! And no breakfast!"
    bs "Don't you dare come my way again!"
    $ kitchen9mix = True
    $ kitchen9mixfirst = True
    $ dtime = 10
    jump kitchen

label kitchen9bsissorry:
    pov "I'm really sorry, [bs]! I didn't think that would happen."
    $ bigsislove += 1
    bs "Liar! You're still angry that I denied you that time!"
    pov "What? Are you serious? I was very young then."
    if inc == True:
        bs "And still a pervert! Wank on your big sister!"
    else:
        bs "And you still a pervert! Wank on your childhood friend!"
    pov "I was young and stupid then. It was all new to me."
    bs "Grrr..."
    scene kitchen 9am 006
    bs "Now I have to wash myself! And no breakfast!"
    bs "Don't you dare come my way again!"
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
    pov "{i}Oh she's drinking something, a smoothie or breakfast drink?{/i}"
    pov "{i}No wonder she's in such good shape.{/i}"
    scene kitchen 9am 003a
    if bigsisrelationship < 30 and bigsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump cassandrashakykitchen
        elif randomnum == 2:
            " "
    bs "Oh [pov], I didn't hear you coming."
    pov "Yeah I came a few seconds before and waited until you finished your drink."
    bs "Oh, it's my breakfast everyday. A vegan energy drink that gives me vitamins and power for the day."
    pov "Ah, so your on a healthy diet now?"
    bs "Yes."
    pov "Does that stuff taste good?"
    bs "Hmm... it's very good."
    scene kitchen 9am 004a
    bs "<gulp> <gulp>"
    pov "{i}Damn she's really in good shape. And getting abs.{/i}"
    jump k9wl1


label k9wl2:
    scene kitchen 9am 005a
    bs "Wow... that was so good."
    pov "{i}Should i tell her, haha?{/i}"
    jump k9sf

label k9sf:
    scene kitchen 9am 005a
    call screen k9sf1

screen k9sf1():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 684 ypos 273 action (Hide('k9sf1'), Jump('kitchen9bsisjoke')) hovered tt.Action ("Make a joke [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1131 ypos 273 action (Hide('k9sf1'), Jump('kitchen9bsisperv')) hovered tt.Action ("Say something kinky [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label kitchen9bsisjoke:
    pov "I'm ready to serve you, my führer!"
    $ bigsislove += 1
    bs "What...?"
    pov "Hahahaha..."
    bs "Oh...?"
    scene kitchen 9am 006c
    bs "Hahaha..."
    pov "Not bad?"
    bs "Yes that one wasn't that bad, haha..."
    jump k9wl3

label kitchen9bsisperv:
    pov "A great update on your makeup. You should do that more often!"
    $ bigsiscorruption += 1
    bs "What do you mean?"
    pov "Something men like to do, haha."
    bs "Oh...!"
    scene kitchen 9am 006b
    bs "You're such a perverted idiot."
    pov "I'm just honest, haha."
    bs "But you won't get me. My mood is to good now."
    pov "That must be that good white stuff."
    jump k9wl3

label k9wl3:
    scene kitchen 9am 007
    bs "So you're back now and I have to bear you from now on."
    pov "Yes, haha..."
    bs "Don't get on my nerves and we won't have any problems together."
    pov "{i}Wow, for her she's really nice. Maybe there are drugs in her drink?{/i}"
    scene kitchen 9am 008
    bs "I have to do some training now. This body was hard work."
    bs "So stop annoying me."
    pov "Don't worry, I have better things to do."
    bs "Good."
    $ kitchen9mix = False
    $ dtime = 10
    jump kitchen


label k9wl1:
    scene kitchen 9am 004a
    call screen k9wl        

screen k9wl():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 759 ypos 233 action (Hide('k9wl'), Jump('kitchen9bsisface')) hovered tt.Action ("Look at face") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1098 ypos 507 action (Hide('k9wl'), Jump('kitchen9bsistits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1163 ypos 771 action (Hide('k9wl'), Jump('kitchen9bsiscrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1175 ypos 233 action (Hide('k9wl'), Jump('k9wl2')) hovered tt.Action ("Stop looking") focus_mask True
        frame:
            xalign .5
            text tt.value


label kitchen9bsisface:
    scene kitchen 9am 003ac
    pov "{i}Damn I want to give her something else white and sticky to drink!{/i}"
    hide kitchen 9am 003ac
    jump k9wl1

label kitchen9bsistits:
    scene kitchen 9am 003ab
    pov "{i}They're so damn big. I want to grope them and play with my dick on them!{/i}"
    jump k9wl1

label kitchen9bsiscrotch:
    scene kitchen 9am 003aa
    pov "{i}What a nice belly piercing! And her panties aren't hiding much. Looks like she's shaved!{/i}"
    jump k9wl1





label kitchen11momslap:
    hide screen locations
    if vlroom8momslap >= 1:
        pov "{i}Let's slap that ass again!{/i}"
    else:
        pov "{i}Let's slap that ass!{/i}"
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
        pov "It had to be done. I'm trying to play the bad ass."
        mom "Oh... but is there a need for you to slap me?"
        pov "Yes when your sticking your ass out like that I slap it like a bad boy would do!"
        if inc == True:
            mom "But I'm your mother!"
        else:
            mom "You can't do that to me!"
        pov "No, in this bad play you're just another bitch."
        mom "But..."
        pov "I'm just trying to play my role well."
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
        mom "I'll make some boiled dinner."
        if kitchen11am == True:
            jump kitchen11repeat
        pov "Boiled dinner?"
        mom "Yes, it's cheap to make and makes us sated."
        pov "Okay..."
        pov "{i}Damn, boiled dinner, ugh!{/i}"
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
        mom "I'll make some boiled dinner."
        if kitchen11am == True:
            jump kitchen11repeat
        pov "Boiled dinner?"
        mom "Yes, it's cheap to make and makes us sated."
        pov "Okay..."
        pov "{i}Damn, boiled dinner, ugh!{/i}"
        jump kitchen11help

label kitchen11help:
    mom "Oh can you help me with something?"
    scene kitchen 11am 004
    pov "Maybe, what is it?"
    mom "Can you set the table? The dishes are over there."
    pov "Hmm..."
    scene kitchen 11am 006
    jump k11h

label k11h:
    scene kitchen 11am 006
    call screen k11h1

screen k11h1():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 992 ypos 146 action (Hide('k11h1'), Jump('kitchen11momhelp')) hovered tt.Action ("Help her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1028 ypos 306 action (Hide('k11h1'), Jump('kitchen11momnohelp')) hovered tt.Action ("Don't help her [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label kitchen11momhelp:
    pov "Yes, I'll help you for sure."
    scene kitchen 11am 007a
    mom "That's so nice from you, thank you."
    if inc == True:
        pov "It's okay mom. You work all day for us and you make the dinner too."
    else:
        pov "It's okay [mother]. You work all day for us and you make the dinner too."
    scene kitchen 11am 008a
    "You walk over and take the dishes."
    scene black
    "Then you set the table."
    scene kitchen 11am 007a
    pov "I'm done mom."
    mom "It's good I have some help."
    $ momlove += 1
    $ kitchen11am = True
    jump k11hu

label k11hu:
    scene kitchen 11am 007a
    call screen k11hu1

screen k11hu1():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_hug_%s.png" xpos 992 ypos 146 action (Hide('k11hu1'), Jump('kitchen11momhug')) hovered tt.Action ("Hug [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1028 ypos 306 action (Hide('k11hu1'), Jump('kitchen11momtalk2')) hovered tt.Action ("Don't hug") focus_mask True
        frame:
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
    jump kitchen11momtalk2

label kitchen11momtalk2:
    scene kitchen 11am 006
    mom "Now I need to get dinner ready."
    pov "{i}What time for it?{/i}"
    mom "At 12pm. It would be nice if you eat with us."
    $ momlove += 1
    $ dtime = 12
    jump kitchen

label kitchen11momnohelp:
    if inc == True:
        pov "No mom this is your job!"
    else:
        pov "No [mother] this is your job!"
    scene kitchen 11am 007b
    mom "But..."
    pov "It's women's work, so you'll do it yourself. The men bring the money, the women do the house!"
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
    ls "Yes, mom is busy."
    if proom19fuck == True:
        pov "I know."
    else:
        pov "Ah, where is she?"
    scene kitchen 7pm 003c
    ls "Mom and dad are making love."
    pov "{i}Making love. How cute!{/i}"
    mom "Ahh... hah... hah..."
    pov "Oh I think they're fucking rather hard together."
    scene kitchen 7pm 004c
    ls "Don't say such things!"
    pov "Why not, it's just the truth."
    pov "It's totally normal that they have sex from time to time."
    ls "They make love every day at this time."
    pov "Oh, so they must have a good sex life."
    mom "Ahh... harder... harder!"
    if inc == True:
        pov "And it seems that mom really likes it!"
    else:
        pov "And it seems that [mother] really likes it!"
    scene kitchen 7pm 005c
    ls "Don't! This is not something we should discuss."
    pov "Why not? We're just talking."
    if inc == True:
        ls "But I'm your sister."
    pov "Just not grown up enough, haha."
    mom "Hmm... hah..."
    pov "Maybe you should enjoy your mom's moaning a lot more, haha."
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
    ls "Oh, it's you, stupid!"
    ls "I work hard here so it's not a performance you could do."
    pov "{i}Hard is something else now too.{/i}"
    pov "Why are you doing the dishes?"
    scene kitchen 7pm 005
    ls "Mom is busy."
    if proom19fuck == True:
        pov "They're fucking, you know?"
        ls "Yes..."
    else:
        pov "Where is she?"
        ls "Mom and dad are making love."
        pov "{i}Making love. How cute!{/i}"
    mom "Ahh... hah... hah..."
    pov "Oh I think they're fucking rather hard together."
    ls "Hmm..."
    "You begin to rub your dick on her ass."
    pov "They don't fuck together often?"
    scene kitchen 7pm 006
    ls "Hmm..."
    ls "No! They do this every day at this time."
    pov "Fucking so hard together?"
    "[ls] is trying to press you away with her ass."
    mom "Ahh... hah... hmm..."
    pov "So you hear them fucking every day when you do the dishes?"
    ls "Hmm..."
    scene kitchen 7pm 007
    if inc == True:
        ls "Brother please stop it."
    else:
        ls "Please stop it."
    pov "What do you mean?"
    ls "I can feel your thing rubbing on me. It makes me feel uncomfortable."
    pov "Oh..."
    jump k19rub

label k19rub:
    call screen k19rub1

screen k19rub1():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 515 ypos 365 action (Hide('k19rub1'), Jump('kitchen19stop')) hovered tt.Action ("Stop [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1151 ypos 90 action (Hide('k19rub1'), Jump('kitchen19nostop')) hovered tt.Action ("Don't stop [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label kitchen19stop:
    scene kitchen 7pm 009a
    pov "Oh, I'm so sorry [ls]. The load moaning carried me away."
    ls "I could feel your thing rubbing on me."
    pov "As I said I'm sorry about that, I don't want to make you feel uncomfortable."
    pov "But I have an idea to calm you down."
    scene kitchen 7pm 010a
    ls "Eh?"
    if inc == True:
        pov "Just relax and let your big brother hug you."
    else:
        pov "Just relax and let me hug you."
    ls "What...?"
    if inc == True:
        pov "No need to feel uncomfortable anymore. We're a family."
        scene kitchen 7pm 011a
        ls "Hmm... that feels so good brother."
    else:
        pov "No need to feel uncomfortable anymore. We live together."
        scene kitchen 7pm 011a
        ls "Hmm... that feels so good [pov]."
    pov "See, you calmed down in a few seconds."
    pov "I won't do anything bad to you. And a good hug can show that."
    pov "{i}But I have still a raging boner.{/i}"
    ls "You're such a sweet dummy. <giggle>"
    scene kitchen 7pm 012a
    pov "Better now?"
    ls "You're like a wizard, haha."
    ls "I feel so relaxed now. I don't get many hugs lately."
    pov "Yes but you should. It helps to relax and it's something you do when you live together."
    ls "I'm sorry that I felt uncomfortable around you."
    pov "No need to. Everything is alright now, cute little dummy."
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
    pov "It's because they moan so loud. It happens automatically to me."
    pov "And I can feel that you're affected to as any young adult."
    ls "No... you're... hah... wrong."
    pov "Let us just listen more and enjoy our nature."
    mom "Ohh... harder... please harder..."
    scene kitchen 7pm 010b
    pov "See? Why should only they enjoy it."
    ls "Hmm... hah..."
    if inc == True:
        "Your sister doesn't fight anymore and goes with your rhythm."
    else:
        "She doesn't fight anymore and goes with your rhythm."
    pov "Good, just relax."
    ls "Hmm... hah... hah..."
    scene kitchen 7pm 009b
    if inc == True:
        ls "No please brother, we have to stop this."
        pov "You're just afraid because it feels good. Trust your brother, you won't regret it."
    else:
        ls "No please, we have to stop this."
        pov "You're just afraid because it feels good. Trust me, you won't regret it."
    ls "No... hah... it's... hmm..."
    pov "I know you like it too, your movements tell me."
    scene kitchen 7pm 011b
    ls "No we have to stop this, we can't do this!"
    pov "But why? You enjoyed it too. You're even moaning."
    if inc == True:
        ls "No, it's wrong. We're brother and sister. This isn't allowed."
    else:
        ls "No, it's wrong. We're living so long together. This isn't allowed."
    pov "{i}Hmm, interesting. She didn't dislike it, she's just against it because it's forbidden.{/i}"
    pov "Relax. I understand your point."
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
    pov "Oh, what is it?"
    pov "{i}I'll get a hug from her? What a nice surprise?{/i}"
    scene kitchen 7pm 013akiss
    ls "Muah!"
    pov "{i}Wow!{/i}"
    "[ls] kisses you on the mouth."
    scene kitchen 7pm 014akiss
    pov "What was that for?"
    ls "Nothing! I just wanted to do it."
    pov "Oh, thank you, I liked it."
    pov "{i}Maybe my advice at the date motivated her?{/i}"
    $ lsiskiss += 1
    $ lilsislove += 1
    jump kitchen19talk2



label kitchen2am:
    hide screen locations
    $ dtime = 2
    scene black
    "After some time you wake up."
    pov "{i}What's that noise? It coming from downstairs.{/i}"
    jump kitchen2am2


label kitchen2am4:
    if k2amntr == False:
        jump kitchen2am5
    else:
        jump kitchen2amrepeat

label kitchen2am5:
    pov "{i}Something must happen there, but it couldn't be the others. I shouldn't hear anything from the basement.{/i}"
    pov "{i}Better check it!{/i}"
    "You walk downstairs."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene kitchen 2am 001
    mom "Oh Davide, slow down! You're too big..."
    davide "No! You need to get punished more! You're a very bad slut!"
    mom "Oh my god! Yes, I'm... hah... a bad slut... hah..."
    pov "{i}What? No! They're even doing it here!{/i}"
    if inc == True:
        pov "{i}And where's dad? He needs to stop this!{/i}"
    else:
        pov "{i}And where's Bruce? He needs to stop this!{/i}"
    mom "You're tearing my ass apart..."
    scene kitchen 2am 002
    davide "Yes! And that's the way you love it. Getting pierced helpless!"
    mom "Hmm... hah... aaahhh..."
    davide "Your hot ass is made for my big dick!"
    davide "And you even can take all of it!"
    mom "So... hah... deep..."
    davide "I'm about to cum! Take every drop of my sperm in your ass!"
    mom "Yes! Give it to me!"
    mom "Haaah... Aaahhh... so... hot..."
    pov "{i}Nooo...!{/i}"
    scene kitchen 2am 003
    mom "Hah... hah... hah..."
    if inc == True:
        pov "{i}That asshole! Defiling my mom's ass and cumming so much in her.{/i}"
    else:
        pov "{i}That asshole! Defiling [mother]'s ass and cumming so much in her.{/i}"
    pov "{i}And now he's grinning at me, celebrating his win over me!{/i}"
    davide "You liked that, slut?"
    mom "Hah... hah... yes!"
    davide "You're not the only one!"
    mom "Wait..."
    scene kitchen 2am 004
    mom "Huh?"
    if inc == True:
        pov "{i}I can't believe it! Mom's enjoying getting fucked by this prick?{/i}"
        mom "What is he doing here?"
        davide "He's enjoying seeing his mom getting fucked like a slut!"
    else:
        pov "{i}I can't believe it! [mother]'s enjoying getting fucked by this prick?{/i}"
        mom "What's he doing here?"
        davide "He's enjoying seeing you getting fucked like a slut!"
    pov "That's not true."
    davide "So why you here then?"
    scene kitchen 2am 005
    mom "That doesn't matter! You shouldn't be here!"
    mom "Sneaking in on us!"
    if inc == True:
        davide "But he like to watch like his father, hahaha..."
    else:
        davide "But he likes to watch like Bruce, hahaha..."
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
    pov "{i}Nooo...!{/i}"
    mom "But he's not allowed to join."
    if gangmember == True:
        pov "But I'm a gang member too."
    else:
        pov "But..."
    scene kitchen 2am 008
    if inc == True:
        davide "Sorry bro. As much I would like to show you how hard your mom needs to get pounded..."
    else:
        davide "Sorry bro. As much I would like to show you how hard [mother] needs to get pounded..."
    davide "but when she don't want you there, she'll have her way."
    mom "And I'll make sure that you won't regret it."
    scene black
    $ k2amntr = True
    pov "{i}Damn it, why is she humiliating me like that?{/i}"
    "You go back to your bed."
    "Thinking all the time how could this happen."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    $ k2amon = True
    if hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard

label kitchen2am2:
    scene black
    call screen kitchen2am3

screen kitchen2am3():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 647 ypos 398 action (Hide('kitchen2am3'), Jump('kitchen2am4')) hovered tt.Action ("Check it out") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1106 ypos 398 action (Hide('kitchen2am3'), Jump('kitchen2am2sleep')) hovered tt.Action ("Go to sleep") focus_mask True
        frame:
            xalign .5
            text tt.value

label kitchen2am2sleep:
    scene black
    pov "No, I don't care!"
    "You go to sleep again."
    if hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard

label kitchen2amrepeat:
    scene black
    "You walk downstairs."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene kitchen 2am 001
    mom "Oh Davide, slow down! You're too big..."
    davide "No! You need to get punished more! You're a very bad slut!"
    mom "Oh my god! Yes, I'm... hah... a bad slut... hah..."
    pov "{i}Again, like last time!{/i}"
    if inc == True:
        pov "{i}And still no dad!{/i}"
    else:
        pov "{i}And still no Bruce!{/i}"
    mom "You're tearing my ass apart..."
    scene kitchen 2am 002
    davide "Yes! And that's the way you love it. Getting pierced helpless!"
    mom "Hmm... hah... aaahhh..."
    davide "Your hot ass is made for my big dick!"
    davide "And you even can take all of it!"
    mom "So... hah... deep..."
    davide "I'm about to cum! Take every drop of my sperm in your ass!"
    mom "Yes! Give it to me!"
    mom "Haaah... Aaahhh... so... hot..."
    pov "{i}Nooo...!{/i}"
    scene kitchen 2am 003
    mom "Hah... hah... hah..."
    if inc == True:
        pov "{i}That asshole! Defiling my mom's ass again and cumming so much in her.{/i}"
    else:
        pov "{i}That asshole! Defiling [mother]'s ass again and cumming so much in her.{/i}"
    pov "{i}And now he's grinning at me, celebrating his win over me again!{/i}"
    davide "You liked that, slut?"
    mom "Hah... hah... yes!"
    davide "You're not the only one!"
    mom "Wait..."
    scene kitchen 2am 004
    mom "Huh?"
    if inc == True:
        mom "You again?"
        davide "He's enjoying seeing his mom getting fucked like a slut!"
    else:
        mom "You again?"
        davide "He's enjoying seeing you getting fucked like a slut!"
    pov "That's not true."
    davide "So why you here then?"
    scene kitchen 2am 005
    mom "That doesn't matter! You shouldn't be here! I told you that before!"
    mom "Sneaking in on us!"
    if inc == True:
        davide "But he likes to watch like his father, hahaha..."
    else:
        davide "But he likes to watch like Bruce, hahaha..."
    mom "Speaking of him, where is he? BRUCE!"
    dad "Hmm...?"
    mom "This pervert is spying on us again!"
    pov "But..."
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
    pov "{i}Nooo...!{/i}"
    mom "But he's not allowed to join."
    if gangmember == True:
        pov "But I'm a gang member too."
    else:
        pov "But..."
    scene kitchen 2am 008
    if inc == True:
        davide "Sorry bro. As much I would like to show you how hard your mom needs to get pounded..."
    else:
        davide "Sorry bro. As much I would like to show you how hard [mother] needs to get pounded..."
    davide "but when she don't want you there, she'll have her will."
    mom "And I'll make sure that you won't regret it."
    scene black
    $ k2amntr = True
    pov "{i}Damn it, why is she humiliating me like that?{/i}"
    "You go back to your bed."
    "Thinking all the time how could this happen."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    $ k2amon = True
    if hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard