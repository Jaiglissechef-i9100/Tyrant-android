#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. Time Location - Featured - Scenes
#----- End List -----

label nicolesecret:
    hide screen locations
    scene black
    "<barf> <urgh>"
    povi "Someone is barfing?"
    if inc == True:
        povi "Is that mom?"
    else:
        povi "Is that [mother]?"
    "You follow the sounds of vomit."
    scene showerdownstairs 7am shower down 001
    povi "It's her alright. She's vomiting in the toilet."
    mom "<barf> <urgh>"
    if inc == True:
        pov "What's wrong mom?"
    else:
        pov "What's wrong [mother]?"
    dad "She's been doing this since early this morning."
    scene showerdownstairs 7am shower down 002
    if inc == True:
        pov "Huh? You scared me dad."
    else:
        pov "Huh? You scared me Bruce."
    dad "She woke up in the middle of the night to vomit."
    pov "So does she have problems with her stomach maybe?"
    dad "The last time I saw her vomit that bad was when she tried the sex-drug accidentally."
    pov "The sex-drug makes her vomit?"
    dad "She's allergic to one of the ingredients."
    pov "Oh..."
    scene showerdownstairs 7am shower down 003
    dad "You were here with her last night. You didn't her gave one, didn't you?"
    pov "What? No! What kind of man to you think I am?"
    povi "Oh shit!"
    scene showerdownstairs 7am shower down 004
    dad "Good, she possible ate something bad or drank too much."
    dad "I hope she feels better soon."
    povi "So, she's allergic to the sex-drug and can't use it."
    if NTR == True:
        povi "But then if she never gets drugged, does she just pretend to enjoy doing kinky things?"
        povi "Damn!"
    povi "But that's good to know just in case."
    scene black
    "You leave after you discovered her secret."
    $ momsecret = True
    $ dtime += 1
    jump droom

label showerd10look:
    hide screen locations
    scene black
    povi "I can't see anything. There's no lock on this door?"
    jump showerdown

label showerd10listen:
    hide screen locations
    scene main shower door downstairs
    povi "Someone is in the shower."
    jump showerdown

label showerd10open:
    hide screen locations
    if dtime == 10:
        scene main shower door downstairs
        povi "Maybe..."
        scene showerdownstairs 10am 001
        povi "Oh. [bs] is cleaning herself after spilling the drink, and she used the shower down here."
        if inc == True:
            povi "But why does this door have no lock. I should ask mom about it."
        else:
            povi "But why does this door have no lock. I should ask [mother] about it."
        jump sd10in
    elif dtime == 15:
        scene main shower door downstairs
        povi "Maybe..."
        if momrelationship <= 5 and NTR == True:
            jump showerd15ntr
        scene showerdownstairs 3pm 001
        if inc == True:
            povi "Mom is showering."
        else:
            povi "[mother] is showering."
        povi "But why does this door has no lock. I need to ask her about it."
        jump sd15in

label sd10in:
    scene showerdownstairs 10am 001
    call screen sd10in1

screen sd10in1():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('sd10in1'), Jump('showerd10looktits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('sd10in1'), Jump('showerd10lookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        if showerd10tits == True and showerd10crotch == True:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('sd10in1'), Jump('showerd10watch')) hovered tt.Action ("Watch longer") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerd10looktits:
    scene showerdownstairs 10am 002
    povi "Oh my god, they are so big and firm."
    povi "Wow! She has nipple rings."
    $ showerd10tits = True
    jump sd10in

label showerd10lookcrotch:
    scene showerdownstairs 10am 003
    povi "And her crotch, so sexy. There is even a sexy little landing strip."
    povi "A nice belly piercing too."
    $ showerd10crotch = True
    jump sd10in

label showerd10watch:
    scene showerdownstairs 10am 004
    povi "Yes please. Show me more of your hot body!"
    povi "Oh this is getting risky, if she opens her eyes I'm dead. Better go."
    $ kitchenmix9 = False
    $ dtime += 1
    jump showerdown

label sd15in:
    hide screen locations
    scene showerdownstairs 3pm 001
    call screen sd15in1

screen sd15in1():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('sd15in1'), Jump('showerd15looktits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('sd15in1'), Jump('showerd15lookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        if showerd15tits == True and showerd15crotch == True:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('sd15in1'), Jump('showerd15watch')) hovered tt.Action ("Watch longer") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerd15looktits:
    scene showerdownstairs 3pm 002
    povi "Oh my god, they are so huge."
    povi "I want to knead them or just use them as pillows."
    $ showerd15tits = True
    jump sd15in

label showerd15lookcrotch:
    scene showerdownstairs 3pm 003
    povi "And her crotch, so sexy. There is even a sexy little landing strip."
    povi "I want to see her pussy so badly."
    $ showerd15crotch = True
    jump sd15in

label showerd15watch:
    scene showerdownstairs 3pm 004
    mom "Ohh... Ahh..."
    povi "Oh my god... Is she...?"
    mom "Hmm..."
    povi "Ah no. She's just enjoying the hot shower."
    povi "But that wonderful body. I wish I could join her."
    scene showerdownstairs 3pm 005
    povi "And that wonderful ass."
    povi "I wonder how my dick would feel between her cheeks?"
    povi "Oh I think she's nearly done. I should go. If she caught me here I would be so dead."
    if momcorruption > 20 or momlove > 30:
        jump showerd15choice
    $ dtime += 1
    jump showerdown

label showerd15choice:
    scene showerdownstairs 3pm 006
    mom "Huh?"
    pov "Oh crap!"
    scene showerdownstairs 3pm 007
    mom "Aaah... [pov]! What are you doing here?"
    povi "What to do now? I gotta think quickly!"
    call screen shower15choice2

screen shower15choice2():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        if momcorruption > 20:
            imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('shower15choice2'), Jump('showerd15cor')) hovered tt.Action ("Dominate her [cr1]") focus_mask True
        if momlove > 30:
            imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('shower15choice2'), Jump('showerd15love')) hovered tt.Action ("Excuse yourself [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
    pov "I heard you running the shower and I wanted to see you."
    mom "..."
    pov "So go on. You can remove your hands now."
    scene showerdownstairs 3pm 009a
    mom "Hnn..."
    pov "Very nice! Your hot body all wet."
    pov "Now continue showering, I want to enjoy watching you!"
    mom "Please, you should go..."
    pov "Haha, no. I don't think you decided to shower in a bathroom without a lock for no reason."
    mom "Hnn..."
    scene showerdownstairs 3pm 010a
    "She continues showering."
    pov "I think you're showering in here because you want to been seen, don't you?"
    mom "It wasn't for you... Bruce..."
    pov "I don't think so. He's not around right now. It's just me and the girls. So I'm the most likely reason you're doing this."
    scene showerdownstairs 3pm 011a
    mom "Hnn..."
    pov "That's a good girl."
    povi "She's still seems a little uncomfortable, but at least she's doing it. She'll get used to it soon."
    if inc == True:
        pov "You're so sexy with your wet shining body, mom!"
    else:
        pov "You're so sexy with your wet shining body, [mother]!"
    mom "You shouldn't be talking like that."
    pov "I think I'm going to talk how I want to! Beside, if you really wanted to stop, you could just leave. I won't stop you..."
    mom "Hnn..."
    pov "That's what I thought. Go on, don't be ashamed. Your tits could use more cleaning!"
    scene showerdownstairs 3pm 012a
    mom "..."
    povi "Damn, I'm getting so horny right now."
    pov "Are your nipples getting hard? You enjoy me watching that much?"
    mom "No, they don't... What are you talking about?"
    povi "Argh, now I want to touch them so badly."
    scene showerdownstairs 3pm 013a
    mom "I think I'm done now. You can leave..."
    povi "Oh, she's playing me now."
    pov "Oh I don't think that was a proper shower."
    mom "But I'm all clean and don't need to shower anymore."
    scene showerdownstairs 3pm 014a
    pov "Oh I don't think you're really done yet!"
    mom "What do you mean?"
    pov "I should help you clean yourself."
    "You start to undress."
    if momcorruption < 35:
        scene showerdownstairs 3pm 015a
        mom "Are you fucking crazy?!"
        povi "Oh shit, too soon!"
        mom "Who do you think you are? You better leave now!"
        povi "Damn, I need to corrupt her more!"
        $ dtime += 1
        $ shower15corfirst = True
        jump showerdown
    mom "You... you want... seriously..."
    "After you strip naked, you enter the shower."
    scene showerdownstairs 3pm 016a
    pov "Wow, they're still in very good shape and feel wonderful in my hands."
    if inc == True:
        pov "You should be proud mom!"
    else:
        pov "You should be proud [mother]!"
    mom "Don't stop..."
    pov "Oh, I won't. After all, I need to clean your body very well!"
    mom "Hnn..."
    scene showerdownstairs 3pm 017a
    pov "As I thought, you're enjoying my cleaning."
    mom "We shouldn't be doing this."
    if inc == True:
        "Why? I'm just helping my mom to get clean."
    else:
        "Why? I'm just helping you to get clean."
    povi "She's not stopping me. Time for another step."
    scene showerdownstairs 3pm 018a
    mom "Hah... hnn..."
    mom "Not so... rough..."
    pov "They need a good scrubbing to get clean!"
    mom "Please... go slower..."
    povi "Slower? Not stop scrubbing. Nice!"
    if inc == True:
        pov "Trust me mom. I know what they need."
    else:
        pov "Trust me [mother]. I know what they need."
    scene showerdownstairs 3pm 019a
    mom "Hah... hah..."
    pov "See? I was right. A good scrub helps every time."
    mom "Hnn..."
    pov "Now that I have cleaned this part of your body, time for another spot!"
    mom "Another... hah..."
    scene showerdownstairs 3pm 020a
    pov "Yes! Your body needs to get completely clean."
    mom "Wait!"
    pov "Ssshh... it's ok. I'll finish what I started, I promise!"
    scene showerdownstairs 3pm 021a
    mom "Hah..."
    pov "You like me cleaning you there?"
    mom "I... I was just surprised by your touch..."
    pov "Are you still lying to yourself about this? Your moaning is at least honest!"
    mom "But, hah... hnn..."
    pov "it's ok to enjoy it. It's only natural."
    scene showerdownstairs 3pm 022a
    mom "Hnn... hmm..."
    povi "Finally she's admitting it."
    pov "So... a little more on this spot."
    mom "Hmm! Hmm! ...yes..."
    povi "What a wonderful view. Seeing her enjoy it while I'm rubbing her clit."
    scene showerdownstairs 3pm 023a
    povi "Time for more"
    mom "Aaahh... hah..."
    povi "Now that was a surprise, haha..."
    pov "Just another spot to clean."
    scene showerdownstairs 3pm 024a
    mom "Hah... hah... hah... deeper..."
    pov "I should help you more often with cleaning, you like it very much."
    mom "Hah... your fingers... hnn..."
    pov "... give you a good feeling. I know!"
    povi "Oh, she's shaking. But I need more!"
    scene showerdownstairs 3pm 025a
    pov "So this spot is clean now too."
    mom "Hnn... so we're done..."
    povi "She sounds disappointed. Nice!"
    pov "No. Move around, time for your back."
    mom "O... OK."
    scene showerdownstairs 3pm 026x
    mom "..."
    povi "What...? She's staring at my dick?"
    scene showerdownstairs 3pm 027x
    povi "Yes take a good look. It's all hard for you, haha."
    scene showerdownstairs 3pm 026a
    mom "You will only... clean... my back?"
    pov "Yes, if that's really all you want. You need to be clean."
    "She stares at you a moment longer."
    scene showerdownstairs 3pm 028a
    pov "Good, no push your back out so I can reach it easier."
    povi "That hot ass. Now it's time for more fun!"
    scene showerdownstairs 3pm 028x
    mom "Hnn!"
    if inc == True:
        pov "Relax mom! I've just started with your back."
    else:
        pov "Relax [mother]! I've just started with your back."
    povi "Did she notice it? She's standing all still."
    pov "Just hold on a bit more. Your back will get a special cleaning."
    scene showerdownstairs 3pm 029x
    povi "What a nice feeling! So which hole should I use?"
    mom "Hnnnnn..."
    povi "Now she knows it for sure!"
    pov "Just relax!"
    mom "S... Stop!"
    scene showerdownstairs 3pm 030a
    mom "This is too much!"
    povi "Oh come on!"
    pov "We're not done yet."
    mom "You had your fun but we need to stop here."
    povi "Damn, still not corrupted enough?"
    pov "You had your fun too. And besides, we can't. Your moaning made me all hard, I need to relieve myself."
    if basement10pmnicoleouting == True and mombasementcorsecond == True:
        jump showerd15fuckslut
    scene showerdownstairs 3pm 031a
    pov "And you need to help me."
    mom "But..."
    pov "No! I helped you clean and now you need to help me."
    pov "Even if I wasn't able to finish my cleaning properly."
    mom "I... I..."
    scene showerdownstairs 3pm 032a
    pov "Go on."
    povi "She stop me from fucking her. Let's see if she'll choose another way to satisfy me."
    mom "Hnn... OK. Then we can finish."
    pov "Yes, when I finish, we can finish."
    scene showerdownstairs 3pm 033a
    pov "Oh..."
    povi "That soft and tight touch."
    pov "Yes, with your tight grip I'll cum in no time!"
    mom "Hnn..."
    pov "And your big boobs are a definite bonus."
    scene showerdownstairs 3pm 034a
    pov "You're doing very good. Can you feel my dick pulsating?"
    mom "Hmm... yes..."
    if inc == True:
        pov "I'm so glad to have such a good mom who's helping me out while we enjoy a shower together."
    else:
        pov "I'm so glad to have such a good girl who's helping me out while we enjoyed a shower together."
    mom "Hnn..."
    pov "We'll need to do this more often so you can get used to it and we can finish our cleaning the proper way like I wanted to do before."
    mom "Hnn!"
    povi "Her grip is getting so tight, I'm sure she'll be ready for more soon."
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
    povi "Well now I just covered her stomach with my cum, we should probably shower again to get her clean... but she probably isn't ready for that so soon."
    scene showerdownstairs 3pm 036a
    pov "Hey, it's ok. Don't be ashamed now. You did such a good job."
    mom "..."
    pov "It was no a big deal. Just something between you and I. I washed you and you thanked me for it."
    mom "Hnn..."
    if inc == True:
        pov "You just rewarded me for being a good son."
    else:
        pov "You just rewarded me for being a good boy."
    pov "Like the way it should always be. And you liked it too, I know it."
    mom "I... I lik..."
    scene black
    "She leaves abrubtly."
    povi "I almost had her..."
    $ dtime += 1
    $ shower15corsecond = True
    jump showerdown

label showerd15love:
    $ momlove += 1
    $ momrelationship += 1
    if inc == True:
        pov "I'm so sorry mom. I was distracted with my own thoughts when I opened the door."
    else:
        pov "I'm so sorry [mother]. I was distracted with my own thoughts when I opened the door."
    scene showerdownstairs 3pm 008b
    mom "Oh... that's ok sweetie."
    pov "I wanted to ask you something earlier and now I forgot it..."
    mom "Oh..."
    povi "What she's doing? Should I be scared?"
    scene showerdownstairs 3pm 009b
    mom "It's alright, you can relax. That can happen to anybody."
    povi "What? Why did she just stop hiding herself?"
    pov "Eh...?"
    mom "What's wrong [pov]? You're looking shocked?"
    if inc == True:
        pov "I... I can see you mom."
    else:
        pov "I... I can see you [mother]."
    mom "<giggle> Come on. You never saw a naked woman before?"
    pov "What? Of course I have."
    scene showerdownstairs 3pm 010b
    mom "So what's the matter then? We're just talking together."
    povi "I can't believe it. Why is this happening?"
    if inc == True:
        mom "Or are you feeling uncomfortable seeing your mother naked?"
    else:
        mom "Or are you feeling uncomfortable seeing your mother's best friend naked?"
    pov "Not uncomfortable... just surprised?"
    scene showerdownstairs 3pm 011b
    mom "I can understand that. But I know that you're a good boy so I can trust you with me like this."
    povi "That's odd, but works great for me!"
    mom "You aren't like the other \"pigs\" in the gang. I'm so proud of you."
    povi " Oh no... standing there all naked and wet. Well that boner was inevitable..."
    scene showerdownstairs 3pm 012b
    mom "I'm very proud of you [pov], have I told you that?"
    pov "Yes, hehe. You literally just did like 2 seconds ago."
    povi "Almost every time we talk."
    "You fall silent and stare at her."
    povi "What a fine and beautiful body. And I'm her precious now. I shouldn't ruin it."
    scene showerdownstairs 3pm 013b
    mom "What happened? You're so quiet."
    pov "Honestly, I'm enjoying the view... and praise."
    mom "Haha, I'm glad I could make you happy."
    povi "You made me happy another way, but I probably shouldn't tell you that now."
    if inc == True:
        "Yes, thank you mom!"
    else:
        "Yes, thank you [mother]!"
    if momlove < 50:
        mom "It's so nice talking with you [pov]. But I finished showering..."
        pov "Oh... OK."
        povi "I'm so damn lucky and a good boy too, haha."
        $ shower15lovefirst = True
        $ dtime += 1
        jump showerdown
    mom "Hmm... maybe you can help me?"
    pov "Help you?"
    scene showerdownstairs 3pm 014b
    mom "You could help me wash my back... if you want."
    pov "Your back?"
    mom "I heard that someone else rubbing your back in the shower can be very erotic and I wanted to try it for so long."
    pov "So I should rub your back?"
    mom "Yes plese! Bruce isn't here so maybe you can do it? I know you'll behave."
    povi "Oh... my... god..."
    pov "But the shower is still running..."
    scene showerdownstairs 3pm 015b
    mom "<giggle> Then your clothes will get wet."
    mom "You have to take them off of course."
    pov "So, get naked then?"
    mom "Do I scare you that much? <giggle>"
    pov "No..."
    mom "Then stop talking and get in here with me."
    scene showerdownstairs 3pm 016b
    "You undress and get into the shower."
    povi "We're both naked in the shower and I'm so close to her."
    povi "All this talk about behaving... that's going to be very hard right now. But I don't want to ruin the good relationship we have right now."
    scene showerdownstairs 3pm 017b
    povi "Oh, oh. This isn't helping."
    mom "What are you waiting for [pov]? Just start with my shoulders and then work your way down."
    if inc == True:
        pov "O... OK mom."
    else:
        pov "O... OK [mother]."
    scene showerdownstairs 3pm 018b
    mom "Yes, just like that."
    pov "Just tell me if I'm doing it right, this is my first time."
    mom "You're doing just fine sweetie. Just rub and knead my back so I can relax."
    mom "You'll know if you hurt me! <giggle>"
    pov "Oh I won't hurt you!"
    mom "I know [pov]... hnn..."
    povi "Oh, now she's even moaning. Be a good boy, be a good boy, be a good boy..."
    mom "You can go lower now."
    scene showerdownstairs 3pm 019b
    if inc == True:
        povi "Just calm down, don't think about it. Don't think about being naked in the shower with mom."
    else:
        povi "Just calm down, don't think about it. Don't think about being naked in the shower with [mother]."
    pov "Am I doing it right?"
    mom "Yes... hah... it feels so good..."
    povi "Your moaning isn't helping me."
    mom "Go even lower please... hnn..."
    pov "Are you sure?"
    mom "Yes go on please."
    scene showerdownstairs 3pm 020b
    povi "Oh boy. I'm rubbing her ass now. There is no way this will go badly..."
    mom "Such a good feeling, hah..."
    povi "Oh shit. I can't hold myself down any longer."
    mom "What have I been missing all... hnn... this time."
    scene showerdownstairs 3pm 021b
    mom "Hnn... hah..."
    pov "Should I go back up."
    mom "No just continue... hnn..."
    povi "Oh no. I poked her with my dick. Seriously, this was going to happen no matter how \"good\" I tried to be!"
    "You freeze."
    mom "What...?"
    scene showerdownstairs 3pm 022b
    mom "Oh..."
    mom "It's OK. You did very good."
    povi "She must have noticed my hard dick poking her. But she's not angry... that's good at least."
    mom "That felt so great! You should try it too."
    pov "Wait. You mean...?"
    scene showerdownstairs 3pm 023b
    mom "Yes, we'll change spots now. I'll rub you and you tell me if I'm doing it right."
    povi "Oh come on! Watch porn much?! She wants to rub me now? Half of the videos on youporn start this way..."
    pov "O... OK. If you want to."
    mom "I do! Your muscles should be relaxed too. Just move around."
    scene showerdownstairs 3pm 024b
    povi "I should be enjoying this..."
    mom "Do you feel it? Just rubbing with the hot water feels great too."
    if inc == True:
        pov "Oh yes, it's really good mom."
    else:
        pov "Oh yes, it's really good [mother]."
    mom "Then just enjoy my hands on you."
    povi "Oh I will, I promise you that. But probably in a way you're not expecting."
    scene showerdownstairs 3pm 025b
    pov "Huh?"
    mom "I decided I wanted to rub your chest too."
    povi "Oh my god. She's pressing her tits on my back and is still rubbing me. What she's up to?"
    mom "I can feel your body relaxing. Good, I really want you to enjoy this too."
    pov "Too? Yes, I... do."
    scene showerdownstairs 3pm 026b
    povi "Wow, she's getting even lower. What if she touches my dick accidentally."
    mom "You're so tense still, you should relax more."
    pov "I'll try."
    povi "But if I'm going to relax how she wants me to, I'll need a release first..."
    mom "Now it's time to finish up."
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
    mom "I felt you getting hard and poking me accidentally. But even then you behaved and didn't try anything crazy."
    if inc == True:
        mom "So this is my reward to my good son for withstanding your urges."
    else:
        mom "So this is my reward to my good boy for withstanding your urges."
    povi "Damn, is she into me or something? This is like the opposite of withstanding urges, but who am I to argue with her?"
    scene showerdownstairs 3pm 028b
    pov "Aaah, hah..."
    mom "Good. Just enjoy my touch and let yourself go when you need to."
    if inc == True:
        pov "Hah, your hands are so soft mom."
    else:
        pov "Hah, your hands are so soft [mother]."
    mom "Now you can feel good like I did from your hands earlier."
    pov "Oh yes, I do!"
    povi "Damn, she's even playing with my balls. I can't hold much longer!"
    if basement10pmnicoleouting == True and mombasementlovesecond == True:
        jump showerd15fucklove
    scene showerdownstairs 3pm 029b
    if inc == True:
        pov "Aaaah... MOM!"
    else:
        pov "Aaaah... [mother]!"
    mom "Good, just let everything out."
    pov "Oh yes! Ahh... hah..."
    mom "Wow, seems like you really liked it."
    pov "Yes, oh..."
    scene showerdownstairs 3pm 030b
    pov "W... why?"
    mom "I have been leaning a lot on you recently and I wanted to say thank you for being so good to me."
    mom "So I wanted to help you too. I know the pain you can get when you can't release things when you need to."
    pov "Ok, but just so we're clear, you did just wank me off right? That was intentional?"
    mom "Yes! And maybe also because I liked your penis? <giggle>"
    if inc == True:
        pov "Haha. Mom!"
    else:
        pov "Haha. [mother]!"
    mom "But you liked it?"
    pov "I loved it!"
    scene showerdownstairs 3pm 031b
    mom "Good. We should probably keep this between us though."
    if inc == True:
        pov "Of course mom!"
    else:
        pov "Of course [mother]!"
    povi "I'm a bit confused and feel a little like a toy. But she wouldn't do that to me, right?"
    povi "Maybe I've grown up to be the man she would like to have, and Bruce isn't like that anymore?"
    scene black
    "She leave the shower and you stand there for some time, still naked and confused."
    $ dtime += 1
    $ shower15lovesecond = True
    jump showerdown

label showerd15ntr:
    scene black
    "You open the door."
    call screen checkdarkerpaths_nicole
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene showerdownstairs 3pm 005n
    mom "Oh... Aaahh..."
    if nicole_voyeur == True or nicole_sadist == True:
        if inc == True:
            povi "Oh mom has a guest."
        else:
            povi "Oh [mother] has a guest."
        povi "It seems like she can't wait until evening."
    else:
        povi "Oh no! This can't be true."
        povi "Why is he here now?"
    scene showerdownstairs 3pm 006n
    povi "Oh...?"
    mom "Huh?"
    davide "What's up slut?"
    scene showerdownstairs 3pm 007n
    mom "We need to stop, let me down!"
    davide "What the hell? There's no way that I'm going to stop now!"
    if nicole_voyeur == True or nicole_sadist == True:
        povi "She's getting angry that I'm watching. But I'd love to see her getting screwed."
    else:
        povi "She wants to stop. Why does this idiot keep going? Did he force her into this?"
    mom "Someone is watching us!"
    davide "Really? Let's see."
    scene showerdownstairs 3pm 008n
    davide "Oh hey [pov]! So you really need to watch us?"
    mom "Stop it! Let me down now!"
    if nicole_voyeur == True or nicole_sadist == True:
        pov "Yes! I want to see her screaming, haha."
        davide "I can understand that, haha."
    else:
        pov "..."
        if nicole_revenge == True:
            povi "When she wants to stop you should let her, asshole!"
        else:
            povi "Why won't he just stop! I can't stop him either."
    davide "She likes it too even if she denies it. She's getting tighter."
    mom "Stop this bullshit!"
    scene showerdownstairs 3pm 009n
    davide "As I said before, I won't stop now. Not until we've had good sex together and I released my junk in you!"
    mom "I said no!"
    davide "Yes you do, but your body say yes! So use your mouth only for moaning and prepare for a hard fuck!"
    if nicole_voyeur == True or nicole_sadist == True:
        if inc == True:
            pov "He's right mom. You could use a hard pounding to calm down, haha."
        else:
            pov "He's right [mother]. You could use a hard punding to calm down, haha."
    else:
        if nicole_revenge == True:
            if inc == True:
                povi "Does he really want to rape my mom in front of me?"
            else:
                povi "Does he really want to rape her in front of me?"
        else:
            if inc == True:
                povi "Does he really want to fuck my mom in front of me?"
            else:
                povi "Does he really want to fuck her in front of me?"
    scene showerdownstairs 3pm 011n
    if nicole_revenge == True or nicole_sadist == True:
        mom "Let me go! I don't want this!"
    else:
        mom "Let me go! I don't want an audience!"
    davide "Shut up slut! You'll get it even harder now!"
    if nicole_voyeur == True or nicole_sadist == True:
        pov "Good, continue now. I want to see something good!"
    else:
        if nicole_revenge == True:
            povi "I need to beat this fucker! Wait... what if I ruin the investigation?"
            povi "I'm sorry, I just don't know what to do!"
        else:
            povi "Wait... She doesn't want an audience? So she wanted to go on with this asshole?"
            povi "I hope I heard something wrong. Why should she enjoy sex with this idiot?"
    scene showerdownstairs 3pm 012n
    if nicole_revenge == True or nicole_sadist == True:
        mom "Hah... hnn... you asshole..."
    else:
        mom "Hah... hnn... you idiot..."
    povi "He's fucking her hard."
    davide "See [pov]? Taking the slut hard shuts her up!"
    if nicole_voyeur == True or nicole_sadist == True:
        pov "I see. And I'm sure in no time she'll love it too! That hot body needs to be screwed often!"
        if inc == True:
            davide "Haha, you heard that? Even your own son is on my side."
        else:
            davide "Haha, you heard that? Even [pov] is on my side."
    else:
        pov "..."
        if nicole_revenge == True:
            povi "You damn asshole! Stop this now! I'll kill you!"
        else:
            povi "You damn asshole! Stop this now! Just stop this!"
        davide "Hmm, look he seems angry or is it confused. Maybe he wants to join us?"
    scene showerdownstairs 3pm 013n
    mom "No... hah...hah..."
    davide "You're enjoying your live-porn, haha?"
    mom "Aaah... so rough... hah... stop..."
    if nicole_voyeur == True:
        pov "Yes this is damn hot. And [mother] is enjoying this now."
        if inc == True:
            pov "You're lika a hot porn-star mom!"
        else:
            pov "You're like a hot porn-star [mother]!"
    elif nicole_sadist == True:
        pov "Yes this is damn hot. Although [mother] isn't enjoying it yet."
        if inc == True:
            pov "You're lika a hot porn-star mom!"
        else:
            pov "You're like a hot porn-star [mother]!"
    else:
        if nicole_revenge == True:
            povi "No, I don't want to see this anymore. She's liking it but doesn't want to!"
            povi "But I won't leave, I'm afraid what that asshole might do with her when they're alone."
            povi "If I was stronger I could interfere!"
        else:
            povi "No, I don't want to see this anymore."
            povi "Only if I were stronger..."
    davide "See [mother]? [pov] is enjoying his show!"
    scene showerdownstairs 3pm 014n
    "Suddenly [mother] holds herself on you, preventing herself from fall over."
    if nicole_revenge == True or nicole_sadist == True:
        mom "Please Stop!, I'm falling, hah..."
    else:
        mom "Go slower, I'll fall, hah..."
    davide "I don't care slut! Take my dick!"
    mom "Hah... hah... aaah..."
    scene showerdownstairs 3pm 015n
    if nicole_voyeur == True:
        if inc == True:
            pov "You're so close mom. Moaning in my face! I'm glad you're enjoying your hard fuck."
        else:
            pov "You're so close [mother]. Moaning in my face! I'm glad you're enjoying your hard fuck."
    elif nicole_sadist == True:
        if inc == True:
            pov "You're so close mom. Moaning in my face!"
        else:
            pov "You're so close [mother]. Moaning in my face!"
    else:
        povi "This is like a punishment. The woman I love is moaning directly in my face."
    if nicole_revenge == True or nicole_sadist == True:
        mom "You're hurting me, please stop! I'm sorry [pov], hah..."
    else:
        mom "He's so big and rough [pov], hah..."
    davide "Oh you're giving him an even better show now. Good that way you can enjoy this now slut!"
    if nicole_revenge == True or nicole_sadist == True:
        mom "No, I'm not! Hah... I will never be yours!"
    else:
        mom "Yes' it's good! Hah... I was wrong, do me harder!"
    if nicole_voyeur == True or nicole_sadist == True:
        pov "So nice! I think I should get the next ride!"
        davide "Good idea! That way you can ride the slut even harder!"
        mom "Harder? Hah... aaahh..."
    else:
        if nicole_revenge == True:
            povi "I'm sorry! You're out of senses because he's raping you so hard!"
            if inc == True:
                povi "There's no way that my mom would like having sex with that pig."
            else:
                povi "There's no way that [mother] would like having sex with that pig."
        else:
            povi "I'm so sorry! There is nothing I can do to stop him. I'm just not strong enough to face him."
    scene showerdownstairs 3pm 016n
    if nicole_revenge == True or nicole_sadist == True:
        mom "Aaaah... haaaahh... Nooooo!"
    else:
        mom "Aaaah... haaaahh... YES!"
    davide "Oh? The slut is coming?"
    if nicole_revenge == True or nicole_sadist == True:
        mom "I hate you! I fucking hate you!"
    else:
        mom "Yes! Harder! HARDER!"
    if nicole_voyeur == True or nicole_sadist == True:
        if inc == True:
            pov "Yes mom! Let me see you cumming. Prove to me that you love hard, rough sex!"
        else:
            pov "Yes [mother]! Let me see you cumming. Prove to me that you love hard, rough sex!"
    else:
        povi "That fucking asshole. Stealing her away from us."
        povi "Maybe he drugged her?"
        if nicole_revenge == True:
            povi "I'll get my revenge and show her that I'm much better."
    davide "Take my junk!"
    mom "Haaahh..."
    scene showerdownstairs 3pm 017n
    "She knelt down in the bath-tub."
    mom "Hah... hah... hah..."
    davide "Did you enjoy that bitch, haha..."
    scene showerdownstairs 3pm 018n
    davide "You noticed? At first she was bitchy and in the end she enjoyed rough fucking."
    if nicole_voyeur == True or nicole_sadist == True:
        pov "Yes. A good show. That's something I need to try with her too sometime."
        davide "Haha, then good luck."
    else:
        pov "..."
        povi "Fuck you, you fucking fuck!"
    if nicole_ntr == True:
        scene showerdownstairs 3pm 019n
        if inc == True:
            pov "Mom, I can't believe you did that!"
        else:
            pov "[mother], I can't believe you did that!"
        mom "Hah...hnn..."
        pov "And you even got more excited when Davide suggested a threesome."
        mom "Please leave."
        scene black
        "You leave the bathroom."
        $ dtime += 1
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        jump showerdown
    elif nicole_voyeur == True:
        scene showerdownstairs 3pm 019n
        if inc == True:
            pov "Oh mom. That was so hot, seeing you cumming hard!"
        else:
            pov "Oh [mother]. That was so hot, seeing you cumming hard!"
        mom "Hah...hnn..."
        pov "And your nice reaction when Davide suggested a threesome."
        mom "Please leave."
        povi "Oh she's so confused."
        scene black
        "You leave the bathroom."
        $ dtime += 1
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        jump showerdown
    elif nicole_revenge == True:
        scene showerdownstairs 3pm 020n
        pov "I'm so sorry I couldn't stop him."
        mom "...Please leave now [pov]. I wish you didn't have to see that..."
        pov "But..."
        povi "She's hurt and confused. It felt good physically, but she was raped. It's a mind fuck."
        mom "Please go. I'll take care of this."
        povi "I can't believe this! It's not fair to her! Dad needs to stop this!"
        pov "Ok... I'm here if you need me."
        mom "Thank you..."
        scene black
        if showeraftermath >= 1:
            "You leave the bathroom"
            $ dtime += 1
            jump showerdown
        else:
            "You start to leave the bathroom."
            if inc == True:
                mom "Son, could you meet me in the dining room in a bit. We should talk about what happened."
            else:
                mom "[pov], could you meet me in the dining room in a bit. We should talk about what happened."
                pov "Of course I can."
            scene diningroom 7am 003
            povi "She looks so sad and tired. Just completely exausted."
            pov "Hey..."
            scene diningroom 7am 004
            mom "Hey sweetie. You want to sit down?"
            pov "Sure."
            scene diningroom 7am 005
            povi "How the hell did things get so bad."
            povi "And why the fuck did I get excited during that?!"
            povi "I was so fucking angry at that asshole, but after seeing her like that..."
            povi "I'm going to hell."
            mom "Sweetie..."
            if inc == True:
                pov "Sorry Mom."
            else:
                pov "Sorry [pov]"
            scene diningroom 7am 005a
            mom "It's ok. I know that can't have been easy to watch."
            pov "He fucking raped you!!! I swear to God I'm going to kill that asshole!"
            scene diningroom 7am 006a
            mom "Shhhh, not so loud! Your sisters will hear you. Please calm down."
            pov "How can I calm down?! How can you?! He violated you!"
            pov "He made you cum against your will in front of your son!"
            scene diningroom 7am 011a
            mom "hmmm..."
            povi "The fuck? She seems both excited and ashamed at the same time."
            povi "Wrong as it might be, I hope it was because I was involved and not that asshole."
            pov "I'm sorry. I'm just so angry."
            pov "How are you so calm? I would be in corner crying my eyes out if that happened to me."
            pov "I just wanted to protect you guys."
            pov "I just wanted to protect you."
            scene diningroom 7am 012a
            mom "Oh baby, you're doing everything you can. I know that."
            mom "I know that was why you stayed."
            mom "You wanted to make sure he didn't hurt me more."
            mom "I wish I could say this was the first time something like this has happened..."
            pov "Dear god..."
            mom "But we decided together to do this."
            if inc == True:
                "Your father and I."
            else:
                "David and I."
            mom "This was a risk. We have done everything we can to prevent this falling on the girls."
            mom "But I haven't been able to avoid all the pitfalls."
            scene diningroom 7am 012
            if inc == True:
                pov "But mother, you deserve so much better than this."
            else:
                pov "But [mother], you derserve so much better than this."
            pov "You deserve someone to hold you and make you feel safe."
            pov "Someone to caress and love you, like a woman and a partner."
            scene diningroom 7am 011
            pov "No one deserves what that asshole did. Least of all someone I love"
            pov "I promise you I will get this to stop."
            pov "I don't know how yet, but I'll find a way."
            scene diningroom 7am 009
            mom "I know you will baby."
            mom "I was so excited to have you finally home with us."
            mom "Even with this messed up situation."
            mom "And see how big, strong and gentleman like you had become..."
            mom "That gave me hope."
            povi "Damn... I'm going start crying if she keeps this up."
            pov "It's ok. I am always going to be here. We'll figure out a way to make this right."
            mom "Yes we will. But until then I need you to hang in there as much as you can."
            mom "I know that will be hard but we need to get this people."
            mom "We've sacrificed too much to quit now."
            scene diningroom 7am 013
            mom "And just remember that no matter what you see happening to me..."
            mom "I don't enjoy it. No matter what my body does or I say in a daze."
            mom "And now I have you to think of when that happens."
            pov "Yeah..."
            povi "Wait... What?!?"
            povi "She's going to be thinking of me during that stuff?!?"
            mom "Well Sweetie I have to get dinner started. I'm glad we were able to stop"
            pov "Wai..."
            scene black
            povi "So... That happened."
            povi "I feel a little better about the situation."
            povi "But what did that last part mean?"
            povi "Does she want me to do those things with her?"
            "You leave the room."
            $ showeraftermath += 1
            $ dtime += 1
            if gamemusic == True and renpy.music.is_playing("bgm") == False:
                stop music fadeout 2
                play music "music/default.mp3"
            jump showerdown
    else:
        scene showerdownstairs 3pm 020n
        if inc == True:
            pov "Oh mom. That was so hot, seeing you cumming hard!"
        else:
            pov "Oh [mother]. That was so hot, seeing you cumming hard!"
        mom "...Please leave now [pov]. I wish you didn't have to see that..."
        pov "But..."
        povi "She's hurt and confused. It felt good physically, but she was raped. It's a mind fuck."
        mom "Please go. I'll take care of this."
        pov "Ok..."
        mom "Thank you."
        scene black
        "You leave the bathroom."
        $ dtime += 1
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        jump showerdown

#----- Custom Scene -----
screen bonusshowernicoleloc():
    modal True
    default tt = Tooltip ("Select Path")
    tag bsnds

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('bonusshowernicoleloc'), SetVariable('bonusshowernicolelove', True), Return(None)) hovered tt.Action ("[lv2] Path") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('bonusshowernicoleloc'), SetVariable('bonusshowernicolelove', False), Return(None)) hovered tt.Action ("[cr2] Path") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

label bonusshowernicole:
    call screen bonusshowernicoleloc
    hide screen locations
    if bonusshowernicolelove == True:
        jump bonusshowernicolelovepath
    else:
        jump bonusshowernicolecorpath

label bonusshowernicolelovepath:
    scene edited showerdownstairs nic 01
    "You walk into the downstairs shower."
    povi "She's so beautiful. I could watch her shower all day."
    if inc == True:
        pov "Hey mom, I thought I would come keep you company for a bit."
    else:
        pov "Hey [mother], I thought I would come keep you company for a bit."
    scene edited showerdownstairs nic 02 love
    mom "Oh hi sweetie!"
    mom "That's so kind of you."
    mom "You know I get lonely when you're not around."
    pov "So how was work this morning?"
    if momrelationship > 5:
        mom "It was pretty slow. Kind of boring actually. You should come visit me there more often."
    else:
        scene edited showerdownstairs nic 02 cor
        mom "It was pretty slow... Nothing important happened..."
        "Her eyes seem to darken for just a moment."
        povi "\"Nothing important\"? That's a weird thing to say. Maybe I should ask her about that later."
    scene edited showerdownstairs nic 03 love
    "She starts posing for you as she rinses the soap from her body. A sly grin on her face the whole time."
    if momrelationship <= 5:
        povi "Looks like she's trying to change the subject. That's ok for now. I'll worry about that later."
    pov "Looks like you are enjoying yourself in there!"
    mom "Oh I am! But the question is, are you enjoying yourself too?"
    pov "I think you know that I am. Look at the bulge in my pants, haha!"
    mom "I see it! Maybe I should finish up. I could help you... relieve that pressure."
    pov "I like the sound of that. I think we both could use a release."
    mom "Release... Hnng..."
    "She knows exactly what you are talking about and quickly shuts the water off and steps out to join you."
    "You undress as she does, leaving you both naked and staring at each other."
    scene edited showerdownstairs nic 04 love
    mom "You're so handsome! I can't believe how lucky I am! Why would you choose to love someone like me? An old woman."
    if inc == True:
        pov "Come on mom! You're not old! You know age doesn't matter to me. Besides, you're ignoring the point."
    else:
        pov "Come on [mother]! You're not old! You know age doesn't matter to me. Besides, you're ignoring the point."
    mom "Oh yeah? And what is... the point?"
    pov "That you are the kindest, strongest and most beautiful woman I've ever known. I've always loved you. I always will love you, no matter what."
    mom "Oh baby! I love you so much!"
    "As if to punctuate her point, she steps back and lifts herself up onto the little counter behind her. Displaying her \"beauty\" for you."
    scene edited showerdownstairs nic 05
    if inc == True:
        mom "I need you son. I need to feel you caress my skin. I need to feel you inside me!"
    else:
        mom "I need you [pov]. I need to feel you caress my skin. I need to feel you inside me!"
    pov "As you wish."
    call screen bonusshowernicolepoa
    jump bonusshowernicolepart2

label bonusshowernicolecorpath:
    scene edited showerdownstairs nic 01
    "You walk into the downstairs shower."
    povi "She's so damn hot, I could watch this all day."
    if inc == True:
        pov "Hello mother, I thought I would come visit you for a bit. You don't mind, right?"
    else:
        pov "Hello [mother], I thought I would come visit you for a bit. You don't mind, right?"
    scene edited showerdownstairs nic 02 cor
    mom "Oh... I didn't see you there."
    mom "I don't mind, if that's what you want..."
    mom "I mean, it is my job to keep you satisfied."
    pov "True, and speaking of your job, how was work this morning?"
    if momrelationship > 5:
        mom "It was pretty slow. Kind of boring actually. You should come visit me there again..."
    else:
        mom "It was pretty slow... Nothing important happened..."
        "Her eyes seem to darken for just a moment."
        povi "\"Nothing important\"? That's a weird thing to say. I should ask her about that later."
    scene edited showerdownstairs nic 03 cor
    "She starts posing for you as she rinses the soap from her body. A sly grin on her face the whole time."
    if momrelationship <= 5:
        povi "Looks like she's trying to change the subject. That's ok for now. I'll worry about that later."
    pov "I'm glad to see you're enjoying yourself in there!"
    mom "Oh I am! But the question is, are you enjoying yourself too?"
    pov "Look how hard my cock is getting and tell me what you think."
    "You grab your dick and shake it a bit through your pants, you erection clearly visible through the fabric."
    mom "I know you do. I think I should finish up. I need to help you... relieve that pressure."
    if inc == True:
        pov "Is that your way of saying you want this cock, mom? Sure sounds like it to me."
    else:
        pov "Is that your way of saying you want this cock, [mother]? Sure sounds like it to me."
    mom "Hnng... Yes, I want it..."
    "She quickly shuts the water off and steps out to join you."
    "You undress as she does, leaving you both naked and staring at each other."
    scene edited showerdownstairs nic 04 cor
    mom "God, I want you! I need to feel your hands on my body! Using me however you want... whenever you want... where ever you want."
    if inc == True:
        pov "I like this new attitude mom. It's about time you've realized how helping me... is really just helping yourself. In more ways than one."
    else:
        pov "I like this new attitude [mother]. It's about time you've realized how helping me... is really just helping yourself. In more ways than one."
    mom "Oh believe me, I know "
    pov "So how exactly are planning to help me?"
    mom "Well, this is what I had in mind..."
    "She steps back and lifts herself up onto the little counter behind her. Displaying herself for you."
    scene edited showerdownstairs nic 05
    if inc == True:
        mom "I want you to fuck me son. I need to feel you hard cock inside me. I want you to use me..."
    else:
        mom "I want you to fuck me [pov]. I need to feel you hard cock inside me. I want you to use me..."
    pov "Happy to oblige."
    call screen bonusshowernicolepoa
    jump bonusshowernicolepart2

screen bonusshowernicolepoa():
    modal True
    default tt = Tooltip ("")
    tag bsnds

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('bonusshowernicolepoa'), SetVariable('bonusshowernicolepussy', True), SetVariable('bonusshowernicoleass', False), Return(None)) hovered tt.Action ("Pussy") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('bonusshowernicolepoa'), SetVariable('bonusshowernicoleass', True), SetVariable('bonusshowernicolepussy', False), Return(None)) hovered tt.Action ("Ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

label bonusshowernicolepart2:
    if bonusshowernicolepussy == True:
        scene edited showerdownstairs nic 06 pussy
        if bonusshowernicolelove == True:
            mom "Oh sweetie, I love the way you tease my pussy like that."
            pov "Yeah? Well I don't think we're done teasing you yet."
            mom "Hnng!"
            call screen bonusshowernicoletease
        else:
            mom "Hnng... I love how you tease my pussy like that."
            pov "Yeah? Well I don't think we're done teasing you yet."
            mom "Hnng!"
            call screen bonusshowernicoletease
    else:
        scene edited showerdownstairs nic 06 ass
        if bonusshowernicolelove == True:
            mom "Oh sweetie, I love the way you tease my ass like that."
            pov "Yeah? Well I don't think we're done teasing you yet."
            mom "Hnng!"
            call screen bonusshowernicoletease
        else:
            mom "Hnng... I love how you tease my ass like that."
            pov "Yeah? Well I don't think we're done teasing you yet."
            mom "Hnng!"
            call screen bonusshowernicoletease

screen bonusshowernicoletease():
    modal True
    default tt = Tooltip ("Select Action")
    tag bsnds

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('bonusshowernicoletease'), Jump('bonusshowernicrub')) hovered tt.Action ("Rub") focus_mask True
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('bonusshowernicoletease'), Jump('bonusshowernicpussy')) hovered tt.Action ("Pussy") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('bonusshowernicoletease'), Jump('bonusshowernicass')) hovered tt.Action ("Ass") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('bonusshowernicoletease'), Jump('bonusshowernicolepart3split')) hovered tt.Action ("Stop Teasing") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

label bonusshowernicrub:
    scene bsnrubani
    if bonusshowernicolelove == True:
        pov "You're so wet!"
        mom "Hmmm... please baby, I want you inside me."
    else:
        pov "You're so wet!"
        mom "Hmmm... fuck me baby. I need to feel your hard cock inside me."
    call screen bonusshowernicoletease

label bonusshowernicpussy:
    scene bsnpussyani
    if bonusshowernicolelove == True:
        pov "Do you like that? Just a little taste of what's to come."
        mom "Oh sweetie, I love it. You're so big!"
    else:
        pov "You like that, slut. You want more?"
        mom "Hnng! Yes! I need more..."
    call screen bonusshowernicoletease

label bonusshowernicass:
    scene bsnassani
    if bonusshowernicolelove == True:
        pov "You like that? You're so tight!"
        mom "Oh god yes! That's amazing!"
    else:
        pov "How about I fuck this tight ass now? You know you want it!"
        mom "I do baby! I want it in my ass!"
    call screen bonusshowernicoletease

label bonusshowernicolepart3split:
    call screen bonusshowernicolepoa
    if bonusshowernicolelove == True:
        jump bonusshowernicolepart3lovepath
    else:
        jump bonusshowernicolepart3corpath

label bonusshowernicolepart3lovepath:
    if bonusshowernicolepussy == True:
        scene edited showerdownstairs nic 07 pussy
        "You shove your cock inside her wet hot pussy, she gasps in surprise"
        mom "Aaahh!!! Oh god! Yes!"
        pov "God you feel amazing. You're so tight!"
        mom "Deeper baby! I need all of you!"
    else:
        scene edited showerdownstairs nic 07 ass
        "You shove your cock inside her tight asshole, she gasps in surprise"
        mom "Aaahh!!! Oh god! Yes!"
        pov "God you feel amazing. You're so tight!"
        mom "Deeper baby! I need all of you!"
    if bonusshowernicolepussy == True:
        scene edited showerdownstairs nic 08 pussy
        "You shove your cock inside her to the hilt. You feel her pussy clamp down tightly and squeeze in pulses."
        povi "Wow, she's coming already. This is so fucking hot."
        mom "Ohhhh shit! HNNGGG!"
        "You both ride out her orgasm enjoying the her bliss."
    else:
        scene edited showerdownstairs nic 08 ass
        "You shove your cock inside her to the hilt. You feel her ass clamp down tightly and squeeze in pulses."
        povi "Wow, she's coming already. This is so fucking hot."
        mom "Ohhhh shit! HNNGGG!"
        "You both ride out her orgasm enjoying the her bliss."
    if inc == True:
        "After you both catch you breath, your mother looks up at you and in a rush embraces you, pressing her lips to yours."
    else:
        "After you both catch you breath, [mother] looks up at you and in a rush embraces you, pressing her lips to yours."
    scene edited showerdownstairs nic 09
    pov "Ohhmnph... Mmmm. <Kisses>"
    mom "Hmmm. <Kisses>"
    if inc == True:
        "The two of you kiss passionately until your mom breaks the kiss and stares into your eyes."
    else:
        "The two of you kiss passionately until [mother] breaks the kiss and stares into your eyes."
    scene edited showerdownstairs nic 10 love
    if inc == True:
        mom "I love you so much son. The time we've had together since your return has been the best I've had in years. Maybe ever. I never want this to end."
    else:
        mom "I love you so much [pov]. The time we've had together since your return has been the best I've had in years. Maybe ever. I never want this to end."
    pov "I don't want it to end either. So we won't let it. We're going to find a way out of this mess and then we'll find a way to be together, for good this time."
    mom "I can't wait!"
    "You start thrusting inside her again. She eagerly meets your thrusts with her own."
    scene edited showerdownstairs nic 11
    pov "Sorry, I'm not going to last long at this rate. It just feels so damn good."
    mom "Hnng! Same here sweetie. Just let it go when you need to. I want to feel your hot cum inside me!"
    "Your thrusts increase in speed and she starts moaning louder and grinding back faster."
    scene edited showerdownstairs nic 12
    mom "Oh god baby! Oh God! Hmmm... Hnng... ah... ahhh!"
    pov "I'm close! I'm going to cum."
    mom "Do it my love! Fill me up! Cum for me baby!"
    "Her words push you over the edge as you burst inside her."
    scene edited showerdownstairs nic 13
    with vpunch
    pov "HnNGHHh! Oh yeah!"
    with vpunch
    mom "I can feel it pouring inside me! I'm cumming too! I'm cumming!!!"
    pov "UNNghhhH!"
    with vpunch
    mom "HNNNGGG!"
    "Your mutual orgasms continue for what feels like a blissful eternity."
    if bonusshowernicolepussy == True:
        scene edited showerdownstairs nic 14 pussy
        "Reluctantly you lift her off your spent cock, cum flowing out from her well used pussy."
    else:
        scene edited showerdownstairs nic 14 ass
        "Reluctantly you lift her off your spent cock, cum flowing out from her well used ass."
    mom "That was amazing!"
    pov "It really was!"
    "You gently set her down and step back, enjoying the view."
    scene edited showerdownstairs nic 15 love
    mom "I'm still having a hard time believing this is all real. If you told me that I would be this happy just a few weeks ago I would have told you that you were crazy!"
    pov "I know what you mean. So much has changed. But I can promise you, it's all real."
    mom "Well, as long as we're together I know we're going to be ok."
    pov "You got that right!"
    scene edited showerdownstairs nic 16
    mom "Now hand me my robe! We can't stand here making love all day!"
    pov "Challenge accepted!"
    mom "Haha! You wish... Ok, well I do too, but I've got errands to run before making dinner."
    pov "Well, I guess I can let you go this time. But next time... you're all mine!"
    scene edited showerdownstairs nic 17 love
    mom "I'm always going to be all yours. Plus, I happen to know you're going to be getting some more of this later tonight... If you want it that is."
    pov "Do you even have to ask?! See later tonight."
    scene black
    "You leave her to get ready. You hear her humming a sweet tune to herself as you turn and walk away."
    $ bonusshowernicolelove = False
    $ bonusshowernicolepussy = False
    $ dtime += 1
    jump showerdown

label bonusshowernicolepart3corpath:
    if bonusshowernicolepussy == True:
        scene edited showerdownstairs nic 07 pussy
        "You shove your cock inside her wet hot pussy, she gasps in surprise"
        mom "Aaahh!!! Oh fuck! Yes!"
        pov "You're so fucking tight!"
        mom "Deeper! Fuck me deeper!"
    else:
        scene edited showerdownstairs nic 07 ass
        "You shove your cock inside her tight asshole, she gasps in surprise"
        mom "Aaahh!!! Oh fuck! Yes!"
        pov "You're so fucking tight!"
        mom "Deeper! Fuck me deeper!"
    if bonusshowernicolepussy == True:
        scene edited showerdownstairs nic 08 pussy
        "You shove your cock inside her to the hilt. You feel her pussy clamp down tightly and squeeze in pulses."
    else:
        scene edited showerdownstairs nic 08 ass
        "You shove your cock inside her to the hilt. You feel her ass clamp down tightly and squeeze in pulses."
    pov "Wow, you're coming already. You're such a fucking slut. I love it!"
    mom "Ohhhh shit! HNNGGG!"
    "You both ride out her orgasm."
    if inc == True:
        "After you both catch you breath, your mother gives you a lusty look and pull herself close to you, pressing her lips to yours. Shoving her tongue into your mouth."
    else:
        "After you both catch you breath, [mother] gives you a lusty look and pull herself close to you, pressing her lips to yours. Shoving her tongue into your mouth."
    scene edited showerdownstairs nic 09
    pov "Ohhmnph... Mmmm. <Kisses>"
    mom "Hmmm. <Kisses>"
    if inc == True:
        "The two of you kiss passionately until your mom breaks the kiss and stares hungrily at you."
    else:
        "The two of you kiss passionately until [mother] breaks the kiss and stares hungrily at you."
    scene edited showerdownstairs nic 10 cor
    if inc == True:
        mom "You're so incredibly hot son. It's amazing how you've taken charge and really started to lead this family. I never want this to end."
    else:
        mom "You're so incredibly hot [pov]. It's amazing how you've taken charge and really started to lead this family. I never want this to end."
    pov "I'm not going anywhere. And with you keeping me so happy, why would I ever let it end?"
    mom "I knew you wouldn't leave me behind! I'm going to keep you so happy! You just watch!"
    "She starts grinding her hips again, your cock pushing deeper inside her. You start meeting her thrusts with your own."
    scene edited showerdownstairs nic 11
    pov "God damn! I'm not going to last long at this rate."
    mom "Hnng! Good baby! Just let it go when you need to. I want to feel your hot cum gushing inside me!"
    "Your thrusts increase in speed and she starts moaning louder and grinding back faster."
    scene edited showerdownstairs nic 12
    mom "Oh fuck baby! Oh fuck! Hmmm... Hnng... ah... ahhh!"
    if bonusshowernicolepussy == True:
        pov "I'm close! I'm going to fill that slutty pussy of yours!"
    else:
        pov "I'm close! I'm going to fill that slutty ass of yours!"
    mom "Do it! Fill me up! Cum for me baby!"
    "Her words push you over the edge as you burst inside her."
    scene edited showerdownstairs nic 13
    with vpunch
    pov "HnNGHHh! Oh shit!"
    with vpunch
    mom "I can feel it pouring inside me! I'm cumming too! I'm cumming!!!"
    pov "UNNghhhH!"
    with vpunch
    mom "HNNNGGG!"
    "Your mutual orgasms continue as you two spasm together in ecstasy."
    if bonusshowernicolepussy == True:
        scene edited showerdownstairs nic 14 pussy
        "Reluctantly you lift her off your spent cock, cum flowing out from her well used pussy."
        mom "Hnng... my pussy feels so full. I love it!"
    else:
        scene edited showerdownstairs nic 14 ass
        "Reluctantly you lift her off your spent cock, cum flowing out from her well used ass."
        mom "Hnng... my ass feels so full. I love it!"
    pov "And that's why you're my favorite cum-dumpster."
    "You set her down and step back, enjoying the view."
    scene edited showerdownstairs nic 15 cor
    mom "I'm glad I could help relieve some of that pent up... energy you have."
    if inc == True:
        pov "All a part of keeping me happy right mom?"
    else:
        pov "All a part of keeping me happy right [mother]?"
    mom "Exactly, you keep Bruce and that non-sense away from us and I'll do anything you want me to do."
    pov "Just what I wanted to hear! Good girl."
    scene edited showerdownstairs nic 16
    mom "Haha, now hand me my robe! We can't stay in here all day!"
    pov "We can if I tell you that what we're doing!"
    mom "True. But I've got errands to run before making dinner..."
    pov "Alrigth, I'll let you go for now."
    scene edited showerdownstairs nic 17 cor
    mom "Besides, if I know you, we're going to be doing much more of this tonight... right?"
    pov "If you're a good girl, then you can bet on it!"
    mom "<giggle> I can't wait!"
    scene black
    "You leave her to get ready. You hear her humming to herself as you turn and walk away."
    $ bonusshowernicolelove = False
    $ bonusshowernicolepussy = False
    $ dtime += 1
    jump showerdown
