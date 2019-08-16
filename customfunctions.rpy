#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

screen checkdarkerpaths_nicole():
    tag screenzy

    if perma_voyeur_nicole == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('nicole_voyeur', True), SetVariable('nicole_ntr', False), SetVariable('nicole_revenge', False), SetVariable('nicole_sadist', False), Return(None))

    elif perma_ntr_nicole == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('nicole_voyeur', False), SetVariable('nicole_ntr', True), SetVariable('nicole_revenge', False), SetVariable('nicole_sadist', False), Return(None))

    elif perma_revenge_nicole == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('nicole_voyeur', False), SetVariable('nicole_ntr', False), SetVariable('nicole_revenge', True), SetVariable('nicole_sadist', False), Return(None))

    elif perma_sadist_nicole == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('nicole_voyeur', False), SetVariable('nicole_ntr', False), SetVariable('nicole_revenge', False), SetVariable('nicole_sadist', True), Return(None))

    else:
        modal True
        default tt = Tooltip ("Select Path")

        hbox xalign .5 yalign .1:

            imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" action (Hide('checkdarkerpaths'), SetVariable('nicole_voyeur', True), SetVariable('nicole_ntr', False), SetVariable('nicole_revenge', False), SetVariable('nicole_sadist', False), Return(None)) hovered tt.Action ("Voyeur") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" action (Hide('checkdarkerpaths'), SetVariable('nicole_voyeur', False), SetVariable('nicole_ntr', True), SetVariable('nicole_revenge', False), SetVariable('nicole_sadist', False), Return(None)) hovered tt.Action ("NTR") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" action (Hide('checkdarkerpaths'), SetVariable('nicole_voyeur', False), SetVariable('nicole_ntr', False), SetVariable('nicole_revenge', True), SetVariable('nicole_sadist', False), Return(None)) hovered tt.Action ("Revenge") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" action (Hide('checkdarkerpaths'), SetVariable('nicole_voyeur', False), SetVariable('nicole_ntr', False), SetVariable('nicole_revenge', False), SetVariable('nicole_sadist', True), Return(None)) hovered tt.Action ("Sadist") focus_mask True

        frame:
            if tt.value == "" or tt.value ==" ":
                background None
            xalign .5
            text tt.value at center

screen checkdarkerpaths_alexis():
    tag screenzy

    if perma_voyeur_alexis == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('alexis_voyeur', True), SetVariable('alexis_ntr', False), SetVariable('alexis_revenge', False), SetVariable('alexis_sadist', False), Return(None))

    elif perma_ntr_alexis == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('alexis_voyeur', False), SetVariable('alexis_ntr', True), SetVariable('alexis_revenge', False), SetVariable('alexis_sadist', False), Return(None))

    elif perma_revenge_alexis == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('alexis_voyeur', False), SetVariable('alexis_ntr', False), SetVariable('alexis_revenge', True), SetVariable('alexis_sadist', False), Return(None))

    elif perma_sadist_alexis == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('alexis_voyeur', False), SetVariable('alexis_ntr', False), SetVariable('alexis_revenge', False), SetVariable('alexis_sadist', True), Return(None))

    else:
        modal True
        default tt = Tooltip ("Select Path")

        hbox xalign .5 yalign .1:

            imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" action (Hide('checkdarkerpaths'), SetVariable('alexis_voyeur', True), SetVariable('alexis_ntr', False), SetVariable('alexis_revenge', False), SetVariable('alexis_sadist', False), Return(None)) hovered tt.Action ("Voyeur") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" action (Hide('checkdarkerpaths'), SetVariable('alexis_voyeur', False), SetVariable('alexis_ntr', True), SetVariable('alexis_revenge', False), SetVariable('alexis_sadist', False), Return(None)) hovered tt.Action ("NTR") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" action (Hide('checkdarkerpaths'), SetVariable('alexis_voyeur', False), SetVariable('alexis_ntr', False), SetVariable('alexis_revenge', True), SetVariable('alexis_sadist', False), Return(None)) hovered tt.Action ("Revenge") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" action (Hide('checkdarkerpaths'), SetVariable('alexis_voyeur', False), SetVariable('alexis_ntr', False), SetVariable('alexis_revenge', False), SetVariable('alexis_sadist', True), Return(None)) hovered tt.Action ("Sadist") focus_mask True

        frame:
            if tt.value == "" or tt.value ==" ":
                background None
            xalign .5
            text tt.value at center

screen checkdarkerpaths_cassandra():
    tag screenzy

    if perma_voyeur_cassandra == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('cassandra_voyeur', True), SetVariable('cassandra_ntr', False), SetVariable('cassandra_revenge', False), SetVariable('cassandra_sadist', False), Return(None))

    elif perma_ntr_cassandra == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('cassandra_voyeur', False), SetVariable('cassandra_ntr', True), SetVariable('cassandra_revenge', False), SetVariable('cassandra_sadist', False), Return(None))

    elif perma_revenge_cassandra == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('cassandra_voyeur', False), SetVariable('cassandra_ntr', False), SetVariable('cassandra_revenge', True), SetVariable('cassandra_sadist', False), Return(None))

    elif perma_sadist_cassandra == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('cassandra_voyeur', False), SetVariable('cassandra_ntr', False), SetVariable('cassandra_revenge', False), SetVariable('cassandra_sadist', True), Return(None))

    else:
        modal True
        default tt = Tooltip ("Select Path")

        hbox xalign .5 yalign .1:

            imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" action (Hide('checkdarkerpaths'), SetVariable('cassandra_voyeur', True), SetVariable('cassandra_ntr', False), SetVariable('cassandra_revenge', False), SetVariable('cassandra_sadist', False), Return(None)) hovered tt.Action ("Voyeur") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" action (Hide('checkdarkerpaths'), SetVariable('cassandra_voyeur', False), SetVariable('cassandra_ntr', True), SetVariable('cassandra_revenge', False), SetVariable('cassandra_sadist', False), Return(None)) hovered tt.Action ("NTR") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" action (Hide('checkdarkerpaths'), SetVariable('cassandra_voyeur', False), SetVariable('cassandra_ntr', False), SetVariable('cassandra_revenge', True), SetVariable('cassandra_sadist', False), Return(None)) hovered tt.Action ("Revenge") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" action (Hide('checkdarkerpaths'), SetVariable('cassandra_voyeur', False), SetVariable('cassandra_ntr', False), SetVariable('cassandra_revenge', False), SetVariable('cassandra_sadist', True), Return(None)) hovered tt.Action ("Sadist") focus_mask True

        frame:
            if tt.value == "" or tt.value ==" ":
                background None
            xalign .5
            text tt.value at center

screen checkdarkerpaths_irina():
    tag screenzy

    if perma_voyeur_irina == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('irina_voyeur', True), SetVariable('irina_ntr', False), SetVariable('irina_revenge', False), SetVariable('irina_sadist', False), Return(None))

    elif perma_ntr_irina == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('irina_voyeur', False), SetVariable('irina_ntr', True), SetVariable('irina_revenge', False), SetVariable('irina_sadist', False), Return(None))

    elif perma_revenge_irina == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('irina_voyeur', False), SetVariable('irina_ntr', False), SetVariable('irina_revenge', True), SetVariable('irina_sadist', False), Return(None))

    elif perma_sadist_irina == True:
        timer 0.01 action (Hide('checkdarkerpaths'), SetVariable('irina_voyeur', False), SetVariable('irina_ntr', False), SetVariable('irina_revenge', False), SetVariable('irina_sadist', True), Return(None))

    else:
        modal True
        default tt = Tooltip ("Select Path")

        hbox xalign .5 yalign .1:

            imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" action (Hide('checkdarkerpaths'), SetVariable('irina_voyeur', True), SetVariable('irina_ntr', False), SetVariable('irina_revenge', False), SetVariable('irina_sadist', False), Return(None)) hovered tt.Action ("Voyeur") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" action (Hide('checkdarkerpaths'), SetVariable('irina_voyeur', False), SetVariable('irina_ntr', True), SetVariable('irina_revenge', False), SetVariable('irina_sadist', False), Return(None)) hovered tt.Action ("NTR") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" action (Hide('checkdarkerpaths'), SetVariable('irina_voyeur', False), SetVariable('irina_ntr', False), SetVariable('irina_revenge', True), SetVariable('irina_sadist', False), Return(None)) hovered tt.Action ("Revenge") focus_mask True
            imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" action (Hide('checkdarkerpaths'), SetVariable('irina_voyeur', False), SetVariable('irina_ntr', False), SetVariable('irina_revenge', False), SetVariable('irina_sadist', True), Return(None)) hovered tt.Action ("Sadist") focus_mask True

        frame:
            if tt.value == "" or tt.value ==" ":
                background None
            xalign .5
            text tt.value at center

#----- Custom Outfit Options -----
label corruptionmenu_nicole:
    call screen corruptionoutfitmenu_nicole

screen corruptionoutfitmenu_nicole():
    modal True
    default tt = Tooltip ("Corruption Options")
    tag screenzy

    hbox xalign .5 yalign .1:

        if vlroom8momtalknight2 == True and momcorruption > momlove:
            if momcorruption >= 10 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_fondle_ass_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8momfondle')) hovered tt.Action ("Fondle her ass [cr1]") focus_mask True
            if momcorruption >= 20 and nicolereddresswear == True or momcorruption >= 20 and nicolebabydollwear == True or momcorruption >= 20 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_fondle_tits_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8fondletits')) hovered tt.Action ("Fondle her tits [cr1]") focus_mask True
            if momcorruption >= 30 and nicolereddresswear == True or momcorruption >= 30 and  nicolebabydollwear == True or momcorruption >= 30 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_rub_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8rubcor')) hovered tt.Action ("Rub yourself on her [cr1]") focus_mask True
            if momcorruption >= 40 and nicolereddresswear == True or momcorruption >= 40 and  nicolebabydollwear == True or momcorruption >= 40 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_french_kiss_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8frenchkiss')) hovered tt.Action ("Give her a French Kiss [cr1]") focus_mask True
            if momcorruption >= 50 and nicolereddresswear == True and mombasementcorsecond == True or momcorruption >= 50 and  nicolebabydollwear == True and mombasementcorsecond == True:
                imagebutton auto "gui/icons/icon_finger_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8fingerpussy')) hovered tt.Action ("Rub her pussy [cr1]") focus_mask True
            if momcorruption >= 60 and  nicolereddresswear == True and mombasementcorsecond == True or momcorruption >= 60 and  nicolebabydollwear == True and mombasementcorsecond == True or momcorruption >= 60 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                imagebutton auto "gui/icons/icon_handjob_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8handjob')) hovered tt.Action ("Handjob [cr1]") focus_mask True
            if momcorruption >= 70 and nicolereddresswear == True and mombasementcorsecond == True or momcorruption >= 70 and  nicolebabydollwear == True and mombasementcorsecond == True or momcorruption >= 70 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8blowjob')) hovered tt.Action ("Blowjob [cr1]") focus_mask True
            if  momcorruption >= 80 and nicolereddresswear == True and mombasementcorsecond == True or momcorruption >= 80 and  nicolebabydollwear == True and mombasementcorsecond == True or momcorruption >= 80 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                imagebutton auto "gui/icons/icon_sex_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8sex')) hovered tt.Action ("Fuck her [cr1]") focus_mask True
            #----- Custom -----
            if momcorruption >= 10 and nicolesweaterpantswear == True or momcorruption >= 10 and nicolerobewear == True or momcorruption >= 10 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_unihand_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8caressarm_cor')) hovered tt.Action ("Caress her arm [cr1]") focus_mask True
            if momcorruption >= 20 and nicolesweaterpantswear == True or momcorruption >= 20 and nicolerobewear == True or momcorruption >= 20 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_hold_hands_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8holdhands_cor')) hovered tt.Action ("Hold hands with her [cr1]") focus_mask True
            if momcorruption >= 30 and nicolesweaterpantswear == True or momcorruption >= 30 and nicolerobewear == True or momcorruption >= 30 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_mouth_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8kiss_cor')) hovered tt.Action ("Kiss her [cr1]") focus_mask True
            if momcorruption >= 40 and nicolesweaterpantswear == True or momcorruption >= 40 and nicolerobewear == True or momcorruption >= 40 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_rub_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8rublove_cor')) hovered tt.Action ("Stand close to her [cr1]") focus_mask True
            if momcorruption >= 50 and nicolesweaterpantswear == True or momcorruption >= 50 and nicolerobewear == True or momcorruption >= 50 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_french_kiss_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8frenchkisslove_cor')) hovered tt.Action ("Give her a French Kiss [cr1]") focus_mask True
            if momcorruption >= 60 and nicolesweaterpantswear == True or momcorruption >= 60 and nicolerobewear == True or momcorruption >= 60 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_handjob_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8handjoblove_cor')) hovered tt.Action ("Get a handjob [cr1]") focus_mask True

        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8momicon')) hovered tt.Action ("Cancel") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

label lovemenu_nicole:
    call screen loveoutfitmenu_nicole

screen loveoutfitmenu_nicole():
    modal True
    default tt = Tooltip ("Love Options")
    tag screenzy

    hbox xalign .5 yalign .1:

        if vlroom8momtalknight2 == True and momlove > momcorruption:
            if momlove >= 10 and nicolesweaterpantswear == True or momlove >= 10 and nicolerobewear == True or momlove >= 10 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_unihand_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8caressarm')) hovered tt.Action ("Caress her arm [lv1]") focus_mask True
            if momlove >= 20 and nicolesweaterpantswear == True or momlove >= 20 and nicolerobewear == True or momlove >= 20 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_hold_hands_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8holdhands')) hovered tt.Action ("Hold hands with her [lv1]") focus_mask True
            if momlove >= 30 and nicolesweaterpantswear == True or momlove >= 30 and nicolerobewear == True or momlove >= 30 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8kiss')) hovered tt.Action ("Kiss her [lv1]") focus_mask True
            if momlove >= 40 and nicolesweaterpantswear == True or momlove >= 40 and nicolerobewear == True or momlove >= 40 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_rub_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8rublove')) hovered tt.Action ("Stand close to her [lv1]") focus_mask True
            if momlove >= 50 and nicolesweaterpantswear == True or momlove >= 50 and nicolerobewear == True or momlove >= 50 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_french_kiss_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8frenchkisslove')) hovered tt.Action ("Give her a French Kiss [lv1]") focus_mask True
            if momlove >= 60 and nicolesweaterpantswear == True or momlove >= 60 and nicolerobewear == True or momlove >= 60 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "gui/icons/icon_handjob_love_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8handjoblove')) hovered tt.Action ("Get a handjob [lv1]") focus_mask True
            #----- Custom -----
            if momlove >= 10 and nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_fondle_ass_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8momfondle_love')) hovered tt.Action ("Fondle her ass [lv1]") focus_mask True
            if momlove >= 20 and nicolereddresswear == True or momlove >= 20 and  nicolebabydollwear == True or momlove >= 20 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_fondle_tits_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8fondletits_love')) hovered tt.Action ("Fondle her tits [lv1]") focus_mask True
            if momlove >= 30 and nicolereddresswear == True or momlove >= 30 and  nicolebabydollwear == True or momlove >= 30 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_rub_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8rubcor_love')) hovered tt.Action ("Rub yourself on her [lv1]") focus_mask True
            if momlove >= 40 and nicolereddresswear == True or momlove >= 40 and  nicolebabydollwear == True or momlove >= 40 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False:
                imagebutton auto "images/edited/gui/vice/icon_french_kiss_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8frenchkiss_love')) hovered tt.Action ("Give her a French Kiss [lv1]") focus_mask True
            if momlove >= 50 and nicolereddresswear == True and mombasementcorsecond == True or momlove >= 50 and  nicolebabydollwear == True and mombasementcorsecond == True:
                imagebutton auto "images/edited/gui/vice/icon_finger_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8fingerpussy_love')) hovered tt.Action ("Rub her pussy [lv1]") focus_mask True
            if momlove >= 60 and nicolereddresswear == True and mombasementcorsecond == True or momlove >= 60 and  nicolebabydollwear == True and mombasementcorsecond == True or momlove >= 60 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                imagebutton auto "images/edited/gui/vice/icon_handjob_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8handjob_love')) hovered tt.Action ("Handjob [lv1]") focus_mask True
            if momlove >= 70 and nicolereddresswear == True and mombasementcorsecond == True or momlove >= 70 and  nicolebabydollwear == True and mombasementcorsecond == True or momlove >= 70 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                imagebutton auto "images/edited/gui/vice/icon_blowjob_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8blowjob_love')) hovered tt.Action ("Blowjob [lv1]") focus_mask True
            if momlove >= 80 and nicolereddresswear == True and mombasementcorsecond == True or momlove >= 80 and  nicolebabydollwear == True and mombasementcorsecond == True or momlove >= 80 and  nicolereddresswear == False and nicolebabydollwear == False and nicolesweaterpantswear == False and nicolerobewear == False and mombasementcorsecond == True:
                imagebutton auto "images/edited/gui/vice/icon_sex_corruption_%s.png" action (Hide('corruptionoutfitmenu_nicole'), Jump('lroom8sex_love')) hovered tt.Action ("Fuck her [lv1]") focus_mask True

        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('loveoutfitmenu_nicole'), Jump('lroom8momicon')) hovered tt.Action ("Cancel") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

label skiptotheweekend:
    $ day = 6
    jump weekendstart

#----- Used to update name after loading from an old save -----
label after_load:
    hide screen locations
    if renpy.seen_label("tutorial") == True:
        if povname == None:
            $ povname = renpy.input(_("So what is your first name?")) or _("Sam")
            $ povname = povname.strip()
            if povname == "":
                $ povname = "Sam"
            $ pov = Character("[povname]", who_color="0066cc", what_color="ffffff")
            $ povi = Character("[povname]", what_italic=True, who_color="0066cc", what_color="ff8000")
        if inc == True:
            if nicolename == None:
                $ nicolename = "Nicole"
                $ momname = "Mom"
        else:
            if nicolename == None:
                $ nicolename = "Nicole"
                $ momname = "Nicole"
        $ mother = Character("[nicolename]", who_color="ea9aff", what_color="ea9aff")
        $ mom = Character("[momname]", who_color="ea9aff", what_color="ea9aff")
        if inc == True:
            $ dadname = "Dad"
        else:
            $ dadname = "Bruce"
        $ dad = Character("[dadname]", who_color="ff3533", what_color="ff3533")
        if bsname == None:
            $ bsname = renpy.input(_("Enter a custom name for Ruby or leave blank for default...")) or _("Cassandra")
            $ bsname = bsname.strip()
            if bsname == "":
                $ bsname = "Cassandra"
                $ bs = Character("[bsname]", who_color="ea9aff", what_color="ea9aff")
        if lsname == None:
            $ lsname = renpy.input(_("Enter a custom name for Ruby or leave blank for default....")) or _("Alexis")
            $ lsname = lsname.strip()
            if lsname == "":
                $ lsname = "Alexis"
            $ ls = Character("[lsname]", who_color="ea9aff", what_color="ea9aff")
        if irinafirstmeet == True:
            if irinaname == None:
                $ irinaname = renpy.input(_("Enter a custom name for Irina or leave blank for default...")) or _("Irina")
                $ irinaname = irinaname.strip()
                if irinaname == "":
                    $ irinaname = "Irina"
                $ irina = Character("[irinaname]", who_color="ea9aff", what_color="ea9aff")
        if katefirstmeet == True:
            if katename == None:
                $ katename = renpy.input(_("Enter a custom name for Kate or leave blank for default...")) or _("Kate")
                $ katename = katename.strip()
                if katename == "":
                    $ katename = "Kate"
                $ kate = Character("[katename]", who_color="ea9aff", what_color="ea9aff")
        if mirandafirstmeet == True:
            if mirandaname == None:
                $ mirandaname = renpy.input(_("Enter a custom name for Miranda or leave blank for default...")) or _("Miranda")
                $ mirandaname = mirandaname.strip()
                if mirandaname == "":
                    $ mirandaname = "Miranda"
                $ miranda = Character("[mirandaname]", who_color="ea9aff", what_color="ea9aff")
        if susanfirstmeet == True:
            if susanname == None:
                $ susanname = renpy.input(_("Enter a custom name for Susan or leave blank for default...")) or _("Susan")
                $ susanname = susanname.strip()
                if susanname == "":
                    $ susanname = "Susan"
                $ susan = Character("[susanname]", who_color="ea9aff", what_color="ea9aff")
        if vivianfirstmeet == True:
            if vivianname == None:
                $ vivianname = renpy.input(_("Enter a custom name for Vivian or leave blank for default...")) or _("Vivian")
                $ vivianname = vivianname.strip()
                if vivianname == "":
                    $ vivianname = "Vivian"
                $ vivian = Character("[vivianname]", who_color="ea9aff", what_color="ea9aff")
        if rubyfirstmeet == True:
            if rubyname == None:
                $ rubyname = renpy.input(_("Enter a custom name for Ruby or leave blank for default...")) or _("Ruby")
                $ rubyname = rubyname.strip()
                if rubyname == "":
                    $ rubyname = "Ruby"
                $ ruby = Character("[rubyname]", who_color="ea9aff", what_color="ea9aff")
        show screen locations
    else:
        show screen locations
    return
