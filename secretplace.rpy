
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
    ls "I want to show you something. Please follow me but take care that no one sees us."
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
    pov "{i}She's playing around with a friend at her secret hideout?{/i}"
    pov "Is your friend male or female?"
    ls "Male! Stop asking stupid questions and meet him."
    pov "{i}Wait! A boy playing with her around here? And I need to meet him? What...?{/i}"
    ls "Oh hey, there you are! Did you miss me?"
    scene town secret 2pm 003
    pov "{i}Oh! Haha, it's just a cat.{/i}"
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
    pov "{i}And maybe all her dirty ones too.{/i}"
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
    pov "You torture him when you're alone here with him."
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
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 490 ypos 122 action (Hide ('sp2pmt1'), Jump('sp2pmtickle')) hovered tt.Action ("Tickle her [lv1] or [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 490 ypos 245 action (Hide ('sp2pmt1'), Jump('sp2pmlove')) hovered tt.Action ("Don't") focus_mask True


    frame:
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
        ls "Hahaha, not so wild, brother."
    else:
        ls "Hahaha, not so wild, [pov]."
    pov "Torturing my name twin. I'll revenge him."
    ls "<giggle>"
    ls "Haha, a true cat lover."
    scene town secret 2pm 012
    ls "Hmm... hmm..."
    pov "{i}Wow, is she moaning? Maybe because she noticed my boner.{/i}"
    pov "No pausing about your punishment, haha."
    if inc == True:
        ls "Big brother?"
    else:
        ls "[pov]?"
    pov "Hmm..."
    ls "Can we please stop it? I feel a little uncomfortable."
    jump sp2pmt2


label sp2pmt2:
    scene town secret 2pm 012
    call screen sp2pmt3

screen sp2pmt3():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 227 ypos 812 action (Hide ('sp2pmt3'), Jump('sp2pmlove')) hovered tt.Action ("Stop it [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 366 ypos 812 action (Hide ('sp2pmt3'), Jump('sp2pmcor')) hovered tt.Action ("Don't stop [cr1]") focus_mask True


    frame:
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
        pov "{i}Damn, she ran away. But that started good.{/i}"
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
    pov "{i}Hmm... she has a cat, named him after me and is in love with him. Interesting.{/i}"
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
    ls "I'll go back now."
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
    pov "{i}It seems she agreed with me, haha.{/i}"
    pov "{i}Then I should try to push her more.{/i}"
    jump sp2pmcor2ch

label sp2pmcor2ch:
    call screen sp2pmcor2ch1

screen sp2pmcor2ch1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 555 ypos 509 action (Hide ('sp2pmcor2ch1'), Jump('sp2pmcor3pi')) hovered tt.Action ("Pinch her nipple [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 555 ypos 414 action (Hide ('sp2pmcor2ch1'), Jump('sp2pmcor3ti')) hovered tt.Action ("Play with her tit [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1289 ypos 863 action (Hide ('sp2pmcor2ch1'), Jump('sp2pmcor3ass')) hovered tt.Action ("Bump on her ass [cr1]") focus_mask True

    frame:
        xalign .5
        text tt.value


label sp2pmcor3pi:
    scene town secret 2pm 016b
    $ sp2pmextend = True
    ls "<whisper> Hng..."
    pov "<whisper> You're doing good. Suppress your voice."
    ls "Hmm..."
    pov "<whisper> Shhh... not so loud."
    pov "{i}She's getting turned on and seems to enjoy it.{/i}"
    if inc == True:
        ls "<whisper> Please... hmm... brother..."
    else:
        ls "<whisper> Please... hmm... [pov]..."
    scene town secret 2pm 017b
    ls "Aaah... hah..."
    pov "<whisper> That's too loud. You're enjoying it to much."
    pov "{i}Wow, she is moaning like crazy.{/i}"
    if lsispronBDSM >= 4:
        ls "<whisper> But you punished me like this... hah... master..."
        scene town secret 2pm 018
        pov "What...?"
        ls "What?"
        pov "{i}Did she really call me master?{/i}"
        scene town secret 2pm 019
        ls "Nooo... <sob>"
        pov "{i}Wow, she's getting into the BDSM stuff I showed her?{/i}"
        pov "{i}Maybe I should follow her?{/i}"
        $ lilsiscorruption += 1
        $ dtime += 1
        jump town
    else:
        ls "<whisper> But you punished me too hard."
        pov "<whisper> So you liked it that much?"
        scene town secret 2pm 019
        ls "Nooo... <sob>"
        pov "{i}Wow, did she really enjoyed it that much?{/i}"
        pov "{i}Maybe I should follow her?{/i}"
        $ lilsiscorruption += 1
        $ dtime += 1
        jump town

label sp2pmcor3ti:
    scene town secret 2pm 016c
    $ sp2pmextend = True
    ls "<whisper> Hng..."
    pov "<whisper> You're doing good. Suppress your voice."
    "You rub her crotch more."
    ls "Hmm..."
    pov "<whisper> Shhh... not so loud."
    pov "{i}She's getting turned on and seems to enjoy it.{/i}"
    if inc == True:
        ls "<whisper> Please... hmm... brother..."
    else:
        ls "<whisper> Please... hmm... [pov]..."
    scene town secret 2pm 017c
    ls "Aaah... hah..."
    pov "<whisper> That's too loud. You're enjoying it to much."
    pov "{i}Wow, she is moaning like crazy.{/i}"
    ls "<whisper> I'm so wet."
    scene town secret 2pm 018
    pov "What...?"
    ls "What?"
    pov "{i}Did she really say that?{/i}"
    scene town secret 2pm 019
    ls "Nooo... <sob>"
    pov "{i}Wow, did she really enjoy it that much?{/i}"
    pov "{i}Maybe I should follow her?{/i}"
    $ lilsiscorruption += 1
    $ dtime += 1
    jump town

label sp2pmcor3ass:
    scene town secret 2pm 016d
    $ sp2pmextend = True
    ls "<whisper> Hng..."
    pov "<whisper> You're doing good. Suppress your voice."
    "You start to bump your crotch on her ass."
    ls "<whisper> What are you...?"
    pov "<whisper> Shh..."
    ls "Hmm..."
    pov "<whisper> Shhh... not so loud."
    pov "{i}She's getting turned on and seems to enjoy it.{/i}"
    if inc == True:
        ls "<whisper> Please... hmm... brother..."
    else:
        ls "<whisper> Please... hmm... [pov]..."
    scene town secret 2pm 017d
    ls "Aaah... hah..."
    pov "<whisper> That's too loud. You're enjoying it to much."
    pov "{i}Wow, she is moaning like crazy.{/i}"
    if lsispronanal >= 4:
        ls "<whisper> Hah... deeper in my ass!"
    else:
        ls "<whisper> Hah... harder!"
    scene town secret 2pm 018d
    pov "What...?"
    ls "What?"
    pov "{i}Did she really say that?{/i}"
    scene town secret 2pm 019
    ls "Nooo... <sob>"
    pov "{i}Wow, did she really enjoy it that much?{/i}"
    pov "{i}Maybe I should follow her?{/i}"
    $ lilsiscorruption += 1
    $ dtime += 1
    jump town


label secretplace:
    scene town secret 2pm 001n
    $ davidecumface = False
    $ davidecuminside = False
    $ mccumface = False
    $ mccuminside = False
    $ secretpmcwatch = False
    $ secret2likentr = False
    $ lilsisrelationship += 1
    pov "{i}Oh it's \"Dummy\". He's running away. I wonder why?{/i}"
    pov "{i}And why is the door open? Is there maybe a stranger inside? The cat won't leave when [ls] is there.{/i}"
    scene town secret 2pm 002n
    ls "<giggle>"
    pov "{i}Oh, she is here.{/i}"
    ls "Why doesn't that count. I pressed the button. You cheated again?"
    pov "{i}Wait! There is somebody with her? But whom?{/i}"
    scene town secret 2pm 003n
    ls "Stop pulling my nipples <giggle>. That's cheating."
    davide "I'm only helping you to relax, haha."
    call screen secret2ntrchoose

screen secret2ntrchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 490 ypos 122 action (Hide ('secret2ntrchoose'), Jump('secretplacentrlike')) hovered tt.Action ("Show yourself") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 490 ypos 245 action (Hide ('secret2ntrchoose'), Jump('secretplacentrlikeh')) hovered tt.Action ("Watch them secretly") focus_mask True


    frame:
        xalign .5
        text tt.value

label secretplacentrlike:
    pov "{i}So they're having fun together. But what's this?{/i}"
    scene town secret 2pm 005n
    pov "{i}Oh he's using the drug on her. So maybe that's his trick to get girls.{/i}"
    pov "{i}Now I'm even more curious.{/i}"
    scene town secret 2pm 006ns
    if inc == True:
        ls "Oh hey brother."
    else:
        ls "Oh hey [pov]."
    davide "Huh?"
    pov "Hey you two. Having fun here I see?"
    ls "Yes I showed Davide my secret place. And now we're playing this game."
    pov "A game?"
    pov "{i}He tricked her to get her naked. Nice playing.{/i}"
    scene town secret 2pm 007ns
    davide "Yes. But she's loosing all the time, haha."
    ls "That's not fair. I pressed the button. Why is this game so hard?"
    pov "Oh I see. And you're good at playing this \"game\" Davide?"
    davide "Haha, you noticed?"
    if inc == True:
        davide "Your little sister is like a gem that needs to be polished."
    else:
        davide "[ls] is like a gem that needs to be polished."
    davide "I only use a grinder, haha."
    pov "I see, haha."
    scene town secret 2pm 008ns
    ls "Ugh! I lost again."
    davide "Well at least you tried and did your best."
    davide "But now it's time to do your last dare."
    ls "Hmpf!"
    davide "Come on. If you want to be my girlfriend you have to deliver!"
    scene town secret 2pm 009ns
    ls "<giggle> OK, my lover. I can do that."
    pov "{i}Wow. They're moving on fast.{/i}"
    if inc == True:
        ls "I hope it doesn't bother you to see me naked, brother?"
    else:
        ls "I hope it doesn't bother you to see me naked, [pov]?"
    pov "No. I think I can endure that."
    ls "Haha, you dummy."
    davide "Let me see that kitty."
    scene town secret 2pm 010ns
    ls "Slowly."
    davide "Yes, there it is."
    pov "Why that weird face, [ls]?"
    ls "It's not easy to keep balance."
    pov "{i}Damn, she's still playing around. I wonder how fast this will change when Davide fucks her.{/i}"
    pov "{i}But...{/i}"
    scene town secret 2pm 012ns
    pov "Damn!"
    davide "Hell yeah."
    ls "What's wrong?"
    davide "We're just admiring your tight kitty, girl!"
    ls "Oh... <giggle>"
    ls "Davide told me that he likes tight girls very much. Like me."
    pov "{i}Oh so she'll soon be very corrupted.{/i}"
    scene town secret 2pm 013ns
    ls "So you like my body?"
    davide "Yes but I'll like it more when I've conquered everything."
    ls "<giggle>"
    pov "You're damn lucky man."
    davide "Oh yes, hahaha. But maybe I'm not the only one."
    pov "Huh?"
    scene town secret 2pm 014ns
    davide "Stay down there cutie. I have something else for you to do too."
    pov "Not wasting any time, haha?"
    davide "She needs to learn it some time and now is that time?"
    ls "I'm sure I know what you want me to do <giggle>"
    pov "{i}I wonder how much he told her about perverted stuff since they know each other.{/i}"
    pov "{i}And if they're also meet without my knowing.{/i}"
    scene town secret 2pm 015ns
    ls "I knew it, haha. You want me to play with your worm."
    pov "Worm. Hahahaha..."
    davide "Damn girl! SNAKE! Call it a snake, not a worm."
    ls "OK. Your snake is so big."
    davide "Much better. Go on now and serve my snake."
    ls "<giggle>"
    scene town secret 2pm 016ns
    ls "It's so hard and warm."
    pov "{i}Holy shit. Is she really going to...{/i}"
    davide "You told me that you already know what to do. So show me what the internet taught you."
    pov "{i}Wait! [ls] prepared herself already?{/i}"
    ls "I'll do my best <giggle>"
    scene town secret 2pm 017ns
    if inc == True:
        ls "But isn't it weird with my brother watching?"
    else:
        ls "But isn't it weird with [pov] watching?"
    davide "Haha, I think he saw something like that before."
    if inc == True:
        ls "But it's my brother!"
    else:
        ls "But it's [pov]!"
    davide "Oh yes, how rude of me. Do you wan to join us [pov]?"
    pov "Huh?"
    call screen secret2ntrjoin

screen secret2ntrjoin():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1090 ypos 122 action (Hide ('secret2ntrjoin'), Jump('secretplacentrlikejoin')) hovered tt.Action ("Join them") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1390 ypos 122 action (Hide ('secret2ntrjoin'), Jump('secretplacentrdislikewatch')) hovered tt.Action ("Just watch") focus_mask True


    frame:
        xalign .5
        text tt.value

label secretplacentrlikejoin:
    pov "Oh hell yeah. Let's see what [ls] can do."
    ls "What? But..."
    scene town secret 2pm 018ns
    davide "What's wrong? You want to please, so you can please him too."
    if inc == True:
        ls "But he's my brother. And I thought you're my boyfriend?"
    else:
        ls "But I've known him for so long. And I thought you're my boyfriend?"
    davide "Yes but I like to share and that's something you need to learn too."
    davide "What's wrong about it, when you can share something good and show it to others?"
    pov "{i}Haha, damn that talker.{/i}"
    ls "Hm..."
    if inc == True:
        davide "And there's nothing bad about it that he's your brother."
    else:
        davide "And there's nothing bad about you knowing each other all your life."
    pov "{i}He's so damn right.{/i}"
    scene town secret 2pm 019ns
    ls "I think you're right. You can join [pov]."
    pov "Hell yes!"
    davide "I'm sure you'll enjoy it, haha."
    "You unpack your dick."
    scene town secret 2pm 020ns
    ls "Oh..."
    if inc == True:
        davide "It's the first time you've seen your brothers dick?"
    else:
        davide "It's the first time you've seen his dick?"
    ls "Y... yes."
    pov "Don't be shy, [ls]."
    davide "Yes go on, show us what you can do."
    scene town secret 2pm 021ns
    ls "OK."
    if inc == True:
        ls "You also seems to be very excited, big brother."
    else:
        ls "You also seems to be very excited, [pov]."
    pov "Oh yes I am. Feeling your soft hand on my dick."
    davide "Yes that's nice, but I'll be here for more action."
    ls "Oh I can do more."
    scene town secret 2pm 022ns
    ls "<kiss>"
    davide "Oh yes, a good start."
    "[ls] strokes your dicks too."
    if inc == True:
        pov "{i}Seeing my little sister giving her boyfriend and me a blow-job.{/i}"
    else:
        pov "{i}Seeing [ls] giving her boyfriend and me a blow-job.{/i}"
    pov "{i}This is like heaven.{/i}"
    image bjal_secret_NTR = Movie(channel="bjal_secret_NTR", play="images/anim/NTR/bjal_secret_NTR.webm")
    scene bjal_secret_NTR with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ls "<lick>"
    davide "Hah..."
    pov "Damn!"
    pov "I can't wait to get that licking too."
    scene town secret 2pm 024ns
    if inc == True:
        ls "Sorry, brother. This is something I'll do only for my boyfriend."
    else:
        ls "Sorry, [pov]. This is something I'll do only for my boyfriend."
    pov "Oh..."
    davide "Normally I'm for full sharing, but this is something I agree with her."
    davide "But I'm sure you can cum."
    pov "Ha, sure but... damn."
    scene town secret 2pm 025ns
    ls "So you like my doing, lover?"
    davide "Yes not bad girl. But we can still improve that."
    pov "{i}Damn, she's trying everything to please him.{/i}"
    ls "Your penis likes it, it got even harder."
    davide "Haha, damn girl. You learn fast."
    scene town secret 2pm 026ns
    if inc == True:
        ls "And you too big brother, getting harder and harder in my hand."
    else:
        ls "And you too [pov], getting harder and harder in my hand."
    pov "{i}She isn't shy anymore. I wonder if that's an effect of the drug. And I'm very sure she doesn't know anything about it.{/i}"
    pov "{i}But a very nice surprise, so I'll just enjoy it.{/i}"
    pov "Yes you're doing very well [ls]."
    ls "<giggle> Thank you."
    davide "Too good, hng."
    scene town secret 2pm 027ns
    davide "I'm about to cum soon, girl! Remember what we talked."
    pov "Huh?"
    ls "I remember, my lover. <giggle>"
    ls "Do you want to put your sperm on my face or in my mouth?"
    pov "{i}Fucking shit, that's so hot I'll cum anytime too. I hope I can choose too.{/i}"
    call screen secret2ntrlikedcum

screen secret2ntrlikedcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 650 ypos 122 action (Hide ('secret2ntrlikedcum'), Jump('secretplacentrlikedcumface')) hovered tt.Action ("Davide cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 650 ypos 367 action (Hide ('secret2ntrlikedcum'), Jump('secretplacentrlikedcumin')) hovered tt.Action ("Davide cum in her mouth") focus_mask True


    frame:
        xalign .5
        text tt.value

label secretplacentrlikedcumface:
    $ davidecumface = True
    davide "I'll cum on your face, prepare yourself!"
    ls "OK, shoot it on me <giggle>."
    scene town secret 2pm 028ns
    davide "HNNG!"
    ls "Aaah..."
    pov "{i}Damn, this is so hot. [ls] is posing like a porn-star.{/i}"
    scene town secret 2pm 029ns
    ls "Hmm..."
    davide "Look at that, I sprayed her good!"
    pov "Haha, yes."
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
    pov "{i}Damn, this is so hot. [ls] is posing like a porn-star.{/i}"
    scene town secret 2pm 029nsa
    ls "Hmm..."
    davide "Look at that, I came so much!"
    pov "Haha, yes."
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
    pov "{i}Oh shit, I can't believe it!{/i}"
    if inc == True:
        pov "{i}My little sister is asking me where I want to put my sperm on her!{/i}"
    else:
        pov "{i}[ls] is asking me where I want to put my sperm on her!{/i}"
    call screen secret2ntrlikemcum

screen secret2ntrlikemcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 750 ypos 122 action (Hide ('secret2ntrlikemcum'), Jump('secretplacentrlikemcumface')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 750 ypos 367 action (Hide ('secret2ntrlikemcum'), Jump('secretplacentrlikemcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True


    frame:
        xalign .5
        text tt.value

label secretplacentrlikemcumface:
    $ mccumface = True
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
    pov "I still can't believe it, that was very hot [ls]."
    ls "<giggle>"
    davide "I think it's time to go back."
    jump secret2ntrlikeend

label secret2ntrlikeend:
    scene town secret 2pm 035ns
    davide "Come here babe, you earned yourself a kiss."
    ls "Oh Davide... <kiss>"
    pov "{i}Oh, she really likes him.{/i}"
    ls "Your penis is poking on my..."
    davide "Yes, and soon it's time to widen your kitty."
    ls "Oh, hnn..."
    scene black
    "You go back home together."
    $ davidegood += 1
    $ dtime += 1
    $ secretplace2pmntrfirst = True
    jump frontdoor

label secretplacentrdislikewatch:
    $ secretpmcwatch = True
    pov "No, but I'd love to watch and see what [ls] can do."
    scene town secret 2pm 018ng
    davide "What? You really want to just watch?"
    ls "Eh?"
    pov "Yes, she's your girlfriend now. But I want to see what she can do."
    ls "You want to watch like a pervert?"
    pov "Hmm... yes."
    scene town secret 2pm 018ns
    davide "That's a little bit surprising but if he want to, we should let him."
    davide "Maybe he can learn something, haha."
    if inc == True:
        ls "But he's my brother. And I thought you're my boyfriend?"
    else:
        ls "But I known him for so long. And I thought you're my boyfriend?"
    davide "Yes but I want to show him what my babe can do."
    davide "What's wrong about it, when you have something good show it to others?"
    pov "{i}Haha, damn that talker.{/i}"
    ls "Hm..."
    if inc == True:
        davide "And there's nothing bad about him being your brother."
    else:
        davide "And there's nothing bad about you knowing each other all your life."
    pov "{i}He's so damn right.{/i}"
    scene town secret 2pm 019ns
    ls "I think you're right. You can watch us [pov]."
    pov "Hell yes!"
    davide "I'm sure you'll enjoy it, haha."
    scene town secret 2pm 021nw
    ls "Hm..."
    pov "Don't be shy, [ls]."
    davide "Yes go on, show us what you can do."
    if inc == True:
        ls "You really like watching me doing this, big brother?"
    else:
        ls "You really like watching me doing this, [pov]?"
    pov "Yes, you're all naked and doing perverted things, just hot."
    davide "Hahaha..."
    scene town secret 2pm 022nw
    ls "<kiss>"
    davide "Oh yes, a good start."
    if inc == True:
        pov "{i}Seeing my little sister giving her boyfriend a blow-job.{/i}"
    else:
        pov "{i}Seeing [ls] giving her boyfriend a blow-job.{/i}"
    pov "{i}This is like heaven.{/i}"
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
    pov "{i}Damn, this gets even better.{/i}"
    scene town secret 2pm 026nw
    ls "His penis is getting harder and harder in my hand."
    pov "{i}She isn't shy anymore. I wonder if that's an effect of the drug. And I'm very sure she doesn't know anything about it.{/i}"
    pov "{i}But a very nice surprise, so I'll just enjoy it.{/i}"
    pov "Yes I think you're doing very good [ls]."
    ls "<giggle> Thank you."
    davide "Too good, hng."
    scene town secret 2pm 027nw
    davide "I'm about to cum soon, girl! Remember what we talked."
    pov "Huh?"
    ls "I remember, my lover. <giggle>"
    ls "Do you want to put your sperm on my face or in my mouth?"
    pov "{i}Fucking shit, that's so hot.{/i}"
    call screen secret2ntrlikedcum

label secretplacentrlikeh:
    pov "{i}They didn't notice me, so I will watch them secretly.{/i}"
    call screen secret2ntrdislikechoose

screen secret2ntrdislikechoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 490 ypos 122 action (Hide ('secret2ntrdislikechoose'), Jump('secretplacentrlikehw')) hovered tt.Action ("Like NTR") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 490 ypos 245 action (Hide ('secret2ntrdislikechoose'), Jump('secretplacentrdislike')) hovered tt.Action ("Dislike NTR") focus_mask True


    frame:
        xalign .5
        text tt.value

label secretplacentrlikehw:
    $ secret2likentr = True
    jump secretplacentrdislike

label secretplacentrdislike:
    pov "{i}So they're having fun together. But what's this?{/i}"
    scene town secret 2pm 005n
    pov "{i}Oh he's using the drug on her. So maybe that's his trick to get girls.{/i}"
    pov "{i}Now I'm even more curious.{/i}"
    if secret2likentr == False:
        if inc == True:
            pov "{i}That asshole drugging my little sister.{/i}"
        else:
            pov "{i}That asshole drugging her.{/i}"
    scene town secret 2pm 008ns
    ls "Ugh! I lost again."
    davide "Well at least you tried and gave your best."
    davide "But now it's time to do your last dare."
    ls "Hmpf!"
    davide "Come on. If you want to be my girlfriend you have to deliver!"
    scene town secret 2pm 010ns
    ls "<giggle> OK, my lover. I can do that."
    if secret2likentr == True:
        pov "{i}Wow. They're moving on fast.{/i}"
    else:
        pov "{i}What did he talk her into?{/i}"
    davide "Yes let me see your kitty, my little slut."
    ls "<giggle> Oh Davide."
    if secret2likentr == False:
        pov "{i}That asshole. Made her into this and then calling her a slut.{/i}"
    else:
        pov "{i}Wow, she's already naked.{/i}"
    scene town secret 2pm 012ns
    pov "{i}Damn, her naked pussy.{/i}"
    scene town secret 2pm 013ns
    ls "So you like my body?"
    davide "Yes but I'll like it more when I've conquered everything."
    ls "<giggle>"
    if secret2likentr == True:
        pov "{i}You're damn lucky man.{/i}"
    else:
        pov "{i}I can't believe this. Why is she falling so easy to him? It can't be only the drug.{/i}"
    scene town secret 2pm 014ns
    davide "Stay down there slut! I have something else for you to do."
    ls "I'm sure I know what you want me to do <giggle>"
    pov "{i}I wonder how much he told her about perverted stuff since they known each other.{/i}"
    pov "{i}And if they're meeting without me knowing.{/i}"
    scene town secret 2pm 015ns
    ls "I knew it, haha. You want me to play with your worm."
    pov "Worm. Hahahaha..."
    davide "Damn slut! SNAKE! Call it a snake, not a worm."
    ls "OK. Your snake is so big."
    davide "Much better. Go on now and serve my snake."
    ls "<giggle>"
    if secret2likentr == False:
        pov "{i}No, I don't want to see this, but I must be sure that he won't hurt her.{/i}"
    else:
        pov "{i}And so they start.{/i}"
    scene town secret 2pm 016ns
    ls "It's so hard and warm."
    pov "{i}Holy shit. Is she really going to...{/i}"
    davide "You told me that you already know what to do. So show me what the internet taught you."
    pov "{i}Wait! [ls] prepared herself already?{/i}"
    ls "I'll do my best <giggle>"
    if secret2likentr == False:
        pov "{i}What are you doing with her? She was so pure and innocent!{/i}"
    scene town secret 2pm 022n
    ls "<kiss>"
    davide "Oh yes, a good start."
    if inc == True:
        pov "{i}Seeing my little sister giving her boyfriend and me a blow-job.{/i}"
    else:
        pov "{i}Seeing [ls] giving her boyfriend and me a blow-job.{/i}"
    if secret2likentr == False:
        pov "{i}This is like hell.{/i}"
    else:
        pov "{i}This is like heaven.{/i}"
    scene town secret 2pm 023n
    ls "<lick>"
    davide "Hah..."
    if secret2likentr == False:
        pov "{i}Stop corrupting her.{/i}"
    else:
        pov "{i}This is getting better and better.{/i}"
    ls "Am I doing good?"
    davide "Yes but you can go even further."
    scene town secret 2pm 024n
    davide "Good, suck on it."
    ls "It's so big. <kiss>"
    davide "That's a very nice view. Seeing my slutty girl down on me."
    if secret2likentr == False:
        pov "{i}...{/i}"
    else:
        pov "{i}I can barely believe that he's getting her so fast into doing this.{/i}"
    davide "Go on, do more."
    scene town secret 2pm 025n
    davide "I'll help you!"
    ls "HNNG!"
    ls "S... Stop... I can't..."
    davide "Come on get it deeper in!"
    if secret2likentr == False:
        pov "{i}You damn motherfucker, stop hurting her!{/i}"
    else:
        pov "{i}Oh he wants to get her deep throating, but he's really to big for her little mouth.{/i}"
    scene town secret 2pm 026n
    davide "Take it deeper little slut!"
    ls "Ugh! Ugh! <choke>"
    if secret2likentr == False:
        pov "{i}She can't breathe! I'll kill you for that, I'll kill you!{/i}"
    else:
        pov "{i}That's a little bit to much for her on her first time. I hope he won't hurt her.{/i}"
    davide "Try harder!"
    ls "HNNG..."
    "He released her."
    scene town secret 2pm 027n
    ls "I'm so... sorry. I... tried, but I can't."
    davide "OK. It wasn't that bad either. But we need to train this more."
    davide "I want to ram my dick down your throat!"
    ls "OK. So you're not mad at me?"
    davide "I can forgive you, but you have to make me cum good."
    if secret2likentr == False:
        pov "{i}She'll never be pure again...{/i}"
    else:
        pov "{i}Oh yes. I like to see her getting slutty.{/i}"
    scene town secret 2pm 028n
    ls "I can do that. You'll love to cum from my treatment."
    davide "We'll see. Now go on slut!"
    if secret2likentr == False:
        pov "{i}Stop it! Please just stop...{/i}"
    scene town secret 2pm 029n
    ls "<lick>"
    davide "Much better. Seeing you slut with tears in your eyes after you tried hard is very nice."
    ls "<faster licking>"
    davide "I'll teach you more to become a good slut!"
    ls "Yes, teach me lover."
    if secret2likentr == False:
        pov "{i}Nooo! I must find a way to stop this fast.{/i}"
    else:
        pov "{i}Damn, she'll fall quickly.{/i}"
    scene town secret 2pm 030n
    davide "Damn, you're right. I'm about to cum!"
    ls "Where do you want to place your sperm?"
    if secret2likentr == False:
        pov "{i}At least he can't hurt her anymore...{/i}"
    call screen secret2ntrdislikedcum

screen secret2ntrdislikedcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 122 action (Hide ('secret2ntrdislikedcum'), Jump('secretplacentrdislikedcumface')) hovered tt.Action ("Davide cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 367 action (Hide ('secret2ntrdislikedcum'), Jump('secretplacentrdislikedcumin')) hovered tt.Action ("Davide cum in her mouth") focus_mask True


    frame:
        xalign .5
        text tt.value


label secretplacentrdislikedcumface:
    $ davidecumface = True
    davide "I'll cum on your face, prepare yourself!"
    ls "OK, shoot it on me <giggle>."
    scene town secret 2pm 031n
    davide "HNNG!"
    ls "Aaah..."
    if secret2likentr == True:
        pov "{i}Damn, this is so hot. [ls] is posing like a porn-star.{/i}"
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
    if secret2likentr == True:
        pov "{i}I need to see this then too. That would be great.{/i}"
    else:
        pov "{i}I can't let it happen. I must find a way out for her and a punishment for him.{/i}"
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
    if secret2likentr == True:
        pov "{i}Damn, this is so hot. [ls] is posing like a porn-star.{/i}"
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
    if secret2likentr == True:
        pov "{i}I need to see this then too. That would be great.{/i}"
    else:
        pov "{i}I can't let it happen. I must find a way out for her and a punishment for him.{/i}"
    davide "Get dressed so we can go, slut!"
    ls "Y...yes Davide."
    jump secret2ntrdislikenend

label secret2ntrdislikenend:
    scene black
    "You leave them before they can notice you."
    "You see them leaving shortly after you."
    if secret2likentr == True:
        $ davidegood += 1
        pov "{i}Damn that was hot.{/i}"
    else:
        $ davidebad += 1
        pov "{i}I need to plan my revenge.{/i}"
    $ dtime += 1
    $ secretplace2pmntrfirst = True
    jump frontdoor