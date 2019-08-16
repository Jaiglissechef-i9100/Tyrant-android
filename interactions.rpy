#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label droom7momicon():
    call screen droom7momicon1

screen droom7momicon1():

    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 7:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('droom7momicon1'), Jump('droom7momtalk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('droom7momicon1'), Jump('droom7momlook')) hovered tt.Action ("Look at tits") focus_mask True
            #imagebutton auto "gui/icons/icon_gift_%s.png" action (Hide('droom7momicon1'), Show('inventorygift7amdr')) hovered tt.Action ("Give her a gift") focus_mask True
        if dtime == 13:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('droom7momicon1'), Jump('droom13talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('droom7momicon1'), Jump('droom13look')) hovered tt.Action ("Look at tits") focus_mask True
        if dtime == 12:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('droom7momicon1'), Jump('droom12talk')) hovered tt.Action ("Talk") focus_mask True
        if dtime == 18:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('droom7momicon1'), Jump('droom18talk')) hovered tt.Action ("Talk") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label lroom8momicon:
    call screen lroom8momicon1

screen lroom8momicon1():

    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 14:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('lroom8momicon1'), Jump('lroom14momcloser')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 15 and irinafirstmeet == False or dtime == 15 and irinafirstmeet == True and irinacorruption > 5 or dtime == 15 and irinafirstmeet == True and irinalove > 5:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lroom8momicon1'), Jump('lroom15tits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lroom8momicon1'), Jump('lroom15crotch')) hovered tt.Action ("Look at crotch") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('lroom8momicon1'), Jump('lroom15talk')) hovered tt.Action ("Talk") focus_mask True
        if dtime == 8:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8momlook')) hovered tt.Action ("Look at ass") focus_mask True
            if nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8momtalk')) hovered tt.Action ("Talk") focus_mask True
            if nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_slap_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8momslap')) hovered tt.Action ("Slap ass [cr1]") focus_mask True

            #----- Corruption Outfit Interactions -----
            #----- Custom Menu -----
            if vlroom8momtalknight2 == True and momcorruption >= 10 and momcorruption > momlove:
                imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('lroom8momicon1'), Jump('corruptionmenu_nicole')) hovered tt.Action ("Corruption Options [cr1]") focus_mask True
            #----- Original Menu -----
            #if vlroom8momtalknight2 == True and momcorruption >= 10 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_fondle_ass_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8momfondle')) hovered tt.Action ("Fondle her ass [cr1]") focus_mask True
            #if vlroom8momtalknight2 == True and momcorruption >= 20 and momcorruption > momlove and nicolereddresswear == True or vlroom8momtalknight2 == True and momcorruption >= 20 and momcorruption > momlove and nicolebabydollwear == True or vlroom8momtalknight2 == True and momcorruption >= 20 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_fondle_tits_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8fondletits')) hovered tt.Action ("Fondle her tits [cr1]") focus_mask True
            #if vlroom8momtalknight2 == True and momcorruption >= 30 and momcorruption > momlove and nicolereddresswear == True or vlroom8momtalknight2 == True and momcorruption >= 30 and momcorruption > momlove and nicolebabydollwear == True or vlroom8momtalknight2 == True and momcorruption >= 30 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_rub_corruption_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8rubcor')) hovered tt.Action ("Rub yourself on her [cr1]") focus_mask True
            #if vlroom8momtalknight2 == True and momcorruption >= 40 and momcorruption > momlove and nicolereddresswear == True or vlroom8momtalknight2 == True and momcorruption >= 40 and momcorruption > momlove and nicolebabydollwear == True or vlroom8momtalknight2 == True and momcorruption >= 40 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_french_kiss_corruption_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8frenchkiss')) hovered tt.Action ("Give her a French Kiss [cr1]") focus_mask True
            #if vlroom8momtalknight2 == True and momcorruption >= 50 and momcorruption > momlove and nicolereddresswear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 50 and momcorruption > momlove and nicolebabydollwear == True and mombasementcorsecond == True:
                #imagebutton auto "gui/icons/icon_finger_corruption_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8fingerpussy')) hovered tt.Action ("Rub her pussy [cr1]") focus_mask True
            #if vlroom8momtalknight2 == True and momcorruption >= 60 and momcorruption > momlove and nicolereddresswear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 60 and momcorruption > momlove and nicolebabydollwear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 60 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                #imagebutton auto "gui/icons/icon_handjob_corruption_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8handjob')) hovered tt.Action ("Handjob [cr1]") focus_mask True
            #if vlroom8momtalknight2 == True and momcorruption >= 70 and momcorruption > momlove and nicolereddresswear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 70 and momcorruption > momlove and nicolebabydollwear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 70 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                #imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8blowjob')) hovered tt.Action ("Blowjob [cr1]") focus_mask True
            #if vlroom8momtalknight2 == True and momcorruption >= 80 and momcorruption > momlove and nicolereddresswear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 80 and momcorruption > momlove and nicolebabydollwear == True and mombasementcorsecond == True or vlroom8momtalknight2 == True and momcorruption >= 80 and momcorruption > momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                #imagebutton auto "gui/icons/icon_sex_corruption_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8sex')) hovered tt.Action ("Fuck her [cr1]") focus_mask True

            #----- Love Outfit Interactions -----
            #----- Custom Menu -----
            if vlroom8momtalknight2 == True and momlove >= 10 and momlove > momcorruption:
                imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('lroom8momicon1'), Jump('lovemenu_nicole')) hovered tt.Action ("Love Options [lv1]") focus_mask True
            #----- Original Menu -----
            #if vlroom8momtalknight2 == True and momlove >= 10 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 10 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 10 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_unihand_love_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8caressarm')) hovered tt.Action ("Caress her arm [lv1]") focus_mask True
            #if vlroom8momtalknight2 == True and momlove >= 20 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 20 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 20 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_hold_hands_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8holdhands')) hovered tt.Action ("Hold hands with her [lv1]") focus_mask True
            #if vlroom8momtalknight2 == True and momlove >= 30 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 30 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 30 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8kiss')) hovered tt.Action ("Kiss her [lv1]") focus_mask True
            #if vlroom8momtalknight2 == True and momlove >= 40 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 40 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 40 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_rub_love_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8rublove')) hovered tt.Action ("Stand close to her [lv1]") focus_mask True
            #if vlroom8momtalknight2 == True and momlove >= 50 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 50 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 50 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_french_kiss_love_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8frenchkisslove')) hovered tt.Action ("Give her a French Kiss [lv1]") focus_mask True
            #if vlroom8momtalknight2 == True and momlove >= 60 and momcorruption < momlove and nicolesweaterpantswear == True or vlroom8momtalknight2 == True and momlove >= 60 and momcorruption < momlove and nicolerobewear == True or vlroom8momtalknight2 == True and momlove >= 60 and momcorruption < momlove and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                #imagebutton auto "gui/icons/icon_handjob_love_%s.png" action (Hide('lroom8momicon1'), Jump('lroom8handjoblove')) hovered tt.Action ("Get a handjob [lv1]") focus_mask True

        if dtime == 10 and kitchen9mix == False:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lroom8momicon1'), Jump('lroom10bsistits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lroom8momicon1'), Jump('lroom10bsiscrotch')) hovered tt.Action ("Look at crotch") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lroom8momicon1'), Jump('lroom10bsisfeet')) hovered tt.Action ("Look at feet") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('lroom8momicon1'), Jump('lroom10bsistalk')) hovered tt.Action ("Talk") focus_mask True
        if dtime == 21 and frontdoorddfirst == True or dtime == 21 and gangmemberaccept >= 1:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('lroom8momicon1'), Jump('lroom21talk')) hovered tt.Action ("Talk") focus_mask True
        if dtime == 22:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('lroom8momicon1'), Jump('lroom22talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lroom8momicon1'), Jump('lroom22ass')) hovered tt.Action ("Look at ass") focus_mask True
        if dtime == 23:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('lroom8momicon1'), Jump('lroom11pmtalk')) hovered tt.Action ("Talk") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label kitchen8lsisicon:
    call screen kitchen8lsisicon1

screen kitchen8lsisicon1():

    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 8:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen8lsistalk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_scare_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen8lsisscare')) hovered tt.Action ("Scare her") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen8lsislookface')) hovered tt.Action ("Look closer at face") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen8lsislooktits')) hovered tt.Action ("Look closer at tits") focus_mask True

        if dtime == 9:
            imagebutton auto "gui/icons/icon_scare_cor_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen9bsisscare')) hovered tt.Action ("Scare her [cr1]") focus_mask True
            imagebutton auto "gui/icons/icon_wait_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen9bsiswait')) hovered tt.Action ("Wait [lv1]") focus_mask True
            #----- Added -----
            if gangmember == True and basementkey == True and basecasfirst == True:
                imagebutton auto "gui/icons/icon_hug_%s.png" action (Hide('kitchen8lsisicon1'), Jump('casbasementrepeat')) hovered tt.Action ("Basement") focus_mask True

        if dtime == 11:
            imagebutton auto "gui/icons/icon_slap_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen11momslap')) hovered tt.Action ("Slap ass") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen11momtalk')) hovered tt.Action ("Talk") focus_mask True

        if dtime == 19:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen19talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('kitchen8lsisicon1'), Jump('kitchen19closer')) hovered tt.Action ("Go closer") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7icon:
    call screen showerup7icon1

screen showerup7icon1():

    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        if dtime == 7:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('showerup7icon1'), Jump('showerup7look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('showerup7icon1'), Jump('showerup7talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('showerup7icon1'), Jump('showerup7listen')) hovered tt.Action ("Listen") focus_mask True

        if dtime == 15:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('showerup7icon1'), Jump('showerup15look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('showerup7icon1'), Jump('showerup15listen')) hovered tt.Action ("Listen") focus_mask True

        if dtime == 20:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('showerup7icon1'), Jump('showerup20look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('showerup7icon1'), Jump('showerup20talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('showerup7icon1'), Jump('showerup20listen')) hovered tt.Action ("Listen") focus_mask True

        if dtime == 22:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('showerup7icon1'), Jump('showerup22look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('showerup7icon1'), Jump('showerup22talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('showerup7icon1'), Jump('showerup22listen')) hovered tt.Action ("Listen") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label bsis78icon:
    call screen bsis78icon1

screen bsis78icon1():

    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 7 or dtime == 8 or dtime == 14 or dtime == 23 or dtime == 24:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('bsis78icon1'), Jump('bsis78look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('bsis78icon1'), Jump('bsis78open')) hovered tt.Action ("Open door") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('bsis78icon1'), Jump('bsis78listen')) hovered tt.Action ("Listen") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerdownicon:
    call screen showerdownicon1

screen showerdownicon1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 10 or dtime == 15:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('showerdownicon1'), Jump('showerd10look')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('showerdownicon1'), Jump('showerd10listen')) hovered tt.Action ("Listen") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('showerdownicon1'), Jump('showerd10open')) hovered tt.Action ("Open") focus_mask True
        #-----Custom-----
        if dtime == 15 and momlove >= 100 and mombasementlovesecond == True and nicolerobe == 4 or dtime == 15 and momcorruption >= 100 and mombasementcorsecond == True and nicolerobe == 4:
            imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('showerdownicon1'), Jump('bonusshowernicole')) hovered tt.Action ("Bonus Shower Nicole") focus_mask True
    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label mcroomicon:
    call screen mcroomicon1

screen mcroomicon1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if vdroom13lilsisbetlost == True and setupnopron == False and setuppron == False and dtime == 14 or vdroom13lilsisbetlost == True and setupnopron == False and setuppron == False and dtime == 15 or vdroom13lilsisbetlost == True  and setupnopron == False and setuppron == False and dtime == 16:
            imagebutton auto "gui/icons/icon_question_%s.png" action (Hide('mcroomicon1'), Jump('mcroomwonbetprep')) hovered tt.Action ("What can i do here?") focus_mask True
        #----- Hard Mode removed in 0.7.1 ----- Left in for now for the Mod
        imagebutton auto "gui/icons/icon_on_%s.png" action (Hide('mcroomicon1'), Jump('hardntron')) hovered tt.Action ("Turn Hard Mode on") focus_mask True
        imagebutton auto "gui/icons/icon_off_%s.png" action (Hide('mcroomicon1'), Jump('hardntroff')) hovered tt.Action ("Turn Hard Mode off") focus_mask True

        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcroomicon'), Jump('cheat')) hovered tt.Action ("Cheat") focus_mask True

        if adate == True:
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('mcroomicon'), Jump('temp')) hovered tt.Action ("[ls] basement") focus_mask True

        #if dtime == 21: - Now Accessible Via Message App
            #imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('mcroomicon'), Jump('irinadatetemple')) hovered tt.Action ("Go on a date with [irina]") focus_mask True

        if dtime == 17:
            if setupnopron == False and setuppron == False and vdroom13lilsisbetlost == True:
                imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('mcroomicon1'), Jump('mcroom17nomessy')) hovered tt.Action ("Talk") focus_mask True
            if setupnopron == True and vdroom13lilsisbetlost == True or dtime == 17 and setuppron == True and vdroom13lilsisbetlost == True:
                imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('mcroomicon1'), Jump('mcroom17yesmessy')) hovered tt.Action ("Talk") focus_mask True

        imagebutton auto "gui/icons/icon_sleep_%s.png" action (Hide('mcroomicon1'), Jump('skip')) hovered tt.Action ("Go to sleep") focus_mask True

        #imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('mcroomicon1'), Jump('gamemusicon')) hovered tt.Action ("Turn default game music on") focus_mask True
        #imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('mcroomicon1'), Jump('gamemusicoff')) hovered tt.Action ("Turn default game music off") focus_mask True

        if nicolereddress == 4:
            imagebutton auto "gui/icons/cloth_red_dress_%s.png" action (Hide('mcroomicon1'), Jump('nicolechangered')) hovered tt.Action ("[mother] should wear the Red Dress") focus_mask True
        if nicolebabydoll == 4:
            imagebutton auto "gui/icons/cloth_babydoll_%s.png" action (Hide('mcroomicon1'), Jump('nicolechangebaby')) hovered tt.Action ("[mother] should wear the Babydoll") focus_mask True
        if nicolesweaterpants == 4:
            imagebutton auto "gui/icons/cloth_sweater_pants_%s.png" action (Hide('mcroomicon1'), Jump('nicolechangesweater')) hovered tt.Action ("[mother] should wear the Sweater+Pants") focus_mask True
        if nicolerobe == 4:
            imagebutton auto "gui/icons/cloth_robe_%s.png" action (Hide('mcroomicon1'), Jump('nicolechangerobe')) hovered tt.Action ("[mother] should wear the Robe") focus_mask True
        imagebutton auto "gui/icons/cloth_leggins_%s.png" action (Hide('mcroomicon1'), Jump('nicolechangeleggins')) hovered tt.Action ("[mother] should wear the Top+Leggins") focus_mask True

        #----- Custom -----
        if gamemusic == False:
            imagebutton auto "gui/icons/icon_listen_%s.png" xpos 488 ypos 274 action (mr.stop, Jump('enablemusic')) hovered tt.Action ("Enable Default Music") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 488 ypos 274 action (mr.stop, Jump('disablemusic')) hovered tt.Action ("Disable Default Music") focus_mask True

        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('mcroomicon1'), Jump('renamecharacters')) hovered tt.Action ("Rename Characters") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('mcroomicon1'), Jump('skiptotheweekend')) hovered tt.Action ("Skip to the Weekend") focus_mask True

        imagebutton auto "images/edited/icons/nicole_%s.png" action (Hide('mcroomicon1'), Jump('ndate21choose')) hovered tt.Action ("Go on a date with [mother]") focus_mask True
        imagebutton auto "images/edited/icons/alexis_%s.png" action (Hide('mcroomicon1'), Jump('adate1choose')) hovered tt.Action ("Go on a date with [ls]") focus_mask True
        imagebutton auto "images/edited/icons/cassandra_%s.png" action (Hide('mcroomicon1'), Jump('cdate5')) hovered tt.Action ("Go on a date with [bs]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom Menus -----
label mcroomlaptopicon:
    call screen mcroomlaptopicon1

screen mcroomlaptopicon1():
    modal True
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcroomlaptopicon1'), Jump('cheat')) hovered tt.Action ("Cheat") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('mcroomlaptopicon1'), Jump('mcroom')) hovered tt.Action ("Cancel") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

#----- Custom Menus -----
label mcroombagicon:
    call screen mcroombagicon1

screen mcroombagicon1():
    modal True
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if hardntr == False:
            imagebutton auto "gui/icons/icon_on_%s.png" action (Hide('mcroombagicon1'), Jump('hardntron')) hovered tt.Action ("Turn hard mode on") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_off_%s.png" action (Hide('mcroombagicon1'), Jump('hardntroff')) hovered tt.Action ("Turn hard mode off") focus_mask True
        if gamemusic == False:
            imagebutton auto "gui/icons/icon_listen_%s.png" action (mr.stop, Hide('mcroombagicon1'), Jump('enablemusic')) hovered tt.Action ("Enable Default Music") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_disapprove_%s.png" action (mr.stop, Hide('mcroombagicon1'), Jump('disablemusic')) hovered tt.Action ("Disable Default Music") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('mcroombagicon1'), Jump('renamecharacters')) hovered tt.Action ("Rename Characters") focus_mask True
        imagebutton auto "gui/icons/icon_sleep_%s.png" action (Hide('mcroombagicon1'), Jump('skip')) hovered tt.Action ("Go to sleep") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('mcroombagicon1'), Jump('mcroom')) hovered tt.Action ("Cancel") focus_mask True
        if vdroom13lilsisbetlost == True and setupnopron == False and setuppron == False and dtime == 14 or vdroom13lilsisbetlost == True and setupnopron == False and setuppron == False and dtime == 15 or vdroom13lilsisbetlost == True  and setupnopron == False and setuppron == False and dtime == 16:
            imagebutton auto "gui/icons/icon_question_%s.png" action (Hide('mcroombagicon1'), Jump('mcroomwonbetprep')) hovered tt.Action ("What can i do here?") focus_mask True
        if dtime == 17:
            if setupnopron == False and setuppron == False and vdroom13lilsisbetlost == True:
                imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('mcroombagicon1'), Jump('mcroom17nomessy')) hovered tt.Action ("Talk") focus_mask True
            if setupnopron == True and vdroom13lilsisbetlost == True or dtime == 17 and setuppron == True and vdroom13lilsisbetlost == True:
                imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('mcroombagicon1'), Jump('mcroom17yesmessy')) hovered tt.Action ("Talk") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

#----- Custom Menus -----
label mcroompictureicon:
    call screen mcroompictureicon1

screen mcroompictureicon1():
    modal True
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if adate == True:
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('mcroompictureicon1'), Jump('temp')) hovered tt.Action ("[ls] basement") focus_mask True
        if dtime == 21:
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('mcroomicon'), Jump('irinadatetemple')) hovered tt.Action ("Go on a date with [irina]") focus_mask True
        imagebutton auto "gui/icons/icon_feet_%s.png" action (Hide('mcroompictureicon1'), Jump('skiptotheweekend')) hovered tt.Action ("Skip to the Weekend") focus_mask True
        imagebutton auto "images/edited/icons/nicole_%s.png" action (Hide('mcroompictureicon1'), Jump('ndate21choose')) hovered tt.Action ("Go on a date with [mother]") focus_mask True
        imagebutton auto "images/edited/icons/alexis_%s.png" action (Hide('mcroompictureicon1'), Jump('adate1choose')) hovered tt.Action ("Go on a date with [ls]") focus_mask True
        imagebutton auto "images/edited/icons/cassandra_%s.png" action (Hide('mcroompictureicon1'), Jump('cdate5')) hovered tt.Action ("Go on a date with [bs]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('mcroompictureicon1'), Jump('mcroom')) hovered tt.Action ("Cancel") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

#----- Custom Menus -----
label mcroomdrawericon:
    call screen mcroomdrawericon1

screen mcroomdrawericon1():
    modal True
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if nicolereddress == 4:
            imagebutton auto "gui/icons/cloth_red_dress_%s.png" action (Hide('mcroomdrawericon1'), Jump('nicolechangered')) hovered tt.Action ("[mother] should wear the Red Dress") focus_mask True
        if nicolebabydoll == 4:
            imagebutton auto "gui/icons/cloth_babydoll_%s.png" action (Hide('mcroomdrawericon1'), Jump('nicolechangebaby')) hovered tt.Action ("[mother] should wear the Babydoll") focus_mask True
        if nicolesweaterpants == 4:
            imagebutton auto "gui/icons/cloth_sweater_pants_%s.png" action (Hide('mcroomdrawericon1'), Jump('nicolechangesweater')) hovered tt.Action ("[mother] should wear the Sweater+Pants") focus_mask True
        if nicolerobe == 4:
            imagebutton auto "gui/icons/cloth_robe_%s.png" action (Hide('mcroomdrawericon1'), Jump('nicolechangerobe')) hovered tt.Action ("[mother] should wear the Robe") focus_mask True
        imagebutton auto "gui/icons/cloth_leggins_%s.png" action (Hide('mcroomdrawericon1'), Jump('nicolechangeleggins')) hovered tt.Action ("[mother] should wear the Top+Leggins") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('mcroomdrawericon1'), Jump('mcroom')) hovered tt.Action ("Cancel") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

label lsisroomicon:
    call screen lsisroomicon1

screen lsisroomicon1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 23 or dtime == 24:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lsisroomicon1'), Jump('lsislook')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('lsisroomicon1'), Jump('lsisopen')) hovered tt.Action ("Open door") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('lsisroomicon1'), Jump('lsislisten')) hovered tt.Action ("Listen") focus_mask True

        if dtime == 21:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('lsisroomicon1'), Jump('lsis21talk')) hovered tt.Action ("Talk") focus_mask True

        if dtime == 14 and lilsisrelationship >= 6:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('lsisroomicon1'), Jump('splace2pmtalk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_gift_%s.png" action (Hide('lsisroomicon1'), Show('inventorygift2pmsp')) hovered tt.Action ("Give her a gift") focus_mask True

        if dtime == 22:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('lsisroomicon1'), Jump('lsis22talk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lsisroomicon1'), Jump('lsis22lookass')) hovered tt.Action ("Look at ass") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('lsisroomicon1'), Jump('lsis22lookfeet')) hovered tt.Action ("Look at feet") focus_mask True
            imagebutton auto "gui/icons/icon_gift_%s.png" action (Hide('lsisroomicon1'), Show('inventorygift10pmls')) hovered tt.Action ("Give her a gift") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label frontdooricon:
    call screen frontdooricon1

screen frontdooricon1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 20 and frontdoorddfirst == False:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('frontdooricon1'), Jump('frontdoorcloser')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 13:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('frontdooricon1'), Jump('frontdoor13closer')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 21 and irinafirstmeet == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('frontdooricon1'), Jump('frontdoor21closer')) hovered tt.Action ("Go closer") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label parentsroomicon:
    call screen parentsroomicon1

screen parentsroomicon1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 24 and momrelationship >= 6:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('parentsroomicon1'), Jump('proom24closer')) hovered tt.Action ("Go closer") focus_mask True

        if dtime == 20:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('parentsroomicon1'), Jump('proomlooktits')) hovered tt.Action ("Look at tits") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('parentsroomicon1'), Jump('proomlookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('parentsroomicon1'), Jump('proomlookpicture')) hovered tt.Action ("Look at picture") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('parentsroomicon1'), Jump('proomtalk')) hovered tt.Action ("Talk") focus_mask True

        if dtime == 18 and caslovefirstfuck == True:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('parentsroomicon1'), Jump('mccassandra6pmevent')) hovered tt.Action ("Open the door") focus_mask True

        if dtime == 19 and basement10pmnicoleouting == False:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('parentsroomicon1'), Jump('proom19watch')) hovered tt.Action ("Watch") focus_mask True
        elif dtime == 19 and basement10pmnicoleouting == True:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('parentsroomicon1'), Jump('proom19extlanding')) hovered tt.Action ("What is that?") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementicon:
    call screen basementicon1

screen basementicon1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 16:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('basementicon1'), Jump('basementlook')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('basementicon1'), Jump('basementtalk')) hovered tt.Action ("Talk") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementicon1'), Jump('basementopen')) hovered tt.Action ("Open") focus_mask True

        #----- Removed and momntr == True and added or dtime == 23 and hardntr == True -----
        if dtime == 23 and NTR == True and momrelationship < 6 or dtime == 23 and hardntr == True:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('basementicon1'), Jump('basementlook')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('basementicon1'), Jump('basement23listen')) hovered tt.Action ("Listen") focus_mask True
            if basementkey == True:
                imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementicon1'), Jump('basement23and24landing')) hovered tt.Action ("Open") focus_mask True
            else:
                imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementicon1'), Jump('basementopen')) hovered tt.Action ("Open") focus_mask True

        #----- Removed and momntr == True and added or dtime == 24 and hardntr == True -----
        if dtime == 24 and NTR == True and momrelationship < 6 or dtime == 24 and hardntr == True:
            imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('basementicon1'), Jump('basementlook')) hovered tt.Action ("Look") focus_mask True
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('basementicon1'), Jump('basement24listen')) hovered tt.Action ("Listen") focus_mask True
            if basementkey == True:
                imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementicon1'), Jump('basement23and24landing')) hovered tt.Action ("Open") focus_mask True
            else:
                imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementicon1'), Jump('basementopen')) hovered tt.Action ("Open") focus_mask True

        #----- Custom -----
        if dtime == 20 and NTR == True and bigsisrelationship < 6 or dtime == 20 and hardntr == True:
            imagebutton auto "gui/icons/icon_listen_%s.png" action (Hide('basementicon1'), Jump('dadcasdarkpathlisten')) hovered tt.Action ("Listen") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementicon1'), Jump('dadcasdarkpathopen')) hovered tt.Action ("Open") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

screen giftdr12icon():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_gift_%s.png" action (Hide('giftdr12icon'), Show('giftdr12icon', transition=None)) hovered tt.Action ("Give someone a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('giftdr12icon'), Show('inventorygiftdr12pmn', transition=None)) hovered tt.Action ("Give [mom] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('giftdr12icon'), Show('inventorygiftdr12pma', transition=None)) hovered tt.Action ("Give [ls] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('giftdr12icon'), Show('inventorygiftdr12pmc', transition=None)) hovered tt.Action ("Give [bs] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('giftdr12icon'), Jump('droom12talkc')) hovered tt.Action ("Don't give anyone a gift") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

screen giftfd21icon():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_gift_%s.png" action (Hide('giftfd21icon'), Show('giftfd21icon', transition=None)) hovered tt.Action ("Give someone a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('giftfd21icon'), Show('inventorygiftfd21i', transition=None)) hovered tt.Action ("Give [irina] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('giftfd21icon'), Show('inventorygiftfd21c', transition=None)) hovered tt.Action ("Give [bs] a gift") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('giftfd21icon'), Jump('frontdoor21talk4')) hovered tt.Action ("Don't give anyone a gift") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value
