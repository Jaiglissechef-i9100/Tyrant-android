



label droom7momicon():
    call screen droom7momicon1

screen droom7momicon1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 7:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 761 ypos 222 action (Hide ('droom7momicon1'), Jump('droom7momtalk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 786 ypos 470 action (Hide ('droom7momicon1'), Jump('droom7momlook')) hovered tt.Action ("Look at tits") focus_mask True

        if dtime == 13:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1104 ypos 236 action (Hide ('droom7momicon1'), Jump('droom13talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1118 ypos 627 action (Hide ('droom7momicon1'), Jump('droom13look')) hovered tt.Action ("Look at tits") focus_mask True
        if dtime == 12:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 807 ypos 153 action (Hide ('droom7momicon1'), Jump('droom12talk')) hovered tt.Action ("Talk") focus_mask True
        if dtime == 18:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 807 ypos 153 action (Hide ('droom7momicon1'), Jump('droom18talk')) hovered tt.Action ("Talk") focus_mask True

    frame:
        xalign .5
        text tt.value


label lroom8momicon:
    call screen lroom8momicon1

screen lroom8momicon1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 14:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 840 ypos 605 action (Hide ('lroom8momicon1'), Jump('lroom14momcloser')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 15 and irinafirstmeet == False or dtime == 15 and irinafirstmeet == True and irinacorruption > 5 or dtime == 15 and irinafirstmeet == True and irinalove >= 5:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1431 ypos 458 action (Hide ('lroom8momicon1'), Jump('lroom15tits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1143 ypos 615 action (Hide ('lroom8momicon1'), Jump('lroom15crotch')) hovered tt.Action ("Look at crotch") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1271 ypos 153 action (Hide ('lroom8momicon1'), Jump('lroom15talk')) hovered tt.Action ("Talk") focus_mask True
        if dtime == 8:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1231 ypos 405 action (Hide ('lroom8momicon1'), Jump('lroom8momlook')) hovered tt.Action ("Look at ass") focus_mask True
            if nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1188 ypos 327 action (Hide ('lroom8momicon1'), Jump('lroom8momtalk')) hovered tt.Action ("Talk") focus_mask True
            if nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_slap_%s.png" xpos 1203 ypos 479 action (Hide ('lroom8momicon1'), Jump('lroom8momslap')) hovered tt.Action ("Slap ass [cr1]") focus_mask True

            if vlroom8momtalknight2 == True and momcorruption >= 10 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_fondle_ass_%s.png" xpos 1231 ypos 563 action (Hide ('lroom8momicon1'), Jump('lroom8momfondle')) hovered tt.Action ("Fondle her ass [cr1]") focus_mask True
            if vlroom8momtalknight2 == True and momcorruption >= 20 and momcorruption > momlove and nicolereddresswear == True or vlroom8momtalknight2 == True and momcorruption >= 20 and momcorruption > momlove and nicolebabydollwear == True or vlroom8momtalknight2 == True and momcorruption >= 20 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_fondle_tits_%s.png" xpos 1292 ypos 479 action (Hide ('lroom8momicon1'), Jump('lroom8fondletits')) hovered tt.Action ("Fondle her tits [cr1]") focus_mask True
            if vlroom8momtalknight2 == True and momcorruption >= 30 and momcorruption > momlove and nicolereddresswear == True or vlroom8momtalknight2 == True and momcorruption >= 30 and momcorruption > momlove and nicolebabydollwear == True or vlroom8momtalknight2 == True and momcorruption >= 30 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_rub_corruption_%s.png" xpos 1300 ypos 376 action (Hide ('lroom8momicon1'), Jump('lroom8rubcor')) hovered tt.Action ("Rub yourself on her [cr1]") focus_mask True
            if vlroom8momtalknight2 == True and momcorruption >= 40 and momcorruption > momlove and nicolereddresswear == True or vlroom8momtalknight2 == True and momcorruption >= 40 and momcorruption > momlove and nicolebabydollwear == True or vlroom8momtalknight2 == True and momcorruption >= 40 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_french_kiss_corruption_%s.png" xpos 1267 ypos 275 action (Hide ('lroom8momicon1'), Jump('lroom8frenchkiss')) hovered tt.Action ("Give her a French Kiss [cr1]") focus_mask True
            if vlroom8momtalknight2 == True and momcorruption >= 50 and momcorruption > momlove and nicolereddresswear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 50 and momcorruption > momlove and nicolebabydollwear == True and mombasementcorsecond == True:
                imagebutton auto "gui/icons/icon_finger_corruption_%s.png" xpos 1366 ypos 222 action (Hide ('lroom8momicon1'), Jump('lroom8fingerpussy')) hovered tt.Action ("Rub her pussy [cr1]") focus_mask True
            if vlroom8momtalknight2 == True and momcorruption >= 60 and momcorruption > momlove and nicolereddresswear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 60 and momcorruption > momlove and nicolebabydollwear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 60 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                imagebutton auto "gui/icons/icon_handjob_corruption_%s.png" xpos 1389 ypos 321 action (Hide ('lroom8momicon1'), Jump('lroom8handjob')) hovered tt.Action ("Handjob [cr1]") focus_mask True
            if vlroom8momtalknight2 == True and momcorruption >= 70 and momcorruption > momlove and nicolereddresswear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 70 and momcorruption > momlove and nicolebabydollwear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 70 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" xpos 1389 ypos 434 action (Hide ('lroom8momicon1'), Jump('lroom8blowjob')) hovered tt.Action ("Blowjob [cr1]") focus_mask True
            if vlroom8momtalknight2 == True and momcorruption >= 80 and momcorruption > momlove and nicolereddresswear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 80 and momcorruption > momlove and nicolebabydollwear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 80 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                imagebutton auto "gui/icons/icon_sex_corruption_%s.png" xpos 1371 ypos 554 action (Hide ('lroom8momicon1'), Jump('lroom8sex')) hovered tt.Action ("Fuck her [cr1]") focus_mask True

            if vlroom8momtalknight2 == True and momlove >= 10 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 10 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 10 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 1136 ypos 222 action (Hide ('lroom8momicon1'), Jump('lroom8caressarm')) hovered tt.Action ("Caress her arm [lv1]") focus_mask True
            if vlroom8momtalknight2 == True and momlove >= 20 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 20 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 20 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_hold_hands_%s.png" xpos 1055 ypos 260 action (Hide ('lroom8momicon1'), Jump('lroom8holdhands')) hovered tt.Action ("Hold hands with her [lv1]") focus_mask True
            if vlroom8momtalknight2 == True and momlove >= 30 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 30 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 30 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 970 ypos 222 action (Hide ('lroom8momicon1'), Jump('lroom8kiss')) hovered tt.Action ("Kiss her [lv1]") focus_mask True
            if vlroom8momtalknight2 == True and momlove >= 40 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 40 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 40 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_rub_love_%s.png" xpos 893 ypos 247 action (Hide ('lroom8momicon1'), Jump('lroom8rublove')) hovered tt.Action ("Stand close to her [lv1]") focus_mask True
            if vlroom8momtalknight2 == True and momlove >= 50 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 50 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 50 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_french_kiss_love_%s.png" xpos 812 ypos 285 action (Hide ('lroom8momicon1'), Jump('lroom8frenchkisslove')) hovered tt.Action ("Give her a French Kiss [lv1]") focus_mask True
            if vlroom8momtalknight2 == True and momlove >= 60 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 60 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 60 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_handjob_love_%s.png" xpos 739 ypos 325 action (Hide ('lroom8momicon1'), Jump('lroom8handjoblove')) hovered tt.Action ("Get a handjob [lv1]") focus_mask True


        if dtime == 10 and kitchen9mix == False:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 875 ypos 833 action (Hide ('lroom8momicon1'), Jump('lroom10bsistits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1184 ypos 815 action (Hide ('lroom8momicon1'), Jump('lroom10bsiscrotch')) hovered tt.Action ("Look at crotch") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1077 ypos 483 action (Hide ('lroom8momicon1'), Jump('lroom10bsisfeet')) hovered tt.Action ("Look at feet") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 663 ypos 623 action (Hide ('lroom8momicon1'), Jump('lroom10bsistalk')) hovered tt.Action ("Talk") focus_mask True
        if dtime == 21 and frontdoorddfirst == True or dtime == 21 and gangmemberaccept >= 1:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 894 ypos 168 action (Hide ('lroom8momicon1'), Jump('lroom21talk')) hovered tt.Action ("Talk") focus_mask True
        if dtime == 22:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1188 ypos 327 action (Hide ('lroom8momicon1'), Jump('lroom22talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1431 ypos 458 action (Hide ('lroom8momicon1'), Jump('lroom22ass')) hovered tt.Action ("Look at ass") focus_mask True
        if dtime == 23:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 882 ypos 348 action (Hide ('lroom8momicon1'), Jump('lroom11pmtalk')) hovered tt.Action ("Talk") focus_mask True

        frame:
            xalign .5
            text tt.value



label kitchen8lsisicon:
    call screen kitchen8lsisicon1

screen kitchen8lsisicon1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 8:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1278 ypos 198 action (Hide ('kitchen8lsisicon1'), Jump('kitchen8lsistalk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_scare_%s.png" xpos 1281 ypos 293 action (Hide ('kitchen8lsisicon1'), Jump('kitchen8lsisscare')) hovered tt.Action ("Scare her") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 954 ypos 276 action (Hide ('kitchen8lsisicon1'), Jump('kitchen8lsislookface')) hovered tt.Action ("Look closer at face") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1234 ypos 459 action (Hide ('kitchen8lsisicon1'), Jump('kitchen8lsislooktits')) hovered tt.Action ("Look closer at tits") focus_mask True

        if dtime == 9:
            imagebutton auto "gui/icons/icon_scare_cor_%s.png" xpos 1281 ypos 293 action (Hide ('kitchen8lsisicon1'), Jump('kitchen9bsisscare')) hovered tt.Action ("Scare her [cr1]") focus_mask True
            imagebutton auto "gui/icons/icon_wait_%s.png" xpos 1278 ypos 198 action (Hide ('kitchen8lsisicon1'), Jump('kitchen9bsiswait')) hovered tt.Action ("Wait [lv1]") focus_mask True
        if dtime == 11:
            imagebutton auto "gui/icons/icon_slap_%s.png" xpos 1062 ypos 539 action (Hide ('kitchen8lsisicon1'), Jump('kitchen11momslap')) hovered tt.Action ("Slap ass") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 804 ypos 276 action (Hide ('kitchen8lsisicon1'), Jump('kitchen11momtalk')) hovered tt.Action ("Talk") focus_mask True

        if dtime == 19:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 452 ypos 150 action (Hide ('kitchen8lsisicon1'), Jump('kitchen19talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 944 ypos 150 action (Hide ('kitchen8lsisicon1'), Jump('kitchen19closer')) hovered tt.Action ("Go closer") focus_mask True

        frame:
            xalign .5
            text tt.value


label showerup7icon:
    call screen showerup7icon1

screen showerup7icon1():

    default tt = Tooltip (" ")

    fixed:

        if dtime == 7:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 920 ypos 615 action (Hide ('showerup7icon1'), Jump('showerup7look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 902 ypos 293 action (Hide ('showerup7icon1'), Jump('showerup7talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 1127 ypos 293 action (Hide ('showerup7icon1'), Jump('showerup7listen')) hovered tt.Action ("Listen") focus_mask True

        if dtime == 15:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 920 ypos 615 action (Hide ('showerup7icon1'), Jump('showerup15look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 1127 ypos 293 action (Hide ('showerup7icon1'), Jump('showerup15listen')) hovered tt.Action ("Listen") focus_mask True

        if dtime == 20:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 920 ypos 615 action (Hide ('showerup7icon1'), Jump('showerup20look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 902 ypos 293 action (Hide ('showerup7icon1'), Jump('showerup20talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 1127 ypos 293 action (Hide ('showerup7icon1'), Jump('showerup20listen')) hovered tt.Action ("Listen") focus_mask True

        if dtime == 22:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 920 ypos 615 action (Hide ('showerup7icon1'), Jump('showerup22look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 902 ypos 293 action (Hide ('showerup7icon1'), Jump('showerup22talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 1127 ypos 293 action (Hide ('showerup7icon1'), Jump('showerup22listen')) hovered tt.Action ("Listen") focus_mask True

        frame:
            xalign .5
            text tt.value


label bsis78icon:
    call screen bsis78icon1

screen bsis78icon1():

    default tt = Tooltip (" ")

    fixed:
        if dtime == 7 or dtime == 8 or dtime == 14 or dtime == 23 or dtime == 24:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1120 ypos 615 action (Hide ('bsis78icon1'), Jump('bsis78look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 902 ypos 293 action (Hide ('bsis78icon1'), Jump('bsis78open')) hovered tt.Action ("Open door") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 1127 ypos 293 action (Hide ('bsis78icon1'), Jump('bsis78listen')) hovered tt.Action ("Listen") focus_mask True

        frame:
            xalign .5
            text tt.value




label showerdownicon:
    call screen showerdownicon1

screen showerdownicon1():
    default tt = Tooltip (" ")

    fixed:
        if dtime == 10 or dtime == 15:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1125 ypos 683 action (Hide ('showerdownicon1'), Jump('showerd10look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 885 ypos 213 action (Hide ('showerdownicon1'), Jump('showerd10listen')) hovered tt.Action ("Listen") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1085 ypos 495 action (Hide ('showerdownicon1'), Jump('showerd10open')) hovered tt.Action ("Open") focus_mask True


    frame:
        xalign .5
        text tt.value



label mcroomicon:
    call screen mcroomicon1

screen mcroomicon1():
    default tt = Tooltip (" ")

    fixed:
        if vdroom13lilsisbetlost == True and setupnopron == False and setuppron == False and dtime == 14 or vdroom13lilsisbetlost == True and setupnopron == False and setuppron == False and dtime == 15 or vdroom13lilsisbetlost == True  and setupnopron == False and setuppron == False and dtime == 16:
            imagebutton auto "gui/icons/icon_question_%s.png" xpos 882 ypos 348 action (Hide ('mcroomicon1'), Jump('mcroomwonbetprep')) hovered tt.Action ("What can i do here?") focus_mask True

        imagebutton auto "gui/icons/icon_on_%s.png" xpos 939 ypos 174 action (Hide('mcroomicon1'), Jump('hardntron')) hovered tt.Action ("Turn hard mode on") focus_mask True
        imagebutton auto "gui/icons/icon_off_%s.png" xpos 1042 ypos 174 action (Hide('mcroomicon1'), Jump('hardntroff')) hovered tt.Action ("Turn hard mode off") focus_mask True


        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 688 ypos 138 action (Hide('mcroomicon'), Jump('cheat')) hovered tt.Action ("Cheat") focus_mask True
        if adate == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 212 ypos 338 action (Hide('mcroomicon'), Jump('temp')) hovered tt.Action ("[ls] basement") focus_mask True


        if dtime == 17:
            if setupnopron == False and setuppron == False and vdroom13lilsisbetlost == True:
                imagebutton auto "gui/icons/icon_talk_%s.png" xpos 750 ypos 450 action (Hide ('mcroomicon1'), Jump('mcroom17nomessy')) hovered tt.Action ("Talk") focus_mask True
            if setupnopron == True and vdroom13lilsisbetlost == True or dtime == 17 and setuppron == True and vdroom13lilsisbetlost == True:
                imagebutton auto "gui/icons/icon_talk_%s.png" xpos 750 ypos 450 action (Hide ('mcroomicon1'), Jump('mcroom17yesmessy')) hovered tt.Action ("Talk") focus_mask True

        imagebutton auto "gui/icons/icon_sleep_%s.png" xpos 1190 ypos 234 action (Hide ('mcroomicon1'), Jump('skip')) hovered tt.Action ("Go to sleep") focus_mask True
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 488 ypos 128 action (Hide ('mcroomicon1'), Jump('gamemusicon')) hovered tt.Action ("Turn default game music on") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 388 ypos 128 action (Hide ('mcroomicon1'), Jump('gamemusicoff')) hovered tt.Action ("Turn default game music off") focus_mask True

        if nicolereddress == 4:
            imagebutton auto "gui/icons/cloth_mcroom_red_dress_%s.png" xpos 1200 ypos 360 action (Hide ('mcroomicon1'), Jump('nicolechangered')) hovered tt.Action ("[mother] should wear the Red Dress") focus_mask True
        if nicolebabydoll == 4:
            imagebutton auto "gui/icons/cloth_mcroom_babydoll_%s.png" xpos 1300 ypos 360 action (Hide ('mcroomicon1'), Jump('nicolechangebaby')) hovered tt.Action ("[mother] should wear the Babydoll") focus_mask True
        if nicolesweaterpants == 4:
            imagebutton auto "gui/icons/cloth_mcroom_sweater_pants_%s.png" xpos 1400 ypos 360 action (Hide ('mcroomicon1'), Jump('nicolechangesweater')) hovered tt.Action ("[mother] should wear the Sweater+Pants") focus_mask True
        if nicolerobe == 4:
            imagebutton auto "gui/icons/cloth_mcroom_robe_%s.png" xpos 1500 ypos 360 action (Hide ('mcroomicon1'), Jump('nicolechangerobe')) hovered tt.Action ("[mother] should wear the Robe") focus_mask True
        imagebutton auto "gui/icons/cloth_mcroom_leggins_%s.png" xpos 1600 ypos 360 action (Hide ('mcroomicon1'), Jump('nicolechangeleggins')) hovered tt.Action ("[mother] should wear the Top+Leggins") focus_mask True

        if alexisrocker == 4:
            imagebutton auto "gui/icons/cloth_mcroom_rocker_%s.png" xpos 1200 ypos 560 action (Hide ('mcroomicon1'), Jump('alexischangerocker')) hovered tt.Action ("[ls] should wear the Rocker Outfit") focus_mask True
        if alexislingerie == 4:
            imagebutton auto "gui/icons/cloth_mcroom_alingerie_%s.png" xpos 1300 ypos 560 action (Hide ('mcroomicon1'), Jump('alexischangelingerie')) hovered tt.Action ("[ls] should wear the Lingerie") focus_mask True
        if alexisjeansskirt == 4:
            imagebutton auto "gui/icons/cloth_mcroom_jeans_skirt_%s.png" xpos 1400 ypos 560 action (Hide ('mcroomicon1'), Jump('alexischangejeansskirt')) hovered tt.Action ("[ls] should wear the White top+Jeans skirt") focus_mask True
        if alexisgrid == 4:
            imagebutton auto "gui/icons/cloth_mcroom_grid_%s.png" xpos 1500 ypos 560 action (Hide ('mcroomicon1'), Jump('alexischangegrid')) hovered tt.Action ("[ls] should wear the Grid suit") focus_mask True
        imagebutton auto "gui/icons/cloth_mcroom_top_hot_pants_%s.png" xpos 1600 ypos 560 action (Hide ('mcroomicon1'), Jump('alexischangetophotpants')) hovered tt.Action ("[ls] should wear the Top+Hot pants") focus_mask True

        if cassandraheartdress == 4:
            imagebutton auto "gui/icons/cloth_mcroom_heart_dress_%s.png" xpos 1200 ypos 760 action (Hide ('mcroomicon1'), Jump('cassandrachangeheartdress')) hovered tt.Action ("[bs] should wear the Heart Dress") focus_mask True
        if cassandralingerie == 4:
            imagebutton auto "gui/icons/cloth_mcroom_clingerie_%s.png" xpos 1300 ypos 760 action (Hide ('mcroomicon1'), Jump('cassandrachangelingerie')) hovered tt.Action ("[bs] should wear the Lingerie") focus_mask True
        if cassandrajeans == 4:
            imagebutton auto "gui/icons/cloth_mcroom_jeans_outfit_%s.png" xpos 1400 ypos 760 action (Hide ('mcroomicon1'), Jump('cassandrachangejeans')) hovered tt.Action ("[bs] should wear the Jeans Outfit") focus_mask True
        if cassandrapajama == 4:
            imagebutton auto "gui/icons/cloth_mcroom_pajamas_%s.png" xpos 1500 ypos 760 action (Hide ('mcroomicon1'), Jump('cassandrachangepajamas')) hovered tt.Action ("[bs] should wear the Pajamas") focus_mask True
        imagebutton auto "gui/icons/cloth_mcroom_top_jeans_%s.png" xpos 1600 ypos 760 action (Hide ('mcroomicon1'), Jump('cassandrachangetopjeans')) hovered tt.Action ("[bs] should wear the Top and the Jeans") focus_mask True




        frame:
            xalign .5
            text tt.value



label lsisroomicon:
    call screen lsisroomicon1

screen lsisroomicon1():
    default tt = Tooltip (" ")

    fixed:
        if dtime == 23 or dtime == 24:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1120 ypos 615 action (Hide ('lsisroomicon1'), Jump('lsislook')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 902 ypos 293 action (Hide ('lsisroomicon1'), Jump('lsisopen')) hovered tt.Action ("Open door") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 1127 ypos 293 action (Hide ('lsisroomicon1'), Jump('lsislisten')) hovered tt.Action ("Listen") focus_mask True

        if dtime == 21:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 807 ypos 153 action (Hide ('lsisroomicon1'), Jump('lsis21talk')) hovered tt.Action ("Talk") focus_mask True

        if dtime == 14 and lilsisrelationship >= 6:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 807 ypos 153 action (Hide ('lsisroomicon1'), Jump('splace2pmtalk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_gift_%s.png" xpos 811 ypos 240 action (Hide ('lsisroomicon1'), Show('inventorygift2pmsp')) hovered tt.Action ("Give her a gift") focus_mask True

        if dtime == 22:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1271 ypos 479 action (Hide ('lsisroomicon1'), Jump('lsis22talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 720 ypos 564 action (Hide ('lsisroomicon1'), Jump('lsis22lookass')) hovered tt.Action ("Look at ass") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 426 ypos 341 action (Hide ('lsisroomicon1'), Jump('lsis22lookfeet')) hovered tt.Action ("Look at feet") focus_mask True
            imagebutton auto "gui/icons/icon_gift_%s.png" xpos 648 ypos 326 action (Hide ('lsisroomicon1'), Show('inventorygift10pmls')) hovered tt.Action ("Give her a gift") focus_mask True

        frame:
            xalign .5
            text tt.value


label frontdooricon:
    call screen frontdooricon1

screen frontdooricon1():
    default tt = Tooltip (" ")

    fixed:
        if dtime == 20 and frontdoorddfirst == False:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 990 ypos 524 action (Hide ('frontdooricon1'), Jump('frontdoorcloser')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 13:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1143 ypos 443 action (Hide ('frontdooricon1'), Jump('frontdoor13closer')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 21 and irinafirstmeet == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 438 ypos 636 action (Hide ('frontdooricon1'), Jump('frontdoor21closer')) hovered tt.Action ("Go closer") focus_mask True


        frame:
            xalign .5
            text tt.value


label parentsroomicon:
    call screen parentsroomicon1

screen parentsroomicon1():
    default tt = Tooltip (" ")

    fixed:
        if dtime == 24 and momrelationship >= 6:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1077 ypos 150 action (Hide ('parentsroomicon1'), Jump('proom24closer')) hovered tt.Action ("Go closer") focus_mask True

        if dtime == 20:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1344 ypos 482 action (Hide ('parentsroomicon1'), Jump('proomlooktits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1058 ypos 765 action (Hide ('parentsroomicon1'), Jump('proomlookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 684 ypos 150 action (Hide ('parentsroomicon1'), Jump('proomlookpicture')) hovered tt.Action ("Look at picture") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1077 ypos 150 action (Hide ('parentsroomicon1'), Jump('proomtalk')) hovered tt.Action ("Talk") focus_mask True

        if dtime == 19 and basement10pmnicoleouting == False:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 942 ypos 260 action (Hide ('parentsroomicon1'), Jump('proom19watch')) hovered tt.Action ("Watch") focus_mask True


        frame:
            xalign .5
            text tt.value


label basementicon:
    call screen basementicon1

screen basementicon1():
    default tt = Tooltip (" ")

    fixed:
        if dtime == 16:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1151 ypos 938 action (Hide ('basementicon1'), Jump('basementlook')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 1106 ypos 287 action (Hide ('basementicon1'), Jump('basementtalk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1251 ypos 732 action (Hide ('basementicon1'), Jump('basementopen')) hovered tt.Action ("Open") focus_mask True

        if dtime == 23 and NTR == True and momrelationship < 6 and momntr == True:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1151 ypos 938 action (Hide ('basementicon1'), Jump('basementlook')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 1106 ypos 287 action (Hide ('basementicon1'), Jump('basement23listen')) hovered tt.Action ("Listen") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1251 ypos 732 action (Hide ('basementicon1'), Jump('basementopen')) hovered tt.Action ("Open") focus_mask True

        if dtime == 24 and NTR == True and momrelationship < 6 and momntr == True:
            imagebutton auto "gui/icons/icon_look_%s.png" xpos 1151 ypos 938 action (Hide ('basementicon1'), Jump('basementlook')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 1106 ypos 287 action (Hide ('basementicon1'), Jump('basement24listen')) hovered tt.Action ("Listen") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1251 ypos 732 action (Hide ('basementicon1'), Jump('basementopen')) hovered tt.Action ("Open") focus_mask True

        frame:
            xalign .5
            text tt.value




screen giftdr12icon():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_gift_%s.png" xpos 886 ypos 215 action (Hide ('giftdr12icon'), Show('giftdr12icon', transition=None)) hovered tt.Action ("Give someone a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" xpos 803 ypos 160 action (Hide ('giftdr12icon'), Show('inventorygiftdr12pmn', transition=None)) hovered tt.Action ("Give [mom] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" xpos 1012 ypos 160 action (Hide ('giftdr12icon'), Show('inventorygiftdr12pma', transition=None)) hovered tt.Action ("Give [ls] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" xpos 804 ypos 310 action (Hide ('giftdr12icon'), Show('inventorygiftdr12pmc', transition=None)) hovered tt.Action ("Give [bs] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 886 ypos 310 action (Hide ('giftdr12icon'), Jump('droom12talkc')) hovered tt.Action ("Don't give anyone a gift") focus_mask True
    frame:
        xalign .5
        text tt.value


screen giftfd21icon():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_gift_%s.png" xpos 905 ypos 104 action (Hide ('giftfd21icon'), Show('giftfd21icon', transition=None)) hovered tt.Action ("Give someone a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" xpos 815 ypos 104 action (Hide ('giftfd21icon'), Show('inventorygiftfd21i', transition=None)) hovered tt.Action ("Give [irina] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" xpos 1007 ypos 104 action (Hide ('giftfd21icon'), Show('inventorygiftfd21c', transition=None)) hovered tt.Action ("Give [bs] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 905 ypos 231 action (Hide ('giftfd21icon'), Jump('frontdoor21talk4')) hovered tt.Action ("Don't give anyone a gift") focus_mask True
    frame:
        xalign .5
        text tt.value