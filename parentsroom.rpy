

label proom19watch:
    hide screen locations
    scene main 7pm parents room
    mom "Ahhh... ahhh... ahhh..."
    if inc == True:
        pov "{i}Mom and dad are fucking.{/i}"
    else:
        pov "{i}[mother] and Bruce are fucking.{/i}"
    mom "Harder... please harder..."
    pov "{i}She seem to enjoy it very much.{/i}"
    pov "{i}Getting that hard ride.{/i}"
    mom "Oh my god, yes. I can feel your hard dick."
    $ proom19fuck = True
    jump parentsroom



label proomlooktits:
    hide screen locations
    scene parentsroom 8pm 002a
    pov "{i}Wow, her beautiful, big boobs.{/i}"
    jump parentsroom

label proomlookcrotch:
    hide screen locations
    scene parentsroom 8pm 002b
    pov "{i}That little black thing is in the way!{/i}"
    pov "{i}I'd love to see her pussy soon. The entrance to heaven.{/i}"
    jump parentsroom

label proomlookpicture:
    hide screen locations
    scene parentsroom 8pm 002c
    pov "{i}Another of those kinky pictures. But the girl is damn hot.{/i}"
    pov "{i}I wonder where they got them?{/i}"
    jump parentsroom

label proomtalk:
    hide screen locations
    if proom8pm == True:
        jump proom8repeat1
    if inc == True:
        pov "Hi mom!"
    else:
        pov "Hi [mother]!"
    scene parentsroom 8pm 003
    if momrelationship < 30 and momntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump nicoleshakylroom
        elif randomnum == 2:
            " "
    mom "Eh?"
    mom "What are you doing here [pov]? Don't you see I'm changing?"
    pov "Yes I see that. But I didn't go in on purpose."
    pov "I wasn't in that room before so I couldn't know."
    scene parentsroom 8pm 004
    mom "Oh, you're right. I didn't tell you about it."
    if inc == True:
        mom "So this is your dad's and my room."
    else:
        mom "So this is Bruce's and my room."
    pov "A little small."
    mom "We need it only for sleeping and changing."
    pov "Sure. But another kinky picture here again. And the most perverted of all."
    scene parentsroom 8pm 005
    mom "You mean...? Yes, you're right."
    pov "You even can see her pussy."
    mom "Hmm..."
    scene parentsroom 8pm 004
    if inc == True:
        mom "Your dad and I decided that this one shouldn't be seen by your sisters."
    else:
        mom "Bruce and I decided that this one shouldn't be seen by our daughters."
    mom "But it's still art."
    pov "Haha, yes."
    pov "So you're trying new stockings for later?"
    mom "Yes I want to change something."
    jump prcinc

label prcinc:
    call screen prcinc1

screen prcinc1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1077 ypos 150 action (Hide('prcinc1'), Jump('proom8love')) hovered tt.Action ("Answer to improve Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 684 ypos 150 action (Hide('prcinc1'), Jump('proom8cor')) hovered tt.Action ("Answer to improve Corruption [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label proom8love:
    pov "That's a good idea!"
    scene parentsroom 8pm 006a
    mom "Thank you."
    pov "You're looking even better with them on."
    pov "I wasn't sure that would be possible."
    mom "You mean...?"
    if inc == True:
        pov "You're so damn beautiful mom. You're hot body packed in these clothes. Like a gift that needs to be unwrapped."
    else:
        pov "You're so damn beautiful [mother]. You're hot body packed in these clothes. Like a gift that needs to be unwrapped."
    scene parentsroom 8pm 007a
    mom "Eh...?"
    mom "Th... thank you [pov]."
    if inc == True:
        pov "No need to be shy, mom. I'm proud that my mom is such a beauty."
    else:
        pov "No need to be shy, [mother]. I'm proud that you're such a beauty."
    mom "..."
    mom "Isn't that wrong...?"
    pov "I don't think so."
    pov "I can't wait to see you later."
    mom "..."
    $ momrelationship += 1
    $ momlove += 1
    $ proom8pm = True
    $ dtime += 1
    jump parentsroom

label proom8cor:
    pov "That's a good idea! You need to look more slutty!"
    scene parentsroom 8pm 006b
    mom "What...?"
    pov "Yes for our new job it's the best to give our best."
    mom "But I wasn't suppose to..."
    if droom7momlookcor == True:
        pov "Maybe, but you forgot about something we talked about."
        mom "Eh?"
        pov "To play out roles correct, the woman should do what the man decide."
        mom "I'm not sure..."
        pov "Remove your hands!"
        mom "..."
        scene parentsroom 8pm 007b
        mom "I don't understand why this is necessary."
        pov "Because I want to see them. The hot tits of a sexy chick."
        mom "Hmm..."
        scene parentsroom 8pm 008b
        if inc == True:
            pov "Dad is so a lucky bastard! Can get his hands on them."
            mom "What are you talking about? Watch your language, son!"
        else:
            pov "Bruce is so a lucky bastard! Can get his hands on them."
            mom "What are you talking about? Watch your language, [pov]!"
        pov "No! I want to knead them."
        mom "No, that's wrong."
        scene parentsroom 8pm 009b
        pov "Maybe it's normally wrong. But in our play I decided it's not!"
        mom "But..."
        pov "No! Don't talk back all the time. It was your wish that I participate and I did."
        pov "So you'll have to play along too, or I can't do it anymore."
        mom "Okay... it's still not right but I won't complain on that anymore."
        pov "Good girl."
        mom "Hmm..."
        $ momrelationship += 1
        $ momcorruption += 1
        $ proom8pm = True
        $ dtime += 1
        jump parentsroom
    else:
        pov "Maybe, but it's still a good idea and i'm curious how you'll look in that outfit later."
        mom "Hmm..."
        $ momrelationship += 1
        $ momcorruption += 1
        $ proom8pm = True
        $ dtime += 1
        jump parentsroom


label proom24closer:
    hide screen locations
    scene parentsroom 0am 002
    if inc == True:
        pov "{i}Mom's sleeping.{/i}"
    else:
        pov "{i}[mother]'s sleeping.{/i}"
    pov "{i}Damn, she's so sexy right now. Maybe I should play a little with her?{/i}"
    jump pr24dec

label pr24dec:
    scene parentsroom 0am 002
    call screen pr24dec1

screen pr24dec1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1100 ypos 158 action (Hide('pr24dec1'), Jump('proom24love')) hovered tt.Action ("Let her sleep [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1271 ypos 158 action (Hide('pr24dec1'), Jump('proom24cor')) hovered tt.Action ("Play with her [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label proom24love:
    pov "{i}No. I can't do that. She had a long day, I should let her sleep.{/i}"
    pov "{i}But she was so tired she didn't undress clearly and even cover herself.{/i}"
    scene parentsroom 0am 007
    "You cover her up."
    pov "{i}Much better. No need that she catches a cold or worse.{/i}"
    pov "{i}Maybe she won't be so tired tomorrow.{/i}"
    $ momlove += 1
    $ dtime += 1
    jump parentsroom

label proom24cor:
    pov "{i}What should I do with her? I want to touch her, maybe jerk off too?{/i}"
    jump pr24dcor

label pr24dcor:
    call screen pr24dcor1

screen pr24dcor1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 1100 ypos 158 action (Hide('pr24dcor1'), Jump('proom24ass')) hovered tt.Action ("Play with her ass [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 1271 ypos 158 action (Hide('pr24dcor1'), Jump('proom24feet')) hovered tt.Action ("Play with her feet [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label proom24ass:
    scene parentsroom 0am 003a
    pov "{i}I can't wait. I want to play with her hot ass.{/i}"
    pov "{i}It's so damn beautiful and big. I need to touch it and now is my chance!{/i}"
    scene parentsroom 0am 004a
    pov "{i}Oh my god! I'm touching her ass cheeks.{/i}"
    pov "{i}And they're so soft and warm. Maybe I should rub my dick between them?{/i}"
    mom "Hmm..."
    pov "{i}She reacted to my touch. But she's still sleeping.{/i}"
    pov "{i}So I shouldn't over do it this time. I'll just jerk off, but I'll have to be quiet.{/i}"
    scene parentsroom 0am 005a
    pov "{i}She's so damn sexy. That hot body and so slender.{/i}"
    pov "{i}I wonder if she works out too for her role?{/i}"
    pov "{i}That make me so horny, I can't take it any longer. But I'll have to cum on her ass. She must be marked, there is no other use!{/i}"
    scene parentsroom 0am 006a
    pov "Hnnng..."
    mom "Hmm..."
    pov "{i}Damn, I'll have to be more quiet!{/i}"
    if inc == True:
        pov "{i}Don't wake up mom while I cum on you!{/i}"
        pov "{i}Dream good and more about making love with your son, hehe.{/i}"
    else:
        pov "{i}Don't wake up [mother] while I cum on you!{/i}"
        pov "{i}Dream good and more about making love with me, hehe.{/i}"
    pov "{i}Wow, that was so good.{/i}"
    $ momcorruption += 1
    $ dtime += 1
    jump parentsroom

label proom24feet:
    scene parentsroom 0am 003b
    pov "{i}I can't wait. I want to play with her sexy feet.{/i}"
    pov "{i}They're so tender and good looking in those stockings. I need to touch them and now is my chance!{/i}"
    scene parentsroom 0am 004b
    pov "{i}Oh my god! I'm touching her sexy feet.{/i}"
    pov "{i}And they're so sexy and warm. Maybe I should rub my dick between them?{/i}"
    mom "Hmm..."
    pov "{i}She reacted to my touch. But she's still sleeping.{/i}"
    pov "{i}So I shouldn't over do it this time. I'll just jerk off, but I'll have to be quiet.{/i}"
    scene parentsroom 0am 005b
    pov "{i}She's so damn sexy. The feeling of these stockings is so amazing.{/i}"
    pov "{i}And the warmth of her feet. That soft touch.{/i}"
    pov "{i}That make me so horny, I can't take it any longer. But I'll have to cum on her feet. She must be marked, there is no other use!{/i}"
    scene parentsroom 0am 006b
    pov "Hnnng..."
    mom "Hmm..."
    pov "{i}Damn, I'll have to be more quiet!{/i}"
    if inc == True:
        pov "{i}Don't wake up mom while I cum on you!{/i}"
        pov "{i}Dream good and more about making love with your son, hehe.{/i}"
    else:
        pov "{i}Don't wake up [mother] while I cum on you!{/i}"
        pov "{i}Dream good and more about making love with me, hehe.{/i}"
    pov "{i}Wow, that was so good.{/i}"
    $ momcorruption += 1
    $ dtime += 1
    jump parentsroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
