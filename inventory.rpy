
screen inventory():

    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        if giftflowers > 0:
            imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action NullAction() hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Amount: [giftflowers]")
        if giftcondoms > 0:
            imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action NullAction() hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Amount: [giftcondoms]") focus_mask True
        if giftchocolate > 0:
            imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action NullAction() hovered tt.Action ("Chocolate + 5 Relationship | Amount: [giftchocolate]") focus_mask True
        if package > 0:
            imagebutton auto "gui/icons/package_%s.png" xpos 882 ypos 156 action NullAction() hovered tt.Action ("Davide's delivery | Amount: [package]") focus_mask True
        if basementkey == True:
            imagebutton auto "gui/icons/key_%s.png" xpos 1081 ypos 156 action NullAction() hovered tt.Action ("Basement key") focus_mask True
        if nicolereddress == 2:
            imagebutton auto "gui/icons/cloth_red_dress_%s.png" xpos 380 ypos 320 action NullAction() hovered tt.Action ("A Red Dress for [mother] [cr1]") focus_mask True
        if nicolebabydoll == 2:
            imagebutton auto "gui/icons/cloth_babydoll_%s.png" xpos 570 ypos 320 action NullAction() hovered tt.Action ("A Babydoll for [mother] [cr1]") focus_mask True
        if nicolesweaterpants == 2:
            imagebutton auto "gui/icons/cloth_sweater_pants_%s.png" xpos 760 ypos 320 action NullAction() hovered tt.Action ("Sweater+Pants for [mother] [lv1]") focus_mask True
        if nicolerobe == 2:
            imagebutton auto "gui/icons/cloth_robe_%s.png" xpos 950 ypos 320 action NullAction() hovered tt.Action ("A Robe for [mother] [lv1]") focus_mask True


        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventory'), Jump('phone1')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        text tt.value



screen inventorygift2pmsp():

    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        if giftflowers > 0:
            imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action (Hide ('inventorygift2pmsp'), Jump('sp2pmgiftfl')) hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Amount: [giftflowers]")
        if giftcondoms > 0:
            imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action (Hide ('inventorygift2pmsp'), Jump('sp2pmgiftco')) hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Amount: [giftcondoms]") focus_mask True
        if giftchocolate > 0:
            imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action (Hide ('inventorygift2pmsp'), Jump('sp2pmgiftcho')) hovered tt.Action ("Chocolate + 5 Relationship | Amount: [giftchocolate]") focus_mask True


        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventorygift2pmsp'), Jump('lsisroom')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        text tt.value


screen inventorygift7amdr():

    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        if giftflowers > 0:
            imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action (Hide ('inventorygift7amdr'), Jump('dr7amgiftfl')) hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Amount: [giftflowers]")
        if giftcondoms > 0:
            imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action (Hide ('inventorygift7amdr'), Jump('dr7amgiftco')) hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Amount: [giftcondoms]") focus_mask True
        if giftchocolate > 0:
            imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action (Hide ('inventorygift7amdr'), Jump('dr7amgiftcho')) hovered tt.Action ("Chocolate + 5 Relationship | Amount: [giftchocolate]") focus_mask True


        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventorygift7amdr'), Jump('droom')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        text tt.value


screen inventorygift10pmls():

    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        if giftflowers > 0:
            imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action (Hide ('inventorygift10pmls'), Jump('ls10pmgiftfl')) hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Amount: [giftflowers]")
        if giftcondoms > 0:
            imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action (Hide ('inventorygift10pmls'), Jump('ls10pmgiftco')) hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Amount: [giftcondoms]") focus_mask True
        if giftchocolate > 0:
            imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action (Hide ('inventorygift10pmls'), Jump('ls10pmgiftcho')) hovered tt.Action ("Chocolate + 5 Relationship | Amount: [giftchocolate]") focus_mask True


        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventorygift10pmls'), Jump('lsisroom')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        text tt.value



screen inventorygiftdr12pmn:
    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        if giftflowers > 0:
            imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action (Hide ('inventorygiftdr12pmn'), Jump('mom12pmgiftfl')) hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Amount: [giftflowers]")
        if giftcondoms > 0:
            imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action (Hide ('inventorygiftdr12pmn'), Jump('mom12pmgiftco')) hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Amount: [giftcondoms]") focus_mask True
        if giftchocolate > 0:
            imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action (Hide ('inventorygiftdr12pmn'), Jump('mom12pmgiftcho')) hovered tt.Action ("Chocolate + 5 Relationship | Amount: [giftchocolate]") focus_mask True
        if nicolereddress == 2:
            imagebutton auto "gui/icons/cloth_red_dress_%s.png" xpos 380 ypos 320 action (Hide ('inventorygiftdr12pmn'), Jump('mom12pmgiftrd')) hovered tt.Action ("A Red Dress for [mother] [cr1]") focus_mask True
        if nicolebabydoll == 2:
            imagebutton auto "gui/icons/cloth_babydoll_%s.png" xpos 570 ypos 320 action (Hide ('inventorygiftdr12pmn'), Jump('mom12pmgiftbd')) hovered tt.Action ("A Babydoll for [mother] [cr1]") focus_mask True
        if nicolesweaterpants == 2:
            imagebutton auto "gui/icons/cloth_sweater_pants_%s.png" xpos 760 ypos 320 action (Hide ('inventorygiftdr12pmn'), Jump('mom12pmgiftsp')) hovered tt.Action ("Sweater+Pants for [mother] [lv1]") focus_mask True
        if nicolerobe == 2:
            imagebutton auto "gui/icons/cloth_robe_%s.png" xpos 950 ypos 320 action (Hide ('inventorygiftdr12pmn'), Jump('mom12pmgiftro')) hovered tt.Action ("A Robe for [mother] [lv1]") focus_mask True


        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventorygiftdr12pmn'), Jump('droom12gift')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        text tt.value


screen inventorygiftdr12pma:
    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        if giftflowers > 0:
            imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action (Hide ('inventorygiftdr12pma'), Jump('ls12pmgiftfl')) hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Amount: [giftflowers]")
        if giftcondoms > 0:
            imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action (Hide ('inventorygiftdr12pma'), Jump('ls12pmgiftco')) hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Amount: [giftcondoms]") focus_mask True
        if giftchocolate > 0:
            imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action (Hide ('inventorygiftdr12pma'), Jump('ls12pmgiftcho')) hovered tt.Action ("Chocolate + 5 Relationship | Amount: [giftchocolate]") focus_mask True


        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventorygiftdr12pma'), Jump('droom12gift')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        text tt.value


screen inventorygiftdr12pmc:
    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        if giftflowers > 0:
            imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action (Hide ('inventorygiftdr12pmc'), Jump('bs12pmgiftfl')) hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Amount: [giftflowers]")
        if giftcondoms > 0:
            imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action (Hide ('inventorygiftdr12pmc'), Jump('bs12pmgiftco')) hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Amount: [giftcondoms]") focus_mask True
        if giftchocolate > 0:
            imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action (Hide ('inventorygiftdr12pmc'), Jump('bs12pmgiftcho')) hovered tt.Action ("Chocolate + 5 Relationship | Amount: [giftchocolate]") focus_mask True


        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventorygiftdr12pmc'), Jump('droom12gift')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        text tt.value


screen inventorygiftfd21i:
    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        if giftflowers > 0:
            imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action (Hide ('inventorygiftfd21i'), Jump('irfd21giftfl')) hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Amount: [giftflowers]")
        if giftcondoms > 0:
            imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action (Hide ('inventorygiftfd21i'), Jump('irfd21giftco')) hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Amount: [giftcondoms]") focus_mask True
        if giftchocolate > 0:
            imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action (Hide ('inventorygiftfd21i'), Jump('irfd21giftcho')) hovered tt.Action ("Chocolate + 5 Relationship | Amount: [giftchocolate]") focus_mask True


        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventorygiftfd21i'), Jump('frontdoor21talk2')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        text tt.value


screen inventorygiftfd21c:
    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        if giftflowers > 0:
            imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action (Hide ('inventorygiftfd21c'), Jump('bsfd21giftfl')) hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Amount: [giftflowers]")
        if giftcondoms > 0:
            imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action (Hide ('inventorygiftfd21c'), Jump('bsfd21giftco')) hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Amount: [giftcondoms]") focus_mask True
        if giftchocolate > 0:
            imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action (Hide ('inventorygiftfd21c'), Jump('bsfd21giftcho')) hovered tt.Action ("Chocolate + 5 Relationship | Amount: [giftchocolate]") focus_mask True


        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventorygiftfd21c'), Jump('frontdoor21talk2')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        text tt.value