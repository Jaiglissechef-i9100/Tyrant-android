#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label cheat:
    hide screen locations
    scene cheats
    call screen cheat1

screen cheat1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 242 ypos 434 action (Hide('cheat1'), Jump('cheatrelnraise')) hovered tt.Action ("+10 Relationship") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 366 ypos 434 action (Hide('cheat1'), Jump('cheatcornraise')) hovered tt.Action ("10 [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 171 ypos 434 action (Hide('cheat1'), Jump('cheatlovenraise')) hovered tt.Action ("10 [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 242 ypos 605 action (Hide('cheat1'), Jump('cheatrelndecrease')) hovered tt.Action ("-10 Relationship") focus_mask True

        imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 686 ypos 434 action (Hide('cheat1'), Jump('cheatrelaraise')) hovered tt.Action ("+10 Relationship") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 789 ypos 434 action (Hide('cheat1'), Jump('cheatcoraraise')) hovered tt.Action ("10 [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 611 ypos 434 action (Hide('cheat1'), Jump('cheatlovearaise')) hovered tt.Action ("10 [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 689 ypos 605 action (Hide('cheat1'), Jump('cheatreladecrease')) hovered tt.Action ("-10 Relationship") focus_mask True

        imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 1206 ypos 434 action (Hide('cheat1'), Jump('cheatrelcraise')) hovered tt.Action ("+10 Relationship") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1331 ypos 434 action (Hide('cheat1'), Jump('cheatcorcraise')) hovered tt.Action ("10 [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1086 ypos 434 action (Hide('cheat1'), Jump('cheatlovecraise')) hovered tt.Action ("10 [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 1206 ypos 605 action (Hide('cheat1'), Jump('cheatrelcdecrease')) hovered tt.Action ("-10 Relationship") focus_mask True

        imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 1658 ypos 434 action (Hide('cheat1'), Jump('cheatreliraise')) hovered tt.Action ("+10 Relationship") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1773 ypos 434 action (Hide('cheat1'), Jump('cheatcoriraise')) hovered tt.Action ("10 [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1553 ypos 434 action (Hide('cheat1'), Jump('cheatloveiraise')) hovered tt.Action ("10 [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 1658 ypos 605 action (Hide('cheat1'), Jump('cheatrelidecrease')) hovered tt.Action ("-10 Relationship") focus_mask True

        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 930 ypos 69 action (Hide('cheat1'), Jump('cheatend')) hovered tt.Action ("Close") focus_mask True

        frame:
            if tt.value == "" or tt.value ==" ":
                background None
            xalign .5
            text tt.value


label cheatrelnraise:
    "+10 Relationship Points"
    $ momrelationship += 10
    "Points now: [momrelationship]"
    jump cheat

label cheatcornraise:
    "+10 Corruption Points"
    $ momcorruption += 10
    "Points now: [momcorruption]"
    jump cheat

label cheatlovenraise:
    "+10 Love Points"
    $ momlove += 10
    "Points now: [momlove]"
    jump cheat

label cheatrelndecrease:
    "-10 Relationship Points"
    $ momrelationship -= 10
    "Points now: [momrelationship]"
    jump cheat



label cheatrelaraise:
    "+10 Relationship Points"
    $ lilsisrelationship += 10
    "Points now: [lilsisrelationship]"
    jump cheat

label cheatcoraraise:
    "+10 Corruption Points"
    $ lilsiscorruption += 10
    "Points now: [lilsiscorruption]"
    jump cheat

label cheatlovearaise:
    "+10 Love Points"
    $ lilsislove += 10
    "Points now: [lilsislove]"
    jump cheat

label cheatreladecrease:
    "-10 Relationship Points"
    $ lilsisrelationship -= 10
    "Points now: [lilsisrelationship]"
    jump cheat


label cheatrelcraise:
    "+10 Relationship Points"
    $ bigsisrelationship += 10
    "Points now: [bigsisrelationship]"
    jump cheat

label cheatcorcraise:
    "+10 Corruption Points"
    $ bigsiscorruption += 10
    "Points now: [bigsiscorruption]"
    jump cheat

label cheatlovecraise:
    "+10 Love Points"
    $ bigsislove += 10
    "Points now: [bigsislove]"
    jump cheat

label cheatrelcdecrease:
    "-10 Relationship Points"
    $ bigsisrelationship -= 10
    "Points now: [bigsisrelationship]"
    jump cheat


label cheatreliraise:
    "+10 Relationship Points"
    $ irinarelationship += 10
    "Points now: [irinarelationship]"
    jump cheat

label cheatcoriraise:
    "+10 Corruption Points"
    $ irinacorruption += 10
    "Points now: [irinacorruption]"
    jump cheat

label cheatloveiraise:
    "+10 Love Points"
    $ irinalove += 10
    "Points now: [irinalove]"
    jump cheat

label cheatrelidecrease:
    "-10 Relationship Points"
    $ irinarelationship -= 10
    "Points now: [irinarelationship]"
    jump cheat

label cheatend:
    jump mcroom
