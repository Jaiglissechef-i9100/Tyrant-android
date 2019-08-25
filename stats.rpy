
label stats:
    hide screen locations
    hide screen townl
    scene black
    if momrelationship >= 40:
        $ momntr = True
    if bigsisrelationship >= 20:
        $ bigsisntr = True
    if lilsisrelationship >= 70:
        $ lilsisntr = True
    if irinarelationship >= 20:
        $ irinantr = True
    if susanrelationship >= 20:
        $ susanntr = True
    if vivianrelationship >= 20:
        $ vivianntr = True
    if katerelationship >= 20:
        $ katentr = True
    call screen stats1

screen stats1():
    text "Stats changing:" xpos 805 ypos 66
    vbox:
        xpos 474 ypos 199
        if inc == True:
            text "Mom:"
        else:
            text "[mother]:"
        text "[bs]:"
        text "[ls]:"
        if irinafirstmeet == True:
            text "[irina]:"
        if susanfirstmeet == True:
            text "[susan]:"
        if katefirstmeet == True:
            text "[kate]:"
        if vivianfirstmeet == True:
            text "[vivian]:"
    vbox:
        xpos 1111 ypos 199
        if momntr == True:
            text "{color=ff0000}-10 Relationship{/color}"
        else:
            text "{color=3cff00}No changes{/color}"
        if bigsisntr == True:
            text "{color=ff0000}-5 Relationship{/color}"
        else:
            text "{color=3cff00}No changes{/color}"
        if lilsisntr == True:
            text "{color=ff0000}-5 Relationship{/color}"
        else:
            text "{color=3cff00}No changes{/color}"
        if irinafirstmeet == True:
            if irinantr == True:
                text "{color=ff0000}-3 Relationship{/color}"
            else:
                text "{color=3cff00}No changes{/color}"
        if susanfirstmeet == True:
            if susanntr == True:
                text "{color=ff0000}-3 Relationship{/color}"
            else:
                text "{color=3cff00}No changes{/color}"
        if katefirstmeet == True:
            if katentr == True:
                text "{color=ff0000}-3 Relationship{/color}"
            else:
                text "{color=3cff00}No changes{/color}"
        if vivianfirstmeet == True:
            if vivianntr == True:
                text "{color=ff0000}-3 Relationship{/color}"
            else:
                text "{color=3cff00}No changes{/color}"
    textbutton _("close") xpos 885 ypos 906 action Jump("night")


label statshard:
    hide screen locations
    hide screen townl
    scene black
    call screen stats7

screen stats7():
    text "Stats changing:" xpos 805 ypos 66
    vbox:
        xpos 474 ypos 199
        if inc == True:
            text "Mom:"
        else:
            text "[mother]:"
        text "[bs]:"
        text "[ls]:"
        if irinafirstmeet == True:
            text "[irina]:"
        if susanfirstmeet == True:
            text "[susan]:"
        if katefirstmeet == True:
            text "[kate]:"
        if vivianfirstmeet == True:
            text "[vivian]:"
    vbox:
        xpos 1111 ypos 199
        text "{color=ff0000}-20 Relationship{/color}"
        text "{color=ff0000}-20 Relationship{/color}"
        text "{color=ff0000}-20 Relationship{/color}"
        if irinafirstmeet == True:
            text "{color=ff0000}-20 Relationship{/color}"
        if susanfirstmeet == True:
            text "{color=ff0000}-20 Relationship{/color}"
        if katefirstmeet == True:
            text "{color=ff0000}-20 Relationship{/color}"
        if vivianfirstmeet == True:
            text "{color=ff0000}-20 Relationship{/color}"
    textbutton _("close") xpos 885 ypos 906 action Jump("nighthard")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
