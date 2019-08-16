#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. Time Location - Featured - Scenes
#----- End List -----

#----- Start of the Weekend ----- DONE
label weekendstart:
    #----- Added 0.7.0 -----
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
    #----- end -----
    $ weekendactivities = 0 #----- added -----
    hide screen locations
    scene black
    "The weekend has begun."
    $ dtime = 9
    "You wake up and go downstairs."
    jump breakfast

label weekendskip:
    $ weekend = False
    $ nicoleweekendntrevent = False
    $ weekendactivities = 0
    $ messagenicolentr = 0
    $ activatesubwayntr = 0
    $ activatesecretplacentr = 0
    $ messagedavidentr = 0
    $ replydavidentr = 0
    $ day = 1
    if adatekiss == True and d1ranormal == False and d1ralove == False and d1racor == False and d1racorf == False and d1rantrdavideyb == False and b4ralove == False and b4racor == False and b4rantrdaviden == False and b4rantrdavidey == False and b4rantrdavidei == False:
        $ dtime = 6
        jump alexismcroomsurprise
    elif d1ranormal == True or d1ralove == True or d1racor == True or d1racorf == True or d1rantrdavideyb == True or b4ralove == True or b4racor == True or b4rantrdaviden == True or b4rantrdavidey == True or b4rantrdavidei == True:
        $ dtime = 6
        jump alexisreac
    elif d9rnntri == True or d9rnntr == True or d9rncor == True or d9rncorf == True or d9rnlove == True or d9rnlovef == True or b9rnntr == True or b9rnntrmir == True or b9rnlove == True or b9rncor == True:
        $ dtime = 62
        jump nicolereac
    else:
        $ dtime = 7
        jump mcroom

#----- Weekend Darker Path Events - Irina and Alexis Lesbian Date 2 - are now accessible from a phone message on the weekend -----

#----- Weekend Introduction ----- DONE
label breakfast:
    scene weekend 9am 001
    mom "Good morning [pov]. I'm glad you're finally awake!"
    pov "Good morning..."
    ls "Oh, still sleepy? <giggle>"
    mom "Come and sit down. Have some breakfast."
    scene weekend 9am 002
    pov "It's so quiet today."
    mom "It's the weekend. We can relax and just enjoy the peace."
    scene weekend 9am 003
    mom "Are you going to go to your friend's house this weekend?"
    pov "Friend's house?"
    mom "Yes, a friend from school. She spends nearly every weekend with her and her parents."
    mom "We miss her, but it's nice to have the house to myself sometimes too."
    scene weekend 9am 004
    ls "Yes I am. This weekend is going to be so much fun. And I think you've earned yourself some free time, mom, haha."
    mom "Haha, thanks."
    povi "I wonder what she'll do with all that free time?"
    scene weekend 9am 005
    mom "And you said you're hanging out with [irina] again? I hope you won't do anything reckless."
    scene weekend 9am 006
    bs "Mom! We never do anything crazy anyway. We're just having some fun."
    povi "Having fun with [irina]. I wonder what they want to do?"
    scene weekend 9am 007
    mom "And what are you want to do this weekend?"
    pov "I don't know... yet..."
    mom "Well you have the house all to yourself, mostly. The guys are out of town to do some work."
    pov "Out of town?"
    mom "Yes, Bruce is with them every weekend. They go to nearby citys for work"
    pov "Oh."
    scene weekend 9am 008
    if inc == True:
        mom "Maybe you can spend some time with your dear old mom this weekend."
    else:
        mom "Maybe you can spend some time with little old me this weekend."
    mom "Or have you found someone special already?"
    pov "What?"
    mom "Maybe a girl you want to spent some time with this weekend?"
    ls "<giggle>"
    scene black
    "Developers Note:" "Here would be an event to start off the weekend."
    "Developers Note:" "Unfortunately it's too buggy to play right now, so it's disabled in this version."
    "Developers Note:" "You can now choose between several weekend activities."
    "Developers Note:" "Some of them need certain requirements to play them."
    "Developers Note:" "You can do three weekend events, then the weekend will finish and you will continue on to Monday."
    if NTR == True and ndate21ntrsex == True and nicoleweekendntrevent == False:
        $ messagepush = True
        $ messagenicolentr = 1
        $ nicolenotification += 1
    elif NTR == True and ndate21ntrhelped == True and nicoleweekendntrevent == False:
        $ messagepush = True
        $ messagenicolentr = 1
        $ nicolenotification += 1
    elif NTR == True and nicoleweekendntrevent == False and momrelationship <= 5 or nicoleweekendntrevent == False and hardntr == True: #----- updated -----
        $ messagepush = True
        $ messagenicolentr = 1
        $ nicolenotification += 1
    else:
        pass
    if NTR == True and secretplace2pmntrfirst == True and lilsisrelationship <= 5 or secretplace2pmntrfirst == True and hardntr == True: #----- updated -----
        $ messagepush = True
        $ messagedavidentr = 1
        $ davidenotification += 1
    jump weekendacchoose

label weekendacchoose:
    $ weekend = True
    scene weekendblack
    show screen phone
    call screen weekendblackchoose

#----- Edited -----
screen weekendblackchoose():
    default tt = Tooltip ("")

    fixed:
        if money >= 200:
            imagebutton auto "gui/icons/wnicole_%s.png" xpos 300 ypos 190 action (Hide('weekendblackchoose'), Jump('ndate21goyes')) hovered tt.Action ("Go with [mother] on your first date") focus_mask True
        if money < 200:
            imagebutton auto "gui/icons/wnicolex_%s.png" xpos 300 ypos 190 action NullAction() hovered tt.Action ("$200 are needed for your first date") focus_mask True
        if gangmember == False and mombasementfirst == True or gangmember == True and mombasementfirst == False or gangmember == False and mombasementfirst == False:
            imagebutton auto "gui/icons/wnicolex_%s.png" xpos 300 ypos 456 action NullAction() hovered tt.Action ("You need to be a gangmember and completed her Corruption basement event as a gangmember | [cr1] Date") focus_mask True
        if gangmember == True and mombasementfirst == True:
            #----- edited ----- jump('nicoleweekendcor')
            imagebutton auto "gui/icons/wnicole_%s.png" xpos 300 ypos 456 action (Hide('weekendblackchoose'), Jump('nicolecorruptiondate2choice')) hovered tt.Action ("Have a second date with [mother] [cr1]/[lv1]") focus_mask True
        if momlove < 80 and ndate21 == False or momlove < 80 and ndate21 == True or momlove >= 80 and ndate21 == False:
            imagebutton auto "gui/icons/wnicolex_%s.png" xpos 300 ypos 729 action NullAction() hovered tt.Action ("80 or more love points are needed and you need to been with her on the first date | [lv1] Date") focus_mask True
        if momlove >= 80 and ndate21 == True:
            #----- edited ----- jump('nicoleweekendlove')
            imagebutton auto "gui/icons/wnicole_%s.png" xpos 300 ypos 729 action (Hide('weekendblackchoose'), Jump('nicolecorruptiondate3choice')) hovered tt.Action ("Have a second date with [mother] [lv1]/[cr1]") focus_mask True

        if money < 20:
            imagebutton auto "gui/icons/walexisx_%s.png" xpos 680 ypos 190 action NullAction() hovered tt.Action ("$20 are needed for your first date") focus_mask True
        if money >= 20:
            imagebutton auto "gui/icons/walexis_%s.png" xpos 680 ypos 190 action (Hide('weekendblackchoose'), Jump('adate1goyes')) hovered tt.Action ("Go with [ls] on your first date") focus_mask True
        if adate == False and lilsislove < 50 or adate == False and lilsislove >= 50 or adate == True and lilsislove < 50:
            imagebutton auto "gui/icons/walexisx_%s.png" xpos 680 ypos 456 action NullAction() hovered tt.Action ("50 or more love points are needed and you need to been with her on the first date | [lv1] Date") focus_mask True
        if adate == True and lilsislove >= 50:
            #----- edited ----- jump('alexisweekendlove')
            imagebutton auto "gui/icons/walexis_%s.png" xpos 680 ypos 456 action (Hide('weekendblackchoose'), Jump('alexisdate2choice')) hovered tt.Action ("Go with [ls] on your second date [lv1]/[cr1] Date") focus_mask True

        imagebutton auto "gui/icons/wcassandra_%s.png" xpos 1060 ypos 190 action (Hide('weekendblackchoose'), Jump('cdate5')) hovered tt.Action ("Go with [bs] on your first date") focus_mask True
        if basecasfirst == False and bigsislove > bigsiscorruption and bigsislove >= 50 or basecasfirst == True and bigsislove <= bigsiscorruption and bigsislove >= 50 or basecasfirst == True and bigsislove > bigsiscorruption and bigsislove < 50:
            imagebutton auto "gui/icons/wcassandrax_%s.png" xpos 1060 ypos 456 action NullAction() hovered tt.Action ("50 or more love points are needed and you must invite her to the basement before") focus_mask True
        if basecasfirst == True and bigsislove > bigsiscorruption and bigsislove >= 50: #----- casweekendfirst changed to casweekendfirst_landing -----
            imagebutton auto "gui/icons/wcassandra_%s.png" xpos 1060 ypos 456 action (Hide('weekendblackchoose'), Jump('casweekendfirst_landing')) hovered tt.Action ("Meet with [bs] [lv1]/[cr1]") focus_mask True

        if activatesecretplacentr == True:
            imagebutton auto "gui/icons/walexis_%s.png" xpos 1460 ypos 190 action (Hide('weekendblackchoose'), Jump('secret4pmntr')) hovered tt.Action ("Spy on Davide and [ls]") focus_mask True
        if activatesubwayntr == True:
            imagebutton auto "gui/icons/wnicole_%s.png" xpos 1460 ypos 456 action (Hide('weekendblackchoose'), Jump('nicoleweekendntr')) hovered tt.Action ("Look after [mother] at the subway") focus_mask True

        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 932 ypos 948 action (Hide('weekendblackchoose'), Jump('weekendskip')) hovered tt.Action ("Skip weekend | Jump to monday") focus_mask True

        #----- Custom Scene -----
        if momlove >= 100 and mombasementlovesecond == True or momcorruption >= 100 and mombasementcorsecond == True:
            imagebutton auto "images/edited/icons/nicole_%s.png" xpos 200 ypos 729 action (Hide('weekendblackchoose'), Jump('bonuslroomnicole')) hovered tt.Action ("Bonus Living Room Scene with [mother] [lv1]/[cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate21choose:
    hide screen locations
    if dtime == 7 or dtime == 8:
        scene main mc room morning
    else:
        scene main mc room day
    "It'll cost you $200 to go on a date with [mother]."
    call screen ndate21choose1

screen ndate21choose1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        if money >= 200:
            imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('ndate21choose1'), Jump('ndate21goyes')) hovered tt.Action ("Go on a date with [mother]") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('ndate21choose1'), Jump('ndate21gono')) hovered tt.Action ("Don't go") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if money >= 20:
            imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('adate1choose1'), Jump('adate1goyes')) hovered tt.Action ("Go on a date with [ls]") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('adate1choose1'), Jump('adate1gono')) hovered tt.Action ("Don't go") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1goyes:
    $ money -= 20
    jump adate1

label adate1gono:
    jump mcroom

#----- Nicole Date -----
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
        "You go on a date with your mother..."
    else:
        "You go with on a date with [mother]..."
    "You arrive at the restaurant you chose for the occasion."
    scene date 21pm 001 #egyptian entrance
    mom "Oh look. They're dressed like Ancient Egyptians."
    pov "Yeah, that's pretty cool."
    "Waitress" "Welcome to our temple, friends of Egypt."
    mom "Ohh..."
    scene date 21pm 002 #egyptian hostess
    "Waitress" "Please follow me. Your table is set."
    mom "And these fires, it's like we're in a forgotten time."
    pov "Yes, it really lives up to it's reputation."
    scene date 21pm 003 #arm around mother - hostess in distance
    if inc == True:
        pov "I'm so glad we're doing this Mom."
    else:
        pov "I'm so glad we're doing this [mother]."
    mom "Me too. I really wanted some alone time with you all to myself!"
    mom "This place is huge! This feels like an exclusive club house or grand hall."
    pov "Yes, they are only open for reservations."
    mom "Wow, I just need a moment to take it all in."
    pov "Take all the time in the world. Nothing is too good for my beautiful date."
    mom "You're so sweet, [pov]!"
    jump ndate21ass

label ndate21ass:
    scene date 21pm 003
    call screen ndate21ass2

screen ndate21ass2():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('ndate21ass2'), Jump('ndate21ass3')) hovered tt.Action ("Look at her ass") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('ndate21ass2'), Jump('ndate221')) hovered tt.Action ("Don't") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate21ass3:
    scene date 21pm 003a #hostess ass
    povi "Damn, half her ass is hanging out... The Ancient Egyptians had good taste in clothes!"
    jump ndate221

label ndate221:
    scene date 21pm 004 #mom touching sarcophagus
    mom "Look! This sarcophagus looks so realistic."
    mom "Do you think there is a Mummy in here? Just waiting to come out and get us?"
    pov "Probably! I hear theere is a curse too!"
    pov "If you steal it's treasure, the Mummy will use all the powers of the desert to hunt the thief down and take it back by killing them!"
    mom "Oh that sounds awful! But it's treasure has to be worth a fortune! Might be worth the risk."
    pov "I think I already have the greatest treasure of them all..."
    "You just stare at her intently, enjoying the view."
    mom "Why are you just staring at me... oh. You mean me!"
    mom "Well aren't you the little charmer tonight. You're too sweet, [pov]."
    povi "Who would have thought all those goofy evil mummy movies would come in handy one day!"
    "You two continue through the massive lobby and follow the hostess to your table."
    scene date 21pm 005 #hostess and table
    "Waitress" "Here's your table. With the wine you requested. We'll be bringing tonight's first course shortly."
    mom "So lovely! And you even ordered red wine, you're so thoughtful!"
    pov "Ok. Thank you."
    mom "You ordered the dinner already?"
    pov "Well, I hope you don't mind."
    pov "But I hear the chef here renowned for his full course meals."
    pov "Each night is a unigue adventure, I hoped we'd try that together if you are game?"
    mom "Oh, yes I definitely am. I'm so excited!"
    scene date 21pm 006 #mom and table
    mom "I still can't believe it that you brought me to such an exquisite place for our date."
    mom "You didn't have to do all of this for me. I would be happy anywhere with you!"
    if inc == True:
        pov "You're the most wonderful woman I know. There is nobody else I'd want to do this with, Mom."
    else:
        pov "You're the most wonderful woman I know. There is nobody else I'd want to do this with, [mother]."
    mom "<giggle> You're such a flatterer, I like that."
    pov "And I would be remise if I didn't mention how much I like that dress. It's stunning!"
    mom "Oh, well I bought it special for tonight. I didn't know if it was a bit too much for the occasion..."
    pov "I think it's perfect!"
    scene date 21pm 007 #mom at table smile left are up
    mom "I'm still wondering why you choose such a special location for our date?"
    mom "But don't worry, I love it here so far, so it was a great choice."
    pov "Well I remember our life before this undercover business and you would talk about going to places like this."
    pov "And I thought you should enjoy it from time to time. You deserve it!"
    scene date 21pm 008 #mom and son clicking glasses of wine
    mom "You're right. Bruce can't take me to such a nice place. That would be too suspicious."
    mom "Honestly, I don't even know if he would take me somewhere like this if he could these days..."
    pov "Hey! None of that! This is a special night with a special woman!"
    pov "Besides, it's my pleasure to get to spoil you from time to time!"
    mom "<giggle> Let's drink to that."
    pov "To my beautiful date!"
    mom "Mine too!"
    scene date 21pm 009 #mom drinking wine
    mom "Hm... <drink>"
    pov "Do you like it? I was pretty sure I figured out your favorite..."
    mom "Hm... hm..."
    jump ndate221l

label ndate221l:
    scene date 21pm 009
    call screen ndate221l1

screen ndate221l1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('ndate221l1'), Jump('ndate221closer')) hovered tt.Action ("Look closer") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('ndate221l1'), Jump('ndate321')) hovered tt.Action ("Don't") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate221closer:
    if spot1000anim == True:
        image date 21pm 009aa = Movie(channel="date 21pm 009aa", play="edited/anim//spot1000/date/21pm 009aa.webm")
        scene date 21pm 009aa with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm 009a #close up of mom breasts at table
    povi "Damn, that dress!"
    if momcorruption > momlove and momcorruption >= 20:
        scene date 21pm 010a #mom at table arms down - neutral face
        mom "Found what you're looking for?"
        pov "Haha, I'm just admiring your dress."
        mom "I'm really glad you like it."
    elif momlove > momcorruption and momlove >= 20:
        scene date 21pm 010b #mom at table arms down - neutral face
        mom "Sweetie, are you lost?"
        pov "Haha, Sorry about about that. I was just admiring your dress."
        mom "It's ok... I knew what I was getting into when I bought it. Haha!"
    else:
        scene date 21pm 010b #mom at table arms down - happy face
        mom "Please stop staring at me like that."
        pov "Oh, I was just admiring your dress."
        mom "It's ok. But maybe not so much out in public."
        povi "Out in public... Would it be ok at home then?"
        pov "Ok, sure."
    jump ndate321

label ndate321:
    scene date 21pm 011 #other couple in the distance
    mom "Oh look! There's another couple here too."
    pov "I see them too."
    mom "It's crazy how spacious this place is. Even with multiple guests you still feel like it's all just for you."
    scene date 21pm 012 #close up of other couple - guy staring
    povi "That creepy guy is just staring at us!"
    scene date 21pm 013 #mom at table hands together - neutral face
    mom "What is it?"
    pov "I was just wondering about that creepy guy just staring at us."
    mom "Oh yes, I noticed that too! I was worried we had something weird going on with us over here."
    if inc == True:
        pov "No I know why he's staring at us. You look so damn beautiful, mom!"
    else:
        pov "No I know why he's staring at us You look so damn beautiful, [mother]!"
    scene date 21pm 014 #mom at table right arm up, smile
    mom "You're just full of compliments tonight."
    pov "Is it too much? I just feel that you haven't been getting your fair share of them at home these days."
    mom "Thank you! It's so good to be with someone who treats me as good as you do."
    mom "And to step away from the situation at home."
    pov "I'm here for you, always. No matter if it's at home or enjoying an evening out. We'll see better times again soon!"
    mom "Oh... better times..."
    "Waitress" "Excuse me..."
    scene date 21pm 015 #mom at table right arm up, smile looking at hostess with food
    "Waitress" "Here's your first course."
    mom "Thank you... and it smells so good."
    pov "Yes it does! I'm excited to try it!"
    mom "Hmm..."
    scene date 21pm 016 #mom and hostess at the table looking at you
    "Waitress" "Here for you, Sir."
    pov "Thank you."
    mom "Hnnn..."
    if inc == True:
        pov "Why is mom looking at me like that?"
    else:
        pov "Why is [mother] looking at me like that?"
    if momcorruption > momlove and momcorruption >= 30:
        if spot1000anim == True:
            image date 21pm 009aa = Movie(channel="date 21pm 009aa", play="edited/anim//spot1000/date/21pm 009aa.webm")
            scene date 21pm 009aa with dissolve:
                size (config.screen_width, config.screen_height)
            pause
        else:
            scene date 21pm 017a #mom holding her breasts at table
        mom "Hahaha, here I am! When you're with me you can stare at my breasts. No need to stare at the waitress too."
        pov "What...?"
        mom "Hahaha, I'm just joking around with you!"
        pov "Oh..."
        jump ndate321joke
    elif momlove > momcorruption and momlove >= 30:
        if spot1000anim == True:
            image date 21pm 017aa = Movie(channel="date 21pm 017aa", play="edited/anim//spot1000/date/21pm 017aa.webm")
            scene date 21pm 017aa with dissolve:
                size (config.screen_width, config.screen_height)
            pause
        else:
            scene date 21pm 017a #mom holding her breasts at table
        mom "Hahaha, You know I bought this dress for you! No need to stare at the waitress when I'm right here for you!"
        pov "What...?"
        mom "Hahaha, I'm just teasing you sweetie!"
        pov "Oh..."
        jump ndate321joke
    else:
        scene date 21pm 017b #mom at table hands down, smile (No wine)
        mom "Oh, I see the waitress caught your eye!"
        pov "Huh?"
        mom "Maybe she could be a possible girlfriend for you?"
        pov "A girlfriend for me?"
        mom "Yes, don't you want a girlfriend now that you're home?"
        jump ndate321gf

label ndate321gf:
    scene date 21pm 017b #mom at table hands down, smile (No wine)
    call screen ndate321gf1

screen ndate321gf1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('ndate321gf1'), Jump('ndate321gflove')) hovered tt.Action ("Flirty comment [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('ndate321gf1'), Jump('ndate321gfno')) hovered tt.Action ("Agree with her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate321gflove:
    scene date 21pm 017b #mom at table hands down, smile (No wine)
    pov "But I'm here with the only woman I'm interested in!"
    scene date 21pm 018b #mom at table left and on ear, smile - shy
    mom "You... you mean with me...?"
    if inc == True:
        pov "Yes! I love you mom! I would prefer you as my girlfriend over anyone else, even if it's just for the night!"
        mom "Oh stop it! I'm your mother, I can't be your girlfriend."
    else:
        pov "Yes! I love you [mother]! I would prefer you as my girlfriend over anyone else, even if it's just for the night!"
        mom "Oh stop it! I can't be your girlfriend. You mother would never forgive me."
    pov "I don't know, I think I'm winning you over! Just follow your heart!"
    scene date 21pm 019a #mom at table hands down, bite lip
    mom "Stop... You're such a tease..."
    $ momlove += 1
    jump ndate421

label ndate321gfno:
    scene date 21pm 017b #mom at table hands down, smile (No wine)
    pov "Maybe you're right. But I'm not sure now is the time."
    mom "Don't worry. I'm sure you'll find the perfect woman for you."
    pov "Thank you..."
    jump ndate421

label ndate321joke:
    scene date 21pm 017a #mom holding her breasts at table
    call screen ndate321joke1

screen ndate321joke1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('ndate321joke1'), Jump('ndate321jokecor')) hovered tt.Action ("Naughty comment [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('ndate321joke1'), Jump('ndate321jokeno')) hovered tt.Action ("No comment") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate321jokecor:
    scene date 21pm 017a #mom holding her breasts at table
    pov "Oh well if you're offering them for later too..."
    scene date 21pm 019a #mom at table hands down, bite lip
    mom "I... I didn't mean it that way..."
    pov "Are you sure? If the date goes well, you might just get lucky!"
    mom "Stop kidding around! You know exactly how I meant it."
    if inc == True:
        pov "Haha, relax, mom."
    else:
        pov "Haha, relax, [mother]."
    $ momcorruption += 1
    jump ndate421

label ndate321jokeno:
    scene date 21pm 017a #mom holding her breasts at table
    pov "..."
    scene date 21pm 018a #mom at table hands up slightly smile
    mom "Oh, come on. You're surprised, weren't you?"
    pov "Yes...very!"
    mom "It's probably better to keep your eyes on your date then and not staring at other woman."
    mom "Makes a woman jealous..."
    pov "Haha, yes you're right. Sorry about that."
    mom "It's ok. I just want you all to myself tonight!"
    jump ndate421

label ndate421:
    scene date 21pm 020 #mom at table surprised looking right
    mom "Oh noo...!"
    pov "What...?"
    mom "This can't be happening now!"
    scene date 21pm 021 #bad man at entrance
    "You turn your head to see what she is talking about."
    pov "What's wrong? Is it something about that guy?"
    pov "It seems like he isn't welcome in the restaurant..."
    mom "<whisper> Hey [pov]!"
    scene date 21pm 022 #mom hiding behind pillar by herself
    pov "Huh? What are you doing way over there?"
    mom "<whisper> Sshh... Come over here quickly! And be quiet about it."
    pov "Ok...?"
    povi "What's gotten into her? Why is she so scared of this man?"
    scene date 21pm 024 #mom and son behind pillar
    pov "Calm down!"
    povi "Oh shit. She looks really scared."
    mom "<whisper> We need to hide, fast! If this man finds me..."
    pov "<whisper> What's with him?"
    mom "<whisper> Sshh... not now. Let's hide first!"
    pov "<whisper> Ok."
    scene date 21pm 023 #bad man at entrance turning
    povi "Maybe she's right. He seems really dangerous. The waiter is running away!"
    povi "But who the hell is he? And why does he scare her so much?"
    mom "<whisper> Shhh... [pov]!"
    povi "Hm.. where is she?"
    scene date 21pm 025 #mom behind wall finger says come here
    povi "How did she get there so fast? I didn't even hear her moving."
    mom "<whisper> Please faster! We need to hide right now!"
    pov "<whisper> Ok, ok."
    "You get close up to her."
    scene date 21pm ntr011w
    mom "<whisper> But where do we hide now?"
    if NTR == True and momrelationship <= 29:
        mom "<whisper> Should we seperate?"
        jump ndate421wc
    else:
        jump ndate421men

label ndate421wc:
    scene date restroom door men
    call screen ndate421wc1

screen ndate421wc1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('ndate421wc1'), Jump('ndate421men')) hovered tt.Action ("Stay together [lv1]/[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate421wc1'), Jump('ndate421women')) hovered tt.Action ("Seperate (Darker Paths)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate421women:
    scene date restroom door men
    "You see her go to the women's restroom and you go to the men's restroom."
    povi "I hope this is a good idea."
    scene date men restroom
    povi "Maybe she can hide and when he finds me alone I can tell him that she already left."
    povi "But... I'm not sure..."
    povi "Shit, he's not coming. I have a bad feeling. I need to check on her."
    scene black
    "You go to the women's restroom."
    scene date 21pm ntr00 #bad man opening door
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    povi "Shit... Shit... He found her."
    "Bad Guy" "You still trying to hide? You should know that you can't trick me!"
    mom "I... I'm sorry Peter."
    "Peter" "Did you really think I would forget you after what I did for you?"
    "Peter" "You owe me [mother]!"
    mom "Please, I'm really sorry. You misunderstand..."
    "Peter" "Get your damn dress off!"
    mom "O... ok. Just don't hurt me, Peter."
    povi "What...? I thought he didn't know her name? Is he's from a rival gang?"
    povi "And now she owes him something? Or does the gang owe him something?"
    povi "This is really wrong!"
    povi "I'm not sure what to do now..."
    call screen ndate21ntrstop

screen ndate21ntrstop():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('ndate21ntrstop'), Jump('ndate21interfere')) hovered tt.Action ("Interfere") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('ndate21ntrstop'), Jump('ndate21ntr1')) hovered tt.Action ("Watch longer") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate21interfere:
    scene date 21pm ntr00 #bad man opening door
    povi "I need to stop this! I'll show you motherfucker!"
    pov "Hey asshole!"
    "Peter" "What?"
    scene date 21pm ntr01stop #kicking door down
    pov "Take this!"
    "You kick the door straight in his face!"
    "Peter" "Aaah..."
    scene date 21pm ntr02stop #bad man bleeding
    "Peter" "You piece of shit. I'll kill you!"
    if inc == True:
        povi "Damn, I think I saw a gun in his coat. I need to try to get him away from my Mom!"
    else:
        povi "Damn, I think I saw a gun in his coat. I need to try to get him away from [pov]!"
    pov "Hey asswipe! I'm calling the cops and telling them you're threatening people with a gun!"
    "You run away."
    scene date 21pm ntr03stop #empty pillar
    povi "Faster! I'll hide here behind a pillar."
    povi "Maybe I'm lucky and he's not thinking clearly after that blow to the head."
    scene date 21pm ntr04stop #bad man searching for son
    povi "There he is..."
    povi "He's talking to the waitress. Where's she pointing to?"
    scene date 21pm ntr05stop #bad man walking away
    povi "Phew! She sent him away. Thank god. I'm not ready for a fight with a mad gun man!"
    povi "But now I have a lot of questions."
    scene date 21pm ntr06stop #mom hallway neurtal
    mom "Are you alright?"
    if inc == True:
        mom "Yes son, I think he's gone."
    else:
        mom "Yes [pov], I think he's gone."
    pov "But I have some questions."
    mom "Yes, I know. But we should problably go home first."
    pov "..."
    mom "Please let's go, I'm feeling really scared here."
    pov "Okay..."
    scene black
    "You go home together." #add scene where she explains he's a part of another gang and Peter feels that Davide owes him because he wouldn't let Peter fuck her.
    $ d9rnntri = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label ndate21ntr1:
    scene date 21pm ntr00 #bad man opening door
    povi "I'll watch a little longer to find out what's going on."
    "Peter" "Now come here [mother]!"
    mom "Yes, Peter."
    "Peter" "You're going to get on top whore! I'm going to put you to work after you made me search around for you!"
    povi "Wait a second..."
    if spot1000anim == True:
        image date 21pm ntr01a = Movie(channel="date 21pm ntr01a", play="edited/anim//spot1000/date/21pm ntr01a.webm")
        scene date 21pm ntr01a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr01 #mom ride bad man
    mom "Haaah... Ow..."
    "Peter" "You're dry bitch! Of course it hurts!"
    povi "They're fucking..."
    if inc == True:
        povi "Seriously, why the hell does everyone want to fuck my Mom?!"
    else:
        povi "Seriously, why the hell does everyone want to fuck [pov]?!"
    povi "Wait, did I seriously just think that? Even I want to fuck her..."
    call screen checkdarkerpaths_nicole
    if nicole_voyeur == True or nicole_ntr == True:
        jump ndate21ntrgood
    else:
        jump ndate21ntrbad

label ndate21ntrgood:
    if spot1000anim == True:
        image date 21pm ntr01a = Movie(channel="date 21pm ntr01a", play="edited/anim//spot1000/date/21pm ntr01a.webm")
        scene date 21pm ntr01a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr01 #mom ride bad man
    if nicole_voyeur == True:
        if inc == True:
            povi "I don't care if mom wants to have fun with other men."
        else:
            povi "I don't care if she wants to have fun with other men."
    else:
        if inc == True:
            povi "What the hell is going on here? Why is my mom doing this?"
        else:
            povi "What the hell is going on here? Why is she doing this?"
    if spot1000anim == True:
        image date 21pm ntr02a = Movie(channel="date 21pm ntr02a", play="edited/anim//spot1000/date/21pm ntr02a.webm")
        scene date 21pm ntr02a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr02
    with vpunch
    "Peter" "That's it! With a little force your juices start flowing!"
    mom "Hnng!"
    if nicole_voyeur == True:
        povi "And she really seems to like riding him."
    else:
        povi "She doesn't seem to be fighting him now..."
    mom "Ohhh..."
    "Peter" "Yes, do it faster. Ride me!"
    if spot1000anim == True:
        image date 21pm ntr02a = Movie(channel="date 21pm ntr02a", play="edited/anim//spot1000/date/21pm ntr02a.webm")
        scene date 21pm ntr02a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr02 #mom ride bad man door more open
    with vpunch
    mom "Oh yes, you're filling my cunt!"
    "Peter" "Good, ride me as hard as you want, slut!"
    mom "Haahhh... Hnng..."
    if nicole_voyeur == True:
        povi "Damn, she's really enjoying it."
    else:
        povi "Damn, she's really enjoying it. Why? I can't believe this!"
    mom "I need more!"
    "Peter" "Come here!"
    if spot1000anim == True:
        image date 21pm ntr03a = Movie(channel="date 21pm ntr03a", play="edited/anim//spot1000/date/21pm ntr03a.webm")
        scene date 21pm ntr03a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr03 #mom ride bad man holding her, her left hand on hair and right hand up exposed right breast
    with vpunch
    mom "Haaah... Ahhh. hah..."
    "Peter" "Better! Now I'm under control."
    mom "Yes, harder, harder!"
    "Peter" "Oh, when I'm done with you, you'll come hard alright."
    if nicole_voyeur == True:
        povi "She really likes it rough."
    else:
        povi "I can't do anything to stop this..."
    if spot1000anim == True:
        image date 21pm ntr04a = Movie(channel="date 21pm ntr04a", play="edited/anim//spot1000/date/21pm ntr04a.webm")
        scene date 21pm ntr04a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr04 #mom riding bad man hands outstreched
    with vpunch
    mom "Oh fuck that's good..."
    "Peter" "Let me help you! You'll love it!"
    mom "Hnnng...!"
    if nicole_voyeur == True:
        povi "Shit! Now that is fucking!"
    else:
        povi "Shit! Isn't that going too far?"
    mom "Harder you old prick!"
    "Peter" "Oh, just wait you slut!"
    mom "Hnng..."
    $ momchoke = True
    if nicole_voyeur == True:
        povi "I can't believe it! She really loves the hard stuff."
        povi "But that's good to know."
    else:
        povi "I can't believe it! She's enjoying this hard stuff."
        povi "I just can't believe it. She's a whore!"
    if spot1000anim == True:
        image date 21pm ntr05a = Movie(channel="date 21pm ntr05a", play="edited/anim//spot1000/date/21pm ntr05a.webm")
        scene date 21pm ntr05a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr05 #bad man on mom, legs around him
    povi "Damn, they almost saw me..."
    mom "Hnng... hnng..."
    "Peter" "Yes, take it! I'm almost there!"
    if nicole_voyeur == True:
        if inc == True:
            povi "What a hard, rough fucking... I wonder if she does this stuff with Dad too?"
        else:
            povi "What a hard, rough fucking... I wonder if she does this stuff with Bruce too?"
    else:
        if inc == True:
            povi "I wonder if she does this stuff with Dad too?"
        else:
            povi "I wonder if she does this stuff with Bruce too?"
    if spot1000anim == True:
        image date 21pm ntr06a = Movie(channel="date 21pm ntr06a", play="edited/anim//spot1000/date/21pm ntr06a.webm")
        scene date 21pm ntr06a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr06 #bad man on mom, legs up
    with vpunch
    mom "Hnng... Haaaahh..."
    "Peter" "Yes! Come with me slut!"
    if nicole_voyeur == True:
        povi "What a hot show! And she seems to be cumming hard."
    else:
        if inc == True:
            povi "She came so hard. What would Dad think of all of this?"
        else:
            povi "She came so hard. What would Bruce think of all of this?"
    mom "Hnn... hnn..."
    "Peter" "Let me mark you good now whore."
    povi "They're done now. I should hide."
    scene date 21pm ntr07 #bad man in mirror
    povi "He's going..."
    "Peter" "Now we're even!"
    mom "Hnn... hnn..."
    povi "Damn, she's seriously wiped out."
    if nicole_voyeur == True:
        scene date 21pm ntr08 #mom coverd in cum on toilet
    elif nicole_ntr == True:
        scene edited date 21pm ntr08 #mom coverd in cum on toilet with blood
    else:
        scene date 21pm ntr08 #mom coverd in cum on toilet
    povi "Wow! She actually fainted."
    povi "I should wake her up so we can go."
    povi "Or maybe..."
    call screen ndate21ntrtake

screen ndate21ntrtake():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('ndate21ntrtake'), Jump('ndate21ntrfuck')) hovered tt.Action ("Fuck her too") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('ndate21ntrtake'), SetVariable('ndate21ntrhelped', True), Jump('ndate21ntrhelp')) hovered tt.Action ("Wake her up") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate21ntrfuck:
    if nicole_voyeur == True:
        scene date 21pm ntr08 #mom coverd in cum on toilet
    elif nicole_ntr == True:
        scene edited date 21pm ntr08 #mom coverd in cum on toilet with blood
    else:
        scene date 21pm ntr08 #mom coverd in cum on toilet
    povi "I want to fuck her too. She's unconscious, so she won't complain."
    povi "Damn I'm so hard right now."
    if inc == True:
        povi "You're mine now, mom!"
    else:
        povi "You're mine now, [mother]!"
    if spot1000anim == True:
        image date 21pm ntr09ba = Movie(channel="date 21pm ntr09ba", play="edited/anim//spot1000/date/21pm ntr09ba.webm")
        scene date 21pm ntr09ba with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr09b #son sex with mom ntr pussy
    with vpunch
    povi "Oh, yes! This is heaven..."
    if inc == True:
        povi "I'm fucking you, mom!"
        with vpunch
    else:
        povi "I'm fucking you, [mother]!"
        with vpunch
    mom "Hnng... hnng..."
    with vpunch
    povi "She noticed the penetration but is still unconscious."
    povi "Damn, that's too much. I'm done..."
    $ ndate21ntrsex = True
    $ d9rnntr = True
    call screen ndate21ntrcum

screen ndate21ntrcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate21ntrcum'), Jump('ndate21ntrinside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate21ntrcum'), Jump('ndate21ntroutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate21ntrinside:
    if spot1000anim == True:
        image date 21pm ntr09ba = Movie(channel="date 21pm ntr09ba", play="edited/anim//spot1000/date/21pm ntr09ba.webm")
        scene date 21pm ntr09ba with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr09b #son sex with mom ntr pussy
    if inc == True:
        povi "Oh yes, take my sperm in you, mom!"
        with vpunch
    else:
        povi "Oh yes, take my sperm in you, [mother]!"
        with vpunch
    pov "Ohhh, yeeess..."
    with vpunch
    mom "Hnng..."
    with vpunch
    "You came inside her."
    scene date 21pm ntr08i #internal son cum shot leaking out
    povi "That was a really good fuck! I needed that!"
    povi "And so much cum on her."
    povi "Let's wake her up now."
    jump ndate21ntrhelp

label ndate21ntroutside:
    scene date 21pm ntr09a #son coming on NTR mom stomach
    if inc == True:
        povi "Let me mark you too, mom!"
    else:
        povi "Let me mark you too, [mother]!"
    pov "Ohhh, yeeess..."
    mom "Hnng..."
    scene date 21pm ntr08o #external son cum shot on stomach
    povi "That was a really good fuck! I needed that!"
    povi "And so much cum on her."
    povi "Let's wake her up now."
    jump ndate21ntrhelp

#----- Edited -----
label ndate21ntrbad:
    if spot1000anim == True:
        image date 21pm ntr01a = Movie(channel="date 21pm ntr01a", play="edited/anim//spot1000/date/21pm ntr01a.webm")
        scene date 21pm ntr01a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr01 #mom ride bad man
    if nicole_revenge == True:
        if inc == True:
            povi "No! That asshole is fucking my mom!"
        else:
            povi "No! That asshole is fucking her!"
    else:
        povi "Wow, that guy is fucking her!"
    mom "Please stop! I can do something else for you... Please. You're hurting me!"
    with vpunch
    mom "Ohhh..."
    with vpunch
    "Peter" "Yes I am bitch! I'm going to do it faster. Ride me harder slut!"
    if spot1000anim == True:
        image date 21pm ntr02a = Movie(channel="date 21pm ntr02a", play="edited/anim//spot1000/date/21pm ntr02a.webm")
        scene date 21pm ntr02a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr02 #mom ride bad man door more open
    with vpunch
    mom "No! stop... I'm not ready..."
    "Peter" "So you think I care! I'm going to fuck you hard for standing me up!"
    mom "Please! Davide shouldn't have promised you anything! Gah..."
    mom "Haahhh... Hnng... <sobs>"
    with vpunch
    if nicole_revenge == True:
        povi "God damn it! I can't do a thing when he has a gun! I could get her killed!"
    else:
        povi "Damn, she's getting raped. Can't say I didn't think about doing the same thing..."
    "Peter" "I need more!"
    "Peter" "Come here!"
    if spot1000anim == True:
        image date 21pm ntr03a = Movie(channel="date 21pm ntr03a", play="edited/anim//spot1000/date/21pm ntr03a.webm")
        scene date 21pm ntr03a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr03 #mom ride bad man holding her, her left hand on hair and right hand up exposed right breast
    mom "Haaah... Ahhh. hah..."
    "Peter" "Better! Now you're even more under my control."
    with vpunch
    mom "Oh god, please stop!"
    "Peter" "Oh, when I'm done with you, you'll come hard bitch. Just give in you slut!"
    povi "He's humiliating her! He's trying to make her act like a slut."
    "Peter" "Here it comes bitch! I'm going to rip you pussy apart with my cock!"
    if spot1000anim == True:
        image date 21pm ntr04a = Movie(channel="date 21pm ntr04a", play="edited/anim//spot1000/date/21pm ntr04a.webm")
        scene date 21pm ntr04a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr04 #mom riding bad man hands outstreched
    with vpunch
    "Peter" "Let me help you whore! You'll love it!"
    mom "Hnnng...!"
    if nicole_revenge == True:
        povi "Shit! She has to brace herself he's fucking her so hard! I'm to kill that bastard! I'll kill them all!"
    else:
        povi "Hot damn! She has to brace herself he's fucking her so hard! Now that looks like a good time!"
    "Peter" "You're starting to like it now aren't you bitch! You're finally getting wet!"
    with vpunch
    mom "Fuck you! You old prick!"
    if nicole_revenge == True:
        povi "Oh god! I think she's bleeding down there."
    "Peter" "Oh, just you wait you slut!"
    mom "Hnng... Oh god it hurts!"
    $ momchoke = True
    if spot1000anim == True:
        image date 21pm ntr05a = Movie(channel="date 21pm ntr05a", play="edited/anim//spot1000/date/21pm ntr05a.webm")
        scene date 21pm ntr05a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr05 #bad man on mom, legs around him
    with vpunch
    povi "Damn, he almost saw me..."
    mom "Hnng... hnng... stop..."
    "Peter" "Yes, take it! I'm almost there!"
    if nicole_revenge == True:
        povi "What a hard, rough fucking... I would give anything to be able to stop this."
        povi "I can't even call the police because of this undercover shit!"
    else:
        povi "What a hard, rough fucking... I would give anything to be guy doing that to her."
    if spot1000anim == True:
        image date 21pm ntr06a = Movie(channel="date 21pm ntr06a", play="edited/anim//spot1000/date/21pm ntr06a.webm")
        scene date 21pm ntr06a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr06 #bad man on mom, legs up
    mom "Hnng... Haaaahh..."
    "Peter" "Yes! Come with me slut!"
    if nicole_revenge == True:
        povi "She's not going to cum you fucker. She hates you!"
    else:
        povi "Yeah, do it you slut!"
    mom "Hnn... hnn..."
    "Peter" "Let me mark you good."
    if nicole_revenge == True:
        povi "They're done now. I better hide. Then I can make sure she's ok."
    else:
        povi "They're done now. I better hide."
    scene date 21pm ntr07 #bad man in mirror
    povi "He's going..."
    "Peter" "Now we're even!"
    mom "Hnn... oww..."
    if nicole_revenge == True:
        povi "She seems to be really done... That damn prick!"
    else:
        povi "She seems to be really done..."
    scene edited date 21pm ntr08 #mom coverd in cum on toilet with blood
    if nicole_revenge == True:
        povi "She's fainted. Oh god! There's blood. That fucker!"
    povi "I should wake her up so we can go."
    povi "Or maybe..."
    #----- Edited -----
    call screen ndate21ntrtake2

#----- Custom -----
screen ndate21ntrtake2():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('ndate21ntrtake'), Jump('ndate21ntrfuck2')) hovered tt.Action ("Fuck her too") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('ndate21ntrtake'), Jump('ndate21ntrhelp')) hovered tt.Action ("Wake her up") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label ndate21ntrfuck2:
    scene edited date 21pm ntr08 #mom coverd in cum on toilet with blood
    povi "This is messed up, but I want to fuck her too. She's unconscious, so she won't know."
    povi "Damn I'm so hard right now."
    if inc == True:
        povi "Please forgive me, mom!"
    else:
        povi "Please forgive me, [mother]!"
    if spot1000anim == True:
        image date 21pm ntr09ba = Movie(channel="date 21pm ntr09ba", play="edited/anim//spot1000/date/21pm ntr09ba.webm")
        scene date 21pm ntr09ba with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr09b #son sex with mom ntr pussy
    with vpunch
    povi "Oh, yes! This is heaven..."
    if inc == True:
        povi "I'm fucking you, mom!"
        with vpunch
    else:
        povi "I'm fucking you, [mother]!"
        with vpunch
    mom "Hnng... hnng..."
    with vpunch
    povi "She noticed the penetration but is still unconscious."
    povi "Damn, this is too much. I'm done..."
    $ ndate21ntrsex = True
    $ d9rnntr = True
    call screen ndate21ntrcum2

#----- Custom -----
screen ndate21ntrcum2():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate21ntrcum'), Jump('ndate21ntrinside2')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate21ntrcum'), Jump('ndate21ntroutside2')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label ndate21ntrinside2:
    if spot1000anim == True:
        image date 21pm ntr09ba = Movie(channel="date 21pm ntr09ba", play="edited/anim//spot1000/date/21pm ntr09ba.webm")
        scene date 21pm ntr09ba with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm ntr09b #son sex with mom ntr pussy
    if inc == True:
        povi "Oh yes, take my sperm in you, mom!"
        with vpunch
    else:
        povi "Oh yes, take my sperm in you, [mother]!"
        with vpunch
    pov "Ohhh, yeeess..."
    with vpunch
    mom "Hnng..."
    with vpunch
    "You came inside her."
    scene date 21pm ntr08i #internal son cum shot leaking out
    povi "There is so much cum on her."
    povi "I'll wake her up now."
    jump ndate21ntrhelp

#----- Custom -----
label ndate21ntroutside2:
    scene date 21pm ntr09a #son coming on NTR mom stomach
    if inc == True:
        povi "Let me mark you too, mom!"
    else:
        povi "Let me mark you too, [mother]!"
    pov "Ohhh, yeeess..."
    mom "Hnng..."
    scene date 21pm ntr08o #external son cum shot on stomach
    povi "There is so much cum on her."
    povi "I'll wake her up now."
    jump ndate21ntrhelp

label ndate21ntrhelp:
    if nicole_voyeur == True:
        scene date 21pm ntr08 #mom coverd in cum on toilet
    elif nicole_ntr == True:
        scene edited date 21pm ntr08 #mom coverd in cum on toilet with blood
    else:
        scene date 21pm ntr08 #mom coverd in cum on toilet
    if inc == True:
        pov "Mom! Wake up mom!"
    else:
        pov "[mother]! Wake up [mother]!"
    pov "We should go. He's gone!"
    mom "Hnn..."
    scene date 21pm ntr09w #mom covered in cum awake
    mom "It's you [pov]..."
    pov "I saw what he did to you, but it's better when we go now."
    mom "Oh god... he raped me..."
    if nicole_voyeur == True or nicole_ntr == True:
        povi "Rape? Still lying to me..."
    elif nicole_revenge == True:
        pov "I know. I'm so sorry I coudn't stop him. He had a gun and I didn't want him to kill you."
    else:
        povi "Yeah he did! It was awesome!"
    pov "Come get your dress back on."
    mom "Thank you for helping me..."
    scene date 21pm ntr010w #mom cum on her face dressed outside stall
    mom "Can you wait a moment outside? I need to clean up a bit."
    if inc == True:
        pov "Sure, mom."
    else:
        pov "Sure, [mother]."
    scene black
    "You wait outside."
    scene date 21pm ntr011w #mom biting lip in yellow hallway
    pov "You're done? Do you want to go home now?"
    mom "Yes. Thank you again for taking care of me."
    if ndate21ntrsex == True:
        if inc == True:
            povi "No, thank you, for letting me fuck you, mom."
        else:
            povi "No, thank you, for letting me fuck you."
    else:
        pov "You're welcome."
        povi "This has to end!"
    scene black
    "You go home together."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label ndate421men:
    scene date 21pm ntr011w
    pov "<whisper> I have an idea! Follow me!"
    mom "<whisper> But that's the men's restroom!"
    pov "<whisper> Trust me!"
    scene date men restroom
    pov "Good, nobody's here."
    mom "But what to do now? He might search here too."
    pov "It's ok we're going to hide in a stall."
    mom "But..."
    scene date 21pm 026 #mom in dress outside stall
    mom "These are pretty small. Do you think we'll both fit?"
    pov "Yes, get in and sit on the toilet, we need to hurry."
    mom "Yeah, you're right."
    scene date 21pm 027 #mom sitting on toilet
    mom "But it's so small..."
    pov "You can sit up on my lap."
    mom "I hope that'll work."
    pov "Just trust me!"
    "Bad Man" "Yeah Davide I'm here. Where is the whore you sent?!"
    pov "<whisper> Shit, he's just outside the restroom!"
    "You dash in and shut the door behind you."
    scene date 21pm 028 #you sitting on toilet facing mom legs up
    pov "<whisper> Sorry... There was no time to turn around."
    pov "<whisper> Just keep your legs up and keep holding on to me if you need to."
    mom "<whisper> It's a little bit weird. You're backwards on the toilet."
    pov "<whisper> Yeah, but hopefully he just thinks I'm some weirdo and stays away from us."
    mom "<whisper> Yeah, I could see that I guess..."
    "You hear the men's restroom door open but no one has come in yet."
    pov "<whisper>Well, we can't turn around now. He might see your shoes and know a woman is in here."
    mom "<whisper> I know."
    pov "<whisper> It will be alright. I'm here with you."
    mom "<whisper> Ok..."
    scene date 21pm 029 #mom close up biting lip
    pov "<whisper> So what's with this asshole? He said Davide sent him."
    mom "<whisper> He's the boss of another gang. I only know his first name. It's Peter. He's a very bad man..."
    pov "<whispher> So did Davide just serve you up as his personal whore to this guy?"
    mom "I don't know. He never said he owed their gang anything when I was around."
    povi "Maybe it is to settle a debt. Or just a sick game. How did Davide even know we'd be here?"
    pov "<whisper> Doesn't matter. I'm going to get that fucker back for this!"
    scene date 21pm 033 #mom close up partial smile
    mom "<whisper> I know sweetie. It's ok. We'll get out of this just like you said."
    mom "<whisper> Peter peter does know what I look like but he doesn't know my name, so he can't track me down at home, thankfully."
    pov "<whisper> Yeah but if he finds us now..."
    scene date 21pm 029 #mom close up biting lip
    mom "<whisper> Yes, it would be very bad. Honestly, I'm scared [pov]."
    "She hugs you a bit tighter."
    pov "<whisper> I'll protect you!"
    mom "<whisper> I'm sure he's carrying a weapon, so don't do something dangerous please, I don't want to lose you!"
    pov "<whisper> I won't."
    povi "Unless there if an opening, then I'm going to make this guy wish he never stepped foot in here."
    povi "She's holding me so tight. In anything situation this would be great."
    if spot1000anim == True:
        image date 21pm 030a = Movie(channel="date 21pm 030a", play="edited/anim//spot1000/date/21pm 030a.webm")
        scene date 21pm 030a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm 030 #mom close up cleavage
    povi "She's so damn..."
    if spot1000anim == True:
        image date 21pm 031a = Movie(channel="date 21pm 031a", play="edited/anim//spot1000/date/21pm 031a.webm")
        scene date 21pm 031a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm 031 #mom close up underwear
    povi "...close to me. I can feel her breathing."
    "You hear someone step inside the restroom."
    scene date 21pm 032 #mom close up open mouth
    mom "<whisper> Oh no! He's coming in."
    pov "<whisper> Just be quiet..."
    "Peter" "Yeah, I know that Davide. I'm not fucking stupid. I'm still looking, but if I don't find her soon..."
    "Peter" "You're going to owe me far more than a free fuck from a gang whore!"
    povi "That was it! I'm going to break Davide's fucking spine for this!"
    "Peter" "Wait, that's weird. I can only see one guy's feet, but the idiot is sitting backwards in the stall..."
    "Peter" "But I could have sworn I heard a two voices in here."
    mom "<whisper> Oh no..."
    pov "<whisper> Shit, what should we do now?"
    scene date 21pm 033a #mom close up bite lip
    mom "<whisper> I think I might have an idea."
    jump ndate421mench

label ndate421mench:
    call screen ndate421mench1

screen ndate421mench1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('ndate421mench1'), Jump('ndate421mencor')) hovered tt.Action ("Go with your own solution [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('ndate421mench1'), Jump('ndate421menlove')) hovered tt.Action ("Hear her idea [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate421mencor:
    scene date 21pm 033 #mom close up partial smile
    pov "<whisper> Wait! I figured it out! Let's pretend we're a couple fooling around. It happens all the time!"
    pov "<whisper> Maybe, he'll just move on and keep looking for you somewhere else."
    mom "<whisper> What..."
    pov "<whisper> Just play along. He's coming closer."
    mom "..."
    "You run your hand down her dress and gently pull it the side exposing a breast."
    scene date 21pm 034a  #mom close up left breast out
    mom "Hmm... hmm..."
    "You nod to her letting her know she's got the right idea. You mouth the words \"louder\"."
    mom "Hmm... Oh yeah..."
    pov "You like that don't you?"
    if inc == True:
        povi "Damn, that so hot. My mom is sitting on my lap moaning and calling out like a woman in heat."
    else:
        povi "Damn, that so hot. [mother] is sitting on my lap moaning and calling out like a woman in heat.."
    "Peter" "Oh, there is someone else in there too..."
    pov "<whisper> Keep going!"
    mom "HMM... HMM..."
    scene date 21pm 034a #mom close up left breast out
    povi "This might be a bit fucked up, but it's still so sexy!"
    scene date 21pm 035a #mom close up mouth more open shocked
    mom "Hnn... <whisper> Do you think this is enough?"
    pov "<whisper> I don't think so he hasn't left yet!"
    mom "<whisper> Ok..."
    pov "<whisper> Just try to concentrate on your moaning. We don't want to get caught, right?"
    if momcorruption < 20:
        scene date 21pm 099 #mom hand up stop
        mom "<whisper> You can stop now. I think he's gone."
        pov "<whisper> You sure? Maybe we should keep going for bit before we risk it."
        mom "<whisper> I'm sure! Just check please!"
        scene date check guy
        pov "You were right, he's gone now..."
        povi "Damn, I wonder if I could have done more if she was more corrupted?"
    else:
        scene date 21pm 036a #mom close up mouth open lust
        mom "Hah... hah..."
        povi "She really seems like she's getting into it."
        povi "It's like I got lost and ended up in heaven. I can play with her all I want right now."
        "Peter" "Well yeah, but I haven't heard anything crazy going on in there yet. If it's like you say it is and it's them hiding in there, they won't go that far to hide..."
        povi "Shit! He's not buying it. Wait... I know what we need to do!"
        if spot1000anim == True:
            image date 21pm 037aa = Movie(channel="date 21pm 037aa", play="edited/anim//spot1000/date/21pm 037aa.webm")
            scene date 21pm 037aa with dissolve:
                size (config.screen_width, config.screen_height)
            pause
        else:
            scene date 21pm 037a #mom close up playing with right and left breast
        with vpunch
        "You pinch her nipple hard!"
        mom "Hnn... Oh god! Hnngg..."
        pov "You like it when I pinch your nipples don't you slut!"
        scene date 21pm 038a #mom close up biting lip sexy lust
        pov "<whisper> I'm sorry, but we need to kick it up a notch to make him believe we're really going at it."
        mom "Hnn... hmm... Oh yeah... oh baby. You slut love's it when you use her body however you want!"
        povi "Wow! It's getting better and better. She's definitely kicking it up an notch. She's got a kinky side."
        if spot1000anim == True:
            image date 21pm 039aa = Movie(channel="date 21pm 039aa", play="edited/anim//spot1000/date/21pm 039aa.webm")
            scene date 21pm 039aa with dissolve:
                size (config.screen_width, config.screen_height)
            pause
        else:
            scene date 21pm 039a #mom close up fondling breasts finger in cleavage
        povi "Kneading these big tits like this... Damn! I'm getting hard so fast."
        pov "Keep moaning you slut. Let me know how much you love this!"
        mom "Hah... Hnng... Oh yes! Use me baby!"
        pov "You want my cock between these big breasts don't you?! Fucking up and down until I come all over your chest!"
        povi "Her legs are squeezing me tighter. Is she getting horny too?"
        povi "Let's find out."
        scene date 21pm 036a #mom close up mouth open lust
        pov "Or maybe you want my fingers ramming into that wet pussy!"
        mom "Hmm... Hnng... God... Yes! I want it baby! Play with your slut"
        "She looking right at me while she speaks... God that's hot!"
        pov "Well, let's see if my slut's pussy is nice and wet already. Like a good whore know's she should be!"
        scene date 21pm 040a #mom close up eyes wide and lip thin from sucking lips in a bit
        povi "Well she's not trying to stop me yet... Here I go!"
        if spot1000anim == True:
            image date 21pm 041aa = Movie(channel="date 21pm 041aa", play="edited/anim//spot1000/date/21pm 041aa.webm")
            scene date 21pm 041aa with dissolve:
                size (config.screen_width, config.screen_height)
            pause
        else:
            scene date 21pm 041a #mom close up son left hand on right breast and right hand on crotch
        povi "Damn, just as I thought. She's soaking those panties."
        if momcorruption < 40:
            scene date 21pm 099 #mom hand up stop
            mom "<whisper> Wait, you can stop now. I think he's gone."
            pov "<whisper> You sure? Maybe we should keep going for bit before we risk it."
            mom "<whisper> I'm sure! Just check please!"
            scene date check guy
            pov "You were right, he's gone now..."
            povi "Damn, I wonder if I could have done more if she was more corrupted?"
        else:
            scene date 21pm 042a #mom close up mouth slightly open sexy eyes
            mom "Hah... hah... Hmm... Feels so good..."
            mom "Hnnng... hmmm... <whisper> Should we stop? We can't go much further..."
            povi "\"We?\" That's interesting, she's definitely not just playing along anymore. She's enjoying it too."
            pov "<whisper> We need to be sure he believes it... keep going. It's ok, even if it's getting us worked up, it's not our fault. We're only human..."
            "You slide her panties to the side while you talk."
            scene date 21pm 043a #mom close up two fingers inside pussy
            with vpunch
            mom "<whisper> But... HAAAH...!"
            povi "She's so wet I can slide in easily. Her hot wet pussy!"
            image fingernic_date = Movie(channel="fingernic_date", play="images/anim/fingernic_date.webm")
            scene fingernic_date with dissolve:
                size (config.screen_width, config.screen_height)
            pause
            mom "Haaahh... Hnnngg... Yes... fuck yes..."
            povi "She's getting so into this even when that guy is outside. Who knew she was into that?"
            povi "The fear is adding to the excitement. I get why people love doing this in public now!"
            "Peter" "Oh wait, I can hear them really getting into it now... Fuck Davide! Where is that bitch? Everyone else is getting action it seems!"
            povi "Ha! That piece of shit is buying it finally."
            povi "Although, I dont't want to stop what we're doing now anyway!"
            if inc == True:
                povi "I've waited so long to get in my mom's pussy."
            else:
                povi "I've waited so long to get in [mother]'s pussy."
            scene date 21pm 044a #mom close up mouth open sexy eyes enjoying it
            mom "Hnng... hah... hah..."
            "You keep plunging your fingers inside her."
            with vpunch
            pov "<whisper> Good. You're doing go good. Let him hear how wet you are and you're getting off on this."
            povi "And me of course!"
            mom "Hah... no... feels too good... wait..."
            pov "<whisper> Shhh! What are you doing? He'll get suspicious. Here, let me help you some more."
            image fingernic_date = Movie(channel="fingernic_date", play="images/anim/fingernic_date.webm")
            scene fingernic_date with dissolve:
                size (config.screen_width, config.screen_height)
            pause
            pov "You dirty slut, do you hear your juices gushing all over my fingers?!"
            povi "She so damn wet now. I'm two fingers wide all in her."
            with vpunch
            mom "Ohhh... ahhh... hnng..."
            with vpunch
            povi "That was right! She's shaking her hips against my hand. She is trying to get herself off."
            mom "Hnnng... ahhh... Yes! I love your fingers deep inside my slutty wet pussy!"
            with vpunch
            povi "This is so awesome! I wonder..."
            "You raise your hand and hold it to the side of her head, pressing you thumb to her lips."
            scene date 21pm 046a #mom close up sucking on finger
            "She put it in her mouth right away. Massaging your thumb with her tongue as she sucks."
            povi "God damn, she did just what I wanted! She's sucking wildly on my thumb while I finger her."
            if inc == True:
                pov "<whisper> Good, you're so tight and wet, mom!"
            else:
                pov "<whisper> Good, you're so tight and wet, [pov]!"
            image fingernic_date = Movie(channel="fingernic_date", play="images/anim/fingernic_date.webm")
            scene fingernic_date with dissolve:
                size (config.screen_width, config.screen_height)
            pause
            mom "<sucking> Hmm... hnng... hmm..."
            povi "She sucking harder now and pressing her hips into my hand so quickly, she's getting close."
            with vpunch
            mom "Hnn... Hnnng... Mmmm..."
            povi "Oh yes that's it! You really are my slut!"
            "You pull your thumb out of her mouth with a nice wet popping noise."
            scene date 21pm 047a #mom close up eyes almost closed mouth open enjoying it
            mom "Ahhh... Hahhh..."
            pov "<whisper> I know you're getting close... just imagine if it was my cock thrusting inside you!"
            image fingernic_date = Movie(channel="fingernic_date", play="images/anim/fingernic_date.webm")
            scene fingernic_date with dissolve:
                size (config.screen_width, config.screen_height)
            pause
            povi "Holy shit, she nearly took my fingers off with how hard she just clenched down with her pussy."
            scene date 21pm 047a #mom close up eyes almost closed mouth open enjoying it
            mom "Hhhhnnng..."
            povi "Haha, she's so horny, I'm sure she want's to go further."
            pov "<whisper> Quick, turn around and bend over. I'm going to pretend to fuck you."
            pov "<whisper> That way if that asshole gets bold and tries to open the stall door, he won't be able to see your face."
            "She doesn't even hesitate and obediently turns around and holds her backside up for you."
            scene date 21pm 048a #mom close up, bent over showing pussy and ass
            pov "<whisper> Perfect! Now just relax!"
            pov "That's a good girl! Keep that ass up high for me!"
            mom "Hah... <whisper> Ok..."
            povi "I don't know how this night could get any better... Well that's not exacty true."
            pov "<whisper> Ok, get ready. I'm going to place my cock between your cheeks now. I just didn't want to you be too surprised."
            mom "Hnn..."
            scene date 21pm 049a #mom close up bent over penis against pussy
            if inc == True:
                povi "Maybe I can actually fuck my mom. I don't think I can wait much longer!"
            else:
                povi "Maybe I can actually fuck [mother]. I don't think I can wait much longer!"
            if spot1000anim == True:
                image date 21pm 050aa = Movie(channel="date 21pm 050aa", play="edited/anim//spot1000/date/21pm 050aa.webm")
                scene date 21pm 050aa with dissolve:
                    size (config.screen_width, config.screen_height)
                pause
            else:
                scene date 21pm 050a #mom close up side view bent over penis against pussy
            mom "<whisper> Oh god, I can feel it!"
            pov "<whisper> Remember what I said. It has to be realistic!"
            if momcorruption < 60:
                mom "<whisper> Wait! You can stop now. I think he's gone."
                pov "<whisper> You sure? Maybe we should keep going for bit before we risk it."
                mom "<whisper> I'm sure! just check please!"
                scene date check guy
                pov "You were right, he's gone now..."
                povi "Damn, I wonder if I could have done more if she was more corrupted?"
            else:
                if spot1000anim == True:
                    image date 21pm 050aa = Movie(channel="date 21pm 050aa", play="edited/anim//spot1000/date/21pm 050aa.webm")
                    scene date 21pm 050aa with dissolve:
                        size (config.screen_width, config.screen_height)
                    pause
                else:
                    scene date 21pm 050a #mom close up side view bent over penis against pussy
                mom "<whisper> Wait, do you thinkg we should stop now, isn't this going too far?"
                povi "So the other things before were ok? I think she only needs a little push."
                pov "<whisper> No, we can't stop now. He could come in here at any moment."
                povi "Although, I haven't heard him speak in a while... He might have left already."
                povi "I don't think I could stop now if I wanted to though!"
                jump ndate421fuck
    $ momcorruption += 1
    jump ndate521

label ndate421fuck:
    call screen ndate421fuck1

screen ndate421fuck1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate421fuck1'), Jump('ndate421ass')) hovered tt.Action ("Fuck her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate421fuck1'), Jump('ndate421pussy')) hovered tt.Action ("Fuck her pussy") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate421ass:
    scene date 21pm 049a #mom close up bent over penis near pussy and ass
    $ momanal += 1
    povi "Here goes nothing... or possibly everything."
    pov "Take it in your ass, slut! You're gushing pussy can wait!"
    "You press the tip of your cock inside her ass."
    if spot1000anim == True:
        image date 21pm 051aba = Movie(channel="date 21pm 051aba", play="edited/anim//spot1000/date/21pm 051aba.webm")
        scene date 21pm 051aba with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm 051ab #mom close up bent over penis in ass
    mom "Haaahhh..."
    pov "Hope you're ready to get pounded into oblivion you whore!"
    povi "Nice, her juices made her asshole nice and wet too."
    if spot1000anim == True:
        image date 21pm 052aa = Movie(channel="date 21pm 052aa", play="edited/anim//spot1000/date/21pm 052aa.webm")
        scene date 21pm 052aa with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm 052a #mom close up side view bent over penis inside ass
    mom "Oh... Hgnn... you're..."
    pov "<whisper> You're doing so good! Keep playing along!"
    pov "You're so damn tight. I've waited so long to fuck this tight little asshole!"
    mom "HNNGG... HNNGG..."
    povi "She's shaking. I bet she waited for it after getting so horny before."
    povi "I need to give it my best to get her off too!"
    scene date 21pm 053ab #mom close up bent over penis in ass deeper
    with vpunch
    pov "Here take me all in! Enjoy my hard dick fucking your ass!"
    with vpunch
    mom "Hah... hah... hah..."
    povi "Damn, she's getting tighter and moving with my rhythm. She's close to cumming."
    with vpunch
    mom "Hah... hnng..."
    povi "I'm so close to cumming too, she's so tight!"
    scene date 21pm 054a #mom close up side view bent over penis inside ass all the way
    if momfirstfuck == False:
        if inc == True:
            povi "I'm fucking my mom ih the ass for the first time and she's about to cum with me!"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it!"
            with vpunch
        else:
            povi "I'm fucking [mother] in the ass for the first time and she's about to cum with me!"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it!"
            with vpunch
    else:
        if inc == True:
            povi "I'm fucking my mom in the ass and she's about to cum with me!"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it!"
            with vpunch
        else:
            povi "I'm fucking [mother] in the ass and she's about to cum with me!"
            pov "You're about to cum from my hard dick? Then enjoy it because you earned it!"
            with vpunch
    jump ndate421cum

label ndate421cum:
    call screen ndate421cum1

screen ndate421cum1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate421cum1'), Jump('ndate421inass')) hovered tt.Action ("Cum inside her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate421cum1'), Jump('ndate421out')) hovered tt.Action ("Cum on her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate421inass:
    scene date 21pm 054a #mom close up side view bent over penis inside ass all the way
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
    povi "She's cumming. I can feel it."
    pov "<whisper> I'm going to cum inside you!"
    "You spurt your sperm inside her asshole."
    with vpunch
    mom "Haaah... Hnnng..."
    pov "Fuck yes you slut, I'm going to fill that ass with my cum!"
    with vpunch
    mom "Oh... fuck! Fill me baby! God... Hggnn..."
    with vpunch
    mom "Hnnn....."
    "After a few more spasms you slowly pull your dick out."
    "She quivers as you slide out of her and mixture of your cum and her juices drips out of her ass and onto the floor."
    scene date 21pm 056a #mom close up bent over cum out of ass
    if inc == True:
        povi "What a wonderful view! My cum is dripping out of my mom's ass."
    else:
        povi "What a wonderful view! My cum is dripping out of [mother]'s ass."
    povi "She came so hard too! I didn't think she'd let me pull out after she was squeezing me so tight."
    if ndate21photoinass == False:
        povi "I should capture this moment."
        scene date photo1
        povi "Done!"
        $ ndate21photoinass = True
    $ ndate21ass = True
    $ ndate21inside = True
    jump ndate521fucked

label ndate421out:
    scene date 21pm 054a #mom close up side view bent over penis inside her all the way
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
    povi "She's cumming. I can feel it."
    pov "<whisper> I'm going to come on your ass and cover you with my sperm!"
    scene date 21pm 055a #mom close up bent over cumming on ass
    pov "Aaahhh..."
    povi "She go me so worked up, look how much cum is on her!"
    scene date 21pm 056 #mom close up bent over cum on of ass
    if inc == True:
        povi "What a wonderful view! My cum smeared on my mom's ass."
    else:
        povi "What a wonderful view! My cum smeared on [mother]'s ass."
    povi "She came hard too!"
    if ndate21photoover == False:
        povi "I should capture this moment."
        scene date photo3
        povi "Done!"
        $ ndate21photoover = True
    $ ndate21outside = True
    jump ndate521fucked

label ndate421pussy:
    scene date 21pm 049a #mom close up bent over penis near pussy and ass
    $ mompussy += 1
    povi "Here goes nothing... or possibly everything."
    pov "Take it in your pussy, slut! It's so wet, I'm going to slide in with ease!"
    "You press the tip of your penis inside her"
    if spot1000anim == True:
        image date 21pm 051aa = Movie(channel="date 21pm 051aa", play="edited/anim//spot1000/date/21pm 051aa.webm")
        scene date 21pm 051aa with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm 051a #mom bent over penis inside pussy
    mom "Haaahhh..."
    pov "Now get ready to get fucked hard!"
    povi "Her pussy is almost squeezing me out."
    if spot1000anim == True:
        image date 21pm 052aa = Movie(channel="date 21pm 052aa", play="edited/anim//spot1000/date/21pm 052aa.webm")
        scene date 21pm 052aa with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm 052a #mom bent over side view penis inside pussy
    pov "<whisper> You doing good! Keep playing along"
    pov "You're so damn tight. I've waited so long to give you a good fucking!"
    mom "HNNGG... HNNGG..."
    povi "She's shaking. She's into this as much as I am!"
    povi "I need to give it my best to get her off too!"
    pov "Here take me all in! Enjoy my hard dick fucking you!"
    scene date 21pm 053a #mom bent over deep inside pussy
    with vpunch
    mom "Hah... hah... hah..."
    povi "Damn, she's getting tighter and moving with my rhythm. She's close to cumming."
    with vpunch
    mom "Hah... hnng..."
    povi "But I can't let her cum alone now!"
    with vpunch
    scene date 21pm 054a #mom close up side view bent over penis inside her all the way
    if momfirstfuck == False:
        if inc == True:
            povi "I'm fucking my mom for the first time and she's about to cum with me!"
            pov "You're about to cum on my hard dick? Then enjoy it because you earned it!"
            with vpunch
        else:
            povi "I'm fucking [mother] for the first time and she's about to cum with me!"
            pov "You're about to cum on my hard dick? Then enjoy it because you earned it !"
            with vpunch
    else:
        if inc == True:
            povi "I'm fucking my mom and she's about to cum with me!"
            pov "You're about to cum on my hard dick? Then enjoy it because you earned it !"
            with vpunch
        else:
            povi "I'm fucking [mother] and she's about to cum with me!"
            pov "You're about to cum on my hard dick? Then enjoy it because you earned it !"
            with vpunch
    jump ndate421cum2

label ndate421cum2:
    call screen ndate421cum3

screen ndate421cum3():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate421cum3'), Jump('ndate421inpussy')) hovered tt.Action ("Cum inside her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('ndate421cum3'), Jump('ndate421out')) hovered tt.Action ("Cum on her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label ndate421inpussy:
    scene date 21pm 054a #mom close up side view bent over penis inside her all the way
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
    povi "She's cumming. I can feel it."
    pov "<whisper> I'm going to cum deep inside you!"
    "You spurt your sperm inside her pussy."
    with vpunch
    mom "Haaah... Hnnng..."
    pov "Oh god yes, take my cum you whore!"
    with vpunch
    mom "Yes! Fuck... I feel it... inside..."
    mom "Hnn...."
    "After a few moments longer your cock stops spasming and cumming inside her. You slowly pull your dick out."
    "She quivers as you slide out of her and mixture of your cum and her juices drips out of her pussy and onto the floor."
    scene date 21pm 056b #mom close up bent over cum out of pussy
    if inc == True:
        povi "What a wonderful view! My cum is dripping out of my moms pussy."
    else:
        povi "What a wonderful view! My cum is dripping out of [mother]'s pussy."
    povi "I didn't think she's let me pull out with how hard her pussy was squeezing!"
    if ndate21photoinpussy == False:
        povi "I should capture this moment."
        scene date photo2
        povi "Done!"
        $ ndate21photoinpussy = True
    $ ndate21pussy = True
    $ ndate21inside = True
    jump ndate521fucked

label ndate521fucked:
    $ momfirstfuck = True
    "You both sit there breathing hard, coming down from your mutual orgasms."
    if inc == True:
        pov "I'm pretty sure he's gone now. We should go too, mom."
        mom "Hnn..."
        pov "Mom?"
    else:
        pov "I'm pretty sure he's gone now. We should go too, [pov]."
        mom "Hnn..."
        pov "[pov]?"
    "Finally, she turns around and sits down the toilet, facing you."
    scene date 21pm 057 #mom on toilet breasts hanging out after sex
    pov "Mom... are you ok?"
    scene date 21pm 058
    mom "You... you fucked me..."
    mom "hnn..."
    scene date 21pm 054b
    pov "Yes, I did. I'm sorry. I just couldn't help myself. We were both just enjoying it so much."
    pov "And it worked too. He didn't find you."
    scene date 21pm 058
    mom "But, there was no need... we shouldn't have gone that far."
    pov "Look, we could probably chalk this up to a life or death situation pushing us to do something crazy..."
    pov "But I think there is more to it than that. I think you wanted me to do that. Just like I wanted to do it."
    mom "..."
    pov "At any point you could have stopped me."
    pov "I would have stopped if you really wanted me to."
    mom "..."
    pov "I only wanted to protect you and I'm sorry again. If you think we went too far."
    pov "But I'm not going to lie to myself about it now and say I didn't love it every second of it."
    pov "And I'm pretty sure you loved it too. You came. Hard"
    scene date 21pm 052b
    mom "Hnng..."
    mom "Well yes... I did... but..."
    pov "It's ok I'm not judging you. I was right there with you."
    mom "Look, no one can ever know what we did here."
    mom "This needs to be just between us."
    scene date 21pm 054b
    if inc == True:
        pov "Ok, mom. I promise."
    else:
        pov "Ok, [mother]. I promise."
    mom "..."
    scene black
    povi "Ok, I still want to kick Davide's ass for putting us in danger..."
    povi "But I don't think that could have gone any better for me! Hot Damn!"
    "You go home together."
    "She is silent most of the trip home. You start to wonder if she is having second thoughts about your encounter."
    "But right when you are about to say something, she places her hand on your leg and smiles a little at you."
    "A naughtly little smirk."
    "Interesting..."
    $ d9rncorf = True
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label ndate521:
    scene date 21pm 098 #mom leaving bathroom stall
    mom "I'm glad he's gone. We should go now too."
    povi "Noooo! Damn it, maybe I'll get another chance next time."
    scene black
    "You go home together."
    $ d9rncor = True
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label ndate421menlove:
    scene date 21pm 033
    pov "What are you thinking?"
    mom "It might sound a little weird..."
    scene date 21pm 033b
    mom "I think we should pretend to make out, maybe he won't disturb us then."
    pov "Do you really think that will stop him?"
    mom "It's the best I can think of right now. We can't fight him."
    scene date 21pm 033
    if inc == True:
        povi "I might be going to hell for this, but I love the idea of \"pretending\" to make out with my mom!"
    else:
        povi "I might be going to hell for this, but I love the idea of \"pretending\" to make out with my mom's best friend!"
    povi "Alright, play it cool. Don't over react. I don't want her to get suspicious..."
    pov "OKAY!!!"
    povi "Shit! What the fuck was at that [pov]!"
    pov "I mean... okay..."
    scene date 21pm 033b
    povi "She's smiling again. At least she found it funny and not creepy."
    mom "<whisper> Ssshh... It's ok, just play along."
    pov "Alright."
    if spot1000anim == True:
        image date 21pm 030a = Movie(channel="date 21pm 030a", play="edited/anim//spot1000/date/21pm 030a.webm")
        scene date 21pm 030a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm 030
    povi "This is really bad. What was she thinking? I'm gonna get horny as fuck quick!"
    if spot1000anim == True:
        image date 21pm 031a = Movie(channel="date 21pm 031a", play="edited/anim//spot1000/date/21pm 031a.webm")
        scene date 21pm 031a with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        scene date 21pm 031
    povi "But then again, she did come up with this..."
    povi "She's holding me tighter and squeezing in even closer to me now."
    if lroom11kiss == True:
        if inc == True:
            povi "Is my resemblance to dad the reason?"
            povi "Like when she tried to make out with me when she was drunk in the living room?"
        else:
            povi "Is my resemblance to my father the reason?"
            povi "Like when she tried to make out with me when she was drunk in the living room?"
    povi "Then again, she's not drunk this time."
    mom "Hnnn..."
    scene date 21pm 036a
    povi "You must be kidding..."
    if inc == True:
        pov "<whisper> Mom, you need to stop inching closer..."
    else:
        pov "<whisper> [mother], you need to stop inching closer..."
    mom "<whisper> I know it may be a little uncomfortable, but just a little longer, [pov]."
    mom "<whisper> I'm sure this will work and help save us."
    povi "Damn, but my boner is killing me. She's going to feel it any moment."
    povi "Fuck it! I can't withstand her any longer."
    scene date 21pm 034b
    mom "Hmm...?"
    if inc == True:
        "You grab her head pull her lips to yours, kissing your mom."
    else:
        "You grab her head pull her lips to yours, kissing her."
    mom "Hmm..."
    povi "Oh yes!"
    if lroom11kiss == True:
        povi "And it's even better when she's not drunk."
    if momlove <= 30:
        scene date 21pm 040a
        mom "<whisper> What are you doing? I thought we were just going to pretend?"
        if inc == True:
            pov "<whisper> I'm sorry mom, I jsut couldn't stand it any longer. I want you!"
        else:
            pov "<whisper> I'm sorry [mother], I couldn't withstand it. I want you!"
        mom "<whisper> Cut that out! I can't beleive you're joking at a time like this!"
        jump ndate21lstop
    else:
        scene date 21pm 035a
        mom "<whisper> What are you doing? I thought we were just going to pretend?"
        if inc == True:
            pov "<whisper> I'm sorry mom, I jsut couldn't stand it any longer. I want you!"
        else:
            pov "<whisper> I'm sorry [mother], I couldn't withstand it. I want you!"
            scene date 21pm 035b
        if inc == True:
            mom "<whisper> I'm sorry I put you in this situation, son."
        else:
            mom "<whisper> I'm sorry I put you in this situation, [pov]."
        mom "<whisper> I think it would be ok if you wanted to pretend just a little bit longer."
        pov "<whisper> I do! I really do"
        scene date 21pm 036b
        "You kiss her again."
        mom "<whisper> Hmm... Hmm..."
        povi "Wow, she's kissing me back. She must like it too."
        scene date 21pm 037b
        mom "Hnn... <whisper> oh sweetie..."
        povi "She's trembling. Is this her weak point?"
        if inc == True:
            "You gently kiss and nuzzle your mother's soft neck, little moans escape her lips"
        else:
            "You gently kiss and nuzzle her soft neck, little moans escape her lips"
        mom "Hmmmm... that's nice..."
        pov "<whisper> You love it getting kissed like this, don't you?"
        mom "Hah... <whisper> yes... but we shouldn't..."
        if momlove <= 50:
            scene date 21pm 040a
            mom "<whisper> We need to stop this! It's going too far."
            pov "<whisper> But you liked it. And I know you love me too."
            mom "<whisper> We just can't do this anymore."
            jump ndate21lstop
        else:
            scene date 21pm 038b
            pov "<whisper> I think we should."
            mom "Hmm... <kiss>"
            if inc == True:
                pov "<whisper> I won't judge you, mom. You know that I love you!"
            else:
                pov "<whisper> I won't judge you, [mother]. You know that I love you!"
            mom "Hm... yes..."
            povi "Wow! She's using her tongue now."
            "You two kiss for a long while, feeling each others mouths with your tongues."
            "Both of your breathing becomes heavy with desire."
            povi "I want to taste and feel even more of her."
            "You stop kissing her and just watch her beautiful face as you move your hands down the front of her dress."
            scene date 21pm 047a
            pov "<whisper> I've wanted to hold you like this for so long."
            "You slide her dress to the side as you free her left breast. Brushing her soft flesh with your finger tips."
            scene date 21pm 034a
            mom "hnnng..."
            "You look back up to her just to make sure it's alright."
            scene date 21pm 044a
            pov "<whisper> Do you want me to stop?"
            mom "No... don't stop..."
            "You free her other breast from the confines of the dress."
            if spot1000anim == True:
                image date 21pm 037aa = Movie(channel="date 21pm 037aa", play="edited/anim//spot1000/date/21pm 037aa.webm")
                scene date 21pm 037aa with dissolve:
                    size (config.screen_width, config.screen_height)
                pause
            else:
                scene date 21pm 037a
            "Gently squeeze her nipple while you knead her other breast."
            mom "Hnngg! Oh baby..."
            pov "<whisper> I want to taste you mom, all of you."
            scene date 21pm 040b
            "You start plying little kisses as you make your way down her body."
            povi "Her breasts are so soft and warm."
            mom "<whisper> Oh... my... god..."
            povi "Yup, this was the right decision."
            mom "Hnn... hm..."
            povi "I can feel her heartbeat and her twitching, when my kisses hit her."
            povi "More!"
            scene date 21pm 041b
            pov "<sucking>"
            mom "Oh...? Hnn..."
            povi "Her hard nipples and I can tastes them."
            if inc == True:
                pov "<whisper> You're tits are so beautiful and tasty, mom!"
            else:
                pov "<whisper> You're tits are so beautiful and tasty, [mother]!"
            scene date 21pm 042b
            mom "Oh baby... <whisper> I..."
            mom "<whisper> Is, this is going too far..."
            pov "<whisper> I don't think so. Why are you worried? We care for each other don't we?"
            if inc == True:
                mom "<whisper> But we're related. What if someone finds out?"
            else:
                mom "<whisper> We're like family. What if someone finds out?"
            pov "<whisper> It's not wrong because we love each other. And this should be between us. No one else matters."
            mom "<whisper> But..."
            scene date 21pm 043b
            pov "<whisper> It's ok. I know you think you need to protest because it feels good. And maybe you're feeling a little guitly enjoying it..."
            pov "<whisper> You don't need to feel that way with me. I want this too. Please let me help you feel good..."
            mom "..."
            pov "<whisper> I'm sure it's been awhile since you've felt like this with someone, given the way we live now."
            if momlove <= 80:
                scene date 21pm 040a
                mom "<whisper> We need to stop this! It's going too far."
                pov "<whisper> But you liked it. And I know you love me too."
                mom "<whisper> We just can't do this anymore."
                jump ndate21lstop
            else:
                mom "Alright..."
                pov "<whisper> Just try to relax and enjoy this moment together!"
                pov "<whisper> There are no judgements here. Just two lovers enjoying each other."
                scene date 21pm 044b
                mom "Hnn..."
                if inc == True:
                    pov "<whisper> I just want to show you my love for you mom! You're my goddess!"
                    pov "<whisper> And I'll still be the son you're proud of, no matter how you decide."
                else:
                    pov "<whisper> I just want to show you my love for you [mother]! You're my goddess!"
                    pov "<whisper> And I'll still be the boy you're proud of, no matter how you decide."
                mom "Hm... <whisper> then... go on..."
                povi "Yes!"
                if inc == True:
                    pov "I love you mom!"
                else:
                    pov "I love you [mother]!"
                if spot1000anim == True:
                    image date 21pm 045ba = Movie(channel="date 21pm 045ba", play="edited/anim//spot1000/date/21pm 045ba.webm")
                    scene date 21pm 045ba with dissolve:
                        size (config.screen_width, config.screen_height)
                    pause
                else:
                    scene date 21pm 045b
                mom "Oh god... baby... I love you too."
                pov "<whisper> Your legs are so long and beautiful."
                mom "Hmm..."
                pov "<whisper> Your so beautiful."
                mom "Ohh..."
                povi "She's really getting into this now!"
                "You kiss your way to her wet panties, the smell her desire is putting off is intoxicating."
                scene date 21pm 046b
                "You kiss and gently lick her silk covered clit, it hardens with the attention."
                mom "Hah... hnn... Oh... Hnngg..."
                povi "She's trembling like crazy."
                if inc == True:
                    pov "<whisper> I've waited so long for this, mom!"
                else:
                    pov "<whisper> I've waited so long for this, [mother]!"
                mom "Hmm... don't stop baby... feels... hnn... good..."
                "You do stop, for a just a moment, to pull her panties to the side."
                if spot1000anim == True:
                    image date 21pm 047ba = Movie(channel="date 21pm 047ba", play="edited/anim//spot1000/date/21pm 047ba.webm")
                    scene date 21pm 047ba with dissolve:
                        size (config.screen_width, config.screen_height)
                    pause
                else:
                    scene date 21pm 047b
                mom "<heavy breathing>"
                pov "<whisper> So beautiful!"
                povi "Now to really get to work."
                if inc == True:
                    povi "I'm going to give my mom an orgasm she'll never forget!"
                else:
                    povi "I'm going to give [mother] an orgasm she'll never forget!"
                scene date 21pm 049b
                "Wet juices drip as you lick and suck her in earnest. She leans back, breathing heavier."
                mom "Hah... Hnng... oh... yes..."
                if inc == True:
                    pov "<whisper> You taste amazing, mom!"
                else:
                    pov "<whisper> You taste amazing, [mother]!"
                mom "Hah! <whisper> Your tongue! So good!"
                pov "<whisper> I told you that you'd love it!"
                mom "Hah! Hah!"
                povi "I found the right spot."
                scene date 21pm 050b
                mom "Hah! Yes, right there!"
                povi "Damn, she's so horny, she doesn't even try to be silent anymore."
                mom "Hah! Hnng! Oh God! Right there baby! Right there!"
                povi "And she's pressing me onto her."
                "You lick her faster and faster, flicking her clit and then reaching deep inside her folds with your tongue."
                mom "It's so damn good! More [pov]! More!"
                scene date 21pm 050bx
                mom "AHHH! AHHHH! GOD!!! YES!!!"
                povi "She's coming. And very hard. Trembling like crazy."
                mom "Hnng! Hnng..."
                "You keep teasing her clit when she's just about to stop cumming."
                povi "I won't let her stop..."
                mom "Oh... my god! Hah! Hah!"
                scene date 21pm 050b
                "You keep her orgasm going for a few minutes, she is nearly gasping for breath when you are done."
                mom "<heavy breathing> Hah... oh... wow..."
                mom "Hnng..."
                "You finally come up for air and see what you have done to her, for her."
                scene date 21pm 051b
                if inc == True:
                    pov "<whisper> It's fantastic to see you cum like this, mom!"
                else:
                    pov "<whisper> It's fantastic to see you cum like this, [mother]!"
                mom "Ha... Oh, Th... thank you..."
                pov "<whisper> You don't have to thank me. It was my pleasure! You made me very happy you let me help you like this."
                pov "<whisper> Gives me the chance to show you how much I love you!"
                if momlove >= 100:
                    mom "<whisper> But I didn't get a chance to show you how much I love you too..."
                    scene edited date 21pm 054bos
                    pov "<whisper> You already have. Every day you show me how much you care."
                    "She rubs her cheek in your hand, enjoying the feeling of being tenderly touched."
                    mom "<whisper> I want to show you that I love you even more..."
                    "She turns her head and takes your thumb into her mouth, teasing it with her tongue as she sucks."
                    scene date 21pm 046a
                    pov "<whisper> Oh..."
                    povi "Holy shit! This is so fucking hot! I'm rock hard again."
                    "She lets your thumb go with a soft wet pop and looks into your eyes."
                    scene date 21pm 046a
                    if inc == True:
                        mom "I want you too, Son."
                    else:
                        mom "I want you too, [pov]."
                    scene date 21pm 033a
                    "She stares at you as she shuffles a little bit. You realize she's taking off her panties!"
                    pov "<whisper> What are you doing?"
                    mom "It's ok..."
                    scene date 21pm 033
                    mom "I hope you're ready for this."
                    "She gets up quickly and turns around, bending over the on the toilet."
                    scene date 21pm 048a
                    povi "Holy fuck! Does she want me to have sex with her?"
                    povi "Please! Oh please! Oh please!"
                    mom "<whisper> I need you inside me sweetie."
                    povi "Thank you God!"
                    if inc == True:
                        pov "<whisper> Oh Mom!"
                    else:
                        pov "<whisper> Oh [pov]!"
                    "You pull your pants down and gently press your cock against her flesh."
                    scene date 21pm 049a
                    mom "<whisper> Oh baby, I can feel how hard you are."
                    pov "<whisper> You're so soft and warm..."
                    mom "<whisper> Do it sweetie, just go slow. I want to feel all of it."
                    "You slowly press yourself into her wet, hot folds, easily pressing the tip of your penis inside her."
                    if spot1000anim == True:
                        image date 21pm 051aa = Movie(channel="date 21pm 051aa", play="edited/anim//spot1000/date/21pm 051aa.webm")
                        scene date 21pm 051aa with dissolve:
                            size (config.screen_width, config.screen_height)
                        pause
                    else:
                        scene date 21pm 051a
                    pov "Oh... god..."
                    mom "Hnng.... Oh yes..."
                    if spot1000anim == True:
                        image date 21pm 050aa = Movie(channel="date 21pm 050aa", play="edited/anim//spot1000/date/21pm 050aa.webm")
                        scene date 21pm 050aa with dissolve:
                            size (config.screen_width, config.screen_height)
                        pause
                    else:
                        scene date 21pm 050a
                    mom "Hold it right here baby."
                    if inc == True:
                        mom "Let Mommy feel your tip for moment."
                    else:
                        mom "Let me feel your tip for moment."
                    povi "She's squeezing it inside her with the walls of her vagina."
                    pov "That's feels so good!"
                    mom "Just wait, I'm going to show you even more!"
                    "She presses herself against the wall and presses her ass backwards, shove more of your cock inside her"
                    if spot1000anim == True:
                        image date 21pm 052aa = Movie(channel="date 21pm 052aa", play="edited/anim//spot1000/date/21pm 052aa.webm")
                        scene date 21pm 052aa with dissolve:
                            size (config.screen_width, config.screen_height)
                        pause
                    else:
                        scene date 21pm 052a
                    mom "Hnngg... Oh shit... so big..."
                    pov "You're so tight!"
                    if inc == True:
                        "You look down to see yourself balls deep inside your mother."
                    else:
                        "You look down to see yourself balls deep inside her."
                    scene date 21pm 053a
                    mom "Oh baby, I feel so full. I love you baby."
                    "You press yourself into the hilt. Feeling your hips against her ass as press yourself as deeply inside as you possibly can."
                    scene date 21pm 054a
                    mom "Oh god baby! You're so deep."
                    pov "You feel amazing! I can feel you squeezing and pulling me in deeper."
                    mom "Hnng..."
                    mom "I need you baby. I need you to do me now!"
                    mom "Do me Hard. I need to feel you deeper!"
                    povi "Fuck yes!"
                    "You don't say anything as you slowly start to pull out your cock, bit by bit..."
                    if spot1000anim == True:
                        image date 21pm 051aa = Movie(channel="date 21pm 051aa", play="edited/anim//spot1000/date/21pm 051aa.webm")
                        scene date 21pm 051aa with dissolve:
                            size (config.screen_width, config.screen_height)
                        pause
                    else:
                        scene date 21pm 051a
                    "...before thrusting it back inside hard and fast!"
                    scene date 21pm 053a
                    with vpunch
                    mom "Oh GOD!!! YES!"
                    if spot1000anim == True:
                        image date 21pm 051aa = Movie(channel="date 21pm 051aa", play="edited/anim//spot1000/date/21pm 051aa.webm")
                        scene date 21pm 051aa with dissolve:
                            size (config.screen_width, config.screen_height)
                        pause
                    else:
                        scene date 21pm 051a
                    mom "Do me baby! Do me so hard!"
                    pov "My pleasure!"
                    scene date 21pm 053a
                    with vpunch
                    mom "Hmmm... Oh... Yes..."
                    if spot1000anim == True:
                        image date 21pm 051aa = Movie(channel="date 21pm 051aa", play="edited/anim//spot1000/date/21pm 051aa.webm")
                        scene date 21pm 051aa with dissolve:
                            size (config.screen_width, config.screen_height)
                        pause
                    else:
                        scene date 21pm 051a
                    mom "You're going so deep baby! Keep going!"
                    scene date 21pm 053a
                    with vpunch
                    mom "Hnng... Oh baby..."
                    if spot1000anim == True:
                        image date 21pm 051aa = Movie(channel="date 21pm 051aa", play="edited/anim//spot1000/date/21pm 051aa.webm")
                        scene date 21pm 051aa with dissolve:
                            size (config.screen_width, config.screen_height)
                        pause
                    else:
                        scene date 21pm 051a
                    if inc == True:
                        mom "That's it! Fuck me! Fuck mommy!"
                    else:
                        mom "That's it! Fuck me! Fuck meee!"
                    scene date 21pm 053a
                    with vpunch
                    mom "Please... Don't stop... Yes..."
                    if spot1000anim == True:
                        image date 21pm 051aa = Movie(channel="date 21pm 051aa", play="edited/anim//spot1000/date/21pm 051aa.webm")
                        scene date 21pm 051aa with dissolve:
                            size (config.screen_width, config.screen_height)
                        pause
                    else:
                        scene date 21pm 051a
                    "You thrust in and out of he with wild abandon! Both of you grunting and moaning as you rut like animals."
                    scene date 21pm 053a
                    with vpunch
                    mom "Haaaahhh... Aaaaahhhh..."
                    mom "Oh.... goood... I'm close baby, I'm so close again!"
                    if spot1000anim == True:
                        image date 21pm 051aa = Movie(channel="date 21pm 051aa", play="edited/anim//spot1000/date/21pm 051aa.webm")
                        scene date 21pm 051aa with dissolve:
                            size (config.screen_width, config.screen_height)
                        pause
                    else:
                        scene date 21pm 051a
                    povi "I'm not going to last much longer!"
                    if inc == True:
                        pov "Me too! I'm going to cum too, Mom!"
                    else:
                        pov "Me too! I'm going to cum too, [mother]!"
                    mom "Oh baby, come inside me..."
                    scene date 21pm 053a
                    with vpunch
                    if inc == True:
                        mom "Come inside Mommy!!!"
                    else:
                        mom "Come inside Meeee!!!"
                    scene date 21pm 054a
                    with vpunch
                    pov "I'm coming! I'm cumming inside you!"
                    with vpunch
                    mom "Yes! Oh god... I feel it! So deep... inside..."
                    with vpunch
                    mom "Hnn...."
                    "After a few moments longer your cock stops spasming and cumming inside her. You slowly pull your dick out."
                    "She quivers as you slide out of her and mixture of your cum and her juices drips out of her pussy and onto the floor."
                    scene date 21pm 056b
                    if inc == True:
                        povi "What a wonderful view! My cum is dripping out of my moms pussy."
                    else:
                        povi "What a wonderful view! My cum is dripping out of [mother]'s pussy."
                    povi "I didn't think she's let me pull out with how hard her pussy was squeezing anyway!"
                    "You both sit there breathing hard, coming down from your mutual orgasms."
                    "Finally, she turns around and sits down the toilet, facing you."
                    scene date 21pm 057 #mom on toilet breasts hanging out after sex
                    mom "Oh... wow... THat was... Amazing..."
                    "She fixes her dress and sits back down."
                    scene date 21pm 058
                    mom "Hnnn..."
                    mom "Get over here sweetie."
                    scene date 21pm 038b
                    "She pulls you and kisses you hard, her tongue escaping into your mouth once again."
                    scene date 21pm 035b
                    mom "I really do love you, you know."
                    pov "Yeah, I know. I love you too."
                mom "We should probably go now."
                povi "She's still seems a little unsure, but at least she showed me that she loves me too."
                scene date 21pm 035a
                mom "<whisper> Oh no! We totally forgot about Peter!"
                pov "<whisper> Shit, you're right, but I'm sure he's gone since he didn't disturb us."
                mom " <whisper> We should check before leaving the stall."
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
                pov "I need to know if you are really ok with what we just did?"
                pov "I know you and I came, but I want to know if you enjoyed doing it with me."
                mom "..."
                if inc == True:
                    pov "You know that I love you, and I just need to know, mom. Please tell me."
                else:
                    pov "You know that I love you, and I just need to know, [mother]. Please tell me."
                mom "I... I liked it what you were doing to me... What we were doing."
                mom "But no one can know about this!"
                scene date 21pm 054b
                if inc == True:
                    pov "Oh course Mom. No one will ever know about this! I love you and won't disappoint you."
                else:
                    pov "Oh course [mother]. No one will ever know about this! I love you and won't disappoint you."
                mom "Hnn..."
                pov "I'm so glad that we had this amazing moment together."
                if inc == True:
                    pov "And I'd be happy to pleasure you any time you need it, mom!"
                else:
                    pov "And I'd be happy to pleasure you any time you need it, [mother]!"
                mom "Hnng..."
                pov "But now let's go home!"
                mom "Yes, let's go."
                scene black
                "You go home together."
                "She is silent most of the trip home. You start to wonder if she is having second thoughts about your encounter."
                "But right when you are about to say something, she places her hand on yours and smiles a little at you."
                "A naughtly little smirk. You grasp her hand in yours and finish driving home that way."
                "Interesting..."
                $ momlove += 1
                $ momdateorgasm = True
                $ d9rnlovef = True
                if day == 6:
                    $ weekendactivities += 1
                    if weekendactivities >= 3:
                        jump weekendskip
                    else:
                        jump weekendacchoose
                else:
                    jump frontdoor

label ndate21lstop:
    scene date 21pm 052b
    mom "<whisper> Please take a look and see if Peter is gone. I want to go home."
    pov "<whisper> O... okay."
    scene date check guy
    "You look under the stalls for him."
    pov "He's gone!"
    scene date 21pm 052b
    mom "Then we should go home now!"
    pov "But..."
    mom "We're going now."
    scene black
    $ momlove += 1
    $ d9rnlove = True
    "You go home together."
    if day == 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

#----- Nicole Second Date (Corruption) -----
label nicoleweekendcor:
    hide screen locations
    $ momcorruption += 1
    scene black
    if inc == True:
        "You and your mother decide to have dinner at home together, just the two of you."
        "You cook dinner for you and your mom and wait for her to come back from her extra shifts."
    else:
        "You and [mother] decide to have dinner at home together, just the two of you."
        "You cook dinner for you and [mother] and wait for her to come back from her extra shifts."
    "You hear the front door open."
    scene weekend 8pm 001
    if inc == True:
        mom "Hey son, I'm back."
    else:
        mom "Hey [pov], I'm back."
    mom "Do you need help with dinner?"
    scene weekend 8pm 002
    mom "Oh? What a nice surprise, it's all done!"
    if inc == True:
        pov "Welcome back, mom."
    else:
        pov "Welcome back, [mother]."
    mom "Oh, the candle is a nice touch as well."
    scene weekend 8pm 003
    mom "I'm so happy you did this for me, sweetie. It's nice to have a man make an effort like this for me. It's been a long time."
    pov "It was my pleasure. Let's eat, we're going to be burning plenty of calories tonight."
    mom "So you have something planned for us this evening besides dinner?"
    if inc == True:
        pov "Of course! We're going to do some more mother-son bonding exercises tonight to build our relationship."
    else:
        pov "Of course! We're going to do some interpersonal communication exercises tonight to build our relationship."
    scene weekend 8pm 004c
    mom "Huh? You mean...?"
    pov "Well, you opened the door with handjobs, blowjobs and letting fuck your breasts. I though we'd take things even further now."
    mom "But... what else do you want?"
    if inc == True:
        pov "You know exactly what we need to do, mom!"
    else:
        pov "You know exactly what we need to do, [mother]!"
    pov "You have been wanting it as much as I have."
    pov "Your pussy needs to my dick deep inside it!"
    scene weekend 8pm 005c
    mom "You're serious. You really want to fuck me?"
    pov "Of course, a good slut needs to be ridden regularly."
    pov "And we have the house to ourselves all night tonight."
    mom "..."
    pov "It's ok, there's not need to say anything about that yet. We still need to eat."
    pov "But i was thinking, how about you remove your shirt, so it won't get dirty."
    mom "What? Oh..."
    "Without any more prompting she removes her shirt and let's it fall to the floor."
    scene weekend 8pm 006c
    pov "I see you know this needs to happen. I'm glad."
    mom "Hnnn..."
    pov "Cat got your tongue? We're all alone. You can say something if you want to."
    pov "Or are you afraid you'll admit you're getting wet just thinking about us... fucking all night long?"
    mom "Hnng..."
    pov "Well, let's eat now. You're going to need all the energy you can get. We're going to have a very long night."
    scene weekend 8pm 007c
    if inc == True:
        pov "Seriously mom, your breast are fucking fantastic!"
        mom "Hnng!"
        pov "I hope you're excited as I am mom."
    else:
        pov "Seriously [mother], your breast are fucking fantastic!"
        mom "Hnng!"
        pov "I hope you're excited as I am [mother]."
    pov "After tonight, we're going to be doing all sorts of horribly dirty things together. Whenever we want to."
    mom "..."
    pov "And you won't have to worry about that loser of a husband trying to please you and failing again and again."
    pov "I'll be the one fucking you until you cry out in pleasure, begging for more."
    mom "Hnng!"
    pov "Since I'm number 2 in the gang, for now, the others will be too afraid to mess with you. You'll be safe, so long as you're with me."
    scene weekend 8pm 008c
    pov "And your luscious tits will get plenty of attention too. They'll be groped and licked and sucked daily."
    mom "Please stop talking like that..."
    scene weekend 8pm 009c
    if inc == True:
        pov "Why, mom?"
    else:
        pov "Why, [mother]?"
    pov "Didn't you choose this? You decided to allow this craziness into your home. And you decided to give yourself to the gang. For the good of the family right?"
    mom "Hnng..."
    pov "Well, I plan to make you live with the consequences of your choices."
    pov "You are going to be my personal slut. You will learn your place is next to me and that I own your body."
    scene weekend 8pm 010c
    pov "Now eat, my dick needs to be inside that pussy!"
    mom "Hnng..."
    "You two eat dinner together, silently."
    scene weekend 8pm 011c
    "After you two finish eating, [mother] clears the dishes and stands obediantly before, waiting for her next command."
    pov "Now go downstairs. I choose a very special outfit for you. Put it on and wait for me."
    pov "And when I come down there, I'm certain you'll remember to be a good girl and do everything I tell you to."
    mom "But..."
    if inc == True:
        pov "No complaining, mom!"
    else:
        pov "No complaining, [mother]!"
    pov "You wanted someone to take care of you! Someone to keep the others in line. This is the cost of your freedom. This is what you wanted."
    mom "Hnn..."
    scene black
    "She goes down at the basement."
    "You follow her after a few minutes."
    povi "I can't wait to see how great she'll look in that outfit."
    scene weekend 10pm 051cp
    "You see her standing at the back of the room. It's just want you were hoping for."
    mom "What are you thinking, [pov]? You just gave me lingerie to wear."
    povi "Oh, she's feeling rebellious again. I like it."
    povi "I am looking forward to breaking her down even more. Soon she'll do everything I want. No questions."
    pov "Then how about you come here and tell me face to face, instead of standing way back there like a coward!"
    mom "Hnng..."
    scene weekend 10pm 052cp
    "She slowly walks up to you, but you can already see her lose some of her resolve."
    mom "I can't believe... you'd make me wear this."
    pov "Why is that such a surprise? I chose a very special outfit for a very special occasion. That makes perfect sense to me."
    mom "Special occasion?"
    pov "Of course, tonight is the night you give yourself to me, completely."
    scene weekend 10pm 053cp
    pov "And look! You see these black accents here? They are not just there to look good."
    mom "Huh? What do you mean?"
    pov "They serve a delightful function as well."
    scene weekend 10pm 054cp
    pov "They're removable!"
    mom "Oh! But... that's..."
    pov "And now your special assets are fully exposed! See how tight the underwear is?"
    if inc == True:
        pov "Your tits are pushing against the fabric like they want to get free. God you're so alluring in this mother!"
    else:
        pov "Your tits are pushing against the fabric like they want to get free. God you're so alluring in this [mother]!"
    scene weekend 10pm 055cp
    if inc == True:
        mom "This... this is so wrong. I'm your mother and you're treating me like your sextoy."
    else:
        mom "This... this is so wrong. I'm your mother's best friend and you're treating me like your sextoy."
    pov "That's exactly what you are though. You asked me to be the bad boy. And bad boys need their hot sluts!"
    mom "What are you talking about!"
    if inc == True:
        pov "I choose you to be my hot slut, mom!"
    else:
        pov "I choose you to be my hot slut, [mother]!"
    mom "[pov]!"
    pov "Who else could it have been? It was always going to be you. Admit it, you want it to be you!"
    "You reach out to hold her face with your hand."
    scene weekend 10pm 056cp
    "She doesn't pull her face away, but instead she leans in and presses her check into your hand."
    povi "She's nearly over the line. I can tell."
    if inc == True:
        pov "I choose you because you're so strong. You're so confident, mom!"
    else:
        pov "I choose you because you're so strong. You're so confident, [mother]!"
    mom "What?"
    pov "A weaker woman would lost her mind and have gone crazy in this situation."
    pov "You've done whatever you could to stay true to yourself and protect your family for over a year and I'm sure you could do it even longer if you had to."
    pov "But you don't have to do this alone anymore. Not while I am here. And not while you are keeping me, happy..."
    mom "But why we have to do sexual things?"
    pov "You know why. You are the one that opened that door. And why not? You enjoy doing those things with me as much as I do."
    scene weekend 10pm 057cp
    "You reach out to pinch her exposed nipple."
    mom "Hah..."
    pov "See, your nipple is already hard."
    mom "Hnng... stop..."
    scene weekend 10pm 058cp
    "She doesn't actually seem that eager to stop you."
    povi "She wants this. That protests are just for show, even if only for her own modesty."
    if inc == True:
        pov "And if we are going to keep playing along with dad's mission, I am going to need to choose a slut. It's part of being a gang member."
    else:
        pov "And if we are going to keep playing along with Bruce's mission, I am going to need to choose a slut. It's part of being a gang member."
    mom "Hnn..."
    if inc == True:
        pov "You know there are rules to follow. If I choose you, then you have to be my slut, mom."
    else:
        pov "You know there are rules to follow. If I choose you, then you have to be my slut, [mother]."
    pov "And I'm fully aware that your body sometimes betrays you. I know you enjoy doing \"forbidden\" things."
    mom "But..."
    scene weekend 10pm 059cp
    pov "I'm even willing to bet that when I touch your pussy now, it'll be wet."
    mom "No, don't..."
    scene weekend 10pm 060cp
    mom "Hnng..."
    pov "Just as I thought."
    if inc == True:
        pov "You're practially flooding, mom."
    else:
        pov "You're practially flooding, [mother]."
    mom "Hnn..."
    scene weekend 10pm 061cp
    pov "There is no need to deny it anymore. I choose you because I understand you. I want you."
    mom "You want me..."
    pov "And I need your help."
    mom "Help...?"
    pov "I need a strong woman standing with me. We need to fix this situation together."
    pov "I'm sure you've already noticed that this is too much for Bruce. He can't handle all of this."
    pov "But I can. And I will. And with your help this will be over much sooner rather than later."
    pov "And it would make me much happier, if I know you wanted this too."
    mom "Hmm..."
    if inc == True:
        pov "I need you to look at me, mom!"
    else:
        pov "I need you to look at me, mom!"
    scene weekend 10pm 062cp
    pov "Are you my slut? Are you with me?"
    mom "..."
    mom "But why do you have to call me a slut all the time?"
    pov "When we're with the gang, it's what I'll be expected to call you."
    pov "It's easier to get used to it now when we're alone than it is in front of the others right?"
    mom "Hmm... Well, yes."
    pov "Then I'm going to need you to say it. Tell me who you are!"
    mom "I... I'm your... slut..."
    pov "Good girl! Now I want you to lay yourself down on that table and get ready for me."
    mom "Ready?"
    pov "You know what we have to do now."
    pov "Sooner or later we need to take this step to be taken serious by the others. If we do it now, it'll be easier."
    mom "..."
    pov "And I want to know that you are truly my slut. That you want this."
    pov "I'm hard as a rock and you're flooding wet, seems like it's the perfect time to fuck."
    if inc == True:
        pov "Show me that I made the right choice, mom. Choosing you as my slut."
    else:
        pov "Show me that I made the right choice, [mother]. Choosing you as my slut."
    mom "I... I'll get ready for you..."
    "She moves over to the table and lays down, her legs spread open, ready to recieve you."
    scene weekend 10pm 065cp
    #----- Insert Evil Villian Monologue Here -----
    povi "Wow. That took more convincing that I first thought, but it succeeded."
    povi "I've told her a story, much of which is true. We need to solve this together. And it's going to take doing things she doesn't want to do at first. For the mission."
    povi "The more she does, the more she'll accept. And on the way she'll lower her expectations for herself, because she'll need to in order to live it."
    povi "And then I can break her completely, make her into the slut I want, at all times. But I'll need to keep a tight schedule with regular training to keep her on track."
    povi "But finally it's time to fuck her and shatter that last taboo between us. I don't think that will be an issue tonight, she so wet. She wants to do this."
    scene weekend 10pm 066cp
    pov "God, you're going make me bust just for looking at you, laying like that in front of me. Inviting me inside you."
    pov "I can't wait to feel your wet, hot pussy on my dick, slut."
    pov "You're going to get the greatest fuck of your life. I waited so long for this."
    scene weekend 10pm 067cp
    mom "Hnn..."
    pov "You feel my hard dick rubbing on the entrance to your pussy?"
    mom "Y... yes..."
    pov "I want you to ask me for it, by name."
    pov "Everything is going to change between now and I want know you're all in."
    if inc == True:
        pov "You're going have sex with your son now, mom."
    else:
        pov "You're going have sex with me now, [mother]. You're best friend's son."
    scene weekend 10pm 068cp
    mom "I... can't. This is just too much..."
    pov "I got the impression that you understood our situation. That you wanted this."
    pov "When you agreed to be my slut, you agreed to obey me no matter what I asked of you!"
    mom "Hnng..."
    pov "I won't fuck if you don't ask me for it. I can leave if this is truly \"just too much\" for you."
    mom "Wait! Hnng... please fuck me, [pov]."
    if inc == True:
        mom "Fuck me son! Fuck mommy!"
    else:
        mom "Fuck me [pov]! Please!"
    if inc == True:
        pov "That's what I need to hear. I'll fuck you as hard as I can now, mom. I promise."
        povi "I can't believe it. I'm going to fuck my mom and she even asked me to do it."
    else:
        pov "That's what I need to hear. I'll fuck you as hard as I can now, [mother]. I promise."
        povi "I can't believe it. I'm going to fuck [mother] and she even asked me to do it."
    scene weekend 10pm 069cp
    pov "Wow, you're more then ready for my dick."
    mom "Hmm..."
    scene weekend 10pm 070cp
    "You press your dick deeper inside."
    mom "Hah... hnn..."
    pov "I can slide so easy, you so fucking wet, slut!"
    pov "Maybe I've found the perfect pussy? It's clinging onto me, begging to get fucked properly."
    mom "Hnn... hah... oh god..."
    if inc == True:
        pov "You want me to fuck you properly now, mom?"
    else:
        pov "You want me to fuck you properly now, [mother]?"
    povi "She needs to realize she wants this. I'm not forcing her. I don't want that to become an excuse later."
    mom "Yes, please fuck me properly [pov]!"
    scene weekend 10pm 071cp
    pov "As you wish. It's sliding in even further now."
    mom "Hnng... hnn..."
    pov "And now you can finally enjoy the pleasure of me fucking you!"
    mom "Hnn... hnn..."
    scene weekend 10pm 072cp
    mom "Haah...!"
    pov "Almost all the way inside you! And it seems that your pussy loves my dick!"
    "You start to fuck her wildly."
    scene weekend 10pm 073cp
    mom "Hah... hah... hah..."
    with vpunch
    pov "Yes, let yourself go. Enjoy it and cum with me, slut!"
    mom "Hah... [pov]... slow down..."
    with vpunch
    pov "No! I can't. I won't!"
    scene weekend 10pm 074cp
    with vpunch
    "You go even wilder!"
    mom "Hah... hah... so rough..."
    with vpunch
    if inc == True:
        pov "I can feel you shaking mom! You're close too."
    else:
        pov "I can feel you shaking [mother]! You're close too."
        with vpunch
    pov "You can't await to cum from my dick!"
    with vpunch
    mom "Hah... Hnng..."
    with vpunch
    pov "I'm about to cum too. You're a very good fuck, slut!"
    pov "Tell me where you want me to cum!"
    call screen nicoleweekendcorcum

screen nicoleweekendcorcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendcorcum'), Jump('nicoleweekendcorcuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendcorcum'), Jump('nicoleweekendcorcumoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicoleweekendcorcuminside:
    $ nicoleweekendcorinside = True
    jump nicoleweekendcorcumoutside

label nicoleweekendcorcumoutside:
    scene weekend 10pm 076cp
    if nicoleweekendcorinside == True:
        mom "Inside me! Oh god... Cum inside my pussy!"
    else:
        mom "Cover me! Oh god... Cum all over my body!"
    mom "HAAAAHH... AAAAHHH..."
    with vpunch
    pov "Yes, cum for me slut!"
    povi "Haha! I think she's still a little ashamed or shy about cumming in front of me."
    povi "But I can feel her body shaking."
    if nicoleweekendcorinside == True:
        if inc == True:
            pov "I'm cumming too! I want you to feel my hot sperm gushing deep inside you pussy, mom!"
        else:
            pov "I'm cumming too! I want you to feel my hot sperm gushing deep inside you pussy, [mother]!"
    else:
        if inc == True:
            pov "I'm cumming too! Mother!"
        else:
            pov "I'm cumming too! [mother]!"
    pov "HNNNG...!"
    if nicoleweekendcorinside == True:
        scene weekend 10pm 077cpi
        pov "I filled you up! It's spilling out. What a wonderful view."
        mom "Hah...hnng..."
    else:
        scene weekend 10pm 077cpo
        pov "I covered your stomach. What a wonderful view."
        mom "Hah... hnng..."
    scene weekend 10pm 078cp
    "[mother] is staring off is a sort of daze."
    if inc == True:
        pov "Come back to me, mom!"
    else:
        pov "Come back to me, [mother]!"
    "Your voice snaps her back from where ever her mind had wondered off to."
    scene weekend 10pm 073cp
    pov "Glad to have you back. Did it blow your mind for second there? Was it that good for you?"
    if inc == True:
        pov "We've done it. We're no longer just mother and son. We're lovers."
    else:
        pov "We've done it. We're no longer just and man and woman with needs. We're lovers."
    mom "Hnng..."
    "[mother] suddenly stands up and moves towards the stairs."
    if nicoleweekendcorinside == True:
        scene weekend 10pm 079cpi
        "[mother] suddenly stands up and moves towards the stairs."
        mom "I can't believe I did that. I can't believe we did that. And you even came inside me."
        pov "Yes I did. And that was easily the best decision I ever made!"
    else:
        scene weekend 10pm 079cpo
        "[mother] suddenly stands up and moves towards the stairs."
        mom "I can't believe I did that. I can't believe we did that. And you even came all over me."
        pov "Yes I did. And that was easily the best decision I ever made!"
    pov "Where do you think you're going, slut!"
    scene weekend 10pm 080cp
    with vpunch
    "You run up to her from behind and quickly shove your dick back inside her pussy."
    mom "AAAAHHH... What are you doing...?"
    pov "We're not done yet. We have all night long."
    if inc == True:
        pov "I'm going to fuck you until my dick falls off, mom!"
    else:
        pov "I'm going to fuck you until my dick falls off, [mother]!"
    scene weekend 10pm 081cp
    mom "Hah... hah... hnn..."
    with vpunch
    "You continue to fuck her."
    pov "I'll fuck you all night! So you can get a proper training, slut!"
    with vpunch
    scene weekend 10pm 082cp
    "You do what you promised her. You two fuck all night long."
    mom "Hah... hah... yes!"
    with vpunch
    pov "Don't you stop bouncing that ass on my cock, slut!"
    with vpunch
    "She gladly slams her hips up and down on your shaft while she moans."
    scene weekend 10pm 083cp
    mom "AAH... AAH... I'm cumming again, [pov]!"
    with vpunch
    mom "Don't stop... oh god... please don't stop!"
    with vpunch
    scene weekend 10pm 084cp
    mom "More, fuck me more. I need your dick [pov]!"
    with vpunch
    pov "As you wish, slut!"
    with vpunch
    scene weekend 10pm 085cp
    "You fuck through out the night until [mother] collapsed from exhaustion."
    "You decide to let her sleep. She more than fulfilled her duty to you, willingly participating all night long."
    povi "You'll become the perfect slut in time and then you'll never want to leave."
    scene black
    "At dawn you go back to your room and get some rest."
    $ nicoleweekendcorinside = False
    $ weekendactivities += 1
    $ mombasementcorsecond = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

#----- Nicole Second Date (Corruption - Love Version) ----- Done
label nicoleweekendcorlove:
    hide screen locations
    $ momlove += 1
    scene black
    if inc == True:
        "You and your mother decide to have dinner at home together, just the two of you."
        "You cook dinner for you and your mom and wait for her to come back from her extra shifts."
    else:
        "You and [mother] decide to have dinner at home together, just the two of you."
        "You cook dinner for you and [mother] and wait for her to come back from her extra shifts."
    "You hear the front door open."
    scene weekend 8pm 001
    if inc == True:
        mom "Hey son, I'm back."
    else:
        mom "Hey [pov], I'm back."
    mom "Do you need help with dinner?"
    scene weekend 8pm 002
    mom "Oh? What a nice surprise, it's all done!"
    if inc == True:
        pov "Welcome back, mom."
    else:
        pov "Welcome back, [mother]."
    mom "Oh, the candle is a nice touch as well."
    scene weekend 8pm 003
    mom "I'm so happy you did this for me, sweetie. It's nice to have a man make an effort like this for me. It's been a long time."
    pov "It was my pleasure. Let's eat. I think we're going to need plenty of energy for tonight."
    mom "So you have something planned for us this evening, besides dinner?"
    if inc == True:
        pov "Of course! I think we should do some more mother-son bonding exercises tonight to build our relationship."
    else:
        pov "Of course! I think we should do some interpersonal communication exercises tonight to build our relationship."
    scene weekend 8pm 004c
    mom "Huh? You mean...?"
    pov "Well, you opened the door with the handjobs, blowjobs and letting me fuck your breasts. I was hoping we could take things even further now."
    mom "But... what else do you want?"
    if inc == True:
        pov "I think you know exactly what I want, mom..."
    else:
        pov "I think you know exactly what I want, [mother]..."
    pov "I believe you have been wanting it as much as I have."
    pov "I want us to be together, completely."
    scene weekend 8pm 005c
    mom "You're serious. You really want to make love to me?"
    pov "Of course I do! Your everything I've ever wanted in a woman."
    pov "And we have the house to ourselves all night tonight."
    mom "..."
    pov "It's ok, there's not need to say anything about it yet. We still need to eat."
    pov "But I was thinking, maybe you should remove your shirt, so it won't get dirty."
    mom "What? Oh..."
    "Without any more prompting she removes her shirt and lets it fall to the floor."
    scene weekend 8pm 006c
    pov "So can I take that to mean you want me too?"
    mom "Hnnn..."
    pov "Cat got your tongue? We're all alone. You can say something if you want to."
    pov "Or are you afraid you'll admit you're getting excited just thinking about us... making love all night long?"
    mom "Hnng..."
    pov "Well, let's eat now. We're going to need all the energy we can get. I think we're going to have a very long night."
    scene weekend 8pm 007c
    if inc == True:
        pov "Seriously mom, your breast are so fantastic!"
        mom "Hnng!"
        pov "I hope you're excited as I am, mom."
    else:
        pov "Seriously [mother], your breast are so fantastic!"
        mom "Hnng!"
        pov "I hope you're excited as I am, [mother]."
    pov "After tonight, we're going to be doing all sorts of wonderful things together. Whenever we want."
    mom "..."
    pov "And you won't have to worry about Bruce trying to please you and failing again and again."
    pov "I'll be the one taking care of you until you cry out in pleasure, begging for more."
    mom "Hnng!"
    pov "And I promise, I'm going to keep the others away from you. We'll figure out a way out of this situation. I'm sure of it!"
    scene weekend 8pm 008c
    pov "And your boobs will get plenty of attention from me too. They'll be groped and licked and sucked daily."
    mom "Please sweetie, you shouldn't be talking like that..."
    scene weekend 8pm 009c
    if inc == True:
        pov "Why, mom?"
    else:
        pov "Why, [mother]?"
    pov "Don't you want this? Don't you want to stop feeling alone even when you in room filled with people?"
    mom "Hnng..."
    pov "Well, I know I want this. I want this more than anything!"
    pov "I want us to be together always! i want you to be truly happy. I want you to be safe and fulfilled."
    scene weekend 8pm 010c
    pov "Please eat, we can talk more about this afterwards!"
    mom "Hnng..."
    "You two eat dinner, quietly enjoying each other's company, but distracted by the conversation before."
    scene weekend 8pm 011c
    "After you two finish eating, you and [mother] clear the dishes and she stands by you, seemingly waiting to see what you'll do next."
    pov "Why don't you go downstairs and choose a very special outfit for you. Put it on and wait for me."
    pov "And when I come down there, we'll discuss this some more."
    mom "Ok..."
    if inc == True:
        pov "I love you, mom!"
    else:
        pov "I love you, [mother]!"
    pov "I just needed you to know that. More than anything else, I love you."
    mom "Hnnn..."
    scene black
    "She goes down to the basement."
    "You follow her after a few minutes."
    povi "I wonder what outfit she'll pick. It doesn't really matter. She looks amazing in everything down there."
    scene weekend 10pm 051cp
    "You see her standing at the back of the room. It's just want you were hoping for."
    mom "Is this what you were thing about, [pov]? I hope it's ok that I picked just lingerie to wear."
    povi "Is it ok? Um... hell yes it's ok!"
    povi "I am looking forward to this even more now. I'm pretty sure she is too. Seeing how she chose that outfit."
    pov "How about you come here and let me get a better look. Besides, it's going to be hard to talk with you standing way back there."
    mom "Hnng..."
    scene weekend 10pm 052cp
    "She slowly walks up to you, her steps are sultry and smooth."
    mom "I can't believe... I'm wearing this in front of you!"
    pov "Why is that such a surprise? I asked you to choose a very special outfit for a very special occasion. This makes perfect sense to me."
    mom "Special occasion?"
    pov "Of course, tonight is the night you we give ourselves to each other, completely."
    scene weekend 10pm 053cp
    pov "I have to say, I really like these black lace accents to the bra. They are pratically see-thru."
    mom "Oh! They are more that that..."
    pov "What do you mean?"
    mom "Pull on them. Go ahead."
    "You do as she asks and pull on them."
    scene weekend 10pm 054cp
    pov "They're removable!"
    mom "See! This is a very \"special\" outfit."
    pov "And now your \"special\" assets are fully exposed! The fit seems a little tight too."
    if inc == True:
        pov "Your breasts are pushing against the fabric like they want to be free. God you're so alluring in this mother!"
    else:
        pov "Your breasts are pushing against the fabric like they want to be free. God you're so alluring in this [mother]!"
    scene weekend 10pm 055cp
    if inc == True:
        mom "Is this... is this wrong? I'm your mother and you're treating me like your lover."
    else:
        mom "Is this... is this wrong? I'm your mother's best friend and you're treating me like your lover."
    pov "That's exactly what you are though. At least I hope you'll be. We love each other, that's all that should matter."
    mom "I do love you..."
    if inc == True:
        pov "I choose you, mom!"
    else:
        pov "I choose you, [mother]!"
    mom "Oh [pov]!"
    pov "Who else could it have been? It was always going to be you. Admit it, you want it to be you!"
    "You reach out to hold her face with your hand."
    scene weekend 10pm 056cp
    "She doesn't pull her face away, but instead she leans in and presses her check into your hand."
    povi "She's wants this. I know she does."
    if inc == True:
        pov "I choose you because you're so strong. You're so confident, mom!"
    else:
        pov "I choose you because you're so strong. You're so confident, [mother]!"
    mom "You really think so?"
    pov "A weaker woman would lost her mind and have gone crazy in this situation."
    pov "You've done whatever you could to stay true to yourself and to protect your family for over a year and I'm sure you could do it even longer if you had to."
    pov "But you don't have to do this alone anymore. Not while I am here. I won't let them hurt you!"
    mom "But are you sure you want to make our relationship sexual?"
    pov "Absolutely! You helped opened that door. And why not? You enjoy doing those things with me as much as I do."
    scene weekend 10pm 057cp
    "You reach out to pinch her exposed nipple."
    mom "Hah..."
    pov "See, your nipple is already hard."
    mom "Hnng... stop..."
    scene weekend 10pm 058cp
    "She doesn't actually seem that eager to stop you."
    povi "She wants this, I'm sure of it. I think she just feels the need to protest because of our situation."
    if inc == True:
        pov "And if we are going to keep playing along with dad's mission, we need to do this together."
    else:
        pov "And if we are going to keep playing along with Bruce's mission, we need to do this together."
    mom "Hnn..."
    if inc == True:
        pov "You're not alone anymore. Please mother. Let's stop pretending that we don't need this. That we don't need each other."
    else:
        pov "You're not alone anymore. Please [mother]. Let's stop pretending that we don't need this. That we don't need each other."
    pov "And believe that your body betrays your hidden feelings. I know you enjoy doing \"forbidden\" things with me."
    mom "But..."
    scene weekend 10pm 059cp
    pov "I'm even willing to bet that when I touch your pussy now, it'll be wet."
    mom "Wait..."
    scene weekend 10pm 060cp
    mom "Hnng..."
    pov "Just as I thought."
    if inc == True:
        pov "You're practially flooding, mom."
    else:
        pov "You're practially flooding, [mother]."
    mom "Hnn..."
    scene weekend 10pm 061cp
    pov "There is no need to deny it anymore. I choose you because I understand you. I want you."
    mom "You want me..."
    pov "And I need your help."
    mom "Help...?"
    pov "I need a strong woman standing with me. We need to fix this situation together."
    pov "I'm sure you've already noticed that this is too much for Bruce. He can't handle any of this."
    pov "But I can. And I will. And with your help this will be over much sooner rather than later."
    pov "I just need to konw that you want this too..."
    mom "Hmm..."
    if inc == True:
        pov "Please, look at me mom!"
    else:
        pov "Please, look at me [mother]!"
    scene weekend 10pm 062cp
    pov "Are you with me?"
    mom "..."
    mom "Do you really want me? Not just physically, but emotionally too?"
    mom "Do you want to be with me for the rest of our lives?"
    mom "Beacuse I don't think I can do this if it's just for a little while."
    mom "If I take that step... it's forever. There is no going back."
    povi "Wow, I didn't realize how much she must be thinking about us too.."
    pov "I'm all in. I promise. I don't just want your body. I want all of you!"
    mom "In that case, my answer is... yes."
    pov "Then show me."
    mom "I... I'll get ready for you..."
    "She moves over to the table and lays down, her legs spread open, ready to recieve you."
    scene weekend 10pm 065cp
    #----- Enter Sappy Speech Here -----
    povi "Wow. I can't believe we're actually going to do this."
    povi "I've had a crush on her for as long as I can remember, but I never thought we'd be here before I left for College."
    povi "But while I was away I thought of her every day. And when I got home things were just so bizarre. I couldn't believe it."
    povi "But seeing her struggling against this situation, it awakened that crush and became something much more."
    povi "And to think she's share those feelings... Well I just know we're going to get through this. Together. No matter what."
    scene weekend 10pm 066cp
    "You snap out of your reverie and get back to the business at hand."
    pov "God, you're going make me bust just from looking at you, laying like that in front of me. Inviting me inside you."
    mom "Hnng..."
    pov "I can't wait to finally be inside you. A part of you."
    pov "This is going to be the greatest night of my life. I waited so long for this."
    scene weekend 10pm 067cp
    mom "Hnn..."
    pov "Can you feel my hard dick rubbing on the entrance to your pussy?"
    mom "Y... yes..."
    pov "I want you to ask me for it. I want to know you crave me too."
    pov "Everything is about to change, forever."
    if inc == True:
        pov "You're going have sex with your son now, mom."
    else:
        pov "You're going have sex with me now, [mother]. You're best friend's son."
    scene weekend 10pm 068cp
    mom "I... can't wait. Please, this is just too much..."
    pov "Should I take that as a yes, you want me inside you? To fill you completely?"
    mom "Hnng..."
    pov "I won't do it until you ask me for it. I want to hear you call out my name."
    mom "Please! Hnng... please fuck me, [pov]."
    if inc == True:
        mom "Fuck me son! Fuck mommy!"
    else:
        mom "Fuck me [pov]! Please!"
    if inc == True:
        pov "That's what I need to hear, mom."
        povi "I can't believe it. I'm going to have sex with my mom and she even asked me to do it."
    else:
        pov "That's what I need to hear, [mother]"
        povi "I can't believe it. I'm going to have sex with my [mother] and she even asked me to do it."
    scene weekend 10pm 069cp
    pov "Wow, you're more then ready for me."
    mom "Hmm..."
    scene weekend 10pm 070cp
    "You press your dick deeper inside."
    mom "Hah... hnn..."
    pov "I can slide so easy, you so incredibly wet!"
    pov "I've found the perfect pussy! It's clinging onto me, pulling me in deeper."
    mom "Hnn... hah... oh god..."
    if inc == True:
        pov "You want me to start thrusting now, mom?"
        povi "I can feel her squeezing me everytime I call her mom. She gets so excited from the taboo nature of our relationship."
    else:
        pov "You want me to start thrusting now, [mother]?"
        povi "I can feel her squeezing me everytime I call her name. She wants this badly."
    mom "Yes, please fill my pussy with you cock [pov]!"
    scene weekend 10pm 071cp
    pov "As you wish. It's sliding in even further now."
    mom "Hnng... hnn..."
    pov "We're finally doing it. We're together at last."
    mom "Hnn... hnn..."
    scene weekend 10pm 072cp
    mom "Haah...!"
    pov "Almost all the way inside you! And it seems that your pussy loves my dick!"
    "You start to thrust inside her wildly."
    scene weekend 10pm 073cp
    mom "Hah... hah... hah..."
    with vpunch
    if inc == True:
        pov "Yes, let yourself go. Enjoy it and cum with me, mom!"
    else:
        pov "Yes, let yourself go. Enjoy it and cum with me, [mother]!"
    mom "Hah... [pov]... faster..."
    with vpunch
    pov "With pleasure!"
    scene weekend 10pm 074cp
    with vpunch
    "You go even wilder!"
    mom "Hah... hah... so rough..."
    with vpunch
    if inc == True:
        pov "I can feel you shaking mom! You're close too."
    else:
        pov "I can feel you shaking [mother]! You're close too."
        with vpunch
    pov "You can't await to cum from my dick!"
    with vpunch
    mom "Hah... Hnng..."
    with vpunch
    pov "I'm about to cum too. You're the best I've ever had!"
    pov "Tell me where you want me to cum!"
    call screen nicoleweekendcorlovecum

screen nicoleweekendcorlovecum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendcorcum'), Jump('nicoleweekendcorlovecuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendcorcum'), Jump('nicoleweekendcorlovecumoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicoleweekendcorlovecuminside:
    $ nicoleweekendcorinside = True
    jump nicoleweekendcorlovecumoutside

label nicoleweekendcorlovecumoutside:
    scene weekend 10pm 076cp
    if nicoleweekendcorinside == True:
        mom "Inside me! Oh god... Cum inside my pussy!"
    else:
        mom "Cover me! Oh god... Cum all over my body!"
    mom "HAAAAHH... AAAAHHH..."
    with vpunch
    if inc == True:
        pov "Yes, cum for me mom!"
    else:
        pov "Yes, cum for me [mother]!"
    povi "Haha! I think she's still a shy about cumming in front of me."
    povi "But I can feel her body shaking."
    if nicoleweekendcorinside == True:
        if inc == True:
            pov "I'm cumming too! I want you to feel my hot sperm gushing deep inside you pussy, mom!"
        else:
            pov "I'm cumming too! I want you to feel my hot sperm gushing deep inside you pussy, [mother]!"
    else:
        if inc == True:
            pov "I'm cumming too! Mother!"
        else:
            pov "I'm cumming too! [mother]!"
    pov "HNNNG...!"
    if nicoleweekendcorinside == True:
        scene weekend 10pm 077cpi
        pov "I filled you up! It's spilling out. What a wonderful view."
        mom "Hah...hnng..."
    else:
        scene weekend 10pm 077cpo
        pov "I covered your stomach. What a wonderful view."
        mom "Hah... hnng..."
    scene weekend 10pm 078cp
    "[mother] is staring off is a sort of daze."
    if inc == True:
        pov "Come back to me, mom!"
    else:
        pov "Come back to me, [mother]!"
    "Your voice snaps her back from where ever her mind had wondered off to."
    scene weekend 10pm 073cp
    pov "Glad to have you back. Did it blow your mind for second there? Was it that good for you?"
    if inc == True:
        pov "We've done it. We're no longer just mother and son. We're lovers."
    else:
        pov "We've done it. We're no longer just and man and woman with needs. We're lovers."
    mom "Hnng..."
    "[mother] suddenly stands up and moves towards the stairs."
    if nicoleweekendcorinside == True:
        scene weekend 10pm 079cpi
        "[mother] suddenly stands up and moves towards the stairs."
        mom "I can't believe I did that. I can't believe WE did that. And you even came inside me."
        pov "Yes I did. And that was easily the best decision I ever made!"
    else:
        scene weekend 10pm 079cpo
        "[mother] suddenly stands up and moves towards the stairs."
        mom "I can't believe I did that. I can't believe we did that. And you even came all over me."
        pov "Yes I did. And that was easily the best decision I ever made!"
    pov "Where do you think you're going!"
    scene weekend 10pm 080cp
    with vpunch
    "You run up to her from behind and quickly shove your dick back inside her pussy."
    mom "AAAAHHH... Oh baby, what are you doing...?"
    pov "We're not done yet. We have all night long."
    if inc == True:
        pov "We can't let this oppportunity pass, mom! We have all night long to ourselves!"
    else:
        "We can't let this oppportunity pass, [mother]! We have all night long to ourselves!"
    scene weekend 10pm 081cp
    mom "Hah... hah... hnn..."
    with vpunch
    "You continue to thrust deep inside her."
    pov "I need you! I don't want this to ever end! I promise, I won't stop if you won't."
    with vpunch
    scene weekend 10pm 082cp
    "You do what you promised her. You two make love all night long."
    mom "Hah... hah... yes!"
    with vpunch
    if inc == True:
        pov "I love the way you bounce that ass, mom!"
    else:
        pov "I love the way you bounce that ass, [mother]!"
    with vpunch
    "She gladly slams her hips up and down on your shaft while she moans."
    scene weekend 10pm 083cp
    mom "AAH... AAH... I'm cumming again, [pov]!"
    with vpunch
    mom "Don't stop... oh god... please don't stop!"
    with vpunch
    scene weekend 10pm 084cp
    mom "More, fuck me more. I need your dick [pov]!"
    with vpunch
    pov "As you wish!"
    with vpunch
    scene weekend 10pm 085cp
    "You to breed like rabbits through out the night until you both collapse from exhaustion."
    "You decide to you both could use the rest. She matched your insatiable desire for sex all night long. The perfect partner."
    povi "I still can't believe the night ended like this. It was amazing!"
    scene black
    "At dawn you two reluctantly go back to your own rooms get some rest."
    $ nicoleweekendcorinside = False
    $ weekendactivities += 1
    $ mombasementlovesecond = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

#----- Nicole Second Date (Love) ----- Done
label nicoleweekendlove:
    $ momlove += 1
    hide screen locations
    scene black
    if inc == True:
        "You and your mother decide to have dinner at home together, just the two of you."
        "You cook dinner for you and your mom and wait for her to come back from her extra shifts."
    else:
        "You and [mother] decide to have dinner at home together, just the two of you."
        "You cook dinner for you and [mother] and wait for her to come back from her extra shifts."
    "You hear the front door open."
    scene weekend 8pm 001
    if inc == True:
        mom "Hey son, I'm back."
    else:
        mom "Hey [pov], I'm back."
    mom "Do you need help with dinner?"
    scene weekend 8pm 002
    mom "Oh? What a nice surprise, it's all done!"
    if inc == True:
        pov "Welcome back, mom."
    else:
        pov "Welcome back, [mother]."
    mom "Oh, the candle is a nice touch as well."
    scene weekend 8pm 003
    mom "I'm so happy you did this for me, sweetie. It's nice to have a man make an effort like this for me. It's been a long time."
    pov "It was my pleasure. Let's eat. I think we're going to need plenty of energy for tonight."
    mom "So you have something planned for us this evening, besides dinner?"
    if inc == True:
        pov "Well nothing specific, I just want to spend as much time as I can with my lovely mom."
    else:
        pov "Well nothing specific, I just want to spend as much time as I can with a lovely woman, [mother]."
    scene weekend 8pm 004l
    mom "You're such a charmer!"
    mom "I'm so happy get to spend my weekend alone with such a gentleman."
    if gangmember == True:
        mom "And you're being awfully sweet, for a dangerous gangmember such as yourself."
    pov "Yes..."
    if inc == True:
        mom "Come here son."
    else:
        mom "Come here [pov]."
    scene weekend 8pm 005l
    mom "Hugging is something I've missed so much in this family."
    if inc == True:
        pov "Haha, we can stay forever like this if you want, mom."
    else:
        pov "Haha, we can stay forever like this if you want, [mother]."
    mom "I'd love that, but I'm also hungry, haha."
    scene weekend 8pm 006l
    mom "So let's eat."
    pov "Sounds great!"
    mom "I want to taste this delicous looking meat now."
    povi "She was looking right at me when she said that..."
    scene weekend 8pm 007l
    mom "I think I'm going to need a workout after eating such a hearty meal!"
    povi "I can think of something we can do together to burn calories. Naked. In bed."
    mom "But I don't want to waste a moment apart from you this evening. So you think we should watch some TV after this?"
    povi "Well, not my first choice, but any time with you is time well spent."
    pov "Sure that sounds fun. And if not, I'm sure we'll think of something to do."
    scene weekend 8pm 008l
    povi "Seriously, that cleavage just sucks me in."
    povi "I'm so glad we're alone together finally. None of the usual jackasses to worry about."
    mom "Yeah, maybe we should do something else..."
    povi "That sounded pretty flirty. Is she teasing me?"
    mom "[pov]!"
    scene weekend 8pm 009l
    pov "Huh?"
    mom "I see you're a bit distracted, haha. So do you have any other ideas about what we should do?"
    pov "Oh? I... Well... Sorry, I didn't it on purpose, I just..."
    mom "Shhh... Sometimes even a gentleman such as yourself, just can't stop themselves! <giggle>"
    povi "She's really is teasing me..."
    mom "You'll never finish eating if you're staring at me all the time."
    scene weekend 8pm 010l
    mom "Let's focus on eating for a bit. You'll have plenty of time for staring at me later..."
    povi "Seriously, she is such a tease tonight! What has gotten into her I wonder?"
    "You literally wolf down your meal."
    "You mother starts to get up."
    scene weekend 8pm 011l
    mom "I'm going to go change in something more comfortable. I'll be back in a few minutes. Ok sweetie?"
    pov "Of course. I can wait down here."
    scene weekend 8pm 011
    povi "Not that I want to... She worked me up with all that teasing. Did she do that on purpose?"
    povi "I want to be with her now. Naked. In bed. Sweating and writhing together."
    "You wait a few minutes thinking about you two making love together."
    povi "Screw it! I'm going up there!"
    "You head upstairs to her room and step inside, not really thinking beyond the fact that you want to be with her."
    scene weekend 8pm 012lb
    mom "There you are [pov]..."
    mom "I knew you couldn't wait until I was done changing."
    povi "Well, yeah. I haven't had a great track record for waiting thus far."
    pov "I... forgot to knock... sorry."
    povi "Seriously, that's what you come up with [pov]?!? You need to think before you act!"
    mom "You're such a poor liar..."
    scene weekend 8pm 013la
    mom "You were undressing me the entire time at dinner. You just couldn't stand it anymore, could you?"
    povi "So she was teasing me on purpose. She knows exactly how to press my buttons."
    mom "I had a feeling you might be up to something, when you put such an effort in preparing a fine meal like that."
    mom "I know you are a gentleman, but you can't be that all the time..."
    mom "It's not healthy for a strong, handsome young man like you to go without that which you desire for too long."
    if inc == True:
        mom "And I think you desire to see your mother naked. Or possibly... even more."
        mom "Something forbidden perhaps?"
    else:
        mom "And I think you desire to see me naked. Or possibly... even more."
    "She turns back around slightly and slowly peels her pants off in front of you, revealing her nakedness underneath."
    scene weekend 8pm 013lb
    pov "<gulp>"
    mom "Honestly dear, you could have chosen any other woman to pursue if you wanted, but you chose me..."
    if inc == True:
        mom "Your mother."
    else:
        mom "An older woman."
    scene weekend 8pm 014lb
    pov "There isn't anyone else I wanted, more that I want you."
    if inc == True:
        pov "And I think I've fallen in love with you, mom."
    else:
        pov "And I think I've fallen in love with you, [mother]."
    mom "You're so honest with me, and I want to be honest with you too."
    mom "You changed so much in just one year. And when you came home you were greeted with this... mess!"
    mom "Even so, you withstood the corruption and pushed back against the darkness around here."
    scene parentsroom 8pm 013a
    if inc == True:
        mom "I'm so very proud of the man you've become. I'm more than proud..."
        mom "I'm intenstly interested in my \"new\" son."
        mom "Even if a mother and son shouldn't share these desires, we do. We've sampled what is forbidden."
    else:
        mom "I'm so very proud of the man you've become. I'm more than proud..."
        mom "I'm intenstly in that man. In you."
        mom "Even if I shouldn't share your desires, I do. We've sampled what is forbidden."
    scene weekend 8pm 015lb
    mom "But now I think we should feast on it!"
    pov "Wow..."
    "She lays down on her bed, looking up to you."
    scene weekend 8pm 016lb
    mom "Well, what are you waiting for?"
    pov "Is this really happening?"
    mom "I bet it's already happened a thousand times in your mind. Just like it has in mine."
    mom "So show me that my fantasies are just a pale imitation of the real thing."
    "You undress in a hurried frenzy."
    mom "<giggle>"
    jump nicoleweekendloveroot

label nicoleweekendloveroot:
    scene weekend 8pm 016lb
    call screen nicoleweekendlovechoose

screen nicoleweekendlovechoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('nicoleweekendlovechoose'), Jump('nicolelovehead')) hovered tt.Action ("Kiss her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" action (Hide('nicoleweekendlovechoose'), Jump('nicoleloveboobs')) hovered tt.Action ("Choose her boobs") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendlovechoose'), Jump('nicolelovehands')) hovered tt.Action ("Ask for a handjob") focus_mask True
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('nicoleweekendlovechoose'), Jump('nicolelovebelly')) hovered tt.Action ("Kiss her belly") focus_mask True
        imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('nicoleweekendlovechoose'), Jump('nicolelovepussy')) hovered tt.Action ("Choose her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('nicoleweekendlovechoose'), Jump('nicolelovefeet')) hovered tt.Action ("Choose her feet") focus_mask True
        imagebutton auto "gui/icons/icon_cowgirl_%s.png" action (Hide('nicoleweekendlovechoose'), Jump('nicolelovecow')) hovered tt.Action ("Let her go on top") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('nicoleweekendlovechoose'), Jump('nicolelovestop')) hovered tt.Action ("Finish") focus_mask True
        if proom19lovesex == True:
            imagebutton auto "gui/icons/icon_skip1_%s.png" action (Hide('nicoleweekendlovechoose'), Jump('proom19extlovelanding')) hovered tt.Action ("Return to previous menu") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicolelovehead:
    pov "God, your lips are drawing me in!"
    mom "Hmm... I'm excited, baby."
    scene weekend 8pm 024lb
    pov "Hm... <kiss>"
    "You make out with her, holding each other close."
    mom "Hnng... <kiss>"
    if inc == True:
        pov "I want to taste you forever, mom."
    else:
        pov "I want to taste you forever, [mother]."
    "You move your kisses to her neck, nibbling and licking your way down it."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    #----- end -----
    scene weekend 8pm 025lb
    pov "<kiss> <lick>"
    mom "Hmm... that's the spot. It feels so good."
    pov "I love kissing your soft skin."
    mom "Hmm..."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicoleloveboobs:
    call screen nicoleweekendloveboobschoose

screen nicoleweekendloveboobschoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('nicoleweekendloveboobschoose'), Jump('nicolelovekissboobs')) hovered tt.Action ("Kiss her boobs") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" action (Hide('nicoleweekendloveboobschoose'), Jump('nicoleloveboobjob')) hovered tt.Action ("Ask for a boobjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicolelovekissboobs:
    pov "I need to taste those luscious mounds!"
    mom "<giggle> Please do!"
    scene weekend 8pm 026lb
    pov "<kiss> <suck>"
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    #----- end -----
    mom "Oh, slowly baby boy <giggle>."
    pov "I love sucking them so much."
    if inc == True:
        mom "You suck them so greedly. Like you did as a baby."
        pov "Oh mom!"
    else:
        mom "You suck them so greedy. Like you're a baby."
        pov "Oh [mother]!"
    mom "Hmm..."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicoleloveboobjob:
    pov "I would love to feel your breasts... around my..."
    mom "Oh, you want a boobjob, sweetie?"
    pov "Y... yes. Is that ok to ask?"
    mom "<giggle> You're so attracted to them. Lay down, honey."
    scene weekend 8pm 050la
    mom "I love the way you stare at me. Devouring me with your eyes."
    mom "<giggle> And you're always \"excited\" to see me!"
    pov "That's an understatement! I feel like my dick could rip a hole in pants when I'm around you."
    mom "Haha. Well the's understandable, you're so big. But I think we can put that to better use."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    #----- end -----
    scene weekend 8pm 051lb
    pov "Ohh... my god, it's so soft."
    mom "And your shaft is burning hot! I told you there would be plenty of time for staring. <wink>"
    pov "Oh I am, believe me! Getting a boobjob from you is the easily best."
    scene weekend 8pm 052lb
    mom "Then I'll put even more effort into it. <giggle>"
    mom "I want to spoil you baby."
    pov "Oh yes, this is heaven."
    mom "You're such a good boy, you earned this."
    if inc == True:
        pov "Oh mom. Your breasts feel so good."
    else:
        pov "Oh [mother]. Your breasts feel so good."
    scene weekend 8pm 053lb
    mom "I'm so glad you like it baby."
    pov "Ohh... Hmm... hah..."
    mom "You're shaking! Is it so good that you're about to cum now?"
    pov "Yes... yes, it's so damn good."
    mom "Then give it to me. Cum all over my tits for me sweetie."
    if inc == True:
        mom "Show your mommy how much you love her!"
    else:
        mom "Show me how much you love me!"
    pov "Oh my god!"
    scene weekend 8pm 054lb
    pov "Aaaahhh...!"
    with vpunch
    mom "You've covering me baby, it's so hot."
    scene weekend 8pm 055lb
    pov "Hnng..."
    with vpunch
    mom "You gave me so much sweetie. I'm so glad I could please you like that baby."
    pov "Oh... it was so great..."
    mom "So, do you want to have more fun or is my baby boy done? <giggle>"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovehands:
    pov "I would love to feel your hands... on my..."
    mom "Oh, you want a handjob honey?"
    pov "Y... yes. Would you?"
    mom "<giggle> Of course! Lay down."
    scene weekend 8pm 050la
    mom "I love the way you stare at me. Devouring me with your eyes."
    mom "<giggle> And you're always \"excited\" to see me!"
    pov "That's an understatement! I feel like my dick could rip a hole in my pants when I'm around you."
    mom "Haha. Well the's understandable, you're so big. But I think we can put that to better use."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    #----- end -----
    scene weekend 8pm 051la
    pov "Ohh... my god, it's so soft."
    mom "And your shaft is burning hot! I told you there would be plenty of time for staring. <wink>"
    pov "Oh I am, believe me! Your hands feel so good and I love how you're squeezing my ballsS."
    scene weekend 8pm 052la
    mom "Then I'll put even more effort into it. <giggle>"
    mom "I want to spoil you baby."
    pov "Oh yes, this is heaven."
    mom "You're such a good boy, you earned this."
    if inc == True:
        pov "Oh mom. Your hands feel so good."
    else:
        pov "Oh [mother]. Your hands feel so good."
    scene weekend 8pm 053la
    mom "I'm so glad you like it baby."
    pov "Ohh... Hmm... hah..."
    mom "You're shaking! Is it so good that you're about to cum now?"
    pov "Yes... yes, it's so damn good."
    mom "Then give it to me. Cum for me baby!"
    if inc == True:
        mom "Show your mommy how much you love her!"
    else:
        mom "Show me how much you love me!"
    pov "Oh my god!"
    scene weekend 8pm 055la
    pov "Aaaahhh...!"
    with vpunch
    mom "I can feel you pulsing in my hands, baby!"
    pov "Hnng..."
    scene weekend 8pm 056la
    mom "You gave me so much sweetie. I'm so glad I could please you like that."
    pov "Oh... it was so great..."
    mom "So, do you want to have more fun or is my baby boy done? <giggle>"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovebelly:
    pov "I'm going to kiss you whole body before we're done!"
    mom "Hm... Sounds like a great plan me!"
    "You work your way down her body, planting kisses along the way, stopping on her belly."
    scene weekend 8pm 027lb
    pov "Hm... <kiss>"
    mom "Hnng... it tickles."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    #----- end -----
    if inc == True:
        pov "I want to taste you forever, mom."
    else:
        pov "I want to taste you forever, [mother]."
    mom "Hmm... that's the spot. It feels so good."
    pov "I love to kiss your soft skin."
    mom "Hmm..."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovepussy:
    pov "Your lovely pussy needs my attention."
    mom "<giggle> It's waiting for you, my love."
    scene weekend 8pm 017lb
    if inc == True:
        pov "Your pussy is so beautiful, mom."
    else:
        pov "Your pussy is so beautiful, [mother]."
    mom "And all your sweet talk has made it so wet."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    #----- end -----
    pov "I'll take good care of it."
    call screen nicoleweekendlovepussychoose

screen nicoleweekendlovepussychoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('nicoleweekendlovepussychoose'), Jump('nicolelovelickpussy')) hovered tt.Action ("Lick her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('nicoleweekendlovepussychoose'), Jump('nicolelovefuckpussy')) hovered tt.Action ("Fuck her pussy") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicolelovelickpussy:
    pov "I'm going to please that pussy with my mouth until you scream my name!"
    mom "Oh, I'm very excited now."
    scene weekend 8pm 018lb
    pov "Hmm... <lick>"
    mom "Hmm... So good. I needed this so much!"
    scene weekend 8pm 019lb
    mom "Mmmh... Oh baby, keeping going..."
    pov "I'm glad you're enjoying it. All you need to do is ask and I'll come take care of your kitty everytime."
    mom "Hmm... that's a tempting offer."
    if inc == True:
        pov "You taste so good, mom."
    else:
        pov "You taste so good, [mother]."
    pov "And you're so wet."
    mom "Hmm..."
    "You bite her clit gently."
    scene weekend 8pm 020lb
    mom "Hah! God! That felt amazing!"
    pov "Looks like I found your weak spot?"
    mom "Yes, please do it more sweetie."
    pov "Your command in my pleasure, my queen."
    mom "<giggle> Hah... more... ahh... like my... ohh... pleasure..."
    scene weekend 8pm 021lb
    "She press your mouth harder onto her pussy, flicking your tongue inside, twisting it around as you play in her juicy wet pussy."
    mom "Ahhh! Oh yeah baby, just like that!"
    pov "Feels like you are getting close? <bite>"
    mom "Hah, yes... You're doing very good."
    pov "Don't forget to scream my name when you cum, haha."
    mom "I'll do anything you want me to do! Just keep going... I'm so close..."
    scene weekend 8pm 022lb
    mom "Oh... hah... hah..."
    mom "AAAAHHH... HAAAH..."
    with vpunch
    mom "<screaming> [pov]! YES! [pov]!"
    with vpunch
    mom "Hnnn... hnn..."
    with vpunch
    povi "Exactly what I wanted to hear."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovefuckpussy:
    pov "I need to be inside you so badly."
    mom "Then do it [pov]. I want to feel you inside me as well."
    povi "A dream come true."
    "You move to press the head of your penis against the dripping wet entrance of her vagina. You can feel the heat eminating from it."
    if inc == True:
        "You were planning on taking your time. Savoring the moment when you enter her, but you mother had some different in mind..."
    else:
        "You were planning on taking your time. Savoring the moment when you enter her, but [mother] had some different in mind..."
    scene weekend 8pm 040la
    "As your the head of your cock pressed into the folds of her vagina, [mother] shoved her hips forward, engulfing your entire shaft all in one go!"
    mom "YES! Hnng... all in. I can't wait any longer, baby! Fuck me, please!"
    pov "God, you were so wet I slide all the way in! I can feel you squeezing me inside there."
    mom "If feels like going to tear me apart. You're so big! It feels amazing!"
    if inc == True:
        pov "If I knew it felt this tight and warm inside you, I never would have left!"
    else:
        pov "If I knew it felt this tight and warm inside you, I would have tried harder to get here sooner!"
    scene weekend 8pm 041la
    "[mother] squeezed her legs around your body, enjoying the sensation of being joined with you at last."
    mom "You're such a naughty boy!"
    mom "I'm not going to lie, the fact it's taboo is making this even hotter!"
    pov "Then we need to do it more often!"
    if inc == True:
        mom "Please fuck me harder, son!"
    else:
        mom "Please fuck me harder, [pov]!"
    "You respond by trusting yourself down hard, pressing your pelvises together forcing your cock deeper inside her."
    "[mother] spreads her legs widly so her hips and wanton womanhood can better recieve your thrusts."
    scene weekend 8pm 042la
    mom "Hah... hah... I'm getting close..."
    mom "Oh shhhit! Fuck! This feels so damn good! You're going to make me cum baby!"
    mom "Haa... aah..."
    if inc == True:
        mom "I'm so close baby, you're gonna make mommy cum on your dick son!"
        mom "Do you want me to cum on that fat fucking dick baby?"
        mom "Hah... Right there baby! Aah! Haa... Don't stop!"
        pov "I'm close too. Let's cum together, mom."
    else:
        mom "I'm so close baby, you're gonna make mommy cum on your dick [pov]!"
        mom "Do you want me to cum on that fat fucking cock baby?"
        mom "Hah... Right there baby! Aah! Haa... Don't stop!"
        pov "I'm close too. Let's cum together, [mother]."
    povi "I can't believe how perfect this is. It's like we were specially built for each other!"
    mom "Hah... hah, oh [pov]!"
    call screen nicoleweekendlovemissionarycum

screen nicoleweekendlovemissionarycum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendlovemissionarycum'), Jump('nicolelovemissionaryinside')) hovered tt.Action ("Cum inside") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendlovemissionarycum'), Jump('nicolelovemissionaryoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicolelovemissionaryinside:
    scene weekend 8pm 043lai
    $ nicoleweekendinside = True
    mom "AAAHHH... I'm cumming... I'm cumming!"
    with vpunch
    if inc == True:
        mom "Cum inside me baby! Cum inside mommy!"
    else:
        mom "Cum inside me baby! Cum inside me!"
    pov "Oh fuck! Hnng... I'm cumming too!"
    with vpunch
    mom "I can feel it, baby! I feel you pusling inside me!. It's so hot."
    scene weekend 8pm 044lai
    mom "Hah... hah... there's... so much inside me..."
    pov "Hah... I've never came so hard before..."
    mom "You came so much... I thought it would never end..."
    mom "I hoped it would never end..."
    povi "I wonder if we went to far... It felt so incredidble."
    povi "But I don't want to worry her if she is concerned about me cumming inside her."
    "As if she was listening in on your thoughts, she wiggles her hips beneath you seductively."
    mom "Hah... ohh... do you want to stop or keep going sweetie?"
    povi "Well she doesn't seemed worried, that's good."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovemissionaryoutside:
    scene weekend 8pm 043lao
    mom "AAAHHH... I'm cumming... I'm cumming!"
    with vpunch
    pov "Oh fuck! Hnng... I'm cumming too!"
    with vpunch
    mom "I can feel it baby, I can feel it spraying me. It's so hot."
    scene weekend 8pm 044lao
    mom "Hah... hah... there's... so much cum on me..."
    pov "Hah... I've never came so hard before..."
    mom "You came so much... I thought it would never end..."
    mom "I hoped it would never end..."
    pov "I'm glad you liked it."
    mom "Hah... ohh... do you want to stop or keep going sweetie?"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovefeet:
    call screen nicoleweekendlovefeetchoose

screen nicoleweekendlovefeetchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('nicoleweekendlovefeetchoose'), Jump('nicolelovekissfeet')) hovered tt.Action ("Kiss her feet") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('nicoleweekendlovefeetchoose'), Jump('nicolelovefeetjob')) hovered tt.Action ("Ask for a footjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicolelovekissfeet:
    pov "I want to kiss your feet."
    mom "My feet?"
    pov "Yes they're so beautiful."
    scene weekend 8pm 030l
    "You suck on her big toe."
    pov "<suck>"
    mom "Oh... that feels nice."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    #----- end -----
    scene weekend 8pm 030la
    mom "Hmm... I thought it would tickle, but it's just wonderful."
    pov "<suck>"
    mom "You love sucking on me, don't you?"
    scene weekend 8pm 030lb
    pov "Yes, I love every part of your body."
    if inc == True:
        pov "And you're very lick and kiss-able, mom."
    else:
        pov "And you're very lick and kiss-able, [mother]."
    mom "Hmm... Then I'm glad I have you around to lick and kiss me."
    scene weekend 8pm 031l
    mom "Hnn... and it's even arousing."
    pov "Your feet are so beautiful, just like every other part of your body."
    pov "<lick> <kiss>"
    mom "Hmm..."
    scene weekend 8pm 031la
    pov "Am I the first one to play with your feet like this?"
    mom "Yes... hmm... and I love it."
    pov "Well there you have it, clear proof that I love you the most."
    mom "Yes baby, love my feet some more [pov]."
    scene weekend 8pm 031lb
    mom "This is so exciting. It's new and feels so good."
    pov "I'm glad you liked it. I did too."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovefeetjob:
    pov "I would love to feel your feet... on my..."
    mom "Oh, you want me to get you off with my feet?"
    pov "Y... yes. Could you do that?"
    mom "<giggle> Yeah, I'll try."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    #----- end -----
    scene weekend 8pm 032l
    mom "Oh, your penis is so hot."
    mom "It feels a little weird, but I kind of like doing it."
    scene weekend 8pm 032la
    pov "I love them like every other part of your body."
    pov "And they feel really good on my dick."
    scene weekend 8pm 032lb
    mom "Then I need to do a good job so I don't let you down. <giggle>"
    pov "You couldn't let me down. Because they're your feet, everything you do with your body is amazing."
    mom "Always the charmer. I bet you'll have a hard time with all that sweet talk when they make you cum! Haha..."
    scene weekend 8pm 033l
    pov "Yes, that feels good. Just like you would do it with your hands."
    mom "It's easier as I thought. And an exciting feeling, your pulsating shaft between my toes."
    pov "You're doing perfect."
    scene weekend 8pm 033la
    pov "And what a sexy view, seeing your beautiful feet working on my dick."
    mom "Then I'm happy that I can please you like this."
    scene weekend 8pm 033lb
    mom "Oh, your penis is shaking. Are you really about to cum from my feet?"
    if inc == True:
        pov "Yes, mom! I always wanted to play with your feet like this."
    else:
        pov "Yes, [mother]! I always wanted to play with your feet like this."
    mom "Then cum for me and my feet."
    scene weekend 8pm 034l
    pov "Yeah that's it, hold them like that. I want to cum all over them."
    mom "Then plaster my feet with your sperm, [pov]."
    pov "I'm so close..."
    scene weekend 8pm 035l
    pov "Hnng..."
    mom "Yes, cum for me..."
    scene weekend 8pm 036lb
    mom "So much came out and it's burning hot on my feet."
    pov "What a beautiful view. We need to do this much more often."
    scene weekend 8pm 034lb
    mom "When it pleases you this much, I'll train hard to give you even more pleasure."
    pov "I'd love that. I came so hard."
    mom "<giggle>"
    scene weekend 8pm 036la
    mom "So, do you want to have more fun or is my baby boy done? <giggle>"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovecow:
    if inc == True:
        pov "I want to have sex with you, mom."
    else:
        pov "I want to have sex with you, [mother]."
    mom "Well here I am. <giggle>"
    pov "Can you... ride me?"
    mom "Ride? Oh, you want me to drive for a while? I'd be happy to sweetie!"
    mom "Go ahead and lay down for me."
    scene weekend 8pm 060la
    pov "Ohh..."
    mom "Good, you're already hard."
    "She presses your cock against the wet lips of her vagina, rubbing herself with it for a while. Little moans and gasps escape her mouth."
    if inc == True:
        pov "I appreciate that you like my dick all stiff for you, mom."
    else:
        pov "I appreciate that you like my dick all stiff for you, [mother]."
    mom "Haha, it is flattering. And all the better for me to ride you."
    pov "I'm so excited. You can use me like that anytime you want."
    scene weekend 8pm 061la
    mom "I will have to take you up on that offer."
    "She grins wickedly at you as she positions the head of your penis below her entrance."
    mom "I'm sliding it inside me now. Slowly. Gently."
    "She let's her hips fall as she speaks, slowly engulfing your cock inside her."
    pov "Oh, I can feel your pussy, so warm and wet."
    mom "And you're burning inside me."
    scene weekend 8pm 061lb
    povi "This wonderful view. My dick deep inside her pussy. Where is belongs."
    mom "I'm going to take it deeper now."
    povi "I love how she's narrating this whole experience, it's like a documentary on fucking. God it turns me on!"
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19lovesex == True and alexisaway == False:
        jump proom19extlovealexis
    #----- end -----
    scene weekend 8pm 062la
    mom "Slowly."
    if inc == True:
        pov "Holy shit. I love that view mom!"
    else:
        pov "Holy shit. I love that view [mother]!"
    mom "I'm glad baby! There is so much of you! I'm still taking you in."
    pov "Your boobs are so big. I can barely see your face."
    mom "I'm going to take that as a compliment."
    pov "You should! That's how I meant it!"
    scene weekend 8pm 063la
    mom "You're almost completely inside me. You're so big and hot. I swear you'll reach my cervix at this point!"
    pov "And you're reaction is so damn sexy. I love watching you. You're so focused on how it feels to have me inside you."
    "She looks at you lustingly, as she pushes herself even lower on your cock."
    mom "Hah... Ahhh... it's all in!"
    scene weekend 8pm 063lb
    pov "I'm balls deep in your pussy. It feels so good."
    mom "Hah, you're so big and hard."
    pov "I can't wait any longer."
    if inc == True:
        pov "Please ride me good and hard, mom!"
    else:
        pov "Please ride me good and hard, [mother]!"
    "She didn't need any more prompting. Without futher ado she starts bouncing up and down on your hard dick."
    scene weekend 8pm 064lb
    mom "Oh, hah... hah..."
    with vpunch
    pov "Yes this is amazing!"
    with vpunch
    mom "You're too big! I won't last much longer. You're hitting all my best spots."
    with vpunch
    pov "Then enjoy yourself and cum when you need to. I'm close. I'm sure you cumming on my dick will drive me over the edge."
    scene weekend 8pm 064la
    mom "Hah... so you'll cum with me...?"
    with vpunch
    if inc == True:
        pov "Yes, mom. Let's cum together."
    else:
        pov "Yes, [mother]. Let's cum together."
    mom "I'm so close... hah... hah..."
    with vpunch
    pov "Then cum with me!"
    mom "HAAAHH... AAAAHHH...!"
    with vpunch
    "You're about to cum too."
    $ alexissuspicous += 1
    call screen nicoleweekendlovecowcum

screen nicoleweekendlovecowcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendlovecowcum'), Jump('nicolelovecowinside')) hovered tt.Action ("Cum inside") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendlovecowcum'), Jump('nicolelovecowoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicolelovecowinside:
    scene weekend 8pm 065lbi
    $ nicoleweekendinside = True
    mom "AAAHHH... I'm cumming... I'm cumming!"
    with vpunch
    if inc == True:
        mom "Cum inside me baby! Cum inside mommy!"
    else:
        mom "Cum inside me baby! Cum inside me!"
    pov "Oh fuck! Hnng... I'm cumming too!"
    with vpunch
    mom "I can feel it, baby! I feel you pusling inside me!. It's so hot."
    scene weekend 8pm 065lai
    mom "Hah... hah... there's... so much inside me..."
    pov "Hah... I've never came so hard before..."
    mom "You came so much... I thought it would never end..."
    mom "I hoped it would never end..."
    povi "I wonder if we went to far... It felt so incredidble."
    povi "But I don't want to worry her if she is concerned about me cumming inside her."
    "As if she was listening in on your thoughts, she wiggles her hips while still impaled by your cock."
    mom "Hah... ohh... do you want to stop or keep going sweetie?"
    povi "Well she doesn't seemed worried, that's good."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovecowoutside:
    scene weekend 8pm 065lbo
    mom "AAAHHH... I'm cumming... I'm cumming!"
    with vpunch
    pov "Oh fuck! Hnng... I'm cumming too!"
    with vpunch
    mom "I can feel it baby, I can feel it spraying me. It's so hot."
    scene weekend 8pm 065lao
    mom "Hah... hah... there's... so much cum on me..."
    pov "Hah... I've never came so hard before..."
    mom "You came so much... I thought it would never end..."
    mom "I hoped it would never end..."
    pov "I'm glad you liked it."
    mom "Hah... ohh... do you want to stop or keep going sweetie?"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump nicoleweekendloveroot

label nicolelovestop:
    pov "I'm spent. I don't think I have another drop of cum inside me. We should take a break."
    mom "Ok, if you're sure there is nothing else left... Then as you wish. <giggle>"
    mom "Come cuddle with me baby."
    if nicoleweekendinside == True:
        scene weekend 8pm 045lao
        if inc == True:
            "You look down at your mother, she's seems exhausted like you, but also very satisfied."
            pov "I love you mother."
        else:
            "You look down at [mother], she's seems exhausted like you, but also very satisfied."
            pov "I love you [mother]."
        "When your declaration isn't echoed back to you, you're not worried. She was probably just enjoying that just fucked for hours feel you were also enjoying."
        "But then her expression changed. A look of concern that worried you."
        scene weekend 8pm 045lai
        pov "Is something wrong?"
        mom "When you came inside me, I felt something change."
        pov "Change? What do you mean?"
        mom "I couldn't help but want it. No, not want. Crave it. I needed you to cum inside me."
        mom "And judging from how powerful it felt when you sprayed your sperm inside me, I think maybe you felt the same way too."
        mom "Like you want to make sure that you impregnated me... That you wanted not only to have sex with me, but to breed with me too."
        mom "Am I going crazy?"
        call screen nicoleweekendlovepreg
    else:
        scene weekend 8pm 045lao
        mom "That was so much fun!"
        pov "I'm glad you liked it too. I can't wait for our next time."
        mom "Yes, we need to do this again."
        mom "I love you so much my sweet boy!"
        pov "I love you too."
        jump nicoleweekendloveend

screen nicoleweekendlovepreg():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('nicoleweekendlovepreg'), Jump('nicolelovepregyes')) hovered tt.Action ("I want to impregnate her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('nicoleweekendlovepreg'), Jump('nicolelovepregno')) hovered tt.Action ("I don't want to impregnate her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value


label nicolelovepregyes:
    pov "You're not crazy..."
    if inc == True:
        pov "I felt it too. I didn't just want to be with you, I wanted to have you for my own, completely, mom!"
        pov "I wanted to fill your womb with my seed and create something beautiful and primal. Together."
        mom "But... you're my son..."
        pov "I know, but that doesn't matter. I want us to be a family. In every sense of the word. I want you to be the mother of my children."
    else:
        pov "I felt it too. I didn't just want to be with you, I wanted to have you for my own, completely, [mother]!"
        pov "I wanted to fill your womb with my seed and create something beautiful and primal. Together."
        mom "But..."
        pov "I want us to be a family. In every sense of the word. I want you to be the mother of my children."
    "She seems to fall deep in thought for a moment, then squeezes you tighter."
    mom "Hmm..."
    povi "Does \"Hmm\" mean she wants that too? Or not? She didn't say no, but maybe she needs some time to think about it."
    "She rests her head on your chest."
    $ nicolebabywant = True
    jump nicoleweekendloveend

label nicolelovepregno:
    pov "I don't think you're crazy, but maybe just caught up in the moment a bit. I just want to give you all I had."
    mom "Oh... ok."
    povi "Is she disappointed?"
    "She rests her head on your chest."
    jump nicoleweekendloveend

label nicoleweekendloveend:
    #----- Added 0.75 Part 1 -----
    if proom19lovesex == True:
        jump proom19extloveend
    #----- End -----
    scene weekend 8pm 046l
    mom "Let's go to sleep, sweetie. I'm so tired."
    if nicolebabywant == True:
        "Her voice is kind and content. You don't think you need to be worried about you talk earlier."
        povi "Maybe was can talk about it later, after we've had some rest."
    if inc == True:
        pov "Sweet dreams, mom."
    else:
        pov "Sweet dreams, [mother]."
    mom "You too my love."
    scene black
    "You spend the night together in each other's arms."
    $ nicoleweekendinside = False
    $ mombasementlovesecond = True
    $ weekendactivities += 1
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

#----- Nicole Second Date (Love) Corruption Version ----- Done
label cornicoleweekendlove:
    $ momlove += 1
    hide screen locations
    scene black
    if inc == True:
        "You and your mother decide to have dinner at home together, just the two of you."
        "You cook dinner for you and your mom and wait for her to come back from her extra shifts."
    else:
        "You and [mother] decide to have dinner at home together, just the two of you."
        "You cook dinner for you and [mother] and wait for her to come back from her extra shifts."
    "You hear the front door open."
    scene weekend 8pm 001
    if inc == True:
        mom "Hey son, I'm back."
    else:
        mom "Hey [pov], I'm back."
    mom "Do you need help with dinner?"
    scene weekend 8pm 002
    mom "Oh? What a nice surprise, it's all done!"
    if inc == True:
        pov "Welcome back, mom."
    else:
        pov "Welcome back, [mother]."
    mom "Oh, the candle is a nice touch as well."
    scene weekend 8pm 003
    mom "I'm so happy you did this for me, sweetie. It's nice to have a man make an effort like this for me. It's been a long time."
    pov "It was my pleasure. Let's eat. We're going to need plenty of energy for tonight."
    mom "So you have something planned for us this evening, besides dinner?"
    if inc == True:
        pov "I do actual. Tonight you're going to be my slutty wife who will stop at nothing to please me. So not too far off from reality, right mom?"
    else:
        pov "I do actual. Tonight you're going to be my slutty wife who will stop at nothing to please me. So not too far off from reality, right [mother]?"
    scene weekend 8pm 004c
    mom "You think I'm a... slutty wife?"
    povi "Wait is she really upset right now? I would have thought that was obvious judging from how much she's played with my cock since I got back!"
    if inc == True:
        povi "Her own son's cock no less."
    scene weekend 8pm 004l
    mom "Well if you're my husband now, then you're absolutely correct! I'm a slutty wife, who'll do \"anything\" to please her man!"
    if gangmember == True:
        mom "My big dangerous gangster. So strong and commanding. I quiver with fear and excitement when you're near me."
    pov "Yes..."
    mom "Come here husband. I wouldn't want you to have to punish me for being a naughty wife."
    scene weekend 8pm 005l
    "She presses her body tightly against you. You can feel her large, supple breasts cramed between you two. She leans her head in and whispers into your ear."
    mom "<whisper> God I love how I feel in your arms. It's like the room is getting warm, my knees getting weak... and my panties getting wet."
    if inc == True:
        pov "<whisper> God damn woman... You're pratically a mewling whore tonight, mom. I love it!"
        mom "I'm not your mother tonight, son. Tonight, I'm your wife... But I'm also hungry, haha."
    else:
        pov "<whisper> God damn woman... You're pratically a mewling whore tonight, [mother]. I love it!"
        mom "Yes husband, I am. But I'm also hungry, haha."
    scene weekend 8pm 004l
    mom "So let's eat."
    pov "Sounds great!"
    mom "I want to taste this delicous looking meat now."
    povi "She was looking right at me when she said that..."
    mom "Oh... I nearly forgot!"
    mom "Close your eyes dear. I have something for you..."
    povi "Damn, she's really getting into this. Might as well play along."
    "You close your eyes."
    scene black
    "You here some rustling and then something hit the floor."
    mom "Ok dear, open your eyes."
    scene weekend 8pm 006c
    pov "Wow! I have to say, I really like this wardrobe change. It's suits you!"
    mom "Anything for my husband. I'm my duty to please him every way that I can."
    pov "Well you are off to a great start! Your tits are just fucking perfect. And will be great to stare at while we eat!"
    "You two move to your seats to enjoy the meal."
    scene edited weekend 8pm 007c #----- Nicole breasts smile only meat -----
    mom "I have to say, you surprised me with this meal. It's fantastic so far!"
    mom "I can't wait to put this savory looking meat in my mouth."
    pov "It'd pretty good, but I bet we can find an even better use for that mouth of yours tonight."
    mom "Oh! I like the sound of that! But what if I want both. I can be insatiable... in so many ways. "
    pov "Sounds great to me. I'm sure you're going to the get all the meat you want tonight."
    scene weekend 8pm 008c #----- Nicole breasts close up -----
    povi "Seriously, that cleavage just sucks me in."
    povi "God I just want to bend her over that table and grip those giant tits while I fuck her silly."
    mom "Some one has something else on their minds I see..."
    povi "I could fuck her tits for hours!"
    mom "[pov]!"
    scene edited weekend 8pm 009c #----- Nicole breasts smile closed hands empty plate -----
    pov "Huh?"
    mom "I see you're a bit distracted, haha. Is it something your voracious wife can help you with?"
    pov "Oh? I... Well... Yeah, I'm sure there are more than a few things you can do for me..."
    mom "Hnng... Well I finished my plate already. Are you planning on finishing your meal, or just stare at my tits all night? <giggle>"
    pov "Don't threaten me with a good time!"
    mom "Well, you'll never finish eating at this rate, maybe we should retire to our bedroom..."
    scene weekend 8pm 010c #----- Nicole breasts looking down biting lip -----
    mom "I am very much looking forward to pleasing my man in every way possible. It's my duty as his wanton wife, right?"
    povi "Seriously, she is such a tease tonight! I could definitely get behind weekly fuck sessions when everyone is gone."
    "You literally wolf down your meal."
    "You mother gets up, leaving the plates and unfinished wine behind."
    scene weekend 8pm 011c #----- Nicole breasts standing looking down -----
    mom "I'm going to go change in something more comfortable... Will you be joining me love?"
    pov "Of course. Be there in just a minute."
    scene weekend 8pm 011 #----- Empty Space -----
    povi "Anticipation and all that. I am excited to see what she's going to wear. Something sexy I'm sure."
    povi "I want to be with her now. Naked. In bed. Sweating and writhing together."
    "You wait a few moments thinking about you two fucking on the her bed..."
    if inc == True:
        povi "Screw it! I'm going up there now! Anticipation can eat a big fucking dick... after my mom eats mine."
    else:
        povi "Screw it! I'm going up there now! Anticipation can eat a big fucking dick... after [mother] eats mine."
    "You head upstairs to \"your\" bedroom and step inside."
    scene weekend 8pm 012lb
    mom "There you are [pov]."
    mom "I knew you wouldn't wait..."
    pov "Well, yeah. I haven't had a great track record for waiting thus far, have I?"
    mom "Haha, no you haven't. Always stopping by to say hello as just the right time to watch me get dressed."
    pov "I didn't want you to get lonely without me around. I know you get... desperate with a big strong man around to \"take care\" of you."
    mom "True... How does it feel to be invited this time?"
    scene weekend 8pm 013la
    mom "You couldn't get enough of these at dinner. I wonder if there is anything else I have to offer that would get so much attention?"
    povi "She's teasing me on purpose. She knows exactly how to press my buttons."
    mom "I had a feeling you might be up to something, when you put such an effort in preparing a fine meal like that."
    mom "A woman konws her man, and I know you..."
    mom "It's not healthy for a strong, handsome young man like you to go without that which you desire for too long."
    if inc == True:
        mom "And I think you desire to see your mother naked. Or possibly... even more."
        mom "Something forbidden perhaps?"
    else:
        mom "And I think you desire to see me naked. Or possibly... even more."
    "She turns back around slightly and slowly peels her pants off in front of you, revealing her nakedness underneath."
    scene weekend 8pm 013lb
    pov "<gulp> I thought you said you were my wife tonight... sorry, I mispoke. My slutty wife."
    mom "Oh I am my love... You could have chosen any other woman to pursue if you wanted, but you chose me..."
    scene weekend 8pm 014lb
    pov "There isn't anyone else I wanted, more that I want you."
    mom "You're so honest with me, and I want to be honest with you too."
    mom "You changed so much in just one year. And when you came home you were greeted with this... fucking mess!"
    mom "And you walk right in and started taking charge. You manuevered you way up the ranks and the others are getting scared... of you."
    if inc == True:
        mom "I'm so very proud of the man you've become. I'm more than proud..."
        mom "I'm intenstly interested \"new\" man in my life."
        mom "Even if a mother and son shouldn't share these desires, we do. We've already sampled what is forbidden."
    else:
        mom "I'm so very proud of the man you've become. I'm more than proud..."
        mom "I'm intenstly in that man. In you."
        mom "Even if I shouldn't share your desires, I do.  We've already sampled what is forbidden."
    scene weekend 8pm 015lb
    mom "But now I think we should feast on it!"
    pov "Wow..."
    mom "I want you to make me yours! I want you to own every inch of me."
    mom "I want you to fuck me until I beg for you stop and then to just keep fucking because you want to."
    "She lays down on her bed, looking up to you."
    scene weekend 8pm 016lb
    mom "Well, what are you waiting for?"
    pov "Is this really happening?"
    mom "You fucking bet it is! I want you to make me forget all about Bruce and his incompetence, his cowardance."
    mom "So show me that my fantasies are just a pale imitation of the real thing. Conquer me completely!"
    "You undress in a hurried frenzy."
    mom "<giggle>"
    jump cornicoleweekendloveroot

label cornicoleweekendloveroot:
    scene weekend 8pm 016lb
    call screen cornicoleweekendlovechoose

screen cornicoleweekendlovechoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('cornicoleweekendlovechoose'), Jump('cornicolelovehead')) hovered tt.Action ("Kiss her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" action (Hide('cornicoleweekendlovechoose'), Jump('cornicoleloveboobs')) hovered tt.Action ("Choose her boobs") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('cornicoleweekendlovechoose'), Jump('cornicolelovehands')) hovered tt.Action ("Ask for a handjob") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('cornicoleweekendlovechoose'), Jump('cornicolelovebelly')) hovered tt.Action ("Kiss her belly") focus_mask True
        imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('cornicoleweekendlovechoose'), Jump('cornicolelovepussy')) hovered tt.Action ("Choose her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('cornicoleweekendlovechoose'), Jump('cornicolelovefeet')) hovered tt.Action ("Choose her feet") focus_mask True
        imagebutton auto "gui/icons/icon_cowgirl_%s.png" action (Hide('cornicoleweekendlovechoose'), Jump('cornicolelovecow')) hovered tt.Action ("Let her go on top") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('cornicoleweekendlovechoose'), Jump('cornicolelovestop')) hovered tt.Action ("Finish") focus_mask True
        if proom19corsex == True:
            imagebutton auto "gui/icons/icon_skip1_%s.png" action (Hide('cornicoleweekendlovechoose'), Jump('proom19extcorlanding')) hovered tt.Action ("Return to previous menu") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cornicolelovehead:
    mom "Kiss me baby! I need to taste you on lips."
    scene weekend 8pm 024lb
    pov "Hmm..."
    "You hold her closely to you as you thrust your tongue into her mouth."
    "Her open mouth greedily accepts the intrusion as her tongue plays with yours."
    mom "Hnng..."
    "You move your kisses to her neck, nibbling and licking your way down it."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    "Your hips grinds against hers. You can feel the heat and wet eminating from her cunt."
    scene weekend 8pm 025lb
    pov "<kiss> <lick>"
    mom "Hmm... that's the spot baby. It feels so damn good."
    if inc == True:
        pov "You're mine forever now, mom. I own you. I own your body. I need you to say it."
    else:
        pov "You're mine forever now, [mother]. I own you. I own your body. I need you to say it."
    mom "Oh god yes! I'm your darling. My body is yours to with what you please!"
    pov "That's a good girl."
    mom "Hmm..."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicoleloveboobs:
    call screen cornicoleweekendloveboobschoose

screen cornicoleweekendloveboobschoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('cornicoleweekendloveboobschoose'), Jump('cornicolelovekissboobs')) hovered tt.Action ("Kiss her boobs") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" action (Hide('cornicoleweekendloveboobschoose'), Jump('cornicoleloveboobjob')) hovered tt.Action ("Ask for a boobjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cornicolelovekissboobs:
    pov "Finally, I get to have my main course!"
    mom "<giggle> I knew you love my tits more than me!"
    scene weekend 8pm 026lb
    pov "<kiss> <suck>"
    mom "Are they as good as you hoped? <giggle>."
    pov "I love sucking on them so much."
    "You flick her nipple with your tongue roughly. A little squeal of excitement escapes her."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    if inc == True:
        mom "You suck them so greedly. Like you did as a baby."
        pov "I was a damn luck baby then!"
    else:
        mom "You suck them so greedy. Like you're a hungry baby."
        pov "Of course I'm a hungry man too!"
    "You bite down on her nipple so she knows you mean it."
    mom "Oh god! Hmm... you can keep doing that lover."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicoleloveboobjob:
    pov "Ok, I know what I want now slut. I want my \"wife\" to jack my fat cock off with her enormous tits!"
    mom "Oh, you want to fuck my tits do you?"
    pov "Not want to... I'm going to fuck your tits, well actually you are going to do the work."
    mom "<giggle> But you're the one that's so attracted to them. Well, I guess it can't be helped. Lay down."
    scene weekend 8pm 050la
    mom "I love the way you stare at me. Devouring me with your eyes."
    mom "<giggle> And you're always \"excited\" to see me!"
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    pov "That's an understatement! It's all I can do to not just rip off your clothes and fuck you while you scream and beg for more when I'm around you."
    mom "Haha. Well what kind of wife would I be if I didn't let my husband fuck me silly at the slightest whim?"
    pov "Not the slutty wanton whore I've grown to love, that's for sure! Now get those tits around this dick!"
    scene weekend 8pm 051lb
    pov "Ohh... fuck yeah. I love 'em. I really do. They are fucking perfect!"
    mom "And your shaft is burning hot! I could definitely get used to this. Maybe we could do this around town, at the gym, the movie theaters, a confessional! <wink>"
    pov "Damn woman! You really are a slut. Do you even go to church?"
    mom "Oh not for a long time, but it would be worth it for a bit of naughty fun. Maybe I could borrow an nun's habit..."
    pov "Oh I'd fuck a nun at church, believe me! Especially if she was stacked like you!"
    "She grins wickedly at you as she lets some spit drip down on your cock, getting you ready."
    scene weekend 8pm 052lb
    mom "Then I'll put even more effort into this then. <giggle>"
    mom "I want to spoil my hubby so he doesn't go around fucking all the big breasted nuns!"
    "She dribbles some more spit between her breasts as she fucks it up and down with her hands pressing her tits tightly together."
    pov "Oh yes! Haha. I don't know though, this is pretty much my idea of heaven right here."
    mom "There you go again, being all charming when I least expect it."
    pov "Well I do have my moments... ahh... god you're amazing. It's so tight and wet between those mounds!"
    scene weekend 8pm 053lb
    mom "I'm so glad you like it baby."
    pov "Ohh... Hmm... hah..."
    mom "You're shaking! Are you going to cum for me? I want you to cum for me!"
    pov "Yes... yes, it's so damn good."
    mom "Then give it to me. Cum all over my tits for me."
    if inc == True:
        mom "Show your slutty mommy how much you love her!"
    else:
        mom "Show me how much you love your slut of a wife!"
    pov "Oh my god!"
    scene weekend 8pm 054lb
    pov "Aaaahhh...!"
    with vpunch
    mom "You've covering me baby, it's so hot."
    scene weekend 8pm 055lb
    pov "Hnng..."
    with vpunch
    mom "You covered me! I'm so glad I could help you out like that."
    pov "Oh... it was so great..."
    mom "So, do you want to have more fun or is my hubby done? <giggle>"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovehands:
    mom "So what do you say about letting get my hands on that monster of cock now?"
    pov "I thought you would never ask!"
    mom "<giggle> Fantastic! Lay your ass down then."
    scene weekend 8pm 050la
    mom "I love the way you stare at me. Devouring me with your eyes."
    mom "<giggle> And you're always \"excited\" to see me!"
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    pov "That's an understatement! It's all I can do to not just rip off your clothes and fuck you while you scream and beg for more when I'm around you."
    mom "Haha. Well what kind of wife would I be if I didn't let my husband fuck me silly at the slightest whim?"
    pov "Not the slutty wanton whore I've grown to love, that's for sure! Now get those hands around this dick!"
    scene weekend 8pm 051la
    pov "I love the feel of your hands on my cock like that! Like they were molded just this."
    mom "And your shaft is burning hot! I could definitely get used to this. Maybe we could do this around town, at the gym, the movie theaters, a confessional! <wink>"
    pov "Damn woman! You really are a slut. Do you even go to church?"
    mom "Oh not for a long time, but it would be worth it for a bit of naughty fun. Maybe I could borrow an nun's habit..."
    pov "Oh I'd fuck a nun at church, believe me! Especially if she was stacked like you!"
    "She grins wickedly at you as she lets some spit drip down on your cock, getting you ready."
    scene weekend 8pm 052la
    mom "Then I'll put even more effort into this then. <giggle>"
    mom "I want to spoil my hubby so he doesn't go around fucking all the big breasted nuns!"
    "She dribbles some more spit between her fingers as she pumps her fist up and down your shaft with increasing speed."
    pov "Oh yes! Haha. I don't know though, this is pretty much my idea of heaven right here."
    mom "There you go again, being all charming when I least expect it."
    pov "Well I do have my moments... ahh... god you're amazing!"
    scene weekend 8pm 053la
    mom "I'm so glad you like it baby."
    pov "Ohh... Hmm... hah..."
    mom "You're shaking! Are you going to cum for me? I want you to cum for me!"
    pov "Yes... yes, it's so damn good."
    mom "Then give it to me. Cum for me baby!"
    if inc == True:
        mom "Show your slutty mommy how much you love her!"
    else:
        mom "Show me how much you love your slut of a wife!"
    pov "Oh my god!"
    scene weekend 8pm 055la
    pov "Aaaahhh...!"
    with vpunch
    mom "I can feel you pulsing in my hands, baby!"
    pov "Hnng..."
    scene weekend 8pm 056la
    mom "You covered me! I'm so glad I could help you out like that."
    pov "Oh... it was so great..."
    mom "So, do you want to have more fun or is my hubby done? <giggle>"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovebelly:
    pov "I'm going to cover your body with love bites and hickies!"
    pov "Then we'll see what Bruce says the next time you guys start up another afternoon delight session..."
    mom "Hm... How positively devious of you! The man won't even get up the courage to ask abou them I bet."
    "You work your way down her body, nipping and sucking along the way, stopping on her belly."
    scene weekend 8pm 027lb
    pov "Hm... <suck>"
    mom "Hnng... it tickles."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    pov "We'll see what we can do about that!"
    "You bite her belly, not enough to break skin, but enough to make her really feel it."
    mom "<Gasps> Hey! You cheeky bastard..."
    "You lick the bite, soothing the skin."
    mom "Hmm... that's the spot. It feels so good."
    pov "A little pain can help accentuate the pleasures in life."
    mom "Hmm... I couldn't agree more!"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovepussy:
    pov "The wet hot pussy of yours needs attention."
    mom "<giggle> It's waiting for you, my love."
    scene weekend 8pm 017lb
    if inc == True:
        pov "Your pussy is glistening, mom. You're so wet."
    else:
        pov "Your pussy is glistening, [mother]. You're so wet."
    mom "And all your naughty talk has made it so wet."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    pov "That's my slutty girl."
    call screen cornicoleweekendlovepussychoose

screen cornicoleweekendlovepussychoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('cornicoleweekendlovepussychoose'), Jump('cornicolelovelickpussy')) hovered tt.Action ("Lick her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('cornicoleweekendlovepussychoose'), Jump('cornicolelovefuckpussy')) hovered tt.Action ("Fuck her pussy") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cornicolelovelickpussy:
    pov "I'm going to eat that pussy out until you scream my name!"
    mom "Oh, I'll scream for you baby."
    scene weekend 8pm 018lb
    pov "Hmm... <lick>"
    mom "Hmm... So good. I needed this so badly!"
    scene weekend 8pm 019lb
    mom "Mmmh... Oh baby, keeping going... that feels go damn good!"
    pov "Does my horny wife not get eaten out enough? All you need to do is ask and I'll come take care of your slutty pussy everytime."
    mom "Hmm... that's a promise I hope you keep!"
    if inc == True:
        pov "You taste so good, mom."
    else:
        pov "You taste so good, [mother]."
    pov "And you're so fucking wet."
    mom "Hmm..."
    "You bite her clit and flick it your tongue."
    scene weekend 8pm 020lb
    mom "Hah! God! That felt amazing!"
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    pov "Looks like I found your weak spot?"
    mom "Oh gawd yes! Keep going!."
    pov "It would be my pleasure. I want to keep my sluts happy."
    mom "<giggle> Hah... more... ahh... like my... ohh... pleasure..."
    scene weekend 8pm 021lb
    "She press your mouth harder onto her pussy, flicking your tongue inside, twisting it around as you play in her juicy wet pussy."
    mom "Ahhh! Oh yeah baby, just like that!"
    pov "Feels like you are getting close? <bite>"
    mom "Hah, yes... yesss... fuck!"
    pov "Don't forget to scream my name when you cum slut, haha."
    mom "I'll do anything you want me to do! Just keep going... I'm so close..."
    scene weekend 8pm 022lb
    mom "Oh... hah... hah..."
    mom "AAAAHHH... HAAAH..."
    with vpunch
    mom "<screaming> [pov]! YES! [pov]!"
    with vpunch
    mom "Hnnn... hnn..."
    with vpunch
    povi "Exactly what I wanted to hear."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovefuckpussy:
    pov "I'm not waiting any longer. It's about time I fuck your dripping wet cunt!"
    mom "Then do it [pov]! I need it baby! I need to be fucked!"
    povi "A dream come true."
    "You move to press the head of your penis against the dripping wet entrance of her vagina. You can feel the heat eminating from it."
    if inc == True:
        "You were planning on taking your time. Savoring the moment when you enter her, but you mother had some different in mind..."
    else:
        "You were planning on taking your time. Savoring the moment when you enter her, but [mother] had some different in mind..."
    scene weekend 8pm 040la
    "As your the head of your cock pressed into the folds of her vagina, [mother] shoved her hips forward, engulfing your entire shaft all in one go!"
    mom "YES! Hnng... all in. I can't wait any longer, baby! Fuck me, please!"
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    pov "God, you were so wet I slide all the way in! I can feel your cunt squeezing me inside there."
    mom "If feels like going to tear me apart. You're so big! It feels so amazing!"
    if inc == True:
        pov "If I knew it felt this tight and warm inside you, I never would have left!"
    else:
        pov "If I knew it felt this tight and warm inside you, I would have tried harder to get here sooner!"
    scene weekend 8pm 041la
    "[mother] squeezed her legs around your body, enjoying the sensation of being joined with you at last."
    mom "You're such a naughty husband!"
    mom "I'm not going to lie, the fact it's taboo is making this even hotter!"
    pov "Then I need to fuck you so much more!"
    if inc == True:
        mom "Harder! Fuck me harder, son!"
    else:
        mom "Harder! fuck me harder, [pov]!"
    "You respond by trusting yourself down hard, pressing your pelvises together forcing your cock deeper inside her."
    "[mother] spreads her legs widly so her hips and wanton womanhood can better recieve your thrusts."
    scene weekend 8pm 042la
    mom "Hah... hah... I'm getting close..."
    mom "Oh shhhit! Fuck! This feels so damn good! You're going to make me cum baby!"
    mom "Haa... aah..."
    if inc == True:
        mom "I'm so close baby, you're gonna make mommy cum on your dick son!"
        mom "Do you want me to cum on that fat fucking dick baby?"
        mom "Hah... Right there baby! Aah! Haa... Don't stop!"
        pov "I'm close too. Let's cum together, mom."
    else:
        mom "I'm so close baby, you're gonna make mommy cum on your dick [pov]!"
        mom "Do you want me to cum on that fat fucking cock baby?"
        mom "Hah... Right there baby! Aah! Haa... Don't stop!"
        pov "I'm close too. Let's cum together, [mother]."
    povi "God damn she get dirty when she's getting pounded! I fucking love it!"
    mom "Hah... hah, oh [pov]!"
    call screen cornicoleweekendlovemissionarycum

screen cornicoleweekendlovemissionarycum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('cornicoleweekendlovemissionarycum'), Jump('cornicolelovemissionaryinside')) hovered tt.Action ("Cum inside") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('cornicoleweekendlovemissionarycum'), Jump('cornicolelovemissionaryoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cornicolelovemissionaryinside:
    scene weekend 8pm 043lai
    $ nicoleweekendinside = True
    mom "AAAHHH... I'm cumming... I'm cumming!"
    with vpunch
    if inc == True:
        mom "Cum inside me baby! Cum inside mommy!"
    else:
        mom "Cum inside me baby! Cum inside me!"
    pov "Oh fuck! Hnng... I'm cumming too!"
    with vpunch
    mom "I can feel it, hubby! I feel you pusling inside me!. It's so fucking hot."
    scene weekend 8pm 044lai
    mom "Hah... hah... there's... so much inside me..."
    pov "Hah... I've never came so hard before..."
    mom "You came so much... I hoped it would never end..."
    povi "I wonder if we went to far... Nah! It felt so incredidble."
    povi "She's like a bitch in heat, begging for me to cum inside her. I want to do that again!"
    "As if she was listening in on your thoughts, she wiggles her hips beneath you seductively."
    mom "Hah... ohh... do you want to stop or keep going?"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovemissionaryoutside:
    scene weekend 8pm 043lao
    mom "AAAHHH... I'm cumming... I'm cumming!"
    with vpunch
    pov "Oh fuck! Hnng... I'm cumming too!"
    with vpunch
    mom "I can feel it baby, I can feel it spraying me. It's so hot."
    scene weekend 8pm 044lao
    mom "Hah... hah... there's... so much cum on me..."
    pov "Hah... I've never came so hard before..."
    mom "You came so much... I hoped it would never end..."
    pov "You're like a bitch in heat! You just can't get enough."
    mom "Hah... ohh... do you want to stop or keep going?"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovefeet:
    call screen cornicoleweekendlovefeetchoose

screen cornicoleweekendlovefeetchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('cornicoleweekendlovefeetchoose'), Jump('cornicolelovekissfeet')) hovered tt.Action ("Kiss her feet") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('cornicoleweekendlovefeetchoose'), Jump('cornicolelovefeetjob')) hovered tt.Action ("Ask for a footjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cornicolelovekissfeet:
    pov "I'm going to kiss your feet now."
    mom "My feet?"
    pov "Well you did say I owned all of your body, right?"
    scene weekend 8pm 030l
    "You suck on her big toe."
    pov "<suck>"
    mom "Oh... that feels nice."
    scene weekend 8pm 030la
    mom "Hmm... I thought it would tickle, but it's actually feels good."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    pov "<suck>"
    mom "You love sucking on me, don't you?"
    scene weekend 8pm 030lb
    pov "Yes, everywhere I possibly can."
    if inc == True:
        pov "And you're very suck-able, mom."
    else:
        pov "And you're very suck-able, [mother]."
    mom "Hmm... Then I'm glad I have you around to do it."
    scene weekend 8pm 031l
    mom "Hnn... and it's even getting me hot and bothered."
    pov "That doesn't surprise me, it's just like every other part of your body. A craven whore through and through."
    pov "<lick> <kiss>"
    mom "Hmm..."
    scene weekend 8pm 031la
    pov "Am I the first one to play with your feet like this?"
    mom "Yes... hmm... and I love it hubby."
    pov "Well there you have it, I get to take your virginity after all."
    mom "Yes baby, love my feet some more [pov]."
    scene weekend 8pm 031lb
    mom "This is so exciting. It's new and feels so good."
    pov "I'm glad you liked it."
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovefeetjob:
    pov "Now you're going to take care me... with your feet."
    mom "Oh, you want me to jack you off with my feet?"
    pov "Not want, command!"
    mom "<giggle> Of course hubby. It's my duty as your wife to please you, right?"
    pov "You're god damn right it is! You're such a well trained slut."
    scene weekend 8pm 032l
    mom "Oh god, your penis is so hot."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    mom "It feels a little weird, but I kind of like it!"
    scene weekend 8pm 032la
    pov "I'm sure we'll find all sorts of new ways to get me off together."
    pov "And they feel great on my dick."
    scene weekend 8pm 032lb
    mom "Then I need to do a good job so I don't let you down. <giggle>"
    pov "Yes, we wouldn't want to do that. I need my bitches doing their best to please me at all times."
    mom "So now I'm just one of your bitches? I bet you'll have a hard time with all that shit talk when I'm making you cum! Haha..."
    scene weekend 8pm 033l
    pov "Yes, that feels good. Just like you would do it with your hands."
    mom "It's easier as I thought. And an exciting feeling, your pulsating shaft between my toes."
    pov "You're doing great."
    scene weekend 8pm 033la
    pov "And what a great view! I can watch your gapping pussy drip while your feet work my dick."
    mom "Then I'm happy we provided you a room with a view."
    scene weekend 8pm 033lb
    mom "Oh, your penis is shaking. Are you really about to cum already?"
    pov "What can I say, you give great foot!"
    mom "Then cum for me and my feet."
    scene weekend 8pm 034l
    pov "Yeah that's it, hold them like that. I'm going to cum all over them."
    mom "Then plaster my feet with your sperm, [pov]."
    pov "I'm so close..."
    scene weekend 8pm 035l
    pov "Hnng..."
    mom "Yes, cum for me..."
    scene weekend 8pm 036lb
    mom "So much came out and it's burning hot on my feet."
    pov "We need to do this much more often."
    scene weekend 8pm 034lb
    mom "When it pleases you this much, I'll neet to train even more to please with my feet."
    pov "Now that is what I like to hear. I came so hard."
    mom "<giggle>"
    scene weekend 8pm 036la
    mom "So, do you want to have more fun or is my hubby done? <giggle>"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovecow:
    if inc == True:
        pov "Time for you to ride your horse, mom."
        mom "Well then, yippee ki-yay motherfucker!"
        pov "Did you seriously just quote die-hard?"
    else:
        pov "Time for you to ride your horse, cowgirl."
        mom "Well then, giddy-up! I'm going to ride you for hours!"
        pov "I'm ready for ya!"
    mom "I'm just glad you're giving me a chance to drive for awhile. It's my turn to fuck you silly!"
    mom "Go ahead and lay down baby."
    scene weekend 8pm 060la
    pov "Ohh..."
    mom "God your cock is a monster. I fucking love how it feels against my lips."
    "She presses your cock against the wet lips of her vagina, rubbing herself with it for a while. Little moans and gasps escape her mouth."
    if inc == True:
        pov "I appreciate that you love my dick and all, but are you going to fuck me or just use me to jill yourself, mom?"
    else:
        pov "I appreciate that you love my dick and all, but are you going to fuck me or just use me to jill yourself, [mother]?"
    mom "Haha, well either way I'm getting off! But I did promise to ride you..."
    pov "I believe you exact words were, \"fuck you silly...\""
    scene weekend 8pm 061la
    mom "Well I better get to it then. I might be a slut, but I'm no liar."
    "She grins wickedly at you as she positions the head of your penis below her entrance."
    mom "Can you feel that, my pussy is hungry for your cock."
    "She let's her hips fall as she speaks, slowly engulfing your cock inside her."
    pov "Oh, I can feel that, so damn wet."
    mom "And you're burning inside me."
    #----- Added 0.75 Part 1 -----
    if alexissuspicous >= 2 and proom19corsex == True and alexisaway == False:
        jump proom19extlovealexiscor
    #----- end -----
    scene weekend 8pm 061lb
    pov "This wonderful view. My dick deep inside your pussy. Where is belongs."
    mom "Not deep enough..."
    povi "I love how she's narrating this whole experience, it's like a documentary on fucking. God it turns me on!"
    scene weekend 8pm 062la
    mom "God, you're thick..."
    if inc == True:
        pov "I love that view mom!"
    else:
        pov "I love that view [mother]!"
    mom "I'm glad baby! There is so much of you! I'm still taking you in."
    pov "Your boobs are so big. I can barely see your face behind them."
    mom "I'm going to take that as a compliment."
    pov "You should! That's how I meant it!"
    scene weekend 8pm 063la
    mom "You're almost completely inside me. You're so big and hot. I swear you'll reach my cervix at this point!"
    pov "It's good to have a dream slut!"
    "She looks at you lustingly, as she pushes herself even lower on your cock."
    mom "Hah... Ahhh... it's all in!"
    scene weekend 8pm 063lb
    pov "I'm balls deep in your pussy. Finally!"
    mom "Hah, you're so big and hard."
    pov "I can't wait any longer."
    if inc == True:
        pov "Fucking ride me good and hard, mom!"
    else:
        pov "Fucking ride me good and hard, [mother]!"
    "She didn't need any more prompting. She starts bouncing up and down on your hard dick loving every moment of it."
    scene weekend 8pm 064lb
    mom "Oh, hah... hah..."
    with vpunch
    pov "Yes this is amazing!"
    with vpunch
    mom "You're too big! I won't last much longer. You're hitting all my best spots."
    with vpunch
    pov "The cum for me when you're ready. I'm close too. I'm sure you cumming on my dick will drive me over the edge."
    scene weekend 8pm 064la
    mom "Hah... so you'll cum with me...?"
    with vpunch
    pov "As long as you don't stop riding my dick like that!"
    mom "I'm so close... hah... hah..."
    with vpunch
    pov "Then cum with me!"
    mom "HAAAHH... AAAAHHH...!"
    with vpunch
    "You're about to cum too."
    call screen cornicoleweekendlovecowcum

screen cornicoleweekendlovecowcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('cornicoleweekendlovecowcum'), Jump('cornicolelovecowinside')) hovered tt.Action ("Cum inside") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('cornicoleweekendlovecowcum'), Jump('cornicolelovecowoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cornicolelovecowinside:
    scene weekend 8pm 065lbi
    $ nicoleweekendinside = True
    mom "AAAHHH... I'm cumming... I'm cumming!"
    with vpunch
    if inc == True:
        mom "Cum inside me baby! Cum inside mommy!"
    else:
        mom "Cum inside me baby! Cum inside me!"
    pov "Oh fuck! Hnng... I'm cumming too!"
    with vpunch
    mom "I can feel it, hubby! I feel you pusling inside me!. It's so fucking hot."
    scene weekend 8pm 065lai
    mom "Hah... hah... there's... so much inside me..."
    pov "Hah... I've never came so hard before..."
    mom "You came so much... I hoped it would never end..."
    povi "I wonder if we went to far... Nah! It felt so incredidble."
    povi "She's like a bitch in heat, begging for me to cum inside her. I want to do that again!"
    "As if she was listening in on your thoughts, she wiggles her hips while still impaled on your cock."
    mom "Hah... ohh... do you want to stop or keep going?"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovecowoutside:
    scene weekend 8pm 065lbo
    mom "AAAHHH... I'm cumming... I'm cumming!"
    with vpunch
    pov "Oh fuck! Hnng... I'm cumming too!"
    with vpunch
    mom "I can feel it baby, I can feel it spraying me. It's so hot."
    scene weekend 8pm 065lao
    mom "Hah... hah... there's... so much cum on me..."
    pov "Hah... I've never came so hard before..."
    mom "You came so much... I hoped it would never end..."
    pov "You're like a bitch in heat! You just can't get enough."
    mom "Hah... ohh... do you want to stop or keep going?"
    $ alexissuspicous += 1 #----- Added 0.75 Part 1 -----
    jump cornicoleweekendloveroot

label cornicolelovestop:
    pov "I'm spent. I don't think I have another drop of cum inside me. You did good wife, you can rest for now."
    mom "Ok, if you're sure there is nothing else left... Then as you wish. <giggle>"
    "She lays down beside you and rests on your chest."
    if nicoleweekendinside == True:
        scene weekend 8pm 045lao
        if inc == True:
            "You look down at your mother, she's seems exhausted like you, but also very satisfied."
            pov "God damn, you're a great fuck mother."
        else:
            "You look down at [mother], she's seems exhausted like you, but also very satisfied."
            pov "God damn, you're a great fuck [mother]."
        "You don't think much of it when she doesn't respond, you wore the bitch out."
        "But then her expression changes. A look of concern that bothers you."
        scene weekend 8pm 045lai
        pov "What's wrong?"
        mom "You came inside me..."
        pov "Yeah, I did. Like a lot. So?"
        mom "I couldn't help but want it. No, not want. Crave it. I needed you to cum inside me."
        mom "And judging from how powerful it felt when you sprayed your sperm inside me, I think maybe you felt the same way too."
        mom "Like you want to make sure that you impregnated me... That you didn't just want to fuck me, but to breed with me."
        mom "Am I going crazy?"
        call screen cornicoleweekendlovepreg
    else:
        scene weekend 8pm 045lao
        mom "That was so much fun!"
        pov "I'm glad you liked it too. I can't wait for our next time, wife."
        mom "We need to do this again."
        mom "But don't forget, that's slutty wife!"
        pov "Oh no, I'd never forget that!"
        jump cornicoleweekendloveend

screen cornicoleweekendlovepreg():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('cornicoleweekendlovepreg'), Jump('cornicolelovepregyes')) hovered tt.Action ("I want to impregnate her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('cornicoleweekendlovepreg'), Jump('cornicolelovepregno')) hovered tt.Action ("I don't want to impregnate her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cornicolelovepregyes:
    pov "You're not crazy..."
    if inc == True:
        pov "I own you, remeber. What better way to show that than to have you mother my children and rub all over Dad's sad face!"
        pov "I wanted to fill your womb with my seed over and over again. Just to be sure."
        mom "But... you're my son..."
        pov "That doesn't matter. You're my slut, you're my plaything. Besides, I could tell you wanted it."
        pov "You begged me to cum inside you and you came all the harder when I did. Don't try to deny it."
    else:
        pov "I own you, remeber. What better way to show that than to have you mother my children and rub all over Bruces's sad face!"
        pov "I wanted to fill your womb with my seed over and over again. Just to be sure."
        mom "But..."
        pov "That doesn't matter. You're my slut, you're my plaything. Besides, I could tell you wanted it."
        pov "You begged me to cum inside you and you came all the harder when I did. Don't try to deny it."
    "She seems like she's about to do just that, but instead she just squeezes you tighter."
    mom "Well... I..."
    povi "I see she doesn't have much to say about that. I'm right about her. She craves to be possessed and used. I'm happy to do just that."
    "She rests her head on your chest."
    $ nicolebabywant = True
    jump cornicoleweekendloveend

label cornicolelovepregno:
    pov "Bitch you are crazy. I just want to fill your holes because I could. I don't want any kids right now."
    mom "Oh... ok."
    povi "Is she disappointed?"
    "She rests her head on your chest."
    jump cornicoleweekendloveend

label cornicoleweekendloveend:
    #----- Added 0.75 Part 1 -----
    if proom19corsex == True:
        jump proom19extloveendcor
    #----- End -----
    scene weekend 8pm 046l
    mom "Let's go to sleep, hubby. I'm so tired."
    if nicolebabywant == False:
        povi "Well I dodged a bullet there. I don't need kids messing with this hot action I'm getting now. I better make sure she's on the pill."
    if inc == True:
        pov "You did good, mom."
    else:
        pov "You did good, [mother]."
    mom "You too."
    scene black
    "You spend the night together in the wet mess you each made on bed."
    $ nicoleweekendinside = False
    $ weekendactivities += 1
    $ mombasementlovesecond = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

#----- Alexis Date -----
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
    pov "I let you choose our picnic location like you asked, but where are we?"
    ls "That's a barn. There's normally horses in it, dummy."
    pov "I know what this it. But who owns it and why did you choose this place?"
    ls "Less talking, more following! <giggle>"
    scene date 1pm 002
    pov "Oh wow, what a surprise! It's a barn!"
    ls "Haha, you got it dummy!"
    pov "Can you know answer my questions?"
    ls "Haha sure. The owner is Jeremy, he's our neighbor."
    pov "And where are the horses?"
    ls "He doesn't own any. He wanted to buy some but I think he forgot about this place."
    pov "Forgot about his own barn?"
    ls "He spent some time in the military and sever since he has some \"brain damage\". <giggle>"
    pov "Hey, that isn't funny."
    ls "Then you don't know him. He doesn't take things so serious because he's like, mega rich."
    ls "He doesn't have to worry about much anymore. A funny old man."
    pov "Oh, ok."
    scene date 1pm 002a
    ls "Now follow me again. Up here is the perfect place."
    pov "Yeah, sure."
    scene date 1pm 003a
    povi "Holy..."
    ls "You still didn't tell me if you like it here?"
    pov "Oh yeah, the view is awesome! And so beautiful!"
    ls "Yes, I know. That's why I choose it."
    scene date 1pm 004a
    povi "Damn, I wonder if she is showing herself to me on purpose?"
    povi "She must have know that climbing up a ladder before me and wearing a skirt would give me a good view."
    povi "Or is she just being naive?"
    scene date 1pm 005a
    ls "Dummy? Dummy!"
    pov "Huh?"
    ls "Stop day dreaming. Come up here with me."
    pov "Oh... yeah, sure."
    scene date 1pm 007a
    ls "Isn't it a nice up here?"
    pov "Yeah, it's a good choice [ls]."
    ls "Haha, I know."
    scene date 1pm 006a
    povi "And so much space. I wonder if that guy really forgot about a whole barn?"
    ls "Lalala..."
    povi "Ha, she's having her fun at least."
    jump adate1eat

label adate1search:
    scene date 1pm 007a
    ls "Want to play something?"
    pov "Yeah, why not?"
    povi "I wonder what she's up to?"
    ls "I hide, you have to find me. But you better give it your best, it won't be easy dummy!"
    pov "So hide and seek?"
    ls "Yes, I hide first! You have to wait here two minutes. And no cheating!"
    pov "I don't need that to win, haha."
    ls "Winning, you? <giggle>"
    scene black
    "You wait around two minutes."
    povi "We haven't played this since we were little. She's probably feeling a bit nostalgic or something."
    povi "But she's having fun, so that's all that matters. I like seeing her so happy."
    povi "So, where to start?"
    jump adate1way

label adate1way:
    if adatehide >= 3 and lilsiscorruption > lilsislove:
        scene date 1pm 005
        povi "There she is."
        jump adate1cor
    elif adatehide >= 3 and lilsislove >= lilsiscorruption:
        scene date 1pm 001f
        povi "I can't find her..."
        jump adate1love
    else:
        scene date 1pm 001f
        call screen adate1way1

screen adate1way1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way1'), Jump('adate1stables')) hovered tt.Action ("Search in the stables") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way1'), Jump('adate1front')) hovered tt.Action ("Go outside at the front") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way1'), Jump('adate1back')) hovered tt.Action ("Go outside at the back") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1stables:
    scene date 1pm 002f
    $ adatehide += 1
    "You search in the stables for her."
    povi "Not here."
    scene date 1pm 002g
    povi "Also empty. I should check somewhere else."
    jump adate1way

label adate1front:
    scene date 1pm 005f
    $ adatehide += 1
    povi "Nothing. Where is she?"
    call screen adate1way2

screen adate1way2():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way2'), Jump('adate1left')) hovered tt.Action ("Go left") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way2'), Jump('adate1right')) hovered tt.Action ("Go right") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way2'), Jump('adate1way')) hovered tt.Action ("Go back in") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1right:
    scene date 1pm 003f
    $ adatehide += 1
    povi "Nothing. And she isn't hiding in the grass either."
    call screen adate1way3

screen adate1way3():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way3'), Jump('adate1front')) hovered tt.Action ("Go back to the front") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way3'), Jump('adate1back')) hovered tt.Action ("Go to the back") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1back:
    scene date 1pm 004f
    $ adatehide += 1
    povi "Hm... Let's go back to the front."
    jump adate1front

label adate1left:
    if NTR == True and davidemeet == False:
        scene date 1pm ntr02
        povi "Oh..."
        jump adate1ntr
    else:
        scene date 1pm 003g
        $ adatehide += 1
        pov "..."
        call screen adate1way4

screen adate1way4():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way4'), Jump('adate1front')) hovered tt.Action ("Go back to the front") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1way4'), Jump('adate1back')) hovered tt.Action ("Go to the back") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1love:
    ls "Hey dummy!"
    pov "Huh?"
    ls "Up here!"
    scene date 1pm 015a
    ls "I knew you wouldn't find me, haha."
    povi "I should have known she would have cheated."
    pov "..."
    if inc == True:
        ls "Oh, don't be sad, big brother. <giggle>"
    else:
        ls "Oh, don't be sad, [pov]. <giggle>"
    pov "I'm not..."
    scene date 1pm 016a
    ls "Ouch!"
    "[ls] hits her head on the roof."
    pov "Haha, dummy!"
    ls "Oh no!"
    scene date 1pm 017a
    povi "Oh shit, she lost her balance."
    ls "Aaaahhh..."
    if inc == True:
        povi "Brace yourself, little sister incoming!"
    else:
        povi "Brace yourself, little girl incoming!"
    scene date 1pm 018a
    ls "Ohh..."
    povi "Ah, damn. That hurts!"
    "You managed to catch her somehow."
    scene date 1pm 019a
    if inc == True:
        ls "Aww... are you alright, big brother?"
    else:
        ls "Aww... are you alright, [pov]?"
    povi "Play it tough! Don't let her know you're in pain, ahh..."
    pov "Owww..."
    povi "Seriously..."
    pov "I'm ok. No harm done."
    scene date 1pm 020a
    ls "Yes! I knew it."
    if inc == True:
        ls "My big brother saved me!"
    else:
        ls "You saved me!"
    ls "I was so high up, I could have died! You're my hero!"
    pov "Oh... ok."
    ls "Don't be so modest! I'm so proud right now!"
    scene date 1pm 021a
    ls "Muah!"
    povi "Wow, what's happening?"
    "[ls] kisses you on the mouth."
    scene date 1pm 022a
    ls "Oh no! No!"
    pov "What?"
    povi "Damn, do I smell bad?"
    scene date 1pm 023a
    ls "No! No! This can't be real!"
    pov "What's with you [ls]? Did I do something wrong?"
    ls "No! <sobs>"
    pov "Are you crying? Why?"
    call screen adate1lovevo

screen adate1lovevo:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1lovevo'), Jump('adate1lovelk')) hovered tt.Action ("Take a peek") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('adate1lovevo'), Jump('adate1love2')) hovered tt.Action ("Don't") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1lovelk:
    scene date 1pm 024a
    povi "Damn, if she wasn't crying this would almost be hot..."
    jump adate1love2

label adate1love2:
    scene date 1pm 025a
    povi "Wow, she's seriously crying. But why?"
    if inc == True:
        pov "Hey little sister, what's wrong? I don't understand."
    else:
        pov "Hey [ls], what's wrong? I don't understand."
    ls "I didn't want to do it, I'm so sorry!"
    pov "Do what? Kiss me?"
    scene date 1pm 026a
    ls "Yes..."
    pov "You gave me a kiss and now you're crying? I still don't get it."
    ls "I did something wrong! I kissed you, but I'm not supposed to!"
    pov "Supposed to?"
    if inc == True:
        ls "I'm your sister, so we can't do this! It's taboo!"
    else:
        ls "We know each other for so long, so we can't do this! It's taboo!"
    pov "Haha, why's that?"
    ls "Mom told me about it."
    pov "Hahaha... hahaha... haha..."
    scene date 1pm 027a
    ls "Why are you laughing?"
    pov "Haha, it's ok! A little kiss isn't the same thing as what you are talking about."
    ls "But..."
    pov "Look, even it was the same thing you're talking about, I don't think it's wrong between two people that care about each other."
    pov "Besides, we're all alone here and there is no one to judge us except us."
    ls "Huh?"
    pov "So if you feel you just did something wrong because I would think it's wrong, you don't have to worry about that. I'm not going to judge you."
    ls "Oh..."
    povi "Yeah, that's not very convincing."
    pov "Come here!"
    scene date 1pm 028a
    ls "Ohh..."
    pov "Stop crying. I won't think bad things about you ever ok. But you don't need to worry, I won't tell anyone about it, ok."
    ls "I'm still sorry... <sob>"
    if inc == True:
        pov "Hey, I'm your big brother. I won't let you down!"
    else:
        pov "Hey, I've known you for so long. I won't let you down!"
    ls "Aww..."
    call screen adate1loveki

screen adate1loveki():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if lilsislove >= 20:
            imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('adate1loveki'), Jump('adate1lovekiss')) hovered tt.Action ("Kiss her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('adate1loveki'), Jump('adate1lovetalk')) hovered tt.Action ("Cheer her up") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1lovetalk:
    scene date 1pm 032a
    pov "Are you feeling better now?"
    ls "Yes, much better. Thank you for your kind words."
    pov "I'm glad, do you want to go home now?"
    ls "Yes. I'm sorry again."
    pov "Don't be! There's no need to."
    scene black
    "You went home with [ls]."
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

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
    pov "Because now you don't have to worry anymore. I did something taboo too. So we're equal now."
    scene date 1pm 031a
    pov "And since when did you become such a goof?"
    ls "Hnn..."
    pov "You never have to worry about that stuff with me. I love you..."
    ls "Hm..."
    pov "My little dummy."
    scene date 1pm 032a
    ls "So you're not mad anymore?"
    pov "I was never mad about it. It was just your imagination."
    ls "Then I'm happy now too."
    pov "Much better."
    scene date 1pm 033a
    if inc == True:
        ls "That my big brother is such a great guy! I'm so glad."
    else:
        ls "That you're such a great guy! I'm so glad."
    pov "And I'm happy that I can be with you too."
    ls "Aww, so sweet."
    pov "And that you're looking so damn cute now."
    ls "<giggle>"
    if lilsislove >= 30:
        pov "I need another one!"
        povi "She's actually a pretty good kisser. I'm getting a bit worked up."
        scene date 1pm 034a
        ls "Hnn..."
        pov "<kissing>"
        ls "Hmm..."
        $ lsiskiss += 1
        scene date 1pm 035a
        ls "Why did you kiss me... again?"
        pov "Because I wanted to?"
        ls "Oh...?"
        pov "Haha, now I'm the bad one. I did it one more time than you. So you're now the good one again."
        scene date 1pm 036a
        ls "Oh I see, haha."
        if inc == True:
            ls "Thank you for cheering me up, big brother!"
        else:
            ls "Thank you for cheering me up, [pov]!"
        pov "You're welcome!"
        povi "I'm pretty sure she knows exactly what I'm up to..."
        if lilsislove >= 50 and lsisproninc >= 4:
            if inc == True:
                ls "Hey big brother... Can I do something for you?"
            else:
                ls "Hey [pov]... Can I do something for you?"
            pov "What do you mean?"
            ls "Well, I noticed your... bulge down there..."
            pov "Oh... Well yeah. That happens sometimes when you're with a pretty girl."
            ls "<giggle> So you think I'm pretty?"
            if inc == True:
                pov "Of course I do! My pretty little sister!"
            else:
                pov "Of course I do! My pretty [pov]!"
            ls "So... I saw something on some of those videos you showed me..."
            povi "Is she talking about the porn videos?"
            scene date 1pm 035a
            ls "I think you'll really like it."
            pov "Ok, what do I need to do?"
            scene date 1pm 036a
            ls "Just stand there!"
            pov "Oh... Ok."
            pov "Wow, she's taking charge now? That's a twist. Espcially after all of this trouble about a kiss."
            "[ls] smiles at you as she slowly gets down on her knees, her hand running down your shirt."
            scene date 1pm 015
            if inc == True:
                pov "Whoa! Wait little sis... What are you doing?!"
            else:
                poc "Whoa! Wait [ls]... What are you doing?!"
            ls "I'm thanking you for saving me earlier..."
            ls "Don't you like this sort of thing? The guys on the videos seemed to like it..."
            pov "I'm not saying I don't like this... but you just made a pretty big deal out of kiss."
            pov "I'm just confused... and really turned on!"
            ls "..."
            if inc == True:
                pov "Sis?"
            else:
                pov "[ls]?"
            ls "I was thinking about this when I brought you out here. I was just to scared to ask you..."
            ls "Then I got scared that you would think I was horrible for wanting to do something like this."
            pov "I would never think that!"
            ls "I know... That's why I really want to do this..."
            "She quickly unzips your pants and reaches in to free your penis from it's confines."
            scene date 1pm 017 #alexis penis in hand looking at you
            "She sits there for a moment, just holding it in her hand, watching you."
            pov "Hmmm... You hand is warm."
            "She smiles at your comment and decides to really look at your dick in her hands"
            scene date 1pm 018 #alexis penis in hand looking at it
            pov "Have you ever seen of these before? Or held one?"
            ls "Well... I've seen one before. Not this close though."
            povi "Interesting... I will need to find out more about that later."
            pov "Well you can do whatever you want with mine, as long as you are careful."
            scene date 1pm 017 #alexis penis in hand looking at you
            ls "Does... my hand... feel good on it?"
            pov "Yes it does. It feels better than my own."
            ls "You touch it often?"
            pov "Well yeah... everytime I pee or want to make myself feel good."
            ls "<giggle> Haha, gross! I don't want to hear about you peeing!"
            povi "Duh [pov]!"
            ls "...but what do you do to make it feel good?"
            pov "Oh... well I hold like you are doing or I rub it or squeeze it... A lot of things"
            scene date 1pm 018 #alexis penis in hand looking at it
            "She squeezes you penis, softly."
            pov "Hmmm... That's good. No release your grip and then squeeze it again."
            ls "Ok."
            "She repeats the cycle of squeezing and releasing then squeezing for a while. You can feel yourself getting close to cumming."
            povi "This is crazy! It feels so good. Her skin is so soft and she looks so, fucking cute!"
            if inc == True:
                pov "Sis, I'm getting close."
            else:
                pov "[pov], I'm getting close."
            ls "Close... to what?"
            pov "Well, when a guy feels really good, like I do from what you're doing now, he releases white stuff from his penis."
            scene date 1pm 017 #alexis penis in hand looking at you
            ls "Does it hurt?"
            pov "No! It feels really good. It's calling cumming."
            ls "I can I see you... cum?"
            povi "Fuck yes you can!"
            pov "Yeah if you want. Keep doing what you are doing."
            scene date 1pm 018 #alexis penis in hand looking at it
            pov "Yeah, that feels good. But it still might take a while."
            ls "How can I make it happen quicker?"
            povi "Holy shit! Maybe I can get her to put it in her mouth!"
            pov "Well, you could put it in your mouth, maybe?"
            ls "Ewww! I don't know..."
            povi "Maybe I should dial it back a bit."
            pov "Maybe you could give it a little kiss?"
            scene date 1pm 017 #alexis penis in hand looking at you
            ls "A kiss?"
            pov "Yeah, you know how it feels nice to be kisses? It feels nice down there too."
            ls "Oh..."
            scene date 1pm 018 #alexis penis in hand looking at it
            ls "I guess... I could do that. it's just a kiss."
            scene date 1pm 019 #alexis penis in hand kissing it
            if inc == True:
                pov "Whoa... yeah, that's really good little sis."
            else:
                pov "Whoa... yeah, that's really good [ls]."
            ls "Mmmm... <kiss>"
            povi "I'm really close, do I tell her? Nah, she like's surprises!"
            ls "<kiss> Can I taste it a little? <kiss>"
            pov "Yes!"
            pov "I mean, sure if you want."
            ls "<kiss><kiss><lick><lick>"
            "That was it, just want you needed. You hold her head close as you blast cum all over, her mouth is slightly open in surprise."
            scene date 1pm 019x #alexis penis in hand kissing it with cum spurting
            if inc == True:
                pov "Oh god sis! Hnnng!"
            else:
                pov "Oh god [ls]! Hnnng!"
            ls "Ohhh!"
            "She's still squeezing you and licking your tip while you cum."
            povi "Damn, she's a natural!"
            "After a while you finally finish cumming."
            scene date 1pm 020 #alexis cum on mouth looking at you
            ls "<giggle>"
            pov "Haha, like that huh?"
            ls "Yeah, it was like fireworks!"
            ls "Tastes a little funny though."
            if inc == True:
                povi "Wow, my little sister is tasting my cum! Best date ever!"
            else:
                povi "Wow, [ls] is tasting my cum! Best date ever!"
            pov "Well, thank you. You made me feel really good! A very nice reward!"
            pov "Why don't you stand up now."
            scene date 1pm 021 #alexis cum on face looking down
            povi "Wait, she looks sad now? She's all over the place emotionally."
            if inc == True:
                pov "Hey, what's the matter now, little sis?"
            else:
                pov "Hey, what's the matter now, [ls]?"
            ls "I just... what if I'm a bad person?"
            povi "This again? Poor girl."
            scene date 1pm 022 #alexis cum on face looking at you hand on face
            pov "You're never going to be a bad person! Why would you think that?"
            ls "Well Mom says girls that like this kind of thing are bad... and I... like it."
            pov "Well Mom is wrong!"
            pov "You love me and I love you. And you just helped me feel very good. That's all."
            ls "Really?"
            pov "Yeah, of course."
            pov "Besides, like I said. This is just between us. I want you all to myself anyway!"
            ls "<giggle> ...dummy!"
            pov "Hey, that's Hero dummy to you!"
            ls "Haha! Ok."
            pov "Now lets get you cleaned up and go on home. Alright?"
            ls "Yes, let's go home."
            "You clean off your cum from her face and start to head towards the barn door putting your arm around her."
            scene date 1pm 033a
            if inc == True:
                pov "And little sis, no more of this bad person talk. You're amazing."
                pov "And if anyone says otherwise... I'll kick their ass for you!"
                ls "Even if it's Mom?!"
            else:
                pov "And little sis, no more of this bad person talk. You're amazing."
                pov "And if anyone says otherwise... I'll kick their ass for you!"
                ls "Even if it's my Mom?!"
            if lilsiscorruption >= 40:
                pov "Well, maybe I'll just spank her ass for you then. Since it's Mom."
                ls "<giggle> She might like that!"
                povi "Wow, what have these girls been talking about when I'm not around?"
                pov "Haha, true! But you remember what I said right? You'll alway be a good person to me."
            else:
                pov "Yup, even if it's her!"
            ls "<giggle> Okay... my Hero!"
            pov "Stop that, Haha!"
            scene black
            "You go home together."
            $ d1ralove = True
            jump frontdoor
    scene date 1pm 036a
    pov "Should we go home now?"
    if inc == True:
        ls "Yes. It was a very nice trip with you, big brother."
    else:
        ls "Yes. It was a very nice trip with you, [pov]."
    pov "Yeah I had fun too, [ls]. Let's go home."
    scene black
    "You go home together."
    $ d1ralove = True
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label adate1cor:
    povi "She can't seriously be stuck on a fence... can she?"
    ls "Hnn... Hm..."
    povi "She's seems to actually be struggling to free herself. But how did she get like this?"
    povi "Lucky for her I'm her noble date... or am I?"
    "You walk over to her silently."
    scene date 1pm 006
    pov "Hanging there completely helpless, geez [ls]."
    ls "Oh you found me? Please help me, I'm stuck."
    pov "Well it serves you right for cheating at the game! Hahaha!"
    ls "I didn't cheat, you're just bad at it, dummy! Now help me please."
    call screen adate1corhelp

screen adate1corhelp():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if lilsiscorruption >= 40:
            imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('adate1corhelp'), Jump('adate1corpunish')) hovered tt.Action ("Play with her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('adate1corhelp'), Jump('adate1corpush')) hovered tt.Action ("Help her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1corpush:
    "You decide to push her over the fence."
    pov "Here let me help you."
    ls "Waaah..."
    scene date 1pm 014x
    ls "Ow..."
    pov "Oh shit. Are you alright?"
    ls "Yes, ow. Thank you."
    pov "Maybe that's your punishment for cheating."
    ls "But I didn't..."
    pov "Yeah... yeah..."
    scene date 1pm 015x
    ls "Can we go home now? My knees hurt."
    pov "So you did get hurt? I'm sorry [ls]."
    ls "Yes I did..."
    pov "Ok. Let's go back home and get you patched up then."
    scene black
    "You go home together."
    $ d1ranormal = True
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label adate1corpunish:
    povi "Let's have some fun with her."
    "You walk closer to her."
    ls "Good, you can push... Aahhh..."
    scene date 1pm 008
    "You pull her panties down."
    ls "What...? What happened?!"
    pov "Bad girls get punished for cheating!"
    ls "But... you can't be serious! You pulled my panties down!"
    pov "Yes I did. It will be better for the punishment."
    ls "Noo! Stop! Don't look at me!"
    pov "What a cute pussy you have."
    if inc == True:
        ls "Please stop! You're my big brother. You shouldn't see me naked."
    else:
        ls "Please stop! We've known each other for to long. You shouldn't see me naked."
    povi "Damn! What to do now?"
    jump adate1corplay

label adate1corplay:
    scene date 1pm 008
    call screen adate1corplay1

screen adate1corplay1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if lsispronBDSM >= 4:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('adate1corplay1'), Jump('adate1corBDSM')) hovered tt.Action ("Slap her ass") focus_mask True
        if lsispronanal >= 4:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('adate1corplay1'), Jump('adate1coranal')) hovered tt.Action ("Finger her asshole") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('adate1corplay1'), Jump('adate1corfinger')) hovered tt.Action ("Finger her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('adate1corplay1'), Jump('adate1corrub')) hovered tt.Action ("Rub her clit") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1corBDSM:
    scene date 1pm 009
    povi "Let's start gentle and then surprise her."
    ls "Noo... You're touching me! Stop!"
    pov "Ssshh..."
    if su15masBDSM == True:
        povi "I saw her masturbating and talking about BDSM, so I'm sure she'll like it."
    else:
        povi "I wonder if she liked any of that BDSM stuff I showed her?"
    scene date 1pm 010slap
    with vpunch
    "You slap her ass."
    scene date 1pm 011slap
    ls "Aaahhh...! You slapped me!"
    pov "Yes! Bad girls need to be spanked."
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
        pov "Your ass is turning red!"
        scene date 1pm 013slap
        ls "Hah... aaahhh... please... stop..."
        pov "You like that, don't you?"
        ls "Hah... no... hah..."
        povi "I don't know, she's getting wet. I think she likes it more than she'll admit."
        pov "Maybe you want even more?"
        if inc == True:
            ls "No, please, big brother. I'm sorry. You've punished me enough."
        else:
            ls "No, please, [pov]. I'm sorry. You've punished me enough."
        pov "That's not the right thing to say to make me stop. I'm pretty sure you know what is!"
        pov "So you need some more!"
        scene date 1pm 012slap
        with vpunch
        pov "Now your ass is even more red!"
        ls "Ah... please stop master!"
        scene date 1pm 013slap
        ls "Hnng... hah... hah..."
        povi "Damn, she really said it. Such a naughty girl."
        povi "I don't want to stop now. She's so wet, I'll lick her now to orgasm and so she'll know she did good."
        jump adate1lick
    else:
        ls "No! Stop it!"
        pov "Oops..."
        povi "She struggled so much that she fell over the fence."
        jump adate1fail

label adate1coranal:
    scene date 1pm 009
    povi "Let's start gentle and then surprise her."
    ls "Noo... You're touching me! Stop!"
    pov "Ssshh..."
    if su15masanal == True:
        povi "I saw her masturbating and talking about anal, so I'm sure she'll like it."
    else:
        povi "I wonder if she liked any of that anal stuff I showed her?"
    scene date 1pm 010anal
    ls "Aaaahhh... What are you doing?"
    pov "Punishing your backdoor."
    ls "No... please, not there."
    povi "Wow she's so tight. I never felt such a tight hole. I can't wait to stick my dick in there."
    if inc == True:
        ls "Please big brother. Your finger is in my asshole. It's so wrong."
    else:
        ls "Please [pov]. Your finger is in my asshole. It's so wrong."
    "You start to move around inside her."
    ls "Hnng... hah..."
    pov "You're not supposed to enjoy your punishment, [ls]!"
    ls "Hnn... I don't, hah..."
    povi "Does she really like anal that much? I can barely believe it. I'll give her more then."
    if lilsiscorruption >= 60:
        scene date 1pm 011anal
        "You push your finger further in and start to pump it in and out slowly."
        ls "Hnng... hah... oh, please..."
        pov "You like that, don't you?"
        if inc == True:
            pov "Getting your asshole fingered by your big brother?"
        else:
            pov "Getting your asshole fingered by me?"
        ls "No... aahhh... you're wro... hah..."
        povi "Damn, her tight asshole clinging around my finger and she's getting wet. Anal is definitely the right thing for her."
        pov "No need to lie to me [ls]. I can feel the reactions of your asshole."
        ls "Hnnng... hah... stop..."
        pov "I can't stop! Your body tells me that you like it."
        ls "Hnnn... not... fair..."
        pov "A punishment is never fair. So...?"
        ls "..."
        ls "It feels... hnn... good! Your finger... makes me... hah... feel good... hah."
        if inc == True:
            pov "So you like your asshole getting fingered by your big brother?"
            ls "Yes... I like your finger in me there... big brother..."
        else:
            pov "So you like your asshole get fingered by me?"
            ls "Yes... I like your finger in me there... [pov]..."
        povi "Damn, she really said it. Such a naughty girl."
        pov "Why stop then while you're enjoying it?"
        ls "Hnng... it's wrong... hah..."
        povi "That crap again."
        povi "I don't want to stop now. She's so wet, I'll lick her now to orgasm and so she'll know that she did good."
        jump adate1lick
    else:
        ls "No! Stop it!"
        pov "Oops..."
        povi "She struggled so much that she fell over the fence."
        jump adate1fail

label adate1corrub:
    scene date 1pm 009
    povi "Let's start gentle and then surprise her."
    ls "Noo... You're touching me! Stop!"
    pov "Ssshh..."
    if su15masnormal == True:
        povi "I saw her masturbating, so I'm sure she'll like it."
    scene date 1pm 010clit
    ls "Aaaahhh... What are you doing?"
    pov "Teasing you for your punishment."
    ls "No... hah... not..."
    povi "Damn, she's sensitive! But her pussy is looking so damn sweet."
    ls "Hnnng... haaah..."
    ls "No! Stop... hah... rubbing me there..."
    pov "Why? I'm sure you rub yourself there before."
    if inc == True:
        ls "Please... don't touch me there... hah... big brother!"
    else:
        ls "Please... don't touch me there... hah... [pov]!"
    pov "You should be thankful. You can enjoy this punishment."
    ls "Hnng... no..."
    povi "She starts twitching. I'll tease her some more."
    pov "I don't know, it seems like you're liking it."
    ls "Noo...!"
    if lilsiscorruption >= 60:
        scene date 1pm 011clit
        povi "Wow, her labia is swelling. She must be real horny right now."
        ls "Hnng... Aahhh... Ahhh..."
        pov "You like that, don't you?"
        if inc == True:
            pov "Getting your clit rubbed by your big brother?"
        else:
            pov "Getting your clit rubbed by me?"
        ls "No... aahhh... you're wro... hah..."
        povi "Damn, her labia is swelling even more and she's so damn wet."
        pov "No need to lie to me [ls]. I can feel the reactions of your pussy."
        ls "Hnnng... hah... stop..."
        pov "I can't stop! Your body tells me that you like it."
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
        povi "Damn, she really said it. Such a naughty girl."
        pov "Why stop then when you're enjoying it?"
        ls "Hnng... it's wrong... hah..."
        povi "That crap again."
        povi "I don't want to stop now. She's so wet, I'll lick her now to orgasm and so she'll know that she did good."
        jump adate1lick
    else:
        ls "No! Stop it!"
        pov "Oops..."
        povi "She struggled so much that she fell over the fence."
        jump adate1fail

label adate1corfinger:
    scene date 1pm 009
    povi "Let's start gentle and then surprise her."
    ls "Noo... You're touching me! Stop!"
    pov "Ssshh..."
    if su15masnormal == True:
        povi "I saw her masturbating, so I'm sure she'll like it."
    scene date 1pm 010finger
    "You enter her pussy."
    ls "Aaaahhh... What are you doing?"
    pov "Exploring your pussy, haha."
    ls "No... hah... not..."
    povi "Damn, she's sensitive! Her pussy is damn warm and sweet. I can't wait to stick my dick in it."
    ls "Hnnng... haaah..."
    ls "No! Stop... hah... you're in me..."
    pov "Yes and it was the right decision."
    if inc == True:
        ls "Please... don't touch me there... hah... big brother!"
    else:
        ls "Please... don't touch me there... hah... [pov]!"
    pov "You should be thankful. You can enjoy this punishment."
    ls "Hnng... no..."
    povi "She start twitching. I'll get deeper in her."
    pov "I don't think I can stop now."
    ls "Noo...!"
    if lilsiscorruption >= 60:
        scene date 1pm 011finger
        povi "Holy shit! She's a virgin, I can feel her hymen!"
        povi "To think about it, I could be her first..."
        ls "Hnng... Aahhh... Ahhh..."
        pov "You like that, don't you?"
        if inc == True:
            pov "Getting fingered by your big brother?"
        else:
            pov "Getting fingered by me?"
        ls "No... aahhh... you're wro... hah..."
        povi "Damn, her pussy is twitching and she's so damn wet."
        pov "No need to lie to me [ls]. I can feel the reactions of your pussy."
        ls "Hnnng... hah... stop..."
        pov "I can't stop! Your body tells me that you like it."
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
        povi "Damn, she really said it. Such a naughty girl."
        pov "Why stop then when you're enjoying it?"
        ls "Hnng... it's wrong... hah..."
        povi "That bullshit again."
        povi "I don't want to stop now. She's so wet, I'll lick her now to orgasm and so she'll know that she did good."
        jump adate1lick
    else:
        ls "No! Stop it!"
        pov "Oops..."
        povi "She struggled so much that she fell over the fence."
        jump adate1fail

label adate1lick:
    "You get behind her."
    scene date 1pm 009lick
    ls "Hnng... stop!"
    if lilsiscorruption >= 80:
        povi "Her sweet taste!"
        ls "Hah... you're licking me..."
        pov "Yes, to complete your punishment you need to cum!"
        ls "No! Hnng... I don't think... hah... to..."
        pov "I have too, its the rules!"
        ls "Aaahhh... haaahhh..."
        if inc == True:
            pov "Enjoy cumming from your big brothers tongue!"
        else:
            pov "Enjoy cumming from my tongue!"
        ls "Noo... Hnng... it's so wrong... feels so good..."
        "You lick her faster."
        scene date 1pm 010lick
        ls "Hah... oh god... hah..."
        pov "I knew you'd love it!"
        ls "Ohhh... ohhh... I can't..."
        pov "Just give in to yourself and stop denying it. You don't actually want me to stop do you?"
        if inc == True:
            pov "You'll cum from your brother's tongue. And you'll love it!"
        else:
            pov "You'll cum from my tongue. And you'll love it!"
        ls "Please... hah... ohhh..."
        povi "She'll cum soon, time to spice it up."
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
        povi "She struggled so much that she fell over the fence."
        jump adate1fail

label adate1lay:
    pov "Wow..."
    scene date 1pm 014
    "She fell over the fence."
    povi "She must have had a strong orgasm. And what a wonderful view. I need more!"
    pov "Hey, is everything alright [ls]?"
    ls "Hah... hah... hah..."
    pov "I think you liked that so much, maybe you want to reward me for punishing you?"
    if lilsiscorruption >= 100:
        scene date 1pm 015
        povi "I know you're done after that hard cumming."
        if inc == True:
            pov "It's your turn to help your brother!"
        else:
            pov "It's your turn to help me!"
        ls "Huh? What do you mean?"
        pov "You did such a good job taking your punishment it made me want to feel good too!"
        ls "You mean...?"
        scene date 1pm 016
        pov "Yes! I'm so hard it's starting to hurt me!"
        ls "Ohh...?"
        pov "Haha, I know it might be your first time you've seen a dick up close like this, but you don't have to be scared."
        ls "It's so... big..."
        pov "Yes and you're the reason it got so big. You should be proud!"
        pov "Now please touch it. I need to cum too, badly!"
        pov "You enjoyed your punishment, now I want to enjoy mine."
        ls "O... ok..."
        scene date 1pm 017
        pov "Ohh.. your fingers are so soft and gentle!"
        ls "Hnn..."
        pov "Yes, rub it slowly. I'll guide you with my hand."
        if inc == True:
            ls "Ok... big brother..."
        else:
            ls "Ok... [pov]..."
        povi "Wow, no more complaints about \"wrong\" or \"forbidden\". She must have enjoyed her orgasm very much. And now she's feeling guilty maybe?"
        pov "Is this the first dick you've held?"
        ls "Yes..."
        if inc == True:
            pov "Good. It's very important that you learn those things from your big brother and not some other boy."
        else:
            pov "Good. It's very important that you learn those things from me and not some other boy."
        ls "You think so?"
        pov "Yes and I know you can be a good girl!"
        pov "Now do it yourself for a while. Show me how much you enjoyed my help before."
        if inc == True:
            ls "Ok... big brother..."
        else:
            ls "Ok... [pov]..."
        scene date 1pm 018
        povi "Damn, she's such a tease! I want to fuck her mouth so badly right now!"
        if inc == True:
            pov "You're treating me so good, lil sis. It's like heaven."
        else:
            pov "You're treating me so good, [ls]. It's like heaven."
        ls "Thank you. I'll do my best."
        povi "Damn! Did she really say that? She's giving me her first hand-job ever and wants to do a good job for me?"
        ls "Your... dick is pulsating. Is that normal?"
        povi "It's like she's playing doctor with me. I wish I could we could do this forever."
        pov "The pulsating shows that I'm about to cum, so I'll have to release soon so it will stop hurting me."
        ls "Hurting you? I know something that will help."
        scene date 1pm 019
        povi "Holy shit! She's kissing my dick! Like kissing the pain away!"
        ls "<kiss> No need for pain! <kiss>"
        povi "Best shit ever!"
        pov "AAAAHH!"
        scene date 1pm 019x
        ls "Ohhh!"
        "You hold her head tight as you cum."
        pov "Yes! Yes! Yes!"
        ls "Hnn..."
        scene date 1pm 020
        ls "Noo! Look what you did!"
        if inc == True:
            ls "Your sperm hit me and some got in my mouth, big brother."
            povi "She has no idea how hot she looks right now. My sperm on my little sister's face. And even in her mouth."
        else:
            ls "Your sperm hit me and some got in my mouth, [pov]."
            povi "She has no idea how hot she looks right now. My sperm on her face. And even in her mouth."
        pov "I see! I couldn't control myself."
        pov "But don't worry. It shows you that you did a very, very good job."
        ls "Hnng..."
        pov "Maybe you should try to taste it."
        if inc == True:
            povi "The taste of your big brother."
        ls "It's salty and thick."
        povi "It's like I'm in heaven. But how I got here is beyond my understanding."
        scene date 1pm 021
        ls "Hnn... hnn..."
        pov "What's wrong? You look sad now."
        ls "We did these forbidden things... and we both liked it..."
        pov "Oh yes, I loved it very much and I'm very glad that you loved it too."
        ls "But..."
        scene date 1pm 022
        if inc == True:
            pov "Don't worry, lil sis. When grown ups feel those natural urges they just satisfy them as we did."
            pov "When we don't need to get depressed and sad about it after. It's a good thing we can help each other with that."
            pov "No one is mad at you because of it and if you liked it, this can be our secret. But we need to trust each other as siblings..."
            pov "And help each other when we feel that way. I'm glad that you're the one helping me. And I'll help you anytime."
            ls "Ok... I understand big brother."
            pov "So you feel better now?"
            ls "Yes. Thank you. I like doing these things with you."
        else:
            pov "Don't worry, [ls]. When grown ups feel those natural urges they just satisfy them as we did."
            pov "When we don't need to get depressed and sad about it after. It's a good thing we can help each other with that."
            pov "No one is mad at you because of it and if you liked it, this can be our secret. But we need to trust each other..."
            pov "And help each other when we feel that way. I'm glad that you're the one helping me. And I'll help you anytime."
            ls "Ok... I understand [pov]."
            pov "So you feel better now?"
            ls "Yes. Thank you. I like doing these things with you."
        pov "Let's go home! It was a very nice trip with you. And I'm sure you'll have much to think about at home."
        ls "Yes, you're right. Let's go home."
        scene black
        "You go home together."
        $ d1racorf = True
        if day >= 6:
            $ weekendactivities += 1
            if weekendactivities >= 3:
                jump weekendskip
            else:
                jump weekendacchoose
        else:
            jump frontdoor
    else:
        ls "No! We should stop this!"
        jump adate1fail

label adate1fail:
    scene date 1pm 014
    ls "No! It has to stop!"
    pov "Oh... oh..."
    scene date 1pm 015x
    ls "It's wrong what you did to me!"
    povi "Damn, maybe she wasn't corrupted enough?"
    ls "I want to go home now."
    pov "Maybe you're right. Let's go home."
    scene black
    "You go home together."
    $ d1racor = True
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label adate1ntr:
    $ adatedavide = True
    povi "What the hell is he doing here?"
    povi "Barging into my time with [ls]."
    scene date 1pm ntr03d
    povi "Oh...? It's seems they don't know each other."
    if inc == True:
        povi "Oh right, mom has kept her away from the gang all this time."
    else:
        povi "oh right, [mother] has kept her away from the gang all this time."
    call screen adate1ntrdec

screen adate1ntrdec():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('adate1ntrdec'), Jump('adate1ntrapp')) hovered tt.Action ("They can be friends (Darker Paths)") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('adate1ntrdec'), Jump('adate1ntrdis')) hovered tt.Action ("They can never be friends") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1ntrapp:
    if inc == True:
        povi "I don't understand why mom makes such a fuss about it."
    else:
        povi "I don't understand why [mother] makes such a fuss about it."
    povi "[ls] is old enough to decide these things for herself. She can choose her own acquaintances."
    call screen checkdarkerpaths_alexis
    jump adate1ntrapp2

label adate1ntrapp2:
    scene date 1pm ntr03d
    if alexis_voyeur == True or alexis_ntr == True:
        if alexis_voyeur == True:
            povi "But I should introduce them. Davide helped me, so I'll help him."
            scene date 1pm ntr04
            pov "Hey there!"
            ls "Oh...?"
            davide "Huh?"
            if inc == True:
                ls "Big brother?"
            else:
                ls "[pov]?"
            davide "Wait, she's here with you? I'm sorry bro, I didn't mean to step up on your business."
            scene date 1pm ntr05
            pov "Haha, relax Davide. What are you doing here?"
            davide "I had an arguement with Jeremy. He's convinced that he owns horses and they're here."
            davide "So I came by to take a photo and show him that he's wrong."
            pov "Haha, that guy has to be seriously weird."
            davide "Yes, haha."
            pov "Oh..."
            scene date 1pm ntr06
            if inc == True:
                pov "No need to be scared, lil sis. This is Davide, a friend of mom and dad."
            else:
                pov "No need to be scared, [ls]. This is Davide, a friend of [mother] and Bruce."
            pov "And he gives me some work from time to time, he's a cool guy."
            ls "Oh? From your meetings at night, the one's I'm not allowed to go to?"
            pov "Yes, that's right."
            ls "So that's the reason I haven't meet him before?"
            pov "Yes, he's a bad boy, haha."
            if inc == True:
                davide "So you're [pov]'s little sister? That's a nice surprise!"
            else:
                davide "So you're [mother]'s youngest daughter? That's a nice surprise!"
            scene date 1pm ntr07
            ls "And mom doesn't want us to know each other?"
            davide "Yes, but I don't know why..."
            pov "Oh, I could tell you, haha."
            ls "So, you're a bad guy?"
            davide "Wanna find out?"
            ls "<giggle>"
            scene date 1pm ntr08
            if inc == True:
                ls "Well a friend of my big brother is a friend of mine."
            else:
                ls "Well a friend of [pov] is a friend of mine."
            davide "Nice to meet you too, beautiful."
            if inc == True:
                davide "But I don't even know your name still."
                ls "Oh, I'm [ls]."
            ls "Nice to meet you too. <giggle>"
            if lsisproninterracial > 4:
                pov "Yeah and I'm sure she has some special interest in you, mainly about your skincolor."
                davide "Because I'm black?"
                pov "Hahaha, oh yes!"
                scene date 1pm ntr09fetish
                if inc == True:
                    ls "Brother!"
                else:
                    ls "[pov]!"
                ls "You can't tell him about that!"
                pov "Why? You love to watch interracial porn, why would that be bad to tell a black man about it, haha?"
                ls "But...!"
                pov "Don't worry. Adults like to share things like that and it's nothing to be ashamed about."
                ls "But..."
                scene date 1pm ntr010f
                if inc == True:
                    davide "Your big brother is right."
                else:
                    davide "[pov] is right."
                davide "Lots of girls fantasize about that, so there is nothing bad about it."
                davide "And it doesn't hurt to start a new friendship out honestly."
                ls "Hnn..."
                pov "No need to be embarrassed [ls]. We won't judge you!"
                davide "He's right. There is no need to be sad."
                scene date 1pm ntr011f
                davide "Besides I wouldn't mind giving you some personal experience with that particular fantasy."
                davide "That way porn won't be your only source for that fantasy."
                ls "Hnn..."
                davide "I see you like that idea, right? It'll be much fun for both of us!"
                povi "Well he certianly isn't wasting anytime, haha."
                scene date 1pm ntr012f
                davide "I see what you did there bro! Letting me meet her after her mom tryed to prevent it."
                pov "Yes, because you're a good guy?"
                davide "Hahaha, I need to go now, we'll talk about it later."
                povi "Good, maybe I can join the gang now faster."
                scene date 1pm ntr08d
                ls "That was nice to meet him finally."
                pov "I see that, haha."
                ls "Shall we continue?"
                pov "Continue?"
                ls "You need to find me, this doesn't count."
                pov "Ok. Hide, but I'll find you anyway."
                ls "Then give it your best, dummy!"
                $ davidemeetint = True
                $ davidemeet = True
                $ d1rantrdavidey = True
                scene date 1pm 003g
                call screen adate1way4
            else:
                davide "I would love to meet with you more often."
                ls "I don't know, maybe. <giggle>"
                scene date 1pm ntr09
                davide "I see what you did there bro! Letting me meet her even when her mom tried to prevent it."
                pov "Yes, because you're such a \"good\" guy?"
                davide "Hahaha, I need to go now, we'll talk about it later."
                povi "Good, maybe I can join the gang faster now."
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
                scene date 1pm 003g
                call screen adate1way4
        else: #----- ntr path -----
            povi "Crap, she looks interested. Maybe I can interupt them and get her away from Davide."
            scene date 1pm ntr04
            pov "Hey there!"
            ls "Oh...?"
            davide "Huh?"
            if inc == True:
                ls "Big brother?"
            else:
                ls "[pov]?"
            davide "Wait, she's here with you? I'm sorry bro, I didn't mean to step up on your business."
            scene date 1pm ntr05
            pov "What are you doing here?"
            davide "I had an arguement with Jeremy. He's convinced that he owns horses and they're here."
            davide "So I came by to take a photo and show him that he's wrong."
            pov "I see...."
            davide "Yes, haha."
            povi "Damn it, she seems to want me to introduce her to him..."
            scene date 1pm ntr06

            if inc == True:
                pov "Lil sis, this is Davide, a \"friend\" of mom and dad."
            else:
                pov "[ls], this is Davide, a friend of [mother] and Bruce."
            pov "He gives me some work from time to time."
            ls "Oh? From your meetings at night, the one's I'm not allowed to go to?"
            pov "Yes, that's right."
            ls "So that's the reason I haven't meet him before?"
            pov "Yup."
            if inc == True:
                davide "So you're [pov]'s little sister? That's a nice surprise!"
            else:
                davide "So you're [mother]'s youngest daughter? That's a nice surprise!"
            povi "Yeah, real nice... god damn it. I hate this guy."
            scene date 1pm ntr07
            ls "And mom doesn't want us to know each other?"
            davide "Yes, but I don't know why..."
            povi "Oh, I could tell you..."
            ls "So, you're a bad guy?"
            davide "Wanna find out?"
            ls "<giggle>"
            povi "Seriously, what am I supposed to do now? I can't run Davide off, he's kick my ass."
            scene date 1pm ntr08
            if inc == True:
                ls "Well a friend of my big brother is a friend of mine."
            else:
                ls "Well a friend of [pov] is a friend of mine."
            pov "I never said he was a..."
            davide "Nice to meet you too, beautiful."
            if inc == True:
                davide "But I don't even know your name still."
                ls "Oh, I'm [ls]."
            ls "Nice to meet you too. <giggle>"
            if lsisproninterracial > 4:
                pov "Yeah and I'm sure she has some special interest in you too, mainly about your skincolor."
                davide "Because I'm black?"
                povi "Fuck! Did I just say that out loud?"
                scene date 1pm ntr09fetish
                if inc == True:
                    ls "Brother!"
                else:
                    ls "[pov]!"
                ls "You can't tell him about that!"
                povi "Believe me I didn't mean to!"
                povi "Shes love to watch interracial porn, so why wouldn't I want to tell the big black man that lears around the house about that?"
                povi "I'm so fucking stupid!"
                pov "Sorry, it just sort of came out..."
                ls "But still..."
                "There is an uncomfortable pause while everyone waits for her to finish."
                ls "...it's embarrassing."
                scene date 1pm ntr010f
                if inc == True:
                    davide "Hey, I'm sure your big brother didn't mean nothing by it."
                else:
                    davide "Hey, I'm sure [pov] didn't mean nothing by it."
                davide "Lots of girls fantasize about that, so there is nothing bad about that."
                davide "And it doesn't hurt to start a new friendship out honestly."
                ls "Hnn..."
                davide "So no need to be embarrassed [ls]. I ain't gonna judge you!"
                davide "No need to be sad."
                scene date 1pm ntr011f
                davide "Besides I wouldn't mind giving you some personal experience with that particular fantasy."
                davide "That way porn won't be your only source."
                ls "Hnn..."
                davide "I see you like that idea, right? It'll be much fun for both of us!"
                povi "Well he certianly isn't wasting anytime, god damn it!."
                scene date 1pm ntr012f
                davide "I have to say, I'm surprised bro. I didn't think you'd want me to meet her. After all, [mother] certainly didn't want me to."
                pov "Well... I... I don't..."
                davide "Anyway, I need to go now, we'll talk about it later."
                if inc == True:
                    povi "Wonderful... That's everything I ever wanted. I can't wait to hear about how much you want to fuck my sister later..."
                else:
                    povi "Wonderful... That's everything I ever wanted. I can't wait to hear about how much you want to fuck her later..."
                povi "Why the hell did I open my big mouth?!?"
                scene date 1pm ntr08d
                ls "That was nice to meet him finally."
                pov "Yeah, sure..."
                ls "Shall we continue?"
                pov "Continue?"
                ls "You need to find me, this doesn't count."
                pov "Ok. Hide, but I'll find you anyway."
                ls "Then give it your best, dummy!"
                $ davidemeetint = True
                $ davidemeet = True
                $ d1rantrdavidey = True
                scene date 1pm 003g
                call screen adate1way4
            else:
                davide "I would love to meet with you more often."
                ls "I don't know, maybe. <giggle>"
                scene date 1pm ntr09
                davide "I have to say, I'm surprised bro. I didn't think you'd want me to meet her. After all, [mother] certainly didn't want me to."
                pov "Well... I... I don't..."
                davide "Anyway, I need to go now, we'll talk about it later."
                if inc == True:
                    povi "Wonderful... That's everything I ever wanted. I can't wait to hear about how much you want to fuck my sister later..."
                else:
                    povi "Wonderful... That's everything I ever wanted. I can't wait to hear about how much you want to fuck her later..."
                povi "Why the hell can't I just tell him to fuck off?!? I'm such a coward!"
                ls "See you..."
                scene date 1pm ntr08d
                ls "That was nice to meet him finally."
                pov "Yeah, sure..."
                ls "Shall we continue?"
                pov "Continue?"
                ls "You need to find me, this doesn't count."
                pov "Ok. Hide, but I'll find you anyway."
                ls "Then give it your best, dummy!"
                $ davidemeet = True
                $ d1rantrdavidey = True
                scene date 1pm 003g
                call screen adate1way4
    elif alexis_revenge == True: #----- Revenge Path -----
        scene date 1pm ntr03d
        povi "I don't really want her getting to know Davide, but if I make a big fuss about it, that will only get her more intrigued."
        povi "[ls] looks shy, I wonder what she'll do?"
        scene date 1pm ntr04d
        povi "Does she realize he's an asshole?"
        povi "Too bad I can't hear them. But I don't want him to know my relationship with her."
        scene date 1pm ntr05d
        povi "She seems like she's being nice to him. I wonder if I should warn her about what a prick he is?"
        povi "But she also could get mad that I distrust her judgment. And I don't want to ruin the date."
        scene date 1pm ntr06d
        povi "Damn, what are they talking about?"
        scene date 1pm ntr07d
        povi "Oh, he's gone. And she seems calm, so it was probably about nothing serious."
        povi "I'll go check in on her now."
        scene date 1pm ntr08d
        pov "Make a new friend?"
        ls "Oh, that guy? No. I just met him for the first time."
        pov "And? What you think of him?"
        ls "I don't know. He seems okay, but also a little, dangerous. I don't think I like being around him."
        povi "Good, she noticed it."
        ls "But we need to continue our game now!"
        pov "Our game?"
        ls "You need to find me, this doesn't count."
        pov "Ok. Hide, but I'll find you anyway."
        ls "Then give your best, dummy!"
    else: #----- Sadist Path -----
        scene date 1pm ntr03d
        povi "[ls] looks shy, I wonder what she'll do?"
        scene date 1pm ntr04d
        povi "Does she realize who he is?"
        povi "Too bad I can't hear them."
        scene date 1pm ntr05d
        povi "She seems like she's being nice to him. I wonder if she's interested in him?"
        scene date 1pm ntr06d
        povi "Damn, what are they talking about?"
        scene date 1pm ntr07d
        povi "Oh, he's gone. And she seems calm."
        povi "I'll go check in on her now."
        scene date 1pm ntr08d
        pov "Make a new friend?"
        ls "Oh, that guy? No. I just met him for the first time."
        pov "And? What you think of him?"
        ls "I don't know. He seems okay, but also a little, dangerous. I don't think I like being around him."
        povi "Yeah, that's probably a good instinct... But then again, he does provide certain, opportunities."
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
    povi "I don't like the idea about her getting to know Davide. He needs to stay away from her!"
    povi "But she does want to be a grown up, so she should be making her own decisions."
    call screen adate1ntrint

screen adate1ntrint():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('adate1ntrint'), Jump('adate1ntrstop')) hovered tt.Action ("Interfere") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('adate1ntrint'), Jump('adate1ntrdisw')) hovered tt.Action ("Just watch") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label adate1ntrstop:
    scene date 1pm ntr03d
    povi "No. I have to help her and stop this. She doesn't know about what kind of guy he really is."
    scene date 1pm ntr04
    pov "Hey!"
    ls "Huh?"
    davide "..."
    pov "What do you think you're doing?"
    davide "What...?"
    pov "This guy is scum! You shouldn't get to know him!"
    if lilsisrelationship < 20:
        scene date 1pm ntr05ang
        ls "Are you serious?"
        pov "Wait... what...?"
        ls "You're trying to tell me what I can do and whom I can meet?"
        pov "Yes, because he's a bad person."
        ls "And you don't think that I can decide that for myself?"
        pov "I just wanted..."
        scene date 1pm ntr06ang
        ls "It was good that you came back, but I'm really sick of being parented by everyone."
        ls "Mom and Dad are annoying enough and now you're starting to do it too?"
        pov "But..."
        ls "No! I'm an adult, I can make my own decisions and I won't let you interfere."
        povi "Shit, what just happened? Did I just make things worse?"
        povi "And that asshole smiling at me!"
        scene date 1pm ntr07
        ls "Just ignore him. Sometimes he likes to be a dad too."
        davide "Haha, it's ok. You're related?"
        if inc == True:
            ls "Yes, he's my stupid big brother."
        else:
            ls "Not really. He lives with us."
        davide "So you're [mother]'s and Bruce's daughter?"
        ls "Yes, you know them?"
        povi "Shit, this is even worse. Now she's telling him everything."
        davide "Yes they're my friends too."
        scene date 1pm ntr08
        ls "Oh then it's nice to meet you. My name is [ls]."
        davide "I'm Davide. What a nice surprise to know that you are [mother]'s daughter."
        davide "We should have meet earlier!"
        ls "Haha, maybe."
        pov "No!"
        scene date 1pm ntr09ang
        ls "You just don't get it, do you?"
        pov "..."
        davide "She can make her own decisions."
        ls "I'm going home now! I don't want to spend more time with you!"
        pov "No, wait..."
        ls "No! You ruined it yourself. See you again sometime, Davide."
        davide "Bye, beautiful!"
        scene black
        "[ls] went home and Davide left too."
        "You also go home."
        $ d1rantrdavideyb = True
        if day >= 6:
            $ weekendactivities += 1
            if weekendactivities >= 3:
                jump weekendskip
            else:
                jump weekendacchoose
        else:
            jump frontdoor
    else:
        scene date 1pm ntr05no
        ls "Oh...?"
        davide "What did you just say?"
        pov "Please go back in [ls]. I'll handle this!"
        ls "O... okay! Please take care."
        scene date 1pm ntr06no
        pov "You'll stay away from her, asshole!"
        davide "You serious? Treating me like this when we're alone here?"
        davide "Maybe I should just smash your head in and then take care of your little girlfriend?"
        povi "I wasn't thinking clearly, I'm not ready to fight him yet. I need to think of how to get out this quick."
        pov "You won't touch me!"
        davide "Oh yeah, and why is that?"
        if inc == True:
            pov "Mom and dad will never forgive you. You'd put the whole gang at risk if you put the beat down on me."
            pov "Especially mom, since she's so proud of me!"
        else:
            pov "[mother] and Bruce will never forgive you. You'd put the whole gang at risk if you put the beat down on me."
            pov "Especially [mother], since she's so proud of me!"
        scene date 1pm ntr07no
        davide "Huh...?"
        pov "You know that I'm right."
        pov "Don't you think I took precautions after I met you? Davide, I've found out a lot about your gang in just a short time."
        pov "You don't hide it well. You even let me handle the drugs. Who's to say I haven't taken pictures or hidden some of the drugs someplace?"
        pov "Maybe I have trusted friends that know where all that evidence is and if something happens to me, that all goes to the police?"
        davide "No you wouldn't. I don't believe you."
        pov "You don't know me, Davide. You have no idea how far I'm willing to go to protect my family, and myself."
        pov "But I can promise you that you'll regret it if you try to get in contact with her again!"
        pov "I'm willing to play ball with your little gang, so long as you also play ball when it somes to my family."
        if inc == True:
            davide "I think you're bluffing. You're parents will get busted too."
            pov "Maybe this shit will land on mom and dad too. But they are just members of the gang. You're the big bad boss remember?"
            pov "The cops will sort it all out."
        else:
            davide "I think you're bluffing. Bruce and [mother] will get busted too."
            pov "Maybe this shit will land on [mother] and Bruce too. But they are just members of the gang. You're the big bad boss remember?"
            pov "The cops will sort it all out."
        scene date 1pm ntr08no
        davide "I'll let you live this time. But you're going to make a mistake sometime and I'll get you then."
        pov "I wouldn't bet on it!"
        davide "So you can have her for now. Enjoy your lesbian love making with your little girlfriend!"
        pov "Get out of here Davide. You lost."
        scene date 1pm 003g
        pov "Good. He's gone. I still can't believe that worked."
        pov "Now it's time to get back to [ls]."
        $ d1rantrdaviden = True
        call screen adate1way4

label adate1ntrdisw:
    scene date 1pm ntr03d
    povi "I don't really want her getting to know Davide, but if I make a big fuss about it, that will only get her more intrigued."
    povi "[ls] looks shy, I wonder what she'll do?"
    scene date 1pm ntr04d
    povi "Does she realize he's an asshole?"
    povi "Too bad I can't hear them. But I don't want him to know my relationship with her."
    scene date 1pm ntr05d
    povi "She seems like she's being nice to him. I wonder if I should warn her about what a prick he is?"
    povi "But she also could get mad that I distrust her judgment. And I don't want to ruin the date."
    scene date 1pm ntr06d
    povi "Damn, what are they talking about?"
    scene date 1pm ntr07d
    povi "Oh, he's gone. And she seems calm, so it was probably about nothing serious."
    povi "I'll go check in on her now."
    scene date 1pm ntr08d
    pov "Make a new friend?"
    ls "Oh, that guy? No. I just met him for the first time."
    pov "And? What you think of him?"
    ls "I don't know. He seems okay, but also a little, dangerous. I don't think I like being around him."
    povi "Good, she noticed it."
    ls "But we need to continue our game now!"
    pov "Our game?"
    ls "You need to find me, this doesn't count."
    pov "Ok. Hide, but I'll find you anyway."
    ls "Then give it your best, dummy!"
    $ davidemeet = True
    $ d1rantrdavidey = True
    scene date 1pm 003g
    call screen adate1way4

label adate1eat:
    scene black
    "You set up your picnic and eat with [ls]."
    jump adate1search

#----- Alexis Second Date (Love) -----
label alexisweekendlove:
    hide screen townl
    hide screen locations
    $ lilsislove += 1
    "[ls] called you and wants to meet. She told you it's urgent."
    scene weekend 01pm 040l
    "You meet [ls] at the barn."
    ls "You came [pov]! Quick, follow me."
    povi "She's acting so weird. What's going on?"
    ls "Come, I won't bite. <giggle>"
    scene weekend 01pm 041l
    ls "What are you afraid of?"
    if inc == True:
        ls "Come closer, brother."
    else:
        ls "Come closer, [pov]."
    povi "Damn, is she teasing me? But why?"
    scene weekend 01pm 042l
    ls "I want to show you something real special today."
    ls "And I'm sure you'll love it. I hope so at least. Please say you'll love it."
    if inc == True:
        pov "Woah! Calm down, lil sis!"
    else:
        pov "Woah! Calm down, [ls]!"
    pov "Are you on drugs or something? You're acting crazy!"
    ls "I... I want to show you something, it's important!"
    pov "Okay okay! Haha. I'm sure I love any surprise you have for me."
    ls "You better!. <giggle>"
    povi "I have to admit, her excitement is contagious!"
    pov "So what now? Are you ready to show me?"
    scene weekend 01pm 043l
    ls "ALmost! Sit over there and close your eyes!"
    pov "Ok..."
    ls "And no peeking or I'll have to hurt you! <giggle>"
    pov "Oh...?"
    ls "I know you. You'll peek if I don't threaten violence!"
    "You sit down obediently."
    scene weekend 01pm 044l
    pov "Can you give me a hint? How long will I need to sit here with my eyes closed?"
    ls "Until I tell you to it's safe to look."
    pov "Safe? What are you going to do?!?"
    ls "You'll see, just wait."
    povi "She's eager to show me whatever it is. Might as well tease her a little while I wait."
    pov "Is it something to eat?"
    ls "Nope."
    pov "Is it something to wear?"
    ls "No."
    pov "Is it... A Brand New Car?"
    povi "That was a pretty good anouncer's voice if I do say so myself."
    ls "Hmph! Ha ha ha! Nooooo!"
    if inc == True:
        ls "Stop guessing, you'll see soon enough, brother! <giggle>"
    else:
        ls "Stop guessing, you'll see soon enough, [pov]! <giggle>"
    pov "OK. OK. I'll wait."
    scene black
    "You close your eyes."
    "You hear rustling in front of you."
    povi "What is she doing? Maybe just a little peek?"
    ls "No peeking!"
    povi "Damn, she really does know me."
    ls "Alright, open your eyes now!"
    scene weekend 01pm 045l
    pov "Wow..."
    ls "Muah! <kiss>"
    scene weekend 01pm 046l
    "She pushes you back and lays herself on top of you. Kissing you passionately."
    ls "Hmm... <french kiss>"
    povi "Well hot damn! She's really into this. I can feel her pelvis grinding against my abs."
    "You two continue to make out for a while."
    povi "So was making out with me the big surprise? She was right at least. I really do love it."
    scene weekend 01pm 047l
    if inc == True:
        ls "So do you like my surprise, brother?"
    else:
        ls "So do you like my surprise, [pov]?"
    povi "She seems nervous. I wonder why? Was she really afraid I wouldn't like it?"
    pov "Yes, I love it! A beautiful naked woman wanting to make out with me? That's never a bad thing!"
    povi "She's covering herself up still. Seems a little late to worry about modesty."
    ls "I can see where you staring, buster. <giggle>"
    scene weekend 01pm 048l
    ls "Here, you can take a better look now."
    povi "She asking me to check her naked body out now? This keeps getting better and better."
    scene weekend 01pm 049l
    povi "So tight. And beautiful, untouched."
    scene weekend 01pm 050l
    ls "Hnng..."
    povi "Her pose is a bit exaggerated. Like a pornstar's pose. But she still looks so innocent and cute."
    if inc == True:
        pov "Your pussy is so beautiful, lil sis."
    else:
        pov "Your pussy is so beautiful, [ls]."
    ls "Why don't you come closer and get an even better look."
    povi "What is she up to now? Well I'm game either way!"
    pov "Of course [ls]."
    scene weekend 01pm 051l
    if inc == True:
        pov "Hey there, beautiful sister of mine."
    else:
        pov "Hey there, beautiful."
    ls "<giggle> You know what your surprise is?"
    pov "Making out with my beautiful girlfriend?"
    ls "I can be your girlfriend?"
    povi "She's shaking with exictement. Does the idea of being my girlfriend make her that happy?"
    pov "Of course, I wouldn't want anyone else to be my girlfriend!"
    ls "<giggle> Well, then it's settled. I'm all your now! My dearest boyfriend."
    ls "So... how about you give your girlfriend something to stare at too? <giggle>"
    povi "Shit! Did she really say that? I like it when she takes charge!"
    scene weekend 01pm 052l
    "You undress in seconds."
    pov "So was making out with me the surprise?"
    ls "Well yes, that was part of it. I did want to make out with my boyfriend..."
    povi "But why is she so eager to make out with me right now. And why is she posing naked for me too?"
    pov "So did something happen to inspire this impromptu make out session?"
    ls "<giggle>"
    povi "She's nervous."
    pov "So what happened? Come on, you tell me.I am your boyfriend now right?"
    scene weekend 01pm 053l
    ls "Well... ok. When I was at my friends house she told me about her new boyfriend."
    pov "And...?"
    ls "And she described you! I was so confused and angry even. I was worried were getting bored with me."
    pov "But I don't even know her!"
    ls "You promise? I just need to know you're not sick of me already."
    povi "This is so cute. She wants me all for herself."
    pov "I promise. Besides, I can't be her boyfriend, because I'm already yours!"
    ls "Hmm..."
    pov "I'll prove it to you..."
    scene weekend 01pm 054l
    povi "She's like a siren, beckoning me forward with her open legs. Inviting me to taste her. Possess her."
    "You climb over her so you can look into her eyes."
    scene weekend 01pm 060lroot
    pov "You're mine and I'm yours, sweetie."
    ls "<giggle> I can feel your penis poking me."
    pov "So what do you crave [ls]? How can I please you best?"
    ls "Maybe, if you want... DO you want to be my fisrt? <giggle>"
    pov "Are you sure? I would be honored to share that will you, but only if that's what you really want."
    ls "Well it should be with someone I really love... And really really love my boyfriend. <giggle>"
    povi "Wow... She's inviting me to be her first. I can't believe it! But should I do it now? Or maybe wait?"
    povi "Let's see..."
    jump barnsex

label barnsex:
    scene weekend 01pm 060lroot
    call screen barnsexchoose

screen barnsexchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('barnsexchoose'), Jump('barnsexhead')) hovered tt.Action ("Choose her head") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" action (Hide('barnsexchoose'), Jump('barnsexboobs')) hovered tt.Action ("Kiss her boobs") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('barnsexchoose'), Jump('barnsexhands')) hovered tt.Action ("Ask for a handjob") focus_mask True
        imagebutton auto "gui/icons/icon_belly_%s.png" action (Hide('barnsexchoose'), Jump('barnsexbelly')) hovered tt.Action ("Kiss her belly") focus_mask True
        imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('barnsexchoose'), Jump('barnsexpussy')) hovered tt.Action ("Choose her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('barnsexchoose'), Jump('barnsexfeet')) hovered tt.Action ("Choose her feet") focus_mask True
        imagebutton auto "gui/icons/icon_69_%s.png" action (Hide('barnsexchoose'), Jump('barnsex69')) hovered tt.Action ("Change position to 69") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('barnsexchoose'), Jump('barnsexstop')) hovered tt.Action ("Finish") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label barnsexhead:
    call screen barnsexheadchoose

screen barnsexheadchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('barnsexheadchoose'), Jump('barnsexheadkiss')) hovered tt.Action ("Kiss her") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('barnsexheadchoose'), Jump('barnsexheadblowjob')) hovered tt.Action ("Ask for a blowjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label barnsexheadkiss:
    pov "I need you to kiss me now!"
    ls "Oh [pov]. <giggle>"
    scene weekend 01pm 055la
    pov "<french kiss>"
    "[ls] open's her mouth and darts her tongue into [pov]'s mouth as they kiss. Their tongues wrestle together as they kiss wetly."
    ls "<lick> <kiss> Hmm..."
    scene weekend 01pm 055lb
    pov "Hmm..."
    povi "I really need to blow her mind. I want to make this something she will never forget."
    ls "Hmm... hmm..."
    scene weekend 01pm 056la
    ls "Hmm, lover! This is so good."
    povi "She loves those pet names. To be honest, I'm starting to enjoy them all the more when their coming from her lips."
    pov "I love feel of your soft skin against my lips, my love."
    ls "Kiss me more..."
    jump barnsex

label barnsexheadblowjob:
    pov "I need to feel that sweet mouth of yours around my shaft."
    ls "You want me to lick your penis?"
    pov "Yes, I want you to lick it, suck it and play with it as much as you want to."
    ls "<giggle> OK. Lover."
    scene weekend 01pm 100la
    povi "Her hand is so warm and soft."
    ls "It's so hard right now. Do you need your girlfriend to help you down there?"
    povi "She loves hearing that word, girlfriend."
    povi "I think she loves the idea of possessing me and being the only one allowed to use me however she wants to."
    pov "Yes, my girlfriend needs to help me or I might just die from pent up excitement!"
    ls "<giggle> Then lay down and let me take care of you, sweetie."
    scene weekend 01pm 101la
    pov "What a wonderful view!"
    ls "Well. then I better give my best."
    pov "I'm sure it will be wonderful. Just feel free to do what you want, I'll let you know if you do anything wrong."
    povi "She needs relax a bit. This is supposed to be fun for both of us. Haha."
    ls "<giggle> Don't worry, I did my research."
    pov "Research?"
    scene weekend 01pm 102la
    ls "I can use the internet too, dummy."
    pov "Oh my... were you watching porn as \"research\"?"
    ls "Haha, maybe?"
    povi "This could be amazing, or get very very strange depending on what porn she was watching!"
    scene weekend 01pm 103la
    povi "She has a strong grip. Perfect."
    pov "Yes. That's good [ls]. That's really starting to feel good."
    ls "You're so big, it's a little hard to get my hands all the way around it."
    pov "Don't worry, I'm sure it'll be perfect."
    pov "My girlfriend is pleasuring me."
    ls "You better believe it! <giggle>"
    "She eagerly leans over to brush her tongue across the tip of your penis."
    scene weekend 01pm 104lb
    ls "<lick>"
    pov "Oh... hmm..."
    pov "I've imagined this before, but seeing you here now and feeling you hold me like that... just amazing!"
    ls "<giggle> <lick>"
    povi "She's seems to be enjoying herself immensely. That's good."
    scene weekend 01pm 105lb
    ls "I want to try something else now."
    pov "Oh?"
    ls "I saw it on the internet and it seemed to really get the guy going in the video."
    pov "Now I'm curious..."
    ls "Oh and just let me know when you're getting close. I want to give my boyfriend the choice of where he cums, in mouth or on my face."
    povi "So good."
    pov "So you don't give the other boys a choice then?"
    "You give her a sly smile to let her know you're joking."
    ls "<giggle> You know what I mean, dummy."
    pov "Haha, Don't worry, I'll let you know."
    scene weekend 01pm 106lb
    ls "<lick> <suck>"
    povi "Wow, she's really working that tongue now. It feels great."
    ls "Hnng..."
    pov "Oh, yes..."
    povi "She really sucking now too. It's getting intense."
    scene weekend 01pm 107lb
    ls "<suck> <lick>"
    povi "Wow. She's trying to take me even deeper."
    ls "Hnng... <slurp>"
    povi "I'm going to cum soon, I need to decide where I want to finish. On or in her?"
    call screen barnsexheadblowjobcum

screen barnsexheadblowjobcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('barnsexheadblowjobcum'), Jump('barnsexheadblowjobinside')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('barnsexheadblowjobcum'), Jump('barnsexheadblowjoboutside')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label barnsexheadblowjobinside:
    pov "I'm getting close, sweetie."
    if inc == True:
        pov "I want to cum in your mouth, lil sis."
    else:
        pov "I want to cum in your mouth, [ls]."
    ls "Hmm..."
    pov "Oh yes, almost there..."
    ls "<suck> <suck>"
    pov "OHHH... YES!"
    "Your cum blasts into her mouth."
    pov "Hngh!!"
    with vpunch
    ls "Hnng..."
    with vpunch
    pov "Ohh..."
    with vpunch
    ls "Hnnn..."
    scene weekend 01pm 108lbi
    ls "Hmm..."
    povi "Is she...? She's holding my cum in her mouth. Is she wondering what to do with the cum now?"
    pov "That was amazing! You can spit it out now if you want."
    scene weekend 01pm 109lbi
    ls "<gulp> <gulp>"
    povi "She's swallowing it. That is so fucking hot!"
    if inc == True:
        povi "My little sister is drinking my cum."
    else:
        povi "[ls] is drinking my cum."
    scene weekend 01pm 110lbi
    ls "Hmm..."
    pov "You really swallowed my sperm..."
    ls "My boyfriend tastes good. <giggle>"
    pov "This was so damn good, sweetie. I'm glad I have a girlfriend like you."
    ls "<giggle>"
    jump barnsex

label barnsexheadblowjoboutside:
    pov "I'm getting close, sweetie."
    if inc == True:
        pov "I want to cum on your face, lil sis."
    else:
        pov "I want to cum on your face, [ls]."
    ls "Hmm..."
    pov "Oh yes, almost there..."
    ls "<suck> <suck>"
    pov "OHHH... YES!"
    with vpunch
    scene weekend 01pm 108lbo
    "You cum on her face."
    with vpunch
    ls "Hmm..."
    with vpunch
    scene weekend 01pm 109lbo
    ls "Hmm... there is so much! And its so warm..."
    if inc == True:
        povi "I came on my little sisters face."
    else:
        povi "I came on [ls]s face."
    pov "I have to say, white really suits you, haha."
    ls "As long as it comes from you. This is your privilege as my boyfriend."
    pov "This was so damn good, sweetie. I'm glad I have a girlfriend like you."
    ls "<giggle>"
    jump barnsex

label barnsexboobs:
    pov "I need to see if you breasts taste as good as they look [ls]!"
    ls "Oh [pov]. <giggle>"
    scene weekend 01pm 057la
    pov "<kiss> <suck>"
    ls "Ohh... That feels good."
    pov "Their are so soft. And I can feel your nipples are getting hard. I love sucking on them."
    ls "Please don't stop. It's so nice, hah..."
    pov "I'm glad you're enjoying it sweetie."
    "You bite her nipple gently."
    ls "Hah... hmm..."
    jump barnsex

label barnsexhands:
    pov "How about you use those soft hands of yours to help me out down there?"
    "You direct her eyes to your cock..."
    ls "You want me to stroke your penis?"
    pov "Yes, I want you to hold it, stoke it and play with it as much as you want to."
    ls "<giggle> OK. Lover."
    scene weekend 01pm 100la
    ls "It's so hard right now. Do you need your girlfriend to help you down there?"
    povi "She loves hearing that word, girlfriend."
    povi "I think she loves the idea of possessing me and being the only one allowed to use me however she wants to."
    pov "Yes, my girlfriend needs to help me or I might just die from pent up excitement!"
    ls "<giggle> Then lay down and let me take care of you, sweetie."
    scene weekend 01pm 101la
    pov "What a wonderful view!"
    ls "Well. then I better give my best."
    pov "I'm sure it will be wonderful. Just feel free to do what you want, I'll let you know if you do anything wrong."
    povi "She needs relax a bit. This is supposed to be fun for both of us. Haha."
    ls "<giggle> Don't worry, I did my research."
    pov "Research?"
    scene weekend 01pm 102la
    ls "I can use the internet too, dummy."
    pov "Oh my... were you watching porn as \"research\"?"
    ls "Haha, maybe?"
    povi "This could be amazing, or get very very strange depending on what porn she was watching!"
    scene weekend 01pm 103la
    povi "She has a strong grip. Perfect."
    pov "Yes. That's good [ls]. That's really starting to feel good."
    ls "You're so big, it's a little hard to get my hands all the way around it."
    pov "Don't worry, I'm sure it'll be perfect."
    pov "My girlfriend is pleasuring me."
    ls "You better believe it! <giggle>"
    "She grips your shaft with her other hand and starts stroking up and down quickly."
    scene weekend 01pm 104la
    pov "Wow! You're really pumping my dick hard now."
    ls "Does it feel good? I read online that this feels intense."
    pov "Ohh... it feels so good sweetie."
    povi "Like a thight and clinging pussy."
    ls "It's like strangling a worm. <giggle>"
    pov "I don't know of any worms that big, do you? It's more like a snake!"
    scene weekend 01pm 105la
    ls "So, I have a boyfriend with a big old snake, haha."
    povi "Her dirty-talk need work, but her hands sure don't. She's a natural."
    pov "Haha, OHHH..."
    if inc == True:
        pov "This feels so good, lil sis."
    else:
        pov "This feels so good, [ls]."
    pov "[ls]!"
    with vpunch
    scene weekend 01pm 106la
    pov "AAAHHH...!"
    with vpunch
    ls "Huh?"
    scene weekend 01pm 107la
    ls "I didn't know I was doing that good?"
    pov "Oh yes. As you can see."
    ls "You came so much. I'm glad I could help you."
    pov "That was perfect, sweetie!"
    jump barnsex

label barnsexbelly:
    "You lean down and gently work your kisses across her supple belly."
    ls "Oh [pov]. <giggle>"
    scene weekend 01pm 057la
    pov "<kiss>"
    ls "Ohh... It tickles."
    pov "I need to kiss every part of your body."
    ls "Please do!"
    ls "Hmm... your kisses are so gentle."
    jump barnsex

label barnsexpussy:
    call screen barnsexpussychoose

screen barnsexpussychoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('barnsexpussychoose'), Jump('barnsexpussylick')) hovered tt.Action ("Lick her pussy") focus_mask True
        if alexisvirgin == True:
            imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('barnsexpussychoose'), Jump('barnsexpussydeflower')) hovered tt.Action ("Deflower her") focus_mask True
        if alexisvirgin == False:
            imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('barnsexpussychoose'), Jump('barnsexpussyfuck')) hovered tt.Action ("Fuck her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label barnsexpussylick:
    pov "Well I think it's time for a snack!"
    ls "Snack?"
    ls "Ohhh... I hope you like it!"
    scene weekend 01pm 059la
    "You lean down and taste her wet pussy. Dragging your tongue across her folds and pressing it deep inside her."
    ls "Ahh... hah... it feels so good."
    pov "<lick> And you're already so wet."
    ls "Oh... your tongue... hah... hah..."
    povi "Damn, she's already shaking. It's only been a few minutes, I'm just getting started."
    povi "She must be getting close from the expectation and excitement from all of this."
    if inc == True:
        ls "Big brother... BROTHER!"
    else:
        ls "[pov]... [pov]!"
    "She's getting close. You suck and flick her clit directly with your tongue to bring her over the edge."
    scene weekend 01pm 060la
    ls "AAAHHH... HNNNG...!"
    with vpunch
    if inc == True:
        pov "Yes, cum for me, lil sis."
    else:
        pov "Yes, cum for me, [ls]."
    "You continue to brush her clit and labia softly with your tongue as her orgasm continues. Keeping her in ecstasy for a few minutes longer."
    ls "That was so good [pov]. You need to do that again."
    pov "I'm glad you liked it. I have to say I really enjoyed my snack too."
    ls "<giggle> You're allowed to eat me everytime you want to."
    povi "Oh, I will definitely take you up on that!"
    jump barnsex

label barnsexpussydeflower:
    pov "I can't wait any longer, my love. I need to be inside you."
    ls "I'm so excited. Will it hurt much?"
    pov "It might hurt a little at first. But I'll be gentle. Just let me know if I need to stop."
    ls "<giggle> You make me feel so safe [pov]."
    ls "I'm glad it's you that I'm giving my virginity to. Make me yours, lover."
    scene weekend 01pm 061la
    ls "I can feel your penis coming inside."
    pov "I'll do it very slowly at first, so you can get used to it's size."
    ls "Hnn... Will that big thing even fit?"
    pov "You're really wet right now. With all your juices, I'm sure I can slide in easily."
    ls "So it's good you made me so wet then. <giggle>"
    scene weekend 01pm 061lb
    pov "The tip of my dick is almost inside."
    ls "So hard and warm..."
    povi "I know she did \"research\" but she might not really know much about the process."
    pov "I'll slide in back and forward when I go deeper, you'll get even more wet naturally."
    ls "I'll give you all my juice, lover."
    scene weekend 01pm 062lb
    ls "Hnng..."
    pov "I'm going deeper now sweetie. I can feel your hymen. Can you feel it resting against something deep inside you?"
    scene weekend 01pm 063la
    ls "Hah... yes. I can feel your penis pushing against it."
    pov "I need to push hard now to break it and this is where it may hurt."
    pov "But I need to do it so you finally can become all mine."
    if inc == True:
        ls "Hnng... then do it. I want to be yours, brother."
    else:
        ls "Hnng... then do it. I want to be yours, [pov]."
    ls "Do it please!"
    scene weekend 01pm 063lb
    ls "HAAH!"
    pov "It's done. I'm your first, [ls]!"
    ls "HNNG... you're the first inside me..."
    pov "I'm going to start moving now. Get thing flowing better and hopefully it start's feeling really good soon."
    ls "Hmm..."
    "You start pumping your cock in and out at a steady pace. It doesn't take long till [ls] starts to moan and move her hips to meet your thrusts."
    scene weekend 01pm 064la
    ls "Oh yes! Fuck me, [pov]!"
    pov "Hnng... you're so tight and wet."
    image alexis_love_sex = Movie(channel="alexis_love_sex", play="images/anim/alexis_love_sex.webm")
    scene alexis_love_sex with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ls "Hah... hah... so big..."
    pov "God, your pussy gripping me like a vice."
    ls "Hah... Hnng... Ahh..."
    if inc == True:
        povi "I'm inside her. I deflowered my little sister. And she's loving it."
    else:
        povi "I'm inside her. I deflowered her. And she's loving it."
    pov "Does it feel good, [ls]?"
    ls "Yes... hah... more..."
    pov "You're so tight, I love your pussy."
    ls "And your penis is making me feel so good. Faster [pov]! Please go faster!"
    scene weekend 01pm 065la
    pov "I'll cum soon, your tight pussy is the best. You're shaking, you're close too?"
    ls "Yes, I think I am. Let's cum together!"
    scene weekend 01pm 066la
    ls "HAAAHH... HNNG..."
    with vpunch
    povi "She's shaking wildy. She must be having a really strong orgasm."
    ls "Aaaahh... I can feel it..."
    with vpunch
    scene weekend 01pm 066lb
    if inc == True:
        ls "Cum with me brother!"
    else:
        ls "Cum with me [pov]!"
    pov "I am!."
    $ alexisvirgin = False
    jump barnsexpussycumchoose

label barnsexpussycumchoose:
    call screen barnsexpussycum

screen barnsexpussycum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('barnsexpussycum'), Jump('barnsexpussyinside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('barnsexpussycum'), Jump('barnsexpussyoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label barnsexpussyinside:
    "She pulls your hips closer as you start to come. Gripping you tightly."
    "Even if you wanted to pull out, you couldn't."
    pov "I'm cumming!"
    with vpunch
    "You shoot your sperm deep inside her pussy quickly filling her tight hole to the brim."
    scene weekend 01pm 067laci
    ls "Ohhh... it's spraying inside me..."
    with vpunch
    pov "Hnng... much more is coming!"
    with vpunch
    if inc == True:
        ls "I can feel your hot sperm inside me, brother!"
    else:
        ls "I can feel your hot sperm inside me, [pov]!"
    with vpunch
    ls "It's so hot, like a fire burning inside me."
    scene weekend 01pm 068laci
    ls "Wow, it's leaking all over! It feels a little weird."
    pov "You'll get used to it, haha."
    ls "Hnng..."
    pov "I can't believe I released so much sperm inside you!"
    ls "Hm..."
    if inc == True:
        pov "I love you so much, lil sis."
    else:
        pov "I love you so much, [ls]."
    ls "Hmm..."
    if inc == True:
        ls "I love you too, big brother!"
    else:
        ls "Love you too, [pov]!"
    scene weekend 01pm 069laci
    povi "I probably should have pulled out, but it just felt so damn good! I know she isn't on pill."
    povi "I wonder if she realizes what could be happening right now?"
    povi "She didn't tell me not come inside her, or try to stop me. Does she not care if she gets pregnant?"
    $ alexisweekendinside = True
    jump barnsex

label barnsexpussyoutside:
    pov "I'm cumming!"
    with vpunch
    "You pull out just in time and spray her body with your sperm."
    scene weekend 01pm 067laco
    pov "Aaah..."
    with vpunch
    ls "I can feel it on my skin..."
    pov "Hnng... much more is coming!"
    with vpunch
    if inc == True:
        ls "I can feel your hot sperm on me, brother!"
    else:
        ls "I can feel your hot sperm on me, [pov]!"
    with vpunch
    scene weekend 01pm 068laco
    pov "Hah, hah... I needed that."
    ls "You released so much! You tried to cover me in cum! <giggle>"
    pov "Haha! Well you kwow why there was so much right?"
    ls "Hm..."
    if inc == True:
        pov "Because I love you so much, lil sis."
        ls "I love you too, big brother."
    else:
        pov "Because I love you so much, [ls]."
        ls "<giggle> I love you too, [pov]."
    jump barnsex

label barnsexpussyfuck:
    pov "I want to fuck that perfect pussy again [ls]."
    ls "Oh... then fuck me, lover."
    povi "She's is loving being my girlfriend and all the fun that comes with it. I am too."
    scene weekend 01pm 061la
    pov "Since you're not a virgin anymore, I'm going to slide in faster. You're so wet already, might as well not wait for the fun part!"
    ls "Yes, please stick it in so we can cum together [pov]!"
    povi "She loves fucking. This is so amazing."
    scene weekend 01pm 063la
    ls "Hah... your big penis is going even deeper inside me."
    pov "Yes and I can't wait to be hammering your tight pussy again."
    ls "<giggle> Then do it, lover. Fuck my pussy!"
    scene weekend 01pm 064la
    ls "Oh yes fuck me, [pov]! Fuck me!"
    with vpunch
    pov "Hnng... you're so tight and wet."
    image alexis_love_sex = Movie(channel="alexis_love_sex", play="images/anim/alexis_love_sex.webm")
    scene alexis_love_sex with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ls "Hah... hah... so big..."
    with vpunch
    pov "God, your pussy gripping me like a vice."
    with vpunch
    ls "Hah... Hnng... Ahh..."
    with vpunch
    if inc == True:
        povi "I'm inside her. I'm fucking my little sister. And she's loving it."
    else:
        povi "I'm inside her. I'm fucking her. And she's loving it."
    with vpunch
    pov "Are loving this as much as I am, [ls]?"
    ls "Yes... hah... more..."
    with vpunch
    pov "You're so tight, I love your pussy."
    ls "And your penis is making me feel so good."
    with vpunch
    scene weekend 01pm 065la
    pov "I'm going to cum soon, your tight pussy is the best. You're shaking, you're close too?"
    ls "Yes, let's cum together again!"
    scene weekend 01pm 066la
    ls "HAAAHH... HNNG..."
    with vpunch
    povi "She's shaking wildy. She must have a strong orgasm."
    ls "Aaaahh... I can feel it..."
    with vpunch
    scene weekend 01pm 066lb
    if inc == True:
        ls "Cum with me brother!"
    else:
        ls "Cum with me [pov]!"
    pov "Oh god yes!"
    jump barnsexpussycumchoose

label barnsexfeet:
    call screen barnsexfeetchoose

screen barnsexfeetchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('barnsexfeetchoose'), Jump('barnsexfeetkiss')) hovered tt.Action ("Kiss her feet") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('barnsexfeetchoose'), Jump('barnsexfeetjob')) hovered tt.Action ("Ask for a footjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label barnsexfeetkiss:
    pov "I want to kiss your feet now."
    ls "My feet?"
    pov "Come here."
    scene weekend 01pm 090l
    ls "Haha, you're sucking on my big toe."
    pov "<suck> <suck>"
    ls "It feels weird but also sort of nice..."
    scene weekend 01pm 090la
    if inc == True:
        ls "My big brother is sucking on my toe. <giggle>"
        pov "Because your feet are so cute, lil sis."
    else:
        ls "[pov] is sucking on my toe. <giggle>"
        pov "Because your feet are so cute, [ls]."
    scene weekend 01pm 090lb
    pov "Hmm... <suck>"
    ls "It's starting to feel good, your warm tongue licking me like that. <giggle>"
    pov "Hmm..."
    ls "So do I need to lick your feet too?"
    scene weekend 01pm 091l
    pov "<lick> Not today. Your feet are on the table."
    ls "Haha, it tickles a bit, but it's feeling better."
    pov "I love your cute feet, [ls]."
    ls "And I love your warm tongue, [pov]."
    scene weekend 01pm 092la
    ls "You can lick my feet anytime you want, slave."
    pov "What...?"
    ls "<giggle>"
    povi "Look's who is feeling more confident now. That's great."
    scene weekend 01pm 091lb
    pov "But I can't stop. You're cute feet are making me horny."
    ls "So you'll get a boner everytime you see them naked?"
    pov "Oh yes. Hide your feet or they're getting licked!"
    ls "Hahaha..."
    jump barnsex

label barnsexfeetjob:
    pov "I want you to use your feet to with my dick."
    ls "You want me to stroke your penis with my feet?"
    pov "Yes, stroke it or play with it as much you want. It feels very nice for me."
    ls "<giggle> OK. I can try, lover."
    scene weekend 01pm 092
    pov "Ohh, your cute feet are touching me."
    ls "Huh? And I'm going to be able to get you off with my feet?"
    pov "Of course."
    scene weekend 01pm 092lb
    pov "That's good, now start rubbing it up and down to help me cum."
    ls "Rubbing on your penis?"
    pov "Like you'd do it with your hands. It's not as easy but you can do it."
    scene weekend 01pm 093l
    ls "Like I would do with my hands? I'll try it then."
    pov "Oh yes, like that. Very good. You're very talented."
    scene weekend 01pm 093la
    ls "I need the practice in case I ever lose my arms and you need to get off. <giggle>"
    pov "Haha! Sounds like you are liking this new experience as much as I am."
    ls "When my cute feet can do this for you..."
    scene weekend 01pm 093lb
    povi "This view is so wonderful. Seeing her cute little feet trying to get me off."
    ls "Your penis is pulsating so much. It loves my feet. <giggle>"
    ls "Let me try more."
    scene weekend 01pm 094l
    ls "Now this is more like how I would do it with my hands."
    pov "Yes, stroking my dick like that... perfect."
    ls "I didn't know I could please you this way."
    pov "So this didn't come up in your \"research\" then?"
    ls "<giggle> No! I didn't even think of it!"
    pov "Well it feels amazing!"
    scene weekend 01pm 094lb
    ls "Good, then I'm going to help you enjoy it even more, lover."
    pov "I can't stop staring! I could watch you do this forever, but..."
    ls "My feet are feeling to good. <giggle>"
    scene weekend 01pm 094la
    pov "I'm going cum soon and I want to cum on your feet."
    ls "Haha, to reward them for their hard work?"
    if inc == True:
        pov "You know exactly what's on my mind, lil sis!"
    else:
        pov "You know exactly what's on my mind, [ls]!"
    ls "Maybe my feet should be your girlfriends then. <giggle>"
    scene weekend 01pm 095l
    povi "She really getting into this! Who knew?"
    pov "Hold them there right there. I'm almost ready."
    ls "They're waiting for their reward. <giggle>"
    scene weekend 01pm 096l
    pov "OHHH... YES!"
    with vpunch
    ls "So much is coming out..."
    pov "This will become a masterpiece."
    with vpunch
    ls "Hahaha..."
    scene weekend 01pm 097lb
    pov "That was fantastic! You did a very good job pleasuring me."
    ls "I wanted to give my best for my boyfriend."
    pov "And you really did. I'm glad."
    scene weekend 01pm 095la
    pov "And it's a pleasant surprise that you had so much fun too."
    ls "It's only fun when it's with you."
    pov "Was that a sweet profession of love?"
    ls "Maybe. <giggle>"
    jump barnsex

label barnsex69:
    pov "Have you heard of 69?"
    ls "Haha, yes. You want to do that with me?"
    pov "You bet I do. That way we can both have some fun!"
    scene weekend 01pm 080l
    pov "Oh, you already know what to do I see, haha."
    ls "<suck> Hmm... <giggle>"
    if inc == True:
        pov "Your pussy tastes so good, lil sis."
    else:
        pov "Your pussy tastes so good, [ls]."
    ls "Hnng..."
    scene weekend 01pm 081l
    pov "<lick> Do you want to play a game?"
    ls "Hmm?"
    pov "Whoever cums first lose the game, haha."
    ls "Hm... hm..."
    pov "I think I have a head start though, you're already very wet."
    ls "Hnng..."
    scene weekend 01pm 082l
    pov "HAH... you cheater, haha."
    ls "<giggle> You're gonna lose. <lick>"
    povi "She's doing really good. Squeezing my balls too. Really either way, I win!."
    pov "Hnng... hah..."
    scene weekend 01pm 083l
    pov "<lick> <bite>"
    ls "Hnng... hah... hah..."
    povi "Damn, I'm trying my best, but she's doing too good. I could cum any moment now."
    pov "I... you're winning... I'm about to cum, hah..."
    ls "Your consolation prize is that you can decide where you want to cum."
    povi "Did she really just say that? This is so hot... Hnng..."
    call screen barnsex69cum

screen barnsex69cum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('barnsex69cum'), Jump('barnsex69inside')) hovered tt.Action ("In her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('barnsex69cum'), Jump('barnsex69outside')) hovered tt.Action ("On her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label barnsex69inside:
    pov "I want to cum in your mouth, sweetie!"
    ls "OK. Tell me when your..."
    scene weekend 01pm 087la
    with vpunch
    pov "HNNNG... AAHHH..."
    with vpunch
    ls "Huh...?"
    pov "I'm cumming, sweetie!"
    with vpunch
    scene weekend 01pm 087lb
    ls "Hnng... <gulp> <gulp>"
    povi "Wow. She's swallowing my sperm. Time to let her also cum."
    scene weekend 01pm 085l
    "You furiously lick her."
    ls "Hnng... hah..."
    if inc == True:
        ls "I... AHHH... HAH... brother!"
    else:
        ls "I... AHHH... HAH... [pov]!"
    with vpunch
    pov "Enjoy your orgasm, [ls]."
    with vpunch
    ls "Hah... hah..."
    with vpunch
    scene weekend 01pm 086lb
    ls "I really loved that game. <giggle>"
    pov "Oh yes, I did too."
    jump barnsex

label barnsex69outside:
    pov "I want to cum on your face, sweetie!"
    ls "OK. Tell me when your..."
    scene weekend 01pm 084l
    with vpunch
    pov "HNNNG... AAHHH..."
    with vpunch
    ls "Huh...?"
    pov "I'm cumming, sweetie!"
    with vpunch
    scene weekend 01pm 085l
    "You furiously lick her."
    ls "Hnng... hah..."
    if inc == True:
        ls "I... AHHH... HAH... brother!"
    else:
        ls "I... AHHH... HAH... [pov]!"
    with vpunch
    pov "Enjoy your orgasm, [ls]."
    with vpunch
    ls "Hah... hah..."
    with vpunch
    scene weekend 01pm 086l
    if inc == True:
        ls "You came so much, brother."
    else:
        ls "You came so much, [pov]."
    ls "But I really loved that game. <giggle>"
    pov "Oh yes, I did too."
    jump barnsex

label barnsexstop:
    pov "OK. I think I have to call it quits! I'm all spent."
    ls "Oh nuts... Ok, lover."
    pov "Let's lay here in the hay a while and relax."
    if alexisweekendinside == True:
        scene weekend 01pm 070laci
        pov "You're being awfully quiet, is something wrong?"
        ls "I was just thinking. I mean you came inside me!"
        pov "Yes I did."
        ls "You know I'm not on the pill right? What if I get pregnant..."
        pov "Oh..."
        if inc == True:
            ls "Mom will kill us when she finds out that we made a baby together."
        else:
            ls "My mom will kill us when she finds out that we made a baby together."
        povi "Wow. She didn't seem to be complaining about the possibility of becoming pregnant, only about what would happen when someone else found out."
        povi "Does she want to have a baby with me?"
        call screen barnsexpregnant
    else:
        scene weekend 01pm 070laco
        ls "That was so much fun!"
        pov "I'm glad you liked it too. I can't wait for next time."
        ls "I can't either! We need to do this again."
        jump barnsexend

screen barnsexpregnant():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('barnsexpregnant'), Jump('barnsexpregnantyes')) hovered tt.Action ("I want a baby with her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('barnsexpregnant'), Jump('barnsexpregnantno')) hovered tt.Action ("I don't want a baby with her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label barnsexpregnantyes:
    if inc == True:
        pov "We'll deal later with mom."
        ls "Huh?"
        pov "I'd love it is we had a baby together, lil sis."
        ls "Even though we're siblings..."
    else:
        pov "We'll deal later with your mom."
        ls "Huh?"
        pov "I'd love it is we had a baby together, [ls]."
        ls "But we know each other all our lives..."
    pov "True, but we're also a couple now. And couples have babies!"
    ls "Hmm..."
    povi "Was that her agreeing with me or just trying not to let me down. Maybe she needs some time to think about it."
    $ alexisbabywant = True
    jump barnsexend

label barnsexpregnantno:
    pov "I don't think that will a problem."
    pov "I wasn't intentionally trying to get you pregnant, I just made a mistake."
    ls "So I can take a morning-after pill."
    pov "Yeah that's a good idea. You're too young to get pregnant."
    ls "Hmm..."
    povi "Is it just me, or did she sound... disappointed?"
    jump barnsexend

label barnsexend:
    scene weekend 01pm 071l
    $ alexisweekendinside = False
    ls "Let's cuddle a while."
    pov "With pleasure."
    if inc == True:
        pov "I love you, lil sis."
        ls "I love you too, big brother."
    else:
        pov "I love you, [ls]."
        ls "I love you too, [pov]."
    scene black
    "After a while you two get up to leave. [ls] heads back to her friend's house, while you go home."
    $ weekendactivities += 1
    $ alexisweekendsecond = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

#---- Custom Corruption Version of Alexis Love Date 2 -----
label coralexisweekendlove:
    hide screen townl
    hide screen locations
    $ lilsislove += 1
    "[ls] called you and wants to meet. She told you it's urgent."
    scene weekend 01pm 040l
    "You meet [ls] at the barn."
    ls "It's about time [pov]! Quick, follow me."
    povi "She's acting so weird. What's going on?"
    ls "Come, I won't bite. <giggle>"
    scene weekend 01pm 041l
    ls "What are you afraid of?"
    if inc == True:
        ls "Come closer, brother."
    else:
        ls "Come closer, [pov]."
    povi "Damn, is she teasing me? But why?"
    scene weekend 01pm 042l
    ls "I need something really bad from you today."
    ls "And I'm sure you'll love it. At least you better!"
    if inc == True:
        pov "Woah! Calm yo tits, lil sis!"
    else:
        pov "Woah! Calm yo tits, [ls]!"
    pov "Are you on drugs or something? You're acting crazy!"
    ls "I wish! But no I'm not on any drugs. Now will you focus?! It's important!"
    pov "Okay okay! What do you need from me anyway?"
    ls "You'll see soon enough!. <giggle>"
    povi "I have to admit, her excitement is getting me worked up a bit!"
    pov "So what now?"
    scene weekend 01pm 043l
    ls "Sit your ass over there and close your eyes!"
    pov "Ok..."
    ls "And no peeking or I'll have to beat you! <giggle>"
    pov "Oh...?"
    ls "I know you. You'll peek if I don't threaten violence!"
    "You sit down obediently."
    scene weekend 01pm 044l
    pov "Can you give me a hint at least? How long will I need to sit here with my eyes closed?"
    ls "Until I tell you to it's safe to look."
    pov "Safe? What are you going to do?!?"
    ls "You'll see, just wait."
    povi "She's eager to show me whatever it is. Might as well tease her a little while I wait."
    pov "Is it something to eat?"
    ls "Nope."
    pov "Is it something to wear?"
    ls "No."
    pov "Is it... A Brand New Car?"
    povi "That was a pretty good anouncer's voice if I do say so myself."
    ls "What the hell? No!"
    if inc == True:
        ls "Stop guessing, you'll see soon enough, brother! <giggle>"
    else:
        ls "Stop guessing, you'll see soon enough, [pov]! <giggle>"
    pov "OK. OK. I'll wait."
    scene black
    "You close your eyes."
    "You hear rustling in front of you."
    povi "What is she doing? Maybe just a little peek?"
    ls "No peeking!"
    povi "Damn, she really does know me."
    ls "Alright, open your eyes now!"
    scene weekend 01pm 045l
    pov "Wow..."
    ls "Muah! <kiss>"
    scene weekend 01pm 046l
    "She pushes you back and lays herself on top of you. Kissing you furiously."
    ls "Hmm... <french kiss>"
    povi "Well hot damn! She's really into this. I can feel her pelvis grinding against my abs."
    "You two continue to make out for a while."
    povi "So was making out with me what she needed me to do? Cause I'm happy to do that with her anytime she wants me to."
    scene weekend 01pm 047l
    if inc == True:
        ls "So do you like what you see, brother?"
    else:
        ls "So do you like what you see, [pov]?"
    povi "She seems different. I wonder why? Kind of like a bitch in heat."
    pov "Yes, I do! A beautiful naked woman wanting to make out with me? That's never a bad thing!"
    povi "She's covering herself up still. Seems a little late to worry about modesty."
    ls "I can see where you staring, pervert. <giggle>"
    scene weekend 01pm 048l
    ls "Here, you can take a better look now."
    povi "She's asking me to check out her naked body now? This keeps getting better and better."
    scene weekend 01pm 049l
    povi "So tight. And beautiful, untouched."
    scene weekend 01pm 050l
    ls "Hnng..."
    povi "Her pose is a bit exaggerated. Like a pornstar's pose. I wonder if that's what's she going for."
    if inc == True:
        pov "Your pussy looks amazing, lil sis."
    else:
        pov "Your pussy looks amazing, [ls]."
    ls "Why don't you come closer and get an even better look."
    povi "What is she up to now? Well I'm game either way!"
    pov "Of course [ls]."
    scene weekend 01pm 051l
    if inc == True:
        pov "Is this what you had in mind? Sister of mine."
    else:
        pov "Is this what you had in mind?"
    ls "<giggle> I know what I want, but the question is, what do you want from me?"
    pov "Well that depends what you're offering..."
    ls "What if I said anything goes, tiger?"
    povi "God damn! She's just full of surprises today! She's practically shaking with exictement."
    pov "Well, in that case, I want it all. I want to make you my personal slave!"
    ls "<giggle> Well, then it's settled. I'm all your now! Master."
    ls "So... how about you be a gracious Master and give your slave something to stare at too? <giggle>"
    povi "Shit! Did she really say that? I like it when she takes charge!"
    scene weekend 01pm 052l
    "You undress in seconds."
    pov "Now the real question is how I'm going to let my slave please me now?"
    ls "Yes Master, that is a very good question indeed. There are so many things a slave wants to do for her Master..."
    povi "I wonder what has gotten into her? She's role-playing as a sex-slave and even posing naked for me too."
    pov "So did something happen to inspire this impromptu role-play?"
    ls "<giggle>"
    povi "Now she's nervous?"
    pov "So what happened? You know a slave must obey her Master!"
    scene weekend 01pm 053l
    ls "Well... ok. When I was at my friends house she told me about her new boyfriend."
    pov "And...?"
    ls "And she described you! I was so confused and angry even. I didn't want that bitch anyhere near you!"
    pov "I don't even know her!"
    ls "You promise? I just need to know you're not sick of me already."
    povi "This is so cute. She wants me all for herself."
    pov "I promise. Besides, why would I want anyone else when I have my personal slave?"
    ls "Hmm..."
    pov "Now I think it's time for you to show your Master some appreciation..."
    scene weekend 01pm 054l
    povi "She's like a siren, beckoning me forward with her open legs. Inviting me to taste her. Possess her."
    "You climb over her so you can look into her eyes."
    scene weekend 01pm 060lroot
    pov "You're mine now, slave."
    ls "<giggle> I can feel your penis poking me."
    pov "Of course it is. I own your body now, you're going to be feeling my penis a lot from now on."
    ls "Maybe, if you want... I could feel it inside me? <giggle>"
    pov "That's exactly what I wanted to hear. My slave knows her place already. Very good."
    ls "I'm happy to serve you Master. <giggle>"
    povi "Wow... She's actually inviting me to be her first. I can't believe it! But should I do it now? Or maybe wait?"
    povi "Let's see..."
    jump corbarnsex

#----- Custom -----
label corbarnsex:
    scene weekend 01pm 060lroot
    call screen corbarnsexchoose

screen corbarnsexchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('corbarnsexchoose'), Jump('corbarnsexhead')) hovered tt.Action ("Choose her head") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" action (Hide('corbarnsexchoose'), Jump('corbarnsexboobs')) hovered tt.Action ("Kiss her boobs") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('corbarnsexchoose'), Jump('corbarnsexhands')) hovered tt.Action ("Ask for a handjob") focus_mask True
        imagebutton auto "gui/icons/icon_belly_%s.png" action (Hide('corbarnsexchoose'), Jump('corbarnsexbelly')) hovered tt.Action ("Kiss her belly") focus_mask True
        imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('corbarnsexchoose'), Jump('corbarnsexpussy')) hovered tt.Action ("Choose her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('corbarnsexchoose'), Jump('corbarnsexfeet')) hovered tt.Action ("Choose her feet") focus_mask True
        imagebutton auto "gui/icons/icon_69_%s.png" action (Hide('corbarnsexchoose'), Jump('corbarnsex69')) hovered tt.Action ("Change position to 69") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('corbarnsexchoose'), Jump('corbarnsexstop')) hovered tt.Action ("Finish") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label corbarnsexhead:
    call screen corbarnsexheadchoose

#----- Custom -----
screen corbarnsexheadchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('corbarnsexheadchoose'), Jump('corbarnsexheadkiss')) hovered tt.Action ("Kiss her") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('corbarnsexheadchoose'), Jump('corbarnsexheadblowjob')) hovered tt.Action ("Ask for a blowjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label corbarnsexheadkiss:
    pov "Kiss me now slave!"
    ls "Oh [pov]. I mean... Yes Master. <giggle>"
    scene weekend 01pm 055la
    pov "<french kiss>"
    "[ls] opens her mouth and darts her tongue into your mouth as you kiss. Your tongues wrestle together as you continue to kiss wetly."
    ls "<lick> <kiss> Hmm..."
    scene weekend 01pm 055lb
    pov "Hmm..."
    povi "I'm going to make make this something she will never forget."
    ls "Hmm... hmm..."
    scene weekend 01pm 056la
    ls "Hmm, Master! This is so good."
    povi "She loves those pet names. To be honest, I'm starting to enjoy them all the more when their coming from her lips."
    pov "I love the feeling of your soft skin against my lips, Slave."
    ls "I will continue if it pleases you..."
    pov "It does slave."
    jump corbarnsex

#----- Custom -----
label corbarnsexheadblowjob:
    pov "I need to feel that sweet mouth of yours around my shaft."
    ls "You want me to lick your penis?"
    pov "I didn't say want. I said NEED. So I expect you to lick, suck and play with cock until I tell you I'm finished."
    ls "<giggle> Yes Master."
    scene weekend 01pm 100la
    povi "Her hand is so warm and soft."
    ls "It's so hard right now. I'm so glad you are allowing me to help you Master!"
    povi "She seems to really like this role-playing."
    povi "I think she loves the idea of being possessing by me."
    pov "Yes, it's my slave's duty to help me with all this pent up excitement!"
    ls "<giggle> Then lay down and let me take care of you, Master."
    scene weekend 01pm 101la
    pov "What an amazing view!"
    ls "Only the best for my Master!"
    pov "I expect nothing less. For now, feel free to do what you want, I'll let you know if you do anything wrong."
    povi "This is supposed to be fun for both of us, right?"
    ls "<giggle> Don't worry, I did my research."
    pov "Research?"
    scene weekend 01pm 102la
    ls "I can use the internet too, you know."
    pov "Oh my... were you watching porn as \"research\"?"
    ls "Haha, maybe?"
    povi "This could be amazing, or get very very strange depending on what porn she was watching!"
    scene weekend 01pm 103la
    povi "She has a strong grip. Perfect."
    pov "Yes. That's good Slave. That's really starting to feel good."
    ls "You're so big, it's a little hard to get my hands all the way around it."
    pov "Don't worry, I'm sure you'll get used to it."
    pov "You're going to be pleasuring me a lot as my slave."
    ls "Thank you Master! <giggle>"
    "She eagerly leans over to brush her tongue across the tip of your penis."
    scene weekend 01pm 104lb
    ls "<lick>"
    pov "Oh... hmm..."
    pov "I've imagined this before, but seeing you here now and feeling you hold me like that... just fucking amazing!"
    ls "<giggle> <lick>"
    povi "She's seems to be enjoying herself immensely. That's good."
    scene weekend 01pm 105lb
    ls "I want to try something else now, Master."
    pov "Oh?"
    ls "I saw it on the internet and it seemed to really get the guy going in the video."
    pov "Now I'm curious..."
    ls "Oh and just let me know when you're getting close. I will need my Master to tell where he wants to cum, in mouth or on my face."
    povi "So good."
    pov "That's a good girl. I'm so glad you understand your place Slave."
    "She gives you a mischievous smile."
    ls "<giggle> I'm ready to begin my Master."
    pov "Well then, do your best. As if you life depends on it."
    "You give her a sly smile just to let her know you're joking... about the her life depending on it. Not about her getting started."
    scene weekend 01pm 106lb
    ls "<lick> <suck>"
    povi "Wow, she's really working that tongue now. It feels great."
    ls "Hnng..."
    pov "Oh, yes..."
    povi "She really sucking now too. It's getting intense."
    scene weekend 01pm 107lb
    ls "<suck> <lick>"
    povi "Wow. She's trying to take me even deeper."
    ls "Hnng... <slurp>"
    pov "Oh fuck, that's real good Slave!"
    povi "I'm going to cum soon, I need to decide where I want to finish. On or in her?"
    call screen corbarnsexheadblowjobcum

#----- Custom -----
screen corbarnsexheadblowjobcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('corbarnsexheadblowjobcum'), Jump('corbarnsexheadblowjobinside')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('corbarnsexheadblowjobcum'), Jump('corbarnsexheadblowjoboutside')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label corbarnsexheadblowjobinside:
    pov "I'm getting close, Slave."
    if inc == True:
        pov "I'm going to cum in your mouth, lil sis."
    else:
        pov "I'm going to cum in your mouth, [ls]."
    ls "Hmm..."
    pov "Oh yes, almost there..."
    ls "<suck> <suck>"
    pov "OHHH... YES!"
    "Your cum blasts into her mouth."
    pov "Hngh!!"
    with vpunch
    ls "Hnng..."
    with vpunch
    pov "Ohh..."
    with vpunch
    ls "Hnnn..."
    scene weekend 01pm 108lbi
    ls "Hmm..."
    povi "Is she...? She's holding my cum in her mouth. Is she wondering what to do with the cum now?"
    pov "That was amazing! I want you to swallow it now."
    scene weekend 01pm 109lbi
    ls "<gulp> <gulp>"
    povi "She's actually swallowing it. That is so fucking hot!"
    if inc == True:
        povi "My little sister is drinking my cum."
    else:
        povi "[ls] is drinking my cum."
    scene weekend 01pm 110lbi
    ls "Hmm..."
    pov "You really swallowed my sperm..."
    ls "My Master gave me an order. I must obey... <giggle>"
    pov "This was so damn good. I'm glad I have a slave like you."
    ls "<giggle>"
    jump corbarnsex

#----- Custom -----
label corbarnsexheadblowjoboutside:
    pov "I'm getting close, Slave."
    if inc == True:
        pov "I'm going to cum on your face, lil sis."
    else:
        pov "I'm going to cum on your face, [ls]."
    ls "Hmm..."
    pov "Oh yes, almost there..."
    ls "<suck> <suck>"
    pov "OHHH... YES!"
    with vpunch
    scene weekend 01pm 108lbo
    "You cum on her face."
    with vpunch
    ls "Hmm..."
    with vpunch
    scene weekend 01pm 109lbo
    ls "Hmm... there is so much! And its so warm..."
    if inc == True:
        povi "I came on my little sisters face."
    else:
        povi "I came on [ls]s face."
    pov "I have to say, white really suits you, slave."
    ls "This is your right as my master. I'll wear any color you want me to."
    pov "This was so damn good. I'm glad I have a slave like you."
    ls "<giggle>"
    jump corbarnsex

#----- Custom -----
label corbarnsexboobs:
    pov "I need to see if you breasts taste as good as they look Slave!"
    ls "Oh Master! <giggle>"
    scene weekend 01pm 057la
    pov "<kiss> <suck>"
    ls "Ohh... That feels good."
    pov "Their are so soft. And I can feel your nipples are getting hard. I love sucking on them."
    ls "Please don't stop. It's so nice, hah..."
    pov "I'm glad you're enjoying it Slave."
    "You bite her nipple for emphasis."
    ls "Hah... hmm..."
    jump corbarnsex

#----- Custom -----
label corbarnsexhands:
    pov "It's time for you use those soft hands of yours Slave."
    "You direct her eyes to your cock..."
    ls "You want me to stroke your penis Master?"
    pov "Yes, I want you to hold it, stoke it, and play with it until I tell you to stop."
    ls "<giggle> Yes Master!"
    scene weekend 01pm 100la
    ls "It's so hard right now. I'm so glad you are allowing me to help you Master!"
    povi "She seems to really like this role-playing."
    povi "I think she loves the idea of being possessing by me."
    pov "Yes, it's my slave's duty to help me with all this pent up excitement!"
    ls "<giggle> Then lay down and let me take care of you, Master."
    scene weekend 01pm 101la
    pov "What an amazing view!"
    ls "Only the best for my Master!"
    pov "I expect nothing less. For now, feel free to do what you want, I'll let you know if you do anything wrong."
    povi "This is supposed to be fun for both of us, right?"
    ls "<giggle> Don't worry, I did my research."
    pov "Research?"
    scene weekend 01pm 102la
    ls "I can use the internet too, you know."
    pov "Oh my... were you watching porn as \"research\"?"
    ls "Haha, maybe?"
    povi "This could be amazing, or get very very strange depending on what porn she was watching!"
    scene weekend 01pm 103la
    povi "She has a strong grip. Perfect."
    pov "Yes. That's good Slave. That's really starting to feel good."
    ls "You're so big, it's a little hard to get my hands all the way around it."
    pov "Don't worry, I'm sure you'll get used to it."
    pov "You're going to be pleasuring me a lot as my slave."
    ls "Thank you Master! <giggle>"
    "She grips your shaft with her other hand and starts stroking up and down quickly."
    scene weekend 01pm 104la
    pov "Wow! You're really pumping my dick hard now."
    ls "Does it feel good, Master? I read online that this feels intense."
    pov "Ohh... it feels so good slave."
    povi "Like a thight and clinging pussy."
    ls "It's like strangling a worm. <giggle>"
    pov "Don't call it that slave, you can call it a snake!"
    scene weekend 01pm 105la
    ls "Yes Master. You have a very big snake, Master."
    povi "Her dirty-talk needs work, but her hands sure don't. She's a natural."
    pov "Haha, OHHH..."
    if inc == True:
        pov "That feels so good, lil sis."
    else:
        pov "That feels so good, [ls]."
    pov "[ls]!"
    with vpunch
    scene weekend 01pm 106la
    pov "AAAHHH...!"
    with vpunch
    ls "Huh?"
    scene weekend 01pm 107la
    ls "I didn't know I was doing that good?"
    pov "Oh yes. As you can see, you've pleased your master."
    ls "You came so much. I'm glad I could help you, Master. I hope can help you much more in the future."
    pov "Oh you will!"
    jump corbarnsex

#----- Custom -----
label corbarnsexbelly:
    "You lean down and gently work your kisses across her supple belly."
    ls "Oh Master. <giggle>"
    scene weekend 01pm 057la
    pov "<kiss>"
    ls "Ohh... It tickles."
    pov "I need to inspect every part of your body."
    ls "With your lips?"
    pov "I'll use anything I want to inspect my slave."
    ls "Hmm..."
    jump corbarnsex

#----- Custom -----
label corbarnsexpussy:
    call screen corbarnsexpussychoose

#----- Custom -----
screen corbarnsexpussychoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('corbarnsexpussychoose'), Jump('corbarnsexpussylick')) hovered tt.Action ("Lick her pussy") focus_mask True
        if alexisvirgin == True:
            imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('corbarnsexpussychoose'), Jump('corbarnsexpussydeflower')) hovered tt.Action ("Deflower her") focus_mask True
        if alexisvirgin == False:
            imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('corbarnsexpussychoose'), Jump('corbarnsexpussyfuck')) hovered tt.Action ("Fuck her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label corbarnsexpussylick:
    pov "Well I think it's time for a snack, Slave!"
    ls "Snack?"
    "You look hungrily at her pussy."
    ls "Ohhh... I hope you like it Master!"
    scene weekend 01pm 059la
    "You lean down and taste her wet pussy. Dragging your tongue across her folds and pressing it deep inside her."
    ls "Ahh... hah... it feels so good."
    pov "<lick> And you're already so wet Slave. I'm please that my slave is such a slut!"
    ls "Oh... your tongue... hah... hah..."
    povi "Damn, she's already shaking. It's only been a few minutes, I'm just getting started."
    povi "She must be getting close from the expectation and excitement from all of this."
    if inc == True:
        ls "Big brother... BROTHER!"
    else:
        ls "[pov]... [pov]!"
    "She's getting close. You suck and flick her clit directly with your tongue to bring her over the edge."
    scene weekend 01pm 060la
    ls "AAAHHH... HNNNG...!"
    with vpunch
    if inc == True:
        pov "Yes, cum for me, lil sis. My personal slut!"
    else:
        pov "Yes, cum for me, [ls]. My personal slut!"
    "You continue to brush her clit and labia softly with your tongue as her orgasm continues. Keeping her in ecstasy for a few minutes longer."
    ls "That was so good. You need to do that again."
    pov "I'm glad you liked it. I have to say I really enjoyed my snack too."
    ls "<giggle> Well my Master is allowed to eat me everytime he wants to."
    povi "Oh, I will definitely take her up on that!"
    jump corbarnsex

#----- Custom -----
label corbarnsexpussydeflower:
    pov "I won't wait any longer, Slave. I need to be inside you."
    ls "I'm so excited. Will it hurt much Master?"
    pov "It might hurt a little at first. But you'll get used to it no time, then the real fun begins."
    ls "<giggle> I can't wait. I want you side me so badly."
    ls "I'm glad it's you that I'm giving my virginity to. Make my body yours forever, Master."
    scene weekend 01pm 061la
    ls "I can feel your penis coming inside."
    pov "I'm going to take me time with you. I want to enjoy every second of this."
    ls "Hnn... Will that big thing even fit?"
    pov "You're really wet right now. With all your juices, I'm sure I can slide in easily."
    ls "So it's good you made me so wet then. <giggle>"
    scene weekend 01pm 061lb
    pov "The tip of my dick is almost inside. Your pussy feels amazing."
    ls "So hard and warm..."
    povi "I wonder how much \"research\" she did for all of this. Does she know what's happening next?"
    pov "When I'm ready, I'm going to slide in deeper and deeper. Thankfully my slave is such a slut, she's already soaking wet."
    ls "I can't help it Master, I just want this so badly!"
    scene weekend 01pm 062lb
    ls "Hnng..."
    pov "I'm going deeper now slave. I can feel your hymen. Can you feel it resting against something deep inside you?"
    scene weekend 01pm 063la
    ls "Hah... yes. I can feel your penis pushing against it."
    pov "I'm going to press in deeper now. You may feel this."
    pov "But I need you to bear it so you finally can become all mine."
    if inc == True:
        ls "Hnng... then do it. I want to be yours, brother."
    else:
        ls "Hnng... then do it. I want to be yours, [pov]."
    ls "Do it please Master!"
    scene weekend 01pm 063lb
    ls "HAAH!"
    pov "It's done. I'm your first, [ls]!"
    ls "HNNG... you're the first inside me..."
    pov "I'm going to start moving now. Get things flowing better and then it's going to start feeling really good soon."
    ls "Hmm..."
    "You start pumping your cock in and out at a steady pace. It doesn't take long till [ls] starts to moan and move her hips to meet your thrusts."
    scene weekend 01pm 064la
    ls "Oh yes! Fuck me, [pov]!"
    pov "Hnng... you're so tight and wet."
    ls "Hah... hah... so big..."
    pov "God, your pussy gripping me like a vice."
    ls "Hah... Hnng... Ahh..."
    if inc == True:
        povi "I'm inside her. I deflowered my little sister. And she's loving it."
    else:
        povi "I'm inside her. I deflowered her. And she's loving it."
    pov "Does it feel good, slave?"
    ls "Yes... hah... more... fuck me Master!"
    pov "You're so tight, I love your pussy."
    ls "And your penis is making me feel so good. Faster Master! Please go faster!"
    "You start fucking in and out of her pussy harder and harder."
    scene weekend 01pm 065la
    pov "I'll cum soon, your tight pussy is the best. You're shaking, you're close too?"
    ls "Yes, I think I am. Let's cum together!"
    scene weekend 01pm 066la
    ls "HAAAHH... HNNG..."
    with vpunch
    povi "She's shaking wildy. She must be having a really strong orgasm."
    ls "Aaaahh... I can feel it..."
    with vpunch
    scene weekend 01pm 066lb
    if inc == True:
        ls "Cum with me brother!"
    else:
        ls "Cum with me [pov]!"
    pov "I am!"
    $ alexisvirgin = False
    jump corbarnsexpussycumchoose

#----- Custom -----
label corbarnsexpussycumchoose:
    call screen corbarnsexpussycum

#----- Custom -----
screen corbarnsexpussycum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('corbarnsexpussycum'), Jump('corbarnsexpussyinside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('corbarnsexpussycum'), Jump('corbarnsexpussyoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label corbarnsexpussyinside:
    "She pulls your hips closer as you start to cum. Gripping you tightly."
    "Even if you wanted to pull out, you couldn't."
    pov "I'm cumming!"
    with vpunch
    "You shoot your sperm deep inside her pussy quickly filling her tight hole to the brim."
    scene weekend 01pm 067laci
    ls "Ohhh... it's spraying inside me..."
    with vpunch
    pov "Hnng... much more is coming!"
    with vpunch
    if inc == True:
        ls "I can feel your hot sperm inside me, brother!"
    else:
        ls "I can feel your hot sperm inside me, [pov]!"
    with vpunch
    ls "It's so hot, like a fire burning inside me."
    scene weekend 01pm 068laci
    ls "Wow, it's leaking all over Master! It feels a little weird."
    pov "You'll get used to it, haha."
    ls "Hnng..."
    pov "I can't believe I released so much sperm inside you!"
    ls "Hm..."
    if inc == True:
        pov "You're such a good little slut, lil sis."
    else:
        pov "You're such a good little slut, [ls]."
    ls "Hmm..."
    if inc == True:
        ls "For you I am, big brother!"
    else:
        ls "For you I am, [pov]!"
    scene weekend 01pm 069laci
    povi "I probably should have pulled out, but it just felt so damn good! I know she isn't on pill."
    povi "I wonder if she realizes what could be happening right now?"
    povi "She didn't tell me not to cum inside her, or try to stop me. Does she not care if she gets pregnant?"
    $ alexisweekendinside = True
    jump corbarnsex

#----- Custom -----
label corbarnsexpussyoutside:
    pov "I'm cumming!"
    with vpunch
    "You pull out just in time and spray her body with your sperm."
    scene weekend 01pm 067laco
    pov "Aaah..."
    with vpunch
    ls "I can feel it on my skin..."
    pov "Hnng... much more is coming!"
    with vpunch
    if inc == True:
        ls "I can feel your hot sperm on me, brother!"
    else:
        ls "I can feel your hot sperm on me, [pov]!"
    with vpunch
    scene weekend 01pm 068laco
    pov "Hah, hah... I needed that."
    ls "You released so much! You tried to cover me in cum! <giggle>"
    pov "Haha! Well you kwow why there was so much right?"
    ls "Hm..."
    if inc == True:
        pov "Because you're such a good little slut, lil sis."
        ls "For you I am, big brother."
    else:
        pov "Because you're such a good little sluth, [ls]."
        ls "<giggle> For you I am, [pov]."
    jump corbarnsex

#----- Custom -----
label corbarnsexpussyfuck:
    pov "I want to fuck that perfect pussy again [ls]."
    ls "Oh... then fuck me, Master."
    povi "She's is loving being my personal slave and all the fun that comes with it. I am too."
    scene weekend 01pm 061la
    pov "You're not a virgin anymore, I'm going to slide in faster. You're so wet already, might as well not wait for the fun part!"
    ls "Yes, please stick it in and fuck me Master!"
    povi "She loves fucking. This is so amazing."
    scene weekend 01pm 063la
    ls "Hah... your big penis is going even deeper inside me."
    pov "Yes and I can't wait to be hammering your tight pussy again."
    ls "<giggle> Then do it, Master. Fuck my pussy!"
    scene weekend 01pm 064la
    ls "Oh yes fuck me, [pov]! Fuck me!"
    with vpunch
    pov "Hnng... you're so tight and wet."
    image alexis_love_sex = Movie(channel="alexis_love_sex", play="images/anim/alexis_love_sex.webm")
    scene alexis_love_sex with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ls "Hah... hah... so big..."
    with vpunch
    pov "God, your pussy gripping me like a vice."
    with vpunch
    ls "Hah... Hnng... Ahh..."
    with vpunch
    if inc == True:
        povi "I'm inside her. I'm fucking my little sister. And she's loving it."
    else:
        povi "I'm inside her. I'm fucking her. And she's loving it."
    with vpunch
    pov "Are loving this as much as I am, Slave?"
    ls "Yes... hah... more... please Master!"
    with vpunch
    pov "You're so tight, I love your pussy."
    ls "And your penis is making me feel so good."
    with vpunch
    scene weekend 01pm 065la
    pov "I'm going to cum soon, your tight pussy is the best. You're shaking, you're close too?"
    ls "Yes, let's cum together again!"
    scene weekend 01pm 066la
    ls "HAAAHH... HNNG..."
    with vpunch
    povi "She's shaking wildy. She must have a strong orgasm."
    ls "Aaaahh... I can feel it..."
    with vpunch
    scene weekend 01pm 066lb
    if inc == True:
        ls "Cum with me brother!"
    else:
        ls "Cum with me [pov]!"
    pov "Oh god yes!"
    jump corbarnsexpussycumchoose

#----- Custom -----
label corbarnsexfeet:
    call screen corbarnsexfeetchoose

#----- Custom -----
screen corbarnsexfeetchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('corbarnsexfeetchoose'), Jump('corbarnsexfeetkiss')) hovered tt.Action ("Kiss her feet") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('corbarnsexfeetchoose'), Jump('corbarnsexfeetjob')) hovered tt.Action ("Ask for a footjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label corbarnsexfeetkiss:
    pov "I'm going to kiss your feet now, slave."
    ls "My feet?"
    pov "Come here."
    scene weekend 01pm 090l
    ls "Haha, you're sucking on my big toe."
    pov "<suck> <suck>"
    ls "It feels weird but also sort of nice..."
    scene weekend 01pm 090la
    ls "My master is sucking on my toe. <giggle>"
    pov "Because your feet are so cute, Slave."
    scene weekend 01pm 090lb
    pov "Hmm... <suck>"
    ls "It's starting to feel good, your warm tongue licking me like that Master. <giggle>"
    pov "Hmm..."
    ls "So do I need to lick your feet too?"
    scene weekend 01pm 091l
    pov "<lick> Not today Slave. Your feet are on the table."
    ls "Haha, it tickles a bit, but it's feeling better."
    pov "I love your cute feet, Slave."
    ls "And I love your warm tongue, Master."
    scene weekend 01pm 092la
    ls "Will you lick my feet more often Master?"
    pov "If I want to."
    ls "<giggle> I hope so!"
    povi "Look's who really getting into this. That's great."
    scene weekend 01pm 091lb
    pov "I won't be stopping any time soon though. You're cute feet are making me horny Slave."
    ls "So you'll get a boner everytime you see them naked?"
    pov "Oh yes. And I expect you to keep them naked from now on!"
    ls "Hahaha... yes Master!"
    jump corbarnsex

#----- Custom -----
label corbarnsexfeetjob:
    pov "I need you to use your feet to with my dick Slave."
    ls "You want me to stroke your penis with my feet Master?"
    pov "Yes, stroke it or play with it as much you want. It will feel very nice for me."
    ls "<giggle> OK. I will try, Master."
    scene weekend 01pm 092
    pov "There, that's where you need to hold them."
    ls "Am I going to be able to get you off with just my feet?"
    pov "Of course Slave."
    scene weekend 01pm 092lb
    pov "That's good, now start rubbing it up and down to help me cum."
    ls "Rubbing on your penis?"
    pov "Like you'd do it with your hands. It's not as easy but you can do it."
    scene weekend 01pm 093l
    ls "Like I would do with my hands? Yes Master."
    pov "Oh yes, like that. Very good. You're very talented slave."
    scene weekend 01pm 093la
    ls "I need the practice in case I ever lose my arms and you need to get off. <giggle>"
    pov "Haha! Sounds like you are liking this new experience as much as I am Slave."
    ls "That's my duty Master. <giggle>"
    scene weekend 01pm 093lb
    povi "This view is so wonderful. Seeing her cute little feet trying to get me off."
    ls "Your penis is pulsating so much. <giggle>"
    ls "Let me see if I can get it to do that even more."
    scene weekend 01pm 094l
    ls "Now this is more like how I would do it with my hands."
    pov "Yes, stroking my dick like that Slave."
    ls "I didn't know I could please you this way."
    pov "So this didn't come up in your \"research\" then?"
    ls "<giggle> No! I didn't even think of it!"
    pov "Well it feels amazing!"
    scene weekend 01pm 094lb
    ls "Good, then I'm going to help you enjoy it even more, Master."
    pov "I can't stop staring! I could watch you do this forever, but..."
    ls "I can feel you getting close Master. <giggle>"
    scene weekend 01pm 094la
    pov "I want to cum on your feet."
    ls "Haha, to reward them for their hard work?"
    pov "You know exactly what's on my mind, Slave!"
    ls "Maybe my feet should be your slaves then. <giggle>"
    scene weekend 01pm 095l
    povi "She really getting into this! Who knew?"
    pov "Hold them there right there. I'm almost ready."
    ls "They're waiting for their reward Master. <giggle>"
    scene weekend 01pm 096l
    pov "OHHH... YES!"
    with vpunch
    ls "So much is coming out..."
    pov "This will become a masterpiece."
    with vpunch
    ls "Hahaha..."
    scene weekend 01pm 097lb
    pov "That was fantastic! You did a very good job pleasuring me Slave."
    ls "I wanted to give my best for my Master."
    pov "You did well."
    scene weekend 01pm 095la
    pov "And it's a pleasant surprise that you had so much fun too."
    ls "It's only fun when it's with you Master."
    pov "Was that a sweet profession of love?"
    ls "Of course it is. <giggle>"
    jump corbarnsex

#----- Custom -----
label corbarnsex69:
    pov "Have you heard of 69?"
    ls "Haha, yes. You want to do that with me Master?"
    pov "Yes I do Slave. That way we can both have some fun!"
    scene weekend 01pm 080l
    pov "Oh, you already know what to do I see. Good!"
    ls "<suck> Hmm... <giggle>"
    pov "Your pussy tastes so good, Slave."
    ls "Hnng..."
    scene weekend 01pm 081l
    pov "<lick> Do you want to play a game?"
    ls "Hmm?"
    pov "Whoever cums first lose the game, haha."
    ls "Hm... hm..."
    pov "I think I have a head start though, you're already very wet Slave."
    ls "Hnng..."
    scene weekend 01pm 082l
    pov "HAH... you cheater, haha."
    ls "<giggle> I have to try my best for Master. <lick>"
    povi "She's doing really good. Squeezing my balls too. Really either way, I win!."
    pov "Hnng... hah..."
    scene weekend 01pm 083l
    pov "<lick> <bite>"
    ls "Hnng... hah... hah..."
    povi "Damn, I'm trying my best, but she's doing too good. I could cum any moment now."
    pov "I... you're winning... I'm about to cum, hah..."
    ls "Your consolation prize is that you can decide where you want to cum Master."
    povi "Did she really just say that? This is so hot... Hnng..."
    call screen corbarnsex69cum

#----- Custom -----
screen corbarnsex69cum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('corbarnsex69cum'), Jump('corbarnsex69inside')) hovered tt.Action ("In her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('corbarnsex69cum'), Jump('corbarnsex69outside')) hovered tt.Action ("On her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label corbarnsex69inside:
    pov "I going to cum in your mouth, Slave!"
    ls "OK. Tell me when your..."
    scene weekend 01pm 087la
    with vpunch
    pov "HNNNG... AAHHH..."
    with vpunch
    ls "Huh...?"
    pov "I'm cumming!"
    with vpunch
    scene weekend 01pm 087lb
    ls "Hnng... <gulp> <gulp>"
    povi "Wow. She's swallowing my sperm. Time to let her also cum."
    scene weekend 01pm 085l
    "You furiously lick her."
    ls "Hnng... hah..."
    if inc == True:
        ls "I... AHHH... HAH... brother!"
    else:
        ls "I... AHHH... HAH... [pov]!"
    with vpunch
    pov "Enjoy your orgasm, Slave."
    with vpunch
    ls "Hah... hah..."
    with vpunch
    scene weekend 01pm 086lb
    ls "I really loved that game. <giggle>"
    pov "Oh yes, I did too."
    jump corbarnsex

#----- Custom -----
label corbarnsex69outside:
    pov "I going to cum on your face, Slave!"
    ls "OK. Tell me when your..."
    scene weekend 01pm 084l
    with vpunch
    pov "HNNNG... AAHHH..."
    with vpunch
    ls "Huh...?"
    pov "I'm cumming!"
    with vpunch
    scene weekend 01pm 085l
    "You furiously lick her."
    ls "Hnng... hah..."
    if inc == True:
        ls "I... AHHH... HAH... brother!"
    else:
        ls "I... AHHH... HAH... [pov]!"
    with vpunch
    pov "Enjoy your orgasm, Slave."
    with vpunch
    ls "Hah... hah..."
    with vpunch
    scene weekend 01pm 086l
    ls "You came so much, Master."
    ls "I really loved that game. <giggle>"
    pov "Oh yes, I did too."
    jump corbarnsex

#----- Custom -----
label corbarnsexstop:
    pov "OK. I think I have to call it quits! I'm all spent."
    ls "Oh nuts... Ok, Master <giggle>."
    pov "Let's lay here in the hay a while and relax."
    if alexisweekendinside == True:
        scene weekend 01pm 070laci
        pov "You're being awfully quiet, is something wrong?"
        ls "I was just thinking. I mean you came inside me!"
        pov "Yes I did."
        ls "You know I'm not on the pill right? What if I get pregnant..."
        pov "Oh..."
        if inc == True:
            ls "Mom will kill us when she finds out I let you fuck me and I got pregnant."
        else:
            ls "My mom will kill us when she finds out I let you fuck me and I got pregnant."
        povi "Wow. She didn't seem to be complaining about the possibility of becoming pregnant, only about what would happen when someone else found out."
        povi "Does she want to have a baby with me?"
        call screen corbarnsexpregnant
    else:
        scene weekend 01pm 070laco
        ls "That was so much fun!"
        pov "I'm glad you liked it too. I can't wait for next time."
        ls "I can't either! We need to do this again, Master."
        jump corbarnsexend

#----- Custom -----
screen corbarnsexpregnant():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('corbarnsexpregnant'), Jump('corbarnsexpregnantyes')) hovered tt.Action ("I want to have a baby with her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('corbarnsexpregnant'), Jump('corbarnsexpregnantno')) hovered tt.Action ("I don't want to have a baby with her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label corbarnsexpregnantyes:
    if inc == True:
        pov "We'll deal later with mom."
        ls "Huh?"
        pov "I kind of like the idea of knocking you up, lil sis."
        ls "Even though we're siblings..."
    else:
        pov "We'll deal later with your mom."
        ls "Huh?"
        pov "I kind of like the idea of knocking you up, [ls]."
        ls "But we know each other all our lives..."
    pov "True, but you're mine now. and I should be able to do whatever I want with you!"
    ls "Hmm..."
    povi "Was that her agreeing with me or just trying not to let me down. Maybe she needs some time to think about it."
    $ alexisbabywant = True
    jump corbarnsexend

#----- Custom -----
label corbarnsexpregnantno:
    pov "I don't think that will a problem."
    pov "I wasn't intentionally trying to knock you up, I just made a mistake."
    ls "So I can take a morning-after pill."
    pov "Yeah that's a good idea. You're too young to get pregnant."
    ls "Hmm..."
    povi "Is it just me, or did she sound... disappointed?"
    jump corbarnsexend

#----- Custom -----
label corbarnsexend:
    scene weekend 01pm 071l
    $ alexisweekendinside = False
    ls "I can't believe we did all that."
    pov "So did you like role-playing as my slave?"
    ls "Yes! It was really hot! I loved the idea of you doing whatever you wanted with me."
    if inc == True:
        pov "I love that idea too, lil sis."
        ls "I'm glad, big brother."
    else:
        pov "I love that idea too, [ls]."
        ls "I'm glad, [pov]."
    scene black
    "After a while you two get up to leave. [ls] heads back to her friend's house, while you go home."
    $ weekendactivities += 1
    $ alexisweekendsecond = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

label cdate5:
    hide screen locations
    scene black
    "*knock knock knock*"
    "You hear that knocking, forever knocking on you door... Fuck you Poe!"
    scene date 5pm 099
    pov "Oh, hi [bs]. What's up?"
    bs "I need to go to the mall and want you to come with me!"
    pov "You want to go with me to the mall?"
    bs "Yes!"
    if bigsiscorruption >= bigsislove and bigsisrelationship >= 20:
        povi "That's a little suspicious. Why would she want me to go with her?"
        "You hesitate a moment."
        bs "Mom wants me to show you the mall, so you can go shopping yourself in the future."
        povi "So that's the reason."
    if bigsislove >= bigsiscorruption and bigsisrelationship >= 20:
        povi "That's a little suspicious. Then again, she has been a little nicer to me recently."
        bs "I don't hate you. You know that right?"
        pov "Well you haven't done a great job of showing me that really."
        bs "Well, let's see what we can do about that."
    pov "Hm..."
    scene date 5pm 098
    bs "Hey! Are you going to make me wait?"
    call screen cdate5start

screen cdate5start():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('cdate5start'), Jump('cdate5yes')) hovered tt.Action ("Join her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('cdate5start'), Jump('cdate5no')) hovered tt.Action ("Don't go") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cdate5no:
    pov "No sorry, [bs] I don't have time to go right now."
    scene date 5pm 097
    bs "What?"
    pov "I'm too busy right now."
    bs "Ok, your loss."
    if day >= 6:
        jump weekendacchoose
    else:
        jump mcroom

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
    "On the way she tells you about her efforts to get famous..."
    povi "Not surprising given the \"new\" attitude..."
    "... and how far she's willing to go to get out of this place."
    povi "I wonder how much of this has to the undercover mess at home?"
    scene date 5pm 000
    bs "Come on follow me. There's something weird going on over there."
    pov "Over there?"
    bs "Yes, see the crowd? Nothing interesting ever happens here!"
    "You follow her."
    scene date 5pm 001
    bs "Seriously?"
    pov "What's wrong?"
    pov "There's a girl doing a photo-shoot and showing her tits in public. What's special about that?"
    if katefirstmeet == True:
        pov "Oh and I know her, it's [kate]."
    scene date 5pm 003
    bs "She's a whore! Everyone knows that!"
    pov "Wow, a bit hursh, don't you think?"
    bs "No! She's just playing innocent, but she's really a bitch. I hate her so much!"
    povi "Is it possible that [bs] is just jealous of her? Or is there more to the story maybe?"
    scene date 5pm 004
    "Photographer" "Let's thank her for doing such a great job. She's a real beauty!"
    "Crowd" "Yeah you did it, hottie!"
    "Man" "You're so damn hot girl!"
    "Girl" "You're so famous! I love you!"
    povi "Yep, [bs] is definitely jealous."
    scene date 5pm 005
    bs "You understand now? She's getting my fame! I'm better than she is. I should be getting the applause."
    pov "Hm..."
    povi "But she does have a nice body too. Probably best to not mention that right now though."
    bs "I'll show her! These people need to see that I'm the better star!"
    povi "Well, she's certainly obsessed with that idea."
    scene date 5pm 006
    "Photographer" "Now I need someone new for our last session."
    bs "Oh...?"
    "Photographer" "These photo-shoots have a chance to get printed in a magazine along with being featured on our website, so take a change, get famous!"
    bs "Actual print?"
    scene date 5pm 007
    bs "Take me! Here!"
    povi "Oh, this could be interesting!"
    bs "Take me, sir! I'm the perfect girl for your photo-shoot!"
    scene date 5pm 008
    "Photographer" "Hm, well. It's good to see someone so motivated!"
    "Photographer" "But where's your partner? This last shoot is a couples photo-shoot."
    povi "Oh, that could work..."
    "Photographer" "You can't do it alone."
    bs "Ok, just a second."
    if bigsisrelationship <= 5 and NTR == True:
        jump cdate5ntr
    scene date 5pm 009
    bs "Hehe..."
    povi "Hm, should I help her? This could be fun..."
    call screen cdate5help

screen cdate5help():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('cdate5help'), Jump('cdate5helpyes')) hovered tt.Action ("Help her") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('cdate5help'), Jump('cdate5helpno')) hovered tt.Action ("Don't help her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cdate5helpno:
    scene date 5pm 009
    pov "No sorry, [bs]. I don't think I could be a couples photo-shoot with you."
    scene black
    bs "What? Are you serious?"
    bs "You're being an asshole! You're going to ruin my chance at being a star."
    scene black
    "She storms off very angry."
    scene black
    "You decide to go home after this \"date\" went so bad."
    $ dtime += 1
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5helpyes:
    scene date 5pm 009
    pov "Ok, ok. I'm in."
    bs "Good decision!"
    $ bigsisrelationship += 1
    scene date 5pm 010
    bs "Follow me."
    "You follow her to the bed."
    povi "Hah, even the photographer is staring. She does look very hot in that outfit."
    povi "And I'm her follow model for this shoot. Maybe I'll get a reward after?"
    scene date 5pm 011
    bs "We can be friends long enought for this photo-shoot can't we?"
    bs "You understand how important this is for me?"
    bs "I'll be grateful if you help me, you might even get a reward."
    povi "I knew it. She is so predictable."
    bs "Just play along, ok?"
    pov "Sure thing!"
    scene date 5pm 012
    bs "I found someone who'll help me. Now we can participate!"
    "Photographer" "Good. Then get on the bed so we can start."
    bs "Ok. Thank you."
    scene date 5pm 013
    povi "Oh wow, she's so hot! This photo-shoot gives me a great chance to get closer to her."
    bs "Come on [pov]."
    pov "I'm right behind you."
    povi "And look foward to get even closer!"
    scene date 5pm 014
    "Photographer" "Good. Just lay there for a few starting shots."
    povi "I might be able to press my luck here."
    povi "she'll be worried about looking bad for the camera and probably won't react as \"violently\" as she normally does."
    "Photographer" "What's your name beautiful?"
    bs "I'm [bs]."
    "Photographer" "Let's welcome [bs]."
    "Crowd" "You can do it [bs]!"
    "Man" "You're so sexy."
    "Photographer" "And your boyfriends name?"
    if bigsislove or bigsiscorruption >=30:
        bs "You heard him babe, tell him your name."
        povi "Wow, she's not even going to correct him, nice!"
    else:
        bs "Oh he isn't my boyfriend, just a friend helping me out."
        if inc == True:
            povi "Now I'm not her brother anymore, just a \"friend\". Interesting..."
        else:
            povi "Now I'm not her childhood friend anymore, just a \"friend\". Interesting..."
        "Photographer" "Oh, ok. And your name is?"
    pov "I'm [pov]."
    "Crowd" "Nice to meet you too, [pov]."
    "Girl" "You're hot [pov]!"
    "Photographer" "So go ahead and just play the happy couple, do what you would normally do in a situation like this."
    "Photographer" "Let's start the photo shoot!"
    bs "Oh... one moment please."
    "Photographer" "Oh, ok..."
    scene date 5pm 015
    bs "<whisper> I'll need you to play along further. We'll just pretend we're boyfriend and girlfriend."
    pov "<whisper> Hm..."
    if inc == True:
        bs "<whisper> Please just do it, little brother!"
        povi "Sure why not? Pretending to be a couple with my hot older sister. What could get wrong?"
    else:
        bs "<whisper> Please just do it, [pov]!"
        povi "Sure why not? Pretending to be a couple with my hot childhood friend. What could get wrong?"
    pov "<whisper> Sure."
    bs "<whisper> Thank you."
    scene date 5pm 016
    bs "Thanks, we just needed a moment to clear some things up. We can start now."
    "Photographer" "Sounds good, just remember... you're a couple in love, so be sure to do your best to show it."
    "Photographer" "The photo's show when you're not being natural!"
    bs "Ok."
    povi "This guy is a genius!"
    "Photographer" "Good then how about you cuddle together for a start?"
    scene date 5pm 017
    "[bs] comes close to you and you hold her for the photos."
    bs "Is this good?"
    "Photographer" "Perfect!"
    "Man" "I want to cuddle with such a hot girl too!"
    povi "Yes! we're cuddling and she likes it, and the crowd seems to love her."
    "Girl" "We need to see her tits!"
    "Photographer" "Hm... the crowd is on right track. A little nudity would be good for the photos."
    scene date 5pm 018
    bs "What...?"
    "Crowd" "Do it! Do it! Do it! Get those tits out!"
    povi "I love the crowd's enthusiasm and fantastic idea. But, I wonder what [bs] will do?"
    bs "But..."
    "Photographer" "The better the photos, the more likely they are to be printed!"
    scene date 5pm 019
    povi "Wow. Did she really think she could make it better than the other girl's photo shoot without showing some skin?"
    bs "<whisper> What... should we do?"
    povi "Is she scared to show her boobs to the crowd or to me?"
    if inc == True:
        povi "Her brother."
    else:
        povi "Her childhood friend."
    pov "<whisper> I can't decide that for you."
    scene date 5pm 020
    bs "I... I..."
    povi "She's paralyzed! Unsure what she wants to do.."
    "Crowd" "Boobies! Boobies! Go [bs]!"
    povi "And the crowd just brutal. They really want to see a good show."
    povi "But maybe I can help her get more comfortable with the situation."
    scene date 5pm 021
    bs "<whisper> Huh? What are you doing?"
    pov "<whisper> I got rid of my shirt, so I'm half naked. I thought it might help you."
    bs "<whisper> How?"
    pov "<whisper> Now I'm naked too and you don't need to be so ashamed because I would be naked too."
    bs "<whisper> Are you kidding me?"
    pov "<whisper> Sorry I don't have tits to show. I could drop my pants if that's better?"
    "Girl" "Show us more, you horndog!"
    scene date 5pm 022
    bs "Hm..."
    "Another girl" "Get away from him you slut, he's mine!"
    "Man" "You're so damn hot [bs]."
    pov "<whisper> Well, it looks like the people love us and are having fun too. Might be a great chance to get some fame."
    pov "<whisper> And don't forget this was your idea."
    bs "Hnn..."
    "Photographer" "We need a decision."
    scene date 5pm 023
    bs "Ok, I'm in!"
    "Crowd" " Yes! You go girl!"
    "Man" "You're so sexy!"
    povi "Very nice."
    povi "But she's still seems embarrassed. Hopefully she can enjoy it more as we go! This is pretty exciting."
    "Photographer" "You're brave, [bs]. Now look at me for a few shots."
    scene date 5pm 024
    "Photographer" "Yes there's that sexy girl [bs]. Tease me with your smile."
    povi "What a charmer. But she seems to love the attention and that's a win for me too."
    "You get closer to her."
    "Crowd" "This is fantastic. You're so beautiful [bs]!"
    povi "Maybe it's time to help her out a little bit."
    povi "She already agreed to show them her tits, this will be just a little... nudge.!"
    scene date 5pm 025a
    bs "Huh?"
    bs "<whisper> What are you doing? Are you crazy?"
    "Crowd" "Yes! You're doing right boy!"
    pov "<whisper> I'm helping you undress. We want to give them a good show, plus we're couple right? This is normal couple stuff."
    "Girl" "They're so big. I want to suck them!"
    bs "Huh?"
    povi "She's getting goosebumps. She enjoys the compliments, I was so right."
    pov "<whisper> See, they love seeing how gorgeous your body is."
    "Photographer" "Not bad!"
    scene date 5pm 026a
    pov "<whisper> It looks like you're earning your fame now, [bs]. Look how much they adore you!"
    "Photographer" " Yes, look to me for a few shots again! You have a very photogenic body."
    pov "<whisper> See? Even the photographer agrees, you're amazing."
    bs "Hnng..."
    povi "Wow. I can feel her heartbeat through her tits. She's excited."
    if inc == True:
        povi "And what's better is she doesn's seem to mind that her brother is holding her naked tits. In public, in front of a crowd of strangers!"
    else:
        povi "And what's better is she doesn's seem to mind that I'm holding her naked tits. In public, in front of a crowd of strangers!"
    povi "This is just awesome!"
    "Photographer" "Let's hear what the crowd thinks! Come on everyone, shout it out!"
    scene date 5pm 027a
    "Crowd" "We love you girl!"
    "Girl" "You're a goddess. Make love with me!"
    "Man" "No! I want her first!"
    bs "Hnng..."
    povi "She's loving the attention she's getting. But who knew there were so many lesbians here?"
    "Man" "Wow, did I see nipple rings there?"
    "Girl" "No you didn't. She's a good girl, not your slut!"
    "Another Man" "Maybe a damn sexy slut."
    bs "Hmm..."
    pov "<whisper> Look, over there! Your rival is boiling with rage."
    scene date 5pm 028a
    bs "<whisper> Haha, you're right. That face!"
    pov "<whisper> She's realizing that she's losing to you."
    pov "<whisper> And I know what we can do to destroy her completely."
    bs "<whisper> Hm...?"
    pov "<whisper> I'm going to move my hands now."
    pov "<whisper> I won't do it unless you want me to, but I figured you got them \"enhanced\" for a reason."
    pov "<whisper> Famous people show off their bodies all the time. Seems like a small price to pay for a big win."
    bs "<whisper> O... ok."
    povi "Wow, she really will do anything to be famous, its almost sad how easy that is to leverage."
    scene date 5pm 031a
    "Girl" "Oh my god!"
    "Crowd" "Ooohhh...!"
    "Man" "See! Nipple rings! Such a sexy slut!"
    "Girl" "Shut up! That's classy! And they're beautiful!"
    pov "<whisper> See? They love it. You're definitely going to win!"
    bs "<whisper> And you get to win too!"
    pov "<whisper> Huh?"
    if inc == True:
        bs "<whisper> Getting your hands on your sister's breasts."
    else:
        bs "<whisper> Getting your hands on my breasts."
    povi "Oh, is she teasing me? Maybe she's enjoying it too now."
    povi "But what if she misunderstand this and thinks I'm pushnig her to do it and is acting slutty to keep up?"
    "Crowd" "They need to be played with!"
    "Man" "Do it faggot!"
    call screen cdate5boobs

screen cdate5boobs():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('cdate5boobs'), Jump('cdate5byes')) hovered tt.Action ("Go further [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('cdate5boobs'), Jump('cdate5bno')) hovered tt.Action ("Calm her down [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cdate5byes:
    scene date 5pm 029a
    $ bigsiscorruption += 1
    bs "Hah..."
    "You pull on her nipple rings."
    pov "<whisper> Time to really give this crowd a show!"
    "Crowd" "Knead them. Make her nips hard!"
    "Girl" "Yes! I'd love to see her turned on."
    bs "<whisper> Not so rough please..."
    scene date 5pm 030a
    "You start to knead them."
    pov "<whisper> Wow. No complaining?"
    bs "Hah... <whisper> II'm just wanting to please the crowd. Like you said."
    povi "Damn, maybe I should start an influencer agency?"
    if inc == True:
        povi "Damn. I'm playing with my sister's tits in public and the only thing she's cares about is what the crowd is thinking."
    else:
        povi "Damn. I'm playing with her tits in public and the only thing she's cares about is what the crowd is thinking."
    povi "I wonder how far I can get her to go with this."
    scene date 5pm 032a
    "Photographer" "Yes tease me more [bs]!"
    "Man" "What a view. I wish I could fap right now!"
    "Girl" "You pervert! Just admire the perfection, don't sully it!"
    "You slide under the blanket."
    povi "Now is the time to push this. I'll never get her in this situation again."
    scene date 5pm 033a
    bs "Aah... What are you doing?"
    "Crowd" "Yes! You go [pov]!"
    "Man" "Best idea ever!"
    "Girl" "Isn't this going too far?"
    pov "<whisper> I know what the people want! Your turn [bs]!"
    bs "<whisper> You can't be serious!"
    pov "<whisper> This is for the fame!"
    "Photographer" "What a nice idea to spice the shoot up!"
    scene date 5pm 034a
    pov "<whisper> See? Everyone loves the idea. Let me help you!"
    bs "<whisper> You want to help take my pants off?"
    pov "<whisper> Yes, the crowd is eating this up. And I'm sure you're enjoying it too."
    if inc == True:
        bs "<whisper> We shouldn't do this. You're my brother! You shouldn't be taking off your sister's pants."
    else:
        bs "<whisper> We shouldn't do this. We've known each other for so long! You shouldn't be take off my pants."
    pov "<whisper> You remember how important it was that I join you for this couple photo-shoot?"
    pov "<whisper> I'm very sure you were aware what could happen and even wanted to do this with me, instead of someone else."
    if bigsislove or bigsiscorruption >=30:
        pov "<whisper> And don't forget, you even said we're boyfriend and girlfriend!"
    bs "<whisper> What? No..."
    pov "<whisper> That's not very persuasive [bs]. Stop me if you really don't want to do this..."
    bs "..."
    pov "<whisper> That's what I thought."
    scene date 5pm 035a
    bs "Hah... ahh..."
    pov "Come here!"
    bs "S... stop... <giggle>"
    "Man" "Oh she needs some help, haha."
    "Crowd" "Yes, convince her!"
    "Girl" "I hope they won't stay under that blanket!"
    if bigsiscorruption <= 20:
        jump cdate5normend
    scene date 5pm 036a
    "Crowd" "Yes, he did it!"
    bs "<whisper> Please, we should stop this."
    if inc == True:
        pov "<whisper> Yes we should stop... stop fighting this, big sis."
    else:
        pov "<whisper> Yes we should stop... stop fighting this, [bs]."
    pov "<whisper> We both know you want it too."
    povi "Oh wow! Her panties are almost transparent!"
    bs "<whisper> But everyone will see..."
    pov "<whisper> Just relax and trust me. We'll slip under the blanket again."
    scene date 5pm 037a
    "Crowd" "Boo! We want to see her panties too!"
    "Photographer" "Please respect the models wishes."
    "Photographer" "But I'm sure there's enough room in your imaginations as to what a couple could do almost naked under that blanket."
    pov "<whisper> You get it? Everyone knows, but nobody sees it. And with their imaginations, you're getting your fame."
    if inc == True:
        bs "<whisper> And you get your big sister almost naked and so close with your little tricks. You pervert..."
    else:
        bs "<whisper> And you almost got me naked and so close with your little tricks. You pervert..."
    pov "<whisper> Oh, you got me! But I can feel how much you're turned on too."
    pov "<whisper> You're burning up and your nipples are hard like rocks. You like the attention a little too much I think."
    pov "<whisper> So let me enjoy my tricks and you can enjoy the rest of your photo-shoot."
    bs "<whisper> Hnnn..."
    "Photographer" " Look here [bs]!"
    scene date 5pm 038a
    bs "Hah..."
    "Photographer" "Yes good [pov]. Hold her nipple like that."
    pov "<whisper> Look! He's taking a close shot of your beautiful pierced nipple!"
    pov "<whisper> Imagine that on the cover of some star magazine!"
    bs "Hnng..."
    "Crowd" "She's getting horny!"
    "Man" "What's going on under that blanket?"
    "Girl" "Can I join you? I want to get touched by that hot guy too!"
    "Photographer" "Now give me something fun [bs]."
    scene date 5pm 039a
    bs "Peace!"
    "Photographer" "Wonderful!"
    "Photographer" "Hold still, just a few more!"
    povi "Damn, I need more too!"
    scene date 5pm 040a
    bs "Hah..."
    "Crowd" "She moaned!"
    "Man" "I bet they're fucking under the blanket!"
    "Other Man" "No way! They wouldn't be stupid enought to do that in public!"
    "Girl" "Yeah! Get your thoughts out of the gutter, pervert!"
    "Photographer" "What's wrong?"
    pov "<whisper> Oh I just improvised a bit to make it a bit more natural."
    "Photographer" "Oh, I see."
    bs "Hah... hah..."
    pov "<whisper> We need just another moment."
    "Photographer" "Ok, sure."
    "Crowd" "What are they saying?"
    scene date 5pm 041a
    bs "<whisper> What the hell are you're thinking. Get your hands off me down there!"
    pov "<whisper> Sshh... relax. I just got more authentic. Also you're flooding down there."
    bs "<whisper> It's not what you're thinking..."
    pov "<whisper> Oh, so you're that horny because of me?"
    bs "<whisper> Of course not!"
    pov "<whisper> Then you can let me continue and just enjoy who it feels without worries."
    if bigsiscorruption <= 50:
        jump cdate5normend
    "Photographer" "Can we continue."
    "Crowd" " Yes, no more breaks. More moaning [bs]!"
    pov "Yes, go on!"
    bs "No, wait..."
    pov "Let's continue!"
    "Photographer" "Ok, look at me again, [bs]. You're doing great."
    scene date 5pm 042a
    bs "Hnng... <smile>"
    "Photographer" "Yes, very hot! You're so talented!"
    "Man" "Because she's a slut!"
    "Girl" "Shut up! I want to be like her!"
    "Another Girl" "I wonder if they are really a couple... [pov] is amazing."
    "Man" "It looks like they're fucking already!"
    pov "<whisper> Are enjoying my fingers? You've been working so hard to get famous, you should be rewarded for that."
    bs "Hnng..."
    povi "Time for more."
    scene date 5pm 043a
    bs "Hahiiiih..."
    "Girl" "Did she cum?"
    "Man" "So hot!"
    "Photographer" "What happened? Are you alright?"
    povi "I happened. Two fingers wide in her wet pussy! Haha."
    pov "<whisper> I wonder how they would react if they knew you're dripping wet."
    scene date 5pm 045a
    bs "Haha, no everything is alright. My nipples are just getting a little too sensitive."
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
        pov "<whisper> Do you enjoy it that much getting fingered by your childhood friend?"
    bs "<whisper> You're... wro... hah!"
    pov "<whisper> You're a bad liar, haha."
    scene date 5pm 046a
    bs "Hnng...!"
    pov "<whisper> You feel my hard dick? Your wet pussy is aching for it!"
    pov "<whisper> And I'll stick it in you soon! We could do it right here even, in front of everyone!"
    "Photographer" "Damn my battery is too low. I need to change it, take a short break."
    "Crowd" "Hurry photographer, we want to see them play more."
    scene date 5pm 047a
    bs "<whisper> Please! We can't do that here!"
    pov "<whisper> Oh we can. I noticed how wet your pussy is, sucked my fingers right in before. You want it badly."
    bs "<whisper> Hnn... Yes but..."
    pov "<whisper> See? Just talking about it turns you on! You're shaking."
    pov "<whisper> I'm not going to judge you for wanting it, I want this too."
    if inc == True:
        pov "<whisper> I've waited so long to fuck my hot sister, I'll give you a proper pounding!"
    else:
        pov "<whisper> I've waited so long to fuck you, I'll give you a proper pounding!"
    scene date 5pm 048a
    bs "<whisper> Hnng..."
    if inc == True:
        pov "<whisper> I want you to be a good girl and take your brothers hard dick!"
        pov "<whisper> We can enjoy each other now, where no one knows that we're siblings."
        pov "<whisper> Think of the rumors, if they only knew how bad you want me, your brother, inside you."
    else:
        pov "<whisper> And I want you to be a good girl and take my hard dick!"
        pov "<whisper> We can enjoy each other now, where no one knows that we're living together."
        pov "<whisper> Think of the rumors, if they only knew how bad you want me, your childhood friend, inside you."
    bs "<whisper> HNNG...!"
    scene date 5pm 049a
    bs "<whisper> Please don't do it here. I'll make it up to you later."
    pov "<whisper> Hm...? And what would be better than ramming my hard dick inside you?"
    bs "<whisper> I... I'll suck you off when this is over. Please don't fuck me here."
    povi "Damn, she's serious, I can see it in her eyes!"
    pov "<whisper> Hm..."
    "You stare in each others eyes."
    "Photographer" "I'm ready, let's continue! Look here please, [bs]!"
    scene date 5pm 050a
    bs "Ok!"
    povi "I could get rewarded with a blowjob later or try to take her now!"
    if bigsiscorruption <= 70:
        jump cdate5bj
    povi "But now I have the chance to take her and she probably won't complain."
    povi "So what should I do?"
    call screen cdate5bjfuck

screen cdate5bjfuck():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('cdate5bjfuck'), Jump('cdate5fuck')) hovered tt.Action ("Fuck her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('cdate5bjfuck'), Jump('cdate5bj')) hovered tt.Action ("Wait for the blowjob [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cdate5fuck:
    povi "Screw it! We've come this far!"
    scene date 5pm 051a
    bs "Oh god... hnng!"
    "You slide your dick in her wet pussy."
    "Photographer" "What's the problem now?"
    bs "I... he... he...aah..."
    pov "<whisper> You won't tell them what we're doing now, will you?"
    scene date 5pm 052a
    bs "Hnng..."
    povi "Haha, is she trying to escape? There's no way out of this now."
    povi "And she doesn't seem to be fighting this real hard, more like she's just shifting positions."
    "Photographer" "What's the problem?"
    povi "She's sucking me in, what a naughty girl!"
    bs "I... I've a cramp... hah... ah..."
    povi "Wow, she has an excuse for everything."
    pov "We're trying to make the couples thing look more authentic by pretending to fuck."
    bs "Hnng... hah..."
    povi "Damn, her pussy pressing on my dick now like crazy. That turned her on so much."
    "Photographer" "Oh, I see. That looks good!"
    "Crowd" "Wow, so realistic."
    "Man" "I bet they're really fucking!"
    scene date 5pm 053a
    pov "<whisper> I think your cramp is better now! Get over here with me and enjoy your fuck!"
    bs "Hah... hah... hah..."
    "Girl" "Yes take her good and then do me too!"
    "Man" "I want to do it with her too!"
    pov "<whisper> I hope you're ready to keep going until we both cum!"
    pov "<whisper> Because it'll be such a shame waste this chance!"
    bs "Hnng... hah... hm..."
    pov "<whisper> I want you to be good, honest girl now and tell me you love it too."
    bs "Hah...!"
    "You fuck her faster!"
    scene date 5pm 054a
    bs "Hah, ahhh..."
    "You stare in each others eyes."
    if inc == True:
        bs "<whisper> I... I love how... hah... you fuck me... aahh... brother!"
    else:
        bs "<whisper> I... I love how... hah... you fuck me... aahh... [pov]!"
    pov "<whisper> Good. Now you're being honest and can enjoy your orgasm like a good girl."
    bs "Hah... hah... haahh..."
    pov "<whisper> Come here!"
    scene date 5pm 055a
    "You start to french kiss her."
    bs "<kiss> hnng..."
    "Crowd" "Wohoo!"
    "Photographer" "Fantastic!"
    povi "Her tongue is dancing around mine. She loves to get kissed like that."
    bs "<kiss> hm... hm..."
    scene date 5pm 056a
    bs "Hnng... hnng..."
    povi "Wow, she looks so happy right now. Finally accepting her desires for me."
    pov "<whisper> I'm glad to see that you're accepting your feelings now. But doing such naughty things in public with me, what a slut you've become!"
    pov "<whisper> My personal slut! Does my slut want to cum now, in front of all these people?"
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
    "Girl" "Oh god, my imagination it going to explode. I want to do that too!"
    bs "Harder [pov]. Harder! I'm almost there!"
    pov "Me too. Your pussy is so good [bs]!"
    scene date 5pm 058a
    bs "Ah... ah... Ahhhh...!"
    "Man" "She's cumming!"
    "Crowd" "What a hot show!"
    povi "I'm at my limit."
    call screen cdate5fcum

screen cdate5fcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('cdate5fcum'), Jump('cdate5fin')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('cdate5fcum'), Jump('cdate5fout')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
    "You can see in her eyes that she loved every moment of it."
    "You nod to let her know that you're very satisfied and enjoyed it too."
    "Crowd" "Again! Do it again, we need more!"
    "Photographer" "Staying close like that! I must say this show was the best yet."
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
    povi "Hahaha, shit..."
    bs "Martin...!"
    martin "What have you done!"
    bs "It's not what it looks like..."
    "Photographer" "Who's that?"
    pov "Her actual boyfriend."
    "Photographer" "Oh... Ohhh!"
    "Crowd" "Ohhhh...!"
    scene black
    "He storms off."
    bs "..."
    "You get dressed again under the blanket and go home together."
    "In total silence."
    $ dtime += 1
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5ntr:
    scene date 5pm 008n
    bs "Hm... now I have to choose one."
    pov "Me...?"
    "Man" "I can help you too!"
    "Girl" "Please choose me!"
    scene date 5pm 009n
    bs "Don't look at me like that [pov]!"
    bs "I can't choose you, you're too ugly, haha!"
    povi "That bitch! Calling me out right here so everyone can hear it."
    bs "Yes that would be a very hard on the photographer."
    "Man" "You're right he's ugly, take me!"
    bs "But maybe if he wears a bag over his head?"
    "Man" "I'LL DO IT!"
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene date 5pm 010n
    "Photographer" "Oh we've got a volunteer!"
    bs "Huh?"
    povi "There's someone really eager to do it, shouting out loud."
    scene date 5pm 011n
    "Man" "Hi cute little one! We'll do this together now. I choose you!"
    bs "Huh? But you..."
    "Photographer" "Great! And you two are very photogenic. Let's start!"
    povi "She seems to know him and isn't amused. Damn, he reeks of alcohol."
    "Man" "Come now. It's time to have some fun!"
    scene date 5pm 012n
    povi "Damn, he's persistent. Is [bs] scared? Maybe he's dangerous?"
    pov "Do you know this guy?"
    "Girl" "He's an alcoholic and a psycho."
    "Man" "Haha, poor girl."
    "Girl" "No one is going to help her. Look at his muscles, he could kill someone."
    povi "Hm, this is bad. Maybe I should stop this? What if he does bad things to her?"
    call screen cdate5ntrhelp

screen cdate5ntrhelp():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('cdate5ntrhelp'), Jump('cdate5ntryescont')) hovered tt.Action ("Let her suffer (Darker Paths)") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('cdate5ntrhelp'), Jump('cdate5ntrno')) hovered tt.Action ("Stop this madness") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cdate5ntrno:
    scene black
    "NOTE: This part of the scene isn't finished yet. But it will still abort the scene."
    $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

#----- Added -----
label cdate5ntryescont:
    call screen checkdarkerpaths_cassandra
    if cassandra_voyeur == True or cassandra_ntr == True:
        jump cdate5ntryes
    else:
        jump cdate5ntrnope

label cdate5ntryes:
    if cassandra_voyeur == True:
        povi "No, I won't be helping her today. She humiliated me in front of the crowd."
        povi "Now it's her turn to get humiliated! I bet this drunkard will make her dream a nightmare."
    else:
        povi "There is nothing I can do to stop him. He's huge! She humiliated me in front of the crowd, but I don't want this!"
    scene date 5pm 013n
    "Photographer" "Good, lay down and give me a smile."
    if cassandra_voyeur == True:
        povi "She's getting angry. Must be having to do a photo-shoot with a drunkard."
    else:
        povi "She's getting angry. Am I the only one that sees she doesn't want this?"
    "Man" "Hm... you're really a damn hottie... hic"
    if cassandra_voyeur == True:
        povi "Hahaha, more humiliation."
    else:
        povi "What a creep!"
    "Photographer" "Oh come on... what's your names?"
    bs "I'm [bs]."
    "Man" "Oh [bs], hot! I'm Ed."
    "Photographer" "Please calm down Ed. We're trying here to make a photo-shoot of a \"loving\" couple."
    "Photographer" "So please act like that."
    "Ed" "But I'm... grrr..."
    scene date 5pm 014n
    if cassandra_voyeur == True:
        povi "Damn, what's he doing? Is he offended?"
        povi "Don't give up so easy Ed!"
    else:
        povi "Damn, what's he doing? Is he offended?"
        povi "Maybe he's going to leave after all!"
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
    "Ed" "I was just getting ready!"
    "Photographer" "Get ready?"
    scene date 5pm 016n
    "Ed" "I undressed so we can start making out!"
    bs "Huh?"
    "Photographer" "What?"
    if cassandra_voyeur == True:
        povi "Wow, he's taking this shit too serious."
    else:
        povi "Maybe he's going to stop this finally!"
    "Girl" "Is he naked?"
    "Man" "Yes he is. He wants to really get started!"
    scene date 5pm 017n
    "Ed" "Let me help you get that top off. Everyone's waiting."
    bs "Wait..."
    if cassandra_voyeur == True:
        povi "Wow, [bs] tits. And her nipple rings."
    "Man" "Damn, girl that's hot!"
    "Girl" "She's a slut! Getting her nipples pierced like that!"
    "Man" "I don't care. I want to play with those boobs!"
    scene date 5pm 018n
    povi "Damn, now he's holding her tight. But I'm sure he isn't stupid enough to try to force her to do something."
    povi "I mean there are so many people here."
    "Crowd" "Yes, Ed. Ed! Ed!"
    if cassandra_voyeur == True:
        povi "But the crowd loves what he's doing. I wonder what [bs] will do?"
    else:
        povi "Stop cheering him on you assholes! I wonder what [bs] will do?"
    bs "I didn't mean..."
    "Ed" "Ssshh...! You're my girl now and we need to do what couples in love do!"
    bs "But I don't even know you..."
    "Ed" "Ok. I'm Ed and you're my slut now!"
    scene date 5pm 019n
    bs "HNNG...!?"
    "Man" "Yes the macho man claims what's his!"
    "Girl" "Look at them kissing."
    povi "What's she doing? Even the photographer isn't sure."
    if cassandra_voyeur == True:
        povi "Normally she's bitching around and now she felt silent. Is she enjoying this?"
    else:
        povi "Normally she's bitching around and now she felt silent. Please don't tell me she's enjoying this?!"
    scene date 5pm 020n
    "Photographer" "Are you alright [bs]?"
    "Ed" "Stop talking to my slut! Just take the photos you want to have!"
    "Photographer" "O... ok."
    "Crowd" "..."
    povi "They're confused too."
    bs "Please... hah... be gentle..."
    if cassandra_voyeur == True:
        povi "What? Is she really a slut?"
    else:
        povi "What? Is she really a slut? Please stop!"
    "Man" "She loves it!"
    "Other man" "Maybe she got drunk from his kiss? Hahaha..."
    "Girl" "She needs to be guided by a strong man!"
    scene date 5pm 021n
    bs "Hah... you're so aggressive..."
    "Ed" "These nipples need to be bitten. You love pain, you pierced them!"
    bs "Hah... hah..."
    if cassandra_voyeur == True:
        povi "Damn, he knows which buttons he needs to press."
    else:
        povi "I can't believe that she's enjoying this..."
    "Man" "Yes! She likes it rough!"
    "Girl" "Give yourself in to that drunk sex god, haha."
    bs "Hnng..."
    scene date 5pm 022n
    "Ed" "Let me help you!"
    bs "Hnn..."
    "Man" "Good get her naked and ready to fuck!"
    if cassandra_voyeur == True:
        povi "Wow, he'll really going to fuck her and she's letting him do it."
        povi "But what's with that look she giving me?"
        povi "Is she scared that she'll get fucked in front of all these people?"
        povi "But she didn't fight against him. Maybe she's just horny and wants to get fucked."
        if inc == True:
            povi "Maybe she's embarrassed by the fact that her brother will see how she likes to get fucked."
        else:
            povi "Maybe she's embarrassed by the fact that I'll see how she likes to get fucked."
    else:
        povi "Is she going to let him fuck her? Really? I can't do anything..."
        povi "But what's with that look she giving me?"
        povi "Is she scared that she'll get fucked in front of all these people?"
        povi "But she didn't fight against him. Please don't look at me like that! I'm too weak!"
        if inc == True:
            povi "I'm a worthless brother. All I can do is watch her get fucked."
        else:
            povi "I'm worthless. All I can do is watch her get fucked."
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
    if cassandra_voyeur == True:
        povi "She's got to be lying! She can't really like having that drunkard fuck her ass, right?"
    else:
        povi "She's got to be lying! She can't really like having that drunkard fuck her ass! Does she?!?"
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
    if cassandra_ntr == True:
        povi "They can't be serious!"
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
    "After some moments Ed leaves."
    scene date 5pm 029n
    bs "Hmm..."
    "Girl" "Does it taste that good? Let me taste some too!"
    "Man" "She can't hear you. She's far away, enjoying his cum."
    "Another girl" "This was the best photo-shoot ever!"
    "Crowd" "You're the best [bs]!"
    scene date 5pm 030n
    bs "You really like my show with Ed? How he fucked my asshole hard and give me his cum?"
    "Photographer" "Damn, girl!"
    "Crowd" "Yes! You're the best!"
    "Crowd" "[bs]! [bs]!"
    povi "Damn, is she really thinking about a porn career after that?"
    if cassandra_voyeur == True:
        povi "I would down for that! Maybe there is something I can do to help her get started!"
    scene black
    if cassandra_voyeur == True:
        "After some time you leave this place, angry [bs] wasn't humilated after all."
    else:
        "After some time you leave this place, completely humilated that you could do nothing to help her."
    "You go home after the bad date."
    $ d5rcntr = True
    $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5ntrnope:
    if cassandra_revenge == True:
        povi "Shit, what am I going to do. That guy is huge!"
        povi "She can be a jerk sometime but I don't want her to be humiliated!"
    else:
        povi "God damn! That guy is huge!"
        povi "She going to be used and abused! Serves the bitch right!"
    scene date 5pm 013n
    "Photographer" "Good, lay down and give me a smile."
    if cassandra_revenge == True:
        povi "She's getting angry. Of course she is, she's having to do a photo-shoot with a drunkard."
    else:
        povi "She's getting angry. Haha! Of course she is, she's having to do a photo-shoot with drunk Hulk!"
    "Man" "Hm... you're really a damn hottie... hic"
    if cassandra_revenge == True:
        povi "I need to think of something quick."
    else:
        povi "Dude, this is going to be epic!"
    "Photographer" "Oh come on... what's your names?"
    bs "I'm [bs]..."
    "Man" "Oh [bs], hot! I'm Ed."
    "Photographer" "Please calm down Ed. We're trying here to make a photo-shoot of a \"loving\" couple."
    "Photographer" "So please act like that."
    "Ed" "But I'm... grrr..."
    scene date 5pm 014n
    if cassandra_revenge == True:
        povi "Damn, what's he doing? Is he offended?"
        povi "Maybe he's going to leave after all!"
    else:
        povi "Damn, what's he doing? Is he offended?"
        povi "Don't give up so easy Ed!"
    "Girl" "What's Ed doing? Is he sleeping?"
    "Man" "Haha, yes he went to sleep because his girl is such a bitch!"
    "Man" "No, she's cute!"
    "Crowd" "Ed! Ed! Ed!"
    "Photographer" "[bs] please look at him. Damn!"
    scene date 5pm 015n
    bs "You know if he's going to sleep maybe we should just call this off."
    "Ed" "Hm... what?"
    bs "I was saying if you're tired, we could just do this another time..."
    "Photographer" "Geez!"
    "Ed" "I was just getting ready!"
    "Photographer" "Getting ready?"
    scene date 5pm 016n
    "Ed" "I undressed so we can start making out!"
    bs "Huh?"
    "Photographer" "What?"
    if cassandra_revenge == True:
        povi "Fuck, he's taking this shit too serious."
    else:
        povi "Fuck, he's taking this shit too serious."
    "Girl" "Is he naked?"
    "Man" "Yes he is. He wants to really get started!"
    scene date 5pm 017n
    "Ed" "Let me help you get that top off. Everyone's waiting."
    bs "Wait... I don't want too..."
    if cassandra_revenge == True:
        povi "Wow, [bs] tits are... Come on! Now's not the time to be thinking about that."
    else:
        povi "Wow, [bs] tits. And her nipple rings."
    "Man" "Damn, girl that's hot!"
    "Girl" "She's a slut! Getting her nipples pierced like that!"
    "Man" "I don't care. I want to play with those boobs!"
    scene date 5pm 018n
    if cassandra_revenge == True:
        povi "Damn, now he's holding her tight. But I'm sure he isn't stupid enough to try to force her to do something."
        povi "I mean there are so many people here."
        "Crowd" "Yes, Ed. Ed! Ed!"
        povi "Stop cheering this on you assholes! I wonder what [bs] will do?"
    else:
        povi "There you go Ed! He's holding her tight. I wonder if he'll try to do something more?"
        povi "I mean there are so many people here..."
        "Crowd" "Yes, Ed. Ed! Ed!"
        povi "But the crowd does love what he's doing. I wonder what [bs] will do?"
    bs "I didn't mean..."
    "Ed" "Ssshh...! You're my girl now and we need to do what couples in love do!"
    bs "But I don't want to..."
    "Ed" "Shhh. I'm Ed and you're my slut now!"
    scene date 5pm 019n
    bs "HMMM...!?"
    "Man" "Yes the macho man claims what's his!"
    "Girl" "Look at their kissing."
    if cassandra_revenge == True:
        povi "What's that asshole doing? Even the photographer isn't sure what to do."
    else:
        povi "Haha! Even the photographer isn't sure what to do!"
    scene date 5pm 020n
    "Photographer" "Are you alright [bs]?"
    pov "You can see that she's not. Stop this!"
    "Ed" "Stop talking to my slut! Just take the photos you want to have!"
    "Photographer" "O... ok."
    "Crowd" "..."
    if cassandra_revenge == True:
        povi "They're confused too."
        bs "Please... hah... don't hurt me..."
        povi "Is no one going to help her? I need to do something!"
        pov "Let her go Ed! She doesn't want to do this!"
    else:
        povi "Nice! You tell them Ed!"
        bs "Please... hah... don't hurt me..."
        povi "Hehe, I think it's too late for that."
        pov "She wants it! Look at her!"
    "Man" "She loves it!"
    "Other man" "Maybe she got drunk from his kiss? Hahaha..."
    "Girl" "She needs to be guided by a strong man!"
    if cassandra_revenge == True:
        povi "Everyone is just ignoring me!"
    else:
        povi "There we go, that worked great!"
    scene date 5pm 021n
    bs "please... stop..."
    "Ed" "These nipples need to be bitten. You love pain, you pierced them!"
    bs "AGHgh... that hurts..."
    if cassandra_revenge == True:
        povi "I'm so sorry [bs] I don't think I can stop him."
    "Man" "Yes! She likes it rough!"
    "Girl" "Give yourself in to that drunk sex god, haha."
    scene date 5pm 022n
    "Ed" "Let me help you!"
    bs "Noo..."
    "Man" "Good get her naked and ready to fuck!"
    if cassandra_revenge == True:
        povi "Oh no, he'll really going to fuck her right here!"
        povi "But what's with that look she giving me? She want's me to stop this!"
        povi "She scared that she'll get fucked in front of all these people?"
        povi "She can't fight against him. He could kill her if he wanted to."
        if inc == True:
            povi "She's probably also embarrassed by the fact that her brother will see it all."
        else:
            povi "She's probably also embarrassed by the fact that I will see it all."
        "You try to rush forward to help her, but the crowd holds you back, not willing to let you ruin their show."
    else:
        povi "Wow, he's really going to fuck her right here!"
        povi "But what's with that look she giving me? Does she want me to stop this? Not likely..."
        povi "She's scared that she'll get fucked in front of all these people?"
        povi "She can't fight against him. He could probably kill her if he wanted to. There is no way I'm going to try to stop him... And I don't really want to anyway."
        if inc == True:
            povi "She's probably also embarrassed by the fact that her brother will see it all."
        else:
            povi "She's probably also embarrassed by the fact that I will see it all. Can't wait to rub that in later."
        "You try to rush forward to see even better, but the crowd holds you back, not willing to give up their view of the show."
    bs "Please don't do this..."
    scene edited date 5pm 023n
    bs "Aggh..."
    "Ed" "Good, your pussy is nice and tight! A bit dry though!"
    "Photographer" "Damn! Who thought this would turn into a porn photo-shoot."
    pov "You piece of shit! Stop this! This isn't porn, its rape!"
    "Crowd" "Yes, fuck her good!"
    "Ed" "I'll get a good lube on my dick for the main part."
    "He spits on his cock as he thrusts it into her."
    bs "What main... part?"
    "Ed" "You're a slut that has bitched around me before, so you haven't earned yourself a fuck in the pussy."
    bs "Huh?"
    scene edited date 5pm 024n
    "Ed" "Your other hole gets my dick!"
    bs "Aaaah... stop! Just stop..."
    "Photographer" "Damn, that's good."
    "Ed" "I told you before, Mr. photographer! Hmm... these cute little toes!"
    "Her eyes roll back in pain, she's trying to think of something, somewhere else."
    "Man" "Wow, now we have anal!"
    "Girl" "You're a sex god Ed!"
    scene edited date 5pm 025n
    "Ed" "You like it in the ass, slut?"
    bs "No... Stop it now! You're so deep in me... it hurts!"
    "Crowd" "Anal-slut! Anal-slut!"
    if cassandra_revenge == True:
        povi "She told you she doesn't like this! She can't like having a drunkard fuck her ass!"
    else:
        pov "Anal-slut! Anal-slut! Give her hell Ed!"
    "Ed" "Good. And keep your asshole tight for me!"
    bs "Hah... no...!"
    scene edited date 5pm 026n
    "Ed" "Come here, so I can enter you deeper!"
    bs "Oh my god, stop... ahhh..."
    "Girl" "Yes do her! She's my idol now. Getting her ass plunged!"
    "Man" "Ride her harder!"
    bs "No... please. No more!"
    "Ed" "As you wish my sexy slut! No means yes!"
    scene edited date 5pm 027n
    bs "AAAGGGHHH... HAAAHHH..."
    "Man" "She's like a pornstar. Milking a stranger with her ass!"
    "Girl" "That hot body. I want to lick all it all over."
    "Crowd" "Fuck harder! Fuck harder!"
    if cassandra_revenge == True:
        povi "They can't be serious!"
    else:
        povi "This crowd is fucking awesome!"
    "Ed" "I'm about to cum slut! You'll take it in your bitch-mouth!"
    bs "NOooo... Noo..."
    "He forces her mouth over his filthy cock."
    scene edited date 5pm 028n
    bs "Bwaaaaah <sobs>"
    "Ed" "YES!"
    "Man" "Damn, he's gagging her. Look at her mouth!"
    "Girl" "But she's taking him good and swallowing his sperm."
    "Another man" "She's like a pro! I love her!"
    "Crowd" "[bs]! [bs]! [bs]!"
    "Ed" "Drink it all!"
    bs "Ggggghhh..."
    scene black
    "After some moments Ed leaves."
    scene edited date 5pm 029n
    bs "Hmm..."
    "Girl" "Does it taste that good? Let me taste some too!"
    "Man" "She can't hear you. She's far away, enjoying his cum."
    "Another girl" "This was the best photo-shoot ever!"
    "Crowd" "You're the best [bs]!"
    if cassandra_revenge == True:
        povi "Her eyes are glazed over. It's like she's lost. God damn it! I'm going to make him pay! One day."
    else:
        povi "Her eyes are glazed over. Now that is someone fucked properly!"
    "Photographer" "Damn, girl!"
    "Crowd" "[bs]! [bs]!"
    pov "[bs] can you hear me?"
    "Crowd" "Yes! You're the best!"
    pov "[bs]!"
    "She finally snaps out of the funk and tries to wipe the tears from her face."
    "She plants a fake smile on her face and pretends like everything is ok, like this never happened."
    scene edited date 5pm 030n
    bs "[pov]?"
    pov "Yes, its me."
    bs "Can we go home now..."
    if cassandra_revenge == True:
        pov "Of course, [bs]. Let's go home."
    else:
        pov "Sure, if you want. Good job [bs]! I'm sure you'll be famous in no time."
    scene black
    "You go home after togther."
    "It isn't until she's alone in her room, that you hear her sobs."
    if cassandra_revenge == True:
        "You failed her."
    else:
        "Serves her right."
    $ d5rcntr = True
    $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5bj:
    if bigsiscorruption <= 70:
        povi "No! I won't risk it now. A blowjob is OK also."
    else:
        povi "I'll take the blowjob. I want to see what she can do with her mouth besides complaining!"
    "After some more photos the shoot ended."
    scene black
    "On your way home together [bs] looks very happy and deep in thought."
    "But a promise is a promise after all."
    scene date 5pm 002bj
    pov "Hey [bs]!"
    bs "..."
    pov "Hold up!"
    scene date 5pm 003bj
    bs "What's up?"
    pov "Look over there!"
    bs "Hm...?"
    pov "Behind you."
    scene date 5pm 004bj
    bs "Yeah, ok. What about it?"
    pov "It would be the perfect place, don't you think so?"
    scene date 5pm 005bj
    bs "Hm... the perfect place...? For what?"
    povi "Did she really forget it or is she trying to avoid it?"
    pov "To suck me off of course. You did promise."
    scene date 5pm 006bj
    if inc == True:
        bs "You... you really want your older sister to suck you off?"
    else:
        bs "You... you really want me to suck you off?"
    pov "Yes. Don't play innocent, we both know how horny you were before."
    bs "But that was about a crazy situation, I felt excited then."
    pov "Stop lying to yourself... I helped you and you promised me a reward."
    scene date 5pm 007bj
    if inc == True:
        bs "Ok, you'll get your reward, pervy brother."
    else:
        bs "Ok, you'll get your reward, pervert."
    povi "I knew it, she was just playing innocent! And she was damn horny before."
    scene date 5pm 008bj
    bs "Come on, let's get it over with."
    if inc == True:
        bs "If you want your sister to taste your dick so badly."
    else:
        bs "If you want me taste your dick so badly."
    povi "Damn, she's teasing me. Maybe she really wants to have a taste?"
    scene date 5pm 009bj
    bs "Let me help you."
    povi "Yes, she's starting it. I can't wait to see my dick in her mouth!"
    bs "Seems like you're already ready for this?"
    pov "Oh yes. I got so damn hard when I rubbed my dick on your ass."
    scene date 5pm 010bj
    bs "Haha, still the little pervert just like before."
    if inc == True:
        bs "Wanting to do naughty things with his big sister all the time."
    else:
        bs "Wanting to do naughty things with me all the time."
    pov "Yes and I still want to!"
    bs "Then sit down over there, so I can start."
    povi "She's really doing it! There is no crazy or forced situation going on now."
    scene date 5pm 011bj
    bs "Huh? Damn!"
    pov "What's wrong [bs]?"
    bs "You're really packed down there..."
    pov "So you like my dick?"
    povi "Damn, her warm hands and her hot breath are a thrill of anticipation."
    scene date 5pm 012bj
    bs "Ha, I'm just surprised that your dick is so big."
    pov "But you'll suck it anyway! I want to feel your wet lips and tongue on it!"
    bs "Hm.. don't worry, I won't ruin your \"moment\"."
    povi "She's cheeky! Maybe she needs a punishment."
    pov "How about you start sucking and stop talking?"
    scene date 5pm 013bj
    if inc == True:
        bs "Geez! Relax brother. I'm going to make you very happy."
    else:
        bs "Geez! Relax, [pov]. I'm going to make you very happy."
    povi "Oh yes! Her warm and wet tongue is touching my dick."
    bs "<lick> <lick>"
    pov "A good start after I waited so long, haha."
    bs "Oh someone is getting cocky!"
    pov "Said by someone who's licking my cock."
    scene date 5pm 014bj
    bs "<lick> <lick>"
    pov "Ohhh..."
    povi "She's licking my tip with her tongue, what a good feeling."
    pov "That feels great [bs]."
    bs "Hm... Let's see if we can do better."
    scene date 5pm 015bj
    bs "<suck> <lick> Hmm..."
    povi "Her wet mouth... And what a fantastic view."
    if inc == True:
        pov "That's a very good place for you, sitting down there and sucking your brother's dick."
    else:
        pov "That's a very good place for you, sitting down there and sucking my dick."
    scene date 5pm 016bj
    bs "Hmm..."
    pov "We should have been doing this way before now!"
    bs "<suck> <suck>"
    pov "Of course I've grown a lot since back then. Haha."
    bs "Hnnmm..."
    povi "She seems to be enjoying it. That's good. Hopefully we can do this again some time."
    scene date 5pm 017bj
    pov "Oh yes! Very good!"
    bs "<suck>"
    povi "I wonder if she's able to take it all in?"
    pov "Do you want to try to take it all in your hot, slippery mouth?"
    if inc == True:
        "Your sister signaled you that she won't do that."
    else:
        "[bs] signaled you that she won't do that."
    pov "Oh, come on..."
    povi "Maybe I should help her? Or just see what else she'll do?"
    call screen cdate5bjchoose

screen cdate5bjchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('cdate5bjchoose'), Jump('cdate5bjdt')) hovered tt.Action ("Help her (deepthroat)") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('cdate5bjchoose'), Jump('cdate5bjn')) hovered tt.Action ("Watch her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cdate5bjn:
    povi "I'll wait and see what she intends to do with me instead."
    scene date 5pm 018bj
    povi "Oh my god!"
    pov "Hnn... what a wonderful idea!"
    bs "<suck> Hm... <giggle>"
    pov "So you're enjoying this too?"
    bs "<giggle>"
    if inc == True:
        pov "Damn your skills are amazing, big sis!"
    else:
        pov "Damn your skills are amazing, [bs]!"
    scene date 5pm 019bj
    bs "<lick> Don't get too excited about it, I might just try to finish you off faster."
    pov "Well you're doing a damn good job of it either way, hah...!"
    pov "Or is it that you like playing with my hard dick?"
    bs "Hm... It's really not that bad, but don't read too much into it, little pervert."
    povi "I knew it! And I bet she was horny before because of my hard dick too."
    scene date 5pm 020bj
    bs "<kiss> <kiss>"
    pov "Yes kiss your lover, haha, hah... hah..."
    bs "<giggle> You wish!"
    pov "Damn, that was worth the wait."
    bs "Are you about to come? Tell me before you do. I don't want to ruin my outfit."
    pov "Ok."
    scene date 5pm 018bj
    povi "Damn, this is so fuckiing hot! I'm so close, I'm gonig to cum any moment."
    bs "<suck> <suck>"
    call screen cdate5bjcum

screen cdate5bjcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('cdate5bjcum'), Jump('cdate5bjcumin')) hovered tt.Action ("Just cum") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('cdate5bjcum'), Jump('cdate5bjcumout')) hovered tt.Action ("Warn her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cdate5bjcumin:
    povi "I don't think I'll warn her. I want to finish in her mouth. Her outfit will be just fine that way too."
    pov "Hnng..."
    scene date 5pm 021bji
    bs "Ommmph!"
    if inc == True:
        "You start cumming into your sister's mouth."
    else:
        "You start cumming into [bs]'s mouth."
    pov "Ohh..."
    scene date 5pm 022bji
    bs "Hmm... hmm..."
    povi "Wow, she's not even getting angry. She's just kneeling there and collecting my sperm in her mouth."
    povi "Holy shit, I'm still cumming! She is so amazing!"
    if inc == True:
        pov "I'm sorry that I didn't warn you, big sis."
    else:
        pov "I'm sorry that I didn't warn you, [bs]."
    pov "I just couldn't hold it any longer."
    bs "Hmm..."
    pov "Why don't you show me what I gave you."
    bs "Hm..."
    scene date 5pm 023bji
    pov "Ohh..."
    bs "I don't understand why men are so obsessed with see their cum after?"
    pov "It's depends on the guy I guess. I just like to see what your hard work did."
    pov "And that was an amazing blow-job."
    bs "Hmm..."
    scene date 5pm 024bji
    bs "<gulp>"
    pov "You... you swallowed it?"
    bs "Yes."
    pov "That's hot! Any particular reason?"
    bs "<giggle> Nope. Just wanted see your face when I did, haha."
    bs "Men are so easily controlled!"
    if inc == True:
        povi "True, but she's the one swallowing my sperm. My big sister swallowed what I gave her!"
    else:
        povi "True, but she's the one swallowing my sperm. [bs] swallowed what I gave her!"
    povi "I still think I got the better end of the deal here."
    bs "Come on, let's go home."
    scene black
    "You go home together."
    $ dtime += 1
    $ cdate5bj = True
    $ d5rcbjsw = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5bjcumout:
    if inc == True:
        pov "I'm there. I'm cumming, sis."
    else:
        pov "I'm there. I'm cumming [bs]."
    scene date 5pm 021bjo
    bs "Wait a second, I'll grab..."
    pov "Hnng..."
    bs "Huh?"
    povi "Right on her face!"
    scene date 5pm 022bjo
    bs "Hnng..."
    povi "What a wonderful view. My sperm all over her face."
    bs "Give me a tissue please... hm..."
    pov "Sure."
    povi "Ha, she can't open her eyes now, I should take a picture, she won't complain because she won't know."
    scene date 5pm 022bjox
    "You silently take a photo of her face covered with your sperm."
    povi "Maybe I can use this some time."
    scene date 5pm 023bjo
    bs "Why is it taking so long?"
    povi "Oh she found a way to handle it. Good she didn't catch me."
    pov "I... I was stunned by that view."
    if inc == True:
        bs "So you like the view of your sperm on your sister's face?"
    else:
        bs "So you like the view of your sperm on my face?"
    pov "Oh yes!"
    bs "Geez! <giggles>"
    scene black
    "[bs] wiped her face clean with a tissue and you go home together."
    $ dtime += 1
    $ cdate5bj = True
    $ d5rcbjout = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5bjdt:
    povi "It's time for her punishment for being so cheeky before."
    scene date 5pm 018bja
    bs "Huh?"
    "You press her face onto your dick."
    "She's not pushing back, but she doesn't seem super happy about it either."
    pov "I'm just trying to help you do the very best you can."
    scene date 5pm 019bja
    bs "Hnng..."
    if inc == True:
        pov "Good sister! Take my dick deeper!"
    else:
        pov "Good girl! Take my dick deeper!"
    pov "That's it, just a little further and you'll have it all in."
    scene date 5pm 020bja
    bs "<choke> HNNG..."
    pov "That's it! God your throat feels amazing!"
    "You hold her hand."
    povi "Wow my dick is all in her mouth. A little dominatation never killed anyone!"
    pov "Good! It'll be over soon and everything will be alright. Be a good girl now."
    "You start to fuck her mouth."
    scene date 5pm 021bja
    bs "<choke> Hng... hng..."
    pov "Good. Let me use your mouth."
    bs "Hmm...!"
    "She's moving with me now. Looks like she's submitting"
    if inc == True:
        pov "Good girl, accept that your brother has the control and let me use you as his toy."
    else:
        pov "Good girl, accept that I have the control and let me use you as my toy."
    pov "Don't panic. Breathe in through your nose more."
    pov "You'll get used too it."
    scene date 5pm 022bja
    pov "God you're amazing. Keep sucking like that."
    bs "Hnn... hnn..."
    pov "I'm getting close. You're going to get your reward for being a good girl. I'll shoot my sperm down your throat."
    bs "Hmm..."
    povi "Wow that answer sounded like a submissive agreement."
    pov "Don't choke on it, just swallow everything that comes."
    scene date 5pm 023bja
    pov "Here it comes!"
    pov "Hnng..."
    bs "<gulp> <gulp> Hnn..."
    if inc == True:
        pov "Swallow it all! I've waited so long to use my slutty sister like that."
    else:
        pov "Swallow it all! I've waited so long to use you, my slutty girl, like this."
    bs "HNNG..."
    "After she swallows it all, you let her head go."
    scene date 5pm 024bja
    bs "Asshole! I could have choked!"
    pov "Relax. You wanted to bribe me with a blow-job."
    bs "But not like that. You practically forced me!"
    pov "No, I was just showing you how I wanted to do it."
    pov "And I know you love to be dominated!"
    bs "Are you crazy?"
    pov "You let it happen and swallowed it all like a good girl. I don't think I'm crazy."
    if bigsiscorruption >= 50:
        pov "You did very well. I'm proud you, my good girl"
        "You reach out and clean the rest of your cum and her tears off with your handkerchief."
        scene date 5pm 024bji
        "She relaxes a bit and the anger leaves her eyes. Maybe she is into dom/sub play."
        bs "Well... Don't get used to it. Perv!"
        scene black
        "You two leave together"
    else:
        bs "Fuck you!"
        scene black
        "She storms off and you go home alone."
    $ dtime += 1
    $ cdate5bj = True
    $ casbjdt += 1
    $ d5rcbjdt = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5normend:
    scene black
    bs "Stop it you asshole!"
    povi "Shit, that was too soon. I need to corrupt her more before I try that again."
    "Photographer" "You need some better manners [pov]."
    "[bs] get dressed and leaves."
    bs "You damn asshole! You ruined my chance."
    "You go home alone."
    $ dtime += 1
    $ d5rccor = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5bno:
    scene date 5pm 031a
    $ bigsislove += 1
    povi "No, I don't want this to be about fame. I want us to do things she would want to do because she cares about me, not because she's pressured into it."
    povi "Also I'm not sure what's gonna happen if she gives in to the crowd's wishes."
    povi "There so many perverts out there."
    povi "I don't count. I'm the hero of this story!"
    scene date 5pm 033b
    bs "Huh?"
    if inc == True:
        pov "<whisper> Relax, big sis. We don't have to do anything you don't want to. You're not their personal toy."
    else:
        pov "<whisper> Relax, [bs]. We don't have to do anything you don't want to. You're not their personal toy."
    bs "<whisper> But I..."
    pov "<whisper> I know that you feel uncomfortable and there's no need to deny it."
    bs "<whisper> But..."
    scene date 5pm 034b
    pov "<whisper> I don't want you doing something you might regret later."
    bs "<whisper> Oh...?"
    if inc == True:
        pov "<whisper> I know we fight often but I'm still your brother, so I'll support what ever you decide, not matter what."
    else:
        pov "<whisper> I know we fight often but we have known each other since childhood, so I'll support what ever you decide, not matter what."
    pov "<whisper> You don't have lose yourself to the rush for fame, we can do it together. Over time."
    if inc == True:
        pov "<whisper> And I love you, big sis."
    else:
        pov "<whisper> And I love you, [bs]."
    scene date 5pm 035b
    bs "<whisper> Hmm..."
    pov "<whisper> So what do you want to do?"
    povi "Now she's confused! I don't think she's used to people used to treating her like a human being."
    bs "..."
    pov "<whisper> I won't let you down either way. You can trust me with this."
    bs "<whisper> T... thank you..."
    if bigsislove <= 30:
        jump cdate5loveend1
    scene date 5pm 036b
    pov "[bs]?"
    bs "<kiss>"
    "Crowd" "Woohoo!"
    "Photographer" "This is something I can work with. Keep going!"
    povi "She's kissing me. This is a nice surprise."
    scene date 5pm 037b
    pov "<whisper> Why did you do that?"
    bs "<whisper> B... because I wanted to!"
    pov "<whisper> I'm confused."
    bs "<whisper> I want to show them something and I want you to participate with me."
    bs "<whisper> If you were being honest and you do want the best for me, then you can show me that now."
    povi "She wants me to make out with her? Or is this a trap?"
    pov "<whisper> So more kissing then?"
    scene date 5pm 038b
    bs "<whisper> Don't be so shy. You can grab them, I know you want too."
    "She lays your hand on her breast."
    pov "<whisper> Wow..."
    bs "<giggle>"
    "Crowd" "Yes go on. Play with her boobs!"
    pov "<whisper> So you really want to make out with me?"
    bs "<whisper> For the photo-shoot, don't read too much into it."
    bs "<whisper> And I want you to enjoy this photo-shoot too."
    bs "<whisper> I don't think you would just use me."
    pov "<whisper> Never!"
    scene date 5pm 039b
    pov "<whisper> Come here!"
    if inc == True:
        "You french kiss your sister."
    else:
        "You french kiss her."
    bs "Hnng..."
    povi "Damn, I cant believe it. I should be careful not to overdo it. I don't want to mess this up."
    "Girl" "Wow, they're really getting started!"
    "Man" "I want to lay my hands on those boobs too."
    scene date 5pm 040b
    pov "Huh?"
    "Man" "Haha, she's taking the lead."
    "Girl" "I want to be that confident too!"
    bs "<whisper> I'm still surprised about what you said before. You said... you love me."
    bs "<whisper> So show me! Show me how badly you want me!"
    povi "Damn, now is she teasing me? Well I'll surprise her with a gentle touch."
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
    bs "<whisper> That feels nice..."
    pov "<whisper> You love getting kissed, don't you?"
    bs "<whisper> Hah, yes..."
    "Your move your hand slowly down her body."
    bs "<whisper> Go on. Try to conquer me. <giggle>"
    scene date 5pm 045b
    bs "<whisper> Ohh... you're there."
    pov "<whisper> And you're wet. Like really wet! I can feel it through your pants."
    bs "<whisper> Well no wonder after all you've done! <giggle>"
    bs "<whisper> But I wonder if you brave enough to go even further?"
    pov "<whisper> You know I probably shouldn't after what I told you before, about the Crowd. I really don't want to just use you."
    bs "<whisper> So you need me to talk you into it then? Like you said, what is under the blanket, stays under the blanket. No one will know."
    if inc == True:
        povi "Wow, my sister wants me to touch her pussy!"
    else:
        povi "Wow, [bs] wants me to touch her pussy!"
    scene date 5pm 046b
    pov "<whisper> As you wish!"
    "You slip your hand in her pants and caress her clit gently."
    bs "Haahh...!"
    "Crowd" "Yes, they're doing something!"
    "Girl" "Her moans are so hot. I want to do her too!"
    "Man" "They're just pretending!"
    povi "Oh...?"
    pov "<whisper> I've wanted you for so long! To hold and feel you writhe with my touch."
    bs "<whisper> Yes, go on! Adore me more! <giggle>"
    pov "<whisper> I know something even better!"
    scene date 5pm 047b
    bs "Hnn..."
    pov "<whisper> All for the want of conquering you!"
    if inc == True:
        bs "<whisper> Hah... you're so bad brother. Fingering your older sister. <gig...> hah..."
    else:
        bs "<whisper> Hah... you're so bad. Fingering me after we've known each other for so long. <gig...> hah..."
    pov "<whisper> Oh I won't stop there! I'll conquer you until my dick has a new home in your beautiful, wet pussy."
    bs "Hnng... hah..."
    pov "<whisper> I want to shoot my sperm inside you again and again. I want you to be my girlfirend. My lover."
    pov "<whisper> I need you! I love you!"
    bs "Hnn... hnng..."
    if inc == True:
        bs "<whisper> But you're my brother!"
        pov "<whisper> That doesn't matter or change my feelings for you! It can be a secret if it must, but I want to be with you!"
    else:
        bs "<whisper> But my mom won't allow that!"
        pov "<whisper> That doesn't matter or change my feelings for you! It can be a secret if it must, but I want to be with you!"
    bs "Hnnngg..."
    martin "What are you doing, [bs]?"
    scene date 5pm 060
    bs "Martin!"
    martin "This can't be happening. Nooo!"
    scene black
    "Martin storms off."
    if martingood >= martinbad or martinbad > martingood and bigsislove < 50:
        jump cdate5loveend2
    elif martinbad > martingood and bigsislove >= 50:
        bs "..."
    pov "<whisper> Do you want to follow him?"
    bs "No, I'm here with you. Please don't stop now."
    povi "Holy shit, I can't believe it. She must be ready to dump him."
    scene date 5pm 048b
    bs "<whisper> Oh, you're very excited too!"
    pov "<whisper> Hm... your hand feels so good."
    bs "<whisper> If I take it out now... hah... would you want to fuck me?"
    pov "<whisper> Yes! But not probably not here. I want you all to myself!"
    pov "<whisper> In a romantic place were we would make love."
    pov "<whisper> I would take my time teasing and licking every inch of your beautiful body."
    pov "<whisper> And then we would connect and enjoy our bodies together long through the night."
    bs "Hnng..."
    scene date 5pm 049b
    pov "<whisper> Just couldn't help yourself, could you? Well what do you think?"
    bs "<whisper> Not bad! <giggle>"
    pov "<whisper> Oh, now you're teasing me!"
    bs "<whisper> You're teasing me all the time. <giggle>"
    pov "<whisper> How about we spend for time pleasuring each other from now on?"
    bs "<whisper> We'll see..."
    pov "<whisper> I'll see what I can do to make that a definite yes!"
    scene date 5pm 050b
    bs "Hnn... haaah..."
    "You rub her faster."
    bs "Hnng..."
    "She starts stroking your dick."
    pov "<whisper> That's wonderful, don't stop."
    pov "<whisper> Am I doing well?"
    bs "<whisper> Hah... yes..."
    pov "<whisper> You're shaking, are you about to cum?"
    bs "<whisper> Yes! Hah!"
    pov "<whisper> But I'm not sure I want them all to see you cum in public."
    bs "<whisper> Please don't stop yet! They all still think we're pretending."
    pov "<whisper> As you wish!"
    scene date 5pm 051b
    bs "AAAAHHH...!"
    if inc == True:
        pov "<whisper> Good girl, cum for me, big sis!"
    else:
        pov "<whisper> Good girl, cum for me, [bs]!"
    "Crowd" "Wow, she's cumming!"
    "Man" "I knew they were really playing with each other under the blanket!"
    "Girl" "I'm sure she's faking it."
    scene date 5pm 052b
    bs "Hah... hah..."
    if inc == True:
        bs "<whisper> You did so good brother!"
    else:
        bs "<whisper> You did so good [pov]!"
    pov "<whisper> Like I said, we're good together."
    if inc == True:
        bs "<whisper> But you're a bad, bad brother. Fingering your sister and making her cum so hard. <giggle>"
    else:
        bs "<whisper> But you're a bad, bad boy. Fingering your friend and making her cum so hard. <giggle>"
    pov "<whisper> I had to do my best in my conquest for you!"
    bs "<whisper> Hmmm.... I like that. And so now you have earned yourself a treat."
    pov "<whisper> Oh? Now I'm curious."
    "She starts stroking your dick faster and faster."
    bs "<whisper> Oh, you know exactly what will happen, your dick is twitching in my hand already."
    scene date 5pm 053b
    pov "<whisper> Hnng..."
    bs "<whisper> I can feel your sperm coming."
    "Girl" "Look at him, he's getting a release too!"
    "Man" "He's just pretending, I know it!"
    "Crowd" "What a hot show!"
    scene date 5pm 054b
    bs "<whisper> So how do you feel now?"
    if inc == True:
        bs "<whisper> After covering your sister with your cum!"
    else:
        bs "<whisper> After covering me with your cum!"
    if bigsislove >= 80:
        pov "<whisper> Amazing, but I don't think we're done yet..."
        scene edited date 5pm 053bo
        bs "<whisper> My god, you're hard again?"
        pov "<whisper> I'm in bed and naked, with you. Hell yes, I'm hard again!"
        pov "<whisper> Why don't you lay on your side for me..."
        bs "<whisper> Are you sure you want to do that... here?"
        pov "<whisper> Are you? I said I wouldn't do anything you didn't want to, remember?"
        scene date 5pm 055a
        "She turns to her side and kisses you. You know what her answer is."
        "Crowd" "I don't think they are finished yet!"
        pov "<whisper> I'm going to put it inside you now. I'm going to claim you, as my own."
        if inc == True:
            bs "<whisper> Do it, brother..."
        else:
            bs "<whisper> Do it, [pov]..."
        scene date 5pm 053a
        "You shove yourself inside her wet hot pussy."
        bs "Hnngg... Oh yes..."
        pov "<whisper> I love how you pussy feels [bs]. So soft and wet. And so damn tight!"
        bs "<whisper> I can't believe we're doing this! Hnnnn..."
        scene date 5pm 054a
        bs "<whisper> Do you really love me? I know you love my body, I can tell that. But do you \"love\" me?"
        bs "Hnnn... hah..."
        pov "<whisper> You know I do. I've always loved you. Why do think I followed you everywhere you went? I always want to be near you."
        bs "<whisper> Hnng... You feel so good."
        bs "<whisper> And you don't care... hah... if I'm not famous or rich?"
        pov "<whisper> That has never mattered to me. You're everything I need. Everything I want!"
        scene date 5pm 056a
        bs "<whisper> I believe you... And I think... hnnn..."
        bs "<whisper> ...I'm falling for you too."
        pov "Oh [bs]!"
        scene date 5pm 055a
        "You two kiss passionately"
        "Photographer" "You two are amazing. Like legendary long lost lovers reunited after all this time!"
        scene date 5pm 056a
        pov "<whisper> While I want this to continue forever, why don't we turn this up an notch for our grand finale."
        pov "<whisper> I want to show you how good I can make you feel physically, as well as emotionally."
        bs "<whisper> Yes please, take me!"
        scene date 5pm 051a
        "You grab her ass and pull her closer as you thrust forward with your cock, pushing it even deeper inside her."
        bs "Oh god yes! Hnngg!"
        "Photographer" "What's the problem now?"
        bs "I... he... he...aah..."
        pov "<whisper> I think we surprised the photographer!"
        scene date 5pm 052a
        bs "Hnng..."
        "You start fucking her hard, she braces herself with the side of the bed as your hips slap together each time you thrust."
        "Photographer" "What's the matter?"
        povi "Oh god! She's sucking me in. What a naughty girl!"
        bs "I... I've got a cramp... hah... ah..."
        povi "Haha, I wonder if they will believe that?"
        pov "We're just thought it would be more authentic for the couples theme if we pretended to have sex."
        bs "Hnng... hah..."
        povi "Damn, her pussy squeezing my dick now like crazy. That turned her on so much."
        "Photographer" "Oh, I see. It looks good!"
        "Crowd" "Wow, so realistic."
        "Man" "I bet they're really fucking!"
        scene date 5pm 053a
        pov "<whisper> If your cramp is better now, then you should get over here with me!"
        bs "Hah... hah... hah..."
        "Girl" "Yes take her good and then do me too!"
        "Man" "I want to do it with her too!"
        pov "<whisper> I hope you're ready to keep going until we both cum!"
        pov "<whisper> Because I promised I'd conquer all of you!"
        bs "Hnng... hah... hm..."
        pov "<whisper> I want you to tell me, do you love this as much as I do?"
        bs "Hah...!"
        "You fuck her faster!"
        scene date 5pm 054a
        bs "Hah, ahhh..."
        "You stare in each others eyes."
        if inc == True:
            bs "<whisper> I... I love how... hah... you fuck me... aahh... brother!"
        else:
            bs "<whisper> I... I love how... hah... you fuck me... aahh... [pov]!"
        pov "<whisper> Good. Now let's enjoy your orgasm together."
        bs "Hah... hah... haahh..."
        pov "<whisper> Come here!"
        scene date 5pm 055a
        "You start to french kiss her again."
        bs "<kiss> hnng..."
        "Crowd" "Wohoo!"
        "Photographer" "Fantastic!"
        povi "Her tongue is dancing around mine. She loves getting kissed like that."
        bs "<kiss> hm... hm..."
        scene date 5pm 056a
        bs "Hnng... hnng..."
        povi "Wow, she looks so happy right now. Just lovely."
        pov "<whisper> I'm glad to see that you love this too."
        pov "<whisper> Do you want to cum now? In front of all these people?"
        if inc == True:
            bs "<whisper> Yes. Please, I need to cum! Make me cum, brother!"
        else:
            bs "<whisper> Yes. Please, I need to cum! Make me cum, [pov]!"
        pov "<whisper> As you wish [bs]. Let's cum together."
        "You go even faster in and out of her dripping wet pussy."
        scene date 5pm 057a
        bs "Aaah... hah... Ahh..."
        "Photographer" "Wow, this is really authentic. You're like pro's."
        "Crowd" "Like a damn porn. More!"
        "Girl" "Oh god, my imagination it going to explode. I want to do that too!"
        bs "Harder [pov]. Harder! I'm almost there!"
        pov "Me too. Your pussy is so good [bs]!"
        scene date 5pm 058a
        bs "Ah... ah... Ahhhh...!"
        "Man" "She's cumming!"
        call screen cdate5fcumpart2
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
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

screen cdate5fcumpart2():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('cdate5fcumpart2'), Jump('cdate5finpart2')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('cdate5fcumpart2'), Jump('cdate5foutpart2')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label cdate5finpart2:
    $ cdate5finside = True
    if inc == True:
        "You cum inside your older sister."
    else:
        "You cum inside her."
    jump cdate5bnopart2

label cdate5foutpart2:
    $ cdate5outside = True
    if inc == True:
        "You spray your cum over your older sisters thighs."
    else:
        "You spray your cum over her thighs."
    jump cdate5bnopart2

label cdate5bnopart2:
    if cdate5finside == True:
        scene date 5pm 059ai
    else:
        scene date 5pm 059ao
    bs "Hnng... hah..."
    "You can see in her eyes that she loved every moment of it."
    "You nod to let her know that you're very satisfied and enjoyed it too."
    "Crowd" "Again! Do it again, we need more!"
    "Photographer" "Stay close like that! I must say this show was the best yet."
    "Photographer" "Let me see it from another angle and... oh... OHH..."
    "He got a peek under the blanket."
    "Girl" "What's wrong?"
    "Photographer" "Nothing! everything is... alright! Let's thanks them for that great show!"
    "Crowd" "<Applause>"
    pov "<whisper> I'm satisfied, for now! Are you?"
    bs "<whisper> Oh god yes, I don't know if I can even walk now."
    pov "<whisper> But just so you know, I will not stop conquering you until you're my girlfriend!"
    bs "<giggle> Now I'm curious."
    pov "I love you [bs]!"
    bs "Hnn..."
    scene black
    "You dress yourselves and go home together."
    "[bs] is practically giddy the whole time."
    $ dtime += 1
    $ d5rclovefuck = True
    $ cdate5fuck = True
    $ d5rclovef = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5loveend1:
    scene date 5pm 035b
    bs "<whisper> But I don't want to do it anymore... Something feels wrong."
    pov "<whisper> Huh?"
    povi "What does she mean? Did I go to far by telling her I loved her?"
    bs "<whisper> I'm sorry."
    scene black
    "[bs] gets dressed and leaves the place."
    "Photographer" "What happened?"
    pov "I'm not sure."
    "Crowd" "Booo!"
    povi "Maybe I caused some feelings in her and she couldn't handle the situation?"
    povi "I'm sure I just need to get her love higher."
    "You also go home."
    $ d5rclove = True
    $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

label cdate5loveend2:
    scene black
    bs "Wait...!"
    "[bs] dresses quickly and follows him."
    "Photographer" "What happened?"
    pov "I'm not sure."
    povi "Damn, and I thought she would be in love with me. Why did he have to interfere?"
    povi "Maybe I need help it along a bit and interfere with their relationship."
    "You also go home."
    $ dtime += 1
    $ d5rclovem = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if day >= 6:
        $ weekendactivities += 1
        if weekendactivities >= 3:
            jump weekendskip
        else:
            jump weekendacchoose
    else:
        jump frontdoor

#----- Custom ----- DONE
label alexisdate2choice:
    scene black
    call screen alexisdate2choice2

screen alexisdate2choice2():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('alexisdate2choice2'), Jump('alexisweekendlove')) hovered tt.Action ("Love Path [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('alexisdate2choice2'), Jump('coralexisweekendlove')) hovered tt.Action ("Corruption Path [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom ----- DONE
label nicolecorruptiondate2choice:
    scene black
    call screen nicolecorruptiondate2choice2

screen nicolecorruptiondate2choice2():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('nicolecorruptiondate2choice2'), Jump('nicoleweekendcorlove')) hovered tt.Action ("Love Path [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('nicolecorruptiondate2choice2'), Jump('nicoleweekendcor')) hovered tt.Action ("Corruption Path [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom ----- DONE
label nicolecorruptiondate3choice:
    scene black
    call screen nicolecorruptiondate2choice3

screen nicolecorruptiondate2choice3():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('nicolecorruptiondate2choice3'), Jump('nicoleweekendlove')) hovered tt.Action ("Love Path [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('nicolecorruptiondate2choice3'), Jump('cornicoleweekendlove')) hovered tt.Action ("Corruption Path [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Add options to go from kissing mouth, tits, belly, to licking pussy -----

# ----- Custom lroom Scene - Nicole -----
label bonuslroomnicole:
    $ bonuslroomchoice = False
    scene black
    call screen bonusnicolelovecorruptmenu

screen bonusnicolelovecorruptmenu():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('bonusnicolelovecorruptmenu'), Jump('bonuslroomnicolestartlove')) hovered tt.Action ("Love Path [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('bonusnicolelovecorruptmenu'), Jump('bonuslroomnicolestartcor')) hovered tt.Action ("Corruption Path [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label bonuslroomnicolestartlove: # ----- Completed -----
    scene edited lroom custom 01 # Nicole sitting on couch - Head in hand
    mom "Hey there sweetie."
    povi "I'm surprised she's wearing her red dress on a weekend, but with her hair up it looks more classy than normal."
    if inc == True:
        pov "Looking good mom!"
    else:
        pov "Looking good [mother]!"
    pov "That dress looks nice with your hair all done up like that. Makes it all seem more... elegant."
    scene edited lroom custom 02 # Nicole sitting on couch - Smile
    mom "I'm glad you like it. I already knew that you were partial to the dress, but I prefer my hair up like this, than the way Bruce wants me to do my hair when we're hanging around the rest of th gang."
    pov "Oh I agree. I think this looks fantastic."
    if inc == True:
        mom "That's my son, the eternal flatterer."
    else:
        mom "That's my [pov], the eternal flatterer."
    scene edited lroom custom 03 # Nicole sitting on couch - legs open
    mom "Why don't you come sit by me? I don't get nearly enough time with you all to myself."
    pov "Of course!"
    scene edited lroom custom 04 # Nicole and MC - Legs over MC
    pov "You're awfully cuddly tonight."
    mom "Do you have a problem with that?"
    pov "Nope, not at all. Just saying."
    mom "Well I think that's enough talking for now!"
    scene edited lroom custom 05 # Nicole and MC - Kissing
    pov "Hmph! <kiss>"
    mom "Mmmm... <kiss>"
    "[mother]'s tongue finds it's way into your mouth and you two make out passionately."
    scene edited lroom custom 06 # Nicole and MC - After Kissing
    pov "So, that was great. What's gotten into you?"
    mom "I just don't want to waste another moment without you."
    mom "Having you back has changed this place. It actually feels like a home when you're here with us."
    "She leans back on the couch and you turn around to see her better."
    scene edited lroom custom 07 # Nicole on couch - Looking down at MC between breasts
    pov "Well, I..."
    "She notices you staring at her open legs and just stares at you for a while before speaking."
    mom "I'm done pretending I was happy here with Bruce, hiding my true self from everyone. Just waiting for the next thing to go wrong. Afraid of what the gang would ask us... ask me to do."
    if inc == True:
        pov "Mom, I'm so sorry I wasn't here to..."
    else:
        pov "[mother], I'm so sorry I wasn't here to..."
    mom "Shhh... Don't do that. You don't need to be sorry. This situation isn't your fault, sweetie."
    pov "Well, either way. I wish I could have stopped it sooner."
    mom "And that's why I love you so much."
    mom "But I don't want to waste our time alone on that. We have better things we can be doing."
    scene edited lroom custom 08 # Nicole on couch - Hands spreading pussy with panties on
    pov "Whoa! I'm guess the better things have to do with that?"
    mom "What do you think?"
    "You climb up the couch and get close to [mother]."
    scene edited lroom custom 09 # Nicole on couch - Nicole CLose up - Sexy Look
    pov "I think you're the best thing in my life and that's definitely something worth celebrating."
    mom "Like I said, you're always sweet-talking. You're going to make a girl blush."
    pov "I don't know if it should count as sweet-talking if it's true. Haha!"
    mom "<giggle> I want you to close your eyes sweetie."
    pov "Given how beautiful you are, that's asking a lot."
    mom "Hehe, just do it..."
    pov "Okay, okay. I'm shutting my eyes now."
    scene black
    "You feel her move to the edge of the couch and hear the rustle of clothing."
    pov "Do I need to keep them closed still?"
    mom "Just one more moment... Okay. Open them."
    scene edited lroom custom 10 # Nicole on couch - Legs in the air - Seductive
    if inc == True:
        mom "See something you like, son?"
    else:
        mom "See something you like, [pov]?"
    pov "You could say that..."
    "She looks down to see your hard cock straining against your jeans."
    mom "Why don't you show me how much you like it?"
    "You get up and move over to her end of the couch, pulling your dick out of it's confines."
    scene edited lroom custom 11 # Nicole on couch - MC cock in hand
    pov "Is this what you wanted?"
    mom "This is exactly what I wanted!"
    scene edited lroom custom 12 # Nicole on couch - MC cock teasing lick
    mom "<lick> Mmmm..."
    pov "Oh that's nice."
    mom "Hnnn... <lick>"
    scene edited lroom custom 13 # Nicole on couch - MC cock in mouth
    mom "Hmph... Hmmm. <suck>"
    pov "I love the way your mouth feels on my cock. So wet and warm."
    mom "<suck> Hnnng."
    "[mother] sucks on your cock contently for a while, then in a sudden rush, she gets on her knees and shoves it deeper into her mouth."
    scene edited lroom custom 14 # Nicole Kneeling - MC cock in mouth
    pov "Oh fuck that's good! Don't stop."
    "Your hands instinctively latch on to the sides of her head."
    mom "<suck> Hmmm.... Mmmm."
    if inc == True:
        pov "Mom, will you deepthroat my cock again?"
    else:
        pov "[mother], will you deepthroat my cock again?"
    mom "Mhmmm!"
    "[mother] happily forces herself further down your shaft, squeezing it into her throat. Her wet tongue hugging the sides of your cock."
    scene edited lroom custom 15 # Niocle Kneeling - MC cock deepthroat
    mom "<gag> Hngh... <cough>"
    pov "Oh God!"
    mom "HNNN. <choke>"
    pov "Just a bit longer."
    "She pulls your cock in even deeper. Clearly eager to please you."
    mom "MHMMM. <cough>"
    "She finally pulls herself off your shaft gasping for air. Her drool still covering your shaft."
    scene edited lroom custom 16 # Nicole Kneeling - Looking up to MC
    if inc == True:
        pov "That was fantastic mom!"
    else:
        pov "That was fantastic [mother]!"
    mom "I'm glad you liked it sweetie."
    "You take of your shirt and toss it behind you."
    pov "How did I get this lucky?"
    mom "I was just thinking the same thing..."
    "You reach down and help her stand. Eagerly pulling her close and tasting her chest."
    scene edited lroom custom 17 # Nicole and MC - Standing Embrace
    pov "Hmmm. <lick>"
    if inc == True:
        mom "Oh son!"
    else:
        mom "Oh [pov]!"
    mom "Hnnng..."
    mom "I can't wait any longer! I need you!"
    "[mother] turns towards the couch and bends over."
    scene edited lroom custom 18 # Nicole - Bent over couch - Ass facing MC
    mom "I need you inside me baby!"
    mom "Please... please put it inside!"
    pov "With pleasure!"
    "You move in behind her and shove your cock inside her warm, wet pussy."
    scene edited lroom custom 19 # Nicole and MC - Standing Doggy Fucking
    with vpunch
    mom "Hnng!"
    pov "Fuck, you're so tight!"
    with vpunch
    mom "Shit, baby you feel so good!"
    mom "Hmmm... hah!"
    with vpunch
    mom "I'm getting close! Hnng! Don't stop!"
    pov "Oh I'm not going to stop."
    if inc == True:
        pov "Are you ready to cum on your son's cock?!"
    else:
        pov "Are you ready to cum on my cock?!"
    "You fuck her harder."
    with vpunch
    mom "YES! Yes, yes baby! I'm going to cum. I'm going to cum!"
    scene edited lroom custom 20 # Nicole and MC - Standing Doggy Nicole Cumming
    mom "AAAAHNNG!"
    with vpunch
    pov "That right! Cum for me!"
    mom "Ohhh... hah... hnng."
    with vpunch
    pov "I can feel those little tremors. You're still cumming!"
    mom "Hnnng... So good..."
    mom "Mmmmm..."
    "[mother] sits down, taking a quick moment to catch her breath and then she looks over to you, seductively."
    scene edited lroom custom 21 # Nicole on couch - Teasing/Inviting MC
    mom "That was amazing! God, everytime with you just gets better and better."
    if inc == True:
        pov "Ah shucks, ma!"
    else:
        pov "Ah, shucks!"
    mom "Ha, ha!"
    mom "Well, I think it's time for you to finished too. Don't you think?"
    pov "I completely agree."
    "You grab her legs and lift them apart as she lets herself fall back onto the couch. You slide back into her with ease."
    scene edited lroom custom 22 # Nicole and MC - Missionary Fucking
    pov "Hmmm... I love your wet pussy. It feels so damn good!"
    mom "Hnng. Take me baby. Use my body! I want you to own me completely!"
    "You start thrusting inside her faster. Her pleas exciting you."
    pov "I'm getting close."
    mom "Yes baby! Cum for me. Fill me up!"
    pov "Ohhh fuck... I'm going to cum!"
    mom "YES! Cum baby! Cum inside me!"
    scene edited lroom custom 23 # Nicole and MC - Missionary MC Cumming
    pov "ARRNNGHH!!!"
    with vpunch
    mom "Oh baby! Keep pumping me full of your cum!"
    pov "Hnngg!"
    with vpunch
    mom "Hmmm... So full..."
    pov "Hah... Wow."
    pov "That was awesome..."
    mom "Mmhmm."
    "You both sit back and just take the moment in. Enjoying the bliss."
    scene edited lroom custom 24 # Nicole on couch - Cute and MC looking down
    pov "I could get used to this."
    if inc == True:
        mom "Oh? Does my naughty son want to fill his mommy up again?"
    else:
        mom "Oh? Does my naughty young man want to fill me up again?"
    pov "Always. But I was talking about being with you, whenever and wherever we want."
    mom "I know sweetie. I feel the same way."
    pov "Soon. I promise you. We're not going to have to hide this for long."
    mom "Hnnng..."
    "You two clean up and enjoy the rest of the day together."
    $ bonuslroomchoice = False
    jump weekendacchoose

label bonuslroomnicolestartcor:
    scene edited lroom custom 01 # Nicole sitting on couch - Head in hand
    mom "Hey there baby."
    povi "I'm surprised she's wearing her red dress on a weekend, and her hair is up too. That's an interesting look."
    if inc == True:
        pov "Looking good mom!"
    else:
        pov "Looking good [nicole]!"
    pov "I'm glad you're wearing that dress tonight too. You know how much I like it."
    scene edited lroom custom 02 # Nicole sitting on couch - Smile
    mom "Of course. That's why I'm wearing it. I need to do my best to please my man. Right?"
    pov "Oh I agree. I'm glad you're understanding your duties and putting extra effort into it now."
    if inc == True:
        mom "That's my job now, son. To please you."
    else:
        mom "That's my job now, [pov]. To please you."
    scene edited lroom custom 03 # Nicole sitting on couch - legs open
    mom "Why don't you come sit by me? I don't get nearly enough time with you all to myself."
    pov "Sure."
    scene edited lroom custom 04 # Nicole and MC - Legs over MC
    pov "You're awfully clingy tonight. Missing my hard body?"
    mom "Would you be mad if I said yes?"
    pov "Nope, not at all."
    mom "Well let me show you how much I've been missing your body!"
    scene edited lroom custom 05 # Nicole and MC - Kissing
    pov "Hmph! <kiss>"
    mom "Mmmm... <kiss>"
    "[mother]'s tongue finds it's way into your mouth and you two make out passionately."
    scene edited lroom custom 06 # Nicole and MC - After Kissing
    pov "I have to say, I really appreciate your change in attitude."
    mom "I just don't want to let you down. I'm yours now. And if I make you happy, then I'm helping myself too."
    mom "Having you back has changed this place. You're so strong. And you're standing up to Bruce and Davide. I think you're really going to change things for us."
    "She leans back on the couch and you turn around to check her body out more."
    scene edited lroom custom 07 # Nicole on couch - Looking down at MC between breasts
    pov "Oh I will... I'm going to change everything. I'm going to control everything, everyone."
    "She notices you staring at her open legs and just stares at you for a while before speaking."
    mom "I'm done pretending that Bruce is anything more than a coward and weakling. If I'm by yourside I know I don't have anything to be afraid of anymore."
    if inc == True:
        pov "So long you you keep my happy, mom..."
    else:
        pov "So long you you keep my happy, [mother]..."
    mom "Of course... I know I need to keep you happy. You're doing so much, it's the least I could do."
    pov "It's good you understand. Now what are you going to do to make me happy today?"
    mom "I thnk I have something that can make you very happy."
    scene edited lroom custom 08 # Nicole on couch - Hands spreading pussy with panties on
    pov "Fuck yeah, slut. I definitely think that wet juicy cunt can keep me very happy."
    mom "Why don't you tell me how much you want it?"
    "You climb up the couch and get close to [mother]."
    scene edited lroom custom 09 # Nicole on couch - Nicole CLose up - Sexy Look
    pov "Want? You mean how much I'm going to enjoy it? I already own you. I can use you however I want. And I'm going to."
    mom "Hnng! Use me..."
    pov "Take you clothes off and show me that pussy I own. Show me where you want me to fuck you next."
    mom "Okay..."
    "You watch her move to the edge of the couch and toss her dress and panties aside."
    scene edited lroom custom 10 # Nicole on couch - Legs in the air - Seductive
    if inc == True:
        mom "See something you like, son?"
    else:
        mom "See something you like, [pov]?"
    pov "You could say that..."
    "She looks down to see your hard cock straining against your jeans."
    mom "Let me take care of that for you!"
    "You get up and move over to her end of the couch, pulling your dick out of it's confines."
    scene edited lroom custom 11 # Nicole on couch - MC cock in hand
    pov "Is this what you wanted?"
    mom "This is exactly what I wanted!"
    mom "You're so big!"
    scene edited lroom custom 12 # Nicole on couch - MC cock teasing lick
    mom "<lick> Mmmm..."
    pov "That's nice slut. I can tell you've had plenty of practice."
    mom "Hnnn... <lick>"
    scene edited lroom custom 13 # Nicole on couch - MC cock in mouth
    mom "Hmph... Hmmm. <suck>"
    pov "I love the way your wet hot mouth feels on my cock."
    mom "<suck> Hnnng."
    "[mother] sucks on your cock contently for a while, then in a sudden rush, she gets on her knees and shoves it deeper into her mouth."
    scene edited lroom custom 14 # Nicole Kneeling - MC cock in mouth
    pov "Oh fuck that's good! Don't stop now slut."
    "Your hands instinctively latch on to the sides of her head."
    mom "<suck> Hmmm.... Mmmm."
    if inc == True:
        pov "Mom, you're going to deepthroat my cock again!"
    else:
        pov "[mother], you're going to deepthroat my cock again!"
    mom "Mhmmm!"
    "You force her further down your shaft, squeezing it into her throat. Her wet tongue hugging the sides of your cock."
    scene edited lroom custom 15 # Niocle Kneeling - MC cock deepthroat
    mom "<gag> Hngh... <cough>"
    pov "Oh God! Keep going whore!"
    mom "HNNN. <choke>"
    pov "I love when you're choking on my cock. I can tell how much you love it!"
    "You push your cock in even deeper. She gags more, but is clearly eager to please you."
    mom "MHMMM. <cough>"
    "You finally let her pull herself off your shaft, she gasps for air. Her drool still covering your shaft."
    scene edited lroom custom 16 # Nicole Kneeling - Looking up to MC
    pov "That was fantastic slut!"
    mom "I'm glad I could please you."
    "You take of your shirt and toss it behind you."
    pov "How did I get this lucky? Who knew I was being raised by such a slut?!"
    mom "I was just thinking the same thing..."
    "You reach down and help her stand. Eagerly pulling her close and tasting her chest."
    scene edited lroom custom 17 # Nicole and MC - Standing Embrace
    pov "Hmmm. <lick>"
    if inc == True:
        mom "Oh son!"
    else:
        mom "Oh [pov]!"
    mom "Hnnng..."
    mom "I can't wait any longer! I need you!"
    "[mother] turns towards the couch and bends over."
    scene edited lroom custom 18 # Nicole - Bent over couch - Ass facing MC
    mom "I need you inside me!"
    mom "Please... Fuck me! Shove that huge cock inside me!"
    pov "With pleasure whore!"
    "You move in behind her and shove your cock inside her warm, wet pussy."
    scene edited lroom custom 19 # Nicole and MC - Standing Doggy Fucking
    with vpunch
    mom "Hnng!"
    pov "Fuck, you're so tight! You like that? Tell me how much you want it."
    with vpunch
    mom "Shit, baby you feel so good! Fuck me! I want your cock to rip me apart!"
    mom "Hmmm... hah!"
    with vpunch
    mom "I'm getting close! Fuck! Don't stop! Don't fucking stop!"
    pov "Oh I'm not going to stop. I'mn going to fuck you silly!"
    with vpunch
    if inc == True:
        pov "Are you ready to cum on your son's cock, slut?!"
    else:
        pov "Are you ready to cum on my cock, slut?!"
    "You fuck her harder."
    with vpunch
    mom "Fuck! Yes, yesss! I'm going to cum. I'm going to CUM!"
    scene edited lroom custom 20 # Nicole and MC - Standing Doggy Nicole Cumming
    mom "AAAAHNNG!"
    with vpunch
    pov "That right! Cum for me whore!"
    mom "Ohhh... hah... hnng."
    with vpunch
    pov "I can feel those little tremors. You're still cumming!"
    mom "Hnnng... So good..."
    mom "Mmmmm..."
    "[mother] falls back in the couch, taking a quick moment to catch her breath and then she looks over to you, seductively."
    scene edited lroom custom 21 # Nicole on couch - Teasing/Inviting MC
    mom "That was fucking amazing! God, everytime you fuck me it just gets better and better."
    pov "Did you expect anything less of me?!?"
    mom "Ha! No. I know better than to underestimate you."
    mom "Well, I think it's time for you to finished too. Don't you think?"
    pov "Yes it is. Get ready to take my cock again, slut!"
    "You grab her legs and lift them apart as she lets herself fall back onto the couch. You slide back into her with ease."
    scene edited lroom custom 22 # Nicole and MC - Missionary Fucking
    pov "Hmmm... I love your wet dripping pussy. It feels so damn good!"
    mom "Hnng. Take me baby. Use my body! I'm your slut! Just yours!"
    "You start thrusting inside her faster. Her pleas exciting you."
    pov "I'm getting close."
    mom "Yes baby! Cum for me. Fill your cum-dumpster!"
    pov "Ohhh fuck... I'm going to cum!"
    mom "YES! Cum baby! Cum inside me!"
    scene edited lroom custom 23 # Nicole and MC - Missionary MC Cumming
    pov "ARRNNGHH!!!"
    with vpunch
    mom "Oh fuck! Keep pumping me full of your cum!"
    pov "Hnngg!"
    with vpunch
    mom "Hmmm... So full..."
    pov "Hah..."
    pov "That was awesome..."
    mom "Mmhmm."
    "You both sit back and catch your breath."
    scene edited lroom custom 24 # Nicole on couch - Cute and MC looking down
    pov "Well you're going to need to get used to this."
    if inc == True:
        mom "Oh? The feeling of my son's cum dripping out my used pussy?"
    else:
        mom "Oh? The feeling of your cum dripping out my used pussy?"
    pov "Always. But I was talking about being used by me, whenever and wherever I want."
    mom "Hnng..."
    pov "Clean this up. I don't want to deal with Bruce getting all pouty faced if he saw this."
    mom "<giggle> ok."
    "You leave her to clean up place."
    $ bonuslroomchoice = False
    jump weekendacchoose
