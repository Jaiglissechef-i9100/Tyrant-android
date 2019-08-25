
label shop:
    show screen hud
    call screen shop1

screen shop1():

    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phonesideinv.png" xpos 142 ypos 114


        imagebutton auto "gui/icons/flowers_%s.png" xpos 320 ypos 156 action (Hide ('shop1'), Jump('buy1fl')) hovered tt.Action ("Flowers +5 Relationship/+ 5 {color=3cff00}Love{/color} | Price: $5")
        imagebutton auto "gui/icons/condoms_%s.png" xpos 494 ypos 156 action (Hide ('shop1'), Jump('buy1co')) hovered tt.Action ("Condoms + 5 Relationship/+ 5 {color=ff0000}Corruption{/color} | Price: $5") focus_mask True
        imagebutton auto "gui/icons/chocolate_%s.png" xpos 690 ypos 156 action (Hide ('shop1'), Jump('buy1cho')) hovered tt.Action ("Chocolate + 5 Relationship | Price: $5") focus_mask True

        if nicolereddress == 1:
            imagebutton auto "gui/icons/cloth_red_dress_%s.png" xpos 380 ypos 320 action (Hide ('shop1'), Jump('buy1rd')) hovered tt.Action ("A Red Dress for [mother] [cr1] | Price: $75 | Requirements: 30[cr1], be a gangmember, have done her second basement event") focus_mask True
        if nicolebabydoll == 1:
            imagebutton auto "gui/icons/cloth_babydoll_%s.png" xpos 570 ypos 320 action (Hide ('shop1'), Jump('buy1bd')) hovered tt.Action ("A Babydoll for [mother] [cr1] | Price: $150 | Requirements: 60[cr1], be a gangmember, have done her weekend basement event ") focus_mask True
        if nicolesweaterpants == 1:
            imagebutton auto "gui/icons/cloth_sweater_pants_%s.png" xpos 760 ypos 320 action (Hide ('shop1'), Jump('buy1sp')) hovered tt.Action ("Sweater+Pants for [mother] [lv1] | Price: $75 | Requirements: 30[lv1]") focus_mask True
        if nicolerobe == 1:
            imagebutton auto "gui/icons/cloth_robe_%s.png" xpos 950 ypos 320 action (Hide ('shop1'), Jump('buy1ro')) hovered tt.Action ("A Robe for [mother] [lv1] | Price: $150 | Requirements: 80[lv1], have done her weekend event at home") focus_mask True
        if alexisrocker == 1:
            imagebutton auto "gui/icons/cloth_rocker_%s.png" xpos 380 ypos 480 action (Hide ('shop1'), Jump('buy1rw')) hovered tt.Action ("A Rocker Outfit for [ls] [cr1] | Price: $75 | Requirements: 30[cr1]") focus_mask True
        if alexislingerie == 1:
            imagebutton auto "gui/icons/cloth_alingerie_%s.png" xpos 570 ypos 480 action (Hide ('shop1'), Jump('buy1al')) hovered tt.Action ("Lingerie for [ls] [cr1] | Price: $150 | Requirements: 60[cr1]") focus_mask True
        if alexisjeansskirt == 1:
            imagebutton auto "gui/icons/cloth_jeans_skirt_%s.png" xpos 760 ypos 480 action (Hide ('shop1'), Jump('buy1js')) hovered tt.Action ("A Top and a Skirt for [ls] [lv1] | Price: $75 | Requirements: 20[lv1]") focus_mask True
        if alexisgrid == 1:
            imagebutton auto "gui/icons/cloth_grid_%s.png" xpos 950 ypos 480 action (Hide ('shop1'), Jump('buy1gs')) hovered tt.Action ("A Grid Suit for [ls] [lv1] | Price: $150 | Requirements: 50[lv1]") focus_mask True
        if cassandraheartdress == 1:
            imagebutton auto "gui/icons/cloth_heart_dress_%s.png" xpos 380 ypos 650 action (Hide ('shop1'), Jump('buy1hd')) hovered tt.Action ("A Heart Dress for [bs] [cr1] | Price: $75 | Requirements: 30[cr1]") focus_mask True
        if cassandralingerie == 1:
            imagebutton auto "gui/icons/cloth_clingerie_%s.png" xpos 570 ypos 650 action (Hide ('shop1'), Jump('buy1cl')) hovered tt.Action ("Lingerie for [bs] [cr1] | Price: $150 | Requirements: 60[cr1]") focus_mask True
        if cassandrajeans == 1:
            imagebutton auto "gui/icons/cloth_jeans_outfit_%s.png" xpos 760 ypos 650 action (Hide ('shop1'), Jump('buy1jo')) hovered tt.Action ("A Jeans Outfit for [bs] [lv1] | Price: $75 | Requirements: 20[lv1]") focus_mask True
        if cassandrapajama == 1:
            imagebutton auto "gui/icons/cloth_pajamas_%s.png" xpos 950 ypos 650 action (Hide ('shop1'), Jump('buy1pa')) hovered tt.Action ("Pajamas for [bs] [lv1] | Price: $150 | Requirements: 50[lv1]") focus_mask True

        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('inventory'), Jump('phone1')) hovered tt.Action ("Close") focus_mask True

    frame:
        xalign .5
        yalign .97
        text tt.value



label buy1fl:
    if money >= 5:
        $ giftflowers += 1
        $ money -= 5
        " You bought 1 flower."
        jump shop
    else:
        "You don't have enough money."
        jump shop


label buy1co:
    if money >= 5:
        $ giftcondoms += 1
        $ money -= 5
        " You bought 1 condom."
        jump shop
    else:
        "You don't have enough money."
        jump shop



label buy1cho:
    if money >= 5:
        $ giftchocolate += 1
        $ money -= 5
        " You bought 1 chocolate."
        jump shop
    else:
        "You don't have enough money."
        jump shop




label buy1rd:
    if gangmember == True and mombasementfirst == True and nicolereddress == 1 and money >= 75 and momcorruption >= 30:
        $ nicolereddress = 2
        $ money -= 75
        "You bought a red dress for [mother]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1sp:
    if momlove >= 30 and nicolesweaterpants == 1 and money >= 75:
        $ nicolesweaterpants = 2
        $ money -= 75
        "You bought a sweater and pants for [mother]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1bd:
    if gangmember == True and mombasementcorsecond == True and nicolebabydoll == 1 and money >= 150 and momcorruption >= 60:
        $ nicolebabydoll = 2
        $ money -= 150
        "You bought a babydoll for [mother]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop



label buy1ro:
    if mombasementlovesecond == True and nicolerobe == 1 and money >= 150 and momlove >= 80:
        $ nicolerobe = 2
        $ money -= 150
        "You bought a robe for [mother]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1rw:
    if alexisrocker == 1 and lilsiscorruption >= 30 and money >= 75:
        $ alexisrocker = 2
        $ money -=75
        "You bought a rocker outfit for [ls]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1al:
    if alexislingerie == 1 and lilsiscorruption >= 60 and money >= 150:
        $ alexislingerie = 2
        $ money -= 150
        "You bought lingerie for [ls]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1js:
    if alexisjeansskirt == 1 and lilsislove >= 20 and money >= 75:
        $ alexisjeansskirt = 2
        $ money -= 75
        "You bought a white top and a jeans skirt for [ls]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1gs:
    if alexisgrid == 1 and lilsislove >= 50 and money >= 150:
        $ alexisgrid = 2
        $ money -= 150
        "You bought a grid suit for [ls]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1hd:
    if cassandraheartdress == 1 and bigsiscorruption >= 30 and money >= 75:
        $ cassandraheartdress = 2
        $ money -= 75
        "You bought a heart dress for [bs]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1cl:
    if cassandralingerie == 1 and bigsiscorruption >= 60 and money >= 150:
        $ cassandralingerie = 2
        $ money -= 150
        "You bought lingerie for [bs]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1jo:
    if cassandrajeans == 1 and bigsislove >= 20 and money >= 75:
        $ cassandrajeans = 2
        $ money -= 75
        "You bought a jeans outfit for [bs]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop


label buy1pa:
    if cassandrapajama == 1 and bigsislove >= 50 and money >= 150:
        $ cassandrapajama = 2
        $ money -= 150
        "You bought pajamas for [bs]."
        jump shop
    else:
        "You don't fulfill all requirements."
        jump shop