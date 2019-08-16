#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label dlh_cassandra:
    call screen dlh_cassandra1

screen dlh_cassandra1():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/dlh_background.png" xpos 152 ypos 106
        add "gui/icons/desc_cassandra.png" xpos 1410 ypos 198
        text "Activate helper" xpos 786 ypos 122
        if cassandra_help_simple_love == True:
            add "gui/icons/dlh_simple_green_idle.png" xpos 183 ypos 198
        if cassandra_help_full_love == True:
            add "gui/icons/dlh_full_green_idle.png" xpos 356 ypos 198
        if cassandra_help_simple_corruption == True:
            add "gui/icons/dlh_simple_green_idle.png" xpos 563 ypos 198
        if cassandra_help_full_corruption == True:
            add "gui/icons/dlh_full_green_idle.png" xpos 734 ypos 198
        imagebutton auto "gui/icons/dlh_deactivate_%s.png" xpos 1175 ypos 122 action (Hide('dlh_cassandra1'), Jump('dlh_deactivate')) hovered Notify("Deactivate the helper") focus_mask True

        text "Love path" xpos 258 ypos 257
        text "Corruption path" xpos 606 ypos 257
        if NTR == True:
            text "NTR" xpos 1087 ypos 257
        text "Activate helper" xpos 786 ypos 122

        if cassandra_help_simple_love == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 183 ypos 198 action (Hide('dlh_cassandra1'), Jump('dlh_simple_love_cas')) hovered Notify("Activate the simple helper") focus_mask True
        if cassandra_help_full_love == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 356 ypos 198 action (Hide('dlh_cassandra1'), Jump('dlh_full_love_cas')) hovered Notify("Activate the full helper") focus_mask True
        if cassandra_help_more_love == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 224 ypos 410 action (Hide('dlh_cassandra1'), Jump('dlh_more_love_cas')) hovered Notify("Show more info") focus_mask True
        if cassandra_help_more_love == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 224 ypos 410 action (Hide('dlh_cassandra1'), Jump('dlh_hide_love_cas')) hovered Notify("Hide") focus_mask True

        if cassandra_help_simple_corruption == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 563 ypos 198 action (Hide('dlh_cassandra1'), Jump('dlh_simple_corruption_cas')) hovered Notify("Activate the simple helper") focus_mask True
        if cassandra_help_full_corruption == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 734 ypos 198 action (Hide('dlh_cassandra1'), Jump('dlh_full_corruption_cas')) hovered Notify("Activate the full helper") focus_mask True
        if cassandra_help_more_corruption == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 601 ypos 410 action (Hide('dlh_cassandra1'), Jump('dlh_more_corruption_cas')) hovered Notify("Show more info") focus_mask True
        if cassandra_help_more_corruption == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 601 ypos 410 action (Hide('dlh_cassandra1'), Jump('dlh_hide_corruption_cas')) hovered Notify("Hide") focus_mask True

        imagebutton auto "gui/icons/dlh_close_%s.png" xpos 1604 ypos 122 action (Hide('dlh_cassandra1'), Jump('dlh')) focus_mask True

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
                if cdate5 == False:
                    text "{size=-10}- Go with [bs] to her first date.{/size}"
                if cdate5 == True and gangmember == False:
                    text "{size=-10}- Become a gangmember.{/size}"
                if cdate5 == True and gangmember == True and basecasfirst == False:
                    text "{size=-10}- Meet her in the kitchen.{/size}"
                if cdate5 == True and gangmember == True and basecasfirst == True and bigsislove < 50:
                    text "{size=-10}- Gain more love.{/size}"
                if cdate5 == True and gangmember == True and basecasfirst == True and bigsislove >= 50 and weekendcasfirst == False:
                    text "{size=-10}- Meet with [bs] for your second date.{/size}"
                if cdate5 == True and gangmember == True and basecasfirst == True and weekendcasfirst == True:
                    text "{size=-10}- End of this path for now.{/size}"

    fixed pos (563,337) xysize (375,50):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                #xpos 563 ypos 337
                if cdate5 == False:
                    text "{size=-10}- Go with [bs] to her first date.{/size}"
                if cdate5 == True and gangmember == False:
                    text "{size=-10}- Become a gangmember.{/size}"
                if cdate5 == True and gangmember == True and basecasfirst == False:
                    text "{size=-10}- Meet her in the kitchen.{/size}"
                if cdate5 == True and gangmember == True and basecasfirst == True and bigsiscorruption < 50:
                    text "{size=-10}- Gain more corruption.{/size}"
                if cdate5 == True and gangmember == True and basecasfirst == True and bigsiscorruption >= 50 and basecassecond == False:
                    text "{size=-10}- Meet her in the kitchen again.{/size}"
                if cdate5 == True and gangmember == True and basecasfirst == True and basecassecond == True and basement10cassandraouting == False:
                    text "{size=-10}- Go with her in the basement.{/size}"
                if cdate5 == True and gangmember == True and basecasfirst == True and basecassecond == True and basement10cassandraouting == True:
                    text "{size=-10}- End of this path for now.{/size}"

    if cassandra_help_more_love == True:
        fixed pos (174,500) xysize (375,450):
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    #xpos 174 ypos 500
                    text "{size=-10}- Go with [bs] to her first date on the weekend.{/size}"
                    text "{size=-10}- Become a gangmember{/size}"
                    text "{size=-10}- Meet her in the kitchen.{/size}"
                    text "{size=-10}- Gain 50 love.{/size}"
                    text "{size=-10}- Meet with [bs] for your second date.{/size}"
                    text "{size=-10}- End of this path for now.{/size}"

    if cassandra_help_more_corruption == True:
        fixed pos (563,500) xysize (375,450):
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    #xpos 563 ypos 500
                    text "{size=-10}- Go with [bs] to her first date on the weekend.{/size}"
                    text "{size=-10}- Become a gangmember.{/size}"
                    text "{size=-10}- Meet her in the kitchen at 9am.{/size}"
                    text "{size=-10}- Gain 50 corruption.{/size}"
                    text "{size=-10}- Meet her in the kitchen again.{/size}"
                    text "{size=-10}- Go with her in the basement at 10pm.{/size}"
                    text "{size=-10}- End of this path for now.{/size}"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label dlh_simple_love_cas:
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
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = True
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    $ player_help_full_gang = False
    "The simple helper is now activated."
    jump dlh_cassandra

label dlh_full_love_cas:
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
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = True
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    $ player_help_full_gang = False
    "The full helper is now activated."
    jump dlh_cassandra

label dlh_more_love_cas:
    $ cassandra_help_more_love = True
    jump dlh_cassandra

label dlh_hide_love_cas:
    $ cassandra_help_more_love = False
    jump dlh_cassandra

label dlh_simple_corruption_cas:
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
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = True
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    $ player_help_full_gang = False
    "The simple helper is now activated."
    jump dlh_cassandra

label dlh_full_corruption_cas:
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
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = True
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    $ player_help_full_gang = False
    "The full helper is now activated."
    jump dlh_cassandra

label dlh_more_corruption_cas:
    $ cassandra_help_more_corruption = True
    jump dlh_cassandra

label dlh_hide_corruption_cas:
    $ cassandra_help_more_corruption = False
    jump dlh_cassandra
