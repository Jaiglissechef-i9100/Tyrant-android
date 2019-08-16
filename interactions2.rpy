#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label club19ch:
    if dtime == 19:
        scene town club main evening middle
        $ club19middle = True
        $ club19right = False
        $ club19left = False
        $ club19leftleft = False
        show screen townl
        call screen clubicon
    else:
        scene town club door middle
        $ clubmiddle = True
        $ clubright = False
        $ clubleft = False
        $ clubleftleft = False
        show screen townl
        call screen clubicon

label club19chr:
    if dtime == 19:
        scene town club main evening right
        $ club19right = True
        $ club19middle = False
        $ club19left = False
        $ club19leftleft = False
        show screen townl
        call screen clubicon
    else:
        scene town club door right
        $ clubmiddle = False
        $ clubright = True
        $ clubleft = False
        $ clubleftleft = False
        show screen townl
        call screen clubicon

label club19chl:
    if dtime == 19:
        scene town club main evening left
        $ club19left = True
        $ club19right = False
        $ club19middle = False
        $ club19leftleft = False
        show screen townl
        call screen clubicon
    else:
        scene town club door left
        $ clubmiddle = False
        $ clubright = False
        $ clubleft = True
        $ clubleftleft = False
        show screen townl
        call screen clubicon

label club19chll:
    if dtime == 19:
        scene town club main evening left left
        $ club19leftleft = True
        $ club19right = False
        $ club19middle = False
        $ club19left = False
        show screen townl
        call screen clubicon
    else:
        scene town club door left left
        $ clubmiddle = False
        $ clubright = False
        $ clubleft = False
        $ clubleftleft = True
        show screen townl
        call screen clubicon

screen clubicon():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 19 and club19middle == True:
            imagebutton auto "gui/icons/icon_left_%s.png" action (Hide('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" action (Hide('clubicon'), Jump('club19chr')) hovered tt.Action ("Turn right") focus_mask True
        if dtime == 19 and club19right == True:
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('clubicon'), Jump('club19ik')) hovered tt.Action ("Go closer") focus_mask True
            imagebutton auto "gui/icons/icon_left_%s.png" action (Hide('clubicon'), Jump('club19ch')) hovered tt.Action ("Turn left") focus_mask True
        if dtime == 19 and club19left == True:
            imagebutton auto "gui/icons/icon_left_%s.png" action (Hide('clubicon'), Jump('club19chll')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" action (Hide('clubicon'), Jump('club19ch')) hovered tt.Action ("Turn right") focus_mask True
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('clubicon'), Jump('club19kate')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 19 and club19leftleft == True:
            imagebutton auto "gui/icons/icon_right_%s.png" action (Hide('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn right") focus_mask True
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('clubicon'), Jump('club19kate')) hovered tt.Action ("Go closer") focus_mask True
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('clubicon'), Jump('club19bs')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 10 and clubmiddle == True:
            imagebutton auto "gui/icons/icon_left_%s.png" action (Hide('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" action (Hide('clubicon'), Jump('club19chr')) hovered tt.Action ("Turn right") focus_mask True
        if dtime == 10 and clubright == True:
            imagebutton auto "gui/icons/icon_left_%s.png" action (Hide('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn left") focus_mask True
            if knowaboutjobsleazy == False:
                imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('clubicon'), Jump('club9vivan')) hovered tt.Action ("Go closer") focus_mask True
            else:
                imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('clubicon'), Jump('club9vivanchoice')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 10 and clubleft == True:
            imagebutton auto "gui/icons/icon_left_%s.png" action (Hide('clubicon'), Jump('club19chll')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" action (Hide('clubicon'), Jump('club19ch')) hovered tt.Action ("Turn right") focus_mask True
        if dtime == 10 and clubleftleft == True:
            imagebutton auto "gui/icons/icon_right_%s.png" action (Hide('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn right") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label subwayicon:
    call screen subwayicon1

screen subwayicon1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 7 and package >= 1 or dtime == 8 and package >= 1:
            imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('subwayicon1'), Jump('subwaydeliever')) hovered tt.Action ("Talk") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label fitnessicon:
    call screen fitnessicon1

screen fitnessicon1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if dtime == 17:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnessicon1'), Jump('fitness_studio')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 9:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnessicon1'), Jump('fitness9am')) hovered tt.Action ("Go closer") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value
