#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

screen locations():
    default tt = Tooltip ("")

    fixed:
        imagebutton auto "gui/icons/icon_living_room_%s.png" xpos 50 ypos 938 action (Hide('locations'), Jump('lroom')) hovered tt.Action ("Living room") focus_mask True
        imagebutton auto "gui/icons/icon_dining_room_%s.png" xpos 162 ypos 938 action (Hide('locations'), Jump('droom')) hovered tt.Action ("Dining room") focus_mask True
        imagebutton auto "gui/icons/icon_kitchen_%s.png" xpos 281 ypos 938 action (Hide('locations'), Jump('kitchen')) hovered tt.Action ("Kitchen") focus_mask True
        imagebutton auto "gui/icons/icon_mc_room_%s.png" xpos 50 ypos 828 action (Hide('locations'), Jump('mcroom')) hovered tt.Action ("Your room") focus_mask True
        imagebutton auto "gui/icons/icon_lil_sis_room_%s.png" xpos 162 ypos 828 action (Hide('locations'), Jump('lsisroom')) hovered tt.Action ("[ls]' room") focus_mask True
        imagebutton auto "gui/icons/icon_big_sis_room_%s.png" xpos 281 ypos 828 action (Hide('locations'), Jump('bsisroom')) hovered tt.Action ("[bs]'s room") focus_mask True
        imagebutton auto "gui/icons/icon_front_door_%s.png" xpos 522 ypos 938 action (Hide('locations'), Jump('frontdoor')) hovered tt.Action ("Front door") focus_mask True
        imagebutton auto "gui/icons/icon_shower_upstairs_%s.png" xpos 401 ypos 828 action (Hide('locations'), Jump('showerup')) hovered tt.Action ("Shower upstairs") focus_mask True
        imagebutton auto "gui/icons/icon_shower_downstairs_%s.png" xpos 401 ypos 938 action (Hide('locations'), Jump('showerdown')) hovered tt.Action ("Shower downstairs") focus_mask True
        imagebutton auto "gui/icons/icon_parents_room_%s.png" xpos 522 ypos 828 action (Hide('locations'), Jump('parentsroom')) hovered tt.Action ("Parents room") focus_mask True
        imagebutton auto "gui/icons/icon_basement_%s.png" xpos 642 ypos 938 action (Hide('locations'), Jump('basement')) hovered tt.Action ("Basement") focus_mask True
        imagebutton auto "gui/icons/icon_town_%s.png" xpos 1739 ypos 896 action (Hide('locations'), Jump('town')) hovered tt.Action ("Town") focus_mask True
        imagebutton auto "gui/icons/icon_skip_%s.png" xpos 641 ypos 828 action (Hide('locations'), Jump('skip1')) hovered tt.Action ("Skip 1 hour") focus_mask True

        if dtime == 7 and momdrugfirst == False:
            add "gui/icons/nicole_small.png" xpos 216 ypos 984
        if dtime == 7 and momdrugfirst == True and momsecret == False:
            add "gui/icons/nicole_small.png" xpos 454 ypos 984
        if dtime == 7:
            add "gui/icons/alexis_small.png" xpos 454 ypos 874
        if dtime == 8:
            add "gui/icons/nicole_small.png" xpos 104 ypos 984
            add "gui/icons/alexis_small.png" xpos 334 ypos 984
        if dtime == 9:
            add "gui/icons/cassandra_small.png" xpos 334 ypos 984
        if dtime == 9 and momlove >= 20 and fitnessmember == True or dtime == 9 and fitnessmember == True and momcorruption >= 20:
            add "gui/icons/nicole_small.png" xpos 1742 ypos 940
        if dtime == 10:
            if kitchen9mix == False:
                add "gui/icons/cassandra_small.png" xpos 104 ypos 984
            elif kitchen9mix == True:
                add "gui/icons/cassandra_small.png" xpos 454 ypos 984
            add "gui/icons/nicole_small.png" xpos 1792 ypos 940
            #----- edited -----
            if momrelationship < 6 and NTR == True and frankfirstmeet == True or hardntr == True and frankfirstmeet == True:
                add "gui/icons/frank_small.png" xpos 1767 ypos 940
        if dtime == 11:
            add "gui/icons/nicole_small.png" xpos 334 ypos 984
        if dtime == 12:
            add "gui/icons/cassandra_small.png" xpos 168 ypos 984
            add "gui/icons/nicole_small.png" xpos 192 ypos 984
            add "gui/icons/alexis_small.png" xpos 216 ypos 984
        if dtime == 13:
            add "gui/icons/nicole_small.png" xpos 192 ypos 984
            add "gui/icons/alexis_small.png" xpos 216 ypos 984
            if dtime == 13 and d5rccorfuck == False and d5rcbjsw == False and d5rcbjout == False and d5rcbjdt == False and d5rclovef == False and d5rcntr == False:
                add "gui/icons/cassandra_small.png" xpos 575 ypos 984
                if martinfirstmeet == True:
                    add "gui/icons/martin_small.png" xpos 551 ypos 984
        if dtime == 14:
            add "gui/icons/nicole_small.png" xpos 104 ypos 984
            if lilsisrelationship >= 6:
                add "gui/icons/alexis_small.png" xpos 216 ypos 874
            add "gui/icons/cassandra_small.png" xpos 334 ypos 874
            if martinfirstmeet == True:
                add "gui/icons/martin_small.png" xpos 310 ypos 874
            #----- edited -----
            if lilsisrelationship < 6 and NTR == True and davidealexisfriends == True or hardntr == True and davidealexisfriends == True:
                add "gui/icons/davide_small.png" xpos 1792 ypos 940
                add "gui/icons/alexis_small.png" xpos 1767 ypos 940
        if dtime == 15:
            #----- edited -----
            if momrelationship <= 5 and NTR == True or hardntr == True:
                add "gui/icons/davide_small.png" xpos 429 ypos 984
            add "gui/icons/nicole_small.png" xpos 454 ypos 984
            if sp2pmextend == True:
                add "gui/icons/alexis_small.png" xpos 454 ypos 874
            if irinafirstmeet == True:
                add "gui/icons/irina_small.png" xpos 80 ypos 984
            add "gui/icons/cassandra_small.png" xpos 104 ypos 984
        if dtime == 16:
            if irinafirstmeet == True:
                add "gui/icons/irina_small.png" xpos 1792 ypos 940
            #----- edited -----
            if irinarelationship < 6 and NTR == True and frankfirstmeet == True or hardntr == True and frankfirstmeet == True:
                add "gui/icons/frank_small.png" xpos 1767 ypos 940
        if dtime == 16 and gangmember == True and selldrugs == False:
            add "gui/icons/bruce_small.png" xpos 695 ypos 984
        if dtime == 17:
            if vdroom13lilsisbetlost == True:
                add "gui/icons/alexis_small.png" xpos 104 ypos 874
            add "gui/icons/nicole_small.png" xpos 1792 ypos 940
            if susanfirstmeet == True:
                add "gui/icons/susan_small.png" xpos 1767 ypos 940
            #----- edited -----
            if momrelationship < 6 and NTR == True or hardntr == True:
                add "gui/icons/frank_small.png" xpos 1750 ypos 940
            add "gui/icons/cassandra_small.png" xpos 1742 ypos 940
        if dtime == 18:
            add "gui/icons/bruce_small.png" xpos 168 ypos 984
            add "gui/icons/nicole_small.png" xpos 192 ypos 984
            add "gui/icons/alexis_small.png" xpos 216 ypos 984
        #----- Custom Event Cassandra and MC Parents Room -----
        if dtime == 18 and caslovefirstfuck == True:
            add "gui/icons/cassandra_small.png" xpos 551 ypos 874
        if dtime == 19: #and basement10pmnicoleouting == False:
            add "gui/icons/bruce_small.png" xpos 551 ypos 874
            add "gui/icons/nicole_small.png" xpos 575 ypos 874
        if dtime == 19:
            add "gui/icons/alexis_small.png" xpos 334 ypos 984
            if irinafirstmeet == True:
                add "gui/icons/irina_small.png" xpos 1768 ypos 940
            add "gui/icons/cassandra_small.png" xpos 1792 ypos 940
        if dtime == 19 and basement10pmnicoleouting == True and proom19first == False:
            add "gui/icons/bruce_small.png" xpos 551 ypos 874
            add "gui/icons/nicole_small.png" xpos 575 ypos 874
        if dtime == 20:
            if frontdoorddfirst == False:
                add "gui/icons/davide_small.png" xpos 551 ypos 984
                add "gui/icons/bruce_small.png" xpos 575 ypos 984
            add "gui/icons/nicole_small.png" xpos 575 ypos 874
            add "gui/icons/alexis_small.png" xpos 454 ypos 874
        if dtime == 21:
            add "gui/icons/nicole_small.png" xpos 192 ypos 874
            add "gui/icons/alexis_small.png" xpos 216 ypos 874
            if club20extend == False:
                if irinafirstmeet == True:
                    add "gui/icons/irina_small.png" xpos 551 ypos 984
                add "gui/icons/cassandra_small.png" xpos 575 ypos 984
            add "gui/icons/davide_small.png" xpos 80 ypos 984
            add "gui/icons/bruce_small.png" xpos 104 ypos 984
        if dtime == 22 and basement10pmnicoleouting == False and basement10cassandraouting == False:
            add "gui/icons/cassandra_small.png" xpos 454 ypos 874
            add "gui/icons/alexis_small.png" xpos 216 ypos 874
            add "gui/icons/davide_small.png" xpos 56 ypos 984
            add "gui/icons/bruce_small.png" xpos 80 ypos 984
            add "gui/icons/nicole_small.png" xpos 104 ypos 984
        if dtime == 22 and basement10pmnicoleouting == True and basement10cassandraouting == True:
            add "gui/icons/cassandra_small.png" xpos 639 ypos 984
            add "gui/icons/davide_small.png" xpos 652 ypos 984
            add "gui/icons/bruce_small.png" xpos 676 ypos 984
            add "gui/icons/nicole_small.png" xpos 701 ypos 984
        if dtime == 23:
            if lroom10mcwin == True:
                add "gui/icons/nicole_small.png" xpos 104 ypos 984
            #----- edited -----
            if NTR == True and momrelationship < 6 or hardntr == True:
                add "gui/icons/davide_small.png" xpos 647 ypos 984
                add "gui/icons/bruce_small.png" xpos 671 ypos 984
                add "gui/icons/nicole_small.png" xpos 695 ypos 984
            #----- Removed as the entry to Nicole's basement stuff is in the Living Room -----
            #if lroom10mcwin == True and gangmember == True and momlove >=50 or lroom10mcwin == True and gangmember == True and momcorruption >= 30:
                #add "gui/icons/nicole_small.png" xpos 695 ypos 984
        if dtime == 24:
            if lroom10mcwin == True:
                add "gui/icons/nicole_small.png" xpos 575 ypos 874
            #----- edited -----
            if NTR == True and momrelationship < 6 or hardntr == True:
                add "gui/icons/davide_small.png" xpos 647 ypos 984
                add "gui/icons/bruce_small.png" xpos 671 ypos 984
                add "gui/icons/nicole_small.png" xpos 695 ypos 984

#----- Shows New Events -----
        # Meet Irina Event - Living Room
        if dtime == 15 and irinafirstmeet == True and irinacorruption > 5 and lroom15extendfirst == False or dtime == 15 and irinafirstmeet == True and irinalove > 5 and lroom15extendfirst == False:
            add "gui/icons/icon_new.png" xpos 50 ypos 938
        # Cassandra Extended Love Event - Living Room
        if dtime == 15 and d5love == True and lroom15extendcaslove == False:
            add "gui/icons/icon_new.png" xpos 50 ypos 938
        # Cassandra Extended Corruption Event - Living Room
        if dtime == 15 and d5corruption == True and lroom15extendcascor == False:
            add "gui/icons/icon_new.png" xpos 50 ypos 938
        # Cassandra Date Corruption Reaction Events - Kitchen
        if dtime == 9 and d5rccor == True and casreaccor == False or dtime == 9 and d5rccorfuck == True and casreaccor == False or dtime == 9 and d5rcbjsw == True and casreaccor == False or dtime == 9 and d5rcbjout == True and casreaccor == False or dtime == 9 and d5rcbjdt == True and casreaccor == False:
            add "gui/icons/icon_new.png" xpos 281 ypos 938
        # Cassandra Date Love Reaction Events - Kitchen
        if dtime == 9 and d5rclove == True and casreaclove == False or dtime == 9 and d5rclovef == True and casreaclove == False or dtime == 9 and d5rclovem == True and casreaclove == False:
            add "gui/icons/icon_new.png" xpos 281 ypos 938
        # Cassandra Date NTR Reaction Events - Kitchen
        if dtime == 9 and d5rcntr == True and casreacntr == False:
            add "gui/icons/icon_new.png" xpos 281 ypos 938
        # Cassandra First Basement Love and Corruption Event - Kitchen
        if dtime == 9 and gangmember == True and basecasfirst == False:
            add "gui/icons/icon_new.png" xpos 281 ypos 938
        # Nicole Downstairs Shower First Corruption Event - Downstairs Shower
        if dtime == 15 and momcorruption >= 20 and shower15corfirst == False:
            add "gui/icons/icon_new.png" xpos 401 ypos 938
        # Nicole Downstairs Shower Second Corruption Event - Downstairs Shower
        if dtime == 15 and momcorruption >= 35 and shower15corsecond == False:
            add "gui/icons/icon_new.png" xpos 401 ypos 938
        # Nicole Downstairs Shower Third Corruption Event - Downstairs Shower
        if dtime == 15 and basement10pmnicoleouting == True and mombasementcorsecond == True and shower15corthird == False:
            add "gui/icons/icon_new.png" xpos 401 ypos 938
        # Nicole Downstairs Shower First Love Event - Downstairs Shower
        if dtime == 15 and momlove >= 30 and shower15lovefirst == False:
            add "gui/icons/icon_new.png" xpos 401 ypos 938
        # Nicole Downstairs Shower Second Love Event - Downstairs Shower
        if dtime == 15 and momlove >= 50 and shower15lovesecond == False:
            add "gui/icons/icon_new.png" xpos 401 ypos 938
        # Nicole Downstairs Shower Third Love Event - Downstairs Shower
        if dtime == 15 and basement10pmnicoleouting == True and mombasementlovesecond == True and shower15lovethird == False:
            add "gui/icons/icon_new.png" xpos 401 ypos 938
        # Cassandra First Basement NTR Event - Basement
        if dtime == 17 and NTR == True and basecasfirst == True and basecasfrankntr == False:
            add "gui/icons/icon_new.png" xpos 642 ypos 938
        # Miranda, Nicole Basement Event - Living Room - Become a Gang Member
        if dtime == 21 and jobdone >= 2 and lroom21pdone == False:
            add "gui/icons/icon_new.png" xpos 50 ypos 938
        # Nicole Fondle Ass Event - Living Room
        if dtime == 8 and momcorruption >= 10 and lroom8fondlefirst == False:
            add "gui/icons/icon_new.png" xpos 50 ypos 938
        # Nicole Slap Ass Event - Town
        if dtime == 10 and momcorruption >= 10 and club10slapfirst == False:
            add "gui/icons/icon_new.png" xpos 1739 ypos 896
        # Irina Extended Love Event - Town
        if dtime == 20 and irinalove >= 20 and club20extendedirinalove == False:
            add "gui/icons/icon_new.png" xpos 1739 ypos 896
        # Nicole Extended Love Event - Parent's Room
        if dtime == 20 and momlove > momcorruption and momlove >= 30 and proom8pm == True: #added 'and proom8pm == True'
            add "gui/icons/icon_new.png" xpos 522 ypos 828
        # Irina Extended Corruption Event - Club
        if dtime == 19 and irinacorruption >= 30 and club20extendedirinacor == False:
            add "gui/icons/icon_new.png" xpos 1739 ypos 896
        # Cassandra First Extended Corruption Event - Town
        if dtime == 19 and bigsiscorruption >= 20 and club20extendedcascorfirst == False:
            add "gui/icons/icon_new.png" xpos 1739 ypos 896
        # Cassandra Second Extended Corruption Event - Town
        if dtime == 19 and bigsiscorruption >= 40 and club20extendedcascorsecond == False:
            add "gui/icons/icon_new.png" xpos 1739 ypos 896
        # Nicole and Bruce Fight Event - Parent's Room
        if dtime == 19 and proom19first == False and basement10pmnicoleouting == True:
            add "gui/icons/icon_new.png" xpos 522 ypos 828
        # Alexis Corruption Event - Alexis Room
        if dtime == 14 and lilsisrelationship >= 6 and lilsiscorruption >= 30 and secret2corfirst == False:
            add "gui/icons/icon_new.png" xpos 162 ypos 828
        # Join Fitness Club Event - Town
        if dtime == 17 and fitnessfirst == False:
            add "gui/icons/icon_new.png" xpos 1739 ypos 896
        # Nicole Outing Basement Event - Basement
        if dtime == 22 and mombasementcorsecond == True and basement10pmnicoleouting == False:
            add "gui/icons/icon_new.png" xpos 642 ypos 938
        # Cassandra Outing Basement Event Fail - Basement
        if dtime == 22 and mombasementlovesecond == True and basement10pmnicoleouting == False:
            add "gui/icons/icon_new.png" xpos 642 ypos 938
        # Nicole, Cassandra, Miranda Orgy - Basement
        if dtime == 22 and basement10pmnicoleouting == True and basement10cassandraouting == True and baseorgyfirst == False:
            add "gui/icons/icon_new.png" xpos 642 ypos 938
        # Cassandra Outing Basement Event Success - Basement
        if dtime == 22 and gangmember == True and basecassecond == True and basement10cassandraouting == False:
            add "gui/icons/icon_new.png" xpos 642 ypos 938
        # Nicole First Basement Event - Basement
        if dtime == 23 and lroom10mcwin == True and gangmember == True and momlove >=50 or dtime == 23 and lroom10mcwin == True and gangmember == True and momcorruption >= 30:
            add "gui/icons/icon_new.png" xpos 642 ypos 938
        # Nicole Secret Event - Downstairs Shower
        if dtime == 7 and momdrugfirst == True and momsecret == False:
            add "gui/icons/icon_new.png" xpos 401 ypos 938
        # First Time Selling Drugs Event - Basement
        if dtime == 16 and gangmember == True and selldrugs == False:
            add "gui/icons/icon_new.png" xpos 642 ypos 938
        # Nicole First Fitness Center Event - Town
        if dtime == 9 and momlove >= 20 and fitnessnicfirst == False and fitnessmember == True or dtime == 9 and momcorruption >= 20 and fitnessnicfirst == False and fitnessmember == True:
            add "gui/icons/icon_new.png" xpos 1739 ypos 896
        # Alexis First Basement Event - Basement
        if dtime == 8 and gangmember == True and lilsisrelationship >= 6 and lilsislove >= 50 and showbasealfirst == False or dtime == 8 and gangmember == True and lilsisrelationship >= 6 and lilsiscorruption >= 30 and showbasealfirst == False:
            add "gui/icons/icon_new.png" xpos 281 ypos 938
        # Custom - Dad and Cassandra - Basement
        if dtime == 20 and basementkey == True and bigsisrelationship <= 5 and dadcasbasementfirst == False or dtime == 20 and gangmember == True and hardntr == True and dadcasbasementfirst == False:
            add "gui/icons/icon_new.png" xpos 642 ypos 938
        # Custom - MC and Cassandra - Parents Room
        if dtime == 18 and caslovefirstfuck == True and cassandmcparentsroom == False:
            add "gui/icons/icon_new.png" xpos 522 ypos 828
        #----- Added in 0.75 Part 2 ----- Unfinished
        if dtime == 7 and showerup7amextfirstcor == False and lilsiscorruption >= lilsislove or dtime == 7 and basealefirst == True and showerup7amextfirstlove == False and lilsiscorruption < lilsislove:
            add "gui/icons/icon_new.png" xpos 401 ypos 828
        #----- Added in 0.75 Part 2 ----- Unfinished
        if dtime == 7 and basealefirst == True and showerup7amextfirstcor == True and showerup7amextfirstcor2 == False or lilsiscorruption >= 60 and dtime == 7 and showerup7amextfirstcor == True and showerup7amextfirstcor2 == False:
            add "gui/icons/icon_new.png" xpos 401 ypos 828
        #----- Added in 0.75 Part 2 ----- Unfinished
        if dtime == 7 and basealefirst == True and lilsislove > lilsiscorruption and showerup7amextfirstlove == True and showerup7amextfirstlove2 == False:
            add "gui/icons/icon_new.png" xpos 401 ypos 828
    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value


screen townl():
    default tt = Tooltip ("")

    fixed:
        #----- edited -----
        if dtime == 14 and lilsisrelationship < 6 and NTR == True or dtime == 14 and hardntr == True:
            imagebutton auto "gui/icons/icon_secret_place_%s.png" xpos 50 ypos 938 action (Hide('townl'), Jump('secretplace')) hovered tt.Action ("Secret place") focus_mask True
        imagebutton auto "gui/icons/icon_club_%s.png" xpos 162 ypos 938 action (Hide('townl'), Jump('club')) hovered tt.Action ("The Sleazy Weasel") focus_mask True
        imagebutton auto "gui/icons/icon_subway_%s.png" xpos 281 ypos 938 action (Hide('townl'), Jump('subway')) hovered tt.Action ("Subway") focus_mask True
        imagebutton auto "gui/icons/icon_tanning_salon_%s.png" xpos 50 ypos 828 action (Hide('townl'), Jump('tanning')) hovered tt.Action ("Tanning Salon") focus_mask True
        imagebutton auto "gui/icons/icon_town_%s.png" xpos 1739 ypos 896 action (Hide('townl'), Jump('town')) hovered tt.Action ("Town") focus_mask True
        if dtime == 17 or dtime == 9:
            imagebutton auto "gui/icons/icon_fitness_studio_%s.png" xpos 162 ypos 828 action (Hide('townl'), Jump('fitness')) hovered tt.Action ("Fitness Studio") focus_mask True
        imagebutton auto "gui/icons/icon_skip_%s.png" xpos 281 ypos 828 action (Hide('townl'), Jump('skip2')) hovered tt.Action ("Skip 1 hour") focus_mask True

        if dtime == 10:
            add "gui/icons/nicole_small.png" xpos 216 ypos 984
            #----- edited -----
            if momrelationship < 6 and NTR == True and frankfirstmeet == True or hardntr == True and frankfirstmeet == True:
                add "gui/icons/frank_small.png" xpos 190 ypos 984
        if dtime == 16:
            if irinafirstmeet == True:
                add "gui/icons/irina_small.png" xpos 104 ypos 874
            #----- edited -----
            if irinarelationship < 6 and NTR == True and frankfirstmeet == True or hardntr == True and frankfirstmeet == True:
                add "gui/icons/frank_small.png" xpos 79 ypos 874
        if dtime == 17:
            add "gui/icons/nicole_small.png" xpos 104 ypos 874
            #----- edited -----
            if momrelationship < 6 and NTR == True and frankfirstmeet == True or hardntr == True and frankfirstmeet == True:
                add "gui/icons/frank_small.png" xpos 79 ypos 874
        if dtime == 19:
            add "gui/icons/kate_small.png" xpos 141 ypos 984
            add "gui/icons/martin_small.png" xpos 166 ypos 984
            add "gui/icons/irina_small.png" xpos 191 ypos 984
            add "gui/icons/cassandra_small.png" xpos 216 ypos 984


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value
