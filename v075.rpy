

label proom19extcorruption:
    hide screen locations
    scene main parents room door
    $ proom19first = True
    pov "{i}Huh? Why is the door closed?{/i}"
    "You hear someone talking behind the door."
    if inc == True:
        pov "{i}That are the voices of mom and dad.{/i}"
    else:
        pov "{i}That are the voices of [mother] and Bruce.{/i}"
    pov "{i}Let's see what's going on.{/i}"
    "You open the door."
    if nicolereddresswear == True:
        scene parentsroom 7pm 002cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 002cc2
    else:
        scene parentsroom 7pm 002c
    pov "{i}What the hell is going on here?{/i}"
    dad "Come on, get your clothes off!"
    mom "But..."
    if nicolereddresswear == True:
        scene parentsroom 7pm 003cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 003cc2
    else:
        scene parentsroom 7pm 003c
    pov "What's going on here? Do you try to fuck my slut?"
    dad "Leave [pov]. Give us some privacy."
    mom "But..."
    pov "{i}This is so wrong. Bruce know that he isn't allowed to lay a hand on her, but she react so submissive.{/i}"
    pov "{i}Normally she would make a scene and tell him a lesson.{/i}"
    pov "{i}There's no way she became so submissive in this short time. But why is she acting like that?{/i}"
    if nicolereddresswear == True:
        scene parentsroom 7pm 004cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 004cc2
    else:
        scene parentsroom 7pm 004c
    dad "Did you understand me, [pov]. Get out of this room, I want to spend some time with my wife!"
    mom "Hnng..."
    pov "{i}Oh I think I get it. She's testing me, wanting to know if I'll stand up for my slut.{/i}"
    pov "{i}That I mean what I told her by being the slut of a strong gang member.{/i}"
    scene parentsroom 7pm 005c
    pov "I can't allow you to lay your hands on my slut!"
    dad "Are you serious? I endured your humiliation when you put up that little show for Davide. Even when it was too much for my taste."
    dad "But now we're alone, so I want to get back to normality."
    pov "You don't understand it. We have to play our little show all the time to be on the safe side."
    dad "No! She's still my wife."
    pov "{i}It's time to tell him the truth. Poor, dumb Bruce...{/i}"
    pov "She isn't your wife anymore. She's mine now, my slut, my playtoy."
    scene parentsroom 7pm 006c
    dad "You can't be..."
    dad "You're serious. Are you mad? You can't just steal my wife!"
    pov "I already did it. And she already accepted me as her new man!"
    pov "And you'll be a good boy and play along, we won't Davide get suspicious, won't we?"
    dad "You're... evil..."
    if nicolereddresswear == True:
        scene parentsroom 7pm 007cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 007cc2
    else:
        scene parentsroom 7pm 007c
    dad "We need to stop this now [mother]. He's gone mad."
    if inc == True:
        dad "He's your son and he wants to have you as his slut, fucking around with you, more than needed for our cover."
    else:
        dad "He's your best friends son and he wants to have you as his slut, fucking around with you, more than needed for our cover."
    dad "Say something! End this madness."
    mom "But..."
    mom "I'm his slut..."
    dad "..."
    scene parentsroom 7pm 008
    dad "You're crazy! Both of you! This isn't normal!"
    dad "I'll leave for now, but this isn't over yet!"
    if nicolereddresswear == True:
        scene parentsroom 7pm 009cc1
    elif nicolebabydollwear == True:
        scene parentsroom 7pm 009cc2
    else:
        scene parentsroom 7pm 009c
    pov "You did good slut. I'm proud."
    if inc == True:
        pov "You submitted to me, your son. I'm in charge of you now."
    else:
        pov "You submitted to me. I'm in charge of you now."
    pov "But I want you to come straight to me, when he try something again. You understand, slut?"
    mom "Y... yes [pov]."
    pov "Good! Now get naked, I need to fuck my slut now!"
    mom "But... [ls] is in the kitchen, she'll hear us!"
    pov "You didn't get it?"
    pov "You submitted to me in front of your ex-husband."
    if inc == True:
        pov "You're mine now, mom!"
        pov "And if I want to fuck my moms brains out, I'll do it whenever I want to!"
    else:
        pov "You're mine now, [mother]!"
        pov "And if I want to fuck your brains out, I'll do it whenever I want to!"
    pov "There's nothing to prevent me! Do you get it now?"
    mom "Yes... I submitted... Do as you please..."
    call screen proom19extcor

screen proom19extcor():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" xpos 348 ypos 316 action (Hide('proom19extcor'), Jump('proom19extcorbj')) hovered tt.Action ("Get naked and on your knees") focus_mask True
        imagebutton auto "gui/icons/icon_sex_corruption_%s.png" xpos 348 ypos 516 action (Hide('proom19extcor'), Jump('proom19extcorsex')) hovered tt.Action ("Get naked and crawl on the bed") focus_mask True

        frame:
            xalign .5
            text tt.value


label proom19extcorbj:
    pov "My dick needs your mouth now!"
    mom "Yes, [pov]."
    scene parentsroom 7pm 010cbj
    mom "<lick>"
    pov "Oh you're already on with it, good slut!"
    mom "<lick> Do... do you like it...?"
    if inc == True:
        pov "Yes, mom. I like your motivation."
    else:
        pov "Yes, [mother]. I like your motivation."
    pov "But just licking won't get me off, put it in your mouth!"
    mom "Yes."
    scene parentsroom 7pm 011cbj
    mom "Hmm... <suck>"
    pov "Very nice."
    mom "Hmm... hmm..."
    pov "You're doing the right thing now, showing me what a good slut you are."
    mom "Hmm..."
    pov "Put your hands behind your back and let me take control over your mouth."
    pov "So I can see that you put your fate in my hands."
    scene parentsroom 7pm 012cbjdt
    mom "Hnng..."
    pov "Good. You're mine to please me and I'll use you now."
    pov "Be a good slut and endure and submit."
    mom "Hmm..."
    scene parentsroom 7pm 014cbjdt
    mom "HNNG...!"
    pov "Ssshh... hold it."
    if inc == True:
        pov "Hold your son's big dick in your throat."
    else:
        pov "Hold my big dick in your throat."
    pov "Put all your trust in me. I'm in charge and I'll take good care of you."
    mom "Hnng..."
    pov "Hold it! You can endure it longer, you're MY slut!"
    mom "<choke>HNNG...!"
    scene parentsroom 7pm 013cbjdt
    mom "<choke> HRRRG...!"
    if inc == True:
        pov "You raised me and now you'll get your reward."
    else:
        pov "You cared about me when I was younger and now you'll get your reward."
    pov "And I'll protect you, because you're my property!"
    mom "<choke> HNNN...!"
    scene parentsroom 7pm 012cbjdt
    mom "Hnn... hnn..."
    pov "You did good. Putting all your trust in me and pleased me."
    if inc == True:
        pov "I'm proud of you, mom!"
    else:
        pov "I'm proud of you [mother]!"
    pov "But your submission made me so hard, I'm already about to come."
    pov "You're a very good cocksucker!"
    call screen proom19extbjcum

screen proom19extbjcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 748 ypos 316 action (Hide('proom19extbjcum'), Jump('proom19extbjcumin')) hovered tt.Action ("I'll cum in your mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1255 ypos 316 action (Hide('proom19extbjcum'), Jump('proom19extbjcumout')) hovered tt.Action ("I'll cum on your face") focus_mask True

        frame:
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
    scene black
    "You leave her."
    $ dtime += 1
    jump parentsroom

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
    scene black
    "You leave her."
    $ dtime += 1
    jump parentsroom

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

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 548 ypos 316 action (Hide('proom19extfuck'), Jump('proom19extfuckp')) hovered tt.Action ("I'll fuck your pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1155 ypos 316 action (Hide('proom19extfuck'), Jump('proom19extfucka')) hovered tt.Action ("I'll fuck your ass") focus_mask True

        frame:
            xalign .5
            text tt.value

label proom19extfucka:
    $ proom19fuckass = True
    jump proom19extfuckp

label proom19extfuckp:
    if proom19fuckass == True:
        scene parentsroom 7pm 011cdg
        mom "Hnn..."
        pov "So you feel my big dick on your tight hole?"
    else:
        scene parentsroom 7pm 011cdgp
        mom "Hnn..."
        pov "So you feel my big dick on your wet pussy?"
    mom "Yes..."
    pov "You push your dick slowly deeper."
    if proom19fuckass == True:
        scene parentsroom 7pm 013cdg
    else:
        scene parentsroom 7pm 013cdgp
    pov "I'll start gentle, but don't get false ideas. I'll give my slut a hard pounding as you need to get used to!"
    mom "Hmm..."
    pov "You need to get pounded hard, you wait for it. Don't you?"
    mom "Hnn..."
    scene parentsroom 7pm 012cdg
    mom "Aaah..."
    "You push hard and deep in her."
    pov "I asked you something, slut!"
    mom "Yes... I... need a hard pounding."
    pov "Good. Then you'll love it."
    "You start to fuck her hard and rough."
    if proom19fuckass == True:
        scene parentsroom 7pm 014cdg
    else:
        scene parentsroom 7pm 014cdgp
    mom "Ahhh... hah..."
    mom "You're so deep inside me!"
    if proom19fuckass == True:
        pov "Yes, your asshole needs to get used to a good pounding!"
    else:
        pov "Yes, your pussy needs to get used to a good pounding!"
    mom "Hah... aahh..."
    "Knock! Knock!"
    mom "Huh?"
    ls "Mom?"
    pov "<whisper>Damn, what is she doing here? You need to get rid of her!"
    mom "<whisper>OK. I'll send her away."
    scene parentsroom 7pm 015
    ls "Mom, you're naked?"
    mom "Yes... I..."
    mom "What do you need, honey?"
    if proom19fuckass == True:
        scene parentsroom 7pm 016a
        pov "{i}Damn, her asshole is still gaping. I can't wait to put my dick back in.{/i}"
    ls "I heard sounds like you having sex with someone, but Dad left the house before."
    mom "Oh... I... that was me."
    ls "You?"
    mom "I... I need to get rid of my... urges."
    ls "What...? What do you mean?"
    mom "Mommy was playing with herself..."
    ls "Playing...?"
    scene parentsroom 7pm 016
    ls "UGH! Don't tell me that mom!"
    mom "But..."
    ls "That's gross, telling me that, ugh!"
    scene parentsroom 7pm 017c
    pov "Good job. She ran away, so she'll disturb us not anymore."
    pov "Now I can pound you even harder until you'll beg for my sperm!"
    pov "Come back here slut!"
    mom "Yes [pov]."
    if proom19fuckass == True:
        scene parentsroom 7pm 014cdg
    else:
        scene parentsroom 7pm 014cdgp
    "You continue to fuck her even harder."
    mom "AAHHH...HAH..."
    pov "That's the way I like it. My slut screaming from my hard pounding!"
    mom "HAH... AHH!"
    scene parentsroom 7pm 012cdg
    pov "You're getting tighter and start to shake. You're about to cum?"
    mom "Yes [pov]. I'm so close, please allow me to cum."
    pov "Not now! You'll hold it a little longer."
    mom "I...I'll try..."
    pov "Be a good slut and endure and submit."
    mom "Yes, I'll submit myself to you!"
    if inc == True:
        pov "You raised me and now you'll get your reward."
    else:
        pov "You cared about me when I was younger and now you'll get your reward."
    pov "And I'll protect you, because you're my property!"
    mom "AAHH... HAH... PLEASE... LET ME CUM!"
    pov "Come here!"
    scene parentsroom 7pm 017cdg
    mom "AHHH... HAH..."
    pov "You'll need to submit more when you want to cum!"
    mom "I will!"
    if inc == True:
        pov "You love it to cum from your son's dick!"
        mom "Yes...!"
        pov "You're a bad mother, craving for the dick of your son!"
        mom "Yes! I'm bad. I'm the slut of my son, I love him using me!"
    else:
        pov "You love it to cum from the dick of your best friends son!"
        mom "Yes...!"
        pov "You're a bad woman, craving for my dick!"
        mom "Yes! I'm bad. I'm the slut of my best friends son, I love him using me!"
    pov "You're allowed to cum now slut!"
    scene parentsroom 7pm 015cdg
    mom "AHHHH... YEEEES!!!"
    "She cum hard."
    pov "Yes slut, this taking me over the edge too!"
    call screen proom19extfuckcum

screen proom19extfuckcum():
    default tt = Tooltip (" ")

    fixed:
        if proom19fuckass == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 748 ypos 316 action (Hide('proom19extfuckcum'), Jump('proom19extfuckcumassin')) hovered tt.Action ("I'll cum inside your ass") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1255 ypos 316 action (Hide('proom19extfuckcum'), Jump('proom19extfuckcumassout')) hovered tt.Action ("I'll cum on your ass") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 748 ypos 316 action (Hide('proom19extfuckcum'), Jump('proom19extfuckcumpin')) hovered tt.Action ("I'll cum inside your pussy") focus_mask True
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1255 ypos 316 action (Hide('proom19extfuckcum'), Jump('proom19extfuckcumpout')) hovered tt.Action ("I'll cum on your ass") focus_mask True

        frame:
            xalign .5
            text tt.value

label proom19extfuckcumassin:
    scene parentsroom 7pm 016cdg
    pov "Ahhh... yes...!"
    "You cum in her asshole."
    mom "Ahhh... so hot..."
    pov "Argh! Receive everything of my hot seed!"
    mom "Hah... hah..."
    scene parentsroom 7pm 020cdg
    pov "Oh yes, so much is inside you now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your hot ass milked my balls dry, mom!"
    else:
        pov "Your hot ass milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 021cdg
    "She fall exhausted on the bed."
    pov "That was a very good fuck, slut. All the way I like it."
    pov "We'll have much more fun together, me training you."
    if inc == True:
        pov "Until you'll become the perfect slut, mom."
    else:
        pov "Until you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'll go now, get yourself ready, maybe we'll have more fun in the basement later."
    mom "Yes, [pov]."
    scene black
    "You leave her."
    $ dtime += 1
    $ proom19fuckass = False
    jump parentsroom

label proom19extfuckcumassout:
    scene parentsroom 7pm 018cdg
    pov "Ahhh... yes...!"
    "You cum on her ass."
    mom "Ahhh... so hot..."
    pov "Argh! Receive everything of my hot seed!"
    mom "Hah... hah..."
    scene parentsroom 7pm 019cdg
    pov "Oh yes, so much is covering your ass now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your hot ass milked my balls dry, mom!"
    else:
        pov "Your hot ass milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 022cdg
    "She fall exhausted on the bed."
    pov "That was a very good fuck, slut. All the way I like it."
    pov "We'll have much more fun together, me training you."
    if inc == True:
        pov "Until you'll become the perfect slut, mom."
    else:
        pov "Until you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'll go now, get yourself ready, maybe we'll have more fun in the basement later."
    mom "Yes, [pov]."
    scene black
    "You leave her."
    $ dtime += 1
    $ proom19fuckass = False
    jump parentsroom

label proom19extfuckcumpin:
    scene parentsroom 7pm 016cdgp
    pov "Ahhh... yes...!"
    "You cum in her pussy."
    mom "Ahhh... so hot..."
    pov "Argh! Receive everything of my hot seed!"
    mom "Hah... hah..."
    scene parentsroom 7pm 020cdgp
    pov "Oh yes, so much is inside you now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your hot pussy milked my balls dry, mom!"
    else:
        pov "Your hot pussy milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 021cdgp
    "She fall exhausted on the bed."
    pov "That was a very good fuck, slut. All the way I like it."
    pov "We'll have much more fun together, me training you."
    if inc == True:
        pov "Until you'll become the perfect slut, mom."
    else:
        pov "Until you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'll go now, get yourself ready, maybe we'll have more fun in the basement later."
    mom "Yes, [pov]."
    scene black
    "You leave her."
    $ dtime += 1
    $ proom19fuckass = False
    jump parentsroom

label proom19extfuckcumpout:
    scene parentsroom 7pm 018cdgp
    pov "Ahhh... yes...!"
    "You cum on her ass."
    mom "Ahhh... so hot..."
    pov "Argh! Receive everything of my hot seed!"
    mom "Hah... hah..."
    scene parentsroom 7pm 019cdgp
    pov "Oh yes, so much is covering your ass now."
    mom "Hah... your sperm is so hot [pov]."
    if inc == True:
        pov "Your hot pussy milked my balls dry, mom!"
    else:
        pov "Your hot pussy milked my balls dry, [mother]!"
    mom "Hnng..."
    scene parentsroom 7pm 022cdgp
    "She fall exhausted on the bed."
    pov "That was a very good fuck, slut. All the way I like it."
    pov "We'll have much more fun together, me training you."
    if inc == True:
        pov "Until you'll become the perfect slut, mom."
    else:
        pov "Until you'll become the perfect slut, [mother]."
    mom "Hmm..."
    pov "I'll go now, get yourself ready, maybe we'll have more fun in the basement later."
    mom "Yes, [pov]."
    scene black
    "You leave her."
    $ dtime += 1
    $ proom19fuckass = False
    jump parentsroom

label proom19extlove:
    hide screen locations
    $ proom19first = True
    $ proom19lovesex = True
    scene main parents room door
    pov "{i}Huh? Why is the door closed?{/i}"
    "You hear someone talking behind the door."
    if inc == True:
        pov "{i}That are the voices of mom and dad.{/i}"
    else:
        pov "{i}That are the voices of [mother] and Bruce.{/i}"
    pov "{i}Let's see what's going on.{/i}"
    "You open the door."
    if nicolesweaterpantswear == True:
        scene parentsroom 7pm 002cl1
    elif nicolerobewear == True:
        scene parentsroom 7pm 002cl2
    else:
        scene parentsroom 7pm 002l
    pov "{i}What the hell is going on here?{/i}"
    dad "Come on, get your clothes off!"
    mom "I told you to leave me alone!"
    pov "What's going on here?"
    if nicolesweaterpantswear == True:
        scene parentsroom 7pm 003cl1
    elif nicolerobewear == True:
        scene parentsroom 7pm 003cl2
    else:
        scene parentsroom 7pm 003l
    mom "That idiot thought he can lay his hands on me."
    dad "She's thinking she need to deny me and play more of her little show for our cover."
    pov "Little show?"
    mom "He still don't get it. I don't want to get laid with him anymore."
    if nicolesweaterpantswear == True:
        scene parentsroom 7pm 004cl1
    elif nicolerobewear == True:
        scene parentsroom 7pm 004cl2
    else:
        scene parentsroom 7pm 004l
    dad "The little show she gave you in the basement to impress Davide."
    pov "{i}So he's thinking that was all a show and he can get back to normal when Davide is not around?{/i}"
    dad "Tell her [pov]. I have no idea what's gotten into her. She's thinking you're in love with her, sexually."
    dad "And she wants to be your slut."
    scene parentsroom 7pm 005c
    pov "Yes, this thing was just for the show."
    dad "Good, I knew it."
    pov "I'm not done."
    pov "She'll never be my slut, I love her too much for that."
    dad "So I was right."
    if inc == True:
        dad "You just love her as a son loves his mother."
    else:
        dad "You just love her and there's nothing sexually."
    pov "All is sexually. I'm her lover and I'm sure I'll be a much better husband for her."
    dad "But she's my wife!"
    pov "{i}It's time to tell him the truth. Poor, dumb Bruce...{/i}"
    pov "No, she isn't your wife anymore. She's mine now and I'm yours."
    scene parentsroom 7pm 006c
    dad "You can't be..."
    dad "You're serious. Are you mad? You can't just steal my wife!"
    pov "I already did it. And she already accepted me as her new man!"
    pov "And you'll be a good boy and play along, we won't Davide get suspicious, won't we?"
    dad "You're... evil..."
    if nicolesweaterpantswear == True:
        scene parentsroom 7pm 007cl1
    elif nicolerobewear == True:
        scene parentsroom 7pm 007cl2
    else:
        scene parentsroom 7pm 007l
    dad "We need to stop this now [mother]. He's gone mad."
    if inc == True:
        dad "He's your son and he wants to be your lover, getting intimate with you, more than needed for our cover."
    else:
        dad "He's your best friends son and he wants to be your lover, getting intimate with you, more than needed for our cover."
    dad "Say something! End this madness."
    mom "Stop talking!"
    if inc == True:
        mom "You won't talk like that about my son anymore!"
    else:
        mom "You won't talk like that about him anymore!"
    mom "I made my decision and you'll respect it, or I'll never forgive you!"
    dad "..."
    scene parentsroom 7pm 008
    dad "You're crazy! Both of you! This isn't normal!"
    dad "I'll leave for now, but this isn't over yet!"
    scene parentsroom 7pm 009l
    mom "So... he's gone now and it's just the two of us left."
    pov "{i}Wow, she got all naked in that time?{/i}"
    mom "How about we spend some time together as lovers?"
    pov "[ls] is in the kitchen at this time. Isn't that too risky?"
    mom "At this time I had fun with Bruce before. She'll think it's like all the times before."
    mom "Or you are afraid and want to leave me unsatisfied."
    if inc == True:
        pov "Hell no, mom. If you need me now, I'll fulfill my duty as your lover."
    else:
        pov "Hell no, [mother]. If you need me now, I'll fulfill my duty as your lover."
    mom "<giggle> You won't regret it."
    scene weekend 8pm 016lb
    mom "What are you waiting for?"
    "You undress in a few seconds."
    mom "<giggle>"
    jump nicoleweekendloveroot

label proom19extlovealexis:
    "Knock! Knock!"
    mom "Huh?"
    ls "Mom?"
    pov "<whisper>Damn, what is she doing here? I need to hide!"
    mom "<whisper>Don't worry. I'll send her away."
    scene parentsroom 7pm 015
    ls "Mom, you're naked?"
    mom "Yes... I'm naked."
    mom "What do you need, honey?"
    ls "I heard sounds like you having sex with someone, but Dad left the house before."
    mom "Oh... that was me."
    ls "You?"
    mom "I'm having some fun."
    ls "Fun...? What do you mean?"
    mom "Mommy was playing with herself..."
    ls "Playing...?"
    scene parentsroom 7pm 016
    ls "UGH! Don't tell me that mom!"
    mom "But..."
    ls "That's gross, telling me that, ugh!"
    scene parentsroom 7pm 017l
    mom "Now she'll bother us anymore."
    pov "Haha, she'll never get near this room anymore."
    mom "I need more of you now!"
    pov "Oh yes, you do, haha."
    $ alexissuspicous = 0
    $ alexisaway = True
    jump nicoleweekendloveroot

label proom19extloveend:
    scene weekend 8pm 046l
    pov "Let's rest a moment, before I need to leave you."
    mom "I'm so proud of you, [pov]."
    pov "I'm proud of you too."
    mom "And now we can really be together as lovers."
    if inc == True:
        pov "I'll be forever your lover, mom."
    else:
        pov "I'll be forever your lover, [mother]."
    $ proom19lovesex = False
    $ proom19extlovefirst = True
    $ dtime += 1
    jump parentsroom




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

    fixed:
        if baseorgymiddle == True:
            imagebutton auto "gui/icons/icon_left_%s.png" xpos 74 ypos 495 action (Hide ('baseorgyscreen'), Jump('baseorgyleft')) hovered tt.Action ("Turn left") focus_mask True
            imagebutton auto "gui/icons/icon_right_%s.png" xpos 1818 ypos 495 action (Hide ('baseorgyscreen'), Jump('baseorgyright')) hovered tt.Action ("Turn right") focus_mask True
        if baseorgyright == True:
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 956 ypos 380 action (Hide ('baseorgyscreen'), Jump('baseorgycas')) hovered tt.Action ("Go closer") focus_mask True
            imagebutton auto "gui/icons/icon_left_%s.png" xpos 74 ypos 495 action (Hide ('baseorgyscreen'), Jump('baseorgystart')) hovered tt.Action ("Turn left") focus_mask True
        if baseorgyleft == True:
            imagebutton auto "gui/icons/icon_right_%s.png" xpos 1818 ypos 495 action (Hide ('baseorgyscreen'), Jump('baseorgystart')) hovered tt.Action ("Turn right") focus_mask True
            imagebutton auto "gui/icons/icon_action_%s.png" xpos 806 ypos 250 action (Hide ('baseorgyscreen'), Jump('baseorgyaoa')) hovered tt.Action ("Go closer") focus_mask True


    frame:
        xalign .5
        text tt.value




label baseorgycas:
    scene basement 10pm 120a
    pov "{i}So, [ls] made a mess and Bruce can't take his eyes off her.{/i}"
    pov "{i}That damn pervert is staring on her ass.{/i}"
    pov "Hey, pervert!"
    scene basement 10pm 121a
    dad "Huh [pov]? Don't scare me like that."
    pov "Did I interrupt you at something, haha?"
    dad "What? No! I... what do you mean?"
    scene basement 10pm 122a
    if inc == True:
        pov "Enjoying my sister's ass?"
    else:
        pov "Enjoying [bs]'s ass?"
    dad "What...?"
    pov "But I can't blame you, while seeing her like that I could mount her instantly."
    dad "What are you talking about? I didn't..."
    pov "You can stop denying it. I know what I saw."
    dad "But..."
    pov "Slut!"
    scene basement 10pm 123a
    bs "Huh? Oh hi, [pov]."
    pov "That's a nice outfit you're wearing."
    bs "Thank you."
    if inc == True:
        pov "But crawling on the floor with that outfit give dad wrong ideas."
    else:
        pov "But crawling on the floor with that outfit give Bruce wrong ideas."
    bs "Huh?"
    dad "I told you..."
    pov "He can't take his eyes off you hot ass!"
    scene basement 10pm 124a
    if inc == True:
        bs "Dad!"
    else:
        bs "Bruce!"
    dad "Why are you doing this to me? Embarrassing me like that?"
    pov "So you think it's ok staring at MY slut like that?"
    dad "But I didn't..."
    if inc == True:
        pov "Oh, shut up, dad!"
    else:
        pov "Oh, shut up, Bruce!"
    scene basement 10pm 125a
    pov "Or did you do this on purpose, teasing him like that?"
    bs "N... No!"
    pov "You're allowed to tease him like you want to, but if you ever cheat on me, you'll be banned from the gang forever."
    bs "I won't do that [pov]."
    pov "You won't do it, because...?"
    bs "Be... because I'm your slut."
    pov "Yes, you are."
    pov "How about you show yourself off to us, we earned a show off your hot body."
    pov "Teasing us all the time."
    bs "Y... yes [pov]."
    scene basement 10pm 126a
    "You push the table away to make her some room."
    if inc == True:
        pov "Go on. Show me and dad what a hot slut you are!"
    else:
        pov "Go on. Show me and Bruce what a hot slut you are!"
    bs "Y... yes..."
    "She begin to dance slowly."
    pov "Isn't that nice, look at her hot body."
    scene basement 10pm 127a
    if inc == True:
        dad "You're mad, treat your own sister like that."
    else:
        dad "You're mad, treat her like that."
    pov "Oh you're trying to insult me? But don't worry, you're not worth that I'll go angry."
    pov "You can move your head, I know you want to see this too."
    dad "This went totally crazy. You better stop before you cross the last border."
    pov "Haha, you're jealous?"
    scene basement 10pm 128a
    pov "Look at her! She's made to please with that hot body."
    pov "She even made her tits bigger to get more attention."
    pov "She'll become the perfect slut and I'm sure she'll enjoy it."
    dad "..."
    pov "Haha, speechless? I knew it."
    scene basement 10pm 129a
    pov "A perfect round ass and you can even get a glimpse of her wet pussy."
    dad "S... stop it."
    pov "Oh I'm far away from being done."
    pov "Think about standing up right now and ram deep in her, giving her a dick, which she awaits all the day."
    bs "Hnng..."
    pov "{i}Damn, did she moan? Is she really getting this slutty?{/i}"
    pov "{i}Maybe it's time I have some fun with her hot body?{/i}"
    pov "Slut!"
    scene basement 10pm 130a
    bs "Yes?"
    pov "Your teasing pushed the right buttons, now it's time you please me with your hot body!"
    bs "R... right now?"
    pov "Yes! Here, right now!"
    scene basement 10pm 131a
    bs "Ok [pov], I'll please you."
    pov "{i}Oh, she doesn't seem to be so happy. Maybe the talking with Bruce confused her.{/i}"
    pov "You will come here and..."
    call screen baseorgycaschoose

screen baseorgycaschoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" xpos 748 ypos 316 action (Hide('baseorgycaschoose'), Jump('baseorgycasbj')) hovered tt.Action ("suck my dick") focus_mask True
        imagebutton auto "gui/icons/icon_sex_corruption_%s.png" xpos 1255 ypos 316 action (Hide('baseorgycaschoose'), Jump('baseorgycassex')) hovered tt.Action ("ride on my dick") focus_mask True

        frame:
            xalign .5
            text tt.value

label baseorgycasbj:
    scene basement 10pm 132a
    dad "You can't be serious!"
    dad "It's already wrong that you want to do this with her..."
    dad "but especially here, right now is the worst."
    pov "Wanna watch, haha?"
    pov "Or maybe a turn after me?"
    dad "Grrr..."
    scene basement 10pm 133a
    dad "I'll leave, I don't need to see this!"
    bs "Hnng..."
    dad "You're going down a path, where's no return."
    pov "Haha, maybe, but it'll be a journey of pleasure and fun."
    scene basement 10pm 134a
    bs "Did I really turned you on so much?"
    pov "{i}Oh, what's that? She's trying to be slutty. Is she so much craving for attention?{/i}"
    pov "{i}Or does she want to impress someone? Or does [miranda] as a stranger gave her some motivation to do a good job?{/i}"
    pov "{i}Any way, it's damn hot.{/i}"
    pov "Yes, you did a good choice for your clothing and a good show off."
    scene basement 10pm 135a
    bs "I'm glad you liked it."
    pov "What's with that motivation today? You're so eager to please me."
    bs "I... I'm not sure..."
    if inc == True:
        pov "Was it my praising you in front of dad? Explaining him why you're so a hot slut."
    else:
        pov "Was it my praising you in front of Bruce? Explaining him why you're so a hot slut."
    bs "Hnng..."
    pov "{i}Oh it seems I hit a nerve. Maybe she have some weird feelings for him...{/i}"
    pov "{i}or she just want to proof him how much \"worth\" she can be.{/i}"
    pov "Go on, don't stare at me, slut. My dick needs some attention."
    bs "Yes [pov]."
    scene basement 10pm 136a
    bs "<suck> <lick>"
    pov "Oh... yes..."
    pov "A good thing to start the night with a good blowjob from my slut."
    bs "<suck> <lick>"
    if inc == True:
        pov "But you need to improve even more and give your best, because your still in a competition with mom, my other slut."
    else:
        pov "But you need to improve even more and give your best, because your still in a competition with your mom, my other slut."
    scene basement 10pm 137a
    pov "But I'm sure you'll give your best."
    bs "<lick> Yes, [pov]. I'll be better than her."
    pov "Good. Then you can show it now, because she's watching us right now."
    bs "<lick> She's watching us while I'm licking your dick?"
    scene basement 10pm 161
    pov "Yes and she seems to be very jealous of you."
    bs "<lick> Hmm..."
    pov "And Bruce is still trying to argue, haha."
    pov "Ohhh... yes..."
    if casbjdt > 2:
        scene basement 10pm 138dt
    else:
        scene basement 10pm 138a
    bs "<suck> <suck>"
    if inc == True:
        pov "Show mom that you're a better slut than her!"
    else:
        pov "Show your mom that you're a better slut than her!"
    bs "<suck> Yessh..."
    pov "{i}That competition idea was very, very good. I'll have so much fun.{/i}"
    scene basement 10pm 162
    if inc == True:
        pov "And mom is so angry right now. I think she's blaming Bruce for it, haha."
    else:
        pov "And your mom is so angry right now. I think she's blaming Bruce for it, haha."
    bs "Hnng... <suck> <suck>"
    if casbjdt > 2:
        scene basement 10pm 138dt
    else:
        scene basement 10pm 138a
    pov "Oh shit, your blowjobs are getting much better, I'm so close."
    call screen baseorgycasbjchoose

screen baseorgycasbjchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 748 ypos 316 action (Hide('baseorgycasbjchoose'), Jump('baseorgycasbjin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1255 ypos 316 action (Hide('baseorgycasbjchoose'), Jump('baseorgycasbjout')) hovered tt.Action ("Cum on her face") focus_mask True

        frame:
            xalign .5
            text tt.value

label baseorgycasbjin:
    pov "You'll swallow my seed now."
    bs "Hmm..."
    pov "Oh yes, ARGHHH...!"
    if casbjdt > 2:
        scene basement 10pm 138dt
    else:
        scene basement 10pm 139ai
    bs "<gulp> <gulp>"
    pov "Yes, good slut!"
    scene basement 10pm 140ai
    bs "Aahh..."
    pov "Oh what a nice surprise. You want to be a good slut and show me some of my handiwork."
    bs "Yesh."
    pov "You can swallow the rest now."
    scene basement 10pm 141ai
    bs "<gulp>"
    bs "Hmm..."
    pov "Enjoy my taste."
    scene basement 10pm 142ai
    bs "Aahh..."
    pov "This'll give you some points for your competition."
    pov "Keep your good sucking or get even better and I'll be very pleased."
    bs "Yes [pov]."
    pov "{i}It's so good to praise them so they will give their best to please.{/i}"
    jump baseorgycasend

label baseorgycasbjout:
    pov "I need to cum on your face."
    bs "Hmm..."
    pov "Oh yes, ARGHHH...!"
    scene basement 10pm 139ao
    bs "Hmm..."
    pov "Yes, good slut!"
    scene basement 10pm 140ao
    bs "Aahh..."
    pov "Oh what a nice view. I marked my slut."
    bs "Yes."
    pov "And you even got some in your mouth so you can have a taste."
    bs "Hmm..."
    pov "This'll give you some points for your competition."
    pov "Keep your good sucking or get even better and I'll be very pleased."
    bs "Yes [pov]."
    pov "{i}It's so good to praise them so they will give their best to please.{/i}"
    jump baseorgycasend

label baseorgycassex:
    scene basement 10pm 132a
    dad "You can't be serious!"
    dad "It's already wrong that you want to do this with her..."
    dad "but especially here, right now is the worst."
    pov "Wanna watch, haha?"
    pov "Or maybe a turn after me?"
    dad "Grrr..."
    scene basement 10pm 133a
    dad "I'll leave, I don't need to see this!"
    bs "Hnng..."
    dad "You're going down a path, where's no return."
    pov "Haha, maybe, but it'll be a journey of pleasure and fun."
    scene basement 10pm 150
    pov "I'll help you to remove the patch so I can fuck you properly."
    bs "Hnng..."
    pov "{i}This'll be good.{/i}"
    scene basement 10pm 151
    pov "What's wrong? Are you afraid to have proper sex with me in front of the others?"
    bs "Hnng..."
    pov "You need to do it, and you know it. You wanted to join the gang and I choose you as my slut."
    pov "There'll be no other way then follow my orders, if you want to continue."
    bs "Hnng..."
    pov "Just sit on my lap and receive my dick inside you, then you'll forget your worries in no time."
    bs "..."
    pov "NOW SLUT!"
    scene basement 10pm 152
    pov "Good, stick it in yourself."
    bs "Hnng..."
    pov "{i}She just needed a push in the right direction. Now she's eager to please again.{/i}"
    if inc == True:
        pov "{i}Oh, mom noticed us. But as my slut she need to accept it.{/i}"
    else:
        pov "{i}Oh, [mother] noticed us. But as my slut she need to accept it.{/i}"
    pov "Your pussy is wet [bs]. No need to wait any longer for my dick."
    bs "Hmm..."
    scene basement 10pm 153
    bs "Aaahh..."
    pov "You take it all in at once. What a naughty slut you are."
    bs "Hnn... so big."
    pov "Good now start riding and let us enjoy a good fuck!"
    if inc == True:
        bs "Y... yes, brother."
    else:
        bs "Y... yes, [pov]."
    "She starts riding you."
    bs "Ahh... hah..."
    scene basement 10pm 154
    pov "See, you already forgot about your worries a few moments ago."
    bs "Yes, thanks to you [pov]."
    pov "Ride me faster!"
    bs "Yes..."
    "She's riding you faster."
    pov "Now that you're concentrating all on pleasing me I can tell you..."
    scene basement 10pm 161
    if inc == True:
        pov "that mom is watching us."
        bs "Mom?"
        pov "{i}Wow, she's tighten up in no time.{/i}"
    else:
        pov "that your mother is watching us."
        bs "My mom?"
        pov "{i}Wow, she's tighten up in no time.{/i}"
    pov "Yes and she seems to be very jealous of you."
    bs "Hah... hah..."
    pov "And Bruce is still trying to argue, haha."
    scene basement 10pm 155
    "You play with her tits."
    pov "Your tits like a rough handling?"
    bs "Yes.., it's feeling so good... [pov]!"
    if inc == True:
        pov "But you need to improve even more and give your best, because your still in a competition with mom, my other slut."
        pov "Show mom that you're a better slut than her!"
    else:
        pov "But you need to improve even more and give your best, because your still in a competition with your mom, my other slut."
        pov "Show your mom that you're a better slut than her!"
    bs "Hah, yes... I am... the best slut."
    scene basement 10pm 162
    if inc == True:
        pov "And mom is so angry right now. I think she's blaming Bruce for it, haha."
    else:
        pov "And your mom is so angry right now. I think she's blaming Bruce for it, haha."
    bs "Hah... AAAHH..."
    pov "You're getting close to orgasm?"
    scene basement 10pm 157
    bs "Yes... yes..."
    pov "Me too. Let's cum together slut! Receive your reward!"
    bs "Yes [pov]! I want to cum!"
    call screen baseorgycasfuckcum

screen baseorgycasfuckcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 316 action (Hide('baseorgycasfuckcum'), Jump('baseorgycasfuckcumin')) hovered tt.Action ("Cum in her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 516 action (Hide('baseorgycasfuckcum'), Jump('baseorgycasfuckcumout')) hovered tt.Action ("Cum on her belly") focus_mask True

        frame:
            xalign .5
            text tt.value

label baseorgycasfuckcumin:
    pov "I'll cum in your pussy!"
    bs "Yes, hah... Cum inside me..."
    if inc == True:
        pov "You want me to cum deep inside you, big sis?"
        bs "Yes, brother... I'm so close... hah..."
    else:
        pov "You want me to cum deep inside you, slut?"
        bs "Yes, [pov]... I'm so close... hah..."
    pov "Yes, receive my seed!"
    bs "AAHHH... HAAAAHHH...!"
    scene basement 10pm 156
    "She cums while you pump your sperm inside her."
    bs "Ahh... I can feel it... so hot..."
    pov "Oh yes..."
    "She stand up from your lap."
    scene basement 10pm 159i
    pov "Such a nice view!"
    pov "Don't clean up, I want to see everybody what I did to my slut!"
    bs "O... OK [pov]."
    pov "This'll give you some points for your competition."
    pov "Let's fuck more often and I'll be very pleased."
    bs "Yes [pov]."
    pov "{i}It's so good to praise them so they will give their best to please.{/i}"
    jump baseorgycasend

label baseorgycasfuckcumout:
    pov "I'll cum on your belly!"
    bs "Yes, hah... Cum over me..."
    if inc == True:
        pov "You want me to cum all over your body, big sis?"
        bs "Yes, brother... I'm so close... hah..."
    else:
        pov "You want me to cum all over your body, slut?"
        bs "Yes, [pov]... I'm so close... hah..."
    pov "Yes, receive my seed!"
    bs "AAHHH... HAAAAHHH...!"
    scene basement 10pm 158o
    "She cums while you spray your sperm over her."
    bs "Ahh... I can feel it... so hot..."
    pov "Oh yes..."
    "She stand up from your lap."
    scene basement 10pm 159o
    pov "Such a nice view!"
    pov "Don't clean up, I want to see everybody what I did to my slut!"
    bs "O... OK [pov]."
    pov "This'll give you some points for your competition."
    pov "Let's fuck more often and I'll be very pleased."
    bs "Yes [pov]."
    pov "{i}It's so good to praise them so they will give their best to please.{/i}"
    jump baseorgycasend

label baseorgycasend:
    pov "Recover slut, maybe I'll use you later again."
    bs "Yes... [pov]... hah..."
    pov "{i}Let's see what's Davide up to.{/i}"
    jump baseorgyaoa


label baseorgyaoa:
    scene black
    "You go over to Davide and [miranda]."
    scene basement 10pm 103a
    pov "Hey there..."
    davide "Oh, hey [pov]."
    miranda "Hello good looking boy..."
    pov "{i}Nice, she's flirting with me again.{/i}"
    davide "Treat him with respect slut. He's a gang member too."
    scene basement 10pm 104m
    miranda "Wow, that's great. Congratulations!"
    pov "Thank you."
    miranda "Now you're a special one too. And I love it to have fun with members of the gang."
    davide "Haha, she loves to be a slut."
    miranda "<giggle>"
    scene basement 10pm 105m
    pov "Oh and I see you're already getting in the mood."
    pov "{i}These hard nipples.{/i}"
    miranda "I can't await to show you what you missed before! You good looking stud!"
    mom "[miranda]!"
    scene basement 10pm 106m
    mom "What do you think you're doing?"
    mom "Get away from him!"
    scene basement 10pm 107m
    miranda "..."
    davide "Haha, [mother] gets angry again."
    if inc == True:
        davide "Protecting her son from the biggest slut."
    else:
        davide "Protecting you from the biggest slut."
    mom "Come here, you whore!"
    scene basement 10pm 108m
    mom "I'll beat your ass off when you lay a finger on him!"
    miranda "Haha, You can't be all the time around him. Sooner or later he'll taste me."
    mom "Grrr..."
    scene basement 10pm 110m
    davide "Don't look so shocked, haha."
    davide "They fight all the time, but never get violent."
    if inc == True:
        davide "Your mom hate her, something in the past must happen, but I don't know about it."
    else:
        davide "[mother] hate her, something in the past must happen, but I don't know about it."
    pov "So they fight all the time?"
    davide "Yes, I think it's very entertaining."
    pov "Entertaining?"
    scene basement 10pm 109m
    davide "Haha, yes."
    davide "We set up challenges for them, so they can play against each other and we can watch and enjoy."
    pov "Haha, but they never get too angry to fight physical?"
    davide "No, never. I think they're just bragging."
    davide "But when they're already in their fighting mood we'd let them play."
    pov "What games do you let them play?"
    davide "I'll show you one of my favorite, I call it \"Ass on Ass\"."
    pov "Haha, now I'm curious."
    davide "They'll get a double dildo in their pussy and then they have to try to get the other one off."
    pov "To get the other one to an orgasm."
    davide "Yes, and they need to do it in doggy style, that's why I call it \"Ass on Ass\"."
    pov "What's the prize?"
    scene basement 10pm 111m
    davide "These..."
    if momsecret == True:
        pov "But [mother] can't take them."
        davide "Yes, only [miranda] can win one."
    else:
        davide "But since [mother] can't have one, only [miranda] can win one."
        pov "[mother] can't use them?"
        davide "Yes, she'll get sick and puke it all out. Maybe she's allergic, I don't know."
        pov "Oh, I didn't know."
    pov "But how did she get the motivation to win then?"
    davide "Haha, she don't want [miranda] to win. Never!"
    pov "Ohh, so much hate..."
    davide "But they're equal or it would be boring. Sometimes [miranda]'s hunger is bigger."
    scene basement 10pm 112m
    pov "That's why you call her the biggest slut."
    davide "Haha, yes."
    davide "So let me show you the game."
    scene black
    "Davide set them up."
    scene basement 10pm 113m
    pov "What a nice view!"
    davide "Haha, like I told you."
    pov "And now we'll watch?"
    davide "Yes, but we need to choose our players. So the sluts can give their best to impress."
    pov "Oh this gets even better."
    if inc == True:
        davide "You'd side with your mother for this first time, because she's your slut."
    else:
        davide "You'd side with [mother] for this first time, because she's your slut."
    davide "I'll side with [miranda]."
    pov "Ok, I'm sure my slut will give her best!"
    mom "I'll [pov]."
    miranda "Haha, you'll lose."
    davide "Get ready."
    scene basement 10pm 114m
    mom "Hnng..."
    miranda "Hah..."
    pov "{i}Letting them get their steam out with games against each other. What an amazing idea. And so perverted.{/i}"
    scene basement 10pm 115m
    davide "You can sit on the other side, so you can cheer your slut better on."
    pov "You played this game very much often, haha?"
    davide "It's one of my favorites!"
    pov "Let's see."
    scene basement 10pm 116m
    pov "We have to win this!"
    mom "Yes, I'll give my best."
    pov "Not trying, you need to win. Davide must see that I choosed the right slut!"
    if inc == True:
        pov "That you're my right slut, mom!"
    else:
        pov "That you're my right slut, [mother]!"
    mom "Yes, I'll win for you [pov]!"
    davide "How about we start? GO!"
    scene basement 10pm 117m
    miranda "Huh? Haah...!"
    mom "Hnng!"
    davide "Oh [mother] start it aggressive. Pushing all in to surprise."
    davide "Don't disappoint me, slut!"
    miranda "I won't, hah..."
    "[miranda] starts to fuck back and it become a rhythm."
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
        pov "{i}And I stole dad's seat.{/i}"
    else:
        pov "{i}And I stole Bruce's seat.{/i}"
    call screen baseorgyaoawin

screen baseorgyaoawin():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 748 ypos 156 action NullAction() hovered tt.Action ("[mother] wins (coming soon)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 975 ypos 156 action NullAction() hovered tt.Action ("Both win/loose (coming soon)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1255 ypos 156 action (Hide('baseorgyaoawin'), Jump('baseorgyaoamirwin')) hovered tt.Action ("[miranda] wins") focus_mask True

        frame:
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
    "She cums hard."
    mom "I'm... so... sorry... hah... haaahh..."
    miranda "Yes! Hnng!"
    pov "{i}Damn, she lost against [miranda].{/i}"
    scene basement 10pm 122mm
    miranda "Hah, look at me, I did it. I finished that slut!"
    davide "Good job!"
    mom "Hnng... Hnn..."
    pov "{i}What a weird view.{/i}"
    scene basement 10pm 123mm
    miranda "Can I get my prize now? We all knew I'd win!"
    davide "Relax, slut. You'll have much fun with your prize soon."
    mom "I... I'm so sorry. Please forgive me [pov]."
    pov "Making me looking so weak before him. He knows now that I chosed the wrong slut."
    pov "{i}That'll push her motivation even more. Davide told me before that they're equal and both of them win or lose some times.{/i}"
    scene basement 10pm 124mm
    miranda "<giggle> Maybe you should take me next time [pov]."
    miranda "I can endure things, but I'm sure your big dick will let me cum in no time."
    pov "{i}Haha, she can't stop teasing.{/i}"
    mom "Hnng...!"
    if inc == True:
        pov "{i}And mom is so humiliated right now.{/i}"
    else:
        pov "{i}And [mother] is so humiliated right now.{/i}"
    pov "{i}I'd use this opportunity!{/i}"
    pov "You disappointed me, slut. Giving up this fast!"
    mom "I'm sorry [pov]. I can do better."
    scene basement 10pm 125mm
    pov "You not even disappointed me, but also your own daughter."
    pov "Seeing you get humiliated like this."
    mom "Hnng..."
    pov "{i}Haha, I think [bs] is more shocked in what she saw, then caring about losing or winning.{/i}"
    if inc == True:
        pov "{i}But this reaction of her is helping me with mom.{/i}"
    else:
        pov "{i}But this reaction of her is helping me with her mom.{/i}"
    scene basement 10pm 126mm
    mom "Please forgive me [pov], I'm so sorry."
    pov "..."
    mom "I'll give everything to be a better slut for you!"
    pov "This can't be forgiven so easily, maybe I should try it with [bs]."
    pov "Or maybe with [miranda]?"
    scene basement 10pm 129mm
    mom "No! You chosed me! I'll be better. I'll do everything as you say."
    pov "{i}What a nice reaction. Is she giving herself in to protect her daughter or does she hate [miranda] so much?{/i}"
    pov "{i}Or did she become a real slut, craving for my attention?{/i}"
    if inc == True:
        mom "I'm your mother, I raised you and know you all my life. I'm the best one to please you!"
    else:
        mom "I'm your mothers best friend, I saw you get raised and know you all my life. I'm the best one to please you!"
    pov "{i}All this eagerness, she's submitting herself entirely to me.{/i}"
    pov "{i}But will it be the right thing to do? Forgiving her or maybe punish her by choosing someone else to give her more motivation?{/i}"
    scene basement 10pm 127mm
    miranda "Hmm..."
    pov "{i}But [miranda] is also an interesting slut. Maybe I can make her mine too?{/i}"
    pov "{i}Now I can understand why Davide is so pleased with her.{/i}"
    scene basement 10pm 128mm
    miranda "I'm so horny right now. Victory feels so good."
    miranda "Hey [pov]! Do you want to have a real slut pleasing you?"
    pov "{i}Hmm... that body.{/i}"
    scene basement 10pm 129mm
    mom "Pleaseee [pov]..."
    pov "{i}Hmm... what to do now?{/i}"
    if inc == True:
        pov "{i}My mom is begging for my dick. She'll let me do everything.{/i}"
    else:
        pov "{i}[mother] is begging for my dick. She'll let me do everything.{/i}"
    pov "{i}And I could demand something for my forgiveness.{/i}"
    pov "{i}But [miranda] has such a nice body.{/i}"
    pov "{i}And what's with Davide? Should he also have some fun or will I risk a fight with the leader?{/i}"
    pov "{i}So much possibilites, haha.{/i}"
    call screen baseorgyaoaniclose

screen baseorgyaoaniclose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 316 action (Hide('baseorgyaoaniclose'), Jump('baseorgyaoaniclosedem')) hovered tt.Action ("Forgive her, but demand something") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 516 action (Hide('baseorgyaoaniclose'), Jump('baseorgyaoanicpunish')) hovered tt.Action ("Forgive her, but punish her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 716 action (Hide('baseorgyaoaniclose'), Jump('baseorgyaoamirfuck')) hovered tt.Action ("Have fun with [miranda]") focus_mask True


        frame:
            xalign .5
            text tt.value

label baseorgyaoaniclosedem:
    pov "I'll forgive you this time, but I want something in return."
    mom "Everything, I'll do everything."
    call screen baseorgyaoaniclosedemch

screen baseorgyaoaniclosedemch():
    default tt = Tooltip (" ")

    fixed:
        if nicoleonpill == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 316 action (Hide('baseorgyaoaniclosedemch'), Jump('baseorgyaoaniclosedempill')) hovered tt.Action ("You want a baby with her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 516 action NullAction() hovered tt.Action ("More choices soon...") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1455 ypos 716 action NullAction() hovered tt.Action ("Nothing for now (soon...)") focus_mask True

        frame:
            xalign .5
            text tt.value

label baseorgyaoaniclosedemno:
    pov "I'm not sure what I want, so I'll punish you only for your loss this time."
    mom "Thank you for forgiving me and yes, I need to be punished."
    jump baseorgyaoanicpunish

label baseorgyaoaniclosedempill:
    pov "I demand you stop taking the pill."
    scene basement 10pm 130mm
    mom "Stop taking the pill? But then..."
    pov "Yes, I'll impregnate you and we'll have a baby together."
    scene basement 10pm 131mm
    mom "What you are saying?"
    if inc == True:
        mom "You're my son and want to breed me."
    else:
        mom "You're my best friends son and want to breed me."
    pov "Yes!"
    pov "You want to be the best slut for me, so it's only natural that you breed my heir!"
    pov "Or did I made another mistake?"
    mom "Hnng..."
    pov "I won't wait any longer."
    scene basement 10pm 132mm
    mom "No wait. It's ok. I'll stop taking the pill and let you breed me."
    mom "Please [pov]... breed me!"
    if inc == True:
        pov "{i}Oh my god! My mom's begging me to breed her. This is heaven!{/i}"
    else:
        pov "{i}Oh my god! [mother]s begging me to breed her. This is heaven!{/i}"
    pov "Perfect, you accept my demand. Let's seal the deal with sex."
    pov "I want you to take the lead and show me, how much you love my seed inside you."
    mom "Y... yes [pov]."
    scene basement 10pm 128mm
    pov "I'll have fun with my slut now."
    if NTR == True and momrelationship < 5 or hardntr == True:
        jump baseorgyaoanicNTR
    miranda "And What is with me? I won the game."
    pov "{i}Can Davide have some fun too or not?{/i}"
    call screen baseorgyniclosedavide

screen baseorgyniclosedavide():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 648 ypos 256 action (Hide('baseorgyniclosedavide'), Jump('baseorgyniclosedavideyes')) hovered tt.Action ("He can have fun with [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 256 action (Hide('baseorgyniclosedavide'), Jump('baseorgyniclosedavideno')) hovered tt.Action ("I don't want him to touch her") focus_mask True

        frame:
            xalign .5
            text tt.value

label baseorgyniclosedavideyes:
    $ baseorgyaoaniclosedavy = True
    pov "You'll please Davide. I'm sure you'll have much fun!"
    miranda "But I want y... OK."
    davide "You'll enjoy your victory, haha."
    jump baseorgyaoaniclosedem2

label baseorgyniclosedavideno:
    pov "Do what you want, it's your victory."
    miranda "But I want you!"
    davide "Ouch, haha."
    pov "No! I need to punish my slut now."
    miranda "Oh..."
    miranda "I'll have some fun with the sybian then."
    davide "You getting yourself off with hard orgasms? I need to see this!"
    jump baseorgyaoaniclosedem2

label baseorgyaoaniclosedem2:
    scene black
    mom "Please lay on the table."
    "You lay on the table."
    scene basement 10pm 133mn
    pov "Oh you seem very motivated now."
    mom "Yes, I'll prove you that I'm better then [miranda]!"
    pov "Good slut! Then show me how much you're craving for my seed."
    mom "Yes [pov]."
    scene basement 10pm 134mn
    mom "Hnng... hah..."
    pov "Oh yes... all in."
    scene basement 10pm 135mn
    mom "Now you know I can do better."
    pov "{i}Damn, their rivality is so hot.{/i}"
    pov "Now ride me until we cum together while I spray my sperm inside you."
    mom "Yes [pov], give me your sperm!"
    "She starts riding you."
    scene basement 10pm 136mn
    mom "Hah... hah... your big dick..."
    pov "{i}Wow, she's doing a hot show. Mostly to fight with [miranda] again.{/i}"
    pov "{i}I won't complain. But I wonder if she's aware, that [bs] is still here?{/i}"
    pov "{i}Let's see how [miranda] celebrates her victory.{/i}"
    if baseorgyaoaniclosedavy == True:
        scene basement 10pm 134mdm
        pov "{i}Oh, the good old strap her in and punish her.{/i}"
        miranda "Oh yes, harder... ahh..."
    else:
        scene basement 10pm 133msyb
        miranda "Aaah... hah... so good..."
        pov "{i}So hot. Maybe I should fuck her some time too.{/i}"
        scene basement 10pm 134msyb
        miranda "Oh YES! YES! Aaahh"
        davide "Wow, already number two in that short time, haha."
    scene basement 10pm 137mn
    mom "Ohh... hah... ahhh..."
    pov "You want my sperm so badly?"
    mom "Yes, [pov]. Please cum inside me!"
    if inc == True:
        pov "I like it very much how you're begging for my seed, mom!"
    else:
        pov "I like it very much how you're begging for my seed, [mother]!"
    mom "Hah... hah..."
    pov "But I want you to let the others know too!"
    scene basement 10pm 137mnb
    mom "Huh? You want me to... tell them? Hah..."
    pov "Yes, I want you ride me harder and tell them that you're mine and I'm the only one allowed to breed you!"
    if inc == True:
        pov "Tell them how much you want to be my slut, mom!"
    else:
        pov "Tell them how much you want to be my slut, [mother]!"
    mom "But [bs] is still here!"
    pov "So you want to disappoint me again?"
    mom "No! I'll... do it for you [pov]!"
    "She began to ride you harder."
    scene basement 10pm 139mn
    mom "Hah... hah... Listen everyone...!"
    if inc == True:
        mom "I'm craving... hah... for my son's seed..."
    else:
        mom "I'm craving... hah... for [pov]'s seed..."
    mom "and I'll stop taking the pill... hah... hah..."
    mom "so he can... can breed me properly... hah... ahh..."
    pov "Good, now let's cum together, slut!"
    pov "{i}Let's see how the others react.{/i}"
    scene basement 10pm 141mn
    if inc == True:
        pov "{i}Oh, big sis is shocked. No wonder, mom told her that she wants a baby with me, haha.{/i}"
    else:
        pov "{i}Oh, [bs] is shocked. No wonder, her mom told her that she wants a baby with me, haha.{/i}"
    if baseorgyaoaniclosedavy == True:
        scene basement 10pm 140mnb
        miranda "Ohhh...."
        pov "{i}[miranda] is speechless. That'll make my slut happy, haha.{/i}"
        davide "Yes, go for it bro!"
    else:
        scene basement 10pm 140mn
        miranda "Ohhh...."
        pov "{i}[miranda] is speechless. That'll make my slut happy, haha.{/i}"
        davide "Yes, go for it bro!"
    pov "{i}Bruce is missing... Did he left again...?{/i}"
    scene basement 10pm 142mn
    mom "Hah... hah... I'm so close [pov]!"
    pov "Then cum with me!"
    mom "Yes, hah... AHHHH... I'm cumming [pov]!"
    pov "Me too, argh..."
    "You spray your sperm in her."
    scene basement 10pm 143mn
    mom "Your hot seed is inside me, hah..."
    pov "{i}What a beautiful view. And much better since she begged for it.{/i}"
    mom "Hah... hah... you're satisfied [pov]?"
    pov "Yes. For now..."
    $ nicoleonpill = False
    $ baseorgyaoaniclosedavy = False
    jump baseorgyend

label baseorgyaoanicpunish:
    scene basement 10pm 128mm
    pov "{i}Let's see what we'll do now.{/i}"

    call screen baseorgyniclosepunchoose

screen baseorgyniclosepunchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 648 ypos 316 action (Hide('baseorgyniclosepunchoose'), Jump('baseorgyniclosepunnicdavmir')) hovered tt.Action ("I'll punish my slut, you can have [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 955 ypos 316 action (Hide('baseorgyniclosepunchoose'), Jump('baseorgyaoamirchoose')) hovered tt.Action ("Let [miranda] choose") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 316 action NullAction() hovered tt.Action ("I'll punish my slut, [miranda] can choose herself (soon...)") focus_mask True

        frame:
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
    "You start to fuck them."
    pov "That's the way I like to punish her."
    davide "It's the best for them, so they can mess with each other again, haha."
    mom "Ahh... hah..."
    davide "How about a little challenge for us. Which slut will orgasm first?"
    pov "Haha, I'm in."
    miranda "Hah... hah... not so rough..."
    davide "Shut up, slut!"
    scene basement 10pm 134mdp
    mom "Hah... hah... you're so rough..."
    pov "Yes this is punishment slut! And you won't disappoint me again."
    mom "No, no, I won't. I'll cum hard and fast from your dick."
    pov "{i}Hmm... maybe I should spice it up a little, so my slut will come faster.{/i}"
    scene basement 10pm 134mcas
    pov "Bring me and Davide a drink, slut!"
    davide "Nice idea!"
    bs "Ok, [pov]."
    mom "No... hah... don't..."
    pov "Shut up!"
    scene basement 10pm 135mcas
    bs "Here is your drink [pov]."
    if inc == True:
        pov "Watch closely how I punish mom for disappointing me!"
    else:
        pov "Watch closely how I punish your mom for disappointing me!"
    bs "Y-Yes, I will."
    mom "Hnng! Hnng!"
    pov "You agree with me that she need a hard punishment?"
    bs "I... I do... [pov]!"
    pov "Good slut!"
    scene basement 10pm 136mcas
    bs "Here is your drink, Davide."
    miranda "Hah... hah..."
    davide "You can be lucky for having so good sluts!"
    pov "Oh yes, I am, haha."
    mom "AHHH... HAAHHH..."
    pov "You're close slut?"
    mom "Yes... hah..."
    scene basement 10pm 135mdp
    mom "AHHH... HAAAHHH..."
    miranda "Ohh... ohh..."
    pov "Haha, this time my slut won!"
    davide "Haha, you're right. But this slut will regret it..."
    miranda "Hah... yes, punish me more, hah... harder...!"
    mom "Hah... hah... [pov]..."
    jump baseorgyend

label baseorgyaoanicNTR:
    scene basement 10pm 128mmntr
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    davide "Oh... no, no, no!"
    davide "This is not how it works. I'll choose which slut you can have."
    pov "But..."
    davide "I'm still the boss here!"
    davide "And I'll punish your slut, hard and good. And you'll fulfill [miranda]'s wish."
    scene basement 10pm 132mm
    mom "No, not her."
    davide "Shut up slut!"
    mom "You need to stand up, do something..."
    pov "{i}Davide would beat me easily, damn...{/i}"
    if inc == True:
        pov "I can't, I'm sorry, mom."
    else:
        pov "I can't, I'm sorry, [mother]."
    davide "Shut up you too and let get the sluts ready."
    scene black
    "You two prepare the girls."
    mom "Hnng...hah..."
    miranda "Ohhh... ohhh..."
    scene basement 10pm 133mNTR
    "You start to fuck them."
    miranda "See, your little boy is fucking me now... hah..."
    mom "No... hah... ouch... Davide, not so rough..."
    davide "Shut the fuck up now."
    pov "{i}Damn, this isn't what I wanted.{/i}"
    "Davide fuck her harder."
    miranda "Yes, fuck me boy... I love your young dick."
    mom "Shut up... hah..."
    scene basement 10pm 134mNTR
    mom "AHH... HAH... HAH..."
    davide "Enjoy your punishment!"
    miranda "Thank you... so much... hah... for letting him fuck me, Davide."
    davide "These sluts are talking too much. I need a drink."
    scene basement 10pm 134mcas
    davide "Bring us some drinks, slut."
    bs "Y...yes Davide."
    scene basement 10pm 135mNTRcas
    bs "Here is your drink Davide."
    davide "Good slut. Maybe I'll ravage your hot body later too."
    mom "Hah... hah..."
    bs "Yes, you can have me later too, Davide."
    if inc == True:
        davide "Give your brother the other drink."
    else:
        davide "Give [pov] the other drink."
    scene basement 10pm 136mNTRcas
    bs "Here [pov]."
    pov "Thank you, slut."
    miranda "Harder, harder, hah..."
    bs "Do I have to let Davide have his fun with me later?"
    bs "Can't you do something?"
    pov "{i}I wish I could, seeing Davide fuck her too is bad, but...{/i}"
    pov "I'm sorry [bs], but I can't. He's the leader, he decide."
    bs "Hnng..."
    scene basement 10pm 135mNTR
    mom "HAAAHH... AAAHHH... YES!"
    if inc == True:
        davide "Enjoy the screaming when I let your mom cum, haha!"
    else:
        davide "Enjoy the screaming when I let [mother] cum, haha!"
    miranda "Oh yes, AAHHH, I'm cumming too. Harder, young stud!"
    pov "{i}That damn asshole, having fun with my slut and I didn't even cum.{/i}"
    scene black
    "The fun for Davide continues over night."
    scene basement 10pm 170NTR
    mom "Ahh... hah... hah..."
    scene basement 10pm 171NTR
    pov "{i}Damn, why do I have to lick her all night.{/i}"
    scene basement 10pm 172NTR
    davide "Look how hard I fuck her!"
    bs "AAHHH... HAAHH... please, not so rough..."
    scene black
    pov "{i}Finally, that damn night ended.{/i}"
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
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
    "A happy night in the basement ended."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    jump skip




label showerup7extcor:
    hide screen locations
    pov "{i}Damn I need a way to get in...{/i}"
    pov "{i}...{/i}"
    pov "{i}Hmm... maybe if I push it a little?{/i}"
    "Knock! Knock!"
    "You knock on the door."
    ls "I'm showering, go away."
    pov "Fast, open the door!"
    ls "But I'm..."
    "Knock! Knock"
    ls "Hmpf!"
    scene showerupstairs 7am shower up 002
    if inc == True:
        ls "What is it, brother?"
    else:
        ls "What is it, [pov]?"
    pov "{i}Wow, what a nice view.{/i}"
    pov "I need to use the shower, I'm in a hurry!"
    scene showerupstairs 7am shower up 003
    ls "Then wait until I'm done."
    pov "{i}Hmm...{/i}"
    pov "I can't..."
    scene showerupstairs 7am shower up 002
    ls "Why...?"
    pov "I got an interview for a job."
    if inc == True:
        pov "You know how much mom want me to get one."
    else:
        pov "You know how much your mom want me to get one."
    pov "{i}Good that I can build up this lie with her wish.{/i}"
    ls "Then use the shower downstairs?"
    pov "You know that shower isn't allowed for us."
    ls "Then I'll hurry and you can use it when I'm done!"
    pov "I have a better idea, I'll join you, wash me quick and then you can finishing your shower..."
    pov "and take all the time you need."
    ls "You can't be serious."
    pov "Time is running up...!"
    "You go further in the bathroom."
    if lilsiscorruption <= 39 and showbasealfirst == False:
        ls "No! Leave me alone!"
        pov "Huh?"
        ls "Leave now or I'll scream!"
        pov "{i}Oh shit, she isn't corrupted enough. I better leave fast.{/i}"
        scene black
        "You leave the bathroom and close the door."
        pov "{i}I'm sure when I corrupt her more she'll let me in next time.{/i}"
        jump showerup
    ls "But..."
    "She seemed to be overwhelmed from your boldness and just look at you."
    pov "Continue with your showering, I'll undress and join you."
    ls "But... I better leave..."
    pov "No! I insist you finish your shower. It's my fault that I'm in a hurry..."
    pov "and I don't want to bear the blame that you need to get smelly to school."
    ls "..."
    pov "{i}Good, that confused her totally.{/i}"
    pov "Now go..."
    scene showerupstairs 7am shower up 005c
    ls "Hnng..."
    pov "{i}Oh, that look. She's unsure if I'm telling the truth. But she don't want to set up a fight with me.{/i}"
    "You start to undress."
    scene showerupstairs 7am shower up 006c
    pov "{i}So cute, she's hiding from me shyly. I'm sure she knows exactly that we won't only wash when we're naked in there together.{/i}"
    pov "{i}And maybe she's interested too, so she can use my boldness as excuse.{/i}"
    scene showerupstairs 7am shower up 007c
    pov "{i}Her hot body. I'm so excited. Let's see how far I can go.{/i}"
    pov "{i}But I need to be careful that we don't get caught.{/i}"
    "You enter the shower naked."
    scene showerupstairs 7am shower up 008c
    pov "{i}Wow, is she looking at my dick or just prevent eye-contact?{/i}"
    pov "{i}Haha, that shy and innocent look.{/i}"
    scene showerupstairs 7am shower up 009c
    pov "{i}She's still trying to hide herself in that small shower.{/i}"
    scene showerupstairs 7am shower up 010c
    pov "{i}What a wonderful sight, her naked body all wet.{/i}"
    pov "{i}And my dick is waking up, waiting for the fun to start.{/i}"
    scene showerupstairs 7am shower up 011c
    pov "Don't be so shy, it makes me uncomfortable!"
    scene showerupstairs 7am shower up 013c
    ls "But..."
    pov "We're just showering together, there's nothing sexually about it!"
    pov "{i}Not yet...{/i}"
    ls "Hnng..."
    scene showerupstairs 7am shower up 012c
    pov "Or are you afraid I would try to rape you?"
    if inc == True:
        pov "My own little sister?"
    else:
        pov "A girl that I know all my life?"
    scene showerupstairs 7am shower up 013c
    ls "No... of course not... I didn't mean..."
    pov "{i}Now I have to push it, so she has not time to object further.{/i}"
    scene showerupstairs 7am shower up 014c
    pov "Good, then I'll start to wash your body first, so I won't waste your time too."
    "You start to grope her tits."
    ls "Hah...!"
    pov "{i}What a nice reaction.{/i}"
    pov "You need to get clean properly."
    ls "Hnng...!"
    scene showerupstairs 7am shower up 015c
    "Your get your hand lower."
    pov "So we can finish this faster."
    ls "Hah..."
    pov "{i}She's trying to resist, but her body is honest. So nice!{/i}"
    pov "You can wash me after then."
    scene showerupstairs 7am shower up 016c
    if inc == True:
        ls "Hah, stop... brother."
    else:
        ls "Hah, stop... [pov]."
    pov "No! You'll need to get clean everywhere while we're showering."
    pov "Open your legs, so I can wash you better."
    scene showerupstairs 7am shower up 017c
    ls "But, you're touching my... hah..."
    pov "As I said before, I just want to wash you, nothing sexually in that."
    ls "But..."
    pov "If you're so sensitive just try to calm down, It'll be over soon."
    ls "Hah... hah..."
    pov "{i}She's trying... but her body let her down, haha.{/i}"
    scene showerupstairs 7am shower up 018c
    pov "{i}Nice, she opened her legs obediently.{/i}"
    pov "{i}But did she do it to get all over with it fast or is she eager awaiting what's comes next?{/i}"
    pov "Good girl!"
    "You slide your finger between her lips and slowly enter her pussy."
    "She starts to tremble lightly."
    ls "Hnng...! Hah..."
    if lsispronanal >= 4:
        jump showerup7extcoranal
    if lsispronBDSM >= 4:
        jump showerup7extcorbdsm
    scene showerupstairs 7am shower up 019c
    "You rub faster on her pussy."
    ls "Hah... hah... hah..."
    pov "{i}Good, now she's honest. She's enjoying it very much.{/i}"
    if inc == True:
        pov "Lil sis, lok at me!"
    else:
        pov "[ls], look at me!"
    scene showerupstairs 7am shower up 020c
    if inc == True:
        ls "What is it? Hah... brother..."
    else:
        ls "What is it? Hah... [pov]..."
    pov "You need to look at me and tell me if I clean you properly, because I can't see where I wash you."
    ls "Huh? Tell you?"
    pov "Yes, is there a dirty spot?"
    "You move your finger to another spot on her pussy."
    ls "Hah... Hah... y... yes..."
    pov "{i}Good, so she need to overwhelm her shame looking and guiding me, when I get her off.{/i}"
    pov "Don't stop instructing me, so we can get done faster."
    scene showerupstairs 7am shower up 021c
    ls "Faster... y-yes... hah..."
    "You push your finger back in her pussy."
    ls "Yes... hah... there too..."
    "She starts to shaking."
    pov "{i}She's close. Now she'll cum from my \"washing\".{/i}"
    ls "Hah... hah..."
    scene showerupstairs 7am shower up 021ac
    ls "AAHHH... HNNG...!"
    pov "{i}She's cumming. So nice.{/i}"
    if inc == True:
        pov "So you're clean now down there, lil sis."
        ls "Yeshh... brother..."
    else:
        pov "So you're clean now down there,[ls]."
        ls "Yeshh... [pov]..."
    jump showerup7extcorhand

label showerup7extcorhand:
    "You stand back up and grab her hand."
    scene showerupstairs 7am shower up 022c
    pov "Now it's time you clean me."
    "You get her hand on your dick."
    ls "Huh?"
    "You start to rub your dick with her hand."
    pov "I cleaned you properly and now you'll clean me."
    scene showerupstairs 7am shower up 023c
    ls "O... OK. I'll... clean you too..."
    "She start to rub your dick on her own, but you still hold her hand to let her know that you're in control."
    scene showerupstairs 7am shower up 024c
    if inc == True:
        pov "Ohh... you're doing good, lil sis."
    else:
        pov "Ohh... you're doing good, [ls]."
    pov "But do it a little faster."
    ls "O... OK."
    "She rubs you a little faster."
    if lilsiscorruption >= 60:
        jump showerup7extcorbj
    else:
        jump showerup7extcorhand2

label showerup7extcorhand2:
    pov "{i}She's so damn cute and obedient, standing there and rubbing my dick. I'll reward her.{/i}"
    "You bend forward..."
    scene showerupstairs 7am shower up 025c
    "and give her a kiss."
    ls "Hnng...?"
    "You french kiss her when she opened her mouth in surprise."
    ls "Hnng...?"
    "Then you continue to rub your dick with her hand."
    scene showerupstairs 7am shower up 026c
    ls "Hmm..."
    "Her tongue starts to play with your tongue and she rubs your dick on her own again."
    if inc == True:
        pov "Hmm... you taste so good, lil sis."
    else:
        pov "Hmm... you taste so good, [ls]."
    "Your tongues are playing wilder with each other."
    pov "{i}She gave in, amazing. She's playing with her tongue on her own and giving me a handjob.{/i}"
    pov "{i}But it's so good I'm getting close. But I don't want to break the kiss, I'll just cum!{/i}"
    scene showerupstairs 7am shower up 027c
    pov "HNNG...! HMM...!"
    "You spray your sperm on her."
    ls "Hnng..."
    "You hold her arm and help her rubbing on you until your done cumming."
    scene showerupstairs 7am shower up 028c
    pov "{i}Wonderful. I came all over her belly.{/i}"
    pov "Oh, you're cleaning was wonderful!"
    ls "..."
    pov "All my dirty spunk came out of me."
    ls "Hnng..."
    scene showerupstairs 7am shower up 029c
    pov "I know this became sexual, but you're started it and I'm glad you invited me!"
    ls "Hnng..."
    pov "{i}No objection? She knows that I'm right. Her body betrayed her...{/i}"
    pov "Don't be sad. We both had our fun as adults."
    ls "Hmm..."
    pov "Unfortunately I made you dirty again, but you can clean this fast off yourself."
    pov "I need to go."
    ls "Hmm..."
    pov "{i}She's confused again. I let her better alone, thinking about the pleasure she got.{/i}"
    scene black
    "You dress up and leave the bathroom."
    $ showerup7amextfirstcor = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

label showerup7extcoranal:
    pov "Turn around!"
    ls "Y-yes..."
    "She turned around."
    scene showerupstairs 7am shower up 020cba
    pov "{i}Now I can see better what I'm doing.{/i}"
    "You start to grope her ass too."
    ls "Hah... hnng..."
    pov "{i}Let's have a little more fun with her, maybe showing her anal porn all the time pays off.{/i}"
    scene showerupstairs 7am shower up 021ca
    "You tease her asshole with your finger, while your other hand still playing with her pussy."
    ls "Hnng... Hnn..."
    pov "{i}Good, she'll get slowly off and I can push things further.{/i}"
    scene showerupstairs 7am shower up 022ca
    "You push your finger in her asshole."
    pov "{i}So tight, but the water is helping me sliding in easily.{/i}"
    scene showerupstairs 7am shower up 022cba
    ls "HAAH... your... finger..."
    pov "Is making you feel even better, I know."
    ls "Hnng..."
    "Her asshole tightens, but she don't try to push your finger out."
    scene showerupstairs 7am shower up 023ca
    "You slide deeper in her asshole."
    ls "Ohhh... hnng..."
    pov "Relax yourself and enjoy the feeling!"
    scene showerupstairs 7am shower up 021cba
    ls "Yeshh... hah..."
    pov "Good girl."
    "You rub her pussy faster."
    pov "{i}Time to reward her, while she was so obedient and letting me explore her more.{/i}"
    ls "Hah... hah..."
    "Then you push your finger out and back in off her asshole too."
    scene showerupstairs 7am shower up 023cba
    ls "AAAHHHH.... HAAAHHH...!"
    "Her ass tighten and she cums hard."
    ls "Hnng... ahh... hah... hah..."
    pov "{i}Nice, she came while I played with her asshole too.{/i}"
    if inc == True:
        pov "So you're clean now down there, lil sis."
        ls "Yeshh... brother..."
    else:
        pov "So you're clean now down there,[ls]."
        ls "Yeshh... [pov]..."
    jump showerup7extcorhand

label showerup7extcorbdsm:
    pov "Turn around!"
    ls "Y-yes..."
    "She turned around."
    scene showerupstairs 7am shower up 020cba
    pov "{i}Now I can see better what I'm doing.{/i}"
    "You start to grope her ass too."
    ls "Hah... hnng..."
    pov "{i}Let's have a little more fun with her, maybe showing her BDSM porn all the time pays off.{/i}"
    scene showerupstairs 7am shower up 021cb
    "You hold your hand up to give her a slap on her ass."
    pov "{i}Let's see how she likes it.{/i}"
    pov "<slap>"
    with vpunch
    scene showerupstairs 7am shower up 022cba
    ls "HAAHH..."
    "She shakes lightly, but doesn't move."
    pov "{i}Nice, let's try some more.{/i}"
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    scene showerupstairs 7am shower up 022cb
    pov "{i}Her ass is getting red, nice view.{/i}"
    ls "Hah... hah..."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    pov "You're a bad girl, aren't you?"
    scene showerupstairs 7am shower up 021cba
    ls "Yeshh... hah... I'm a bad girl..."
    pov "So you need more punishment?"
    ls "Yeshh... hnn... please... [pov]."
    pov "Hmm... that isn't the right thing you need to say."
    ls "..."
    pov "{i}She's thinking about the BDSM porn, I'm sure.{/i}"
    ls "I need more punishment, please master. Hnng..."
    pov "Good girl, you learn fast."
    scene showerupstairs 7am shower up 023cb
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    pov "{i}This is so hot! She's getting in to it and getting close to an orgasm, I can feel it.{/i}"
    "You give a few more slaps."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    pov "<slap>"
    with vpunch
    ls "AAHH... hah... hah..."
    "She's shaken wildly."
    scene showerupstairs 7am shower up 023cba
    ls "AAAHHHH.... HAAAHHH...!"
    "She cums hard."
    ls "Hnng... ahh... hah... hah..."
    pov "{i}Nice, she came while I spanked her ass.{/i}"
    if inc == True:
        pov "So you're clean now down there, lil sis."
        ls "Yeshh... master..."
    else:
        pov "So you're clean now down there,[ls]."
        ls "Yeshh... master..."
    jump showerup7extcorhand

label showerup7extcorbj:
    call screen showerup7extcorchoose

screen showerup7extcorchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_handjob_corruption_%s.png" xpos 648 ypos 316 action (Hide('showerup7extcorchoose'), Jump('showerup7extcorhand')) hovered tt.Action ("I want her to continue [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_handjob_corruption_%s.png" xpos 848 ypos 316 action (Hide('showerup7extcorchoose'), Jump('showerup7extcorbj2')) hovered tt.Action ("I want her to get down on her knees [cr1]") focus_mask True

        frame:
            xalign .5
            text tt.value


label showerup7extcorbj2:
    pov "{i}She's so damn cute and obedient, standing there and rubbing my dick. But I want more!{/i}"
    scene showerupstairs 7am shower up 030c
    "You lay your arm around her shoulder."
    pov "I know a way you can clean me much faster."
    "You press her down."
    ls "Hnng..."
    pov "{i}Hmm... I think she knows what I'm up to.{/i}"
    scene showerupstairs 7am shower up 031c
    ls "Hnng..."
    pov "You can see it better and get the cleaning faster done!"
    "She stares at your dick, but don't move."
    pov "{i}She struggles with herself. I better help her.{/i}"
    scene showerupstairs 7am shower up 032c
    "You move her hand onto your dick."
    pov "Continue to rub it clean and we're done in no time!"
    ls "Hnng..."
    pov "{i}It's time to push her further.{/i}"
    scene showerupstairs 7am shower up 033c
    pov "You started to make our cleaning sexual, by letting out so sexy moans while I washed you."
    pov "Now take responsibility and get this done."
    if inc == True:
        pov "I won't be able to leave the shower, after you turned me so on, lil sis."
    else:
        pov "I won't be able to leave the shower, after you turned me so on, [ls]."
    pov "You need to help me now!"
    ls "Hnn..."
    scene showerupstairs 7am shower up 034c
    ls "<kiss> Hmm..."
    pov "Ohh, yes..."
    pov "{i}Damn, that's a nice surprise. I hoped for a continuing of the handjob, but this is even better.{/i}"
    "She put more kisses on your dick."
    ls "<kiss> <kiss>"
    if inc == True:
        pov "Yes, you're helping me very good, lil sis."
    else:
        pov "Yes, you're helping me very good, [ls]."
    pov "I'm so proud of you."
    scene showerupstairs 7am shower up 035c
    if inc == True:
        ls "<lick> Thank you... brother..."
    else:
        ls "<lick> Thank you... [pov]..."
    pov "{i}She's eager to help me now. Maybe she feels guilty for being the only one, who had fun until now.{/i}"
    pov "{i}Feeling her improvise is so good, I'm so close. But I want to feel her sexy mouth too, before I relieve myself.{/i}"
    scene showerupstairs 7am shower up 036c
    "You push your dick in her mouth."
    pov "Yes... this is so good [ls]!"
    ls "Hnng...!"
    pov "{i}So obedient! She's surprised but don't fight back and just hold my dick in her mouth.{/i}"
    pov "Your sexy mouth is so good, I need to cum now!"
    call screen showerup7extcorbjcum

screen showerup7extcorbjcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 448 ypos 316 action (Hide('showerup7extcorbjcum'), Jump('showerup7extcorbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 316 action (Hide('showerup7extcorbjcum'), Jump('showerup7extcorbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True

        frame:
            xalign .5
            text tt.value

label showerup7extcorbjcumin:
    pov "{i}I want her to taste my spunk!{/i}"
    pov "{i}So it's better I don't tell her to make sure she'll swallow it.{/i}"
    "You hold her head tighter, so she can't move away."
    scene showerupstairs 7am shower up 037ci
    pov "HNNG...!"
    ls "Hnn..."
    "You spray your sperm in her mouth."
    pov "Oh yes, so good."
    pov "{i}She tried to move back, but now she just holds still. So she was just surprised.{/i}"
    ls "Hnn... <gulp> <gulp>"
    pov "Good girl. Drink it all down."
    scene showerupstairs 7am shower up 038ci
    "You let go of her head."
    ls "Hnng..."
    if inc == True:
        pov "You did very good, not to struggle when I came, lil sis."
    else:
        pov "You did very good, not to struggle when I came, [ls]."
    pov "I needed to do that, I wanted to let you taste my sperm."
    pov "You understand that?"
    ls "Hnng... y-yes..."
    pov "{i}So obedient, nice.{/i}"
    pov "And do you like my taste?"
    ls "Hnn..."
    pov "{i}She's getting confused again. Trapped in her thoughts. Well, she'll get used to my taste.{/i}"
    pov "Don't be sad. We both had our fun as adults."
    ls "Hmm..."
    scene black
    "You dress up and leave the bathroom."
    $ showerup7amextfirstcor = True
    $ showerup7amextfirstcor2 = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

label showerup7extcorbjcumout:
    pov "{i}I want to cum on her face!{/i}"
    pov "{i}So it's better I don't tell her to make sure she won't move.{/i}"
    scene showerupstairs 7am shower up 037co
    pov "HNNG...!"
    ls "Hnn..."
    "You spray your on her face."
    pov "Oh yes, so good."
    pov "{i}She moved back, but not far enough. So she was surprised.{/i}"
    scene showerupstairs 7am shower up 038co
    ls "Hnng..."
    if inc == True:
        pov "You did very good, catched all with your face when I came, lil sis."
    else:
        pov "You did very good, catched all with your face when I came, [ls]."
    pov "I needed to do that, I wanted to mark you with my sperm."
    pov "You understand that?"
    ls "Hnng... y-yes..."
    pov "{i}So obedient, nice.{/i}"
    pov "And do you like my sperm on your skin?"
    ls "Hnn..."
    pov "{i}She's getting confused again. Trapped in her thoughts. Well, she'll get used to my taste.{/i}"
    pov "Don't be sad. We both had our fun as adults."
    ls "Hmm..."
    scene black
    "You dress up and leave the bathroom."
    $ showerup7amextfirstcor = True
    $ showerup7amextfirstcor2 = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup


label showerup7extlove:
    hide screen locations
    pov "{i}Damn I need a way to get in...{/i}"
    pov "{i}...{/i}"
    pov "{i}Hmm... maybe if I push it a little?{/i}"
    "Knock! Knock!"
    "You knock on the door."
    ls "I'm showering, go away."
    pov "Fast, open the door!"
    ls "But I'm..."
    "Knock! Knock"
    ls "Hmpf!"
    scene showerupstairs 7am shower up 002
    if inc == True:
        ls "What is it, brother?"
    else:
        ls "What is it, [pov]?"
    pov "{i}Wow, what a nice view.{/i}"
    pov "I need to use the shower, I'm in a hurry!"
    scene showerupstairs 7am shower up 003
    pov "{i}What a nice view. So innocent...{/i}"
    pov "..."
    ls "[pov]? [pov]!"
    pov "Huh?"
    scene showerupstairs 7am shower up 004l
    ls "You can come in, dummy."
    pov "You let me in?"
    ls "Yes, you want to share the shower with me? We can do this."
    pov "{i}Oh, this went better then expected. So she opens more and more to me, nice.{/i}"
    scene showerupstairs 7am shower up 005l
    ls "<giggle> Are you dreaming?"
    pov "Oh... I just..."
    ls "When you're in a hurry, you shouldn't let me wait... <giggle>"
    pov "{i}Is she teasing me?{/i}"
    if inc == True:
        pov "{i}My little sister is all naked and want to share the shower with me.{/i}"
    else:
        pov "{i}[ls] is all naked and want to share the shower with me.{/i}"
    pov "{i}I hope this isn't a dream an I wake up.{/i}"
    scene showerupstairs 7am shower up 006l
    pov "{i}Our visit at the basement together must have boost her confidence.{/i}"
    pov "{i}She don't even hide her body right now.{/i}"
    scene showerupstairs 7am shower up 007l
    pov "{i}Unbelieveable. So she really starts to see me as her lover now, doing everything together.{/i}"
    pov "{i}And I love it, especially her teasing. From innocent and prude to open and adventurous.{/i}"
    scene showerupstairs 7am shower up 008l
    ls "What's up [pov]? You're still dressed? <giggle>"
    pov "I..."
    if inc == True:
        ls "Or do you just want to see your little sister showering? <giggle>"
    else:
        ls "Or do you just want to see me showering? <giggle>"
    pov "No... I'll join you."
    pov "{i}Enough watching, I need to be close to her now!{/i}"
    scene showerupstairs 7am shower up 009l
    ls "Undress yourself and join me. Or are you afraid of me, dummy?"
    pov "{i}So damn cute. And also damn sexy.{/i}"
    "You undress yourself and enter the shower."
    scene showerupstairs 7am shower up 011l
    if inc == True:
        ls "Now you finally joined me, brother."
        pov "{i}Yes, finally I'm naked with my little sister in the shower.{/i}"
    else:
        ls "Now you finally joined me, [pov]."
        pov "{i}Yes, finally I'm naked with [ls] in the shower.{/i}"
    ls "<giggle> Lost your words?"
    pov "Well, being together with such a beautiful girl."
    ls "Ohh, [pov]. Kiss me!"
    scene showerupstairs 7am shower up 012l
    "She kiss you."
    ls "<kiss>"
    pov "{i}What a promising start...{/i}"
    pov "<kiss>"
    scene showerupstairs 7am shower up 010l
    "She starts to rub over your chest."
    pov "Oh, that's feeling so good."
    ls "I can see that <giggle>."
    pov "{i}Oh, I have already a boner. But her wet body is so hot.{/i}"
    pov "So you don't mind?"
    scene showerupstairs 7am shower up 013l
    ls "<giggle> Of course not."
    ls "I wonder more if I'll get you cleaned?"
    pov "What why?"
    ls "You're so full of dirty thoughts, my naughty dummy. <giggle>"
    pov "Haha, you got me."
    scene showerupstairs 7am shower up 014l
    ls "So maybe I need to modify my cleaning this time..."
    "Her hand moves lower."
    pov "I'm sure you'll choose the right solution..."
    pov "{i}She's so straight forward, like we're already lovers. Just amazing!{/i}"
    scene showerupstairs 7am shower up 015l
    pov "Ohh..."
    ls "Let me clean you here now. <giggle>"
    pov "{i}Her hands are so soft, I can't wait to do her more.{/i}"
    ls "It's so hard and hot. No wonder you need to get clean fast."
    pov "And I'm happy that you're helping me."
    ls "You're welcome. <giggle>"
    if showerup7amextfirstlove == True:
        jump showerup7extlovehump
    scene showerupstairs 7am shower up 016l
    ls "Hello there, little dummy."
    pov "{i}That's so cute and make me incredible horny.{/i}"
    ls "You missed me? <giggle>"
    if inc == True:
        pov "You have no idea, lil sis."
    else:
        pov "You have no idea, [ls]."
    scene showerupstairs 7am shower up 017l
    "She starts to rub your dick."
    ls "This will help you to get clean in no time!"
    pov "Oh yes..."
    pov "{i}Her soft hand rubbing on my dick and that naughty look...{/i}"
    ls "It's good you came to me to get you clean."
    pov "Talking about \"come\"... oh shit!"
    pov "{i}That pulled the trigger, I can't hold it any longer!{/i}"
    pov "I'm cumming, [ls]!"
    ls "Then just let your dirty thoughts out <giggle>"
    call screen showerup7extlovecum

screen showerup7extlovecum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 448 ypos 316 action (Hide('showerup7extlovecum'), Jump('showerup7extlovecumf')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1455 ypos 316 action (Hide('showerup7extlovecum'), Jump('showerup7extlovecumt')) hovered tt.Action ("Cum on her tits") focus_mask True

        frame:
            xalign .5
            text tt.value

label showerup7extlovecumf:
    scene showerupstairs 7am shower up 018lfo
    pov "AHHH... HNNG...!"
    "You cum on her face."
    ls "Hmm..."
    pov "{i}Damn, even while I'm cumming on her face she's so cute.{/i}"
    scene showerupstairs 7am shower up 019lfo
    ls "Now I've all your dirty thoughts. <giggle>"
    pov "So you're happy you got them?"
    ls "More, that I could help you with your problem."
    if inc == True:
        pov "You're amazing, lil sis. I love it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, big brother."
    else:
        pov "You're amazing. I love it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, [pov]."
    ls "I need to wash myself now to get ready for school."
    pov "Yes, and I need to realize now that this wasn't a dream, haha."
    ls "You can dream of me too and feel free to let me clean you more often. <giggle>"
    pov "{i}Oh... my god...{/i}"
    scene black
    "You dress yourself and leave the bathroom."
    $ showerup7amextfirstlove = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup

label showerup7extlovecumt:
    scene showerupstairs 7am shower up 018lto
    pov "AHHH... HNNG...!"
    "You cum on her tits."
    ls "Hmm... so much..."
    scene showerupstairs 7am shower up 019lto
    ls "Now I've all your dirty thoughts. <giggle>"
    pov "So you're happy you got them?"
    ls "More, that I could help you with your problem."
    if inc == True:
        pov "You're amazing, lil sis. I love it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, big brother."
    else:
        pov "You're amazing. I love it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, [pov]."
    ls "I need to wash myself now to get ready for school."
    pov "Yes, and I need to realize now that this wasn't a dream, haha."
    ls "You can dream of me too and feel free to let me clean you more often. <giggle>"
    pov "{i}Oh... my god...{/i}"
    scene black
    "You dress yourself and leave the bathroom."
    $ showerup7amextfirstlove = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup


label showerup7extlovehump:
    ls "This time I'll try something new to clean you."
    pov "Something new?"
    ls "Yes, I'll show you."
    scene showerupstairs 7am shower up 020l
    pov "{i}Her hot little ass!{/i}"
    pov "So what are you up to?"
    ls "Oh you'll like it, but you have to promise to let me retain control."
    pov "Sure, what ever you want."
    pov "{i}Is she going to fuck me?{/i}"
    scene showerupstairs 7am shower up 021l
    "She's holding her ass up so your dick is laying on it."
    pov "This is getting me excited, I'm eager to see what you'll do next."
    ls "You'll like it. <giggle>"
    scene showerupstairs 7am shower up 023l
    "She moves her ass slowly back towards you."
    pov "{i}Her ass rubbing on my dick feels really nice.{/i}"
    scene showerupstairs 7am shower up 024l
    pov "{i}Damn, I could fuck her right now!{/i}"
    ls "Hmm... "
    pov "Your ass feels so good."
    scene showerupstairs 7am shower up 022l
    ls "And I didn't even started yet. <giggle>"
    if inc == True:
        pov "Then stop teasing me, lil sis."
    else:
        pov "Then stop teasing me, [ls]."
    ls "OK. <giggle>"
    scene showerupstairs 7am shower up 025l
    "She rubs your dick further with her asschecks and it slips between her ass cheeks."
    pov "Ohh... this feels so good."
    ls "<giggle>"
    pov "{i}What a hot view. And I'm so near her pussy.{/i}"
    scene showerupstairs 7am shower up 026l
    ls "Hnng..."
    pov "{i}What's with her? Is she getting horny too?{/i}"
    pov "Are you getting naughty thoughts too?"
    ls "Hnng..."
    if inc == True:
        pov "Relax, lil sis. You can have fun at cleaning me too."
    else:
        pov "Relax, [ls]. You can have fun at cleaning me too."
    pov "{i}Is she afraid that I could take advantage of the situation?{/i}"
    pov "You can enjoy it too, we'll do it your way, I won't force you to anything!"
    scene showerupstairs 7am shower up 022l
    ls "<giggle> Yes, you're right! I was afraid a moment."
    if inc == True:
        ls "Forgive me, brother."
    else:
        ls "Forgive me, [pov]."
    pov "There's nothing to forgive, everything is fine."
    ls "Then enjoy this. <giggle>"
    scene showerupstairs 7am shower up 027l
    "She starts to rub you faster."
    pov "Hmm..."
    pov "{i}I'm not sure it's just the water or she's getting wet. She's already trembling lightly.{/i}"
    scene showerupstairs 7am shower up 028l
    ls "Hah... Hmm..."
    pov "{i}Oh, she's getting excited!{/i}"
    pov "{i}And she's rubbing me now with her pussy.{/i}"
    pov "Yes... more..."
    scene showerupstairs 7am shower up 029l
    ls "Hah... hah... hah..."
    pov "So you're enjoying your cleaning method too?"
    ls "Yes... hah... your big dick..."
    pov "Then I'm glad you can have fun too."
    ls "Hah... yes, I do... hah..."
    scene showerupstairs 7am shower up 030l
    "She starts to rub furiously on your dick."
    if inc == True:
        ls "Hah... hah... big brother!"
    else:
        ls "Hah... hah... [pov]!"
    "Her body shakes and trembles."
    pov "{i}So hot! She's getting herself off on my dick.{/i}"
    ls "Ohh... ooh... OOHHH!"
    pov "You're getting an orgasm?"
    ls "Yes... yes, [pov]! AAAAHHHH!"
    pov "This is to much! I'm cumming too!"
    scene showerupstairs 7am shower up 031l
    pov "AHHH... HNNG...!"
    "You cum all over her ass."
    ls "Hmm..."
    scene showerupstairs 7am shower up 032l
    pov "Oh, oh... that was so good."
    ls "I can feel your dirty thoughts on my ass. <giggle>"
    pov "Yes I loved your cleaning method very much."
    pov "And even more that you had your fun too."
    ls "Yes, it felt really good."
    scene showerupstairs 7am shower up 033l
    if inc == True:
        pov "You're amazing, lil sis. I love it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, big brother."
    else:
        pov "You're amazing. I love it."
        ls "And me?"
        pov "I love you too, [ls]."
        ls "And I love you more, [pov]."
    ls "I need to wash myself now to get ready for school."
    pov "Yes, and I need to realize now that this wasn't a dream, haha."
    ls "You can dream of me too and feel free to let me clean you more often. <giggle>"
    pov "{i}Oh... my god...{/i}"
    scene black
    "You dress yourself and leave the bathroom."
    $ showerup7amextfirstlove2 = True
    $ showerup7amextyes = True
    $ dtime += 1
    jump showerup