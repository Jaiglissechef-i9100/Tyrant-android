
label messenger:

    $ messagepush = False
    call screen messenger1

screen messenger1():


    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phone.png" xpos 714 ypos 44
        imagebutton auto "gui/icons/icon_messenger_nicole_%s.png" xpos 782 ypos 175 action (Hide('messenger1'), Jump('mes_nicole')) hovered tt.Action ("Open the conversation with [mother]") focus_mask True
        if nicolenotification > 0:
            textbutton "{color=ff0000}[nicolenotification]{/color}" xpos 878 ypos 258



        if irinafirstmeet == True:
            imagebutton auto "gui/icons/icon_messenger_irina_%s.png" xpos 782 ypos 363 action (Hide('messenger1'), Jump('mes_irina')) hovered tt.Action ("Open the conversation with [irina]") focus_mask True
        if irinafirstmeet == True and irinanotification > 0:
            textbutton "{color=ff0000}[irinanotification]{/color}" xpos 878 ypos 452
        if NTR == True and messagedavidentr >= 1:
            imagebutton auto "gui/icons/icon_messenger_davide_%s.png" xpos 1000 ypos 363 action (Hide('messenger1'), Jump('mes_davide')) hovered tt.Action ("Open the conversation with Davide") focus_mask True
        if NTR == True and messagedavidentr >= 1 and davidenotification > 0:
            textbutton "{color=ff0000}[davidenotification]{/color}" xpos 1097 ypos 452

        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('messenger1'), Jump('phone1')) hovered tt.Action ("Close") focus_mask True


    frame:
        xalign .5
        text tt.value




label mes_nicole:

    $ nicolenotification = 0
    call screen conversation_nicole

screen conversation_nicole():


    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phone.png" xpos 714 ypos 44
        add "gui/icons/icon_messenger_nicole.png" xpos 763 ypos 167
        if inc == True:
            text "Mom" xpos 867 ypos 170
        else:
            text " [mother]" xpos 867 ypos 170
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1075 ypos 167 action (Hide('conversation_nicole'), Jump('messenger')) hovered tt.Action ("back") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('conversation_nicole'), Jump('messenger')) hovered tt.Action ("Close") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1218 ypos 452 action (Jump('replynicolelove1')) hovered tt.Action ("Reply [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1218 ypos 593 action (Jump('replynicolecorruption1')) hovered tt.Action ("Reply [cr1]") focus_mask True
        if messagenicolentr == 1 and weekend == True:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1218 ypos 734 action (Hide('conversation_nicole'), Jump('replynicolentr1')) hovered tt.Action ("Meet with her") focus_mask True

    viewport:
        area (746, 287, 426, 656)

        scrollbars "vertical"
        mousewheel True
        draggable True

        side_yfill False
        has vbox:
            xpos 750 ypos 287
        if messagenicolelove >= 1:
            textbutton "I'm so glad that you're back." style "chat_left"
        if replynicolelove == 1:
            textbutton "{color=00ff30}Me too.{/color}" style "chat_right"
        if replynicolecorruption == 1:
            textbutton "{color=ff0000}Me too.{/color}" style "chat_right"
        if messagenicolelove >= 2:
            textbutton "{u}New{/u}" style "chat_center"
            textbutton "I want to hold you [pov]" style "chat_left"
        if replynicolelove == 2:
            textbutton "{color=00ff30}Come find me :){/color}" style "chat_right"
            textbutton "You're so nice." style "chat_left"
        if replynicolecorruption == 2:
            textbutton "{color=ff0000}You can hold something else ;){/color}" style "chat_right"
            textbutton "What do you mean?" style "chat_left"
        if messagenicolelove >= 3:
            textbutton "{u}New{/u}" style "chat_center"
            textbutton "You deserve a treat <3" style "chat_left"
        if replynicolelove == 3:
            textbutton "{color=00ff30}I can't wait!{/color}" style "chat_right"
            textbutton "You'll love it." style "chat_left"
        if replynicolecorruption == 3:
            textbutton "{color=ff0000}Yes, I hope it's something good.{/color}" style "chat_right"
        if messagenicolelove >= 4:
            textbutton "{u}New{/u}" style "chat_center"
            textbutton "I think of you!" style "chat_left"
            imagebutton:
                idle "photo/nicole parentsroom evening.jpg" xpos 0.01
                action Show("zoompic", pic="photo/nicole parentsroom evening.jpg"), With(Dissolve(0.1))
                at customzoom
        if replynicolelove == 4:
            textbutton "{color=00ff30}I'll think of you too.{/color}" style "chat_right"
        if replynicolecorruption == 4:
            textbutton "{color=ff0000}Cum hard for me!{/color}" style "chat_right"


        if messagenicolentr == 1:
            textbutton "{u}New{/u}" style "chat_center"
            textbutton "I wait for you on the subway station." style "chat_left"



    frame:
        xalign .5
        text tt.value


label replynicolelove1:
    if messagenicolelove >= 1 and messagenicolelove < 2:
        $ replynicolelove = 1
        $ momlove += 1
    if messagenicolelove >= 2 and messagenicolelove < 3:
        $ replynicolelove = 2
        $ momlove += 1
    if messagenicolelove >= 3 and messagenicolelove < 4:
        $ replynicolelove = 3
        $ momlove += 1
    if messagenicolelove >= 4 and messagenicolelove < 5:
        $ replynicolelove = 4
        $ momlove += 1
    jump mes_nicole

label replynicolecorruption1:
    if messagenicolelove >= 1 and messagenicolelove < 2:
        $ replynicolecorruption = 1
        $ momcorruption += 1
    if messagenicolelove >= 2 and messagenicolelove < 3:
        $ replynicolecorruption = 2
        $ momcorruption += 1
    if messagenicolelove >= 3 and messagenicolelove < 4:
        $ replynicolecorruption = 3
        $ momcorruption += 1
    if messagenicolelove >= 4 and messagenicolelove < 5:
        $ replynicolecorruption = 4
        $ momcorruption += 1
    jump mes_nicole

label replynicolentr1:
    $ activatesubwayntr = True
    jump mes_nicole



label mes_davide:

    $ davidenotification = 0
    call screen conversation_davide

screen conversation_davide():


    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phone.png" xpos 714 ypos 44
        add "gui/icons/icon_messenger_davide.png" xpos 763 ypos 167
        text " Davide" xpos 867 ypos 170
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1075 ypos 167 action (Hide('conversation_davide'), Jump('messenger')) hovered tt.Action ("back") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('conversation_davide'), Jump('messenger')) hovered tt.Action ("Close") focus_mask True
        if NTR == True and messagedavidentr == 1:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1218 ypos 452 action (Hide('conversation_davide'), Jump('messagedavidentry')) hovered tt.Action ("Let it happen") focus_mask True
            imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1218 ypos 593 action (Hide('conversation_davide'), Jump('messagedavidentrn')) hovered tt.Action ("Don't allow it") focus_mask True



    viewport:
        area (746, 287, 426, 656)

        scrollbars "vertical"
        mousewheel True
        draggable True

        side_yfill False
        has vbox:
            xpos 750 ypos 287
        if messagedavidentr == 1:
            textbutton "Today is the day, bro." style "chat_left"
            if inc == True:
                textbutton "I'll ravage your little sister's pussy." style "chat_left"
            else:
                textbutton "I'll ravage [ls]'s pussy." style "chat_left"
        if replydavidentr == 1:
            textbutton "{color=00ff30}I'm sorry to cockblock you, but I can't allow this now!{/color}" style "chat_right"
            textbutton "{color=00ff30}You'll cancel your date or [mother] will know what you do with her innocent daughter.{/color}" style "chat_right"
            textbutton "You can't be serious." style "chat_left"
            textbutton "You won this time. But we've to talk about this!" style "chat_left"


    frame:
        xalign .5
        text tt.value


label messagedavidentry:
    scene black
    pov "{i}I don't care, they're are both adults. But I will spy on them.{/i}"
    $ activatesecretplacentr = True
    jump mes_davide

label messagedavidentrn:
    scene black
    pov "{i}I'll stop this now. My secret weapon is [mother].{/i}"
    "You wrote back."
    $ replydavidentr = 1
    jump mes_davide


label mes_irina:

    $ irinanotification = 0
    call screen conversation_irina

screen conversation_irina():


    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phone.png" xpos 714 ypos 44
        add "gui/icons/icon_messenger_irina.png" xpos 763 ypos 167
        text " [irina]" xpos 867 ypos 170
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1075 ypos 167 action (Hide('conversation_irina'), Jump('messenger')) hovered tt.Action ("back") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('conversation_irina'), Jump('messenger')) hovered tt.Action ("Close") focus_mask True


        if messageirina == 1 or messageirina == 2:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1218 ypos 452 action (Hide('conversation_irina'), Jump('replyirinayes1')) hovered tt.Action ("Yes") focus_mask True
            imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1218 ypos 593 action (Hide('conversation_irina'), Jump('replyirinano1')) hovered tt.Action ("No") focus_mask True



    viewport:
        area (746, 287, 426, 656)

        scrollbars "vertical"
        mousewheel True
        draggable True

        side_yfill False
        has vbox:
            xpos 750 ypos 287
        if messageirina == 1:
            textbutton "Do you want to go on a date with me? <3" style "chat_left"
        if replyirinayes == 1:
            textbutton "{color=00ff30}Yes, I'm on my way!{/color}" style "chat_right"
            textbutton "Great." style "chat_left"
        if replyirinano == 1:
            textbutton "{color=00ff30}Sorry, not today!{/color}" style "chat_right"
            textbutton "Oh, OK." style "chat_left"
        if messageirina == 2:
            textbutton "Come and see two girls having fun!" style "chat_left"
        if replyirinayes == 2:
            textbutton "{color=00ff30}Yes, I'm on my way!{/color}" style "chat_right"
        if replyirinano == 2:
            textbutton "{color=00ff30}Sorry, not today!{/color}" style "chat_right"



    frame:
        xalign .5
        text tt.value


label replyirinayes1:
    if messageirina == 1:
        $ messageirina = 0
        $ replyirinayes = 1
        $ activateirinadate = True
    elif messageirina == 2 and NTR == True and lilsisrelationship < 5:
        $ messageirina = 0
        $ replyirinayes = 2
        $ activateirinalesbianntr = True
    elif messageirina == 2:
        $ messageirina = 0
        $ replyirinayes = 2
        $ activateirinalesbian = True
    jump mes_irina

label replyirinano1:
    if messageirina == 1:
        $ replyirinano = 1
    if messageirina == 2:
        $ replyirinano = 2
    jump mes_irina
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
