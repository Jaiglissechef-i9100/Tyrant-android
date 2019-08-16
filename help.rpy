#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

screen dlhs():
    zorder 100
    default tt = Tooltip ("")

    fixed:
        if frontdoorddfirst == False and gangmember == False and player_help_simple_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet Davide") focus_mask True
        if frontdoorddfirst == True and gangmember == False and jobgang == False and player_help_simple_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet Davide again") focus_mask True
        if frontdoorddfirst == True and gangmember == False and jobgang == True and jobdone < 2 and player_help_simple_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Deliver packages") focus_mask True
        if frontdoorddfirst == True and gangmember == False and jobgang == True and jobdone >= 2 and player_help_simple_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet Davide again") focus_mask True
        if gangmember == True and player_help_simple_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("You're a gangmember now") focus_mask True
        if frontdoorddfirst == False and gangmember == False and player_help_full_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet Davide at 8pm at the front door") focus_mask True
        if frontdoorddfirst == True and jobgang == False and gangmember == False and player_help_full_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet Davide at 9pm in the livingroom") focus_mask True
        if frontdoorddfirst == True and jobgang == True and jobdone < 2 and gangmember == False and player_help_full_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Deliver 2 packages") focus_mask True
        if frontdoorddfirst == True and jobgang == True and jobdone >= 2 and gangmember == False and player_help_full_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet Davide at 9pm in the livingroom") focus_mask True
        if gangmember == True and player_help_full_gang == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("You're a gangmember now") focus_mask True

        if ndate21 == False and nicole_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [mother] to her first date") focus_mask True
        if ndate21 == True and gangmember == False and momlove < 50 and nicole_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember and gain more love") focus_mask True
        if ndate21 == True and gangmember == True and momlove >= 50 and basenicfirst == False and nicole_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet [mother] in the livingroom") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == False and nicole_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [mother] to her second date") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == False and nicole_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with her in the basement") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True and proom19first == False and nicole_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered tt.Action ("Meet [mother] in the parentsroom") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True and proom19first == True and nicole_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True

        if ndate21 == False and nicole_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [mother] to her first date on the weekend") focus_mask True
        if ndate21 == True and gangmember == False and momlove < 50 and nicole_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember and gain 50 love") focus_mask True
        if ndate21 == True and gangmember == True and momlove >= 50 and basenicfirst == False and nicole_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet [mother] at 10pm in the livingroom") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == False and nicole_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [mother] to her second date on the weekend") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == False and nicole_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with her in the basement at 10pm") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True and proom19first == False and nicole_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered tt.Action ("Meet [mother] at 7pm in the parentsroom") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True and proom19first == True and nicole_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True


        if ndate21 == False and nicole_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [mother] to her first date") focus_mask True
        if ndate21 == True and gangmember == False and momcorruption < 30 and nicole_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember and gain more corruption") focus_mask True
        if ndate21 == True and gangmember == True and momcorruption >= 30 and basenicfirst == False and nicole_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet [mother] in the livingroom") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == False and nicole_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [mother] to her second date") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == False and nicole_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with her in the basement") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True and proom19first == False and nicole_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered tt.Action ("Meet [mother] in the parentsroom") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == True and proom19first == True and nicole_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True

        if ndate21 == False and nicole_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [mother] to her first date on the weekend") focus_mask True
        if ndate21 == True and gangmember == False and momcorruption < 30 and nicole_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember and gain 30 corruption") focus_mask True
        if ndate21 == True and gangmember == True and momcorruption >= 30 and basenicfirst == False and nicole_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet [mother] at 10pm in the livingroom") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == False and nicole_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [mother] to her second date on the weekend") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == False and nicole_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with her in the basement at 10pm") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementlovesecond == True and basement10pmnicoleouting == True and proom19first == False and nicole_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered tt.Action ("Meet [mother] at 7pm in the parentsroom") focus_mask True
        if ndate21 == True and basenicfirst == True and mombasementcorsecond == True and basement10pmnicoleouting == True and proom19first == True and nicole_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True

        if cdate5 == False and cassandra_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [bs] to her first date") focus_mask True
        if cdate5 == True and gangmember == False and cassandra_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == False and cassandra_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet her in the kitchen") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsislove < 50 and cassandra_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Gain more love") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsislove >= 50 and weekendcasfirst == False and cassandra_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet with [bs] for your second date") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and weekendcasfirst == True and cassandra_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True

        if cdate5 == False and cassandra_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [bs] to her first date on the weekend") focus_mask True
        if cdate5 == False and gangmember == False  and cassandra_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == False and cassandra_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet her in the kitchen at 9am") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsislove < 50 and cassandra_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Gain 50 love") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and weekendcasfirst == False and bigsislove >= 50 and cassandra_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet with [bs] for your second date on the weekend") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and weekendcasfirst == True and cassandra_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True

        if cdate5 == False and cassandra_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [bs] to her first date") focus_mask True
        if cdate5 == True and gangmember == False and cassandra_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == False and cassandra_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet her in the kitchen") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsiscorruption < 50 and cassandra_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Gain more corruption") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsiscorruption >= 50 and basecassecond == False and cassandra_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet her in the kitchen again") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and basecassecond == True and basement10cassandraouting == False and cassandra_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with her in the basement") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and basecassecond == True and basement10cassandraouting == True and cassandra_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True


        if cdate5 == False and cassandra_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [bs] to her first date on the weekend") focus_mask True
        if cdate5 == False and gangmember == False  and cassandra_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == False and cassandra_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet her in the kitchen at 9am") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and bigsiscorruption < 50 and cassandra_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Gain 50 corruption") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and basecassecond == False and bigsiscorruption >= 50 and cassandra_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet her in the kitchen again at 9am") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and basecassecond == True and basement10cassandraouting == False and cassandra_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with her in the basement at 10pm") focus_mask True
        if cdate5 == True and gangmember == True and basecasfirst == True and basecassecond == True and basement10cassandraouting == True and cassandra_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True


        if adate == False and alexis_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [ls] to her first date") focus_mask True
        if adate == True and lilsislove < 50 and alexis_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Gain more love") focus_mask True
        if adate == True and alexisweekendsecond == False and lilsislove >= 50 and alexis_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [ls] to her second date") focus_mask True
        if adate == True and alexisweekendsecond == True and alexis_help_simple_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True

        if adate == False and alexis_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [ls] to her first date on the weekend") focus_mask True
        if adate == True and lilsislove < 50 and alexis_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Gain 50 love") focus_mask True
        if adate == True and alexisweekendsecond == False and lilsislove >= 50 and alexis_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [ls] to her second date") focus_mask True
        if adate == True and alexisweekendsecond == True and alexis_help_full_love == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True


        if adate == False and alexis_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [ls] to her first date") focus_mask True
        if adate == True and gangmember == False and alexis_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember") focus_mask True
        if adate == True and gangmember == True and lilsiscorruption < 30 and alexis_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Gain more corruption") focus_mask True
        if adate == True and showbasealfirst == False and lilsiscorruption >= 30 and gangmember == True and alexis_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet [ls] in the kitchen") focus_mask True
        if adate == True and showbasealfirst == True and alexis_help_simple_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True

        if adate == False and alexis_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [ls] to her first date on the weekend") focus_mask True
        if adate == True and gangmember == False and alexis_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Become a gangmember") focus_mask True
        if adate == True and gangmember == True and lilsiscorruption < 30 and alexis_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Gain 30 corruption") focus_mask True
        if adate == True and showbasealfirst == False and lilsiscorruption >= 30 and gangmember == True and alexis_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Meet [ls] int he kitchen at 8am") focus_mask True
        if adate == True and showbasealfirst == True and alexis_help_full_corruption == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True

        if NTR == True and adate == False and alexis_help_simple_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [ls] to her first date") focus_mask True
        if NTR == True and adate == True and basealefirst == False and alexis_help_simple_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Sneak with her in the basement") focus_mask True
        if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == False and alexis_help_simple_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go to the secret place") focus_mask True
        if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == True and base2amalexisntrfirst == False and alexis_help_simple_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Wait until the basement event at night happened") focus_mask True
        if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == True and base2amalexisntrfirst == True and secretplace4pmntrfirst == False and alexis_help_simple_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Stay the next weekend alone") focus_mask True
        if NTR == True and secretplace4pmntrfirst == True and alexis_help_simple_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True


        if NTR == True and adate == False and alexis_help_full_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go with [ls] to her first date and let her meet Davide") focus_mask True
        if NTR == True and adate == True and basealefirst == False and alexis_help_full_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Sneak with her in the basement, start it in your room") focus_mask True
        if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == False and alexis_help_full_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Go to the secret place at 2pm") focus_mask True
        if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == True and base2amalexisntrfirst == False and alexis_help_full_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Wait until the basement event at night happened at 2am") focus_mask True
        if NTR == True and adate == True and basealefirst == True and secretplace2pmntrfirst == True and base2amalexisntrfirst == True and secretplace4pmntrfirst == False and alexis_help_full_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("Stay the next weekend alone or skip at least one activity") focus_mask True
        if NTR == True and secretplace4pmntrfirst == True and alexis_help_full_NTR == True:
            imagebutton auto "gui/icons/dlh_green_%s.png" xpos 1830 ypos 200 action NullAction() hovered Notify("End of this path for now") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label dlh:
    hide screen phone
    hide screen hud
    hide screen messenger1
    call screen dlhmenu

screen dlhmenu():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/dlh_background.png" xpos 152 ypos 106
        text "I need help with:" xpos 786 ypos 146
        imagebutton auto "gui/icons/dlh_nicole_small_%s.png" xpos 211 ypos 253 action (Hide('dlhmenu'), Jump('dlh_nicole')) hovered Notify("I need more help with [mother]") focus_mask True
        imagebutton auto "gui/icons/dlh_alexis_small_%s.png" xpos 398 ypos 253 action (Hide('dlhmenu'), Jump('dlh_alexis')) hovered Notify("I need more help with [ls]") focus_mask True
        imagebutton auto "gui/icons/dlh_cassandra_small_%s.png" xpos 584 ypos 253 action (Hide('dlhmenu'), Jump('dlh_cassandra')) hovered Notify("I need more help with [bs]") focus_mask True
        imagebutton auto "gui/icons/dlh_player_small_%s.png" xpos 780 ypos 253 action (Hide('dlhmenu'), Jump('dlh_player')) hovered Notify("I need more help for myself") focus_mask True
        imagebutton auto "gui/icons/dlh_close_%s.png" xpos 1604 ypos 122 action (Hide('dlhmenu'), Jump('phone1')) hovered Notify("Close") focus_mask True
        #----- Custom -----
        imagebutton auto "gui/icons/package_%s.png" xpos 1500 ypos 800 action (Hide('dlhmenu'), Jump('dlh_modwalkthrough')) hovered Notify("What's in the box?!?") focus_mask True

    vbox:
        xpos 203 ypos 730
        text "Here you can find hints for the paths or events which need a"
        text "setup before. You can read the walkthrough for the girls."
        text "And set up the helper to guide you ingame"
        text "with simple or full help."

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label dlh_player:
    call screen dlh_player1

screen dlh_player1():
    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/dlh_background.png" xpos 152 ypos 106
        text "Activate helper" xpos 786 ypos 122
        if player_help_simple_gang == True:
            add "gui/icons/dlh_simple_green_idle.png" xpos 183 ypos 198
        if player_help_full_gang == True:
            add "gui/icons/dlh_full_green_idle.png" xpos 356 ypos 198
        imagebutton auto "gui/icons/dlh_deactivate_%s.png" xpos 1175 ypos 122 action (Hide('dlh_player1'), Jump('dlh_deactivate')) hovered Notify("Deactivate the helper") focus_mask True

        text "How to become a gangmember" xpos 228 ypos 257
        text "Activate helper" xpos 786 ypos 122

        if player_help_simple_gang == False:
            imagebutton auto "gui/icons/dlh_simple_%s.png" xpos 183 ypos 198 action (Hide('dlh_player1'), Jump('dlh_simple_gang_mc')) hovered Notify("Activate the simple helper") focus_mask True
        if player_help_full_gang == False:
            imagebutton auto "gui/icons/dlh_full_%s.png" xpos 356 ypos 198 action (Hide('dlh_player1'), Jump('dlh_full_gang_mc')) hovered Notify("Activate the full helper") focus_mask True
        if player_help_more_gang == False:
            imagebutton auto "gui/icons/dlh_show_%s.png" xpos 224 ypos 410 action (Hide('dlh_player1'), Jump('dlh_more_gang_mc')) hovered Notify("Show more info") focus_mask True
        if player_help_more_gang == True:
            imagebutton auto "gui/icons/dlh_hide_%s.png" xpos 224 ypos 410 action (Hide('dlh_player1'), Jump('dlh_hide_gang_mc')) hovered Notify("Hide") focus_mask True
        imagebutton auto "gui/icons/dlh_close_%s.png" xpos 1604 ypos 122 action (Hide('dlh_player1'), Jump('dlh')) focus_mask True

    vbox:
        xpos 1000 ypos 337 xmaximum 750
        text "{b}General hints{/b}"
        text "{size=-10}- You can find work at the tanning salon.{/size}"
        text "{size=-10}- Also you can sell drugs in the basment when you're a gangmember.{/size}"
        text "{size=-10}- You'll find the shop in your phone.{/size}"
        text "{size=-10}- Some events are placed in your room.{/size}"

    fixed pos (174,330) xysize (750,65):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                #xpos 174 ypos 337
                if frontdoorddfirst == False and gangmember == False:
                    text "- Meet Davide"
                if frontdoorddfirst == True and jobgang == False and gangmember == False:
                    text "- Meet Davide again"
                if frontdoorddfirst == True and jobgang == True and jobdone < 2 and gangmember == False:
                    text "- Deliver packages"
                if frontdoorddfirst == True and jobgang == True and jobdone >= 2 and gangmember == False:
                    text "- Meet Davide again"
                if gangmember == True:
                    text "- You're a gangmember now"

    if player_help_more_gang == True:
        fixed pos (174,500) xysize (750,450):
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    #xpos 174 ypos 500
                    text "{size=-10}- Meet Davide at 8pm at the front door.{/size}"
                    text "{size=-10}- Meet Davide at 9pm in the livingroom to pick up drug packages.{/size}"
                    text "{size=-10}- Deliver 2 packages to the Subway at 7am or 8am on Tuesday or Thursday.{/size}"
                    text "{size=-10}- Meet Davide again at 9pm in the livingroom.{/size}"

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label dlh_deactivate:
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = False
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    $ player_help_full_gang = False
    "The helper is now deactivated."
    jump dlh

label dlh_simple_gang_mc:
    $ player_help_simple_gang = True
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = False
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_full_gang = False
    "The simple helper is now activated."
    jump dlh_player

label dlh_full_gang_mc:
    $ player_help_full_gang = True
    $ nicole_help_simple_love = False
    $ nicole_help_full_love = False
    $ nicole_help_simple_corruption = False
    $ nicole_help_full_corruption = False
    $ nicole_help_simple_NTR = False
    $ nicole_help_full_NTR = False
    $ alexis_help_simple_love = False
    $ alexis_help_full_love = False
    $ alexis_help_simple_corruption = False
    $ alexis_help_full_corruption = False
    $ alexis_help_simple_NTR = False
    $ alexis_help_full_NTR = False
    $ cassandra_help_simple_love = False
    $ cassandra_help_full_love = False
    $ cassandra_help_simple_corruption = False
    $ cassandra_help_full_corruption = False
    $ cassandra_help_simple_NTR = False
    $ cassandra_help_full_NTR = False
    $ player_help_simple_gang = False
    "The full helper is now activated."
    jump dlh_player

label dlh_more_gang_mc:
    $ player_help_more_gang = True
    jump dlh_player

label dlh_hide_gang_mc:
    $ player_help_more_gang = False
    jump dlh_player

#----- Custom -----
label dlh_modwalkthrough:
    call screen dlh_modwalkthrough1

screen dlh_modwalkthrough1():

    $ corruption = "{color=#ff0000}Corruption{/color}"
    $ love = "{color=#3cff00}Love{/color}"
    $ darkerpaths = "{color=#0000ff}Darker Paths{/color}"
    $ good = "{color=#3cff00}Good{/color}"
    $ bad = "{color=#ff0000}Bad{/color}"
    $ twisted = "{color=#3cff00}T{/color}{color=#ff0000}w{/color}{color=#3cff00}i{/color}{color=#ff0000}s{/color}{color=#3cff00}t{/color}{color=#ff0000}e{/color}{color=#3cff00}d{/color} and/or {color=#3cff00}E{/color}{color=#ff0000}x{/color}{color=#3cff00}t{/color}{color=#ff0000}e{/color}{color=#3cff00}n{/color}{color=#ff0000}d{/color}{color=#3cff00}e{/color}{color=#ff0000}d{/color}"
    $ fanart = "{color=#ffa500}Fan Art{/color}"
    $ custom = "{color=#ffa500}Custom{/color}"
    $ activated = "{color=#ffa500}Activated{/color}"
    $ repeatable = "{color=#ffa500}Repeatable{/color}"
    $ triggered = "{color=#ffa500}Triggered{/color}"
    $ limited = "{color=#ffa500}Limited{/color}"
    $ fetish = "{color=#ffa500}Fetish{/color}"

    zorder 100
    modal True
    default tt = Tooltip ("")

    fixed:
        add "gui/icons/dlh_background.png" xpos 152 ypos 106
        imagebutton auto "gui/icons/dlh_close_%s.png" xpos 1604 ypos 122 action (Hide('dlh_modwalkthrough1'), Jump('dlh')) focus_mask True

    vbox xpos 174 ypos 122:
        text "The Tyrant 0.7.5 Part 1 and 2 Mod Guide: {size=-10}By S A Z{/size}"

    fixed xalign .5 ypos 200 xysize (1550,760):
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                add "images/edited/walkthrough.png" maxsize None
    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value
