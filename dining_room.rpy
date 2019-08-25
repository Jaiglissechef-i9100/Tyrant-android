






label droom7momlook:
    hide screen locations
    scene diningroom 7am 002a
    pov "{i}What a lovely, lovely view this top gives me. They're nearly about to fall out.{/i}"
    jump droom



label droom7momtalk:
    hide screen locations
    scene diningroom 7am 003
    if inc == True:
        pov "{i}Oh, mom is still sleepy.{/i}"
        pov "Good morning mom!"
    else:
        pov "{i}Oh, [mother] is still sleepy.{/i}"
        pov "Good morning [mother]!"
    scene diningroom 7am 004
    if k2amon == True:
        jump droom7momntr
    if momrelationship < 30 and momntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump nicoleshakydroom
        elif randomnum == 2:
            " "
    if droom7momtalknight1 == False:
        mom "Oh, good morning [pov]! Did you sleep well in your new home?"
        pov "Not so good, but I'll get used to it."
        pov "But you look very sleepy."
        mom "Yes, it was another long night again."
    else:
        mom "Oh, good morning [pov]!"
        pov "But you look very sleepy again."
    if lroom11part1 == True and lroom11hj == False and lroom11kiss == False:
        scene diningroom 7am 005a
        mom "Yes, maybe I drank too much last night."
        mom "Did something happened?"
        pov "No. Not really."
    elif lroom11part1 == True and lroom11hj == True:
        scene diningroom 7am 005a
        mom "Yes, maybe I drank too much last night."
        mom "And I had a very weird dream."
        jump droom7momhj
    elif lroom11part1 == True and lroom11kiss == True:
        mom "Yes, maybe I drank too much last night."
        mom "And I had a very weird dream."
        jump droom7momkiss
    else:
        scene diningroom 7am 005
        if inc == True:
            mom "Your dad's friends can be so annoying."
        else:
            mom "Bruce's friends can be so annoying."
            pov "Ha, after I met them I know exactly what you mean."
            pov "But it seemed that they are close friends to you too."
        scene diningroom 7am 006
        mom "Only for our cover. They're stupid trash but as you know, it could be worse."
        pov "Yes, you're right."
        if inc == True:
            mom "I'm not sure what your dad told you that night, but you should know I'll support every decision you take."
            mom "If you want to participate in our playing or stand aside, I'll always love you and be proud of you, my son."
        else:
            mom "I'm not sure what Bruce told you that night, but you should know I'll support every decision you take."
            mom "If you want to participate in our playing or stand aside, I'll always love you and be proud of you, [pov]."
        pov "I'm not sure at the moment."
        scene diningroom 7am 007
        mom "Don't stress yourself! The important things is to find a job and plan for your future."
        if inc == True:
            mom "It'll be easier when your dad finishes his job, but I'm sure you'll make the best out of this \"new\" situation."
            pov "Sure, thank you mom."
        else:
            mom "It'll be easier when Bruce finishes his job, but I'm sure you'll make the best out of this \"new\" situation."
            pov "Sure, thank you [mother]."
        jump d7a1

label d7a1:
    call screen d7a1s

screen d7a1s():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 1258 ypos 892 action (Hide('d7a1s'), Jump('droom7momcaresslove')) hovered tt.Action ("Hold her hand [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_look_corruption_%s.png" xpos 501 ypos 676 action (Hide('d7a1s'), Jump('droom7momlookcor')) hovered tt.Action ("Stare at her tits [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1105 ypos 286 action (Hide('d7a1s'), Jump('droom7momtalk2')) hovered tt.Action ("Do nothing") focus_mask True
        frame:
            xalign .5
            text tt.value


label droom7momcaresslove:
    scene diningroom 7am 008
    $ momlove += 1
    if droom7momhold == True:
        jump droom7momloverepeat
    mom "What are you doing?"
    if inc == True:
        pov "Relax mom. I'm just holding your hand."
        pov "I'm happy too that I'm back home. We'll have much fun together as a family again."
        scene diningroom 7am 009
        mom "Oh my son has became a true gentleman."
    else:
        pov "Relax [mother]. I'm just holding your hand."
        pov "I'm happy too that I'm back home. We'll have much fun together again."
        scene diningroom 7am 009
        mom "Oh you have became a true gentleman."
    pov "Hahaha... I just want to feel you after such a long time."
    mom "You have no idea how proud I am."
    if inc == True:
        pov "Mom! Haha."
    else:
        pov "[mother]! Haha."
    $ droom7momhold = True
    jump droom7momtalk2


label droom7momlookcor:
    scene diningroom 7am 010
    $ momcorruption += 1
    mom "Is something wrong?"
    pov "No, I'm just admiring your beautiful boobs."
    if droom7momlookcor == True:
        jump droom7momcorrepeat
    scene diningroom 7am 011a
    if inc == True:
        mom "Stop it! You can't look at me this way! I'm your mother!"
        pov "I don't understand why you're upset. In your new outfits you show them off every time."
        mom "But you're my son and family members shouldn't do such things."
    else:
        mom "Stop it! You can't look at me this way!"
        pov "I don't understand why you're upset. In your new outfits you show them off every time."
        mom "But we knew each other for so long so we shouldn't do such things."
    pov "{i}This will be a long way to have fun with her, sigh.{/i}"
    pov "If I'm going to fit in my new role, I'll have to get used to your revealing outfits."
    pov "And you should have known that I'll look at you when I participate. Like the other men staring at you."
    scene diningroom 7am 012a
    mom "But I thought you could be civilized? Especially when you know what I \"must\" do."
    pov "That's why you have to calm down. I know that you have to do it, but I also have to stay in my new role and must act like that."
    if inc == True:
        mom "But I'm uncomfortable when my son stares at me like dad's trashy friends."
    else:
        mom "But I'm uncomfortable when you stares at me like Bruce's trashy friends."
    pov "You'll need to get used to it. Or do you want us to get caught just because of such a trifle?"
    mom "No... of course not..."
    pov "So you understand it now."
    $ droom7momlookcor = True
    jump droom7momtalk2

label droom7momtalk2:
    if droom7momlookcor == True:
        scene diningroom 7am 013a
    else:
        scene diningroom 7am 013
    mom "I need to do some other things now. You'll find something to do for yourself."
    if inc == True:
        pov "Sure mom."
        mom "And think about the job thing I told you."
        pov "Mom!"
    else:
        pov "Sure [mother]."
        mom "And think about the job thing I told you."
        pov "[mother]!"
    $ droom7momtalknight1 = True
    $ momrelationship += 1
    $ dtime = 8
    jump droom


label droom7momhj:
    pov "Was it about you giving me a hand-job?"
    scene diningroom 7am 006a
    mom "What? How...?"
    if inc == True:
        pov "It wasn't a dream, mom!"
        pov "You made out with me and stroked my dick until I came!"
        scene diningroom 7am 007a
        mom "No! That can't be true!"
        pov "Yes it is, mom!"
        mom "But why didn't you stop me? You know that's wrong too."
        pov "I tried. But you were so eager to do it, you didn't let me stop you."
        mom "No! No! No! I jerked my own son off."
        pov "Relax mom. It wasn't that bad, so I'm not angry."
        scene diningroom 7am 008a
        mom "This is so wrong! I'm so sorry..."
        pov "{i}Wow getting a hand-job from my hot mom and staying innocent. Nice!{/i}"
        $ lroom11part1 = False
        $ lroom11hj = False
        $ momrelationship += 1
        $ momcorruption += 1
        $ dtime = 8
        jump droom
    else:
        pov "It wasn't a dream, [mother]!"
        pov "You made out with me and stroked my dick until I came!"
        scene diningroom 7am 007a
        mom "No! That can't be true!"
        pov "Yes it is, [mother]!"
        mom "But why didn't you stop me? You know that's wrong."
        pov "I tried. But you were so eager to do it, you didn't let me stop you."
        mom "No! No! No! I jerked you off. What should I say to your mother?"
        pov "Relax [mother]. It wasn't that bad, so I'm not angry."
        scene diningroom 7am 008a
        mom "This is so wrong! I'm so sorry..."
        pov "{i}Wow getting a hand-job from her and staying innocent. Nice!{/i}"
        $ lroom11part1 = False
        $ lroom11hj = False
        $ momcorruption += 1
        $ momrelationship += 1
        $ dtime = 8
        jump droom

label droom7momkiss:
    pov "Was it about us making out together?"
    scene diningroom 7am 006a
    mom "What? How...?"
    if inc == True:
        pov "It wasn't a dream, mom!"
        pov "You made out with me!"
        scene diningroom 7am 007a
        mom "No! That can't be true!"
        pov "Yes it is, mom!"
        mom "But why didn't you stop me? You know that's wrong."
        pov "I tried. But you were so eager to do it, you didn't let me stop you."
        mom "No! No! No! I made out with my own son."
        pov "Relax mom. It was just kissing, that isn't bad."
        scene diningroom 7am 008a
        mom "This is so wrong! I'm so sorry..."
        pov "MOM!"
        scene diningroom 7am 009a
        pov "I'm not mad. I still love you as my mom. Please don't make a fuss out of it."
        $ lroom11part1 = False
        $ lroom11kiss = False
        $ momlove += 1
        $ momrelationship += 1
        $ dtime = 8
        jump droom
    else:
        pov "It wasn't a dream, [mother]!"
        pov "You made out with me!"
        scene diningroom 7am 007a
        mom "No! That can't be true!"
        pov "Yes it is, [mother]!"
        mom "But why didn't you stop me? You know that's wrong."
        pov "I tried. But you were so eager to do it, you didn't let me stop you."
        mom "No! No! No! I made out with you. What should I say to your mother?"
        pov "Relax [mother]. It was just kissing, that isn't bad."
        scene diningroom 7am 008a
        mom "This is so wrong! I'm so sorry..."
        pov "[mother]!"
        scene diningroom 7am 009a
        pov "I'm not mad. I still love you as a true friend of my family. Please don't make a fuss out of it."
        $ lroom11part1 = False
        $ lroom11kiss = False
        $ momlove += 1
        $ momrelationship += 1
        $ dtime = 8
        jump droom


label droom7momntr:
    hide screen locations
    scene diningroom 7am 004c
    mom "What did I tell you about our activities at night?"
    pov "What...?"
    mom "You spied on us! I told you this is stuff is for gang members only!"
    pov "{i}Is she talking about the incident in the kitchen last night?{/i}"
    pov "I heard a noise..."
    pov "And then I saw you getting fucked by that creep!"
    mom "And that is why you shouldn't spy on us! It's needed for the job and you could get a false impression."
    pov "He fucked you and you seemed to like it?"
    mom "I was just playing to satisfy him, but if you would have done what I told you we mustn't talk about that!"
    pov "I'm not sure anymore..."
    scene diningroom 7am 005c
    mom "I don't care! It's hard enough to play this life."
    mom "So stay away at night as long as you're not a gang member."
    mom "When you become one you will see everything in relation and will understand it."
    pov "But..."
    mom "No! And now leave me alone."
    $ dtime += 1
    jump droom


label droom13look:
    hide screen locations
    if nicolereddresswear == True:
        scene diningroom 1pm 001ancc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 001ancc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 001ancl1
    elif nicolerobewear == True:
        scene diningroom 1pm 001ancl2
    else:
        scene diningroom 1pm 001a
    pov "{i}Damn, why do they have to show so much cleavage?{/i}"
    pov "{i}And [ls] tits are so damn fine and soft!{/i}"
    jump droom

label droom13talk:
    hide screen locations
    if nicolereddresswear == True:
        scene diningroom 1pm 002ncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 002ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 002ncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 002ncl2
    else:
        scene diningroom 1pm 002
    $ lilsisrelationship += 1
    $ momrelationship += 1
    ls "Oh, hi [pov]."
    if droom13 == True:
        show blur
        "You can skip the event, because it'll repeat as you seen before."
        "When you achieve the requirements for something new, you'll get noticed, so you won't miss anything."
        "But you'll still collect points."
        "Do you want to skip this event?"
        call screen skiplroom13

        screen skiplroom13():
            default tt = Tooltip (" ")

            fixed:
                imagebutton auto "gui/icons/icon_approve_%s.png" xpos 348 ypos 550 action (Hide('skiplroom13'), Jump('skipdroom13yes')) hovered tt.Action ("Yes") focus_mask True
                imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 348 ypos 750 action (Hide('skiplroom13'), Jump('droom13con')) hovered tt.Action ("No") focus_mask True


                frame:
                    xalign .5
                    text tt.value

        label skipdroom13yes:
            "Would you collect corruption or love points?"
            call screen droom13points

            screen droom13points():
                default tt = Tooltip (" ")

                fixed:
                    imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 348 ypos 550 action (Hide('droom13points'), Jump('droom13cpoints')) hovered tt.Action ("Collect [cr1] points") focus_mask True
                    imagebutton auto "gui/icons/icon_love_%s.png" xpos 348 ypos 750 action (Hide('droom13points'), Jump('droom13lpoints')) hovered tt.Action ("Collect [lv1] points") focus_mask True

                frame:
                    xalign .5
                    text tt.value

        label droom13cpoints:
            $ momcorruption += 1
            $ lilsiscorruption += 1
            $ vdroom13lilsisbetlost = True
            $ dtime += 1
            jump droom

        label droom13lpoints:
            $ lilsislove += 1
            $ dtime += 1
            jump droom
    else:
        jump droom13con

label droom13con:
    hide blur
    mom "Hello [pov]."
    pov "Hello you two."
    "You sit down."
    if nicolereddresswear == True:
        scene diningroom 1pm 003ncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 003ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 003ncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 003ncl2
    else:
        scene diningroom 1pm 003
    ls "Math homework, ugh!"
    mom "She needs to work more on her math skills."
    pov "Oh..."
    mom "And I help her so she can get better."
    if nicolereddresswear == True:
        scene diningroom 1pm 004ncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 004ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 004ncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 004ncl2
    else:
        scene diningroom 1pm 004
    mom "And it isn't that bad, is it?"
    ls "Ugh! It's math mom. Math! I hate it."
    pov "Oh I didn't like it either back at school."
    ls "See mom. No one likes math."
    mom "Come on let's continue."
    if nicolereddresswear == True:
        scene diningroom 1pm 005ncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 005ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 005ncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 005ncl2
    else:
        scene diningroom 1pm 005
    ls "Okay mom."
    mom "I'm watching over you, but this one is really hard."
    if inc == True:
        pov "Your math isn't that good either, mom?"
        mom "No, but someone needs to help your little sister."
    else:
        pov "Your math isn't that good either, [mother]?"
        mom "No, but someone needs to help her."
    ls "Mom!"
    jump droom13tits

label droom13tits:
    if nicolereddresswear == True:
        scene diningroom 1pm 005ncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 005ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 005ncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 005ncl2
    else:
        scene diningroom 1pm 005
    call screen droom13tits1

screen droom13tits1():
    default tt = Tooltip (" ")

    fixed:
        if inc == True:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 689 ypos 735 action (Hide('droom13tits1'), Jump('droom13lookmom')) hovered tt.Action ("Look at mom's tits") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 689 ypos 735 action (Hide('droom13tits1'), Jump('droom13lookmom')) hovered tt.Action ("Look at [mother]'s tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1227 ypos 707 action (Hide('droom13tits1'), Jump('droom13looklsis')) hovered tt.Action ("Look at [ls]'s tits") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 968 ypos 297 action (Hide('droom13tits1'), Jump('droom13talk2')) hovered tt.Action ("Stop looking") focus_mask True
        frame:
            xalign .5
            text tt.value

label droom13lookmom:
    if nicolereddresswear == True:
        scene diningroom 1pm 005ancc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 005ancc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 005ancl1
    elif nicolerobewear == True:
        scene diningroom 1pm 005ancl2
    else:
        scene diningroom 1pm 005a
    pov "{i}Damn I could look at her boobs all day.{/i}"
    jump droom13tits

label droom13looklsis:
    scene diningroom 1pm 005b
    pov "{i}Her growing tits are so hot. I want to feel her softness.{/i}"
    jump droom13tits

label droom13talk2:
    if droom7momlookcor == True:
        if nicolereddresswear == True:
            scene diningroom 1pm 005ncc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 005ncc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 005ncl1
        elif nicolerobewear == True:
            scene diningroom 1pm 005ncl2
        else:
            scene diningroom 1pm 005
        call screen droom13tits2
    else:
        jump droom13talk3

screen droom13tits2():
    default tt = Tooltip (" ")

    fixed:
        if inc == True:
            imagebutton auto "gui/icons/icon_look_corruption_%s.png" xpos 689 ypos 735 action (Hide('droom13tits2'), Jump('droom13staremom')) hovered tt.Action ("Stare at mom's tits [cr1]") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_look_corruption_%s.png" xpos 689 ypos 735 action (Hide('droom13tits2'), Jump('droom13staremom')) hovered tt.Action ("Stare at [mother]'s tits [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 968 ypos 297 action (Hide('droom13tits2'), Jump('droom13talk3')) hovered tt.Action ("Don't") focus_mask True
        frame:
            xalign .5
            text tt.value

label droom13staremom:
    $ vdroom13momtits = True
    if nicolereddresswear == True:
        scene diningroom 1pm 005ancc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 005ancc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 005ancl1
    elif nicolerobewear == True:
        scene diningroom 1pm 005ancl2
    else:
        scene diningroom 1pm 005a
    pov "{i}I won't stop. I must make her show me them. Like soft, hot pillows.{/i}"
    if nicolereddresswear == True:
        scene diningroom 1pm 005cncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 005cncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 005cncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 005cncl2
    else:
        scene diningroom 1pm 005c
    pov "{i}Huh?{/i}"
    if nicolereddresswear == True:
        scene diningroom 1pm 005dncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 005dncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 005dncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 005dncl2
    else:
        scene diningroom 1pm 005d
    "She's looking at you unsure."
    pov "{i}Hah she won't make a scene in front of [ls].{/i}"
    ls "And this is... no that makes no sense..."
    "You shake your head and form the word \"role-play\" with your lips."
    if nicolereddresswear == True:
        scene diningroom 1pm 005encc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 005encc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 005encl1
    elif nicolerobewear == True:
        scene diningroom 1pm 005encl2
    else:
        scene diningroom 1pm 005e
    mom "Hnn..."
    "Now you form the word \"better\"."
    $ momcorruption += 1
    jump droom13talk3

label droom13talk3:
    if vdroom13momtits == True:
        if nicolereddresswear == True:
            scene diningroom 1pm 005encc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 005encc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 005encl1
        elif nicolerobewear == True:
            scene diningroom 1pm 005encl2
        else:
            scene diningroom 1pm 005e
    else:
        if nicolereddresswear == True:
            scene diningroom 1pm 005ncc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 005ncc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 005ncl1
        elif nicolerobewear == True:
            scene diningroom 1pm 005ncl2
        else:
            scene diningroom 1pm 005
    ls "Damn, I don't get it."
    mom "Watch your language honey!"
    ls "Sorry mom."
    jump droom13help

label droom13help:
    call screen droom13help1

screen droom13help1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1229 ypos 890 action (Hide('droom13help1'), Jump('droom13help2')) hovered tt.Action ("Help her") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 690 ypos 882 action (Hide('droom13help1'), Jump('droom13talk4')) hovered tt.Action ("Don't") focus_mask True
        frame:
            xalign .5
            text tt.value

label droom13talk4:
    if vdroom13momtits == True:
        if nicolereddresswear == True:
            scene diningroom 1pm 005encc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 005encc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 005encl1
        elif nicolerobewear == True:
            scene diningroom 1pm 005encl2
        else:
            scene diningroom 1pm 005e
    else:
        if nicolereddresswear == True:
            scene diningroom 1pm 005ncc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 005ncc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 005ncl1
        elif nicolerobewear == True:
            scene diningroom 1pm 005ncl2
        else:
            scene diningroom 1pm 005
    pov "I'll go now. This is boring."
    mom "Yeah sure, see you later."
    ls "See you stupid."
    $ droom13 = True
    $ dtime = 14
    jump droom

label droom13help2:
    if vdroom13momtits == True:
        if nicolereddresswear == True:
            scene diningroom 1pm 006ancc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 006ancc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 006ancl1
        elif nicolerobewear == True:
            scene diningroom 1pm 006ancl2
        else:
            scene diningroom 1pm 006a
    else:
        if nicolereddresswear == True:
            scene diningroom 1pm 006ncc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 006ncc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 006ncl1
        elif nicolerobewear == True:
            scene diningroom 1pm 006ncl2
        else:
            scene diningroom 1pm 006
    pov "I can help you!"
    ls "Huh?"
    ls "You mean... help with math...?"
    pov "{i}Haha, who's stupid now?{/i}"
    pov "Yes sure, my math was good back in school."
    if vdroom13momtits == True:
        if nicolereddresswear == True:
            scene diningroom 1pm 007ancc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 007ancc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 007ancl1
        elif nicolerobewear == True:
            scene diningroom 1pm 007ancl2
        else:
            scene diningroom 1pm 007a
    else:
        if nicolereddresswear == True:
            scene diningroom 1pm 007ncc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 007ncc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 007ncl1
        elif nicolerobewear == True:
            scene diningroom 1pm 007ncl2
        else:
            scene diningroom 1pm 007
    ls "Hahahahaha..."
    pov "I wasn't kidding."
    ls "Hahaha... sure..."
    if vdroom13momtits == False:
        mom "He's right."
    ls "No, he's stupid, haha."
    pov "You're almost right. The answer to your question is 42."
    if vdroom13momtits == True:
        if nicolereddresswear == True:
            scene diningroom 1pm 009ancc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 009ancc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 009ancl1
        elif nicolerobewear == True:
            scene diningroom 1pm 009ancl2
        else:
            scene diningroom 1pm 009a
    else:
        if nicolereddresswear == True:
            scene diningroom 1pm 008ancc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 008ancc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 008ancl1
        elif nicolerobewear == True:
            scene diningroom 1pm 008ancl2
        else:
            scene diningroom 1pm 008a
    ls "42?"
    pov "Your homework dummy."
    ls "How did you...?"
    if vdroom13momtits == False and inc == True:
        mom "That's my intelligent son."
    elif vdroom13momtits == False and inc == False:
        mom "He's intelligent."
    pov "And I can help you with the rest. You would be done much sooner."
    ls "Really...?"
    jump droom13help3

label droom13help3:
    call screen dr13h4

screen dr13h4():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1229 ypos 890 action (Hide('dr13h4'), Jump('droom13helplove')) hovered tt.Action ("Just help her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 690 ypos 882 action (Hide('dr13h4'), Jump('droom13helpcor')) hovered tt.Action ("Demand something [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label droom13helplove:
    if vdroom13momtits == True:
        if nicolereddresswear == True:
            scene diningroom 1pm 009ancc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 009ancc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 009ancl1
        elif nicolerobewear == True:
            scene diningroom 1pm 009ancl2
        else:
            scene diningroom 1pm 009a
    else:
        if nicolereddresswear == True:
            scene diningroom 1pm 008ancc1
        elif nicolebabydollwear == True:
            scene diningroom 1pm 008ancc2
        elif nicolesweaterpantswear == True:
            scene diningroom 1pm 008ancl1
        elif nicolerobewear == True:
            scene diningroom 1pm 008ancl2
        else:
            scene diningroom 1pm 008a
    pov "Yes just ask me anything and we can do it together."
    if inc == True:
        ls "That's a great idea brother."
    else:
        ls "That's a great idea [pov]."
    if nicolereddresswear == True:
        scene diningroom 1pm 011ncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 011ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 011ncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 011ncl2
    else:
        scene diningroom 1pm 011
    mom "Good we have someone that can help."
    "You finish the math homework together with her."
    if nicolereddresswear == True:
        scene diningroom 1pm 012ncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 012ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 012ncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 012ncl2
    else:
        scene diningroom 1pm 012
    ls "Yay! I did it!"
    pov "You? We did it."
    ls "Oh yes, haha."
    mom "Fine. And next time you can help her alone."
    pov "Hmm... maybe."
    $ droom13 = True
    $ vdroom13lilsisjusthelp = True
    $ lilsislove += 1
    $ dtime = 14
    jump droom

label droom13helpcor:
    if nicolereddresswear == True:
        scene diningroom 1pm 009ancc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 009ancc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 009ancl1
    elif nicolerobewear == True:
        scene diningroom 1pm 009ancl2
    else:
        scene diningroom 1pm 009a
    pov "I can help you but you need to do something in return for me."
    mom "..."
    ls "What is it?"
    pov "You'll have to clean my room, haha."
    pov "Nothing is for free."
    pov "When you do that I'll help you with your math homework."
    if nicolereddresswear == True:
        scene diningroom 1pm 010ancc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 010ancc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 010ancl1
    elif nicolerobewear == True:
        scene diningroom 1pm 010ancl2
    else:
        scene diningroom 1pm 010a
    ls "O... okay... I can do that."
    ls "But you won't trick me!"
    pov "Sure, a deal is a deal."
    ls "Okay, deal."
    if nicolereddresswear == True:
        scene diningroom 1pm 011ncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 011ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 011ncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 011ncl2
    else:
        scene diningroom 1pm 011
    mom "Good we have someone that can help."
    "You finish the math homework together with her."
    if nicolereddresswear == True:
        scene diningroom 1pm 012ncc1
    elif nicolebabydollwear == True:
        scene diningroom 1pm 012ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 1pm 012ncl1
    elif nicolerobewear == True:
        scene diningroom 1pm 012ncl2
    else:
        scene diningroom 1pm 012
    ls "Yay! I did it!"
    pov "You? We did it."
    ls "Oh yes, haha."
    mom "Fine. And next time you can help her alone."
    pov "And don't forget about our deal."
    ls "Yes, I'll come later at 5pm to clean your room. Is that okay?"
    pov "Sure."
    $ droom13 = True
    $ vdroom13lilsisbetlost = True
    $ lilsiscorruption += 1
    $ dtime = 14
    jump droom




label droom12talk:
    hide screen locations
    scene diningroom 12pm 002
    if nicolereddresswear == True:
        show 12pm002niccorruption1:
            xpos 900
            ypos 240
    elif nicolebabydollwear == True:
        show 12pm002niccorruption2:
            xpos 900
            ypos 240
    elif nicolesweaterpantswear == True:
        show 12pm002niclove1:
            xpos 900
            ypos 240
    elif nicolerobewear == True:
        show 12pm002niclove2:
            xpos 900
            ypos 240
    else:
        show 12pm002nicnormal:
            xpos 900
            ypos 240
    if alexisrockerwear == True:
        show 12pm002alecorruption1:
            xpos 1365
            ypos 390
    elif alexislingeriewear == True:
        show 12pm002alecorruption2:
            xpos 1365
            ypos 390
    elif alexisjeansskirtwear == True:
        show 12pm002alelove1:
            xpos 1365
            ypos 390
    elif alexisgridwear == True:
        show 12pm002alelove2:
            xpos 1365
            ypos 390
    else:
        show 12pm002alenormal:
            xpos 1365
            ypos 390
    if cassandraheartdresswear == True:
        show 12pm002cascorruption1:
            xpos 102
            ypos 490
    elif cassandralingeriewear == True:
        show 12pm002cascorruption2:
            xpos 102
            ypos 490
    elif cassandrajeanswear == True:
        show 12pm002caslove1:
            xpos 102
            ypos 490
    elif cassandrapajamawear == True:
        show 12pm002caslove2:
            xpos 102
            ypos 490
    else:
        show 12pm002casnormal:
            xpos 102
            ypos 490
    $ momrelationship += 1
    $ lilsisrelationship += 1
    $ bigsisrelationship += 1
    mom "Oh you're here [pov]. Come on eat with us."
    if inc == True:
        ls "Oh hey big brother."
    else:
        ls "Oh hey dummy."
    bs "Yeah, yeah, hello."
    pov "Hello all."
    "You sit down to eat with them."
    scene diningroom 12pm 003
    if nicolereddresswear == True:
        show 12pm003niccorruption1:
            xpos 244
            ypos 291
    elif nicolebabydollwear == True:
        show 12pm003niccorruption2:
            xpos 244
            ypos 291
    elif nicolesweaterpantswear == True:
        show 12pm003niclove1:
            xpos 244
            ypos 291
    elif nicolerobewear == True:
        show 12pm003niclove2:
            xpos 244
            ypos 291
    else:
        show 12pm003nicnormal:
            xpos 244
            ypos 291
    if alexisrockerwear == True:
        show 12pm003alecorruption1:
            xpos 1192
            ypos 454
    elif alexislingeriewear == True:
        show 12pm003alecorruption2:
            xpos 1192
            ypos 454
    elif alexisjeansskirtwear == True:
        show 12pm003alelove1:
            xpos 1192
            ypos 454
    elif alexisgridwear == True:
        show 12pm003alelove2:
            xpos 1192
            ypos 454
    else:
        show 12pm003alenormal:
            xpos 1192
            ypos 454
    mom "So what are we talking about [bs]?"
    jump droom12gift

label droom12gift:
    hide screen locations
    scene diningroom 12pm 003
    if nicolereddresswear == True:
        show 12pm003niccorruption1:
            xpos 244
            ypos 291
    elif nicolebabydollwear == True:
        show 12pm003niccorruption2:
            xpos 244
            ypos 291
    elif nicolesweaterpantswear == True:
        show 12pm003niclove1:
            xpos 244
            ypos 291
    elif nicolerobewear == True:
        show 12pm003niclove2:
            xpos 244
            ypos 291
    else:
        show 12pm003nicnormal:
            xpos 244
            ypos 291
    if alexisrockerwear == True:
        show 12pm003alecorruption1:
            xpos 1192
            ypos 454
    elif alexislingeriewear == True:
        show 12pm003alecorruption2:
            xpos 1192
            ypos 454
    elif alexisjeansskirtwear == True:
        show 12pm003alelove1:
            xpos 1192
            ypos 454
    elif alexisgridwear == True:
        show 12pm003alelove2:
            xpos 1192
            ypos 454
    else:
        show 12pm003alenormal:
            xpos 1192
            ypos 454
    call screen droom12gift1

screen droom12gift1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_gift_%s.png" xpos 886 ypos 215 action (Hide ('droom12gift1'), Show('giftdr12icon', transition=None)) hovered tt.Action ("Give someone a gift") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 886 ypos 310 action (Hide ('droom12gift1'), Jump('droom12talkc')) hovered tt.Action ("Don't give anyone a gift") focus_mask True
    frame:
        xalign .5
        text tt.value



label droom12talkc:
    scene diningroom 12pm 003
    if nicolereddresswear == True:
        show 12pm003niccorruption1:
            xpos 244
            ypos 291
    elif nicolebabydollwear == True:
        show 12pm003niccorruption2:
            xpos 244
            ypos 291
    elif nicolesweaterpantswear == True:
        show 12pm003niclove1:
            xpos 244
            ypos 291
    elif nicolerobewear == True:
        show 12pm003niclove2:
            xpos 244
            ypos 291
    else:
        show 12pm003nicnormal:
            xpos 244
            ypos 291
    if alexisrockerwear == True:
        show 12pm003alecorruption1:
            xpos 1192
            ypos 454
    elif alexislingeriewear == True:
        show 12pm003alecorruption2:
            xpos 1192
            ypos 454
    elif alexisjeansskirtwear == True:
        show 12pm003alelove1:
            xpos 1192
            ypos 454
    elif alexisgridwear == True:
        show 12pm003alelove2:
            xpos 1192
            ypos 454
    else:
        show 12pm003alenormal:
            xpos 1192
            ypos 454
    pov "{i}Is [ls] protruding her tongue at me?{/i}"
    pov "{i}Hah, it looks somewhat cute.{/i}"
    scene diningroom 12pm 004
    if nicolereddresswear == True:
        show 12pm004niccorruption1:
            xpos 274
            ypos 310
    elif nicolebabydollwear == True:
        show 12pm004niccorruption2:
            xpos 274
            ypos 310
    elif nicolesweaterpantswear == True:
        show 12pm004niclove1:
            xpos 274
            ypos 310
    elif nicolerobewear == True:
        show 12pm004niclove2:
            xpos 274
            ypos 310
    else:
        show 12pm004nicnormal:
            xpos 274
            ypos 310
    if alexisrockerwear == True:
        show 12pm004alecorruption1:
            xpos 1165
            ypos 418
    elif alexislingeriewear == True:
        show 12pm004alecorruption2:
            xpos 1165
            ypos 418
    elif alexisjeansskirtwear == True:
        show 12pm004alelove1:
            xpos 1165
            ypos 418
    elif alexisgridwear == True:
        show 12pm004alelove2:
            xpos 1165
            ypos 418
    else:
        show 12pm004alenormal:
            xpos 1165
            ypos 418
    ls "Boo..."
    mom "Eh?"
    ls "*kiss*"
    mom "What are you doing, [ls]?"
    scene diningroom 12pm 005
    if nicolereddresswear == True:
        show 12pm005niccorruption1:
            xpos 303
            ypos 328
    elif nicolebabydollwear == True:
        show 12pm005niccorruption2:
            xpos 303
            ypos 328
    elif nicolesweaterpantswear == True:
        show 12pm005niclove1:
            xpos 303
            ypos 328
    elif nicolerobewear == True:
        show 12pm005niclove2:
            xpos 303
            ypos 328
    else:
        show 12pm005nicnormal:
            xpos 303
            ypos 328
    if alexisrockerwear == True:
        show 12pm005alecorruption1:
            xpos 1117
            ypos 387
    elif alexislingeriewear == True:
        show 12pm005alecorruption2:
            xpos 1117
            ypos 387
    elif alexisjeansskirtwear == True:
        show 12pm005alelove1:
            xpos 1117
            ypos 387
    elif alexisgridwear == True:
        show 12pm005alelove2:
            xpos 1117
            ypos 387
    else:
        show 12pm005alenormal:
            xpos 1117
            ypos 387
    ls "Oh I was just talking to [pov] in his dummy language, haha."
    pov "{i}Oh she wants to play. That needs revenge.{/i}"
    mom "Oh I understand."
    pov "Hey..."
    if droom12pm == True:
        jump droom12pmrepeat
    bs "Are you going to see your retarded friend later too?"
    scene diningroom 12pm 006
    pov "What...?"
    bs "I mean [ls]!"
    scene diningroom 12pm 006a
    pov "{i}Damn, that shirt is transparent..{/i}"
    scene diningroom 12pm 007
    ls "Watch your mouth [bs]!"
    bs "Why? That little, flat-chested monster is retarded like you, maybe that's the reason why you are best friends, haha."
    pov "Flat-chested monster?"
    ls "Not everyone needs a doctor for her tits like you, ugly!"
    mom "Hey...!"
    pov "{i}Oh so [bs] tits are made. No wonder they are so firm and round.{/i}"
    bs "Watch out, little sister. I could get you."
    scene diningroom 12pm 008
    ls "How about you shut up and fuck yourself!"
    mom "What...?"
    pov "{i}Wow, [ls] got mad.{/i}"
    bs "W... what...?"
    ls "You heard me!"
    scene diningroom 12pm 009
    bs "I'll kill you, you little slut!"
    mom "Stop it, [bs]!"
    mom "I don't want to hear those words in our house."
    bs "Better prepare yourself!"
    scene diningroom 12pm 010
    ls "I'll leave now. No need to sit with \"something\" on one table."
    mom "But honey..."
    ls "No mom. It isn't your fault that she's so stupid."
    bs "Watch your mouth."
    pov "{i}Wow, what a \"happy\" family.{/i}"
    scene diningroom 12pm 011
    mom "Was that really necessary?"
    bs "I was just asking a question."
    pov "{i}What a bitch.{/i}"
    pov "And how are you doing with our \"new\" situation?"
    scene diningroom 12pm 013a
    pov "You're done with school, are you working somewhere?"
    pov "And did you really have surgery on your breasts?"
    mom "[pov]!"
    scene diningroom 12pm 014a
    bs "Oh you didn't see? Yes I made my breasts bigger and more firm, because my job needed them."
    pov "{i}She needed them for her job? Is she a prostitute?{/i}"
    pov "You needed them for your job?"
    bs "Yes I'm a famous influencer. People love me and my lifestyle."
    bs "So for me it's all better now and I can wear what I want."
    bs "And dad's friends like me too."
    bs "So yes, I love the \"new\" life."
    scene diningroom 12pm 015a
    mom "That's not the way I raised you!"
    bs "I'm an adult, I can do what I want mom."
    mom "But it's not right and it doesn't suit you."
    scene diningroom 12pm 016a
    bs "So you're the only one allowed to dress up slutty and sexy?"
    mom "What...?"
    bs "Don't you think I'm right [pov]? Mom dresses like a slut."
    scene diningroom 12pm 017a
    mom "Are you serious? Talking that way about me?"
    bs "Are you with me or not, [pov]?"
    jump dr12md

label dr12md:
    call screen dr12md1

screen dr12md1():
    default tt = Tooltip (" ")

    fixed:
        if inc == True:
            imagebutton auto "gui/icons/icon_love_%s.png" xpos 748 ypos 316 action (Hide('dr12md1'), Jump('droom12momlove')) hovered tt.Action ("Disagree with [bs] [lv1]/Mom") focus_mask True
            imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1255 ypos 316 action (Hide('dr12md1'), Jump('droom12momcor')) hovered tt.Action ("Agree with [bs] [cr1]/Mom") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_love_%s.png" xpos 748 ypos 316 action (Hide('dr12md1'), Jump('droom12momlove')) hovered tt.Action ("Disagree with [bs] [lv1]/[mother]") focus_mask True
            imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1255 ypos 316 action (Hide('dr12md1'), Jump('droom12momcor')) hovered tt.Action ("Agree with [bs] [cr1]/[mother]") focus_mask True
        frame:
            xalign .5
            text tt.value

label droom12momlove:
    pov "No you're wrong. It maybe something revealing, but she don't dress like a slut."
    pov "And it's also needed for our cover."
    scene diningroom 12pm 019a
    mom "Thank you [pov]."
    mom "You're so wrong [bs], I hope you see that now."
    scene diningroom 12pm 018a
    bs "Hmm... I thought you saw that [pov]."
    $ momlove += 1
    jump dr12bsd

label droom12momcor:
    if inc == True:
        pov "Yes, you're right. Mom looks like a slut."
    else:
        pov "Yes, you're right. [mother] looks like a slut."
    $ droom12momslut = True
    scene diningroom 12pm 018ab
    mom "What...?"
    pov "But like a real sexy and hot slut."
    if inc == True:
        pov "You play your role very good mom. I'm proud!"
        mom "Hmm..."
        scene diningroom 12pm 015b
        bs "So I was right. You're on my line brother."
    else:
        pov "You play your role very good [mother]. I'm proud!"
        mom "Hmm..."
        scene diningroom 12pm 015b
        bs "So I was right. You're on my line [pov]."
    pov "Yes, you're right with that."
    $ momcorruption += 1
    jump dr12bsd

label dr12bsd:
    call screen dr12bsd1

screen dr12bsd1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1255 ypos 96 action (Hide('dr12bsd1'), Jump('droom12bigsislove')) hovered tt.Action ("Compliment [bs] [lv1]/[bs])") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1255 ypos 316 action (Hide('dr12bsd1'), Jump('droom12bigsiscor')) hovered tt.Action ("Insult [bs] [cr1]/[bs])") focus_mask True
        frame:
            xalign .5
            text tt.value

label droom12bigsiscor:
    if droom12momslut == True:
        pov "But I think you look like a slut too. A kinky girl who dresses like you want to get laid with everyone!"
    else:
        pov "But I think you look like a slut instead. A kinky girl who dresses like you want to get laid with everyone!"
    scene diningroom 12pm 016b
    bs "What...? Are you serious?"
    bs "Saying something to me?"
    pov "I'm only honest."
    bs "You fucking pervert!"
    scene diningroom 12pm 017b
    if inc == True:
        mom "You can't say something to your sister [pov]!"
    else:
        mom "You can't say something to her [pov]!"
    pov "Why not, she asked for it!"
    mom "What's gotten into you?"
    scene diningroom 12pm 018b
    bs "Fuck you! You damn asshole!"
    pov "..."
    bs "I'll take care of that you'll regret it!"
    bs "I'm out of here, you fucking me up!"
    $ bigsiscorruption += 1
    $ droom12bsisslut = True
    jump dr12endsluts

label droom12bigsislove:
    pov "And I think you're looking really good in your new outfit."
    pov "No wonder everyone loves you."
    scene diningroom 12pm 019ab
    bs "Wow, I got a compliment from you. Is it opposite day today, haha?"
    if inc == True:
        pov "No, I'm just honest like I rated mom's outfit."
    else:
        pov "No, I'm just honest like I rated [mother]'s outfit."
    bs "Good, then I have another fan."
    pov "Oh then I can have an autograph?"
    bs "Hahaha..."
    scene diningroom 12pm 020ab
    mom "It's nice that you two understand each other, but I still think that it's to revealing."
    bs "Oh come on mom. You heard [pov]. He's a man, also other men will think that way too."
    pov "Calm down. It isn't that bad."
    $ bigsislove += 1
    jump dr12endlove

label dr12endlove:
    if droom12momslut == True:
        scene diningroom 12pm 020c
        if inc == True:
            pov "But like I said mom. It's okay when you want to dress like a slut."
        else:
            pov "But like I said [mother]. It's okay when you want to dress like a slut."
        pov "We must all make sacrifices for this undercover thing."
        mom "Hmm..."
        scene diningroom 12pm 021b
        mom "I'll leave you now. You two are so wrong but I can't discuss this with you."
        if inc == True:
            bs "Oh come on mom. Just accept the rating of your children. We're just honest."
        else:
            bs "Oh come on mom. Just accept our rating. We're just honest."
        pov "No need to be offended."
        $ droom12pm = True
        $ dtime += 1
        jump droom
    else:
        scene diningroom 12pm 021b
        mom "No, I'm still not with you. So I'll go now."
        mom "I can't change your mind, but I know that I'm right."
        bs "Seriously mom?"
        pov "..."
        scene diningroom 12pm 019ab
        if inc == True:
            bs "Looks like we won, little brother, haha."
        else:
            bs "Looks like we won, haha."
        pov "Hmm..."
        bs "It's good to have someone on my side."
        pov "Sure..."
        $ droom12pm = True
        $ dtime += 1
        jump droom

label dr12endsluts:
    if droom12momslut == False:
        scene diningroom 12pm 019b
        mom "You shouldn't be that mean to her."
        pov "But I was only saying the truth. And you think the same."
        mom "Maybe, but I'm not sure how she'll get on with that."
        mom "You came here after a year and told her something."
        pov "Maybe you're right, maybe not... She's an adult now, she can handle it."
        mom "Maybe you're right."
        $ droom12pm = True
        $ dtime += 1
        jump droom
    else:
        scene diningroom 12pm 019b
        mom "You shouldn't be that mean to her."
        pov "But I was only saying the truth. And you think the same."
        mom "Maybe, but I'm not sure how she'll get on with that."
        mom "You came here after a year and told her something."
        pov "Maybe you're right, maybe not... She's an adult now, she can handle it."
        mom "Maybe you're right."
        pov "Yes and I'm right with the other thing I said."
        scene diningroom 12pm 020b
        pov "You dress like a slut and I wonder if you really did that for your role only?"
        mom "W... what? You want to say...?"
        pov "Yeah I think you want to reveal so much to be seen by other men."
        pov "And maybe seen by me too."
        scene diningroom 12pm 021c
        mom "You can't be serious!"
        pov "Oh yes I am. Long ago you were more prim and now this."
        if inc == True:
            mom "I told you it's to support your dad's work."
        else:
            mom "I told you it's to support Bruce's work."
        pov "Haha, sure. Maybe. But I love the outcome."
        mom "Hmm..."
        $ droom12pm = True
        $ dtime += 1
        jump droom


label droom18talk:
    hide screen locations
    if nicolereddresswear == True:
        scene diningroom 6pm 002ncc1
    elif nicolebabydollwear == True:
        scene diningroom 6pm 002ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 6pm 002ncl1
    elif nicolerobewear == True:
        scene diningroom 6pm 002ncl2
    else:
        scene diningroom 6pm 002
    $ momrelationship += 1
    $ lilsisrelationship += 1
    mom "I'm glad you came to eat with us."
    ls "Hey [pov]."
    dad "[pov], good to see you again."
    pov "Hello."
    if droom6pm == True:
        jump droom6pmrepeat
    scene diningroom 6pm 003
    if inc == True:
        mom "Your dad and I have something to discuss with you."
        pov "Oh, OK. What is it?"
        dad "It's something about your future, son."
    else:
        mom "Bruce and I have something to discuss with you."
        pov "Oh, OK. What is it?"
        dad "It's something about your future."
    scene diningroom 6pm 004
    ls "Maybe they want send you back to school, dummy. You need it for sure, haha."
    mom "[ls]!"
    ls "And when you're good in school, you'll get some rewards."
    ls "But let me think... no rewards for you! <giggle>"
    mom "You can't..."
    dad "Calm down, [mother]. They haven't seen each other so long, let them have their fun."
    mom "Hmm..."
    scene diningroom 6pm 005
    ls "Speaking about rewards. How much better grades must I get in math to get my new smartphone?"
    ls "My old one is still broken!"
    pov "{i}Still breaking everything? Who's the dummy, haha.{/i}"
    scene diningroom 6pm 006
    mom "We talked about this several times, honey."
    ls "Yes but I don't want to wait longer."
    dad "Are you really getting better at math?"
    ls "Yes dad."
    scene diningroom 6pm 007
    mom "When you raise your grades in math you'll get your new smartphone."
    ls "But I raised them already."
    mom "Yes and at the end of the year we'll see and then it will be the time."
    scene diningroom 6pm 008
    ls "At the end of the year?"
    mom "Yes?"
    ls "That's not what we agreed!"
    ls "I need it now, all my friends have the new \"Banana 8\" and I'll have the 5 with a broken glass!"
    scene diningroom 6pm 009
    mom "You know that we can't afford it right now. But we can find a way at the end of the year."
    mom "If your grades are good then."
    dad "Yes that sounds good, doesn't it?"
    scene diningroom 6pm 010
    ls "No! Mom! That's not fair!"
    ls "You lied to me. I got better at math and I want my new phone."
    scene diningroom 6pm 011
    mom "Calm down honey."
    dad "Watch your language [ls]!"
    mom "You need to understand our situation. There is no other way at the moment."
    scene diningroom 6pm 012
    ls "No! I don't agree! I'll find another way to get the money!"
    mom "Honey..."
    ls "I'll work for Jeremy. He may be an asshole, but then I can buy a phone myself!"
    dad "No you won't. Jeremy is a liar and can't be trusted."
    dad "It could be he won't even pay you!"
    mom "Your dad is right. He's a scammer!"
    ls "I don't care. Those are only lies other people tell about him. He won't betray me."
    ls "Sarah worked for him and she got the money he promised."
    mom "[ls]..."
    ls "No! I hate you!"
    scene diningroom 6pm 013
    dad "Do you really think she'll do such a thing?"
    mom "No! When she wants to collect the money after working around his house, she'll need years to get the money."
    mom "She just wants to rebel. I'll talk with her later."
    dad "Hmm... I think you're right."
    scene diningroom 6pm 014
    if inc == True:
        mom "So, let us talk about you! Enough of your sisters hate!"
    else:
        mom "So, let us talk about you! Enough of her hate!"
    pov "Okay...?"
    mom "How does the \"new\"situation working out for you?"
    dad "Yes tell us. Are you getting used to it?"
    pov "Hmm... I'm still not sure. But I noticed that the basement is always locked for me."
    pov "Why can't I enter it and when will the time come for that?"
    scene diningroom 6pm 015
    mom "The basement?"
    pov "Yes... Where the gang activities happen!"
    mom "That's not possible!"
    dad "..."
    pov "Not possible? For now? Why not? Are you hiding something from me?"
    mom "No! I mean it's not possible because you have to be in the gang to enter."
    pov "The gang?"
    scene diningroom 6pm 016
    mom "It's right isn't it? The basement is the place for gang-members only."
    dad "Y... yes sure."
    pov "{i}Why is she so nervous right now? Is she coming up with something?{/i}"
    pov "So I'll have to join the gang!"
    scene diningroom 6pm 017
    mom "Wait! I'm sure we can find another way to get you in the basement."
    pov "Why is that now?"
    mom "I hoped you'd find a normal job and can stay away from these idiots."
    pov "A normal job?"
    mom "Yes now that you finished school it's about time you get a good job."
    pov "Okay..."
    dad "But we could use his help! And he can help me with my investigation."
    mom "No! I want him to have a better life!"
    dad "But..."
    mom "So what are your plans?"
    pov "I want..."
    jump d6d

label d6d:
    call screen d6d1

screen d6d1():
    default tt = Tooltip (" ")

    fixed:
        if inc == True:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 939 ypos 174 action (Hide('d6d1'), Jump('droom6approve')) hovered tt.Action ("A normal job [lv1]/Mom [bd1]/Dad)") focus_mask True
            imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1142 ypos 174 action (Hide('d6d1'), Jump('droom6disapprove')) hovered tt.Action ("Join the gang [cr1]/Mom [gd1]/Dad)") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 939 ypos 174 action (Hide('d6d1'), Jump('droom6approve')) hovered tt.Action ("A normal job [lv1]/[mother] [bd1]/Bruce)") focus_mask True
            imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1142 ypos 174 action (Hide('d6d1'), Jump('droom6disapprove')) hovered tt.Action ("Join the gang [cr1]/[mother] [gd1]/Bruce)") focus_mask True
        frame:
            xalign .5
            text tt.value

label droom6disapprove:
    scene diningroom 6pm 018a
    mom "You can't be serious!"
    dad "I knew I could count on you!"
    pov "I think it's better if I stay with the role-playing here and do what a thugs son would do."
    mom "But I thought..."
    scene diningroom 6pm 019a
    if inc == True:
        mom "It's all your fault! You corrupted my son!"
    else:
        mom "It's all your fault! You corrupted him!"
    dad "What...?"
    mom "What did you tell him?"
    dad "I didn't..."
    pov "It's my decision!"
    mom "That's wrong and you both know it!"
    dad "Wait, dear..."
    scene diningroom 6pm 020a
    dad "Don't bother about her. She'll calm down and understand it."
    pov "You think so?"
    dad "Oh, I'm sure about that."
    dad "I'm glad you decided to support me here. It's a bit rough to play the macho bad boy, but together we can bring it to a good end!"
    if inc == True:
        pov "I hope so, dad."
        dad "I'm sure about it, because you're my son!"
        pov "Okay..."
        dad "Now I'll have to look out for your mom. See you later!"
    else:
        pov "I hope so, Bruce."
        dad "I'm sure about it, because I know you!"
        pov "Okay..."
        dad "Now I'll have to look out for her. See you later!"
    $ momcorruption += 1
    $ droom6pm = True
    $ dadgood += 1
    $ dtime += 1
    jump droom

label droom6approve:
    scene diningroom 6pm 018b
    if inc == True:
        mom "Yes, I knew it. My son would choose the right thing."
        dad "What...? I thought you'd help me!"
        pov "No sorry dad. I've other plans."
    else:
        mom "Yes, I knew it. You would choose the right thing."
        dad "What...? I thought you'd help me!"
        pov "No sorry Bruce. I've other plans."
        mom "I'm so happy right now!"
    scene diningroom 6pm 019b
    mom "See? I was right about him. He won't hang around with your idiotic friends."
    dad "But wouldn't it be better if he can learn more about this stuff?"
    mom "No! I'm sure you can do it alone. He can do much better than that."
    if inc == True:
        pov "Wow! Thank you mom."
    else:
        pov "Wow! Thank you [mother]."
    dad "I'm not happy with this decision."
    scene diningroom 6pm 020b
    mom "He'll get used to your decision. He knows it's better for you."
    pov "I didn't know he wanted me to join them."
    mom "He has the idea that it'll be done sooner with you by his side, but we both know that is just dreaming."
    pov "Hmm... I think you're right."
    mom "I am, but now I should look after him. To improve his mood."
    $ momlove += 1
    $ droom6pm = True
    $ dadbad += 1
    $ dtime += 1
    jump droom