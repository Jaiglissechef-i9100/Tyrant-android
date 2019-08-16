#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label dlh_nicole:
    call screen dlh_nicole1

screen dlh_nicole1():
    zorder 100
    modal True
    default tt = Tooltip ("")

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
        imagebutton auto "gui/icons/dlh_deactivate_%s.png" xpos 1175 ypos 122 action (Hide('dlh_nicole1'), Jump('dlh_deactivate')) hovered Notify("Deactivate the helper") focus_mask True

        text "Love path" xpos 258 ypos 257
        text "Corruption path" xpos 606 ypos 257
        if NTR == True:
            text "NTR" xpos 1087 ypos 257
        text "Activate helper" xpos 786 ypos 122

        if nicole_help_simple_love == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 183 ypos 198 action (Hide('dlh_nicole1'), Jump('dlh_simple_love_nic')) hovered Notify("Activate the simple helper") focus_mask True
        if nicole_help_full_love == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 356 ypos 198 action (Hide('dlh_nicole1'), Jump('dlh_full_love_nic')) hovered Notify("Activate the full helper") focus_mask True
        if nicole_help_more_love == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 224 ypos 410 action (Hide('dlh_nicole1'), Jump('dlh_more_love_nic')) hovered Notify("Show more info") focus_mask True
        if nicole_help_more_love == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 224 ypos 410 action (Hide('dlh_nicole1'), Jump('dlh_hide_love_nic')) hovered Notify("Hide") focus_mask True

        if nicole_help_simple_corruption == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 563 ypos 198 action (Hide('dlh_nicole1'), Jump('dlh_simple_corruption_nic')) hovered Notify("Activate the simple helper") focus_mask True
        if nicole_help_full_corruption == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 734 ypos 198 action (Hide('dlh_nicole1'), Jump('dlh_full_corruption_nic')) hovered Notify("Activate the full helper") focus_mask True
        if nicole_help_more_corruption == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 601 ypos 410 action (Hide('dlh_nicole1'), Jump('dlh_more_corruption_nic')) hovered Notify("Show more info") focus_mask True
        if nicole_help_more_corruption == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 601 ypos 410 action (Hide('dlh_nicole1'), Jump('dlh_hide_corruption_nic')) hovered Notify("Hide") focus_mask True

        imagebutton auto "gui/icons/dlh_close_%s.png" xpos 1604 ypos 122 action (Hide('dlh_nicole1'), Jump('dlh')) focus_mask True

    vbox:
        xpos 981 ypos 337 xmaximum 375
        if NTR == True:
            text "{b}General hints{/b}"
            text "{size=-10}- Hold relationship on 5 or lower then you can see events on different times at different places.{/size}"

    fixed pos (174,337) xysize (375,50):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                #xpos 174 ypos 337
                if ndate21 == False:
                    text "{size=-10}- Go with [mother] to her first date{/size}"
                if ndate21 == True and gangmember == False and momlove < 50:
                    text "{size=-10}- Become a gangmember and gain more love{/size}"
                if ndate21 == True and gangmember == True and momlove >= 50 and basenicfirst == False:
                    text "{size=-10}- Meet [mother] in the livingroom{/size}"
                if ndate21 == True and basenicfirst == True and mombasementlovesecond == False:
                    text "{size=-10}- Go with [mother] to her second date{/size}"
                if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == False:
                    text "{size=-10}- Go with her in the basement.{/size}"
                if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True and proom19first == False:
                    text "{size=-10}- Meet her in the parentsroom{/size}"
                if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True and proom19first == True:
                    text "{size=-10}- End of this path for now{/size}"

    fixed pos (563,337) xysize (375,50):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                #xpos 563 ypos 337
                if ndate21 == False:
                    text "{size=-10}- Go with [mother] to her first date{/size}"
                if ndate21 == True and gangmember == False and momcorruption < 30:
                    text "{size=-10}- Become a gangmember and gain more corruption{/size}"
                if ndate21 == True and gangmember == True and momlove >= 30 and basenicfirst == False:
                    text "{size=-10}- Meet [mother] in the livingroom{/size}"
                if ndate21 == True and basenicfirst == True and mombasementcorsecond == False:
                    text "{size=-10}- Go with [mother] to her second date{/size}"
                if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == False:
                    text "{size=-10}- Go with her in the basement.{/size}"
                if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == True and proom19first == False:
                    text "{size=-10}- Meet her in the parentsroom{/size}"
                if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == True and proom19first == True:
                    text "{size=-10}- End of this path for now{/size}"

    if nicole_help_more_love == True:
        fixed pos (174,500) xysize (375,450):
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    #xpos 174 ypos 500
                    text "{size=-10}- Go with [mother] to her first date on the weekend.{/size}"
                    text "{size=-10}- Become a gangmember and gain 50 love.{/size}"
                    text "{size=-10}- Meet [mother] in the livingroom at 10pm.{/size}"
                    text "{size=-10}- Go with [mother] to her first second on the weekend.{/size}"
                    text "{size=-10}- Go with [mother] to the basement at 10pm.{/size}"
                    text "{size=-10}- Meet [mother] in the parentsroom at 7pm.{/size}"
                    text "{size=-10}- End of this path for now{/size}"

    if nicole_help_more_corruption == True:
        fixed pos (563,500) xysize (375,450):
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    #xpos 563 ypos 500
                    text "{size=-10}- Go with [mother] to her first date on the weekend.{/size}"
                    text "{size=-10}- Become a gangmember and gain 30 corruption.{/size}"
                    text "{size=-10}- Meet [mother] in the livingroom at 10pm.{/size}"
                    text "{size=-10}- Go with [mother] to her first second on the weekend.{/size}"
                    text "{size=-10}- Go with [mother] to the basement at 10pm.{/size}"
                    text "{size=-10}- Meet [mother] in the parentsroom at 7pm.{/size}"
                    text "{size=-10}- End of this path for now.{/size}"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
