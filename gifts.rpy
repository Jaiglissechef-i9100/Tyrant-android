

label sp2pmgiftfl:
    hide screen locations
    if giftflowersdaya == True:
        scene black
        "You already gave her flowers today."
    else:
        $ giftflowers -= 1
        $ giftflowersdaya = True
        if lilsisrelationship > 5:
            scene town secret 2pm 000gilo
            ls "You bought me flowers. That's so nice [pov]! Thank you!"
            pov "You're welcome."
        else:
            scene town secret 2pm 000gilored
            ls "Oh you bought me flowers. Thanks."
            pov "You're welcome."
        $ lilsisrelationship += 5
        $ lilsislove += 5
    jump lsisroom


label sp2pmgiftco:
    hide screen locations
    if giftcondomsdaya == True:
        scene black
        "You already gave her condoms today."
    else:
        $ giftcondoms -= 1
        $ giftcondomsdaya = True
        if lilsisrelationship > 5:
            scene town secret 2pm 000gico
            ls "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            ls "Oh... thank you..."
            pov "You're welcome."
        else:
            scene town secret 2pm 000gicored
            ls "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            ls "..."
            pov "You're welcome."
        $ lilsisrelationship += 5
        $ lilsiscorruption += 5
    jump lsisroom


label sp2pmgiftcho:
    hide screen locations
    if giftchocolatedaya == True:
        scene black
        "You already gave her chocolate today."
    else:
        $ giftchocolate -= 1
        $ giftchocolatedaya = True
        if lilsisrelationship > 5:
            scene town secret 2pm 000gilo
            ls "You bought me chocolate. That's so nice [pov]! Thank you!"
            pov "You're welcome."
        else:
            scene town secret 2pm 000gilored
            ls "Oh you bought me chocolate. Thanks."
            pov "You're welcome."
        $ lilsisrelationship += 5
    jump lsisroom


label mom12pmgiftfl:
    if giftflowersdayn == True:
        scene black
        "You already gave her flowers today."
    else:
        $ giftflowers -= 1
        $ giftflowersdayn = True
        if momrelationship > 5:
            if nicolereddresswear == True:
                scene diningroom 12pm 003ngilocc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003ngilocc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003ngilocl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003ngilocl2
            else:
                scene diningroom 12pm 003ngilo
            mom "You bought me flowers. That's so nice [pov]! Thank you!"
            ls "Oh, how sweet!"
            pov "You're welcome."
        else:
            if nicolereddresswear == True:
                scene diningroom 12pm 003ngiloredcc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003ngiloredcc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003ngiloredcl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003ngiloredcl2
            else:
                scene diningroom 12pm 003ngilored
            mom "Oh you bought me flowers. Thanks."
            ls "Oh, how sweet!"
            pov "You're welcome."
        $ momrelationship += 5
        $ momlove += 5
    jump droom12gift

label mom12pmgiftco:
    if giftcondomsdayn == True:
        scene black
        "You already gave her condoms today."
    else:
        $ giftcondoms -= 1
        $ giftcondomsdayn = True
        if momrelationship > 5:
            if nicolereddresswear == True:
                scene diningroom 12pm 003ngicocc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003ngicocc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003ngicocl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003ngicocl2
            else:
                scene diningroom 12pm 003ngico
            mom "You bought me condoms?"
            mom "But..."
            ls "Ohh..."
            bs "<giggle>"
            pov "Yes, you'll need them soon!"
            mom "Oh... thank you..."
            pov "You're welcome."
        else:
            if nicolereddresswear == True:
                scene diningroom 12pm 003ngicoredcc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003ngicoredcc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003ngicoredcl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003ngicoredcl2
            else:
                scene diningroom 12pm 003ngicored
            mom "You bought me condoms?"
            mom "But..."
            ls "Ohh..."
            bs "<giggle>"
            pov "Yes, you'll need them soon!"
            mom "..."
            pov "You're welcome."
        $ momrelationship += 5
        $ momcorruption += 5
    jump droom12gift

label mom12pmgiftcho:
    if giftchocolatedayn == True:
        scene black
        "You already gave her chocolate today."
    else:
        $ giftchocolate -= 1
        $ giftchocolatedayn = True
        if lilsisrelationship > 5:
            if nicolereddresswear == True:
                scene diningroom 12pm 003ngilocc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003ngilocc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003ngilocl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003ngilocl2
            else:
                scene diningroom 12pm 003ngilo
            mom "You bought me chocolate. That's so nice [pov]! Thank you!"
            ls "Oh, tasty!"
            pov "You're welcome."
        else:
            if nicolereddresswear == True:
                scene diningroom 12pm 003ngiloredcc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003ngiloredcc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003ngiloredcl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003ngiloredcl2
            else:
                scene diningroom 12pm 003ngilored
            mom "Oh you bought me chocolate. Thanks."
            ls "Oh, tasty!"
            pov "You're welcome."
        $ momrelationship += 5
    jump droom12gift

label mom12pmgiftrd:
    $ nicolereddress = 3
    scene diningroom 12pm 003ngico
    mom "You bought me this?"
    mom "But..."
    ls "Ohh..."
    bs "<giggle>"
    mom "Can we talk later?"
    pov "Of course."
    jump droom12gift

label mom12pmgiftbd:
    $ nicolebabydoll = 3
    if nicolereddresswear == True:
        scene diningroom 12pm 003ngicocc1
    else:
        scene diningroom 12pm 003ngico
    mom "You bought me this?"
    mom "But..."
    ls "Ohh..."
    bs "<giggle>"
    mom "Can we talk later?"
    pov "Of course."
    jump droom12gift

label mom12pmgiftsp:
    $ nicolesweaterpants = 3
    scene diningroom 12pm 003ngilo
    mom "You bought me this?"
    mom "But..."
    ls "Ohh..."
    bs "<giggle>"
    mom "Can we talk later?"
    pov "Of course."
    jump droom12gift

label mom12pmgiftro:
    $ nicolerobe = 3
    if nicolesweaterpantswear == True:
        scene diningroom 12pm 003ngilocl1
    else:
        scene diningroom 12pm 003ngilo
    mom "You bought me this?"
    mom "But..."
    ls "Ohh..."
    bs "<giggle>"
    mom "Can we talk later?"
    pov "Of course."
    jump droom12gift





label ls12pmgiftfl:
    if giftflowersdaya == True:
        scene black
        "You already gave her flowers today."
    else:
        $ giftflowers -= 1
        $ giftflowersdaya = True
        if lilsisrelationship > 5:
            if nicolereddresswear == True:
                scene diningroom 12pm 003agilocc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003agilocc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003agilocl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003agilocl2
            else:
                scene diningroom 12pm 003agilo
            ls "You bought me flowers. That's so nice [pov]! Thank you!"
            mom "What a nice idea!"
            pov "You're welcome."
        else:
            if nicolereddresswear == True:
                scene diningroom 12pm 003agiloredcc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003agiloredcc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003agiloredcl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003agiloredcl2
            else:
                scene diningroom 12pm 003agilored
            ls "Oh you bought me flowers. Thanks."
            mom "What a nice idea!"
            pov "You're welcome."
        $ lilsisrelationship += 5
        $ lilsislove += 5
    jump droom12gift

label ls12pmgiftco:
    if giftcondomsdaya == True:
        scene black
        "You already gave her condoms today."
    else:
        $ giftcondoms -= 1
        $ giftcondomsdaya = True
        if lilsisrelationship > 5:
            if nicolereddresswear == True:
                scene diningroom 12pm 003agicocc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003agicocc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003agicocl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003agicocl2
            else:
                scene diningroom 12pm 003agico
            ls "You bought me condoms?"
            ls "But..."
            mom "You did what...?"
            bs "<giggle>"
            pov "Yes, you'll need them soon!"
            ls "Oh... thank you..."
            mom "I don't think so."
            pov "You're welcome."
        else:
            if nicolereddresswear == True:
                scene diningroom 12pm 003agicoredcc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003agicoredcc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003agicoredcl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003agicoredcl2
            else:
                scene diningroom 12pm 003agicored
            ls "You bought me condoms?"
            ls "But..."
            mom "You did what...?"
            bs "<giggle>"
            pov "Yes, you'll need them soon!"
            ls "..."
            mom "I don't think so."
            pov "You're welcome."
        $ lilsisrelationship += 5
        $ lilsiscorruption += 5
    jump droom12gift

label ls12pmgiftcho:
    if giftchocolatedaya == True:
        scene black
        "You already gave her chocolate today."
    else:
        $ giftchocolate -= 1
        $ giftchocolatedaya = True
        if lilsisrelationship > 5:
            if nicolereddresswear == True:
                scene diningroom 12pm 003agilocc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003agilocc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003agilocl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003agilocl2
            else:
                scene diningroom 12pm 003agilo
            ls "You bought me chocolate. That's so nice [pov]! Thank you!"
            mom "Haha, but no eating it now!"
            pov "You're welcome."
        else:
            if nicolereddresswear == True:
                scene diningroom 12pm 003agiloredcc1
            elif nicolebabydollwear == True:
                scene diningroom 12pm 003agiloredcc2
            elif nicolesweaterpantswear == True:
                scene diningroom 12pm 003agiloredcl1
            elif nicolerobewear == True:
                scene diningroom 12pm 003agiloredcl2
            else:
                scene diningroom 12pm 003agilored
            ls "Oh you bought me chocolate. Thanks."
            mom "Haha, but no eating it now!"
            pov "You're welcome."
        $ lilsisrelationship += 5
    jump droom12gift


label bs12pmgiftfl:
    if giftflowersdayc == True:
        scene black
        "You already gave her flowers today."
    else:
        $ giftflowers -= 1
        $ giftflowersdayc = True
        if bigsisrelationship > 5:
            scene diningroom 12pm 003cgilo
            bs "You bought me flowers? That's a nice surprise! Thank you!"
            mom "See, he can be nice to you too."
            ls "That must be a mistake, haha."
            pov "You're welcome."
        else:
            scene diningroom 12pm 003cgilored
            bs "You bought me flowers? Thanks."
            mom "See, he can be nice to you too."
            ls "That must be a mistake, haha."
            pov "You're welcome."
        $ bigsisrelationship += 5
        $ bigsislove += 5
    jump droom12gift

label bs12pmgiftco:
    if giftcondomsdayc == True:
        scene black
        "You already gave her condoms today."
    else:
        $ giftcondoms -= 1
        $ giftcondomsdayc = True
        if bigsisrelationship > 5:
            scene diningroom 12pm 003cgico
            bs "You bought me condoms?"
            bs "Serious...?"
            mom "..."
            ls "Ohh..."
            pov "Yes, you'll need them soon!"
            bs "Hmm... thank you..."
            ls "<giggle>"
            pov "You're welcome."
        else:
            scene diningroom 12pm 003cgicored
            bs "You bought me condoms?"
            bs "Serious...?"
            mom "..."
            ls "Ohh..."
            pov "Yes, you'll need them soon!"
            bs "..."
            ls "<giggle>"
            pov "You're welcome."
        $ bigsisrelationship += 5
        $ bigsiscorruption += 5
    jump droom12gift

label bs12pmgiftcho:
    if giftchocolatedayc == True:
        scene black
        "You already gave her chocolate today."
    else:
        $ giftchocolate -= 1
        $ giftchocolatedayc = True
        if bigsisrelationship > 5:
            scene diningroom 12pm 003cgilo
            bs "You bought me chocolate. I don't think I can eat it. But thank you!"
            pov "You're welcome."
            ls "Can I have it?"
        else:
            scene diningroom 12pm 003cgilored
            bs "You bought me chocolate. Hmm, thanks."
            pov "You're welcome."
            ls "Can I have it?"
        $ bigsisrelationship += 5
    jump droom12gift



label dr7amgiftfl:
    hide screen locations
    if giftflowersdayn == True:
        scene black
        "You already gave her flowers today."
    else:
        $ giftflowers -= 1
        $ giftflowersdayn = True
        if momrelationship > 5:
            scene diningroom 7am 004gilo
            mom "You bought me flowers. That's so nice [pov]! Thank you!"
            pov "You're welcome."
        else:
            scene diningroom 7am 004gilored
            mom "Oh you bought me flowers. Thanks."
            pov "You're welcome."
        $ momrelationship += 5
        $ momlove += 5
    jump droom

label dr7amgiftco:
    hide screen locations
    if giftcondomsdayn == True:
        scene black
        "You already gave her condoms today."
    else:
        $ giftcondoms -= 1
        $ giftcondomsdayn = True
        if momrelationship > 5:
            scene diningroom 7am 004gico
            mom "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            mom "Oh... thank you..."
            pov "You're welcome."
        else:
            scene diningroom 7am 004gicored
            mom "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            mom "..."
            pov "You're welcome."
        $ momrelationship += 5
        $ momcorruption += 5
    jump droom

label dr7amgiftcho:
    hide screen locations
    if giftchocolatedayn == True:
        scene black
        "You already gave her chocolate today."
    else:
        $ giftchocolate -= 1
        $ giftchocolatedayn = True
        if momrelationship > 5:
            scene diningroom 7am 004gilo
            mom "You bought me chocolate. That's so nice [pov]! Thank you!"
            pov "You're welcome."
        else:
            scene diningroom 7am 004gilored
            mom "Oh you bought me chocolate. Thanks."
            pov "You're welcome."
        $ momrelationship += 5
    jump droom



label ls10pmgiftfl:
    hide screen locations
    if giftflowersdaya == True:
        scene black
        "You already gave her flowers today."
    else:
        $ giftflowers -= 1
        $ giftflowersdaya = True
        if lilsisrelationship > 5:
            scene lilsisroom 10pm 004gilo
            ls "You bought me flowers. That's so nice [pov]! Thank you!"
            pov "You're welcome."
        else:
            scene lilsisroom 10pm 004gilored
            ls "Oh you bought me flowers. Thanks."
            pov "You're welcome."
        $ lilsisrelationship += 5
        $ lilsislove += 5
    jump lsisroom

label ls10pmgiftco:
    hide screen locations
    if giftcondomsdaya == True:
        scene black
        "You already gave her condoms today."
    else:
        $ giftcondoms -= 1
        $ giftcondomsdaya = True
        if lilsisrelationship > 5:
            scene lilsisroom 10pm 004gico
            ls "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            ls "Oh... thank you..."
            pov "You're welcome."
        else:
            scene lilsisroom 10pm 004gicored
            ls "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            ls "..."
            pov "You're welcome."
        $ lilsisrelationship += 5
        $ lilsiscorruption += 5
    jump lsisroom

label ls10pmgiftcho:
    hide screen locations
    if giftchocolatedaya == True:
        scene black
        "You already gave her chocolate today."
    else:
        $ giftchocolate -= 1
        $ giftchocolatedaya = True
        if lilsisrelationship > 5:
            scene lilsisroom 10pm 004gilo
            ls "You bought me chocolate. That's so nice [pov]! Thank you!"
            pov "You're welcome."
        else:
            scene lilsisroom 10pm 004gilored
            ls "Oh you bought me chocolate. Thanks."
            pov "You're welcome."
        $ lilsisrelationship += 5
    jump lsisroom


label irfd21giftfl:
    if giftflowersdayi == True:
        scene black
        "You already gave her flowers today."
    else:
        $ giftflowers -= 1
        $ giftflowersdayi = True
        if irinarelationship > 5:
            scene frontdoor 9pm 003igilo
            irina "You bought me flowers. That's so nice [pov]! Thank you!"
            pov "You're welcome."
            bs "..."
        else:
            scene frontdoor 9pm 003igilored
            irina "Oh you bought me flowers. Thanks."
            pov "You're welcome."
            bs "..."
        $ irinarelationship += 5
        $ irinalove += 5
    jump frontdoor21talk2

label irfd21giftco:
    if giftcondomsdayi == True:
        scene black
        "You already gave her condoms today."
    else:
        $ giftcondoms -= 1
        $ giftcondomsdayi = True
        if irinarelationship > 5:
            scene frontdoor 9pm 003igico
            irina "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            irina "Oh... thank you..."
            pov "You're welcome."
        else:
            scene frontdoor 9pm 003igicored
            irina "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            irina "..."
            pov "You're welcome."
        $ irinarelationship += 5
        $ irinacorruption += 5
    jump frontdoor21talk2

label irfd21giftcho:
    if giftchocolatedayi == True:
        scene black
        "You already gave her chocolate today."
    else:
        $ giftchocolate -= 1
        $ giftchocolatedayi = True
        if irinarelationship > 5:
            scene frontdoor 9pm 003igilo
            irina "You bought me chocolate. That's so nice [pov]! Thank you!"
            pov "You're welcome."
            bs "..."
        else:
            scene frontdoor 9pm 003igilored
            irina "Oh you bought me chocolate. Thanks."
            pov "You're welcome."
            bs "..."
        $ irinarelationship += 5
    jump frontdoor21talk2


label bsfd21giftfl:
    if giftflowersdayc == True:
        scene black
        "You already gave her flowers today."
    else:
        $ giftflowers -= 1
        $ giftflowersdayc = True
        if bigsisrelationship > 5:
            scene frontdoor 9pm 003cgilo
            bs "You bought me flowers. ... Thank you!"
            pov "You're welcome."
            irina "Oh, how sweet!"
        else:
            scene frontdoor 9pm 003cgilored
            bs "Oh you bought me flowers..."
            pov "You're welcome."
            irina "Oh, how sweet!"
        $ bigsisrelationship += 5
        $ bigsislove += 5
    jump frontdoor21talk2

label bsfd21giftco:
    if giftcondomsdayc == True:
        scene black
        "You already gave her condoms today."
    else:
        $ giftcondoms -= 1
        $ giftcondomsdayc = True
        if bigsisrelationship > 5:
            scene frontdoor 9pm 003cgico
            bs "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            bs "Oh... thank you..."
            pov "You're welcome."
        else:
            scene frontdoor 9pm 003cgicored
            bs "You bought me condoms?"
            pov "Yes, you'll need them soon!"
            bs "..."
            pov "You're welcome."
        $ bigsisrelationship += 5
        $ bigsiscorruption += 5
    jump frontdoor21talk2

label bsfd21giftcho:
    if giftchocolatedayc == True:
        scene black
        "You already gave her chocolate today."
    else:
        $ giftchocolate -= 1
        $ giftchocolatedayc = True
        if bigsisrelationship > 5:
            scene frontdoor 9pm 003cgilo
            bs "You bought me chocolate. Hmm, thanks."
            pov "You're welcome."
            irina "Can I have it?"
        else:
            scene frontdoor 9pm 003cgilored
            bs "You bought me chocolate..."
            pov "You're welcome."
            irina "Can I have it?"
        $ bigsisrelationship += 5
    jump frontdoor21talk2