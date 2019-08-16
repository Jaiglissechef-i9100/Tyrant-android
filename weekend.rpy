

label weekendstart:
    $ roomlroom = False
    $ roomdroom = False
    $ roomkitchen = False
    $ roomalexis = False
    $ roomcassandra = False
    $ roommc = False
    $ roomshowerup = False
    $ roomshowerdown = False
    $ roomfrontdoor = False
    $ roombasement = False
    $ roomparents = False
    $ roomtown = False
    $ roomtanning = False
    $ roomsubway = False
    $ roomhideout = False
    $ roomfitness = False
    $ roomclub = False
    $ roomweekend = True
    hide screen locations
    scene black
    "The weekend has begun."
    $ dtime = 9
    "You wake up and go downstairs."
    jump breakfast


label weekendskip:
    $ day = 1
    $ dtime = 7
    $ weekend = False
    jump mcroom



label breakfast:
    scene weekend 9am 001
    mom "Good morning [pov]. So you're awake now?"
    pov "Good morning..."
    ls "Oh, still sleepy? <giggle>"
    mom "Sit and eat with us breakfast."
    scene weekend 9am 002
    pov "It's so silent today."
    mom "It's weekend. So there is no need to hurry and we all can be relaxed."
    scene weekend 9am 003
    mom "You'll go to your friend again over the weekend?"
    pov "Her friend?"
    mom "Yes, from school. She spent every weekend with her and her parents, so I have some free time for myself."
    scene weekend 9am 004
    ls "Yes, this will be so much fun. And you earned yourself some free time, mom, haha."
    mom "Haha, yes."
    pov "{i}I wonder what she'll do with all that free time?{/i}"
    scene weekend 9am 005
    mom "And you'll hang out with [irina] again? I hope you won't do anything stupid."
    scene weekend 9am 006
    bs "Mom! We never did anything stupid. We just have fun."
    pov "{i}Having fun with [irina]. I wonder what they want to do?{/i}"
    scene weekend 9am 007
    mom "And what are you want to do on the weekend?"
    pov "I don't know... yet..."
    mom "You have this all for you, the other men are droven away to do some work."
    pov "Droven away to do some work?"
    mom "Yes, Bruce is with them every weekend when they're in another town."
    pov "Oh."
    scene weekend 9am 008
    mom "Or did you find already someone special just for you?"
    pov "?"
    mom "Maybe a girl you want to spent time on this weekend?"
    ls "<giggle>"
    scene black
    "Developers Note:" "Here takes a event for the start of the weekend place."
    "Developers Note:" "Unfortunately it's to buggy to play, so it's disabled in this version."
    "Developers Note:" "You can now choose between several weekend activities."
    "Developers Note:" "Some of them need certain requirements to play them."
    "Developers Note:" "You can do three events, then the weekend finish and you continue on monday."
    if NTR == True and ndate21ntrsex == True and nicoleweekendntrevent == False:
        $ messagepush = True
        $ messagenicolentr = 1
        $ nicolenotification += 1
    if NTR == True and secretplace2pmntrfirst == True:
        $ messagepush = True
        $ messagedavidentr = 1
        $ davidenotification += 1
    jump weekendacchoose

label weekendacchoose:
    $ weekend = True
    scene weekendblack
    show screen phone
    call screen weekendblackchoose

screen weekendblackchoose():
    default tt = Tooltip (" ")

    fixed:
        if money >= 200:
            imagebutton auto "gui/icons/wnicole_%s.png" xpos 300 ypos 190 action (Hide('weekendblackchoose'), Jump('ndate21goyes')) hovered tt.Action ("Go with [mother] on your first date [lv1] or [cr1]") focus_mask True
        if money < 200:
            imagebutton auto "gui/icons/wnicolex_%s.png" xpos 300 ypos 190 action NullAction() hovered tt.Action ("$200 are needed for your first date") focus_mask True
        if gangmember == False and mombasementfirst == True or gangmember == True and mombasementfirst == False or gangmember == False and mombasementfirst == False:
            imagebutton auto "gui/icons/wnicolex_%s.png" xpos 300 ypos 456 action NullAction() hovered tt.Action ("You need to be a gangmember and did her basement event as a gangmember | [cr1] Date") focus_mask True
        if gangmember == True and mombasementfirst == True:
            imagebutton auto "gui/icons/wnicole_%s.png" xpos 300 ypos 456 action (Hide('weekendblackchoose'), Jump('nicoleweekendcor')) hovered tt.Action ("Have a second date with [mother] [cr1]") focus_mask True
        if momlove < 80 and ndate21 == False or momlove < 80 and ndate21 == True or momlove >= 80 and ndate21 == False:
            imagebutton auto "gui/icons/wnicolex_%s.png" xpos 300 ypos 729 action NullAction() hovered tt.Action ("80 or more love points are needed and you need to been with her on the first date | [lv1] Date") focus_mask True
        if momlove >= 80 and ndate21 == True:
            imagebutton auto "gui/icons/wnicole_%s.png" xpos 300 ypos 729 action (Hide('weekendblackchoose'), Jump('nicoleweekendlove')) hovered tt.Action ("Have a second date with [mother] [lv1]") focus_mask True

        if money < 20:
            imagebutton auto "gui/icons/walexisx_%s.png" xpos 680 ypos 190 action NullAction() hovered tt.Action ("$20 are needed for your first date") focus_mask True
        if money >= 20:
            imagebutton auto "gui/icons/walexis_%s.png" xpos 680 ypos 190 action (Hide('weekendblackchoose'), Jump('adate1goyes')) hovered tt.Action ("Go with [ls] on your first date") focus_mask True
        if adate == False and lilsislove < 50 or adate == False and lilsislove >= 50 or adate == True and lilsislove < 50:
            imagebutton auto "gui/icons/walexisx_%s.png" xpos 680 ypos 456 action NullAction() hovered tt.Action ("50 or more love points are needed and you need to been with her on the first date | [lv1] Date") focus_mask True
        if adate == True and lilsislove >= 50:
            imagebutton auto "gui/icons/walexis_%s.png" xpos 680 ypos 456 action (Hide('weekendblackchoose'), Jump('alexisweekendlove')) hovered tt.Action ("Go with [ls] on your second date [lv1] Date") focus_mask True

        imagebutton auto "gui/icons/wcassandra_%s.png" xpos 1060 ypos 190 action (Hide('weekendblackchoose'), Jump('cdate5')) hovered tt.Action ("Go with [bs] on your first date [lv1] or [cr1]") focus_mask True
        if basecasfirst == False and bigsislove > bigsiscorruption and bigsislove >= 50 or basecasfirst == True and bigsislove <= bigsiscorruption and bigsislove >= 50 or basecasfirst == True and bigsislove > bigsiscorruption and bigsislove < 50:
            imagebutton auto "gui/icons/wcassandrax_%s.png" xpos 1060 ypos 456 action NullAction() hovered tt.Action ("50 or more love points are needed and you must invite her to the basement before") focus_mask True
        if basecasfirst == True and bigsislove > bigsiscorruption and bigsislove >= 50:
            imagebutton auto "gui/icons/wcassandra_%s.png" xpos 1060 ypos 456 action (Hide('weekendblackchoose'), Jump('casweekendfirst')) hovered tt.Action ("Meet with [bs] [lv1]") focus_mask True
        if activatesecretplacentr == True:
            imagebutton auto "gui/icons/walexis_%s.png" xpos 1460 ypos 190 action (Hide('weekendblackchoose'), Jump('secret4pmntr')) hovered tt.Action ("Spy on Davide and [ls]") focus_mask True
        if activatesubwayntr == True:
            imagebutton auto "gui/icons/wnicole_%s.png" xpos 1460 ypos 456 action (Hide('weekendblackchoose'), Jump('nicoleweekendntr')) hovered tt.Action ("Look after [mother] at the subway") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 932 ypos 948 action (Hide('weekendblackchoose'), Jump('weekendskip')) hovered tt.Action ("Skip weekend | Jump to monday") focus_mask True


        frame:
            xalign .5
            text tt.value
















































label ndate21choose:
    hide screen locations
    if dtime == 7 or dtime == 8:
        scene main mc room morning
    else:
        scene main mc room day
    "It'll cost you 200$ to go on a date with [mother]."
    call screen ndate21choose1

screen ndate21choose1():
    default tt = Tooltip (" ")

    fixed:

        if money >= 200:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 605 ypos 193 action (Hide('ndate21choose1'), Jump('ndate21goyes')) hovered tt.Action ("Go on a date with [mother]") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1286 ypos 193 action (Hide('ndate21choose1'), Jump('ndate21gono')) hovered tt.Action ("Don't go") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate21goyes:
    $ money -= 200
    jump ndate21

label ndate21gono:
    jump mcroom

label adate1choose:
    hide screen locations
    if dtime == 7 or dtime == 8:
        scene main mc room morning
    else:
        scene main mc room day
    "It'll cost you 20$ to go on a date with [ls]."
    call screen adate1choose1

screen adate1choose1():
    default tt = Tooltip (" ")

    fixed:

        if money >= 20:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 605 ypos 193 action (Hide('adate1choose1'), Jump('adate1goyes')) hovered tt.Action ("Go on a date with [ls]") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1286 ypos 193 action (Hide('adate1choose1'), Jump('adate1gono')) hovered tt.Action ("Don't go") focus_mask True
        frame:
            xalign .5
            text tt.value

label adate1goyes:
    $ money -= 20
    jump adate1

label adate1gono:
    jump mcroom


label ndate21:
    hide screen locations
    scene black
    $ ndate21ass = False
    $ ndate21pussy = False
    $ ndate21inside = False
    $ ndate21outside = False
    $ momrelationship += 1
    $ ndate21 = True
    if inc == True:
        "You go on a date with your mother."
    else:
        "You go with on a date with [mother]."
    "You arrive at the restaurant you choose."
    "Its a special themed place."
    scene date 21pm 001
    mom "Oh look. They're dressed like in ancient Egypt."
    pov "Yeah, they take that all serious."
    "Waitress" "Welcome to our temple, friends of Egypt."
    mom "Ohh..."
    scene date 21pm 002
    "Waitress" "Please follow me. Your table is set."
    mom "And these fire bowls. Like we're in a forgotten time."
    pov "Yes, it's really an interesting place."
    pov "Come with me."
    scene date 21pm 003
    mom "And this wide places. This is like an exclusive club."
    pov "Yes, they only open for reservations."
    mom "Wow I can't stop wondering."
    pov "All for my beautiful date."
    mom "You're so sweet, [pov]!"
    jump ndate21ass

label ndate21ass:
    scene date 21pm 003
    call screen ndate21ass2

screen ndate21ass2():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 890 ypos 452 action (Hide('ndate21ass2'), Jump('ndate21ass3')) hovered tt.Action ("Look at her ass") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 890 ypos 214 action (Hide('ndate21ass2'), Jump('ndate221')) hovered tt.Action ("Don't") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate21ass3:
    scene date 21pm 003a
    pov "{i}Damn, that outfit is short.{/i}"
    jump ndate221

label ndate221:
    scene date 21pm 004
    mom "Look! This sarcophagus looks so realistic."
    mom "So you can save your loved one forever, even when he's/she's dead, haha."
    pov "I know a beauty who I will need to have a sarcophagus."
    mom "Ohh such a nice compliment."
    scene date 21pm 005
    "Waitress" "Here's your table. With some wine. I'll bring the dinner soon."
    mom "So lovely!"
    pov "Ok. Thank you."
    mom "You ordered the dinner already?"
    pov "Yes, because I know really well what you love to eat."
    mom "Oh, yes that's right. I'm so excited."
    scene date 21pm 006
    mom "I still can't believe it that you brought me to such an exquisite place with you."
    if inc == True:
        pov "You're the most beautiful woman, nobody else I'd want to do this with, mom."
    else:
        pov "You're the most beautiful woman, nobody else I'd want to do this with, [mother]."
    mom "<giggle> You're such a flatterer, I like that."
    pov "And your dress was also a very good choice."
    mom "Yes I'm happy that I choose it for this location."
    scene date 21pm 007
    mom "I'm still wondering why you choose such a special, exclusive location for our date?"
    mom "But don't worry, I love it here, so it was a good choice."
    pov "You remember our life before this undercover thing? We used to enjoy such things more."
    pov "And I thought you should enjoy it from time to time again. You deserve it!"
    scene date 21pm 008
    mom "You're right. Bruce can't take me to such a nice place. That would be to suspicious."
    pov "Yes and it's my duty to care about you."
    mom "<giggle> Let's drink to this."
    pov "To my beautiful date!"
    mom "Mine too!"
    scene date 21pm 009
    mom "Hm... <drink>"
    pov "Does it taste well?"
    mom "Hm... hm..."
    jump ndate221l

label ndate221l:
    scene date 21pm 009
    call screen ndate221l1

screen ndate221l1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 550 ypos 870 action (Hide('ndate221l1'), Jump('ndate221closer')) hovered tt.Action ("Look closer") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1273 ypos 427 action (Hide('ndate221l1'), Jump('ndate321')) hovered tt.Action ("Don't") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate221closer:
    scene date 21pm 009a
    pov "Damn, that dress!"
    if momcorruption >= momlove and momcorruption >= 20:
        scene date 21pm 010a
        mom "Found what you're looking for?"
        pov "Haha, I'm just admiring your dress."
        mom "But don't stare all the time please."
    else:
        scene date 21pm 010b
        mom "Please stop staring at me like that."
        pov "Oh, I just wanted to inspect that dress closer."
        mom "Ok. But it makes me uncomfortable at this place."
        pov "{i}At this place...?{/i}"
        pov "Ok sorry."
    jump ndate321

label ndate321:
    scene date 21pm 011
    mom "Oh look! There's another couple here too."
    pov "I see them."
    mom "But we're still all alone. Such a nice idea."
    scene date 21pm 012
    pov "{i}That creepy guy is staring at us!{/i}"
    pov "{i}Damn, what a freak!{/i}"
    scene date 21pm 013
    mom "What is it?"
    pov "I was just wondering about that creepy guy."
    mom "Oh yes, he's looking creepy and that weird hair-cut. Gross!"
    if inc == True:
        pov "But no wonder he's staring at us. You look so damn beautiful, mom!"
    else:
        pov "But no wonder he's staring at us. You look so damn beautiful, [mother]!"
    scene date 21pm 014
    mom "You won't stop giving me compliments, will you?"
    pov "No, because it's true!"
    mom "Thank you! It's so good to be with someone who can stand aside our family situation now."
    pov "As a reminder that the better times will come back?"
    mom "Oh... the better times..."
    "Waitress" "Excuse me..."
    scene date 21pm 015
    "Waitress" "Here's your dinner."
    mom "Oh... and it smells so good."
    pov "Some good steaks for us."
    mom "Hmm..."
    scene date 21pm 016
    "Waitress" "Here for you, Sir."
    pov "Thank you."
    mom "Hnn..."
    if inc == True:
        pov "Why is mom looking so weird?"
    else:
        pov "Why is [mother] looking so weird?"
    if momcorruption >= momlove and momcorruption >= 30:
        scene date 21pm 017a
        mom "Hahaha, here I am! When you're with me you can stare at my breasts. No need to stare at the waitress too."
        pov "What...?"
        mom "Hahaha, I'm just joking around with you!"
        pov "Oh..."
        jump ndate321joke
    else:
        scene date 21pm 017b
        mom "Oh, did you find a woman for your interests?"
        pov "Huh?"
        mom "Maybe she could be a possible girlfriend for you?"
        pov "A girlfriend for me?"
        mom "Yes, it's time that you got a girlfriend."
        jump ndate321gf

label ndate321gf:
    scene date 21pm 017b
    call screen ndate321gf1

screen ndate321gf1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 605 ypos 193 action (Hide('ndate321gf1'), Jump('ndate321gflove')) hovered tt.Action ("Loving comment [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1286 ypos 193 action (Hide('ndate321gf1'), Jump('ndate321gfno')) hovered tt.Action ("Approve with her") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate321gflove:
    scene date 21pm 017b
    pov "But I'm here with the woman I'm interested in!"
    scene date 21pm 018b
    mom "You... you mean with me...?"
    if inc == True:
        pov "Yes! I love you mom! I would prefer you as my girlfriend over some other ugly women!"
        mom "Stop saying such things! I'm your mother, I can't be your girlfriend."
    else:
        pov "Yes! I love you [mother]! I would prefer you as my girlfriend over some other ugly women!"
        mom "Stop saying such things! I can't be your girlfriend. You mother would never forgive me."
    pov "That's your opinion now, but over the time you'll follow your heart."
    mom "Please stop..."
    $ momlove += 1
    jump ndate421

label ndate321gfno:
    scene date 21pm 017b
    pov "Oh yes, maybe you're right. But I'm not sure now."
    mom "Don't worry. I'm sure you'll find the perfect woman for yourself."
    pov "Thank you..."
    jump ndate421

label ndate321joke:
    scene date 21pm 017a
    call screen ndate321joke1

screen ndate321joke1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1286 ypos 193 action (Hide('ndate321joke1'), Jump('ndate321jokecor')) hovered tt.Action ("Naughty comment [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" xpos 605 ypos 193 action (Hide('ndate321joke1'), Jump('ndate321jokeno')) hovered tt.Action ("No comment") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate321jokecor:
    scene date 21pm 017a
    pov "Then you'll reward me later with them?"
    scene date 21pm 019a
    mom "I... I didn't mean it that way..."
    pov "But I think it could be a nice idea to thank me for this great date!"
    mom "Stop kidding! You know exactly how I meant it."
    if inc == True:
        pov "Haha, relax, mom."
    else:
        pov "Haha, relax, [mother]."
    $ momcorruption += 1
    jump ndate421

label ndate321jokeno:
    scene date 21pm 017a
    pov "..."
    scene date 21pm 018a
    mom "Oh, come on. You're surprised, weren't you?"
    pov "Yes..."
    mom "So it's better to stay with your date and don't stare at other woman then?"
    pov "Haha, yes you're right."
    jump ndate421

label ndate421:
    scene date 21pm 020
    mom "Oh noo...!"
    pov "What...?"
    mom "This can't happen now."
    scene date 21pm 021
    pov "What's wrong? It's something about this guy?"
    pov "It seems he isn't welcome in this restaurant."
    mom "<whisper> Hey [pov]!"
    scene date 21pm 022
    pov "Huh?"
    mom "<whisper> Sshh... Come to me in silence. Fast!"
    pov "Ok...?"
    pov "{i}What's gotten into her? Why is she so scared about this man?{/i}"
    scene date 21pm 024
    pov "Calm down!"
    pov "{i}Oh shit. She looks really scared.{/i}"
    mom "<whisper> We need to hide, fast! If this man finds me..."
    pov "<whisper> What's with him?"
    mom "<whisper> Sshh... not now. Let's hide first!"
    pov "<whisper> Ok."
    scene date 21pm 023
    pov "{i}Maybe she's right. He must be really dangerous. The waiter is running away!{/i}"
    pov "{i}But who is he that he scares her so much?{/i}"
    mom "<whisper> Shhh... [pov]!"
    pov "{i}Hm.. where is she?{/i}"
    scene date 21pm 025
    pov "{i}How did she get there so fast? I didn't even hear her moving.{/i}"
    mom "<whisper> Please faster! It's urgent that we hide fast."
    pov "<whisper> Ok, ok."
    "You close up to her."
    scene date restroom door men
    mom "<whisper> But where to hide now?"
    if NTR == True and momrelationship <= 29:
        mom "<whisper> Should we seperate?"
        jump ndate421wc
    else:
        jump ndate421men

label ndate421wc:
    scene date restroom door men
    call screen ndate421wc1

screen ndate421wc1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1286 ypos 193 action (Hide('ndate421wc1'), Jump('ndate421men')) hovered tt.Action ("Stay together [lv1]/[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 605 ypos 193 action (Hide('ndate421wc1'), Jump('ndate421women')) hovered tt.Action ("Seperate") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate421women:
    scene date restroom door men
    "You let her go to the women's restroom and go to the men's restroom."
    pov "{i}I hope this is a good idea.{/i}"
    scene date men restroom
    pov "{i}Maybe she can hide and when he found me alone I can tell him that she already left.{/i}"
    pov "{i}But... I'm not sure...{/i}"
    pov "{i}Shit, he's not coming. I have a bad feeling. I need to check on her.{/i}"
    scene black
    "You go to the women's restroom."
    scene date 21pm ntr00
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    pov "{i}Shit... Shit... He found her.{/i}"
    "Bad Guy" "You still trying to hide? You should know that you can't trick me!"
    mom "I... I'm sorry Peter."
    "Bad Guy" "Did you really think I would forget you after I did it for you?"
    "Bad Guy" "You owe me [mother]!"
    mom "Please, I'm really sorry. You misunderstand..."
    "Bad Guy" "Get your damn dress off!"
    mom "O... ok. Don't get mad, Peter."
    pov "{i}What...? I thought he didn't know her name? And he's from a rival gang?{/i}"
    pov "{i}And now she owes him something? But then she must have lied to me?{/i}"
    pov "{i}Something is really wrong here!{/i}"
    pov "{i}I'm not sure anymore what to do now... Help her or watch and find more out?{/i}"
    call screen ndate21ntrstop

screen ndate21ntrstop():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_action_%s.png" xpos 964 ypos 270 action (Hide('ndate21ntrstop'), Jump('ndate21interfere')) hovered tt.Action ("Interfere") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1257 ypos 270 action (Hide('ndate21ntrstop'), Jump('ndate21ntr1')) hovered tt.Action ("Watch longer") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate21interfere:
    scene date 21pm ntr00
    pov "{i}I need to stop this! I'll show you motherfucker!{/i}"
    pov "Hey asshole!"
    "Bad Guy" "What?"
    scene date 21pm ntr01stop
    pov "Take this!"
    "You kick the door straight in his face!"
    "Bad Guy" "Aaah..."
    scene date 21pm ntr02stop
    "Bad Guy" "You piece of shit. I'll kill you!"
    pov "{i}Damn, he is still standing. I need to run!{/i}"
    "You run away."
    scene date 21pm ntr03stop
    pov "{i}Faster! I'll hide here behind a pillar.{/i}"
    pov "{i}Maybe I'm, lucky and I damaged his head.{/i}"
    scene date 21pm ntr04stop
    pov "{i}There he is.{/i}"
    pov "{i}He's talking to the waitress. Where's she pointing at?{/i}"
    scene date 21pm ntr05stop
    pov "{i}Phew! She sent him away. I hope he won't take revenge on her.{/i}"
    pov "{i}But now I have a lot of questions.{/i}"
    scene date 21pm ntr06stop
    mom "Are you alright?"
    if inc == True:
        mom "Yes no problem. He's gone."
    else:
        mom "Yes no problem. He's gone."
    pov "But I have some questions."
    mom "Yes, I know. But I need to go home now."
    pov "..."
    mom "Please let's go, I'm feeling really bad."
    pov "Okay..."
    scene black
    "You go home together."
    $ d9rnntri = True
    $ weekendactivities += 1
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label ndate21ntr1:
    scene date 21pm ntr00
    pov "{i}I'll watch longer to find out what's going on.{/i}"
    "Bad Guy" "Now come here [mother]!"
    mom "Yes, Peter."
    mom "Haaah..."
    "Peter" "You're so damn wet again!"
    pov "{i}Wet? Wait a second...{/i}"
    scene date 21pm ntr01
    pov "{i}They're fucking...{/i}"
    pov "{i}So she definitely lied at me, but why? Maybe she didn't want me to know that they're together?{/i}"
    call screen ndate21ntrapp

screen ndate21ntrapp():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1286 ypos 193 action (Hide('ndate21ntrapp'), Jump('ndate21ntrgood')) hovered tt.Action ("I don't care") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 605 ypos 193 action (Hide('ndate21ntrapp'), Jump('ndate21ntrbad')) hovered tt.Action ("That's so wrong") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate21ntrgood:
    scene date 21pm ntr01
    $ ntrlovenic = True
    $ ntrhatenic = False
    if inc == True:
        pov "{i}But I don't care when mom wants to have fun with other men.{/i}"
    else:
        pov "{i}But I don't care when she wants to have fun with other men.{/i}"
    pov "{i}And she really seems to like it with him, riding on him.{/i}"
    mom "Ohhh..."
    "Peter" "Yes, do it faster. Ride me!"
    scene date 21pm ntr02
    mom "Oh yes, you're all in me!"
    "Peter" "Good, ride me as hard as you want, slut!"
    mom "Haahhh... Hnng..."
    pov "{i}Damn, she's really enjoying it.{/i}"
    mom "I need more!"
    "Peter" "Come here!"
    scene date 21pm ntr03
    mom "Haaah... Ahhh. hah..."
    "Peter" "Better! Now you're sitting free and I'm under control."
    mom "Yes, harder, harder!"
    "Peter" "Oh, when I'm done with you, you'll come hard."
    pov "{i}Wow, she really likes it rough.{/i}"
    scene date 21pm ntr04
    "Peter" "Let me help you! You'll love it!"
    mom "Hnnng...!"
    pov "{i}Shit! Isn't that going too far?{/i}"
    mom "Harder you old prick!"
    "Peter" "Oh, wait you slut!"
    mom "Hnng..."
    pov "{i}I can't believe it! She really loves the hard stuff.{/i}"
    $ momchoke = True
    pov "{i}But good to know.{/i}"
    scene date 21pm ntr05
    pov "{i}Damn, they almost saw me...{/i}"
    mom "Hnng... hnng..."
    "Peter" "Yes, take it! I'm almost there!"
    pov "{i}What a hard, rough fucking... I wonder if she does this stuff with Bruce too?{/i}"
    scene date 21pm ntr06
    mom "Hnng... Haaaahh..."
    "Peter" "Yes! Come with me slut!"
    pov "{i}What a damn show! And she seems to have cum hard.{/i}"
    mom "Hnn... hnn..."
    "Peter" "Let me mark you good."
    pov "{i}They're done now. Let's hide.{/i}"
    scene date 21pm ntr07
    pov "{i}He's going...{/i}"
    "Peter" "Now we're even!"
    mom "Hnn... hnn..."
    pov "{i}She seems to be really done...{/i}"
    scene date 21pm ntr08
    pov "{i}Wow! She even fainted.{/i}"
    pov "{i}I should wake her up, we should go.{/i}"
    pov "{i}Or maybe...{/i}"
    call screen ndate21ntrtake

screen ndate21ntrtake():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1286 ypos 193 action (Hide('ndate21ntrtake'), Jump('ndate21ntrfuck')) hovered tt.Action ("Fuck her too") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 605 ypos 193 action (Hide('ndate21ntrtake'), Jump('ndate21ntrhelp')) hovered tt.Action ("Wake her up") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate21ntrfuck:
    scene date 21pm ntr08
    pov "{i}I want to fuck her too. She's unconscious, so she won't complain.{/i}"
    pov "{i}Damn I'm so hard right now.{/i}"
    if inc == True:
        pov "{i}You're mine now, mom!{/i}"
    else:
        pov "{i}You're mine now, [mother]!{/i}"
    scene date 21pm ntr09b
    pov "{i}Oh, yes! This is heaven...{/i}"
    if inc == True:
        pov "{i}I'm fucking you, mom!{/i}"
    else:
        pov "{i}I'm fucking you, [mother]!{/i}"
    mom "Hnng... hnng..."
    pov "{i}She noticed the penetration but is still unconscious.{/i}"
    pov "{i}Damn, that's too much. I'm done...{/i}"
    $ ndate21ntrsex = True
    $ d9rnntr = True
    call screen ndate21ntrcum

screen ndate21ntrcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 397 ypos 719 action (Hide('ndate21ntrcum'), Jump('ndate21ntrinside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 765 ypos 534 action (Hide('ndate21ntrcum'), Jump('ndate21ntroutside')) hovered tt.Action ("Cum outside") focus_mask True
        frame:
            xalign .5
            text tt.value


label ndate21ntrinside:
    scene date 21pm ntr09b
    if inc == True:
        pov "{i}Oh yes, take my sperm in you, mom!{/i}"
    else:
        pov "{i}Oh yes, take my sperm in you, [mother]!{/i}"
    pov "Ohhh, yeeess..."
    mom "Hnng..."
    "You came inside her."
    scene date 21pm ntr08i
    pov "{i}That was a really good fuck! I needed that!{/i}"
    pov "{i}And so much cum on her.{/i}"
    pov "{i}Let's wake her up now.{/i}"
    jump ndate21ntrhelp

label ndate21ntroutside:
    scene date 21pm ntr09a
    if inc == True:
        pov "{i}Let me mark you too, mom!{/i}"
    else:
        pov "{i}Let me mark you too, [mother]!{/i}"
    pov "Ohhh, yeeess..."
    mom "Hnng..."
    scene date 21pm ntr08o
    pov "{i}That was a really good fuck! I needed that!{/i}"
    pov "{i}And so much cum on her.{/i}"
    pov "{i}Let's wake her up now.{/i}"
    jump ndate21ntrhelp

label ndate21ntrbad:
    scene date 21pm ntr01
    $ ntrlovenic = False
    $ ntrhatenic = True
    if inc == True:
        pov "{i}No that asshole is fucking my mom!{/i}"
    else:
        pov "{i}No this asshole is fucking her!{/i}"
    pov "{i}And she really seems to like it with him, riding on him. Nooo!{/i}"
    mom "Ohhh..."
    "Peter" "Yes, do it faster. Ride me!"
    scene date 21pm ntr02
    mom "Oh yes, you're all in me!"
    "Peter" "Good, ride me as hard as you want, slut!"
    mom "Haahhh... Hnng..."
    pov "{i}Damn, she can't be enjoying that old prick.{/i}"
    mom "I need more!"
    "Peter" "Come here!"
    scene date 21pm ntr03
    mom "Haaah... Ahhh. hah..."
    "Peter" "Better! Now you're sitting free and I'm under control."
    mom "Yes, harder, harder!"
    "Peter" "Oh, when I'm done with you, you'll come hard."
    pov "{i}What has he done with her? She's acting like a slut.{/i}"
    scene date 21pm ntr04
    "Peter" "Let me help you! You'll love it!"
    mom "Hnnng...!"
    pov "{i}Shit! Isn't that going too far?{/i}"
    mom "Harder you old prick!"
    "Peter" "Oh, wait you slut!"
    mom "Hnng..."
    pov "{i}I can't believe it! She really loves that hard stuff.{/i}"
    $ momchoke = True
    pov "{i}But good to know.{/i}"
    scene date 21pm ntr05
    pov "{i}Damn, they almost saw me...{/i}"
    mom "Hnng... hnng..."
    "Peter" "Yes, take it! I'm almost there!"
    pov "{i}What a hard, rough fucking... I should kill this asshole. Take her like a slut.{/i}"
    scene date 21pm ntr06
    mom "Hnng... Haaaahh..."
    "Peter" "Yes! Come with me slut!"
    pov "{i}He took her too hard!{/i}"
    mom "Hnn... hnn..."
    "Peter" "Let me mark you good."
    pov "{i}They're done now. Let's hide.{/i}"
    scene date 21pm ntr07
    pov "{i}He's going...{/i}"
    "Peter" "Now we're even!"
    mom "Hnn... hnn..."
    pov "{i}She seems to be really done... That damn prick!{/i}"
    scene date 21pm ntr08
    pov "{i}Wow! She even fainted.{/i}"
    pov "{i}I should wake her up, we should go.{/i}"
    pov "{i}Or maybe...{/i}"
    call screen ndate21ntrtake

label ndate21ntrhelp:
    scene date 21pm ntr08
    if inc == True:
        pov "Mom! Wake up mom!"
    else:
        pov "[mother]! Wake up [mother]!"
    pov "We should go. He's gone!"
    mom "Hnn..."
    scene date 21pm ntr09w
    mom "It's you [pov]..."
    pov "I saw what he did to you, but it's better when we go now."
    mom "Oh... he raped me..."
    pov "{i}Rape? Still lying to me...{/i}"
    pov "Come get your dress back on."
    mom "Thank you for helping me..."
    scene date 21pm ntr010w
    mom "Can you wait a moment outside? I need to clear me."
    if inc == True:
        pov "Sure, mom."
    else:
        pov "Sure, [mother]."
    scene black
    "You wait outside."
    scene date 21pm ntr011w
    pov "You're done? Can we go now?"
    mom "Yes. Thank you again for taking care of me."
    if ndate21ntrsex == True:
        if inc == True:
            pov "{i}No, thank you, for letting me fuck you, mom.{/i}"
        else:
            pov "{i}No, thank you, for letting me fuck you.{/i}"
    else:
        pov "You're welcome."
    scene black
    "You go home together."
    $ weekendactivities += 1
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose




label ndate421men:
    scene date restroom door men
    pov "<whisper> I have an idea! Follow me!"
    mom "<whisper> But that's the men's restroom!"
    pov "<whisper> Trust me! It'll work out."
    scene date men restroom
    pov "Good, nobody's here."
    mom "But what to do now? He might search here too."
    pov "Let's hide in a stall."
    mom "But..."
    scene date 21pm 026
    mom "You mean we're together in this small space?"
    pov "Yes get in and sit on the toilet, no waiting time now."
    mom "Yeah you're right."
    scene date 21pm 027
    mom "But it's so small. We won't fit together on it."
    pov "I'll take you on my lap, so he'll just see my feet when he checks the stalls."
    mom "I hope that'll work."
    pov "Just trust me!"
    scene date 21pm 028
    pov "See...? Now we fit good on that small spot."
    pov "Yes good, hold yourself on me."
    mom "It's a little bit weird. Sitting so close with you on your lap."
    pov "You have a better idea how to hide ourselves?"
    mom "No..."
    pov "Then calm down. We're just sitting here and hiding."
    mom "Maybe you're right..."
    scene date 21pm 029
    pov "So what's with him? Why are you so scared?"
    mom "He's the boss of another gang. His reputation is very bad because he's very violent and even kills people."
    pov "So it could be very bad if he founding you as a member of the rival gang?"
    mom "Yes and he know my face. Luckily he doesn't know my name, so I have only to fear him when I meet him accidentally."
    pov "Like here and now."
    mom "Yes. He must not find me. I'm so scared."
    pov "I'll protect you!"
    mom "I'm sure he'll carry a weapon, so don't do something stupid please!"
    pov "We'll get out of it!"
    scene date 21pm 030
    pov "{i}She so damn...{/i}"
    scene date 21pm 031
    pov "{i}close to me.{/i}"
    "You hear the restroom door open."
    scene date 21pm 032
    mom "<whisper>Oh no! He's here."
    pov "<whisper> Just stay silent."
    "Bad Guy" "Yeah I know. Trust me if she's here I'll find her."
    pov "{i}He's on the phone?{/i}"
    "Bad Guy" "That's weird! I see only one guys feet but I'm sure I heard two voices."
    scene date 21pm 033
    mom "<whisper> Oh no..."
    pov "<whisper> Shit what to do now?"
    mom "<whisper> I think I know something."
    jump ndate421mench

label ndate421mench:
    call screen ndate421mench1

screen ndate421mench1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1589 ypos 305 action (Hide('ndate421mench1'), Jump('ndate421mencor')) hovered tt.Action ("Choose your solution [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1589 ypos 449 action (Hide('ndate421mench1'), Jump('ndate421menlove')) hovered tt.Action ("Hear her solution [lv1]") focus_mask True
        frame:
            xalign .5
            text tt.value



label ndate421mencor:
    scene date 21pm 033
    pov "<whisper> Let's pretend we're a couple and making out. So he won't get suspicious!"
    mom "<whisper> What..."
    pov "<whisper> Just do as I say. He's moving closer."
    mom "..."
    scene date 21pm 034a
    mom "Hmm... hmm..."
    "You nod to her showing her doing it right."
    "Bad Guy" "Oh there's a couple in here..."
    mom "Hmm..."
    if inc == True:
        pov "{i}Damn, that so hot. My mom is sitting on my lap moaning. I'll have to take advantage of it.{/i}"
    else:
        pov "{i}Damn, that so hot. [mother] is sitting on my lap moaning. I'll have to take advantage of it.{/i}"
    pov "<whisper> Give yourself in!"
    mom "HMM... HMM..."
    pov "{i}Damn, she shouldn't overdo it. Let's check what he's doing.{/i}"
    scene date check guy
    pov "{i}Oh good, he's gone. But wait a second...{/i}"
    if inc == True:
        pov "{i}Mom doesn't know it so I can play this opportunity out!{/i}"
    else:
        pov "{i}[mother] doesn't know it so I can play this opportunity out!{/i}"
    scene date 21pm 034a
    pov "{i}I need to play with them! And she had to play along with me. That should be great.{/i}"
    scene date 21pm 035a
    mom "Hnn... <whisper> what are you doing?"
    pov "<whisper> We need to make it more realistic! Or he won't believe it!"
    mom "<whisper> No, please... it's wrong!"
    pov "<whisper> Sshhh, just concentrate on your moaning. You don't want to get caught, do you?"
    if momcorruption < 20:
        scene date 21pm 099
        mom "You can stop now. I think he's gone."
        pov "You sure? We shouldn't risk it."
        mom "I'm sure! Let me check it!"
        pov "{i}Damn, she got suspicious too fast. I wonder if I could have done more if she was more corrupted?{/i}"
    else:
        scene date 21pm 036a
        mom "Hah... hah..."
        pov "{i}Good, she believes me,{/i}"
        scene date 21pm 037a
        pov "{i}It's like heaven. I can play with her and she thinks I'm doing this to help her.{/i}"
        pov "{i}Wait... this will help us both!{/i}"
        mom "Hnn..."
        scene date 21pm 038a
        pov "<whisper> You're doing good. You're moaning sounds more and more realistic."
        mom "Hnn... hmm..."
        pov "{i}That's getting better and better. It's like she's enjoying it.{/i}"
        scene date 21pm 039a
        pov "{i}Kneading these fine, big tits. Damn, I'm getting hard so fast.{/i}"
        pov "{i}More! I need to knead them more.{/i}"
        mom "Hah... Hnng..."
        pov "{i}Her moaning sounds very realistic right now. Is she getting horny?{/i}"
        pov "{i}Let's check what can I do further.{/i}"
        scene date 21pm 040a
        mom "Hmm... Hnng..."
        "She begins to shake her head wildly."
        scene date 21pm 041a
        pov "{i}Damn, as I thought. She's getting wet.{/i}"
        if momcorruption < 40:
            scene date 21pm 099
            mom "You can stop now. I think he's gone."
            pov "You sure? We shouldn't risk it."
            mom "I'm sure! Let me check it!"
            pov "{i}Damn, she got suspicious. I wonder if I could have done more if she was more corrupted?{/i}"
        else:
            scene date 21pm 042a
            mom "Hah... hah..."
            mom "<whisper> Stop... we can't go further..."
            pov "{i}\"We?\" Interesting, so she's getting really horny and enjoying it.{/i}"
            pov "<whisper> We need to be sure! You have to keep going. Give yourself in!"
            mom "<whisper> But... HAAAH...!"
            image fingernic_date = Movie(channel="fingernic_date", play="images/anim/fingernic_date.webm")
            scene fingernic_date with dissolve:
                size (config.screen_width, config.screen_height)
            pause            
            pov "{i}She's so wet I can slide in easily. Her hot wet pussy!{/i}"
            mom "Haaahh... Hnnngg..."
            pov "{i}That she's getting so horny even when she's thinking that guy is outside. Maybe she's a slut?{/i}"
            pov "{i}Or she didn't tell me everything. I wonder how she can get so horny when fearing death?{/i}"
            pov "{i}But that's so perfect now.{/i}"
            if inc == True:
                pov "{i}I've waited so long to get in my mom's pussy.{/i}"
            else:
                pov "{i}I've waited so long to get in [mother]'s pussy.{/i}"
            scene date 21pm 044a
            mom "Hnng... hah... hah..."
            pov "<whisper> Good. Now you're doing it right. Let him hearing you getting off."
            pov "{i}And me of course!{/i}"
            mom "Hah... No... stop..."
            pov "<whisper> What are you doing. He'll get suspicious. Let me help you some more."
            image fingernic_date = Movie(channel="fingernic_date", play="images/anim/fingernic_date.webm")
            scene fingernic_date with dissolve:
                size (config.screen_width, config.screen_height)
            pause                        
            pov "{i}She so damn wet now. I'm two fingers wide all in her.{/i}"
            mom "Ohhh... ahhh... hnng..."
            pov "{i}That was right! She's shaking her hips against my hand. She is trying to get herself off.{/i}"
            mom "Hnnng... ahhh..."
            pov "{i}But that won't happen, I'm so far now, I want to have fun too.{/i}"
            scene date 21pm 046a
            pov "{i}Damn, now she's sucking wildly on my finger.{/i}"
            if inc == True:
                pov "<whisper>Good, give yourself all in, mom!"
            else:
                pov "<whisper>Good, give yourself all in, mom!"
            mom "<sucking> Hmm... hnng... hmm..."
            pov "{i}It's so... damn time for more. But how to do it?{/i}"
            mom "Hnn..."
            pov "{i}Oh yes that's it! That's the way I would get the chance to fuck her!{/i}"
            scene date 21pm 047a
            mom "Ahhh... Hahhh..."
            pov "<whisper> Did you hear that? He's checking the stalls. We need to improvise!"
            mom "Hnnng..."
            pov "{i}Haha, she's too horny to think straight.{/i}"
            pov "<whisper> Bend over! I'll pretend to fuck you, so he'll only see my back when he opens this stall."
            scene date 21pm 048a
            pov "<whisper> Perfect! Now relax yourself and let's get this over with!"
            mom "Hah... <whisper> over with?"
            pov "{i}Oh shit. Don't ruin it yet.{/i}"
            pov "<whisper> The pretending to fuck. He'll see only me and your back and I'm sure he'll go when he sees what we're doing!"
            mom "Hnn..."
            scene date 21pm 049a
            if inc == True:
                pov "{i}Time to fuck my mom now. I can't wait!{/i}"
            else:
                pov "{i}Time to fuck [mother] now. I can't wait!{/i}"
            scene date 21pm 050a
            mom "<whisper> Stop! You can't be serious!"
            pov "<whisper> Remember what I said. It has to be realistic!"
            if momcorruption < 60:
                scene date 21pm 099
                mom "You'll stop now! I think he's gone."
                pov "You sure? We shouldn't risk it."
                mom "I'm sure! Let me check it!"
                pov "{i}Damn, that was too much! I wonder if I could have done more if she were more corrupted?{/i}"
            else:
                scene date 21pm 050a
                mom "<whisper> We have to stop, this is going to far."
                pov "{i}So the other things before were ok? I think she only needs the last push!{/i}"
                pov "<whisper> No, we have to finish this now!"
                pov "{i}Nothing will stop me now!{/i}"
                jump ndate421fuck
    $ momcorruption += 1
    jump ndate521

label ndate421fuck:
    call screen ndate421fuck1

screen ndate421fuck1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 509 ypos 113 action (Hide('ndate421fuck1'), Jump('ndate421ass')) hovered tt.Action ("Fuck her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 299 ypos 531 action (Hide('ndate421fuck1'), Jump('ndate421pussy')) hovered tt.Action ("Fuck her pussy") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate421ass:
    scene date 21pm 051ab
    $ momanal += 1
    pov "Take it in your ass, slut! Making me all horny with your moaning!"
    mom "Haaahhh..."
    pov "Now receive your pounding!"
    pov "{i}Good that her juices made her asshole all wet.{/i}"
    scene date 21pm 052a
    pov "<whisper> I need to talk dirty to stay realistic. So don't wonder about it!"
    pov "You're so damn tight. I've waited so long to give you a good fuck. You'll love it too!"
    mom "HNNGG... HNNGG..."
    pov "{i}She's shaking. I bet she waited for it after getting so horny before.{/i}"
    pov "{i}I need to give my best to get her off too!{/i}"
    scene date 21pm 053ab
    pov "Here take me all in! Enjoy my hard dick fucking you!"
    mom "Hah... hah... hah..."
    pov "{i}Damn, she's getting tighter and moving with my rhythm. She's close to cumming.{/i}"
    mom "Hah... hnng..."
    pov "{i}But I can't let her cum alone now!{/i}"
    scene date 21pm 054a
    if momfirstfuck == False:
        if inc == True:
            pov "{i}I'm fucking my mom for the first time and she's about to cum from me! Time to enjoy this with me cumming too!{/i}"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it!"
        else:
            pov "{i}I'm fucking [mother] for the first time and she's about to cum from me! Time to enjoy this with me cumming too!{/i}"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it!"
    else:
        if inc == True:
            pov "{i}I'm fucking my mom and she's about to cum from me! Time to enjoy this with me cumming too!{/i}"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it!"
        else:
            pov "{i}I'm fucking [mother] and she's about to cum from me! Time to enjoy this with me cumming too!{/i}"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it!"
    jump ndate421cum

label ndate421cum:
    call screen ndate421cum1

screen ndate421cum1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 714 ypos 70 action (Hide('ndate421cum1'), Jump('ndate421inass')) hovered tt.Action ("Cum inside her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 878 ypos 70 action (Hide('ndate421cum1'), Jump('ndate421out')) hovered tt.Action ("Cum on her ass") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate421inass:
    scene date 21pm 054a
    if momfirstfuck == False:
        if inc == True:
            pov "<whisper> I'm about to cum too, mom. I'm glad that you enjoyed our first time fucking together that much!"
        else:
            pov "<whisper> I'm about to cum too, [mother]. I'm glad that you enjoy our first time fucking together that much!"
    else:
        if inc == True:
            pov "<whisper> I'm about to cum too, mom. I'm glad that you enjoy us fucking together that much!"
        else:
            pov "<whisper> I'm about to cum too, [mother]. I'm glad that you enjoy us fucking together that much!"
    mom "Haaaahhh... Aaaaahhhh..."
    pov "{i}She's cumming. I can feel it.{/i}"
    pov "<whisper> I'll release myself inside you! Enjoy my hot sperm!"
    "You spurt your sperm inside her asshole."
    mom "Haaah... Hnnng..."
    "After a few moments longer you pull your dick out."
    scene date 21pm 056a
    if inc == True:
        pov "{i}What a wonderful view! My cum is dripping out off my moms ass.{/i}"
    else:
        pov "{i}What a wonderful view! My cum is dripping out off [mother]'s ass.{/i}"
    pov "{i}And she enjoyed it so much that she came too!{/i}"
    if ndate21photoinass == False:
        pov "{i}I should capture this moment. Let's take a photo.{/i}"
        scene date photo1
        pov "{i}Done!{/i}"
        $ ndate21photoinass = True
    $ ndate21ass = True
    $ ndate21inside = True
    jump ndate521fucked

label ndate421out:
    scene date 21pm 054a
    if momfirstfuck == False:
        if inc == True:
            pov "<whisper> I'm about to cum too, mom. I'm glad that you enjoy our first time fucking together that much!"
        else:
            pov "<whisper> I'm about to cum too, [mother]. I'm glad that you enjoy our first time fucking together that much!"
    else:
        if inc == True:
            pov "<whisper> I'm about to cum too, mom. I'm glad that you enjoy us fucking together that much!"
        else:
            pov "<whisper> I'm about to cum too, [mother]. I'm glad that you enjoy us fucking together that much!"
    mom "Haaaahhh... Aaaaahhhh..."
    pov "{i}She's cumming. I can feel it.{/i}"
    pov "<whisper> I'll release myself on your ass! So I'll mark you!"
    scene date 21pm 055a
    pov "Aaahhh..."
    pov "{i}She pressed so much out of me!{/i}"
    scene date 21pm 056
    if inc == True:
        pov "{i}What a wonderful view! My cum smeared on my mom's ass. Now she's marked as mine.{/i}"
    else:
        pov "{i}What a wonderful view! My cum smeared on [mother]'s ass. Now she's marked as mine.{/i}"
    pov "{i}And she enjoyed it so much that she came too!{/i}"
    if ndate21photoover == False:
        pov "{i}I should capture this moment. Let's take a photo.{/i}"
        scene date photo3
        pov "{i}Done!{/i}"
        $ ndate21photoover = True
    $ ndate21outside = True
    jump ndate521fucked

label ndate421pussy:
    scene date 21pm 051a
    $ mompussy += 1
    pov "Take it in your pussy, slut! Making me all horny with your moaning!"
    mom "Haaahhh..."
    pov "Now receive your pounding!"
    pov "{i}Good she's so wet that I can slide easy into her.{/i}"
    scene date 21pm 052a
    pov "<whisper> I need to talk dirty to stay realistic. So don't wonder about it!"
    pov "You're so damn tight. I've waited so long to give you a good fuck. You'll love it too!"
    mom "HNNGG... HNNGG..."
    pov "{i}She's shaking. I bet she waited for it after getting so horny before.{/i}"
    pov "{i}I need to give my best to get her off too!{/i}"
    scene date 21pm 053a
    pov "Here take me all in! Enjoy my hard dick fucking you!"
    mom "Hah... hah... hah..."
    pov "{i}Damn, she's getting tighter and moving with my rhythm. She's close to cumming.{/i}"
    mom "Hah... hnng..."
    pov "{i}But I can't let her cum alone now!{/i}"
    scene date 21pm 054a
    if momfirstfuck == False:
        if inc == True:
            pov "{i}I'm fucking my mom for the first time and she's about to cum from me! Time to enjoy this with me cumming too!{/i}"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it!"
        else:
            pov "{i}I'm fucking [mother] for the first time and she's about to cum from me! Time to enjoy this with me cumming too!{/i}"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it !"
    else:
        if inc == True:
            pov "{i}I'm fucking my mom and she's about to cum from me! Time to enjoy this with me cumming too!{/i}"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it !"
        else:
            pov "{i}I'm fucking [mother] and she's about to cum from me! Time to enjoy this with me cumming too!{/i}"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it !"
    jump ndate421cum2

label ndate421cum2:
    call screen ndate421cum3

screen ndate421cum3():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 714 ypos 70 action (Hide('ndate421cum3'), Jump('ndate421inpussy')) hovered tt.Action ("Cum inside her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 878 ypos 70 action (Hide('ndate421cum3'), Jump('ndate421out')) hovered tt.Action ("Cum on her ass") focus_mask True
        frame:
            xalign .5
            text tt.value

label ndate421inpussy:
    scene date 21pm 054a
    if momfirstfuck == False:
        if inc == True:
            pov "<whisper> I'm about to cum too, mom. I'm glad that you enjoy our first time fucking together that much!"
        else:
            pov "<whisper> I'm about to cum too, [mother]. I'm glad that you enjoy our first time fucking together that much!"
    else:
        if inc == True:
            pov "<whisper> I'm about to cum too, mom. I'm glad that you enjoy us fucking together that much!"
        else:
            pov "<whisper> I'm about to cum too, [mother]. I'm glad that you enjoy us fucking together that much!"
    mom "Haaaahhh... Aaaaahhhh..."
    pov "{i}She's cumming. I can feel it.{/i}"
    pov "<whisper> I'll release myself inside you! Enjoy my hot sperm!"
    "You spurt your sperm inside her pussy."
    mom "Haaah... Hnnng..."
    "After a few moments longer you pull your dick out."
    scene date 21pm 056b
    if inc == True:
        pov "{i}What a wonderful view! My cum is dripping out off my moms pussy.{/i}"
    else:
        pov "{i}What a wonderful view! My cum is dripping out off [mother]'s pussy.{/i}"
    pov "{i}And she enjoyed it so much that she came too!{/i}"
    if ndate21photoinpussy == False:
        pov "{i}I should capture this moment. Let's take a photo.{/i}"
        scene date photo2
        pov "{i}Done!{/i}"
        $ ndate21photoinpussy = True
    $ ndate21pussy = True
    $ ndate21inside = True
    jump ndate521fucked


label ndate521fucked:
    $ momfirstfuck = True
    if inc == True:
        pov "He's gone. Let's go too, mom."
    else:
        pov "He's gone. Let's go too, [mother]"
    mom "Hnn..."
    scene date 21pm 057
    pov "Everything alright? You enjoyed it a little bit too much, huh?"
    mom "You... you fucked me... hnn..."
    pov "Yes, sorry! I got carried away while we were hiding."
    mom "But, there was no need..."
    pov "Oh yes. You needed to sound more realistic and then it was too much for me."
    pov "You gave yourself in to much."
    mom "..."
    pov "I did it only to protect you and it's gone out for good."
    pov "And I'm sure it wasn't your first fuck."
    mom "Hnng..."
    pov "Don't get mad now. I know you came too."
    scene date 21pm 058
    mom "No one can ever know that!"
    if inc == True:
        pov "Ok, mom. But let me say that fucking you was just wonderful!"
    else:
        pov "Ok, [mother]. But let me say that fucking you was just wonderful!"
    mom "No more talking about it!"
    scene black
    "You go home together."
    $ d9rncorf = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label ndate521:
    scene date 21pm 098
    mom "As I thought, he's gone. We should go now too."
    pov "{i}Noooo! Damn, maybe I'll get another chance.{/i}"
    scene black
    "You go home together."
    $ d9rncor = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose


label ndate421menlove:
    scene date 21pm 033
    pov "What are you thinking of?"
    mom "It might sound a little weird..."
    scene date 21pm 033b
    mom "but if we're pretending to make out, he won't disturb us."
    pov "Do you really think this is a good idea?"
    mom "The best I can think of at the moment. We can't fight him."
    if inc == True:
        pov "{i}This could get really weird, pretending to make out with my mom!{/i}"
    else:
        pov "{i}This could get really weird, pretending to make out with my mom's best friend!{/i}"
    pov "But..."
    scene date 21pm 033
    mom "<whisper> Ssshh... Just play along."
    pov "Ok."
    scene date 21pm 030
    pov "{i}This is really bad. What's she thinking of? I'm gonna get horny as fuck!{/i}"
    scene date 21pm 031
    pov "{i}But why did she come up with this?{/i}"
    if lroom11kiss == True:
        if inc == True:
            pov "{i}Is my resemblance to dad the reason?{/i}"
            pov "{i}Like when she tried to make out with me when she was drunk in the living room?{/i}"
        else:
            pov "{i}Is my resemblance to my father the reason?{/i}"
            pov "{i}Like when she tried to make out with me when she was drunk in the living room?{/i}"
    mom "Hah... hah... hah..."
    scene date 21pm 036a
    pov "{i}You must be kidding...{/i}"
    if inc == True:
        pov "<whisper> Mom, you need to stop..."
    else:
        pov "<whisper> [mother], you need to stop..."
    mom "<whisper> I know it may be uncomfortable, but just a little longer, [pov]."
    mom "<whisper> I'm sure it'll work and save us."
    pov "{i}Damn, but my boner is killing me.{/i}"
    pov "{i}Fuck it! I can't withstand her any longer.{/i}"
    scene date 21pm 034b
    mom "Hmm...?"
    if inc == True:
        "You kiss your mom."
    else:
        "You kiss her."
    mom "Hmm..."
    pov "{i}Oh yes, I did it!{/i}"
    if lroom11kiss == True:
        pov "{i}And it's even better when she's not drunk.{/i}"
    if momlove <= 30:
        scene date 21pm 040a
        mom "<whisper> What are you doing? Are you crazy?"
        if inc == True:
            pov "<whisper> I'm sorry mom, I couldn't withstand it. I love you!"
        else:
            pov "<whisper> I'm sorry [mother], I couldn't withstand it. I love you!"
        mom "<whisper> Cut it out! We can't do this!"
        jump ndate21lstop
    else:
        scene date 21pm 035a
        mom "<whisper> What are you doing? Are you crazy?"
        if inc == True:
            pov "<whisper> I'm sorry mom, I couldn't withstand it. I love you!"
        else:
            pov "<whisper> I'm sorry [mother], I couldn't withstand it. I love you!"
            scene date 21pm 035b
        if inc == True:
            mom "<whisper> I'm sorry to get you in this situation, son."
        else:
            mom "<whisper> I'm sorry to get you in this situation, [pov]."
        mom "<whisper> But we must pretend this just a little bit longer."
        pov "<whisper> I can't stop now!"
        scene date 21pm 036b
        "You kiss her again."
        mom "<whisper> No, wait... Hmm..."
        pov "{i}Hm, not much resistance from her anymore. She must like it too.{/i}"
        scene date 21pm 037b
        mom "Hnn... <whisper> not there..."
        pov "{i}She's trembling. Is it her weak point?{/i}"
        pov "<whisper> Your soft skin! You love it getting kissed like this, don't you?"
        mom "Hah... <whisper> we shouldn't..."
        if momlove <= 50:
            scene date 21pm 040a
            mom "<whisper> We need to stop this! It's going to far."
            pov "<whisper> But you liked it. And I know you love me too."
            mom "<whisper> We can't do this anymore!"
            jump ndate21lstop
        else:
            scene date 21pm 038b
            pov "<whisper> Yes, we should!"
            mom "Hm... <kiss>"
            if inc == True:
                pov "<whisper> I won't judge you, mom. You know that I love you!"
            else:
                pov "<whisper> I won't judge you, [mother]. You know that I love you!"
            mom "Hm..."
            pov "{i}Hm, that seemed to relax her a little bit.{/i}"
            pov "{i}But I want to taste more of her.{/i}"
            scene date 21pm 040b
            "You go down with your kisses."
            pov "{i}Her breasts are so soft and warm.{/i}"
            mom "<whisper> Oh... my... god..."
            pov "{i}The right decision.{/i}"
            mom "Hnn... hm..."
            pov "{i}I can feel her heartbeat and her twitching, when my kisses hit her.{/i}"
            pov "{i}More!{/i}"
            scene date 21pm 041b
            pov "<sucking>"
            mom "Oh...? Hnn..."
            pov "{i}Her hard nipples and I can tastes them.{/i}"
            if inc == True:
                pov "<whisper> You're tits are so beautiful and tasty, mom!"
            else:
                pov "<whisper> You're tits are so beautiful and tasty, [mother]!"
            scene date 21pm 042b
            mom "<whisper> This is going too far..."
            pov "<whisper> Why are you so scared?"
            if inc == True:
                mom "<whisper> We're related. This must stop."
            else:
                mom "<whisper> We're like a family. This must stop."
            pov "<whisper> No we must not. It's not wrong that we love each other."
            mom "<whisper> But..."
            scene date 21pm 043b
            pov "<whisper> I felt your reactions while I kissed you. You enjoyed it!"
            pov "<whisper> It's time that you gave in and let me pleasure you..."
            mom "..."
            pov "<whisper> I'm very sure that you miss getting spoiled in this new situation."
            if momlove <= 80:
                scene date 21pm 040a
                mom "<whisper> No, I shouldn't do it."
                pov "<whisper> But you liked it. And I know you love me too."
                mom "<whisper> We've gone this far!"
                jump ndate21lstop
            else:
                mom "..."
                pov "<whisper> Just enjoy the pleasure I want to give you!"
                pov "<whisper> There won't be any judging, just two lovers enjoying each other."
                scene date 21pm 044b
                mom "Hnn..."
                if inc == True:
                    pov "<whisper> I just want to show you my love mom! You're my goddess!"
                    pov "<whisper> And I'll still be the son you're proud of, no matter how you decide."
                else:
                    pov "<whisper> I just want to show you my love [mother]! You're my goddess!"
                    pov "<whisper> And I'll still be the boy you're proud of, no matter how you decide."
                mom "Hm... <whisper> then... go on..."
                pov "{i}Yes!{/i}"
                if inc == True:
                    pov "I love you mom!"
                else:
                    pov "I love you [mother]!"
                scene date 21pm 045b
                pov "<whisper> Your legs are so long and beautiful."
                mom "Hm..."
                pov "<whisper>Your beautiful body needs to get more rewards."
                mom "Ohh..."
                if inc == True:
                    pov "{i}She gave in! My mother enjoys the pleasure I give her!{/i}"
                else:
                    pov "{i}She gave in! [mother] enjoys the pleasure I give her!{/i}"
                scene date 21pm 046b
                pov "<kiss>"
                mom "Hah... hnn..."
                pov "{i}She's trembling like crazy. I found the lock to her heart.{/i}"
                if inc == True:
                    pov "<whisper> I've waited so long for this, mom!"
                else:
                    pov "<whisper> I've waited so long for this, [mother]!"
                mom "Hmm..."
                scene date 21pm 047b
                mom "<heavy breathing>"
                pov "<whisper> So beautiful!"
                pov "{i}I'll convince her by letting her cum.{/i}"
                if inc == True:
                    pov "{i}Getting an orgasm from her own son will show her my seriousness.{/i}"
                else:
                    pov "{i}Getting an orgasm from the son of her best friend will show her my seriousness.{/i}"
                scene date 21pm 049b
                pov "<lick> <lick>"
                mom "Hah... Hnng..."
                if inc == True:
                    pov "<whisper> You taste amazing, mom!"
                else:
                    pov "<whisper> You taste amazing, [mother]!"
                mom "Hah! <whisper> Your tongue!"
                pov "<whisper> I told you that you'd love it!"
                mom "Hah! Hah!"
                pov "{i}I found the right spot.{/i}"
                scene date 21pm 050b
                mom "Hah! Yes, right there!"
                pov "{i}Damn, she's so horny, she doesn't even try to be silent anymore.{/i}"
                mom "Hah! Hnng!"
                pov "{i}And she's pressing me onto her.{/i}"
                pov "<faster licking>"
                mom "It's so good. More [pov]!"
                scene date 21pm 050bx
                mom "AHHH! AHHHH!"
                pov "{i}She's coming. And very hard, trembling like crazy.{/i}"
                mom "Hnng! Hnng..."
                pov "{i}It won't stop...{/i}"
                mom "Oh... my god! Hah! Hah!"
                scene date 21pm 051b
                mom "Hnng..."
                if inc == True:
                    pov "<whisper> It's fantastic to see you cum like this, mom!"
                else:
                    pov "<whisper> It's fantastic to see you cum like this, [mother]!"
                mom "Th... thank you..."
                pov "<whisper> Don't be sad. It was the right thing. You made me very happy."
                pov "<whisper> Giving me the chance to show you how much I love you!"
                pov "<whisper> And it was a very enjoyable date for the two of us."
                mom "We should go now."
                pov "{i}She's still unsure, but at least she showed me that she loved it too.{/i}"
                scene date 21pm 053b
                mom "<whisper> Oh no! We totally forgot about the bad guy!"
                pov "<whisper> Yes you're right, but I'm sure he's gone since he didn't disturb us."
                mom " <whisper> We need to check first!"
                scene date check guy
                "You look under the stalls for him."
                pov "He's gone!"
                mom "Good. Then we can go home now!"
                if inc == True:
                    pov "Wait mom!"
                else:
                    pov "Wait [mother]!"
                scene date 21pm 052b
                mom "Hm...?"
                pov "I need to know if you enjoyed what I did?"
                pov "I know you came, but I want to know if you liked doing it with me."
                mom "..."
                if inc == True:
                    pov "You know that I love you, so I need to know, mom. Please tell me."
                else:
                    pov "You know that I love you, so I need to know, [mother]. Please tell me."
                mom "I... I liked it what you were doing to me..."
                mom "But no one can know about this!"
                scene date 21pm 054b
                if inc == True:
                    pov "Relax mom. No one will ever know about this! I love you and won't disappoint you."
                else:
                    pov "Relax [mother]. No one will ever know about this! I love you and won't disappoint you."
                mom "Hnn..."
                pov "I'm so glad that we had this amazing moment together."
                if inc == True:
                    pov "And I'll give you even more pleasure every time you need it, mom!"
                else:
                    pov "And I'll give you even more pleasure every time you need it, [mother]!"
                mom "Hnng..."
                pov "But now let's go home!"
                mom "Yes, let's go."
                scene black
                "You go home together."
                $ momlove += 1
                $ momdateorgasm = True
                $ d9rnlovef = True
                $ weekendactivities += 1
                if weekendactivities == 3:
                    jump weekendskip
                else:
                    jump weekendacchoose

label ndate21lstop:
    scene date 21pm 052b
    mom "<whisper> Please take a look if the bad guy is gone. I want to go home, I feel uncomfortable."
    pov "<whisper> O... okay."
    scene date check guy
    "You look under the stalls for him."
    pov "He's gone!"
    scene date 21pm 052b
    mom "Then we'll go home now!"
    pov "But..."
    mom "Cut it out! We're going now."
    scene black
    $ momlove += 1
    $ d9rnlove = True
    "You go home together."
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose



label nicoleweekendcor:
    hide screen locations
    $ momcorruption += 1
    scene black
    "You got a call from [mother] that she want to eat dinner at home, so you decide to spend time with her."
    if inc == True:
        "After you cooked dinner for your mom and yourself, you wait for her."
    else:
        "After you cooked dinner for [mother] and yourself, you wait for her."
    "You hear the front door open."
    scene weekend 8pm 001
    mom "Hey [pov], I'm back."
    mom "Did you make a dinner?"
    scene weekend 8pm 002
    mom "Oh? What a nice surprise!"
    if inc == True:
        pov "Welcome back, mom."
    else:
        pov "Welcome back, [mother]."
    mom "And a lovely decoration too."
    scene weekend 8pm 003
    mom "I'm happy you did this for me."
    pov "Yes let's eat and then we can spend the evening together."
    mom "So you have already something in mind?"
    pov "We need to bond our dirty secret more!"
    scene weekend 8pm 004c
    mom "Huh? You mean...?"
    pov "Ha, did you think it's done with a few blowjobs?"
    mom "But... what else do you want?"
    if inc == True:
        pov "You know exactly what we need to do, mom!"
    else:
        pov "You know exactly what we need to do, [mother]!"
    pov "Your pussy need also to get used to my dick!"
    scene weekend 8pm 005c
    mom "You're serious. You really want to fuck me."
    pov "Of course, a good slut needs to be ridden properly."
    pov "And we have all night just for ourselves."
    mom "..."
    pov "But now it's time to eat. How about you remove your shirt, so it won't get dirty."
    mom "What? Oh..."
    scene weekend 8pm 006c
    pov "You got the hint. I'll see them all night."
    mom "Hnng..."
    pov "Why the sad face? We're all alone and I need an appetizer for later."
    pov "Let's eat now. You'll need much energy, it'll be along night."
    scene weekend 8pm 007c
    pov "That meal will taste even better."
    mom "Hnng!"
    if inc == True:
        pov "You should be happy mom."
    else:
        pov "You should be happy [mother]."
    pov "You'll cum much often and server a higher gang member well."
    scene weekend 8pm 008c
    pov "And your hot boobs will get attention too. When they get groped and licked."
    mom "Please stop talking like that."
    scene weekend 8pm 009c
    if inc == True:
        pov "No, mom!"
    else:
        pov "No, [mother]!"
    pov "You choosed this new life and you'll have to deal with the consequences now!"
    mom "Hnng..."
    pov "I'll treat you as my slut and you'll accept your place."
    scene weekend 8pm 010c
    pov "Now eat, my dick needs some pussy!"
    mom "Hnng..."
    "You two eat dinner silent."
    scene weekend 8pm 011c
    pov "Now go downstairs. I choosed a outfit for you, wear it and wait for me."
    pov "And when I come down you'll remember to be a good girl and serve me good as your boss."
    mom "But..."
    if inc == True:
        pov "Stop complaining, mom!"
    else:
        pov "Stop complaining, [mother]!"
    pov "It's my decision!"
    mom "Hnn..."
    scene black
    "She goes down at the basement."
    "You follow her after a few minutes."
    pov "{i}Let's see if she did what I ordered.{/i}"
    scene weekend 10pm 051cp
    mom "What are you thinking, [pov]? You gave me just underwear."
    pov "{i}Oh, she's again in her rebellious mode.{/i}"
    pov "{i}Maybe I should modify my tactic to break her confidence.{/i}"
    pov "How about you come here and tell me face to face, instead of standing away like a coward!"
    mom "Hnng..."
    scene weekend 10pm 052cp
    mom "I can't believe you make me wear this."
    pov "It's a special underwear and you're a special one to wear it."
    mom "Special?"
    pov "Yes perfect as a appetizer for me."
    scene weekend 10pm 053cp
    pov "These parts with a different color giving the underwear it special style."
    pov "But they have another use too and you should use to wear them like that."
    mom "Huh? What do you mean?"
    scene weekend 10pm 054cp
    pov "They're removable!"
    mom "Huh?"
    pov "And now your special assets are fully focused on! See how tight the underwear is?"
    pov "Your tits are pushing like they want to get free. Now you're a real sexbomb!"
    scene weekend 10pm 055cp
    if inc == True:
        mom "This is so wrong. I'm your mother and you treat me like a sextoy."
    else:
        mom "This is so wrong. I'm your mothers best friend and you treat me like a sextoy."
    pov "That's the way this game is played. The bad boys need their hot sluts!"
    mom "What are you talking about!"
    if inc == True:
        pov "I choosed you to be my slut, mom!"
    else:
        pov "I choosed you to be my slut, [mother]!"
    mom "[pov]!"
    pov "I see you still don't get it why I choosed you! Especially YOU!"
    scene weekend 10pm 056cp
    if inc == True:
        pov "I choosed you because you're so strong and confident, mom!"
    else:
        pov "I choosed you because you're so strong and confident, [mother]!"
    mom "Huh?"
    pov "Another weaker woman would lost her mind and go crazy in this situation."
    pov "But you stayed yourself true over a year and I'm sure you can master this even longer."
    mom "But why we have to do sexual things?"
    scene weekend 10pm 057cp
    pov "Why not? You enjoy this too."
    mom "Hah..."
    pov "See, your nipple is already hard."
    mom "Hnng... stop it."
    scene weekend 10pm 058cp
    pov "And this is a part of the gang that every member has his slut."
    mom "Hnn..."
    if inc == True:
        pov "And because I choosed you, you have to follow the rules and be my slut, mom!"
    else:
        pov "And because I choosed you, you have to follow the rules and be my slut, [mother]!"
    pov "And I'm fully aware that your body sometines betrays you and enjoy the \"forbidden\" thing."
    mom "But..."
    scene weekend 10pm 059cp
    pov "I bet when I touch your pussy now, it'll be wet."
    mom "No, don't..."
    scene weekend 10pm 060cp
    mom "Hnng..."
    pov "As I thought."
    if inc == True:
        pov "You're flooding, mom."
    else:
        pov "You're flooding, [mother]."
    mom "Hnn..."
    pov "So there is no need that you deny it any longer."
    scene weekend 10pm 061cp
    pov "I need your help with that."
    mom "Help...?"
    pov "I need a strong woman standing with me. We need to solve this situation together."
    pov "I'm sure you already noticed that this is too much for Bruce. He can't handle this stuff."
    pov "But I can and I will. And with your help this will be over much sooner."
    pov "And I can be a little happy when I know that you can also enjoy it at least."
    mom "Hmm..."
    if inc == True:
        pov "Look at me, mom!"
    else:
        pov "Look at me, [mother]!"
    scene weekend 10pm 062cp
    pov "You're now my slut! Accept it!"
    mom "..."
    mom "But why you have to call me slut all the time?"
    pov "It's part of the gang-culture. Women are mostly sluts. And this way you'll get used to it faster."
    mom "Hmm..."
    pov "You need to say it!"
    mom "I... I'm your... slut..."
    pov "Good girl! I want you to lay yourself on that table now and get ready for me."
    mom "Ready?"
    pov "You know what we have to do now!"
    pov "Sooner or later we have to take this step to seem serious. When we do it now, it'll get easier."
    mom "..."
    pov "And I need a proof that my slut submit to me."
    pov "I'm hard as a rock and you're flooding wet, so we can have a good fuck together."
    if inc == True:
        pov "Show me that I made the right decision choosing you as my slut, mom."
    else:
        pov "Show me that I made the right decision choosing you as my slut, [mother]."
    mom "I... I'll get ready for you..."
    "She move to the table."
    scene weekend 10pm 065cp
    pov "{i}Wow. This was hard work but it succeeded.{/i}"
    pov "{i}I told her a story how much I need her help to solve this and now she's convinced that she's doing it for our mission.{/i}"
    pov "{i}Soon she'll accept everything. And on her way she'll lower her defences, because of her thinking it's needed.{/i}"
    pov "{i}And then I can break her completly and make her my real slut. But I mustn't forget to train her good.{/i}"
    pov "{i}But now it's time to fuck her and break one of her last taboos. And she's so wet she'll enjoy it.{/i}"
    scene weekend 10pm 066cp
    pov "You make me so damn horny, laying like that in front of me."
    pov "I can't wait to feel your wet, hot pussy on my dick, slut."
    pov "You'll get the best fuck of your life. I waited so long for this."
    scene weekend 10pm 067cp
    mom "Hnn..."
    pov "You can feel my hard dick rubbing on the entrance to your pussy?"
    mom "Y... yes..."
    pov "I want you to call me by my name."
    pov "We'll break now this taboo and I need to know, if you giving yourself all in."
    if inc == True:
        pov "You'll have sex now with your son, mom."
    else:
        pov "You'll have sex now with the son of your best friend, [mother]."
    scene weekend 10pm 068cp
    mom "I... can't. This is too much."
    pov "As I talked with you before I got the impression, that you understood my arguments."
    pov "When you want to be my slut, you have to obey me in all possibilities!"
    mom "Hnng..."
    pov "I can't fuck you when you won't give in."
    mom "Hnng... please fuck me, [pov]."
    if inc == True:
        pov "When you ask me so nice, I'll fuck you as hard as I can, mom."
        pov "{i}I can't believe it. I can fuck my mom and she even asked me to do it.{/i}"
    else:
        pov "When you ask me so nice, I'll fuck you as hard as I can, [mother]."
        pov "{i}I can't believe it. I can fuck [mother] and she even asked me to do it.{/i}"
    scene weekend 10pm 069cp
    pov "You're more then ready for my dick."
    mom "Hmm..."
    scene weekend 10pm 070cp
    "You stick your dick deeper inside."
    mom "Hah... hnn..."
    pov "I can slide so easy, because of your wetness, slut!"
    pov "Maybe I found the perfekt pussy? It's clinging on me, waiting to get fucked properly."
    mom "Hnn... hah..."
    if inc == True:
        pov "You want me to fuck you properly now, mom?"
    else:
        pov "You want me to fuck you properly now, [mother]?"
    pov "{i}Humiliating her like that could be also part of her future training.{/i}"
    mom "Yes, please fuck me properly [pov]!"
    scene weekend 10pm 071cp
    pov "See, it's about to get easier."
    mom "Hnng... hnn..."
    pov "And you can finally enjoy the pleasure when I'm fucking you!"
    mom "Hnn... hnn..."
    scene weekend 10pm 072cp
    mom "Haah...!"
    pov "Almost all inside you! And your pussy loves my dick!"
    "You start to fuck her wildly."
    scene weekend 10pm 073cp
    mom "Hah... hah... hah..."
    pov "Yes, let yourself go. Enjoy it and cum with me, slut!"
    mom "Hah... [pov]... slow down..."
    pov "No I can't and I won't."
    scene weekend 10pm 074cp
    "You go even wilder!"
    mom "Hah... hah... not so rough..."
    if inc == True:
        pov "I can feel you shaking, you're close, mom."
    else:
        pov "I can feel you shaking, you're close, [mother]."
    pov "You can't await to cum from my dick!"
    mom "Hah... Hnng..."
    pov "I'm about to cum too. You're a very good fuck, slut!"
    call screen nicoleweekendcorcum

screen nicoleweekendcorcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1329 ypos 179 action (Hide ('nicoleweekendcorcum'), Jump('nicoleweekendcorcuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1572 ypos 179 action (Hide ('nicoleweekendcorcum'), Jump('nicoleweekendcorcumoutside')) hovered tt.Action ("Cum outside") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicoleweekendcorcuminside:
    $ nicoleweekendcorinside = True
    jump nicoleweekendcorcumoutside

label nicoleweekendcorcumoutside:
    scene weekend 10pm 076cp
    mom "HAAAAHH... AAAAHHH..."
    pov "Yes, cum for me slut!"
    pov "{i}She's still to ashamed to show me how she's cumming.{/i}"
    pov "{i}But I can feel her body shaking.{/i}"
    if nicoleweekendcorinside == True:
        if inc == True:
            pov "I'll cum too, deep in your pussy. I want you to feel my hot sperm inside you, mom!"
        else:
            pov "I'll cum too, deep in your pussy. I want you to feel my hot sperm inside you, [mother]!"
    else:
        pov "I'll cum too, [mother]!"
    pov "HNNNG...!"
    if nicoleweekendcorinside == True:
        scene weekend 10pm 077cpi
        pov "I'll released so much inside you. What a wonderful view."
        mom "Hah...hnng..."
    else:
        scene weekend 10pm 077cpo
        pov "I came so much on you. What a wonderful view."
        mom "Hah... hnng..."
    scene weekend 10pm 078cp
    if inc == True:
        pov "Don't give me such a sad face, mom!"
    else:
        pov "Don't give me such a sad face, [mother]!"
    pov "We enjoyed the sex like other adults would do too."
    pov "And you also had the confidence to break that taboo."
    mom "Hnng..."
    if nicoleweekendcorinside == True:
        scene weekend 10pm 079cpi
        mom "I can't believe I did that. And you even came inside me."
        pov "Yes I did. And it was the best decision I ever made!"
    else:
        scene weekend 10pm 079cpo
        mom "I can't believe I did that. And you even came all over me."
        pov "Yes I did. And it was the best decision I ever made!"
    pov "Where do you think you're going, slut!"
    scene weekend 10pm 080cp
    "You attack her from behind and shove your dick back in her pussy."
    mom "AAAAHHH... What are you doing...?"
    pov "We're not done yet. We have all night."
    if inc == True:
        pov "I'll fuck you until my dick fell off, mom!"
    else:
        pov "I'll fuck you until my dick fell off, [mother]!"
    scene weekend 10pm 081cp
    mom "Hah... hah... hnn..."
    "You continue to fuck her."
    pov "I'll fuck you all night! So you can get a proper training, slut!"
    scene weekend 10pm 082cp
    "You do what you promised her. You two fuck all night."
    mom "Hah... hah... yes!"
    pov "{i}She's even riding on herself now. She got so horny!{/i}"
    scene weekend 10pm 083cp
    mom "AAH... AAH... I'm cumming again, [pov]!"
    scene weekend 10pm 084cp
    mom "More, fuck me more. I need your dick [pov]!"
    pov "As you wish, slut!"
    scene weekend 10pm 085cp
    "You fucked together all night until [mother] collapsed."
    "Then you decide to let her sleep, because she was a good slut and endured it all night."
    pov "{i}You'll become the perfect slut and we can stay our whole lives together.{/i}"
    scene black
    "At damn you go back to your room and sleep there too."
    $ nicoleweekendcorinside = False
    $ weekendactivities += 1
    $ mombasementcorsecond = True
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose


label nicoleweekendlove:
    $ momlove += 1
    hide screen locations
    scene black
    "You got a call from [mother] that she want to eat dinner at home, so you decide to spend time with her."
    if inc == True:
        "After you cooked dinner for your mom and yourself, you wait for her."
    else:
        "After you cooked dinner for [mother] and yourself, you wait for her."
    "You hear the front door open."
    scene weekend 8pm 001
    mom "Hey [pov], I'm back."
    mom "Did you make a dinner?"
    scene weekend 8pm 002
    mom "Oh? What a nice surprise!"
    if inc == True:
        pov "Welcome back, mom."
    else:
        pov "Welcome back, [mother]."
    mom "And a lovely decoration too."
    scene weekend 8pm 003
    mom "I'm happy you did this for me."
    pov "Yes let's eat and then we can spend the evening together."
    mom "So you have already something in mind?"
    if inc == True:
        pov "I'm not sure, I just want to spend some time with my lovely mom."
    else:
        pov "I'm not sure, I just want to spend some time with you, lovely [mother]."
    scene weekend 8pm 004l
    mom "You're such a charmer!"
    mom "I'm so happy that I can spend my weekend time with such a gentleman."
    if gangmember == True:
        mom "And you stay all that nice, even when you're a gangmember now."
    pov "Yes..."
    if inc == True:
        mom "Come here son."
    else:
        mom "Come here [pov]."
    scene weekend 8pm 005l
    mom "Hugging is something I missed so much in this family."
    if inc == True:
        pov "Haha, we can stay forever like this, mom."
    else:
        pov "Haha, we can stay forever like this, [mother]."
    mom "I'd love that, but I'm also hungry, haha."
    scene weekend 8pm 006l
    mom "So let's eat."
    pov "OK."
    mom "I want to taste your lovely meat now."
    pov "{i}Oh shit. That sound like something else.{/i}"
    scene weekend 8pm 007l
    mom "When I eat such a heavy meal I should do a good work out after."
    pov "{i}Oh I would love to make a good work out together with you. Naked. In bed.{/i}"
    mom "But you made it, so I want to spend the evening with you. Maybe we watch TV after?"
    pov "{i}Oh... Damn it.{/i}"
    pov "Of course. Or we find something else."
    scene weekend 8pm 008l
    pov "{i}We're all alone this time and I'm so horny. Seeing her fine boobs.{/i}"
    mom "Yes, maybe we can do something else."
    pov "{i}And this huge cleavage. Is she teasing me?{/i}"
    mom "[pov]!"
    scene weekend 8pm 009l
    pov "Huh?"
    mom "I see you're distracted, haha. So you have other ideas what we should do?"
    pov "Oh?... I... I didn't it on purpose, I just..."
    mom "Shhh... Sometimes each gentleman fail <giggle>"
    pov "{i}She's really teasing me...{/i}"
    mom "You'll never finish eating when you stare all the time at me."
    scene weekend 8pm 010l
    mom "So let's just eat, you have much more time after that staring at me."
    pov "{i}Stop teasing me like that. How should I survive this?{/i}"
    "You literally wolf down your meal."
    scene weekend 8pm 011l
    mom "I'll change in something more comfortable. I'll be back in a few minutes."
    pov "OK. I'll wait of course."
    scene weekend 8pm 011
    pov "{i}I can't wait... She teased me all the time. Did she do it on purpose?{/i}"
    pov "{i}I want to be together with her now. Naked. In bed. Sweating together and do a special work out.{/i}"
    pov "{i}Fuck it! I need to see her now!{/i}"
    "You go to her room."
    scene weekend 8pm 012lb
    mom "I knew you can't wait until I'm done."
    pov "{i}Bad timing...{/i}"
    pov "I... forgot to knock... sorry."
    mom "You're such a bad liar..."
    mom "You undressed me at dinner all the time and no you can't stand it anymore."
    pov "{i}So she teased me on purpose. Knowing exactly how to press my buttons.{/i}"
    scene weekend 8pm 013lb
    mom "No one would put such an effort in preparing dinner like this and beeing a gentleman all the time..."
    mom "when he wouldn't be up to something."
    if inc == True:
        mom "And you're up to seeing your mother naked. Or even more."
        mom "The forbidden fruit."
    else:
        mom "And you're up to seeing me naked. Or even more."
    pov "<gulp>"
    mom "A gentleman like you could choose the finest women, but you choose me..."
    if inc == True:
        mom "Your mother."
    else:
        mom "An older woman."
    scene weekend 8pm 014lb
    pov "Yes. You're right. I choosed you."
    if inc == True:
        pov "And I think I'm falling in love with you, mom!"
    else:
        pov "And I think I'm falling in love with you, [mother]!"
    mom "You're so honest with me, so I'll be honest with you too."
    mom "You changed so much in even one year and still withstand all the bad influence in this new situation."
    if inc == True:
        mom "I'm also very interested in my \"new\" son."
        mom "Even if a mother and son shouldn't share such interests. But I've already tasted the forbidden fruit."
    else:
        mom "I'm also very interested in the son of my best friend."
        mom "Even if I shouldn't share such interests with you. But I've already tasted the forbidden fruit."
    pov "Wow..."
    scene weekend 8pm 016lb
    mom "What are you waiting for?"
    pov "Huh? Is this really happening?"
    mom "I bet you already have fantasies about me. Now show me them too."
    "You undress in a few seconds."
    mom "<giggle>"
    jump nicoleweekendloveroot

label nicoleweekendloveroot:
    scene weekend 8pm 016lb
    call screen nicoleweekendlovechoose

screen nicoleweekendlovechoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 1832 ypos 245 action (Hide ('nicoleweekendlovechoose'), Jump('nicolelovehead')) hovered tt.Action ("Kiss her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" xpos 1832 ypos 315 action (Hide ('nicoleweekendlovechoose'), Jump('nicoleloveboobs')) hovered tt.Action ("Choose her boobs") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1832 ypos 385 action (Hide ('nicoleweekendlovechoose'), Jump('nicolelovehands')) hovered tt.Action ("Ask for a handjob") focus_mask True
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 1832 ypos 457 action (Hide ('nicoleweekendlovechoose'), Jump('nicolelovebelly')) hovered tt.Action ("Kiss her belly") focus_mask True
        imagebutton auto "gui/icons/icon_pussy_%s.png" xpos 1832 ypos 529 action (Hide ('nicoleweekendlovechoose'), Jump('nicolelovepussy')) hovered tt.Action ("Choose her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" xpos 1832 ypos 602 action (Hide ('nicoleweekendlovechoose'), Jump('nicolelovefeet')) hovered tt.Action ("Choose her feet") focus_mask True
        imagebutton auto "gui/icons/icon_cowgirl_%s.png" xpos 1832 ypos 672 action (Hide ('nicoleweekendlovechoose'), Jump('nicolelovecow')) hovered tt.Action ("Let her go on top") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1832 ypos 749 action (Hide ('nicoleweekendlovechoose'), Jump('nicolelovestop')) hovered tt.Action ("Finish") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicolelovehead:
    pov "Your sweet mouth need some kisses now!"
    mom "Hm... I'm excited."
    scene weekend 8pm 024lb
    pov "Hm... <kiss>"
    "You two french kiss."
    mom "Hnng... <kiss>"
    if inc == True:
        pov "I want to taste you forever, mom."
    else:
        pov "I want to taste you forever, [mother]."
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    scene weekend 8pm 025lb
    pov "<kiss> <lick>"
    mom "Hmm... this spot. It feels so good."
    pov "I love to kiss your soft skin."
    mom "Hmm..."
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicoleloveboobs:
    call screen nicoleweekendloveboobschoose

screen nicoleweekendloveboobschoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 1635 ypos 246 action (Hide ('nicoleweekendloveboobschoose'), Jump('nicolelovekissboobs')) hovered tt.Action ("Kiss her boobs") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" xpos 1635 ypos 398 action (Hide ('nicoleweekendloveboobschoose'), Jump('nicoleloveboobjob')) hovered tt.Action ("Ask for a boobjob") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicolelovekissboobs:
    pov "I need to kiss your boobs now!"
    mom "<giggle> Then go on."
    scene weekend 8pm 026lb
    pov "<kiss> <suck>"
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    mom "Oh, slowly baby boy <giggle>."
    pov "I love to suck them so much."
    if inc == True:
        mom "You suck them so greedy. Like you did as a baby."
        pov "Oh mom! This make me so horny."
    else:
        mom "You suck them so greedy. Like you're a baby."
        pov "Oh [mother]! This make me so horny."
    mom "Hmm..."
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicoleloveboobjob:
    pov "I would love to feel your boobs... on my..."
    mom "Oh, you want a boobjob from me?"
    pov "Y... yes. Can I have one?"
    mom "<giggle> You're so attracted to them. Lay down."
    scene weekend 8pm 050la
    mom "I love to see how I can attract you. Standing all stiff."
    pov "It'll never soften when I'm in bed with you!"
    mom "I hope so. You're so big and I want to please you too."
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    scene weekend 8pm 051lb
    pov "Ohh... So soft."
    mom "And your shaft is burning. Now you can enjoy your staring."
    pov "Oh I will. Getting a boob job from you is the best."
    scene weekend 8pm 052lb
    mom "Then I'll put much more effort in it. <giggle>"
    pov "Oh yes, this is like heaven."
    mom "You're such a good boy, you earned this."
    if inc == True:
        pov "Oh mom. Your boobs feel so good."
    else:
        pov "Oh [mother]. Your boobs feel so good."
    scene weekend 8pm 053lb
    mom "Then I'll please you even more."
    pov "Ohh... Hmm... hah..."
    mom "You're shaking. Is it so good that you're about to cum now?"
    pov "Yes... yes, it's so damn good."
    mom "Then give it to me. Cum over my boobs."
    if inc == True:
        mom "Show your mommy how much you love her!"
    else:
        mom "Show me how much you love me!"
    pov "Oh my god!"
    scene weekend 8pm 054lb
    pov "Aaaahhh...!"
    mom "I can feel it! So burning hot."
    pov "Hnng..."
    scene weekend 8pm 055lb
    mom "You gave me so much. I'm glad you liked my doing."
    pov "Oh... it was so great..."
    mom "So, do you want to have more fun or is my baby boy done? <giggle>"
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovehands:
    pov "I would love to feel your hands... on my..."
    mom "Oh, you want a handjob from me?"
    pov "Y... yes. Can I have one?"
    mom "<giggle> Yes. Lay down."
    scene weekend 8pm 050la
    mom "I love to see how I can attract you. Standing all stiff."
    pov "It'll never soften when I'm in bed with you!"
    mom "I hope so. You're so big and I want to please you too."
    scene weekend 8pm 051la
    pov "Ohh... So soft."
    mom "And your shaft is burning. Now you can enjoy your staring."
    pov "Oh I will. Your hands feel so good and how you play with my balls."
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    scene weekend 8pm 052la
    mom "Then I'll put much more effort in it. <giggle>"
    pov "Oh yes, this is like heaven."
    mom "You're such a good boy, you earned this."
    if inc == True:
        pov "Oh mom. Your hands feel so good."
    else:
        pov "Oh [mother]. Your hands feel so good."
    scene weekend 8pm 053la
    mom "Then I'll please you even more."
    pov "Ohh... Hmm... hah..."
    mom "You're shaking. Is it so good that you're about to cum now?"
    pov "Yes... yes, it's so damn good."
    mom "Then give it to me. Just cum on me."
    if inc == True:
        mom "Show your mommy how much you love her!"
    else:
        mom "Show me how much you love me!"
    pov "Oh my god!"
    scene weekend 8pm 055la
    pov "Aaaahhh...!"
    mom "I can feel it! So burning hot."
    pov "Hnng..."
    scene weekend 8pm 056la
    mom "You gave me so much. I'm glad you liked my doing."
    pov "Oh... it was so great..."
    mom "So, do you want to have more fun or is my baby boy done? <giggle>"
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovebelly:
    pov "I need to kiss your belly!"
    mom "Hm... I'm excited."
    scene weekend 8pm 027lb
    pov "Hm... <kiss>"
    mom "Hnng... it tickles."
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    if inc == True:
        pov "I want to taste you forever, mom."
    else:
        pov "I want to taste you forever, [mother]."
    mom "Hmm... this spot. It feels so good."
    pov "I love to kiss your soft skin."
    mom "Hmm..."
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovepussy:
    pov "Your lovely pussy needs my attention."
    mom "<giggle> It's also waiting for you."
    scene weekend 8pm 017lb
    if inc == True:
        pov "Your pussy is so beautiful, mom."
    else:
        pov "Your pussy is so beautiful, [mother]."
    mom "And all your charming made it all wet."
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    pov "Then I'll take good care of it."
    call screen nicoleweekendlovepussychoose

screen nicoleweekendlovepussychoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 1635 ypos 246 action (Hide ('nicoleweekendlovepussychoose'), Jump('nicolelovelickpussy')) hovered tt.Action ("Lick her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_pussy_%s.png" xpos 1635 ypos 398 action (Hide ('nicoleweekendlovepussychoose'), Jump('nicolelovefuckpussy')) hovered tt.Action ("Fuck her pussy") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicolelovelickpussy:
    pov "I'll please you with my tongue now until you sscream my name!"
    mom "Oh, I'm very excited now."
    scene weekend 8pm 018lb
    pov "Hmm... <lick>"
    mom "Hmm... So good. I need that!"
    scene weekend 8pm 019lb
    pov "You're really enjoying it. Just ask for it and I'll lick you everytime."
    mom "Hmm... that's a tempting offer."
    if inc == True:
        pov "You taste so good, mom."
    else:
        pov "You taste so good, [mother]."
    pov "And you're so wet."
    mom "Hmm..."
    "You bite her clit gently."
    scene weekend 8pm 020lb
    mom "Hah! This felt amazing."
    pov "So I found your weak spot?"
    mom "Yes, please do it more."
    pov "As you wish, my queen."
    mom "<giggle> Hah..."
    scene weekend 8pm 021lb
    "She push your head closer to her pussy."
    pov "So it's so good that you're going close? <bite>"
    mom "Hah, yes... You're doing very good."
    pov "Don't forget to scream my name when you cum, haha."
    mom "I'll do everything, just continue... I'm so close..."
    scene weekend 8pm 022lb
    mom "Oh... hah... hah..."
    mom "AAAAHHH... HAAAH..."
    mom "<screaming> [pov]! YES! [pov]!"
    mom "Hnnn... hnn..."
    pov "{i}Good, she came and screamed.{/i}"
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovefuckpussy:
    pov "I need to fuck with you so badly."
    mom "Then do it [pov]. I want to feel you also in me."
    pov "A dream come true."
    scene weekend 8pm 040la
    mom "Hah, all in. Like a wild animal!"
    pov "I need this so badly. And you're so wet that I could drove all in."
    mom "You're burning in me and it feels so good."
    if inc == True:
        pov "I had to leave you when I was born and now I'm back inside you."
    else:
        pov "I had to leave a pussy when I was born and now I'm conquering yours."
    scene weekend 8pm 041la
    mom "You're such a naughty boy."
    mom "And this forbidden love turns me so on."
    pov "Then we need to do it more often!"
    if inc == True:
        mom "Please love me harder, son!"
    else:
        mom "Please love me harder, [pov]!"
    pov "I will!"
    scene weekend 8pm 042la
    mom "Hah... hah... I'm getting close..."
    mom "You do it so good, you'll make me cum!"
    if inc == True:
        pov "I'm close too. Let's cum together, mom."
    else:
        pov "I'm close too. Let's cum together, [mother]."
    pov "Let's share my dream by cumming together when we're fucking."
    mom "Hah... hah, [pov]!"
    call screen nicoleweekendlovemissionarycum

screen nicoleweekendlovemissionarycum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 668 ypos 836 action (Hide ('nicoleweekendlovemissionarycum'), Jump('nicolelovemissionaryinside')) hovered tt.Action ("Cum inside") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 908 ypos 836 action (Hide ('nicoleweekendlovemissionarycum'), Jump('nicolelovemissionaryoutside')) hovered tt.Action ("Cum outside") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicolelovemissionaryinside:
    scene weekend 8pm 043lai
    $ nicoleweekendinside = True
    mom "AAAHHH... I'm cumming..."
    pov "Me too! Hnng... feel my sperm!"
    mom "I can feel it. It's so hot."
    scene weekend 8pm 044lai
    mom "Hah... hah... so much is inside me..."
    pov "Hah... as I want to. Giving you all I had."
    mom "You released so much... I thought it would never stop."
    pov "{i}She's so confused. Did I go to far?{/i}"
    mom "Hah... do you want to stop or continue?"
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovemissionaryoutside:
    scene weekend 8pm 043lao
    mom "AAAHHH... I'm cumming..."
    pov "Me too! Hnng... feel my sperm!"
    mom "I can feel it. It's so hot."
    scene weekend 8pm 044lao
    mom "Hah... hah... so much over me..."
    pov "Hah... as I want to. Giving you all I had."
    mom "You released so much... I thought it would never stop."
    pov "I'm glad you liked it."
    mom "Hah... do you want to stop or continue?"
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovefeet:
    call screen nicoleweekendlovefeetchoose

screen nicoleweekendlovefeetchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 1635 ypos 246 action (Hide ('nicoleweekendlovefeetchoose'), Jump('nicolelovekissfeet')) hovered tt.Action ("Kiss her feet") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" xpos 1635 ypos 398 action (Hide ('nicoleweekendlovefeetchoose'), Jump('nicolelovefeetjob')) hovered tt.Action ("Ask for a feetjob") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicolelovekissfeet:
    pov "I want to kiss your feet."
    mom "My feet?"
    pov "Yes they're so beautiful."
    scene weekend 8pm 030l
    "You suck her big toe."
    pov "<suck>"
    mom "Oh... this feels good."
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    scene weekend 8pm 030la
    mom "Hmm... I thought it would tickle, but it's just wonderful."
    pov "<suck>"
    mom "You love sucking on me, don't you?"
    scene weekend 8pm 030lb
    pov "Yes, I love every part of your body."
    if inc == True:
        pov "And you're very lick- and kissable, mom."
    else:
        pov "And you're very lick- and kissable, [mother]."
    mom "Hmm... Then I'm glad I have you."
    scene weekend 8pm 031l
    mom "Hnn... and it's even arousing."
    pov "Your feet are so beautiful, like every other part of your body."
    pov "<lick> <kiss>"
    mom "Hmm..."
    scene weekend 8pm 031la
    pov "I'm the first one who give you pleasure like this?"
    mom "Yes... hmm... and I love it."
    pov "Then you have the proof that I love you the most."
    mom "Yes, love my feet more [pov]."
    scene weekend 8pm 031lb
    mom "This was so exciting. New for me, but very good."
    pov "I'm glad you liked it. I loved it too."
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovefeetjob:
    pov "I would love to feel your feet... on my..."
    mom "Oh, you want me to get you off with my feet?"
    pov "Y... yes. Can you do that?"
    mom "<giggle> Yes, I'll try."
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    scene weekend 8pm 032l
    mom "Oh, your penis is so hot."
    pov "And your beautiful feet are feeling fantastic on it."
    mom "It's feeling weird that my feet getting this attention."
    scene weekend 8pm 032la
    pov "I love them like every other part of your body."
    pov "And they're feeling so good on my dick."
    scene weekend 8pm 032lb
    mom "Then they'll give you the best experience. <giggle>"
    pov "I know they will. Because they're yours."
    mom "I bet you stop your charming when they make you cum! Haha..."
    scene weekend 8pm 033l
    pov "Yes, good. Do it as you would do it with your hands."
    mom "It's easier as I thought. And a exciting feeling, your pulsating shaft."
    pov "You're doing perfect."
    scene weekend 8pm 033la
    pov "And the sexy view, seeing your beautiful feet working on my dick."
    mom "Then I'm happy that I can please you this way."
    scene weekend 8pm 033lb
    mom "Oh, your penis is shaking. Are you really about to cum from my feet?"
    if inc == True:
        pov "Yes, mom! I always wanted to play with your feet this way."
    else:
        pov "Yes, [mother]! I always wanted to play with your feet this way."
    mom "Then cum for me and my feet."
    scene weekend 8pm 034l
    pov "Yes hold them like that. I want to cum all over them."
    mom "Then plaster my feet with your sperm, [pov]."
    pov "I'm so close..."
    scene weekend 8pm 035l
    pov "Hnng..."
    mom "Yes, cum for me..."
    scene weekend 8pm 036lb
    mom "So much came out and it's burning on my feet."
    pov "What a beautiful view. We need to do this much more often."
    scene weekend 8pm 034lb
    mom "When it pleases you so much, I'll train to give you even more pleasure."
    pov "I'd love that. I came so hard."
    mom "<giggle>"
    scene weekend 8pm 036la
    mom "So, do you want to have more fun or is my baby boy done? <giggle>"
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovecow:
    pov "I want to have sex with you."
    mom "Then go on. <giggle>"
    pov "Can you... ride on me..?"
    mom "I...? Oh, you want to give me the control. That's nice."
    mom "Lay down."
    scene weekend 8pm 060la
    pov "Ohh..."
    mom "Good that you're already so stiff."
    if inc == True:
        pov "I appreciate that you like my dick all stiff, mom."
    else:
        pov "I appreciate that you like my dick all stiff, [mother]."
    mom "Haha, it's just better for this posititon."
    pov "I'm so excited, please stop teasing me."
    scene weekend 8pm 061la
    mom "Then I'll slinding it inside me, slowly and gentle."
    pov "Oh, I can feel your pussy, so warm and wet."
    mom "And you're burning inside me."
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    scene weekend 8pm 061lb
    pov "{i}This wonderful view. My dick in her pussy.{/i}"
    mom "I'll take it deeper now."
    scene weekend 8pm 062la
    mom "Slowly."
    pov "Ha, what are you doing?"
    mom "Taking it slowly in."
    pov "Your boobs are to big. I can barely see your face."
    mom "Even that is a copliment."
    scene weekend 8pm 063la
    mom "You're almost all inside me. You're so big and hot."
    pov "And you're reaction is so sexy when you're taking me all in."
    mom "Hah... Ahhh... it's all in!"
    scene weekend 8pm 063lb
    pov "I'm balls deep in your pussy. It feels so good."
    mom "Hah, you're so big and hard."
    pov "I can't wait any longer."
    if inc == True:
        pov "Please ride me good, mom!"
    else:
        pov "Please ride me good, [mother]!"
    scene weekend 8pm 064lb
    mom "Oh, hah... hah..."
    pov "Yes this is amazing!"
    mom "You're to big! I won't endure it much long. You're hitting my best spots."
    pov "Then enjoy yourself and cum when you need to. Your cumming will give me the rest too."
    scene weekend 8pm 064la
    mom "Hah... so you'll cum with me...?"
    if inc == True:
        pov "Yes, mom. Let's share our orgasms."
    else:
        pov "Yes, [mother]. Let's share our orgasms."
    mom "I'm so close... hah... hah..."
    pov "Then cum with me!"
    mom "HAAAHH... AAAAHHH...!"
    "You're about to cum too."
    $ alexissuspicous += 1
    call screen nicoleweekendlovecowcum

screen nicoleweekendlovecowcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 228 action (Hide ('nicoleweekendlovecowcum'), Jump('nicolelovecowinside')) hovered tt.Action ("Cum inside") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 405 action (Hide ('nicoleweekendlovecowcum'), Jump('nicolelovecowoutside')) hovered tt.Action ("Cum outside") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicolelovecowinside:
    scene weekend 8pm 065lbi
    $ nicoleweekendinside = True
    mom "AAAHHH... I'm cumming..."
    pov "Me too! Hnng... feel my sperm!"
    mom "I can feel it. It's so hot."
    scene weekend 8pm 065lai
    mom "Hah... hah... so much is inside me..."
    pov "Hah... as I want to. Giving you all I had."
    mom "You released so much... I thought it would never stop."
    pov "{i}She's so confused. Did I go to far?{/i}"
    mom "Hah... do you want to stop or continue?"
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovecowoutside:
    scene weekend 8pm 065lbo
    mom "AAAHHH... I'm cumming..."
    pov "Me too! Hnng... feel my sperm!"
    mom "I can feel it. It's so hot."
    scene weekend 8pm 065lao
    mom "Hah... hah... so much over me..."
    pov "Hah... as I want to. Giving you all I had."
    mom "You released so much... I thought it would never stop."
    pov "I'm glad you liked it."
    mom "Hah... do you want to stop or continue?"
    $ alexissuspicous += 1
    jump nicoleweekendloveroot

label nicolelovestop:
    pov "I'm so done. Let's stop here."
    mom "OK. As you wish. <giggle>"
    mom "Come, lay with me."
    if nicoleweekendinside == True:
        scene weekend 8pm 045lai
        pov "Is something wrong?"
        mom "When you came inside me I could feel that you changed."
        pov "I changed? What do you mean?"
        mom "You pushed your sperm out like you have to give me all you have."
        mom "Like when you give me more sperm, it would overpower the anti baby pill."
        mom "Like you want to make sure that you impregnate me..."
        call screen nicoleweekendlovepreg
    else:
        scene weekend 8pm 045lao
        mom "That was so much fun."
        pov "I'm glad you liked it too. I can't wait for our next time."
        mom "Yes, we need to do this again."
        jump nicoleweekendloveend

screen nicoleweekendlovepreg():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1475 ypos 284 action (Hide ('nicoleweekendlovepreg'), Jump('nicolelovepregyes')) hovered tt.Action ("I want to impregnate her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1631 ypos 284 action (Hide ('nicoleweekendlovepreg'), Jump('nicolelovepregno')) hovered tt.Action ("I don't want to impregnate her") focus_mask True


    frame:
        xalign .5
        text tt.value


label nicolelovepregyes:
    pov "You caught me."
    if inc == True:
        pov "I'd love to have a baby with you, mom!"
        mom "But... you're my son..."
        pov "I don't care! I want to improve our family with you, as mother of my childs."
    else:
        pov "I'd love to have a baby with you, [mother]!"
        mom "But..."
        pov "I don't care! I want to have a family with you, as mother of my childs."
    mom "Hmm..."
    pov "{i}Was that a agreeing \"hmm\" or a denying one? Or maybe she needs some time to think about it.{/i}"
    $ nicolebabywant = True
    jump nicoleweekendloveend

label nicolelovepregno:
    pov "No. You're mistaken there. I just want to give you all I had."
    mom "Oh, good."
    pov "{i}Is she disappointed?{/i}"
    jump nicoleweekendloveend

label nicoleweekendloveend:
    if proom19lovesex == True:
        jump proom19extloveend
    scene weekend 8pm 046l
    $ nicoleweekendinside = False
    mom "Let's sleep."
    if inc == True:
        pov "Sweet dreams, mom."
    else:
        pov "Sweet dreams, [mother]."
    mom "You too."
    scene black
    "You spend the night together."
    $ weekendactivities += 1
    $ mombasementlovesecond = True
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose




label adate1:
    hide screen locations
    scene black
    $ adate = True
    $ lilsisrelationship += 1
    if inc == True:
        "You go on a date with your little sister."
    else:
        "You go on a date with [ls]."
    scene date 1pm 001
    pov "I let you choose our picnic location as you wanted. But where are we?"
    ls "That's a barn. There's normally horses in it, dummy."
    pov "I know what this it. But who owns it and why did you choose this place?"
    ls "Less talking, more following <giggle>"
    scene date 1pm 002
    pov "Oh wow, surprise! It's a barn!"
    ls "Haha, you got it dummy!"
    pov "Can you know answer my questions?"
    ls "Haha sure. The owner is Jeremy, he's our neighbor."
    pov "And where are the horses?"
    ls "He doesn't own any. He wanted to buy some but I think he forgot about this place."
    pov "Forgot his own barn?"
    ls "He spent some time in a war and since he has some brain damage <giggle>"
    pov "Hey, this isn't funny."
    ls "Then you don't know him. He doesn't take things so serious because he's rich. A funny old man."
    pov "Oh, ok."
    scene date 1pm 002a
    ls "Now follow me again. Up here is the perfect place."
    pov "Yeah, sure."
    scene date 1pm 003a
    pov "{i}Holy...{/i}"
    ls "You still didn't tell me if you like it here?"
    pov "Oh yeah, the view is awesome! And so beautiful!"
    ls "Yes, I know. That's why I choose it."
    scene date 1pm 004a
    pov "{i}Damn, I wonder if she is showing herself to me on purpose?{/i}"
    pov "{i}She must have know that climbing up a ladder before me and wearing a skirt woouuld give me a good view.{/i}"
    pov "{i}Or is she just naive?{/i}"
    scene date 1pm 005a
    ls "Dummy? Dummy!"
    pov "Huh?"
    ls "Stop sleeping. Come here up to me."
    pov "Oh... yes sure."
    scene date 1pm 007a
    ls "Isn't it a nice little place up here?"
    pov "Yes a good choice [ls]."
    ls "Haha, I know."
    scene date 1pm 006a
    pov "{i}And so much space. I wonder if that guy really forgot about his barn?{/i}"
    ls "Lalala..."
    pov "{i}Ha, she has her fun.{/i}"
    jump adate1eat



label adate1search:
    scene date 1pm 007a
    ls "Want to play something?"
    pov "Yeah, why not?"
    pov "{i}I wonder what she's up to?{/i}"
    ls "I hide, you have to find me. But give your best, it won't be easy dummy!"
    pov "So hide and seek?"
    ls "Yes, I hide first! You have to wait here two minutes. And no cheating!"
    pov "I don't need that to win, haha."
    ls "Winning, you? <giggle>"
    scene black
    "You wait around two minutes."
    pov "{i}Ha what a stupid game. She's not as grown up she wants to be.{/i}"
    pov "{i}But she should have her fun. I like her so happy.{/i}"
    pov "{i}So, where to start?{/i}"
    jump adate1way

label adate1way:
    if adatehide >= 3 and lilsiscorruption > lilsislove:
        scene date 1pm 005
        pov "{i}There she is.{/i}"
        jump adate1cor
    elif adatehide >= 3 and lilsislove >= lilsiscorruption:
        scene date 1pm 001f
        pov "{i}I can't find her...{/i}"
        jump adate1love
    else:
        scene date 1pm 001f
        call screen adate1way1

screen adate1way1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 826 ypos 240 action (Hide('adate1way1'), Jump('adate1stables')) hovered tt.Action ("Search in the stables") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 961 ypos 924 action (Hide('adate1way1'), Jump('adate1front')) hovered tt.Action ("Go outside at the front") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1151 ypos 232 action (Hide('adate1way1'), Jump('adate1back')) hovered tt.Action ("Go outside at the back") focus_mask True
        frame:
            xalign .5
            text tt.value

label adate1stables:
    scene date 1pm 002f
    $ adatehide += 1
    "You search in the stables for her."
    pov "{i}Not here.{/i}"
    scene date 1pm 002g
    pov "{i}Also empty. Let's go somewhere else.{/i}"
    jump adate1way

label adate1front:
    scene date 1pm 005f
    $ adatehide += 1
    pov "{i}Nothing. Where is she?{/i}"
    call screen adate1way2

screen adate1way2():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 401 ypos 525 action (Hide('adate1way2'), Jump('adate1left')) hovered tt.Action ("Go left") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1838 ypos 525 action (Hide('adate1way2'), Jump('adate1right')) hovered tt.Action ("Go right") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1130 ypos 525 action (Hide('adate1way2'), Jump('adate1way')) hovered tt.Action ("Go back in") focus_mask True
        frame:
            xalign .5
            text tt.value

label adate1right:
    scene date 1pm 003f
    $ adatehide += 1
    pov "{i}Nothing. And she isn't hiding in the grass either.{/i}"
    call screen adate1way3

screen adate1way3():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 339 ypos 423 action (Hide('adate1way3'), Jump('adate1front')) hovered tt.Action ("Go back to the front") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1228 ypos 423 action (Hide('adate1way3'), Jump('adate1back')) hovered tt.Action ("Go to the back") focus_mask True
        frame:
            xalign .5
            text tt.value

label adate1back:
    scene date 1pm 004f
    $ adatehide += 1
    pov "{i}Hm... Let's go back to the front.{/i}"
    jump adate1front

label adate1left:
    if NTR == True and davidemeet == False:
        scene date 1pm ntr02
        pov "{i}Oh...{/i}"
        jump adate1ntr
    else:
        scene date 1pm 003g
        $ adatehide += 1
        pov "..."
        call screen adate1way4

screen adate1way4():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1554 ypos 337 action (Hide('adate1way4'), Jump('adate1front')) hovered tt.Action ("Go back to the front") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 700 ypos 337 action (Hide('adate1way4'), Jump('adate1back')) hovered tt.Action ("Go to the back") focus_mask True
        frame:
            xalign .5
            text tt.value



label adate1love:
    ls "Hey dummy!"
    pov "Huh?"
    ls "Up here!"
    scene date 1pm 015a
    ls "I knew you wouldn't find me, haha."
    pov "{i}I should have known she would have cheated.{/i}"
    pov "..."
    if inc == True:
        ls "Oh, don't be sad, big brother. <giggle>"
    else:
        ls "Oh, don't be sad, [pov]. <giggle>"
    pov "I'm not..."
    scene date 1pm 016a
    ls "Au!"
    "[ls] hits her head on the roof."
    pov "Haha, dummy!"
    ls "Oh no!"
    scene date 1pm 017a
    pov "{i}Oh shit, she lost her balance.{/i}"
    ls "Aaaahhh..."
    if inc == True:
        pov "{i}Brace yourself, little sister incoming!{/i}"
    else:
        pov "{i}Brace yourself, little girl incoming!{/i}"
    scene date 1pm 018a
    ls "Ohh..."
    pov "{i}Ah, damn. That much pain!{/i}"
    "You managed to catch her somehow."
    scene date 1pm 019a
    if inc == True:
        ls "Aww... are you alright, big brother?"
    else:
        ls "Aww... are you alright, [pov]?"
    pov "{i}Don't let her know that I'm almost dead, ahh...{/i}"
    pov "Yes sure. No harm done. It was easy to catch you."
    scene date 1pm 020a
    ls "Yes! I knew it."
    if inc == True:
        ls "My big brother saved me!"
    else:
        ls "You saved me!"
    ls "I could have harmed myself bad but you're my hero now!"
    pov "Oh... ok."
    ls "Don't be so modest! I'm so proud right now!"
    scene date 1pm 021a
    ls "Muah!"
    pov "{i}Wow, what's happening?{/i}"
    "[ls] kisses you on the mouth."
    scene date 1pm 022a
    ls "Oh no! No!"
    pov "What?"
    pov "{i}Damn, do I smell bad?{/i}"
    scene date 1pm 023a
    ls "No! No! This can't be real!"
    pov "What's with you [ls]? Did I do something wrong?"
    ls "No, boohoo!"
    pov "Are you crying? Why?"
    call screen adate1lovevo

screen adate1lovevo:
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 618 ypos 938 action (Hide('adate1lovevo'), Jump('adate1lovelk')) hovered tt.Action ("Take a peek") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 618 ypos 783 action (Hide('adate1lovevo'), Jump('adate1love2')) hovered tt.Action ("Don't") focus_mask True
        frame:
            xalign .5
            text tt.value

label adate1lovelk:
    scene date 1pm 024a
    pov "{i}Damn, so damn near me. But I won't have fun while she's crying.{/i}"
    jump adate1love2

label adate1love2:
    scene date 1pm 025a
    pov "{i}Damn, she's seriously crying. But why?{/i}"
    if inc == True:
        pov "Hey little sister, what's wrong? I don't get it."
    else:
        pov "Hey [ls], what's wrong? I don't get it."
    ls "I didn't want to do it, I'm so sorry!"
    pov "Doing what? Kissing me?"
    scene date 1pm 026a
    ls "Yes..."
    pov "You gave me a kiss and now you're crying? I still don't get it."
    ls "I did something wrong! I kissed you, but that's forbidden!"
    pov "Forbidden?"
    if inc == True:
        ls "I'm your sister, so we can't do this! It's forbidden!"
    else:
        ls "We know each other for so long, so we can't do this! It's forbidden!"
    pov "Haha, why's that?"
    ls "Mom told me about it."
    pov "Hahaha... hahaha... haha..."
    scene date 1pm 027a
    ls "Why are you laughing?"
    pov "Haha, you want to be a grown up and make a fuss about that crap!"
    ls "But..."
    pov "I know it's forbidden, haha. But we're all alone here and I don't care, so there is no need to get sad."
    ls "Huh?"
    pov "Or you're afraid that you just did something wrong and I'm now better than you?"
    ls "NO!"
    pov "{i}Oh that sounds not so persuasive.{/i}"
    pov "Come here!"
    scene date 1pm 028a
    ls "Ohh..."
    pov "Stop crying. I won't think bad about you and won't tell anyone about it."
    ls "I'm still sorry... <sob>"
    if inc == True:
        pov "I'm your big brother. I won't let you down!"
    else:
        pov "I've known you for so long. I won't let you down!"
    ls "Aww..."
    call screen adate1loveki

screen adate1loveki():
    default tt = Tooltip (" ")

    fixed:
        if lilsislove >= 20:
            imagebutton auto "gui/icons/icon_love_%s.png" xpos 605 ypos 193 action (Hide('adate1loveki'), Jump('adate1lovekiss')) hovered tt.Action ("Kiss her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1286 ypos 193 action (Hide('adate1loveki'), Jump('adate1lovetalk')) hovered tt.Action ("Cheer her up") focus_mask True
        frame:
            xalign .5
            text tt.value

label adate1lovetalk:
    scene date 1pm 032a
    pov "You're feeling better now?"
    ls "Yes, much better. Thank you for your kind words."
    pov "Good, but I think it's better we end this now."
    ls "Yes. I'm sorry again."
    pov "Don't! There's no need to."
    scene black
    "You went home with [ls]."
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label adate1lovekiss:
    scene date 1pm 029a
    $ lilsislove += 1
    $ adatekiss = True
    if inc == True:
        "You kiss your little sister."
    else:
        "You kiss [ls]."
    $ lsiskiss += 1
    ls "Hnn...?"
    pov "<kissing>"
    ls "Hnn..."
    scene date 1pm 030a
    ls "You... you kissed me..."
    pov "Haha, yes!"
    ls "But... why?"
    pov "Because you don't have to worry anymore. I did something forbidden too. So we're equal now."
    scene date 1pm 031a
    pov "And since when did you become such a wonk?"
    ls "Hnn..."
    pov "Oh I can't do it, it's forbidden! No one will know about it, so you can forget about it now."
    ls "Hm..."
    pov "My little dummy."
    scene date 1pm 032a
    ls "So you're not mad anymore?"
    pov "I was never mad about it. It was just your imagination."
    ls "Then I'm happy now too."
    pov "Much better."
    scene date 1pm 033a
    if inc == True:
        ls "That my big brother is such a nice person! I'm so glad."
    else:
        ls "That you're such a nice person! I'm so glad."
    pov "And I'm happy that I can be with you too."
    ls "Aww, so sweet."
    pov "And you're looking so damn cute now."
    ls "<giggle>"
    if lilsislove >= 30:
        pov "I need another one!"
        scene date 1pm 034a
        ls "Hnn..."
        pov "<kissing>"
        ls "Hmm..."
        $ lsiskiss += 1
        scene date 1pm 035a
        ls "Why did you kiss me... again?"
        pov "Because I wanted to?"
        ls "Huh?"
        pov "Haha, I'm now the bad one. I did it one more time than you. So you're now the good one again."
        scene date 1pm 036a
        ls "Oh I see, haha."
        if inc == True:
            ls "Thank you for cheering me up, big brother!"
        else:
            ls "Thank you for cheering me up, [pov]!"
        pov "You're welcome!"
        pov "{i}I'm sure she knows exactly what I'm up to and she liked the kisses.{/i}"
        pov "{i}It couldn't be possible that she's that naive.{/i}"
    scene date 1pm 036a
    pov "Shall we go home now?"
    if inc == True:
        ls "Yes it was a very nice trip with you, big brother."
    else:
        ls "Yes it was a very nice trip with you, [pov]."
    pov "I think the same, [ls]. Let's go home."
    scene black
    "You go home together."
    $ d1ralove = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose


label adate1cor:
    pov "{i}Getting stuck on the fence, haha. This could be fun.{/i}"
    ls "Hnn... Hm..."
    pov "{i}She's struggling and can't free herself. But how did she get in this situation?{/i}"
    pov "{i}Luckily for her I'm her date... or maybe not, hehe.{/i}"
    "You walk over to her silently."
    scene date 1pm 006
    pov "Hanging there completely helpless, geez [ls]."
    ls "Oh you found me? Please help me, I'm stuck."
    pov "Getting stuck when you're cheating at hide and seek, what a funny surprise, hahaha."
    ls "I didn't cheat, you're just bad at this game, dummy. Now help me please."
    call screen adate1corhelp

screen adate1corhelp():
    default tt = Tooltip (" ")

    fixed:
        if lilsiscorruption >= 40:
            imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 605 ypos 193 action (Hide('adate1corhelp'), Jump('adate1corpunish')) hovered tt.Action ("Play with her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1286 ypos 193 action (Hide('adate1corhelp'), Jump('adate1corpush')) hovered tt.Action ("Help her") focus_mask True
        frame:
            xalign .5
            text tt.value

label adate1corpush:
    "You decide to push her over the fence."
    pov "Here let me help you."
    ls "Waaah..."
    scene date 1pm 014x
    ls "Au..."
    pov "Oh shit. Are you alright?"
    ls "Yes, au. Thank you."
    pov "Maybe that's your punishment for cheating."
    ls "But I didn't..."
    pov "Yeah... yeah..."
    scene date 1pm 015x
    ls "Can we go home now? My knees hurt."
    pov "So the falling did hurt you a little?"
    ls "Yes..."
    pov "Ok. Let's go back home."
    scene black
    "You go home together."
    $ d1ranormal = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label adate1corpunish:
    pov "{i}I won't miss this chance! Let's have some fun with her.{/i}"
    "You walk closer to her."
    ls "Good, you can push... Aahhh..."
    scene date 1pm 008
    "You strip her panties down."
    ls "What...? What happened?!"
    pov "The bad girl gets punished now for cheating!"
    ls "But... you can't be serious! You pulled my panties down!"
    pov "Yes, you're a smart girl, haha."
    ls "Noo! Stop! Don't look at me!"
    pov "What a cute pussy you have."
    if inc == True:
        ls "Please stop! You're my big brother. You shouldn't see me naked."
    else:
        ls "Please stop! We've known each other for to long. You shouldn't see me naked."
    pov "{i}Damn! What to do now?{/i}"
    jump adate1corplay

label adate1corplay:
    scene date 1pm 008
    call screen adate1corplay1

screen adate1corplay1():
    default tt = Tooltip (" ")

    fixed:
        if lsispronBDSM >= 4:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1352 ypos 213 action (Hide('adate1corplay1'), Jump('adate1corBDSM')) hovered tt.Action ("Slap her ass") focus_mask True
        if lsispronanal >= 4:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1392 ypos 392 action (Hide('adate1corplay1'), Jump('adate1coranal')) hovered tt.Action ("Finger her asshole") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1392 ypos 539 action (Hide('adate1corplay1'), Jump('adate1corfinger')) hovered tt.Action ("Finger her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1392 ypos 681 action (Hide('adate1corplay1'), Jump('adate1corrub')) hovered tt.Action ("Rub her clit") focus_mask True
        frame:
            xalign .5
            text tt.value

label adate1corBDSM:
    scene date 1pm 009
    pov "{i}Let's start gentle and then surprise her.{/i}"
    ls "Noo... You're touching me! Stop!"
    pov "Ssshh..."
    if su15masBDSM == True:
        pov "{i}I saw her masturbating to that stuff, so I'm sure she'll like it.{/i}"
    else:
        pov "{i}I wonder if she got into that stuff I showed her?{/i}"
    scene date 1pm 010slap
    with vpunch
    "You slap her ass."
    scene date 1pm 011slap
    ls "Aaahhh...! You slapped me!"
    pov "Yes! The bad girl gets slapped."
    ls "No... please don't, hah..."
    pov "I'm not done yet, I know you need some more."
    ls "Nooo..."
    if lilsiscorruption >= 60:
        scene date 1pm 010slap
        with vpunch
        "You slap her ass more."
        scene date 1pm 011slap
        ls "Ahh... hah..."
        if inc == True:
            pov "You're a bad, bad little sister!"
        else:
            pov "You're a bad, bad girl!"
        scene date 1pm 012slap
        with vpunch
        pov "And more on your red ass!"
        scene date 1pm 013slap
        ls "Hah... aaahhh... please... stop..."
        pov "You like that, don't you?"
        ls "Hah... no... hah..."
        pov "{i}What a bad liar she is. Everybody can see that she's getting wet.{/i}"
        pov "Maybe you need even more?"
        if inc == True:
            ls "No, please, big brother. I'm sorry. You've punished me enough."
        else:
            ls "No, please, [pov]. I'm sorry. You've punished me enough."
        pov "That's not the right thing you have to say to stop me and you know that very well!"
        pov "So you need some more!"
        scene date 1pm 012slap
        with vpunch
        pov "And more on your red ass!"
        ls "Ah... please stop master!"
        scene date 1pm 013slap
        ls "Hnng... hah... hah..."
        pov "{i}Damn, she really said it. Such a naughty girl.{/i}"
        pov "{i}But I don't want to stop now. She's so wet, I'll lick her now to orgasm and so she'll get approval that she did good.{/i}"
        jump adate1lick
    else:
        ls "No! Stop it!"
        pov "Oops..."
        pov "{i}She struggled so much that she fell over the fence.{/i}"
        jump adate1fail


label adate1coranal:
    scene date 1pm 009
    pov "{i}Let's start gentle and then surprise her.{/i}"
    ls "Noo... You're touching me! Stop!"
    pov "Ssshh..."
    if su15masanal == True:
        pov "{i}I saw her masturbating to that stuff, so I'm sure she'll like it.{/i}"
    else:
        pov "{i}I wonder if she got into that stuff I showed her?{/i}"
    scene date 1pm 010anal
    ls "Aaaahhh... What are you doing?"
    pov "Punishing you through the backdoor."
    ls "No please, not there."
    pov "{i}Damn she's so tight. I never touched such a tight hole. I can't wait to stick my dick in that hole.{/i}"
    if inc == True:
        ls "Please big brother. Your finger is in my asshole. It's so wrong."
    else:
        ls "Please [pov]. Your finger is in my asshole. It's so wrong."
    "You start to move around inside her."
    ls "Hnng... hah..."
    pov "You're not supposed to enjoy your punishment, [ls]!"
    ls "Hnn... I don't, hah..."
    pov "{i}Does she really like anal that much? I can barely believe it. So I'll give her more.{/i}"
    if lilsiscorruption >= 60:
        scene date 1pm 011anal
        "You push your finger further in and start to pump in and out slowly."
        ls "Hnng... hah... oh, please..."
        pov "You like that, don't you?"
        if inc == True:
            pov "Getting your asshole fingered by your big brother?"
        else:
            pov "Getting your asshole fingered by me?"
        ls "No... aahhh... you're wro... hah..."
        pov "{i}Damn, her tight asshole clinging around my finger and she's getting wet. Anal is the right thing for her.{/i}"
        pov "No need to lie to me [ls]. I can feel the reactions of your asshole."
        ls "Hnnng... hah... stop..."
        pov "I can't stop! Your body tells me that you like it but you deny it. So maybe I'm wrong and I need to continue."
        ls "Hnnn... not... fair..."
        pov "A punishment is never fair. So...?"
        ls "..."
        ls "It feels... hnn... good! Your finger... make me... hah... feel good... hah."
        if inc == True:
            pov "So you like your asshole getting fingered by your big brother?"
            ls "Yes... I like your finger in me there... big brother..."
        else:
            pov "So you like your asshole get fingered by me?"
            ls "Yes... I like your finger in me there... [pov]..."
        pov "{i}Damn, she really said it. Such a naughty girl.{/i}"
        pov "Why stop then while you're enjoying it?"
        ls "Hnng... it's wrong... hah..."
        pov "{i}That bullshit again.{/i}"
        pov "{i}But I don't want to stop now. She's so wet, I'll lick her now to orgasm and so she'll get approval that she did good.{/i}"
        jump adate1lick
    else:
        ls "No! Stop it!"
        pov "Oops..."
        pov "{i}She struggled so much that she fell over the fence.{/i}"
        jump adate1fail

label adate1corrub:
    scene date 1pm 009
    pov "{i}Let's start gentle and then surprise her.{/i}"
    ls "Noo... You're touching me! Stop!"
    pov "Ssshh..."
    if su15masnormal == True:
        pov "{i}I saw her masturbating, so I'm sure she'll like it.{/i}"
    scene date 1pm 010clit
    ls "Aaaahhh... What are you doing?"
    pov "Teasing you for punishment."
    ls "No... hah... not..."
    pov "{i}Damn, she's sensitive! But her pussy is looking so damn sweet.{/i}"
    ls "Hnnng... haaah..."
    ls "No! Stop... hah... rubbing me there..."
    pov "Why? I'm sure you rub yourself there before."
    if inc == True:
        ls "Please... don't touch me there... hah... big brother!"
    else:
        ls "Please... don't touch me there... hah... [pov]!"
    pov "You should be thankful. You can enjoy this punishment."
    ls "Hnng... no..."
    pov "{i}She starts twitching. I'll tease her some more.{/i}"
    pov "Enjoy it some more. I'm not stopping now."
    ls "Noo...!"
    if lilsiscorruption >= 60:
        scene date 1pm 011clit
        pov "{i}Wow, her labia is swelling. She must be real horny right now.{/i}"
        ls "Hnng... Aahhh... Ahhh..."
        pov "You like that, don't you?"
        if inc == True:
            pov "Getting your clit rubbed by your big brother?"
        else:
            pov "Getting your clit rubbed by me?"
        ls "No... aahhh... you're wro... hah..."
        pov "{i}Damn, her labia swells some more and she's so damn wet.{/i}"
        pov "No need to lie to me [ls]. I can feel the reactions of your pussy."
        ls "Hnnng... hah... stop..."
        pov "I can't stop! Your body tells me that you like it but you deny it. So maybe I'm wrong and I need to continue."
        ls "Hnnn... not... fair..."
        pov "A punishment is never fair. So...?"
        ls "..."
        ls "It feels... hnn... good! Your rubbing... make me... hah... feel good... hah."
        if inc == True:
            pov "So you like your clit rubbed by your big brother?"
            ls "Yes... I like how you rubbing me there... big brother..."
        else:
            pov "So you like your clit rubbed by me?"
            ls "Yes... I like how you rub me there... [pov]..."
        pov "{i}Damn, she really said it. Such a naughty girl.{/i}"
        pov "Why stop then when you're enjoying it?"
        ls "Hnng... it's wrong... hah..."
        pov "{i}That bullshit again.{/i}"
        pov "{i}But I don't want to stop now. She's so wet, I'll lick her now to orgasm and so she'll get approval that she did good.{/i}"
        jump adate1lick
    else:
        ls "No! Stop it!"
        pov "Oops..."
        pov "{i}She struggled so much that she fell over the fence.{/i}"
        jump adate1fail

label adate1corfinger:
    scene date 1pm 009
    pov "{i}Let's start gentle and then surprise her.{/i}"
    ls "Noo... You're touching me! Stop!"
    pov "Ssshh..."
    if su15masnormal == True:
        pov "{i}I saw her masturbating, so I'm sure she'll like it.{/i}"
    scene date 1pm 010finger
    "You enter her pussy."
    ls "Aaaahhh... What are you doing?"
    pov "Exploring your pussy, haha."
    ls "No... hah... not..."
    pov "{i}Damn, she's sensitive! But her pussy is damn warm and sweet. I can't wait to stick my dick in it.{/i}"
    ls "Hnnng... haaah..."
    ls "No! Stop... hah... you're in me..."
    pov "Yes and it was the right decision."
    if inc == True:
        ls "Please... don't touch me there... hah... big brother!"
    else:
        ls "Please... don't touch me there... hah... [pov]!"
    pov "You should be thankful. You can enjoy this punishment."
    ls "Hnng... no..."
    pov "{i}She start twitching. I'll get deeper in her.{/i}"
    pov "Enjoy it some more. I'm not stopping now."
    ls "Noo...!"
    if lilsiscorruption >= 60:
        scene date 1pm 011finger
        pov "{i}Holy shit! She's a virgin, I can feel her hymen!{/i}"
        pov "{i}To think about it, I can be her first.. or maybe getting a reward for selling her virginity?{/i}"
        ls "Hnng... Aahhh... Ahhh..."
        pov "You like that, don't you?"
        if inc == True:
            pov "Getting fingered by your big brother in your intimate places?"
        else:
            pov "Getting fingered by me in your intimate place?"
        ls "No... aahhh... you're wro... hah..."
        pov "{i}Damn, her pussy is twitching and she's so damn wet.{/i}"
        pov "No need to lie to me [ls]. I can feel the reactions of your pussy."
        ls "Hnnng... hah... stop..."
        pov "I can't stop! Your body tells me that you like it but you deny it. So maybe I'm wrong and I need to continue."
        ls "Hnnn... not... fair..."
        pov "A punishment is never fair. So...?"
        ls "..."
        ls "It feels... hnn... good! Your finger so deep in me... make me... hah... feel good... hah."
        if inc == True:
            pov "So you like your pussy fingered by your big brother?"
            ls "Yes... I like feeling you in my pussy... big brother..."
        else:
            pov "So you like your pussy fingered by me?"
            ls "Yes... I like feeling you in my pussy... [pov]..."
        pov "{i}Damn, she really said it. Such a naughty girl.{/i}"
        pov "Why stop then when you're enjoying it?"
        ls "Hnng... it's wrong... hah..."
        pov "{i}That bullshit again.{/i}"
        pov "{i}But I don't want to stop now. She's so wet, I'll lick her now to orgasm and so she'll get approval that she did good.{/i}"
        jump adate1lick
    else:
        ls "No! Stop it!"
        pov "Oops..."
        pov "{i}She struggled so much that she fell over the fence.{/i}"
        jump adate1fail

label adate1lick:
    "You get behind her."
    scene date 1pm 009lick
    ls "Hnng... stop!"
    if lilsiscorruption >= 80:
        pov "{i}Her sweet taste!{/i}"
        ls "Hah... you're licking me..."
        pov "Yes, to end your punishment you need to cum!"
        ls "No! Hnng... I don't want... hah... to..."
        pov "Maybe... but you're body is telling me something else!"
        ls "Aaahhh... haaahhh..."
        if inc == True:
            pov "Enjoy it cum from your big brothers tongue!"
        else:
            pov "Enjoy it cum from my tongue!"
        ls "Noo... Hnng... it's so wrong..."
        "You lick her faster."
        scene date 1pm 010lick
        ls "Hah... oh god... hah..."
        pov "I knew you'd love it!"
        ls "Ohhh... ohhh... I can't..."
        pov "Just give in to yourself and stop denying it. You can't do anything."
        if inc == True:
            pov "You'll cum from your brothers tongue. And you'll love it!"
        else:
            pov "You'll cum from my tongue. And you'll love it!"
        ls "Please... hah... ohhh..."
        pov "{i}She'll cum soon, time to spice it up.{/i}"
        pov "You're at your limit. I can feel it! Stop fighting and tell me how you like it!"
        ls "Ohh... aaahhh... I... love..."
        pov "Yes..?"
        ls "I love your tongue... hah... licking me there... ohh..."
        pov "Good girl! Time to cum!"
        if inc == True:
            ls "AAAHHH! Big brother!"
            "Your little sister is cumming."
        else:
            ls "AAAHHH! [pov]!"
            "[ls] is cumming."
        jump adate1lay
    else:
        ls "No! Stop it!"
        pov "Oops..."
        pov "{i}She struggled so much that she fell over the fence.{/i}"
        jump adate1fail

label adate1lay:
    pov "Wow..."
    scene date 1pm 014
    "She fell over the fence."
    pov "{i}She must have had a strong orgasm. But what a wonderful view. I need more!{/i}"
    pov "Hey, everything alright [ls]?"
    ls "Hah... hah... hah..."
    pov "Come on, get up. It's time to pay me back."
    if lilsiscorruption >= 100:
        scene date 1pm 015
        pov "{i}I know you're done after that hard cumming.{/i}"
        if inc == True:
            pov "But now it's your turn helping your brother!"
        else:
            pov "But now it's your turn helping me!"
        ls "Huh? What do you mean?"
        pov "You're behavior and your lust wanting me to feel good too!"
        ls "You mean...?"
        scene date 1pm 016
        pov "Yes! I'm so hard it's starting to hurt me!"
        ls "Huh...?"
        pov "Haha, I know it's maybe your first time that you've seen a dick live, but you don't have to be scared."
        ls "It's so... big..."
        pov "Yes and you're the reason it got so big. You should be proud!"
        pov "Now please touch it. I need to cum too, badly!"
        pov "You enjoyed your cumming, now I want to enjoy mine."
        ls "O... ok..."
        scene date 1pm 017
        pov "Ohh.. your fingers are so soft and gentle!"
        ls "Hnn..."
        pov "Yes, rub it slowly. I'll guide you with my hand."
        if inc == True:
            ls "Ok... big brother..."
        else:
            ls "Ok... [pov]..."
        pov "{i}Wow, no more words about \"wrong\" or \"forbidden\". She must have enjoyed her orgasm very much. And now she's feeling guilty maybe?{/i}"
        pov "Is this the first dick you've touching?"
        ls "Yes..."
        if inc == True:
            pov "Good. It's very important that you learn those things from your big brother and not some childish boy."
        else:
            pov "Good. It's very important that you learn those things from me and not some childish boy."
        ls "You think so?"
        pov "Yes and I know you can be a good girl!"
        pov "Now do it yourself for some time. Show me how much you enjoyed my help before."
        if inc == True:
            ls "Ok... big brother..."
        else:
            ls "Ok... [pov]..."
        scene date 1pm 018
        pov "{i}Damn, she's such a tease! And I could fuck her mouth so badly right now!{/i}"
        if inc == True:
            pov "You're treating me so good, lil sis. It's like heaven."
        else:
            pov "You're treating me so good, [ls]. It's like heaven."
        ls "Thank you. I'll do my best."
        pov "{i}Damn! Did she really say that? She's giving me her first hand-job ever and wants to do a good job for me?{/i}"
        ls "Your... dick is pulsating. Is that normal?"
        pov "{i}It's like she's playing doctor-games with me. I wish I could suppress my cum forever.{/i}"
        pov "The pulsating shows that I'm about to cum, so I'll have to release soon or it won't stop hurting me."
        ls "Hurting you? I know something."
        scene date 1pm 019
        pov "{i}Fucking shit! She's kissing my dick! Like kissing the pain away!{/i}"
        ls "<kiss> No need for pain! <kiss>"
        pov "{i}Best shit ever!{/i}"
        pov "AAAAHH!"
        scene date 1pm 019x
        ls "Ohhh!"
        "You hold her head tight as you cum."
        pov "Yes! Yes! Yes!"
        ls "Hnn..."
        scene date 1pm 020
        ls "Noo! Look what you did!"
        if inc == True:
            ls "Your sperm hit me and something got in my mouth, big brother."
            pov "{i}She has no idea how hot she looks right now. My sperm on my little sister's face. And even in her mouth.{/i}"
        else:
            ls "Your sperm hit me and something got in my mouth, [pov]."
            pov "{i}She has no idea how hot she looks right now. My sperm on her face. And even in her mouth.{/i}"
        pov "I see! I couldn't control myself."
        pov "But don't worry. It shows you that you did very, very good. And that much for your first time."
        ls "Hnng..."
        pov "Maybe you should just enjoy the taste."
        if inc == True:
            pov "{i}The taste of your big brother.{/i}"
        ls "It's salty and thick."
        pov "{i}It's like heaven. But I wonder why I could get there?{/i}"
        scene date 1pm 021
        ls "Hnn... hnn..."
        pov "What's wrong? You look sad."
        ls "We did this forbidden things and we both liked it..."
        pov "Oh yes, I loved it very much and I'm very glad that you loved it too."
        ls "But..."
        scene date 1pm 022
        if inc == True:
            pov "Don't worry yourself anymore, lil sis. When grown ups feel those natural urges they just satisfy them as we did."
            pov "When we don't we get depressed and sad in no time. So it's all fine when we can help together with that."
            pov "No one is mad at you because of that and if you feel better it can be our secret. But we need to trust each other as siblings..."
            pov "and help each other. And I'm glad that you're the one helping me with that. And I'll help you of course."
            ls "Ok... I understand big brother."
            pov "So you're feeling better now?"
            ls "Yes. Thank you. I can now try to be a better grown up."
        else:
            pov "Don't worry yourself anymore, [ls]. When grown ups feel those natural urges they just satisfy them as we did."
            pov "When we don't we would get depressed and sad in no time. So it's all fine when we can help us together with that."
            pov "No one is mad at you because of that and if you feel better it can be our secret. But we need to trust each other..."
            pov "and help each other. And I'm glad that you're the one helping me with that. And I'll help you of course."
            ls "Ok... I understand [pov]."
            pov "So you're feeling better now?"
            ls "Yes. Thank you. I can now try to be a better grown up."
        pov "Let's go home! It was a very nice trip with you. And I'm sure you'll have much to think about at home."
        ls "Yes, you're right. Let's go home."
        scene black
        "You go home together."
        $ d1racorf = True
        $ weekendactivities += 1
        if weekendactivities == 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        ls "No! Stop it!"
        jump adate1fail

label adate1fail:
    scene date 1pm 014
    ls "No! It has to stop!"
    pov "Oh... oh..."
    scene date 1pm 015x
    ls "It's enough! It's wrong what you did to me!"
    pov "{i}Damn, maybe she wasn't corrupted enough?{/i}"
    ls "I want to go home now."
    pov "Yes, maybe you're right. Let's go home."
    scene black
    "You go home together."
    $ d1racor = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose



label adate1ntr:
    $ adatedavide = True
    pov "{i}What the hell is he doing here?{/i}"
    pov "{i}Disturbing my time with [ls].{/i}"
    scene date 1pm ntr03d
    pov "{i}Oh...? It's seems they don't know each other.{/i}"
    if inc == True:
        pov "{i}Right, mom prevents them from meeting each other all the time.{/i}"
    else:
        pov "{i}Right, [mother] prevents them from meeting each other all the time.{/i}"
    call screen adate1ntrdec

screen adate1ntrdec():
    default tt = Tooltip (" ")

    fixed:

        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 605 ypos 193 action (Hide('adate1ntrdec'), Jump('adate1ntrapp')) hovered tt.Action ("They can be friends") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 805 ypos 193 action (Hide('adate1ntrdec'), Jump('adate1ntrdis')) hovered tt.Action ("They can never be friends") focus_mask True
        frame:
            xalign .5
            text tt.value

label adate1ntrapp:
    if inc == True:
        pov "{i}I don't understand why mom makes such a fuss about it.{/i}"
    else:
        pov "{i}I don't understand why [mother] makes such a fuss about it.{/i}"
    pov "{i}[ls] is old enough to handle her life herself. She can choose her own acquaintances.{/i}"
    if davidegood > davidebad:
        pov "{i}But I should introduce them. Davide helped me, so I'll help him.{/i}"
        scene date 1pm ntr04
        pov "Hey there!"
        ls "Oh...?"
        davide "Huh?"
        if inc == True:
            ls "Big brother?"
        else:
            ls "[pov]?"
        davide "You're here with her?"
        scene date 1pm ntr05
        pov "Haha, yes relax Davide. What are you doing here?"
        davide "I had a dispute with Jeremy. He's convinced that he owns horses and they're here."
        davide "So I came by to take a photo and show him that he's wrong."
        pov "Haha, that guy seems to be really weird."
        davide "Yes, haha."
        pov "Oh..."
        scene date 1pm ntr06
        if inc == True:
            pov "No need to be scared, lil sis. This is Davide, a friend of mom and dad."
        else:
            pov "No need to be scared, [ls]. This is Davide, a friend of [mother] and Bruce."
        pov "And he gives me some work from time to time, he's a cool guy."
        ls "Oh? At your meetings at night, where I'm not allowed to participate?"
        pov "Yes, you're right."
        ls "So that's the reason I didn't meet him before?"
        pov "Yes, he's a bad boy, haha."
        if inc == True:
            davide "So you're [pov]'s little sister? A very nice surprise!"
        else:
            davide "So you're [mother]'s youngest daughter? A very nice surprise!"
        scene date 1pm ntr07
        ls "And mom doesn't want us to know each other?"
        davide "Yes, but I don't know why?"
        pov "Oh, I could tell, haha."
        ls "So, you're a bad guy?"
        davide "Wanna find out?"
        ls "<giggle>"
        scene date 1pm ntr08
        if inc == True:
            ls "But when you're a friend of my big brother than you're my friend too."
        else:
            ls "But when you're a friend of [pov] than you're my friend too."
        davide "Nice to meet you beautiful girl."
        if inc == True:
            davide "But I don't even know your name."
            ls "Oh sure. I'm [ls]."
        ls "Nice to meet you too. <giggle>"
        if lsisproninterracial > 4:
            pov "Yeah and I'm sure she has some special interests in you, mainly about your skincolor."
            davide "Because I'm black?"
            pov "Hahaha, oh yes!"
            scene date 1pm ntr09fetish
            if inc == True:
                ls "Brother!"
            else:
                ls "[pov]!"
            ls "You can't tell him about it!"
            pov "Why? When you love to watch interracial porn, why should it be bad to tell a black man about it, haha?"
            ls "But...!"
            pov "Don't worry. Adults like to share such things and it's nothing bad about it to have such dreams."
            ls "But..."
            scene date 1pm ntr010f
            if inc == True:
                davide "Your big brother is right."
            else:
                davide "[pov] is right."
            davide "You share that dream with many girls so there is nothing bad."
            davide "And I'm sure this could be a positive boost for a possible future friendship. Starting this honest."
            ls "Hnn..."
            pov "No need to be embarrassed [ls]. We won't judge you!"
            davide "He's right. There is no need to be sad."
            scene date 1pm ntr011f
            davide "And you can be pleased because I can give you more hints about that directly."
            davide "So you don't need to get your information about that second-hand from porn."
            ls "Hnn..."
            davide "So I see you like that idea, would you? It'll be much fun for both of us!"
            pov "{i}He knows how to talk her into his ideas, haha.{/i}"
            scene date 1pm ntr012f
            davide "I see what you did there bro! Letting me meet her after her mom tryed to prevent it."
            pov "Yes, because you're a good guy?"
            davide "Hahaha, I need to go now, we'll talk about it later."
            pov "{i}Good, maybe I can join the gang now faster.{/i}"
            scene date 1pm ntr08d
            ls "It was nice to meet him."
            pov "Oh yes, I see that, haha."
            ls "So we can continue?"
            pov "Continue?"
            ls "You need to find me, this doesn't count."
            pov "Ok. Hide, but I'll find you anyway."
            ls "Then give your best, dummy!"
            $ davidemeetint = True
            $ davidemeet = True
            $ d1rantrdavidey = True
            $ ntrloveale = True
            $ ntrhateale = False
            scene date 1pm 003g
            call screen adate1way4
        else:
            davide "I would love to meet with you more often."
            ls "I don't know, maybe. <giggle>"
            scene date 1pm ntr09
            davide "I see what you did there bro! Letting me meet her after her mom tryed to prevent it."
            pov "Yes, because you're a good guy?"
            davide "Hahaha, I need to go now, we'll talk about it later."
            pov "{i}Good, maybe I can join the gang now faster.{/i}"
            ls "See you..."
            scene date 1pm ntr08d
            ls "It was nice to meet him."
            pov "Oh yes, I see that, haha."
            ls "So we can continue?"
            pov "Continue?"
            ls "You need to find me, this doesn't count."
            pov "Ok. Hide, but I'll find you anyway."
            ls "Then give your best, dummy!"
            $ davidemeet = True
            $ d1rantrdavidey = True
            $ ntrloveale = True
            $ ntrhateale = False
            scene date 1pm 003g
            call screen adate1way4            
    else:
        scene date 1pm ntr03d
        if inc == True:
            pov "{i}They really don't know each other like mom wanted.{/i}"
        else:
            pov "{i}They really don't know each other like [mother] wanted.{/i}"
        pov "{i}[ls] looks shy, I wonder what she'll do?{/i}"
        scene date 1pm ntr04d
        pov "{i}Does she realize he's an asshole?{/i}"
        pov "{i}Too bad I can't hear them. But I don't want him to know my relationship to her.{/i}"
        scene date 1pm ntr05d
        pov "{i}She seems to like him. I wonder if I should warn her what a prick he is?{/i}"
        pov "{i}But she also could get mad that I distrust her judgment. And I don't want to ruin my date with her also.{/i}"
        scene date 1pm ntr06d
        pov "{i}Damn, what are they talking about?{/i}"
        scene date 1pm ntr07d
        pov "{i}Oh, he's gone. And she seems to be calm, so they talked nothing bad.{/i}"
        pov "{i}Let's go to her.{/i}"
        scene date 1pm ntr08d
        pov "Made a new friend?"
        ls "Oh, this guy? No. I just met him for the first time."
        pov "And? What you think of him?"
        ls "I don't know. He seems to be nice, but also a little weird."
        pov "{i}Good, she noticed it too.{/i}"
        ls "But we need to continue our game now!"
        pov "Our game?"
        ls "You need to find me, this doesn't count."
        pov "Ok. Hide, but I'll find you anyway."
        ls "Then give your best, dummy!"
        $ davidemeet = True
        $ d1rantrdaviden = True
        scene date 1pm 003g
        call screen adate1way4

label adate1ntrdis:
    pov "{i}I don't like the idea that he'll know about her. He should stay away from her!{/i}"
    pov "{i}But she also wants to be a grown up, so she must do her own decisions.{/i}"
    call screen adate1ntrint

screen adate1ntrint():
    default tt = Tooltip (" ")

    fixed:

        imagebutton auto "gui/icons/icon_action_%s.png" xpos 605 ypos 193 action (Hide('adate1ntrint'), Jump('adate1ntrstop')) hovered tt.Action ("Interfere") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 805 ypos 193 action (Hide('adate1ntrint'), Jump('adate1ntrdisw')) hovered tt.Action ("Just watch") focus_mask True
        frame:
            xalign .5
            text tt.value


label adate1ntrstop:
    scene date 1pm ntr03d
    pov "{i}No. I have to help her and stop this. She doesn't know about him.{/i}"
    scene date 1pm ntr04
    pov "Hey!"
    ls "Huh?"
    davide "..."
    pov "What you're think you're doing?"
    davide "What...?"
    pov "He's criminal scum! You shouldn't get to know him!"
    if lilsisrelationship < 20:
        scene date 1pm ntr05ang
        ls "Are you serious?"
        pov "Wait... what...?"
        ls "You're trying to tell me what I can do and whom I can meet?"
        pov "Yes, because he's a bad person."
        ls "And you don't think that I can decide that for myself?"
        pov "But I just wanted..."
        scene date 1pm ntr06ang
        ls "It was good that you came back, but I'm sick of being parented by everyone."
        ls "Mom and Dad are annoying enough and now you're starting with it too?"
        pov "But..."
        ls "No! I'm an adult, I can make my own decisions and you won't interfere."
        pov "{i}Shit, what happened? Did I just lose my relationship with her so badly?{/i}"
        pov "{i}And that asshole smiling at me!{/i}"
        scene date 1pm ntr07
        ls "Just ignore him. Sometimes he likes to be a dad too."
        davide "Haha, ok. You're related?"
        if inc == True:
            ls "Yes, he's my stupid big brother."
        else:
            ls "Not really. He lives with us."
        davide "So you're [mother]'s and Bruce's daughter?"
        ls "Yes, you know them?"
        pov "{i}Shit, this is even worse. Now she's telling him everything.{/i}"
        davide "Yes they're my friends too."
        scene date 1pm ntr08
        ls "Oh then it's nice to meet you. My name is [ls]."
        davide "I'm Davide. What a nice surprise to know that you are [mother]'s daughter."
        davide "We'd have meet earlier!"
        ls "Haha, maybe."
        pov "No!"
        scene date 1pm ntr09ang
        ls "You just don't get it, do you?"
        pov "..."
        davide "The beauty can make her own decisions."
        ls "I'll go home now! I don't want to spend more time with you!"
        pov "No, wait..."
        ls "No! You ruined it yourself. See you again sometime, Davide."
        davide "Bye, beautiful!"
        scene black
        "[ls] went home and Davide left too."
        "You also go home."
        $ d1rantrdavideyb = True
        $ ntrloveale = False
        $ ntrhateale = True
        $ weekendactivities += 1
        if weekendactivities == 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        scene date 1pm ntr05no
        ls "Oh...?"
        davide "What did you just say?"
        pov "Please go back in. I'll handle this!"
        ls "O... okay! Please take care."
        scene date 1pm ntr06no
        pov "You'll stay away from her, asshole!"
        davide "You serious? Treating me while we're alone here?"
        davide "Maybe I should just smash your head and then take care of your little girlfriend?"
        pov "{i}Shit, he's right. I must think fast about something.{/i}"
        pov "Hah, you won't touch me!"
        if inc == True:
            pov "Mom and dad will never forgive you and you'll get in much trouble with them."
            pov "Especially mom, since she's so proud of me!"
        else:
            pov "[mother] and Bruce will never forgive you and you'll get in much trouble with them."
            pov "Especially [mother], since she's so proud of me!"
        scene date 1pm ntr07no
        davide "Huh...?"
        pov "Yes you know that I'm right."
        pov "And I would go even further! I would even tell the cops about you and your little business."
        davide "No you won't. I don't believe you."
        pov "You don't know me. But you'll regret it if you try to get in contact with her again!"
        if inc == True:
            pov "Maybe it'll hit on mom and dad too. But they're only followers and the cops will see that too."
        else:
            pov "Maybe it'll hit on [mother] and Bruce too. But they're only followers and the cops will see that too."
        pov "I'm not kidding. You'll regret it badly!"
        scene date 1pm ntr08no
        davide "Maybe you got this round. But you'll make a mistake some time."
        pov "I wouldn't bet on it!"
        davide "So you can have her for now. Enjoy your lesbian time with your little girlfriend!"
        pov "Just go!"
        scene date 1pm 003g
        pov "Good. He's gone. Luckily this worked out."
        pov "Now it's time to go back to [ls]."
        $ d1rantrdaviden = True
        $ ntrloveale = False
        $ ntrhateale = True
        call screen adate1way4

label adate1ntrdisw:
    scene date 1pm ntr03d
    if inc == True:
        pov "{i}They really don't know each other like mom wanted.{/i}"
    else:
        pov "{i}They really don't know each other like [mother] wanted.{/i}"
    pov "{i}[ls] looks shy, I wonder what she'll do?{/i}"
    scene date 1pm ntr04d
    pov "{i}Did she realize that he's an asshole?{/i}"
    pov "{i}Too bad I can't hear them. But I don't want him to know my relationship to her.{/i}"
    scene date 1pm ntr05d
    pov "{i}She seems to like him. I wonder if I should warn her what a prick he is?{/i}"
    pov "{i}But she also could get mad that I distrust her judgment. And I don't want to ruin my date with her.{/i}"
    scene date 1pm ntr06d
    pov "{i}Damn, what are they talking about?{/i}"
    scene date 1pm ntr07d
    pov "{i}Oh, he's gone. And she seems to be calm, so they talked nothing bad.{/i}"
    pov "{i}Let's go to her.{/i}"
    scene date 1pm ntr08d
    pov "Made a new friend?"
    ls "Oh, this guy? No. I just met him for the first time."
    pov "And? What you think of him?"
    ls "I don't know. He seems to be nice, but also a little weird."
    pov "{i}Good, she noticed it too.{/i}"
    ls "But we need to continue our game now!"
    pov "Our game?"
    ls "You need to find me, this doesn't count."
    pov "Ok. Hide, but I'll find you anyway."
    ls "Then give your best, dummy!"
    $ davidemeet = True
    $ d1rantrdavidey = True
    $ ntrloveale = False
    $ ntrhateale = True
    scene date 1pm 003g
    call screen adate1way4


label adate1eat:
    scene black
    "You set up your picnic and eat with [ls]."
    jump adate1search


label alexisweekendlove:
    hide screen townl
    hide screen locations
    $ lilsislove += 1
    "[ls] contacted you to meet her. She told you it's urgent."
    scene weekend 01pm 040l
    "You meet [ls] at the barn."
    ls "You came [pov]! Now come closer please."
    pov "{i}She's so suspicious. What's going on?{/i}"
    ls "Come, I won't bite. <giggle>"
    scene weekend 01pm 041l
    ls "What are you afraid of?"
    if inc == True:
        ls "Come closer, brother."
    else:
        ls "Come closer, [pov]."
    pov "{i}Damn, she's teasing me. But why?{/i}"
    scene weekend 01pm 042l
    ls "I want to show you something really special today."
    ls "And I'm sure you'll love it. I hope so. Please love it."
    if inc == True:
        pov "Woah! Calm down, lil sis!"
    else:
        pov "Woah! Calm down, [ls]!"
    pov "Did you do drugs? You're overexcited."
    ls "I... I want to show you!"
    pov "It's alright. I'll look at the surprise you want to show me and then I'm sure you choosed something good."
    ls "Yes, I'will. <giggle>"
    pov "{i}Damn it! Now I can't await to see it!{/i}"
    pov "So what now? Won't you show me?"
    scene weekend 01pm 043l
    ls "Haha, you're right. Sit there and close your eyes!"
    pov "OK."
    ls "And no peeking or I'll need to hurt you! <giggle>"
    pov "Oh...?"
    ls "I know you. You'll try!"
    "You sit down."
    scene weekend 01pm 044l
    pov "Can you give me a hint? How long do I sit here with my eyes closed?"
    ls "Until I'm done."
    pov "And what is it?"
    ls "You'll see, just wait."
    pov "Is it something to eat?"
    pov "{i}This is funny. I know she's eager to show it to me and I can tease her a little.{/i}"
    if inc == True:
        ls "Stop being stupid, brother! <giggle>"
    else:
        ls "Stop being stupid, [pov]! <giggle>"
    pov "OK. OK. I'll wait then."
    scene black
    "You close your eyes."
    "You hear her rustling."
    pov "{i}What is she doing? Maybe a short peek?{/i}"
    ls "No peeking!"
    pov "{i}Damn, she really know me.{/i}"
    ls "Open your eyes now!"
    scene weekend 01pm 045l
    pov "Wow..."
    ls "Muah! <kiss>"
    scene weekend 01pm 046l
    ls "Hmm... <french kiss>"
    pov "{i}Damn. She's giving me a french kiss and doing that by laying naked on me.{/i}"
    pov "<kiss>"
    pov "{i}So was making out with me her surprise? She was right, I really love it.{/i}"
    scene weekend 01pm 047l
    if inc == True:
        ls "Do you like my surprise, brother?"
    else:
        ls "Do you like my surprise, [pov]?"
    pov "{i}She's nervous. But I wonder why? Was she really afraid I wouldn't like it?{/i}"
    pov "Yes, I love it! Seeing you taking the initiative and also all naked!"
    pov "{i}But her hands are in the way!{/i}"
    ls "I can see where you staring at. <giggle>"
    scene weekend 01pm 048l
    ls "You can take a better look now."
    pov "{i}She invites me to look at her pussy. This get even better.{/i}"
    scene weekend 01pm 049l
    pov "{i}So tight. And beautiful. And untouched, ready to be conquered.{/i}"
    scene weekend 01pm 050l
    ls "Hnng..."
    pov "{i}She's posing so unnatural. Like a pornstar. This innocence is very cute.{/i}"
    if inc == True:
        pov "Your pussy is so beautiful, lil sis."
    else:
        pov "Your pussy is so beautiful, [ls]."
    ls "Then please come closer."
    pov "{i}What is she up to now? Now I'm even more excited.{/i}"
    pov "Of course [ls]."
    scene weekend 01pm 051l
    if inc == True:
        pov "Hi there, beautiful sis."
    else:
        pov "Hi there, beautiful."
    ls "<giggle> You know what your surprise is?"
    pov "Making out with my beautiful girlfriend?"
    ls "I can be your girlfriend?"
    pov "{i}She's shaking. Did this make her that happy?{/i}"
    pov "Of course, I won't be that stupid to reject you."
    ls "<giggle> Then I'm your girlfriend now!"
    ls "How about you give your girlfriend something to stare at too? <giggle>"
    pov "{i}Shit! Did she really say that? She's getting serious!{/i}"
    scene weekend 01pm 052l
    "You undress in seconds."
    pov "So you want to make out with me as your surprise?"
    ls "Yes, I want to make out with my boyfriend."
    pov "{i}But why is she so eager to make out with me right now. And posing naked for me too?{/i}"
    pov "What happened to make you want to do this with me so suddenly?"
    ls "<giggle>"
    pov "{i}She's nervous.{/i}"
    pov "Please tell me, GIRLFRIEND."
    scene weekend 01pm 053l
    ls "When I was at my friends house she told me about her new boyfriend."
    pov "Hmm...?"
    ls "And she described you! I was so confused and afraid you'd cheat on me."
    pov "But I don't even know her?"
    ls "You really don't? I need to make this for sure."
    pov "{i}This is so cute. She wants me all for herself.{/i}"
    pov "I cant be her boyfriend, because I'm yours!"
    ls "Hmm..."
    pov "I'll prove that and give you the best pleasure today, like lovers would do!"
    scene weekend 01pm 054l
    pov "{i}Laying here all naked in front of me with her legs open, awaiting me to pleasure her.{/i}"
    pov "{i}This will get amazing!{/i}"
    scene weekend 01pm 060lroot
    pov "I can't wait to have fun together with you, sweetie."
    ls "<giggle> I can feel your penis poking on me."
    pov "So you maybe want to take \"that\" big step?"
    ls "You want to deflower me? <giggle>"
    pov "You want me to be your first?"
    ls "Only my boyfriend can be the first. <giggle>"
    pov "{i}Oh my... She invite me to be her first. I can't believe it! But should I do it now? Or maybe wait?{/i}"
    pov "{i}Let's see...{/i}"
    jump barnsex


label barnsex:
    scene weekend 01pm 060lroot
    call screen barnsexchoose

screen barnsexchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_head_%s.png" xpos 1832 ypos 245 action (Hide ('barnsexchoose'), Jump('barnsexhead')) hovered tt.Action ("Choose her head") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" xpos 1832 ypos 315 action (Hide ('barnsexchoose'), Jump('barnsexboobs')) hovered tt.Action ("Kiss her boobs") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1832 ypos 385 action (Hide ('barnsexchoose'), Jump('barnsexhands')) hovered tt.Action ("Ask for a handjob") focus_mask True
        imagebutton auto "gui/icons/icon_belly_%s.png" xpos 1832 ypos 457 action (Hide ('barnsexchoose'), Jump('barnsexbelly')) hovered tt.Action ("Kiss her belly") focus_mask True
        imagebutton auto "gui/icons/icon_pussy_%s.png" xpos 1832 ypos 529 action (Hide ('barnsexchoose'), Jump('barnsexpussy')) hovered tt.Action ("Choose her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" xpos 1832 ypos 602 action (Hide ('barnsexchoose'), Jump('barnsexfeet')) hovered tt.Action ("Choose her feet") focus_mask True
        imagebutton auto "gui/icons/icon_69_%s.png" xpos 1832 ypos 672 action (Hide ('barnsexchoose'), Jump('barnsex69')) hovered tt.Action ("Change position to 69") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1832 ypos 749 action (Hide ('barnsexchoose'), Jump('barnsexstop')) hovered tt.Action ("Finish") focus_mask True



    frame:
        xalign .5
        text tt.value




label barnsexhead:
    call screen barnsexheadchoose

screen barnsexheadchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 1635 ypos 246 action (Hide ('barnsexheadchoose'), Jump('barnsexheadkiss')) hovered tt.Action ("Kiss her") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" xpos 1635 ypos 398 action (Hide ('barnsexheadchoose'), Jump('barnsexheadblowjob')) hovered tt.Action ("Ask for a blowjob") focus_mask True


    frame:
        xalign .5
        text tt.value

label barnsexheadkiss:
    pov "I need to kiss you now!"
    ls "Oh [pov]. <giggle>"
    scene weekend 01pm 055la
    pov "<french kiss>"
    pov "{i}She open her mouth all by herself. She really love french kissing.{/i}"
    ls "<lick> <kiss> Hmm..."
    scene weekend 01pm 055lb
    pov "Hmm..."
    pov "{i}She's so pure and inexperienced. I'll make this unforgetable for her.{/i}"
    ls "Hmm... hmm..."
    scene weekend 01pm 056la
    ls "Hmm, lover! This is so good."
    pov "{i}Good. She's all in her new girlfriend role.{/i}"
    pov "I love to kiss your soft skin, sweetie!"
    ls "Kiss me more..."
    jump barnsex

label barnsexheadblowjob:
    pov "Maybe you can give me some pleasure with that sweet mouth of yours?"
    ls "You want me to lick on your penis?"
    pov "Yes, lick it or suck it as you want to. Feeling your mouth on my dick is real pleasure."
    ls "<giggle> OK. Lover."
    scene weekend 01pm 100la
    pov "{i}Oh, she's touching me.{/i}"
    ls "It's so hard and warm. So you need your girlfriend to help you there?"
    pov "{i}She's loving her role as my girlfriend. Being the only one that is allowed to help me that way.{/i}"
    pov "Yes, my girlfriend needs to help me."
    ls "Then lay down. <giggle>"
    scene weekend 01pm 101la
    pov "What a wonderful view!"
    ls "Then I'll give my best."
    pov "I'm very sure you will. Just do what you want, experience isn't needed here."
    pov "{i}I don't need to push her. She need to be relaxed.{/i}"
    ls "<giggle> Don't worry, I prepared myself."
    pov "Prepared?"
    scene weekend 01pm 102la
    ls "I can use the internet too, dummy."
    pov "Oh my... did you really watched porn to prepare?"
    ls "Haha, maybe?"
    pov "{i}This will get amazing.{/i}"
    scene weekend 01pm 103la
    pov "{i}She has a strong grip. Perfect.{/i}"
    pov "Yes, that start to feel good."
    ls "You're so big, but I'll try."
    pov "Don't stress yourself, it'll be perfect."
    pov "Seeing my girlfriend pleasuring me."
    ls "I'd love to. <giggle>"
    scene weekend 01pm 104lb
    ls "<lick>"
    pov "Oh... hmm..."
    pov "Such a cute view. Amazing!"
    ls "<giggle> <lick>"
    pov "{i}She's enjoying it too.{/i}"
    scene weekend 01pm 105lb
    ls "I want to try something with you now."
    pov "Oh?"
    ls "I saw it on the internet and when I do it right you will like it very much."
    pov "Now I'm curious."
    ls "And as my boyfriend you can decide if you want to cum in my mouth or on me."
    pov "{i}So good.{/i}"
    pov "As your boyfriend? That sound very weird, like others couldn't decide..."
    ls "<giggle> You know what I mean, dummy."
    pov "That reassures me, haha."
    scene weekend 01pm 106lb
    ls "<lick> <suck>"
    pov "{i}She's beginning. It feels so good.{/i}"
    ls "Hnng..."
    pov "Oh, yes..."
    pov "{i}Her tongue on my dick and her sucking. And this view. I won't hold out very long. Like a wonderful dream.{/i}"
    scene weekend 01pm 107lb
    ls "<suck> <lick>"
    pov "{i}Wow. She's trying to take me deep. Licking and sucking like she saw it.{/i}"
    ls "Hnng... <slurp>"
    pov "{i}I'll cum soon, I need to decide where I want my cum. On or in her?{/i}"
    call screen barnsexheadblowjobcum

screen barnsexheadblowjobcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 797 ypos 105 action (Hide ('barnsexheadblowjobcum'), Jump('barnsexheadblowjobinside')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1295 ypos 105 action (Hide ('barnsexheadblowjobcum'), Jump('barnsexheadblowjoboutside')) hovered tt.Action ("Cum on her face") focus_mask True


    frame:
        xalign .5
        text tt.value

label barnsexheadblowjobinside:
    if inc == True:
        pov "I want to cum in your mouth, lil sis."
    else:
        pov "I want to cum in your mouth, [ls]."
    ls "Hmm..."
    pov "Oh yes, almost there..."
    ls "<suck> <suck>"
    pov "OHHH... YES!"
    "You cum in her mouth."
    ls "Hnng..."
    scene weekend 01pm 108lbi
    ls "Hmm..."
    pov "{i}Is she...? She's holding my cum in her mouth.{/i}"
    pov "I came so good. You can spit it out now."
    scene weekend 01pm 109lbi
    ls "<gulp> <gulp>"
    pov "{i}She's swallowing it. This is so hot!{/i}"
    if inc == True:
        pov "{i}My little sister is drinking my cum.{/i}"
    else:
        pov "{i}[ls] is drinking my cum.{/i}"
    scene weekend 01pm 110lbi
    ls "Hmm..."
    pov "You really swallowed my sperm..."
    ls "My boyfriend tastes good. <giggle>"
    pov "This was so damn good, sweetie. I'm glad I have a girlfriend like you."
    ls "<giggle>"
    jump barnsex

label barnsexheadblowjoboutside:
    if inc == True:
        pov "I want to cum on your face, lil sis."
    else:
        pov "I want to cum on your face, [ls]."
    ls "Hmm..."
    pov "Oh yes, almost there..."
    ls "<suck> <suck>"
    pov "OHHH... YES!"
    scene weekend 01pm 108lbo
    "You cum on her face."
    ls "Hmm..."
    scene weekend 01pm 109lbo
    ls "Hmm... so much and so warm..."
    if inc == True:
        pov "{i}I came on my little sisters face.{/i}"
    else:
        pov "{i}I came on [ls]s face.{/i}"
    pov "Now I gave you some of my makeup, haha."
    ls "This is your privilege as my boyfriend, haha."
    pov "This was so damn good, sweetie. I'm glad I have a girlfriend like you."
    ls "<giggle>"
    jump barnsex

label barnsexboobs:
    pov "I need to kiss your boobs now!"
    ls "Oh [pov]. <giggle>"
    scene weekend 01pm 057la
    pov "<kiss> <suck>"
    ls "Ohh... This feels good."
    pov "Your boobs are so soft. And your nipples are getting hard. I love to suck on them."
    ls "Then do it. It's so nice, hah..."
    pov "Enjoy it sweetie."
    "You bite her nipple gentle."
    ls "Hah... hmm..."
    jump barnsex

label barnsexhands:
    pov "Maybe you can give me some pleasure with your hands?"
    ls "You want me to stroke your penis?"
    pov "Yes, stroke it or play with it as you want to. Feeling your hands on my dick is real pleasure."
    ls "<giggle> OK. Lover."
    scene weekend 01pm 100la
    pov "{i}Oh, she's touching me.{/i}"
    ls "It's so hard and warm. So you need your girlfriend to help you there?"
    pov "{i}She's loving her role as my girlfriend. Being the only one that is allowed to help me that way.{/i}"
    pov "Yes, my girlfriend needs to help me."
    ls "Then lay down. <giggle>"
    scene weekend 01pm 101la
    pov "What a wonderful view!"
    ls "Then I'll give my best."
    pov "I'm very sure you will. Just do what you want, experience isn't needed here."
    pov "{i}I don't need to push her. She need to be relaxed.{/i}"
    ls "<giggle> Don't worry, I prepared myself."
    pov "Prepared?"
    scene weekend 01pm 102la
    ls "I can use the internet too, dummy."
    pov "Oh my... did you really watched porn to prepare?"
    ls "Haha, maybe?"
    pov "{i}This will get amazing.{/i}"
    scene weekend 01pm 103la
    pov "{i}She has a strong grip. Perfect.{/i}"
    pov "Yes, that start to feel good."
    ls "You're so big, but I'll try."
    pov "Don't stress yourself, it'll be perfect."
    pov "Seeing my girlfriend pleasuring me."
    ls "I'd love to. <giggle>"
    scene weekend 01pm 104la
    pov "Wow! You're pumping my dick."
    ls "Yes, I read this gives you much pleasure."
    pov "Ohh..."
    pov "{i}Like a thight and clinging pussy.{/i}"
    ls "It's like strangle a worm. <giggle>"
    pov "Oh, don't call it a worm. It's more like a snake!"
    scene weekend 01pm 105la
    ls "So, I have a boyfriend with a snake, haha."
    pov "{i}Her dirty-talk is weird, but her hands...{/i}"
    pov "Haha, OHHH..."
    if inc == True:
        pov "This is so good, lil sis."
    else:
        pov "This is so good, [ls]."
    pov "[ls]!"
    scene weekend 01pm 106la
    pov "AAAHHH...!"
    ls "Huh?"
    scene weekend 01pm 107la
    ls "So my doing was that good?"
    pov "Oh yes. As you can see."
    ls "You came so much. I'm glad I could help you."
    pov "That was perfect, sweetie!"
    jump barnsex

label barnsexbelly:
    pov "I need to kiss your belly now!"
    ls "Oh [pov]. <giggle>"
    scene weekend 01pm 057la
    pov "<kiss>"
    ls "Ohh... It tickles."
    pov "I need to kiss every part of your body."
    ls "Hmm... your gentle kisses."
    jump barnsex


label barnsexpussy:
    call screen barnsexpussychoose

screen barnsexpussychoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 1635 ypos 246 action (Hide ('barnsexpussychoose'), Jump('barnsexpussylick')) hovered tt.Action ("Lick her pussy") focus_mask True
        if alexisvirgin == True:
            imagebutton auto "gui/icons/icon_pussy_%s.png" xpos 1635 ypos 398 action (Hide ('barnsexpussychoose'), Jump('barnsexpussydeflower')) hovered tt.Action ("Deflower her") focus_mask True
        if alexisvirgin == False:
            imagebutton auto "gui/icons/icon_pussy_%s.png" xpos 1635 ypos 398 action (Hide ('barnsexpussychoose'), Jump('barnsexpussyfuck')) hovered tt.Action ("Fuck her") focus_mask True


    frame:
        xalign .5
        text tt.value


label barnsexpussylick:
    pov "I need to eat you now!"
    ls "Eat me?"
    ls "Ohhh... Please do it."
    scene weekend 01pm 059la
    "You lick her pussy."
    ls "Ahh... hah... it feels so good."
    pov "<lick> And you're already so wet."
    ls "Oh... your tongue... hah... hah..."
    pov "{i}Damn, she's already shaking. But I couldn't lick her so fast so close to cum.{/i}"
    pov "{i}She must be getting close by the expectation of our makeout.{/i}"
    if inc == True:
        ls "Big brother... BROTHER!"
    else:
        ls "[pov]... [pov]!"
    scene weekend 01pm 060la
    ls "AAAHHH... HNNNG...!"
    if inc == True:
        pov "Yes, cum for me, lil sis."
    else:
        pov "Yes, cum for me, [ls]."
    ls "That was so good [pov]. You need to do this again."
    pov "I'm glad you liked it. So I can taste you and you have fun too."
    ls "<giggle> You're allowed to eat me everytime you want to."
    pov "{i}Oh this will come handy.{/i}"
    jump barnsex

label barnsexpussydeflower:
    pov "I'll take my privilege as your boyfriend and be your first."
    ls "I'm so excited. Will it hurt much?"
    pov "Just a little, I'll be gentle. But the outcome in fun is the best."
    ls "<giggle> Then take me lover."
    scene weekend 01pm 061la
    ls "I can feel your penis coming inside."
    pov "I'll do it very slow, so you can get used to it's size."
    ls "Hnn... Will this big thing even fit?"
    pov "You're really wet right now. With your juices I can slide in easily."
    ls "So it's good you made me wet. <giggle>"
    scene weekend 01pm 061lb
    pov "The tip of my dick is almost inside."
    ls "So hard and warm..."
    pov "I'll take slide in back and forward when I go deeper so you can produce more juices."
    ls "I'll give you all my juice, lover."
    scene weekend 01pm 062lb
    ls "Hnng..."
    pov "I'll go deeper. I can feel your hymen. You can feel me poking there too?"
    scene weekend 01pm 063la
    ls "Hah... yes. I can feel your penis pushing against it."
    pov "I need to push hard now to break it and it'll hurt."
    pov "But I need to do it so you can become finally mine."
    if inc == True:
        ls "Hnng... then do it. I want to be yours, brother."
    else:
        ls "Hnng... then do it. I want to be yours, [pov]."
    ls "Do it please!"
    scene weekend 01pm 063lb
    ls "HAAH!"
    pov "It's done. I'm your first, [ls]!"
    ls "HNNG... you're the first inside me..."
    pov "I'll start to fuck you now properly, so the pain will become joy."
    ls "Hmm..."
    scene weekend 01pm 064la
    ls "Oh yes fuck me, [pov]!"
    pov "Hnng... you're so tight and wet."
    ls "Hah... hah... so big..."
    image alexis_love_sex = Movie(channel="alexis_love_sex", play="images/anim/alexis_love_sex.webm")
    scene alexis_love_sex with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ls "Hah... Hnng... Ahh..."
    if inc == True:
        pov "{i}I'm inside her. I deflowered my little sister. And she's loving it.{/i}"
    else:
        pov "{i}I'm inside her. I deflowered her. And she's loving it.{/i}"
    pov "Does it feel good, [ls]?"
    ls "Yes... hah... more..."
    pov "You're so tight, I love your pussy."
    ls "And your penis is making me feel so good."
    pov "I'll cum soon, your tight pussy is the best. You're shaking, you're close too?"
    ls "Yes, I'll cum also. Let's cum together!"
    scene weekend 01pm 066la
    ls "HAAAHH... HNNG..."
    pov "{i}She's shaking wildy. She must have a strong orgasm.{/i}"
    ls "Aaaahh... I can feel it..."
    scene weekend 01pm 066lb
    if inc == True:
        ls "Cum with me brother!"
    else:
        ls "Cum with me [pov]!"
    pov "Oh yes, I will."
    $ alexisvirgin = False
    jump barnsexpussycumchoose

label barnsexpussycumchoose:
    call screen barnsexpussycum

screen barnsexpussycum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1709 ypos 222 action (Hide ('barnsexpussycum'), Jump('barnsexpussyinside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1709 ypos 446 action (Hide ('barnsexpussycum'), Jump('barnsexpussyoutside')) hovered tt.Action ("Cum outside") focus_mask True


    frame:
        xalign .5
        text tt.value

label barnsexpussyinside:
    pov "I'm cumming!"
    "You shoot your sperm in her pussy."
    scene weekend 01pm 067laci
    ls "Ohhh... I feel your hot sperm..."
    pov "Hnng... much more is coming!"
    if inc == True:
        ls "I can feel your hot sperm inside me, brother!"
    else:
        ls "I can feel your hot sperm inside me, [pov]!"
    ls "It's like a fire burning inside me."
    scene weekend 01pm 068laci
    ls "It's flowing outside. It feels weird."
    pov "You'll get used to it very fast, haha."
    ls "Hnng..."
    pov "You know why I released so much sperm inside you?"
    ls "Hm..."
    if inc == True:
        pov "Because I love you so much, lil sis."
    else:
        pov "Because I love you so much, [ls]."
    ls "Hmm..."
    scene weekend 01pm 069laci
    pov "{i}She's still confused. I wonder if she know that I'm aware that she's not on the pill.{/i}"
    pov "{i}That I'll possible made her pregnant right now. But I wonder why she didn't complained or tried to stop me?{/i}"
    $ alexisweekendinside = True
    jump barnsex

label barnsexpussyoutside:
    pov "I'm cumming!"
    scene weekend 01pm 067laco
    pov "Aaah..."
    ls "I can feel it on my skin..."
    pov "Hnng... much more is coming!"
    if inc == True:
        ls "I can feel your hot sperm on me, brother!"
    else:
        ls "I can feel your hot sperm on me, [pov]!"
    scene weekend 01pm 068laco
    pov "Hah, hah... I needed this."
    ls "You released so much, you tried to paint on me. <giggle>"
    pov "You know why I released so much sperm inside you?"
    ls "Hm..."
    if inc == True:
        pov "Because I love you so much, lil sis."
        ls "I love you too, brother."
    else:
        pov "Because I love you so much, [ls]."
        ls "I love you too, [pov]."
    jump barnsex

label barnsexpussyfuck:
    pov "I want to fuck with you [ls]."
    ls "Oh... then fuck me, lover."
    pov "{i}She's loving to be my girlfriend and the fun that comes with it.{/i}"
    scene weekend 01pm 061la
    pov "Since you're not a virgin anymore, I'll slide in faster. You're so wet again."
    ls "Yes, please stick it in so we can cum together [pov]!"
    pov "{i}She loves fucking. This is so amazing.{/i}"
    scene weekend 01pm 063la
    ls "Hah... your big penis is getting deeper inside me."
    pov "Yes and I'm very excited that I can hammer in your tight pussy again."
    ls "<giggle> Then do it, lover."
    scene weekend 01pm 064la
    ls "Oh yes fuck me, [pov]!"
    pov "Hnng... you're so tight and wet."
    ls "Hah... hah... so big..."
    image alexis_love_sex = Movie(channel="alexis_love_sex", play="images/anim/alexis_love_sex.webm")
    scene alexis_love_sex with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ls "Hah... Hnng... Ahh..."
    if inc == True:
        pov "{i}I'm inside her. I'm fucking my little sister. And she's loving it.{/i}"
    else:
        pov "{i}I'm inside her. I'm fucking her. And she's loving it.{/i}"
    pov "Does it feel good, [ls]?"
    ls "Yes... hah... more..."
    pov "You're so tight, I love your pussy."
    ls "And your penis is making me feel so good."
    pov "I'll cum soon, your tight pussy is the best. You're shaking, you're close too?"
    ls "Yes, I'll cum also. Let's cum together!"
    scene weekend 01pm 066la
    ls "HAAAHH... HNNG..."
    pov "{i}She's shaking wildy. She must have a strong orgasm.{/i}"
    ls "Aaaahh... I can feel it..."
    scene weekend 01pm 066lb
    if inc == True:
        ls "Cum with me brother!"
    else:
        ls "Cum with me [pov]!"
    pov "Oh yes, I will."
    jump barnsexpussycumchoose

label barnsexfeet:
    call screen barnsexfeetchoose

screen barnsexfeetchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 1635 ypos 246 action (Hide ('barnsexfeetchoose'), Jump('barnsexfeetkiss')) hovered tt.Action ("Kiss her feet") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" xpos 1635 ypos 398 action (Hide ('barnsexfeetchoose'), Jump('barnsexfeetjob')) hovered tt.Action ("Ask for a footjob") focus_mask True


    frame:
        xalign .5
        text tt.value

label barnsexfeetkiss:
    pov "I want to kiss your feet now."
    ls "My feet?"
    pov "Come here."
    scene weekend 01pm 090l
    ls "Haha, you're sucking on my big toe."
    pov "<suck> <suck>"
    ls "It feels weird but also new."
    scene weekend 01pm 090la
    if inc == True:
        ls "My big brother is sucking on my toe. <giggle>"
        pov "Because your feet are so cute, lil sis."
    else:
        ls "[pov] is sucking on my toe. <giggle>"
        pov "Because your feet are so cute, [ls]."
    scene weekend 01pm 090lb
    pov "Hmm... <suck>"
    ls "It's starting to feel good, your warm tongue licking on my toe. <giggle>"
    pov "Hmm..."
    ls "So I need to lick your feet too?"
    scene weekend 01pm 091l
    pov "<lick> Not today. Your feet are on the table."
    ls "Haha, it tickles a bit, but feeling better."
    pov "I love your cute feet, [ls]."
    ls "And I love your warm tongue, [pov]."
    scene weekend 01pm 092la
    ls "You can lick my feet everytime you want, slave."
    pov "What...?"
    ls "<giggle>"
    pov "Haha, this is funny."
    scene weekend 01pm 091lb
    pov "But I can't stop. You're cute feet make me horny."
    ls "So you'll get a boner everytime you see them naked?"
    pov "Oh yes. Hide your feet or they get licked!"
    ls "Hahaha..."
    jump barnsex

label barnsexfeetjob:
    pov "I want you to play with your feet on my dick."
    ls "You want me to stroke your penis with my feet?"
    pov "Yes, stroke it or play with it as you want to. Feeling your feets on my dick is real pleasure."
    ls "<giggle> OK. I can try, lover."
    scene weekend 01pm 092
    pov "Ohh, your cute feet are touching me."
    ls "Huh? And you can get off with my feet."
    pov "Of course."
    scene weekend 01pm 092lb
    pov "Seeing your cute feet on my dick. And when you now start to rub on it I'll cum very fast."
    ls "Rubbing on your penis?"
    pov "Like you'd do it with your hands. It's not so easy but you can do it."
    scene weekend 01pm 093l
    ls "Like I would do with my hands? I'll try then."
    pov "Oh yes, like that. Very good. You're very talented."
    scene weekend 01pm 093la
    ls "Like I used need to if I had no hands. <giggle>"
    pov "So I see you like that new experience mostly more than me, haha."
    ls "When my cute feet can do this for you..."
    scene weekend 01pm 093lb
    pov "{i}This view is so wonderful. Seeing her cute little feet trying to get me off.{/i}"
    ls "Your penis is pulsating so much. It loves my feet. <giggle>"
    ls "Let me try more."
    scene weekend 01pm 094l
    ls "Now it's like I would do with my hands."
    pov "Yes, stroking on my dick like that."
    ls "I wasn't aware, that I can please you this way."
    pov "The feeling is incredible good!"
    scene weekend 01pm 094lb
    ls "Then enjoy it even more, lover."
    pov "I can't stop staring at that! I could watch you forever doing this, but..."
    ls "My feet are feeling to good. <giggle>"
    scene weekend 01pm 094la
    pov "Oh yes! I'll cum soon and I want to cum on your feet."
    ls "Haha, to reward them for their hard work?"
    if inc == True:
        pov "You know exactly what's on my mind, lil sis!"
    else:
        pov "You know exactly what's on my mind, [ls]!"
    ls "Maybe my feet should be your girlfriends then. <giggle>"
    scene weekend 01pm 095l
    pov "{i}She has so much fun pleasing me like that. Amazing!{/i}"
    pov "Hold them there. I'll cum much on them."
    ls "They're waiting for their reward. <giggle>"
    scene weekend 01pm 096l
    pov "OHHH... YES!"
    ls "So much is coming out..."
    pov "This will become a masterpiece."
    ls "Hahaha..."
    scene weekend 01pm 097lb
    pov "This was fantastic! You did a very good job, pleasuring me."
    ls "I wanted to give my best for my boyfriend."
    pov "And you really did. I'm glad."
    scene weekend 01pm 095la
    pov "And it's a pleasant surprise that you have so much fun too."
    ls "It's only fun when it's with you."
    pov "That's a very sweet profession of love!"
    ls "Maybe. <giggle>"
    jump barnsex

label barnsex69:
    pov "You ever heard of the position 69?"
    ls "Haha, yes. You want to do this with me?"
    pov "You can bet. So we both can have fun."
    scene weekend 01pm 080l
    pov "Oh, you know already what your part is, haha."
    ls "<suck> Hmm... <giggle>"
    if inc == True:
        pov "Your pussy tastes so good, lil sis."
    else:
        pov "Your pussy tastes so good, [ls]."
    ls "Hnng..."
    scene weekend 01pm 081l
    pov "<lick> Do you want to make it a little game?"
    ls "Hmm?"
    pov "Who cums first lose the game, haha."
    ls "Hm... hm..."
    pov "This will be easy, you're already very wet."
    ls "Hnng..."
    scene weekend 01pm 082l
    pov "HAH... you cheater, haha."
    ls "<giggle> You'll lose. <lick>"
    pov "{i}She's doing really good. Squeezing my balls too. The best win-win.{/i}"
    pov "Hnng... hah..."
    scene weekend 01pm 083l
    pov "<lick> <bite>"
    ls "Hnng... hah... hah..."
    pov "{i}Damn, I try my best but she's doing to good. I'll cum any moment but I still have to do my duty.{/i}"
    pov "I... you'll win this... I'm about to cum, hah..."
    ls "My losing lover can decide where he wants to cum."
    pov "{i}Did she really asked me that? This is so hot... Hnng...{/i}"
    call screen barnsex69cum

screen barnsex69cum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1722 ypos 248 action (Hide ('barnsex69cum'), Jump('barnsex69inside')) hovered tt.Action ("In her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1722 ypos 459 action (Hide ('barnsex69cum'), Jump('barnsex69outside')) hovered tt.Action ("On her face") focus_mask True


    frame:
        xalign .5
        text tt.value

label barnsex69inside:
    pov "I want to cum in your mouth, sweetie!"
    ls "OK. Tell me when your..."
    scene weekend 01pm 087la
    pov "HNNNG... AAHHH..."
    ls "Huh...?"
    pov "I'm cumming, sweetie!"
    scene weekend 01pm 087lb
    ls "Hnng... <gulp> <gulp>"
    pov "{i}Wow. She's swallowing my sperm. Time to let her also cum.{/i}"
    scene weekend 01pm 085l
    "You furious lick her."
    ls "Hnng... hah..."
    if inc == True:
        ls "I... AHHH... HAH... brother!"
    else:
        ls "I... AHHH... HAH... [pov]!"
    pov "Enjoy your orgasm, [ls]."
    ls "Hah... hah..."
    scene weekend 01pm 086lb
    ls "I really loved that game. <giggle>"
    pov "Oh yes, me too."
    jump barnsex

label barnsex69outside:
    pov "I want to cum on your face, sweetie!"
    ls "OK. Tell me when your..."
    scene weekend 01pm 084l
    pov "HNNNG... AAHHH..."
    ls "Huh...?"
    pov "I'm cumming, sweetie!"
    scene weekend 01pm 085l
    "You furious lick her."
    ls "Hnng... hah..."
    if inc == True:
        ls "I... AHHH... HAH... brother!"
    else:
        ls "I... AHHH... HAH... [pov]!"
    pov "Enjoy your orgasm, [ls]."
    ls "Hah... hah..."
    scene weekend 01pm 086l
    if inc == True:
        ls "You came so much on my face, brother."
    else:
        ls "You came so much on my face, [pov]."
    ls "But I really loved that game. <giggle>"
    pov "Oh yes, me too."
    jump barnsex

label barnsexstop:
    pov "OK. I'm done. Let's stop."
    ls "OK, lover."
    pov "Let's lay here in the hay and relax a little."
    if alexisweekendinside == True:
        scene weekend 01pm 070laci
        pov "Is something wrong?"
        ls "You came inside me!"
        pov "Yes."
        ls "I'm not on the pill, maybe I got pregnant."
        pov "Oh..."
        if inc == True:
            ls "Mom will kill us when she finds out that we made a baby."
        else:
            ls "My mom will kill us when she finds out that we made a baby."
        pov "{i}Wow. She didn't complain that she could have a baby, only about the consequences what can happen when others know about it.{/i}"
        pov "{i}Does she want to have a baby with me?{/i}"
        call screen barnsexpregnant
    else:
        scene weekend 01pm 070laco
        ls "That was so much fun!"
        pov "I'm glad you liked it too. I can't wait for our next time."
        ls "Yes, we need to do this again."
        jump barnsexend

screen barnsexpregnant():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1329 ypos 179 action (Hide ('barnsexpregnant'), Jump('barnsexpregnantyes')) hovered tt.Action ("I want a baby with her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1572 ypos 179 action (Hide ('barnsexpregnant'), Jump('barnsexpregnantno')) hovered tt.Action ("I don't want a baby with her") focus_mask True


    frame:
        xalign .5
        text tt.value

label barnsexpregnantyes:
    if inc == True:
        pov "We'll deal later with mom."
        ls "Huh?"
        pov "I'd love to have a baby with you, lil sis."
        ls "But we're siblings..."
    else:
        pov "We'll deal later with your mom."
        ls "Huh?"
        pov "I'd love to have a baby with you, [ls]."
        ls "But we know each other all our lives..."
    pov "And we're also a couple now. And couples can have babies!"
    ls "Hmm..."
    pov "{i}Was that a agreeing \"hmm\" or a denying one? Or maybe she needs some time to think about it.{/i}"
    $ alexisbabywant = True
    jump barnsexend

label barnsexpregnantno:
    pov "No we won't need to deal with her."
    pov "I don't want to get you pregnant, I just made a mistake."
    ls "So I can take a after-sex-pill."
    pov "Yes that's a good idea. You're too young to get pregnant."
    ls "Hmm..."
    pov "{i}Is she disappointed?{/i}"
    jump barnsexend

label barnsexend:
    scene weekend 01pm 071l
    $ alexisweekendinside = False
    pov "Let's cuddle a while."
    ls "Oh yes. I need this now."
    if inc == True:
        pov "I love you, lil sis."
        ls "I love you too, big brother."
    else:
        pov "I love you, [ls]."
        ls "I love you too, [pov]."
    scene black
    "After I while she leaves you to go back to her friend. You go home."
    $ weekendactivities += 1
    $ alexisweekendsecond = True
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose


label cdate5:
    hide screen locations
    scene black
    "*knock *knock"
    "You hear someone knocking at your door."
    scene date 5pm 099
    pov "Oh, hi [bs]. What do you want?"
    bs "I need to go to the mall and want you to come with me!"
    pov "You want to go with me to the mall?"
    bs "Yes!"
    if bigsiscorruption >= bigsislove:
        pov "{i}That's a little suspicious. Why would she choose me?{/i}"
        "You hesitate a moment."
    bs "Mom wants me to show you the mall, so you can go shopping yourself in the future."
    if bigsiscorruption >= bigsislove:
        pov "{i}So that's the reason.{/i}"
    pov "Hm..."
    scene date 5pm 098
    bs "What? You're making me wait?"
    call screen cdate5start

screen cdate5start():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 890 ypos 452 action (Hide('cdate5start'), Jump('cdate5yes')) hovered tt.Action ("Join her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 890 ypos 214 action (Hide('cdate5start'), Jump('cdate5no')) hovered tt.Action ("Don't go") focus_mask True
        frame:
            xalign .5
            text tt.value


label cdate5no:
    pov "No sorry, [bs] I don't want to join you."
    scene date 5pm 097
    bs "What?"
    pov "You heard me. I won't join you!"
    bs "Ok, your loss."
    jump weekendacchoose

label cdate5yes:
    pov "Sure, let's go!"
    scene date 5pm 096
    bs "Great!"
    scene black
    $ cdate5 = True
    $ cdate5finside = False
    $ cdate5foutside = False
    if inc == True:
        "You go with your big sister to the mall."
    else:
        "You go with [bs] to the mall."
    "All the way she tells you about her efforts to get famous..."
    pov "{i}So boring...{/i}"
    "and what she'll do when she makes her way out of this shithole."
    scene date 5pm 000
    bs "Come on follow me. There's something suspicious going on there."
    pov "Over there?"
    bs "Yes, see the crowd? Nothing interesting ever happens here!"
    "You follow her."
    scene date 5pm 001
    bs "Oh no!"
    pov "What's wrong?"
    pov "There's a girl doing a photo-shoot and showing her tits in public. What's special with that?"
    if katefirstmeet == True:
        pov "Oh and I know her, it's [kate]."
    scene date 5pm 003
    bs "She's a whore! Everyone knows that!"
    pov "Wow! Ok..."
    bs "Yes. She's playing innocent, but she's a bitch. I hate her so much!"
    pov "{i}Is it possible that [bs] is just jealous of her? Or is there a story maybe?{/i}"
    scene date 5pm 004
    "Photographer" "Let's thank her for doing such a good job. She's a real beauty!"
    "Crowd" "Yeah you did it, hottie!"
    "Man" "You're so damn hot girl!"
    "Girl" "You're so famous! I love you!"
    pov "{i}Oh yes, [bs] is jealous.{/i}"
    scene date 5pm 005
    bs "You understand now? She's getting my fame! I'm better than her and should get the applause."
    pov "Hm..."
    pov "{i}But she has also a nice body. Better not comment on that.{/i}"
    bs "I'll pay her back! The people need to learn that I'm a better star!"
    pov "{i}Well, she's obsessed with that idea.{/i}"
    scene date 5pm 006
    "Photographer" "Now I need someone new for our last session."
    bs "Oh...?"
    "Photographer" "This photo-shoots have a chance to get printed in a magazine besides our website, so take your chance."
    bs "Real printed stuff?"
    scene date 5pm 007
    bs "Take me! Here!"
    pov "{i}Oh, this could be fun!{/i}"
    bs "Take me, sir! I'm the perfect girl for your photo-shoot!"
    scene date 5pm 008
    "Photographer" "Hm, well. Someone so motivated!"
    "Photographer" "But where's your partner? The last one is always a couple photo-shoot."
    pov "{i}Oh, oh...{/i}"
    "Photographer" "You can't do it alone."
    bs "Ok, please wait a second."
    if bigsisrelationship <= 5 and NTR == True:
        jump cdate5ntr
    scene date 5pm 009
    bs "Hehe..."
    pov "{i}Hm, should I help her? Maybe this could be fun...{/i}"
    call screen cdate5help

screen cdate5help():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 816 ypos 150 action (Hide('cdate5help'), Jump('cdate5helpyes')) hovered tt.Action ("Help her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1086 ypos 150 action (Hide('cdate5help'), Jump('cdate5helpno')) hovered tt.Action ("Don't help her") focus_mask True
        frame:
            xalign .5
            text tt.value

label cdate5helpno:
    scene date 5pm 009
    pov "No sorry, [bs]. I don't like to get photographed with you in a shoot."
    scene black
    bs "What? Are you serious?"
    bs "You damn asshole! You'll pay for that, ruining my chance to do this."
    scene black
    "She storms off very angry."
    scene black
    "You decide to go home after this \"date\" went so bad."
    $ dtime += 1
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5helpyes:
    scene date 5pm 009
    pov "Ok, ok. I'm in."
    bs "Good decision!"
    $ bigsisrelationship += 1
    scene date 5pm 010
    bs "Follow me."
    "You go with her to the bed."
    pov "{i}Hah, the photographer is staring, because she looks very hot in that outfit.{/i}"
    pov "{i}And I'm her helper now! Maybe I'll get a reward?{/i}"
    scene date 5pm 011
    bs "We can forget our differences for this photo-shoot, can we?"
    bs "You understand how important this is for me?"
    bs "I'll be grateful if you help me and you'll get a reward."
    pov "{i}Oh... chances...{/i}"
    bs "Just play along."
    scene date 5pm 012
    bs "I found someone who'll help me. Now I can participate!"
    "Photographer" "Good. Then go on the bed so we can start."
    bs "Ok. Thank you."
    scene date 5pm 013
    pov "{i}Oh wow, she's so hot. And I can get close to her now.{/i}"
    bs "Come on [pov]."
    pov "I'm right behind you."
    pov "{i}And I'll love to get closer!{/i}"
    scene date 5pm 014
    "Photographer" "Good. Just lay there for a few starting shots."
    pov "{i}Damn, maybe I should take advantage of her needful situation.{/i}"
    "Photographer" "What's your name beautiful girl?"
    bs "I'm [bs]."
    "Photographer" "Let's welcome [bs]."
    "Crowd" "You can do it [bs]!"
    "Man" "You're sexy."
    "Photographer" "And your boyfriends name?"
    bs "Oh he isn't my boyfriend, just a friend helping me out."
    "Photographer" "Oh, ok. And your name is?"
    pov "I'm [pov]."
    "Crowd" "Nice to meet you too, [pov]."
    "Girl" "You're hot!"
    if inc == True:
        pov "{i}And now I'm not her brother anymore, just a friend.{/i}"
    else:
        pov "{i}And now I'm not her childhood friend anymore, just a friend.{/i}"
    "Photographer" "So when your friend is helping you out he may help you to pretend to be a couple too."
    "Photographer" " Because this should be a couple shoot!"
    bs "Oh..."
    scene date 5pm 015
    bs "<whisper> I'll need you to play along further. We'll just pretend to do that."
    pov "<whisper> Hm..."
    if inc == True:
        bs "<whisper> Please just do it, little brother!"
        pov "{i}Sure why not? Pretending to be a couple with my hot older sister. What could get wrong?{/i}"
    else:
        bs "<whisper> Please just do it, [pov]!"
        pov "{i}Sure why not? Pretending to be a couple with my hot childhood friend. What could get wrong?{/i}"
    pov "<whisper> Sure."
    bs "<whisper> Thank you."
    scene date 5pm 016
    bs "We need just a moment to clear some things. Now we can start."
    "Photographer" " Good, but remember... Pretend as much and best as you can that you're a couple."
    "Photographer" "Naturalness is absolutely needed for good photos!"
    bs "Ok."
    pov "{i}This guy is a genius!{/i}"
    "Photographer" "Good then how about you cuddle together for a start?"
    scene date 5pm 017
    "[bs] comes close to you and you hold her for the photos."
    bs "Is that good?"
    "Photographer" "Perfect!"
    "Man" "I want to cuddle such a hot girl too!"
    pov "{i}Yes! I'm so close I can smell her hair and she likes it, because the crowd seems to love her.{/i}"
    "Girl" "We need to see her tits!"
    "Photographer" "Hm... the crowd is right. A little nudity would be good."
    scene date 5pm 018
    bs "What...?"
    "Crowd" "Yes we're right. Get those tits out!"
    pov "{i}I love the crowd. Fantastic idea. I wonder what [bs] will do?{/i}"
    bs "But..."
    "Photographer" "We need to make good photos!"
    scene date 5pm 019
    pov "{i}Haha, that face. Did she really think she could make it better then the other girl without showing some skin?{/i}"
    bs "<whisper> What... should we do?"
    pov "{i}Oh is she scared to show her boobs to the crowd or just to me?{/i}"
    if inc == True:
        pov "{i}Her brother.{/i}"
    else:
        pov "{i}Her childhood friend.{/i}"
    pov "<whisper> I can't decide that for you."
    scene date 5pm 020
    bs "I... i..."
    pov "{i}She's paralyzed! Unsure what's right{/i}."
    "Crowd" "Boobies! Boobies! Go [bs]!"
    pov "{i}And the crowd is without mercy. They want to enjoy the new star.{/i}"
    pov "{i}But maybe I can help her to get her more comfortable with the situation.{/i}"
    scene date 5pm 021
    bs "<whisper> Huh? What did you do?"
    pov "<whisper> I got rid of my shirt, so I'm half naked. I thought it might help you."
    bs "<whisper> How?"
    pov "<whisper> Now I'm naked too and you don't need to be so ashamed because I stripped too."
    bs "<whisper> Are you kidding me?"
    pov "<whisper> Sorry I don't have tits to show."
    "Girl" "Show us more, you horndog!"
    scene date 5pm 022
    bs "Hm..."
    "Another girl" "Get away from him you slut, he's mine!"
    "Man" "You're so damn hot [bs]."
    pov "<whisper> See? The people love us and are having their fun too. A great chance to get some fame."
    pov "<whisper> And don't forget this was your idea."
    bs "Hnn..."
    "Photographer" "We need a decision."
    scene date 5pm 023
    bs "Ok, I'm in!"
    "Crowd" " Yes! You go girl!"
    "Man" "You're so sexy!"
    pov "{i}Very nice. The crowd decided.{/i}"
    pov "{i}But she's still seems embarrassed. But I bet she's enjoying it more!{/i}"
    "Photographer" "You're brave, [bs]. Now look at me for a few shots."
    scene date 5pm 024
    "Photographer" "Yes you're a sexy girl [bs]. Tease me with your smile."
    pov "{i}What a charmer. But she loves it anyway and it's a win for me too.{/i}"
    "You get closer to her."
    "Crowd" "This is fantastic. You're so beautiful [bs]!"
    pov "{i}This is too much for me. I'll help her with showing her tits.{/i}"
    pov "{i}She already agreed to show them, so I'll do nothing wrong. I must see them{/i}!"
    scene date 5pm 025a
    bs "Huh?"
    bs "<whisper> What are you doing? Are you crazy?"
    "Crowd" "Yes you're doing right boy!"
    pov "<whisper> I'm helping you show them your tits. When I cover them they can't see them and you fulfilled your end."
    "Girl" "They're so big. I want to suck them!"
    bs "Huh?"
    pov "{i}She's getting goosebumps. She enjoys the compliments, I was so right.{/i}"
    pov "<whisper> See, they love my idea."
    "Photographer" "Not bad!"
    pov "{i}Oh he hears us and likes my idea too?{/i}"
    scene date 5pm 026a
    pov "<whisper> You earn your fame [bs]. Look how much they adore you!"
    "Photographer" " Yes, look to me for a few shots again! You have a very photogenic body."
    pov "<whisper> See? Even the photographer liked my idea."
    bs "Hnng..."
    pov "{i}Wow. I can feel her heartbeat through her tits. She's excited.{/i}"
    if inc == True:
        pov "{i}So much that she doesn't complain that her brother is holding her naked tits. In public, seen by a crowd of strangers!{/i}"
    else:
        pov "{i}So much that she doesn't complain that her childhood friend is holding her naked tits. In public, seen by a crowd of strangers!{/i}"
    pov "{i}This is just amazing!{/i}"
    "Photographer" "Now give the crowd some audience please."
    scene date 5pm 027a
    "Crowd" "We love you girl!"
    "Girl" "You're a goddess. Make love with me!"
    "Man" "No! I want her first!"
    bs "Hnng..."
    pov "{i}She's loving the attention she's getting. But there are many lesbians here?{/i}"
    "Man" "Wow, did I see nipple rings there?"
    "Girl" "No you didn't. She's a good girl, not your slut!"
    "Another Man" "Maybe a damn sexy slut."
    bs "Hmm..."
    pov "<whisper> Look, over there! Your rival is boiling with rage."
    scene date 5pm 028a
    bs "<whisper> Haha, you're right. That face!"
    pov "<whisper> She's realizing that she's losing her fame to you."
    pov "<whisper> And I know what we can do to destroy her completely."
    bs "<whisper> Hm...?"
    pov "<whisper> I'll uncover your boobs now!"
    pov "<whisper> They people will adore you more then and you want someone to see them, that's why you doctored your boobs."
    pov "<whisper> Every famous star shows her boobs, so it's a small bet for a high win."
    bs "<whisper> O... ok."
    pov "{i}She's loving my idea too.{/i}"
    scene date 5pm 031a
    "Girl" "Oh my god!"
    "Crowd" "Ooohhh...!"
    "Man" "Nipple rings! Such a sexy slut!"
    "Girl" "Shut up! That's classy! And they're beautiful!"
    pov "<whisper> See? They love it. A win-win-win situation for you."
    bs "<whisper> And you have your win too!"
    pov "<whisper> Huh?"
    if inc == True:
        bs "<whisper> Getting your hands on your sister's breasts."
    else:
        bs "<whisper> Getting your hands on my breasts."
    pov "{i}Oh, is she teasing me? Maybe she's enjoying it a little too much. Getting the wrong idea?{/i}"
    pov "{i}What if she misunderstand it and is getting to slutty? Do I want this?{/i}"
    "Crowd" "They need to be played with!"
    "Man" "Do it faggot!"
    call screen cdate5boobs

screen cdate5boobs():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1170 ypos 95 action (Hide('cdate5boobs'), Jump('cdate5byes')) hovered tt.Action ("Go further [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 569 ypos 95 action (Hide('cdate5boobs'), Jump('cdate5bno')) hovered tt.Action ("Calm her down [lv1]") focus_mask True
        frame:
            xalign .5
            text tt.value



label cdate5byes:
    scene date 5pm 029a
    $ bigsiscorruption += 1
    bs "Hah..."
    "You pull on her nipple rings."
    pov "<whisper> Time to fulfill the wish of the crowd."
    "Crowd" "Knead them. Make her nips hard!"
    "Girl" "Yes! I'd love to see her turned on."
    bs "<whisper> Not so rough please..."
    scene date 5pm 030a
    "You start to knead them."
    pov "<whisper> Wow. No complaining?"
    bs "Hah... <whisper> It's the wish of the crowd. Like you said."
    pov "{i}Damn, maybe I should start an influence agency?{/i}"
    if inc == True:
        pov "{i}Damn. I'm playing with my sister's tits in public and the only thing she's aware of, is what the people are thinking.{/i}"
    else:
        pov "{i}Damn. I'm playing with her tits in public and the only thing she's aware of, is what the people are thinking.{/i}"
    pov "{i}I wonder how far I can get her to go with this.{/i}"
    scene date 5pm 032a
    "Photographer" "Yes tease me more [bs]!"
    "Man" "What a view. I wish I could fap right now!"
    "Girl" "You pervert! Just admire the perfection."
    "You slide under the blanket."
    pov "{i}Let's test it out more. I'll never get her in this situation again.{/i}"
    scene date 5pm 033a
    bs "Aah... What are you doing?"
    "Crowd" "Yes! You go [pov]!"
    "Man" "Best idea ever!"
    "Girl" "Isn't this going too far?"
    pov "<whisper> I know what the people want! Your turn [bs]!"
    bs "<whisper> You can't be serious!"
    pov "<whisper> For the fame!"
    "Photographer" "What a nice idea to spice the shoot up!"
    scene date 5pm 034a
    pov "<whisper> See? Everyone loves the idea. Let me help you!"
    bs "<whisper> You want to help me get out off my pants?"
    pov "<whisper> Yes, as a wish of the audience. And I'm sure you're enjoying it too."
    if inc == True:
        bs "<whisper> We shouldn't do this. You're my brother! You shouldn't take off your sister's pants."
    else:
        bs "<whisper> We shouldn't do this. We've known each other for so long! You shouldn't take off my pants."
    pov "<whisper> You remember how important it was that you choose me for a couple photo-shoot?"
    pov "<whisper> I'm very sure you were aware what could happen and wanted to do this with me, instead of someone else."
    bs "<whisper> What? No."
    pov "<whisper> That's not so persuasive. I'll do this now!"
    scene date 5pm 035a
    bs "Hah... ahh..."
    pov "Come here!"
    bs "S... stop..."
    "Man" "Oh she needs some help, haha."
    "Crowd" "Yes, convince her!"
    "Girl" "I hope they won't stay under that blanket!"
    if bigsiscorruption <= 20:
        jump cdate5normend
    scene date 5pm 036a
    "Crowd" "Yes, he did it!"
    bs "<whisper> Please stop it."
    if inc == True:
        pov "<whisper> Stop fighting, big sis."
    else:
        pov "<whisper> Stop fighting, [bs]."
    pov "<whisper> We both know you want it too. These sexy panties need to be seen."
    pov "{i}And they're almost transparent!{/i}"
    bs "<whisper> But everyone will see..."
    pov "<whisper> Just relax and trust me. We'll slip under the blanket again."
    scene date 5pm 037a
    "Crowd" "Booh! We want to see her panties too!"
    "Photographer" "Please respect the models wishes."
    "Photographer" "But I'm sure there's enough room for your imaginations what a couple could do almost naked under the blanket."
    pov "<whisper> You got it? Everyone knows but nobody sees it. And through their imagination you're getting your fame."
    if inc == True:
        bs "<whisper> And you get your big sister almost naked so close with your tricks. You little pervert!"
    else:
        bs "<whisper> And you almost got me naked with your tricks. You little pervert!"
    pov "<whisper> Oh you got me! But I can feel how much you're turned on."
    pov "<whisper> You're burning and your nipples are hard like rocks. You like the attention a little too much."
    pov "<whisper> So let me enjoy my winning and you can enjoy the rest of your photo-shoot."
    bs "<whisper> Hm..."
    "Photographer" " Look here [bs]!"
    scene date 5pm 038a
    bs "Hah..."
    "Photographer" "Yes good [pov]. Hold her nipple like that."
    pov "<whisper> Look! He's taking a close shot of your beautiful pierced nipple!"
    pov "<whisper> Imagine that on a star magazine!"
    bs "Hnng..."
    "Crowd" "She's getting horny!"
    "Man" "What's going on under that blanket?"
    "Girl" "Can I join you? I want to get touched by that hot guy too!"
    "Photographer" "Now give me something cool [bs]."
    scene date 5pm 039a
    bs "Peace!"
    "Photographer" "Wonderful!"
    "Photographer" "Hold still, just a few more!"
    pov "{i}Damn, I need more too!{/i}"
    scene date 5pm 040a
    bs "Hah..."
    "Crowd" "She moaned!"
    "Man" "I bet they're fucking under the blanket!"
    "Other Man" "No they won't be so stupid to do that in public!"
    "Girl" "Yes! Get your thoughts together, pervert!"
    "Photographer" "What's wrong?"
    pov "<whisper> Oh I just improved our pretending to be more natural."
    "Photographer" "Oh, I see."
    bs "Hah... hah..."
    pov "<whisper> We need a moment."
    "Photographer" "Ok, sure."
    "Crowd" "What are they saying?"
    scene date 5pm 041a
    bs "<whisper> What the hell are you're thinking. Get your hands off there!"
    pov "<whisper> Sshh... relax. I just got more authentic, you're also flooding down there."
    bs "<whisper> It's not what you're thinking..."
    pov "<whisper> Oh, so you're that horny because of me?"
    bs "<whisper> Of course not!"
    pov "<whisper> Then you can let me continue and just enjoy your pleasure without a bad mind."
    if bigsiscorruption <= 50:
        jump cdate5normend
    "Photographer" "Can we continue."
    "Crowd" " Yes, no more breaks. More moaning [bs]!"
    pov "Yes, go on!"
    bs "No, wait..."
    pov "Go on!"
    "Photographer" "Ok, look at me again, [bs]. You're doing good."
    scene date 5pm 042a
    bs "Hnng... <smile>"
    "Photographer" "Yes, very hot! You're talented!"
    "Man" "Because she's a slut!"
    "Girl" "Shut up! I want to be like her!"
    "Another Girl" "Her pretending to be a couple with [pov] is amazing."
    "Man" "Yes, you think they're fucking already!"
    pov "<whisper> Enjoy my fingers. You earned it and everyone rewards you for that."
    bs "Hnng..."
    pov "{i}Time for more.{/i}"
    scene date 5pm 043a
    bs "Hahiiiih..."
    "Girl" "Did she cum?"
    "Man" "So hot!"
    "Photographer" "What happened? You alright?"
    pov "{i}I happened. Two fingers wide in her wet pussy! Haha.{/i}"
    pov "<whisper> You better play along! I'm not sure how they'll react if they know you're dripping wet."
    scene date 5pm 045a
    bs "Haha, no everything is alright. My nipples are a little to sensitive."
    bs "[pov]'s playing with them all the time, maybe it's time to stop."
    bs "Hahaha, hah... ah..."
    "Crowd" "No! Don't stop! Play more, she loves it."
    "Girl" "Yes let her moan more!"
    "Man" "Oh god. I need to fap."
    "Photographer" "So we can continue again...?"
    bs "Yes... sorry... please continue."
    pov "<whisper> Good girl! Enjoy your reward!"
    scene date 5pm 044a
    bs "Hnng... Hah..."
    "Girl" "Yes my hero. He won't stop!"
    "Crowd" "That moaning. You go girl!"
    pov "<whisper> You're enjoying this a little bit too much, aren't you?"
    pov "<whisper> Telling them how good my hands feel in you?"
    bs "Hah... hah..."
    if inc == True:
        pov "<whisper> Do you enjoy it that much getting fingered by your little brother?"
    else:
        pov "<whisper> Do you enjoy it that much getting fingered by your little brother?"
    bs "<whisper> You're... wro... hah!"
    pov "<whisper> You're a bad liar, haha."
    scene date 5pm 046a
    bs "Hnng...!"
    pov "<whisper> You feel my hard dick? Your wet pussy is aching for it!"
    pov "<whisper> And I'll stick it in you soon! Fucking you good!"
    "Photographer" "Damn my battery is too low. I need to change it, so a short break."
    "Crowd" "Hurry photographer, we want to see them play more."
    scene date 5pm 047a
    bs "<whisper> Please! We can't do that!"
    pov "<whisper> Oh we can. I noticed how wet your pussy is, sucked my fingers in before. You want it badly."
    bs "<whisper> Hnn..."
    pov "<whisper> See? Alone the thinking of it turns you on! You're shaking."
    pov "<whisper> But I won't judge you!"
    if inc == True:
        pov "<whisper> I've waited so long to fuck my hot sister, I'll give you a good pounding!"
    else:
        pov "<whisper> I've waited so long to fuck you, I'll give you a good pounding!"
    scene date 5pm 048a
    bs "<whisper> Hnng..."
    if inc == True:
        pov "<whisper> And I want you to be a good girl and take your brothers hard dick!"
        pov "<whisper> We can enjoy each other now, no one knows that we're siblings."
        pov "<whisper> I feel that you'd love to spread rumors about your photo-shoot now."
    else:
        pov "<whisper> And I want you to be a good girl and take my hard dick!"
        pov "<whisper> We can enjoy each other now, no one knows that we're staying so close."
        pov "<whisper> I feel that you'd love to spread rumors about your photo-shoot now."
    bs "<whisper> HNNG...!"
    scene date 5pm 049a
    bs "<whisper> Please don't do it. I'll make it up to you."
    pov "<whisper> Hm...? And what could stop me now from ramming my hard dick in you?"
    bs "<whisper> I... I'll suck you off when this is over. But please don't fuck me."
    pov "{i}Damn, she's serious, I can see it in her eyes!{/i}"
    pov "<whisper> Hm..."
    "You stare in each others eyes."
    "Photographer" "I'm ready, let's continue! Look here please, [bs]!"
    scene date 5pm 050a
    bs "Ok!"
    pov "{i}I could get rewarded with a blowjob wanted by her or try to take her now!{/i}"
    if bigsiscorruption <= 70:
        jump cdate5bj
    pov "{i}But now I have the chance to take her and she won't complain.{/i}"
    pov "{i}So what should I do?{/i}"
    call screen cdate5bjfuck

screen cdate5bjfuck():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1479 ypos 83 action (Hide('cdate5bjfuck'), Jump('cdate5fuck')) hovered tt.Action ("Fuck her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1652 ypos 83 action (Hide('cdate5bjfuck'), Jump('cdate5bj')) hovered tt.Action ("Wait for the blowjob [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label cdate5fuck:
    pov "{i}Screw it! Her number's up now!{/i}"
    scene date 5pm 051a
    bs "Huh?"
    "You slide your dick in her wet pussy."
    "Photographer" "What's the problem now?"
    bs "I... he... he...aah..."
    pov "<whisper> You won't tell them what we're doing now, will you?"
    scene date 5pm 052a
    bs "Hnng..."
    pov "{i}Haha, is she trying to escape? There's no way out of it now.{/i}"
    "Photographer" "What's the problem?"
    pov "{i}She's sucking me in, but won't accept it. Naughty girl!{/i}"
    bs "I... I've a cramp... hah... ah..."
    pov "{i}Wow, she has an excuse for everything.{/i}"
    pov "We're trying to make the couples thing look more authentic by pretending to fuck."
    bs "Hnng... hah..."
    pov "{i}Damn, her pussy pressing on my dick now like crazy. That turned her on very much.{/i}"
    "Photographer" "Oh, I see. That looks good!"
    "Crowd" "Wow, so realistic."
    "Man" "I bet they're really fucking!"
    scene date 5pm 053a
    pov "<whisper> No more escaping! Stay here with me and enjoy your fuck!"
    bs "Hah... hah... hah..."
    "Girl" "Yes take her good and then do me too!"
    "Man" "I want to pretend it too with her!"
    pov "<whisper> We'll enjoy this now together until we both cum!"
    pov "<whisper> Because it'll be such a shame if the blanket drops off now!"
    bs "Hnng... hah... hm..."
    pov "<whisper> So I want you now to be good, honest girl and tell me you love it too."
    bs "Hah...!"
    "You fuck her faster!"
    scene date 5pm 054a
    bs "Hah, ahhh..."
    "You stare in each others eyes."
    if inc == True:
        bs "<whisper> I... I love how... hah... you fuck me... aahh... brother!"
    else:
        bs "<whisper> I... I love how... hah... you fuck me... aahh... [pov]!"
    pov "<whisper> Good. Now you're honest and can enjoy your cum."
    bs "Hah... hah... haahh..."
    pov "<whisper> Come here!"
    scene date 5pm 055a
    "You start to french kiss her."
    bs "<kiss> hnng..."
    "Crowd" "Wohoo!"
    "Photographer" "Fantastic!"
    pov "{i}Her tongue is tingling active around mine. She loves to get kissed like that.{/i}"
    bs "<kiss> hm... hm..."
    scene date 5pm 056a
    bs "Hnng... hnng..."
    pov "{i}Wow, she looks so happy right now. Accepting her desires.{/i}"
    pov "<whisper> I'm glad to see that you accept it now. Doing such bad things in public with me!"
    if inc == True:
        bs "<whisper> Yes. Please, I need to cum! Make me cum, brother!"
    else:
        bs "<whisper> Yes. Please, I need to cum! Make me cum, [pov]!"
    pov "<whisper> As you wish [bs]. Let's cum together."
    "You go even faster in and out of her."
    scene date 5pm 057a
    bs "Aaah... hah... Ahh..."
    "Photographer" "Wow, this is really authentic. You're like pro's."
    "Crowd" "Like a damn porn. More!"
    "Girl" "Oh god, my imagination. I want to do that too!"
    bs "Harder [pov]. Harder! I'm almost there!"
    pov "Me too. Your pussy is so good [bs]!"
    scene date 5pm 058a
    bs "Ah... ah... Ahhhh...!"
    "Man" "She's cumming!"
    "Crowd" "What a hot show!"
    pov "{i}I'm at my limit too.{/i}"
    call screen cdate5fcum

screen cdate5fcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 639 ypos 237 action (Hide('cdate5fcum'), Jump('cdate5fin')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1077 ypos 237 action (Hide('cdate5fcum'), Jump('cdate5fout')) hovered tt.Action ("Cum outside") focus_mask True
        frame:
            xalign .5
            text tt.value

label cdate5fin:
    $ cdate5finside = True
    if inc == True:
        "You cum inside your older sister."
    else:
        "You cum inside her."
    jump cdate5fucked

label cdate5fout:
    $ cdate5outside = True
    if inc == True:
        "You spray your cum over your older sisters thighs."
    else:
        "You spray your cum over her thighs."
    jump cdate5fucked

label cdate5fucked:
    if cdate5finside == True:
        scene date 5pm 059ai
    else:
        scene date 5pm 059ao
    bs "Hnng... hah..."
    "You can see in her eyes her agreement and how unsure she is about what she did."
    "You signal her back that you're very satisfied and enjoyed it."
    "Crowd" "Again! Do it again, we need more!"
    "Photographer" "Staying so close I must say the show was even better."
    "Photographer" "Seeing it from another angle and... oh... OHH..."
    "He got a peek under the blanket."
    "Girl" "What's wrong?"
    "Photographer" "Nothing! everything is... alright! Let's thanks them for that great show!"
    "Crowd" "<Applause>"
    $ d5rccorfuck = True
    $ cdate5fuck = True
    jump cdate5martin

label cdate5martin:
    martin "No, nooo!"
    scene date 5pm 060
    pov "{i}Hahaha, shit...{/i}"
    bs "Martin...!"
    martin "What have you done!"
    bs "It's not what it looks like..."
    "Photographer" "Who's that?"
    pov "Her boyfriend."
    "Photographer" "Oh... Ohhh!"
    "Crowd" "Ohhhh...!"
    scene black
    "He storms off."
    bs "..."
    "You get dressed again under the blanket and go home together."
    "In total silence."
    $ dtime += 1
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5ntr:
    scene date 5pm 008n
    bs "Hm... now I have to choose one."
    pov "Me...?"
    "Man" "I can help you too!"
    "Girl" "Please choose me!"
    scene date 5pm 009n
    bs "Don't look at me like that [pov]!"
    bs "I can't choose you, you're to ugly, haha!"
    pov "{i}That bitch! Calling me out right here so everyone can hear it.{/i}"
    bs "Yes that would be a very hard threat to the photographer."
    "Man" "You're right he's ugly, take me!"
    bs "But maybe if he wears a bag over his head?"
    "Man" "I'LL DO IT!"
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene date 5pm 010n
    "Photographer" "Oh we've a volunteer!"
    bs "Huh?"
    pov "{i}There's someone really eager to do it, shouting out loud.{/i}"
    scene date 5pm 011n
    "Man" "Hi cute one! We'll do this now together. I choose you!"
    bs "Huh? But you..."
    "Photographer" "Great! And you two are photogenic. Let's start!"
    pov "{i}She seems to know him and isn't amused. Damn, he's reeking of alcohol.{/i}"
    "Man" "Come now. It's time to have some fun!"
    scene date 5pm 012n
    pov "{i}Damn, he's persistent. Is [bs] scared? Maybe he's dangerous?{/i}"
    pov "This guy seems to be known around town."
    "Girl" "He's an alcoholic and known for being a psycho."
    "Man" "Haha, poor girl."
    "Girl" "And no one will help her. Look at his muscles, he could kill someone."
    pov "{i}Hm, this is bad. Maybe I should stop this? What if he did bad things to her?{/i}"
    call screen cdate5ntrhelp

screen cdate5ntrhelp():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 420 ypos 116 action (Hide('cdate5ntrhelp'), Jump('cdate5ntryes')) hovered tt.Action ("Let her suffer") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 420 ypos 290 action (Hide('cdate5ntrhelp'), Jump('cdate5ntrno')) hovered tt.Action ("Stop this") focus_mask True
        frame:
            xalign .5
            text tt.value

label cdate5ntrno:
    scene black
    "NOTE: This part of the scene isn't finished yet. But it'll still abort the NTR scene."
    $ dtime += 1
    $ weekendactivities += 1
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5ntryes:
    pov "{i}No, I won't help her. She humiliated me in front of the crowd.{/i}"
    pov "{i}Now it's her turn to get humiliated! I bet this drunk pal will make her dream worse.{/i}"
    scene date 5pm 013n
    "Photographer" "Good, lay down and give me a motive."
    pov "{i}She's getting angry. Must be doing a photo-shoot with a drunkard.{/i}"
    pov "{i}Haha, she challenged it!{/i}"
    "Man" "Hm... you're really a damn hottie... hic"
    pov "{i}Hahaha, more humiliation.{/i}"
    "Photographer" "Oh come on... what's your names?"
    bs "I'm [bs]."
    "Man" "Oh [bs], hot! I'm Ed."
    "Photographer" "Please calm down Ed. We're trying here to make a photo-shoot pretending to be a loving couple."
    "Photographer" "So please act like that."
    "Ed" "But I'm... grrr..."
    scene date 5pm 014n
    pov "{i}Damn, what's he doing? Is he offended?{/i}"
    pov "{i}Don't give up so easy Ed!{/i}"
    "Girl" "What's Ed doing? Is he sleeping?"
    "Man" "Haha, yes he went to sleep because his girl is such a bitch!"
    "Man" "No, she's cute!"
    "Crowd" "Ed! Ed! Ed!"
    "Photographer" "[bs] please look at him. Damn!"
    scene date 5pm 015n
    bs "Hey wake up! Don't ruin this to me! You need to get serious."
    "Ed" "Hm... what?"
    bs "Stop being an idiot!"
    "Photographer" "Geez!"
    "Ed" "I just get ready!"
    "Photographer" "Get ready?"
    scene date 5pm 016n
    "Ed" "I undressed so we can start making out!"
    bs "Huh?"
    "Photographer" "What?"
    pov "{i}Shit, he's taking this shit to serious.{/i}"
    "Girl" "Is he naked?"
    "Man" "Yes he is. He wants to really get started!"
    scene date 5pm 017n
    "Ed" "Let me help you get that top off. Everyone's waiting."
    bs "Wait..."
    pov "{i}Wow, [bs] tits. And her nipple rings.{/i}"
    "Man" "Damn, girl that's hot!"
    "Girl" "She's a slut! Getting her nipples pierced like that!"
    "Man" "I don't care. I want to play with those boobs!"
    scene date 5pm 018n
    pov "{i}Damn, now he's holding her tight. But I'm sure he isn't that stupid to force her to something.{/i}"
    pov "{i}I mean there are so many people here.{/i}"
    "Crowd" "Yes, Ed. Ed! Ed!"
    pov "{i}But the crowd love what he's doing. I wonder what [bs] will do?{/i}"
    bs "I didn't mean..."
    "Ed" "Ssshh...! You're my girl now and we need to do what couples in love do!"
    bs "But I don't even know you..."
    "Ed" "Ok. I'm Ed and you're my slut now!"
    scene date 5pm 019n
    bs "HNNG...!?"
    "Man" "Yes the macho claims what's his!"
    "Girl" "Look at their kissing."
    pov "{i}What's she doing? Even the photographer isn't sure.{/i}"
    pov "{i}Normally she's bitching around and now she felt silent. Is she enjoying this?{/i}"
    scene date 5pm 020n
    "Photographer" "Are you alright [bs]?"
    "Ed" "Stop talking to my slut! Just take the photos you want to have!"
    "Photographer" "O... ok."
    "Crowd" "..."
    pov "{i}They're confused too.{/i}"
    bs "Please... hah... be gentle..."
    pov "{i}What? Is she really a slut?{/i}"
    "Man" "She loves it!"
    "Other man" "Maybe she got drunk from his kiss? Hahaha..."
    "Girl" "She needs to be guided by a strong man!"
    scene date 5pm 021n
    bs "Hah... you're so aggressive..."
    "Ed" "These nipples need to be bitten. You love the pain, you pierced them!"
    bs "Hah... hah..."
    pov "{i}Damn, he knows which buttons he needs to press.{/i}"
    "Man" "Yes! She likes it rough!"
    "Girl" "Give yourself in to that drunk sex god, haha."
    bs "Hnng..."
    scene date 5pm 022n
    "Ed" "Let me help you!"
    bs "Hnn..."
    "Man" "Good get her naked and ready to fuck!"
    pov "{i}Wow, he'll really fuck her and she's letting him do it.{/i}"
    pov "{i}But what's with that look she gives me?{/i}"
    pov "{i}Is she scared that she'll get fucked in front of all these people?{/i}"
    pov "{i}But she didn't fight against him, so I think she's horny and wants to get fucked.{/i}"
    if inc == True:
        pov "{i}Maybe she's embarrassed by the fact that her brother will see how she gets fucked.{/i}"
    else:
        pov "{i}Maybe she's embarrassed by the fact that I'll see how she gets fucked.{/i}"
    scene date 5pm 023n
    bs "Aaah..."
    "Ed" "Good, your pussy is already wet! You're a good slut!"
    "Photographer" "Damn who thought this would turn into a porn photo-shoot."
    "Crowd" "Yes, fuck her good!"
    "Ed" "I'll get a good lube on my dick for the main part."
    bs "Hah... the main... hah... part?"
    "Ed" "You slut bitched around before, so you haven't earned yourself a fuck in the pussy."
    bs "Huh?"
    scene date 5pm 024n
    "Ed" "Your other hole gets my dick!"
    bs "Aaaah... hah... slowly..."
    "Photographer" "Damn, that's good."
    "Ed" "I told you before, Mr. photographer! Hmm... these cute little toes!"
    bs "Aah... hah... hah..."
    "Man" "Wow, now we have anal!"
    "Girl" "You're a sex god Ed!"
    scene date 5pm 025n
    bs "Hnn... hah... hnng..."
    "Ed" "You like it in the ass, slut?"
    bs "Hm... yes... you're so deep in me!"
    "Crowd" "Anal-slut! Anal-slut!"
    pov "{i}She's lying! She can't like it having that drunkard fucking her ass!{/i}"
    "Ed" "Good. And keep your asshole tight for me!"
    bs "Hah... yes...!"
    scene date 5pm 026n
    "Ed" "Come here, so I can enter you deeper!"
    bs "Oh my god, hah... ahhh..."
    "Girl" "Yes do her! She's my idol now. Getting her ass plunged!"
    "Man" "Ride her harder!"
    bs "Yes... please harder. Fuck me harder!"
    "Ed" "As you wish my sexy slut!"
    scene date 5pm 027n
    bs "AAAHHH... HAAAHHH..."
    "Man" "She's like a pornstar. Milking a stranger with her ass!"
    "Girl" "That hot body. I want to lick all it all over."
    "Crowd" "Fuck harder! Fuck harder!"
    pov "{i}They can't be serious!{/i}"
    "Ed" "I'm about to cum slut! You'll take it in your bitch-mouth!"
    bs "Haaahh... yes..."
    scene date 5pm 028n
    bs "Bwaaaaah"
    "Ed" "YES!"
    "Man" "Damn, he's gagging her. Look at her mouth!"
    "Girl" "But she's taking him good and swallowing his sperm."
    "Another man" "She's like a pro! I love her!"
    "Crowd" "[bs]! [bs]! [bs]!"
    "Ed" "Drink it all!"
    bs "HNNG..."
    scene black
    "After some moments Ed leaves the scene."
    scene date 5pm 029n
    bs "Hmm..."
    "Girl" "Does it taste that good? Let me taste some too!"
    "Man" "She can't hear you. She's away, enjoying his cum."
    "Another girl" "This was the best photo-shoot ever!"
    "Crowd" "You're the best [bs]!"
    scene date 5pm 030n
    bs "You really like my show with Ed? How he fucked my asshole hard and give me his cum?"
    "Photographer" "Damn, girl!"
    "Crowd" "Yes! You're the best!"
    "Crowd" "[bs]! [bs]!"
    pov "{i}Damn, is she really thinking about a porn career after that?{/i}"
    scene black
    "After some time you leave this place, angry about [bs]."
    "You go home after the bad date."
    $ d5rcntr = True
    $ dtime += 1
    $ weekendactivities += 1
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5bj:
    if bigsiscorruption <= 70:
        pov "{i}No! I won't risk it now. A blowjob is OK also.{/i}"
    else:
        pov "{i}I'll take the blowjob. I want to see what she can do!{/i}"
    "After some more photos the two of you ended the photo-shoot."
    scene black
    "On your silent way home together [bs] looks very happy and deep in thoughts."
    "Then you can't hold it longer. A promise is a promise."
    scene date 5pm 002bj
    pov "Hey [bs]!"
    bs "..."
    pov "Hey, stop!"
    scene date 5pm 003bj
    bs "What's up?"
    pov "Look over there!"
    bs "Hm...?"
    pov "Behind you."
    scene date 5pm 004bj
    bs "What's with that corner?"
    pov "It would be the perfect place, don't you think so?"
    scene date 5pm 005bj
    bs "Hm... the perfect place...? For what?"
    pov "{i}Did she really forget it or is she trying to avoid it?{/i}"
    pov "Your promise. To suck me off!"
    scene date 5pm 006bj
    if inc == True:
        bs "You... you really want your older sister to suck you off?"
    else:
        bs "You... you really want me to suck you off?"
    pov "Yes as you promised. Don't play innocent, we both know how horny you were before."
    bs "But this was about the stormy situation, I felt excited then."
    pov "Stop lying to yourself... I helped you and you promised me a reward."
    scene date 5pm 007bj
    if inc == True:
        bs "Ok, you'll get your reward, pervy brother."
    else:
        bs "Ok, you'll get your reward, pervert."
    pov "{i}I knew it, she was just playing innocent! And she was damn horny before.{/i}"
    scene date 5pm 008bj
    bs "Come on let's get it over with."
    if inc == True:
        bs "If you want your sister to taste your dick so badly."
    else:
        bs "If you want me taste your dick so badly."
    pov "{i}Damn, she's teasing me. Maybe she really wants to have a taste?{/i}"
    scene date 5pm 009bj
    bs "Let me help you."
    pov "{i}Yes, she's starting it. I can't wait to see my dick in her mouth!{/i}"
    bs "Seems like you're already ready for this?"
    pov "Oh yes. I got so damn hard when I rubbed my dick on your ass."
    scene date 5pm 010bj
    bs "Haha, still the little pervert like in the past."
    if inc == True:
        bs "Want to do naughty things with his big sister all the time."
    else:
        bs "Want to do naughty things with me all the time."
    pov "Yes and I still want to!"
    bs "Then sit down there, so I can start."
    pov "{i}She's really doing it! There is no stormy or another forced situation now.{/i}"
    scene date 5pm 011bj
    bs "Huh? Damn!"
    pov "What's wrong [bs]?"
    bs "You're really packed down there..."
    pov "So you like my dick?"
    pov "{i}Damn, her warm hands and her hot breath are a thrill of anticipation.{/i}"
    scene date 5pm 012bj
    bs "Ha, I'm just surprised that your dick is so big."
    pov "But you'll suck it anyway! I want to feel your wet lips and tongue on it!"
    bs "Hm.. don't worry, I won't ruin your \"moment\"."
    pov "{i}She's cheeky! Maybe she needs a punishment.{/i}"
    pov "How about you start sucking and stop talking?"
    scene date 5pm 013bj
    if inc == True:
        bs "Geez! Relax brother."
    else:
        bs "Geez! Relax, [pov]."
    pov "{i}Oh yes! Her warm and wet tongue is touching my dick.{/i}"
    bs "<lick> <lick>"
    pov "A good start after I waited so long, haha."
    bs "Oh someone is getting cocky!"
    pov "Said by someone who's licking my dick."
    scene date 5pm 014bj
    bs "<lick> <lick>"
    pov "Ohhh..."
    pov "{i}She's licking my tip with her tongue, what a good feeling.{/i}"
    pov "Go on, time to take it in your mouth."
    bs "Hm..."
    scene date 5pm 015bj
    bs "<suck> <lick> Hmm..."
    pov "{i}Her wet mouth... And what a fantastic view.{/i}"
    if inc == True:
        pov "That's a very good place for you, sitting down there and sucking your brother's dick."
    else:
        pov "That's a very good place for you, sitting down there and sucking my dick."
    scene date 5pm 016bj
    bs "Hmm..."
    pov "Take it deeper in. Work on it and suck it properly!"
    bs "<suck> <suck>"
    pov "Or am I to big for your little mouth, haha."
    bs "Grrr..."
    pov "{i}Oh, she isn't amused that I'm in charge now, haha.{/i}"
    scene date 5pm 017bj
    pov "Oh yes! Very good!"
    bs "<suck>"
    pov "{i}I wonder if she's able to take it all in?{/i}"
    pov "How about you try to take it all in your hot, slippery mouth?"
    if inc == True:
        "Your sister signaled you that she won't do that."
    else:
        "[bs] signaled you that she won't do that."
    pov "Oh, come on!"
    pov "{i}Maybe I should help her? Or see what else she'll do?{/i}"
    call screen cdate5bjchoose

screen cdate5bjchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 594 ypos 167 action (Hide('cdate5bjchoose'), Jump('cdate5bjdt')) hovered tt.Action ("Help her (deepthroat)") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1331 ypos 167 action (Hide('cdate5bjchoose'), Jump('cdate5bjn')) hovered tt.Action ("Watch her") focus_mask True
        frame:
            xalign .5
            text tt.value

label cdate5bjn:
    pov "{i}I'll wait and see what she intend to do with me.{/i}"
    scene date 5pm 018bj
    pov "{i}Oh my god!{/i}"
    pov "Hnn... what a wonderful idea!"
    bs "<suck> Hm... <giggle>"
    pov "So you're enjoying this too?"
    bs "<giggle>"
    if inc == True:
        pov "Damn your skills are amazing, big sis!"
    else:
        pov "Damn your skills are amazing, [bs]!"
    scene date 5pm 019bj
    bs "<lick> Don't get too excited about it, I'll just try to finish you faster."
    pov "And you're doing a damn good job, hah...!"
    pov "Or do you like it working on my hard dick?"
    bs "Hm... It's really not that bad, but don't imagine something, little pervert."
    pov "{i}I knew it! And I bet she was horny before because of my hard dick too.{/i}"
    scene date 5pm 020bj
    bs "<kiss> <kiss>"
    pov "Yes kiss your lover, haha, hah... hah..."
    bs "<giggle> Not a bad joke."
    pov "Damn, that was worth the wait."
    bs "Are you about to come? Tell me before, I don't want to ruin my outfit."
    pov "Ok."
    scene date 5pm 018bj
    pov "{i}Damn, this is so damn hot! I'm so damn close, I'll cum any moment.{/i}"
    bs "<suck> <suck>"
    call screen cdate5bjcum

screen cdate5bjcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 480 ypos 104 action (Hide('cdate5bjcum'), Jump('cdate5bjcumin')) hovered tt.Action ("Just cum") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 729 ypos 104 action (Hide('cdate5bjcum'), Jump('cdate5bjcumout')) hovered tt.Action ("Warn her") focus_mask True
        frame:
            xalign .5
            text tt.value

label cdate5bjcumin:
    pov "{i}I don't care about her wish. I want to finish in her mouth.{/i}"
    pov "Hnng..."
    scene date 5pm 021bji
    bs "Huh?"
    if inc == True:
        "You start cumming into your sister's mouth."
    else:
        "You start cumming into [bs]'s mouth."
    pov "Ohh..."
    scene date 5pm 022bji
    bs "Hmm... hmm..."
    pov "{i}Wow, she's not getting angry. Just kneeling there and collecting my sperm in her mouth.{/i}"
    pov "{i}But I'm still cumming, her sucking was so amazing!{/i}"
    if inc == True:
        pov "I'm sorry that I didn't warn you, big sis."
    else:
        pov "I'm sorry that I didn't warn you, [bs]."
    pov "Because you did too good, I couldn't hold it any longer."
    bs "Hm..."
    pov "But please do me a last favor, show me what I gave you."
    bs "Hm..."
    scene date 5pm 023bji
    pov "Ohh..."
    bs "I don't understand why men are so obsessed to see their cum after?"
    pov "It's about the amount. When the girl was good, the man gives her extra."
    pov "Just like I gave you extra for that amazing blow-job."
    bs "Hmm..."
    scene date 5pm 024bji
    bs "<gulp>"
    pov "You... you swallowed it?"
    bs "Yes."
    pov "But... why? Because it tasted so good?"
    bs "<giggle> No. Just to see your unbelievable face, haha."
    bs "Men are so easily controlled!"
    if inc == True:
        pov "{i}But she swallowed my sperm. My big sister swallowed what I gave her!{/i}"
    else:
        pov "{i}But she swallowed my sperm. [bs] swallowed what I gave her!{/i}"
    bs "Come on, let's go home."
    scene black
    "You go home together."
    $ dtime += 1
    $ cdate5bj = True
    $ d5rcbjsw = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5bjcumout:
    if inc == True:
        pov "I'm there. I'm cumming, sis."
    else:
        pov "I'm there. I'm cumming [bs]."
    scene date 5pm 021bjo
    bs "Wait a second, I'll grab..."
    pov "Hnng..."
    bs "Huh?"
    pov "{i}Right on her face!{/i}"
    scene date 5pm 022bjo
    bs "Hnng..."
    pov "{i}What a wonderful view. My sperm all over her face. Now I marked her!{/i}"
    bs "Give me a tissue please... hm..."
    pov "Yes."
    pov "{i}Ha, she can't open her eyes now, I should take a picture, she won't complain because she won't know.{/i}"
    scene date 5pm 022bjox
    "You silently take a photo of her face covered with your sperm."
    pov "{i}Maybe I could use this some time.{/i}"
    scene date 5pm 023bjo
    bs "Why is it taking so long?"
    pov "{i}Oh she found a way to handle it. Good she didn't catch me.{/i}"
    pov "I... I was stunned by that view."
    if inc == True:
        bs "So you like the view of your sperm on your sister's face?"
    else:
        bs "So you like the view of your sperm on my face?"
    pov "Oh yes!"
    bs "Geez!"
    scene black
    "[bs] wiped her face clean with a tissue and you go home together."
    $ dtime += 1
    $ cdate5bj = True
    $ d5rcbjout = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5bjdt:
    pov "{i}It's time for her punishment for being so cheeky before. So she can learn her proper place.{/i}"
    scene date 5pm 018bja
    bs "Huh?"
    "You press her face onto your dick."
    "She's pushing her head back."
    pov "Don't fight back, I'm stronger. And so you'll learn to service me properly, faster."
    scene date 5pm 019bja
    bs "Hnng..."
    if inc == True:
        pov "Good sister! Take my dick deeper!"
    else:
        pov "Good girl! Take my dick deeper!"
    pov "Just let it happen and don't think about it don't bite or you could hurt yourself."
    scene date 5pm 020bja
    bs "<choke> HNNG..."
    pov "Stop fighting!"
    "You hold her hand."
    pov "{i}Wow my dick is all in her mouth. What a good feeling to dominate her!{/i}"
    pov "Relax! It'll be over soon and everything will be alright if you submit."
    "You start to fuck her mouth."
    scene date 5pm 021bja
    bs "<choke> Hng... hng..."
    pov "Good. Let me use your mouth."
    bs "Hmm...!"
    "She's still trying to press herself back."
    pov "Give up!"
    if inc == True:
        pov "Accept it that your brother has the control and uses you as his toy."
    else:
        pov "Accept it that I have the control and use you as my toy."
    pov "And don't panic. Your tears are a sign that you are overwhelmed by this new situation."
    pov "You'll get used too it."
    scene date 5pm 022bja
    pov "Very well, no more fighting back anymore. You accepted your fate."
    bs "Hnn... hnn..."
    pov "Soon you'll get your reward for being a good girl. I'll shoot my sperm down your throat."
    bs "Hmm..."
    pov "{i}Wow that answer sounded like a submissive agreement.{/i}"
    pov "Don't choke on it just swallow everything that comes."
    scene date 5pm 023bja
    pov "Here it comes!"
    pov "Hnng..."
    bs "<gulp> <gulp> Hnn..."
    if inc == True:
        pov "Swallow all! I've waited so long to use my bitchy sister like that."
    else:
        pov "Swallow all! I've waited so long to use your bitchy self like this."
    bs "HNNG..."
    "After she swallowed all, you let her head go."
    scene date 5pm 024bja
    bs "You asshole, why did you do that?"
    pov "Wow relax. You wanted to bribe me with a blow-job."
    bs "But not like that. You forced me!"
    pov "No I just decided how I wanted to do it."
    pov "And I know you loved it to be dominated!"
    bs "Are you crazy?"
    pov "You let it happen and swallowed it all like a good girl."
    bs "Fuck you!"
    scene black
    "She storms off and you go home alone."
    $ dtime += 1
    $ cdate5bj = True
    $ casbjdt += 1
    $ d5rcbjdt = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5normend:
    scene black
    bs "Stop it you asshole!"
    pov "{i}Shit, that was too soon. I need to corrupt her more before I try again.{/i}"
    "Photographer" "You better show some manners [pov]."
    "[bs] get dressed and leaves the place."
    bs "You damn asshole ruined my chance."
    "After you accepted your mistake you go home alone."
    $ dtime += 1
    $ d5rccor = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose


label cdate5bno:
    scene date 5pm 031a
    $ bigsislove += 1
    pov "{i}No, I'd love to get her back to her old personality. So I don't want her to get any more slutty.{/i}"
    pov "{i}Also I'm not sure what's gonna happen when she gives in to the crowd's wishes.{/i}"
    pov "{i}There so many bad perverts out there.{/i}"
    scene date 5pm 033b
    bs "Huh?"
    if inc == True:
        pov "<whisper> Relax, big sis. There is no need to whore yourself out for them."
    else:
        pov "<whisper> Relax, [bs]. There is no need to whore yourself out for them."
    bs "<whisper> But I..."
    pov "<whisper> I know that you feel uncomfortable and there's no need to deny it."
    bs "<whisper> But..."
    scene date 5pm 034b
    pov "<whisper> Hey! I won't allow you do something that might give you a bad reputation."
    bs "<whisper> Oh...?"
    if inc == True:
        pov "<whisper> Maybe we're fighting often but I'm still your brother, so I'll support you everytime."
    else:
        pov "<whisper> Maybe we fight often but we have known each other since childhood, so I'll support you every time."
    pov "<whisper> And I think the slower way to your goals will suit you better."
    if inc == True:
        pov "<whisper> And I love you, big sis."
    else:
        pov "<whisper> And I love you, [bs]."
    scene date 5pm 035b
    bs "<whisper> Hmm..."
    pov "<whisper> You know that I'm right!"
    pov "{i}Now she's confused! Hearing such good words from me.{/i}"
    bs "..."
    pov "<whisper> I won't throw you under the bus. You can trust me with this."
    bs "<whisper> T... thank you..."
    if bigsislove <= 30:
        jump cdate5loveend1
    scene date 5pm 036b
    pov "Huh?"
    bs "<kiss>"
    "Crowd" "Woohoo!"
    "Photographer" "At least something I can work with."
    pov "{i}She's kissing me. Why? Was my speech that good?{/i}"
    scene date 5pm 037b
    pov "<whisper> Why did you do that?"
    bs "<whisper> B... because I wanted to!"
    pov "<whisper> I'm confused."
    bs "<whisper> It's my decision to show them something and I want you to participate with me."
    bs "<whisper> When you're honest and want the best for me so you can show it now."
    pov "{i}She wants me to pretend to make out with her? Or is this a trap?{/i}"
    pov "<whisper> So more kissing?"
    scene date 5pm 038b
    bs "<whisper> Don't be so shy. You can grab them, I know you want too."
    "She lays your hand on her breast."
    pov "<whisper> Wow..."
    bs "<giggle>"
    "Crowd" "Yes go on. Play with her boobs!"
    pov "<whisper> So you really want to make out with me?"
    bs "<whisper> Pretend to make out. Don't lay your hopes in it."
    bs "<whisper> I'll let you decide how I present myself in this photo-shoot."
    bs "<whisper> I hope you won't use me!"
    pov "<whisper> Never!"
    scene date 5pm 039b
    pov "<whisper> Come here!"
    if inc == True:
        "You french kiss your sister."
    else:
        "You french kiss her."
    bs "Hnng..."
    pov "{i}Damn, I cant believe it. But I must take care to don't overdo it.{/i}"
    "Girl" "Wow, they started!"
    "Man" "I want to lay my hands on those boobs too."
    scene date 5pm 040b
    pov "Huh?"
    "Man" "Haha, she's taking the lead."
    "Girl" "I want to be that confident too!"
    bs "<whisper> I'm still surprised about your speech before. You said you love me."
    bs "<whisper> Show me! Show me how bad you want me!"
    pov "{i}Damn, now she's teasing me. I'll surprise her with gentle actions.{/i}"
    scene date 5pm 041b
    pov "<suck>"
    bs "Hah... Hm...!"
    "Crowd" "What are you doing? We want to see too!"
    pov "<bite gently>"
    bs "Hng... hah..."
    "Photographer" "That's perfect. You're talented!"
    scene date 5pm 042b
    pov "<whisper> See how much I want you?"
    bs "<giggle> What a pleasant surprise."
    if inc == True:
        bs "<whisper> My little brother is a gentleman in bed."
    else:
        bs "<whisper> You're a gentleman in bed."
    pov "<whisper> Oh, there will be more. If you want it."
    scene date 5pm 043b
    bs "<whisper> You really want to do more?"
    if inc == True:
        bs "<whisper> After you made out with your sister so shamelessly? <giggle>"
    else:
        bs "<whisper> After you made out with me so shamelessly? <giggle>"
    pov "<whisper> Oh yes!"
    "Crowd" "Go on, continue your make out! We want more!"
    bs "<whisper> You heard them? <giggle>"
    bs "Then go on, surprise me some more."
    pov "<whisper> As you wish!"
    scene date 5pm 044b
    pov "<kiss> <lick>"
    "You caress her chest gently."
    bs "Hm... hm..."
    bs "<whisper> What a nice feeling..."
    pov "<whisper> You love to get kissed, don't you?"
    bs "<whisper> Hah, yes..."
    "Your hand go slowly down."
    bs "<whisper> Go on. Try to conquer me. <giggle>"
    scene date 5pm 045b
    bs "<whisper> Ohh... you're there."
    pov "<whisper> And you're wet. Surprisingly! I can feel it through your pants."
    bs "<whisper> And you wonder after all you've done? <giggle>"
    bs "<whisper> But I wonder if you brave enough to go even further?"
    pov "<whisper> You know I shouldn't after what I told you before about the Crowd."
    bs "<whisper> So you need me to talk you into? When it stays under the blanket no one will know."
    if inc == True:
        pov "{i}Wow, my sister wants me to touch her pussy!{/i}"
    else:
        pov "{i}Wow, [bs] wants me to touch her pussy!{/i}"
    scene date 5pm 046b
    pov "<whisper> Say no more!"
    "You slip your hand in her pants and caress her clit gently."
    bs "Haahh...!"
    "Crowd" "Yes, they're doing something!"
    "Girl" "She moans so hot. I want to do her too!"
    "Man" "They're just pretending!"
    pov "{i}Oh...?{/i}"
    pov "<whisper> After years of waiting I finally can touch your sweetest spot!"
    bs "<whisper> Yes, go on. Adore me more! <giggle>"
    pov "<whisper> I know something better!"
    scene date 5pm 047b
    bs "Hnn..."
    pov "<whisper> Now I conquer you!"
    if inc == True:
        bs "<whisper> Hah... you're a bad brother. Fingering your older sister. <gig...> hah..."
    else:
        bs "<whisper> Hah... you're a bad guy. Fingering me after we've known each other for so long. <gig...> hah..."
    pov "<whisper> Oh I won't stop there! I'll conquer you more until my dick has his new home in your beautiful, wet pussy."
    bs "Hnng... hah..."
    pov "<whisper> I want to shoot my sperm into you so often until you're my girlfirend."
    pov "<whisper>Because I love you so much!"
    bs "Hnn... hnng..."
    if inc == True:
        bs "<whisper> But you're my brother!"
        pov "<whisper> I don't care! It can be a secret relationship, but I want to be with you!"
    else:
        bs "<whisper> But my mom won't allow that!"
        pov "<whisper> I don't care! It can be a secret relationship, but I want to be with you!"
        martin "What are you doing, [bs]?"
    scene date 5pm 060
    bs "Martin!"
    martin "This can't be, nooo!"
    scene black
    "Martin storms off."
    if martingood >= martinbad or martinbad > martingood and bigsislove < 50:
        jump cdate5loveend2
    elif martinbad > martingood and bigsislove >= 50:
        bs "..."
    pov "<whisper> You don't want to follow him?"
    bs "No, I'm here with you now. Just continue and pretend that never happened."
    pov "{i}Oh my god, I can't believe it. She must be very excited to dump him.{/i}"
    scene date 5pm 048b
    bs "<whisper> Oh, you're very excited too!"
    pov "<whisper> Hm... your hand feels so good on my crotch."
    bs "<whisper> If I take it out now... hah... would you fuck me?"
    pov "<whisper> No! I mean yes! But not here. When we're alone."
    pov "<whisper> In a more romantic place. And then we would make love."
    pov "<whisper> I would take my time and have long foreplay, licking each inch of your beautiful body."
    pov "<whisper> And then we would connect and enjoy each other all night long."
    bs "Hnng..."
    scene date 5pm 049b
    pov "<whisper> So you're eager to feel it?"
    bs "<whisper> Not bad! <giggle>"
    pov "<whisper> Oh, now you're teasing me!"
    bs "<whisper> You're teasing me all the time. <giggle>"
    pov "<whisper> So I earned you pleasuring me too?"
    bs "<whisper> We'll see..."
    pov "<whisper> So then I must do better!"
    scene date 5pm 050b
    bs "Hnn... haaah..."
    "You rub her faster."
    bs "Hnng..."
    "She starts stroking your dick."
    pov "<whisper> What a nice reaction."
    pov "<whisper> Am I doing that good?"
    bs "<whisper> Hah... yes..."
    pov "<whisper> You're shaking, are you about to cum?"
    bs "<whisper> Yes! Hah!"
    pov "<whisper> But I'm not sure I want to see you cum in public."
    bs "<whisper> Please don't stop yet! They all still think we're pretending."
    pov "<whisper> As you wish!"
    scene date 5pm 051b
    bs "AAAAHHH...!"
    if inc == True:
        pov "<whisper> Good, cum for me, big sis!"
    else:
        pov "<whisper> Good, cum for me, [bs]!"
    "Crowd" "Wow, she's cumming!"
    "Man" "I knew they were playing with each other under the blanket!"
    "Girl" "I'm sure she's faking it."
    scene date 5pm 052b
    bs "Hah... hah..."
    if inc == True:
        bs "<whisper> You did very good brother!"
    else:
        bs "<whisper> You did very good [pov]!"
    pov "<whisper> As I told you, I'm good for you."
    if inc == True:
        bs "<whisper> But you're a bad, bad brother. Fingering your sister to cum. <giggle>"
    else:
        bs "<whisper> But you're a bad, bad boy. Fingering your friend to cum. <giggle>"
    pov "<whisper> It needs to be done on my way to conquering you!"
    bs "<whisper> I like that. And so you have earned a treat."
    pov "<whisper> Oh now I'm curious."
    "She starts stroking your dick faster and faster."
    bs "<whisper> Oh you know exactly what will happen, your dick is twitching in my hand."
    scene date 5pm 053b
    pov "<whisper> Hnng..."
    bs "<whisper> I can feel your sperm coming."
    "Girl" "Look at him, he's getting a release too!"
    "Man" "He's just playing, I know it!"
    "Crowd" "What a hot show!"
    scene date 5pm 054b
    bs "<whisper> And how do you feel now?"
    if inc == True:
        bs "<whisper> Marked your sister with your cum!"
    else:
        bs "<whisper> Marked me with your cum!"
    pov "<whisper> Satisfied, for now!"
    pov "<whisper> But I will not stop conquering you until you're my girlfriend!"
    bs "<giggle> Now I'm curious."
    pov "I love you [bs]!"
    bs "Hnn..."
    scene black
    "You dress yourselves and go home together."
    "[bs] is awkwardly silent the whole time."
    $ dtime += 1
    $ cdate5hj = True
    $ d5rclovef = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5loveend1:
    scene date 5pm 035b
    bs "<whisper> But I don't want to do it anymore... Something feels wrong."
    pov "<whisper> Huh?"
    pov "{i}What does she mean? Did she get uncomfortable by my good behavior at this intimate moment?{/i}"
    bs "<whisper> I'm sorry."
    scene black
    "[bs] gets dressed and leaves the place."
    "Photographer" "What happened?"
    pov "I'm not sure."
    "Crowd" "Booo!"
    pov "{i}Maybe my speech revealed some feelings in her and she couldn't handle this new situation?{/i}"
    pov "{i}I'm sure I need to get her love higher.{/i}"
    "You also go home."
    $ d5rclove = True
    $ dtime += 1
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5loveend2:
    scene black
    bs "Wait...!"
    "[bs] dresses quickly and follows him."
    "Photographer" "What happened?"
    pov "I'm not sure."
    pov "{i}Damn, and I thought she would be in love with me. Why does he have to interfere?{/i}"
    pov "{i}Maybe I need help it a bit and interfere in their relationship.{/i}"
    "You also go home."
    $ dtime += 1
    $ d5rclovem = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose