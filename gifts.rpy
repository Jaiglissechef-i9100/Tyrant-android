

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
            scene diningroom 12pm 003ngilo
            if nicolereddresswear == True:
                show 12pm003ngiloniccorruption1:
                    xpos 244
                    ypos 309
            elif nicolebabydollwear == True:
                show 12pm003ngiloniccorruption2:
                    xpos 244
                    ypos 309
            elif nicolesweaterpantswear == True:
                show 12pm003ngiloniclove1:
                    xpos 244
                    ypos 309
            elif nicolerobewear == True:
                show 12pm003ngiloniclove2:
                    xpos 244
                    ypos 309
            else:
                show 12pm003ngilonicnormal:
                    xpos 244
                    ypos 309
            if alexisrockerwear == True:
                show 12pm003ngiloalecorruption1:
                    xpos 1141
                    ypos 385
            elif alexislingeriewear == True:
                show 12pm003ngiloalecorruption2:
                    xpos 1141
                    ypos 385
            elif alexisjeansskirtwear == True:
                show 12pm003ngiloalelove1:
                    xpos 1141
                    ypos 385
            elif alexisgridwear == True:
                show 12pm003ngiloalelove2:
                    xpos 1141
                    ypos 385
            else:
                show 12pm003ngiloalenormal:
                    xpos 1141
                    ypos 385
            mom "You bought me flowers. That's so nice [pov]! Thank you!"
            ls "Oh, how sweet!"
            pov "You're welcome."
        else:
            scene diningroom 12pm 003ngilored
            if nicolereddresswear == True:
                show 12pm003ngiloredniccorruption1:
                    xpos 240
                    ypos 330
            elif nicolebabydollwear == True:
                show 12pm003ngiloredniccorruption2:
                    xpos 240
                    ypos 330
            elif nicolesweaterpantswear == True:
                show 12pm003ngiloredniclove1:
                    xpos 240
                    ypos 330
            elif nicolerobewear == True:
                show 12pm003ngiloredniclove2:
                    xpos 240
                    ypos 330
            else:
                show 12pm003ngilorednicnormal:
                    xpos 240
                    ypos 330
            if alexisrockerwear == True:
                show 12pm003ngiloalecorruption1:
                    xpos 1141
                    ypos 385
            elif alexislingeriewear == True:
                show 12pm003ngiloalecorruption2:
                    xpos 1141
                    ypos 385
            elif alexisjeansskirtwear == True:
                show 12pm003ngiloalelove1:
                    xpos 1141
                    ypos 385
            elif alexisgridwear == True:
                show 12pm003ngiloalelove2:
                    xpos 1141
                    ypos 385
            else:
                show 12pm003ngiloalenormal:
                    xpos 1141
                    ypos 385
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
            scene diningroom 12pm 003ngico
            if nicolereddresswear == True:
                show 12pm003ngiconiccorruption1:
                    xpos 244
                    ypos 309
            elif nicolebabydollwear == True:
                show 12pm003ngiconiccorruption2:
                    xpos 244
                    ypos 309
            elif nicolesweaterpantswear == True:
                show 12pm003ngiconiclove1:
                    xpos 244
                    ypos 309
            elif nicolerobewear == True:
                show 12pm003ngiconiclove2:
                    xpos 244
                    ypos 309
            else:
                show 12pm003ngiconicnormal:
                    xpos 244
                    ypos 309
            if alexisrockerwear == True:
                show 12pm003ngicoalecorruption1:
                    xpos 1146
                    ypos 399
            elif alexislingeriewear == True:
                show 12pm003ngicoalecorruption2:
                    xpos 1146
                    ypos 399
            elif alexisjeansskirtwear == True:
                show 12pm003ngicoalelove1:
                    xpos 1146
                    ypos 399
            elif alexisgridwear == True:
                show 12pm003ngicoalelove2:
                    xpos 1146
                    ypos 399
            else:
                show 12pm003ngicoalenormal:
                    xpos 1146
                    ypos 399
            mom "You bought me condoms?"
            mom "But..."
            ls "Ohh..."
            bs "<giggle>"
            pov "Yes, you'll need them soon!"
            mom "Oh... thank you..."
            pov "You're welcome."
        else:
            scene diningroom 12pm 003ngicored
            if nicolereddresswear == True:
                show 12pm003ngicoredniccorruption1:
                    xpos 246
                    ypos 331
            elif nicolebabydollwear == True:
                show 12pm003ngicoredniccorruption2:
                    xpos 246
                    ypos 331
            elif nicolesweaterpantswear == True:
                show 12pm003ngicoredniclove1:
                    xpos 246
                    ypos 331
            elif nicolerobewear == True:
                show 12pm003ngicoredniclove2:
                    xpos 246
                    ypos 331
            else:
                show 12pm003ngicorednicnormal:
                    xpos 246
                    ypos 331
            if alexisrockerwear == True:
                show 12pm003ngicoalecorruption1:
                    xpos 1146
                    ypos 399
            elif alexislingeriewear == True:
                show 12pm003ngicoalecorruption2:
                    xpos 1146
                    ypos 399
            elif alexisjeansskirtwear == True:
                show 12pm003ngicoalelove1:
                    xpos 1146
                    ypos 399
            elif alexisgridwear == True:
                show 12pm003ngicoalelove2:
                    xpos 1146
                    ypos 399
            else:
                show 12pm003ngicoalenormal:
                    xpos 1146
                    ypos 399
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
            scene diningroom 12pm 003ngilo
            if nicolereddresswear == True:
                show 12pm003ngiloniccorruption1:
                    xpos 244
                    ypos 309
            elif nicolebabydollwear == True:
                show 12pm003ngiloniccorruption2:
                    xpos 244
                    ypos 309
            elif nicolesweaterpantswear == True:
                show 12pm003ngiloniclove1:
                    xpos 244
                    ypos 309
            elif nicolerobewear == True:
                show 12pm003ngiloniclove2:
                    xpos 244
                    ypos 309
            else:
                show 12pm003ngilonicnormal:
                    xpos 244
                    ypos 309
            if alexisrockerwear == True:
                show 12pm003ngiloalecorruption1:
                    xpos 1141
                    ypos 385
            elif alexislingeriewear == True:
                show 12pm003ngiloalecorruption2:
                    xpos 1141
                    ypos 385
            elif alexisjeansskirtwear == True:
                show 12pm003ngiloalelove1:
                    xpos 1141
                    ypos 385
            elif alexisgridwear == True:
                show 12pm003ngiloalelove2:
                    xpos 1141
                    ypos 385
            else:
                show 12pm003ngiloalenormal:
                    xpos 1141
                    ypos 385
            mom "You bought me chocolate. That's so nice [pov]! Thank you!"
            ls "Oh, tasty!"
            pov "You're welcome."
        else:
            scene diningroom 12pm 003ngilored
            if nicolereddresswear == True:
                show 12pm003ngiloredniccorruption1:
                    xpos 240
                    ypos 330
            elif nicolebabydollwear == True:
                show 12pm003ngiloredniccorruption2:
                    xpos 240
                    ypos 330
            elif nicolesweaterpantswear == True:
                show 12pm003ngiloredniclove1:
                    xpos 240
                    ypos 330
            elif nicolerobewear == True:
                show 12pm003ngiloredniclove2:
                    xpos 240
                    ypos 330
            else:
                show 12pm003ngilorednicnormal:
                    xpos 240
                    ypos 330
            if alexisrockerwear == True:
                show 12pm003ngiloalecorruption1:
                    xpos 1141
                    ypos 385
            elif alexislingeriewear == True:
                show 12pm003ngiloalecorruption2:
                    xpos 1141
                    ypos 385
            elif alexisjeansskirtwear == True:
                show 12pm003ngiloalelove1:
                    xpos 1141
                    ypos 385
            elif alexisgridwear == True:
                show 12pm003ngiloalelove2:
                    xpos 1141
                    ypos 385
            else:
                show 12pm003ngiloalenormal:
                    xpos 1141
                    ypos 385
            mom "Oh you bought me chocolate. Thanks."
            ls "Oh, tasty!"
            pov "You're welcome."
        $ momrelationship += 5
    jump droom12gift

label mom12pmgiftrd:
    $ nicolereddress = 3
    scene diningroom 12pm 003ngico
    show 12pm003ngiconicnormal:
        xpos 244
        ypos 309
    if alexisrockerwear == True:
        show 12pm003ngicoalecorruption1:
            xpos 1146
            ypos 399
    elif alexislingeriewear == True:
        show 12pm003ngicoalecorruption2:
            xpos 1146
            ypos 399
    elif alexisjeansskirtwear == True:
        show 12pm003ngicoalelove1:
            xpos 1146
            ypos 399
    elif alexisgridwear == True:
        show 12pm003ngicoalelove2:
            xpos 1146
            ypos 399
    else:
        show 12pm003ngicoalenormal:
            xpos 1146
            ypos 399
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
        scene diningroom 12pm 003ngico
        show 12pm003ngiloniccorruption1:
            xpos 244
            ypos 309
        if alexisrockerwear == True:
            show 12pm003ngicoalecorruption1:
                xpos 1146
                ypos 399
        elif alexislingeriewear == True:
            show 12pm003ngicoalecorruption2:
                xpos 1146
                ypos 399
        elif alexisjeansskirtwear == True:
            show 12pm003ngicoalelove1:
                xpos 1146
                ypos 399
        elif alexisgridwear == True:
            show 12pm003ngicoalelove2:
                xpos 1146
                ypos 399
        else:
            show 12pm003ngicoalenormal:
                xpos 1146
                ypos 399
    else:
        scene diningroom 12pm 003ngico
        show 12pm003ngilonicnormal:
            xpos 244
            ypos 309
        if alexisrockerwear == True:
            show 12pm003ngicoalecorruption1:
                xpos 1146
                ypos 399
        elif alexislingeriewear == True:
            show 12pm003ngicoalecorruption2:
                xpos 1146
                ypos 399
        elif alexisjeansskirtwear == True:
            show 12pm003ngicoalelove1:
                xpos 1146
                ypos 399
        elif alexisgridwear == True:
            show 12pm003ngicoalelove2:
                xpos 1146
                ypos 399
        else:
            show 12pm003ngicoalenormal:
                xpos 1146
                ypos 399
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
    show 12pm003ngilonicnormal:
        xpos 244
        ypos 309
    if alexisrockerwear == True:
        show 12pm003ngiloalecorruption1:
            xpos 1141
            ypos 385
    elif alexislingeriewear == True:
        show 12pm003ngiloalecorruption2:
            xpos 1141
            ypos 385
    elif alexisjeansskirtwear == True:
        show 12pm003ngiloalelove1:
            xpos 1141
            ypos 385
    elif alexisgridwear == True:
        show 12pm003ngiloalelove2:
            xpos 1141
            ypos 385
    else:
        show 12pm003ngiloalenormal:
            xpos 1141
            ypos 385
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
        scene diningroom 12pm 003ngilo
        show 12pm003ngiloniclove1:
            xpos 244
            ypos 309
        if alexisrockerwear == True:
            show 12pm003ngiloalecorruption1:
                xpos 1141
                ypos 385
        elif alexislingeriewear == True:
            show 12pm003ngiloalecorruption2:
                xpos 1141
                ypos 385
        elif alexisjeansskirtwear == True:
            show 12pm003ngiloalelove1:
                xpos 1141
                ypos 385
        elif alexisgridwear == True:
            show 12pm003ngiloalelove2:
                xpos 1141
                ypos 385
        else:
            show 12pm003ngiloalenormal:
                xpos 1141
                ypos 385
    else:
        scene diningroom 12pm 003ngilo
        show 12pm003ngilonicnormal:
            xpos 244
            ypos 309
        if alexisrockerwear == True:
            show 12pm003ngiloalecorruption1:
                xpos 1141
                ypos 385
        elif alexislingeriewear == True:
            show 12pm003ngiloalecorruption2:
                xpos 1141
                ypos 385
        elif alexisjeansskirtwear == True:
            show 12pm003ngiloalelove1:
                xpos 1141
                ypos 385
        elif alexisgridwear == True:
            show 12pm003ngiloalelove2:
                xpos 1141
                ypos 385
        else:
            show 12pm003ngiloalenormal:
                xpos 1141
                ypos 385
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
            scene diningroom 12pm 003agilo
            if nicolereddresswear == True:
                show 12pm003agiloniccorruption1:
                    xpos 327
                    ypos 346
            elif nicolebabydollwear == True:
                show 12pm003agiloniccorruption2:
                    xpos 327
                    ypos 346
            elif nicolesweaterpantswear == True:
                show 12pm003agiloniclove1:
                    xpos 327
                    ypos 346
            elif nicolerobewear == True:
                show 12pm003agiloniclove2:
                    xpos 327
                    ypos 346
            else:
                show 12pm003agilonicnormal:
                    xpos 327
                    ypos 346
            if alexisrockerwear == True:
                show 12pm003agiloalecorruption1:
                    xpos 1093
                    ypos 389
            elif alexislingeriewear == True:
                show 12pm003agiloalecorruption2:
                    xpos 1093
                    ypos 389
            elif alexisjeansskirtwear == True:
                show 12pm003agiloalelove1:
                    xpos 1093
                    ypos 389
            elif alexisgridwear == True:
                show 12pm003agiloalelove2:
                    xpos 1093
                    ypos 389
            else:
                show 12pm003agiloalenormal:
                    xpos 1093
                    ypos 389
            ls "You bought me flowers. That's so nice [pov]! Thank you!"
            mom "What a nice idea!"
            pov "You're welcome."
        else:
            scene diningroom 12pm 003agilored
            if nicolereddresswear == True:
                show 12pm003agiloniccorruption1:
                    xpos 327
                    ypos 346
            elif nicolebabydollwear == True:
                show 12pm003agiloniccorruption2:
                    xpos 327
                    ypos 346
            elif nicolesweaterpantswear == True:
                show 12pm003agiloniclove1:
                    xpos 327
                    ypos 346
            elif nicolerobewear == True:
                show 12pm003agiloniclove2:
                    xpos 327
                    ypos 346
            else:
                show 12pm003agilonicnormal:
                    xpos 327
                    ypos 346
            if alexisrockerwear == True:
                show 12pm003agiloredalecorruption1:
                    xpos 1119
                    ypos 406
            elif alexislingeriewear == True:
                show 12pm003agiloredalecorruption2:
                    xpos 1119
                    ypos 406
            elif alexisjeansskirtwear == True:
                show 12pm003agiloredalelove1:
                    xpos 1119
                    ypos 406
            elif alexisgridwear == True:
                show 12pm003agiloredalelove2:
                    xpos 1119
                    ypos 406
            else:
                show 12pm003agiloredalenormal:
                    xpos 1119
                    ypos 406
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
            scene diningroom 12pm 003agico
            if nicolereddresswear == True:
                show 12pm003agiconiccorruption1:
                    xpos 285
                    ypos 313
            elif nicolebabydollwear == True:
                show 12pm003agiconiccorruption2:
                    xpos 285
                    ypos 313
            elif nicolesweaterpantswear == True:
                show 12pm003agiconiclove1:
                    xpos 285
                    ypos 313
            elif nicolerobewear == True:
                show 12pm003agiconiclove2:
                    xpos 285
                    ypos 313
            else:
                show 12pm003agiconicnormal:
                    xpos 285
                    ypos 313
            if alexisrockerwear == True:
                show 12pm003agicoalecorruption1:
                    xpos 1160
                    ypos 379
            elif alexislingeriewear == True:
                show 12pm003agicoalecorruption2:
                    xpos 1160
                    ypos 379
            elif alexisjeansskirtwear == True:
                show 12pm003agicoalelove1:
                    xpos 1160
                    ypos 379
            elif alexisgridwear == True:
                show 12pm003agicoalelove2:
                    xpos 1160
                    ypos 379
            else:
                show 12pm003agicoalenormal:
                    xpos 1160
                    ypos 379
            ls "You bought me condoms?"
            ls "But..."
            mom "You did what...?"
            bs "<giggle>"
            pov "Yes, you'll need them soon!"
            ls "Oh... thank you..."
            mom "I don't think so."
            pov "You're welcome."
        else:
            scene diningroom 12pm 003agicored
            if nicolereddresswear == True:
                show 12pm003agiconiccorruption1:
                    xpos 285
                    ypos 313
            elif nicolebabydollwear == True:
                show 12pm003agiconiccorruption2:
                    xpos 285
                    ypos 313
            elif nicolesweaterpantswear == True:
                show 12pm003agiconiclove1:
                    xpos 285
                    ypos 313
            elif nicolerobewear == True:
                show 12pm003agiconiclove2:
                    xpos 285
                    ypos 313
            else:
                show 12pm003agiconicnormal:
                    xpos 285
                    ypos 313
            if alexisrockerwear == True:
                show 12pm003agicoalecorruption1:
                    xpos 1160
                    ypos 378
            elif alexislingeriewear == True:
                show 12pm003agicoalecorruption2:
                    xpos 1160
                    ypos 378
            elif alexisjeansskirtwear == True:
                show 12pm003agicoalelove1:
                    xpos 1160
                    ypos 378
            elif alexisgridwear == True:
                show 12pm003agicoalelove2:
                    xpos 1160
                    ypos 378
            else:
                show 12pm003agicoalenormal:
                    xpos 1160
                    ypos 378
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
            scene diningroom 12pm 003agilo
            if nicolereddresswear == True:
                show 12pm003agiloniccorruption1:
                    xpos 327
                    ypos 346
            elif nicolebabydollwear == True:
                show 12pm003agiloniccorruption2:
                    xpos 327
                    ypos 346
            elif nicolesweaterpantswear == True:
                show 12pm003agiloniclove1:
                    xpos 327
                    ypos 346
            elif nicolerobewear == True:
                show 12pm003agiloniclove2:
                    xpos 327
                    ypos 346
            else:
                show 12pm003agilonicnormal:
                    xpos 327
                    ypos 346
            if alexisrockerwear == True:
                show 12pm003agiloalecorruption1:
                    xpos 1093
                    ypos 389
            elif alexislingeriewear == True:
                show 12pm003agiloalecorruption2:
                    xpos 1093
                    ypos 389
            elif alexisjeansskirtwear == True:
                show 12pm003agiloalelove1:
                    xpos 1093
                    ypos 389
            elif alexisgridwear == True:
                show 12pm003agiloalelove2:
                    xpos 1093
                    ypos 389
            else:
                show 12pm003agiloalenormal:
                    xpos 1093
                    ypos 389
            ls "You bought me chocolate. That's so nice [pov]! Thank you!"
            mom "Haha, but no eating it now!"
            pov "You're welcome."
        else:
            scene diningroom 12pm 003agilored
            if nicolereddresswear == True:
                show 12pm003agiloniccorruption1:
                    xpos 327
                    ypos 346
            elif nicolebabydollwear == True:
                show 12pm003agiloniccorruption2:
                    xpos 327
                    ypos 346
            elif nicolesweaterpantswear == True:
                show 12pm003agiloniclove1:
                    xpos 327
                    ypos 346
            elif nicolerobewear == True:
                show 12pm003agiloniclove2:
                    xpos 327
                    ypos 346
            else:
                show 12pm003agilonicnormal:
                    xpos 327
                    ypos 346
            if alexisrockerwear == True:
                show 12pm003agiloredalecorruption1:
                    xpos 1119
                    ypos 406
            elif alexislingeriewear == True:
                show 12pm003agiloredalecorruption2:
                    xpos 1119
                    ypos 406
            elif alexisjeansskirtwear == True:
                show 12pm003agiloredalelove1:
                    xpos 1119
                    ypos 406
            elif alexisgridwear == True:
                show 12pm003agiloredalelove2:
                    xpos 1119
                    ypos 406
            else:
                show 12pm003agiloredalenormal:
                    xpos 1119
                    ypos 406
            ls "Oh you bought me chocolate. Thanks."
            mom "Haha, but no eating it now!"
            pov "You're welcome."
        $ lilsisrelationship += 5
    jump droom12gift

label ls12pmgiftrw:
    $ alexisrocker = 3
    scene diningroom 12pm 003agico
    show 12pm003agicoalenormal:
        xpos 1160
        ypos 379
    if nicolereddresswear == True:
        show 12pm003agiconiccorruption1:
            xpos 285
            ypos 313
    elif nicolebabydollwear == True:
        show 12pm003agiconiccorruption2:
            xpos 285
            ypos 313
    elif nicolesweaterpantswear == True:
        show 12pm003agiconiclove1:
            xpos 285
            ypos 313
    elif nicolerobewear == True:
        show 12pm003agiconiclove2:
            xpos 285
            ypos 313
    else:
        show 12pm003agiconicnormal:
            xpos 285
            ypos 313
    ls "You bought me this?"
    ls "But..."
    mom "Ohh..."
    bs "<giggle>"
    ls "Can we talk later?"
    pov "Of course."
    jump droom12gift

label ls12pmgiftli:
    $ alexislingerie = 3
    if alexisrockerwear == True:
        scene diningroom 12pm 003agico
        show 12pm003agicoalecorruption1:
            xpos 1160
            ypos 379
        if nicolereddresswear == True:
            show 12pm003agiconiccorruption1:
                xpos 285
                ypos 313
        elif nicolebabydollwear == True:
            show 12pm003agiconiccorruption2:
                xpos 285
                ypos 313
        elif nicolesweaterpantswear == True:
            show 12pm003agiconiclove1:
                xpos 285
                ypos 313
        elif nicolerobewear == True:
            show 12pm003agiconiclove2:
                xpos 285
                ypos 313
        else:
            show 12pm003agiconicnormal:
                xpos 285
                ypos 313
    else:
        scene diningroom 12pm 003agico
        show 12pm003agicoalenormal:
            xpos 1160
            ypos 379
        if nicolereddresswear == True:
            show 12pm003agiconiccorruption1:
                xpos 285
                ypos 313
        elif nicolebabydollwear == True:
            show 12pm003agiconiccorruption2:
                xpos 285
                ypos 313
        elif nicolesweaterpantswear == True:
            show 12pm003agiconiclove1:
                xpos 285
                ypos 313
        elif nicolerobewear == True:
            show 12pm003agiconiclove2:
                xpos 285
                ypos 313
        else:
            show 12pm003agiconicnormal:
                xpos 285
                ypos 313
    ls "You bought me this?"
    ls "But..."
    mom "Ohh..."
    bs "<giggle>"
    ls "Can we talk later?"
    pov "Of course."
    jump droom12gift

label ls12pmgiftjs:
    $ alexisjeansskirt = 3
    scene diningroom 12pm 003agilo
    show 12pm003agiloalenormal:
        xpos 1093
        ypos 389
    if nicolereddresswear == True:
        show 12pm003agiloniccorruption1:
            xpos 327
            ypos 346
    elif nicolebabydollwear == True:
        show 12pm003agiloniccorruption2:
            xpos 327
            ypos 346
    elif nicolesweaterpantswear == True:
        show 12pm003agiloniclove1:
            xpos 327
            ypos 346
    elif nicolerobewear == True:
        show 12pm003agiloniclove2:
            xpos 327
            ypos 346
    else:
        show 12pm003agilonicnormal:
            xpos 285
            ypos 346
    ls "You bought me this?"
    ls "But..."
    mom "Ohh..."
    bs "<giggle>"
    ls "Can we talk later?"
    pov "Of course."
    jump droom12gift

label ls12pmgiftgr:
    $ alexisgrid = 3
    if alexisjeansskirtwear == True:
        scene diningroom 12pm 003agilo
        show 12pm003agiloalelove1:
            xpos 1093
            ypos 389
        if nicolereddresswear == True:
            show 12pm003agiloniccorruption1:
                xpos 327
                ypos 346
        elif nicolebabydollwear == True:
            show 12pm003agiloniccorruption2:
                xpos 327
                ypos 346
        elif nicolesweaterpantswear == True:
            show 12pm003agiloniclove1:
                xpos 327
                ypos 346
        elif nicolerobewear == True:
            show 12pm003agiloniclove2:
                xpos 327
                ypos 346
        else:
            show 12pm003agilonicnormal:
                xpos 327
                ypos 346
    else:
        scene diningroom 12pm 003agilo
        show 12pm003agiloalenormal:
            xpos 1093
            ypos 389
        if nicolereddresswear == True:
            show 12pm003agiloniccorruption1:
                xpos 327
                ypos 346
        elif nicolebabydollwear == True:
            show 12pm003agiloniccorruption2:
                xpos 327
                ypos 346
        elif nicolesweaterpantswear == True:
            show 12pm003agiloniclove1:
                xpos 327
                ypos 346
        elif nicolerobewear == True:
            show 12pm003agiloniclove2:
                xpos 327
                ypos 346
        else:
            show 12pm003agilonicnormal:
                xpos 327
                ypos 346
    ls "You bought me this?"
    ls "But..."
    mom "Ohh..."
    bs "<giggle>"
    ls "Can we talk later?"
    pov "Of course."
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
            if cassandraheartdresswear == True:
                show 12pm003cgilocascorruption1:
                    xpos 201
                    ypos 502
            elif cassandralingeriewear == True:
                show 12pm003cgilocascorruption2:
                    xpos 201
                    ypos 502
            elif cassandrajeanswear == True:
                show 12pm003cgilocaslove1:
                    xpos 201
                    ypos 502
            elif cassandrapajamawear == True:
                show 12pm003cgilocaslove2:
                    xpos 201
                    ypos 502
            else:
                show 12pm003cgilocasnormal:
                    xpos 201
                    ypos 502
            bs "You bought me flowers? That's a nice surprise! Thank you!"
            mom "See, he can be nice to you too."
            ls "That must be a mistake, haha."
            pov "You're welcome."
        else:
            scene diningroom 12pm 003cgilored
            if cassandraheartdresswear == True:
                show 12pm003cgilocascorruption1:
                    xpos 201
                    ypos 502
            elif cassandralingeriewear == True:
                show 12pm003cgilocascorruption2:
                    xpos 201
                    ypos 502
            elif cassandrajeanswear == True:
                show 12pm003cgilocaslove1:
                    xpos 201
                    ypos 502
            elif cassandrapajamawear == True:
                show 12pm003cgilocaslove2:
                    xpos 201
                    ypos 502
            else:
                show 12pm003cgilocasnormal:
                    xpos 201
                    ypos 502
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
            if cassandraheartdresswear == True:
                show 12pm003cgicocascorruption1:
                    xpos 193
                    ypos 469
            elif cassandralingeriewear == True:
                show 12pm003cgicocascorruption2:
                    xpos 193
                    ypos 469
            elif cassandrajeanswear == True:
                show 12pm003cgicocaslove1:
                    xpos 193
                    ypos 469
            elif cassandrapajamawear == True:
                show 12pm003cgicocaslove2:
                    xpos 193
                    ypos 469
            else:
                show 12pm003cgicocasnormal:
                    xpos 193
                    ypos 469
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
            if cassandraheartdresswear == True:
                show 12pm003cgicocascorruption1:
                    xpos 193
                    ypos 469
            elif cassandralingeriewear == True:
                show 12pm003cgicocascorruption2:
                    xpos 193
                    ypos 469
            elif cassandrajeanswear == True:
                show 12pm003cgicocaslove1:
                    xpos 193
                    ypos 469
            elif cassandrapajamawear == True:
                show 12pm003cgicocaslove2:
                    xpos 193
                    ypos 469
            else:
                show 12pm003cgicocasnormal:
                    xpos 193
                    ypos 469
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
            if cassandraheartdresswear == True:
                show 12pm003cgilocascorruption1:
                    xpos 201
                    ypos 502
            elif cassandralingeriewear == True:
                show 12pm003cgilocascorruption2:
                    xpos 201
                    ypos 502
            elif cassandrajeanswear == True:
                show 12pm003cgilocaslove1:
                    xpos 201
                    ypos 502
            elif cassandrapajamawear == True:
                show 12pm003cgilocaslove2:
                    xpos 201
                    ypos 502
            else:
                show 12pm003cgilocasnormal:
                    xpos 201
                    ypos 502
            bs "You bought me chocolate. I don't think I can eat it. But thank you!"
            pov "You're welcome."
            ls "Can I have it?"
        else:
            scene diningroom 12pm 003cgilored
            if cassandraheartdresswear == True:
                show 12pm003cgilocascorruption1:
                    xpos 201
                    ypos 502
            elif cassandralingeriewear == True:
                show 12pm003cgilocascorruption2:
                    xpos 201
                    ypos 502
            elif cassandrajeanswear == True:
                show 12pm003cgilocaslove1:
                    xpos 201
                    ypos 502
            elif cassandrapajamawear == True:
                show 12pm003cgilocaslove2:
                    xpos 201
                    ypos 502
            else:
                show 12pm003cgilocasnormal:
                    xpos 201
                    ypos 502
            bs "You bought me chocolate. Hmm, thanks."
            pov "You're welcome."
            ls "Can I have it?"
        $ bigsisrelationship += 5
    jump droom12gift

label bs12pmgifthd:
    $ cassandraheartdress = 3
    scene diningroom 12pm 003cgico
    show 12pm003cgicocasnormal:
        xpos 193
        ypos 469
    bs "You bought me this?"
    bs "But..."
    mom "Ohh..."
    ls "<giggle>"
    bs "Can we talk later?"
    pov "Of course."
    jump droom12gift

label bs12pmgiftli:
    $ cassandralingerie = 3
    if cassandraheartdresswear == True:
        scene diningroom 12pm 003cgico
        show 12pm003cgicocascorruption1:
            xpos 193
            ypos 469
    else:
        scene diningroom 12pm 003cgico
        show 12pm003cgicocasnormal:
            xpos 193
            ypos 469
    bs "You bought me this?"
    bs "But..."
    mom "Ohh..."
    ls "<giggle>"
    bs "Can we talk later?"
    pov "Of course."
    jump droom12gift

label bs12pmgiftjs:
    $ cassandrajeans = 3
    scene diningroom 12pm 003cgilo
    show 12pm003cgilocasnormal:
        xpos 201
        ypos 502
    bs "You bought me this?"
    bs "But..."
    mom "Ohh..."
    ls "<giggle>"
    bs "Can we talk later?"
    pov "Of course."
    jump droom12gift

label bs12pmgiftpa:
    $ cassandrapajama = 3
    if cassandrajeanswear == True:
        scene diningroom 12pm 003cgilo
        show 12pm003cgilocaslove1:
            xpos 201
            ypos 502
    else:
        scene diningroom 12pm 003cgilo
        show 12pm003cgilocasnormal:
            xpos 201
            ypos 502
    bs "You bought me this?"
    bs "But..."
    mom "Ohh..."
    ls "<giggle>"
    bs "Can we talk later?"
    pov "Of course."
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