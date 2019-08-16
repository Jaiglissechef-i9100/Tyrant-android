#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 7pm Parent's Room - Alexis, Bruce, MC, Nicole - Love, Corruption
# 2. Basement - Bruce, Cassandra, David, MC, Miranda, Nicole - Love, Corruption, Twisted, Darker Paths
# 3. 7am Upstairs Shower - Alexis, MC - Love, Corrpution, Twisted
#----- End List -----

#----- Parent's Room - Confront Bruce Scenes ----- Done
label proom19extlanding:
    $ alexisaway = False
    call screen proom19extchoice

screen proom19extchoice:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('proom19extchoice'), Jump('proom19extlove')) hovered tt.Action ("Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('proom19extchoice'), Jump('proom19extcorruption')) hovered tt.Action ("Corruption [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- 7pm Parent's Room Event Corruption ----- Done
label proom19extcorruption:
    hide screen locations
    scene main parents room door
    $ proom19first = True
    $ proom19corsex = True
    povi "Huh? Why is the door closed?"
    "You hear someone talking inside."
    if inc == True:
        povi "That's mom and dad arguing."
    else:
        povi "That's [mother] and Bruce arguing."
    povi "Let's see what's going on."
    "You open the door."
    if nicolereddresswear == True:
        scene parentsroom 7pm 002cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 002cc2
    else:
        scene parentsroom 7pm 002c
    povi "What the hell is going on here?"
    dad "Come on, take your clothes off!"
    mom "But..."
    if nicolereddresswear == True:
        scene parentsroom 7pm 003cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 003cc2
    else:
        scene parentsroom 7pm 003c
    pov "What's going on here? Are you trying to fuck my slut?"
    dad "Leave us alone [pov]. That's not funny! Give us some privacy..."
    mom "But..."
    povi "Bruce knows that he isn't allowed to lay a hand on her, but [mother] is reacting so submissively."
    povi "Normally she would make a scene and tell him off now."
    povi "There's no way she became so submissive to him in this short of a time. But why is she acting like that?"
    if nicolereddresswear == True:
        scene parentsroom 7pm 004cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 004cc2
    else:
        scene parentsroom 7pm 004c
    dad "Did you hear me, [pov]. Get out of this room right now, I want to spend some time with my wife!"
    mom "Hnng..."
    povi "Wait a minute, I get it now. She's testing me. She wants to know if I'll stand up him for her."
    povi "She want's to see if she made the right choice in backing me instead of him."
    scene parentsroom 7pm 005c
    if inc == True:
        pov "I'm not going anywhere dad. The slut is mine now and you know that."
    else:
        pov "I'm not going anywhere Bruce. The slut is mine now and you know that."
    dad "Seriously? I endured your humiliation when you put on that little show for Davide. Even when things when way too far..."
    dad "But now we're alone and I want to my life back."
    pov "You don't understand. We're not putting on any shows now. I'm telling you that is how it is. She's mine."
    dad "No! She's still my wife."
    povi "Poor, sad little Bruce..."
    pov "She isn't your wife anymore. She's mine now. My slut. My plaything."
    mom "Hnng..."
    dad "You can't be..."
    scene parentsroom 7pm 006c
    "You watch the realization spread across his face."
    dad "You're serious!"
    dad "Are you crazy? You can't just steal my wife!"
    pov "I already have, and she's already decided that's all mine! Just mine!"
    pov "Now you'll be a good boy and play along. We wouldn't ever want Davide get to suspicious about your real intentions now, would we?"
    dad "You're... evil..."
    if nicolereddresswear == True:
        scene parentsroom 7pm 007cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 007cc2
    else:
        scene parentsroom 7pm 007c
    dad "We need to stop this now [mother]. He's gone mad."
    if inc == True:
        dad "He's your son and he wants to have you as his slut! Fucking you whenever he wants. It's not just to protect our cover."
    else:
        dad "He's your best friends son and he wants to have you as his slut! Fucking you whenever he wants. It's not just to protect our cover."
    dad "Say somethingm please! End this madness."
    mom "But..."
    mom "I'm his slut... His plaything."
    dad "..."
    povi "He's completely overwhelmed, hehe."
    "You both silently watch as he storms over to the door."
    scene parentsroom 7pm 008
    dad "You're crazy! Both of you! This isn't normal!"
    dad "I can't be here any longer! But this isn't over yet!"
    if nicolereddresswear == True:
        scene parentsroom 7pm 009cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 009cc2
    else:
        scene parentsroom 7pm 009c
    pov "You did good slut."
    if inc == True:
        pov "You see now that choosing me, your son, was the best choice? I'm in charge of now. And you're mine."
    else:
        pov "You see now that choosing me was the best choice? I'm in charge of now. And you're mine."
    pov "But from now on I want you to come straight to me if he tries something again. You understand, slut?"
    mom "Y... yes [pov]."
    pov "Good! Now get naked, I need to fuck my slut now!"
    mom "But... [ls] is in the kitchen, she'll hear us!"
    pov "You didn't get it?"
    pov "You chose me over your ex-husband..."
    if inc == True:
        pov "You're truly just mine now, mom!"
        pov "And if I want to fuck my moms brains out, and I'll do it whenever I want to!"
    else:
        pov "You're truly just mine now, [mother]!"
        pov "And if I want to fuck your brains out, and I'll do it whenever I want to!"
    pov "There's no reason to hide it anymore! Do you get it now?"
    mom "Yes... I'm all yours... Do as you please with me. Hnng!"
    "She strips her clothes waiting for your command."
    #call screen proom19extcor
    jump proom19extcorlanding

label proom19extcorlanding:
    call screen proom19extcor

screen proom19extcor():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('proom19extcor'), Jump('proom19extcorbj')) hovered tt.Action ("Then get on your knees") focus_mask True
        imagebutton auto "gui/icons/icon_sex_corruption_%s.png" action (Hide('proom19extcor'), Jump('proom19extcorsex')) hovered tt.Action ("Then crawl onto the bed") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('proom19extcor'), Jump('cornicoleweekendloveroot')) hovered tt.Action ("[lv1] to [cr1] Events") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('proom19extcor'), Jump('proom19extcorend')) hovered tt.Action ("Call it for now") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom19extcorbj:
    pov "I need to feel those lip around my cock now!"
    mom "Yes, [pov]."
    scene parentsroom 7pm 010cbj
    mom "<lick>"
    pov "Getting right to it with no complaint, good slut!"
    mom "<lick> Do... do you like it...?"
    if inc == True:
        pov "Yes, mom. I like your... enthusiasm."
    else:
        pov "Yes, [mother]. I like your... enthusiasm."
    pov "But just licking it is not going to be enough, understand?"
    mom "Yes."
    scene parentsroom 7pm 011cbj
    mom "Hmm... <suck>"
    pov "Very nice."
    mom "Hmm... hmm..."
    pov "That's a good girl, showing me what a great slut you are."
    mom "Hmm..."
    pov "Now put your hands behind your back and let me take control for a while."
    scene parentsroom 7pm 012cbjdt
    mom "Hnng..."
    pov "Good. You're mine to use and play with."
    pov "Be a good slut now and relax."
    mom "Hmm..."
    pov "Oh and breathe in..."
    "She realizes what you're about to do and breathes in quickly through her nose."
    scene parentsroom 7pm 014cbjdt
    mom "HNNG...!"
    pov "That's it... hold it."
    if inc == True:
        pov "Let your son's big dick slide down your throat."
    else:
        pov "Let that big dick slide down your throat."
    pov "Don't worry, I'll take good care of you."
    mom "Hnng..."
    pov "Hold it! Just a bit longer, you're MY slut!"
    mom "<choke>HNNG...!"
    scene parentsroom 7pm 013cbjdt
    mom "<choke> HRRRG...!"
    if inc == True:
        pov "What a great reward for raising me, don't you think?"
    else:
        pov "What a great reward for taking me in, don't you think?"
    pov "And you don't need to worry, I'll protect you. You're my property after all!"
    mom "<choke> HNNN...!"
    scene parentsroom 7pm 012cbjdt
    mom "Hnn... hnn..."
    pov "You did good. You didn't even try to pull away once."
    if inc == True:
        pov "I'm proud of you, mom!"
    else:
        pov "I'm proud of you, [mother]!"
    pov "And now I have another reward for you, I'm ready to cum."
    pov "You're a very good cocksucker!"
    call screen proom19extbjcum

screen proom19extbjcum():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('proom19extbjcum'), Jump('proom19extbjcumin')) hovered tt.Action ("Have her swallow") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('proom19extbjcum'), Jump('proom19extbjcumout')) hovered tt.Action ("Cover her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom19extbjcumin:
    pov "Take it and swallow it all down!"
    mom "Hm... hm..."
    scene parentsroom 7pm 015cbjdt
    pov "Yes! Swallow my seed, slut!"
    "You cum in her mouth."
    mom "<gulp> <gulp>"
    pov "Hnng..."
    scene parentsroom 7pm 019cbj
    mom "Aaah..."
    pov "Good girl. Showing me that you swallowed it all."
    scene parentsroom 7pm 018cbj
    pov "We'll have much more fun together, me training you."
    if inc == True:
        pov "Until you'll become the perfect slut, mom."
    else:
        pov "Until you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'll go now, get yourself ready, maybe we'll have more fun in the basement later."
    mom "Yes, [pov]."
    #scene black
    #"You leave her."
    #$ dtime += 1
    #jump parentsroom
    jump proom19extcorlanding

label proom19extbjcumout:
    pov "Prepare yourself and receive my seed!"
    mom "Hm... hm..."
    scene parentsroom 7pm 016cbjdt
    pov "Yes! Receive it, slut!"
    mom "Hmm..."
    pov "Hnng..."
    scene parentsroom 7pm 017cbjdt
    mom "Hnng..."
    pov "Good girl. Presenting me my handiwork."
    pov "We'll have much more fun together, me training you."
    if inc == True:
        pov "Until you'll become the perfect slut, mom."
    else:
        pov "Until you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'll go now, get yourself ready, maybe we'll have more fun in the basement later."
    mom "Yes, [pov]."
    #scene black
    #"You leave her."
    #$ dtime += 1
    #jump parentsroom
    jump proom19extcorlanding

label proom19extcorsex:
    pov "You need to get a good pounding."
    mom "Yes, [pov]."
    scene parentsroom 7pm 010cdg
    pov "Very good, seeing you on all fours, presenting your holes to me."
    mom "Do... do you like it...?"
    if inc == True:
        pov "Yes, mom. I like your motivation."
    else:
        pov "Yes, [mother]. I like your motivation."
    pov "But which hole should I pound? Do you prefer one, slut?"
    mom "N...no, use me as you please..."
    pov "Good answer."
    call screen proom19extfuck

screen proom19extfuck():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_sex_corruption_%s.png" action (Hide('proom19extfuck'), Jump('proom19extfuckp')) hovered tt.Action ("I'll fuck your pussy") focus_mask True
        imagebutton auto "gui/icons/icon_rub_corruption_%s.png" action (Hide('proom19extfuck'), Jump('proom19extfucka')) hovered tt.Action ("I'll fuck your ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom19extfucka:
    $ proom19fuckass = True
    jump proom19extfuckp

label proom19extfuckp:
    if proom19fuckass == True:
        scene parentsroom 7pm 011cdg
        mom "Hnnng..."
        pov "Do you like how my big dick feels against your tight hole?"
    else:
        scene parentsroom 7pm 011cdgp
        mom "Hnnng..."
        pov "Do you like how my big dick feels against your wet pussy?"
    mom "Yes..."
    pov "You push your dick slowly inside her."
    if proom19fuckass == True:
        scene parentsroom 7pm 013cdg
    else:
        scene parentsroom 7pm 013cdgp
    pov "Don't worry, I might be starting slowly, but you're still going to get that hard pounding my slut needs."
    mom "Hmm..."
    pov "That is what you want right? I need you to say it..."
    mom "Hnn..."
    scene parentsroom 7pm 012cdg
    with vpunch
    mom "Aaah..."
    "You push hard and deep in her."
    pov "I asked you something, slut!"
    mom "Yes... I... need a hard pounding."
    pov "Good. You're going to love this."
    "You start to fuck her hard and rough."
    if proom19fuckass == True:
        scene parentsroom 7pm 014cdg
    else:
        scene parentsroom 7pm 014cdgp
    mom "Ahhh... hah..."
    mom "You're so deep inside me!"
    if proom19fuckass == True:
        pov "Your ass really needs a good pounding!"
    else:
        pov "Your pussy really needs a good pounding!"
    mom "Hah... aahh..."
    "Knock! Knock!"
    mom "Huh?"
    ls "Mom?"
    pov "<whisper> Damn, what is she doing here? If we want to keep going you need to do something."
    mom "<whisper> Okay. I'll take care of it."
    scene parentsroom 7pm 015
    ls "Mom, you're naked?"
    mom "Yes... I..."
    mom "What do you need, honey?"
    if proom19fuckass == True:
        scene parentsroom 7pm 016a
        povi "Damn, her asshole is still gaping. I can't wait to get my dick back in there."
    ls "I heard sounds like you having sex with someone, but Dad left the house earlier."
    mom "Oh... I... that was me."
    ls "You?"
    mom "I... I needed to take care of my... urges."
    ls "What...? What do you mean?"
    mom "Mommy was playing with herself..."
    ls "Playing...?"
    scene parentsroom 7pm 016
    ls "UGH! Don't tell me that mom!"
    mom "But..."
    ls "Seriously, overshare much? Ugh!"
    scene parentsroom 7pm 017c
    pov "Good thinking. She not going to interupt us again anytime soon."
    pov "I think its time to pound you even harder until you're begging for my cum!"
    pov "Now get back over here slut!"
    mom "Yes [pov]."
    if proom19fuckass == True:
        scene parentsroom 7pm 014cdg
        with vpunch
    else:
        scene parentsroom 7pm 014cdgp
        with vpunch
    "You continue to fuck her again, going even harder this time."
    mom "AAHHH...HAH..."
    with vpunch
    pov "That's the way I like it. My slut letting it all out as I fuck her hard!"
    mom "HAH... AHH!"
    with vpunch
    scene parentsroom 7pm 012cdg
    pov "You're getting tighter and starting to shake. Are you about to cum already?"
    mom "Yes [pov]. I'm so close, please can I cum?"
    pov "Not yet! You need to hold it for a little longer."
    mom "I...I'll try..."
    pov "You're a good slut, submitting without any back talk."
    mom "Yes, I submit myself to you!"
    if inc == True:
        pov "You raised me to become this, now you'll get your reward."
    else:
        pov "You cared for me when was I younger. You helped me become this, now you'll get your reward."
    pov "And don't worry, I'll protect you. Because you're my property!"
    mom "AAHH... HAH... PLEASE... LET ME CUM!"
    pov "Come here!"
    scene parentsroom 7pm 017cdg
    mom "AHHH... HAH..."
    with vpunch
    pov "You'll need to submit even more if you really want to cum!"
    with vpunch
    mom "I will!"
    if inc == True:
        pov "You're gonna love cumming on your son's dick!"
        with vpunch
        mom "Yes...!"
        pov "You're a bad mother, craving your son's dick like this!"
        with vpunch
        mom "Yes! I'm bad. I'm so bad! I'm a dirty slut for my son! I love it when he uses me!"
    else:
        pov "You're gonna love cumming on your my dick!"
        with vpunch
        mom "Yes...!"
        pov "You're a bad friend, craving your best friend's son. Craving his dick like this!"
        with vpunch
        mom "Yes! I'm bad. I'm so bad! I'm a dirty slut for you! I love it when you use me!"
    pov "You're allowed to cum now slut!"
    scene parentsroom 7pm 015cdg
    with vpunch
    mom "AHHHH... YEEEES!!!"
    "She cums hard on your dick, deep inside her."
    pov "Oh, you slut! I love it! You're pushing me over the edge too!"
    call screen proom19extfuckcum

screen proom19extfuckcum():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        if proom19fuckass == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom19extfuckcum'), Jump('proom19extfuckcumassin')) hovered tt.Action ("I'll cum inside your ass") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom19extfuckcum'), Jump('proom19extfuckcumassout')) hovered tt.Action ("I'll cum on your ass") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom19extfuckcum'), Jump('proom19extfuckcumpin')) hovered tt.Action ("I'll cum inside your pussy") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom19extfuckcum'), Jump('proom19extfuckcumpout')) hovered tt.Action ("I'll cum on your ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom19extfuckcumassin:
    scene parentsroom 7pm 016cdg
    pov "Ahhh... yes...!"
    with vpunch
    "You spray cum inside her asshole."
    mom "Ahhh... so hot..."
    pov "Ahngh! I'm going to drain every last drop inside you!"
    with vpunch
    mom "Hah... hah..."
    scene parentsroom 7pm 020cdg
    pov "Oh hell ya, there's so much inside you now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your hot ass milked my balls dry, mom!"
    else:
        pov "Your hot ass milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 021cdg
    "She falls, exhausted, onto the bed."
    pov "That was a very good fuck, slut. Just the way I like it."
    pov "We'll have much more fun together now. With me training you..."
    if inc == True:
        pov "Soon, you'll become the perfect slut, mom."
    else:
        pov "Soon, you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'm going now, but get yourself ready. We'll probably be having even more fun in the basement later."
    mom "Yes, [pov]."
    #scene black
    #"You leave her."
    $ proom19fuckass = False
    #$ dtime += 1
    #jump parentsroom
    jump proom19extcorlanding

label proom19extfuckcumassout:
    scene parentsroom 7pm 018cdg
    pov "Ahhh... yes...!"
    with vpunch
    "You spray cum all over her ass."
    mom "Ahhh... so hot..."
    pov "Ahngh! I'm going to drain every last drop on you!"
    with vpunch
    mom "Hah... hah..."
    scene parentsroom 7pm 019cdg
    pov "Oh hell ya, there's so much on you now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your hot ass milked my balls dry, mom!"
    else:
        pov "Your hot ass milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 022cdg
    "She falls, exhausted, onto the bed."
    pov "That was a very good fuck, slut. Just the way I like it."
    pov "We'll have much more fun together now. With me training you..."
    if inc == True:
        pov "Soon, you'll become the perfect slut, mom."
    else:
        pov "Soon, you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'm going now, but get yourself ready. We'll probably be having even more fun in the basement later."
    mom "Yes, [pov]."
    #scene black
    #"You leave her."
    $ proom19fuckass = False
    #$ dtime += 1
    #jump parentsroom
    jump proom19extcorlanding

label proom19extfuckcumpin:
    scene parentsroom 7pm 016cdgp
    pov "Ahhh... yes...!"
    with vpunch
    "You spray cum inside her pussy."
    mom "Ahhh... so hot..."
    pov "Ahngh! I'm going to drain every last drop inside you!"
    with vpunch
    mom "Hah... hah..."
    scene parentsroom 7pm 020cdgp
    pov "Oh hell ya, there's so much inside you now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your tight pussy milked my balls dry, mom!"
    else:
        pov "Your tight pussy milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 021cdgp
    "She falls, exhausted, onto the bed."
    pov "That was a very good fuck, slut. Just the way I like it."
    pov "We'll have much more fun together now. With me training you..."
    if inc == True:
        pov "Soon, you'll become the perfect slut, mom."
    else:
        pov "Soon, you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'm going now, but get yourself ready. We'll probably be having even more fun in the basement later."
    mom "Yes, [pov]."
    #scene black
    #"You leave her."
    $ proom19fuckass = False
    #$ dtime += 1
    #jump parentsroom
    jump proom19extcorlanding

label proom19extfuckcumpout:
    scene parentsroom 7pm 018cdgp
    pov "Ahhh... yes...!"
    with vpunch
    "You spray cum all over her ass."
    mom "Ahhh... so hot..."
    pov "Ahngh! I'm going to drain every last drop on you!"
    with vpunch
    mom "Hah... hah..."
    scene parentsroom 7pm 019cdgp
    pov "Oh hell ya, there's so much on your ass now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your tight pussy milked my balls dry, mom!"
    else:
        pov "Your tight pussy milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 022cdgp
    "She falls, exhausted, onto the bed."
    pov "That was a very good fuck, slut. Just the way I like it."
    pov "We'll have much more fun together now. With me training you..."
    if inc == True:
        pov "Soon, you'll become the perfect slut, mom."
    else:
        pov "Soon, you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'm going now, but get yourself ready. We'll probably be having even more fun in the basement later."
    mom "Yes, [pov]."
    #scene black
    #"You leave her."
    $ proom19fuckass = False
    #$ dtime += 1
    #jump parentsroom
    jump proom19extcorlanding

label proom19extcorend:
    scene black
    "You two finish up and get ready for tonight."
    $ proom19corsex = False
    $ dtime += 1
    jump parentsroom

#----- 7pm Parent's Room Event Love ----- Done
label proom19extlove:
    hide screen locations
    $ proom19first = True
    $ proom19lovesex = True
    scene main parents room door
    povi "Huh? Why is the door closed?"
    "You hear someone talking inside."
    if inc == True:
        povi "That's mom and dad arguing."
    else:
        povi "That's [mother] and Bruce arguing."
    povi "Let's see what's going on."
    "You open the door."
    if nicolesweaterpantswear == True:
        scene parentsroom 7pm 002cl1
    elif nicolerobewear == True:
        scene parentsroom 7pm 002cl2
    else:
        scene parentsroom 7pm 002l
    povi "What the hell is going on here?"
    dad "Come on, take your clothes off!"
    mom "I told you to leave me alone!"
    pov "What's going on here?"
    if nicolesweaterpantswear == True:
        scene parentsroom 7pm 003cl1
    elif nicolerobewear == True:
        scene parentsroom 7pm 003cl2
    else:
        scene parentsroom 7pm 003l
    mom "That idiot thinks he can lay his hands on me."
    dad "She's being unreasonable. She sticking to that little show of her's you two put on for our cover."
    pov "Little show?"
    mom "He still doen't get it. I'm never sleeping with him again."
    if nicolesweaterpantswear == True:
        scene parentsroom 7pm 004cl1
    elif nicolerobewear == True:
        scene parentsroom 7pm 004cl2
    else:
        scene parentsroom 7pm 004l
    dad "Come one, you can stop playing around! I know that little show she gave you in the basement to impress Davide as just a farce."
    povi "So he thinks that was all just a show and he can go back to normal when Davide is not around?"
    dad "Tell her [pov]. I have no idea what's gotten into her. She thinks you're in love with her, as in sexually."
    dad "And all that business about her she's saying she wants to be your slut, that was going too far!"
    scene parentsroom 7pm 005c
    pov "Look, that was just for show."
    dad "Good, I knew it..."
    if inc == True:
        pov "But, I'm not done yet dad."
    else:
        pov "But, I'm not done yet Bruce."
    pov "She'll never be my \"slut\", I love her too much for that."
    dad "That's what I was saying."
    if inc == True:
        dad "You love her like a son would and should love his mother."
    else:
        dad "You love her as friend and there's nothing sexually about it."
    pov "No... that is not what I was saying. What we have is sexual and so much more."
    pov "She's my lover, and I'm certain I'll be a much better husband for her than you ever were."
    dad "But she's my wife!"
    povi "It's time to make him understand that he's lost her. Poor, dumb Bruce..."
    pov "No, she isn't your wife anymore. She's mine now. Forever."
    scene parentsroom 7pm 006c
    dad "You can't be..."
    dad "You're serious. Are you mad? You can't just steal my wife!"
    pov "I already did. She's with me now and you need to respect that."
    pov "You're going to accept thing and act accordingly. We don't Davide to get suspicious, do we?"
    dad "You're... evil..."
    if nicolesweaterpantswear == True:
        scene parentsroom 7pm 007cl1
    elif nicolerobewear == True:
        scene parentsroom 7pm 007cl2
    else:
        scene parentsroom 7pm 007l
    dad "We need to stop this now [mother]. He's gone mad."
    if inc == True:
        dad "He's your son and he wants to be your lover. This is well beyond what we needed for our cover. This is going way too far!"
    else:
        dad "He's your best friend's son and he wants to be your lover. This is well beyond what we needed for our cover. This is going way too far!"
    dad "You tell him he's crazy! End this madness."
    mom "Stop talking Bruce!"
    if inc == True:
        mom "You won't talk like that about my son anymore!"
    else:
        mom "You won't talk like that about him anymore!"
    mom "I made my decision and you'll respect it, or I'll never forgive you!"
    dad "..."
    scene parentsroom 7pm 008
    dad "You're both crazy! This isn't normal!"
    dad "I'm out of here, but this isn't over yet!"
    scene parentsroom 7pm 009l
    mom "So... he's gone now and it's just the us left."
    povi "What the fu... How did she get naked that quick?"
    mom "How about we spend some time together now, as lovers?"
    pov "[ls] is in in the kitchen still. Might be a bit risky..."
    mom "Wthi was usually the time I was with Bruce before. She'll probably think it's just like all the times before."
    mom "You wouldn't want to leave me unsatisfied, right?"
    if inc == True:
        pov "Hell no, mom. If you need me now, then I won't let you down."
    else:
        pov "Hell no, [mother]. If you need me now, then I won't let you down."
    mom "<giggle> You won't regret it."
    scene weekend 8pm 016lb
    mom "What are you waiting for?"
    "You undress in a matter of seconds."
    mom "<giggle>"
    jump proom19extlovelanding
    #jump nicoleweekendloveroot - Old version

#----- 7pm Parent's Room Event Alexis Interupt Event Love ----- Done
label proom19extlovealexis:
    "Knock! Knock!"
    mom "Huh?"
    ls "Mom?"
    pov "<whisper> Damn, what is she doing here? Do you want me to hide?"
    mom "<whisper> Don't worry. I'll send her away."
    scene parentsroom 7pm 015
    ls "Mom, you're naked?"
    mom "Yes... I'm naked."
    mom "What do you need, honey?"
    ls "I heard sounds like you having sex with someone, but Dad left the house earlier."
    mom "Oh... that was me."
    ls "You?"
    mom "I'm having some fun."
    ls "Fun...? What do you mean?"
    mom "Mommy was playing with herself..."
    ls "Playing...?"
    scene parentsroom 7pm 016
    ls "UGH! Don't tell me that mom!"
    mom "But..."
    ls "There is such a thing as overshare, ugh!"
    scene parentsroom 7pm 017l
    mom "I don't think she'll bother us again."
    pov "Haha, I doubt she'll want to come near this room ever again after that!"
    mom "I need more of you right now!"
    pov "Oh yes, you do, haha."
    $ alexissuspicous = 0
    $ alexisaway = True
    jump proom19extlovelanding
    #jump nicoleweekendloveroot - Old version

label proom19extloveend:
    scene weekend 8pm 046l
    pov "Let's rest a moment, that was awesome."
    mom "I'm so proud of you, [pov]."
    pov "I'm proud of you too."
    mom "And now we can really be together, for real."
    if inc == True:
        pov "I'll alway be yours, mom."
    else:
        pov "I'll alway be yours, [mother]."
    $ proom19lovesex = False
    $ proom19extlovefirst = True
    $ dtime += 1
    jump parentsroom

#----- Custom Corruption to Love Landing Menu ----- Done
label proom19extlovelanding:
    call screen proom19extlovemenu

screen proom19extlovemenu():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('proom19extlovemenu'), Jump('nicoleweekendloveroot')) hovered tt.Action ("Love Options [lv1]") focus_mask True
        imagebutton auto "edited/gui/vice/icon_corruption_%s.png" action (Hide('proom19extlovemenu'), Jump('proom19extcorstartlove')) hovered tt.Action ("Coruption to Love Options [cr1]to[lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('proom19extlovemenu'), Jump('proom19extloveend')) hovered tt.Action ("Call it for the day") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom 7pm Parent's Room Events Twisted Paths ----- Done
#----- Custom Corruption version of Love Event Alexis Interupt ----- Done
label proom19extlovealexiscor:
    "Knock! Knock!"
    mom "Huh?"
    ls "Mom?"
    pov "<whisper> Damn, what is she doing here? Do you want me to hide?"
    mom "<whisper> Don't worry. I'll send her away."
    scene parentsroom 7pm 015
    ls "Mom, you're naked?"
    mom "Yes... I'm naked."
    mom "What do you need, honey?"
    ls "I heard sounds like you having sex with someone, but Dad left the house earlier."
    mom "Oh... that was me."
    ls "You?"
    mom "I'm having some fun."
    ls "Fun...? What do you mean?"
    mom "Mommy was playing with herself..."
    ls "Playing...?"
    scene parentsroom 7pm 016
    ls "UGH! Don't tell me that mom!"
    mom "But..."
    ls "There is such a thing as overshare, ugh!"
    scene parentsroom 7pm 017l
    mom "I don't think she'll bother us again."
    pov "Haha, I doubt she'll want to come near this room ever again after that!"
    mom "I need more of you right now!"
    pov "Oh yes, you do, haha."
    $ alexissuspicous = 0
    $ alexisaway = True
    jump proom19extlovelanding

#----- Custom Corruption version of Love event Nicole----- Done
label proom19extloveendcor:
    $ proom19corsex = False
    $ proom19extlovefirst = True
    $ dtime += 1
    jump parentsroom

#----- Custom Love version of Corruption event ----- Done
label proom19extcorstartlove: #added corruption to love options
    call screen proom19extcorlove

screen proom19extcorlove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "edited/gui/vice/icon_blowjob_corruption_%s.png" action (Hide('proom19extcorlove'), Jump('proom19extcorbjlove')) hovered tt.Action ("Then get on your knees") focus_mask True
        imagebutton auto "edited/gui/vice/icon_sex_corruption_%s.png" action (Hide('proom19extcorlove'), Jump('proom19extcorsexlove')) hovered tt.Action ("Then crawl onto the bed") focus_mask True
        imagebutton auto "gui/icons/icon_skip1_%s.png" action (Hide('proom19extcorlove'), Jump('proom19extlovelanding')) hovered tt.Action ("Return to previous menu") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom19extcorbjlove:
    pov "I want to feel those lip around my cock!"
    mom "Gladly, [pov]."
    scene parentsroom 7pm 010cbj
    mom "<lick>"
    pov "Hmmm..."
    mom "<lick> Do... do you like it...?"
    if inc == True:
        pov "Yes, mom. I do."
    else:
        pov "Yes, [mother]. I do."
    mom "Then you're really going to like this."
    scene parentsroom 7pm 011cbj
    mom "Hmm... <suck>"
    pov "Very nice."
    mom "Hmm... hmm..."
    pov "That's a good girl."
    mom "Hmm..."
    "She puts her hands behind her back and looks up at your expectingly. You take that as you cue to hold the sides of her head."
    scene parentsroom 7pm 012cbjdt
    mom "Hnng..."
    pov "Do you want me to control how fast you do it?"
    mom "Mmhm..."
    pov "Ok then, take a deep breathe..."
    "She realizes what you're about to do and breathes in quickly through her nose."
    scene parentsroom 7pm 014cbjdt
    mom "HNNG...!"
    pov "That's... yeah... just hold it."
    if inc == True:
        pov "Your son's big dick is sliding down your throat."
    else:
        pov "My big dick is sliding down your throat."
    pov "Don't worry, I'll take good care of you."
    mom "Hnng..."
    pov "Hold it just a bit longer..."
    mom "<choke>HNNG...!"
    scene parentsroom 7pm 013cbjdt
    mom "<choke> HRRRG...!"
    if inc == True:
        pov "That's amazing mom!"
    else:
        pov "That's amazing [mother]!"
    mom "<choke> HNNN...!"
    "She waves her hands behind her back so you know she needs to breathe. You loosen your grip on her head so she can pull back and breathe a bit."
    scene parentsroom 7pm 012cbjdt
    mom "Hnn... hnn..."
    if inc == True:
        pov "I need to come after that, mom!"
    else:
        pov "I need to come after that, [mother]!"
    pov "You're a very good at this."
    call screen proom19extbjcumlove

screen proom19extbjcumlove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "edited/gui/vice/icon_mouth_love_%s.png" action (Hide('proom19extbjcumlove'), Jump('proom19extbjcuminlove')) hovered tt.Action ("Have her swallow") focus_mask True
        imagebutton auto "edited/gui/vice/icon_blowjob_love_%s.png" action (Hide('proom19extbjcumlove'), Jump('proom19extbjcumoutlove')) hovered tt.Action ("Cover her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom19extbjcuminlove:
    pov "Will you swallow it?"
    mom "Mmhm..."
    scene parentsroom 7pm 015cbjdt
    pov "Yes! Swallow my seed!"
    "You cum in her mouth."
    mom "<gulp> <gulp>"
    pov "Hnng..."
    scene parentsroom 7pm 019cbj
    mom "Aaah..."
    pov "Good girl. I love it when you show me that you swallowed it all."
    scene parentsroom 7pm 018cbj
    pov "This is fun. We should do this all the time."
    mom "Hnng..."
    if inc == True:
        pov "I love you, mom."
    else:
        pov "I love you,  [mother]."
    scene parentsroom 7pm 010cbj
    mom "Hmm... Love you too. <lick>"
    #$ dtime += 1
    jump proom19extcorstartlove

label proom19extbjcumoutlove:
    pov "Can I cum on your face?"
    mom "Mm... hm..."
    scene parentsroom 7pm 016cbjdt
    pov "Yes! I'm cumming!"
    mom "Hmm..."
    pov "Hnng..."
    scene parentsroom 7pm 017cbjdt
    mom "Hnng..."
    pov "Good girl. I love it when you show me my handiwork."
    pov "This is fun. We should do this all the time."
    mom "Hnng..."
    if inc == True:
        pov "I love you, mom."
    else:
        pov "I love you,  [mother]."
    mom "Hmm... Love you too."
    #$ dtime += 1
    jump proom19extcorstartlove

label proom19extcorsexlove:
    mom "I want you to do me from behind this time."
    if inc == True:
        pov "Ok, mom."
    else:
        pov "Ok, [mother]."
    scene parentsroom 7pm 010cdg
    pov "Wow, I just can't get over this view."
    mom "You like it huh...?"
    if inc == True:
        pov "Yes, mom. I do."
    else:
        pov "Yes, [mother]. I do."
    mom "Good, now pick which hole you want to use..."
    povi "Awesome!"
    call screen proom19extfucklove

screen proom19extfucklove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "edited/gui/vice/icon_sex_love_%s.png" action (Hide('proom19extfucklove'), Jump('proom19extfuckplove')) hovered tt.Action ("I'll fuck your pussy") focus_mask True
        imagebutton auto "edited/gui/vice/icon_rub_love_%s.png" action (Hide('proom19extfucklove'), Jump('proom19extfuckalove')) hovered tt.Action ("I'll fuck your ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom19extfuckalove:
    $ proom19fuckass = True
    jump proom19extfuckplove

label proom19extfuckplove:
    if proom19fuckass == True:
        scene parentsroom 7pm 011cdg
        mom "Hnnng..."
        pov "Do you like how it feels against your tight hole?"
    else:
        scene parentsroom 7pm 011cdgp
        mom "Hnnng..."
        pov "Do you like how it feels against your wet pussy?"
    mom "Yes..."
    pov "You push your dick slowly inside her."
    if proom19fuckass == True:
        scene parentsroom 7pm 013cdg
    else:
        scene parentsroom 7pm 013cdgp
    pov "Do you like that? Nice and slow strokes?"
    mom "Hmm... I do baby."
    pov "That is what you want right? Of do you want me to go faster..."
    mom "Hnng... I want you to really give it to me!"
    scene parentsroom 7pm 012cdg
    with vpunch
    mom "Aaah..."
    "You pushed hard and deep inside her."
    pov "Like that?!"
    mom "Yes... I... need a hard pounding."
    povi "This is hot! She's asking me to fuck her hard."
    "You start to fuck her hard and rough."
    if proom19fuckass == True:
        scene parentsroom 7pm 014cdg
    else:
        scene parentsroom 7pm 014cdgp
    mom "Ahhh... hah..."
    mom "You're so deep inside me!"
    if proom19fuckass == True:
        pov "Your ass really needs a good pounding!"
    else:
        pov "Your pussy really needs a good pounding!"
    mom "Hah... aahh..."
    "Knock! Knock!"
    mom "Huh?"
    ls "Mom?"
    pov "<whisper> Dang it, what is she doing here?."
    mom "<whisper> It's okay. I'll take care of it."
    "She give you a loving grin before going to the door."
    scene parentsroom 7pm 015
    ls "Mom, you're naked?"
    mom "Yes... I..."
    mom "What do you need, honey?"
    if proom19fuckass == True:
        scene parentsroom 7pm 016a
        povi "Wow, her asshole is still gaping."
    ls "I heard sounds like you having sex with someone, but Dad left the house earlier."
    mom "Oh... I... that was me."
    ls "You?"
    mom "I... I needed to take care of my... urges."
    ls "What...? What do you mean?"
    mom "Mommy was playing with herself..."
    ls "Playing...?"
    scene parentsroom 7pm 016
    ls "UGH! Don't tell me that mom!"
    mom "But..."
    ls "Seriously, overshare much? Ugh!"
    scene parentsroom 7pm 017c
    pov "Good thinking. She not going to interupt us again anytime soon."
    mom "Thanks. Are you ready to get back to fucking me?"
    povi "She's acting real naughty now. I really like it!"
    pov "Yes I am!"
    if proom19fuckass == True:
        scene parentsroom 7pm 014cdg
        with vpunch
    else:
        scene parentsroom 7pm 014cdgp
        with vpunch
    "You continue to fuck her again, going even harder this time."
    mom "AAHHH...HAH..."
    with vpunch
    povi "It's great we don't need to be quiet. She sounds so sexy when she moans like that."
    mom "HAH... AHH!"
    with vpunch
    scene parentsroom 7pm 012cdg
    pov "You're getting tighter and starting to shake. Are you about to cum already?"
    mom "Yes [pov]. I'm so close, please can I cum?"
    pov "Wait if you can for just a little longer."
    mom "I...I'll try..."
    pov "Thanks. I really want us to come together."
    mom "Yes, me too!"
    pov "You're everything I've ever wanted!"
    mom "AAHH... HAH... You... are too!"
    mom "I want you to pull my hair sweetie!"
    scene parentsroom 7pm 017cdg
    mom "AHHH... HAH..."
    with vpunch
    pov "Is this what you wanted?!"
    with vpunch
    mom "YES AHhh...!"
    if inc == True:
        pov "You're gonna love cumming on your son's dick!"
        with vpunch
        mom "Yes... oh god yes!"
        pov "You're a naughty mother, craving your son's dick like this!"
        with vpunch
        mom "Yes! I'm naughty. I'm so naughty! I'm a dirty girl for my son! I love it when he fucks me!"
    else:
        pov "You're gonna love cumming on your my dick!"
        with vpunch
        mom "Yes... oh god yes!"
        pov "You're a naughty friend, craving your best friend's son. Craving his dick like this!"
        with vpunch
        mom "Yes! I'm naughty. I'm so naughty! I'm a dirty girl for you! I love it when you fuck me!"
    pov "I'm so close now!"
    scene parentsroom 7pm 015cdg
    with vpunch
    mom "AHHHH... YEEEES!!!"
    "She cums hard on your dick, deep inside her."
    pov "Oh, shit! I love it! You're pushing me over the edge too!"
    call screen proom19extfuckcumlove

screen proom19extfuckcumlove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        if proom19fuckass == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom19extfuckcumlove'), Jump('proom19extfuckcumassinlove')) hovered tt.Action ("I'll cum inside your ass") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom19extfuckcumlove'), Jump('proom19extfuckcumassoutlove')) hovered tt.Action ("I'll cum on your ass") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom19extfuckcumlove'), Jump('proom19extfuckcumpinlove')) hovered tt.Action ("I'll cum inside your pussy") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom19extfuckcumlove'), Jump('proom19extfuckcumpoutlove')) hovered tt.Action ("I'll cum on your ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom19extfuckcumassinlove:
    scene parentsroom 7pm 016cdg
    pov "Ahhh... yes...!"
    with vpunch
    "You spray cum inside her asshole."
    mom "Ahhh... so hot..."
    pov "Ahngh! I'm draining every last drop inside you!"
    with vpunch
    mom "Hah... hah..."
    scene parentsroom 7pm 020cdg
    pov "Oh wow, there's so much inside you now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your hot ass milked my balls dry, mom!"
    else:
        pov "Your hot ass milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 021cdg
    "She falls, exhausted, onto the bed."
    pov "That was a amazing! I really liked it."
    mom "Me too, baby."
    pov "We'll have much more fun together now..."
    if inc == True:
        pov "This is so perfect, mom."
    else:
        pov "This is so perfect, [mother]."
    mom "Hmm... yes it is..."
    pov "I'm going now, we'll probably be having even more fun in the basement later."
    mom "Ok, my lovely boy."
    #scene black
    #"You leave her."
    #$ dtime += 1
    $ proom19fuckass = False
    jump proom19extcorstartlove

label proom19extfuckcumassoutlove:
    scene parentsroom 7pm 018cdg
    pov "Ahhh... yes...!"
    with vpunch
    "You spray cum all over her ass."
    mom "Ahhh... so hot..."
    pov "Ahngh! I'm draining every last drop on you!"
    with vpunch
    mom "Hah... hah..."
    scene parentsroom 7pm 019cdg
    pov "Oh wow, there's so much inside you now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your tight pussy milked my balls dry, mom!"
    else:
        pov "Your tight pussy milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 022cdg
    "She falls, exhausted, onto the bed."
    pov "That was a amazing! I really liked it."
    mom "Me too, baby."
    pov "We'll have much more fun together now..."
    if inc == True:
        pov "This is so perfect, mom."
    else:
        pov "This is so perfect, [mother]."
    mom "Hmm... yes it is..."
    pov "I'm going now, we'll probably be having even more fun in the basement later."
    mom "Ok, my lovely boy."
    #scene black
    #"You leave her."
    #$ dtime += 1
    $ proom19fuckass = False
    jump proom19extcorstartlove

label proom19extfuckcumpinlove:
    scene parentsroom 7pm 016cdgp
    pov "Ahhh... yes...!"
    with vpunch
    "You spray cum inside her pussy."
    mom "Ahhh... so hot..."
    pov "Ahngh! I'm draining every last drop inside you!"
    with vpunch
    mom "Hah... hah..."
    scene parentsroom 7pm 020cdgp
    pov "Oh hell ya, there's so much inside you now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your tight pussy milked my balls dry, mom!"
    else:
        pov "Your tight pussy milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 021cdgp
    "She falls, exhausted, onto the bed."
    pov "That was a amazing! I really liked it."
    mom "Me too, baby."
    pov "We'll have much more fun together now..."
    if inc == True:
        pov "This is so perfect, mom."
    else:
        pov "This is so perfect, [mother]."
    mom "Hmm... yes it is..."
    pov "I'm going now, we'll probably be having even more fun in the basement later."
    mom "Ok, my lovely boy."
    #scene black
    #"You leave her."
    #$ dtime += 1
    $ proom19fuckass = False
    jump proom19extcorstartlove

label proom19extfuckcumpoutlove:
    scene parentsroom 7pm 018cdgp
    pov "Ahhh... yes...!"
    with vpunch
    "You spray cum all over her ass."
    mom "Ahhh... so hot..."
    pov "Ahngh! I'm draining every last drop on you!"
    with vpunch
    mom "Hah... hah..."
    scene parentsroom 7pm 019cdgp
    pov "Oh wow, there's so much on your ass now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your tight pussy milked my balls dry, mom!"
    else:
        pov "Your tight pussy milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 022cdgp
    "She falls, exhausted, onto the bed."
    pov "That was a amazing! I really liked it."
    mom "Me too, baby."
    pov "We'll have much more fun together now..."
    if inc == True:
        pov "This is so perfect, mom."
    else:
        pov "This is so perfect, [mother]."
    mom "Hmm... yes it is..."
    pov "I'm going now, we'll probably be having even more fun in the basement later."
    mom "Ok, my lovely boy."
    #scene black
    #"You leave her."
    #$ dtime += 1
    $ proom19fuckass = False
    jump proom19extcorstartlove

#----- Basement Orgy Corruption Event ----- Done
label baseorgystart:
    $ baseorgyfirst = True
    hide screen locations
    scene basement 10pm 101
    $ baseorgymiddle = True
    $ baseorgyright = False
    $ baseorgyleft = False
    call screen baseorgyscreen

label baseorgyright:
    scene basement 10pm 100
    $ baseorgymiddle = False
    $ baseorgyright = True
    $ baseorgyleft = False
    call screen baseorgyscreen

label baseorgyleft:
    scene basement 10pm 102a
    $ baseorgymiddle = False
    $ baseorgyright = False
    $ baseorgyleft = True
    call screen baseorgyscreen

screen baseorgyscreen():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        if baseorgymiddle == True:
            imagebutton auto "gui/icons/icon_left_%s.png" action (Hide ('baseorgyscreen'), Jump('baseorgyleft')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" action (Hide ('baseorgyscreen'), Jump('baseorgyright')) hovered tt.Action ("Turn right") focus_mask True
        if baseorgyright == True:
            imagebutton auto "gui/icons/icon_left_%s.png" action (Hide ('baseorgyscreen'), Jump('baseorgystart')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide ('baseorgyscreen'), Jump('basementorgycasmenu')) hovered tt.Action ("Go closer") focus_mask True
        if baseorgyleft == True:
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide ('baseorgyscreen'), Jump('basementorgyaoamenu')) hovered tt.Action ("Go closer") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" action (Hide ('baseorgyscreen'), Jump('baseorgystart')) hovered tt.Action ("Turn right") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custome baseorgycas landing -----
label basementorgycasmenu:
    call screen basementorgycasoptions

screen basementorgycasoptions():
    default tt = Tooltip ("[bs]")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide ('basementorgycasoptions'), Jump('baseorgycas')) hovered tt.Action ("[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide ('basementorgycasoptions'), Jump('baseorgycaslove')) hovered tt.Action ("[cr1] to [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custome baseorgyaoa landing -----
label basementorgyaoamenu:
    call screen basementorgyaoaoptions

screen basementorgyaoaoptions():
    default tt = Tooltip ("[mother]")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide ('basementorgyaoaoptions'), Jump('baseorgyaoa')) hovered tt.Action ("[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide ('basementorgyaoaoptions'), Jump('baseorgyaoalove')) hovered tt.Action ("[cr1] to [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Basement Orgy Corruption Event Cassandra ----- Done
label baseorgycas:
    scene basement 10pm 120a
    povi "So, [bs] is cleaning a mess and now Bruce can't take his eyes off her."
    povi "That damn pervert is staring on her ass."
    pov "Hey, pervert!"
    scene basement 10pm 121a
    dad "Huh [pov]? Don't scare me like that."
    pov "Did I interrupt you staring at something, haha?"
    dad "What? No! I... what do you mean?"
    scene basement 10pm 122a
    if inc == True:
        pov "Enjoying the view of my sister's ass?"
    else:
        pov "Enjoying the view of [bs]'s ass?"
    dad "What...?"
    pov "I mean, I can't blame you. Seeing her like that makes me want to mount her right here and now."
    dad "What are you talking about? I didn't..."
    pov "You can stop denying it. I know what I saw."
    dad "But..."
    pov "Slut!"
    scene basement 10pm 123a
    bs "Huh? Oh hi, [pov]."
    pov "That's a nice outfit you're wearing."
    bs "Thank you."
    if inc == True:
        pov "But crawling on the floor with that outfit on is giving dad the wrong ideas."
    else:
        pov "But crawling on the floor with that outfit on is giving Bruce the wrong ideas."
    bs "Huh?"
    dad "I told you..."
    pov "He can't take his eyes off your hot ass!"
    scene basement 10pm 124a
    if inc == True:
        bs "Dad!"
    else:
        bs "Bruce!"
    dad "Why are you doing this to me? Embarrassing me like that?"
    pov "Because you seem to think it's ok staring at MY slut like that!"
    dad "But I didn't..."
    if inc == True:
        pov "Oh, shut up, dad!"
    else:
        pov "Oh, shut up, Bruce!"
    scene basement 10pm 125a
    pov "Wait, did you do this on purpose slut, teasing him like that?"
    bs "N... No!"
    pov "You're allowed to tease him like you want to, but if you ever let anyone else touch you, you'll be banned from the gang forever."
    bs "I won't do that [pov]."
    pov "You won't do it, because...?"
    bs "Be... because I'm your slut."
    pov "Yes, you are."
    pov "How about you show us some of that hot body of yours. I think we've earned a show after all that teasing."
    bs "Y... yes [pov]."
    scene basement 10pm 126a
    "You push the table away to make some room for her."
    if inc == True:
        pov "Go on. Show me and dad what a hot slut you are!"
    else:
        pov "Go on. Show me and Bruce what a hot slut you are!"
    bs "Y... yes..."
    "She begins to dance slowly."
    pov "Isn't that nice, look at her hot body."
    scene basement 10pm 127a
    if inc == True:
        dad "Hey! Don't treat your sister like that."
    else:
        dad "Hey! Don't treat her like that."
    pov "Seriously, you're saying that to me? After I caught you eye-fucking her just now... But don't worry, you're not worth getting angry over."
    pov "You should turn your head, I know you want to see this too."
    dad "This is totally crazy. You better stop before you cross a line you can't come back from."
    pov "Haha, are you jealous?"
    scene basement 10pm 128a
    pov "Look at her! She was born to please with that hot body."
    pov "She even made her tits bigger to get more attention."
    pov "She's going to become the perfect slut and I'm sure she'll enjoy doing it."
    dad "..."
    pov "Haha, speechless? I knew it."
    scene basement 10pm 129a
    pov "Look at that perfectly round ass and you can even get a glimpse of her wet pussy."
    dad "S... stop it."
    pov "Oh I don't think so. I'm far away from done here."
    pov "Think about standing up right now and ramming deep inside her, giving her a thick hard dick, which she's been craving all day."
    bs "Hnng..."
    povi "Damn, did she just moan? Is she really getting this slutty?"
    povi "Maybe it's time I have some fun with her hot body?"
    pov "Slut!"
    scene basement 10pm 130a
    bs "Yes?"
    pov "Your teasing has pushed all the right buttons, now it's time you please me with your hot body!"
    bs "R... right now?"
    pov "Yes! Right here, right now!"
    scene basement 10pm 131a
    bs "Ok [pov], I'll please you."
    povi "Oh now she seems hesitant. Probably this whole thing with Bruce is making her nervous."
    pov "You will come over here and..."
    call screen baseorgycaschoose

screen baseorgycaschoose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('baseorgycaschoose'), Jump('baseorgycasbj')) hovered tt.Action ("suck my dick!") focus_mask True
        imagebutton auto "gui/icons/icon_sex_corruption_%s.png" action (Hide('baseorgycaschoose'), Jump('baseorgycassex')) hovered tt.Action ("ride on my dick!") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgycasbj:
    scene basement 10pm 132a
    dad "You can't be serious!"
    dad "It's so wrong that you even want to do this with her..."
    dad "...but especially here, right now, that is the worst."
    pov "Wanna watch, haha?"
    pov "Or maybe get a turn after me?"
    povi "Like I'd ever let him. Ha!"
    dad "Grrr..."
    scene basement 10pm 133a
    dad "I'm out of here, I don't need to see this!"
    bs "Hnng..."
    dad "You're going down a path, where there's no return."
    pov "Haha, maybe, but it'll be a journey of pleasure and fun."
    scene basement 10pm 134a
    bs "Did I really turn you on that much?"
    povi "Oh, what's this, she's trying to be slutty now. Yeah, it was clearly bothering her to be this way in front of Bruce."
    povi "It's to be expected I suppose, but I'll need to train that out of her."
    povi "Or maybe she wants to impress me? It's also possible she doesn't want to seem like she doesn't know what she's doing in front of [miranda]."
    povi "No matter the reason, it's damn hot."
    pov "Of course, you selected a great outfit and did a good job dancing."
    scene basement 10pm 135a
    bs "I'm glad you liked it."
    pov "What's with the extra motivation you seem to have today? You're so eager to please me."
    bs "I... I'm not sure..."
    if inc == True:
        pov "Was it how I described you in front of dad? Explaining to him why you're such a hot slut."
    else:
        pov "Was it how I described you in front of Bruce? Explaining to him why you're such a hot slut."
    bs "Hnng..."
    povi "Oh it seems I hit a nerve. Defintely has daddy issues..."
    povi "Of course I knew that. But still, it's good to confirm it."
    pov "Go on, don't just stare at me, slut. My dick needs some attention."
    bs "Yes [pov]."
    scene basement 10pm 136a
    bs "<suck> <lick>"
    pov "Oh... yes..."
    pov "I think this is my favorite way to start the night, with a great blowjob from my slut."
    bs "<suck> <lick>"
    if inc == True:
        pov "But you need to keep improving your skills and give your best, because your in direct competition with mom now, my other slut."
    else:
        pov "But you need to keep improving your skills and give your best, because your in direct competition with your mom now, my other slut."
    scene basement 10pm 137a
    pov "Not that I was worried about that, I'm sure you'll give your best."
    bs "<lick> Yes, [pov]. I'll be so much better than her."
    pov "Good. Then you can prove it to me now, because she's watching us..."
    bs "<lick> She's watching us while I'm licking your dick?"
    scene basement 10pm 161
    pov "Yes and she seems to be very jealous of you."
    bs "<lick> Hmm..."
    pov "And that idiot Bruce is so busy freaking out, he doesn't even realize it, haha."
    pov "Ohhh... yes..."
    if casbjdt > 2:
        scene basement 10pm 138dt
    else:
        scene basement 10pm 138a
    bs "<suck> <suck>"
    if inc == True:
        pov "Show mom that you're a better slut than she is!"
    else:
        pov "Show your mom that you're a better slut than she is!"
    bs "<suck> Yessh..."
    povi "Putting them in direct competition idea was very, very good. I'm going to have so much fun."
    scene basement 10pm 162
    if inc == True:
        pov "Mom is so angry right now. I think she's blaming Bruce for this, haha."
    else:
        pov "Your mom is so angry right now. I think she's blaming Bruce for this, haha."
    bs "Hnng... <suck> <suck>"
    if casbjdt > 2:
        scene basement 10pm 138dt
    else:
        scene basement 10pm 138a
    pov "Oh shit, your blowjobs are getting even better, I'm so close."
    call screen baseorgycasbjchoose

screen baseorgycasbjchoose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('baseorgycasbjchoose'), Jump('baseorgycasbjin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('baseorgycasbjchoose'), Jump('baseorgycasbjout')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgycasbjin:
    pov "You're going to swallow my seed now."
    bs "Hmm..."
    pov "Oh yes, ARGHHH...!"
    if casbjdt > 2:
        scene basement 10pm 138dt
        with vpunch
    else:
        scene basement 10pm 139ai
        with vpunch
    bs "<gulp> <gulp>"
    pov "Yes, good slut!"
    scene basement 10pm 140ai
    bs "Aahh..."
    pov "oh, that's a nice surprise. You want to be a good slut and show me some of my handiwork."
    "She nods in agreement."
    pov "You can swallow the rest now."
    scene basement 10pm 141ai
    bs "<gulp>"
    bs "Hmm..."
    pov "Enjoying my taste?"
    scene basement 10pm 142ai
    bs "Aahh..."
    pov "Well this was definitely a possitive entry for the competition."
    pov "Keep up this up or better yet, surpass this level and I'll be very pleased."
    bs "Yes [pov]."
    povi "Who would have known she'd be responsive to positive reinforcement like this? Nice."
    jump baseorgycasend

label baseorgycasbjout:
    pov "I'm going to cum on your face."
    bs "Hmm..."
    pov "Oh yes, ARGHHH...!"
    scene basement 10pm 139ao
    with vpunch
    bs "Hmm..."
    pov "Yes, good slut!"
    scene basement 10pm 140ao
    bs "Aahh..."
    pov "Oh what a nice view. My slut covered with my cum."
    bs "Yes."
    pov "And you even got some in your mouth so you can have a little taste too."
    bs "Hmm..."
    pov "Well this was definitely a possitive entry for the competition."
    pov "Keep up this up or better yet, surpass this level and I'll be very pleased."
    bs "Yes [pov]."
    povi "Who would have known she'd be responsive to positive reinforcement like this? Nice."
    jump baseorgycasend

label baseorgycassex:
    scene basement 10pm 132a
    dad "You can't be serious!"
    dad "It's so wrong that you even want to do this with her..."
    dad "...but especially here, right now, that is the worst."
    pov "Wanna watch, haha?"
    pov "Or maybe get a turn after me?"
    povi "Like I'd ever let him. Ha!"
    dad "Grrr..."
    scene basement 10pm 133a
    dad "I'm out of here, I don't need to see this!"
    bs "Hnng..."
    dad "You're going down a path, where there's no return."
    pov "Haha, maybe, but it'll be a journey of pleasure and fun."
    scene basement 10pm 150
    pov "I'll help you to remove that patch so I can fuck you properly."
    bs "Hnng..."
    povi "This is going be great."
    scene basement 10pm 151
    pov "What's wrong? Are you afraid to have sex with me in front of the others?"
    bs "Hnng..."
    pov "You need to get past that and I think you know it. You wanted to join the gang, so I choose you as my slut so no one else would have you."
    pov "You need to follow my orders, if you want to continue to be a part of this."
    bs "Hnng..."
    pov "Just sit on my lap and let my dick slide inside you. I'm sure you'll forget your worries in no time."
    bs "..."
    pov "NOW SLUT!"
    scene basement 10pm 152
    pov "Good, now put it in for me."
    bs "Hnng..."
    povi "She just needed a nudge in the right direction. Now she's eager to please again."
    if inc == True:
        povi "Oh, mom has noticed us. She's a good slut though, she won't make a fuss."
    else:
        povi "Oh, [mother] has noticed us. She's a good slut though, she won't make a fuss."
    pov "Your pussy is so wet [bs]. You don't need to wait any longer."
    bs "Hmm..."
    scene basement 10pm 153
    bs "Aaahh..."
    pov "You took it all in at once. What a naughty slut you are."
    bs "Hnn... so big."
    pov "Good now start riding me and let's enjoy a good fuck!"
    if inc == True:
        bs "Y... yes, brother."
    else:
        bs "Y... yes, [pov]."
    "She starts riding you."
    bs "Ahh... hah..."
    scene basement 10pm 154
    pov "See, you already forgot about those worries floating through your mind a moment ago."
    bs "Yes, thanks to you [pov]."
    pov "Ride me faster!"
    bs "Yes..."
    "She's riding you faster."
    pov "Now that you're properly focused on pleasing me I can tell you..."
    scene basement 10pm 161
    if inc == True:
        pov "that mom is watching us."
        bs "Mom?"
        povi "Wow, she's gotten even tighter."
    else:
        pov "that your mother is watching us."
        bs "My mom?"
        povi "Wow, she's gotten even tighter."
    pov "Yes and she seems to be very jealous of you."
    bs "Hah... hah..."
    pov "And that idiot Bruce is so busy freaking out, he doesn't even realize it, haha."
    scene basement 10pm 155
    "You play with her tits."
    pov "You like it when I'm rough with them, don't you?"
    bs "Yes... it's feels so good... [pov]!"
    if inc == True:
        pov "But you need to keep improving your skills and give your best, because your in direct competition with mom now, my other slut."
        pov "Show mom that you're a better slut than she is!"
    else:
        pov "But you need to keep improving your skills and give your best, because your in direct competition with your mom now, my other slut."
        pov "Show your mom that you're a better slut than she is!"
    bs "Hah, yes... I'm... the best slut."
    scene basement 10pm 162
    if inc == True:
        pov "Mom is so angry right now. I think she's blaming Bruce for this, haha."
    else:
        pov "Your mom is so angry right now. I think she's blaming Bruce for this, haha."
    bs "Hah... AAAHH..."
    pov "You're getting close?"
    scene basement 10pm 157
    bs "Yes... yes..."
    pov "Me too. Let's cum together slut! Receive your well earned reward!"
    bs "Yes [pov]! I want to cum with you!"
    call screen baseorgycasfuckcum

screen baseorgycasfuckcum():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('baseorgycasfuckcum'), Jump('baseorgycasfuckcumin')) hovered tt.Action ("Cum in her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_belly_%s.png" action (Hide('baseorgycasfuckcum'), Jump('baseorgycasfuckcumout')) hovered tt.Action ("Cum on her belly") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgycasfuckcumin:
    pov "I'm going cum inside your pussy!"
    bs "Yes, hah... cum inside me..."
    if inc == True:
        pov "You want me to cum deep inside you, big sis?"
        bs "Yes, brother... I'm so close... hah..."
    else:
        pov "You want me to cum deep inside you, slut?"
        bs "Yes, [pov]... I'm so close... hah..."
    pov "With pleasure!"
    bs "AAHHH... HAAAAHHH...!"
    scene basement 10pm 156
    with vpunch
    "She cums while you pump hot cum inside her."
    bs "Ahh... I can feel it... so warm..."
    pov "Oh yes..."
    "She slowly stands up from your lap, letting your cock slip out with a wet sloppy pop."
    scene basement 10pm 159i
    pov "Such a nice view!"
    pov "Don't clean it up though, I want to see everybody what I did to my slut!"
    bs "O... OK [pov]."
    pov "This is defintely a positive entry for the competition."
    pov "If we fuck more often and I'll be very pleased."
    bs "Yes [pov]."
    povi "Who would have known she'd be responsive to positive reinforcement like this? Nice."
    jump baseorgycasend

label baseorgycasfuckcumout:
    pov "I'll cum on your stomach!"
    bs "Yes, hah... Cum over me..."
    if inc == True:
        pov "You want me to cum all over your body, big sis?"
        bs "Yes, brother... I'm so close... hah..."
    else:
        pov "You want me to cum all over your body, slut?"
        bs "Yes, [pov]... I'm so close... hah..."
    pov "With pleasure!"
    bs "AAHHH... HAAAAHHH...!"
    scene basement 10pm 158o
    with vpunch
    "She cums while you spray your hot cum all over her."
    bs "Ahh... I can feel it... so warm..."
    pov "Oh yes..."
    "She slowly stands up from your lap."
    scene basement 10pm 159o
    pov "Such a nice view!"
    pov "Don't clean it up though, I want to see everybody what I did to my slut!"
    bs "O... OK [pov]."
    pov "This is defintely a positive entry for the competition."
    pov "If we fuck more often and I'll be very pleased."
    bs "Yes [pov]."
    povi "Who would have known she'd be responsive to positive reinforcement like this? Nice."
    jump baseorgycasend

label baseorgycasend:
    pov "Rest now slut, maybe I'll use you again later."
    bs "Yes... [pov]... hah..."
    povi "Let's see what Davide is up to."
    jump basementorgyaoamenu

#----- Basement Orgy Corruption Event - Tug o War - Done
label baseorgyaoa:
    scene black
    "You go over to Davide and [miranda]."
    scene basement 10pm 103a
    pov "Hey there..."
    davide "Oh, hey [pov]."
    miranda "Hello good looking..."
    povi "Nice, she's flirting with me again."
    davide "Treat him with respect slut. That's a fucking gang member your speaking to now."
    scene basement 10pm 104m
    miranda "Wow, that's great. Congratulations!"
    pov "Thank you."
    miranda "Now you're one them, I look forward to getting to know you more. I'm friends with all the gang members"
    davide "Haha, she loves being a slut."
    miranda "<giggle>"
    scene basement 10pm 105m
    pov "I see someone is ready to party."
    povi "Those rock hard nipples."
    miranda "I can't wait to show you what you been missing! A good looking stud like you needs to be pleased!"
    mom "[miranda]!"
    scene basement 10pm 106m
    mom "What do you think you're doing?"
    mom "Get away from him!"
    scene basement 10pm 107m
    miranda "..."
    davide "Haha, of course [mother] is angry again."
    if inc == True:
        davide "She thinks she needs to protect her son from our biggest slut."
    else:
        davide "She thinks she needs to protect you from our biggest slut."
    mom "Come here, you whore!"
    scene basement 10pm 108m
    mom "I'll rip your ass off if you lay a finger on him!"
    miranda "Haha, You can't be around him all the time. Sooner or later he'll taste a lot more of me than my finger."
    mom "Grrr..."
    scene basement 10pm 110m
    davide "Don't look so shocked, haha."
    davide "They fight all the time, but it never gets violent."
    if inc == True:
        davide "Your mom hates her. Something that went down a while back, I don't give a two shits about it. But it's funny as hell."
    else:
        davide "[mother] hates her. Something that went down a while back, I don't give a two shits about it. But it's funny as hell."
    pov "So they fight all the time?"
    davide "Yes, I think it's very entertaining."
    pov "Entertaining?"
    scene basement 10pm 109m
    davide "Haha, hell yes."
    davide "Watch, we'll set up some challenges for them, so they can prove which of them is the better slut and we just sit back enjoy the show. Better than fucking pay-per-view!"
    pov "Haha, so you're really not worried that they'll actually hurt each other?"
    davide "Fuck if I know, but they haven't yet. I think they're just talking smack."
    davide "But there isnt much else we'll be able to get them to do while their all fired up like that."
    pov "What challenge did you have in mind?"
    davide "I'll show you one of my favorites, I call it \"Ass vs Ass\"."
    pov "Haha, Ok, now I'm curious."
    davide "They get a double-sided dildo stuffed in their pussies and then they have to try to get the other one off."
    pov "First one to orgasm loses I'm assuming?"
    davide "Now you got it! We have them do it in doggy style. And that's why I call it \"Ass vs Ass\"."
    pov "So what's the prize?"
    scene basement 10pm 111m
    davide "These..."
    if momsecret == True:
        pov "But [mother] can't take those."
        davide "True, only [miranda] can win one."
    else:
        davide "But since [mother] can't have them, only [miranda] can win one."
        pov "[mother] can't use them?"
        davide "Yeah, she gets sick and pukes it all out. Maybe she's allergic or some shit, I don't know."
        pov "Oh, I didn't know that."
        $ momsecret = True
    if inc == True:
        pov "So how do we get my mother motivated to win then?"
    else:
        pov "So how do we get [mother] motivated to win then?"
    davide "Haha, she'll do anything to make sure [miranda] doesn't win."
    pov "Wow, there's so much hate there..."
    davide "Yeah for both of them. Sometimes [miranda]'s drive to make [mother] fail is even bigger."
    scene basement 10pm 112m
    pov "Well I shouldn't be surprised by the biggest slut's drive, right?."
    davide "Haha, yeah."
    davide "Let's get this game going."
    scene black
    "Davide starts running his mouth about how [mother] could never beat [miranda] and in just moments, they were ready to compete in front of everyone."
    scene basement 10pm 113m
    pov "What a nice view!"
    davide "Haha, see! It's just like I told you."
    pov "And now we just sit back and watch?"
    davide "Yes, but we need to choose our players first. We want the sluts to give it their best to impress us."
    pov "Oh this gets even better!"
    if inc == True:
        davide "You probably better side with your mother for this first time, she's your slut after all."
    else:
        davide "You probably better side with [mother] for this first time, she's your slut after all."
    davide "I'll side with [miranda]."
    pov "Ok, I'm sure my slut will give her best!"
    mom "I will [pov]."
    miranda "Haha, you wish! You're definitely gonna lose."
    davide "Get ready."
    scene basement 10pm 114m
    mom "Hnng..."
    miranda "Hah..."
    povi "Letting them get their steam out with games against each other. What an amazing idea. And so perverted."
    scene basement 10pm 115m
    davide "You sit on the other side, so you can cheer on your slut better."
    pov "Now I'm wondering if that's why these chairs were setup this way to begin with, haha?"
    davide "Well it is one of my favorites!"
    pov "Let's do this."
    scene basement 10pm 116m
    pov "We have to win this!"
    mom "Yes, I'll give my best."
    pov "Don't just try, you need to win. Everyone needs see that I chose the right slut!"
    if inc == True:
        pov "That you're my slut, mom!"
    else:
        pov "That you're my slut, [mother]!"
    mom "Yes, I'll win for you [pov]!"
    davide "How about we start? Three... Two... One... GO!"
    scene basement 10pm 117m
    miranda "Huh? Haah...!"
    mom "Hnng!"
    davide "Wow, that's an agressive start from [mother]. Pushing it all in, what a surprise!"
    povi "Ok, was that just me or was Davide channeling he inner sports announcer?"
    davide "Don't disappoint me, slut!"
    miranda "I won't, hah..."
    "[miranda] starts to fuck back and they fall into a rhythm."
    scene basement 10pm 118m
    mom "Hnng...! Hah... hah..."
    davide "Harder slut!"
    miranda "Yes... aaah... hah..."
    if inc == True:
        pov "You can do this mom."
    else:
        pov "You can do this [mother]."
    mom "Hah... yes..."
    scene basement 10pm 119m
    mom "Hmm...! Hah... Haaaah..."
    miranda "Hnng! Hnng! Hah..."
    davide "Having fun on the other side [pov]?"
    pov "Haha, yes. That shit is great!"
    if inc == True:
        povi "And now I have dad's seat."
    else:
        povi "And now I have Bruce's seat."
    call screen baseorgyaoawin

screen baseorgyaoawin():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("[mother] wins (coming soon)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("It's a tie (coming soon)") focus_mask True
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyaoawin'), Jump('baseorgyaoamirwin')) hovered tt.Action ("[miranda] wins") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyaoamirwin:
    scene basement 10pm 120m
    mom "Oh no! Hah... Ahh... hah..."
    pov "What do you mean \"Oh no\"?"
    mom "I'm so... hah... close..."
    davide "You hear that [miranda]? Finish her!"
    pov "Don't you dare to lose, slut!"
    mom "I... I... Hah..."
    scene basement 10pm 121m
    mom "AAAHHH... HAAAHHH..."
    with vpunch
    "She cums hard in front of you."
    mom "I'm... so... sorry... hah... haaahh..."
    miranda "Yes! Hnng!"
    povi "Damn it, she lost to [miranda]."
    scene basement 10pm 122mm
    miranda "Hah, that's right, I did it. I finished that slut!"
    davide "Good job!"
    mom "Hnng... Hnn..."
    povi "Seriously, everyone should get to have this happen to them at least once in their lives."
    scene basement 10pm 123mm
    miranda "Can I get my prize now? We all knew I'd win anyways!"
    davide "Relax, slut. You'll have plenty of fun with your prize soon."
    mom "I... I'm so sorry. Please forgive me [pov]."
    pov "I just don't know if I can. You made me lose face in front of Davide."
    povi "I'll rub it in for a while, hopefully that will light a fire under her for next time."
    scene basement 10pm 124mm
    miranda "<giggle> Maybe you should choose me next time [pov]."
    miranda "I can last a long time, but I'm sure your big dick will make me cum in no time."
    povi "Haha, she can't stop teasing."
    mom "Hnng...!"
    if inc == True:
        povi "Mom is so humiliated right now."
    else:
        povi "[mother] is so humiliated right now."
    povi "Might as well twist the knife a bit."
    pov "You disappointed me, slut. Giving up that quickly!"
    mom "I'm sorry [pov]. I can do better."
    scene basement 10pm 125mm
    pov "You not only disappointed me, but your own daughter as well."
    pov "She shouldn't have to watch her own mother lose like that."
    mom "Hnng..."
    povi "Haha, I think [bs] is more shocked by what she just saw, then she actually cares about [mother] winning or losing."
    if inc == True:
        povi "But that reaction is helping me with mom regardless."
    else:
        povi "But that reaction is helping me with her mom regardless."
    scene basement 10pm 126mm
    mom "Please forgive me [pov], I'm so sorry."
    pov "..."
    mom "I'll do anything to be a better slut for you!"
    pov "I don't know. I don't think this can't be forgotten just like that. Maybe I should have [bs] do it next time."
    pov "Or maybe I should choose [miranda]?"
    scene basement 10pm 129mm
    mom "No! You chose me! I'll be better. I'll do anything. Anything you want!"
    povi "Now that's the reaction I was looking for. But is she giving herself to me to protect her daughter or does she really hate [miranda] that much?"
    povi "Or maybe she's actually just being the slut I want her to be and she's craving my attention?"
    if inc == True:
        mom "I'm your mother. I raised you and I know you the best. I'm the one who can please you the most!"
    else:
        mom "I'm your mother's best friend. I helped raise you and I know you the best. I'm the one who can please you the most!"
    povi "Damn, she's submitting herself entirely to me."
    scene basement 10pm 127mm
    miranda "Hmm..."
    povi "But... [miranda] is also an interesting slut. Maybe I can make her mine too?"
    povi "I can understand why Davide is so pleased with her."
    scene basement 10pm 128mm
    miranda "I'm so horny right now. Victory feels so good."
    miranda "Hey [pov]! Do you want to have a real slut please you for once?"
    povi "Hmm... that body."
    scene basement 10pm 129mm
    mom "Pleeease [pov]..."
    povi "Hmm... what to do now?"
    if inc == True:
        povi "My mom is begging me for my dick. She'll let me do anything."
    else:
        povi "[mother] is begging me for my dick. She'll let me do anything."
    povi "And I could demand something else in return for my forgiveness."
    povi "But [miranda] has such a nice body."
    povi "And what's with Davide? Should he also have some fun or do I risk a fight with the leader of the gang?"
    povi "So many possibilites, haha."
    call screen baseorgyaoaniclose

screen baseorgyaoaniclose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyaoaniclose'), Jump('baseorgyaoaniclosedem')) hovered tt.Action ("Forgive her, but demand something in return") focus_mask True
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyaoaniclose'), Jump('baseorgyaoanicpunish')) hovered tt.Action ("Forgive her, but punish her as well") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("Have fun with [miranda] (soon)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyaoaniclosedem:
    pov "I'll forgive you this time, but I want something in return."
    mom "Anything, I'll do anything."
    call screen baseorgyaoaniclosedemch

screen baseorgyaoaniclosedemch():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyaoaniclosedemch'), Jump('baseorgyaoaniclosedempill')) hovered tt.Action ("Stop taking birth control") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("More choices soon...") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action NullAction() hovered tt.Action ("Nothing for now (soon...)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyaoaniclosedemno:
    pov "I suppose you've learned a lesson, so I'll just punish you for your loss today and we'll leave it at that."
    mom "Thank you for forgiving me!"
    mom "And yes, I need to be punished."
    jump baseorgyaoanicpunish

label baseorgyaoaniclosedempill:
    pov "I want you stop taking birth control."
    scene basement 10pm 130mm
    mom "Stop taking birth control? But then..."
    pov "That's right, I'm going to breed you and you're going to have my child."
    scene basement 10pm 131mm
    mom "What you are saying?"
    if inc == True:
        mom "You're my son and you want to breed me?"
    else:
        mom "You're my best friend's son and you want to breed me?"
    pov "Yes!"
    pov "You said you wanted to be the best slut for me, so it's only natural that you carry my heir!"
    pov "Or have I made another mistake?"
    mom "Hnng..."
    pov "I'm not going to wait any longer for an answer."
    scene basement 10pm 132mm
    mom "No wait. It's ok. I'll stop taking birth control and let you breed me."
    mom "Please [pov]... breed me!"
    if inc == True:
        povi "Oh my god! My mom's begging me to breed her. This is awesome!"
    else:
        povi "Oh my god! [mother]s begging me to breed her. This is awesome!"
    pov "Perfect, let's seal the deal with sex."
    pov "I want you to take the lead and show me, how much you want my seed inside you."
    mom "Y... yes [pov]."
    scene basement 10pm 128mm
    pov "I'll have fun with my slut now."
    if NTR == True and momrelationship < 5 or hardntr == True:
        jump baseorgyaoanicNTR
    miranda "And what about me? I won the game..."
    povi "Should Davide have some fun too or not?"
    call screen baseorgyniclosedavide

screen baseorgyniclosedavide():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('baseorgyniclosedavide'), Jump('baseorgyniclosedavideyes')) hovered tt.Action ("He can have fun with [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('baseorgyniclosedavide'), Jump('baseorgyniclosedavideno')) hovered tt.Action ("I don't want him to touch her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyniclosedavideyes:
    $ baseorgyaoaniclosedavy = True
    pov "You'll please Davide. I'm sure he'll help you have fun.!"
    miranda "But I want you... OK."
    davide "Don't worry slut, I'm sure you'll enjoy your victory still, haha."
    jump baseorgyaoaniclosedem2

label baseorgyniclosedavideno:
    pov "Do what you want, it's your victory."
    miranda "But I want you!"
    davide "Ouch, haha."
    pov "I can't now I'm afraid! I need to punish my slut."
    miranda "Oh..."
    miranda "I'll have some fun with the sybian then."
    davide "Damn, you chose a sybian over me huh? Well, good sluts should get to choose. You better believe I'm gonna watch though!"
    jump baseorgyaoaniclosedem2

label baseorgyaoaniclosedem2:
    scene black
    mom "Please lay on the table."
    "You lay on the table."
    scene basement 10pm 133mn
    pov "Oh you seem very motivated now."
    mom "I am. I'm going to prove to you that I'm better then [miranda]!"
    pov "Good slut! Then show me how much you're craving my seed."
    mom "Yes [pov]."
    scene basement 10pm 134mn
    mom "Hnng... hah..."
    pov "Oh yes... all in."
    scene basement 10pm 135mn
    mom "Now you know I can do better."
    povi "Damn, their rivalry is the greatest thing to ever happen to me."
    pov "Then ride me until I spray hot cum inside you!"
    mom "Yes [pov], give me your cum!"
    "She starts riding you."
    scene basement 10pm 136mn
    mom "Hah... hah... your big dick... so... good..."
    povi "Wow, she's putting on a hot show. I wonder if this is all to try to stick it [miranda] again."
    povi "I won't complain. But I wonder if she's aware that [bs] is still here?"
    povi "Let's see how [miranda] celebrates her victory."
    if baseorgyaoaniclosedavy == True:
        scene basement 10pm 134mdm
        povi "Strapping her in and going to work on her backside again. Classic."
        miranda "Oh yes, harder... ahh..."
    else:
        scene basement 10pm 133msyb
        miranda "Aaah... hah... so good..."
        povi "She's pretty damn hot. Maybe I should fuck her sometime too."
        scene basement 10pm 134msyb
        miranda "Oh YES! YES! Aaahh"
        davide "Wow, already number two in no time at all, haha."
    scene basement 10pm 137mn
    mom "Ohh... hah... ahhh..."
    pov "Do you want my sperm so badly?"
    mom "Yes, [pov]. Please cum inside me!"
    if inc == True:
        pov "That's it, I love how you're begging for my seed, mom!"
    else:
        pov "That's it, I love how you're begging for my seed, [mother]!"
    mom "Hah... hah..."
    pov "But I don't think everyone else heard you!"
    scene basement 10pm 137mnb
    mom "Huh? You want me to... tell them? Hah..."
    pov "Yes, I want you ride me even harder and then tell them that you're mine and I'm the only one allowed to breed you!"
    if inc == True:
        pov "Tell them how much you want to be my slut, mom!"
    else:
        pov "Tell them how much you want to be my slut, [mother]!"
    mom "But [bs] is still here!"
    pov "Do you really want to disappoint me again?"
    mom "No! I'll... do it for you [pov]!"
    "She begins to ride you harder."
    scene basement 10pm 139mn
    mom "Hah... hah... Listen everyone...!"
    if inc == True:
        mom "I'm craving... hah... my son's seed..."
    else:
        mom "I'm craving... hah... [pov]'s seed..."
    mom "and I'm done taking the pill... hah... hah..."
    mom "so he can... can breed me properly... hah... ahh..."
    pov "Good, now let's cum together, slut!"
    povi "Let's see how the others react."
    scene basement 10pm 141mn
    if inc == True:
        povi "Oh, looks like big sis is shocked. No wonder, mom did just announce to everyone her she wants to have a baby with me, haha."
    else:
        povi "Oh, looks like [bs] is shocked. No wonder, her mom did just announce to everyone her she wants to have a baby with me, haha."
    if baseorgyaoaniclosedavy == True:
        scene basement 10pm 140mnb
        miranda "Ohhh...."
        povi "[miranda] is speechless. That'll make my slut happy, haha."
        davide "Yeah, go for it bro!"
        povi "It's crazy, he's really been treating me more like a friend these days instead of... whatever the hell he was treating me like before."
    else:
        scene basement 10pm 140mn
        miranda "Ohhh...."
        povi "[miranda] is speechless. That'll make my slut happy, haha."
        davide "Yeah, go for it bro!"
        povi "It's crazy, he's really been treating me more like a friend these days instead of... whatever the hell he was treating me like before."
    povi "Dang it, Bruce is missing... Did he leave again...?"
    scene basement 10pm 142mn
    mom "Hah... hah... I'm so close [pov]!"
    pov "Then cum with me!"
    mom "Yes, hah... AHHHH... I'm cumming [pov]!"
    with vpunch
    pov "Me too, argh..."
    with vpunch
    "You spray your cum deep inside her."
    scene basement 10pm 143mn
    mom "Your hot seed is inside me, hah..."
    povi "What a beautiful view. And made all the better since she begged for it."
    mom "Hah... hah... you're satisfied [pov]?"
    pov "Yes. For now..."
    $ nicoleonpill = False
    $ baseorgyaoaniclosedavy = False
    jump baseorgyend

label baseorgyaoanicpunish:
    scene basement 10pm 128mm
    povi "Let's see what we'll do now."

    call screen baseorgyniclosepunchoose

screen baseorgyniclosepunchoose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyniclosepunchoose'), Jump('baseorgyniclosepunnicdavmir')) hovered tt.Action ("I'll punish my slut, you can have [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("I'll punish my slut, [miranda] can decide for herself (soon...)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyniclosepunnicdavmir:
    if NTR == True and momrelationship < 5 or hardntr == True:
        jump baseorgyaoanicNTR
    scene black
    "You two prepare the girls."
    mom "Hnng...hah..."
    miranda "Ohhh... ohhh..."
    scene basement 10pm 133mdp
    "You both start to fuck them."
    pov "Now this is the way I like to punish a slut."
    davide "It's the best thing for them, they get all riled up again afterwards, haha."
    mom "Ahh... hah..."
    davide "How about we have ourselves a little competition to see which slut will orgasm first?"
    pov "Haha, I'm in."
    miranda "Hah... hah... not so rough..."
    davide "Shut up, slut!"
    scene basement 10pm 134mdp
    mom "Hah... hah... you're so rough..."
    pov "Of course I am! This is punishment slut! And you're not going to disappoint me again."
    mom "No, no, I won't. I'll cum hard and fast from your fat dick."
    povi "Hmm... maybe I should spice it up a little more, so my slut will come faster."
    scene basement 10pm 134mcas
    pov "Bring me and Davide a drink, slut!"
    davide "Nice idea, I could use a drink!"
    bs "Ok, [pov]."
    mom "No... hah... don't..."
    pov "Shut up, slut!"
    scene basement 10pm 135mcas
    bs "Here is your drink [pov]."
    if inc == True:
        pov "Watch closely how I punish mom for disappointing me!"
    else:
        pov "Watch closely how I punish your mom for disappointing me!"
    bs "Y-Yes, I will."
    mom "Hnng! Hnng!"
    pov "So do you agree with me that she needs a hard punishment?"
    bs "I... I do... [pov]!"
    pov "Good slut!"
    scene basement 10pm 136mcas
    bs "Here is your drink, Davide."
    miranda "Hah... hah..."
    davide "You're pretty damn lucky for having such obedient sluts!"
    pov "Oh yes, I am, haha. But I did have to tame this one a bit."
    with vpunch
    "You thrust your cock extra hard to help make your point."
    mom "AHHH... HAAHHH..."
    pov "You're close slut?"
    mom "Yes... hah..."
    scene basement 10pm 135mdp
    mom "AHHH... HAAAHHH..."
    with vpunch
    miranda "Ohh... ohh..."
    pov "Haha, this time my slut won!"
    davide "Haha, you're right. But don't worry this slut will regret losing..."
    miranda "Hah... yes, punish me more, hah... harder...!"
    mom "Hah... hah... [pov]..."
    jump baseorgyend
#----- Twisted Paths - Love version of Corruption Events ----- Done

#----- Basement Orgy Corruption to Love Event Cassandra ----- Done - Create Option in Menu above
label baseorgycaslove:
    povi "Ok, this is just like we talked about. [bs] and I will keep up the ruse, while I try to protect from Davide."
    scene basement 10pm 120a
    povi "Seriously Bruce?! Could you perv on her any harder right now? Well, I got to play the part right..."
    pov "Hey, pervert!"
    scene basement 10pm 121a
    dad "Huh [pov]? Don't scare me like that."
    pov "Did I interrupt you staring at something, haha?"
    dad "What? No! I... what do you mean?"
    scene basement 10pm 122a
    if inc == True:
        pov "Enjoying the view of my sister's ass?"
    else:
        pov "Enjoying the view of [bs]'s ass?"
    dad "What...?"
    pov "I mean, I can't blame you. Seeing her like that makes me want to mount her right here and now."
    dad "What are you talking about? I didn't..."
    pov "You can stop denying it. I know what I saw."
    dad "But..."
    pov "Slut!"
    scene basement 10pm 123a
    bs "Huh? Oh hi, [pov]."
    pov "That's a nice outfit you're wearing."
    bs "Thank you."
    if inc == True:
        pov "But crawling on the floor with that outfit on is giving dad naughty ideas."
    else:
        pov "But crawling on the floor with that outfit on is giving Bruce naughty ideas."
    bs "Huh?"
    dad "I told you..."
    pov "He can't take his eyes off your hot ass!"
    scene basement 10pm 124a
    if inc == True:
        bs "Dad!"
    else:
        bs "Bruce!"
    dad "Why are you doing this to me? Embarrassing me like that?"
    pov "Because you seem to think it's ok staring at MY slut like that!"
    povi "And you pretty much put me in this situation..."
    dad "But I didn't..."
    povi "Time to play the asshole."
    if inc == True:
        pov "Oh, shut up, dad!"
    else:
        pov "Oh, shut up, Bruce!"
    scene basement 10pm 125a
    pov "Wait, did you do this on purpose slut, teasing him like that?"
    bs "N... No!"
    pov "You're allowed to tease him if you want to, but if you ever let anyone else touch you, you'll be banned from the gang forever."
    bs "I won't do that [pov]."
    pov "You won't do it, because...?"
    bs "Be... because I'm your slut."
    pov "Yes, you are."
    povi "I swear this is just like watching a nature documentary. I have to mark my territory to keep other assholes from taking it..."
    pov "How about you show us some of that hot body of yours. I think we've earned a show after all that teasing."
    bs "Y... yes [pov]."
    scene basement 10pm 126a
    "You push the table away to make some room for her."
    if inc == True:
        pov "Go on, show dad and I what a hot slut you are!"
    else:
        pov "Go on, show Bruce and I what a hot slut you are!"
    bs "Y... yes..."
    "She begins to dance slowly."
    pov "She's so fucking hot!"
    scene basement 10pm 127a
    if inc == True:
        dad "Hey! Don't talk about your sister like that."
    else:
        dad "Hey! Don't talk about her like that."
    pov "Seriously, you're saying that to me? After I caught you eye-fucking her just now... But don't worry, you're not worth getting angry over."
    pov "You should turn your head, I know you want to see this too."
    dad "This is totally crazy. You better stop before you cross a line you can't come back from."
    povi "Really wish I could, but this is where we're at until I find us a way out of your mess."
    pov "Haha, are you jealous?"
    scene basement 10pm 128a
    pov "Look at her! She was born to please with that hot body."
    pov "She even made her tits bigger to get more attention."
    pov "She's going to become the perfect slut and I'm sure she'll enjoy doing it."
    pov "I'm getting a little too good at playing the asshole role these days."
    dad "..."
    pov "Haha, speechless? I knew it."
    scene basement 10pm 129a
    pov "Look at that perfectly round ass and you can even get a glimpse of her wet pussy."
    dad "S... stop it."
    pov "Oh I don't think so. I'm far away from done here."
    pov "Think about standing up right now and ramming deep inside her, giving her a thick hard dick, which she's been craving all day."
    bs "Hnng..."
    povi "Did she just moan? I mean, she's crazy hot right now, but we're trying to get through tonight, without incident."
    povi "Then again, maybe we can have a little fun too..."
    pov "Slut!"
    scene basement 10pm 130a
    bs "Yes?"
    pov "Your teasing has pushed all the right buttons, now it's time you please me with that hot body of yours!"
    bs "R... right now?"
    pov "Yes! Right here, right now!"
    povi "I think she's feeling it too, we'll see."
    scene basement 10pm 131a
    bs "Ok [pov], I'll please you."
    povi "She seems hesitant. Probably this whole thing with Bruce is making her nervous."
    povi "We just need to keep up appearances. If she's not into it, we'll just fake it."
    pov "You will come over here and..."
    call screen baseorgycaschooselove

screen baseorgycaschooselove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "edited/gui/vice/icon_blowjob_love_%s.png" action (Hide('baseorgycaschooselove'), Jump('baseorgycasbjlove')) hovered tt.Action ("Blowjob") focus_mask True
        imagebutton auto "edited/gui/vice/icon_sex_love_%s.png" action (Hide('baseorgycaschooselove'), Jump('baseorgycassexlove')) hovered tt.Action ("Cowgirl") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgycasbjlove:
    scene basement 10pm 132a
    dad "You can't be serious!"
    dad "It's so wrong that you even want to do this with her..."
    dad "...but especially here, right now, that is the worst."
    povi "If I get him angry enough, I bet he'll leave again."
    pov "Wanna watch, haha?"
    pov "Or maybe get a turn after me?"
    dad "Grrr..."
    scene basement 10pm 133a
    dad "I'm out of here, I don't need to see this!"
    bs "Hnng..."
    dad "You're going down a path, where there's no return."
    pov "Haha, maybe, but it'll be a journey of pleasure and fun."
    scene basement 10pm 134a
    bs "Did I really turn you on that much?"
    povi "Wow, she definitely seems into it now."
    povi "I think she just didn't want to do things in front of Bruce, which I can't really blame her for that either."
    pov "Of course, you selected a great outfit and looked fantastic dancing."
    scene basement 10pm 135a
    bs "I'm glad you liked it."
    pov "What's with the extra motivation you seem to have today?"
    bs "I... I'm not sure..."
    if inc == True:
        pov "<whisper> You don't have to do anything more if you don't want to, sis. I think a handjob would be enough to keep the others away from you."
    else:
        pov "<whisper> You don't have to do anything more if you don't want to, [bs]. I think a handjob would be enough to keep the others away from you."
    bs "What if... I want to?"
    povi "Oh, Well then, it would be rude of me to not let her, right?"
    "You raise your voice so everyone can hear you better for the ruse."
    pov "Go on then slut, don't just stare at me. My dick needs some attention."
    bs "Yes [pov]."
    scene basement 10pm 136a
    bs "<suck> <lick>"
    pov "Oh... yes..."
    pov "I think this is my favorite way to start the night, with a great blowjob from my slut."
    bs "<suck> <lick>"
    if inc == True:
        pov "<whisper> Is it wrong that I'm incredibly turned on right now? You and me sis, doing things in front of everyone?"
    else:
        pov "<whisper> Is it wrong that I'm incredibly turned on right now? You and me [bs], doing things in front of everyone?"
    scene basement 10pm 137a
    bs "<lick> <whisper> No, to be honest, I think it's pretty damn hot too."
    if inc == True:
        pov "<whisper> Well that's good then, because mom is watching us right now..."
    else:
        pov "<whisper> Well that's good then, because your mom is watching us right now..."
    bs "<lick> <whisper> She's watching us while I'm licking your dick?"
    scene basement 10pm 161
    pov "<whisper> Yes and she seems to be very jealous of you."
    bs "<lick> Hmm..."
    if inc == True:
        pov "<whisper> But dad is still freaking out and he doesn't even realize she's staring at us."
    else:
        pov "<whisper> But Bruce is still freaking out and he doesn't even realize she's staring at us."
    bs "Hnng..."
    pov "Ohhh... yes..."
    if casbjdt > 2:
        scene basement 10pm 138dt
    else:
        scene basement 10pm 138a
    bs "<suck> <suck>"
    if inc == True:
        pov "Holy shit! That's good, sis!"
    else:
        pov "Holy shit! That's good, [bs]!"
    bs "<suck> Yessh..."
    povi "There are times when I'm actually a little glad we have to put on our show for the gang."
    scene basement 10pm 162
    if inc == True:
        pov "<whisper> Mom is so angry right now. I think she's blaming Bruce for this."
    else:
        pov "<whisper> Your mom is so angry right now. I think she's blaming Bruce for this."
    bs "Hnng... <suck> <suck>"
    if casbjdt > 2:
        scene basement 10pm 138dt
    else:
        scene basement 10pm 138a
    pov "Oh shit, your blowjobs are getting even better, I'm so close."
    call screen baseorgycasbjchooselove

screen baseorgycasbjchooselove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "edited/gui/vice/icon_mouth_love_%s.png" action (Hide('baseorgycasbjchooselove'), Jump('baseorgycasbjinlove')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "edited/gui/vice/icon_blowjob_love_%s.png" action (Hide('baseorgycasbjchooselove'), Jump('baseorgycasbjoutlove')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgycasbjinlove:
    pov "I want you to swallow my cum!"
    bs "Hmm..."
    pov "Oh yes, ARGHHH...!"
    if casbjdt > 2:
        scene basement 10pm 138dt
        with vpunch
    else:
        scene basement 10pm 139ai
        with vpunch
    bs "<gulp> <gulp>"
    povi "Shit, I need to rememeber to keep up appearances."
    pov "Yes, good slut! <loudly>"
    scene basement 10pm 140ai
    bs "Aahh..."
    pov "oh, that's a nice surprise. You want to be a good slut and show me some of my handiwork."
    "She nods in agreement."
    pov "You can swallow the rest now."
    scene basement 10pm 141ai
    bs "<gulp>"
    bs "Hmm..."
    pov "<whisper> That was perfect, they seemed to believe our performance."
    scene basement 10pm 142ai
    bs "Aahh... good."
    povi "I don't know if she's showing me she swallowed it all because she's still putting on a show for everyone, or she just wanted to... but it's crazy hot!"
    "She stands up and stretches out a bit in front of you and again you wonder if she's showing off for the group, or just for you."
    scene basement 10pm 126a
    bs "I know you did. <giggle>"
    pov "Well this was definitely an incredible blow job."
    pov "Keep up this up or better yet, surpass this level and I'll be very pleased."
    bs "Yes [pov]."
    povi "Well, that should do it for now."
    jump baseorgycasend

label baseorgycasbjoutlove:
    pov "I'm going to cum on your face."
    bs "Hmm..."
    pov "Oh yes, ARGHHH...!"
    scene basement 10pm 139ao
    with vpunch
    bs "Hmm..."
    povi "Shit, I need to rememeber to keep up appearances."
    pov "Yes, good slut! <loudly>"
    scene basement 10pm 140ao
    bs "Aahh..."
    pov "Oh what a nice view. My slut covered with my cum."
    bs "Yes."
    pov "And you even got some in your mouth so you can have a little taste too."
    bs "Hmm..."
    pov "<whisper> That was perfect, they seemed to believe our performance."
    "She stands up and stretches out a bit in front of you and again you wonder if she's showing off for the group, or just for you."
    scene basement 10pm 126a
    bs "I know you did. <giggle>"
    pov "Well this was definitely an incredible blow job."
    pov "Keep up this up or better yet, surpass this level and I'll be very pleased."
    bs "Yes [pov]."
    povi "Well, that should do it for now."
    jump baseorgycasendlove

label baseorgycassexlove:
    scene basement 10pm 132a
    dad "You can't be serious!"
    dad "It's so wrong that you even want to do this with her..."
    dad "...but especially here, right now, that is the worst."
    povi "I need to make him angry, he tends to run away when he's pissed."
    pov "Wanna watch, haha?"
    pov "Or maybe get a turn after me?"
    povi "Like I'd ever let him. Ha!"
    dad "Grrr..."
    scene basement 10pm 133a
    dad "I'm out of here, I don't need to see this!"
    bs "Hnng..."
    dad "You're going down a path, where there's no return."
    pov "Haha, maybe, but it'll be a journey of pleasure and fun."
    scene basement 10pm 150
    pov "<whisper> Ok, I can leave this one if you don't want to go further. We can just grind and put on a show."
    bs "<whisper> No, it's ok. I want to. It's kinda hot with everyone watching."
    povi "Well damn, it would just be rude not to give the lady what she wants, right?"
    pov "I'll help you to remove that patch so I can fuck you properly. <loudly>"
    bs "Hnng..."
    povi "This is going be interesting."
    scene basement 10pm 151
    pov "<whisper> What's wrong? I thought you said you wanted to do this."
    bs "Hnng... <whisper> I do..."
    pov "<whisper> Really? Look you don't have to go all this way right now just for this little show we have to do. I wouldn't blame you."
    bs "<whisper> I want you to tell me to do it... so everyone can hear..."
    povi "Wow, I realized she liked an audience on our dates, but she's really getting into this."
    povi "This will go will with Davide though, he loves it when you take control of your \"bitches\"."
    pov "<loudly> Well, get to it slut. Put mh fat cock inside you!"
    bs "Mmmm..."
    pov "You need to follow my orders, if you want to continue to be a part of the gang."
    bs "Hnng..."
    pov "Just sit on my lap and let my dick slide inside you. I'm sure you'll forget your worries in no time."
    bs "..."
    pov "NOW SLUT!"
    scene basement 10pm 152
    pov "Good, now put it in for me."
    bs "Hnng..."
    povi "Wow, she's dripping down there. I gotta admit, it's turning me on a lot more than I would like to admit."
    if inc == True:
        povi "Oh, mom has noticed us."
    else:
        povi "Oh, [mother] has noticed us."
    pov "Your pussy is so wet [bs]. You don't need to wait any longer."
    bs "Hmm..."
    scene basement 10pm 153
    bs "Aaahh..."
    "You nearly forget you're supposed to be putting on a show as she slides her tight wet pussy down to the hilt of your cock."
    pov "Anghh... You took it all in at once. What a naughty slut you are."
    bs "Hnn... so big."
    pov "Now start riding me and let's enjoy a good fuck!"
    if inc == True:
        bs "Y... yes, brother."
    else:
        bs "Y... yes, [pov]."
    "She starts riding you."
    bs "Ahh... hah..."
    scene basement 10pm 154
    pov "See, you already forgot about those worries floating through your mind a moment ago."
    bs "Yeah, thanks to you [pov]."
    pov "Go faster!"
    bs "Yes..."
    "She's riding you faster."
    pov "<whisper> Don't know if you want me to tell you this but..."
    scene basement 10pm 161
    if inc == True:
        pov "Mom is watching us."
        bs "Mom?"
    else:
        pov "Your mom is watching us."
        bs "My mom?"
    povi "Wow, she's even tighter now."
    pov "<quietly> She acting rather jealous right now."
    bs "Hah... hah..."
    pov "<quietly> And that idiot Bruce is so busy freaking out, he doesn't even realize it, haha."
    scene basement 10pm 155
    "You start playing with her tits."
    pov "You like it when I'm rough with them, don't you?"
    bs "Yes... it's feels so good... [pov]!"
    if inc == True:
        pov "<quietly> Is it crazy that I'm incredibly turned on right now? You and me sis, fucking in front of everyone?"
    else:
        pov "<quietly> Is it crazy that I'm incredibly turned on right now? You and me, fucking in front of everyone?"
    bs "<quietly> No, hnng... I think it's pretty damn hot too."
    bs "Hah, yes... I'm... your slut."
    scene basement 10pm 162
    if inc == True:
        pov "<whisper> Mom is so angry right now. I think she's blaming Bruce for this."
    else:
        pov "<whisper> Your mom is so angry right now. I think she's blaming Bruce for this."
    "You feel her spasm around your cock, squeezing it even tighter."
    bs "Hah... AAAHH..."
    pov "<whisper> You're getting close?"
    scene basement 10pm 157
    bs "Yes... yes..."
    pov "<quietly> Me too. <loudly> Let's cum together slut! Receive your well earned reward!"
    bs "Yes [pov]! I want to cum with you!"
    call screen baseorgycasfuckcumlove

screen baseorgycasfuckcumlove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_pussy_%s.png" action (Hide('baseorgycasfuckcumlove'), Jump('baseorgycasfuckcuminlove')) hovered tt.Action ("Cum in her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_belly_%s.png" action (Hide('baseorgycasfuckcumlove'), Jump('baseorgycasfuckcumoutlove')) hovered tt.Action ("Cum on her belly") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgycasfuckcuminlove:
    pov "I'm going cum inside your pussy!"
    bs "Yes, hah... cum inside me..."
    if inc == True:
        pov "You want me to cum deep inside you, big sis?"
        bs "Yes, brother... I'm so close... hah..."
    else:
        pov "You want me to cum deep inside you, slut?"
        bs "Yes, [pov]... I'm so close... hah..."
    pov "With pleasure!"
    bs "AAHHH... HAAAAHHH...!"
    scene basement 10pm 156
    with vpunch
    "She cums while you pump hot cum inside her."
    bs "Ahh... I can feel it... so warm..."
    pov "Oh yes..."
    "She slowly stands up from your lap, letting your cock slip out with a wet sloppy pop."
    scene basement 10pm 159i
    pov "Such a nice view!"
    pov "Don't clean it up though, I want to see everybody what I did to my slut!"
    bs "O... OK [pov]."
    pov "<whisper> That was perfect, they seemed to believe our performance."
    bs "I know you did. <giggle>"
    pov "Well that was defintely an amazing ride."
    pov "If we fuck more often, I'll be very pleased."
    bs "Yes [pov]."
    povi "Well, that should do it for now."
    jump baseorgycasendlove

label baseorgycasfuckcumoutlove:
    pov "I'll cum on your stomach!"
    bs "Yes, hah... Cum over me..."
    if inc == True:
        pov "You want me to cum all over your body, big sis?"
        bs "Yes, brother... I'm so close... hah..."
    else:
        pov "You want me to cum all over your body, slut?"
        bs "Yes, [pov]... I'm so close... hah..."
    pov "With pleasure!"
    bs "AAHHH... HAAAAHHH...!"
    scene basement 10pm 158o
    with vpunch
    "She cums while you spray your hot cum all over her."
    bs "Ahh... I can feel it... so warm..."
    pov "Oh yes..."
    "She slowly stands up from your lap."
    scene basement 10pm 159o
    pov "Such a nice view!"
    pov "Don't clean it up though, I want to see everybody what I did to my slut!"
    bs "O... OK [pov]."
    pov "<whisper> That was perfect, they seemed to believe our performance."
    bs "I know you did. <giggle>"
    pov "Well that was defintely an amazing ride."
    pov "If we fuck more often, I'll be very pleased."
    bs "Yes [pov]."
    povi "Well, that should do it for now."
    jump baseorgycasendlove

label baseorgycasendlove:
    pov "Rest now slut, maybe I'll use you again later."
    bs "Yes... [pov]... hah..."
    povi "Hopefully, that gave Davide the message that she's mine and he'll stay away from her."
    jump basementorgyaoamenu

#----- Basement Orgy Corruption to Love Event - Tug o War - Done
label baseorgyaoalove:
    scene black
    "You decided to check on Davide and [miranda] to make sure they aren't going to cause problems."
    scene basement 10pm 103a
    pov "Hey..."
    davide "Oh, hey [pov]."
    miranda "Well hello good looking..."
    povi "She's flirting with me again."
    davide "Treat him with respect slut. That's a fucking gang member your speaking to now!"
    povi "Well at least they are predictable."
    scene basement 10pm 104m
    miranda "Wow, that's great. Congratulations!"
    pov "Thank you."
    miranda "Now you're one them, I look forward to getting to know you more. I'm friends with all the gang members"
    davide "Haha, she loves being a slut."
    miranda "<giggle>"
    scene basement 10pm 105m
    pov "I see someone is ready to party."
    povi "She's going to poke someone's eyes out with those."
    miranda "I can't wait to show you what you been missing! A good looking stud like you needs to be pleased!"
    mom "[miranda]!"
    if inc == True:
        povi "Seriously mom! We need to not rock the boat. We're trying to avoid them getting interested in anyone else. I can handle this."
    else:
        povi "Seriously mom! We need to not rock the boat. We're trying to avoid them getting interested in anyone else. I can handle this."
    scene basement 10pm 106m
    mom "What do you think you're doing?"
    mom "Get away from him!"
    scene basement 10pm 107m
    miranda "..."
    davide "Haha, of course [mother] is angry again."
    if inc == True:
        davide "She thinks she needs to protect her son from our biggest slut."
    else:
        davide "She thinks she needs to protect you from our biggest slut."
    mom "Come here, you whore!"
    scene basement 10pm 108m
    mom "I'll rip your ass off if you lay a finger on him!"
    miranda "Haha, You can't be around him all the time. Sooner or later he'll taste a lot more of me than my finger."
    mom "Grrr..."
    pov "Well... shit."
    scene basement 10pm 110m
    davide "Don't look so shocked, haha."
    davide "They fight all the time, but it never gets violent."
    if inc == True:
        davide "Your mom hates her. Something that went down a while back, I don't give a two shits about it. But it's funny as hell."
    else:
        davide "[mother] hates her. Something that went down a while back, I don't give a two shits about it. But it's funny as hell."
    pov "So they fight all the time?"
    davide "Yes, I think it's very entertaining."
    if inc == True:
        povi "Entertaining? I'm trying to keep Davide's attention away from mom."
    else:
        povi "Entertaining? I'm trying to keep Davide's attention away from [mother]."
    povi "This is the exact opposite of that."
    pov "Oh really?"
    scene basement 10pm 109m
    davide "Haha, hell yes."
    davide "Watch, we'll set up some challenges for them, so they can prove which of them is the better slut and we just sit back enjoy the show. Better than fucking pay-per-view!"
    povi "So... I'm 90% sure these ideas game to him while watching reality tv. I can hear him now..."
    povi "\"You know what the Survivors is really missing? Bitches fucking, but without those tiny little boxes over their junk.\""
    pov "Haha, so you're really not worried that they'll actually hurt each other?"
    davide "Fuck if I know, but they haven't yet. I think they're just talking smack."
    davide "But there isnt much else we'll be able to get them to do while their all fired up like that."
    pov "What challenge did you have in mind?"
    davide "I'll show you one of my favorites, I call it \"Ass to Ass\"."
    pov "Haha, Ok, now I'm curious."
    davide "They get a double-sided dildo stuffed in their pussies and then they have to try to get the other one off."
    pov "First one to orgasm loses, I'm assuming?"
    davide "Now you got it! We have them do it in doggy style. And that's why I call it \"Ass to Ass\"."
    pov "So what's the prize?"
    scene basement 10pm 111m
    davide "These..."
    if momsecret == True:
        pov "But [mother] can't take those."
        davide "True, only [miranda] can win one."
    else:
        davide "But since [mother] can't have them, only [miranda] can win one."
        pov "[mother] can't use them?"
        davide "Yeah, she gets sick and pukes it all out. Maybe she's allergic or some shit, I don't know."
        pov "Oh, I didn't know that."
        $ momsecret = True
    if inc == True:
        pov "So how do we get my mother motivated to win then?"
    else:
        pov "So how do we get [mother] motivated to win then?"
    davide "Haha, she'll do anything to make sure [miranda] doesn't win."
    pov "Wow, there's so much hate there..."
    davide "Yeah for both of them. Sometimes [miranda]'s drive to make [mother] fail is even bigger."
    povi "I knew they didn't like each other, but I didn't figure them for some sort of rivals..."
    scene basement 10pm 112m
    povi "Well this should be better than Davide getting involved directly. I guess we just go with it for now."
    pov "Well I shouldn't be surprised by our biggest slut's drive, right?."
    davide "Haha, yeah."
    davide "Let's get this game going."
    scene black
    "Davide starts running his mouth about how [mother] could never beat [miranda] and in just moments, they were ready to compete in front of everyone."
    scene basement 10pm 113m
    pov "What a nice view!"
    davide "Haha, see! It's just like I told you."
    pov "And now we just sit back and watch?"
    davide "Yes, but we need to choose our players first. We want the sluts to give it their best to impress us."
    pov "Oh this gets even better!"
    if inc == True:
        davide "You probably better side with your mother for this first time, she's your slut after all."
    else:
        davide "You probably better side with [mother] for this first time, she's your slut after all."
    povi "Oh, I was going to."
    davide "I'll side with [miranda]."
    pov "Ok, I'm sure my slut will give her best!"
    mom "I will [pov]."
    miranda "Haha, you wish! You're definitely gonna lose."
    davide "Get ready."
    scene basement 10pm 114m
    mom "Hnng..."
    miranda "Hah..."
    povi "Ok, I know I'm supposed to be here to help the girls stay out of trouble... But come on! I'm only human!"
    scene basement 10pm 115m
    davide "You sit on the other side, so you can cheer on your slut better."
    pov "Now I'm wondering if that's why these chairs were setup this way to begin with, haha?"
    davide "Well it is one of my favorites!"
    pov "Let's do this."
    scene basement 10pm 116m
    pov "We have to win this!"
    mom "Yes, I'll give my best."
    if inc == True:
        pov "<whisper> I'm sorry, mom. I figured this would be better than letting Davide get other ideas about what to do to pass the time down here."
        mom "<whipser. It's alright, son. I know you're doing your best. Just keep playing the bad guy for now. I trust you.>"
    else:
        pov "<whisper> I'm sorry, [mother]."
        mom "<whipser. It's alright, [pov]. I know you're doing your best. Just keep playing the bad guy for now. I trust you.>"
    pov "Don't just try, you need to win. Everyone needs see that I chose the right slut!"
    if inc == True:
        pov "That you're my slut, mom!"
    else:
        pov "That you're my slut, [mother]!"
    mom "Yes, I'll win for you [pov]!"
    davide "How about we start? Three... Two... One... GO!"
    scene basement 10pm 117m
    miranda "Huh? Haah...!"
    mom "Hnng!"
    davide "Wow, that's an agressive start from [mother]. Pushing it all in, what a surprise!"
    povi "Ok, was that just me or was Davide channeling he inner sports announcer?"
    davide "Don't disappoint me, slut!"
    miranda "I won't, hah..."
    "[miranda] starts to fuck back and they fall into a rhythm."
    scene basement 10pm 118m
    mom "Hnng...! Hah... hah..."
    davide "Harder slut!"
    miranda "Yes... aaah... hah..."
    if inc == True:
        pov "You can do this mom."
    else:
        pov "You can do this [mother]."
    mom "Hah... yes..."
    scene basement 10pm 119m
    mom "Hmm...! Hah... Haaaah..."
    miranda "Hnng! Hnng! Hah..."
    davide "Having fun on the other side [pov]?"
    pov "Haha, yes. That shit is great!"
    if inc == True:
        povi "So... yeah... I'm actually having fun right now. Probably best not to share that information with mom later. I feel guilty enough as it is."
    else:
        povi "So... yeah... I'm actually having fun right now. Probably best not to share that information with [mother] later. I feel guilty enough as it is."
    call screen baseorgyaoawinlove

screen baseorgyaoawinlove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("[mother] wins (coming soon)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("It's a tie (coming soon)") focus_mask True
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyaoawinlove'), Jump('baseorgyaoamirwinlove')) hovered tt.Action ("[miranda] wins") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyaoamirwinlove:
    scene basement 10pm 120m
    mom "Oh no! Hah... Ahh... hah..."
    pov "What do you mean \"Oh no\"?"
    mom "I'm so... hah... close..."
    davide "You hear that [miranda]? Finish her!"
    povi "Test your might, fight! God damn it! Get out of my head Mortal Kombat!"
    pov "Don't you dare to lose, slut!"
    mom "I... I... Hah..."
    scene basement 10pm 121m
    mom "AAAHHH... HAAAHHH..."
    with vpunch
    "She cums hard in front of you."
    mom "I'm... so... sorry... hah... haaahh..."
    povi "She does know that she doesn't have to apologise to me right? This was all for show anyway."
    miranda "Yes! Hnng!"
    scene basement 10pm 122mm
    miranda "Hah, that's right, I did it. I finished that slut!"
    davide "Good job!"
    mom "Hnng... Hnn..."
    pov "<quietly> It's ok. You did good. And Davide is focusing all his attention on [miranda] right now, so it worked."
    scene basement 10pm 123mm
    miranda "Can I get my prize now? We all knew I'd win anyways!"
    davide "Relax, slut. You'll have plenty of fun with your prize soon."
    mom "I... I'm so sorry. Please forgive me [pov]."
    povi "Why is she acting like she actually let her down. It's got to be because she actually wanted to beat [miranda]. I need to find out what happened between them."
    pov "I just don't know if I can. You made me lose face in front of Davide."
    scene basement 10pm 124mm
    miranda "<giggle> Maybe you should choose me next time [pov]."
    miranda "I can last a long time, but I'm sure your big dick will make me cum in no time."
    povi "She just can't stop herself from teasing."
    mom "Hnng...!"
    if inc == True:
        povi "Mom looks so humiliated right now."
    else:
        povi "[mother] looks so humiliated right now."
    povi "I'm so sorry."
    pov "You'll do better next time, I know it... Slut!"
    povi "Almost forgot we're still putting on a show here for them."
    mom "I'm sorry [pov]. I can do better."
    scene basement 10pm 125mm
    if inc == True:
        povi "[bs] looks so embarassed over there. Who can blame her. She just had to watch our mother get off in front of everyone for sport."
        pov "She shouldn't have to watch our mother lose like that."
    else:
        povi "[bs] looks so embarassed over there. Who can blame her. She just had to watch her mother get off in front of everyone for sport."
        pov "She shouldn't have to watch her own mother lose like that."
    mom "What..."
    scene basement 10pm 126mm
    mom "Please forgive me [pov], I'm so sorry."
    pov "<quitely> Sorry about that. I didn't mean to say that out loud. I don't blame you. I'm just pissed we have to go through all of this."
    mom "<quitely> I know you're doing your best. I love you so much. We're lucky you've returned to us."
    pov "<quitely> I don't know about all of that, but I appreciate it. We better get back to pretending again."
    pov "Or maybe I should choose [miranda]?!"
    scene basement 10pm 129mm
    mom "No! You chose me! I'll be better. I'll do anything. Anything!"
    povi "She does this so well. Sometimes I forget we're just playing our roles down here."
    if inc == True:
        mom "I'm your mother. I raised you and I know you best. I'm the one who can please you the most!"
    else:
        mom "I'm your mother's best friend. I helped raise you and I know you best. I'm the one who can please you the most!"
    scene basement 10pm 127mm
    miranda "Hmm..."
    povi "And now [miranda] is going to try to start something..."
    scene basement 10pm 128mm
    miranda "I'm so horny right now. Victory feels so good."
    miranda "Hey [pov]! Do you want to have a real slut please you for once?"
    povi "She does have a nice body."
    scene basement 10pm 129mm
    mom "Pleeease [pov]..."
    if inc == True:
        povi "My mom is begging me for my dick. With that look in her eyes, I really think it's not all an act for the gang."
    else:
        povi "[mother] is begging me for my dick. With that look in her eyes, I really think it's not all an act for the gang."
    povi "I think she actually wants to do thing with me down here."
    povi "But what's with Davide? He's just watching me. I guess he's waiting to see what I do."
    call screen baseorgyaoanicloselove

screen baseorgyaoanicloselove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyaoanicloselove'), Jump('baseorgyaoaniclosedemlove')) hovered tt.Action ("Forgive her") focus_mask True
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyaoanicloselove'), Jump('baseorgyaoanicpunishlove')) hovered tt.Action ("Forgive her, but put on a act of punishing her as well") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("Have fun with [miranda] (soon)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyaoaniclosedemlove:
    pov "I'll forgive you this time. Just don't for get, you did say anything..."
    mom "Anything, I'll do anything."
    call screen baseorgyaoaniclosedemchlove

screen baseorgyaoaniclosedemchlove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyaoaniclosedemchlove'), Jump('baseorgyaoaniclosedempilllove')) hovered tt.Action ("[mother]'s request") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("More choices soon...") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action NullAction() hovered tt.Action ("Nothing for now (soon...)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyaoaniclosedemnolove:
    pov "I suppose you've learned a lesson, so I'll just punish you for your loss today and we'll leave it at that."
    pov "<whisper> I'll pretend to be rough with you, but this way no one else will bother you if you with me."
    mom "<whisper> Thank you [pov]. For everything."
    mom "Yes, I need to be punished."
    jump baseorgyaoanicpunishlove

label baseorgyaoaniclosedempilllove:
    mom "I have something to ask you."
    if nicolebabywant == False:
        mom "Were you serious before, about wanting to make me pregnant?"
    else:
        mom "Have you thought about... getting me pregnant?"
    scene basement 10pm 130mm
    if nicolebabywant == False:
        pov "Yes, I wouldn't have said it if I wasn't."
    else:
        pov "Well, yeah. It's crossed my mind that you could get pregnant since we are lovers."
    scene basement 10pm 131mm
    mom "So do you want to?"
    if inc == True:
        mom "You're my son and I want you to breed me..."
    else:
        mom "You're my best friend's son and I want you to breed me..."
    pov "...ok."
    pov "I want that too. So let's do it. No more waiting."
    scene basement 10pm 132mm
    mom "Hnng..."
    pov "<whisper> I think we should make a big show of this, Davide eats this stuff up and it will help me claim you in his eyes even more. Which will protect you."
    "She nods in agreement and starts the show..."
    mom "Ok, I'll do it! I'll stop taking birth control and let you breed me."
    mom "Please [pov]... breed me!"
    if inc == True:
        povi "My mom's begging for me to breed her... It's so hot, no matter what the circumstances!"
    else:
        povi "[mother]s begging for me to breed her... It's so hot, no matter what the circumstances!"
    pov "Perfect, let's seal the deal with sex."
    pov "I want you to take the lead. Show me how much you want my seed inside you."
    mom "Y... yes [pov]."
    scene basement 10pm 128mm
    pov "I'll have fun with my slut now."
    if NTR == True and momrelationship < 5 or hardntr == True:
        jump baseorgyaoanicNTR
    miranda "And what about me? I won the game..."
    povi "Should Davide have some fun too or not?"
    call screen baseorgyniclosedavidelove

screen baseorgyniclosedavidelove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('baseorgyniclosedavidelove'), Jump('baseorgyniclosedavideyeslove')) hovered tt.Action ("He can have fun with [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('baseorgyniclosedavidelove'), Jump('baseorgyniclosedavidenolove')) hovered tt.Action ("I don't want him to touch her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyniclosedavideyeslove:
    $ baseorgyaoaniclosedavy = True
    pov "You'll please Davide. I'm sure he'll help you have fun.!"
    miranda "But I want you... OK."
    davide "Don't worry slut, I'm sure you'll enjoy your victory still, haha."
    jump baseorgyaoaniclosedem2love

label baseorgyniclosedavidenolove:
    pov "Do what you want, it's your victory."
    miranda "But I want you!"
    davide "Ouch, haha."
    pov "I can't now I'm afraid! I need to punish my slut."
    miranda "Oh..."
    miranda "I'll have some fun with the sybian then."
    davide "Damn, you chose a sybian over me huh? Well, good sluts should get to choose. You better believe I'm gonna watch though!"
    jump baseorgyaoaniclosedem2love

label baseorgyaoaniclosedem2love:
    scene black
    mom "Please lay back on the table."
    "You lay down on the table."
    scene basement 10pm 133mn
    pov "You seem very motivated now."
    mom "I am. I'm going to prove to you that I'm better then [miranda]!"
    pov "Good slut! Then show me how much you're craving my seed."
    mom "Yes [pov]."
    scene basement 10pm 134mn
    mom "Hnng... hah..."
    pov "Oh yes... all in."
    scene basement 10pm 135mn
    mom "Now you know I can do better."
    if inc == True:
        povi "Ok, I know the situation is crazy, but holy shit this is hot. I'm going to impregnate my mom!"
    else:
        povi "Ok, I know the situation is crazy, but holy shit this is hot. I'm going to impregnate [mother]!"
    pov "Then ride me until I spray hot cum inside you!"
    mom "Yes [pov], give me your cum!"
    "She starts riding you."
    scene basement 10pm 136mn
    mom "Hah... hah... your big dick... so... good..."
    povi "Wow, she's putting on a hot show.."
    povi "I wonder if she remembers that [bs] is still here?"
    povi "What is [miranda] and Davide up to?"
    if baseorgyaoaniclosedavy == True:
        scene basement 10pm 134mdm
        povi "Strapping her in and going to work on her backside again. Classic."
        miranda "Oh yes, harder... ahh..."
    else:
        scene basement 10pm 133msyb
        miranda "Aaah... hah... so good..."
        povi "She is pretty damn hot, I'll give her that."
        scene basement 10pm 134msyb
        miranda "Oh YES! YES! Aaahh"
        davide "Wow, already number two in no time at all, haha."
    scene basement 10pm 137mn
    mom "Ohh... hah... ahhh..."
    if inc == True:
        mom "<whisper> I love you son!"
        pov "<whisper> I love you too mom!"
    else:
        mom "<whisper> I love you [pov]!pov "
        pov "<whisper> I love you too [mother]!"
    "You two share an intimate moment of silence between each other before going back to putting on the show for the others."
    pov "Do you want my sperm that badly?"
    mom "Yes, [pov]. Please! Cum inside me!"
    if inc == True:
        pov "That's it, I love how you're begging for my seed, mom!"
    else:
        pov "That's it, I love how you're begging for my seed, [mother]!"
    mom "Hah... hah..."
    pov "But I don't think everyone else heard you!"
    scene basement 10pm 137mnb
    mom "Huh? You want me to... tell them? Hah..."
    pov "Yes, I want you ride me even harder and then tell them that you're mine and I'm the only one allowed to breed you!"
    if inc == True:
        pov "Tell them how much you want to be my slut, mom!"
    else:
        pov "Tell them how much you want to be my slut, [mother]!"
    mom "But [bs] is still here!"
    pov "Do you really want to disappoint me again?"
    mom "No! I'll... do it for you [pov]!"
    "She begins to ride you harder."
    scene basement 10pm 139mn
    mom "Hah... hah... Listen everyone...!"
    if inc == True:
        mom "I'm craving... hah... my son's seed..."
    else:
        mom "I'm craving... hah... [pov]'s seed..."
    mom "and I'm done taking the pill... hah... hah..."
    mom "so he can... can breed me properly... hah... ahh..."
    pov "Good, now let's cum together, slut!"
    povi "Let's see how the others react."
    scene basement 10pm 141mn
    if inc == True:
        povi "Looks like big sis is shocked. No wonder, mom did just announce to everyone her she wants to have a baby with me."
    else:
        povi "Looks like [bs] is shocked. No wonder, her mom did just announce to everyone her she wants to have a baby with me."
    if baseorgyaoaniclosedavy == True:
        scene basement 10pm 140mnb
        miranda "Ohhh...."
        povi "[miranda] is speechless. That'll make [mother] happy."
        davide "Yeah, go for it bro!"
        povi "It's crazy, he's really been treating me more like a friend these days instead of... whatever the hell he was treating me like before."
    else:
        scene basement 10pm 140mn
        miranda "Ohhh...."
        povi "[miranda] is speechless. That'll make [mother] happy."
        davide "Yeah, go for it bro!"
        povi "It's crazy, he's really been treating me more like a friend these days instead of... whatever the hell he was treating me like before."
    povi "Bruce is missing still... Did he leave again...?"
    scene basement 10pm 142mn
    mom "Hah... hah... I'm so close [pov]!"
    pov "Then cum with me!"
    mom "Yes, hah... AHHHH... I'm cumming [pov]!"
    with vpunch
    pov "Me too, argh..."
    with vpunch
    "You spray your cum deep inside her."
    scene basement 10pm 143mn
    mom "Your hot seed is inside me, hah..."
    povi "What a beautiful view."
    mom "Hah... hah... you're satisfied [pov]?"
    pov "Yes. For now..."
    povi "That was insane. Hot, but insane!"
    $ nicoleonpill = False
    $ baseorgyaoaniclosedavy = False
    jump baseorgyend

label baseorgyaoanicpunishlove:
    scene basement 10pm 128mm
    povi "Let's see what we'll do now."
    call screen baseorgyniclosepunchooselove

screen baseorgyniclosepunchooselove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('baseorgyniclosepunchooselove'), Jump('baseorgyniclosepunnicdavmirlove')) hovered tt.Action ("I'll punish my slut, you can have [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action NullAction() hovered tt.Action ("I'll punish my slut, [miranda] can choose herself (soon...)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label baseorgyniclosepunnicdavmirlove:
    if NTR == True and momrelationship < 5 or hardntr == True:
        jump baseorgyaoanicNTR
    scene black
    "You two prepare the girls."
    mom "Hnng...hah..."
    miranda "Ohhh... ohhh..."
    scene basement 10pm 133mdp
    "You both start to fuck them."
    pov "Now this is the way I like to punish a slut."
    davide "It's the best thing for them, they get all riled up again afterwards, haha."
    mom "Ahh... hah..."
    davide "How about we have ourselves a little competition to see which slut will orgasm first?"
    pov "Haha, I'm in."
    miranda "Hah... hah... not so rough..."
    davide "Shut up, slut!"
    scene basement 10pm 134mdp
    mom "Hah... hah... you're so rough..."
    pov "Of course I am! This is punishment slut! And you're not going to disappoint me again."
    mom "No, no, I won't. I'll cum hard and fast from your fat dick."
    povi "Hmm... Maybe I should make [bs] get us drinks to reinforce the idea that she's mine too. We're trying to protect everyone."
    scene basement 10pm 134mcas
    pov "Bring me and Davide a drink, slut!"
    davide "Nice idea, I could use a drink!"
    bs "Ok, [pov]."
    mom "No... hah... don't..."
    pov "Shut up, slut!"
    povi "Sorry about that. We need to do this to impress Davide so we'll leave you both alone."
    scene basement 10pm 135mcas
    bs "Here is your drink [pov]."
    if inc == True:
        pov "Watch closely how I punish mom for disappointing me!"
    else:
        pov "Watch closely how I punish your mom for disappointing me!"
    bs "Y-Yes, I will."
    mom "Hnng! Hnng!"
    pov "So do you agree with me that she needs a hard punishment?"
    bs "I... I do... [pov]!"
    pov "Good slut!"
    scene basement 10pm 136mcas
    bs "Here is your drink, Davide."
    miranda "Hah... hah..."
    davide "You're pretty damn lucky for having such obedient sluts!"
    pov "Oh yes, I am, haha. But I did have to tame this one a bit."
    with vpunch
    "You thrust your cock extra hard to help make your point."
    mom "AHHH... HAAHHH..."
    pov "You're close slut?"
    mom "Yes... hah..."
    scene basement 10pm 135mdp
    mom "AHHH... HAAAHHH..."
    with vpunch
    miranda "Ohh... ohh..."
    pov "Haha, this time my slut won!"
    davide "Haha, you're right. But don't worry this slut will regret losing..."
    miranda "Hah... yes, punish me more, hah... harder...!"
    mom "Hah... hah... [pov]..."
    jump baseorgyend

#----- Basement Orgy Scene Darker Paths ----- Done
label baseorgyaoanicNTR:
    call screen checkdarkerpaths_nicole
    scene basement 10pm 128mmntr
    davide "Oh... no, no, no!"
    davide "That is not how this works. I get to choose which slut you can have."
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            pov "Ok..."
        else: #nicole_ntr
            pov "Nooo..."
    elif nicole_revenge == True or nicole_sadist == True:
        if nicole_revenge == True:
            pov "hell no..."
        else: #nicole_sadist
            pov "For now maybe..."
    davide "I'm still the boss here!"
    davide "And I'll punish your slut, good and hard. You're going to reward [miranda] by fulfilling her wish."
    scene basement 10pm 132mm
    mom "No, not her."
    davide "Shut up slut!"
    mom "You need to stand up and do something..."
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            povi "Well, I don't really think that's my place here right now, besides we're all going to have fun here..."
            if inc == True:
                pov "I can't, I'm sorry, mom. Let's not rock the boat."
            else:
                pov "I can't, I'm sorry, [mother]. Let's not rock the boat."
        else: #nicole_ntr
            povi "Davide would beat me easily in a fight right now, god damn it..."
            if inc == True:
                pov "I can't, I'm sorry, mom. He would kick my ass..."
            else:
                pov "I can't, I'm sorry, [mother]. He would kick my ass..."
    elif nicole_revenge == True or nicole_sadist == True:
        if nicole_revenge == True:
            povi "Davide would probably beat me in a fight right now, damn it..."
            if inc == True:
                pov "I don't think I can mom. We just have to make through this for tonight. I'm so sorry."
            else:
                pov "I don't think I can [mother]. We just have to make through this for tonight. I'm so sorry."
        else: #nicole_sadist
            povi "Well if I gave a shit about what happens to you then maybe... But I really don't care who I fuck. And I like to see you upset."
            if inc == True:
                pov "I won't be doing that, mom."
            else:
                pov "I won't be doing that, [mother]."
    davide "Shut up you two. Let's get the sluts ready [pov]."
    scene black
    "You two prepare the girls."
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hnng... hah..."
    elif nicole_revenge == True or nicole_sadist == True:
        mom "Ouch... stop..."
    miranda "Ohhh... ohhh..."
    scene basement 10pm 133mNTR
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            "You both start to fuck them."
        else: #nicole_ntr
            "You both start to fuck them, even though you're seething at Davide right now."
    elif nicole_revenge == True or nicole_sadist == True:
        if nicole_revenge == True:
            "You both start to fuck them. There is nothing you can do to stop this yet. But soon Davide is going to get what he deserves!"
        else: #nicole_sadist
            "You both start to fuck them. Hard."
    miranda "See, your little boy is fucking me now... hah..."
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hmmm... hah... ouch... Davide, not so rough..."
    elif nicole_revenge == True or nicole_sadist == True:
        mom "No... hah... ouch... Davide, stop this..."
    davide "Shut the fuck up."
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            povi "Damn, this isn't what I wanted."
        else: #nicole_ntr
            povi "Noooo, this isn't what I wanted. I can't do anything to stop him. I'm so damn weak."
    elif nicole_revenge == True or nicole_sadist == True:
        if nicole_revenge == True:
            povi "God damn it! I hate this. I need to stop him somehow!"
        else: #nicole_sadist
            povi "Well now, this is starting to be a pretty good night."
    "Davide fucks her harder."
    miranda "Yes, fuck me boy... I love your young dick."
    if nicole_sadist == True:
        pov "Don't call me boy slut! Call me master!"
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Shut up... [miranda]... hah..."
    elif nicole_revenge == True or nicole_sadist == True:
        mom "Shut up... [miranda]... stop..."
    scene basement 10pm 134mNTR
    if nicole_voyeur == True or nicole_ntr == True:
        mom "AHH... HAH... HAH..."
    elif nicole_revenge == True or nicole_sadist == True:
        mom "You asshole! HAH... I HATE you Davide!"
    davide "Enjoy your punishment!"
    miranda "Thank you... so much... hah... for letting him fuck me, Davide."
    if nicole_sadist == True:
        pov "Bitch, don't thank him! I'm your master right now."
    davide "These sluts are talking too much. I need a drink."
    scene basement 10pm 134mcas
    davide "Bring us some drinks, slut."
    bs "Y...yes Davide."
    scene basement 10pm 135mNTRcas
    bs "Here is your drink Davide."
    davide "Good slut. Maybe I'll ravage your hot body later too."
    call screen checkdarkerpaths_cassandra
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hah... hah..."
    elif nicole_revenge == True or nicole_sadist == True:
        mom "Nooo... don't..."
    if cassandra_voyeur == True or cassandra_ntr == True:
        bs "Yes, you can have me later too, Davide."
    elif cassandra_revenge == True or cassandra_sadist == True:
        bs "..."
    if inc == True:
        davide "Give your brother the other drink."
    else:
        davide "Give [pov] the other drink."
    scene basement 10pm 136mNTRcas
    bs "Here [pov]."
    pov "Thank you, slut."
    miranda "Harder, harder, hah..."
    if cassandra_voyeur == True or cassandra_ntr == True:
        bs "Do I have to let Davide have his fun with me later?"
        bs "Can't you do something?"
    elif cassandra_revenge == True or cassandra_sadist == True:
        bs "Please don't let Davide have his fun with me later!"
        bs "Can't you do something?"
    if cassandra_voyeur == True or cassandra_ntr == True:
        if cassandra_voyeur == True:
            povi "I don't think I should. Davide is still in charge..."
            pov "I'm sorry [bs], but I can't. He's the leader after all, he get's to decide."
        else: #cassandra_ntr
            povi "I wish I could, seeing Davide fuck her too would be the very worst, but... he'd kill me."
            pov "I'm sorry [bs], but I can't do anything. He's the leader so... he get's to decide."
    elif cassandra_revenge == True or cassandra_sadist == True:
        if cassandra_revenge == True:
            povi "I really wish I could, seeing Davide fuck her too would horrible, but... I just don't have a way to stop him yet. I would risk making him really hurt that girls."
            pov "I'm sorry [bs], but I can't. Until we come up with a way to stop him for good, he's going to decide."
        else: #cassandra_sadist
            povi "Hell no. I want to see him rip your holes apart later."
            pov "No [bs], I won't be doing that. Until I'm in charge, he get's to decide."
    if cassandra_voyeur == True or cassandra_ntr == True:
        bs "Hnng..."
    elif cassandra_revenge == True or cassandra_sadist == True:
        bs "..."
    scene basement 10pm 135mNTR
    if nicole_voyeur == True or nicole_ntr == True:
        mom "HAAAHH... AAAHHH... YES!"
    elif nicole_revenge == True or nicole_sadist == True:
        mom "You bastard!... AAAHHH... NOOOO!"
    if inc == True:
        davide "Enjoy the screaming [pov] when I let your mom cum, haha!"
    else:
        davide "Enjoy the screaming [pov] when I let [mother] cum, haha!"
    if nicole_sadist == True:
        miranda "Oh yes, AAHHH, I'm cumming too. Harder, Master!"
    else:
        miranda "Oh yes, AAHHH, I'm cumming too. Harder, young stud!"
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            povi "At least everyone is having fun, just sucks I haven't gotten to cum yet."
        else: #nicole_ntr
            povi "That asshole, having fun with my slut and I didn't even get to cum."
    elif nicole_revenge == True or nicole_sadist == True:
        if nicole_revenge == True:
            povi "That fucker, treating her like that! I will stop him!"
        else: #nicole_sadist
            povi "The fuck is that about? I didn't even cum yet. Does the bitch thinks I'm done too?"
    scene black
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            "The fun for Davide continues throughout the night."
        else: #nicole_ntr
            "The fun for Davide continues throughout the night. Leaving you to scraps at best."
    elif nicole_revenge == True or nicole_sadist == True:
        if nicole_revenge == True:
            "Davide continues abusing the women throughout the night."
        else: #nicole_sadist
            "Davide continues abusing the women throughout the night. It would be a great night if you got more than scraps to yourself."
    scene basement 10pm 170NTR
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Ahh... hah... hah..."
    elif nicole_revenge == True or nicole_sadist == True:
        mom "Don't... please... just stop..."
    scene basement 10pm 171NTR
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            povi "Well at least I get to lick her all night."
        else: #nicole_ntr
            povi "I get to lick her all night. That's something at least... even if I can't do anything about the others."
    elif nicole_revenge == True or nicole_sadist == True:
        if nicole_revenge == True:
            povi "This would normally be a good time, but there is no way I can enjoy this with the others being treated like that."
        else: #nicole_sadist
            povi "Cum for me you whore!"
    scene basement 10pm 172NTR
    davide "Look how hard I fuck her!"
    if cassandra_voyeur == True or cassandra_ntr == True:
        bs "AAHHH... HAAHH... please, not so rough..."
    elif cassandra_revenge == True or cassandra_sadist == True:
        bs "Stop! Don't... please, it's too rough... just stop..."
    scene black
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            povi "Well that was a fun night."
        else: #nicole_ntr
            povi "Finally, this shitty night is over."
    elif nicole_revenge == True or nicole_sadist == True:
        if nicole_revenge == True:
            povi "Finally, this nightmare is over now."
        else: #nicole_sadist
            povi "Next time, I'm in fucking charge."
    jump skip

label baseorgyend:
    scene black
    "The fun continues over night."
    scene basement 10pm 171
    bs "Hah... hah..."
    scene basement 10pm 170
    if inc == True:
        pov "Receive my seed, mom!"
    else:
        pov "Receive my seed, [mother]!"
    scene basement 10pm 172
    miranda "Yes... more..."
    scene black
    "What a great night in the basement."
    jump skip

#----- 0.75 Part 2 Content ----- Done - All paths tested - Still need to clean up icons

#----- 7am Upstairs Bathroom Alexis Event Corruption ----- Done
label showerup7extcor:
    hide screen locations
    povi "Damn it, I need a way to get in there..."
    povi "..."
    povi "Hmm... maybe if I push her a it a little?"
    "Knock! Knock!"
    "You knock on the door loudly."
    ls "I'm showering, go away."
    pov "Hurry up and open the door!"
    ls "But I'm..."
    "Knock! Knock"
    pov "Come on! I need to get in!"
    ls "Hmpf!"
    scene showerupstairs 7am shower up 002
    if inc == True:
        ls "What is it, brother?"
    else:
        ls "What is it, [pov]?"
    povi "Wow, what a nice view."
    pov "I need to use the shower, I'm in a hurry!"
    scene showerupstairs 7am shower up 003
    ls "You need to wait until I'm done."
    povi "Hmm..."
    pov "I can't..."
    scene showerupstairs 7am shower up 002
    ls "Why...?"
    pov "I got an interview for a job."
    if inc == True:
        pov "You know how much mom wants me to get one."
    else:
        pov "You know how much your mom wants me to get one."
    povi "[ls] wants to help everyone, this is perfect."
    ls "Why don't you use the shower downstairs?"
    pov "You know we're not supposed to use that one."
    ls "Then I'll hurry up and finish and you can use it when I'm done!"
    pov "I have a better idea, why don't I just join you. I can wash up real quick and then you can finishing your shower..."
    pov "...and take all the time you need."
    ls "You can't be serious."
    pov "Come on... Please! I'm not going to make it otherwise."
    "You try to go further in the bathroom."
    if lilsiscorruption <= 39 and showbasealfirst == False:
        ls "No! Leave me alone!"
        pov "Huh?"
        ls "Leave now or I'll scream!"
        povi "Oh shit, she just isn't buying this. I better get out of here."
        scene black
        "You leave the bathroom and close the door."
        povi "Maybe if I keep trying to corrupt her she'll let me in next time."
        jump showerup
    ls "Well... I don't know..."
    "She seems to be overwhelmed from your insistence and is just staring at you."
    pov "Just keep showering, I'll undress and join you."
    ls "But... maybe I should leave..."
    pov "No! Don't do that. I insist you finish your shower. It's my fault that I'm in a hurry."
    pov "Besides I don't want to be the reason for you having to go to school all smelly..."
    ls "..."
    povi "She's still trying to work this all out in her mind."
    pov "Go ahead, it's ok..."
    scene showerupstairs 7am shower up 005c
    ls "Hnng..."
    povi "Oh, that's the look I was hoping for. She's unsure what to do about all of this, but she doesn't want to start an argument."
    "You start to undress."
    scene showerupstairs 7am shower up 006c
    povi "That's so cute, she's shy. I'm pretty sure she knows being naked in here together, washing isn't the only thing we'll be doing."
    povi "I bet she's interested in that too. She probably thinking she can use my boldness as excuse."
    scene showerupstairs 7am shower up 007c
    povi "Her tight little body. I'm so excited to see how far I can go."
    povi "But I need to be careful so that we don't get caught."
    "You enter the shower naked."
    scene showerupstairs 7am shower up 008c
    povi "Wow, is she looking at my dick or just trying to prevent eye-contact?"
    povi "Haha, that shy and innocent look on her face."
    scene showerupstairs 7am shower up 009c
    povi "She's still trying to cover herself up."
    scene showerupstairs 7am shower up 010c
    povi "What a wonderful sight, her wet naked body."
    povi "I'm getting excited just thinking about the fun we're going to have."
    scene showerupstairs 7am shower up 011c
    pov "You don't need to be so shy, you gonna make me uncomfortable. Haha."
    scene showerupstairs 7am shower up 013c
    ls "But..."
    pov "We're just showering together, there's nothing bad about that!"
    povi "Not yet..."
    ls "Hnng..."
    scene showerupstairs 7am shower up 012c
    pov "Or are you afraid I would try to do something lewd with you?"
    if inc == True:
        pov "My own little sister?"
    else:
        pov "A girl who is like a sister to me?"
    scene showerupstairs 7am shower up 013c
    ls "No... of course not... I didn't mean..."
    povi "Now to really start pushing things so she doesn't have time to object..."
    scene showerupstairs 7am shower up 014c
    pov "Good, then you won't mind if I help you wash as a thank you for letting me save time with you."
    "You start groping her tits."
    ls "Hah...!"
    povi "Well, she's not trying to stop me, that's a good sign."
    pov "We need to make sure to get everywhere."
    ls "Hnng...!"
    scene showerupstairs 7am shower up 015c
    "Your run the back of your hand down her stomach."
    if inc == True:
        pov "So soft. You have nice skin, little sis."
    else:
        pov "So soft. You have nice skin, [ls]."
    ls "Hah..."
    povi "She's hesitant, but her body is being so honest. Very nice!"
    pov "You can wash me after this..."
    scene showerupstairs 7am shower up 016c
    if inc == True:
        ls "Hah, wait... brother."
    else:
        ls "Hah, wait... [pov]."
    pov "It's ok. You need to be cleaned everywhere while we're showering."
    pov "Spread your legs, so I can wash you better."
    scene showerupstairs 7am shower up 017c
    ls "But, you're touching my... hah..."
    pov "As I said before, I just want to wash you, there is nothing wrong with that right?"
    ls "But..."
    pov "It's ok if you're feeling sensitive down there. Just try to relax, it will get easier the more we do this."
    ls "Hah... hah..."
    povi "She's trying to relax... but her body is letting her down, haha."
    scene showerupstairs 7am shower up 018c
    povi "Nice, she opened her legs more."
    povi "Question is whether she did to get this over with quicker or because she wanted it?"
    pov "Good girl!"
    "You slide your finger between her lips and slowly enter her pussy."
    "She starts to trembling lightly."
    ls "Hnng...! Hah..."
    if lsispronanal >= 4 or lsispronBDSM >= 4:
        call screen showerup7extcorfetish
    scene showerupstairs 7am shower up 019c
    "You finger her pussy faster."
    ls "Hah... hah... hah..."
    povi "Oh, she's definitely enjoying it."
    if inc == True:
        pov "Lil sis, look at me!"
    else:
        pov "[ls], look at me!"
    scene showerupstairs 7am shower up 020c
    if inc == True:
        ls "Why? Hah... brother..."
    else:
        ls "Why? Hah... [pov]..."
    pov "You need to look at me and tell me if I'm clean you properly, because I can't see inside there to know if I'm getting everywhere."
    ls "Huh? You want me to tell you...?"
    pov "Yes, you need to tell me if I'm hitting the right spots."
    "You move your finger to another spot in her pussy."
    ls "Hah... Hah... y... yes..."
    povi "Good, now she's guiding my finger. She's not just a passive participant anymore."
    pov "Don't stop guiding me, I want to do a good job for you."
    scene showerupstairs 7am shower up 021c
    ls "Faster... y-yes... hah..."
    "You push your finger in and out of her pussy quicker."
    ls "Yes... hah... there too..."
    "She starts to shaking."
    povi "She's close. Now to get her to cum from my \"helping hand\"."
    ls "Hah... hah..."
    scene showerupstairs 7am shower up 021ac
    ls "AAHHH... HNNG...!"
    with vpunch
    povi "She's cumming!"
    if inc == True:
        pov "So you're nice and clean now down there, lil sis. Does it feel good?"
        ls "Yeshh... brother..."
    else:
        pov "So you're nice and clean now down there, [ls]. Does it feel good?"
        ls "Yeshh... [pov]..."
    jump showerup7extcorhand

label showerup7extcorhand:
    "You stand back up and grab her hand."
    scene showerupstairs 7am shower up 022c
    pov "Now it's time for you to clean me."
    "You rest her hand on your dick."
    ls "Huh?"
    "You start to rub your dick with her hand."
    pov "I think I did a good job, so it's only fair if you help me, right?."
    scene showerupstairs 7am shower up 023c
    ls "O... OK. I'll... clean you too..."
    "She starts to rub your dick on her own, you keep your hand on hers just to make sure she doesn't stop before you're ready for her to."
    scene showerupstairs 7am shower up 024c
    if inc == True:
        pov "Ohh... you're doing so good, lil sis."
    else:
        pov "Ohh... you're doing so good, [ls]."
    pov "But can you do it a little faster?"
    ls "O... OK."
    "She rubs you a little faster."
    if lilsiscorruption >= 60:
        call screen showerup7extcorchoices
    else:
        jump showerup7extcorhand2

label showerup7extcorhand2:
    povi "She's so damn cute and obedient, standing there and rubbing my dick."
    "You bend forward..."
    scene showerupstairs 7am shower up 025c
    "...and give her a kiss."
    ls "Hnng...?"
    "You french kiss her when she opens her mouth in surprise."
    ls "Hnng...?"
    "Then you help her continue to rub your dick with her hand."
    scene showerupstairs 7am shower up 026c
    ls "Hmm..."
    "Her tongue starts to play with your tongue and she starts rubbing your dick on her own again."
    if inc == True:
        pov "Hmm... you taste so good, lil sis."
    else:
        pov "Hmm... you taste so good, [ls]."
    "Your tongues play wildly with each other."
    povi "She doing it on her own, amazing. She's giving me a handjob while sticking her tongue in my mouth."
    povi "It's so good I'm getting close. But I don't want to break this kiss, I'll just cum!"
    scene showerupstairs 7am shower up 027c
    pov "HNNG...! HMM...!"
    with vpunch
    "You spray your cum on her."
    ls "Hnng..."
    "You hold her arm and keep her jacking your cock until your done cumming."
    scene showerupstairs 7am shower up 028c
    povi "Awesome! I came all over her belly."
    pov "Now that was some great cleaning!"
    ls "..."
    if inc == True:
        pov "I came a lot. Now you know you did great job, sis."
    else:
        pov "I came a lot. Now you know you did great job, [ls]."
    ls "Hnng..."
    scene showerupstairs 7am shower up 029c
    pov "That was great! I'm glad you invited me to shower with you!"
    ls "Hnng..."
    povi "She didn't correct me? She knows that I'm right. She wanted this..."
    pov "Don't worry. We're both adults and we were just having a little fun."
    ls "Hmm..."
    pov "Unfortunately I made you dirty again, let me help you with that."
    "You use the opportunity to feel up her body again while you clean cum off of her."
    ls "Hmm..."
    povi "She's hesitating again. I should get out of here before she forgets the fun we had and starts worrying again."
    scene black
    "You quickly dress and leave the bathroom."
    $ showerup7amextfirstcor = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

#----- Custom Choice for Corruption Content -----
screen showerup7extcorchoices():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('showerup7extcorchoices'), Jump('showerup7extcorbj')) hovered tt.Action ("Blowjob [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_handjob_corruption_%s.png" action (Hide('showerup7extcorchoices'), Jump('showerup7extcorhand2')) hovered tt.Action ("Handjob [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('showerup7extcorchoices'), Jump('showerup7extlovecorruption')) hovered tt.Action ("[lv1] to [cr1] Events") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom Choice for Fetish Content -----
screen showerup7extcorfetish():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_rub_corruption_%s.png" action (Hide('showerup7extcorfetish'), Jump('showerup7extcoranal')) hovered tt.Action ("Anal [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_slap_%s.png" action (Hide('showerup7extcorfetish'), Jump('showerup7extcorbdsm')) hovered tt.Action ("BDSM [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('showerup7extcorfetish'), Return(None)) hovered tt.Action ("No Fetish") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extcoranal:
    pov "Turn around now."
    ls "Y-yes..."
    "She obediently turns around."
    scene showerupstairs 7am shower up 020cba
    povi "That's better. Now I can see what I'm doing."
    "You start to grope her ass too."
    ls "Hah... hnng..."
    povi "Let's have a little more fun with her, maybe showing her all that anal porn will finally pay off."
    scene showerupstairs 7am shower up 021ca
    "You tease her asshole with your finger, while you use your other hand to play with her pussy."
    ls "Hnng... Hnn..."
    povi "Good, she's into it. I'll go a little further."
    scene showerupstairs 7am shower up 022ca
    "You push your finger into her asshole."
    povi "It's so tight, but the water is helping me sliding in easily."
    scene showerupstairs 7am shower up 022cba
    ls "HAAH... your... finger..."
    pov "This making you feel good, right?"
    ls "Hnng..."
    "Her asshole tightens, but she doesn't try to take your finger out."
    scene showerupstairs 7am shower up 023ca
    "You slide it deeper into her asshole."
    ls "Ohhh... hnng..."
    pov "Relax a bit and try enjoy it."
    scene showerupstairs 7am shower up 021cba
    ls "Yeshh... hah..."
    pov "Good girl."
    "You rub her pussy faster."
    povi "Time to reward her for being so obedient and letting me explore her body."
    ls "Hah... hah..."
    "You slide you finger in and out of her asshole faster as well."
    scene showerupstairs 7am shower up 023cba
    ls "AAAHHHH.... HAAAHHH...!"
    with vpunch
    "Her ass tightens and she cums hard."
    ls "Hnng... ahh... hah... hah..."
    povi "Nice, she came while I played with her asshole."
    if inc == True:
        pov "You're clean down here now, lil sis."
        ls "Yeshh... brother..."
    else:
        pov "You're clean down here now, [ls]."
        ls "Yeshh... [pov]..."
    jump showerup7extcorhand

label showerup7extcorbdsm:
    pov "Turn around!"
    ls "Y-yes..."
    "She turns around."
    scene showerupstairs 7am shower up 020cba
    povi "Better, now I can really see what I'm doing."
    "You start to grope her ass."
    ls "Hah... hnng..."
    povi "Let's have a little more fun with her, maybe showing her all that BDSM porn will finally pay off."
    scene showerupstairs 7am shower up 021cb
    "You hold your hand up to give her a smack on her ass."
    povi "Let's see how she likes it."
    pov "<slap>"
    with vpunch
    scene showerupstairs 7am shower up 022cba
    ls "HAAHH..."
    "She shakes lightly, but doesn't move."
    povi "Nice, let's try some more."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    scene showerupstairs 7am shower up 022cb
    povi "Her ass is getting nice and red, what a view."
    ls "Hah... hah..."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    pov "You're a bad girl, aren't you?"
    scene showerupstairs 7am shower up 021cba
    ls "Yeshh... hah... I'm a bad girl..."
    pov "Do you need more punishment?"
    ls "Yeshh... hnn... please... [pov]."
    pov "Hmm... no, that's not what you're say."
    ls "..."
    povi "She's thinking about all that BDSM porn, I'm sure."
    ls "I need more punishment, master. Please?! Hnng..."
    pov "Good girl, you learn fast."
    scene showerupstairs 7am shower up 023cb
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    povi "This is so hot! She's getting in to it and she's event getting close to an orgasm, I can feel it."
    "You give a few more slaps."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    "She's shaking wildly."
    scene showerupstairs 7am shower up 023cba
    ls "AAAHHHH.... HAAAHHH...!"
    with vpunch
    "She cums hard."
    ls "Hnng... ahh... hah... hah..."
    povi "Nice, she came while I spanked her ass."
    if inc == True:
        pov "You're clean down here now, lil sis."
    else:
        pov "You're clean down here now, [ls]."
    ls "Yeshh... Master..."
    jump showerup7extcorhand

label showerup7extcorbj:
    call screen showerup7extcorchoose

screen showerup7extcorchoose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_handjob_corruption_%s.png" action (Hide('showerup7extcorchoose'), Jump('showerup7extcorhand')) hovered tt.Action ("I want her to continue stroking it") focus_mask True
        imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('showerup7extcorchoose'), Jump('showerup7extcorbj2')) hovered tt.Action ("I want her to get down on her knees [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extcorbj2:
    povi "She's so damn cute and obedient, standing there rubbing my dick. But I want more!"
    scene showerupstairs 7am shower up 030c
    "You place your hand on her shoulder."
    pov "I know a way you can clean me even faster."
    "You press her shoulder down."
    ls "Hnng..."
    povi "Hmm... I think she knows what I'm up to."
    scene showerupstairs 7am shower up 031c
    ls "Hnng..."
    pov "You can see it better from there and clean it faster too."
    "She stares at your dick, but doesn't move."
    povi "She struggling with herself. I better help her make her mind up."
    scene showerupstairs 7am shower up 032c
    "You move her hand onto your dick."
    pov "Continue to rub it clean and we'll be done in no time!"
    ls "Hnng..."
    povi "It's time to push her further."
    scene showerupstairs 7am shower up 033c
    pov "You know, you're partially to blame for this. Letting out so many sexy little moans while I washed you."
    pov "Are you going to take responsiblity?"
    if inc == True:
        pov "I won't be able to leave the shower like this, lil sis. You turned me on too much."
    else:
        pov "I won't be able to leave the shower like this, [ls]. You turned me on too much."
    ls "Hnn..."
    scene showerupstairs 7am shower up 034c
    ls "<kiss> Hmm..."
    pov "Ohh, yes..."
    povi "That's a nice surprise. I was just thinking she would continue the handjob, but this is even better."
    "She gives the head of you penis tiny little kisses."
    ls "<kiss> <kiss>"
    if inc == True:
        pov "You're very good at helping me, little sis."
    else:
        pov "You're very good at helping me, [ls]."
    pov "I'm so proud of you."
    scene showerupstairs 7am shower up 035c
    if inc == True:
        ls "<lick> Thank you... brother..."
    else:
        ls "<lick> Thank you... [pov]..."
    povi "She's eager to help me now. Maybe she feels guilty for being the only one who has had any fun until now."
    povi "Feeling her improvise is so great, I'm getting close already. But I want to feel her sexy mouth too, before I relieve myself."
    scene showerupstairs 7am shower up 036c
    "You push the tip of your dick in her mouth."
    pov "That is so good [ls]!"
    ls "Hnng...!"
    povi "So obedient. She isn't even trying to resist."
    ls "<lick><lick>"
    povi "Wow! She's licking the tip on her own."
    if inc == True:
        pov "Your sexy mouth is so good, little sis. I need to cum now!"
    else:
        pov "Your sexy mouth is so good, [ls]. I need to cum now!"
    call screen showerup7extcorbjcum

screen showerup7extcorbjcum():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('showerup7extcorbjcum'), Jump('showerup7extcorbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('showerup7extcorbjcum'), Jump('showerup7extcorbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extcorbjcumin:
    povi "I want her to taste my cum!"
    povi "I think it's better I don't warn her to make sure she doesn't try to pull away."
    "You hold her head tighter."
    scene showerupstairs 7am shower up 037ci
    pov "HNNG...!"
    with vpunch
    ls "Hnn..."
    "You spray your sperm in her mouth."
    pov "Oh yes, so good."
    with vpunch
    povi "She tried to move back at first, but now she's just holding still and accepting my cum. She was just surprised."
    ls "Hnn... <gulp> <gulp>"
    pov "Good girl. Drink it all down."
    scene showerupstairs 7am shower up 038ci
    "You let go of her head."
    ls "Hnng..."
    if inc == True:
        pov "You did very good, you didn't struggle much when I came, lil sis."
    else:
        pov "You did very good, you didn't struggle much when I came, [ls]."
    pov "I needed that. I'm glad you tasted my sperm like that."
    pov "Are you glad you tasted it too?"
    ls "Hnng... y-yes..."
    povi "So obedient, nice."
    pov "And did you like my taste?"
    ls "Hnn..."
    povi "She's getting lost in her own thoughts again. Well, she'll get used to my taste eventually."
    pov "It's ok. We're both adults having a bit of fun. That's all that matters."
    ls "Hmm..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstcor = True
    $ showerup7amextfirstcor2 = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

label showerup7extcorbjcumout:
    povi "I want her to feel my cum on her face!"
    povi "I think it's better I don't warn her to make sure she doesn't try to pull away."
    "You push her hand back and hold it in front of your cock."
    scene showerupstairs 7am shower up 037co
    pov "HNNG...!"
    with vpunch
    ls "Hnn..."
    "You spray your cum on her face."
    pov "Oh yes, so good."
    with vpunch
    povi "She tried to move back at first, but now she's just holding still and accepting my cum. She was just surprised."
    scene showerupstairs 7am shower up 038co
    ls "Hnng..."
    if inc == True:
        pov "You did very good, catching all that cum with your face, lil sis."
    else:
        pov "You did very good, catching all that cum with your face, [ls]."
    pov "I needed that. I wanted you to fell what it was like with my cum on your skin."
    pov "Are you glad I did that?"
    ls "Hnng... y-yes..."
    povi "So obedient, nice."
    pov "And did you like my sperm on your skin?"
    ls "Hnn..."
    povi "She's getting lost in her own thoughts again. Well, she'll get used to it eventually."
    pov "It's ok. We're both adults having a bit of fun. That's all that matters."
    ls "Hmm..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstcor = True
    $ showerup7amextfirstcor2 = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

#----- Custom 7am Upstairs Shower Alexis Love to Corruption Events ----- Done
label showerup7extlovecorruption:
    hide screen locations
    scene showerupstairs 7am shower up 011l
    if inc == True:
        ls "I'm glad you finally decided to join me, brother."
    else:
        ls "I'm glad you finally decided to join me, [pov]."
    povi "Wow, she's shifted from acting shy to more confident. I wonder what she's up to."
    ls "<giggle> Lost for words are we?"
    pov "Well, I can't be blamed for losing my cool a bit, I'm naked with such a beautiful girl."
    ls "Kiss me, [pov]. Now!"
    scene showerupstairs 7am shower up 012l
    "She kisses you."
    ls "<kiss>"
    povi "I think how she's acting now. I wonder if it's from any of the porn we've been watching together..."
    pov "<kiss>"
    scene showerupstairs 7am shower up 010l
    "She starts to rub her hands on your chest."
    pov "Oh, that feels good."
    ls "I can see that you like it. <giggle>."
    povi "Her wet naked body is so hot. Of course I got a boner."
    pov "You like that too?"
    scene showerupstairs 7am shower up 013l
    ls "<giggle> Of course I do."
    ls "I'm just coming up with the best way \"clean\" you."
    pov "Really?"
    ls "You're so full of dirty thoughts, my naughty dummy. <giggle>"
    pov "I definitely am."
    scene showerupstairs 7am shower up 014l
    ls "I know how to help you get clean again..."
    "Her hand moves lower."
    pov "I'm sure you'll find the right solution..."
    povi "She's being so straight forward, like she's in charge. Awesome!"
    scene showerupstairs 7am shower up 015l
    pov "Ohh..."
    ls "I'll clean here first. <giggle>"
    "She gives your cock a hard squeeze."
    pov "Ouch! That's attached you know."
    ls "<giggle> It's so hard and warm. We should definitely start here."
    if inc == True:
        pov "Thanks sis, it's great that you're \"helping\" me."
    else:
        pov "Thanks [ls], it's great that you're \"helping\" me."
    ls "My pleasure. <giggle>"
    if showerup7amextfirstlove == True:
        call screen showerup7extlovechoicescorruption #----- removed - jump showerup7extlovehump
    scene showerupstairs 7am shower up 016l
    ls "Hello there..."
    povi "She's being so forward and it's making me incredible horny."
    ls "You missed me? <giggle>"
    if inc == True:
        pov "You have no idea, lil sis."
    else:
        pov "You have no idea, [ls]."
    scene showerupstairs 7am shower up 017l
    "She starts to stoke your dick."
    ls "This will help you get \"clean\" in no time!"
    pov "Oh yes..."
    povi "Her soft hand rubbing my dick and that naughty look on her face..."
    ls "It's good you came to me to help you get clean."
    pov "I haven't \"came\" yet..."
    ls "I don't think that's going to take long. He's twitching in my hand."
    povi "She's right about that."
    pov "I'm cumming, [ls]!"
    ls "That's it, give me all your dirty thoughts. <giggle>"
    call screen showerup7extlovecumcorruption

screen showerup7extlovecumcorruption():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('showerup7extlovecumcorruption'), Jump('showerup7extlovecumfcorruption')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" action (Hide('showerup7extlovecumcorruption'), Jump('showerup7extlovecumtcorruption')) hovered tt.Action ("Cum on her tits") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extlovecumfcorruption:
    scene showerupstairs 7am shower up 018lfo
    pov "AHHH... HNNG...!"
    with vpunch
    "You cum on her face."
    ls "Hmm..."
    povi "Damn, even while I'm cumming on her face she looks good."
    scene showerupstairs 7am shower up 019lfo
    ls "Are you sure that's all your dirty thoughts? I don't want to miss any. <giggle>"
    pov "You were pretty thorough..."
    ls "I'm happy that I could help you with that."
    if inc == True:
        pov "You're amazing, little sis. I loved it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, big brother."
    else:
        pov "You're amazing. I loved it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, [pov]."
    ls "I need to wash up now to get ready for school."
    pov "Ok. That was like a wet dream come true, haha."
    ls "You can dream about me anytime you want. And come see me more often to help you keep clean. <giggle>"
    povi "Oh... my god..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstlove = True
    $ showerup7amextyes = True
    $ dtime += 1
jump showerup

label showerup7extlovecumtcorruption:
    scene showerupstairs 7am shower up 018lto
    pov "AHHH... HNNG...!"
    with vpunch
    "You cum on her tits."
    ls "Hmm... there's so much..."
    scene showerupstairs 7am shower up 019lto
    ls "Are you sure that's all your dirty thoughts? I don't want to miss any. <giggle>"
    pov "You were pretty thorough..."
    ls "I'm happy that I could help you with that."
    if inc == True:
        pov "You're amazing, little sis. I loved it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, big brother."
    else:
        pov "You're amazing. I loved it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, [pov]."
    ls "I need to wash up now to get ready for school."
    pov "Ok. That was like a wet dream come true, haha."
    ls "You can dream about me anytime you want. And come see me more often to help you keep clean. <giggle>"
    povi "Oh... my god..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstlove = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

#----- Custom Love to corruption options -----
screen showerup7extlovechoicescorruption():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_rub_love_%s.png" action (Hide('showerup7extlovechoicescorruption'), Jump('showerup7extlovehumpcorruption')) hovered tt.Action ("Hump [lv1] to [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('showerup7extlovechoicecorruptions'), Return(None)) hovered tt.Action ("Continue") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extlovehumpcorruption:
    ls "I've got something special to help clean you up this time."
    pov "Something special?"
    ls "Yes, let me show you."
    scene showerupstairs 7am shower up 020l
    povi "Her hot little ass looks fantastic!"
    pov "What do you have in mind?"
    ls "Oh you'll like it, but you have to remmeber, I'm in charge."
    pov "Sure, whatever you want."
    povi "Is she going to fuck me?"
    scene showerupstairs 7am shower up 021l
    "She's holds her ass up so your dick is laying on it."
    pov "This is getting interesting."
    ls "You're going to like this. <giggle>"
    scene showerupstairs 7am shower up 023l
    "She moves her ass slowly back towards you."
    povi "Her ass rubbing on my dick feels really good."
    scene showerupstairs 7am shower up 024l
    povi "Damn, I wish I could fuck her right now!"
    ls "Hmm... "
    pov "Your ass feels so good."
    scene showerupstairs 7am shower up 022l
    ls "Oh, I haven't even gotten started yet. <giggle>"
    if inc == True:
        pov "You're such a naughty tease, lil sis."
    else:
        pov "You're such a naughty tease, [ls]."
    ls "I don't think I'm teasing you enough!"
    pov "How about you stop teasing me and show me what you really want to do."
    ls "Fine. I guess I've waited long enough. <giggle>"
    scene showerupstairs 7am shower up 025l
    "She rubs your dick further into her asschecks and it slips between her them."
    pov "Ohh... hell yeah!"
    ls "<giggle>"
    povi "What a hot view. I'm close enough I can feel the warmth of her pussy too."
    scene showerupstairs 7am shower up 026l
    ls "Hnng..."
    povi "What's with her? Is she getting excited too?"
    pov "Are you being a naughty girl right now?"
    ls "Hnng..."
    if inc == True:
        pov "It's ok, lil sis. You're allowed to enjoy this too."
    else:
        pov "It's ok, [ls]. You're allowed to enjoy this too."
    povi "Is she afraid that I'm going to take over and just jump her bones?"
    if inc == True:
        pov "You're in charge remember, we'll do it your way. I want to see how naughty my little sister is."
    else:
        pov "You're in charge remember, we'll do it your way. I want to see how naughty you are."
    scene showerupstairs 7am shower up 022l
    ls "<giggle> You're right! This is my show."
    if inc == True:
        ls "Get ready, brother."
    else:
        ls "Get ready, [pov]."
    pov "Oh, I'm definitely ready for this."
    ls "Then enjoy it. <giggle>"
    scene showerupstairs 7am shower up 027l
    "She starts to rub you faster."
    pov "Hmm..."
    povi "I'm oretty sure she's getting wetter down there. She's already starting to tremble."
    scene showerupstairs 7am shower up 028l
    ls "Hah... Hmm..."
    povi "She's defintely getting wetter and it's not just the water!"
    povi "She's rubbing me with her pussy now."
    pov "Yes... more..."
    scene showerupstairs 7am shower up 029l
    ls "Hah... hah... hah..."
    pov "So are you enjoying your cleaning method as much as I am?"
    ls "Yes... hah... your big dick..."
    pov "I'm glad you're having fun too."
    ls "Hah... yes, I am... hah..."
    scene showerupstairs 7am shower up 030l
    "She starts to rub furiously on your dick."
    if inc == True:
        ls "Hah... hah... big brother!"
    else:
        ls "Hah... hah... [pov]!"
    "Her body shakes and trembles."
    povi "So hot! She's getting herself off on my dick."
    ls "Ohh... ooh... OOHHH!"
    pov "Are you comming?"
    ls "Yes... yes, [pov]! AAAAHHHH!"
    with vpunch
    pov "This is to much! I'm cumming too!"
    scene showerupstairs 7am shower up 031l
    pov "AHHH... HNNG...!"
    with vpunch
    "You cum all over her ass."
    ls "Hmm..."
    scene showerupstairs 7am shower up 032l
    pov "Oh, oh... that was so good."
    ls "I can feel your dirty thoughts all over my ass. <giggle>"
    pov "Well I think your cleaning method was fucking great. It was very inventive."
    pov "And you had lot's of fun too."
    ls "Yeah, it felt soooo good."
    scene showerupstairs 7am shower up 033l
    if inc == True:
        pov "You're amazing, lil sis. That was hot."
        ls "And me?"
        pov "You're hot too, [ls]."
        ls "Why thank you, big brother. You're not so bad yourself."
    else:
        pov "You're amazing... That was hot."
        ls "And me?"
        pov "You're hot too, [ls]."
        ls "Why thank you, [pov]. You're not so bad yourself."
    ls "I need to wash up now to get ready for school. You can leave now."
    pov "Ok. This was just like a wet dream come true, haha."
    ls "You can dream about me whenever you want. And feel free to let me clean you more often too. <giggle>"
    povi "Oh... my god..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstlove2 = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

#----- 7am Upstairs Bathroom Alexis Event Love ----- Done
label showerup7extlove:
    hide screen locations
    povi "Damn it, I need a way to get in there..."
    povi "..."
    povi "Hmm... maybe if I push her a it a little?"
    "Knock! Knock!"
    "You knock on the door loudly."
    ls "I'm showering, go away."
    pov "Hurry up and open the door!"
    ls "But I'm..."
    "Knock! Knock"
    pov "Come on! I need to get in!"
    ls "Hmpf!"
    scene showerupstairs 7am shower up 002
    if inc == True:
        ls "What is it, brother?"
    else:
        ls "What is it, [pov]?"
    povi "Wow, what a nice view."
    pov "I need to use the shower, I'm in a hurry!"
    scene showerupstairs 7am shower up 003
    povi "What a nice view. So innocent..."
    pov "..."
    ls "[pov]? [pov]!"
    pov "Huh?"
    scene showerupstairs 7am shower up 004l
    ls "You can come in, dummy."
    pov "You're letting me in?"
    ls "Of course, you want to share the shower with me, right? We can do that."
    povi "Oh, this is going better then expected. She seems open to do more and more with me, nice."
    scene showerupstairs 7am shower up 005l
    ls "<giggle> Are you dreaming?"
    pov "Oh... I just..."
    ls "If you're in such a hurry, you shouldn't mke me wait... <giggle>"
    povi "Is she teasing me?"
    if inc == True:
        povi "My little sister is naked and asking me to share the shower with her."
    else:
        povi "[ls] is naked and asking me to share the shower with her."
    povi "I hope this isn't a juast a dream, because if it is, then I really don't want to wake up."
    scene showerupstairs 7am shower up 006l
    povi "Our visit to the basement together must have boosted her confidence."
    povi "She doesn't even try to hide her body from me."
    scene showerupstairs 7am shower up 007l
    povi "This is wonderful. She is really starting to see me as her lover now, doing all sorts of things together."
    povi "I love it, especially her teasing. From innocent and prudish to open and adventurous."
    scene showerupstairs 7am shower up 008l
    ls "What's up [pov]? You're still dressed? <giggle>"
    pov "I..."
    if inc == True:
        ls "Or do you just want to watch your little sister showering? <giggle>"
    else:
        ls "Or do you just want to watch me showering? <giggle>"
    pov "No... I'll join you."
    povi "Enough watching, I need to get in there now!"
    scene showerupstairs 7am shower up 009l
    ls "Well then get undressed and get in here. Or are you afraid to, dummy?"
    povi "So damn cute. And also pretty damn sexy."
    "You undress and enter the shower."
    scene showerupstairs 7am shower up 011l
    if inc == True:
        ls "You finally decided to join me, brother."
        povi "Yes, I'm naked with my little sister in the shower. At her request no less!"
    else:
        ls "You finally decided to join me, [pov]."
        povi "Yes, I'm naked with [ls] in the shower. At her request no less!"
    ls "<giggle> Lost for words?"
    pov "Well, I can't be blamed for losing my cool a bit, being naked with such a beautiful girl."
    ls "Ohh, [pov]. Kiss me!"
    scene showerupstairs 7am shower up 012l
    "She kisses you."
    ls "<kiss>"
    povi "What a promising start..."
    pov "<kiss>"
    scene showerupstairs 7am shower up 010l
    "She starts to rub her hands on your chest."
    pov "Oh, that feels good."
    ls "I can see that <giggle>."
    povi "I already got a boner. Her wet naked body is so hot."
    pov "You don't mind, do you?"
    scene showerupstairs 7am shower up 013l
    ls "<giggle> Of course not."
    ls "I'm just wondering, what would be the best way to help you get \"clean\"?"
    pov "What?"
    ls "You're so full of dirty thoughts, my naughty dummy. <giggle>"
    pov "Haha, you got me."
    scene showerupstairs 7am shower up 014l
    ls "I think I have an idea on how to help you get clean..."
    "Her hand moves lower."
    pov "I'm sure you'll find the right solution..."
    povi "She's being so straight forward, like we're already lovers. Awesome!"
    scene showerupstairs 7am shower up 015l
    pov "Ohh..."
    ls "I'll clean here first. <giggle>"
    povi "Her hands are so soft."
    ls "It's so hard and warm. We should definitely start here."
    if inc == True:
        pov "Thanks sis, I'm happy that you're helping me."
    else:
        pov "Thanks [ls], I'm happy that you're helping me."
    ls "You're welcome. <giggle>"
    if showerup7amextfirstlove == True:
        call screen showerup7extlovechoices #----- removed - jump showerup7extlovehump
    scene showerupstairs 7am shower up 016l
    ls "Hello there, little dummy."
    povi "That's so cute and it's making me incredible horny."
    ls "You missed me? <giggle>"
    if inc == True:
        pov "You have no idea, lil sis."
    else:
        pov "You have no idea, [ls]."
    scene showerupstairs 7am shower up 017l
    "She starts to stoke your dick."
    ls "This will help you get clean in no time!"
    pov "Oh yes..."
    povi "Her soft hand rubbing my dick and that naughty look on her face..."
    ls "It's good you came to me to help you get clean."
    pov "I haven't \"came\" yet..."
    ls "I can tell little dummy really missed me. He's twitching in my hand."
    povi "That did it, I can't hold on any longer!"
    pov "I'm cumming, [ls]!"
    ls "Just let your dirty thoughts come out. <giggle>"
    call screen showerup7extlovecum

screen showerup7extlovecum():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_head_%s.png" action (Hide('showerup7extlovecum'), Jump('showerup7extlovecumf')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_boobs_%s.png" action (Hide('showerup7extlovecum'), Jump('showerup7extlovecumt')) hovered tt.Action ("Cum on her tits") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extlovecumf:
    scene showerupstairs 7am shower up 018lfo
    pov "AHHH... HNNG...!"
    with vpunch
    "You cum on her face."
    ls "Hmm..."
    povi "Damn, even while I'm cumming on her face she's cute."
    scene showerupstairs 7am shower up 019lfo
    ls "Now I've cleaned up all your dirty thoughts. <giggle>"
    pov "Are you happy you have them?"
    ls "I'm more happy that I could help you with your problem."
    if inc == True:
        pov "You're amazing, little sis. I loved it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, big brother."
    else:
        pov "You're amazing. I loved it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, [pov]."
    ls "I need to wash up now to get ready for school."
    pov "Ok. I think I just realized that this wasn't a dream, haha."
    ls "You can dream of me too if you want. And feel free to let me clean you more often. <giggle>"
    povi "Oh... my god..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstlove = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

label showerup7extlovecumt:
    scene showerupstairs 7am shower up 018lto
    pov "AHHH... HNNG...!"
    with vpunch
    "You cum on her tits."
    ls "Hmm... there's so much..."
    scene showerupstairs 7am shower up 019lto
    ls "Now I've cleaned up all your dirty thoughts. <giggle>"
    pov "Are you happy you have them?"
    ls "I'm more happy that I could help you with your problem."
    if inc == True:
        pov "You're amazing, little sis. I love it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, big brother."
    else:
        pov "You're amazing. I love it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, [pov]."
    ls "I need to wash up now to get ready for school."
    pov "Ok. I think I just realized that this wasn't a dream, haha."
    ls "You can dream of me too if you want. And feel free to let me clean you more often. <giggle>"
    povi "Oh... my god..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstlove = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

#----- Custom Love options -----
screen showerup7extlovechoices():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_rub_love_%s.png" action (Hide('showerup7extlovechoices'), Jump('showerup7extlovehump')) hovered tt.Action ("Hump [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('showerup7extlovechoices'), Jump('showerup7extcorlove')) hovered tt.Action ("[cr1] to [lv1] Events") focus_mask True
        imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('showerup7extlovechoices'), Return(None)) hovered tt.Action ("Continue") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extlovehump:
    ls "This time I'm going try something different to clean you up."
    pov "Something different?"
    ls "Yep, I'll show you."
    scene showerupstairs 7am shower up 020l
    povi "Her hot little ass looks fantastic!"
    pov "So what are you up to?"
    ls "Oh you'll like it, but you have to promise to let me do it on my own pace."
    pov "Sure, whatever you want."
    povi "Is she going to have sex me?"
    scene showerupstairs 7am shower up 021l
    "She's holds her ass up so your dick is laying on it."
    pov "This is getting interesting, I'm eager to see what you'll do next."
    ls "You'll like it. <giggle>"
    scene showerupstairs 7am shower up 023l
    "She moves her ass slowly back towards you."
    povi "Her ass rubbing on my dick feels real nice."
    scene showerupstairs 7am shower up 024l
    povi "Damn, I wish I could fuck her right now!"
    ls "Hmm... "
    pov "Your ass feels so good."
    scene showerupstairs 7am shower up 022l
    ls "And I haven't even started yet. <giggle>"
    if inc == True:
        pov "Oh so you're teasing me, lil sis."
    else:
        pov "Oh so you're teasing me, [ls]."
    pov "That's cheeky of you."
    ls "Wow, did you really make a pun about my ass right now?"
    pov "Sorry I couldn't help it. How about you stop teasing me and show me what you really want to do."
    ls "OK. <giggle>"
    scene showerupstairs 7am shower up 025l
    "She rubs your dick further into her asschecks and it slips between her them."
    pov "Ohh... this feels sooo good."
    ls "<giggle>"
    povi "What a hot view. I'm close enough I can feel the warmth of her pussy too."
    scene showerupstairs 7am shower up 026l
    ls "Hnng..."
    povi "What's with her? Is she getting excited too?"
    pov "Are you getting naughty thoughts too?"
    ls "Hnng..."
    if inc == True:
        pov "It's ok, lil sis. You can have fun while cleaning me too."
    else:
        pov "It's ok, [ls]. You can have fun while cleaning me too."
    povi "Is she afraid that I would take advantage of the situation?"
    pov "You can enjoy it too, we'll do it your way, I won't force you to do anything. Promise!"
    scene showerupstairs 7am shower up 022l
    ls "<giggle> You're right! I wasn't really thinking there for a moment."
    if inc == True:
        ls "Forgive me, brother."
    else:
        ls "Forgive me, [pov]."
    pov "There's nothing to forgive, everything is great."
    ls "Then enjoy this. <giggle>"
    scene showerupstairs 7am shower up 027l
    "She starts to rub you faster."
    pov "Hmm..."
    povi "I'm not sure if it's just the water or if she's getting wetter. She's already trembling lightly."
    scene showerupstairs 7am shower up 028l
    ls "Hah... Hmm..."
    povi "She's defintely getting more excited too!"
    povi "She's rubbing me with her pussy now."
    pov "Yes... more..."
    scene showerupstairs 7am shower up 029l
    ls "Hah... hah... hah..."
    pov "So you're enjoying your cleaning method as much as I am?"
    ls "Yes... hah... your big dick..."
    pov "I'm glad you're having fun too."
    ls "Hah... yes, I am... hah..."
    scene showerupstairs 7am shower up 030l
    "She starts to rub furiously on your dick."
    if inc == True:
        ls "Hah... hah... big brother!"
    else:
        ls "Hah... hah... [pov]!"
    "Her body shakes and trembles."
    povi "So hot! She's getting herself off on my dick."
    ls "Ohh... ooh... OOHHH!"
    pov "Are you comming?"
    ls "Yes... yes, [pov]! AAAAHHHH!"
    with vpunch
    pov "This is to much! I'm cumming too!"
    scene showerupstairs 7am shower up 031l
    pov "AHHH... HNNG...!"
    with vpunch
    "You cum all over her ass."
    ls "Hmm..."
    scene showerupstairs 7am shower up 032l
    pov "Oh, oh... that was so good."
    ls "I can feel your dirty thoughts on my ass. <giggle>"
    pov "Well I loved your cleaning method very much. It was very inventive."
    pov "And I'm even more happy that you had lot's of fun too."
    ls "Yeah, it felt really good."
    scene showerupstairs 7am shower up 033l
    if inc == True:
        pov "You're amazing, lil sis. I loved it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, big brother."
    else:
        pov "You're amazing. I loved it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, [pov]."
    ls "I need to wash up now to get ready for school."
    pov "Ok. I think I just realized that this wasn't a dream, haha."
    ls "You can dream of me too if you want. And feel free to let me clean you more often. <giggle>"
    povi "Oh... my god..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstlove2 = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

#----- Custom 7am Upstairs Shower Alexis Corruption to Love Events ----- Done
label showerup7extcorlove:
    scene showerupstairs 7am shower up 008c
    povi "Is she looking at my dick or just trying to prevent eye-contact?"
    povi "That shy and innocent look on her face is just adorable."
    scene showerupstairs 7am shower up 009c
    povi "She's still trying to cover herself up."
    scene showerupstairs 7am shower up 010c
    povi "Her wet naked body is amazing."
    scene showerupstairs 7am shower up 011c
    pov "You don't need to be so shy. I'm not going to do anything you don't want me to."
    scene showerupstairs 7am shower up 013c
    ls "I know it's just..."
    "You can tell she's blushing a little."
    pov "We're just showering together, there's nothing bad about that!"
    ls "Hnng..."
    scene showerupstairs 7am shower up 012c
    pov "Do you think I would do anything to you without making sure it's ok with you first?"
    if inc == True:
        pov "My own little sister?"
    else:
        pov "A girl who is like a sister to me?"
    scene showerupstairs 7am shower up 013c
    ls "No... of course not... I mean..."
    povi "She's so cute when she's afraid to really ask for what she wants..."
    pov "Good, in that case do you want then you wwant me help you wash? As a thank you for letting me save time with you."
    ls "...yes..."
    scene showerupstairs 7am shower up 014c
    "You start with washing her tits."
    ls "Hah...!"
    povi "Well, she's not trying to stop me, that's a good sign."
    pov "We need to make sure we get everywhere."
    ls "Hnng...!"
    scene showerupstairs 7am shower up 015c
    "Your run the back of your hand down her stomach."
    if inc == True:
        pov "So soft. You have nice skin, little sis."
    else:
        pov "So soft. You have nice skin, [ls]."
    ls "Hah..."
    povi "Those little moans are just so cute!"
    pov "You can wash me after this if you want..."
    scene showerupstairs 7am shower up 016c
    if inc == True:
        ls "Hah, ok... brother."
    else:
        ls "Hah, ok... [pov]."
    pov "Spread your legs for me please, so I can wash you better."
    "She obediently spreads her legs for you."
    scene showerupstairs 7am shower up 017c
    ls "You're touching my... hah..."
    pov "As I said before, I need to wash you everywhere. Is this ok?"
    ls "Yeah..."
    pov "It's ok if you're feeling sensitive down there. Just try to relax, it will get easier the more we do this."
    ls "Hah... hah..."
    povi "She's trying to relax... but her body is letting her down."
    scene showerupstairs 7am shower up 018c
    povi "She's opening her legs even more."
    pov "Good girl!"
    "You slide your finger between her lips and slowly enter her pussy."
    "She starts to trembling lightly."
    ls "Hnng...! Hah..."
    if lsispronanal >= 4 or lsispronBDSM >= 4:
        call screen showerup7extcorfetishlove
    scene showerupstairs 7am shower up 019c
    "You finger her pussy faster."
    ls "Hah... hah... hah..."
    povi "Oh, she's definitely enjoying this too."
    if inc == True:
        pov "Little sis, look at me, ok?"
    else:
        pov "[ls], look at me ok?"
    scene showerupstairs 7am shower up 020c
    if inc == True:
        ls "Ok. Hah... brother..."
    else:
        ls "Ok. Hah... [pov]..."
    pov "Keep looking at me and tell me if I'm clean you properly, I want to make sure I'm hitting all the places you want me to."
    ls "Huh? You want me to tell you...?"
    pov "If I'm hitting the right spots."
    "You move your finger to another spot in her pussy."
    ls "Hah... Hah... y... yes..."
    povi "That should help her feel even more comfortable while we're together."
    pov "Please don't stop guiding me, I want to do a good job for you."
    scene showerupstairs 7am shower up 021c
    ls "Faster... y-yes... hah..."
    "You push your finger in and out of her pussy quicker."
    ls "Yes... hah... there too..."
    "She starts to shaking."
    povi "She's close. Now to get her to cum from my \"helping hand\"."
    ls "Hah... hah..."
    scene showerupstairs 7am shower up 021ac
    ls "AAHHH... HNNG...!"
    with vpunch
    povi "She's cumming!"
    if inc == True:
        pov "You're nice and clean now down there, little sis. Did it feel good?"
        ls "Yeshh... brother..."
    else:
        pov "You're nice and clean now down there, [ls].Did it feel good?"
        ls "Yeshh... [pov]..."
    jump showerup7extcorhandlove

label showerup7extcorhandlove:
    "You stand back up and softly guide her hand."
    scene showerupstairs 7am shower up 022c
    pov "Will you clean me now too."
    "You rest her hand on your dick."
    ls "Ok..."
    "You start to help her rub your dick with her hand."
    pov "I really appreciate you helping clean me like this."
    scene showerupstairs 7am shower up 023c
    ls "O... OK. I'll... clean you too..."
    "She starts to rub your dick on her own, you keep your hand on hers to help her get started."
    scene showerupstairs 7am shower up 024c
    if inc == True:
        pov "Ohh... you're doing so good, lil sis."
    else:
        pov "Ohh... you're doing so good, [ls]."
    pov "Could you do it a little faster?"
    ls "O... OK."
    "She rubs you a little faster."
    if lilsislove >= 60:
        call screen showerup7extcorchoiceslove
    else:
        jump showerup7extcorhand2love

label showerup7extcorhand2love:
    povi "She's so damn cute, standing there and rubbing my dick."
    "You bend forward..."
    scene showerupstairs 7am shower up 025c
    "...and give her a kiss."
    ls "Hnng...?"
    "You french kiss her when she opens her mouth in surprise."
    ls "Hnng...?"
    "You continue to help her rub your dick with her hand."
    scene showerupstairs 7am shower up 026c
    ls "Hmm..."
    "Her tongue starts to play with yours and she's rubbing your dick on her own again."
    if inc == True:
        pov "Hmm... you taste so good, lil sis."
    else:
        pov "Hmm... you taste so good, [ls]."
    "Your tongues play wildly with each other."
    povi "She doing it on her own, amazing. She's giving me a handjob while sticking her tongue in my mouth."
    povi "It's so good I'm getting close. But I don't want to break this kiss, I'll just cum!"
    scene showerupstairs 7am shower up 027c
    pov "HNNG...! HMM...!"
    with vpunch
    "You spray your cum on her."
    ls "Hnng..."
    "You hold her arm tightly as she keeps jacking your cock until your done cumming."
    scene showerupstairs 7am shower up 028c
    povi "Awesome! I came all over her belly."
    pov "Now that was some great cleaning!"
    ls "..."
    if inc == True:
        pov "I came a lot. You did great job, little sis."
    else:
        pov "I came a lot. You did great job, [ls]."
    ls "Hnng..."
    scene showerupstairs 7am shower up 029c
    pov "I'm really glad you invited me to shower with you!"
    ls "Hnng..."
    povi "She didn't correct me? I'm pretty sure she wanted this as much as I did..."
    pov "Don't worry. We're both adults and we were just having a little fun."
    ls "Hmm..."
    pov "I made you dirty again though, let me help you with that."
    "You clean the cum off of her. You both seem to enjoy the opportunity this provides you to feel her body with your hands again."
    ls "Hmm..."
    pov "Thanks again sis. See you tomorrow?"
    ls "Oh... Ok."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstcor = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

#----- Custom Choice for Corruption to Love Content -----
screen showerup7extcorchoiceslove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "edited/gui/vice/icon_blowjob_love_%s.png" action (Hide('showerup7extcorchoiceslove'), Jump('showerup7extcorbjlove')) hovered tt.Action ("Blowjob [cr1] to [lv1]") focus_mask True
        imagebutton auto "edited/gui/vice/icon_handjob_love_%s.png" action (Hide('showerup7extcorchoiceslove'), Jump('showerup7extcorhand2love')) hovered tt.Action ("Handjob [cr1] to [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom Choice for Fetish Content Corruption to Love -----
screen showerup7extcorfetishlove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "edited/gui/vice/icon_rub_love_%s.png" action (Hide('showerup7extcorfetishlove'), Jump('showerup7extcoranallove')) hovered tt.Action ("Anal [cr1] to [lv1]") focus_mask True
        imagebutton auto "edited/gui/vice/icon_unihand_love_%s.png" action (Hide('showerup7extcorfetishlove'), Jump('showerup7extcorbdsmlove')) hovered tt.Action ("BDSM [cr1] to [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('showerup7extcorfetishlove'), Return(None)) hovered tt.Action ("No Fetish") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extcoranallove:
    if inc == True:
        ls "Hey, brother..."
        pov "Yes, Little sis?"
    else:
        ls "Hey, [pov]..."
        pov "Yes, [ls]?"
    ls "Can we try something I want to do?"
    pov "Of course, anything you want."
    "She hesitates for a moment, then turns around."
    scene showerupstairs 7am shower up 020cba
    ls "Will you... play with..."
    pov "Play with what?"
    ls "...my ass."
    povi "Wow, I didn't expect that."
    povi "Maybe it's that anal porn we watched together that's got her curious about this."
    pov "Sure thing."
    "You start to grope her ass too."
    ls "Hah... hnng..."
    scene showerupstairs 7am shower up 021ca
    "You tease her asshole with your finger, while you use your other hand to play with her pussy."
    ls "Hnng... Hnn..."
    povi "She's really getting into it. I'll go a little further now."
    scene showerupstairs 7am shower up 022ca
    "You push your finger into her asshole."
    povi "It's so tight, but the water is helping me sliding in easily."
    scene showerupstairs 7am shower up 022cba
    ls "HAAH... your... finger..."
    pov "Is this making you feel good?"
    ls "Hnng..."
    "Her asshole tightens, and she doesn't try to take your finger out."
    povi "I guess I have my answer."
    scene showerupstairs 7am shower up 023ca
    "You slide your finger deeper into her asshole."
    ls "Ohhh... hnng..."
    pov "You need to relax a bit so you can enjoy it more."
    scene showerupstairs 7am shower up 021cba
    ls "Yeshh... hah..."
    pov "Good girl."
    "You rub her pussy faster."
    povi "Time to reward her for being so adventurous and letting me explore her body."
    ls "Hah... hah..."
    "You slide you finger in and out of her asshole faster as well."
    scene showerupstairs 7am shower up 023cba
    ls "AAAHHHH.... HAAAHHH...!"
    with vpunch
    "Her ass tightens and she cums hard."
    ls "Hnng... ahh... hah... hah..."
    povi "Nice, she came while I played with her asshole."
    if inc == True:
        pov "You're clean down here now, lil sis."
        ls "Yeshh... thank you, brother..."
    else:
        pov "You're clean down here now, [ls]."
        ls "Yeshh... thank you, [pov]..."
    pov "My pleasure."
    jump showerup7extcorhandlove

label showerup7extcorbdsmlove:
    if inc == True:
        ls "Hey, brother..."
        pov "Yes, Little sis?"
    else:
        ls "Hey, [pov]..."
        pov "Yes, [ls]?"
    ls "Can we try something I want to do?"
    pov "Of course, anything you want."
    "She hesitates for a moment, then turns around."
    scene showerupstairs 7am shower up 020cba
    ls "Will you... maybe..."
    pov "Will I what?"
    ls "...spank me a little."
    povi "Wow, I didn't expect that."
    povi "Maybe it's that BDSM porn we watched together that's got her curious about this."
    pov "Sure thing."
    ls "Hnng..."
    scene showerupstairs 7am shower up 021cb
    "You hold your hand up to give her a test smack on her ass."
    povi "Let's see how she likes it."
    pov "<slap>"
    with vpunch
    scene showerupstairs 7am shower up 022cba
    ls "HAAHH..."
    "She shakes lightly, but doesn't move."
    povi "Nice, let's try some more."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    scene showerupstairs 7am shower up 022cb
    povi "Her ass is getting nice and red, what a view."
    ls "Hah... hah..."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    pov "You're a naughty girl, aren't you?"
    scene showerupstairs 7am shower up 021cba
    ls "Yeshh... hah... I'm a naughty girl..."
    pov "Do you need more punishment?"
    ls "Yeshh... hnn... please... [pov]."
    pov "I think you're supposed to call me something else, right?."
    ls "..."
    povi "She's thinking about the BDSM porn I think."
    ls "I need more punishment, master. Please?! Hnng..."
    pov "Good girl, you learn fast."
    scene showerupstairs 7am shower up 023cb
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    povi "This is so hot! She's getting in to it. I think she's getting close to orgasm too."
    "You give a few more slaps."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    "She's shaking wildly."
    scene showerupstairs 7am shower up 023cba
    ls "AAAHHHH.... HAAAHHH...!"
    with vpunch
    "She cums hard."
    ls "Hnng... ahh... hah... hah..."
    povi "Nice, she came while I was spanking her ass."
    if inc == True:
        pov "You're clean down here now, lil sis."
    else:
        pov "You're clean down here now, [ls]."
    ls "Yeshh... thank you Master..."
    jump showerup7extcorhandlove

label showerup7extcorbjlove:
    call screen showerup7extcorchooselove

screen showerup7extcorchooselove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_handjob_love_%s.png" action (Hide('showerup7extcorchooselove'), Jump('showerup7extcorhandlove')) hovered tt.Action ("I want her to continue stroking for a while") focus_mask True
        imagebutton auto "edited/gui/icons/icon_blowjob_love_%s.png" action (Hide('showerup7extcorchooselove'), Jump('showerup7extcorbj2love')) hovered tt.Action ("I want her to get down on her knees [cr1] to [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extcorbj2love:
    povi "She's so damn cute, standing there rubbing my dick. But I wonder if she's getting tired"
    scene showerupstairs 7am shower up 030c
    "You place your hand on her shoulder."
    pov "You can kneel down if that would be better."
    "She kneels down in front of you."
    ls "Hnng..."
    povi "Wait, why is she getting more excited? I just want her to be comfortable."
    scene showerupstairs 7am shower up 031c
    ls "Hnng..."
    pov "Are you ok down there?."
    "She stares at your dick, but doesn't move."
    povi "Maybe she thinks I'm trying to get her to do something else."
    scene showerupstairs 7am shower up 032c
    "You move her hand onto your dick."
    pov "It's ok, I just thought you would be more comfortable down there, that's all."
    ls "Hnng..."
    scene showerupstairs 7am shower up 033c
    if inc == True:
        pov "I really appreciate this, little sis."
        pov "I won't be able to leave the shower like this, lil sis. You turned me on too much."
    else:
        pov "I really appreciate this, [ls]."
        pov "I won't be able to leave the shower like this, [ls]. You turned me on too much."
    ls "Really? I turn you on?"
    pov "Of course you do. You're gorgeous!"
    ls "Hnng..."
    "She leans in closer..."
    scene showerupstairs 7am shower up 034c
    ls "<kiss> Hmm..."
    pov "Ohh, yes..."
    povi "That's a nice surprise. I was just thinking she would just continue the handjob, but this is even better."
    "She gives the head of you penis tiny little kisses."
    ls "<kiss> <kiss>"
    if inc == True:
        pov "You're very good at helping me, little sis."
    else:
        pov "You're very good at helping me, [ls]."
    scene showerupstairs 7am shower up 035c
    if inc == True:
        ls "<lick> Thank you... brother..."
    else:
        ls "<lick> Thank you... [pov]..."
    povi "She seems even more eager to help me now. I wonder if it's because I told her she turns me on."
    scene showerupstairs 7am shower up 036c
    "She puts the tip of your dick in her mouth."
    pov "That is so good [ls]!"
    ls "Hnng...!"
    povi "She's really going to town on my cock."
    ls "<lick><lick>"
    if inc == True:
        pov "Your sexy little mouth feels so good, little sis. I'm going to cum soon!"
    else:
        pov "Your sexy little mouth feels so good, [ls]. I'm going to cum soon!"
    ls "Omphay!"
    call screen showerup7extcorbjcumlove

screen showerup7extcorbjcumlove():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('showerup7extcorbjcumlove'), Jump('showerup7extcorbjcuminlove')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "edited/gui/icons/icon_blowjob_love_%s.png" action (Hide('showerup7extcorbjcumlove'), Jump('showerup7extcorbjcumoutlove')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerup7extcorbjcuminlove:
    pov "Can I cum in your mouth?"
    ls "Mmhmm!"
    "You stoke the side of her head while you cum. She seems to lean into your hand while sucking even harder on your cock."
    scene showerupstairs 7am shower up 037ci
    pov "HNNG...!"
    with vpunch
    ls "Hnn..."
    "You spray your sperm inside her mouth."
    pov "Oh yes, so good."
    with vpunch
    povi "She tried to move back at first, but she much had just been surprised. She's swallowing it down now on her own."
    ls "Hnn... <gulp> <gulp>"
    pov "Good girl. Drink it all down."
    scene showerupstairs 7am shower up 038ci
    "She looks up lovingly at you."
    ls "Hnng..."
    if inc == True:
        pov "You did very good, little sis."
    else:
        pov "You did very good, [ls]."
    pov "I needed that. I'm glad you helped me out like that."
    pov "Did you like it too?"
    ls "Hnng... y-yes..."
    povi "So sweet."
    pov "Did you like how it tastes?"
    ls "Hmmm..."
    "She gives you a tiny nod up and down."
    pov "I'm glad. So should I come and see you tomorrow morning too?"
    ls "Mmmhmm..."
    pov "Ok, see you then."
    ls "Hnng..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstcor = True
    $ showerup7amextfirstcor2 = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

label showerup7extcorbjcumoutlove:
    pov "Can I cum on your face?"
    ls "Mmhmm!"
    "You stoke the side of her head while you pull out to cum on her. She seems to lean into your hand while she waits for you to cum."
    scene showerupstairs 7am shower up 037co
    pov "HNNG...!"
    with vpunch
    ls "Hnn..."
    "You spray your cum on her face."
    pov "Oh yes, so good."
    with vpunch
    povi "She tried to move back at first, but she much had just been surprised. She's holding still now."
    scene showerupstairs 7am shower up 038co
    "She looks up lovingly at you."
    ls "Hnng..."
    if inc == True:
        pov "You did very good, little sis."
    else:
        pov "You did very good, [ls]."
    pov "I needed that. I'm glad you helped me out like that."
    pov "Did you like it too?"
    ls "Hnng... y-yes..."
    povi "So sweet."
    pov "Do you like how it feels on your face?"
    ls "Hmmm..."
    "She gives you a tiny nod up and down."
    pov "I'm glad. So should I come and see you tomorrow morning too?"
    ls "Mmmhmm..."
    pov "Ok, see you then."
    ls "Hnng..."
    scene black
    "You get dressed and leave the bathroom."
    $ showerup7amextfirstcor = True
    $ showerup7amextfirstcor2 = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup
