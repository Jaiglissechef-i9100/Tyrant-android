

label club19ik:
    hide screen townl
    scene town club 7pm 001a
    if vivianfirstmeet == False:
        pov "Oh it's [irina] and a bartender."
    else:
        pov "Oh it's [irina] and [vivian]."
    jump club19ik1

label club19ik1:
    scene town club 7pm 001a
    call screen club19ik2

screen club19ik2():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 1271 ypos 471 action (Hide('club19ik2'), Jump('club19iklookbelly1')) hovered tt.Action ("Look at belly") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 705 ypos 471 action (Hide('club19ik2'), Jump('club19iklookbelly2')) hovered tt.Action ("Look at belly") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 419 ypos 606 action (Hide('club19ik2'), Jump('club19iklookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" xpos 966 ypos 134 action (Hide('club19ik2'), Jump('club19iktalk')) hovered tt.Action ("Talk") focus_mask True
        frame:
            xalign .5
            text tt.value

label club19iklookbelly1:
    scene town club 7pm 002a
    pov "{i}What a hot belly she has. And those fine big tits.{/i}"
    jump club19ik1

label club19iklookbelly2:
    scene town club 7pm 003a
    pov "{i}What a sexy view. That dress is killing me.{/i}"
    jump club19ik1

label club19iklookcrotch:
    scene town club 7pm 004a
    pov "{i}That sexy dress. Showing so much off but hiding the best parts. I wonder if she's wearing it without panties?{/i}"
    jump club19ik1

label club19iktalk:
    scene town club 7pm 005a
    if vivianfirstmeet == True:
        pov "Hi you two!"
        irina "Oh hi [pov]!"
        vivian "Hello."
    else:
        pov "Hi, [irina]!"
        irina "Oh hi [pov]!"
        "Bartender" "Hello."
    scene town club 7pm 006a
    irina "What a surprise to see you here."
    pov "I wanted to check out what happens in town at this time."
    irina "Oh normally I'm here with [bs], having some fun."
    pov "And wearing that sexy dress again."
    irina "<giggle>"
    $ irinarelationship += 1
    if vivianfirstmeet == True:
        $ vivianrelationship += 1
    jump club19ikgreet

label club19ikgreet:
    scene town club 7pm 006a
    call screen club19ikgreet1

screen club19ikgreet1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 489 ypos 206 action (Hide('club19greet1'), Jump('club19iklove')) hovered tt.Action ("Greet her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1236 ypos 206 action (Hide('club19greet1'), Jump('club19ikcor')) hovered tt.Action ("Greet her [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label club19ikcor:
    scene town club 7pm 007a
    "You grope her ass."
    irina "Huh..."
    pov "Oh come on. You want to show off to me and tease me."
    irina "Hmm..."
    pov "That's how I like it. Firm but still soft and wrapped in that sexy dress."
    scene town club 7pm 008a
    irina "Hmm..."
    pov "So I was right."
    irina "..."
    pov "Then it's good that I'm here now so we can have some fun together, don't you think?"
    irina "Y... yes, sure."
    scene town club 7pm 011a
    if vivianfirstmeet == False:
        "Bartender" "You're really a weird couple."
    else:
        vivian "You're really a weird couple."
    pov "Oh we aren't together. Yet!"
    scene town club 7pm 012a
    irina "<giggle>"
    pov "But it won't take long and she'll be my girl!"
    irina "With a cute boyfriend <giggle>"
    pov "Maybe cute, but demanding!"
    irina "<giggle>"
    pov "Let's go!"
    $ irinacorruption += 1
    $ dtime += 1
    jump club

label club19iklove:
    scene town club 7pm 009a
    pov "Come here!"
    irina "Ohh..."
    pov "A good hug for a nice girl."
    irina "<giggle> I could get used to that."
    pov "Haha, oh you will."
    scene town club 7pm 010a
    irina "It's so good to see you again [pov]."
    pov "That's the same thing I would say."
    irina "Ohh... <giggle>"
    pov "So how about we hang out together?"
    irina "I'd love to. And that's what I really want."
    scene town club 7pm 011a
    if vivianfirstmeet == False:
        "Bartender" "You're really a weird couple."
    else:
        vivian "You're really a weird couple."
    pov "Oh, we aren't together. But maybe this beautiful girl will have me."
    scene town club 7pm 012a
    irina "Oh my god. You're so cute."
    pov "Oh I can be everything you want, haha."
    irina "And so nice and surprising."
    pov "So how about we take a look around?"
    irina "I'd love to."
    $ irinalove += 1
    $ dtime += 1
    jump club



label club19kate:
    hide screen townl
    scene town club 7pm 001b
    "You get closer to the dancing girl."
    "She shows off her skills at dancing."
    pov "{i}Nice outfit.{/i}"
    scene town club 7pm 002b
    pov "{i}Wow! A really nice outfit. And those moves.{/i}"
    pov "{i}She seems to be really fit and agile.{/i}"
    jump club19katech

label club19katech:
    scene town club 7pm 002b
    call screen club19katech1

screen club19katech1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 863 ypos 528 action (Hide('club19katech1'), Jump('club19katelove')) hovered tt.Action ("Dance with her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1001 ypos 528 action (Hide('club19katech1'), Jump('club19katecor')) hovered tt.Action ("Dance with her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 929 ypos 666 action (Hide('club19katech1'), Jump('club19chl')) hovered tt.Action ("Leave her alone") focus_mask True
        frame:
            xalign .5
            text tt.value

label club19katecor:
    scene town club 7pm 003b
    "You decide to dance very close with her and pressing her onto you."
    pov "{i}Wow, that hot ass grinding now on my dick.{/i}"
    pov "{i}That trained and slender body. So hot.{/i}"
    "The girl is lost in her dancing."
    scene town club 7pm 004b
    "Girl" "Aaahh..."
    pov "{i}Oh, the wild horse woke up! So you'll need to be tamed good.{/i}"
    "Girl" "What...? No!"
    pov "{i}Grinding her ass all the time on me and now playing surprised? Slut!{/i}"
    scene town club 7pm 005b
    "Girl" "What the hell are you doing?"
    pov "Hmm... Dancing with you?"
    "Girl" "Dancing? You groped me and rubbed yourself on me!"
    pov "I thought that was part of your sexy dancing. And all alone you could need a partner!"
    "Girl" "Are you serious? What the fuck is wrong with you?"
    pov "Nothing! Just some dancing with a sexy girl."
    scene town club 7pm 006b
    "Girl" "Fuck you! Don't you dare touch me ever again."
    pov "{i}Still playing innocent after such a hot show. I know that she liked it.{/i}"
    pov "{i}Maybe she want to be conquered the hard way?{/i}"
    pov "{i}Slut.{/i}"
    $ katecorruption += 1
    $ dtime += 1
    jump club

label club19katelove:
    scene town club 7pm 007b
    "You decide to dance behind her."
    pov "{i}Oh my god. What a beautiful body she has. And these moves!{/i}"
    pov "{i}I wonder why this beauty is dancing all alone? I hope she isn't a lesbian.{/i}"
    "You're caught by her moves."
    scene town club 7pm 008b
    "Girl" "Huh?"
    pov "{i}Oh, she noticed me.{/i}"
    pov "Hi!"
    "Girl" "..."
    scene town club 7pm 009b
    pov "{i}Shit! That outfit is killing me. Is it supposed to be worn so low?{/i}"
    "Girl" "Hi, you really want to sneak up on me like that?"
    pov "Oh, I wouldn't scare you. I just won't interrupt your dancing."
    "Girl" "Oh, OK."
    pov "Hi again. I'm [pov]. I'm all caught up by your cool dancing moves."
    "Girl" "Ah, so that's your move on girls?"
    pov "No! I never met a girl with those dancing skills."
    scene town club 7pm 010b
    "Girl" "After you show some manners I'll tell you my name."
    "Girl" "But don't waste your time, I already have a boyfriend."
    if katefirstmeet == False:
        $ kate = renpy.input(_("Her name is...")) or _("Kate")
    $ katefirstmeet = True
    kate "He's over there. The DJ of the club."
    scene town club 7pm 011b
    pov "{i}What? This guy is the boyfriend of that beautiful girl?{/i}"
    pov "{i}Something must be wrong? Maybe he's rich or the owner of the club?{/i}"
    kate "Are you still here?"
    pov "Oh yes, sorry. Nice to meet you [kate]."
    kate "Sure! But please don't bother me anymore, so I can continue dancing."
    kate "Alone!"
    pov "{i}Damn, why is she so rude?{/i}"
    $ katelove += 1
    $ katerelationship += 1
    $ dtime += 1
    jump club


label club19bs:
    hide screen townl
    scene town club 7pm 001c
    pov "{i}There is [bs] with her boyfriend.{/i}"
    jump club19bslook

label club19bslook:
    scene town club 7pm 001c
    call screen club19bslook1

screen club19bslook1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 852 ypos 326 action (Hide('club19bslook1'), Jump('club19bslooktits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" xpos 647 ypos 602 action (Hide('club19bslook1'), Jump('club19bslookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" xpos 924 ypos 170 action (Hide('club19bslook1'), Jump('club19bstalk')) hovered tt.Action ("Talk") focus_mask True
        frame:
            xalign .5
            text tt.value

label club19bslooktits:
    scene town club 7pm 002c
    pov "{i}Now I have a chance to take a good look at this dress. So much of her nice skin.{/i}"
    jump club19bslook

label club19bslookcrotch:
    scene town club 7pm 003c
    pov "{i}What a damn hot view. And those boots make the outfit even sexier.{/i}"
    jump club19bslook

label club19bstalk:
    scene town club 7pm 004c
    pov "Hey there!"
    martin "Oh hey [pov]. What you're doing here?"
    bs "Oh... hi..."
    if inc == True:
        pov "{i}Oh big sis. Annoying as ever. But that dress is killing me.{/i}"
    else:
        pov "{i}Oh [bs]. Annoying as ever. But that dress is killing me.{/i}"
    pov "I want to know what's going on here at this time of day."
    martin "Not much. The most people around don't have the money to come here often."
    pov "Oh... so only a few."
    martin "Yes and mostly the same."
    pov "{i}Haha, [bs] is staring so bad. Maybe she wants to be alone with Martin.{/i}"
    jump club19bsch

label club19bsch:
    scene town club 7pm 004c
    call screen club19bsch1

screen club19bsch1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 614 ypos 203 action (Hide('club19bsch1'), Jump('club19bslove')) hovered tt.Action ("Leave them alone [lv1]/[bs] [gd1]/Martin") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 966 ypos 203 action (Hide('club19bsch1'), Jump('club19bscor')) hovered tt.Action ("Blame Martin [cr1]/[bs] [bd1]/Martin") focus_mask True
        frame:
            xalign .5
            text tt.value

label club19bslove:
    pov "I'll leave you now so you can enjoy your time together."
    martin "Okay, see you around [pov]."
    bs "Bye..."
    $ bigsislove += 1
    $ bigsisrelationship += 1
    $ martingood += 1
    $ dtime += 1
    jump club

label club19bscor:
    pov "{i}Let's corrupt their relationship, haha.{/i}"
    pov "Hey Martin, there is a girl outside asking for you."
    scene town club 7pm 005c
    martin "What...?"
    bs "What?"
    pov "Yeah she said she can't wait to get plugged again."
    martin "No way!"
    scene town club 7pm 006c
    bs "A girl asking for you and talking about plugging?"
    bs "You better explain that now!"
    martin "I don't know a girl that I should have plugged..."
    martin "This must be a mistake!"
    pov "But aren't you the singer from the band \"The Chosen\" then?"
    scene town club 7pm 008c
    bs "Oh yes he is! I knew it! You damn cheater!"
    martin "What no! I told you before and tell you know there are no other girls."
    bs "Why should he lie out of nowhere?"
    pov "{i}Hahaha, just wunderful.{/i}"
    scene town club 7pm 009c
    bs "Stay away from me you asshole!"
    bs "Don't you dare call me until you can prove that you're right!"
    martin "But [bs], you have to believe me!"
    bs "No! I knew you couldn't keep your hands of your groupies!"
    bs "Fuck you! I'm staying with [irina]."
    scene town club 7pm 010c
    if inc == True:
        martin "I don't get it! I never betrayed your sister."
    else:
        martin "I don't get it! I never betrayed her."
    martin "The girl must have a bad reason to do that."
    pov "No she didn't."
    martin "How do you know?"
    pov "There was no girl. I lied!"
    martin "What...? Why did you do that? I thought our karma would match?"
    pov "{i}What the fuck? Is he serious?{/i}"
    scene town club 7pm 011c
    martin "What have I ever done to you that you're so bad with me?"
    if inc == True:
        pov "It's easy. I don't like you and I think my big sister deserve someone better."
    else:
        pov "It's easy. I don't like you and I think she deserve someone better."
    pov "And also you're an emo-freak!"
    martin "She was right from the start, you're really evil."
    pov "Maybe..."
    martin "I'll prove to her what you did and then I'll get her back."
    pov "Sure, Idiot!"
    $ bigsiscorruption += 1
    $ bigsisrelationship += 1
    $ martinbad += 1
    $ dtime += 1
    jump club20maway


label club20maway:
    scene town club 8pm 001
    pov "{i}What's [bs] now up to?{/i}"
    pov "{i}I should go near them to get to know what they're doing.{/i}"
    scene town club 8pm 002
    if vivianfirstmeet == True:
        vivian "Are you sure?"
    else:
        "Barkeeper" "Are you sure?"
    bs "Oh yes! I need that now and [irina] will assist me!"
    if vivianfirstmeet == True:
        vivian "So your boyfriend was an asshole again?"
    else:
        "Barkeeper" "So your boyfriend was an asshole again?"
    bs "You have no idea!"
    if vivianfirstmeet == True:
        vivian "Ok. You know what you're doing."
    else:
        "Barkeeper" "Ok. You know what you're doing."
    scene town club 8pm 003
    bs "We don't need them, they're all pigs!"
    irina "Haha, when you say that."
    bs "You know it's true. Drink with me, my friend!"
    irina "Cheers!"
    scene town club 8pm 004
    pov "{i}Wait! I lied to get rid of Martin, he's the bad guy and they're getting drunk?{/i}"
    bs "<gulp> <gulp>"
    irina "<gulp> <gulp>"
    pov "{i}Haha, nice!{/i}"
    pov "{i}But it seems they're doing this more often. Maybe Martin isn't the nice guy he claims to be.{/i}"
    scene town club 8pm 005
    irina "Hah..."
    bs "So good!"
    irina "More?"
    bs "Oh yes!"
    pov "{i}Damn. Are they used to this hard stuff? Drinking it like water.{/i}"
    bs "Let's get it over with!"
    scene town club 8pm 006
    irina "Oh... Hi!"
    pov "{i}Wow that took some time to notice me.{/i}"
    bs "<gulp> <gulp>"
    irina "..."
    pov "..."
    irina "..."
    pov "{i}She's just staring at me. What's she up to?{/i}"
    scene town club 8pm 007
    bs "Oh... Why did you stop drinking?"
    irina "He... he's just standing there and looking at us."
    pov "Is that wrong?"
    irina "You showed some manners and waited there."
    pov "{i}What? She's serious? What else should I do, rape them? Are all guys here jerks?{/i}"
    bs "He just wants to peep on us! I know him better then you, trust me."
    irina "I'm not sure! I think I'll give him a chance."
    scene town club 8pm 008
    bs "You must be kidding. He's a pig like all the others. We have to stay together."
    irina "I don't agree with you this time! You have chosen wrong maybe, but I have a good feeling."
    pov "{i}Oh, she's very attracted to me.{/i}"
    bs "I warn you. He'll abuse you too."
    irina "Haha, relax [bs]. Sometimes you get so angry. I'm a big girl too."
    scene town club 8pm 009
    bs "Whatever! I can drink on my own!"
    irina "Hi again!"
    pov "{i}Haha, is the alcohol already doing it's job?{/i}"
    pov "Hi [irina]."
    irina "You... you wanna dance with me, maybe?"
    jump club20idance

label club20idance:
    call screen club20idance1

screen club20idance1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_tickle_%s.png" xpos 813 ypos 300 action (Hide('club20idance1'), Jump('club20idanceyes')) hovered tt.Action ("Dance with her [lv1]/[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1600 ypos 300 action (Hide('club20idance1'), Jump('club20abort')) hovered tt.Action ("Leave them alone") focus_mask True
        frame:
            xalign .5
            text tt.value

label club20abort:
    scene town club 8pm 009
    pov "{i}I don't wanna stay with them while they're getting drunk.{/i}"
    pov "No sorry, [irina]. I'll do something else."
    scene town club 8pm 009a
    irina "Oh... I understand."
    irina "[bs] was right!"
    "You leave them alone."
    jump club

label club20idanceyes:
    scene town club 8pm 009
    $ irinarelationship += 1
    $ club20extend = True
    pov "Sure!"
    scene town club 8pm 010
    irina "Yes! You want to dance with me. Let's go."
    bs "<gulp> <gulp>"
    irina "You won't regret it!"
    scene town club 8pm 011
    irina "I'm so happy that you're dancing with me."
    pov "Me too. Dancing with a beautiful girl!"
    irina "<giggle>"
    pov "Do you two often get drunk when you here in the club?"
    if inc == True:
        irina "Haha, no! Only when your sister is having her \"time\"."
    else:
        irina "Haha, no! Only when [bs] is having her \"time\"."
    pov "{i}I wonder how often that happens?{/i}"
    irina "But we should stay aware. She gets weird when she's getting too much booze, <giggle>."
    pov "Oh. And what about you?"
    irina "I'm not, haha."
    irina "Haha look at her!"
    scene town club 8pm 012
    "[bs] dances drunk alone."
    pov "Oh, you're so right."
    scene town club 8pm 013
    pov "And still drinking more and more."
    irina "She can be embarrassing sometimes, <giggle>."
    pov "I don't care as long as I can stay with you."
    scene town club 8pm 014
    pov "Come here!"
    irina "I'd love to."
    jump club20idancech

label club20idancech:
    call screen club20idancech1

screen club20idancech1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1275 ypos 105 action (Hide('club20idancech1'), Jump('club20idancelove')) hovered tt.Action ("Dance romantic with her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1275 ypos 269 action (Hide('club20idancech1'), Jump('club20idancecor')) hovered tt.Action ("Dance sexy with her [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label club20idancecor:
    irina "Huh?"
    scene town club 8pm 014a
    pov "Let me see how sexy you can dance!"
    "You press her ass on your crotch."
    irina "Hmm..."
    pov "Go on. You'll love that too."
    irina "Ok..."
    "She starts grinding herself on you."
    scene town club 8pm 015a
    irina "Hmm..."
    pov "Nice! Show me what we can do together soon."
    "You start to hump your crotch on her ass like fucking."
    irina "Hng..."
    pov "I bet you'd love a good pounding."
    scene town club 8pm 016a
    "[irina] pump her ass on you."
    pov "That's a good girl!"
    irina "Hmm..."
    pov "I told you, you'd love it too."
    $ irinacorruption += 1
    jump club20bs

label club20idancelove:
    scene town club 8pm 014
    pov "I really enjoy dancing with you like this."
    irina "Me too. I don't think I've ever danced with such a cute boy before."
    scene town club 8pm 015
    pov "And I think you've already fallen for me, haha."
    irina "Which girl could withstand a gentleman like you, <giggle>?"
    pov "So I'm lucky that you're such a beauty!"
    irina "And you're worth staring at all the time."
    scene town club 8pm 016
    irina "It's like you drugged me, you know?"
    pov "That's not what I would call it."
    irina "You know what I mean! <giggle>"
    pov "Yes. And I like it, haha."
    irina "Just hold me more please."
    pov "Sure, my lady."
    irina "<giggle>"
    if irinalove >= 20:
        irina "I'm sorry. I can't wait any longer."
        scene town club 8pm 017
        irina "Hmm..."
        pov "{i}Wow. What a nice surprise.{/i}"
        "You hold her close while she gives you a long kiss."
        $ club20extendedirinalove = True
    $ irinalove += 1
    jump club20bs

label club20bs:
    bs "URGH!"
    $ bigsisrelationship += 1
    scene town club 8pm 018
    irina "Huh?"
    bs "Urgh... I could puke right now!"
    pov "{i}Oh shit. She's hard drunk!{/i}"
    scene town club 8pm 019
    bs "What are you doing? Being a slut for this pig?"
    irina "Calm down [bs]! You're drunk."
    pov "{i}Haha, she's getting really weird while she's drunk.{/i}"
    pov "{i}But not much, haha.{/i}"
    scene town club 8pm 020
    bs "I'll proove it! He's just a pig like the others."
    irina "What? Sorry. I'm not sure what she's up to?"
    pov "Relax [irina]."
    scene town club 8pm 021
    bs "He just wants to fuck a pussy. It doesn't matter which girl owns it."
    irina "[bs]?"
    bs "I'll show you. Like all other pigs he'll forget about you in no time."
    pov "{i}Can this get more weird?{/i}"
    scene town club 8pm 022
    bs "You're hard aren't you? Thinking all the time of fucking my naive friend."
    pov "{i}Shit. She's groping at my crotch. Is this a dream?{/i}"
    irina "..."
    bs "I bet you would ram it in every wet hole right now!"
    bs "Like the animal you are!"
    scene town club 8pm 023
    irina "Stop it!"
    if inc == True:
        irina "You can't do that. He's your brother."
        bs "No! He's just another pig!"
    else:
        irina "You can't do that."
        bs "I'll prove it to you!"
    "[bs] is kneading your dick through your pants."
    pov "{i}I still can't believe this.{/i}"
    bs "His dick's aching for attention. I feel it."
    scene town club 8pm 024
    irina "You have to stop it. You're too drunk."
    bs "But I only want to help you. You need to see the proof."
    irina "No, it's wrong!"
    pov "{i}Wow. What should I do? Let [irina] stop her or have my fun with [bs] trying to get her proof?{/i}"
    pov "{i}I shouldn't be the bad guy in this after [bs] started it right away, even when she's drunk.{/i}"
    jump club20proof

label club20proof:
    call screen club20proof1

screen club20proof1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 990 ypos 138 action (Hide('club20proof1'), Jump('club20prooflove')) hovered tt.Action ("Let [irina] stop her [lv1]/[irina] [lv1]/[bs]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 990 ypos 290 action (Hide('club20proof1'), Jump('club20proofcor')) hovered tt.Action ("Let [bs] continue [cr1]/[irina] [cr1]/[bs]") focus_mask True
        frame:
            xalign .5
            text tt.value

label club20proofcor:
    scene town club 8pm 025a
    pov "Calm down [irina]. I want to see if [bs] can proof it."
    irina "Huh?"
    pov "I'm sure she's just a talker!"
    bs "Hah, you want to challenge me?"
    irina "But..."
    pov "{i}Hah, this should be fun.{/i}"
    scene town club 8pm 026a
    bs "Trust me and I'll show you that I'm right."
    pov "{i}How lucky am I now. Having her so close to me so suddenly.{/i}"
    irina "But... stop..."
    bs "This would be short. His dick is already poking against my crotch. I bet he wants to fuck me right now!"
    irina "Please stop [bs]. I don't want to see this!"
    bs "Calm down! I need to prove it."
    irina "Stop it or I'll leave! You shouldn't do this, you're my friend!"
    pov "{i}No! Don't stop now. Stay strong [bs]!{/i}"
    if irinacorruption >= 30:
        pov "{i}But another idea comes up.{/i}"
        $ club20extendedirinacor = True
        jump club20three
    jump club20threeabort

label club20three:
    call screen club20three1

screen club20three1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1014 ypos 206 action (Hide('club20three1'), Jump('club20threeabort')) hovered tt.Action ("Let her go") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1014 ypos 360 action (Hide('club20three1'), Jump('club20threeyes')) hovered tt.Action ("Demand her to stay [cr1]/[irina]") focus_mask True
        frame:
            xalign .5
            text tt.value

label club20threeyes:
    scene town club 8pm 027ab
    pov "Stay here with us [irina]. And I'll prove to you that [bs] is wrong."
    pov "You're the girl I'm after."
    "You also grab [bs] ass and hold her close to provoke her."
    pov "{i}Damn this should get even better.{/i}"
    pov "Come here!"
    bs "I won't lose! Pig!"
    scene town club 8pm 028ab
    irina "Hmm..."
    bs "What...?"
    "You pull [irina] to you and kiss her. [bs] is staying surprised beside you."
    pov "{i}Wow, I'm holding them both by their asses, but they don't complain.{/i}"
    pov "{i}Making fun of Martin was the best idea.{/i}"
    irina "Hm... <kiss>"
    scene town club 8pm 029ab
    pov "{i}Wow!{/i}"
    "[irina] is getting more turned on and gives you a french kiss."
    bs "But..."
    pov "You're... <kiss> a good girl."
    irina "Y... yes <kiss> I am YOUR good girl."
    pov "{i}Haha, what a great win/win. I'm groping to hot girls and getting rewarded!{/i}"
    scene town club 8pm 030ab
    pov "See? [bs] was wrong. You're my only girl."
    irina "Yes. I'm sorry that I was unsure. You're my personal animal. <giggle>"
    bs "You can't be serious? He tricked you! I know it."
    irina "You're wrong [bs]. Just admit it."
    bs "No! I have to save you!"
    scene town club 8pm 031ab
    irina "Huh?"
    pov "Wow."
    bs "He's still a pig like all men. I need to prove to you that I'm better then him."
    irina "[bs]?"
    bs "<kiss> <kiss>"
    pov "{i}Hmm... Is [bs] such a bad looser or is she unable to share \"her\" friend with me?{/i}"
    pov "{i}But this lesbian kissing is damn hot.{/i}"
    scene town club 8pm 032ab
    "You hold them two close to you, enjoying the view of them kissing each other."
    irina "Hmm... but [pov] is here..."
    bs "<kiss> I don't care..."
    pov "Don't mind me. Enjoy yourself!"
    pov "{i}Oh my god.{/i}"
    irina "<kiss> Oh, [bs]."
    "While you hold them close by their asses you wonder how far [bs] would go to protect [irina] from you."
    "You're stunned by the idea of a threesome with them, imaging their tongues working on your dick."
    "And you're also damn lucky that [bs] is so drunk. She'll kill you when she finds out what she did."
    $ bigsiscorruption += 1
    $ irinacorruption += 2
    scene black
    "After some time [bs] is feeling bad and [irina] took her home."
    $ dtime += 1
    $ club8pmfirst = True
    jump town

label club20threeabort:
    scene town club 8pm 027ba
    irina "No, I don't want to see this. I'm out!"
    bs "Wait [irina]!"
    irina "No..."
    pov "{i}Damn, she's really going! But I don't want [bs] to stop now!{/i}"
    pov "{i}I need to show her that she's right. And I'm a dumb pig that only want to fuck her, haha.{/i}"
    bs "[irina]!"
    scene town club 8pm 027aa
    bs "Damn, that wasn't planned."
    "[bs] try's to get away but you hold her."
    pov "{i}No, no. We're not done now! First teasing and then you want to leave your pig? not happening, haha.{/i}"
    pov "{i}It's time to have my fun with her! She can't blame me after she started this thing.{/i}"
    jump club20bsproof

label club20bsproof:
    call screen club20bsproof1

screen club20bsproof1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1208 ypos 783 action (Hide('club20bsproof1'), Jump('club20bsass')) hovered tt.Action ("Play with her ass [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1208 ypos 270 action (Hide('club20bsproof1'), Jump('club20bskiss')) hovered tt.Action ("Get her close to you [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label club20bsass:
    scene town club 8pm 028aa
    bs "What're you doing?"
    pov "You're right [bs]. I'm just a pig and I'll have fun with you now!"
    bs "You can't be serious!"
    if bigsiscorruption >= 20:
        pov "Oh yes I am. You started this now enjoy the consequences!"
        "She starts to struggle but you hold her tight so she can't free herself."
        pov "Are you such a bad looser?"
        pov "I know you did this to prove some thing. You just want to get naughty!"
        bs "What...? No..."
        $ club20extendedcascorfirst = True
        jump club20bsass2
    else:
        scene town club 8pm 027cc
        bs "Stay away from me you freak!"
        pov "{i}Damn, she's not corrupted enough!{/i}"
        bs "[irina] is gone. It would be useless now."
        scene black
        "[bs] left the club too."
        $ dtime += 1
        $ club8pmfirst = True
        jump town

label club20bsass2:
    scene town club 8pm 029aa
    " You hold her and start pumping on her ass."
    "She doesn't struggle anymore and endures it."
    bs "Hnng..."
    pov "I knew it! You're just horny and want to get used by a \"pig\"."
    bs "N... no... hmm..."
    pov "Suppressing your moans? Haha."
    pov "But you're right from the start. You know me too well."
    bs "Hng... hng..."
    if inc == True:
        pov "I like my big sis so naughty!"
    else:
        pov "I like you so naughty!"
    bs "I'm not... You're just taking advantage of me because I'm drunk."
    "You start to pound her harder."
    bs "No stop it, that's enough!"
    if bigsiscorruption >= 40:
        pov "Haha, no! We've just started."
        scene town club 8pm 030aa
        pov "Let me treat you properly!"
        bs "Hah... hah... don't!"
        pov "Stop suppressing your moans. You're enjoying it too much, aren't you?"
        bs "No... hah... hah..."
        pov "I bet you only got drunk because you hoped \"the pig\" would take advantage of you!"
        pov "You want to get treated this way, because your boyfriend is a looser!"
        bs "Hah... Hnng..."
        pov "No talking back? Good slut!"
        "She starts grinding her ass on your dick."
        pov "Want to feel my big dick deep inside you? Don't deny it!"
        bs "Hnng..."
        pov "{i}Too bad that she's drunk. I hope she won't pass out.{/i}"
        scene town club 8pm 031aa
        bs "Hah... what... are..."
        pov "As I thought. You're damn wet!"
        bs "D... hng... don't..."
        pov "You're getting all wet, thinking of me taking you like the slut you are."
        bs "I'm not... hah..."
        "You rub her through her wet thong."
        bs "Hng...hah... like a slut..."
        pov "Yes, no denying anymore. We both know the truth."
        bs "I'm... hah... a slut..."
        pov "No, you're my slut!"
        bs "Hngg... hah your slut..."
        pov "Yes and my slut gets a good treatment!"
        bs "Oh... hah... oh god..."
        pov "Yes, cum for me, slut!"
        scene town club 8pm 032aa
        bs "Hnngg... Damn..."
        pov "Let it go!"
        bs "Hah... hah..."
        pov "Damn, cumming for me in public. You really want to be my slut."
        bs "Hng... hah... hah..."
        pov "{i}Time to let her go.{/i}"
        $ club20extendedcascorsecond = True
        jump club20bsstop
    else:
        jump club20bsstop


label club20bsstop:
    scene town club 8pm 040
    "You let her go."
    "You see how she realizes what happened."
    bs "Hah... hah..."
    pov "I like you're proving things."
    bs "Hah... fuck you..."
    pov "Hahaha, you can't deny that you enjoyed it."
    bs "I didn't!"
    pov "{i}What a bad liar she is.{/i}"
    scene black
    "She's leaving the club with her knees shaking."
    $ bigsiscorruption += 1
    $ dtime += 1
    $ club8pmfirst = True
    jump town


label club20bskiss:
    scene town club 8pm 028ba
    bs "What are you doing?"
    pov "You're right [bs]. I'm just a pig and I'll have fun with you now!"
    bs "You can't be serious!"
    if bigsiscorruption >= 20:
        pov "Oh yes I am. You started this now enjoy the consequences!"
        "She starts to struggle but you hold her tight so that she can't free herself."
        pov "Are you such a bad looser?"
        pov "I know you didn't this just to prove some thing. You want to get naughty!"
        bs "What...? No..."
        jump club20bskiss2
    else:
        scene town club 8pm 027cc
        bs "Stay away from me you freak!"
        pov "{i}Damn, she's not corrupted enough!{/i}"
        bs "[irina] is gone. It would be useless now."
        scene black
        "[bs] left the club too."
        $ dtime += 1
        $ club8pmfirst = True
        jump town

label club20bskiss2:
    scene town club 8pm 029ba
    "You hold her close and kiss her."
    bs "Huh?"
    pov "<kiss>"
    "She trys to get herself free, but you keep holding her tight."
    bs "You can't... hmm... be serious... <kiss>"
    scene town club 8pm 030ba
    pov "I knew it! You're just horny and want to get used by a \"pig\"."
    bs "N... no... you kissed me!"
    pov "Yes! But you were right from the start. You know me too well."
    if inc == True:
        bs "You're my brother. You kissed me!"
        pov "Yes, because my big sis is so naughty!"
    else:
        bs "You kissed me!"
        pov "Yes, because you're so naughty!"
    bs "I'm not... You're just taking advantage of me because I'm drunk."
    pov "Yes I am. Let's kiss more! I know you want it too!"
    bs "No stop it, that's enough!"
    if bigsiscorruption >= 40:
        pov "Haha, no! We've just started."
        scene town club 8pm 031ba
        bs "But... <kiss>"
        "You french kiss her and her tongue plays with yours."
        pov "No denying anymore. I see you need it too."
        bs "Hah... <lick> <kiss>"
        pov "You tast so good... hm..."
        bs "Hmm..."
        pov "You only get drunk to make out with your \"pig\", don't you?"
        bs "Hnn... no... I had... <kiss> to prove..."
        pov "Nice try. But now you're kissing me wildly."
        bs "You started... hmm..."
        pov "{i}Hm... Who thought you liked kissing so much. She can't stop.{/i}"
        pov "Your boyfriend doesn't take advantage of you, does he?"
        pov "You need to get treated properly from time to time."
        bs "Don't... hm... talk about... him..."
        pov "Then how about you stop holding back and show me what you want?"
        scene town club 8pm 032ba
        pov "Now you're honest finally."
        bs "Hmm... <kiss> tighter... hold... me..."
        "You hold her tighter."
        bs "Hnng... hah..."
        pov "Good, enjoy it more with me."
        "She kisses you even wilder."
        pov "You're my girl now!"
        bs "Hm... <kiss>"
        pov "Say it! You want it too."
        bs "Hm... hah... I'm... I'm..."
        bs "<kiss> your... hmm... girl now."
        pov "Yes you're my girlfriend now."
        bs "Hah... <kiss> <lick>."
        pov "{i}What a shame that she won't remember anything about this tomorrow.{/i}"
        pov "{i}But I'm sure she's showing her honest side when she's drunk.{/i}"
        pov "We'll make out every day."
        bs "Hmm... I'd like... hah... that..."
        pov "{i}Damn she's starting to taste weird. We need to stop or she'll loose the alcohol another way.{/i}"
        pov "Let's stop, my lover. We'll have other chances."
        bs "But... hm... <kiss>..."
        "You separate from her."
        jump club20bsstop
    else:
        jump club20bsstop


label club20prooflove:
    scene town club 8pm 025b
    pov "No [bs], [irina] is right."
    pov "You're to drunk, you'll do something you'll regret later."
    irina "Good, you're with me!"
    bs "Wha...?"
    scene town club 8pm 026b
    bs "You can't be serious!"
    irina "Yes we are. It's all for the best, trust us."
    pov "{i}Haha, handle her with care, like she's retarded.{/i}"
    bs "But... what are you doing?"
    irina "Taking care of my drunk friend."
    scene town club 8pm 027b
    bs "I'm not drunk, you damn cunt!"
    pov "{i}Haha, oh shit.{/i}"
    irina "Just ignore her, It's always the same when she's too drunk."
    bs "You're wrong. I must unmask this pig!"
    irina "I think it's better if we carry her home now."
    bs "No I won't go home! I have something to do!"
    pov "Yes, you're right [irina]."
    bs "No! Don't touch me!"
    scene town club 8pm 028b
    bs "Let me go you damn freaks!"
    irina "You're doing good [pov]. Just ignore her."
    pov "Won't people get suspicious?"
    irina "Ha, she's known for it."
    bs "I'll kill you, asshole!"
    irina "But it's good that you're helping me, doing it alone is very hard sometimes."
    pov "{i}So [bs] has a drinking problem?{/i}"
    scene black
    "After some time you manage to take her home."
    scene town club 8pm 029b
    bs "Leave me alone. <sob>"
    irina "Come on, don't be mad. We did this only for you."
    bs "But I did nothing wrong."
    pov "{i}Oh, now she's feeling guilty.{/i}"
    irina "Calm down. We're not mad at you, you're just drunk."
    bs "But... <sob>"
    scene town club 8pm 030b
    irina "I'm glad I had you with me. Don't worry [bs] it's fine."
    pov "Ok..."
    irina "And that you stay calm after [bs] ruined our dance."
    pov "Oh no problem."
    irina "It would be great if we could repeat it some time."
    irina "Without our drunkard <giggle>"
    pov "Yes, we can do that."
    irina "But know you earned your reward."
    scene town club 8pm 031b
    irina "<kiss>"
    pov "Hmm..."
    bs "Huh?"
    irina "My... <kiss> gentleman."
    "[irina] gives you a long sensual kiss."
    scene town club 8pm 032b
    irina "This was a good one <giggle>"
    bs "What...?"
    pov "Nice. Now I have a good reason to earn more rewards, haha."
    irina "Oh yes, you will <giggle>"
    bs "I... too..."
    scene town club 8pm 033b
    bs "<kiss>"
    irina "Ohh...?"
    pov "{i}Wait, what...?{/i}"
    "[bs] gives you a long sensual kiss."
    scene town club 8pm 034b
    irina "Haha, wow. What a fast opinion-change!"
    bs "What? But you rewarded him too."
    irina "Yes, because I like him. But you were sure he was just a \"pig\"."
    bs "But he isn't. He carried me home."
    pov "{i}What weird situations alcohol creates.{/i}"
    irina "But I'm not mad at you, my drunk girl, haha."
    scene town club 8pm 035b
    irina "You aren't mad at her, are you?"
    irina "Getting two rewards."
    pov "Haha, no!"
    bs "I... just want to... thank..."
    pov "Calm down [bs], everything is fine."
    irina "It's time to drag her to bed. I can't wait to meet you again [pov]."
    pov "Me neither."
    scene black
    "[irina] drags [bs] into her room."
    $ irinalove += 1
    $ bigsislove += 1
    $ dtime += 1
    $ club8pmfirst = True
    jump frontdoor


label club9vivan:
    hide screen townl
    scene town club 9am 001
    "Bartender" "Hello there. You must be new in town."
    pov "Yes, I am. And now I'm checking new places here in town."
    "Bartender" "So you found this club. A good choice. Maybe I'll see you more often around?"
    pov "Haha, yes. It seems to be the only club in town."
    "Bartender" "Yes, haha. So everyone loves it."
    if vivianfirstmeet == False:
        "Bartender" "My name is..."
        $ vivian = renpy.input(_("Her name is...")) or _("Vivian")
    $ vivianfirstmeet = True
    vivian "And you are?"
    pov "My name is [pov]! Nice to meet you."
    vivian "But you aren't here just to talk with me?"
    pov "Haha, maybe? But something to drink would be nice too."
    vivian "Yes I'll send a waitress. You can choose where you want to sit, since there aren't many people here."
    pov "Okay, thank you."
    scene black
    "You walk over to the other side of the club to sit at a table where you have a good view over the place."
    scene town club 9am 002
    "Then you notice something."
    if inc == True:
        pov "{i}Is that mom?{/i}"
    else:
        pov "{i}Is that [mother]?{/i}"
    pov "{i}So she's working here in the mornings?{/i}"
    scene town club 9am 003
    pov "{i}Yes, she is. She's waving to me.{/i}"
    pov "{i}But it's good that I found her here. So I know where she is in the mornings.{/i}"
    scene town club 9am 004
    mom "Hello [pov], so you found your way into town?"
    if inc == True:
        pov "Hi mom. Yes and I found a good club here."
        pov "So my mom can me serve a coffee like at home, haha."
    else:
        pov "Hi mom. Yes and I found a good club here."
        pov "So my mom can me serve a coffee like at home, haha."
    mom "Hahaha..."
    pov "But it's a nice outfit you're wearing."
    mom "Oh, I'm happy you like it."
    scene town club 9am 004a
    pov "Wow!"
    mom "<giggle> I like it too."
    pov "{i}Interesting. Discreet but also somewhat sexy with those stockings. Much but not too much.{/i}"
    pov "Yes, you're looking really good in it."
    scene town club 9am 004
    mom "Thank you."
    mom "So you want a coffee?"
    pov "Actually I want something else before."
    mom "Huh?"
    $ vivianrelationship += 1
    jump club9momch

label club9momch:
    scene town club 9am 004
    call screen club9momch1

screen club9momch1():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 786 ypos 261 action (Hide('club9momch1'), Jump('club9momlove')) hovered tt.Action ("Greet her properly [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1277 ypos 261 action (Hide('club9momch1'), Jump('club9momcor')) hovered tt.Action ("Greet her properly [cr1]") focus_mask True
        frame:
            xalign .5
            text tt.value

label club9momlove:
    if inc == True:
        pov "Come here mom."
    else:
        pov "Come here [mother]."
    scene town club 9am 005b
    if vlroom8momhug > 0:
        mom "Oh another hug. <giggle>"
    else:
        mom "Oh a hug. That's nice."
    pov "You earned that."
    mom "That's so sweet of you, [pov]."
    if inc == True:
        pov "I know, mom."
    else:
        pov "I know, [mother]."
    mom "Haha, you won't let me go, will you?"
    if momlove > 10:
        scene town club 9am 006b
        pov "No, I'll hold you longer!"
        pov "I was away so long, I want to feel your closeness."
        mom "But we'll see each other so often now?"
        if inc == True:
            pov "It's nothing wrong when a son wants to hold his mother in his arms."
            mom "Oh this is the sweetest thing I ever heard. Then you can hold me longer."
            pov "Sometimes a hug is a good feeling, isn't it?"
            mom "Yes that's true, especially when no one else hugs me."
        else:
            pov "It's nothing wrong that I want to hold you in my arms when we know each other so long."
            mom "Oh this is the sweetest thing I ever heard. Then you can hold me longer."
            pov "Sometimes a hug is a good feeling, isn't it?"
            mom "Yes that's true, especially when no one else hugs me."
        mom "But now we should stop or I could get fired, hahaha."
    scene town club 9am 007b
    mom "Wow! That was really nice."
    pov "I'm glad you liked it."
    mom "You should come here everyday, so I can get more hugs, haha."
    if inc == True:
        pov "Haha, oh mom."
    else:
        pov "Haha, oh [mother]."
    pov "And I'll get my coffee now nevertheless?"
    mom "Oh sure. I'll bring it."
    $ momlove += 1
    jump club9momwalk

label club9momcor:
    if inc == True:
        pov "Come here mom."
    else:
        pov "Come here [mother]."
    scene town club 9am 005a
    with vpunch
    mom "Hah..."
    pov "Your hot ass needs to be slapped!"
    if momcorruption > 10:
        scene town club 9am 006a
        $ momcorruption += 1
        mom "Y... you slapped me in public..."
        pov "Yes! Because I'm a bad boy, remember?"
        pov "So I had to slap you and because I wanted to, haha."
        mom "..."
        pov "So how about you bring me a coffee now!"
        mom "O...okay..."
        $ club10slapfirst = True
        jump club9momwalk
    else:
        scene town club 9am 006ab
        mom "How dare you to slap me!"
        pov "{i}Oh shit...{/i}"
        mom "Are you out of your mind?"
        if inc == True:
            pov "But mom..."
        else:
            pov "But [mother]..."
        mom "No buts!"
        mom "It's better you leave now, you won't get anything from me!"
        pov "..."
        mom "Leave now!"
        pov "O... okay..."
        pov "{i}Damn, maybe she isn't corrupted enough.{/i}"
        $ dtime += 1
        $ club10amfirst = True
        jump club

label club9momwalk:
    scene town club 9am 008
    if inc == True:
        pov "{i}Damn that outfit is really hot. Mom as a waitress serving me, like a fantasy, haha.{/i}"
    else:
        pov "{i}Damn that outfit is really hot. [mother] as a waitress serving me, like a fantasy, haha.{/i}"
    pov "{i}And that guy sleeping on the table since I came in here. What a wasted guy.{/i}"
    if inc == True:
        pov "{i}I wonder if I can work here too? Together with mom.{/i}"
    else:
        pov "{i}I wonder if I can work here too? Together with her.{/i}"
    scene town club 9am 009
    mom "Here is your coffee, [pov]."
    if inc == True:
        pov "Thank you, mom."
    else:
        pov "Thank you, [mother]."
    mom "So what are you going to do with your day?"
    pov "Hmm..."
    mom "Time to find a job?"
    pov "Maybe I can work here too?"
    mom "Hmm... you could ask [vivian], she's responsible for the jobs here. And she's a good friend of mine so it could happen."
    pov "Oh, good to know."
    vivian "[mother]!"
    scene town club 9am 010
    mom "Hmm..."
    vivian "I have some work to do for you. Can you do it?"
    mom "Oh sure. Just a moment."
    vivian "Ok. But you better hurry."
    scene town club 9am 011
    mom "I have to work so we must delay our chat."
    pov "Haha, sure. I won't disturb you anymore."
    mom "See you later. And don't forget to look for a job."
    if inc == True:
        pov "Sure, mom."
    else:
        pov "Sure, [mother]."
    pov "{i}Hmm... maybe I should take my coffee and go. Sitting here alone is boring.{/i}"
    if momrelationship < 6 and momntr == True and NTR == True:
        jump club9hardntr
    else:
        $ momrelationship += 1
        $ dtime += 1
        $ club10amfirst = True
        jump club

label club9hardntr:
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene town club 9am 012
    pov "{i}Hmm... wait, where's she going so fast?{/i}"
    pov "{i}I didn't realize that upstairs is something too.{/i}"
    scene town club 9am 013
    pov "{i}There she is. But who's that guy?{/i}"
    if frankfirstmeet == True:
        pov "{i}Is that Frank? The guy from the tanning salon?{/i}"
    pov "{i}What are they talking about? Damn if I get closer they could see me.{/i}"
    scene town club 9am 014
    if inc == True:
        pov "{i}He's scolding mom? Did she do something wrong?{/i}"
    else:
        pov "{i}He's scolding her? Did she do something wrong?{/i}"
    pov "{i}She's standing there obedient and listening to him. If I could hear what he's say. Damn!{/i}"
    scene town club 9am 015
    pov "{i}What the hell? Is he about to spank her?{/i}"
    if inc == True:
        pov "{i}That ass hole is about to spank my mom! And she bent over obedient. What did she do wrong?{/i}"
    else:
        pov "{i}That ass hole is about to spank her! And she bent over obedient. What did she do wrong?{/i}"
    scene town club 9am 016
    mom "Hnng... hah..."
    pov "{i}He's hitting her so hard that even I can hear her screaming! Why isn't [vivian] interfering?{/i}"
    mom "HAH..."
    pov "{i}Even harder... you bastard!{/i}"
    pov "{i}But I can't do anything until I know what happened. I don't won't to get her into bigger trouble.{/i}"
    scene town club 9am 017
    pov "{i}Oh, they're done. Damn, did she forget her panties? It looks like she isn't wearing any.{/i}"
    pov "{i}And now she's standing like a slave before him. Why is this happening? And how often?{/i}"
    pov "{i}I must find out what the reason was. I must help her to get away from that asshole.{/i}"
    scene town club 9am 018
    pov "{i}Good. It's over now. Now I have to wait for her so I can ask her.{/i}"
    pov "{i}And that asshole sitting there and enjoy his power over her.{/i}"
    if inc == True:
        pov "{i}Spanked my mom hard in public!{/i}"
    else:
        pov "{i}Spanked [mother] hard in public!{/i}"
    "You wait for half an hour but you still can't see her."
    pov "{i}Damn, is she gone? Maybe there is another exit.{/i}"
    pov "{i}So I should waste time here and search for her instead.{/i}"
    $ vipntrfrank = True
    $ dtime += 1
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    $ club10amfirst = True
    jump club
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
