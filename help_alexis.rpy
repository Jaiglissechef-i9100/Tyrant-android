

label dlh_alexis:
    call screen dlh_alexis1

screen dlh_alexis1():

    default tt = Tooltip (" ")

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
        if NTR == True and alexis_help_simple_NTR:
            add "gui/icons/dlh_simple_green_idle.png" xpos 1001 ypos 198
        if NTR == True and alexis_help_full_NTR:
            add "gui/icons/dlh_full_green_idle.png" xpos 1167 ypos 198
        imagebutton auto "gui/icons/dlh_deactivate_%s.png" xpos 1175 ypos 122 action (Hide('dlh_alexis1'), Jump('dlh_deactivate')) hovered tt.Action ("Deactivate the helper") focus_mask True

        text "Love path" xpos 258 ypos 257
        text "Corruption path" xpos 606 ypos 257
        if NTR == True:
            text "NTR" xpos 1087 ypos 257
            text "{size=-10}(5 or lower relationship needed){/size}" xpos 987 ypos 300
        text "Activate helper" xpos 786 ypos 122


        if alexis_help_simple_love == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 183 ypos 198 action (Hide ('dlh_alexis1'), Jump('dlh_simple_love_ale')) hovered tt.Action ("Activate the simple helper") focus_mask True
        if alexis_help_full_love == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 356 ypos 198 action (Hide ('dlh_alexis1'), Jump('dlh_full_love_ale')) hovered tt.Action ("Activate the full helper") focus_mask True
        if alexis_help_more_love == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 224 ypos 410 action (Hide ('dlh_alexis1'), Jump('dlh_more_love_ale')) hovered tt.Action ("Show more info") focus_mask True
        if alexis_help_more_love == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 224 ypos 410 action (Hide ('dlh_alexis1'), Jump('dlh_hide_love_ale')) hovered tt.Action ("Hide") focus_mask True

        if alexis_help_simple_corruption == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 563 ypos 198 action (Hide ('dlh_alexis1'), Jump('dlh_simple_corruption_ale')) hovered tt.Action ("Activate the simple helper") focus_mask True
        if alexis_help_full_corruption == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 734 ypos 198 action (Hide ('dlh_alexis1'), Jump('dlh_full_corruption_ale')) hovered tt.Action ("Activate the full helper") focus_mask True
        if alexis_help_more_corruption == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 601 ypos 410 action (Hide ('dlh_alexis1'), Jump('dlh_more_corruption_ale')) hovered tt.Action ("Show more info") focus_mask True
        if alexis_help_more_corruption == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 601 ypos 410 action (Hide ('dlh_alexis1'), Jump('dlh_hide_corruption_ale')) hovered tt.Action ("Hide") focus_mask True

        if NTR == True and alexis_help_simple_NTR == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 1001 ypos 198 action (Hide ('dlh_alexis1'), Jump('dlh_simple_NTR_ale')) hovered tt.Action ("Activate the simple helper") focus_mask True
        if NTR == True and alexis_help_full_NTR == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 1167 ypos 198 action (Hide ('dlh_alexis1'), Jump('dlh_full_NTR_ale')) hovered tt.Action ("Activate the full helper") focus_mask True
        if NTR == True and alexis_help_more_NTR == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 1019 ypos 410 action (Hide ('dlh_alexis1'), Jump('dlh_more_NTR_ale')) hovered tt.Action ("Show more info") focus_mask True
        if NTR == True and alexis_help_more_NTR == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 1019 ypos 410 action (Hide ('dlh_alexis1'), Jump('dlh_hide_NTR_ale')) hovered tt.Action ("Hide") focus_mask True



        imagebutton auto "gui/icons/dlh_close_%s.png" xpos 1604 ypos 122 action (Hide ('dlh_alexis1'), Jump('dlh')) focus_mask True



    vbox:
        xpos 174 ypos 307
        if adate == False:
            text "{size=-10}- Go with [ls]{/size}"
            text "{size=-10}to her first date.{/size}"
        if adate == True and lilsislove < 50:
            text "{size=-10}- Gain more love.{/size}"
        if adate == True and alexisweekendsecond == False and lilsislove >= 50:
            text "{size=-10}- Go with [ls]{/size}"
            text "{size=-10}to her second date.{/size}"
        if adate == True and alexisweekendsecond == True:
            text "{size=-10}- End of this path for now{/size}"


    frame:
        area (174, 500, 339, 475)
        has side "c r"
        viewport id "alexis_love_vp":
            draggable True
            mousewheel True
            has vbox:
                xpos 178 ypos 500
            if alexis_help_more_love == True:
                text "{size=-10}- Go with [ls]{/size}"
                text "{size=-10}to her first date{/size}"
                text "{size=-10}on the weekend.{/size}"
                text "{size=-10}- Gain 50 love.{/size}"
                text "{size=-10}- Go with [ls]{/size}"
                text "{size=-10}to her second date{/size}"
                text "{size=-10}on the weekend.{/size}"
                text "{size=-10}- End of this path for now{/size}"
        vbar value YScrollValue ("alexis_love_vp")


    vbox:
        xpos 563 ypos 307
        if adate == False:
            text "{size=-10}- Go with [ls]{/size}"
            text "{size=-10}to her first date.{/size}"
        if adate == True and gangmember == False:
            text "{size=-10}- Become a gangmember.{/size}"
        if adate == True and gangmember == True and lilsiscorruption < 30:
            text "{size=-10}- Gain more corruption.{/size}"
        if adate == True and showbasealfirst == False and lilsiscorruption >= 30 and gangmember == True:
            text "{size=-10}- Meet [ls] in the kitchen.{/size}"
        if adate == True and alexisweekendsecond == True:
            text "{size=-10}- End of this path for now{/size}"

    frame:
        area (563, 500, 339, 475)
        has side "c r"
        viewport id "alexis_corruption_vp":
            draggable True
            mousewheel True
            has vbox:
                xpos 567 ypos 500
            if alexis_help_more_corruption == True:
                text "{size=-10}- Go with [ls]{/size}"
                text "{size=-10}to her first date{/size}"
                text "{size=-10}on the weekend.{/size}"
                text "{size=-10}- Become a gangmember.{/size}"
                text "{size=-10}- Gain 30 corruption.{/size}"
                text "{size=-10}- Go with [ls]{/size}"
                text "{size=-10}- Meet [ls] in the{/size}"
                text "{size=-10}kitchen at 8am.{/size}"
                text "{size=-10}- End of this path for now{/size}"
        vbar value YScrollValue ("alexis_corruption_vp")


    vbox:
        xpos 981 ypos 307
        if NTR == True and adate == False:
            text "{size=-10}- Go with [ls]{/size}"
            text "{size=-10}to her first date.{/size}"
        if NTR == True and adate == True and basealefirst == False:
            text "{size=-10}- Sneak with her{/size}"
            text "{size=-10}in the basement.{/size}"
        if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == False:
            text "{size=-10}- Go to the{/size}"
            text "{size=-10}secret place.{/size}"
        if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == True and base2amalexisntrfirst == False:
            text "{size=-10}- Wait until the{/size}"
            text "{size=-10}basement event at{/size}"
            text "{size=-10}night happened.{/size}"
        if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == True and base2amalexisntrfirst == True and secretplace4pmntrfirst == False:
            text "{size=-10}- Stay the next{/size}"
            text "{size=-10}weekend alone.{/size}"
        if NTR == True and secretplace4pmntrfirst == True:
            text "{size=-10}- End of this path for now{/size}"


    frame:
        area (981, 500, 339, 475)
        has side "c r"
        viewport id "alexis_ntr_vp":
            draggable True
            mousewheel True
            has vbox:
                xpos 985 ypos 500
            if NTR == True and alexis_help_more_NTR == True:
                text "{size=-10}- Go with [ls]{/size}"
                text "{size=-10}to her first date on the weekend.{/size}"
                text "{size=-10}- Sneak with her at{/size}"
                text "{size=-10}the basement, start in{/size}"
                text "{size=-10}your room.{/size}"
                text "{size=-10}- Go to the secret place at 2pm.{/size}"
                text "{size=-10}- Wait until the basement event{/size}"
                text "{size=-10} at night happened, at 2am.{/size}"
                text "{size=-10}- Stay the next{/size}"
                text "{size=-10}weekend alone.{/size}"
                text "{size=-10}- End of this path for now{/size}"
        vbar value YScrollValue ("alexis_ntr_vp")

    frame:
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