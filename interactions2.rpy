



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
    default tt = Tooltip (" ")

    fixed:
        if dtime == 19 and club19middle == True:
            imagebutton auto "gui/icons/icon_left_%s.png" xpos 74 ypos 495 action (Hide ('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" xpos 1818 ypos 495 action (Hide ('clubicon'), Jump('club19chr')) hovered tt.Action ("Turn right") focus_mask True
        if dtime == 19 and club19right == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 956 ypos 380 action (Hide ('clubicon'), Jump('club19ik')) hovered tt.Action ("Go closer") focus_mask True
            imagebutton auto "gui/icons/icon_left_%s.png" xpos 74 ypos 495 action (Hide ('clubicon'), Jump('club19ch')) hovered tt.Action ("Turn left") focus_mask True
        if dtime == 19 and club19left == True:
            imagebutton auto "gui/icons/icon_left_%s.png" xpos 74 ypos 495 action (Hide ('clubicon'), Jump('club19chll')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" xpos 1818 ypos 495 action (Hide ('clubicon'), Jump('club19ch')) hovered tt.Action ("Turn right") focus_mask True
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 738 ypos 260 action (Hide ('clubicon'), Jump('club19kate')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 19 and club19leftleft == True:
            imagebutton auto "gui/icons/icon_right_%s.png" xpos 1818 ypos 495 action (Hide ('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn right") focus_mask True
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1706 ypos 250 action (Hide ('clubicon'), Jump('club19kate')) hovered tt.Action ("Go closer") focus_mask True
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 495 ypos 188 action (Hide ('clubicon'), Jump('club19bs')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 10 and clubmiddle == True:
            imagebutton auto "gui/icons/icon_left_%s.png" xpos 74 ypos 495 action (Hide ('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" xpos 1818 ypos 495 action (Hide ('clubicon'), Jump('club19chr')) hovered tt.Action ("Turn right") focus_mask True
        if dtime == 10 and clubright == True:
            imagebutton auto "gui/icons/icon_left_%s.png" xpos 74 ypos 495 action (Hide ('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 1133 ypos 356 action (Hide ('clubicon'), Jump('club9vivan')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 10 and clubleft == True:
            imagebutton auto "gui/icons/icon_left_%s.png" xpos 74 ypos 495 action (Hide ('clubicon'), Jump('club19chll')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" xpos 1818 ypos 495 action (Hide ('clubicon'), Jump('club19ch')) hovered tt.Action ("Turn right") focus_mask True
        if dtime == 10 and clubleftleft == True:
            imagebutton auto "gui/icons/icon_right_%s.png" xpos 1818 ypos 495 action (Hide ('clubicon'), Jump('club19chl')) hovered tt.Action ("Turn right") focus_mask True

    frame:
        xalign .5
        text tt.value




label subwayicon:
    call screen subwayicon1

screen subwayicon1():
    default tt = Tooltip (" ")

    fixed:
        if dtime == 7 and package >= 1 or dtime == 8 and package >= 1:
            imagebutton auto "gui/icons/icon_talk_%s.png" xpos 279 ypos 107 action (Hide ('subwayicon1'), Jump('subwaydeliever')) hovered tt.Action ("Talk") focus_mask True

        frame:
            xalign .5
            text tt.value


label fitnessicon:
    call screen fitnessicon1

screen fitnessicon1():
    default tt = Tooltip (" ")

    fixed:
        if dtime == 17:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1287 ypos 218 action (Hide ('fitnessicon1'), Jump('fitness_studio')) hovered tt.Action ("Go closer") focus_mask True
        if dtime == 9:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1287 ypos 218 action (Hide ('fitnessicon1'), Jump('fitness9am')) hovered tt.Action ("Go closer") focus_mask True

        frame:
            xalign .5
            text tt.value