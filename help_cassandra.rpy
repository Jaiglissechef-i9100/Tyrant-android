

label dlh_cassandra:
    call screen dlh_cassandra1

screen dlh_cassandra1():

    default tt = Tooltip (" ")

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
        imagebutton auto "gui/icons/dlh_deactivate_%s.png" xpos 1175 ypos 122 action (Hide('dlh_cassandra1'), Jump('dlh_deactivate')) hovered tt.Action ("Deactivate the helper") focus_mask True

        text "Love path" xpos 258 ypos 257
        text "Corruption path" xpos 606 ypos 257
        if NTR == True:
            text "NTR" xpos 1087 ypos 257
        text "Activate helper" xpos 786 ypos 122


        if cassandra_help_simple_love == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 183 ypos 198 action (Hide ('dlh_cassandra1'), Jump('dlh_simple_love_cas')) hovered tt.Action ("Activate the simple helper") focus_mask True
        if cassandra_help_full_love == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 356 ypos 198 action (Hide ('dlh_cassandra1'), Jump('dlh_full_love_cas')) hovered tt.Action ("Activate the full helper") focus_mask True
        if cassandra_help_more_love == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 224 ypos 410 action (Hide ('dlh_cassandra1'), Jump('dlh_more_love_cas')) hovered tt.Action ("Show more info") focus_mask True
        if cassandra_help_more_love == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 224 ypos 410 action (Hide ('dlh_cassandra1'), Jump('dlh_hide_love_cas')) hovered tt.Action ("Hide") focus_mask True

        if cassandra_help_simple_corruption == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 563 ypos 198 action (Hide ('dlh_cassandra1'), Jump('dlh_simple_corruption_cas')) hovered tt.Action ("Activate the simple helper") focus_mask True
        if cassandra_help_full_corruption == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 734 ypos 198 action (Hide ('dlh_cassandra1'), Jump('dlh_full_corruption_cas')) hovered tt.Action ("Activate the full helper") focus_mask True
        if cassandra_help_more_corruption == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 601 ypos 410 action (Hide ('dlh_cassandra1'), Jump('dlh_more_corruption_cas')) hovered tt.Action ("Show more info") focus_mask True
        if cassandra_help_more_corruption == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 601 ypos 410 action (Hide ('dlh_cassandra1'), Jump('dlh_hide_corruption_cas')) hovered tt.Action ("Hide") focus_mask True





        imagebutton auto "gui/icons/dlh_close_%s.png" xpos 1604 ypos 122 action (Hide ('dlh_cassandra1'), Jump('dlh')) focus_mask True



    vbox:
        xpos 174 ypos 307
        if cdate5 == False:
            text "{size=-10}- Go with [bs]{/size}"
            text "{size=-10}to her first date.{/size}"
        if cdate5 == True and gangmember == False:
            text "{size=-10}- Become a gangmember.{/size}"
        if cdate5 == True and gangmember == True and basecasfirst == False:
            text "{size=-10}- Meet her{/size}"
            text "{size=-10}in the kitchen.{/size}"
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsislove < 50:
            text "{size=-10}- Gain more love.{/size}"
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsislove >= 50 and weekendcasfirst == False:
            text "{size=-10}- Meet with [bs]{/size}"
            text "{size=-10}for your second{/size}"
            text "{size=-10}date.{/size}"
        if cdate5 == True and gangmember == True and basecasfirst == True and weekendcasfirst == True:
            text "{size=-10}- End of this path for now{/size}"

    frame:
        area (174, 500, 339, 475)
        has side "c r"
        viewport id "cassandra_love_vp":
            draggable True
            mousewheel True
            has vbox:
                xpos 178 ypos 500
            if cassandra_help_more_love == True:
                text "{size=-10}- Go with [bs]{/size}"
                text "{size=-10}to her first date{/size}"
                text "{size=-10}on the weekend.{/size}"
                text "{size=-10}- Become a gangmember{/size}"
                text "{size=-10}- Meet her{/size}"
                text "{size=-10}in the kitchen.{/size}"
                text "{size=-10}- Gain 50 love.{/size}"
                text "{size=-10}- Meet with [bs]{/size}"
                text "{size=-10}for your second{/size}"
                text "{size=-10}date.{/size}"
                text "{size=-10}- End of this path for now{/size}"
        vbar value YScrollValue ("cassandra_love_vp")


    vbox:
        xpos 563 ypos 307
        if cdate5 == False:
            text "{size=-10}- Go with [bs]{/size}"
            text "{size=-10}to her first date.{/size}"
        if cdate5 == True and gangmember == False:
            text "{size=-10}- Become a gangmember.{/size}"
        if cdate5 == True and gangmember == True and basecasfirst == False:
            text "{size=-10}- Meet her{/size}"
            text "{size=-10}in the kitchen.{/size}"
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsiscorruption < 50:
            text "{size=-10}- Gain more corruption.{/size}"
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsiscorruption >= 50 and basecassecond == False:
            text "{size=-10}- Meet her in{/size}"
            text "{size=-10}the kitchen again.{/size}"
        if cdate5 == True and gangmember == True and basecasfirst == True and basecassecond == True and basement10cassandraouting == False:
            text "{size=-10}- Go with her in{/size}"
            text "{size=-10}the basement.{/size}"
        if cdate5 == True and gangmember == True and basecasfirst == True and basecassecond == True and basement10cassandraouting == True:
            text "{size=-10}- End of this path for now{/size}"

    frame:
        area (563, 500, 339, 475)
        has side "c r"
        viewport id "cassandra_corruption_vp":
            draggable True
            mousewheel True
            has vbox:
                xpos 567 ypos 500
            if cassandra_help_more_corruption == True:
                text "{size=-10}- Go with [bs]{/size}"
                text "{size=-10}to her first date{/size}"
                text "{size=-10}on the weekend.{/size}"
                text "{size=-10}- Become a gangmember.{/size}"
                text "{size=-10}- Meet her in{/size}"
                text "{size=-10}the kitchen at 9am.{/size}"
                text "{size=-10}- Gain 50 corruption.{/size}"
                text "{size=-10}- Meet her in{/size}"
                text "{size=-10}the kitchen again.{/size}"
                text "{size=-10}Go with her in the.{/size}"
                text "{size=-10}basement at 10pm.{/size}"
                text "{size=-10}- End of this path for now{/size}"
        vbar value YScrollValue ("cassandra_corruption_vp")


    vbox:
        xpos 981 ypos 307
        if NTR == True:
            text "{b}General hints{/b}"
            text "{size=-10}- Hold relationship on 5 or lower{/size}"
            text "{size=-10}then you can see events{/size}"
            text "{size=-10}on different times at{/size}"
            text "{size=-10}different places.{/size}"


    frame:
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
