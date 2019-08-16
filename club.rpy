#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 7pm Club - Cassandra, Kate, Irina, Martin, MC, Vivian - Love, Corruption
# 2. 8pm Club - Cassandra, Irina, MC - Love, Corruption
# 3. 9am Club - Frank, MC, Nicole, Vivian - Love, Corruption, Darker Paths
#----- End List -----

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
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('club19ik2'), Jump('club19iklookbelly1')) hovered tt.Action ("Look at belly") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('club19ik2'), Jump('club19iklookbelly2')) hovered tt.Action ("Look at belly") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('club19ik2'), Jump('club19iklookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('club19ik2'), Jump('club19iktalk')) hovered tt.Action ("Talk") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club19iklookbelly1:
    scene town club 7pm 002a
    povi "She has such a toned body... and some amazing tits!"
    jump club19ik1

label club19iklookbelly2:
    scene town club 7pm 003a
    povi "What a sexy view. That dress is killing me."
    jump club19ik1

label club19iklookcrotch:
    scene town club 7pm 004a
    povi "What a sexy dress. Showing off so much but covering up just the right spots. I don't think she's wearing panties..."
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
    pov "I wanted to check out the night life in this town."
    irina "Oh, I'm usually here with [bs], trying to find some fun."
    pov "I'm glad you chose that dress again."
    irina "<giggle>"
    $ irinarelationship += 1
    if vivianfirstmeet == True:
        $ vivianrelationship += 1
    jump club19ikgreet

label club19ikgreet:
    scene town club 7pm 006a
    call screen club19ikgreet1

screen club19ikgreet1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('club19greet1'), Jump('club19iklove')) hovered tt.Action ("Greet her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('club19greet1'), Jump('club19ikcor')) hovered tt.Action ("Greet her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club19ikcor:
    scene town club 7pm 007a
    "You grope her ass."
    irina "Huh..."
    pov "This is what you wanted right? You want to show off and get my attention or are you just teasing me?"
    irina "Hmm..."
    pov "That's how I like it. Firm but still soft and wrapped in a sexy dress."
    scene town club 7pm 008a
    irina "Hmm..."
    pov "So I was right. You do want my attention."
    irina "..."
    pov "Then it's good that I'm here now, so we can have some fun together, don't you think?"
    irina "Y... yes, sure."
    scene town club 7pm 011a
    if vivianfirstmeet == False:
        "Bartender" "You're really a weird couple."
    else:
        vivian "You're really a weird couple."
    pov "Oh we aren't together. Yet!"
    scene town club 7pm 012a
    irina "<giggle>"
    pov "But I don't think it will take long until she's my girl!"
    irina "With a cute boyfriend <giggle>"
    pov "Cute and demanding!"
    irina "<giggle>"
    pov "Let's go!"
    $ irinacorruption += 1
    $ dtime += 1
    jump club

label club19iklove:
    scene town club 7pm 009a
    pov "Come here!"
    irina "Ohh..."
    pov "Only hugs are good enough for a nice girl like you."
    irina "<giggle> I could get used to that."
    pov "Haha, oh you will around me. I'm definitely a hugger."
    povi "At least when beautiful women are involved..."
    scene town club 7pm 010a
    irina "It's so good to see you again [pov]."
    pov "That's the same thing I would say!"
    irina "Ohh... <giggle>"
    pov "So how about we hang out together?"
    irina "I'd love that very much!"
    scene town club 7pm 011a
    if vivianfirstmeet == False:
        "Bartender" "You're really a weird couple."
    else:
        vivian "You're really a weird couple."
    pov "Oh, we aren't together. But maybe if I'm very lucky, this beautiful girl will have me one day."
    scene town club 7pm 012a
    irina "Oh my god. You're so cute."
    pov "Oh I can be anything you want me to be, haha."
    irina "I'm glad to hear that. You're nice and... surprising."
    pov "So how about we take a look around?"
    irina "Yes, please."
    $ irinalove += 1
    $ dtime += 1
    jump club

label club19kate:
    hide screen townl
    scene town club 7pm 001b
    "You get closer to the girl dancing."
    "She's really showing off her... dancing skills."
    povi "Nice outfit too."
    scene town club 7pm 002b
    povi "Wow! A really nice outfit. And those moves."
    povi "She's really fit and agile."
    jump club19katech

label club19katech:
    scene town club 7pm 002b
    call screen club19katech1

screen club19katech1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('club19katech1'), Jump('club19katelove')) hovered tt.Action ("Dance with her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('club19katech1'), Jump('club19katecor')) hovered tt.Action ("Dance with her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('club19katech1'), Jump('club19chl')) hovered tt.Action ("Leave her alone") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club19katecor:
    scene town club 7pm 003b
    "You decide to dance with her, pressing her onto you."
    povi "Wow, that hot ass is really grinding on my dick."
    povi "She's so toned and slender. Very hot."
    "The girl is lost in her dancing."
    scene town club 7pm 004b
    "Girl" "Aaahh..."
    povi "Oh, the wild horse woke up! Let's see if I can tame her."
    "Girl" "What...? No!"
    povi "Grinding her ass all the time on me and now she's acting surprised? Please, slut!"
    scene town club 7pm 005b
    "Girl" "What the hell are you doing?"
    pov "Hmm... Dancing with you?"
    "Girl" "Dancing? You were groping me and rubbing yourself on me!"
    pov "I thought that was point of that kind of dancing. You needed a partner!"
    "Girl" "Are you serious? What the fuck is wrong with you?"
    pov "Nothing! Just dancing with a sexy girl."
    scene town club 7pm 006b
    "Girl" "Fuck you! Don't you dare touch me like that again."
    povi "Still playing innocent after such a hot show. I know she liked it."
    povi "She's just playing hard to get."
    if katefirstmeet == False:
        "You head back to the bar to regroup."
        scene town club 7pm 011a
        if vivianfirstmeet == True:
            pov "Hey [vivian]! What's that girl's name dancing out there?"
            vivian "Oh yeah, that's...."
        else:
            pov "Hey [vivian]! What's that girl's name dancing out there?"
            "Bartender" "Oh yeah, that's...."
        $ katename = renpy.input(_("Her name is...")) or _("Kate")
        $ katename = katename.strip()
        if katename == "":
            $ katename = "Kate"
        $ katefirstmeet = True
        povi "Hmm, [kate] huh? I like that."
        $ katefirstmeet = True
    $ katecorruption += 1
    $ dtime += 1
    jump club

label club19katelove:
    scene town club 7pm 007b
    "You decide to dance behind her."
    povi "Oh my god. What a beautiful body she has. And these moves!"
    povi "I wonder why this beauty is dancing all alone? I hope she not a lesbian."
    "You're caught up in her moves."
    scene town club 7pm 008b
    "Girl" "Huh?"
    povi "Oh, she noticed me."
    pov "Hi!"
    "Girl" "..."
    scene town club 7pm 009b
    povi "Shit! That outfit is killing me. Is it supposed to be worn so low?"
    "Girl" "Hi there. Look at you sneaking up on me like that..."
    pov "Oh, I didn't mean to scare you. I just didn't want to interrupt your dancing."
    "Girl" "Oh, it's okay."
    pov "Let me start over. I'm [pov]. I'm the guy that was frozen behind you, completely mesmerized by your dance moves."
    "Girl" "Haha, so is that your best pick up line?"
    pov "No! I just never met a girl that could dance like that before."
    scene town club 7pm 010b
    "Girl" "Well, you seem nice enough... I guess I can tell you my name."
    "Girl" "But don't waste too much of your time, I already have a boyfriend."
    if katefirstmeet == False:
        $ katename = renpy.input(_("Her name is...")) or _("Kate")
        $ katename = katename.strip()
        if katename == "":
            $ katename = "Kate"
    $ katefirstmeet = True
    kate "He's over there. The DJ of the club."
    scene town club 7pm 011b
    povi "Damn, some guys have all the luck!"
    povi "He doesn't seem to stand out really. Maybe he's rich or the owner of the club?"
    kate "Are you still here with me?"
    pov "Oh yes, sorry. Nice to meet you [kate]."
    kate "Nice to meet you too [pov]. But I think I'm going to keep dancing."
    kate "Alone this time! Haha"
    povi "Hmmm... I'm going to have to see what I can do about getting her to like me more."
    $ katelove += 1
    $ katerelationship += 1
    $ dtime += 1
    jump club

label club19bs:
    hide screen townl
    scene town club 7pm 001c
    povi "There is [bs] with her boyfriend."
    jump club19bslook

label club19bslook:
    scene town club 7pm 001c
    call screen club19bslook1

screen club19bslook1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('club19bslook1'), Jump('club19bslooktits')) hovered tt.Action ("Look at tits") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('club19bslook1'), Jump('club19bslookcrotch')) hovered tt.Action ("Look at crotch") focus_mask True
        imagebutton auto "gui/icons/icon_talk_%s.png" action (Hide('club19bslook1'), Jump('club19bstalk')) hovered tt.Action ("Talk") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club19bslooktits:
    scene town club 7pm 002c
    povi "Now I have a chance to take a good look at that dress, so much skin showing."
    jump club19bslook

label club19bslookcrotch:
    scene town club 7pm 003c
    povi "What a hot view. And those boots make the outfit even sexier."
    jump club19bslook

label club19bstalk:
    scene town club 7pm 004c
    pov "Hey there!"
    martin "Oh hey [pov]. What you're doing here?"
    bs "Oh... hi..."
    if inc == True:
        povi "Oh sis, fiesty as ever. But that dress is killing me."
    else:
        povi "Oh [bs], fiesty as ever. But that dress is killing me."
    pov "Just checking out the night life here."
    martin "Not much going on really. Most people around here don't have the money to go out often."
    pov "Oh... so only a few people party at a place like this."
    martin "Yes and mostly the same ones."
    povi "Haha, [bs] is glaring at me. Maybe she wants to be alone with Martin."
    jump club19bsch

label club19bsch:
    scene town club 7pm 004c
    call screen club19bsch1

screen club19bsch1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('club19bsch1'), Jump('club19bslove')) hovered tt.Action ("Leave them alone [lv1]/[bs] [gd1]/Martin") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('club19bsch1'), Jump('club19bscor')) hovered tt.Action ("Blame Martin [cr1]/[bs] [bd1]/Martin") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
    povi "It's too easy to mess with these guys, haha."
    pov "Hey Martin, there is a girl outside asking for you."
    scene town club 7pm 005c
    martin "What...?"
    bs "What?"
    pov "Yeah she said she can't wait to feel your cock inside her again."
    martin "No way!"
    scene town club 7pm 006c
    bs "What the fuck Martin?! You're cock inside her again?! Really?!"
    martin "I don't know any girls like that..."
    martin "[pov] must be mistaken!"
    pov "But aren't you the singer from the band \"The Chosen\"?"
    scene town club 7pm 008c
    bs "Yes he is! I knew it! You're a damn cheater!"
    martin "What no! I told you before and there are no other girls."
    bs "Why would [pov] make something like that up?"
    povi "Hahaha, just wunderful."
    scene town club 7pm 009c
    bs "Stay away from me you asshole!"
    bs "Don't you dare call me until you can prove that you're right!"
    martin "But [bs], you have to believe me!"
    bs "No! I knew you couldn't keep your hands off of your groupies!"
    bs "Fuck you! I'm staying with [irina]."
    scene town club 7pm 010c
    if inc == True:
        martin "I don't get it! I never betrayed your sister."
    else:
        martin "I don't get it! I never betrayed her."
    martin "The girl must be crazy to say something like that."
    pov "No she didn't."
    martin "How do you know?"
    pov "There was no girl. I lied!"
    martin "What...? Why did you do that? I thought we were getting along?"
    povi "What the fuck? Is he serious?"
    scene town club 7pm 011c
    martin "What have I ever done to you?"
    if inc == True:
        pov "It's easy. I don't like you and I think my big sister deserve someone better."
    else:
        pov "It's easy. I don't like you and I think she deserve someone better."
    pov "And also you're an emo-freak that she already believes cheats on her! Where there is smoke there is likely fire bro."
    martin "She was right from the start, you really are evil."
    pov "Maybe..."
    martin "I'll prove what you did and then I'll get her back."
    pov "Well it wouldn't be fun if you didn't at least try!"
    $ bigsiscorruption += 1
    $ bigsisrelationship += 1
    $ martinbad += 1
    $ dtime += 1
    jump club20maway

label club20maway:
    scene town club 8pm 001
    povi "What's [bs] now up to?"
    povi "I should go over to them and see what they're doing."
    scene town club 8pm 002
    if vivianfirstmeet == True:
        vivian "Are you sure?"
    else:
        "Barkeeper" "Are you sure?"
    bs "Oh yes! I need something to drink! [irina] will take care of me later!"
    if vivianfirstmeet == True:
        vivian "So your boyfriend was an asshole again?"
    else:
        "Barkeeper" "So your boyfriend was an asshole again?"
    bs "You have no idea!"
    if vivianfirstmeet == True:
        vivian "Ok. If you know what you're doing."
    else:
        "Barkeeper" "Ok. If you know what you're doing."
    scene town club 8pm 003
    bs "Men! We don't need them, they're all pigs!"
    irina "Haha."
    bs "You know it's true. Drink with me, my friend!"
    irina "Cheers!"
    scene town club 8pm 004
    povi "Wait! I lied to get rid of Martin, setting him up as the bad guy and they're the one's getting drunk?"
    bs "<gulp> <gulp>"
    irina "<gulp> <gulp>"
    povi "Wow they can really drink!"
    povi "It doesn't seem like this is a new thing... Maybe Martin isn't the nice guy he claims to be anyway."
    scene town club 8pm 005
    irina "Hah..."
    bs "So good!"
    irina "More?"
    bs "Oh yes!"
    povi "Damn. Are they used to this hard stuff? They are drinking it like water."
    bs "Let's get this over with!"
    scene town club 8pm 006
    irina "Oh... Hi!"
    povi "Wow that took a while to notice me."
    bs "<gulp> <gulp>"
    irina "..."
    pov "..."
    irina "..."
    povi "She's just staring at me. What's she up to?"
    scene town club 8pm 007
    bs "Oh... Why did you stop drinking?"
    irina "He... he's just standing there... looking at us."
    pov "Is that wrong?"
    irina "You just being so polite by waiting."
    povi "What? She's serious? What else should I do, rape them? Are all guys here jerks?"
    bs "He just wants to perv on us! I know him better then you, trust me."
    irina "I'm not sure! I think I'll give him a chance."
    scene town club 8pm 008
    bs "You must be kidding. He's a pig like all the others. We should stay together."
    irina "I think you're wrong this time! I have a good feeling about him."
    povi "Oh, she seems attracted to me. Hopefully it's not just the booze."
    bs "I warn you. He'll abuse you too."
    irina "Haha, relax [bs]. Sometimes you get so angry you don't think straight. I'm a big girl you know."
    scene town club 8pm 009
    bs "Fine! Do whatever you want! I'll drink on my own!"
    irina "Hi again!"
    povi "Haha, ok she's definitely a little drunk."
    pov "Hi [irina]."
    irina "You... you wanna dance with me, maybe?"
    jump club20idance

label club20idance:
    call screen club20idance1

screen club20idance1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('club20idance1'), Jump('club20idanceyes')) hovered tt.Action ("Dance with her [lv1]/[cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('club20idance1'), Jump('club20abort')) hovered tt.Action ("Leave them alone") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club20abort:
    scene town club 8pm 009
    povi "I don't wanna stay with them while they're getting drunk."
    pov "No sorry, [irina]. I've got to do something else."
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
    irina "Yes! You want to dance with me! Let's go."
    bs "<gulp> <gulp>"
    irina "You won't regret it!"
    scene town club 8pm 011
    irina "I'm so happy that you're dancing with me."
    pov "Me too. Dancing with a beautiful girl!"
    irina "<giggle>"
    pov "Do you two often get drunk when you here in the club?"
    if inc == True:
        irina "Haha, no! Only when your sister is having one of her \"moments\"."
    else:
        irina "Haha, no! Only when [pov] is having one of her \"moments\"."
    povi "I wonder how often that happens?"
    irina "But we should watch out for her. She gets weird when she drinks too much booze, <giggle>."
    pov "Oh. And what about you?"
    irina "I'm not weird, haha."
    irina "Haha, look at her!"
    scene town club 8pm 012
    "[bs] dances drunk alone."
    pov "Oh, you're right."
    scene town club 8pm 013
    pov "And she's still drinking more."
    irina "She can be embarrassing sometimes, <giggle>."
    pov "I don't care as long as I get to stay with you."
    scene town club 8pm 014
    pov "Come here!"
    irina "I'd love to!"
    jump club20idancech

label club20idancech:
    call screen club20idancech1

screen club20idancech1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('club20idancech1'), Jump('club20idancelove')) hovered tt.Action ("Dance romantic with her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('club20idancech1'), Jump('club20idancecor')) hovered tt.Action ("Dance sexy with her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club20idancecor:
    irina "Huh?"
    scene town club 8pm 014a
    pov "Let me see how sexy you can dance!"
    "You press her ass on your crotch."
    irina "Hmm..."
    pov "Go on. You'll love it too."
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
    irina "What girl could withstand a gentleman like you, <giggle>?"
    pov "I'm just lucky that you're such a beauty!"
    irina "And that you're worth staring at all the time."
    scene town club 8pm 016
    irina "It's like you drugged me, you know?"
    pov "That's not what I would call it."
    irina "You know what I mean! <giggle>"
    pov "Yes. And I like it, haha."
    irina "Just hold me more please."
    pov "Always."
    irina "<giggle>"
    if irinalove >= 20:
        irina "I'm sorry. I can't wait any longer."
        scene town club 8pm 017
        irina "Hmm..."
        povi "Wow. What a nice surprise."
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
    povi "Oh shit. She's seriously drunk!"
    scene town club 8pm 019
    bs "What are you doing? Being a slut for this pig?"
    irina "Calm down [bs]! You're drunk."
    povi "Wow she really does get weird while she's drunk."
    povi "But not much more than usual, haha."
    scene town club 8pm 020
    bs "I'll proove it! He's just a pig like the others."
    irina "What? Sorry. I'm not sure what she's up to?"
    pov "Relax [irina]."
    scene town club 8pm 021
    bs "He just wants to fuck a pussy. It doesn't matter which girl owns it."
    irina "[bs]?"
    bs "I'll show you. Like all other pigs he'll forget about you in no time."
    povi "Can this get more weird?"
    scene town club 8pm 022
    bs "You're hard aren't you? Thinking about fucking my naive friend."
    povi "Shit. She's groping my crotch. Is this a dream?"
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
    povi "I still can't believe this."
    bs "His dick's aching for attention. I feel it."
    scene town club 8pm 024
    irina "You have to stop it. You're too drunk."
    bs "But I only want to help you. You need to see the proof."
    irina "No, it's wrong!"
    povi "Wow. What should I do? Let [irina] stop her or have my fun with [bs] trying to get her proof?"
    povi "I shouldn't be the bad guy here since [bs] started it this time, even if she's drunk."
    jump club20proof

label club20proof:
    call screen club20proof1

screen club20proof1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('club20proof1'), Jump('club20prooflove')) hovered tt.Action ("Let [irina] stop her [lv1]/[irina] [lv1]/[bs]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('club20proof1'), Jump('club20proofcor')) hovered tt.Action ("Let [bs] continue [cr1]/[irina] [cr1]/[bs]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club20proofcor:
    scene town club 8pm 025a
    pov "Calm down [irina]. I want to see if [bs] can prove it."
    irina "Huh?"
    pov "I'm sure she's all talk!"
    bs "Hah, you want to challenge me?"
    irina "But..."
    povi "Hah, this should be fun."
    scene town club 8pm 026a
    bs "Trust me and I'll show you that I'm right."
    povi "How lucky is this turn of events. Having her so close to me all the suddenly."
    irina "But... stop..."
    bs "This will be short. His dick is already poking against my crotch. I bet he wants to fuck me right now!"
    irina "Please stop [bs]. I don't want to see this!"
    bs "Calm down! I need to prove it."
    irina "Stop it or I'll leave! You shouldn't do this, you're my friend!"
    povi "No! Don't stop now. Stay strong [bs]!"
    if irinacorruption >= 30:
        povi "Oh, I just had another idea."
        $ club20extendedirinacor = True
        jump club20three
    jump club20threeabort

label club20three:
    call screen club20three1

screen club20three1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('club20three1'), Jump('club20threeabort')) hovered tt.Action ("Let her go") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('club20three1'), Jump('club20threeyes')) hovered tt.Action ("Have her to stay [cr1]/[irina]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club20threeyes:
    scene town club 8pm 027ab
    pov "Stay here with us [irina]. And I'll prove to you that [bs] is wrong."
    pov "You're the girl I'm after."
    "You also grab [bs] ass and hold her close to provoke her."
    povi "Damn this should get even better."
    pov "Come here!"
    bs "I won't lose! Pig!"
    scene town club 8pm 028ab
    irina "Hmm..."
    bs "What...?"
    "You pull [irina] to you and kiss her. [bs] is staying surprisingly close to you."
    povi "Wow, I'm holding them both by their asses, and not one complain."
    povi "Playing that joke on Martin was the best idea."
    irina "Hm... <kiss>"
    scene town club 8pm 029ab
    povi "Wow!"
    "[irina] is getting more turned on and gives you a french kiss."
    bs "But..."
    pov "You're... <kiss> a good girl."
    irina "Y... yes <kiss> I am YOUR good girl."
    povi "Haha, what a great win/win. I'm groping two hot girls and getting rewarded!"
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
    povi "Hmm... Is [bs] such a poor loser or is she unable to share \"her\" friend with me?"
    povi "But watching them kiss is pretty damn hot."
    scene town club 8pm 032ab
    "You hold them both close to you, enjoying the view of them kissing each other."
    irina "Hmm... but [pov] is here..."
    bs "<kiss> I don't care..."
    pov "Don't mind me. Enjoy yourself!"
    povi "Oh my god."
    irina "<kiss> Oh, [bs]."
    "While you hold them close by their asses you wonder how far [bs] would go to protect [irina] from you."
    "You're get the idea of having a threesome with them, imaging their tongues working on your dick."
    "And you're also damn lucky that [bs] is so drunk. She'll kill you when she finds out what she did."
    $ bigsiscorruption += 1
    $ irinacorruption += 2
    scene black
    "After some time [bs] was feeling bad so [irina] took her home."
    $ dtime += 1
    $ club8pmfirst = True
    jump town

label club20threeabort:
    scene town club 8pm 027ba
    irina "No, I don't want to see this. I'm out!"
    bs "Wait [irina]!"
    irina "No..."
    povi "Damn, she's really going! But I don't want [bs] to stop now!"
    povi "I need to show her that she's right. And I'm a dumb pig that only wants to fuck her, haha."
    bs "[irina]!"
    scene town club 8pm 027aa
    bs "Damn, that didn't go like I had planned."
    "[bs] try's to get away but you hold her tight."
    povi "No, no. We're not done now! First teasing and then you want to leave your pig? That's not going to happen."
    povi "It's time to have my fun with her! She can't blame me after she started this."
    jump club20bsproof

label club20bsproof:
    call screen club20bsproof1

screen club20bsproof1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('club20bsproof1'), Jump('club20bsass')) hovered tt.Action ("Play with her ass [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('club20bsproof1'), Jump('club20bskiss')) hovered tt.Action ("Get her close to you [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club20bsass:
    scene town club 8pm 028aa
    bs "What're you doing?"
    pov "You're right [bs]. I'm just a pig and I'll have some fun with you now!"
    bs "You can't be serious!"
    if bigsiscorruption >= 20:
        pov "Oh yes I am. You started this, now enjoy the consequences!"
        "She starts to struggle but you hold her tight so she can't free herself."
        pov "Are you such a bad loser?"
        pov "I know you didn't do this to prove something. You just wanted to get naughty!"
        bs "What...? No..."
        $ club20extendedcascorfirst = True
        jump club20bsass2
    else:
        scene town club 8pm 027cc
        bs "Stay away from me you freak!"
        povi "Damn, she's not corrupted enough!"
        bs "[irina] is gone too now. It would be useless."
        scene black
        "[bs] leaves the club."
        $ dtime += 1
        $ club8pmfirst = True
        jump town

label club20bsass2:
    scene town club 8pm 029aa
    " You hold her and start pumping against her ass."
    "She doesn't struggle anymore and just let's it happen."
    bs "Hnng..."
    pov "I knew it! You're just horny and want to get used by a \"pig\"."
    bs "N... no... hmm..."
    pov "Suppressing your moans? Haha."
    pov "But you're right from the start. You know me too well."
    bs "Hng... hng..."
    if inc == True:
        pov "I like my big sis when sh'es so naughty!"
    else:
        pov "I like when you're so naughty!"
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
        pov "I bet you only got drunk because you hoped this \"pig\" would take advantage of you!"
        pov "You want to get treated this way, because your boyfriend is a loser!"
        bs "Hah... Hnng..."
        pov "No talking back? Good slut!"
        "She starts grinding her ass on your dick."
        pov "You want to feel my big dick deep inside you? Don't deny it!"
        bs "Hnng..."
        povi "Too bad that she's drunk. I hope she doesn't pass out anytime soon."
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
        pov "Yes and my slut gets a treated very well!"
        bs "Oh... hah... oh god..."
        pov "Yes, cum for me, slut!"
        scene town club 8pm 032aa
        bs "Hnngg... Damn..."
        pov "Let it go!"
        bs "Hah... hah..."
        pov "Damn, cumming for me in public. You really want to be my slut."
        bs "Hng... hah... hah..."
        povi "Time to let her go."
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
    if bigsislove or bigsiscorruption >= 40:
        bs "Hah... Of course you do..."
    else:
        bs "Hah... fuck you..."
    pov "Hahaha, you can't deny that you enjoyed it."
    if bigsislove or bigsiscorruption >= 40:
        bs "Maybe... Maybe not..."
    else:
        bs "I didn't!"
    povi "What a bad liar she is."
    scene black
    "She's leaving the club with her knees shaking."
    $ bigsiscorruption += 1
    $ dtime += 1
    $ club8pmfirst = True
    jump town

label club20bskiss:
    scene town club 8pm 028ba
    bs "What are you doing?"
    pov "You're right [bs]. I'm just a pig and I'll have some fun with you now!"
    bs "You can't be serious!"
    if bigsiscorruption >= 20:
        pov "Oh yes I am. You started this, now enjoy the consequences!"
        "She starts to struggle but you hold her tight so that she can't free herself."
        pov "Are you such a bad loser?"
        pov "I know you didn't do this just to prove something. You just wanted to get naughty!"
        bs "What...? No..."
        jump club20bskiss2
    else:
        scene town club 8pm 027cc
        bs "Stay away from me you freak!"
        povi "Damn, she's not corrupted enough!"
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
        pov "You taste so good... hm..."
        bs "Hmm..."
        pov "You only got drunk to make out with your \"pig\", don't you?"
        bs "Hnn... no... I had... <kiss> to prove..."
        pov "Nice try. But now you're kissing me wildly."
        bs "You started... hmm..."
        povi "Hm... Who thought you liked kissing so much. She can't stop."
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
        bs "Hah... yes! <kiss> <lick>."
        povi "What a shame that she probably won't remember anything about this tomorrow."
        povi "But I'm sure she's showing her honest side when she's drunk."
        pov "We'll make out every day."
        bs "Hmm... I'd like... hah... that..."
        povi "Damn she's starting to taste weird. We need to stop or she'll lose the alcohol another way."
        pov "Let's stop, my lover. We'll have other chances."
        bs "But... hm... <kiss>..."
        "You separate from her."
        jump club20bsstop
    else:
        jump club20bsstop

label club20prooflove:
    scene town club 8pm 025b
    pov "No [bs], [irina] is right."
    pov "You're too drunk, you'll do something you'll regret later."
    irina "Good, I'm glad you're with me!"
    bs "Wha...?"
    scene town club 8pm 026b
    bs "You can't be serious!"
    irina "Yes we are. It's all for the best, trust us."
    povi "Haha, handle her with care, like she's retarded."
    bs "But... what are you doing?"
    irina "Taking care of my drunk friend."
    scene town club 8pm 027b
    bs "I'm not drunk, you damn cunt!"
    povi "Haha, oh shit."
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
    povi "So [bs] has a drinking problem?"
    scene black
    "After some time you manage to take her home."
    scene town club 8pm 029b
    bs "Leave me alone. <sob>"
    irina "Come on, don't be mad. We only did this for you."
    bs "But I did nothing wrong."
    povi "Oh, now she's feeling guilty."
    irina "Calm down. We're not mad at you, you're just drunk."
    bs "But... <sob>"
    scene town club 8pm 030b
    irina "I'm glad I had you with me. Don't worry [bs] it's fine."
    pov "Ok..."
    irina "And thank you for staying calm after [bs] ruined our dance."
    pov "Oh, no problem."
    irina "It would be great if we could repeat it some time."
    irina "Without our drunkard <giggle>"
    pov "Yes, we should do that."
    irina "But you know you earned your reward right?"
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
    povi "Wait, what...?"
    "[bs] gives you a long sensual kiss."
    scene town club 8pm 034b
    irina "Haha, wow. What a fast opinion-change there [bs]!"
    bs "What? But you rewarded him too."
    irina "Yes, because I like him. But you were sure he was just a \"pig\"."
    bs "But he isn't. He carried me home."
    povi "What weird situations alcohol creates."
    irina "But I'm not mad at you, my drunk girl, haha."
    scene town club 8pm 035b
    irina "You aren't mad at her, are you?"
    irina "Getting two rewards."
    pov "Haha, no!"
    bs "I... just want to... thank..."
    pov "Calm down [bs], everything is fine."
    irina "It's time to drag her to bed. I can't wait to see you again [pov]."
    pov "Me neither."
    scene black
    "[irina] drags [bs] into her room."
    $ irinalove += 1
    $ bigsislove += 1
    $ dtime += 1
    $ club8pmfirst = True
    jump frontdoor

label club9vivanchoice:
    hide screen townl
    scene town club 9am 001
    call screen club9vivanchoices

screen club9vivanchoices:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if acceptjobsleazy == False:
            imagebutton auto "gui/icons/icon_question_%s.png" action (Hide('club9vivanchoices'), Jump('club9askforjob')) hovered tt.Action ("Ask for a job") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_action_%s.png" action (Hide('club9vivanchoices'), Jump('club9workthejob')) hovered tt.Action ("Work") focus_mask True
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('club9vivanchoices'), Jump('club9vivan')) hovered tt.Action ("Get some hot coffee") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club9askforjob:
    vivian "Hey there good looking!"
    pov "Hey [vivian]. How are you doing today?"
    vivian "Better now that you're here."
    pov "Well I'll never argue with a beautiful woman happy to see me."
    vivian "Cute as always! But I hope you're serious about that."
    pov "Serious about what?"
    vivian "Serious about never arguing with a beautiful woman."
    pov "Oh yeah, what would be arguing about?"
    if inc == True:
        vivian "Your mother tells me you need a job and it just so happens that I need a man."
    else:
        vivian "[mother] tells me you need a job and it just so happens that I need a man."
    pov "Really [vivian]? I had assumed you could have any man you wanted."
    vivian "Oh hush you, I meant a man to help me out around here."
    vivian "So what do you say, you wanna be my man?"
    povi "She's got to be teasing me, asking it like that. I like it."
    pov "Well how much does it pay?"
    vivian "Well I can offer you $50 dollars a day. You'll be doing some odds and ends around here."
    vivian "Nothing too... extreme. Probably only take an hour or so each day."
    call screen club9wantthejob
    if acceptjobsleazy == True:
        $ vivianrelationship += 1
        pov "Well in that case, I'm your man [vivian]."
        vivian "Oh I like the sound of that!"
        povi "This is going to be interesting!"
    else:
        pov "I'll have to get back to you [vivian]. I'm still looking into a few other options."
        vivian "Well I can say I'm surprised, a strong, handsome man such as yourself."
        vivian "But I am sad I couldn't entice you to come work with me."
        pov "Well I didn't say no, just not yet."
        vivian "I guess I can live with that for now sugar."
    $ dtime += 1
    jump club


screen club9wantthejob:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('club9wantthejob'), SetVariable('acceptjobsleazy', True), Return(None)) hovered tt.Action ("Accept the Job") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('club9wantthejob'), SetVariable('acceptjobsleazy', False), Return(None)) hovered tt.Action ("Decline the Job") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label club9workthejob:
    pov "What have you got for me today [vivian]?"
    vivian "Well if you could sweep and mop the dance floor that would be great."
    if katefirstmeet == True:
        vivian "[kate] said the floor was stickly last night. I'm sure she'd appreciate it too."
        $ katerelationship += 1
    pov "I'm on it boss!"
    vivian "Oh, I like a man that gets to business."
    "She winks at you before you head off to clean the dance floor."
    scene town club 9am 002 #----- Nicole and Vivian Talking -----
    "It takes a little over an hour to get the floors nice and shiny."
    povi "There we go. All finished!"
    if inc == True:
        povi "Oh hey, mom and [vivian] are chatting. I'll go say hello after I put these cleaning supplies away."
    else:
        povi "Oh hey, [mother] and [vivian] are chatting. I'll go say hello after I put these cleaning supplies away."
    povi "Is it just me or is [vivian] almost always looking over at me while I work?"
    scene town club 9am 003 #----- Nicole Says Hello, Vivian at Bar -----
    "After putting the cleaning supplies away, you walk over to the girls chatting at the bar."
    mom "Hey sweetie, I see you're doing a good job for [vivian] out there."
    if inc == True:
        pov "Thanks mom, I really hope so."
    else:
        pov "Thanks [mother], I really hope so."
    vivian "Oh you definitely are [pov]!"
    vivian "One of these days I'll need to get you to use those strong hands on something else around here."
    if inc == True:
        povi "Wow, she's flirting with me in front of my mom."
    else:
        povi "Wow, she's flirting with me in front of [mother]."
    povi "She didn't seem to notice though. That's probably best for now."
    pov "Well, I'm all done here. I guess I'll see you both tomorrow."
    "Both" "See ya, sweetie!"
    "You chuckle to yourself as you leave, after collecting your $50 from [vivian]"
    $ dtime += 1
    $ money += 50
    jump club

label club9vivan:
    hide screen townl
    scene town club 9am 001
    if club10amfirst == False:
        "Bartender" "Hello there. You must be new in town."
        pov "Yes, I am. Just trying to find my bearings around town. I was told this is the place to be."
        "Bartender" "Yes it is! Maybe I'll get to see you more often around then?"
        pov "Haha, yes. I definitely hope so. You're here so I don't see why I would want go anywhere else!"
        "Bartender" "Haha, true. Plus it's the only club in town, so everyone come here to party."
        if vivianfirstmeet == False:
            "Bartender" "My name is..."
            $ vivianname = renpy.input(_("Her name is...")) or _("Vivian")
            $ vivianname = vivianname.strip()
            if vivianname == "":
                $ vivianname = "Vivian"
            $ vivianfirstmeet = True
        vivian "And you are?"
        pov "My name is [pov]! Nice to meet you."
        vivian "But you aren't here just to talk to me right?"
        pov "Haha, maybe I am! But something to drink would be nice too."
        vivian "You're cute. Well if you aren't sitting at the bar then you can pick any table and I'll send a waitress over to you."
        pov "Okay, thank you."
    else:
        vivian "Hey [pov], it's good to see you again, but you aren't here just to talk to me right?"
        pov "Haha, maybe I am! But even if I'm not something to drink would be nice too."
        vivian "You're cute. Well if you aren't sitting at the bar then you can pick any table and I'll send [mother] over to you."
        pov "Okay, thank you."
    scene black
    "You walk over to the other side of the club to sit at a table where you have a good view of the place."
    scene town club 9am 002
    if club10amfirst == False:
        "Then you notice her."
        if inc == True:
            povi "Is that mom?"
        else:
            povi "Is that [mother]?"
        povi "So she's working here in the mornings?"
    else:
        pov "There she is."
    scene town club 9am 003
    if club10amfirst == False:
        povi "Yes, that is her. She's waving at me."
        povi "Well, now I know where she goes in the mornings."
    else:
        mom "Be right there honey."
    scene town club 9am 004
    if club10amfirst == False:
        mom "Hey [pov], so you found your way into town?"
        if inc == True:
            pov "Hi mom. Yes and I was told I need to check out the club scene here."
            pov "And now my mom can serve me a coffee just like at home, haha."
        else:
            pov "Hi [mother]. Yes and I was told I need to check out the club scene here."
            pov "And now you can serve me a coffee just like at home, haha."
        mom "Hahaha...cheeky, [pov]!"
        pov "But that is a nice outfit you're wearing."
        mom "Oh, I'm happy you like it."
    else:
        mom "Hey [pov], what brings you into town?"
        if inc == True:
            pov "Hi mom. I just wanted to come and say hello."
            pov "And now my mom can serve me a coffee just like at home, haha."
        else:
            pov "Hi [mother]. I just wanted to come and say hello."
            pov "And now you can serve me a coffee just like at home, haha."
        mom "Hahaha...cheeky, [pov]!"
        pov "I still really like that outfit you're wearing."
        mom "Oh, I'm happy you like it."
    scene town club 9am 004a
    pov "Wow!"
    mom "<giggle> I like it too."
    povi "Interesting. Discreet but also somewhat sexy with those stockings. It's subtle but aluring."
    pov "Yes, you look really good in it."
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
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('club9momch1'), Jump('club9momlove')) hovered tt.Action ("Greet her properly [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('club9momch1'), Jump('club9momcor')) hovered tt.Action ("Greet her properly [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
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
        pov "Nah mom, just treating you right."
    else:
        pov "Nah [mother], just treating you right."
    pov "Just seemed like you weren't getting enough of them at home is all!"
    mom "Haha, you won't let me go, will you?"
    if momlove > 10:
        scene town club 9am 006b
        pov "Nope, I'll hold you forever!"
        pov "I was away for so long, I just like to feel you close again."
        mom "But we'll get to see each other more often now."
        if inc == True:
            pov "True, but there's nothing wrong when a son wanting to hold his mother in his arms right?"
            mom "Of course not sweetie! That's just about the sweetest thing I ever heard. You can hold me a long as you want."
            pov "Sometimes a hug is just what you need, isn't it?"
            mom "Yes that's true, especially when no one else hugs me like you do."
            mom "Makes me feel appreciated and loved"
            pov "Exactly!"
        else:
            pov "True, but there's nothing wrong wanting to hold you in my arms right?"
            mom "Of course not sweetie! That's just about the sweetest thing I ever heard. You can hold me a long as you want."
            pov "Sometimes a hug is just what you need, isn't it?"
            mom "Yes that's true, especially when no one else hugs me like you do."
            mom "Makes you feel appreciated and loved"
            pov "Exactly!"
        mom "I do eventually have to go back to work though, don't want to get fired, hahaha."
    scene town club 9am 007b
    mom "Wow! That was really nice."
    pov "I thought so too."
    mom "You should come here everyday, so I can get more hugs, haha."
    if inc == True:
        pov "Haha, oh mom."
    else:
        pov "Haha, oh [mother]."
    pov "Deal, and maybe I can get coffee in exhange?"
    mom "Haha! Sure. That sounds like a good trade! I'll bring it right away."
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
        mom "Oh hnnn... you slapped me in public..."
        pov "Yes! Because I'm a bad boy, remember?"
        mom "..."
        pov "So how about you bring me that coffee now!"
        mom "O...okay..."
        $ club10slapfirst = True
        jump club9momwalk
    else:
        scene town club 9am 006ab
        mom "What the hell do you think you are doing!"
        povi "Oh shit..."
        mom "Are you out of your mind?"
        if inc == True:
            pov "But mom..."
        else:
            pov "But [mother]..."
        mom "No buts!"
        mom "It's better you leave now, I'm very disappointed in you right now!"
        pov "..."
        mom "Leave now!"
        pov "O... okay..."
        povi "Damn, maybe she isn't corrupted enough."
        $ dtime += 1
        $ club10slapfirst = True
        jump club

label club9momwalk:
    scene town club 9am 008
    if inc == True:
        povi "Damn that outfit is really hot. Never thought mom would be serving me like as a waitress, a bit like a fantasy, haha."
    else:
        povi "Damn that outfit is really hot. Never thought [mother] would be serving me like as a waitress, a bit like a fantasy, haha."
    povi "And that guy has sleeping on the table since I came in here. He must be so wasted."
    if knowaboutjobsleazy == False:
        if inc == True:
            povi "I wonder if I can work here too, with mom?"
        else:
            povi "I wonder if I can work here too, with [mother]?"
    scene town club 9am 009
    mom "Here is your coffee, [pov]."
    if inc == True:
        pov "Thanks, mom."
    else:
        pov "Thanks, [mother]."
    mom "So what are you going to do with your day?"
    pov "Hmm..."
    if knowaboutjobsleazy == False:
        mom "Are you out looking for a job?"
        pov "Maybe I can work here too?"
        mom "Hmm... you could ask [vivian], she's responsible for the jobs here. And she's a good friend of mine so it could happen."
        pov "Oh, that's good to know."
        $ knowaboutjobsleazy = True
    vivian "[mother]!"
    scene town club 9am 010
    mom "Hmm..."
    vivian "I have some work to do for you. Are you available right now?"
    mom "Oh sure. Just a moment."
    vivian "Ok. Thanks."
    scene town club 9am 011
    mom "I have to get back to work so we will have to talk later."
    pov "Sure thing. I won't bug you anymore."
    mom "Alright dear, see you later. And don't forget to look for that job."
    if inc == True:
        pov "Sure, mom."
    else:
        pov "Sure, [mother]."
    povi "Hmm... maybe I should take my coffee to go. Sitting here alone is a bit boring."
    #----- Added  and NTR == True or hardntr == True to force the NTR scene if HardNTR is set to on -----
    if momrelationship < 6 and NTR == True or hardntr == True:
        jump club9hardntr
    else:
        $ momrelationship += 1
        $ dtime += 1
        $ club10amfirst = True
        jump club

label club9hardntr:
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene town club 9am 012
    povi "Hmm... wait, where's she going so fast?"
    povi "I didn't realize that upstairs is something too."
    scene town club 9am 013
    povi "There she is. But who's that guy?"
    if frankfirstmeet == True:
        povi "Is that Frank? The guy from the tanning salon?"
    povi "What are they talking about? Damn if I get closer they could see me."
    call screen checkdarkerpaths_nicole
    if nicole_voyeur == True or nicole_ntr == True:
        scene town club 9am 014
        if inc == True:
            povi "He's scolding mom? Did she do something wrong?"
        else:
            povi "He's scolding her? Did she do something wrong?"
        povi "She just standing there and listening to him. If I could just hear what he's saying. Damn it!"
        scene town club 9am 015
        povi "What the hell? Is he about to spank her?"
        if nicole_voyeur == True:
            if inc == True:
                povi "He is about to spank my mom! And she just bent herself over so obediently. Nice!"
            else:
                povi "He is about to spank her! And she just bent herself over so obediently. Nice!"
        if nicole_ntr == True:
            if inc == True:
                povi "That creep is about to spank my mom! And she just bent herself over so obediently. What the hell?"
            else:
                povi "That creep is about to spank her! And she just bent herself over so obediently. What the hell?"
        scene town club 9am 016
        mom "Hnng... hah..."
        if vivianfirstmeet == True:
            povi "Wow! He's hitting her so hard. Wait it sounds like she is enjoying it? Why isn't [vivian] interfering?"
        else:
            povi "Wow! He's hitting her so hard. Wait it sounds like she is enjoying it? Why isn't the bartender interfering?"
        mom "HAH..."
        if nicole_voyeur == True:
            povi "Even harder that time... you dirty bastard! I'm getting jealous now!"
        if nicole_ntr == True:
            povi "Even harder that time... you dirty bastard! I can't believe this!"
        povi "I shouldn't do anything until I know what happened. I don't won't to get her into bigger trouble."
        scene town club 9am 017
        if nicole_voyeur == True:
            povi "Oh, they're done. Damn, is she not wearing panties? It looks like she wasn't wearing any."
            povi "And now she's standing like a slave before him. How often does she do this?"
            povi "I gotta find out what the reason she's doing this. Maybe I can use that to get something out of this myself."
            scene town club 9am 018
            povi "I should probably just wait here for her and see if I can get anything out of her about this."
            povi "Just look at that asshole sitting there and enjoy his power over her, That's going to be me someday!"
            if inc == True:
                povi "Spanking my mom like that in public! So naughty!"
            else:
                povi "Spanking [mother] like that in public! So naughty!"
        if nicole_ntr == True:
            povi "Looks like he's done now. Was she not wearing panties? It looked like she wasn't wearing any."
            povi "And now she's standing like a slave before him. How often does he do this her?"
            povi "I gotta find out what the reason she's doing this. Maybe I can help her stop this."
            scene town club 9am 018
            povi "I should probably just wait here for her and see if I can get anything out of her about this."
            povi "Just look at that asshole sitting there and enjoy his power over her. What an asshole!"
            if inc == True:
                povi "Spanking my mom like that in public!"
            else:
                povi "Spanking [mother] like that in public!"
        "You wait for half an hour but you still can't see her."
        povi "Damn, is she gone? Maybe there is another exit."
        povi "Guess I should stop wasting time here and go find her."
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        $ vipntrfrank = True
        $ dtime += 1
        $ club10amfirst = True
        jump club
    elif nicole_revenge == True:
        scene town club 9am 014
        if inc == True:
            povi "He's scolding mom? Did she do something wrong?"
        else:
            povi "He's scolding her? Did she do something wrong?"
        povi "She's standing there obedient and listening to him. If I could hear what he's say. Damn!"
        scene town club 9am 015
        povi "What the hell? Is he about to spank her?"
        if inc == True:
            povi "That asshole is about to spank my mom! And she bent over so obediently. What did she do wrong?"
        else:
            povi "That asshole is about to spank her! And she bent over so obediently. What did she do wrong?"
        scene town club 9am 016
        mom "Hnng... hah..."
        if vivianfirstmeet == True:
            povi "He's hitting her so hard that even I can hear her screaming! Why isn't [vivian] interfering?"
        else:
            povi "He's hitting her so hard that even I can hear her screaming! Why isn't the bartender interfering?"
        mom "HAH..."
        povi "Even harder... you bastard!"
        povi "But I can't do anything until I know what happened. I don't won't to get her into bigger trouble."
        scene town club 9am 017
        povi "Oh, they're done. Damn, did she forget her panties? It looks like she isn't wearing any."
        povi "And now she's standing like a slave before him. Why is this happening? And how often?"
        povi "I've got to find out what the reason is for her to act like this. I need to help her to get away from that asshole."
        scene town club 9am 018
        povi "Good. It's over now. Now I have to wait for her so I can ask her."
        povi "Just look at that asshole sitting there and enjoy his power over her."
        if inc == True:
            povi "Spanking my mom like that in public!"
        else:
            povi "Spanking [mother] like that in public!"
        "You wait for half an hour but you still can't see her."
        povi "Damn, is she gone? Maybe there is another exit."
        povi "Guess I should stop wasting time here and go find her."
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        $ vipntrfrank = True
        $ dtime += 1
        $ club10amfirst = True
        jump club
    elif nicole_sadist == True:
        scene town club 9am 014
        if inc == True:
            povi "He's scolding mom? Did she do something wrong?"
        else:
            povi "He's scolding her? Did she do something wrong?"
        povi "She's standing there obedient and listening to him. If I could only hear what he's saying. Damn!"
        scene town club 9am 015
        povi "What the hell? Is he about to spank her?"
        if inc == True:
            povi "That asshole is about to spank my mom! And the bitch is bent over so obediently."
        else:
            povi "That asshole is about to spank her! And the bitch is bent over so obediently."
        scene town club 9am 016
        mom "Hnng... hah..."
        povi "He's hitting her so hard that even I can hear her screaming! Fuck yeah!"
        mom "HAH..."
        povi "Even harder that time! A man after my own twisted heart I see."
        povi "I need to get in on this! I wonder what he has on her... Or maybe she's just a dirty whore that likes it? That would be convenient!"
        scene town club 9am 017
        povi "Oh, they're done. Damn. Hey, she's not wearing panties! That little minx."
        povi "Wow, look at her obedientatly waiting to be dismissed. She's been doing this for a while it seems. He almost has her trained."
        povi "I've got to find out what the reason is for her to act like this. I could use it against her just like he is."
        scene town club 9am 018
        povi "I think I'll wait for her to come back down and press her on it. See if I can get anything out of her."
        povi "Just look at that asshole sitting there and enjoy his power over her. That will be me soon!"
        if inc == True:
            povi "Spanking my mom like that in public! Living the dream!"
        else:
            povi "Spanking [mother] like that in public! Living the dream!"
        "You wait for half an hour but you still can't see her."
        povi "Damn, is she gone? Maybe there is another exit."
        povi "Guess I should stop wasting time here and go find her."
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        $ vipntrfrank = True
        $ dtime += 1
        $ club10amfirst = True
        jump club
    else:
        if gamemusic == True and renpy.music.is_playing("bgm") == False:
            stop music fadeout 2
            play music "music/default.mp3"
        jump club
