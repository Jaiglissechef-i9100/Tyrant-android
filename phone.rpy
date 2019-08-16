#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

screen contacts():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneside.png" xpos 142 ypos 114
        add "gui/icons/nicole.png" xpos 375 ypos 153
        add "gui/icons/alexis.png" xpos 812 ypos 153
        add "gui/icons/cassandra.png" xpos 1246 ypos 153
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide('contacts'), Jump('phone1')) hovered Notify("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide('contacts'), Show('contacts4', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide('contacts'), Show('contacts1', transition=None)) hovered Notify("Next") focus_mask True

    vbox:
        xpos 335 ypos 506
        if inc == True:
            text "Mom"
        else:
            text "[mother]"
        if momrelationship >= 30:
            text "Relationship: {color=3cff00}[momrelationship]{/color}"
        elif momrelationship < 30 and momrelationship >= 6:
            text "Relationship: {color=ffd200}[momrelationship]{/color}"
        elif momrelationship < 6:
            text "Relationship: {color=ff0000}[momrelationship]{/color}"
        text "[lv1]: [momlove]"
        text "[cr1]: [momcorruption]"
        if NTR == True:
            if nicole_ntr == False and nicole_voyeur == False and nicole_revenge == False and nicole_sadist == False:
                text "Darker Paths: undecided"
            elif nicole_ntr == True:
                text "Darker Paths: {color=ff0000}NTR{/color}"
            elif nicole_voyeur == True:
                text "Darker Paths: {color=3cff00}Voyeur{/color}"
            elif nicole_revenge == True:
                text "Darker Paths: {color=3cff00}Revenge{/color}"
            elif nicole_sadist == True:
                text "Darker Paths: {color=ff0000}Sadist{/color}"
    vbox:
        xpos 772 ypos 506
        text "[ls]"
        if lilsisrelationship >= 40:
            text "Relationship: {color=3cff00}[lilsisrelationship]{/color}"
        elif lilsisrelationship < 40 and lilsisrelationship >= 6:
            text "Relationship: {color=ffd200}[lilsisrelationship]{/color}"
        elif lilsisrelationship < 6:
            text "Relationship: {color=ff0000}[lilsisrelationship]{/color}"
        text "[lv1]: [lilsislove]"
        text "[cr1]: [lilsiscorruption]"
        if NTR == True:
            if alexis_ntr == False and alexis_voyeur == False and alexis_revenge == False and alexis_sadist == False:
                text "Darker Paths: undecided"
            elif alexis_ntr == True:
                text "Darker Paths: {color=ff0000}NTR{/color}"
            elif alexis_voyeur == True:
                text "Darker Paths: {color=3cff00}Voyeur{/color}"
            elif alexis_revenge == True:
                text "Darker Paths: {color=3cff00}Revenge{/color}"
            elif alexis_sadist == True:
                text "Darker Paths: {color=ff0000}Sadist{/color}"
    vbox:
        xpos 1209 ypos 506
        text "[bs]"
        if bigsisrelationship >= 30:
            text "Relationship: {color=3cff00}[bigsisrelationship]{/color}"
        elif bigsisrelationship < 30 and bigsisrelationship >= 6:
            text "Relationship: {color=ffd200}[bigsisrelationship]{/color}"
        elif bigsisrelationship < 6:
            text "Relationship: {color=ff0000}[bigsisrelationship]{/color}"
        text "[lv1]: [bigsislove]"
        text "[cr1]: [bigsiscorruption]"
        if NTR == True:
            if cassandra_ntr == False and cassandra_voyeur == False and cassandra_revenge == False and cassandra_sadist == False:
                text "Darker Paths: undecided"
            elif cassandra_ntr == True:
                text "Darker Paths: {color=ff0000}NTR{/color}"
            elif cassandra_voyeur == True:
                text "Darker Paths: {color=3cff00}Voyeur{/color}"
            elif cassandra_revenge == True:
                text "Darker Paths: {color=3cff00}Revenge{/color}"
            elif cassandra_sadist == True:
                text "Darker Paths: {color=ff0000}Sadist{/color}"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value


screen contacts1():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneside.png" xpos 142 ypos 114
        add "gui/icons/bruce.png" xpos 375 ypos 153
        add "gui/icons/davide.png" xpos 812 ypos 153
        add "gui/icons/steve.png" xpos 1246 ypos 153
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide('contacts1'), Jump('phone1')) hovered Notify("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide('contacts1'), Show('contacts', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide('contacts1'), Show('contacts2', transition=None)) hovered Notify("Next") focus_mask True
    vbox:
        xpos 335 ypos 506
        if inc == True:
            text "Dad"
        else:
            text "Bruce"
        text "[gd1]: [dadgood]"
        text "[bd1]: [dadbad]"
    vbox:
        xpos 772 ypos 506
        text "Davide"
        text "[gd1]: [davidegood]"
        text "[bd1]: [davidebad]"
    vbox:
        xpos 1209 ypos 506
        text "Steve"
        text "[gd1]: [stevegood]"
        text "[bd1]: [stevebad]"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

screen contacts2():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneside.png" xpos 142 ypos 114
        if irinafirstmeet == True:
            add "gui/icons/irina.png" xpos 375 ypos 153
        else:
            add "gui/icons/unknown.png" xpos 375 ypos 153
        if martinfirstmeet == True:
            add "gui/icons/martin.png" xpos 812 ypos 153
        else:
            add "gui/icons/unknown.png" xpos 812 ypos 153
        if susanfirstmeet == True:
            add "gui/icons/susan.png" xpos 1246 ypos 153
        else:
            add "gui/icons/unknown.png" xpos 1246 ypos 153
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide('contacts2'), Jump('phone1')) hovered Notify("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide('contacts2'), Show('contacts1', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide('contacts2'), Show('contacts3', transition=None)) hovered Notify("Next") focus_mask True
    vbox:
        xpos 335 ypos 506
        if irinafirstmeet == True:
            text "[irina]"
        else:
            text "Unknown"
        if irinarelationship >= 20:
            text "Relationship: {color=3cff00}[irinarelationship]{/color}"
        elif irinarelationship < 20 and irinarelationship >= 6:
            text "Relationship: {color=ffd200}[irinarelationship]{/color}"
        elif irinarelationship < 6:
            text "Relationship: {color=ff0000}[irinarelationship]{/color}"
        text "[lv1]: [irinalove]"
        text "[cr1]: [irinacorruption]"
        if NTR == True:
            if irina_ntr == False and irina_voyeur == False and irina_revenge == False and irina_sadist == False:
                text "Darker Paths: undecided"
            elif irina_ntr == True:
                text "Darker Paths: {color=ff0000}NTR{/color}"
            elif irina_voyeur == True:
                text "Darker Paths: {color=3cff00}Voyeur{/color}"
            elif irina_revenge == True:
                text "Darker Paths: {color=3cff00}Revenge{/color}"
            elif irina_sadist == True:
                text "Darker Paths: {color=ff0000}Sadist{/color}"
    vbox:
        xpos 772 ypos 506
        if martinfirstmeet == True:
            text "Martin"
        else:
            text "Unknown"
        text "[gd1]: [martingood]"
        text "[bd1]: [martinbad]"
    vbox:
        xpos 1209 ypos 506
        if susanfirstmeet == True:
            text "[susan]"
        else:
            text "Unknown"
        if susanrelationship >= 20:
            text "Relationship: {color=3cff00}[susanrelationship]{/color}"
        elif susanrelationship < 20 and susanrelationship >= 6:
            text "Relationship: {color=ffd200}[susanrelationship]{/color}"
        elif susanrelationship < 6:
            text "Relationship: {color=ff0000}[susanrelationship]{/color}"
        text "[lv1]: [susanlove]"
        text "[cr1]: [susancorruption]"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

screen contacts3():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneside.png" xpos 142 ypos 114
        if vivianfirstmeet == True:
            add "gui/icons/vivian.png" xpos 375 ypos 153
        else:
            add "gui/icons/unknown.png" xpos 375 ypos 153
        if katefirstmeet == True:
            add "gui/icons/kate.png" xpos 812 ypos 153
        else:
            add "gui/icons/unknown.png" xpos 812 ypos 153
        if frankfirstmeet == True:
            add "gui/icons/frank.png" xpos 1246 ypos 153
        else:
            add "gui/icons/unknown.png" xpos 1246 ypos 153
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide('contacts3'), Jump('phone1')) hovered Notify("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide('contacts3'), Show('contacts2', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide('contacts3'), Show('contacts4', transition=None)) hovered Notify("Next") focus_mask True
    vbox:
        xpos 335 ypos 506
        if vivianfirstmeet == True:
            text "[vivian]"
        else:
            text "Unknown"
        if vivianrelationship >= 30:
            text "Relationship: {color=3cff00}[vivianrelationship]{/color}"
        elif vivianrelationship < 30 and vivianrelationship >= 6:
            text "Relationship: {color=ffd200}[vivianrelationship]{/color}"
        elif vivianrelationship < 6:
            text "Relationship: {color=ff0000}[vivianrelationship]{/color}"
        text "[lv1]: [vivianlove]"
        text "[cr1]: [viviancorruption]"
    vbox:
        xpos 772 ypos 506
        if katefirstmeet == True:
            text "[kate]"
        else:
            text "Unknown"
        if katerelationship >= 40:
            text "Relationship: {color=3cff00}[katerelationship]{/color}"
        elif katerelationship < 40 and katerelationship >= 6:
            text "Relationship: {color=ffd200}[katerelationship]{/color}"
        elif katerelationship < 6:
            text "Relationship: {color=ff0000}[katerelationship]{/color}"
        text "[lv1]: [katelove]"
        text "[cr1]: [katecorruption]"
    vbox:
        xpos 1209 ypos 506
        if frankfirstmeet == True:
            text "Frank"
        else:
            text "Unknown"
        text "[gd1]: [frankgood]"
        text "[bd1]: [frankbad]"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

screen contacts4():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/phoneside.png" xpos 142 ypos 114
        if mirandafirstmeet == True:
            add "gui/icons/miranda.png" xpos 375 ypos 153
        else:
            add "gui/icons/unknown.png" xpos 375 ypos 153
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide('contacts4'), Jump('phone1')) hovered Notify("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide('contacts4'), Show('contacts3', transition=None)) hovered Notify("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide('contacts4'), Show('contacts', transition=None)) hovered Notify("Next") focus_mask True
    vbox:
        xpos 335 ypos 506
        if mirandafirstmeet == True:
            text "[miranda]"
        else:
            text "Unknown"
        if mirandarelationship >= 30:
            text "Relationship: {color=3cff00}[mirandarelationship]{/color}"
        elif mirandarelationship < 30 and mirandarelationship >= 6:
            text "Relationship: {color=ffd200}[mirandarelationship]{/color}"
        elif mirandarelationship < 6:
            text "Relationship: {color=ff0000}[mirandarelationship]{/color}"
        text "[lv1]: [mirandalove]"
        text "[cr1]: [mirandacorruption]"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

# ----- Custom Code -----

label phonecheat:
    show screen hud
    call screen cheats

screen cheats():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        #----- Phone Backgroung -----
        add "gui/icons/phoneside.png" xpos 142 ypos 114

        #----- Nicole -----
        imagebutton auto "gui/icons/icon_hug_%s.png" xpos 360 ypos 175 action (SetVariable('momrelationship', momrelationship+10), Notify("[rp1] Points now: [momrelationship]")) hovered Notify("+10 [rp1] Nicole") focus_mask True
        imagebutton auto "gui/icons/icon_slap_%s.png" xpos 435 ypos 175 action (SetVariable('momrelationship', momrelationship-10), Notify("[rp1] Points now: [momrelationship]")) hovered Notify("-10 [rp1] Nicole") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 510 ypos 175 action (SetVariable('momlove', momlove+10), Notify("[lv1] Points now: [momlove]")) hovered Notify("10 [lv1] Nicole") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 585 ypos 175 action (SetVariable('momcorruption', momcorruption+10), Notify("[cr1] Points now: [momcorruption]")) hovered Notify("10 [cr1] Nicole") focus_mask True
        if perma_voyeur_nicole == True:
            imagebutton auto "images/edited/gui/paths/icon_voyeuron_%s.png" xpos 660 ypos 175 action (SetVariable('perma_voyeur_nicole', False), SetVariable('perma_ntr_nicole', False), SetVariable('perma_revenge_nicole', False), SetVariable('perma_sadist_nicole', False), Notify("Voyeur Path Off for Nicole")) hovered Notify("Turn off Voyeur - Nicole") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" xpos 660 ypos 175 action (SetVariable('perma_voyeur_nicole', True), SetVariable('perma_ntr_nicole', False), SetVariable('perma_revenge_nicole', False), SetVariable('perma_sadist_nicole', False), Notify("Voyeur Path Active for Nicole")) hovered Notify("Force Voyeur - Nicole") focus_mask True
        if perma_ntr_nicole == True:
            imagebutton auto "images/edited/gui/paths/icon_ntron_%s.png" xpos 735 ypos 175 action (SetVariable('perma_voyeur_nicole', False), SetVariable('perma_ntr_nicole', False), SetVariable('perma_revenge_nicole', False), SetVariable('perma_sadist_nicole', False), Notify("NTR Path Off for Nicole")) hovered Notify("Turn off NTR - Nicole") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" xpos 735 ypos 175 action (SetVariable('perma_voyeur_nicole', False), SetVariable('perma_ntr_nicole', True), SetVariable('perma_revenge_nicole', False), SetVariable('perma_sadist_nicole', False), Notify("NTR Path Active for Nicole")) hovered Notify("Force NTR - Nicole") focus_mask True
        if perma_revenge_nicole == True:
            imagebutton auto "images/edited/gui/paths/icon_revengeon_%s.png" xpos 810 ypos 175 action (SetVariable('perma_voyeur_nicole', False), SetVariable('perma_ntr_nicole', False), SetVariable('perma_revenge_nicole', False), SetVariable('perma_sadist_nicole', False), Notify("Revenge Path Off for Nicole")) hovered Notify("Turn off Revenge - Nicole") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" xpos 810 ypos 175 action (SetVariable('perma_voyeur_nicole', False), SetVariable('perma_ntr_nicole', False), SetVariable('perma_revenge_nicole', True), SetVariable('perma_sadist_nicole', False), Notify("Revenge Path Active for Nicole")) hovered Notify("Force Revenge - Nicole") focus_mask True
        if perma_sadist_nicole == True:
            imagebutton auto "images/edited/gui/paths/icon_sadiston_%s.png" xpos 885 ypos 175 action (SetVariable('perma_voyeur_nicole', False), SetVariable('perma_ntr_nicole', False), SetVariable('perma_revenge_nicole', False), SetVariable('perma_sadist_nicole', False), Notify("Sadist Path Off for Nicole")) hovered Notify("Turn off Sadist - Nicole") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" xpos 885 ypos 175 action (SetVariable('perma_voyeur_nicole', False), SetVariable('perma_ntr_nicole', False), SetVariable('perma_revenge_nicole', False), SetVariable('perma_sadist_nicole', True), Notify("Sadist Path Active for Nicole")) hovered Notify("Force Sadist - Nicole") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 960 ypos 175 action (SetVariable('nicole_voyeur', False), SetVariable('nicole_ntr', False), SetVariable('nicole_revenge', False), SetVariable('nicole_sadist', False), Notify("All Dark Paths Off for Nicole")) hovered Notify("Turn Off Darker Paths - Nicole") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1035 ypos 175 action (SetVariable('momrelationship', 0), SetVariable('momcorruption', 0), SetVariable('momlove', 0), Notify("[lv2], [cr2], [rp2] Points Cleared for Nicole")) hovered Notify("Clear Stats - Nicole") focus_mask True
        imagebutton:
            auto "images/edited/icons/nicole_%s.png"
            xpos 1110
            ypos 175
            action [
            SetVariable('nicolenotification', 0),
            SetVariable('mcreplynicole', 0),
            SetVariable('messagenicolelove', 0),
            SetVariable('replynicolelove', 0),
            SetVariable('replynicolecorruption', 0),
            SetVariable('mcnicolereply1', 0),
            SetVariable('mcnicolereply2', 0),
            SetVariable('mcnicolereply3', 0),
            SetVariable('mcnicolereply4', 0),
            Notify("Nicole's Messages are Reset")
            ]
            hovered Notify("Reset Nicole's Messages")
            focus_mask True

        #---- Alexis -----
        imagebutton auto "gui/icons/icon_hug_%s.png" xpos 360 ypos 250 action (SetVariable('lilsisrelationship', lilsisrelationship+10), Notify("[rp1] Points now: [lilsisrelationship]")) hovered Notify("+10 [rp1] Alexis") focus_mask True
        imagebutton auto "gui/icons/icon_slap_%s.png" xpos 435 ypos 250 action (SetVariable('lilsisrelationship', lilsisrelationship-10), Notify("[rp1] Points now: [lilsisrelationship]")) hovered Notify("-10 [rp1] Alexis") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 510 ypos 250 action (SetVariable('lilsislove', lilsislove+10), Notify("[lv1] Points now: [lilsislove]")) hovered Notify("10 [lv1] Alexis") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 585 ypos 250 action (SetVariable('lilsiscorruption', lilsiscorruption+10), Notify("[cr1] Points now: [lilsiscorruption]")) hovered Notify("10 [cr1] Alexis") focus_mask True
        if perma_voyeur_alexis == True:
            imagebutton auto "images/edited/gui/paths/icon_voyeuron_%s.png" xpos 660 ypos 250 action (SetVariable('perma_voyeur_alexis', False), SetVariable('perma_ntr_alexis', False), SetVariable('perma_revenge_alexis', False), SetVariable('perma_sadist_alexis', False), Notify("Voyeur Path Off for Alexis")) hovered Notify("Turn off Voyeur - Alexis") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" xpos 660 ypos 250 action (SetVariable('perma_voyeur_alexis', True), SetVariable('perma_ntr_alexis', False), SetVariable('perma_revenge_alexis', False), SetVariable('perma_sadist_alexis', False), Notify("Voyeur Path Active for Alexis")) hovered Notify("Force Voyeur - Alexis") focus_mask True
        if perma_ntr_alexis == True:
            imagebutton auto "images/edited/gui/paths/icon_ntron_%s.png" xpos 735 ypos 250 action (SetVariable('perma_voyeur_alexis', False), SetVariable('perma_ntr_alexis', False), SetVariable('perma_revenge_alexis', False), SetVariable('perma_sadist_alexis', False), Notify("NTR Path Off for Alexis")) hovered Notify("Turn off NTR - Alexis") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" xpos 735 ypos 250 action (SetVariable('perma_voyeur_alexis', False), SetVariable('perma_ntr_alexis', True), SetVariable('perma_revenge_alexis', False), SetVariable('perma_sadist_alexis', False), Notify("NTR Path Active for Alexis")) hovered Notify("Force NTR - Alexis") focus_mask True
        if perma_revenge_alexis == True:
            imagebutton auto "images/edited/gui/paths/icon_revengeon_%s.png" xpos 810 ypos 250 action (SetVariable('perma_voyeur_alexis', False), SetVariable('perma_ntr_alexis', False), SetVariable('perma_revenge_alexis', False), SetVariable('perma_sadist_alexis', False), Notify("Revenge Path Off for Alexis")) hovered Notify("Turn off Revenge - Alexis") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" xpos 810 ypos 250 action (SetVariable('perma_voyeur_alexis', False), SetVariable('perma_ntr_alexis', False), SetVariable('perma_revenge_alexis', True), SetVariable('perma_sadist_alexis', False), Notify("Revenge Path Active for Alexis")) hovered Notify("Force Revenge - Alexis") focus_mask True
        if perma_sadist_alexis == True:
            imagebutton auto "images/edited/gui/paths/icon_sadiston_%s.png" xpos 885 ypos 250 action (SetVariable('perma_voyeur_alexis', False), SetVariable('perma_ntr_alexis', False), SetVariable('perma_revenge_alexis', False), SetVariable('perma_sadist_alexis', False), Notify("Sadist Path Off for Alexis")) hovered Notify("Turn off Sadist - Alexis") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" xpos 885 ypos 250 action (SetVariable('perma_voyeur_alexis', False), SetVariable('perma_ntr_alexis', False), SetVariable('perma_revenge_alexis', False), SetVariable('perma_sadist_alexis', True), Notify("Sadist Path Active for Alexis")) hovered Notify("Force Sadist - Alexis") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 960 ypos 250 action (SetVariable('alexis_voyeur', False), SetVariable('alexis_ntr', False), SetVariable('alexis_revenge', False), SetVariable('alexis_sadist', False), Notify("All Dark Paths Off for Alexis")) hovered Notify("Turn Off Darker Paths - Alexis") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1035 ypos 250 action (SetVariable('lilsisrelationship', 0), SetVariable('lilsiscorruption', 0), SetVariable('lilsislove', 0), Notify("[lv2], [cr2], [rp2] Points Cleared for Alexis")) hovered Notify("Clear Stats - Alexis") focus_mask True
        add "images/edited/icons/alexis_idle.png" xpos 1110 ypos 250

        #----- Cassandra -----
        imagebutton auto "gui/icons/icon_hug_%s.png" xpos 360 ypos 325 action (SetVariable('bigsisrelationship', bigsisrelationship+10), Notify("[rp1] Points now: [bigsisrelationship]")) hovered Notify("+10 [rp1] Cassandra") focus_mask True
        imagebutton auto "gui/icons/icon_slap_%s.png" xpos 435 ypos 325 action (SetVariable('bigsisrelationship', bigsisrelationship-10), Notify("[rp1] Points now: [bigsisrelationship]")) hovered Notify("-10 [rp1] Cassandra") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 510 ypos 325 action (SetVariable('bigsislove', bigsislove+10), Notify("[lv1] Points now: [bigsislove]")) hovered Notify("10 [lv1] Cassandra") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 585 ypos 325 action (SetVariable('bigsiscorruption', bigsiscorruption+10), Notify("[cr1] Points now: [bigsiscorruption]")) hovered Notify("10 [cr1] Cassandra") focus_mask True
        if perma_voyeur_cassandra == True:
            imagebutton auto "images/edited/gui/paths/icon_voyeuron_%s.png" xpos 660 ypos 325 action (SetVariable('perma_voyeur_cassandra', False), SetVariable('perma_ntr_cassandra', False), SetVariable('perma_revenge_cassandra', False), SetVariable('perma_sadist_cassandra', False), Notify("Voyeur Path Off for Cassandra")) hovered Notify("Turn off Voyeur - Cassandra") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" xpos 660 ypos 325 action (SetVariable('perma_voyeur_cassandra', True), SetVariable('perma_ntr_cassandra', False), SetVariable('perma_revenge_cassandra', False), SetVariable('perma_sadist_cassandra', False), Notify("Voyeur Path Active for Cassandra")) hovered Notify("Force Voyeur - Cassandra") focus_mask True
        if perma_ntr_cassandra == True:
            imagebutton auto "images/edited/gui/paths/icon_ntron_%s.png" xpos 735 ypos 325 action (SetVariable('perma_voyeur_cassandra', False), SetVariable('perma_ntr_cassandra', False), SetVariable('perma_revenge_cassandra', False), SetVariable('perma_sadist_cassandra', False), Notify("NTR Path Off for Cassandra")) hovered Notify("Turn off NTR - Cassandra") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" xpos 735 ypos 325 action (SetVariable('perma_voyeur_cassandra', False), SetVariable('perma_ntr_cassandra', True), SetVariable('perma_revenge_cassandra', False), SetVariable('perma_sadist_cassandra', False), Notify("NTR Path Active for Cassandra")) hovered Notify("Force NTR - Cassandra") focus_mask True
        if perma_revenge_cassandra == True:
            imagebutton auto "images/edited/gui/paths/icon_revengeon_%s.png" xpos 810 ypos 325 action (SetVariable('perma_voyeur_cassandra', False), SetVariable('perma_ntr_cassandra', False), SetVariable('perma_revenge_cassandra', False), SetVariable('perma_sadist_cassandra', False), Notify("Revenge Path Off for Cassandra")) hovered Notify("Turn off Revenge - Cassandra") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" xpos 810 ypos 325 action (SetVariable('perma_voyeur_cassandra', False), SetVariable('perma_ntr_cassandra', False), SetVariable('perma_revenge_cassandra', True), SetVariable('perma_sadist_cassandra', False), Notify("Revenge Path Active for Cassandra")) hovered Notify("Force Revenge - Cassandra") focus_mask True
        if perma_sadist_cassandra == True:
            imagebutton auto "images/edited/gui/paths/icon_sadiston_%s.png" xpos 885 ypos 325 action (SetVariable('perma_voyeur_cassandra', False), SetVariable('perma_ntr_cassandra', False), SetVariable('perma_revenge_cassandra', False), SetVariable('perma_sadist_cassandra', False), Notify("Sadist Path Off for Cassandra")) hovered Notify("Turn off Sadist - Cassandra") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" xpos 885 ypos 325 action (SetVariable('perma_voyeur_cassandra', False), SetVariable('perma_ntr_cassandra', False), SetVariable('perma_revenge_cassandra', False), SetVariable('perma_sadist_cassandra', True), Notify("Sadist Path Active for Cassandra")) hovered Notify("Force Sadist - Cassandra") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 960 ypos 325 action (SetVariable('cassandra_voyeur', False), SetVariable('cassandra_ntr', False), SetVariable('cassandra_revenge', False), SetVariable('cassandra_sadist', False), Notify("All Dark Paths Off for Cassandra")) hovered Notify("Turn Off Darker Paths - Cassandra") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1035 ypos 325 action (SetVariable('bigsisrelationship', 0), SetVariable('bigsiscorruption', 0), SetVariable('bigsislove', 0), Notify("[lv2], [cr2], [rp2] Points Cleared for Cassandra")) hovered Notify("Clear Stats - Cassandra") focus_mask True
        add "images/edited/icons/cassandra_idle.png" xpos 1110 ypos 325

        #----- Irina -----
        imagebutton auto "gui/icons/icon_hug_%s.png" xpos 360 ypos 400 action (SetVariable('irinarelationship', irinarelationship+10), Notify("[rp1] Points now: [irinarelationship]")) hovered Notify("+10 [rp1] Irina") focus_mask True
        imagebutton auto "gui/icons/icon_slap_%s.png" xpos 435 ypos 400 action (SetVariable('irinarelationship', irinarelationship-10), Notify("[rp1] Points now: [irinarelationship]")) hovered Notify("-10 [rp1] Irina") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 510 ypos 400 action (SetVariable('irinalove', irinalove+10), Notify("[lv1] Points now: [irinalove]")) hovered Notify("10 [lv1] Irina") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 585 ypos 400 action (SetVariable('irinacorruption', irinacorruption+10), Notify("[cr1] Points now: [irinacorruption]")) hovered Notify("10 [cr1] Irina") focus_mask True
        if perma_voyeur_irina == True:
            imagebutton auto "images/edited/gui/paths/icon_voyeuron_%s.png" xpos 660 ypos 400 action (SetVariable('perma_voyeur_irina', False), SetVariable('perma_ntr_irina', False), SetVariable('perma_revenge_irina', False), SetVariable('perma_sadist_irina', False), Notify("Voyeur Path Off for Irina")) hovered Notify("Turn off Voyeur - Irina") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" xpos 660 ypos 400 action (SetVariable('perma_voyeur_irina', True), SetVariable('perma_ntr_irina', False), SetVariable('perma_revenge_irina', False), SetVariable('perma_sadist_irina', False), Notify("Voyeur Path Active for Irina")) hovered Notify("Force Voyeur - Irina") focus_mask True
        if perma_ntr_irina == True:
            imagebutton auto "images/edited/gui/paths/icon_ntron_%s.png" xpos 735 ypos 400 action (SetVariable('perma_voyeur_irina', False), SetVariable('perma_ntr_irina', False), SetVariable('perma_revenge_irina', False), SetVariable('perma_sadist_irina', False), Notify("NTR Path Off for Irina")) hovered Notify("Turn off NTR - Irina") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" xpos 735 ypos 400 action (SetVariable('perma_voyeur_irina', False), SetVariable('perma_ntr_irina', True), SetVariable('perma_revenge_irina', False), SetVariable('perma_sadist_irina', False), Notify("NTR Path Active for Irina")) hovered Notify("Force NTR - Irina") focus_mask True
        if perma_revenge_irina == True:
            imagebutton auto "images/edited/gui/paths/icon_revengeon_%s.png" xpos 810 ypos 400 action (SetVariable('perma_voyeur_irina', False), SetVariable('perma_ntr_irina', False), SetVariable('perma_revenge_irina', False), SetVariable('perma_sadist_irina', False), Notify("Revenge Path Off for Irina")) hovered Notify("Turn off Revenge - Irina") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" xpos 810 ypos 400 action (SetVariable('perma_voyeur_irina', False), SetVariable('perma_ntr_irina', False), SetVariable('perma_revenge_irina', True), SetVariable('perma_sadist_irina', False), Notify("Revenge Path Active for Irina")) hovered Notify("Force Revenge - Irina") focus_mask True
        if perma_sadist_irina == True:
            imagebutton auto "images/edited/gui/paths/icon_sadiston_%s.png" xpos 885 ypos 400 action (SetVariable('perma_voyeur_irina', False), SetVariable('perma_ntr_irina', False), SetVariable('perma_revenge_irina', False), SetVariable('perma_sadist_irina', False), Notify("Sadist Path Off for Irina")) hovered Notify("Turn off Sadist - Irina") focus_mask True
        else:
            imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" xpos 885 ypos 400 action (SetVariable('perma_voyeur_irina', False), SetVariable('perma_ntr_irina', False), SetVariable('perma_revenge_irina', False), SetVariable('perma_sadist_irina', True), Notify("Sadist Path Active for Irina")) hovered Notify("Force Sadist - Irina") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 960 ypos 400 action (SetVariable('irina_voyeur', False), SetVariable('irina_ntr', False), SetVariable('irina_revenge', False), SetVariable('irina_sadist', False), Notify("All Dark Paths Off for Irina")) hovered Notify("Turn Off Darker Paths - Irina") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1035 ypos 400 action (SetVariable('irinarelationship', 0), SetVariable('irinacorruption', 0), SetVariable('irinalove', 0), Notify("[lv2], [cr2], [rp2] Points Cleared for Irina")) hovered Notify("Clear Stats - Irina") focus_mask True
        add "images/edited/icons/irina_idle.png" xpos 1110 ypos 400

        #----- Vivian -----
        imagebutton auto "gui/icons/icon_hug_%s.png" xpos 360 ypos 475 action (SetVariable('vivianrelationship', vivianrelationship+10), Notify("[rp1] Points now: [vivianrelationship]")) hovered Notify("+10 [rp1] Vivian") focus_mask True
        imagebutton auto "gui/icons/icon_slap_%s.png" xpos 435 ypos 475 action (SetVariable('vivianrelationship', vivianrelationship-10), Notify("[rp1] Points now: [vivianrelationship]")) hovered Notify("-10 [rp1] Vivian") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 510 ypos 475 action (SetVariable('vivianlove', vivianlove+10), Notify("[lv1] Points now: [vivianlove]")) hovered Notify("10 [lv1] Vivian") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 585 ypos 475 action (SetVariable('viviancorruption', viviancorruption+10), Notify("[cr1] Points now: [viviancorruption]")) hovered Notify("10 [cr1] Vivian") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" xpos 660 ypos 475 action (SetVariable('vivian_voyeur', True), SetVariable('vivian_ntr', False), SetVariable('vivian_revenge', False), SetVariable('vivian_sadist', False), Notify("Voyeur Path Active for Vivian")) hovered Notify("Voyeur - Vivian") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" xpos 735 ypos 475 action (SetVariable('vivian_voyeur', False), SetVariable('vivian_ntr', True), SetVariable('vivian_revenge', False), SetVariable('vivian_sadist', False), Notify("NTR Path Active for Vivian")) hovered Notify("NTR - Vivian") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" xpos 810 ypos 475 action (SetVariable('vivian_voyeur', False), SetVariable('vivian_ntr', False), SetVariable('vivian_revenge', True), SetVariable('vivian_sadist', False), Notify("Revenge Path Active for Vivian")) hovered Notify("Revenge - Vivian") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" xpos 885 ypos 475 action (SetVariable('vivian_voyeur', False), SetVariable('vivian_ntr', False), SetVariable('vivian_revenge', False), SetVariable('vivian_sadist', True), Notify("Sadist Path Active for Vivian")) hovered Notify("Sadist - Vivian") focus_mask True
        #imagebutton auto "gui/icons/icon_abort_%s.png" xpos 960 ypos 475 action (SetVariable('vivian_voyeur', False), SetVariable('vivian_ntr', False), SetVariable('vivian_revenge', False), SetVariable('vivian_sadist', False), Notify("All Dark Paths Off for Vivian")) hovered Notify("Turn Off Darker Paths - Vivian") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1035 ypos 475 action (SetVariable('vivianrelationship', 0), SetVariable('viviancorruption', 0), SetVariable('vivianlove', 0), Notify("[lv2], [cr2], [rp2] Points Cleared for Vivian")) hovered Notify("Clear Stats - Vivian") focus_mask True
        add "images/edited/icons/vivian_idle.png" xpos 1110 ypos 475

        #----- Kate -----
        imagebutton auto "gui/icons/icon_hug_%s.png" xpos 360 ypos 550 action (SetVariable('katerelationship', katerelationship+10), Notify("[rp1] Points now: [katerelationship]")) hovered Notify("+10 [rp1] Kate") focus_mask True
        imagebutton auto "gui/icons/icon_slap_%s.png" xpos 435 ypos 550 action (SetVariable('katerelationship', katerelationship-10), Notify("[rp1] Points now: [katerelationship]")) hovered Notify("-10 [rp1] Kate") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 510 ypos 550 action (SetVariable('katelove', katelove+10), Notify("[lv1] Points now: [katelove]")) hovered Notify("10 [lv1] Kate") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 585 ypos 550 action (SetVariable('katecorruption', katecorruption+10), Notify("[cr1] Points now: [katecorruption]")) hovered Notify("10 [cr1] Kate") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" xpos 660 ypos 550 action (SetVariable('kate_voyeur', True), SetVariable('kate_ntr', False), SetVariable('kate_revenge', False), SetVariable('kate_sadist', False), Notify("Voyeur Path Active for Kate")) hovered Notify("Voyeur - Kate") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" xpos 735 ypos 550 action (SetVariable('kate_voyeur', False), SetVariable('kate_ntr', True), SetVariable('kate_revenge', False), SetVariable('kate_sadist', False), Notify("NTR Path Active for Kate")) hovered Notify("NTR - Kate") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" xpos 810 ypos 550 action (SetVariable('kate_voyeur', False), SetVariable('kate_ntr', False), SetVariable('kate_revenge', True), SetVariable('kate_sadist', False), Notify("Revenge Path Active for Kate")) hovered Notify("Revenge - Kate") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" xpos 885 ypos 550 action (SetVariable('kate_voyeur', False), SetVariable('kate_ntr', False), SetVariable('kate_revenge', False), SetVariable('kate_sadist', True), Notify("Sadist Path Active for Kate")) hovered Notify("Sadist - Kate") focus_mask True
        #imagebutton auto "gui/icons/icon_abort_%s.png" xpos 960 ypos 550 action (SetVariable('kate_voyeur', False), SetVariable('kate_ntr', False), SetVariable('kate_revenge', False), SetVariable('kate_sadist', False), Notify("All Dark Paths Off for Kate")) hovered Notify("Turn Off Darker Paths - Kate") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1035 ypos 550 action (SetVariable('katerelationship', 0), SetVariable('katecorruption', 0), SetVariable('katelove', 0), Notify("[lv2], [cr2], [rp2] Points Cleared for Kate")) hovered Notify("Clear Stats - Kate") focus_mask True
        add "images/edited/icons/kate_idle.png" xpos 1110 ypos 550

        #----- Miranda -----
        imagebutton auto "gui/icons/icon_hug_%s.png" xpos 360 ypos 625 action (SetVariable('mirandarelationship', mirandarelationship+10), Notify("[rp1] Points now:  [mirandarelationship]")) hovered Notify("+10 [rp1] Miranda") focus_mask True
        imagebutton auto "gui/icons/icon_slap_%s.png" xpos 435 ypos 625 action (SetVariable('mirandarelationship', mirandarelationship-10), Notify("[rp1] Points now: [mirandarelationship]")) hovered Notify("-10 [rp1] Miranda") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 510 ypos 625 action (SetVariable('mirandalove', mirandalove+10), Notify("[lv1] Points now: [mirandalove]")) hovered Notify("10 [lv1] Miranda") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 585 ypos 625 action (SetVariable('mirandacorruption', mirandacorruption+10), Notify("[cr1] Points now: [mirandacorruption]")) hovered Notify("10 [cr1] Miranda") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_voyeur_%s.png" xpos 660 ypos 625 action (SetVariable('miranda_voyeur', True), SetVariable('miranda_ntr', False), SetVariable('miranda_revenge', False), SetVariable('miranda_sadist', False), Notify("Voyeur Path Active for Miranda")) hovered Notify("Voyeur - Miranda") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_ntr_%s.png" xpos 735 ypos 625 action (SetVariable('miranda_voyeur', False), SetVariable('miranda_ntr', True), SetVariable('miranda_revenge', False), SetVariable('miranda_sadist', False), Notify("NTR Path Active for Miranda")) hovered Notify("NTR - Miranda") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_revenge_%s.png" xpos 810 ypos 625 action (SetVariable('miranda_voyeur', False), SetVariable('miranda_ntr', False), SetVariable('miranda_revenge', True), SetVariable('miranda_sadist', False), Notify("Revenge Path Active for Miranda")) hovered Notify("Revenge - Miranda") focus_mask True
        #imagebutton auto "images/edited/gui/paths/icon_sadist_%s.png" xpos 885 ypos 625 action (SetVariable('miranda_voyeur', False), SetVariable('miranda_ntr', False), SetVariable('miranda_revenge', False), SetVariable('miranda_sadist', True), Notify("Sadist Path Active for Miranda")) hovered Notify("Sadist - Miranda") focus_mask True
        #imagebutton auto "gui/icons/icon_abort_%s.png" xpos 960 ypos 625 action (SetVariable('miranda_voyeur', False), SetVariable('miranda_ntr', False), SetVariable('miranda_revenge', False), SetVariable('miranda_sadist', False), Notify("All Dark Paths Off for Miranda")) hovered Notify("Turn Off Darker Paths - Miranda") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 1035 ypos 625 action (SetVariable('mirandarelationship', 0), SetVariable('mirandacorruption', 0), SetVariable('mirandalove', 0), Notify("[lv2], [cr2], [rp2] Points Cleared for Miranda")) hovered Notify("Clear Stats - Miranda") focus_mask True
        add "images/edited/icons/miranda_idle.png" xpos 1110 ypos 625

        #----- Davide -----
        if davidealexisfriends == False:
            imagebutton auto "images/edited/icons/davide_%s.png" xpos 1110 ypos 700 action (SetVariable('davidealexisfriends', True), Notify("Davide and Alexis are now friends.")) hovered Notify("Make Davide and Alexis Friends") focus_mask True
        else:
            imagebutton auto "images/edited/icons/davide_%s.png" xpos 1110 ypos 700 action (SetVariable('davidealexisfriends', False), Notify("Davide and Alexis are no longer friends.")) hovered Notify("Make Davide and Alexis NOT Friends") focus_mask True

        #----- Flowers -----
        imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 1260 ypos 175 action (SetVariable('giftflowers', giftflowers+1), Notify("Gift Flowers now: [giftflowers]")) hovered Notify("+1 Flowers") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 1360 ypos 175 action (SetVariable('giftflowers', giftflowers+5), Notify("Gift Flowers now: [giftflowers]")) hovered Notify("+5 Flowers") focus_mask True
        add "images/edited/gui/flowers_small.png" xpos 1460 ypos 175

        #----- Condoms -----
        imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 1260 ypos 250 action (SetVariable('giftcondoms', giftcondoms+1), Notify("Gift Condoms now: [giftcondoms]")) hovered Notify("+1 Condoms") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 1360 ypos 250 action (SetVariable('giftcondoms', giftcondoms+5), Notify("Gift Condoms now: [giftcondoms]")) hovered Notify("+5 Condoms") focus_mask True
        add "images/edited/gui/condoms_small.png" xpos 1460 ypos 250

        #----- Chocolates -----
        imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 1260 ypos 325 action (SetVariable('giftchocolate', giftchocolate+1), Notify("Gift Chocolates now: [giftchocolate]")) hovered Notify("+1 Chocolates") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" xpos 1360 ypos 325 action (SetVariable('giftchocolate', giftchocolate+5), Notify("Gift Chocolates now: [giftchocolate]")) hovered Notify("+5 Chocolates") focus_mask True
        add "images/edited/gui/chocolate_small.png" xpos 1460 ypos 325

        #----- Money -----
        imagebutton auto "gui/icons/icon_gift_%s.png" xpos 1360 ypos 425 action (SetVariable('money', money+500), Notify("Money now: [money]")) hovered Notify("Add $500 to Wallet") focus_mask True

        #----- Incest off/on -----
        if inc == False:
            imagebutton auto "gui/icons/icon_on_%s.png" xpos 1260 ypos 425 action (SetVariable('inc', True), Notify("Incest Enabled")) hovered Notify("Incest On") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_off_%s.png" xpos 1260 ypos 425 action (SetVariable('inc', False), Notify("Incest Disabled")) hovered Notify("Incest Off") focus_mask True

        #----- spot1000 Animations on/off -----
        vbox xpos 360 ypos 750:
            text "{color=ffffff}{u}Expansions:{/u}{/color}"
        if renpy.exists("images/edited/anim/spot1000/spot1000_key.rpy") == True:
            if spot1000anim == False:
                imagebutton auto "gui/icons/icon_on_%s.png" xpos 360 ypos 825 action (SetVariable('spot1000anim', True), Notify("spot1000 Animations Enabled")) hovered Notify("spot1000 Animations On") focus_mask True
            else:
                imagebutton auto "gui/icons/icon_off_%s.png" xpos 360 ypos 825 action (SetVariable('spot1000anim', False), Notify("spot1000 Animations Disabled")) hovered Notify("spot1000 Animations Off") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_abort_%s.png" xpos 360 ypos 825 action (SetVariable('spot1000anim', False), Notify("spot1000 Animations Disabled")) hovered Notify("Disable spot1000 Animations") focus_mask True

        #----- Enable All Dates -----
        imagebutton:
            auto "gui/icons/icon_wait_%s.png"
            xpos 1460
            ypos 425
            action [
            If(momlove<1, SetVariable('momlove', 100), SetVariable('momlove', momlove+100)),
            If(momcorruption<1, SetVariable('momcorruption', 100), SetVariable('momcorruption', momlove+100)),
            If(lilsislove<1, SetVariable('lilsislove', 50), SetVariable('lilsislove', lilsislove+50)),
            If(bigsislove<bigsiscorruption, (SetVariable('bigsislove', 125), SetVariable('bigsiscorruption', 100)), SetVariable('bigsislove', bigsislove+50)),
            SetVariable('money', money+500),
            SetVariable('gangmember', True),
            SetVariable('mombasementfirst', True),
            SetVariable('adate', True),
            SetVariable('ndate21', True),
            SetVariable('mombasementlovesecond', True),
            SetVariable('mombasementcorsecond', True),
            SetVariable('basecasfirst', True),
            Notify("All Dates Enabled")
            ]
            hovered Notify("Enable All Dates")
            focus_mask True

        #----- Close Button -----
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide('cheats'), Jump('phone1')) hovered Notify("Close") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Phone Options -----
label phoneoptions:
    call screen phonewallmenu

screen phonewallmenu():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        if phonebackindex == 1:
            add "images/edited/gui/phoneback/background01.png" xpos 714 ypos 44
        elif phonebackindex == 2:
            add "images/edited/gui/phoneback/background02.png" xpos 714 ypos 44
        elif phonebackindex == 3:
            add "images/edited/gui/phoneback/background03.png" xpos 714 ypos 44
        elif phonebackindex == 4:
            add "images/edited/gui/phoneback/background04.png" xpos 714 ypos 44
        elif phonebackindex == 5:
            add "images/edited/gui/phoneback/background05.png" xpos 714 ypos 44
        elif phonebackindex == 6:
            add "images/edited/gui/phoneback/background06.png" xpos 714 ypos 44
        elif phonebackindex == 7:
            add "images/edited/gui/phoneback/background07.png" xpos 714 ypos 44
        elif phonebackindex == 8:
            add "images/edited/gui/phoneback/background08.png" xpos 714 ypos 44
        elif phonebackindex == 9:
            add "images/edited/gui/phoneback/background09.png" xpos 714 ypos 44
        elif phonebackindex == 10:
            add "images/edited/gui/phoneback/background10.png" xpos 714 ypos 44
        elif phonebackindex == 11:
            add "images/edited/gui/phoneback/background11.png" xpos 714 ypos 44
        elif phonebackindex == 12:
            add "images/edited/gui/phoneback/background12.png" xpos 714 ypos 44
        elif phonebackindex == 13:
            add "images/edited/gui/phoneback/background13.png" xpos 714 ypos 44
        elif phonebackindex == 14:
            add "images/edited/gui/phoneback/background14.png" xpos 714 ypos 44
        elif phonebackindex == 15:
            add "images/edited/gui/phoneback/background15.png" xpos 714 ypos 44
        elif phonebackindex == 16:
            add "images/edited/gui/phoneback/background16.png" xpos 714 ypos 44
        elif phonebackindex == 17:
            add "images/edited/gui/phoneback/background17.png" xpos 714 ypos 44
        elif phonebackindex == 18:
            add "images/edited/gui/phoneback/background18.png" xpos 714 ypos 44
        elif phonebackindex == 19:
            add "images/edited/gui/phoneback/background19.png" xpos 714 ypos 44
        elif phonebackindex == 20:
            add "images/edited/gui/phoneback/background20.png" xpos 714 ypos 44
        else:
            add "gui/icons/phone.png" xpos 714 ypos 44

        imagebutton auto "gui/icons/icon_left_%s.png" xpos 768 ypos 189 action (Hide('phonewallmenu'), Jump('lastwallpaper')) hovered Notify("Last Wallpaper") focus_mask True
        imagebutton auto "gui/icons/icon_right_%s.png" xpos 892 ypos 189 action (Hide('phonewallmenu'), Jump('nextwallpaper')) hovered Notify("Next Wallpaper") focus_mask True
        if phoneiconpos == True:
            imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 768 ypos 313 action (Hide('phonewallmenu'), Jump('phoneiconlocation')) hovered Notify("Move Icon's to the Bottom") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_approve_%s.png" xpos 768 ypos 313 action (Hide('phonewallmenu'), Jump('phoneiconlocation')) hovered Notify("Move Icon's to the Top") focus_mask True
        imagebutton auto "gui/icons/close_%s.png" xpos 924 ypos 980 action (Hide('phonewallmenu'), Jump('phone1')) hovered Notify("Close") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nextwallpaper:
    if phonebackindex < 0:
        $ phonebackindex = 0
        $ renpy.notify("Disaplying the Default Background")
        jump phoneoptions
    elif phonebackindex == 20:
        $ phonebackindex = 0
        $ renpy.notify("Disaplying the Default Background")
        jump phoneoptions
    elif phonebackindex >= 0 and phonebackindex <= 19:
        $ phonebackindex += 1
        $ renpy.notify("Displaying Wallpaper [phonebackindex] of 20")
        jump phoneoptions
    else:
        $ phonebackindex = 0
        $ renpy.notify("Disaplying the Default Background")
        jump phoneoptions

label lastwallpaper:
    if phonebackindex < 0:
        $ phonebackindex = 0
        $ renpy.notify("Disaplying the Default Background")
        jump phoneoptions
    elif phonebackindex == 0:
        $ phonebackindex = 20
        $ renpy.notify("Displaying Wallpaper [phonebackindex] of 20")
        jump phoneoptions
    elif phonebackindex >= 1 and phonebackindex <= 20:
        $ phonebackindex -= 1
        if phonebackindex == 0:
            $ renpy.notify("Disaplying the Default Background")
        else:
            $ renpy.notify("Displaying Wallpaper [phonebackindex] of 20")
        jump phoneoptions
    else:
        $ phonebackindex = 0
        $ renpy.notify("Disaplying the Default Background")
        jump phoneoptions

label phoneiconlocation:
    if phoneiconpos == True:
        $ renpy.notify("Phone Icon's Moved to the Bottom")
        $ phoneiconpos = False
    else:
        $ renpy.notify("Phone Icon's Moved to the Top")
        $ phoneiconpos = True
    jump phoneoptions
