

label droom7momcorrepeat:
    scene diningroom 7am 014a
    mom "..."
    pov "Good girl!"
    mom "Hnn..."
    pov "I love to look at your big boobs!"
    mom "Please..."
    pov "Ssshh..."
    "You stare some time longer at her boobs."
    jump droom7momtalk2

label droom7momloverepeat:
    mom "Oh you want to hold my hand again?"
    pov "Yes it's a good way to start the morning."
    scene diningroom 7am 009
    mom "Oh that's so sweet [pov]."
    if inc == True:
        pov "You're welcome, mom."
    else:
        pov "You're welcome [mother]."
    "You silently look at each other."
    jump droom7momtalk2


label lroom8momfondle:
    hide screen locations
    $ momcorruption += 1
    scene livingroom 8am 012
    pov "{i}I need to fondle that ass!{/i}"
    mom "Huh?"
    "You knead her ass-cheek."
    scene livingroom 8am 013
    mom "Please stop. That's going to far."
    pov "No, I need to fondle your hot ass."
    pov "It's also your fault for showing it that way."
    scene livingroom 8am 014
    mom "Hnn..."
    "She lets you fondle her ass for some time."
    $ lroom8fondlefirst = True
    jump lroom8momtalk3


label bsis142look:
    hide screen locations
    scene bigsisroom 2pm 002
    pov "{i}Oh, they're fighting again. Better leave.{/i}"
    $ bigsisrelationship += 1
    $ dtime += 1
    jump bsisroom


label kitchen11repeat:
    pov "Urg! Not again!"
    if momcorruption > momlove:
        if nicolereddresswear == True:
            scene kitchen 11am 011ancc1
        elif nicolebabydollwear == True:
            scene kitchen 11am 011ancc2
        elif nicolesweaterpantswear == True:
            scene kitchen 11am 011ancl1
        elif nicolerobewear == True:
            scene kitchen 11am 011ancl2
        else:
            scene kitchen 11am 011a
        mom "I'm sorry."
    else:
        if nicolereddresswear == True:
            scene kitchen 11am 011bncc1
        elif nicolebabydollwear == True:
            scene kitchen 11am 011bncc2
        elif nicolesweaterpantswear == True:
            scene kitchen 11am 011bncl1
        elif nicolerobewear == True:
            scene kitchen 11am 011bncl2
        else:
            scene kitchen 11am 011b
        mom "Oh come on. It isn't that bad."
    pov "{i}This has to change...{/i}"
    call screen k11h2

screen k11h2():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 992 ypos 146 action (Hide('k11h2'), Jump('kitchen11momhelprepeat')) hovered tt.Action ("Help her with the dinner[lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1028 ypos 306 action (Hide('k11h2'), Jump('kitchen11momnohelprepeat')) hovered tt.Action ("Don't help her [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label kitchen11momhelprepeat:
    $ momlove += 1
    pov "I'll help you again with the dinner."
    if nicolereddresswear == True:
        scene kitchen 11am 007ancc1
    elif nicolebabydollwear == True:
        scene kitchen 11am 007ancc2
    elif nicolesweaterpantswear == True:
        scene kitchen 11am 007ancl1
    elif nicolerobewear == True:
        scene kitchen 11am 007ancl2
    else:
        scene kitchen 11am 007a
    mom "Thank you so much!"
    pov "You're welcome."
    "You help her."
    $ dtime += 1
    jump kitchen

label kitchen11momnohelprepeat:
    $ momcorruption += 1
    pov "No, I won't help you, no need to ask me."
    if nicolereddresswear == True:
        scene kitchen 11am 007bncc1
    elif nicolebabydollwear == True:
        scene kitchen 11am 007bncc2
    elif nicolesweaterpantswear == True:
        scene kitchen 11am 007bncl1
    elif nicolerobewear == True:
        scene kitchen 11am 007bncl2
    else:
        scene kitchen 11am 007b
    mom "But I didn't want to..."
    pov "Even better. Because it's a woman's job."
    $ dtime += 1
    jump kitchen



label kitchen8amrepeat1:
    pov "I wonder if she's doing that on purpose. No way she smells an orange every morning."
    pov "Or is she just some sort of crazy."
    jump kitchen

label kitchen8amrepeat2:
    pov "Damn, I can't get enough of this view. But it would be even better with some cleavage."
    jump kitchen

label kitchen8amrepeat3:
    scene kitchen 8am 012
    ls "You got me again <giggle>."
    ls "But next time I'll be aware."
    jump kitchen8lsistalk

label kitchen8amrepeat4:
    scene kitchen 8am 006
    ls "I need to go to school soon. But can we do something together this afternoon?"
    if inc == True:
        pov "We'll see if I have time for my lovely little sister."
    else:
        pov "We'll see if I have time for my lovely girl."
    ls "Please... It's so boring all alone"
    pov "Hmm..."
    if gangmember == True and lilsisrelationship >= 6 and lilsislove >= 50 or gangmember == True and lilsisrelationship >= 6 and lilsiscorruption >= 30:
        pov "I have something else for you. Meet me at 4am tomorrow in the kitchen."
        scene kitchen 8am 007
        ls "Why? You want to show me something special?"
        pov "Yes, very special. But I won't tell you now, you'll see then. And stay silent so no one else knows."
        ls "Oh, now I'm very interested."
        $ meet4am = True
    jump kitchen8lsistalk2


label proom8repeat1:
    scene main 8pm parents room
    pov "{i}She's changing again.{/i}"
    call screen proom8rep

screen proom8rep():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1077 ypos 150 action (Hide('proom8rep'), Jump('proom8repeat2')) hovered tt.Action ("Leave her alone [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 684 ypos 150 action (Hide('proom8rep'), Jump('proom8repeat3')) hovered tt.Action ("Stay and watch [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label proom8repeat2:
    pov "{i}I should leave her alone while she's changing.{/i}"
    if momlove >= 30:
        scene parentsroom 8pm 008a
        mom "[pov]!"
        if inc == True:
            pov "Oh hi mom."
        else:
            pov "Oh hi [mother]."
        mom "Are you watching me changing?"
        pov "No... I mean I was about to leave..."
        scene parentsroom 8pm 009a
        mom "Haha, relax [pov]. I'm not mad."
        pov "But you know I can see your boobs."
        mom "I said I'm not mad. <giggle>"
        scene parentsroom 8pm 010a
        mom "Tell me your opinion about these stockings."
        mom "Aren't they beautiful?"
        pov "Y... yes. And they look even better on your legs."
        mom "Oh, thank you [pov]."
        scene parentsroom 8pm 011a
        pov "Let me feel it!"
        mom "Huh?"
        pov "It's so soft and warm on your leg."
        mom "[pov]!"
        pov "Huh?"
        scene parentsroom 8pm 012a
        mom "Your hand..."
        if inc == True:
            pov "I'm sorry mom. I just wanted to feel it, I didn't think..."
        else:
            pov "I'm sorry [mother]. I just wanted to feel it, I didn't think..."
        scene parentsroom 8pm 013a
        mom "It's alright [pov]. Just tell me next time before, I was just surprised."
        if inc == True:
            pov "Oh, OK, mom. But it's really soft and I like it."
        else:
            pov "Oh, OK, [mother]. But it's really soft and I like it."
        mom "Then it's good that you like it means I made the right decision."
        pov "{i}What's with her? Standing half naked here and letting me touch her?{/i}"
        mom "[pov]? Are you alright?"
        pov "Oh... sure. I'll go now."
        mom "Thank you for helping me out."
    $ momlove += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

label proom8repeat3:
    pov "{i}I want to see her changing.{/i}"
    if inc == True:
        pov "Hi mom!"
    else:
        pov "Hi [mother]!"
    scene parentsroom 8pm 003
    mom "Eh?"
    mom "What are you doing here [pov]? You know that I'm changing!"
    pov "I know. I just came to see you half-naked again!"
    scene parentsroom 8pm 004
    mom "..."
    pov "I need to see your hot body more often!"
    mom "Hmm..."
    if droom7momlookcor == True:
        scene parentsroom 8pm 007b
        pov "Good, you remembered."
        scene parentsroom 8pm 008b
        pov "Your hot big tits!"
        pov "I need to play with them soon!"
        mom "But..."
        if gangmember == True:
            if inc == True:
                pov "No mom! I'm a gang-member now, so I can do what I want to!"
            else:
                pov "No [mother]! I'm a gang-member now, so I can do what I want to!"
            pov "And now turn around."
            mom "Turn around?"
            pov "Just do it!"
            scene parentsroom 8pm 010b
            pov "{i}It's time to teach her a lesson.{/i}"
            call screen proom8chless                
        else:
            pov "Oh I'm sure you won't complain when it happens!"
            mom "..."
        pov "They're already waiting for me!"
        mom "Hnn..."
    scene parentsroom 8pm 009b
    pov "But you're already done changing, maybe I'll need to come by sooner next time!"
    mom "No you mustn't."
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    $ momcorruption += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

screen proom8chless():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1491 ypos 67 action (Hide('proom8chless'), Jump('proom8lesstits')) hovered tt.Action ("Grope her tits") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1351 ypos 740 action (Hide('proom8chless'), Jump('proom8lessass')) hovered tt.Action ("Grope her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1491 ypos 740 action (Hide('proom8chless'), Jump('proom8lessslap')) hovered tt.Action ("Slap her ass") focus_mask True
        frame:
            xalign .5
            text tt.value

label proom8lesstits:
    pov "{i}That'll teach her a lesson.{/i}"
    scene parentsroom 8pm 011d
    mom "Hah..."
    pov "I love your big, soft tits!"
    scene parentsroom 8pm 012d
    mom "Why?"
    pov "Because I want to! You need to accept that I claimed you."
    mom "Hnng..."
    pov "We'll have so much fun together."
    pov "But you're already done changing, maybe I'll need to come by sooner next time!"
    mom "No you mustn't."
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    $ momcorruption += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

label proom8lessass:
    pov "{i}That'll teach her a lesson.{/i}"
    scene parentsroom 8pm 011c
    mom "Hah..."
    pov "I love your hot, firm ass!"
    scene parentsroom 8pm 012b
    mom "Why?"
    pov "Because I want to! You need to accept that I claimed you."
    mom "Hnng..."
    pov "We'll have so much fun together."
    pov "But you're already done changing, maybe I'll need to come by sooner next time!"
    mom "No you mustn't."
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    $ momcorruption += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom

label proom8lessslap:
    pov "{i}That'll teach her a lesson.{/i}"
    scene parentsroom 8pm 011b
    with vpunch
    mom "Hah..."
    pov "I love your hot, firm ass!"
    scene parentsroom 8pm 012b
    mom "Why?"
    pov "Because I want to! You need to accept that I claimed you."
    mom "Hnng..."
    pov "We'll have so much fun together."
    pov "But you're already done changing, maybe I'll need to come by sooner next time!"
    mom "No you mustn't."
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    $ momcorruption += 1
    $ momrelationship += 1
    $ dtime += 1
    jump parentsroom



label droom6pmrepeat:
    pov "Yeah, another dinner with sandwiches."
    if nicolereddresswear == True:
        scene diningroom 6pm 006ncc1
    elif nicolebabydollwear == True:
        scene diningroom 6pm 006ncc2
    elif nicolesweaterpantswear == True:
        scene diningroom 6pm 006ncl1
    elif nicolerobewear == True:
        scene diningroom 6pm 006ncl2
    else:
        scene diningroom 6pm 006
    "You eat dinner together and talk about some gossip."
    $ dtime += 1
    jump droom


label droom12pmrepeat:
    scene diningroom 12pm 003
    if nicolereddresswear == True:
        show 12pm003niccorruption1:
            xpos 244
            ypos 291
    elif nicolebabydollwear == True:
        show 12pm003niccorruption2:
            xpos 244
            ypos 291
    elif nicolesweaterpantswear == True:
        show 12pm003niclove1:
            xpos 244
            ypos 291
    elif nicolerobewear == True:
        show 12pm003niclove2:
            xpos 244
            ypos 291
    else:
        show 12pm003nicnormal:
            xpos 244
            ypos 291
    if alexisrockerwear == True:
        show 12pm003alecorruption1:
            xpos 1192
            ypos 454
    elif alexislingeriewear == True:
        show 12pm003alecorruption2:
            xpos 1192
            ypos 454
    elif alexisjeansskirtwear == True:
        show 12pm003alelove1:
            xpos 1192
            ypos 454
    elif alexisgridwear == True:
        show 12pm003alelove2:
            xpos 1192
            ypos 454
    else:
        show 12pm003alenormal:
            xpos 1192
            ypos 454
    "You enjoy eating together and talk about some gossip."
    "[ls] is still teasing you."
    if nicolereddress == 3 or nicolebabydoll == 3 or nicolesweaterpants == 3 or nicolerobe == 3:
        jump droom12pmclothreactions
    if alexisrocker == 3 or alexislingerie == 3 or alexisjeansskirt == 3 or alexisgrid == 3:
        jump droom12pmclothreactionsalexis
    if cassandraheartdress == 3 or cassandralingerie == 3 or cassandrajeans == 3 or cassandrapajama == 3:
        jump droom12pmclothreactionscassandra
    $ dtime += 1
    jump droom


label lroom15repeat:
    $ bigsisrelationship += 1
    $ irinarelationship += 1
    "You get closer to her."
    scene livingroom 3pm 003
    pov "Hey [irina]!"
    scene livingroom 3pm 004b
    irina "Oh, hello [pov]."
    if inc == True:
        pov "You're here to meet with my sister again?"
    else:
        pov "You're here to meet with [bs] again?"
    scene livingroom 3pm 006
    irina "Yes we're outside and now she's lingering again."
    pov "Haha, I know."
    call screen lroom15repchoice

screen lroom15repchoice():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 543 ypos 231 action (Hide('lroom15repchoice'), Jump('lroom15repirinalove')) hovered tt.Action ("Greet her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1388 ypos 231 action (Hide('lroom15repchoice'), Jump('lroom15repirinacor')) hovered tt.Action ("Greet her [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom15repirinalove:
    scene livingroom 3pm 002d
    $ irinalove += 1
    $ irinalroom15love = True
    pov "Come here!"
    irina "Again you're so nice to me."
    pov "Yes, because I really like you."
    irina "Then just hold me tight."
    "You hold her a few moments longer."
    scene livingroom 3pm 003d
    irina "That was something I never want to miss."
    pov "Me too."
    irina "I still can't believe that you are so nice to me and not trying to get in my pants."
    pov "Haha, maybe I still want to go there."
    irina "Maybe, but I like the way you do it slowly. <giggle>"
    scene livingroom 3pm 004d
    irina "And I'm also totally lost in the way you look at me."
    "She comes closer."
    pov "Then I'll look at you more."
    irina "I... can't... stop..."
    scene livingroom 3pm 005d
    irina "<kiss>"
    pov "Hm... what a nice surprise."
    irina "I'm glad you like it, hmm."
    irina "<kiss more>"
    scene livingroom 3pm 006d
    irina "That was so wonderful, we should continue this sometime."
    pov "Now?"
    irina "<giggle> Not now, [bs] would kill us and you know that."
    pov "You're worth it!"
    irina "Ohh... <giggle>"
    scene livingroom 3pm 010
    bs "Oh you're here again [pov]!"
    pov "Hmm, yes!"
    bs "Want to try your perverted things on her again?"
    jump lroom15repboth


label lroom15repirinacor:
    scene livingroom 3pm 002d
    $ irinacorruption += 1
    $ irinalroom15cor = True
    pov "Come here!"
    irina "Oh, so nice."
    pov "Then enjoy it more."
    scene livingroom 3pm 003c
    "You grope her ass."
    irina "Hnn...?"
    pov "That crisp ass."
    irina "Hmm..."
    scene livingroom 3pm 004c
    pov "So you liked your hug?"
    irina "..."
    pov "I had to do it after you teased me with your hot ass in that short skirt."
    irina "Hnn..."
    pov "And when we talk about teasing."
    scene livingroom 3pm 005c
    pov "That cleavage you show is another good reason why I chose you."
    irina "You... chose me..."
    pov "Yes, I'm sure I told you that before and you should stop teasing me like that."
    irina "Stop teasing...?"
    scene livingroom 3pm 005cb
    pov "Yes and the best way is to show me your tits now, so I don't have to fantasize about them any more."
    irina "You want me to show you my boobs right now?"
    pov "Right. Prove to me you're worth it to be my girl."
    irina "But [bs] is coming any moment."
    pov "Oh I don't care about her, only about your tits at the moment."
    irina "Hmm... OK."
    scene livingroom 3pm 005cc
    pov "Oh these are some hot tits, you should be glad!"
    irina "T... Thank you..."
    pov "I can't wait to lay my hands on them and play with them."
    irina "But... you... can't do it now."
    pov "Hm... we'll see."
    scene livingroom 3pm 005cd
    irina "Please... [bs] is coming."
    pov "Haha, OK. You're my good girl, you can get dressed again."
    irina "T... Thank you..."
    pov "I'll play with them another time."
    scene livingroom 3pm 010
    bs "Oh you're here again [pov]!"
    pov "Hmm, yes!"
    bs "Want to try your perverted things on her again?"
    jump lroom15repboth


label lroom15repboth:
    call screen lroom15repbothchoice

screen lroom15repbothchoice():
    default tt = Tooltip (" ")

    fixed:
        if irinalroom15love == True:
            imagebutton auto "gui/icons/icon_love_%s.png" xpos 785 ypos 185 action (Hide('lroom15repbothchoice'), Jump('lroom15repirinalove2')) hovered tt.Action ("Show her more love [lv1]/[irina]") focus_mask True
            imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 785 ypos 327 action (Hide('lroom15repbothchoice'), Jump('lroom15repirinacor2')) hovered tt.Action ("Play with her [cr1]/[irina]") focus_mask True
        if irinalroom15cor == True:
            imagebutton auto "gui/icons/icon_love_%s.png" xpos 785 ypos 185 action (Hide('lroom15repbothchoice'), Jump('lroom15repirinalove2')) hovered tt.Action ("Show her some love [lv1]/[irina]") focus_mask True
            imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 785 ypos 327 action (Hide('lroom15repbothchoice'), Jump('lroom15repirinacor2')) hovered tt.Action ("Play with her more [cr1]/[irina]") focus_mask True
        if d5love == True:
            imagebutton auto "gui/icons/icon_love_%s.png" xpos 1121 ypos 185 action (Hide('lroom15repbothchoice'), Jump('lroom15repcaslove')) hovered tt.Action ("Go for her [lv1]/[bs]") focus_mask True
        if d5corruption == True:
            imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1121 ypos 327 action (Hide('lroom15repbothchoice'), Jump('lroom15repcascor')) hovered tt.Action ("Have some fun with her [cr1]/[bs]") focus_mask True
        frame:
            xalign .5
            text tt.value

label lroom15repirinalove2:
    scene livingroom 3pm 007d
    $ irinalove += 1
    pov "Yes, but I won't call it perverted."
    irina "Hnn... <giggle>"
    pov "I wouldn't do such things to her."
    irina "More. <giggle>"
    scene livingroom 3pm 008d
    bs "What...?"
    irina "He's so sweet. Isn't he?"
    bs "Are you drunk? Letting him touch you like that?!"
    pov "Oh this isn't all."
    scene livingroom 3pm 009d
    bs "Wha...?"
    pov "<kiss>"
    irina "Hmm!"
    "[irina] is returning your kiss eagerly."
    pov "You waited for this, didn't you?"
    irina "Hmm... yes..."
    bs "..."
    scene livingroom 3pm 010d
    bs "You two are fucking crazy! I'm out of here!"
    pov "Calm down, I just had to do it."
    irina "<giggle>"
    bs "Idiots!"
    scene livingroom 3pm 011d
    irina "Haha, that was too much for her. But not for me, thank you for kissing me."
    pov "I couldn't withstand it, I had to kiss you and prove to her that we're together."
    irina "I can't wait to prove her some more. <giggle>"
    if irinalroom15love == True:
        irina "I would love to stay here with you now and kiss some more, but I think I should go after her."
        irina "She does stupid things when she's angry and she's still my friend after all."
        pov "Yes, you should follow her, we'll have more time to know each other better."
        irina "Oh, I can't wait. See you my gentleman."
        $ irinalroom15love = False
        $ lroom15extendfirst = True
        $ dtime += 1
        jump lroom
    else:
        irina "I was surprised when you suddenly kissed me like that after you were so demanding before."
        irina "But it was a very nice surprise and I would love to get more like that from you, but I think I should now go after her."
        irina "She does stupid things when she's angry and she's still my friend after all."
        pov "Yes, you should follow her and maybe I'll surprise you more often."
        irina "Oh, I can't wait. See you [pov]."
        $ irinalroom15cor = False
        $ lroom15extendfirst = True
        $ dtime += 1
        jump lroom

label lroom15repirinacor2:
    scene livingroom 3pm 006c
    $ irinacorruption += 1
    pov "Yes, maybe that's my plan."
    "You get closer to [irina]."
    irina "<giggle>"
    bs "What's going on here?"
    pov "{i}Oh it seems [irina] likes it when she's charmed with [bs] around.{/i}"
    scene livingroom 3pm 007c
    "You grope her secretly."
    irina "Hnn..."
    scene livingroom 3pm 008c
    irina "Hnn..."
    pov "{i}Oh [irina] is lightly shaking. But I'm sure she'll do everything to prevent getting caught.{/i}"
    bs "Just forget it [pov]. [irina] won't fell for your attempts. She isn't like the sluts you're wishing for."
    pov "Oh, you're so sure about it?"
    irina "Hmm!"
    bs "Oh yes, I am!"
    pov "{i}Time for more fun.{/i}"
    scene livingroom 3pm 009c
    "You probe her asshole with your finger."
    pov "{i}She's already mine, haha.{/i}"
    scene livingroom 3pm 010c
    "Your finger enters her."
    irina "Aaah..."
    if irinalroom15love == True:
        "She's obviously shocked that you took advantage of her while you started so nice."
        pov "{i}Hah, I'm full of surprises.{/i}"
    bs "What is it [irina]?"
    irina "Hnn..."
    scene livingroom 3pm 011c
    irina "I... I just bit my tongue."
    pov "{i}A good answer, haha.{/i}"
    bs "Everything alright, you look confused."
    irina "Yes, yes. Everything is alright."
    "You feel her asshole getting tight, so you let go of her."
    pov "{i}No need to overdo it now. I made my statement.{/i}"
    bs "Come on we should go now and leave that looser so he can play with himself."
    pov "{i}Oh that's not nice. But I'm not even mad, haha.{/i}"
    irina "O... OK."
    "They leave and [irina] walks somewhat uncomfortable."
    $ irinalroom15cor = False
    $ irinalroom15love = False
    $ lroom15extendfirst = True
    $ dtime += 1
    jump lroom

label lroom15repcaslove:
    scene livingroom 3pm 006e
    $ bigsislove += 1
    "You move closer to [bs]."
    irina "Hah, you're still so mad at him?"
    bs "Of course, he's just a silly pervert."
    if cdate5bj == True or cdate5fuck == True or cdate5hj == True:
        pov "{i}Wow, talking like that after we had so much fun at the mall.{/i}"
    pov "{i}I'll show her that she's wrong.{/i}"
    scene livingroom 3pm 011b
    if inc == True:
        "You hug your sister."
    else:
        "You hug her."
    bs "Huh?"
    irina "Oh..."
    pov "<whisper> I want to talk to you alone."
    scene livingroom 3pm 003f
    irina "What's happening?"
    bs "Everything is alright, I think."
    if inc == True:
        bs "Can you go first? I need to talk to my brother."
    else:
        bs "Can you go first? I need to talk to [pov]."
    irina "Oh... sure."
    "[irina] leaves you."
    scene livingroom 3pm 004f
    bs "What's the problem, [pov]?"
    pov "I had to see you alone. Just the two of us."
    bs "Hm... for a special reason?"
    pov "I'm still thinking about what happened at the mall all the time."
    bs "I told you about that..."
    scene livingroom 3pm 005f
    pov "I know but I can't endure it anymore."
    bs "What? You can't..."
    pov "But I have too and nothing can stop me now."
    if inc == True:
        pov "I love you big sis."
    else:
        pov "I love you [bs]."
    scene livingroom 3pm 006f
    pov "<kiss>"
    bs "Oh... hah..."
    pov "I can't wait anymore."
    bs "S...stop... don't kiss me there."
    pov "No, I'm at the perfect spot. <kiss>"
    bs "Hah... but I told you..."
    pov "I know you love getting kissed."
    bs "Hah... [pov]."
    scene livingroom 3pm 007f
    bs "You... kissed me..."
    pov "Yes and I'll do it more and more until you admit that I'm a better boyfriend for you."
    bs "But... you won't stop even after I told you it was a mistake?"
    pov "No, I won't It wasn't a mistake you loved it too. It's a mistake that you make it only once."
    scene livingroom 3pm 008f
    pov "You know that I'm right, just think more about it."
    bs "Hmm..."
    pov "We can make it our secret!"
    bs "Hmm..."
    pov "You won't find anyone that loves you like me all my life and won't abandon you."
    if inc == True:
        pov "You're my sister, we can stay together forever."
    else:
        pov "You're my childhood friend, we can stay together forever."
    bs "You're confusing me very much right now."
    pov "So you'll think about it?"
    bs "I must go now and see after [irina]."
    "She leaves you."
    $ irinalroom15cor = False
    $ irinalroom15love = False
    $ lroom15extendcaslove = True
    $ dtime += 1
    jump lroom

label lroom15repcascor:
    scene livingroom 3pm 006e
    $ bigsiscorruption += 1
    "You move closer to [bs]."
    irina "Hah, you're still so mad at him?"
    bs "Of course, he's just a silly pervert."
    pov "{i}Wow, talking like that after we had so much fun at the mall.{/i}"
    pov "{i}I'll teach her a lesson.{/i}"
    scene livingroom 3pm 007e
    "You grope her secretly."
    bs "Huh?"
    scene livingroom 3pm 008e
    pov "{i}Haha, she's staring so confused by me.{/i}"
    irina "What's wrong [bs]?"
    bs "No... nothing, it's just..."
    if inc == True:
        pov "{i}She won't fight back, she won't risk getting caught while her little brother gropes her ass so shameless{/i}"
    else:
        pov "{i}She won't fight back, she won't risk getting caught while I grope her ass so shameless{/i}"
    pov "{i}And especially not when I could tell her friend what we did together, haha.{/i}"
    scene livingroom 3pm 009e
    irina "I'm talking to you [bs]!"
    bs "Oh, hnn..."
    "You knead her ass more."
    bs "Every... thing is alright. My thoughts just flew away."
    irina "Haha, you're really crazy sometimes."
    irina "Let's go?"
    scene livingroom 3pm 010e
    pov "You can go first [irina], I have to talk with [bs]."
    if inc == True:
        pov "Siblings-talk."
    bs "Hnn..."
    irina "You sure?"
    bs "Yes, go first. I'll come soon."
    irina "Haha, OK. See you [pov]."
    scene livingroom 3pm 011e
    bs "Are you fucking crazy? Groping me like that in front of my friend!"
    pov "Shhh... you better stop talking now."
    bs "What's wrong with you!"
    pov "Maybe I should tell [irina] what happened at the mall?"
    scene livingroom 3pm 012e
    bs "...no... you can't."
    pov "Oh you're learning fast. But don't worry, I wont do it."
    pov "Not until you're my girl!"
    bs "I can't be your girl."
    pov "Says the girl that loved to be dominated, even when her best friend is around."
    bs "I... I..."
    pov "Stop denying it. I already decided that I'll make you mine."
    bs "..."
    if inc == True:
        pov "We'll have a secret relationship as lovers, brother and sister as it should be!"
    else:
        pov "We'll have a secret relationship as lovers, childhood friends as it should be!"
    bs "Hnn... I... have to go..."
    pov "Sure, but remember my words, girlfriend!"
    "She leaves you in a hurry."
    $ irinalroom15cor = False
    $ irinalroom15love = False
    $ lroom15extendcascor  = True
    $ dtime += 1
    jump lroom