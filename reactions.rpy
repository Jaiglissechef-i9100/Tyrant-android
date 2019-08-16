#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label alexisreac:
    scene black
    "You leave your room."
    scene lilsisroom 62am 001
    ls "Good morning [pov]."
    pov "Oh, good morning [ls]."
    pov "Come with me, I need to talk to you."
    ls "Huh?"
    scene lilsisroom 62am 002
    ls "What is it? Did something happen?"
    pov "I want to talk with you about..."
    if d1ranormal == True or d1ralove == True or d1racor == True or d1racorf == True or d1rantrdavideyb == True:
        pov "Our date."
        jump alreacdate
    elif b4ralove == True or b4racor == True or b4rantrdaviden == True or b4rantrdavidey == True or b4rantrdavidei == True:
        pov "what happened in the basement."
        jump alreacbase

label alreacdate:
    if d1rantrdavidey == True and d1ranormal == True or d1rantrdavidey == True and d1ralove == True or d1rantrdavidey == True and d1racor == True or d1rantrdavidey == True and d1racorf == True:
        jump alreacdatedavide
    elif d1rantrdaviden == True and d1ranormal == True or d1rantrdaviden == True and d1ralove == True or d1rantrdaviden == True and d1racor == True or d1rantrdaviden == True and d1racorf == True:
        jump alreacdatedavidedeny
    elif d1rantrdavidey == False and d1ranormal == True or d1rantrdavidey == False and d1ralove == True or d1rantrdavidey == False and d1racor == True or d1rantrdavidey == False and d1racorf == True:
        jump alreacdatenodavide
    elif d1rantrdaviden == False and d1ranormal == True or d1rantrdaviden == False and d1ralove == True or d1rantrdaviden == False and d1racor == True or d1rantrdaviden == False and d1racorf == True:
        jump alreacdatenodavide
    elif d1rantrdavideyb == True:
        jump alreacdatedavideabort

label alreacdatedavideabort:
    scene lilsisroom 62am 003b
    ls "Our date..."
    pov "Yes when you met your new \"friend\"."
    ls "You mean Davide?"
    pov "Yes, he seems to be very interested in you."
    scene lilsisroom 62am 004d
    ls "Stop being like that! I can decide who my friends are!"
    pov "But he's an asshole and he'e going to take advantage of you!"
    ls "Are you jealous of him?"
    pov "No! I just worry about you."
    ls "I don't believe you! You're lying!"
    pov "But..."
    ls "Get out! Now!"
    scene black
    "You leave her room."
    povi "Damn it!"
    jump alreacend

label alreacdatedavide:
    scene lilsisroom 62am 003b
    ls "Our date..."
    pov "Yes when you met your new \"friend\"."
    ls "You mean Davide?"
    pov "Yes, he seems to be very interested in you."
    scene lilsisroom 62am 004b
    ls "Really? You think so?"
    povi "Damn, is she joking with me? Or is she really that naive?"
    pov "Yes, it was really hard to miss!"
    ls "Oh..."
    pov "He really likes you. I'm sure uou'll notice it when you meet him again."
    povi "Hm... is that really a good idea?"
    ls "That's great! I like him too. He's so strong... and big... and that cool hair-cut..."
    pov "Ok, ok that's enough! I goet it."
    if d1ranormal == True:
        jump alreacdate2normal
    elif d1ralove == True:
        jump alreacdate2love
    elif d1racor == True or d1racorf == True:
        jump alreacdate2cor

label alreacdatedavidedeny:
    scene lilsisroom 62am 003b
    ls "Our date..."
    pov "Yes when you met that guy."
    scene lilsisroom 62am 011b
    ls "You mean that black man?"
    ls "I didn't like him. He scared me a little."
    pov "That's good. I don't like him either."
    if inc == True:
        pov "He's a friend of mom and dad. And mom doesn't want him to know about you."
    else:
        pov "He's a friend of your mom and dad. And your mom doesn't want him to know about you."
    ls "Why...?"
    pov "I think he would like to fuck you or even worse, rape you!"
    ls "Now I'm more scared."
    pov "Don't worry, I'll protect you."
    ls "Oh... Ok."
    pov "But back to our date..."
    if d1ranormal == True:
        jump alreacdate2normal
    elif d1ralove == True:
        jump alreacdate2love
    elif d1racor == True or d1racorf == True:
        jump alreacdate2cor

label alreacdatenodavide:
    if d1ranormal == True:
        jump alreacdate2normal
    elif d1ralove == True:
        jump alreacdate2love
    elif d1racor == True or d1racorf == True:
        jump alreacdate2cor

label alreacdate2normal:
    pov "Sorry we couldn't continue after you fell."
    scene lilsisroom 62am 004n
    ls "Yes, but it did hurt."
    pov "I'm sorry, but that it was your punishment for cheating, dummy!"
    scene lilsisroom 62am 004b
    ls "Hahaha... no you're the dummy!"
    ls "But a lovable dummy, so it's ok!"
    scene lilsisroom 62am 020
    ls "Oh, I need to go to the bathroom now."
    ls "See you later, DUMMY!"
    pov "..."
    jump alreacend

label alreacdate2love:
    pov "Let's talk about what happened after I found you."
    scene lilsisroom 62am 004b
    if inc == True:
        ls "That my hero brother saved me when I fell?"
    else:
        ls "That my hero saved me when I fell?"
    pov "Hehe..."
    pov "I meant your kiss... or our kissing..."
    scene lilsisroom 62am 011b
    ls "Was it wrong? But you said..."
    pov "Oh now... It was just fine. I liked it."
    pov "I just want to make sure that you're really ok with that."
    if inc == True:
        ls "Ok with kissing my big brother even if it's forbidden?"
    else:
        ls "Ok with kissing you even if it's forbidden?"
    pov "Yes..."
    scene lilsisroom 62am 005b
    ls "<kiss>"
    povi "Oh that's a good answer."
    scene lilsisroom 62am 004b
    ls "You had another question? <giggle>"
    if inc == True:
        pov "No, not anymore my lovely lil sis."
    else:
        pov "No, not anymore my lovely [ls]."
    ls "<giggle>"
    scene lilsisroom 62am 020
    ls "Oh, I need to go to the bathroom now."
    ls "See you later, lovely dummy!"
    pov "..."
    jump alreacend

label alreacdate2cor:
    pov "Let's talk about what happened after I found you."
    scene lilsisroom 62am 004a
    ls "Oh, when you... you touched me..."
    pov "Yes... but did you liked it."
    ls "Well... yes but..."
    ls "We shouldn't do that, it's forbidden."
    povi "Not this crap again!"
    pov "We did it already and I could tell by your reaction that you wanted more."
    ls "No! ...you're wrong."
    scene lilsisroom 62am 005a
    pov "I'm not! You enjoyed it very much!"
    pov "Don't you want me to the boy you share this sort of thing with! Someone that loves you like I do?"
    ls "..."
    pov "See? You admit it with your silence."
    if d1racorf == True:
        scene lilsisroom 62am 006a
        ls "Hnn..."
        pov "We known each other all our lives and now your grown up and you realize that you want me to be your first."
        ls "Your hand..."
        pov "Is on your beautiful breast. You want this, don't you?"
        scene lilsisroom 62am 007a
        ls "Hah..."
        pov "Like when I licked you down there. You loved your orgasm!"
        ls "Hnn..."
        pov "You're even shivering right now. I bet you're already a little wet."
        ls "Hah..."
        scene lilsisroom 62am 008a
        pov "So stop denying it, you can just admit it if you want."
        pov "You sucked my dick and tasted my sperm. And you loved it, I saw that."
        if inc == True:
            ls "Hah... big brother..."
        else:
            ls "Hah... [pov]..."
        pov "So maybe we should take this further? Make this bed shake as we make love?"
        ls "Hah... hah... stop!"
        scene black
        "[ls] suddenly stands up and runs to the door."
        scene lilsisroom 62am 020
        ls "I need to go to the bathroom now."
        ls "Hah... hah..."
        pov "Don't touch yourself!"
        povi "Very good, haha."
        jump alreacend
    else:
        ls "No, you're wrong."
        scene black
        "She frees herself and runs to the door."
        scene lilsisroom 62am 020
        ls "I need to go to the bathroom now."
        ls "Please leave my room."
        pov "Hey [ls], I'm sorry."
        povi "Damn, I need to convince her more."
        jump alreacend

label alreacbase:
    if b4ralove == True:
        jump alreacbaselove
    elif b4racor == True:
        jump alreacbasecor
    elif b4rantrdaviden == True:
        jump alreacbasedavideno
    elif b4rantrdavidey == True:
        jump alreacbasedavideyes
    elif b4rantrdavidei == True:
        jump alreacbasedavidei

label alreacbasecor:
    scene lilsisroom 62am 003a
    ls "The basement..."
    if inc == True:
        pov "Yes, mostly about your behavior when mom was there."
    else:
        pov "Yes, mostly about your behavior when your mom was there."
    ls "Hnng..."
    pov "And when she masturbated right by us."
    scene lilsisroom 62am 004a
    ls "She acted like a... slut..."
    pov "Yes, but you started to get horny too. Like a daughter of a slut would."
    ls "No! Don't say that."
    scene lilsisroom 62am 005a
    pov "But that happened! And you enjoyed it even more when I touched you."
    ls "I... I was just overwhelmed."
    if inc == True:
        pov "You're a bad liar lil sis."
    else:
        pov "You're a bad liar [ls]."
    pov "You're shivering right now when I accuse you of being a slut."
    ls "I'm not a slut."
    if inc == True:
        pov "No, you're not. Now! But I know you. You like the idea of being naughty like mom."
    else:
        pov "No, you're not. Now! But I know you. You like the idea of being naughty like your mom."
    scene lilsisroom 62am 006a
    ls "What are you doing?"
    pov "Proving that you want this."
    ls "You're touching me..."
    pov "Yes I am. Like before when moaned like woman begging for it."
    ls "But I told you..."
    pov "Ssshhh..."
    ls "No!"
    scene black
    "She frees herself and runs to the door."
    scene lilsisroom 62am 020
    ls "I need to go to the bathroom now."
    ls "Please leave my room."
    pov "Hey [ls], I'm sorry."
    povi "Damn, I need to convince her more."
    jump alreacend

label alreacbaselove:
    scene lilsisroom 62am 003b
    ls "The basement..."
    if inc == True:
        pov "Yes, mostly your behavior when mom was there."
    else:
        pov "Yes, mostly your behavior when your mom was there."
    ls "You already helped me there."
    pov "Yes but I was a little confused about your kiss."
    scene lilsisroom 62am 004b
    ls "Why? We did that before."
    pov "You french kissed me."
    scene lilsisroom 62am 004n
    ls "Was that wrong?"
    pov "No. But why you did you do it? It was our first time."
    scene lilsisroom 62am 004b
    ls "So it was your first time too?"
    ls "Did I steal your french kiss virginity? <giggle>"
    pov "No, you didn't. But why did you gave me one after you were so unsure about kissing in the first place."
    ls "I don't know for sure. I felt very safe with you there."
    pov "Oh, that's good."
    ls "And I feel very safe right now too."
    scene lilsisroom 62am 005b
    ls "<kiss>"
    povi "What a nice surprise. She's opening herself up to me and more."
    ls "<giggle>"
    povi "What's the matter now?"
    scene lilsisroom 62am 006b
    ls "<kiss> <lick>"
    povi "Oh... another french kiss."
    if inc == True:
        "You and your little sister enjoy making out for a while."
    else:
        "You and [ls] sister enjoy making out for a while."
    scene lilsisroom 62am 007b
    ls "Hah... hah..."
    pov "My tongue taste that good?"
    if inc == True:
        ls "You really are a dummy, big brother."
    else:
        ls "You really are a dummy, [pov]."
    ls "But you're my dummy. <giggle>"
    povi "Her dummy? Does she want me to be her boyfriend?"
    scene lilsisroom 62am 020
    ls "I need to go to the bathroom now."
    ls "See you later, my dummy!"
    pov "Thanks for the kiss!"
    ls "<giggle>"
    jump alreacend

label alreacbasedavideno:
    pov "When you were flirting with that idiot while I was still there."
    ls "Then why did you still hide?"
    pov "Because..."
    ls "You're a coward?"
    pov "What...?"
    scene lilsisroom 62am 004d
    ls "Do you think I'm stupid?"
    pov "Wha..."
    ls "You're afraid of him and now you're jealous because I like him!"
    pov "No, because he's an asshole."
    ls "That's not your decision!"
    pov "But..."
    ls "Get out! Now!"
    scene black
    "You leave her room."
    povi "Damn!"
    jump alreacend

label alreacbasedavidei:
    pov "When that asshole found you!"
    ls "Yes I was a little scared too. He was so aggressive."
    scene lilsisroom 62am 011b
    pov "That could have ended badly."
    ls "You're right. I'm glad that you saved me."
    if inc == True:
        pov "There's a reason why mom doesn't want you to know him."
    else:
        pov "There's a reason why your mom doesn't want you to know him."
    ls "Now I'm even more scared."
    pov "I'm sorry that I scared you but you needed to know that."
    ls "Thank you..."
    scene lilsisroom 62am 020
    ls "I need to go to the bathroom now."
    pov "..."
    jump alreacend

label alreacbasedavideyes:
    pov "When you had fun with your new \"friend\"."
    ls "We're not together."
    pov "Oh that'll happen very soon."
    scene lilsisroom 62am 004b
    ls "You're jealous? <giggle>"
    pov "Haha, maybe...?"
    ls "I would understand that. He's so strong."
    if lsisproninterracial >= 4:
        ls "And so black!"
    pov "Haha, stop it."
    pov "But maybe he'll share you with me."
    ls "Share? What do you mean?"
    pov "Two men on one girl. You have at least 3 usable holes."
    scene lilsisroom 62am 011b
    ls "You mean...?"
    pov "I should ask him soon."
    ls "Two men together..."
    pov "Hahaha, I was kidding. Look at your face."
    scene lilsisroom 62am 004b
    if inc == True:
        ls "Oh, you're a bad big brother. <giggle>"
    else:
        ls "Oh you're bad [pov]. <giggle>"
    pov "But I hope you won't be disappointed."
    ls "Huh?"
    pov "He's going to conquer you really fast. You'll have to have a lot of sex with him."
    ls "Oh, stop it. <giggle>"
    pov "You like him that much?"
    ls "<giggle> Maybe I should convince him that he should conquer you too!"
    pov "Hahaha, ouch."
    scene lilsisroom 62am 020
    ls "I need to go to the bathroom now."
    ls "Be careful that you don't get conquered. <giggle>"
    pov "Haha..."
    jump alreacend

label alreacend:
    $ d1ranormal = False
    $ d1ralove = False
    $ d1racor = False
    $ d1racorf = False
    $ d1rantrdavidey = False
    $ d1rantrdaviden = False
    $ d1rantrdavideyb = False
    $ b4ralove = False
    $ b4racor = False
    $ b4rantrdaviden = False
    $ b4rantrdavidey = False
    $ b4rantrdavidei = False
    if d9rnntri == True or d9rnntr == True or d9rncor == True or d9rncorf == True or d9rnlove == True or d9rnlovef == True or b9rnntr == True or b9rnntrmir == True or b9rnlove == True or b9rncor == True:
        $ dtime = 62
        jump nicolereac
    else:
        $ dtime = 7
        jump mcroom

label nicolereac:
    scene black
    "You go down to the kitchen."
    if nicolereddresswear == True:
        scene kitchen 6am 001cc1
    elif nicolebabydollwear == True:
        scene kitchen 6am 001cc2
    elif nicolesweaterpantswear == True:
        scene kitchen 6am 001cl1
    elif nicolerobewear == True:
        scene kitchen 6am 001cl2
    else:
        scene kitchen 6am 001
    if inc == True:
        povi "Oh, mom is already up."
    else:
        povi "Oh, [mother] is already up."
    povi "I should go say hello."
    call screen nicreacmeet

screen nicreacmeet():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('nicreacmeet'), Jump('nicreaccor')) hovered tt.Action ("Slap her ass [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('nicreacmeet'), Jump('nicreaclove')) hovered tt.Action ("Say good morning [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicreaccor:
    $ momcorruption += 1
    if nicolereddresswear == True:
        scene kitchen 6am 002acc1
    elif nicolebabydollwear == True:
        scene kitchen 6am 002acc2
    elif nicolesweaterpantswear == True:
        scene kitchen 6am 002acl1
    elif nicolerobewear == True:
        scene kitchen 6am 002acl2
    else:
        scene kitchen 6am 002a
    with vpunch
    mom "Aaah..."
    povi "Damn, that ass..."
    if nicolereddresswear == True:
        scene kitchen 6am 003acc1
    elif nicolebabydollwear == True:
        scene kitchen 6am 003acc2
    elif nicolesweaterpantswear == True:
        scene kitchen 6am 003acl1
    elif nicolerobewear == True:
        scene kitchen 6am 003acl2
    else:
        scene kitchen 6am 003a
    mom "Oh it's you. Don't scare me like that."
    povi "Hm... no complaining that I slapped her ass. Good."
    pov "But I love your ass so much!"
    mom "Hnn..."
    if inc == True:
        pov "We need to talk mom."
    else:
        pov "We need to talk [mother]."
    if d9rnntri == True or d9rnntr == True or d9rncor == True or d9rncorf == True or d9rnlove == True or d9rnlovef == True:
        pov "About our date."
    elif b9rnntr == True or b9rnntrmir == True or b9rnlove == True or b9rncor == True:
        pov "About what happened in the basement."
    jump nicreactalk

label nicreaclove:
    if inc == True:
        pov "Good morning, mom!"
    else:
        pov "Good morning, [mother]!"
    if nicolereddresswear == True:
        scene kitchen 6am 002bcc1
    elif nicolebabydollwear == True:
        scene kitchen 6am 002bcc2
    elif nicolesweaterpantswear == True:
        scene kitchen 6am 002bcl1
    elif nicolerobewear == True:
        scene kitchen 6am 002bcl2
    else:
        scene kitchen 6am 002b
    mom "Oh, good morning [pov]."
    pov "I knew I would find you at the coffee-maker so early, haha."
    mom "Haha, yes."
    if inc == True:
        pov "We need to talk mom."
    else:
        pov "We need to talk [mother]."
    if d9rnntri == True or d9rnntr == True or d9rncor == True or d9rncorf == True or d9rnlove == True or d9rnlovef == True:
        pov "About our date."
    elif b9rnntr == True or b9rnntrmir == True or b9rnlove == True or b9rncor == True:
        pov "About what happened in the basement."
    jump nicreactalk

label nicreactalk:
    if d9rncor == True or d9rncorf == True or b9rncor == True:
        jump nicreactalkcor
    elif d9rnlove == True or d9rnlovef == True or b9rnlove == True or d9rnntri == True:
        jump nicreactalklove
    elif d9rnntr == True or b9rnntr == True or b9rnntrmir == True:
        jump nicreactalkntr
    else:
        jump nicreacend

label nicreactalkcor:
    if nicolereddresswear == True:
        scene kitchen 6am 004acc1
    elif nicolebabydollwear == True:
        scene kitchen 6am 004acc2
    elif nicolesweaterpantswear == True:
        scene kitchen 6am 004acl1
    elif nicolerobewear == True:
        scene kitchen 6am 004acl2
    else:
        scene kitchen 6am 004a
    if d9rncor == True:
        mom "I know! I ruined our date."
        mom "I'm so sorry we had to hide when that man showed up there."
        pov "I'm not mad with you, it wasn't your fault."
        pov "And I get the chance to spend some \"intimate\" time with you."
        if nicolereddresswear == True:
            scene kitchen 6am 004bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 004bcl2
        else:
            scene kitchen 6am 004b
        mom "I'm not sure that was right. We probably shouldn't have done that."
        pov "But you loved the thrill of it too, didn't you?"
        mom "..."
        if inc == True:
            pov "We should do this more often. I want to explore your sexy body more, mom!"
        else:
            pov "We should do this more often. I want to explore your sexy body more, [mother]!"
        mom "Come on! Stop saying such things!"
        pov "Nope! It will happen and you know that!"
        mom "I don't want to have this conversation anymore! Cut it out!"
        if nicolereddresswear == True:
            scene kitchen 6am 020cc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 020cc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 020cl1
        elif nicolerobewear == True:
            scene kitchen 6am 020cl2
        else:
            scene kitchen 6am 020
        mom "I'll have my coffee now and we can just forget about this conversation!"
        pov "Don't leave me like that."
        mom "No!"
        povi "Damn, I'll have to get further next time."
        jump nicreacend
    elif d9rncorf == True:
        mom "I know! I ruined our date."
        mom "I'm so sorry we had to hide when that man showed up there."
        pov "I'm not mad with you, it wasn't your fault."
        pov "And I get the chance to spend some \"intimate\" time with you."
        if nicolereddresswear == True:
            scene kitchen 6am 004bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 004bcl2
        else:
            scene kitchen 6am 004b
        mom "I'm not sure that was right. We probably shouldn't have done that."
        pov "But you loved the thrill of it too, didn't you?"
        mom "..."
        if inc == True:
            pov "We should do this more often. I want to explore your sexy body more, mom!"
        else:
            pov "We should do this more often. I want to explore your sexy body more, [mother]!"
        mom "Stop saying such things!"
        pov "No! It's going to happen again and you know it. I think you even want it!"
        mom "I don't want to have this conversation anymore! Cut it out!"
        pov "I can't! We've gone this far, we need to talk about this now!"
        pov "First it's about time you'd show me those fine tits of yours again, don't you think?"
        mom "What...?"
        pov "Oh you went that far on our date and now your shy, haha?"
        if nicolereddresswear == True:
            scene kitchen 6am 005acc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 005acc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 005acl1
        elif nicolerobewear == True:
            scene kitchen 6am 005acl2
        else:
            scene kitchen 6am 005a
        mom "Hnn..."
        pov "I missed them so much. I love to play with them."
        if nicolereddresswear == True:
            scene kitchen 6am 007acc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 007acc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 007acl1
        elif nicolerobewear == True:
            scene kitchen 6am 007acl2
        else:
            scene kitchen 6am 007a
        mom "We did it to get that jerk away and you know that. But it's still wrong."
        pov "Hmm, I'm not sure. You enjoyed it a little to much."
        mom "You tricked me and took advantage of me there."
        pov "And you loved it, playing the innocent housewife."
        mom "I don't..."
        if nicolereddresswear == True:
            scene kitchen 6am 008acc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 008acc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 008acl1
        elif nicolerobewear == True:
            scene kitchen 6am 008acl2
        else:
            scene kitchen 6am 008a
        if inc == True:
            pov "Is that why you didn't fight back, when I fucked you then?"
            pov "A strong mother and women just let herself get tricked and didn't fight back when her son fucked her? I don't think so."
        else:
            pov "Is that why you didn't fight back, when I fucked you then ?"
            pov "A strong woman let herself get tricked and didn't fight back when I fucked her? I don't think so."
        pov "Stop talking like that!"
        if nicolereddresswear == True:
            scene kitchen 6am 009acc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 009acc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 009acl1
        elif nicolerobewear == True:
            scene kitchen 6am 009acl2
        else:
            scene kitchen 6am 009a
        mom "..."
        pov "And I bet you're also wet right now, thinking about that orgasm you had."
        pov "You love it that I took what I wanted. And especially the idea of me taking it from you."
        if inc == True:
            pov "The son that conquered his mother. Even when it's forbidden and against the law."
        else:
            pov "The son of your best friend that conquered you."
        pov "And that it has to be a secret relationship. The thrill of doing such a naughty thing."
        if nicolereddresswear == True:
            scene kitchen 6am 010acc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 010acc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 010acl1
        elif nicolerobewear == True:
            scene kitchen 6am 010acl2
        else:
            scene kitchen 6am 010a
        mom "Hah..."
        pov "So you're honest now? Good!"
        pov "Because I'll fuck you even more. Until you're all mine!"
        mom "Hnn..."
        mom "Please... don't say anyone..."
        pov "Oh I won't, it'll be our secret!"
        pov "But you should stop fighting yourself and accept that you love to have my dick inside you."
        mom "..."
        pov "Haha, still trying to fight?"
        pov "Well, that'll change soon."
        "You remove your hand from her crotch."
        if nicolereddresswear == True:
            scene kitchen 6am 020cc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 020cc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 020cl1
        elif nicolerobewear == True:
            scene kitchen 6am 020cl2
        else:
            scene kitchen 6am 020
        mom "Hnn..."
        pov "Have fun with your coffee, my slut!"
        mom "..."
        jump nicreacend
    elif b9rncor == True:
        mom "It was so wrong what you did in the basement."
        pov "No it wasn't! That's one of my privileges now!"
        mom "But you humiliated me in front of others."
        pov "Oh, so it's OK if it's not in front of others, haha?"
        mom "No..."
        if inc == True:
            pov "Show me your tits mom!"
        else:
            pov "Show me your tits [mother]!"
        mom "What...?"
        pov "You want to get humiliated without an audience. Then we'll do it now."
        mom "I didn't meant it like that."
        pov "But I do! Or should I ask Davide about those privileges?"
        if nicolereddresswear == True:
            scene kitchen 6am 005acc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 005acc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 005acl1
        elif nicolerobewear == True:
            scene kitchen 6am 005acl2
        else:
            scene kitchen 6am 005a
        mom "You treat me like a whore..."
        pov "Oh come on. No, more like a toy!"
        mom "..."
        pov "It was your idea to participate in the first place. So I'll play with you then."
        mom "That's not the way it's meant to be! You know why I have to do that!"
        if nicolereddresswear == True:
            scene kitchen 6am 006acc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 006acc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 006acl1
        elif nicolerobewear == True:
            scene kitchen 6am 006acl2
        else:
            scene kitchen 6am 006a
        pov "Yes and I'll play my role well.  And I will have as much fun with you as I can, and those huge tits!"
        mom "Hnng..."
        if inc == True:
            pov "You and dad wanted me to participate and I'll do it now. So it was your choice!"
        else:
            pov "You and Bruce wanted me to participate and I'll do it now. So it was your choice!"
        mom "Why...?"
        if nicolereddresswear == True:
            scene kitchen 6am 007acc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 007acc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 007acl1
        elif nicolerobewear == True:
            scene kitchen 6am 007acl2
        else:
            scene kitchen 6am 007a
        pov "You didn't think I could get this position did you, haha."
        pov "I have to participate on your shitty play now. So I still want some fun."
        pov "So be a good girl now and we can have both have fun until it ends."
        mom "Don't push your luck! Davide won't help you all the time!"
        pov "Ohh..."
        povi "Hm... I should stay aware."
        mom "I'll have my coffee now. Consider carefully what you choose to do!"
        if nicolereddresswear == True:
            scene kitchen 6am 020cc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 020cc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 020cl1
        elif nicolerobewear == True:
            scene kitchen 6am 020cl2
        else:
            scene kitchen 6am 020
        povi "Hmm... she won't give in that easy. But I'll break her."
        jump nicreacend

label nicreactalklove:
    if d9rnlove == True:
        if nicolereddresswear == True:
            scene kitchen 6am 003bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 003bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 003bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 003bcl2
        else:
            scene kitchen 6am 003b
        mom "I know! I ruined our date."
        mom "I'm so sorry we had to hide when that man showed up there."
        pov "I'm not mad with you, it wasn't your fault."
        pov "And I get the chance to spend some \"intimate\" time with you."
        if nicolereddresswear == True:
            scene kitchen 6am 004bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 004bcl2
        else:
            scene kitchen 6am 004b
        mom "I'm not sure that was right. We probably shouldn't have done that."
        pov "I know. I'm so sorry, but I couldn't hold back. I'm just so in love with you."
        mom "Hm... don't say that."
        mom "It was my fault! I should have stopped it, but..."
        pov "But...?"
        if nicolereddresswear == True:
            scene kitchen 6am 005bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 005bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 005bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 005bcl2
        else:
            scene kitchen 6am 005b
        mom "..."
        if inc == True:
            pov "It's ok mom! I don't think it was a bad thing."
        else:
            pov "It's ok [mother]! I don't think it was a bad thing."
        pov "Come here!"
        if nicolereddresswear == True:
            scene kitchen 6am 006bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 006bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 006bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 006bcl2
        else:
            scene kitchen 6am 006b
        pov "I'm not mad. I love you!"
        mom "Thank you [pov]..."
        if nicolereddresswear == True:
            scene kitchen 6am 007bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 007bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 007bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 007bcl2
        else:
            scene kitchen 6am 007b
        mom "Huh?"
        pov "<kiss>"
        if inc == True:
            pov "I love you mom! I love you so much!"
        else:
            pov "I love you [mother]! I love you so much!"
        mom "Hnn..."
        if nicolereddresswear == True:
            scene kitchen 6am 008bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 008bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 008bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 008bcl2
        else:
            scene kitchen 6am 008b
        pov "I can't stop kissing you..."
        mom "..."
        mom "Sweetie... please..."
        pov "..."
        mom "We need to stop!"
        if nicolereddresswear == True:
            scene kitchen 6am 020cc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 020cc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 020cl1
        elif nicolerobewear == True:
            scene kitchen 6am 020cl2
        else:
            scene kitchen 6am 020
        if inc == True:
            pov "I'm sorry, mom!"
        else:
            pov "I'm sorry, [mother]!"
        mom "I'm just so confused right now..."
        mom "I care about you too, maybe more than I should..."
        povi "So does this mean she wants this too?"
        jump nicreacend
    elif d9rnlovef == True:
        if nicolereddresswear == True:
            scene kitchen 6am 003bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 003bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 003bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 003bcl2
        else:
            scene kitchen 6am 003b
        mom "I know! I ruined our date."
        mom "I'm so sorry we had to hide when that man showed up there."
        pov "I'm not mad with you, it wasn't your fault."
        pov "And I get the chance to spend some \"intimate\" time with you."
        if nicolereddresswear == True:
            scene kitchen 6am 004bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 004bcl2
        else:
            scene kitchen 6am 004b
        mom "I'm not sure that was right. We probably shouldn't have done that."
        pov "I know. I'm so sorry, but I couldn't hold back. I'm just so in love with you."
        mom "Hm... don't say that."
        mom "It was my fault! I should have stopped it, but..."
        pov "But...?"
        if nicolereddresswear == True:
            scene kitchen 6am 005bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 005bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 005bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 005bcl2
        else:
            scene kitchen 6am 005b
        mom "..."
        if inc == True:
            pov "It's ok mom! I don't think it was a bad thing."
        else:
            pov "It's ok [mother]! I don't think it was a bad thing."
        pov "Come here!"
        if nicolereddresswear == True:
            scene kitchen 6am 006bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 006bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 006bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 006bcl2
        else:
            scene kitchen 6am 006b
        pov "I'm not mad. I love you!"
        mom "Thank you [pov]..."
        if nicolereddresswear == True:
            scene kitchen 6am 007bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 007bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 007bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 007bcl2
        else:
            scene kitchen 6am 007b
        mom "Huh?"
        pov "<kiss>"
        if inc == True:
            pov "I love you mom! I love you so much!"
        else:
            pov "I love you [mother]! I love you so much!"
        mom "Hnn..."
        if nicolereddresswear == True:
            scene kitchen 6am 008bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 008bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 008bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 008bcl2
        else:
            scene kitchen 6am 008b
        pov "I can't stop kissing you..."
        mom "..."
        pov "..."
        if nicolereddresswear == True:
            scene kitchen 6am 009bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 009bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 009bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 009bcl2
        else:
            scene kitchen 6am 009b
        if inc == True:
            pov "I love you so much, mom!"
        else:
            pov "I love you so much, [mother]!"
        pov "<kiss>"
        mom "Hmm..."
        mom "I love you too sweetie!"
        povi "Wow, she's kissing me back!"
        mom "<kiss>"
        if nicolereddresswear == True:
            scene kitchen 6am 010bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 010bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 010bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 010bcl2
        else:
            scene kitchen 6am 010b
        pov "So you're ok with this too?"
        mom "Hnn... nobody can know about this!"
        pov "Nobody will ever know. I promise!"
        povi "Oh my god! Is this really happening?"
        mom "I'm so confused..."
        pov "Don't be. You're with me. This is a good thing!"
        if nicolereddresswear == True:
            scene kitchen 6am 020cc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 020cc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 020cl1
        elif nicolerobewear == True:
            scene kitchen 6am 020cl2
        else:
            scene kitchen 6am 020
        mom "I need some time."
        mom "Forgive me..."
        povi "She still isn't at the point where she can admit it."
        povi "But I know now that it wasn't an accident. She has intimate feelings for me."
        povi "I'll give her some time and show her I will always be there for her."
        jump nicreacend
    elif b9rnlove:
        if nicolereddresswear == True:
            scene kitchen 6am 004ccc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004ccc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004ccl1
        elif nicolerobewear == True:
            scene kitchen 6am 004ccl2
        else:
            scene kitchen 6am 004c
        pov "Huh? You aren't mad anymore?"
        mom "No. You proved that you won't fall to the \"dark side\", so you really can be a great help here."
        pov "But... I spanked you..."
        mom "<giggle> Oh you're still such a gentleman. I'm so proud!"
        pov "What...?"
        if nicolereddresswear == True:
            scene kitchen 6am 005ccc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 005ccc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 005ccl1
        elif nicolerobewear == True:
            scene kitchen 6am 005ccl2
        else:
            scene kitchen 6am 005c
        mom "I told you to do it. And even then you still tried to behave."
        pov "I didn't want to punish you."
        mom "It's better to get punished from you then from that idiot."
        pov "Hm..."
        mom "Now I'm happy to see you down there helping us."
        if inc == True:
            pov "I'd love to help you, mom. I love you!"
        else:
            pov "I'd love to help you [mother]. I love you!"
        mom "<giggle>"
        if base9nickiss == True:
            pov "Why did you kiss me down there?"
            mom "I kissed you?"
            pov "Yes? Before I had to punish you."
            mom "No, I don't remember a kiss. <giggle>"
            povi "Is she playing with me?"
            if inc == True:
                pov "Mom!"
            else:
                pov "[mother]!"
            mom "I'm sorry. Maybe it was just your imagination?"
            povi "Oh still playing? I'll get you... "
            pov "Hmm..."
        if nicolereddresswear == True:
            scene kitchen 6am 006ccc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 006ccc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 006ccl1
        elif nicolerobewear == True:
            scene kitchen 6am 006ccl2
        else:
            scene kitchen 6am 006c
        mom "I need my coffee now. Let's talk another time."
        pov "OK."
        jump nicreacend
    elif d9rnntri == True:
        if nicolereddresswear == True:
            scene kitchen 6am 003bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 003bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 003bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 003bcl2
        else:
            scene kitchen 6am 003b
        mom "I know! I ruined our date."
        mom "I'm so sorry we had to hide when that man showed up there."
        pov "I'm not mad with you, it wasn't your fault."
        mom "But I chose the wrong place to hide."
        pov "Maybe. But I took care of that asshole."
        if nicolereddresswear == True:
            scene kitchen 6am 004acc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004acc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004acl1
        elif nicolerobewear == True:
            scene kitchen 6am 004acl2
        else:
            scene kitchen 6am 004a
        mom "I shouldn't put you in that much danger."
        pov "But everything worked out ok in the end!"
        mom "But it shouldn't have happened! I'm so sorry!"
        pov "Stop it!"
        if inc == True:
            pov "I wouldn't let anyone rape my mom, so cut it out."
        else:
            pov "I wouldn't let anyone rape you, so cut it out."
        mom "Next time I'll make it up to you, I promise."
        if nicolereddresswear == True:
            scene kitchen 6am 020cc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 020cc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 020cl1
        elif nicolerobewear == True:
            scene kitchen 6am 020cl2
        else:
            scene kitchen 6am 020
        if inc == True:
            pov "Mom! It's alright, I promise!"
        else:
            pov "[mother]! It's alright, I promise!"
        mom "...Thank...you..."
        jump nicreacend
    elif d9rnntr == True:
        if nicolereddresswear == True:
            scene kitchen 6am 003bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 003bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 003bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 003bcl2
        else:
            scene kitchen 6am 003b
        mom "I know! I ruined our date."
        mom "I'm so sorry we had to hide when that man showed up there."
        pov "I'm not mad with you, it wasn't your fault."
        mom "But I chose the wrong place to hide."
        mom "He found me and raped me!"
        povi "Why is she still lying? Why won't she admit that she liked it too?"
        povi "Is she hiding something. Maybe she lied about that guy?"
        pov "So we need to get revenge then!"
        if nicolereddresswear == True:
            scene kitchen 6am 004bcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004bcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004bcl1
        elif nicolerobewear == True:
            scene kitchen 6am 004bcl2
        else:
            scene kitchen 6am 004b
        mom "No!"
        mom "I mean, we can't..."
        pov "But after what he did, he has to pay!"
        mom "I'll ask Davide for help."
        pov "Oh I don't think this is something Davide can handle. We need the cops!"
        mom "We can't tell them and you know that!"
        pov "But he raped you!"
        if nicolereddresswear == True:
            scene kitchen 6am 004dcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004dcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004dcl1
        elif nicolerobewear == True:
            scene kitchen 6am 004dcl2
        else:
            scene kitchen 6am 004d
        mom "I told you to stop!"
        mom "I'll take care of that and you'll do nothing that could you in danger again!"
        mom "Do you understand that?"
        povi "What the fuck? She really won't let that that guy caught. Maybe this is something where I should dig in deeper."
        if inc == True:
            pov "OK, OK mom. Calm down, I got it."
        else:
            pov "OK, OK [mother]. Calm down, I got it."
        if nicolereddresswear == True:
            scene kitchen 6am 006dcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 006dcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 006dcl1
        elif nicolerobewear == True:
            scene kitchen 6am 006dcl2
        else:
            scene kitchen 6am 006d
        mom "I'm sorry about our date, but it's enough for now."
        pov "Sure..."
        povi "Wow, that escalated quickly..."
        jump nicreacend

label nicreactalkntr:
    if b9rnntr == True:
        if nicolereddresswear == True:
            scene kitchen 6am 004dcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004dcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004dcl1
        elif nicolerobewear == True:
            scene kitchen 6am 004dcl2
        else:
            scene kitchen 6am 004d
        mom "What's wrong with you?"
        pov "Huh?"
        mom "Don't play dumb!"
        pov "Is this because of the basement? I'm allowed to be down there now."
        mom "Maybe, but you didn't leave when I got punished. Because of you!"
        pov "Because of me?"
        mom "I didn't want to have you there and then you didn't leave when you should have."
        if nicole_revenge == True:
            povi "I couldn't leave, I needed to be there in case he hurt you. But I don't know if you'll understand..."
        else:
            pov "I don't get it. You did something wrong and got punished for that. How is that my fault?"
        if nicolereddresswear == True:
            scene kitchen 6am 005dcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 005dcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 005dcl1
        elif nicolerobewear == True:
            scene kitchen 6am 005dcl2
        else:
            scene kitchen 6am 005d
        mom "You stood there and watched me get punished!"
        if nicole_revenge == True:
            povi "You mean raped... I wish I could have stopped it!"
            mom "Aren't you going to say anything, you pervert!"
            mom "A normal guy would have left, but you stood there and watched me the whole time!"
            povi "I'm so sorry!"
            mom "There will be consequences!"
        else:
            pov "You mean as you got fucked!"
            mom "And now you admit it you pervert!"
            mom "A normal guy would have left, but you stood there and watched me the whole time!"
            pov "But you liked it!"
            mom "No I didn't! Shut up! There will be consequences!"
        if nicolereddresswear == True:
            scene kitchen 6am 006dcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 006dcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 006dcl1
        elif nicolerobewear == True:
            scene kitchen 6am 006dcl2
        else:
            scene kitchen 6am 006d
        mom "I still can't believe it. And you won't even apologize."
        pov "..."
        if nicole_ntr == True or nicole_voyeur == True or nicole_sadist == True:
            povi "Why is she so angry about that?"
        jump nicreacend
    elif b9rnntrmir == True:
        if nicolereddresswear == True:
            scene kitchen 6am 004dcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 004dcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 004dcl1
        elif nicolerobewear == True:
            scene kitchen 6am 004dcl2
        else:
            scene kitchen 6am 004d
        mom "What's wrong with you?"
        pov "Huh?"
        mom "Don't play dumb!"
        pov "Is this because of the basement? I'm allowed to be down there now."
        mom "Maybe, but you didn't leave when I got punished. Because of you!"
        pov "Because of me?"
        mom "I didn't want to have you there and then you didn't leave when you should have."
        if nicole_revenge == True:
            povi "I couldn't leave, I needed to be there in case he hurt you. But I don't know if you'll understand..."
        else:
            pov "I don't get it. You did something wrong and got punished for that. How is that my fault?"
        if nicolereddresswear == True:
            scene kitchen 6am 005dcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 005dcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 005dcl1
        elif nicolerobewear == True:
            scene kitchen 6am 005dcl2
        else:
            scene kitchen 6am 005d
        mom "And on top of that you fucked that whore, while I got punished!"
        if nicole_revenge == True:
            povi "You mean raped... I wish I could have stopped it!"
            mom "Aren't you going to say anything, you pervert!"
            mom "A normal guy would have left, but you stayed and fucked another woman while watching me too!"
            povi "I'm so sorry!"
            mom "There will be consequences!"
        else:
            pov "You mean as you got fucked!"
            mom "And now you admit it you pervert!"
            mom "A normal guy would have left, but you stayed and fucked another woman while watching me too!"
            pov "But you liked it!"
            mom "No I didn't! Shut up! There will be consequences!"
        if nicolereddresswear == True:
            scene kitchen 6am 006dcc1
        elif nicolebabydollwear == True:
            scene kitchen 6am 006dcc2
        elif nicolesweaterpantswear == True:
            scene kitchen 6am 006dcl1
        elif nicolerobewear == True:
            scene kitchen 6am 006dcl2
        else:
            scene kitchen 6am 006d
        mom "I still can't believe it. And not a word of apology."
        pov "..."
        if nicole_ntr == True or nicole_voyeur == True or nicole_sadist == True:
            povi "Why is she so angry about that?"
        jump nicreacend

label nicreacend:
    $ d9rnntri = False
    $ d9rnntr = False
    $ d9rncor = False
    $ d9rncorf = False
    $ d9rnlove = False
    $ d9rnlovef = False
    $ b9rnntr = False
    $ b9rnntrmir = False
    $ b9rnlove = False
    $ b9rncor = False
    $ base9nickiss = False
    $ dtime = 7
    jump kitchen
