#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label messenger:
    $ messagepush = False
    call screen messenger1

screen messenger1():
    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phone.png" xpos 714 ypos 44
        imagebutton auto "gui/icons/icon_messenger_nicole_%s.png" xpos 782 ypos 175 action (Hide('messenger1'), Jump('mes_nicole')) hovered Notify("Open the conversation with [mother]") focus_mask True
        if nicolenotification > 0:
            textbutton "{color=ff0000}[nicolenotification]{/color}" xpos 878 ypos 258

        if irinafirstmeet == True:
            imagebutton auto "gui/icons/icon_messenger_irina_%s.png" xpos 782 ypos 363 action (Hide('messenger1'), Jump('mes_irina')) hovered Notify("Open the conversation with [irina]") focus_mask True
        if irinafirstmeet == True and irinanotification > 0:
            textbutton "{color=ff0000}[irinanotification]{/color}" xpos 878 ypos 452
        if NTR == True and messagedavidentr >= 1:
            imagebutton auto "gui/icons/icon_messenger_davide_%s.png" xpos 1000 ypos 363 action (Hide('messenger1'), Jump('mes_davide')) hovered Notify("Open the conversation with Davide") focus_mask True
        if NTR == True and messagedavidentr >= 1 and davidenotification > 0:
            textbutton "{color=ff0000}[davidenotification]{/color}" xpos 1097 ypos 452

        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('messenger1'), Jump('phone1')) hovered Notify("Close") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1075 ypos 167 action (Hide('conversation_nicole'), Jump('messenger')) hovered Notify("back") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('conversation_nicole'), Jump('messenger')) hovered Notify("Close") focus_mask True
        if weekend == False:
            imagebutton auto "gui/icons/icon_love_%s.png" xpos 1218 ypos 452 action (Jump('replynicolelove1')) hovered Notify("Reply [lv1]") focus_mask True
            imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1218 ypos 593 action (Jump('replynicolecorruption1')) hovered Notify("Reply [cr1]") focus_mask True
        if messagenicolentr == 1 and weekend == True:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1218 ypos 734 action (Hide('conversation_nicole'), Jump('replynicolentr1')) hovered Notify("Meet with her") focus_mask True

    viewport:
        area (746, 287, 426, 656)

        scrollbars "vertical"
        mousewheel True
        draggable True

        side_yfill False
        has vbox:
            xpos 750 ypos 287
        if messagenicolelove >= 1:
            if inc == True:
                textbutton "I'm so glad you're back son. :)" style "chat_left"
            else:
                textbutton "I'm so glad you're back [pov]. :)" style "chat_left"
        #if replynicolelove == 1:
        if mcnicolereply1 == 1:
            textbutton "{color=00ff30}Me too.{/color}" style "chat_right"
        #if replynicolecorruption == 1:
        if mcnicolereply1 == 2:
            textbutton "{color=ff0000}Me too.{/color}" style "chat_right"

        if messagenicolelove >= 2:
            textbutton "{u}New{/u}" style "chat_center"
            if inc == True:
                textbutton "I want to hold you son!" style "chat_left"
            else:
                textbutton "I want to hold you [pov]!" style "chat_left"
        #if replynicolelove == 2:
        if mcnicolereply2 == 1:
            textbutton "{color=00ff30}Come find me! :){/color}" style "chat_right"
            textbutton "Don't think I won't track you down!" style "chat_left"
            textbutton "{color=00ff30}I can't wait... let know when you need a hint! Haha!{/color}" style "chat_right"
            textbutton "Oh I will!" style "chat_left"
        #if replynicolecorruption == 2:
        if mcnicolereply2 == 2:
            textbutton "{color=ff0000}You can definitely hold something of mine! ;){/color}" style "chat_right"
            textbutton "What do you mean?" style "chat_left"
            textbutton "{color=ff0000}8===D{/color}" style "chat_right"
            textbutton "Oh... ok. :)" style "chat_left"

        if messagenicolelove >= 3:
            textbutton "{u}New{/u}" style "chat_center"
            textbutton "You deserve a treat <3" style "chat_left"
            imagebutton:
                idle "photo/nicole boobs.jpg" xpos 0.01
                action Show("zoompic", pic="photo/nicole boobs.jpg"), With(Dissolve(0.1))
                at customzoom
        #if replynicolelove == 3:
        if mcnicolereply3 == 1:
            textbutton "{color=00ff30}That's an amazing treat!{/color}" style "chat_right"
            textbutton "I'm so glad you love it." style "chat_left"
        #if replynicolecorruption == 3:
        if mcnicolereply3 == 2:
            textbutton "{color=ff0000}Oh, I see. You're phone auto-corrected tits to treats! Haha.{/color}" style "chat_right"
            textbutton "Maybe... ;)" style "chat_left"

        if messagenicolelove >= 4:
            textbutton "{u}New{/u}" style "chat_center"
            textbutton "I'm thinking of you!" style "chat_left"
            imagebutton:
                idle "photo/nicole parentsroom evening.jpg" xpos 0.01
                action Show("zoompic", pic="photo/nicole parentsroom evening.jpg"), With(Dissolve(0.1))
                at customzoom
        #if replynicolelove == 4:
        if mcnicolereply4 == 1:
            textbutton "{color=00ff30}I'm thinking of you too.{/color}" style "chat_right"
        #if replynicolecorruption == 4:
        if mcnicolereply4 == 2:
            textbutton "{color=ff0000}Cum hard for me!{/color}" style "chat_right"

        if messagenicolentr == 1:
            textbutton "{u}New{/u}" style "chat_center"
            textbutton "I wait for you at the subway station." style "chat_left"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label replynicolelove1:
    if messagenicolelove >= 1 and messagenicolelove < 2:
        $ replynicolelove = 1
        $ momlove += 1
        $ mcreplynicole = 1
        $ mcnicolereply1 = 1 #----- Custom -----
    if messagenicolelove >= 2 and messagenicolelove < 3:
        $ replynicolelove = 2
        $ momlove += 1
        $ mcreplynicole = 2
        $ mcnicolereply2 = 1 #----- Custom -----
    if messagenicolelove >= 3 and messagenicolelove < 4:
        $ replynicolelove = 3
        $ momlove += 1
        $ mcreplynicole = 3
        $ mcnicolereply3 = 1 #----- Custom -----
    if messagenicolelove >= 4 and messagenicolelove < 5:
        $ replynicolelove = 4
        $ momlove += 1
        $ mcreplynicole = 4
        $ mcnicolereply4 = 1 #----- Custom -----
    jump mes_nicole

label replynicolecorruption1:
    if messagenicolelove >= 1 and messagenicolelove < 2:
        $ replynicolecorruption = 1
        $ momcorruption += 1
        $ mcreplynicole = 1
        $ mcnicolereply1 = 2 #----- Custom -----
    if messagenicolelove >= 2 and messagenicolelove < 3:
        $ replynicolecorruption = 2
        $ momcorruption += 1
        $ mcreplynicole = 2
        $ mcnicolereply2 = 2 #----- Custom -----
    if messagenicolelove >= 3 and messagenicolelove < 4:
        $ replynicolecorruption = 3
        $ momcorruption += 1
        $ mcreplynicole = 3
        $ mcnicolereply3 = 2 #----- Custom -----
    if messagenicolelove >= 4 and messagenicolelove < 5:
        $ replynicolecorruption = 4
        $ momcorruption += 1
        $ mcreplynicole = 4
        $ mcnicolereply4 = 2 #----- Custom -----
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
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1075 ypos 167 action (Hide('conversation_davide'), Jump('messenger')) hovered Notify("back") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('conversation_davide'), Jump('messenger')) hovered Notify("Close") focus_mask True
        if NTR == True and messagedavidentr == 1:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1218 ypos 452 action (Hide('conversation_davide'), Jump('messagedavidentry')) hovered Notify("Let it happen") focus_mask True
            imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1218 ypos 593 action (Hide('conversation_davide'), Jump('messagedavidentrn')) hovered Notify("Don't allow it") focus_mask True

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
                textbutton "I'm going to ravage your little sister's pussy." style "chat_left"
            else:
                textbutton "I'm going to ravage [ls]'s pussy." style "chat_left"
        if replydavidentr == 1:
            textbutton "{color=00ff30}Fuck that Davide!{/color}" style "chat_right"
            textbutton "{color=00ff30}If you go near her, I'll show [mother] what you plan do with her innocent daughter.{/color}" style "chat_right"
            textbutton "You can't be serious." style "chat_left"
            textbutton "{color=00ff30}Like a fucking heart attack.{/color}" style "chat_right"
            textbutton "You won this time. But you better believe we're going to have a talk about this shit!" style "chat_left"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label messagedavidentry:
    screen black
    povi "Who cares? They're are both adults. But I don't think I'm going to let her be alone with him. I'll check in on them."
    $ activatesecretplacentr = True
    jump mes_davide

label messagedavidentrn:
    screen black
    povi "I'm stopping this shit right now. I've got a secret weapon."
    "You write back."
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
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1075 ypos 167 action (Hide('conversation_irina'), Jump('messenger')) hovered Notify("back") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('conversation_irina'), Jump('messenger')) hovered Notify("Close") focus_mask True
        if messageirina == 3:
            imagebutton auto "gui/icons/icon_love_%s.png" xpos 1218 ypos 452 action (Jump('replyirinalove1')) hovered Notify("Reply [lv1]") focus_mask True
            imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1218 ypos 593 action (Jump('replyirinacorruption1')) hovered Notify("Reply [cr1]") focus_mask True
        elif messageirina == 1 or messageirina == 2:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1218 ypos 452 action (Hide('conversation_irina'), Jump('replyirinayes1')) hovered Notify("Yes") focus_mask True
            imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1218 ypos 593 action (Hide('conversation_irina'), Jump('replyirinano1')) hovered Notify("No") focus_mask True
        else:
            pass

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
            textbutton "Oh, OK. :(" style "chat_left"
        if messageirina == 2:
            textbutton "I've got a surprise for you! Come to the barn." style "chat_left"
        if replyirinayes == 2:
            textbutton "{color=00ff30}Sweet, I'm on my way!{/color}" style "chat_right"
            textbutton "Awesome!" style "chat_left"
        if replyirinano == 2:
            textbutton "{color=00ff30}Sorry, not today!{/color}" style "chat_right"
            textbutton "Boo. You're no fun! :(" style "chat_left"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
