

label dlh_nicole:
    call screen dlh_nicole1

screen dlh_nicole1():

    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/dlh_background.png" xpos 152 ypos 106
        add "gui/icons/desc_nicole.png" xpos 1410 ypos 198
        text "Activate helper" xpos 786 ypos 122
        if nicole_help_simple_love == True:
            add "gui/icons/dlh_simple_green_idle.png" xpos 183 ypos 198
        if nicole_help_full_love == True:
            add "gui/icons/dlh_full_green_idle.png" xpos 356 ypos 198
        if nicole_help_simple_corruption == True:
            add "gui/icons/dlh_simple_green_idle.png" xpos 563 ypos 198
        if nicole_help_full_corruption == True:
            add "gui/icons/dlh_full_green_idle.png" xpos 734 ypos 198
        imagebutton auto "gui/icons/dlh_deactivate_%s.png" xpos 1175 ypos 122 action (Hide('dlh_nicole1'), Jump('dlh_deactivate')) hovered tt.Action ("Deactivate the helper") focus_mask True

        text "Love path" xpos 258 ypos 257
        text "Corruption path" xpos 606 ypos 257
        if NTR == True:
            text "NTR" xpos 1087 ypos 257
        text "Activate helper" xpos 786 ypos 122


        if nicole_help_simple_love == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 183 ypos 198 action (Hide ('dlh_nicole1'), Jump('dlh_simple_love_nic')) hovered tt.Action ("Activate the simple helper") focus_mask True
        if nicole_help_full_love == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 356 ypos 198 action (Hide ('dlh_nicole1'), Jump('dlh_full_love_nic')) hovered tt.Action ("Activate the full helper") focus_mask True
        if nicole_help_more_love == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 224 ypos 410 action (Hide ('dlh_nicole1'), Jump('dlh_more_love_nic')) hovered tt.Action ("Show more info") focus_mask True
        if nicole_help_more_love == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 224 ypos 410 action (Hide ('dlh_nicole1'), Jump('dlh_hide_love_nic')) hovered tt.Action ("Hide") focus_mask True

        if nicole_help_simple_corruption == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 563 ypos 198 action (Hide ('dlh_nicole1'), Jump('dlh_simple_corruption_nic')) hovered tt.Action ("Activate the simple helper") focus_mask True
        if nicole_help_full_corruption == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 734 ypos 198 action (Hide ('dlh_nicole1'), Jump('dlh_full_corruption_nic')) hovered tt.Action ("Activate the full helper") focus_mask True
        if nicole_help_more_corruption == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 601 ypos 410 action (Hide ('dlh_nicole1'), Jump('dlh_more_corruption_nic')) hovered tt.Action ("Show more info") focus_mask True
        if nicole_help_more_corruption == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 601 ypos 410 action (Hide ('dlh_nicole1'), Jump('dlh_hide_corruption_nic')) hovered tt.Action ("Hide") focus_mask True





        imagebutton auto "gui/icons/dlh_close_%s.png" xpos 1604 ypos 122 action (Hide ('dlh_nicole1'), Jump('dlh')) focus_mask True



    vbox:
        xpos 174 ypos 312
        if ndate21 == False:
            text "{size=-17}- Go with [mother]{/size}"
            text "{size=-17}to her first date{/size}"
        if ndate21 == True and gangmember == False and momlove < 50:
            text "{size=-17}- Become a gangmember{/size}"
            text "{size=-17}and gain more love{/size}"
        if ndate21 == True and gangmember == True and momlove >= 50 and basenicfirst == False:
            text "{size=-17}- Meet [mother] in the{/size}"
            text "{size=-17}livingroom{/size}"
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == False:
            text "{size=-17}- Go with [mother]{/size}"
            text "{size=-17}to her second date{/size}"
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True:
            text "{size=-17}- Go with her in the basement.{/size}"
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True:
            text "{size=-17}- Meet her in the parentsroom{/size}"
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True and proom19first == True:
            text "{size=-17}- End of this path for now{/size}"


    frame:
        area (174, 500, 339, 475)
        has side "c r"
        viewport id "nicole_love_vp":
            draggable True
            mousewheel True
            has vbox:
                xpos 174 ypos 500
            if nicole_help_more_love == True:
                text "{size=-17}- Go with [mother] to her first date on the weekend.{/size}"
                text "{size=-17}- Become a gangmember and gain 50 love.{/size}"
                text "{size=-17}- Meet [mother] in the livingroom at 10pm.{/size}"
                text "{size=-17}- Go with [mother] to her first second on the weekend.{/size}"
                text "{size=-17}- Go with [mother] to the basement at 10pm.{/size}"
                text "{size=-17}- Meet [mother] in the parentsroom at 7pm.{/size}"
                text "{size=-17}- End of this path for now{/size}"
        vbar value YScrollValue ("nicole_love_vp")



    vbox:
        xpos 563 ypos 312
        if ndate21 == False:
            text "{size=-17}- Go with [mother]"
            text "{size=-17}to her first date{/size}"
        if ndate21 == True and gangmember == False and momcorruption < 30:
            text "{size=-17}- Become a gangmember{/size}"
            text "{size=-17}and gain more corruption{/size}"
        if ndate21 == True and gangmember == True and momlove >= 30 and basenicfirst == False:
            text "{size=-17}- Meet [mother] in the{/size}"
            text "{size=-17}livingroom{/size}"
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == False:
            text "{size=-17}- Go with [mother]{/size}"
            text "{size=-17}to her second date{/size}"
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == False:
            text "{size=-17}- Go with her in the basement.{/size}"
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == True:
            text "{size=-17}- Meet her in the parentsroom{/size}"
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == True and proom19first == True:
            text "{size=-17}- End of this path for now{/size}"


    frame:
        area (563, 500, 339, 475)
        has side "c r"
        viewport id "nicole_corruption_vp":
            draggable True
            mousewheel True
            has vbox:
                xpos 563 ypos 500
            if nicole_help_more_corruption == True:
                text "{size=-17}- Go with [mother] to her first date on the weekend.{/size}"
                text "{size=-17}- Become a gangmember and gain 30 corruption.{/size}"
                text "{size=-17}- Meet [mother] in the livingroom at 10pm.{/size}"
                text "{size=-17}- Go with [mother] to her first second on the weekend.{/size}"
                text "{size=-17}- Go with [mother] to the basement at 10pm.{/size}"
                text "{size=-17}- Meet [mother] in the parentsroom at 7pm.{/size}"
                text "{size=-17}- End of this path for now{/size}"
        vbar value YScrollValue ("nicole_corruption_vp")


    vbox:
        xpos 981 ypos 337
        if NTR == True:
            text "{b}General hints{/b}"
            text "{size=-17}- Hold relationship on 5 or lower{/size}"
            text "{size=-17}then you can see events{/size}"
            text "{size=-17}on different times at{/size}"
            text "{size=-17}different places.{/size}"


    frame:
        xalign .5
        text tt.value



label dlh_simple_love_nic:
    $ nicole_help_simple_love = True
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = False
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    $ player_help_full_gang = False
    "The simple helper is now activated."
    jump dlh_nicole


label dlh_full_love_nic:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = True
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = False
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    $ player_help_full_gang = False
    "The full helper is now activated."
    jump dlh_nicole


label dlh_more_love_nic:
    $ nicole_help_more_love = True
    jump dlh_nicole


label dlh_hide_love_nic:
    $ nicole_help_more_love = False
    jump dlh_nicole


label dlh_simple_corruption_nic:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = True
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = False
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    $ player_help_full_gang = False
    "The simple helper is now activated."
    jump dlh_nicole


label dlh_full_corruption_nic:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = True
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = False
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    $ player_help_full_gang = False
    "The full helper is now activated."
    jump dlh_nicole


label dlh_more_corruption_nic:
    $ nicole_help_more_corruption = True
    jump dlh_nicole


label dlh_hide_corruption_nic:
    $ nicole_help_more_corruption = False
    jump dlh_nicole