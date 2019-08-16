#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label shop:
    show screen hud
    call screen shop1

screen shop1():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneshop.png" xpos 714 ypos 44
        add "gui/icons/flowers_idle.png" xpos 874 ypos 366
        text "Flowers" xpos 908 ypos 273

        if money >= 5:
            imagebutton auto "gui/icons/icon_buy1_%s.png" xpos 788 ypos 758 action (Hide('shop1'), Jump('buy1fl')) hovered Notify("Buy 1") focus_mask True
        if money >= 25:
            imagebutton auto "gui/icons/icon_buy5_%s.png" xpos 1011 ypos 758 action (Hide('shop1'), Jump('buy5fl')) hovered Notify("Buy 5") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 799 ypos 950 action (Hide('shop1'), Show('shop7', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1058 ypos 950 action (Hide('shop1'), Show('shop2', transition=None)) hovered Notify("Next") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('shop1'), Jump('phone1')) hovered Notify("Close") focus_mask True

    vbox:
        xpos 855 ypos 567
        text "+ 5 Relationship"
        text "+ 5 {color=3cff00}Love{/color}"

        text "Price: $5"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label buy1fl:
    $ giftflowers += 1
    $ money -= 5
    " You bought 1 flower."
    jump shop

label buy5fl:
    $ giftflowers += 5
    $ money -= 25
    " You bought 5 flowers."
    jump shop

label shopco:
    call screen shop2

screen shop2():
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneshop.png" xpos 714 ypos 44
        add "gui/icons/condoms_idle.png" xpos 874 ypos 366
        text "Condoms" xpos 908 ypos 273

        if money >= 5:
            imagebutton auto "gui/icons/icon_buy1_%s.png" xpos 788 ypos 758 action (Hide('shop2'), Jump('buy1co')) hovered Notify("Buy 1") focus_mask True
        if money >= 25:
            imagebutton auto "gui/icons/icon_buy5_%s.png" xpos 1011 ypos 758 action (Hide('shop2'), Jump('buy5co')) hovered Notify("Buy 5") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 799 ypos 950 action (Hide('shop2'), Show('shop1', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1058 ypos 950 action (Hide('shop2'), Show('shop3', transition=None)) hovered Notify("Next") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('shop2'), Jump('phone1')) hovered Notify("Close") focus_mask True

    vbox:
        xpos 855 ypos 567
        text "+ 5 Relationship"
        text "+ 5 {color=ff0000}Corruption{/color}"

        text "Price: $5"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label buy1co:
    $ giftcondoms += 1
    $ money -= 5
    " You bought 1 condom."
    jump shopco

label buy5co:
    $ giftcondoms += 5
    $ money -= 25
    " You bought 5 condoms."
    jump shopco

label shopcho:
    call screen shop3

screen shop3():
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneshop.png" xpos 714 ypos 44
        add "gui/icons/chocolate_idle.png" xpos 874 ypos 366
        text "Chocolate" xpos 908 ypos 273

        if money >= 5:
            imagebutton auto "gui/icons/icon_buy1_%s.png" xpos 788 ypos 758 action (Hide('shop3'), Jump('buy1cho')) hovered Notify("Buy 1") focus_mask True
        if money >= 25:
            imagebutton auto "gui/icons/icon_buy5_%s.png" xpos 1011 ypos 758 action (Hide('shop3'), Jump('buy5cho')) hovered Notify("Buy 5") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 799 ypos 950 action (Hide('shop3'), Show('shop2', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1058 ypos 950 action (Hide('shop3'), Show('shop4', transition=None)) hovered Notify("Next") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('shop3'), Jump('phone1')) hovered Notify("Close") focus_mask True

    vbox:
        xpos 855 ypos 567
        text "+ 5 Relationship"

        text "Price: $5"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label buy1cho:
    $ giftchocolate += 1
    $ money -= 5
    " You bought 1 chocolate."
    jump shopcho

label buy5cho:
    $ giftchocolate += 5
    $ money -= 25
    " You bought 5 chocolates."
    jump shopcho

label shoprd:
    call screen shop4

screen shop4():
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneshop.png" xpos 714 ypos 44
        add "gui/icons/cloth_red_dress_idle.png" xpos 930 ypos 366
        text "[mother]'s Red Dress" xpos 820 ypos 273

        if gangmember == True and mombasementfirst == True and nicolereddress == 1 and money >= 75 and momcorruption >= 30:
            imagebutton auto "gui/icons/icon_buy1_%s.png" xpos 900 ypos 820 action (Hide('shop4'), Jump('buy1rd')) hovered Notify("Buy 1") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 799 ypos 950 action (Hide('shop4'), Show('shop3', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1058 ypos 950 action (Hide('shop4'), Show('shop5', transition=None)) hovered Notify("Next") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('shop4'), Jump('phone1')) hovered Notify("Close") focus_mask True

    vbox:
        xpos 760 ypos 507
        text "Requirements:"
        text "30+ Corruption"
        text "Be a gangmember"
        text "Second basement event"
        text "Price: $75"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label buy1rd:
    $ nicolereddress = 2
    $ money -= 75
    "You bought a red dress for [mother]."
    jump shoprd

label shopsp:
    call screen shop5

screen shop5():
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneshop.png" xpos 714 ypos 44
        add "gui/icons/cloth_sweater_pants_idle.png" xpos 930 ypos 366
        text "Sweater + Pants ([mother])" xpos 780 ypos 273

        if momlove >= 30 and nicolesweaterpants == 1 and money >= 75:
            imagebutton auto "gui/icons/icon_buy1_%s.png" xpos 900 ypos 820 action (Hide('shop5'), Jump('buy1sp')) hovered Notify("Buy 1") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 799 ypos 950 action (Hide('shop5'), Show('shop4', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1058 ypos 950 action (Hide('shop5'), Show('shop6', transition=None)) hovered Notify("Next") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('shop5'), Jump('phone1')) hovered Notify("Close") focus_mask True

    vbox:
        xpos 760 ypos 507
        text "Requirements:"
        text "30+ Love"

        text "Price: $75"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label buy1sp:
    $ nicolesweaterpants = 2
    $ money -= 75
    "You bought a sweater and pants for [mother]."
    jump shopsp


label shopbd:
    call screen shop6

screen shop6():
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneshop.png" xpos 714 ypos 44
        add "gui/icons/cloth_babydoll_idle.png" xpos 930 ypos 366
        text "[mother]'s Babydoll" xpos 820 ypos 273

        if gangmember == True and mombasementcorsecond == True and nicolebabydoll == 1 and money >= 150 and momcorruption >= 60:
            imagebutton auto "gui/icons/icon_buy1_%s.png" xpos 900 ypos 820 action (Hide('shop6'), Jump('buy1bd')) hovered Notify("Buy 1") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 799 ypos 950 action (Hide('shop6'), Show('shop5', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1058 ypos 950 action (Hide('shop6'), Show('shop7', transition=None)) hovered Notify("Next") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('shop6'), Jump('phone1')) hovered Notify("Close") focus_mask True

    vbox:
        xpos 760 ypos 507
        text "Requirements:"
        text "60+ Corruption"
        text "Be a gangmember"
        text "Basement event (weekend)"

        text "Price: $150"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label buy1bd:
    $ nicolebabydoll = 2
    $ money -= 150
    "You bought [mother]'s babydoll."
    jump shopbd

label shopro:
    call screen shop7

screen shop7():
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneshop.png" xpos 714 ypos 44
        add "gui/icons/cloth_robe_idle.png" xpos 930 ypos 366
        text "[mother]'s Robe" xpos 820 ypos 273

        if mombasementlovesecond == True and nicolerobe == 1 and money >= 150 and momlove >= 80:
            imagebutton auto "gui/icons/icon_buy1_%s.png" xpos 900 ypos 820 action (Hide('shop7'), Jump('buy1ro')) hovered Notify("Buy 1") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 799 ypos 950 action (Hide('shop7'), Show('shop6', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1058 ypos 950 action (Hide('shop7'), Show('shop1', transition=None)) hovered Notify("Next") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('shop7'), Jump('phone1')) hovered Notify("Close") focus_mask True

    vbox:
        xpos 760 ypos 507
        text "Requirements:"
        text "80+ Love"
        text "Home event (weekend)"

        text "Price: $150"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label buy1ro:
    $ nicolerobe = 2
    $ money -= 150
    "You bought [mother]'s robe."
    jump shopro
