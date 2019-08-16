

label town:
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
    $ roomtown = True
    $ roomtanning = False
    $ roomsubway = False
    $ roomhideout = False
    $ roomfitness = False
    $ roomclub = False
    $ roomweekend = False
    scene main town
    call screen town1

screen town1():
    default tt = Tooltip (" ")

    fixed:
        if dtime == 14 and lilsisrelationship < 6 and NTR == True and davidealexisfriends == True:
            imagebutton auto "gui/icons/icon_secret_place_%s.png" xpos 1145 ypos 299 action (Hide ('town1'), Jump('secretplace')) hovered tt.Action ("Secret place") focus_mask True
        imagebutton auto "gui/icons/icon_club_%s.png" xpos 1344 ypos 624 action (Hide ('town1'), Jump('club')) hovered tt.Action ("The Sleazy Weasel") focus_mask True
        imagebutton auto "gui/icons/icon_subway_%s.png" xpos 1764 ypos 482 action (Hide ('town1'), Jump('subway')) hovered tt.Action ("Subway") focus_mask True
        imagebutton auto "gui/icons/icon_tanning_salon_%s.png" xpos 674 ypos 542 action (Hide ('town1'), Jump('tanning')) hovered tt.Action ("Tanning Salon") focus_mask True
        imagebutton auto "gui/icons/icon_home_%s.png" xpos 375 ypos 68 action (Hide ('town1'), Jump('frontdoor')) hovered tt.Action ("Home") focus_mask True
        if dtime == 17 or dtime == 9 and fitnessmember == True:
            imagebutton auto "gui/icons/icon_fitness_studio_%s.png" xpos 512 ypos 861 action (Hide ('townl'), Jump('fitness')) hovered tt.Action ("Fitness Studio") focus_mask True

        if dtime == 10:
            add "gui/icons/nicole_small.png" xpos 1396 ypos 669
            if momrelationship < 6 and momntr == True and NTR == True and frankfirstmeet == True:
                add "gui/icons/frank_small.png" xpos 1371 ypos 669
        if dtime == 14 and lilsisrelationship < 6 and NTR == True and davidealexisfriends == True:
            add "gui/icons/davide_small.png" xpos 1174 ypos 344
            add "gui/icons/alexis_small.png" xpos 1199 ypos 344
        if dtime == 16:
            if irinafirstmeet == True:
                add "gui/icons/irina_small.png" xpos 728 ypos 588
            if irinarelationship < 6 and NTR == True and frankfirstmeet == True:
                add "gui/icons/frank_small.png" xpos 703 ypos 588
        if dtime == 17:
            add "gui/icons/nicole_small.png" xpos 728 ypos 588
            if momrelationship < 6 and momntr == True and NTR == True and frankfirstmeet == True:
                add "gui/icons/frank_small.png" xpos 703 ypos 588
            add "gui/icons/cassandra_small.png" xpos 566 ypos 908
        if dtime == 9 and momlove >= 20  and fitnessmember == True or dtime == 9 and momcorruption >= 20 and fitnessmember == True:
            add "gui/icons/nicole_small.png" xpos 566 ypos 908
        if dtime == 19:
            add "gui/icons/kate_small.png" xpos 1350 ypos 669
            add "gui/icons/martin_small.png" xpos 1365 ypos 669
            add "gui/icons/irina_small.png" xpos 1380 ypos 669
            add "gui/icons/cassandra_small.png" xpos 1396 ypos 669

        if dtime == 10 and momcorruption >= 10 and club10slapfirst == False:
            add "gui/icons/icon_new.png" xpos 1344 ypos 624
        if dtime == 19 and irinalove >= 20 and club20extendedirinalove == False:
            add "gui/icons/icon_new.png" xpos 1344 ypos 624
        if dtime == 19 and irinacorruption >= 30 and club20extendedirinacor == False:
            add "gui/icons/icon_new.png" xpos 1344 ypos 624
        if dtime == 19 and bigsiscorruption >= 20 and club20extendedcascorfirst == False:
            add "gui/icons/icon_new.png" xpos 1344 ypos 624
        if dtime == 19 and bigsiscorruption >= 40 and club20extendedcascorsecond == False:
            add "gui/icons/icon_new.png" xpos 1344 ypos 624
        if dtime == 17 and fitnessfirst == False:
            add "gui/icons/icon_new.png" xpos 512 ypos 861
        if dtime == 9 and momlove >= 20 and fitnessnicfirst == False and fitnessmember == True or dtime == 9 and momcorruption >= 20 and fitnessnicfirst == False and fitnessmember == True:
            add "gui/icons/icon_new.png" xpos 512 ypos 861

    frame:
        xalign .5
        text tt.value



label tanning:
    if activateirinadate == True:
        jump irinadatetemple
    if activateirinalesbian == True:
        jump lesbiandate
    if activateirinalesbianntr == True:
        jump lesbiandatentr
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
    $ roomtanning = True
    $ roomsubway = False
    $ roomhideout = False
    $ roomfitness = False
    $ roomclub = False
    $ roomweekend = False
    if dtime == 10 and momlove >= 20 and messagenicolelove == 0:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 40 and messagenicolelove == 1:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 60 and messagenicolelove == 2:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 80 and messagenicolelove == 3:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 22 and irinafirstmeet == True and day == 2 or dtime == 22 and irinafirstmeet == True and day == 4 or dtime == 22 and irinafirstmeet == True and day == 5:
        $ messagepush = True
        $ messageirina = 1
        $ irinanotification += 1
    show screen townl
    if dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene town tanning main
    call screen tanning1

screen tanning1():

    default tt = Tooltip (" ")

    fixed:
        if dtime > 9 and dtime < 20:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 960 ypos 477 action (Hide ('tanningicon'), Jump('tanningenter')) hovered tt.Action ("Interact") focus_mask True

    frame:
        xalign .5
        text tt.value



label subway:
    if activateirinadate == True:
        jump irinadatetemple
    if activateirinalesbian == True:
        jump lesbiandate
    if activateirinalesbianntr == True:
        jump lesbiandatentr
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
    $ roomsubway = True
    $ roomhideout = False
    $ roomfitness = False
    $ roomclub = False
    $ roomweekend = False
    if dtime == 10 and momlove >= 20 and messagenicolelove == 0:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 40 and messagenicolelove == 1:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 60 and messagenicolelove == 2:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 80 and messagenicolelove == 3:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 22 and irinafirstmeet == True and day == 2 or dtime == 22 and irinafirstmeet == True and day == 4 or dtime == 22 and irinafirstmeet == True and day == 5:
        $ messagepush = True
        $ messageirina = 1
        $ irinanotification += 1
    if dtime == 16 and lesbiandate1 == True and lesbiandate2 == False:
        $ messagepush = True
        $ messageirina = 2
        $ irinanotification += 1
    show screen townl
    if dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene town subway 3pm 001
    call screen subway1

screen subway1():

    default tt = Tooltip (" ")

    fixed:
        if day == 2 and dtime == 7 and package >= 1 or day == 2 and dtime == 8 and package >= 1:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 377 ypos 189 action (Hide ('subway1'), Jump('subwayicon')) hovered tt.Action ("Interact") focus_mask True
        if day == 4 and dtime == 7 and package >= 1 or day == 4 and dtime == 8 and package >= 1:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 377 ypos 189 action (Hide ('subway1'), Jump('subwayicon')) hovered tt.Action ("Interact") focus_mask True

    frame:
        xalign .5
        text tt.value


label hideout:
    if activateirinadate == True:
        jump irinadatetemple
    if activateirinalesbian == True:
        jump lesbiandate
    if activateirinalesbianntr == True:
        jump lesbiandatentr
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
    $ roomhideout = True
    $ roomfitness = False
    $ roomclub = False
    $ roomweekend = False
    if dtime == 10 and momlove >= 20 and messagenicolelove == 0:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 40 and messagenicolelove == 1:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 60 and messagenicolelove == 2:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 80 and messagenicolelove == 3:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 22 and irinafirstmeet == True and day == 2 or dtime == 22 and irinafirstmeet == True and day == 4 or dtime == 22 and irinafirstmeet == True and day == 5:
        $ messagepush = True
        $ messageirina = 1
        $ irinanotification += 1
    if dtime == 16 and lesbiandate1 == True and lesbiandate2 == False:
        $ messagepush = True
        $ messageirina = 2
        $ irinanotification += 1
    scene town secret secret place
    show screen townl    















label fitness:
    if activateirinadate == True:
        jump irinadatetemple
    if activateirinalesbian == True:
        jump lesbiandate
    if activateirinalesbianntr == True:
        jump lesbiandatentr
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
    $ roomfitness = True
    $ roomclub = False
    $ roomweekend = False
    if dtime == 10 and momlove >= 20 and messagenicolelove == 0:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 40 and messagenicolelove == 1:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 60 and messagenicolelove == 2:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 10 and momlove >= 80 and messagenicolelove == 3:
        $ messagepush = True
        $ messagenicolelove += 1
        $ nicolenotification += 1
    if dtime == 22 and irinafirstmeet == True and day == 2 or dtime == 22 and irinafirstmeet == True and day == 4 or dtime == 22 and irinafirstmeet == True and day == 5:
        $ messagepush = True
        $ messageirina = 1
        $ irinanotification += 1
    if dtime == 16 and lesbiandate1 == True and lesbiandate2 == False:
        $ messagepush = True
        $ messageirina = 2
        $ irinanotification += 1
    show screen townl
    if dtime == 17:
        scene town fitness fitness2
    elif dtime == 9:
        scene town fitness 9am 025
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    call screen fitness1

screen fitness1():

    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_action_%s.png" xpos 1287 ypos 218 action (Hide ('fitness1'), Jump('fitnessicon')) hovered tt.Action ("Interact") focus_mask True

    frame:
        xalign .5
        text tt.value


label club:
    if activateirinadate == True:
        jump irinadatetemple
    if activateirinalesbian == True:
        jump lesbiandate
    if activateirinalesbianntr == True:
        jump lesbiandatentr
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
    $ roomclub = True
    $ roomweekend = False
    show screen townl
    if dtime == 10:
        scene town club SW front
    elif dtime == 19:
        scene town club SW front
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene town club SW front
    call screen club1

screen club1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 10:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 851 ypos 350 action (Hide ('club1'), Jump('club19ch')) hovered tt.Action ("Enter") focus_mask True


        if dtime == 19:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 489 ypos 179 action (Hide ('club1'), Jump('club19ch')) hovered tt.Action ("Enter") focus_mask True

    frame:
        xalign .5
        text tt.value