#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label dlh_alexis:
    call screen dlh_alexis1

screen dlh_alexis1():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/dlh_background.png" xpos 152 ypos 106
        add "gui/icons/desc_alexis.png" xpos 1410 ypos 198
        text "Activate helper" xpos 786 ypos 122
        if alexis_help_simple_love == True:
            add "gui/icons/dlh_simple_green_idle.png" xpos 183 ypos 198
        if alexis_help_full_love == True:
            add "gui/icons/dlh_full_green_idle.png" xpos 356 ypos 198
        if alexis_help_simple_corruption == True:
            add "gui/icons/dlh_simple_green_idle.png" xpos 563 ypos 198
        if alexis_help_full_corruption == True:
            add "gui/icons/dlh_full_green_idle.png" xpos 734 ypos 198
        if NTR == True and alexis_help_simple_NTR == True:
            add "gui/icons/dlh_simple_green_idle.png" xpos 1001 ypos 198
        if NTR == True and alexis_help_full_NTR == True:
            add "gui/icons/dlh_full_green_idle.png" xpos 1167 ypos 198
        imagebutton auto "gui/icons/dlh_deactivate_%s.png" xpos 1175 ypos 122 action (Hide('dlh_alexis1'), Jump('dlh_deactivate')) hovered Notify("Deactivate the helper") focus_mask True

        text "Love path" xpos 258 ypos 257
        text "Corruption path" xpos 606 ypos 257
        if NTR == True:
            text "NTR" xpos 1087 ypos 257
        text "Activate helper" xpos 786 ypos 122

        if alexis_help_simple_love == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 183 ypos 198 action (Hide('dlh_alexis1'), Jump('dlh_simple_love_ale')) hovered Notify("Activate the simple helper") focus_mask True
        if alexis_help_full_love == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 356 ypos 198 action (Hide('dlh_alexis1'), Jump('dlh_full_love_ale')) hovered Notify("Activate the full helper") focus_mask True
        if alexis_help_more_love == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 224 ypos 410 action (Hide('dlh_alexis1'), Jump('dlh_more_love_ale')) hovered Notify("Show more info") focus_mask True
        if alexis_help_more_love == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 224 ypos 410 action (Hide('dlh_alexis1'), Jump('dlh_hide_love_ale')) hovered Notify("Hide") focus_mask True

        if alexis_help_simple_corruption == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 563 ypos 198 action (Hide('dlh_alexis1'), Jump('dlh_simple_corruption_ale')) hovered Notify("Activate the simple helper") focus_mask True
        if alexis_help_full_corruption == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 734 ypos 198 action (Hide('dlh_alexis1'), Jump('dlh_full_corruption_ale')) hovered Notify("Activate the full helper") focus_mask True
        if alexis_help_more_corruption == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 601 ypos 410 action (Hide('dlh_alexis1'), Jump('dlh_more_corruption_ale')) hovered Notify("Show more info") focus_mask True
        if alexis_help_more_corruption == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 601 ypos 410 action (Hide('dlh_alexis1'), Jump('dlh_hide_corruption_ale')) hovered Notify("Hide") focus_mask True

        if NTR == True and alexis_help_simple_NTR == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 1001 ypos 198 action (Hide('dlh_alexis1'), Jump('dlh_simple_NTR_ale')) hovered Notify("Activate the simple helper") focus_mask True
        if NTR == True and alexis_help_full_NTR == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 1167 ypos 198 action (Hide('dlh_alexis1'), Jump('dlh_full_NTR_ale')) hovered Notify("Activate the full helper") focus_mask True
        if NTR == True and alexis_help_more_NTR == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 1019 ypos 410 action (Hide('dlh_alexis1'), Jump('dlh_more_NTR_ale')) hovered Notify("Show more info") focus_mask True
        if NTR == True and alexis_help_more_NTR == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 1019 ypos 410 action (Hide('dlh_alexis1'), Jump('dlh_hide_NTR_ale')) hovered Notify("Hide") focus_mask True

        imagebutton auto "gui/icons/dlh_close_%s.png" xpos 1604 ypos 122 action (Hide('dlh_alexis1'), Jump('dlh')) focus_mask True

    fixed pos (174,337) xysize (375,50):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                #xpos 174 ypos 337
                if adate == False:
                    text "{size=-10}- Go with [ls] to her first date.{/size}"
                if adate == True and lilsislove < 50:
                    text "{size=-10}- Gain more love.{/size}"
                if adate == True and alexisweekendsecond == False and lilsislove >= 50:
                    text "{size=-10}- Go with [ls] to her second date.{/size}"
                if adate == True and alexisweekendsecond == True:
                    text "{size=-10}- End of this path for now.{/size}"

    fixed pos (563,337) xysize (375,50):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                #xpos 563 ypos 337
                if adate == False:
                    text "{size=-10}- Go with [ls] to her first date.{/size}"
                if adate == True and gangmember == False:
                    text "{size=-10}- Become a gangmember.{/size}"
                if adate == True and gangmember == True and lilsiscorruption < 30:
                    text "{size=-10}- Gain more corruption.{/size}"
                if adate == True and showbasealfirst == False and lilsiscorruption >= 30 and gangmember == True:
                    text "{size=-10}- Meet [ls] in the kitchen.{/size}"
                if adate == True and alexisweekendsecond == True:
                    text "{size=-10}- End of this path for now.{/size}"

    fixed pos (981,337) xysize (375,50):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                #xpos 981 ypos 337
                text "{size=-10}(5 or lower relationship needed){/size}" #xpos 987 ypos 300
                if NTR == True and adate == False:
                    text "{size=-10}- Go with [ls] to her first date.{/size}"
                if NTR == True and adate == True and basealefirst == False:
                    text "{size=-10}- Sneak with her in the basement.{/size}"
                if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == False:
                    text "{size=-10}- Go to the secret place.{/size}"
                if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == True and base2amalexisntrfirst == False:
                    text "{size=-10}- Wait until the basement event at night happened.{/size}"
                if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == True and base2amalexisntrfirst == True and secretplace4pmntrfirst == False:
                    text "{size=-10}- Stay the next weekend alone.{/size}"
                if NTR == True and secretplace4pmntrfirst == True:
                    text "{size=-10}- End of this path for now.{/size}"

    if alexis_help_more_love == True:
        fixed pos (174,500) xysize (375,450):
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    #xpos 174 ypos 500
                    text "{size=-10}- Go with [ls] to her first date on the weekend.{/size}"
                    text "{size=-10}- Gain 50 love.{/size}"
                    text "{size=-10}- Go with [ls] to her second date on the weekend.{/size}"
                    text "{size=-10}- End of this path for now.{/size}"

    if alexis_help_more_corruption == True:
        fixed pos (563,500) xysize (375,450):
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    #xpos 563 ypos 500
                    text "{size=-10}- Go with [ls] to her first date on the weekend.{/size}"
                    text "{size=-10}- Become a gangmember.{/size}"
                    text "{size=-10}- Gain 30 corruption.{/size}"
                    text "{size=-10}- Go with [ls].{/size}"
                    text "{size=-10}- Meet [ls] in the kitchen at 8am.{/size}"
                    text "{size=-10}- End of this path for now.{/size}"

    if NTR == True and alexis_help_more_NTR == True:
        fixed pos (981,500) xysize (375,450):
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    #xpos 981 ypos 500
                    text "{size=-10}- Go with [ls] to her first date on the weekend. Let her be friends with Davide.{/size}"
                    text "{size=-10}- Sneak with her at the basement, start in your room.{/size}"
                    text "{size=-10}- Go to the secret place at 2pm.{/size}"
                    text "{size=-10}- Wait until the basement event at night happens, at 2am.{/size}"
                    text "{size=-10}- Stay the next weekend alone.{/size}"
                    text "{size=-10}- End of this path for now.{/size}"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label dlh_simple_love_ale:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = True
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
    jump dlh_alexis

label dlh_full_love_ale:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = True
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
    jump dlh_alexis

label dlh_more_love_ale:
    $ alexis_help_more_love = True
    jump dlh_alexis

label dlh_hide_love_ale:
    $ alexis_help_more_love = False
    jump dlh_alexis

label dlh_simple_corruption_ale:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = True
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
    jump dlh_alexis

label dlh_full_corruption_ale:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = True
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
    jump dlh_alexis

label dlh_more_corruption_ale:
    $ alexis_help_more_corruption = True
    jump dlh_alexis

label dlh_hide_corruption_ale:
    $ alexis_help_more_corruption = False
    jump dlh_alexis

label dlh_simple_NTR_ale:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = False
    $ alexis_help_simple_NTR = True
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
    jump dlh_alexis

label dlh_full_NTR_ale:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = False
    $ alexis_help_simple_NTR = True
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
    jump dlh_alexis

label dlh_more_NTR_ale:
    $ alexis_help_more_NTR = True
    jump dlh_alexis

label dlh_hide_NTR_ale:
    $ alexis_help_more_NTR = False
    jump dlh_alexis
