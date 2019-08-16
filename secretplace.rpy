#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. Time Location - Featured - Scenes
#----- End List -----

label splace2pmtalk:
    hide screen locations
    scene main 2pm floor
    if lilsisrelationship < 40 and lilsisntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump alexisshakyhideout
        elif randomnum == 2:
            " "
    $ lilsisrelationship += 1
    pov "Hi [ls], what's up?"
    ls "Hmm..."
    ls "I want to show you something. Please follow me but make sure no one sees us."
    pov "Oh? A secret hideout?"
    ls "Yes, come on!"
    scene black
    "You follow her to a place behind the house."
    scene town secret 2pm 001
    if inc == True:
        ls "Here it is. Come in big brother."
    else:
        ls "Here it is. Come in [pov]."
    ls "But you must promise me, that you'll never tell anyone about this place."
    pov "Okay..."
    ls "I'm sure my friend is already waiting and I want you to meet them."
    pov "Your friend?"
    ls "Yes, we spend our time here playing around."
    scene town secret 2pm 002
    povi "She's playing around with a friend at her secret hideout?"
    pov "Is your friend male or female?"
    ls "Male! Stop asking stupid questions and come meet him."
    povi "Wait! A boy playing around with her here? And I need to meet him? What...?"
    ls "Oh hey, there you are! Did you miss me?"
    scene town secret 2pm 003
    povi "Oh! Haha, it's just a cat."
    ls "Yes, yes I'm here now."
    "cat" "Meow!"
    scene town secret 2pm 004
    ls "Look! This is my friend!"
    pov "Oh hello cat."
    ls "And this is my stupid brother, haha."
    pov "What's his name?"
    ls "He has your name."
    pov "Oh how cute, hello [pov]."
    scene town secret 2pm 005
    pov "Hmm... he doesn't like me."
    ls "Haha, no. You must say his name."
    pov "But I did?"
    ls "His name is after you, dummy!"
    pov "Dummy?"
    "cat" "Meow!"
    ls "<giggle>"
    pov "Haha..."
    scene town secret 2pm 006
    pov "So what are you doing here all alone in this secret place?"
    dummy "Meow?"
    pov "I bet you know all her secrets."
    povi "And maybe all her dirty ones too."
    ls "Let me show you something he really loves."
    if inc == True:
        pov "So you're now a dummy too for my cruel sister, haha."
    else:
        pov "So you're now a dummy too for her, haha."
    scene town secret 2pm 007
    ls "He loves it when you stroke his head like this."
    dummy "Purr..."
    pov "Haha, so you want to stroke my head too?"
    ls "Don't be stupid, you're skin isn't that fluffy."
    pov "Maybe you just have to try?"
    ls "Hahaha."
    dummy "MEOW!"
    scene town secret 2pm 008
    pov "What...?"
    dummy "MEOW!"
    ls "Huh?"
    scene town secret 2pm 009
    ls "Huh? What he's doing?"
    pov "You scared him. So he jumped away."
    ls "But he never does that..."
    pov "Wait! I know what's going on."
    ls "Huh?"
    pov "You torture him when you're alone with him here!"
    scene town secret 2pm 010
    ls "What...?"
    pov "That's why you need it to be a secret place. Torturing a little helpless cat."
    ls "You can't be serious?"
    pov "Hahaha... look at your face!"
    ls "You mean...? Haha..."
    jump sp2pmt

label sp2pmt:
    scene town secret 2pm 010
    call screen sp2pmt1

screen sp2pmt1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('sp2pmt1'), Jump('sp2pmtickle')) hovered tt.Action ("Tickle her [lv1] or [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('sp2pmt1'), Jump('sp2pmlove')) hovered tt.Action ("Don't") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label sp2pmtickle:
    pov "You need to be punished for that!"
    ls "Huh?"
    scene town secret 2pm 011
    if inc == True:
        ls "Oh no! Big brother wants to punish me, hahaha."
    else:
        ls "Oh no! [pov] wants to punish me, hahaha."
    pov "Yes, now you're due!"
    if inc == True:
        ls "Hahaha, not so rough, brother."
    else:
        ls "Hahaha, not so rough, [pov]."
    pov "Torturing my name twin. I'll get revenge for him."
    ls "<giggle>"
    ls "Haha, a true cat lover."
    scene town secret 2pm 012
    ls "Hmm... hmm..."
    povi "Wow, is she moaning? Maybe because she noticed my boner."
    pov "No pausing about your punishment, haha."
    if inc == True:
        ls "Big brother?"
    else:
        ls "[pov]?"
    pov "Hmm..."
    ls "Maybe we should stop now? I felt something down there again."
    jump sp2pmt2

label sp2pmt2:
    scene town secret 2pm 012
    call screen sp2pmt3

screen sp2pmt3():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('sp2pmt3'), Jump('sp2pmlove')) hovered tt.Action ("Stop it [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('sp2pmt3'), Jump('sp2pmcor')) hovered tt.Action ("Don't stop [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label sp2pmcor:
    pov "Haha, since when does the victim decide when the punishment stops?"
    if inc == True:
        ls "Please brother..."
    else:
        ls "Please [pov]..."
    pov "No! We're not done yet."
    ls "Hnng..."
    scene town secret 2pm 013b
    ls "Stop..."
    pov "Oh no. Do you enjoy your punishment? Haha..."
    ls "Hnng... hah..."
    ls "Your hand... no..."
    pov "Oh? Are you getting horny?"
    if inc == True:
        ls "Brother, no. Hah... hah..."
    else:
        ls "[pov], no. Hah... hah..."
    if lilsiscorruption >= 30:
        jump sp2pmcor2
    else:
        pov "Wait..."
        scene black
        pov "Ouch!"
        povi "Damn, she ran away. But that started good."
        scene town secret 2pm 014b
        pov "And what are you looking at?"
        dummy "Meow!"
        pov "Watching us playing around, you little perv, hahaha..."
        $ lilsiscorruption += 1
        $ dtime += 1
        $ secretplace2pmfirst = True
        jump town


label sp2pmlove:
    scene town secret 2pm 013a
    ls "Haha look. Dummy is back."
    dummy "Meow..."
    pov "He really likes you."
    ls "Yes he knows who is good for him."
    povi "Hmm... she has a cat, named him after me and is in love with him. Interesting."
    dummy "Purr..."
    scene town secret 2pm 014a
    ls "Haha, what are you...?"
    pov "Is something wrong?"
    ls "Hnng... dummy is licking..."
    pov "Oh hahaha... maybe he's hungry?"
    scene town secret 2pm 015a
    ls "Bad dummy! You can't lick me there!"
    pov "Why not? Maybe you're tasty, haha?"
    ls "Hahaha, you see dummy? Now you know where you got you're name."
    pov "I like him!"
    ls "Haha, i bet..."
    ls "I'm going to go back now."
    pov "Okay..."
    $ lilsislove += 1
    $ dtime += 1
    $ secretplace2pmfirst = True
    jump town

label sp2pmcor2:
    $ secret2corfirst = True
    scene town secret 2pm 015b
    "You decide to push it farther."
    ls "Huh?"
    pov "So soft."
    ls "Stop! That's enough punishment."
    ls "Huh?"
    "You hear a dog barking."
    pov "<whisper> It seems someone is walking his dog. So we have to stay quiet."
    pov "<whisper> No one should find your secret place!"
    ls "<whisper> Hmm..."
    povi "It seems she agreed with me, haha."
    povi "Then I should try to push her more."
    jump sp2pmcor2ch

label sp2pmcor2ch:
    call screen sp2pmcor2ch1

screen sp2pmcor2ch1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('sp2pmcor2ch1'), Jump('sp2pmcor3pi')) hovered tt.Action ("Pinch her nipple [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('sp2pmcor2ch1'), Jump('sp2pmcor3ti')) hovered tt.Action ("Play with her tit [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('sp2pmcor2ch1'), Jump('sp2pmcor3ass')) hovered tt.Action ("Grind against her ass [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label sp2pmcor3pi:
    scene town secret 2pm 016b
    $ sp2pmextend = True
    ls "<whisper> Hng..."
    pov "<whisper> You're doing good. Being quiet like a good girl."
    ls "Hmm..."
    pov "<whisper> Shhh... not so loud."
    povi "She's getting turned on and seems to be enjoying it too."
    if inc == True:
        ls "<whisper> Please... hmm... brother..."
    else:
        ls "<whisper> Please... hmm... [pov]..."
    scene town secret 2pm 017b
    ls "Aaah... hah..."
    pov "<whisper> That's too loud. You're enjoying it too much."
    povi "Wow, she is moaning like crazy."
    if lsispronBDSM >= 4:
        ls "<whisper> But you're punishings me like this... hah... master..."
        scene town secret 2pm 018
        pov "What...?"
        ls "What?"
        povi "Did she really call me master?"
        scene town secret 2pm 019
        ls "Nooo... <sob>"
        povi "Wow, she's getting into the BDSM stuff I showed her?"
        povi "Maybe I should follow her?"
        $ lilsiscorruption += 1
        $ dtime += 1
        jump town
    else:
        ls "<whisper> But you punished me too hard."
        pov "<whisper> So you liked it that much?"
        scene town secret 2pm 019
        ls "Nooo... <sob>"
        povi "Wow, did she really enjoyed it that much?"
        povi "Maybe I should follow her?"
        $ lilsiscorruption += 1
        $ dtime += 1
        jump town

label sp2pmcor3ti:
    scene town secret 2pm 016c
    $ sp2pmextend = True
    ls "<whisper> Hng..."
    pov "<whisper> You're doing good. Being quiet like a good girl."
    "You rub her crotch more."
    ls "Hmm..."
    pov "<whisper> Shhh... not so loud."
    povi "She's getting turned on and seems to enjoy it."
    if inc == True:
        ls "<whisper> Please... hmm... brother..."
    else:
        ls "<whisper> Please... hmm... [pov]..."
    scene town secret 2pm 017c
    ls "Aaah... hah..."
    pov "<whisper> That's too loud. You're enjoying it to much."
    povi "Wow, she is moaning like crazy."
    ls "<whisper> I'm so wet."
    scene town secret 2pm 018
    pov "What...?"
    ls "What?"
    povi "Did she really say that?"
    scene town secret 2pm 019
    ls "Nooo... <sob>"
    povi "Wow, did she really enjoy it that much?"
    povi "Maybe I should follow her?"
    $ lilsiscorruption += 1
    $ dtime += 1
    jump town

label sp2pmcor3ass:
    scene town secret 2pm 016d
    $ sp2pmextend = True
    ls "<whisper> Hng..."
    pov "<whisper> You're doing good. Being quiet like a good girl."
    "You start grind your crotch against her ass."
    ls "<whisper> What are you...?"
    pov "<whisper> Shh..."
    ls "Hmm..."
    pov "<whisper> Shhh... not so loud."
    povi "She's getting turned on and seems to enjoy it."
    if inc == True:
        ls "<whisper> Please... hmm... brother..."
    else:
        ls "<whisper> Please... hmm... [pov]..."
    scene town secret 2pm 017d
    ls "Aaah... hah..."
    pov "<whisper> That's too loud. You're enjoying it to much."
    povi "Wow, she is moaning like crazy."
    if lsispronanal >= 4:
        ls "<whisper> Hah... deeper in my ass!"
    else:
        ls "<whisper> Hah... harder!"
    scene town secret 2pm 018d
    pov "What...?"
    ls "What?"
    povi "Did she really say that?"
    scene town secret 2pm 019
    ls "Nooo... <sob>"
    povi "Wow, did she really enjoy it that much?"
    povi "Maybe I should follow her?"
    $ lilsiscorruption += 1
    $ dtime += 1
    jump town

#----- Alexis Secret Place NTR Events -----
label secretplace:
    scene town secret 2pm 001n
    $ davidecumface = False
    $ davidecuminside = False
    $ mccumface = False
    $ mccuminside = False
    $ secretpmcwatch = False
    $ secret2likentr = False
    $ lilsisrelationship += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    call screen checkdarkerpaths_alexis
    scene town secret 2pm 001n
    povi "Oh it's \"Dummy\". He's running away. I wonder why?"
    povi "And why is the door open? Maybe there is a stranger inside? The cat wouldn't leave when [ls] is there."
    scene town secret 2pm 002n
    if alexis_voyeur == True or alexis_ntr == True:
        ls "<giggle>"
    else:
        ls "Hey, stop that!"
    povi "Oh, she is here."
    ls "Why doesn't that count. I pressed the button. You cheated again?"
    povi "Wait! There is somebody with her? I wonder who it is."
    scene town secret 2pm 003n
    if alexis_voyeur == True or alexis_ntr == True:
        ls "Stop pulling my nipples <giggle>. That's cheating."
    else:
        ls "Stop pulling my nipples... you're cheating."
        povi "She sounds... wierd..."
    davide "I'm only helping you to relax, haha."
    call screen secret2ntrchoose

screen secret2ntrchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('secret2ntrchoose'), Jump('secretplacentrlike')) hovered tt.Action ("Show yourself") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('secret2ntrchoose'), Jump('secretplacentrlikeh')) hovered tt.Action ("Watch them secretly") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label secretplacentrlike:
    if alexis_voyeur == True:
        povi "So they're having fun together. But what's this?"
    elif alexis_ntr == True:
        povi "Is she with a boyfriend? I didn't know she was seeing anyone..."
    elif alexis_revenge == True:
        povi "What the hell is going on here?"
    else:
        povi "Pulling my nipples? Sounds like something fun is going here."
    scene town secret 2pm 005n
    povi "Oh he's using the drug on her. He's such an ass. I bet this is how he gets girls."
    povi "I have to admit though, I'm pretty curious about that drug still."
    scene town secret 2pm 006ns
    if inc == True:
        ls "Oh hey brother."
    else:
        ls "Oh hey [pov]."
    davide "Huh?"
    if alexis_voyeur == True:
        pov "Hey you two. Having fun here I see?"
    elif alexis_ntr == True:
        pov "Hey Alexis. Davide. So what's going on here?"
    elif alexis_revenge == True:
        pov "Hey [ls], are you ok?"
    else:
        pov "Having some fun here I see?"
    ls "I'm showing Davide my secret place. And now we're playing this game."
    pov "A game?"
    if alexis_voyeur == True:
        povi "He tricked her to get her naked. Nice \"playing\". Ha!"
    elif alexis_ntr == True:
        povi "He tricked her to get her naked. I hate this guy!"
    elif alexis_revenge == True:
        povi "He drugged and tricked her to get her naked. I'm sure of it!"
    else:
        povi "Drugging her to get her naked. Sounds like my kind \"playing\". Ha!"
    scene town secret 2pm 007ns
    davide "Yes. But she's losing big time, haha."
    ls "That's not fair. I pressed the button. Why is this game so hard?"
    if alexis_revenge == True:
        povi "She's clearly not reacting normally to things. This is messed up."
        povi "I need to see if I can get her away from him, she wouldn't want this if she wasn't drugged."
    pov "Oh I see. And you're good at playing this \"game\" Davide?"
    davide "Haha, you noticed?"
    if inc == True:
        davide "Your little sister is like a gem that needs to be polished."
    else:
        davide "[ls] is like a gem that needs to be polished."
    davide "I only need use a grinder, haha."
    if alexis_voyeur == True:
        pov "I see, haha."
    elif alexis_ntr == True:
        povi "Seriously, metaphoric innuendo now? What an ass!"
    elif alexis_revenge == True:
        pov "I see..."
    else:
        pov "I see, haha."
    scene town secret 2pm 008ns
    ls "Ugh! I lost again."
    davide "Well at least you tried and did your best."
    davide "But now it's time to do your last dare."
    ls "Hmpf!"
    davide "Come on. If you want to be my girlfriend you have to deliver!"
    if alexis_revenge == True:
        povi "Seriously Davide, your girlfriend?! You're taking advantage of her under the influence. I'm going to kick your ass one day!"
    scene town secret 2pm 009ns
    if alexis_voyeur == True:
        ls "<giggle> OK, my lover. I can do that."
        povi "Wow. They're moving on fast."
        if inc == True:
            ls "I hope it doesn't bother you to see me naked, brother?"
        else:
            ls "I hope it doesn't bother you to see me naked, [pov]?"
        pov "No. I think I can endure that."
        ls "Haha, you dummy."
    elif alexis_ntr == True:
        ls "<giggle> OK, my lover. I can do that."
        povi "Damn it Davide, you're not wasting any time..."
        if inc == True:
            ls "I hope it doesn't bother you to see me naked, brother?"
        else:
            ls "I hope it doesn't bother you to see me naked, [pov]?"
        pov "What? Who are..."
        ls "Haha, you dummy."
    elif alexis_revenge == True:
        ls "OK... I have to do that..."
        povi "No you don't!"
        if inc == True:
            ls "I hope it doesn't bother you to see me naked, brother?"
        else:
            ls "I hope it doesn't bother you to see me naked, [pov]?"
        pov "I think I will manage..."
        ls "Haha, you dummy."
    else:
        ls "OK... I have to do that..."
        povi "Well you don't have to do that, but yeah... it's going to happen. Haha."
        if inc == True:
            ls "I hope it doesn't bother you to see me naked, brother?"
        else:
            ls "I hope it doesn't bother you to see me naked, [pov]?"
        pov "I think I will manage."
        ls "Haha, you dummy."
    davide "Let me see that kitty."
    scene town secret 2pm 010ns
    ls "Slowly..."
    if alexis_revenge == True:
        povi "It's like she's in a trance... The drugs have to be messing with her mind now. She's not like this."
    davide "Yes, there it is."
    pov "Why are you making that weird face, [ls]?"
    ls "It's not easy to keep balance."
    if alexis_voyeur == True:
        povi "She's playing around like this is all normal... I wonder how fast this will change when Davide fucks her."
        povi "But..."
    elif alexis_ntr == True:
        povi "She's playing around like this is all normal... I don't want this to go further."
    elif alexis_revenge == True:
        povi "Damn, she's pratically drunk from the drug. I need to get her out of here before Davide tries to fuck her."
    else:
        "It probably won't be easy to keep your balance when he starts fucking you either."
    scene town secret 2pm 012ns
    if alexis_voyeur == True or alexis_sadist == True:
        pov "Wow!"
    else:
        povi "Damn, she shaved!"
    davide "Hell yeah."
    ls "What's wrong?"
    davide "We're just admiring your tight kitty, girl!"
    ls "Oh... <giggle>"
    ls "Davide told me that he likes tight girls very much. Like me."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Oh I'm sure she'll be corrupted very soon!"
    else:
        povi "Oh, I'm sure he did. But in your current state, you just don't understand how fuck up this is."
    scene town secret 2pm 013ns
    if alexis_voyeur == True:
        ls "So you like my body?"
        davide "Yes but I'll like it more when I've conquered everything."
        ls "<giggle>"
        pov "You're damn lucky man."
        davide "Oh yes, hahaha. But maybe I'm not the only one."
    elif alexis_ntr == True:
        ls "So you like my body?"
        davide "Yes but I'll like it more when I've conquered everything."
        ls "<giggle>"
        pov "I don't... Maybe she's ready for that yet, Davide?"
        davide "Oh she's ready, hahaha. But maybe I'm not the only one."
    elif alexis_revenge == True:
        ls "Can I get dressed now?"
        davide "No, I'm not done conquering you yet."
        ls "Conquer?"
        pov "I don't think she's ready for that yet, Davide."
        davide "Oh she's ready, hahaha. But maybe I'm not the only one."
    else:
        ls "Can I get dressed now?"
        davide "No, I'm not done conquering you yet."
        ls "Conquer?"
        pov "You heard what Davide said [ls], he needs to conquer you more."
        davide "Yup she's ready for more, hahaha. But maybe I'm not the only one."
    pov "Huh?"
    scene town secret 2pm 014ns
    davide "Stay down there cutie. I have something else for you to do too."
    if alexis_voyeur == True or alexis_sadist == True:
        pov "Not wasting any time, haha?"
        davide "She needs to learn it some time and now is that time!"
        ls "I'm sure I know what you want me to do <giggle>"
        povi "I wonder how much he told her about perverted stuff since they've known each other."
        povi "And how much they're are meeting without my knowing about it."
    else:
        povi "Please don't be what I think it is..."
        davide "She needs to learn it some time and now is that time?"
        if alexis_ntr == True:
            ls "I'm sure I know what you want me to do <giggle>"
        else:
            ls "I'm not sure I know what you want me to do."
        povi "I wonder how much he told her about perverted stuff since they've known each other."
        povi "And if he's hanging out with her when I'm not around all the time now? Fucking Davide!"
    scene town secret 2pm 015ns
    if alexis_voyeur == True or alexis_sadist == True:
        ls "I knew it, haha. You want me to play with your worm."
        pov "Worm. Hahahaha..."
        davide "Damn girl! SNAKE! Call it a snake, not a worm."
        ls "OK. Your snake is so big."
        davide "Much better. Go on now and serve my snake."
        ls "<giggle>"
    else:
        ls "You want me to play with your worm?"
        if alexis_ntr == True:
            pov"Worm? Haha!"
        else:
            pov "Worm? Hmph... hehe."
        davide "Damn girl! SNAKE! Call it a snake, not a worm."
        ls "OK... Geez! Your \"snake\"."
        davide "Much better. Go on now and serve my snake."
        ls "..."
        if alexis_ntr == True:
            povi "I can't do anything to stop this. He's just too strong."
        else:
            povi "I can't do anything yet, his hand is practically around her neck. He could really hurt her."
    scene town secret 2pm 016ns
    if alexis_voyeur == True or alexis_ntr == True:
        ls "It's so hard and warm."
        povi "Holy shit. Is she really going to..."
        davide "You told me that you already know what to do. So show me what the internet taught you."
        povi "Wait! [ls] prepared herself already?"
        if alexis_voyeur == True:
            povi "That's awesome!"
        ls "I'll do my best <giggle>"
    else:
        ls "It's hard..."
        povi "Holy shit. Is she really going to..."
        davide "You told me that you already know what to do. So show me what the internet taught you."
        if alexis_revenge == True:
            povi "Wait! [ls] don't do it!"
            ls "Fine, but only because you said you'd be mean if I didn't before."
            povi "I knew he was doing the same shit again. Once I find a way to get rid of him for good..."
        else:
            pov "I'm interested in seeing that too."
            ls "Fine, but only because you said you'd be mean if I didn't before."
            povi "I knew he was doing the same thing again. It's easy to threaten little girls into doing shit."
    scene town secret 2pm 017ns
    if inc == True:
        ls "But isn't it weird with my brother watching?"
    else:
        ls "But isn't it weird with [pov] watching?"
    davide "Haha, I think he's seen something like this before."
    if inc == True:
        ls "But it's my brother!"
    else:
        ls "But it's [pov]!"
    davide "Oh yes, how rude of me. Do you want to join us [pov]?"
    pov "Huh?"
    call screen secret2ntrjoin

screen secret2ntrjoin():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('secret2ntrjoin'), Jump('secretplacentrlikejoin')) hovered tt.Action ("Join them") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('secret2ntrjoin'), Jump('secretplacentrdislikewatch')) hovered tt.Action ("Just watch") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label secretplacentrlikejoin:
    if alexis_voyeur == True:
        pov "Oh hell yeah. Let's see what [ls] can do."
    elif alexis_ntr == True:
        pov "Yeah..."
    elif alexis_revenge == True:
        povi "Ok, this is beyond messed up, but if I say no, Davide might try to kick me out... Sorry [ls]."
        pov "Yeah, I think I will join you..."
    else:
        pov "Oh hell yeah. Let's see what [ls] can do."
    ls "What? But..."
    scene town secret 2pm 018ns
    davide "What's wrong? You want to please people right? So you can please him too."
    if inc == True:
        ls "But he's my brother. And I thought you're my boyfriend?"
    else:
        ls "But I've known him for so long. And I thought you're my boyfriend?"
    if alexis_revenge == True:
        povi "Seriously, she's almost slurring her words. This drug is messing her up."
    davide "Yes but I like to share and that's something you need to learn too."
    davide "What's wrong about it? Isn't it good if you can share something good and show it to others?"
    if alexis_voyeur == True:
        povi "Haha, damn what a smooth talker."
    elif alexis_ntr == True:
        povi "I don't like that I have to be here with Davide, but I can't pass this up."
    elif alexis_revenge == True:
        povi "What a manipulative piece of shit!"
    else:
        "What a manipulative piece of shit... I don't mind."
    ls "Hm..."
    if inc == True:
        davide "And there's nothing bad about him being your brother."
    else:
        davide "And there's nothing bad about you knowing each other for so long."
    if alexis_voyeur == True:
        povi "He's so damn right."
    scene town secret 2pm 019ns
    ls "I think you're right. You can join [pov]."
    if alexis_voyeur == True:
        pov "Hell yes!"
    elif alexis_ntr == True:
        pov "Thanks..."
    elif alexis_revenge == True:
        pov "Ok [ls]..."
    else:
        pov "Of course I can, you would never tell me no, right [ls]?"
    davide "I'm sure you'll enjoy it, haha."
    "You pull your dick out."
    if alexis_revenge == True:
        povi "I'm going to hell... again..."
    scene town secret 2pm 020ns
    ls "Oh..."
    if inc == True:
        davide "It's the first time you've seen your brothers dick?"
    else:
        davide "It's the first time you've seen his dick?"
    ls "Y... yes."
    if alexis_voyeur == True:
        pov "Don't be shy, [ls]."
    elif alexis_ntr == True:
        povi "But hopefully it will be just the two of us next time."
    elif alexis_revenge == True:
        pov "It's ok, [ls]."
    else:
        pov "Don't be shy, [ls]."
    davide "Yes go on, show us what you can do."
    scene town secret 2pm 021ns
    ls "OK."
    if inc == True:
        ls "You also seems to be very excited, big brother."
    else:
        ls "You also seems to be very excited, [pov]."
    if alexis_voyeur == True:
        pov "Oh yes I am. Feeling your soft hand on my dick."
    elif alexis_ntr == True:
        pov "I can't help it, your hands are so soft."
    elif alexis_revenge == True:
        pov "yeah, its from feeling your soft hand on my dick."
    else:
        pov "I definitely am."
    davide "Yes that's nice, but I'm here for more action."
    if alexis_voyeur == True or alexis_ntr == True:
        ls "Oh I can do more."
    else:
        ls "I need to do more?"
    scene town secret 2pm 022ns
    davide "Use your mouth now."
    ls "<kiss>"
    davide "Oh yes, a good start."
    "[ls] strokes your dick too."
    if alexis_voyeur == True:
        if inc == True:
            povi "Seeing my little sister giving her boyfriend and me a blow-job."
        else:
            povi "Seeing [ls] giving her boyfriend and me a blow-job."
        povi "This is like heaven."
    elif alexis_ntr == True:
        if inc == True:
            povi "Seeing my little sister like this..."
        else:
            povi "Seeing [ls] like this..."
        povi "This is like heaven."
    elif alexis_revenge == True:
        if inc == True:
            povi "Seeing my little sister giving Davide a blow-job makes me sick."
        else:
            povi "Seeing [ls] giving Davide a blow-job makes me sick."
        povi "This is like hell."
    else:
        if inc == True:
            povi "Seeing my little sister like this..."
        else:
            povi "Seeing [ls] like this..."
        povi "It's about time!"
    image bjal_secret_NTR = Movie(channel="bjal_secret_NTR", play="images/anim/NTR/bjal_secret_NTR.webm")
    scene bjal_secret_NTR with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ls "<lick>"
    davide "Hah..."
    if alexis_voyeur == True or alexis_sadist == True:
        pov "Damn!"
        pov "I can't wait to get that licking too."
    else:
        povi "Damn it, this is going to far and there is nothing I can do!"
        pov "[ls] you don't need to lick me too."
    scene town secret 2pm 024ns
    if alexis_voyeur == True or alexis_ntr == True:
        if inc == True:
            ls "Sorry, brother. This is something I'll do only for my boyfriend."
        else:
            ls "Sorry, [pov]. This is something I'll do only for my boyfriend."
        pov "Oh..."
        davide "Normally I'm for full sharing, but this is something I agree with her on."
        davide "But I'm sure you can cum."
        if alexis_voyeur == True:
            pov "Ha, sure but... damn."
        else:
            pov "Ok..."
    elif alexis_revenge == True:
        if inc == True:
            ls "That's ok, brother. This is something I'll do only for my boyfriend."
        else:
            ls "That's ok, [pov]. This is something I'll do only for my boyfriend."
        pov "Ok..."
        povi "I think the drugs are progressing, she's even repeating Davides boyfriend/girlfriend shit!"
        davide "Normally I'd insist on full sharing, but this is something I agree with her on."
        davide "But I'm sure you can cum either way."
        pov "Sure..."
    else:
        if inc == True:
            ls "Sorry, brother. This is something I'll do only for my boyfriend."
        else:
            ls "Sorry, [pov]. This is something I'll do only for my boyfriend."
        pov "That's bullshit."
        davide "Normally I'm for full sharing, but this is something I agree with her on."
        davide "But I'm sure you can cum still."
        povi "Well no shit I can. Next time I'll just make sure he's not here to get greedy."
    scene town secret 2pm 025ns
    ls "So you like what I'm doing, lover?"
    davide "Yes not bad girl. But we can still improve that."
    povi "Damn, she's trying everything to please him."
    ls "Your penis likes it, it got even harder."
    davide "Haha, damn girl. You learn fast."
    scene town secret 2pm 026ns
    if inc == True:
        ls "And you too big brother, getting harder and harder in my hand."
    else:
        ls "And you too [pov], getting harder and harder in my hand."
    povi "She isn't shy or trying to stop anymore. The effect of the drug is getting stronger over time. And I'm very sure she doesn't know anything about it."
    if alexis_voyeur == True:
        povi "But it's also a very nice surprise, so I'll just enjoy it."
    pov "Yes, you're doing very well [ls]."
    if alexis_revenge == True:
        povi "Shit, I'm getting into the handjob too much!"
    ls "<giggle> Thank you."
    davide "Too good, hng."
    scene town secret 2pm 027ns
    davide "I'm about to cum soon, girl! Remember what we talked."
    pov "Huh?"
    ls "I remember, my lover. <giggle>"
    ls "Do you want to put your sperm on my face or in my mouth?"
    if alexis_voyeur == True:
        povi "Fucking shit, that's so hot I'll cum soon too. I hope I can choose where it goes too."
    elif alexis_sadist == True:
        povi "Fucking shit, that's so hot I'll cum soon too. I better get to choose where it goes too."
    else:
        povi "Fucking shit, Davide! He's really been working on her when I'm not around."
    call screen secret2ntrlikedcum

screen secret2ntrlikedcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('secret2ntrlikedcum'), Jump('secretplacentrlikedcumface')) hovered tt.Action ("Davide cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('secret2ntrlikedcum'), Jump('secretplacentrlikedcumin')) hovered tt.Action ("Davide cum in her mouth") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label secretplacentrlikedcumface:
    $ davidecumface = True
    davide "I'll cum on your face, prepare yourself!"
    ls "OK, shoot it on me <giggle>."
    scene town secret 2pm 028ns
    davide "HNNG!"
    ls "Aaah..."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Damn, this is so hot. [ls] is posing like a porn-star."
    scene town secret 2pm 029ns
    ls "Hmm..."
    davide "Look at that, I sprayed her good!"
    if alexis_voyeur == True or alexis_sadist == True:
        pov "Haha, yes."
    else:
        povi "Nooo..."
    if secretpmcwatch == True:
        jump secret2ntrlikeend
    else:
        jump secret2ntrlikemcchoose

label secretplacentrlikedcumin:
    $ davidecuminside = True
    davide "I'll cum in your mouth, prepare yourself!"
    ls "OK. Shoot it in my mouth <giggle>."
    scene town secret 2pm 028nsa
    davide "HNNG!"
    ls "Aaah..."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Damn, this is so hot. [ls] is posing like a porn-star."
    scene town secret 2pm 029nsa
    ls "Hmm..."
    davide "Look at that, I came so much!"
    if alexis_voyeur == True or alexis_sadist == True:
        pov "Haha, yes."
    else:
        povi "Nooo..."
    davide "Now swallow it!"
    scene town secret 2pm 030nsa
    ls "<gulp>"
    davide "Nice. Do you like my taste?"
    ls "Yes! You taste salty and it's thick, but I like it."
    if secretpmcwatch == True:
        jump secret2ntrlikeend
    else:
        jump secret2ntrlikemcchoose

label secret2ntrlikemcchoose:
    if davidecumface == True:
        scene town secret 2pm 031ns
    else:
        scene town secret 2pm 031nsa
    if inc == True:
        ls "Now it's your turn big brother."
    else:
        ls "Now it's your turn [pov]."
    ls "Where do you wan to spray your sperm?"
    povi "Oh shit..."
    if inc == True:
        povi "My little sister is asking me where I want to put my sperm on her!"
    else:
        povi "[ls] is asking me where I want to put my sperm on her!"
    call screen secret2ntrlikemcum

screen secret2ntrlikemcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('secret2ntrlikemcum'), Jump('secretplacentrlikemcumface')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('secret2ntrlikemcum'), Jump('secretplacentrlikemcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label secretplacentrlikemcumface:
    $ mccumface = True
    if alexis_revenge == True:
        povi "Well I came this far..."
    pov "I want to cum on your face."
    ls "Then give it to me."
    if davidecumface == True:
        scene town secret 2pm 032ns1
    else:
        scene town secret 2pm 032ns2
    pov "ARGH!"
    ls "Hnn..."
    if inc == True:
        davide "Haha, yes! Cum on your little sisters face."
    else:
        davide "Haha, yes! Cum on her face."
    if davidecumface == True:
        scene town secret 2pm 033ns1
    else:
        scene town secret 2pm 033ns3
    if inc == True:
        ls "You shot so much on me too brother. <giggle>"
    else:
        ls "You shot so much on me too [pov]. <giggle>"
    pov "Oh yes, I needed that."
    davide "Haha, we can see that."
    ls "So much cum! <giggle>"
    davide "Time to clean yourself up babe. So we can go."
    ls "OK. <giggle>"
    jump secret2ntrlikeend

label secretplacentrlikemcumin:
    $ mccuminside = True
    if alexis_revenge == True:
        povi "Well I came this far..."
    pov "I want to cum in your mouth."
    ls "Then give it to me."
    if davidecumface == True:
        scene town secret 2pm 032ns3
    else:
        scene town secret 2pm 032ns4
    pov "ARGH!"
    ls "Hnn..."
    if inc == True:
        davide "Haha, yes! Cum in your little sisters mouth."
    else:
        davide "Haha, yes! Cum in her mouth."
    if davidecumface == True:
        scene town secret 2pm 033ns4
    else:
        scene town secret 2pm 033ns2
    ls "Hnn..."
    pov "Oh yes, show me what I gave you."
    if inc == True:
        davide "Go on, swallow your brothers junk."
    else:
        davide "Go on, swallow [pov]'s junk."
    ls "Hmm..."
    if davidecumface == True:
        scene town secret 2pm 034ns2
    else:
        scene town secret 2pm 034ns
    ls "<gulp>"
    pov "Wow, you really did it."
    if inc == True:
        davide "And do you like your brothers cum?"
    else:
        davide "And do you like [pov]'s cum?"
    if davidecuminside == True:
        ls "Yes, but yours is thicker and a little bit tastier."
    else:
        ls "Yes, it's thick and salty but good."
    if alexis_voyeur == True or alexis_sadist == True:
        pov "I still can't believe it, that was very hot [ls]."
    ls "<giggle>"
    davide "I think it's time to go back."
    jump secret2ntrlikeend

label secret2ntrlikeend:
    scene town secret 2pm 035ns
    davide "Come here babe, you earned yourself a kiss."
    ls "Oh Davide... <kiss>"
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Oh, she really likes him."
    elif alexis_ntr == True:
        povi "She doesn't actually like him, does she?"
    else:
        povi "Fucking sex drug."
    ls "Your penis is poking on my..."
    davide "Yes, and soon it's time to widen your kitty."
    ls "Oh, hnn..."
    scene black
    "You go back home together."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ davidegood += 1
    $ dtime += 1
    $ secretplace2pmntrfirst = True
    jump frontdoor

label secretplacentrdislikewatch:
    $ secretpmcwatch = True
    if alexis_revenge == True:
        povi "I may not be able to stop this now, but I can make sure it doesn't turn violent."
    pov "No, but I'd love to watch and see what [ls] can do."
    scene town secret 2pm 018ng
    davide "What? You really want to just watch?"
    ls "Eh?"
    if alexis_voyeur == True:
        pov "Yes, she's your girlfriend now. But I want to see what she can do."
    elif alexis_ntr == True:
        pov "Well yeah, I just want to watch..."
    elif alexis_revenge == True:
        pov "Yes, she's your \"girlfriend\" now... But I want to see what she can do."
    else:
        pov "I'll sit this one out. But I do want to see what she can do."
    ls "You want to watch like a pervert?"
    if alexis_ntr == True or alexis_revenge == True:
        povi "Harsh!"
    pov "Hmm... yes."
    scene town secret 2pm 018ns
    davide "That's a little bit surprising but if he wants to, we should let him."
    davide "Maybe he can learn something, haha."
    if inc == True:
        ls "But he's my brother. And I thought you're my boyfriend?"
    else:
        ls "But I known him for so long. And I thought you're my boyfriend?"
    if alexis_revenge == True:
        povi "Seriously, she's almost slurring her words. This drug is messing her up."
    davide "Yes but I want to show him what my babe can do."
    davide "What's wrong about it, when you have something good show it to others?"
    if alexis_voyeur == True:
        povi "Haha, damn what a smooth talker."
    elif alexis_ntr == True:
        povi "I don't like that I have to be here with Davide, but I can't pass this up."
    elif alexis_revenge == True:
        povi "What a manipulative piece of shit!"
    else:
        povi "What a manipulative piece of shit... I'm ok with that."
    ls "Hm..."
    if inc == True:
        davide "And there's nothing bad about him being your brother."
    else:
        davide "And there's nothing bad about you knowing each other all your life."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "He's so damn right."
    scene town secret 2pm 019ns
    ls "I think you're right. You can watch us [pov]."
    pov "Hell yes!"
    if alexis_revenge == True:
        povi "Sorry for the this [ls] I need you guys to believe I'm just a perv that likes to watch, so I can make sure you're ok when Davide is done."
    davide "I'm sure you'll enjoy it, haha."
    scene town secret 2pm 021nw
    ls "Hm..."
    pov "Don't be shy, [ls]."
    davide "Yes go on, show us what you can do."
    if inc == True:
        ls "You really like watching me doing this, big brother?"
    else:
        ls "You really like watching me doing this, [pov]?"
    pov "Yes, you're all naked and doing perverted things, it's very hot."
    davide "Hahaha..."
    scene town secret 2pm 022nw
    ls "<kiss>"
    davide "Oh yes, a good start."
    if alexis_voyeur == True:
        if inc == True:
            povi "Seeing my little sister giving her boyfriend and me a blow-job."
        else:
            povi "Seeing [ls] giving her boyfriend and me a blow-job."
        povi "This is like heaven."
    elif alexis_ntr == True:
        if inc == True:
            povi "Seeing my little sister like this..."
        else:
            povi "Seeing [ls] like this..."
        povi "This is like heaven."
    elif alexis_revenge == True:
        if inc == True:
            povi "Seeing my little sister giving Davide a blow-job makes me sick."
        else:
            povi "Seeing [ls] giving Davide a blow-job makes me sick."
        povi "This is like hell."
    else:
        if inc == True:
            povi "Seeing my little sister like this..."
        else:
            povi "Seeing [ls] like this..."
        povi "It's about time."
    scene town secret 2pm 023nw
    ls "<lick>"
    davide "Hah..."
    pov "Damn! That's somewhat cute."
    scene town secret 2pm 024nw
    ls "And how I am doing?"
    pov "I'm a little surprised at what you're showing us. Very nice, haha."
    ls "<giggle>"
    davide "Haha crazy. But don't forget that you're my girl, babe!"
    scene town secret 2pm 025nw
    ls "Yes, Davide. You're my only lover."
    davide "Good girl. Then go on and stroke my dick harder so I can reward you."
    ls "As you wish."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Damn, this gets even better."
    scene town secret 2pm 026nw
    ls "His penis is getting harder and harder in my hand."
    povi "She isn't shy or trying to stop anymore. The effect of the drug is getting stronger over time. And I'm very sure she doesn't know anything about it."
    if alexis_voyeur == True:
        povi "But a very nice surprise, so I'll just enjoy it."
    pov "Yes I think you're doing very good [ls]."
    ls "<giggle> Thank you."
    davide "Too good, hng."
    scene town secret 2pm 027nw
    davide "I'm about to cum soon, girl! Remember what we talked."
    pov "Huh?"
    ls "I remember, my lover. <giggle>"
    ls "Do you want to put your sperm on my face or in my mouth?"
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Fucking shit, that's so hot."
    call screen secret2ntrlikedcum

label secretplacentrlikeh:
    povi "They didn't notice me, so I will watch them secretly."
    call screen checkdarkerpaths_alexis
    jump secretplacentrdislike

label secretplacentrdislike:
    povi "What's this?"
    scene town secret 2pm 005n
    povi "Oh he's using the drug on some girl. He's such an asshole, this has to be how he con's his girls."
    povi "I'm curious about that drug though."
    if alexis_ntr == True or alexis_revenge == True:
        if inc == True:
            povi "That asshole is drugging my little sister. Why is she here with him?"
        else:
            povi "That asshole is drugging her. Why is she here with him?"
    scene town secret 2pm 008ns
    ls "Ugh! I lost again."
    davide "Well at least you tried and gave your best."
    davide "But now it's time to do your last dare."
    ls "Hmpf!"
    davide "Come on. If you want to be my girlfriend you have to deliver!"
    scene town secret 2pm 010ns
    ls "<giggle> OK, my lover. I can do that."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Wow. They're moving on fast."
    else:
        povi "What did he talk her into?"
    davide "Yes let me see your kitty, my little slut."
    ls "<giggle> Oh Davide."
    if alexis_voyeur == True:
        povi "Wow, she's already naked."
    elif alexis_ntr == False:
        povi "That asshole. I don't want her with him!"
    elif alexis_revenge == True:
        povi "That asshole. Forcing her into this and then calling her a slut."
    else:
        povi "Wow, the bitch is already naked."
    scene town secret 2pm 012ns
    povi "Damn, her naked pussy."
    scene town secret 2pm 013ns
    ls "So you like my body?"
    davide "Yes but I'll like it more when I've conquered everything."
    ls "<giggle>"
    if alexis_voyeur == True or alexis_sadist == True:
        povi "You're damn lucky man."
    else:
        povi "I can't believe this. Why is she falling so easily for him?"
    scene town secret 2pm 014ns
    davide "Stay down there slut! I have something else for you to do."
    ls "I'm sure I know what you want me to do <giggle>"
    povi "I wonder how much he told her about perverted stuff since they known each other."
    povi "And if they're meeting without me knowing."
    scene town secret 2pm 015ns
    ls "I knew it, haha. You want me to play with your worm."
    pov "Worm. Hahahaha..."
    davide "Damn slut! SNAKE! Call it a snake, not a worm."
    ls "OK. Your snake is so big."
    davide "Much better. Go on now and serve my snake."
    ls "<giggle>"
    if alexis_voyeur == True:
        povi "Here they go."
    elif alexis_ntr == False:
        povi "No, I don't want to see this, but I just can't seem to walk away either."
    elif alexis_revenge == True:
        povi "No, I don't want to see this, but I need to be sure that he won't hurt her."
    else:
        povi "Here they go."
    scene town secret 2pm 016ns
    ls "It's so hard and warm."
    povi "Holy shit. Is she really going to..."
    davide "You told me that you already know what to do. So show me what the internet taught you."
    povi "Wait! [ls] prepared herself already?"
    ls "I'll do my best <giggle>"
    if alexis_revenge == False:
        povi "What are you doing with her? She was so pure and innocent!"
    scene town secret 2pm 022n
    ls "<kiss>"
    davide "Oh yes, a good start."
    if inc == True:
        povi "Watching my little sister giving him a blow-job..."
    else:
        povi "Watching [ls] giving him a blow-job..."
    if alexis_ntr == True or alexis_revenge == True:
        povi "...this is like hell."
    else:
        povi "...this is like heaven."
    scene town secret 2pm 023n
    ls "<lick>"
    davide "Hah..."
    if secret2likentr == False:
        povi "Stop corrupting her."
    else:
        povi "This is getting better and better."
    ls "Am I doing good?"
    davide "Yes but you can go even further."
    scene town secret 2pm 024n
    davide "Good, suck on it."
    ls "It's so big. <kiss>"
    davide "That's a very nice view. Seeing my slutty girl down on me."
    if alexis_ntr == True or alexis_revenge == True:
        povi "..."
    else:
        povi "I can barely believe that he's getting her to do this so fast."
    davide "Go on, do more."
    scene town secret 2pm 025n
    davide "I'll help you!"
    ls "HNNG!"
    ls "S... Stop... I can't..."
    davide "Come on get it deeper in!"
    if alexis_ntr == True or alexis_revenge == True:
        povi "You damn motherfucker, stop hurting her!"
    else:
        povi "Oh he wants to get her deep throating, but he's really too big for her little mouth."
    scene town secret 2pm 026n
    davide "Take it deeper little slut!"
    ls "Ugh! Ugh! <choke>"
    if alexis_ntr == True or alexis_revenge == True:
        if alexis_revenge == True:
            povi "She can't breathe! I'll kill you for that, I'll kill you!"
        else:
            povi "She can't breathe and I can't do anything to help her!"
    else:
        if alexis_voyeur == True:
            povi "That's a little bit too much for her on her first time. I hope he won't hurt her."
        else:
            povi "That's a little bit too much for her on her first time. He might hurt her..."
    davide "Try harder!"
    ls "HNNG..."
    "He released her."
    scene town secret 2pm 027n
    ls "I'm so... sorry. I... tried, but I can't."
    davide "OK. It wasn't that bad either. But we need to train this more."
    davide "I want to ram my dick down your throat!"
    ls "OK. So you're not mad at me?"
    davide "I can forgive you, but you have to make me cum good."
    if alexis_ntr == True or alexis_revenge == True:
        povi "She's just a kid..."
    else:
        povi "Oh yes. I like to see her getting slutty."
    scene town secret 2pm 028n
    ls "I can do that. You'll love to cum from me."
    davide "We'll see. Now go on slut!"
    if alexis_ntr == True or alexis_revenge == True:
        povi "Stop it! Please just stop..."
    scene town secret 2pm 029n
    ls "<lick>"
    davide "Much better. Seeing you slut with tears in your eyes after you tried hard is very nice."
    ls "<faster licking>"
    davide "I'll teach you more to become a good slut!"
    ls "Yes, teach me lover."
    if alexis_ntr == True or alexis_revenge == True:
        if alexis_ntr == True:
            povi "Nooo! Please don't do this [ls]!"
        else:
            povi "Nooo! I need to find a way to stop this fast."
    else:
        povi "Damn, she'll fall quickly."
    scene town secret 2pm 030n
    davide "Damn, you're right. I'm about to cum!"
    ls "Where do you want to put your sperm?"
    if alexis_revenge == True:
        povi "At least he can't hurt her anymore..."
    call screen secret2ntrdislikedcum

screen secret2ntrdislikedcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('secret2ntrdislikedcum'), Jump('secretplacentrdislikedcumface')) hovered tt.Action ("Davide cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('secret2ntrdislikedcum'), Jump('secretplacentrdislikedcumin')) hovered tt.Action ("Davide cum in her mouth") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label secretplacentrdislikedcumface:
    $ davidecumface = True
    davide "I'll cum on your face, prepare yourself!"
    ls "OK, shoot it on me <giggle>."
    scene town secret 2pm 031n
    davide "HNNG!"
    ls "Aaah..."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Damn, this is so hot. [ls] is posing like a porn-star."
    davide "Yes, take it slut!"
    scene town secret 2pm 032n
    ls "You came so much."
    davide "Yes I like to paint your face."
    ls "<giggle>"
    davide "And we need to do this more often."
    ls "Anything for my lover."
    davide "And soon I'll widen your cherry!"
    scene town secret 2pm 033n
    ls "You want to... make love to me?"
    davide "Hahaha... love. No I want to pound you until you're screaming, slut!"
    ls "Hnn..."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "I need to see this then too. That would be great."
    else:
        if alexis_revenge == True:
            povi "I can't let it happen. I need to find a way out for her and a way to punish him."
        else:
            povi "Please say this isn't actually happening?!? I can't stop it!"
    davide "Get dressed so we can go, slut!"
    ls "Y...yes Davide."
    jump secret2ntrdislikenend

label secretplacentrdislikedcumin:
    $ davidecuminside = True
    davide "I'll cum in your mouth, prepare yourself!"
    ls "OK. Shoot in my mouth <giggle>."
    scene town secret 2pm 031n2
    davide "HNNG!"
    ls "Aaah..."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Damn, this is so hot. [ls] is posing like a porn-star."
    davide "Yes, take it slut!"
    scene town secret 2pm 032n2
    davide "Yes. A good slut shows what she earned."
    ls "Here..."
    davide "Now go on and swallow your reward."
    scene town secret 2pm 033n2
    ls "<gulp>"
    ls "Are you happy with me now?"
    davide "Yes, that wasn't bad. I came good."
    ls "<giggle>"
    davide "And we need to do this more often."
    ls "Anything for my lover."
    davide "And soon I'll widen your cherry!"
    scene town secret 2pm 034n2
    ls "You want to... make love to me?"
    davide "Hahaha... love. No I want to pound you until you're screaming, slut!"
    ls "Hnn..."
    if alexis_voyeur == True or alexis_sadist == True:
        povi "I need to see this then too. That would be great."
    else:
        if alexis_revenge == True:
            povi "I can't let it happen. I need to find a way out for her and a way to punish him."
        else:
            povi "Please say this isn't actually happening?!? I can't stop it!"
    davide "Get dressed so we can go, slut!"
    ls "Y...yes Davide."
    jump secret2ntrdislikenend

label secret2ntrdislikenend:
    scene black
    "You leave them before they can notice you."
    "You see them leaving shortly after you."
    if alexis_voyeur == True or alexis_sadist == True:
        $ davidegood += 1
        povi "Damn that was hot."
    else:
        $ davidebad += 1
        if alexis_revenge == True:
            povi "I need to plan my revenge."
        else:
            povi "Why does this keep happening to me?!"
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ dtime += 1
    $ secretplace2pmntrfirst = True
    jump frontdoor
