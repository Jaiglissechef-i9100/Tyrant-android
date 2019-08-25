

screen contacts():

    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phoneside.png" xpos 142 ypos 114
        add "gui/icons/nicole.png" xpos 375 ypos 153
        add "gui/icons/alexis.png" xpos 812 ypos 153
        add "gui/icons/cassandra.png" xpos 1246 ypos 153
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('contacts'), Jump('phone1')) hovered tt.Action ("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide ('contacts'), Show('contacts4', transition=None)) hovered tt.Action ("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide ('contacts'), Show('contacts1', transition=None)) hovered tt.Action ("Next") focus_mask True
    vbox:
        xpos 335 ypos 506
        if inc == True:
            text "Mom"
        else:
            text "[mother]"
        if momrelationship >= 30:
            text "{size=-10}Relationship: {color=3cff00}[momrelationship]{/color}"
        elif momrelationship < 30 and momrelationship >= 6:
            text "{size=-10}Relationship: {color=ffd200}[momrelationship]{/color}"
        elif momrelationship < 6:
            text "{size=-10}Relationship: {color=ff0000}[momrelationship]{/color}"
        text "{size=-10}[lv1]: [momlove]"
        text "{size=-10}[cr1]: [momcorruption]"
        if NTR == True:
            if ntrhatenic == False and ntrlovenic == False:
                text "{size=-10}NTR: undecided"
            elif ntrhatenic == True:
                text "{size=-10}NTR: {color=ff0000}dislike{/color}"
            elif ntrlovenic == True:
                text "{size=-10}NTR: {color=3cff00}like{/color}"
    vbox:
        xpos 772 ypos 506
        text "[ls]"
        if lilsisrelationship >= 40:
            text "{size=-10}Relationship: {color=3cff00}[lilsisrelationship]{/color}"
        elif lilsisrelationship < 40 and lilsisrelationship >= 6:
            text "{size=-10}Relationship: {color=ffd200}[lilsisrelationship]{/color}"
        elif lilsisrelationship < 6:
            text "{size=-10}Relationship: {color=ff0000}[lilsisrelationship]{/color}"
        text "{size=-10}[lv1]: [lilsislove]"
        text "{size=-10}[cr1]: [lilsiscorruption]"
        if NTR == True:
            if ntrhateale == False and ntrloveale == False:
                text "{size=-10}NTR: undecided"
            elif ntrhateale == True:
                text "{size=-10}NTR: {color=ff0000}dislike{/color}"
            elif ntrloveale == True:
                text "{size=-10}NTR: {color=3cff00}like{/color}"
    vbox:
        xpos 1209 ypos 506
        text "[bs]"
        if bigsisrelationship >= 30:
            text "{size=-10}Relationship: {color=3cff00}[bigsisrelationship]{/color}"
        elif bigsisrelationship < 30 and bigsisrelationship >= 6:
            text "{size=-10}Relationship: {color=ffd200}[bigsisrelationship]{/color}"
        elif bigsisrelationship < 6:
            text "{size=-10}Relationship: {color=ff0000}[bigsisrelationship]{/color}"
        text "{size=-10}[lv1]: [bigsislove]"
        text "{size=-10}[cr1]: [bigsiscorruption]"
        if NTR == True:
            if ntrhatecas == False and ntrlovecas == False:
                text "{size=-10}NTR: undecided"
            elif ntrhatecas == True:
                text "{size=-10}NTR: {color=ff0000}dislike{/color}"
            elif ntrlovecas == True:
                text "{size=-10}NTR: {color=3cff00}like{/color}"

    frame:
        xalign .5
        text tt.value


screen contacts1():

    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phoneside.png" xpos 142 ypos 114
        add "gui/icons/bruce.png" xpos 375 ypos 153
        add "gui/icons/davide.png" xpos 812 ypos 153
        add "gui/icons/steve.png" xpos 1246 ypos 153
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('contacts1'), Jump('phone1')) hovered tt.Action ("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide ('contacts1'), Show('contacts', transition=None)) hovered tt.Action ("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide ('contacts1'), Show('contacts2', transition=None)) hovered tt.Action ("Next") focus_mask True
    vbox:
        xpos 335 ypos 506
        if inc == True:
            text "Dad"
        else:
            text "Bruce"
        text "{size=-10}[gd1]: [dadgood]"
        text "{size=-10}[bd1]: [dadbad]"
    vbox:
        xpos 772 ypos 506
        text "Davide"
        text "{size=-10}[gd1]: [davidegood]"
        text "{size=-10}[bd1]: [davidebad]"
    vbox:
        xpos 1209 ypos 506
        text "Steve"
        text "{size=-10}[gd1]: [stevegood]"
        text "{size=-10}[bd1]: [stevebad]"

    frame:
        xalign .5
        text tt.value

screen contacts2():

    default tt = Tooltip (" ")

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
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('contacts2'), Jump('phone1')) hovered tt.Action ("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide ('contacts2'), Show('contacts1', transition=None)) hovered tt.Action ("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide ('contacts2'), Show('contacts3', transition=None)) hovered tt.Action ("Next") focus_mask True
    vbox:
        xpos 335 ypos 506
        if irinafirstmeet == True:
            text "[irina]"
        else:
            text "Unknown"
        if irinarelationship >= 20:
            text "{size=-10}Relationship: {color=3cff00}[irinarelationship]{/color}"
        elif irinarelationship < 20 and irinarelationship >= 6:
            text "{size=-10}Relationship: {color=ffd200}[irinarelationship]{/color}"
        elif irinarelationship < 6:
            text "{size=-10}Relationship: {color=ff0000}[irinarelationship]{/color}"
        text "{size=-10}[lv1]: [irinalove]"
        text "{size=-10}[cr1]: [irinacorruption]"
        if NTR == True:
            if ntrhateiri == False and ntrloveiri == False:
                text "{size=-10}NTR: undecided"
            elif ntrhateiri == True:
                text "{size=-10}NTR: {color=ff0000}dislike{/color}"
            elif ntrloveiri == True:
                text "{size=-10}NTR: {color=3cff00}like{/color}"
    vbox:
        xpos 772 ypos 506
        if martinfirstmeet == True:
            text "Martin"
        else:
            text "Unknown"
        text "{size=-10}[gd1]: [martingood]"
        text "{size=-10}[bd1]: [martinbad]"
    vbox:
        xpos 1209 ypos 506
        if susanfirstmeet == True:
            text "[susan]"
        else:
            text "Unknown"
        if susanrelationship >= 20:
            text "{size=-10}Relationship: {color=3cff00}[susanrelationship]{/color}"
        elif susanrelationship < 20 and susanrelationship >= 6:
            text "{size=-10}Relationship: {color=ffd200}[susanrelationship]{/color}"
        elif susanrelationship < 6:
            text "{size=-10}Relationship: {color=ff0000}[susanrelationship]{/color}"
        text "{size=-10}[lv1]: [susanlove]"
        text "{size=-10}[cr1]: [susancorruption]"

    frame:
        xalign .5
        text tt.value

screen contacts3():

    default tt = Tooltip (" ")

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
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('contacts3'), Jump('phone1')) hovered tt.Action ("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide ('contacts3'), Show('contacts2', transition=None)) hovered tt.Action ("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide ('contacts3'), Show('contacts', transition=None)) hovered tt.Action ("Next") focus_mask True
    vbox:
        xpos 335 ypos 506
        if vivianfirstmeet == True:
            text "[vivian]"
        else:
            text "Unknown"
        if vivianrelationship >= 30:
            text "{size=-10}Relationship: {color=3cff00}[vivianrelationship]{/color}"
        elif vivianrelationship < 30 and vivianrelationship >= 6:
            text "{size=-10}Relationship: {color=ffd200}[vivianrelationship]{/color}"
        elif vivianrelationship < 6:
            text "{size=-10}Relationship: {color=ff0000}[vivianrelationship]{/color}"
        text "{size=-10}[lv1]: [vivianlove]"
        text "{size=-10}[cr1]: [viviancorruption]"
    vbox:
        xpos 772 ypos 506
        if katefirstmeet == True:
            text "[kate]"
        else:
            text "Unknown"
        if katerelationship >= 40:
            text "{size=-10}Relationship: {color=3cff00}[katerelationship]{/color}"
        elif katerelationship < 40 and katerelationship >= 6:
            text "{size=-10}Relationship: {color=ffd200}[katerelationship]{/color}"
        elif katerelationship < 6:
            text "{size=-10}Relationship: {color=ff0000}[katerelationship]{/color}"
        text "{size=-10}[lv1]: [katelove]"
        text "{size=-10}[cr1]: [katecorruption]"
    vbox:
        xpos 1209 ypos 506
        if frankfirstmeet == True:
            text "Frank"
        else:
            text "Unknown"
        text "{size=-10}[gd1]: [frankgood]"
        text "{size=-10}[bd1]: [frankbad]"

    frame:
        xalign .5
        text tt.value

screen contacts4():
    default tt = Tooltip (" ")

    fixed:
        add "gui/icons/phoneside.png" xpos 142 ypos 114
        if mirandafirstmeet == True:
            add "gui/icons/miranda.png" xpos 375 ypos 153
        else:
            add "gui/icons/unknown.png" xpos 375 ypos 153
        imagebutton auto "gui/icons/close_%s.png" xpos 947 ypos 851 action (Hide ('contacts4'), Jump('phone1')) hovered tt.Action ("Close") focus_mask True
        imagebutton auto "gui/icons/back_%s.png" xpos 852 ypos 834 action (Hide ('contacts4'), Show('contacts3', transition=None)) hovered tt.Action ("Back") focus_mask True
        imagebutton auto "gui/icons/forward_%s.png" xpos 1057 ypos 834 action (Hide ('contacts4'), Show('contacts', transition=None)) hovered tt.Action ("Next") focus_mask True
    vbox:
        xpos 335 ypos 506
        if vivianfirstmeet == True:
            text "[miranda]"
        else:
            text "Unknown"
        if vivianrelationship >= 30:
            text "{size=-10}Relationship: {color=3cff00}[mirandarelationship]{/color}"
        elif vivianrelationship < 30 and vivianrelationship >= 6:
            text "{size=-10}Relationship: {color=ffd200}[mirandarelationship]{/color}"
        elif vivianrelationship < 6:
            text "{size=-10}Relationship: {color=ff0000}[mirandarelationship]{/color}"
        text "{size=-10}[lv1]: [mirandalove]"
        text "{size=-10}[cr1]: [mirandacorruption]"

    frame:
        xalign .5
        text tt.value