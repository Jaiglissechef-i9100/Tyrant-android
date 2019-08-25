

label lroom:
    if activateirinadate == True:
        jump irinadatetemple
    if activateirinalesbian == True:
        jump lesbiandate
    if activateirinalesbianntr == True:
        jump lesbiandatentr
    $ roomlroom = True
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
    show screen locations
    if dtime == 7:
        scene main morning living room
    elif dtime == 8:
        if nicolereddresswear == True:
            scene main 08am living room 001cc1
        elif nicolebabydollwear == True:
            scene main 08am living room 001cc2
        elif nicolesweaterpantswear == True:
            scene main 08am living room 001cl1
        elif nicolerobewear == True:
            scene main 08am living room 001cl2
        else:
            scene main 8am living room
    elif dtime == 10 and kitchen9mix == False:
        scene main 10am living room
    elif dtime == 14:
        if nicolereddresswear == True:
            scene main 2pm living room 001cc1
        elif nicolebabydollwear == True:
            scene main 2pm living room 001cc2
        elif nicolesweaterpantswear == True:
            scene main 2pm living room 001cl1
        elif nicolerobewear == True:
            scene main 2pm living room 001cl2
        else:
            scene main 2pm living room
    elif dtime == 15 and irinafirstmeet == False or dtime == 15 and irinafirstmeet == True and irinacorruption > 5 or dtime == 15 and irinafirstmeet == True and irinalove >= 5:
        scene main 3pm living room
    elif dtime == 21:
        scene main 9pm living room
    elif dtime == 22:
        scene main 10pm living room
    elif dtime == 23 and momrelationship >= 6 and lroom10mcwin == True:
        scene main 11pm living room
    else:
        scene main day living room
    call screen lroom1


screen lroom1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 14:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 818 ypos 507 action (Hide ('lroom1'), Jump('lroom8momicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 15 and irinafirstmeet == False or dtime == 15 and irinafirstmeet == True and irinacorruption > 5 or dtime == 15 and irinafirstmeet == True and irinalove > 5 or dtime == 22:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1106 ypos 287 action (Hide ('lroom1'), Jump('lroom8momicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 23 and momrelationship >= 6 and lroom10mcwin == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1106 ypos 287 action (Hide ('lroom1'), Jump('lroom8momicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 8:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1145 ypos 401 action (Hide ('lroom1'), Jump('lroom8momicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 10 and kitchen9mix == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1145 ypos 401 action (Hide ('lroom1'), Jump('lroom8momicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 21 and frontdoorddfirst == True and basementkey == False or dtime == 21 and gangmemberaccept >= 1 and basementkey == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 875 ypos 293 action (Hide ('lroom1'), Jump('lroom8momicon')) hovered tt.Action ("Interact") focus_mask True


        frame:
            xalign .5
            text tt.value




label droom:
    if activateirinadate == True:
        jump irinadatetemple
    if activateirinalesbian == True:
        jump lesbiandate
    if activateirinalesbianntr == True:
        jump lesbiandatentr
    $ roomlroom = False
    $ roomdroom = True
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
    show screen locations
    if dtime == 7:
        scene main 7am dining room
    elif dtime == 8:
        scene main morning dining room
    elif dtime == 12:
        scene main 12pm dining room
        if nicolereddresswear == True:
            show 12pm001niccorruption1:
                xpos 913
                ypos 226
        elif nicolebabydollwear == True:
            show 12pm001niccorruption2:
                xpos 913
                ypos 226
        elif nicolesweaterpantswear == True:
            show 12pm001niclove1:
                xpos 913
                ypos 226
        elif nicolerobewear == True:
            show 12pm001niclove2:
                xpos 913
                ypos 226
        else:
            show 12pm001nicnormal:
                xpos 913
                ypos 226
        if alexisrockerwear == True:
            show 12pmdiningroom001alecorruption1:
                xpos 1351
                ypos 218
        elif alexislingeriewear == True:
            show 12pmdiningroom001alecorruption2:
                xpos 1351
                ypos 218
        elif alexisjeansskirtwear == True:
            show 12pmdiningroom001alelove1:
                xpos 1351
                ypos 218
        elif alexisgridwear == True:
            show 12pmdiningroom001alelove2:
                xpos 1351
                ypos 218
        else:
            show 12pmdiningroom001alenormal:
                xpos 1351
                ypos 218
        if cassandraheartdresswear == True:
            show 12pmdiningroom001cascorruption1:
                xpos 81
                ypos 485
        elif cassandralingeriewear == True:
            show 12pmdiningroom001cascorruption2:
                xpos 81
                ypos 485
        elif cassandrajeanswear == True:
            show 12pmdiningroom001caslove1:
                xpos 81
                ypos 485
        elif cassandrapajamawear == True:
            show 12pmdiningroom001caslove2:
                xpos 81
                ypos 485
        else:
            show 12pmdiningroom001casnormal:
                xpos 81
                ypos 485
    elif dtime == 13:
        if nicolereddresswear == True:
            scene main 1pm dining room 001ncc1
        elif nicolebabydollwear == True:
            scene main 1pm dining room 001ncc2
        elif nicolesweaterpantswear == True:
            scene main 1pm dining room 001ncl1
        elif nicolerobewear == True:
            scene main 1pm dining room 001ncl2
        else:
            scene main 1pm dining room
    elif dtime == 18:
        if nicolereddresswear == True:
            scene main 6pm dining roomncc1
        elif nicolebabydollwear == True:
            scene main 6pm dining roomncc2
        elif nicolesweaterpantswear == True:
            scene main 6pm dining roomncl1
        elif nicolerobewear == True:
            scene main 6pm dining roomncl2
        else:
            scene main 6pm dining room
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main day dining room
    call screen droom1

screen droom1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 7 or dtime == 12 or dtime == 13 or dtime == 18:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 757 ypos 326 action (Hide ('droom1'), Jump('droom7momicon')) hovered tt.Action ("Interact") focus_mask True


    frame:
        xalign .5
        text tt.value




label kitchen:
    if activateirinadate == True:
        jump irinadatetemple
    if activateirinalesbian == True:
        jump lesbiandate
    if activateirinalesbianntr == True:
        jump lesbiandatentr
    $ roomlroom = False
    $ roomdroom = False
    $ roomkitchen = True
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
    show screen locations
    if dtime == 7:
        scene main day kitchen
    elif dtime == 8 and showerup7amextyes == False:
        scene main 8am kitchen
    elif dtime == 9 and gangmember == True:
        jump casbasement
    elif dtime == 9 and d5rccor == True or d5rccorfuck == True or d5rcbjsw == True or d5rcbjout == True or d5rcbjdt == True:
        jump casreacdatecor
    elif dtime == 9 and d5rclove == True or d5rclovef == True or d5rclovem == True:
        jump casreacdatelove
    elif dtime == 9 and d5rcntr == True:
        jump casreacdatentr
    elif dtime == 9 and d5rccor == False and d5rccorfuck == False and d5rcbjsw == False and d5rcbjout == False and d5rcbjdt == False and d5rclove == False and d5rclovef == False and d5rclovem == False and d5rcntr == False:
        scene main 9am kitchen
    elif dtime == 11:
        if nicolereddresswear == True:
            scene main 11am kitchen 001ncc1
        elif nicolebabydollwear == True:
            scene main 11am kitchen 001ncc2
        elif nicolesweaterpantswear == True:
            scene main 11am kitchen 001ncl1
        elif nicolerobewear == True:
            scene main 11am kitchen 001ncl2
        else:
            scene main 11am kitchen
    elif dtime == 19:
        scene main 7pm kitchen
        if alexisrockerwear == True:
            show 7pmkitchen001alecorruption1:
                xpos 545
                ypos 113
        elif alexislingeriewear == True:
            show 7pmkitchen001alecorruption2:
                xpos 545
                ypos 113
        elif alexisjeansskirtwear == True:
            show 7pmkitchen001alelove1:
                xpos 545
                ypos 113
        elif alexisgridwear == True:
            show 7pmkitchen001alelove2:
                xpos 545
                ypos 113
        else:
            pass
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main day kitchen
    call screen kitchen1

screen kitchen1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 8:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1191 ypos 250 action (Hide ('kitchen1'), Jump('kitchen8lsisicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 9 and d5rccor == False and d5rccorfuck == False and d5rcbjsw == False and d5rcbjout == False and d5rcbjdt == False and d5rclove == False and d5rclovef == False and d5rclovem == False and d5rcntr == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1191 ypos 250 action (Hide ('kitchen1'), Jump('kitchen8lsisicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 11:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 989 ypos 366 action (Hide ('kitchen1'), Jump('kitchen8lsisicon')) hovered tt.Action ("Interact") focus_mask True

        if dtime == 19:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 989 ypos 366 action (Hide ('kitchen1'), Jump('kitchen8lsisicon')) hovered tt.Action ("Interact") focus_mask True


    frame:
        xalign .5
        text tt.value



label lsisroom:
    if activateirinadate == True:
        jump irinadatetemple
    if activateirinalesbian == True:
        jump lesbiandate
    if activateirinalesbianntr == True:
        jump lesbiandatentr
    $ roomlroom = False
    $ roomdroom = False
    $ roomkitchen = False
    $ roomalexis = True
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
    show screen locations
    if dtime == 7 or dtime == 8:
        scene main lil sis room morning
    elif dtime == 14 and lilsisrelationship >= 6:
        scene main 2pm floor
    elif dtime == 21:
        scene main 9pm lil sis room
    elif dtime == 23 and lilsisrelationship >= 6 or dtime == 24 or dtime == 25 or dtime == 2 or dtime == 3:
        scene main room upstairs
    elif dtime == 22:
        scene main 10pm lil sis room
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main lil sis room
    call screen lsisroom1

screen lsisroom1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 23 or dtime == 24:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1022 ypos 363 action (Hide ('lsisroom1'), Jump('lsisroomicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 21 or dtime == 14 and lilsisrelationship >= 6:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 746 ypos 260 action (Hide ('lsisroom1'), Jump('lsisroomicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 22:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 989 ypos 366 action (Hide ('lsisroom1'), Jump('lsisroomicon')) hovered tt.Action ("Interact") focus_mask True


    frame:
        xalign .5
        text tt.value




label bsisroom:
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
    $ roomcassandra = True
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
    show screen locations
    if dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main room upstairs
    call screen bsisroom1

screen bsisroom1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 7 or dtime == 8 or dtime == 14 or dtime == 23 or dtime == 24:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1022 ypos 363 action (Hide ('bsisroom1'), Jump('bsis78icon')) hovered tt.Action ("Interact") focus_mask True


    frame:
        xalign .5
        text tt.value



label mcroom:
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
    $ roommc = True
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
    show screen locations
    if dtime == 7 or dtime == 8:
        scene main mc room morning
    elif dtime == 17 and setupnopron == False and setuppron == False and vdroom13lilsisbetlost == True:
        scene main 5pm mc room a
    elif dtime == 17 and setupnopron == True and vdroom13lilsisbetlost == True or dtime == 17 and setuppron == True and vdroom13lilsisbetlost == True:
        scene main 5pm mc room b
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main mc room day
    call screen mcroom1

screen mcroom1():

    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_action_%s.png" xpos 882 ypos 450 action (Hide ('mcroom1'), Jump('mcroomicon')) hovered tt.Action ("Interact") focus_mask True


    frame:
        xalign .5
        text tt.value




label showerup:
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
    $ roomshowerup = True
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
    show screen locations
    if dtime == 7 or dtime == 20 or dtime == 22:
        scene main shower door upstairs
    elif dtime == 15 and sp2pmextend == True:
        scene main shower door upstairs
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main shower upstairs
    call screen showerup1

screen showerup1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 7 or dtime == 20 or dtime == 22 or dtime == 15 and sp2pmextend == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1022 ypos 363 action (Hide ('showerup1'), Jump('showerup7icon')) hovered tt.Action ("Interact") focus_mask True


    frame:
        xalign .5
        text tt.value



label showerdown:
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
    $ roomshowerdown = True
    $ roomfrontdoor = False
    $ roombasement = False
    $ roomparents = False
    $ roomtown = False
    $ roomtanning = False
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
    if dtime == 16 and lesbiandate1 == True and lesbiandate2 == False:
        $ messagepush = True
        $ messageirina = 2
        $ irinanotification += 1
    show screen locations
    if dtime == 10 and kitchen9mix == True:
        scene main shower door downstairs
    elif dtime == 15 or dtime == 7:
        scene main shower door downstairs
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main shower downstairs
    call screen showerdown1

screen showerdown1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 10 and kitchen9mix == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 950 ypos 360 action (Hide ('showerdown1'), Jump('showerdownicon')) hovered tt.Action ("Interact") focus_mask True

        if dtime == 15:
            if momrelationship <= 5 and NTR == True:
                imagebutton auto "gui/icons/icon_action_%s.png" xpos 950 ypos 360 action (Hide ('showerdown1'), Jump('showerdownicon')) hovered tt.Action ("Interact") focus_mask True
            elif momrelationship >= 6:
                imagebutton auto "gui/icons/icon_action_%s.png" xpos 950 ypos 360 action (Hide ('showerdown1'), Jump('showerdownicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 7 and momdrugfirst == True and momsecret == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 950 ypos 360 action (Hide ('showerdown1'), Jump('nicolesecret')) hovered tt.Action ("What's happening?") focus_mask True


    frame:
        xalign .5
        text tt.value


label frontdoor:
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
    $ roomfrontdoor = True
    $ roombasement = False
    $ roomparents = False
    $ roomtown = False
    $ roomtanning = False
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
    if dtime == 16 and lesbiandate1 == True and lesbiandate2 == False:
        $ messagepush = True
        $ messageirina = 2
        $ irinanotification += 1
    show screen locations
    if dtime == 7 or dtime == 8:
        scene main morning front door
    elif dtime == 13 and d5rccorfuck == False and d5rcbjsw == False and d5rcbjout == False and d5rcbjdt == False and d5rclovef == False and d5rcntr == False:
        scene main 1pm front door
    elif dtime == 20 and frontdoorddfirst == False:
        scene main 8pm front door
    elif dtime == 21 and irinafirstmeet == True and club20extend == False:
        scene main 9pm front door
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main day front door
    call screen frontdoor1

screen frontdoor1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 20 and frontdoorddfirst == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 989 ypos 366 action (Hide ('frontdoor1'), Jump('frontdooricon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 13 and d5rccorfuck == False and d5rcbjsw == False and d5rcbjout == False and d5rcbjdt == False and d5rclovef == False and d5rcntr == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1106 ypos 287 action (Hide ('frontdoor1'), Jump('frontdooricon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 21 and irinafirstmeet == True and club20extend == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 944 ypos 150 action (Hide ('frontdoor1'), Jump('frontdooricon')) hovered tt.Action ("Interact") focus_mask True


    frame:
        xalign .5
        text tt.value



label basement:
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
    $ roombasement = True
    $ roomparents = False
    $ roomtown = False
    $ roomtanning = False
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
    if dtime == 16 and lesbiandate1 == True and lesbiandate2 == False:
        $ messagepush = True
        $ messageirina = 2
        $ irinanotification += 1
    show screen locations
    if dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main basement door
    call screen basement1

screen basement1():

    default tt = Tooltip (" ")

    fixed:

        if dtime == 23 and NTR == True and momrelationship < 6 and momntr == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1274 ypos 390 action (Hide ('basement1'), Jump('basementicon')) hovered tt.Action ("Interact") focus_mask True

        if dtime == 24 and NTR == True and momrelationship < 6 and momntr == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1274 ypos 390 action (Hide ('basement1'), Jump('basementicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 23 and lroom10mcwin == True and gangmember == True and momlove >= 50 or dtime == 23 and lroom10mcwin == True and gangmember == True and momcorruption >= 30:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1274 ypos 390 action (Hide ('basement1'), Jump('base10pmnic')) hovered tt.Action ("Enter the basement") focus_mask True
        if dtime == 16 and gangmember == True and selldrugs == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1274 ypos 390 action (Hide ('basement1'), Jump('sellingdrugs1')) hovered tt.Action ("Enter the basement") focus_mask True
        if dtime == 16 and gangmember == True and selldrugs == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1274 ypos 390 action (Hide ('basement1'), Jump('sellingdrugs2')) hovered tt.Action ("Enter the basement") focus_mask True
        if dtime == 17 and gangmember == True and basecasfirst == True and NTR == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1274 ypos 390 action (Hide ('basement1'), Jump('casbasementntr')) hovered tt.Action ("Enter the basement") focus_mask True
        if dtime == 22 and gangmember == True and mombasementcorsecond == True and basement10pmnicoleouting == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1274 ypos 390 action (Hide ('basement1'), Jump('basementnicoleoutingcorruption')) hovered tt.Action ("Enter the basement with [mother]") focus_mask True
        if dtime == 22 and gangmember == True and mombasementlovesecond == True and momlove > momcorruption and basement10pmnicoleouting == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1274 ypos 390 action (Hide ('basement1'), Jump('basementnicoleoutinglove')) hovered tt.Action ("Enter the basement with [mother]") focus_mask True
        if dtime == 22 and gangmember == True and basecassecond == True and basement10cassandraouting == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1074 ypos 390 action (Hide ('basement1'), Jump('basementcassandraoutingcorruption')) hovered tt.Action ("Enter the basement with [bs]") focus_mask True
        if dtime == 22 and gangmember == True and basecassecond == True and basement10cassandraouting == False and basement10pmnicoleouting == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1074 ypos 390 action (Hide ('basement1'), Jump('basementcassandraoutingcorruptionfail')) hovered tt.Action ("Enter the basement with [bs]") focus_mask True
        if dtime == 22 and gangmember == True and basement10cassandraouting == True and basement10pmnicoleouting == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1174 ypos 490 action (Hide ('basement1'), Jump('baseorgystart')) hovered tt.Action ("Join the orgy") focus_mask True



    frame:
        xalign .5
        text tt.value



label parentsroom:
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
    $ roomparents = True
    $ roomtown = False
    $ roomtanning = False
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
    if dtime == 16 and lesbiandate1 == True and lesbiandate2 == False:
        $ messagepush = True
        $ messageirina = 2
        $ irinanotification += 1
    show screen locations
    if dtime == 19 and basement10pmnicoleouting == False:
        scene main 7pm parents room
    if dtime == 19 and basement10pmnicoleouting == True and proom19first == False:
        scene main parents room door
    elif dtime == 20:
        scene main 8pm parents room
    elif dtime == 24 and momrelationship >= 6 and lroom10mcwin == True:
        scene main 0am parents room
    elif dtime == 15 and irinafirstmeet == False:
        hide screen locations
        scene main 3pm living room
        "You hear something in the livingroom and go there."
        jump lroom15talk
    else:
        scene main parents room door
    call screen parentsroom1

screen parentsroom1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 20:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 942 ypos 267 action (Hide ('parentsroom1'), Jump('parentsroomicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 24 and momrelationship >= 6 and lroom10mcwin == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1022 ypos 363 action (Hide ('parentsroom1'), Jump('parentsroomicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 19 and basement10pmnicoleouting == False:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 746 ypos 260 action (Hide ('parentsroom1'), Jump('parentsroomicon')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 19 and basement10pmnicoleouting == True and proom19first == False and momcorruption >= momlove:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 946 ypos 460 action (Hide ('parentsroom1'), Jump('proom19extcorruption')) hovered tt.Action ("Interact") focus_mask True
        if dtime == 19 and basement10pmnicoleouting == True and proom19first == False and momcorruption < momlove:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 946 ypos 460 action (Hide ('parentsroom1'), Jump('proom19extlove')) hovered tt.Action ("Interact") focus_mask True

    frame:
        xalign .5
        text tt.value




label skip:
    show screen dlhs
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
    $ roomweekend = False
    $ showerup7amextyes = False
    if messageirina == 1 or messageirina == 2:
        $ messageirina = 0
        $ irinanotification = 0
        $ messagepush = False
    if replyirinayes == 1 or replyirinayes == 2:
        $ replyirinayes = 0
    if replyirinano == 1 or replyirinano == 2:
        $ replyirinano = 0
    hide screen locations
    hide screen townl
    scene black
    "You go to sleep."
    if momrelationship < 6 and momntr == True and NTR == True:
        jump kitchen2am
    if NTR == True and lilsisrelationship <= 5 and davidealexisfriends == True:
        jump basement2am
    if meet4am == True:
        $ dtime = 4
        scene black
        "You woke up."
        pov "{i}It's 4am. I should meet with [ls].{/i}"
        jump base4amal
    if hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard

label night:
    if momntr == True:
        $ momrelationship -= 10
        if momrelationship < 0:
            $ momrelationship = 0
    if bigsisntr == True:
        $ bigsisrelationship -= 5
        if bigsisrelationship < 0:
            $ bigsisrelationship = 0
    if lilsisntr == True:
        $ lilsisrelationship -= 5
        if lilsisrelationship < 0:
            $ lilsisrelationship = 0
    if irinantr == True:
        $ irinarelationship -= 3
        if irinarelationship < 0:
            $ irinarelationship = 0
    if susanntr == True:
        $ susanrelationship -= 3
        if susanrelationship < 0:
            $ susanrelationship = 0
    if katentr == True:
        $ katerelationship -= 3
        if katerelationship < 0:
            $ katerelationship = 0
    if vivianntr == True:
        $ vivianrelationship -= 3
        if vivianrelationship < 0:
            $ vivianrelationship = 0

    $ giftflowersdaya = False
    $ giftcondomsdaya = False
    $ giftchocolatedaya = False
    $ giftflowersdayn = False
    $ giftcondomsdayn = False
    $ giftchocolatedayn = False
    $ giftflowersdayc = False
    $ giftcondomsdayc = False
    $ giftchocolatedayc = False
    $ giftflowersdayi = False
    $ giftcondomsdayi = False
    $ giftchocolatedayi = False
    $ giftflowersdays = False
    $ giftcondomsdays = False
    $ giftchocolatedays = False
    $ k2amon = False
    $ club20extend = False
    $ sp2pmextend = False
    $ kitchenmix9 = False
    $ selldrugsamount = 0
    $ vkitchen8lsisrubass = False
    $ lroom10mcwin = False
    if day == 0:
        $ day = 1
    elif day == 1:
        $ weekendactivities = 0
        $ day = 2
    elif day == 2:
        $ day = 3
    elif day == 3:
        $ day = 4
    elif day == 4:
        $ day = 5
    elif day == 5:
        $ day = 6
        jump weekendstart
    elif day == 6:
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

label skip1:
    if dtime < 25:
        $ dtime += 1
        jump mcroom
    else:
        jump skip

label skip2:
    if dtime < 25:
        $ dtime += 1
        jump town
    else:
        jump skip



label nighthard:
    $ momrelationship -= 20
    if momrelationship < 0:
        $ momrelationship = 0
    $ bigsisrelationship -= 20
    if bigsisrelationship < 0:
        $ bigsisrelationship = 0
    $ lilsisrelationship -= 20
    if lilsisrelationship < 0:
        $ lilsisrelationship = 0
    if irinafirstmeet == True:
        $ irinarelationship -= 20
        if irinarelationship < 0:
            $ irinarelationship = 0
    if susanfirstmeet == True:
        $ susanrelationship -= 20
        if susanrelationship < 0:
            $ susanrelationship = 0
    if katefirstmeet == True:
        $ katerelationship -= 20
        if katerelationship < 0:
            $ katerelationship = 0
    if vivianfirstmeet == True:
        $ vivianrelationship -= 20
        if vivianrelationship < 0:
            $ vivianrelationship = 0

    $ giftflowersdaya = False
    $ giftcondomsdaya = False
    $ giftchocolatedaya = False
    $ giftflowersdayn = False
    $ giftcondomsdayn = False
    $ giftchocolatedayn = False
    $ giftflowersdayc = False
    $ giftcondomsdayc = False
    $ giftchocolatedayc = False
    $ giftflowersdayi = False
    $ giftcondomsdayi = False
    $ giftchocolatedayi = False
    $ giftflowersdays = False
    $ giftcondomsdays = False
    $ giftchocolatedays = False
    $ k2amon = False
    $ club20extend = False
    $ sp2pmextend = False
    $ kitchenmix9 = False
    $ selldrugsamount = 0
    $ vkitchen8lsisrubass = False
    $ lroom10mcwin = False
    if day == 0:
        $ day = 1
    elif day == 1:
        $ weekendactivities = 0
        $ day = 2
    elif day == 2:
        $ day = 3
    elif day == 3:
        $ day = 4
    elif day == 4:
        $ day = 5
    elif day == 5:
        $ day = 6
        jump weekendstart
    elif day == 6:
        $ day = 1
    if adatekiss == True and d1ranormal == False and d1ralove == False and d1racor == False and d1racorf == False and d1rantrdavideyb == False and b4ralove == False and b4racor == False and b4rantrdaviden == False and b4rantrdavidey == False and b4rantrdavidei == False:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
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