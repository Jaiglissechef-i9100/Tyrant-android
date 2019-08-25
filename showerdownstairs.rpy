

label nicolesecret:
    hide screen locations
    scene black
    "<barf> <urgh>"
    pov "{i}Someone is barfing?{/i}"
    if inc == True:
        pov "{i}Is that mom?{/i}"
    else:
        pov "{i}Is that [mother]?{/i}"
    "You follow the noise."
    scene showerdownstairs 7am shower down 001
    pov "{i}It's her. She's vomiting in the toilet.{/i}"
    mom "<barf> <urgh>"
    if inc == True:
        pov "What's wrong mom?"
    else:
        pov "What's wrong [mother]?"
    dad "She's doing this since the early morning."
    scene showerdownstairs 7am shower down 002
    if inc == True:
        pov "Huh? You scared me dad."
    else:
        pov "Huh? You scared me Bruce."
    dad "She woke up in the middle of the night to vomit."
    pov "So she has problems with her stomach maybe?"
    dad "The last time I saw her vomit that bad was when she tried the sex-drug accidentally."
    pov "The sex-drug let her vomit?"
    dad "She's allergic to one of the ingredients."
    pov "Oh..."
    scene showerdownstairs 7am shower down 003
    dad "You were with here last night. You didn't her gave one, didn't you?"
    pov "What? No! What do you think of me?"
    pov "{i}Oh shit!{/i}"
    scene showerdownstairs 7am shower down 004
    dad "Good, so then she must have eaten something wrong or drank to much."
    dad "I hope she's feeling better soon."
    pov "{i}So, she's allergic to the sex-drug and can't use it.{/i}"
    if NTR == True:
        pov "{i}But then she never gets drugged and just enjoy to do kinky things.{/i}"
        pov "{i}Damn it!{/i}"
    pov "{i}But good to know for my further doings.{/i}"
    scene black
    "You leave after you discovered a secret."
    $ momsecret = True
    $ dtime += 1
    jump droom


label showerd10look:
    hide screen locations
    scene black
    pov "{i}I can't see anything. There's no lock?{/i}"
    jump showerdown

label showerd10listen:
    hide screen locations
    scene main shower door downstairs
    pov "{i}Someone is in the shower.{/i}"
    jump showerdown


label showerd10open:
    hide screen locations
    if dtime == 10:
        scene main shower door downstairs
        pov "{i}Maybe...{/i}"
        scene showerdownstairs 10am 001
        pov "{i}Oh. [bs] is cleaning herself from the drink, and she used the shower here.{/i}"
        if inc == True:
            pov "{i}But why, this door has no lock. I must ask mom about it.{/i}"
        else:
            pov "{i}But why, this door has no lock. I must ask [mother] about it.{/i}"
        jump sd10in
    elif dtime == 15:
        scene main shower door downstairs
        pov "{i}Maybe...{/i}"
        if momrelationship <= 5 and NTR == True:
            jump showerd15ntr
        scene showerdownstairs 3pm 001
        if inc == True:
            pov "{i}Mom is showering.{/i}"
        else:
            pov "{i}[mother] is showering.{/i}"
        pov "{i}But why, this door has no lock. I must ask her about it.{/i}"
        jump sd15in


label sd10in:
    scene showerdownstairs 10am 001
    call screen sd10in1

screen sd10in1():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1082 ypos 396 action (Hide('sd10in1'), Jump('showerd10looktits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1019 ypos 839 action (Hide('sd10in1'), Jump('showerd10lookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        if showerd10tits == True and showerd10crotch == True:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1121 ypos 65 action (Hide('sd10in1'), Jump('showerd10watch')) hovered tt.Action ("Watch longer") focus_mask True
        frame:
            xalign .5
            text tt.value

label showerd10looktits:
    scene showerdownstairs 10am 002
    pov "{i}Oh my god, they are so firm and big.{/i}"
    pov "{i}And she has nipple rings.{/i}"
    $ showerd10tits = True
    jump sd10in

label showerd10lookcrotch:
    scene showerdownstairs 10am 003
    pov "{i}And her crotch, so sexy. And a sexy landing strip.{/i}"
    pov "{i}A nice belly piercing too.{/i}"
    $ showerd10crotch = True
    jump sd10in

label showerd10watch:
    scene showerdownstairs 10am 004
    pov "{i}Yes show me more of your hot body.{/i}"
    pov "{i}Oh this is risky, if she opens her eyes I'm dead. Better go.{/i}"
    $ kitchenmix9 = False
    $ dtime += 1
    jump showerdown



label sd15in:
    hide screen locations
    scene showerdownstairs 3pm 001
    call screen sd15in1

screen sd15in1():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 585 ypos 446 action (Hide('sd15in1'), Jump('showerd15looktits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 639 ypos 869 action (Hide('sd15in1'), Jump('showerd15lookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        if showerd15tits == True and showerd15crotch == True:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1121 ypos 65 action (Hide('sd15in1'), Jump('showerd15watch')) hovered tt.Action ("Watch longer") focus_mask True
        frame:
            xalign .5
            text tt.value

label showerd15looktits:
    scene showerdownstairs 3pm 002
    pov "{i}Oh my god, they are so huge.{/i}"
    pov "{i}I want to knead them. And use them as pillows.{/i}"
    $ showerd15tits = True
    jump sd15in

label showerd15lookcrotch:
    scene showerdownstairs 3pm 003
    pov "{i}And her crotch, so sexy. And a sexy landing strip.{/i}"
    pov "{i}I want to see her pussy so badly.{/i}"
    $ showerd15crotch = True
    jump sd15in

label showerd15watch:
    scene showerdownstairs 3pm 004
    mom "Ohh... Ahh..."
    pov "{i}Oh my god... Is she...?{/i}"
    mom "Hmm..."
    pov "{i}Ah no. She's just enjoying the hot shower.{/i}"
    pov "{i}But that wonderful body. I wish I could join her.{/i}"
    scene showerdownstairs 3pm 005
    pov "{i}And that wonderful big ass.{/i}"
    pov "{i}I wonder how my dick would feel between her cheeks?{/i}"
    pov "{i}Oh I think she's nearly done. I should go. If she caught me here I would be so dead.{/i}"
    if momcorruption > 20 or momlove > 30:
        jump showerd15choice
    $ dtime += 1
    jump showerdown


label showerd15choice:
    scene showerdownstairs 3pm 006
    mom "Huh?"
    pov "Oh shit!"
    scene showerdownstairs 3pm 007
    mom "Aaah... [pov]! What are you doing here?"
    pov "{i}What to do now? I should choose fast!{/i}"
    call screen shower15choice2

screen shower15choice2():
    default tt = Tooltip (" ")
    fixed:
        if momcorruption > 20:
            imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1314 ypos 275 action (Hide('shower15choice2'), Jump('showerd15cor')) hovered tt.Action ("Dominate her [cr1]") focus_mask True
        if momlove > 30:
            imagebutton auto "gui/icons/icon_love_%s.png" xpos 564 ypos 275 action (Hide('shower15choice2'), Jump('showerd15love')) hovered tt.Action ("Excuse yourself [lv1]") focus_mask True

        frame:
            xalign .5
            text tt.value

label showerd15cor:
    $ momcorruption += 1
    $ momrelationship += 1
    if inc == True:
        pov "I came to see you, mom!"
    else:
        pov "I came to see you, [mother]!"
    scene showerdownstairs 3pm 008a
    mom "What...?"
    pov "I heard you running the shower and I want to see you."
    mom "..."
    pov "So go on and remove your hands."
    scene showerdownstairs 3pm 009a
    mom "Hnn..."
    pov "Very nice! Your hot body all wet."
    pov "Now continue showering, I want to enjoy watching you!"
    mom "Please go..."
    pov "Haha, no. It's your own fault showering in a room without a lock on the door."
    mom "Hnn..."
    scene showerdownstairs 3pm 010a
    "She continues showering."
    pov "You're showering here because you want to been seen, don't you?"
    mom "It wasn't for you."
    pov "But I took my chance and it was a good idea!"
    scene showerdownstairs 3pm 011a
    mom "Hnn..."
    pov "{i}She's still uncomfortable, but at least she's doing it. I'll make her get used to it.{/i}"
    if inc == True:
        pov "You're so sexy with your shining body, mom!"
    else:
        pov "You're so sexy with your shining body, [mother]!"
    mom "Stop talking like that."
    pov "It was a damn fine idea to remove the lock of this door!"
    mom "Hnn..."
    pov "Go on, don't be ashamed. Your tits could use more cleaning!"
    scene showerdownstairs 3pm 012a
    mom "..."
    pov "{i}Damn, I'm getting so horny right now.{/i}"
    pov "Are your nipples getting hard? You enjoy me watching that much?"
    mom "No, they don't... What are you talking about?"
    pov "{i}Argh, now I want to touch them so badly.{/i}"
    scene showerdownstairs 3pm 013a
    mom "I'm done. You can leave now!"
    pov "{i}Oh, she's trying to cheat on me.{/i}"
    pov "Oh I don't think that was a proper shower."
    mom "But I'm clean and don't need to shower more."
    scene showerdownstairs 3pm 014a
    pov "Oh you won't get away that easily. Putting up a show and then stopping so abruptly!"
    mom "What do you mean?"
    pov "I'll help you clean yourself!"
    "You start to undress."
    if momcorruption < 35:
        scene showerdownstairs 3pm 015a
        mom "Are you fucking crazy?!"
        pov "{i}Oh shit, too soon!{/i}"
        mom "Who do you think you are? You better leave now!"
        pov "{i}Damn, I need to corrupt her more!{/i}"
        $ dtime += 1
        $ shower15corfirst = True
        jump showerdown
    mom "You... can't be... serious..."
    "As you strip naked you enter the shower."
    scene showerdownstairs 3pm 016a
    pov "They're still in very good shape and give my hands a wonderful feeling."
    if inc == True:
        pov "You can be proud mom!"
    else:
        pov "You can be proud [mother]!"
    mom "Stop..."
    pov "Yes I'll stop. After I have cleaned your body well!"
    mom "Hnn..."
    scene showerdownstairs 3pm 017a
    pov "As I thought, you're enjoying my cleaning."
    mom "We shouldn't be doing this."
    if inc == True:
        "Why? I'm just helping my mom to get clean."
    else:
        "Why? I'm just helping you to get clean."
    pov "{i}She's still fighting back. Time for a lesson.{/i}"
    scene showerdownstairs 3pm 018a
    mom "Hah... hnn..."
    mom "Not so... rough..."
    pov "They need a good scrubbing to get clean!"
    mom "Please... go slower..."
    pov "{i}Oh so no stopping anymore?{/i}"
    if inc == True:
        pov "Trust me mom. I know what they need."
    else:
        pov "Trust me [mother]. I know what they need."
    scene showerdownstairs 3pm 019a
    mom "Hah... hah..."
    pov "See? I was right. A good rub helps every time."
    mom "Hnn..."
    pov "Now that I have cleaned this part of your body, time for another spot!"
    mom "Another... hah..."
    scene showerdownstairs 3pm 020a
    pov "Yes! Your body needs to get completely clean."
    mom "Wait!"
    pov "Ssshh... it's needless to complain all the time. I'll finish what I started!"
    scene showerdownstairs 3pm 021a
    mom "Hah..."
    pov "You like me cleaning you there?"
    mom "I... I was just surprised by your touch..."
    pov "You're still lying about it? Your moaning betrayed you!"
    mom "But, hah... hnn..."
    pov "Just enjoy it. It's all natural."
    scene showerdownstairs 3pm 022a
    mom "Hnn... hmm..."
    pov "{i}Finally she gave up and admits it.{/i}"
    pov "So... a little more on this spot."
    mom "Hmm! Hmm!"
    pov "{i}What a wonderful view. Seeing her enjoy it while I'm rubbing her clit.{/i}"
    scene showerdownstairs 3pm 023a
    pov "{i}Time for more{/i}"
    mom "Aaahh... hah..."
    pov "{i}Now that was a surprise, haha...{/i}"
    pov "Just another spot to clean."
    scene showerdownstairs 3pm 024a
    mom "Hah... hah... hah..."
    pov "I should help you more often with cleaning, you like it very much."
    mom "Hah... your fingers... hnn..."
    pov "... give you a good feeling. I know!"
    pov "{i}Oh, she's shaking. But I need more!{/i}"
    scene showerdownstairs 3pm 025a
    pov "So this spot is clean now too."
    mom "Hnn... so we're done..."
    pov "{i}She sounds disappointed. Nice!{/i}"
    pov "No. Move around, time for your back."
    mom "O... OK."
    scene showerdownstairs 3pm 026x
    mom "..."
    pov "{i}What...? She's staring at my dick?{/i}"
    scene showerdownstairs 3pm 027x
    pov "{i}Yes take a good look. It's all hard for you, haha.{/i}"
    scene showerdownstairs 3pm 026a
    mom "You will only... clean... my back?"
    pov "Yes, as I said. You need to be clean."
    "She stares at you a moment longer."
    scene showerdownstairs 3pm 028a
    pov "Good, push your back out so I can reach it easier."
    pov "{i}That hot ass. Now it's time for more fun!{/i}"
    scene showerdownstairs 3pm 028x
    mom "Hnn!"
    if inc == True:
        pov "Relax mom! I've just started with your back."
    else:
        pov "Relax [mother]! I've just started with your back."
    pov "{i}Did she notice it? She's standing all still.{/i}"
    pov "Just hold out more. Your back will get a special cleaning."
    scene showerdownstairs 3pm 029x
    pov "{i}What a nice feeling! So which hole should I use?{/i}"
    mom "Hnnnnn..."
    pov "{i}Now she knows it for sure!{/i}"
    pov "Just relax!"
    mom "S... Stop!"
    scene showerdownstairs 3pm 030a
    mom "This is too much!"
    pov "{i}What the hell?{/i}"
    pov "We're not done yet!"
    mom "You had your fun but we need to stop here."
    if basement10pmnicoleouting == True and mombasementcorsecond == True:
        jump showerd15fuckslut
    pov "{i}Damn, still not corrupted enough?{/i}"
    pov "We can't. Your moaning made me all hard, I need to relieve myself."
    scene showerdownstairs 3pm 031a
    pov "And you need to help me!"
    mom "But..."
    pov "No! I helped you clean and now you need to help me."
    pov "Even if I finished my cleaning properly."
    mom "I... I..."
    scene showerdownstairs 3pm 032a
    pov "Go on. So we can finish showering."
    pov "{i}She prevented the fucking so she'll choose the easier way to satisfy me.{/i}"
    mom "Hnn... OK. Then we can finish."
    pov "Yes, when my hardness is gone we're equal."
    scene showerdownstairs 3pm 033a
    pov "Oh..."
    pov "{i}That soft and tight touch.{/i}"
    pov "Yes, with your tight grip I'll cum in no time!"
    mom "Hnn..."
    pov "And your big boobs give me some more motivation."
    scene showerdownstairs 3pm 034a
    pov "You're doing very good. Can you feel my dick pulsating?"
    mom "Hmm..."
    if inc == True:
        pov "I'm proud to have such a good mom who's helping me out after we enjoyed a shower together."
    else:
        pov "I'm proud to have such a good girl who's helping me out after we enjoyed a shower together."
    mom "Hnn..."
    pov "We'll repeat this more often so you can get used to it and we can finish our cleaning the proper way like I wanted to do before."
    mom "Hnn!"
    pov "{i}Her grip is getting so tight, I'm sure she'll be ready for more soon.{/i}"
    if inc == True:
        pov "Yes, that's it, mom!"
    else:
        pov "Yes, that's it [mother]!"
    scene showerdownstairs 3pm 035a
    pov "Aaahhh! Yes...!"
    mom "Hnn...!"
    if inc == True:
        pov "Milk me until I'm dry mom!"
    else:
        pov "Milk me until I'm dry [mother]!"
    pov "{i}Ha, now I've dirtied her. So we need to start again. But I'm sure she'd kill me then, haha.{/i}"
    scene showerdownstairs 3pm 036a
    pov "Wow, stop. Don't be ashamed!"
    mom "..."
    pov "It wasn't a big thing. Just like a deal! I washed you and you thanked me for it."
    mom "Hnn..."
    if inc == True:
        pov "You just rewarded me for being a good son."
    else:
        pov "You just rewarded me for being a good boy."
    pov "Like the way it should always be. And you liked it too, I know it."
    mom "I... I lik..."
    scene black
    "She storms off."
    pov "{i}I almost had her...{/i}"
    $ dtime += 1
    $ shower15corsecond = True
    jump showerdown

label showerd15love:
    $ momlove += 1
    $ momrelationship += 1
    if inc == True:
        pov "I'm so sorry mom. I was in thoughts when I opened the door."
    else:
        pov "I'm so sorry [mother]. I was in thoughts when I opened the door."
    scene showerdownstairs 3pm 008b
    mom "Oh..."
    pov "I wanted to ask you something and now I forgot it..."
    mom "Oh..."
    pov "{i}What she's doing? Should I be scared?{/i}"
    scene showerdownstairs 3pm 009b
    mom "Oh, then you can calm down. This can happen to anybody."
    pov "{i}What? Why did she just stop hiding herself?{/i}"
    pov "Eh...?"
    mom "What's wrong [pov]? You're looking shocked?"
    if inc == True:
        pov "I... I can see you mom."
    else:
        pov "I... I can see you [mother]."
    mom "<giggle> Come on. You never saw a naked woman before?"
    pov "What? Of course I have."
    scene showerdownstairs 3pm 010b
    mom "So what's the stutter then? We're just talking together."
    pov "{i}I can't believe it. Why is this happening?{/i}"
    if inc == True:
        mom "Or are you feeling uncomfortable seeing your mother naked?"
    else:
        mom "Or are you feeling uncomfortable seeing your mother's best friend naked?"
    pov "No... just surprised?"
    scene showerdownstairs 3pm 011b
    mom "I can understand you. But I know that you're a good boy with manners so I can trust you."
    pov "{i}Oh that's the reason.{/i}"
    mom "You aren't like the other \"pigs\" of men, so I can be proud of you."
    pov "{i} Oh no... saying this to me standing there all naked and wet.{/i}"
    scene showerdownstairs 3pm 012b
    mom "I'm very proud of you, have I told you that?"
    pov "Yes, you have."
    pov "{i}Almost every time we talk.{/i}"
    "You fall silent and stare at her."
    pov "{i}What a fine and beautiful body. And I'm her precious now. I shouldn't ruin it.{/i}"
    scene showerdownstairs 3pm 013b
    mom "What happened? You're so quiet."
    pov "I enjoy your praising."
    mom "Haha, then it's good I could make you happy."
    pov "{i}You made me happy another way, but I shouldn't tell you that now.{/i}"
    if inc == True:
        "Yes, thank you mom!"
    else:
        "Yes, thank you [mother]!"
    if momlove < 50:
        mom "It was nice talking with you [pov]. But I finished showering so you can leave."
        pov "Oh... OK."
        pov "{i}I'm so damn lucky and a good boy too, haha.{/i}"
        $ shower15lovefirst = True
        $ dtime += 1
        jump showerdown
    mom "Hmm... maybe you can help me?"
    pov "Help you?"
    scene showerdownstairs 3pm 014b
    mom "You can earn yourself more praise when you help me with my back."
    pov "Your back?"
    mom "I heard that back rubbing could reanimate the urge and I wanted to try it for so long."
    pov "So I should rub your back?"
    mom "Yes! Bruce isn't here so you can do that. I know you'll behave."
    pov "{i}Oh... my... god...{/i}"
    pov "But when the shower is running..."
    scene showerdownstairs 3pm 015b
    mom "<giggle> Then your clothes will get wet."
    mom "You have to take them off of course."
    pov "So, all naked?"
    mom "Do I scare you so much? <giggle>"
    pov "No..."
    mom "Then stop talking and join me."
    scene showerdownstairs 3pm 016b
    "You undress and get into the shower."
    pov "{i}We're both naked in the shower and I'm so close to her.{/i}"
    pov "{i}How should I withstand the temptation. But I must manage it. We have such a good relationship.{/i}"
    scene showerdownstairs 3pm 017b
    pov "{i}Oh, oh. This isn't helping.{/i}"
    mom "What are you waiting for [pov]? Just start with my shoulders and then go down."
    if inc == True:
        pov "O... OK mom."
    else:
        pov "O... OK [mother]."
    scene showerdownstairs 3pm 018b
    mom "Yes, just like that."
    pov "But I have no idea about massaging."
    mom "You don't need to know massaging. Just rub and knead it so I can relax."
    mom "You'll know it soon enough if you hurt me <giggle>"
    pov "Oh I won't hurt you!"
    mom "I know [pov]... hnn..."
    pov "{i}Oh, now she's even moaning. Just be a good boy...{/i}"
    mom "You can go lower now."
    scene showerdownstairs 3pm 019b
    if inc == True:
        pov "{i}Just calm down, don't think about it, that I'm naked in the shower with mom.{/i}"
    else:
        pov "{i}Just calm down, don't think about it, that I'm naked in the shower with [mother].{/i}"
    pov "Am I doing it right?"
    mom "Yes... hah... it feels so good..."
    pov "{i}Your moaning isn't helping me.{/i}"
    mom "Go even lower please... hnn..."
    pov "Are you sure?"
    mom "Yes go on please."
    scene showerdownstairs 3pm 020b
    pov "{i}Oh boy. I'm on her ass now.{/i}"
    mom "Such a good feeling, hah..."
    pov "{i}Oh shit. I can't hold myself down any longer.{/i}"
    mom "What I have missed all... hnn... the time."
    scene showerdownstairs 3pm 021b
    mom "Hnn... hah..."
    pov "Should I go back up."
    mom "No just continue... hnn..."
    pov "{i}Oh no. I poked her with my dick. She'll get mad that I couldn't behave good.{/i}"
    "You freeze."
    mom "What...?"
    scene showerdownstairs 3pm 022b
    mom "Oh..."
    mom "It's OK. You did very good."
    pov "{i}She must have noticed my hard dick poking her. But why isn't she angry?{/i}"
    mom "That was so a good feeling you should try it too."
    pov "Wait. You mean...?"
    scene showerdownstairs 3pm 023b
    mom "Yes, now we'll change. I'll rub you now and you can enjoy."
    pov "{i}She wants to rub me? But I'm already hard.{/i}"
    pov "O... OK. If you want to."
    mom "Yes, your muscles should get relaxed too. Just move around."
    scene showerdownstairs 3pm 024b
    pov "{i}I should enjoy this, but I also have a bad feeling.{/i}"
    mom "Do you feel it? Just rubbing with the hot water does it."
    if inc == True:
        pov "Oh yes, it's really good mom."
    else:
        pov "Oh yes, it's really good [mother]."
    mom "Then just enjoy my hands on you."
    pov "{i}Oh I enjoy this, but in another way that you pretend to.{/i}"
    scene showerdownstairs 3pm 025b
    pov "Huh?"
    mom "Since you're a man I'll rub your chest too."
    pov "{i}Oh my god. She's pressing her tits on my back and keeps rubbing me. What she's up to?{/i}"
    mom "I can feel your body relaxing. Good that you can enjoy it to."
    pov "Y... yes, I...do."
    scene showerdownstairs 3pm 026b
    pov "{i}She's getting even lower. What if she touches my dick accidentally.{/i}"
    mom "You're so tense yourself, you should relax more."
    pov "I try."
    pov "{i}Should I cum then or will she kill me then?{/i}"
    mom "Now it's time to finish it."
    scene showerdownstairs 3pm 027b
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    mom "Ssshhh, just relax and let me help you [pov]."
    image handjob_showerdown = Movie(channel="handjob_showerdown", play="images/anim/handjob_showerdown.webm")
    scene handjob_showerdown with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    pov "But why are you touching my dick?"
    mom "I felt you getting hard and poking me accidentally. But even then you behaved and showed some good manners."
    if inc == True:
        mom "So it's my reward to help my good son after you withstood your urges."
    else:
        mom "So it's my reward to help my good boy after you withstood your urges."
    pov "{i}Damn, is she into me? I could hardly believe that it's just about that good boy thing.{/i}"
    pov "Aaah, hah..."
    mom "Good. Just enjoy my touching and relieve yourself when you need to."
    if inc == True:
        pov "Hah, your hands are so soft mom."
    else:
        pov "Hah, your hands are so soft [mother]."
    mom "So you can feel good like I did before from your hands."
    pov "Oh yes I do!"
    pov "{i}Damn, she's even playing with my balls. I can't hold much longer!{/i}"
    if basement10pmnicoleouting == True and mombasementlovesecond == True:
        jump showerd15fucklove
    scene showerdownstairs 3pm 029b
    if inc == True:
        pov "Aaaah... MOM!"
    else:
        pov "Aaaah... [mother]!"
    mom "Good, just spurt everything out."
    pov "Oh yes! Ahh... hah..."
    mom "You enjoyed it, your penis is getting limp."
    pov "Yes, oh..."
    scene showerdownstairs 3pm 030b
    pov "W... why?"
    mom "Maybe I gave you too strong a burden and you can't restrain your urges."
    mom "So I wanted to help you too. I know the pain you can get when you can't release yourself."
    pov "But you wanked me off."
    mom "Maybe because I liked your penis? <giggle>"
    if inc == True:
        pov "Haha. Mom!"
    else:
        pov "Haha. [mother]!"
    mom "But you liked it?"
    pov "I loved it!"
    scene showerdownstairs 3pm 031b
    mom "Good then it's easier for you to keep this as our secret."
    if inc == True:
        pov "Of course mom!"
    else:
        pov "Of course [mother]!"
    pov "{i}I'm confused and feel like a toy. But she won't do that to me, I'm sure.{/i}"
    pov "{i}Maybe I've grown up to be the man she would like to have, maybe Bruce isn't like that?{/i}"
    scene black
    "She leave the shower and you stand there some time still naked and confused."
    $ dtime += 1
    $ shower15lovesecond = True
    jump showerdown

label showerd15ntr:
    scene black
    "You open the door."
    call screen showerd15ntrchoice

screen showerd15ntrchoice():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 580 ypos 330 action (Hide('shower15choice2'), Jump('showerd15ntrlove')) hovered tt.Action ("Like NTR") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1150 ypos 330 action (Hide('shower15choice2'), Jump('showerd15ntrhate')) hovered tt.Action ("Hate NTR") focus_mask True

        frame:
            xalign .5
            text tt.value

label showerd15ntrlove:
    $ ntrlovenic = True
    jump showerd15ntr2

label showerd15ntrhate:
    $ ntrhatenic = True
    jump showerd15ntr2

label showerd15ntr2:
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene showerdownstairs 3pm 005n
    mom "Oh... Aaahh..."
    if ntrlovenic == True:
        if inc == True:
            pov "{i}Oh mom has a guest.{/i}"
        else:
            pov "{i}Oh [mother] has a guest.{/i}"
        pov "{i}It seems like she can't wait until evening.{/i}"
    else:
        pov "{i}Oh no! This can't be true.{/i}"
        pov "{i}Why is he here now?{/i}"
    scene showerdownstairs 3pm 006n
    pov "{i}Oh...?{/i}"
    mom "Huh?"
    davide "What's up slut?"
    scene showerdownstairs 3pm 007n
    mom "We need to stop, let me down!"
    davide "What the hell? There's no way that I'm going to stop now!"
    if ntrlovenic == True:
        pov "{i}She's getting angry that I'm watching. But I'd love to see her getting screwed.{/i}"
    else:
        pov "{i}She wants to stop. Why is this idiot going on? Did he force her?{/i}"
    mom "Someone is watching us!"
    davide "Really? Let's see."
    scene showerdownstairs 3pm 008n
    davide "Oh hey [pov]! So you really need to watch us?"
    mom "Stop it! Let me down now!"
    if ntrlovenic == True:
        pov "Yes! I want to see her screaming, haha."
        davide "I can understand that, haha."
    else:
        pov "..."
        pov "{i}When she wants to stop you should let her, asshole!{/i}"
    davide "She likes it too even if she denies it. She's getting tighter."
    mom "Stop this bullshit!"
    scene showerdownstairs 3pm 009n
    davide "As I said before, I won't stop now. Not until we've had good sex together and I released my junk in you!"
    mom "I said no!"
    davide "Yes you do, but your body say yes! So use your mouth only for moaning and prepare for a hard fuck!"
    if ntrlovenic == True:
        if inc == True:
            pov "He's right mom. You could use a hard pounding to calm down, haha."
        else:
            pov "He's right [mother]. You could use a hard punding to calm down, haha."
    else:
        if inc == True:
            pov "{i}Does he really want to rape my mom in front of me?{/i}"
        else:
            pov "{i}Does he really want to rape her in front of me?{/i}"
    scene showerdownstairs 3pm 011n
    mom "Let me go! I don't want an audience!"
    davide "Shut up slut! You'll get it even harder now!"
    if ntrlovenic == True:
        pov "Good, continue now. I want to see something!"
    else:
        pov "{i}Wait... She doesn't want an audience? So she wanted to go on with this asshole?{/i}"
        pov "{i}I hope I heard something wrong. Why should she enjoy sex with this idiot?{/i}"
    scene showerdownstairs 3pm 012n
    mom "Hah... hnn... you idiot..."
    pov "{i}He's fucking her hard.{/i}"
    davide "See [pov]? Taking the slut hard shuts her up!"
    if ntrlovenic == True:
        pov "I see. And I'm sure in no time she'll love it too! That hot body needs to be screwed often!"
        if inc == True:
            davide "Haha, you heard that? Even your own son is on my side."
        else:
            davide "Haha, you heard that? Even [pov] is on my side."
    else:
        pov "..."
        pov "{i}You damn asshole! Stop this now! I'll kill you!{/i}"
        davide "Hmm, look he seems confused. Maybe he wants to join us?"
    scene showerdownstairs 3pm 013n
    mom "No... hah...hah..."
    davide "You're enjoying your live-porn, haha?"
    mom "Aaah... so rough... hah... hah..."
    if ntrlovenic == True:
        pov "Yes this is damn hot. And [mother] is enjoying this now."
        if inc == True:
            "You're lika a hot porn-star mom!"
        else:
            "You're like a hot porn-star [mother]!"
    else:
        pov "{i}No, I don't want to see this anymore. She's liking it but doesn't want me to know!{/i}"
        pov "{i}But I won't leave, I'm afraid what that asshole might do with her when they're alone.{/i}"
        pov "{i}If I was stronger I could interfere!{/i}"
    davide "See [mother]? [pov] is enjoying his show!"
    scene showerdownstairs 3pm 014n
    "Suddenly [mother] holds herself on you, preventing herself from fall over."
    mom "Go slower, I'll fall, hah..."
    davide "I don't care slut! Take my dick!"
    mom "Hah... hah... aaah..."
    scene showerdownstairs 3pm 015n
    if ntrlovenic == True:
        if inc == True:
            pov "You're so close mom. Moaning in my face! I'm glad you're enjoying your hard fuck."
        else:
            pov "You're so close [mother]. Moaning in my face! I'm glad you're enjoying your hard fuck."
    else:
        pov "{i}This is like punishment. The women I love moaning direct in my face. I must see how she's enjoying it.{/i}"
    mom "He's so big and rough [pov], hah..."
    davide "Oh you're giving him an even better show now. Good that way you can enjoy this now slut!"
    mom "Yes' it's good! Hah... I was wrong, do me harder!"
    if ntrlovenic == True:
        pov "So nice! I want to join someday too!"
        davide "Good idea! That way you can ride the slut even harder!"
        mom "Harder? Hah... aaahh..."
    else:
        pov "{i}No, stop talking. You're out of senses because he's raping you so hard!{/i}"
        if inc == True:
            pov "{i}There's no way that my mom would like having sex with that pig.{/i}"
        else:
            pov "{i}There's no way that my mom would like having sex with that pig.{/i}"
    scene showerdownstairs 3pm 016n
    mom "Aaaah... haaaahh... YES!"
    davide "Oh? The slut is coming?"
    mom "Yes! Harder! HARDER!"
    if ntrlovenic == True:
        if inc == True:
            pov "Yes mom! Let me see you cumming. Prove to me that you love hard, rough sex!"
        else:
            pov "Yes [mother]! Let me see you cumming. Prove to me that you love hard, rough sex!"
    else:
        pov "{i}That fucking asshole. Stealing her away from me. I'll get my revenge and show her that I'm much better.{/i}"
        pov "{i}Maybe he drugged her?{/i}"
    davide "Take my junk!"
    mom "Haaahh..."
    scene showerdownstairs 3pm 017n
    "She knelt down in the bath-tub."
    mom "Hah... hah... hah..."
    davide "So you had very much fun, haha..."
    scene showerdownstairs 3pm 018n
    davide "You noticed? At first she was bitchy and in the end she praised me for the rough fucking."
    if ntrlovenic == True:
        pov "Yes. A good show. That's something I need to try with her too sometimes."
        davide "Haha, then good luck."
    else:
        pov "..."
        pov "{i}Fuck you, you fucking fuck!{/i}"
    if ntrlovenic == True:
        scene showerdownstairs 3pm 019n
        if inc == True:
            pov "Oh mom. That was so hot, seeing you cumming hard!"
        else:
            pov "Oh [mother]. That was so hot, seeing you cumming hard!"
        mom "Hah...hnn..."
        pov "And your nice reaction when Davide suggested a threesome."
        mom "Please leave."
        pov "{i}Oh she's so confused.{/i}"
        scene black
        "You leave the bathroom."
        $ dtime += 1
        if gamemusic == True:
            stop music fadeout 2
            play music "music/default.mp3"
        jump showerdown
    else:
        scene showerdownstairs 3pm 020n
        mom "Leave now [pov]! You weren't suppose to watch us! What are you thinking?"
        pov "But..."
        pov "{i}Now it's my fault that I just wanted to be sure that he wouldn't hurt her more?{/i}"
        mom "No you heard me! I'm very angry!"
        pov "{i}I can't believe this! That's not fair!{/i}"
        scene black
        "You leave the bathroom."
        $ dtime += 1
        if gamemusic == True:
            stop music fadeout 2
            play music "music/default.mp3"
        jump showerdown
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
