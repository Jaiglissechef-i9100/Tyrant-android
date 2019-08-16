

label showerup7look:
    hide screen locations
    pov "{i}Maybe I can see something.{/i}"
    scene showerupstairs 7am shower up
    pov "{i}Oh my god. I can see her. She's so hot.{/i}"
    pov "{i}But the angle is wrong. I can't see more.{/i}"
    pov "{i}I need to do something! Maybe a second mirror? Or a way to get in?{/i}"
    jump showerup

label showerup7talk:
    hide screen locations
    pov "Who's in there?"
    ls "Go away! I'm showering right now."
    pov "..."
    if lilsiscorruption >= lilsislove:
        jump showerup7extcor
    elif basealefirst == True and lilsiscorruption < lilsislove:
        jump showerup7extlove
    else:
        jump showerup

label showerup7listen:
    hide screen locations
    "You listen through the door."
    pov "{i}Someone is showering.{/i}"
    jump showerup



label showerup20talk:
    hide screen locations
    pov "Who's in there?"
    ls "Go away! The bathroom is occupied."
    pov "..."
    jump showerup

label showerup20listen:
    hide screen locations
    "You listen through the door."
    pov "{i}Someone is in the bathroom. But it's very quiet in there.{/i}"
    jump showerup

label showerup20look:
    hide screen locations
    pov "{i}Maybe I can see something.{/i}"
    scene showerupstairs 8pm shower upstairs 002
    pov "{i}[ls] is in there. Is she checking herself out?{/i}"
    ls "Fine... very well..."
    scene showerupstairs 8pm shower upstairs 003
    pov "{i}Oh my god! These panties are cute. And her ass too.{/i}"
    ls "Lalala..."
    $ dtime += 1
    jump showerup

label showerup22talk:
    hide screen locations
    pov "Who's in there?"
    bs "Go away! The bathroom is occupied."
    pov "..."
    jump showerup

label showerup22listen:
    hide screen locations
    "You listen through the door."
    pov "{i}Someone is in the bathroom. But it's very quiet in there.{/i}"
    jump showerup

label showerup22look:
    hide screen locations
    pov "{i}Maybe I can see something.{/i}"
    scene showerupstairs 10pm shower upstairs 002
    pov "{i}[bs] is in there. Is she checking herself out?{/i}"
    pov "{i}Her nipples are hard too and her tits are so hot.{/i}"
    scene showerupstairs 10pm shower upstairs 003
    bs "Hmm... hmm..."
    pov "{i}Is she? Oh yeah. She's playing with herself. So hot.{/i}"
    pov "{i}I wonder where she was outside before?{/i}"
    pov "{i}Maybe with her boyfriend?{/i}"
    scene showerupstairs 10pm shower upstairs 004
    bs "Yes... yes, do me harder!"
    pov "{i}She's getting herself off and I can watch. Perfect!{/i}"
    bs "Hah... hmm... yes!"
    pov "{i}Oh, already done...{/i}"
    $ dtime += 1
    jump showerup


label showerup15listen:
    hide screen locations
    "You listen through the door."
    ls "Hah... Hmm..."
    pov "{i}There she went. But what's she doing?{/i}"
    jump showerup

label showerup15look:
    hide screen locations
    pov "{i}Maybe I can see something.{/i}"
    if lsispronBDSM >= 4:
        scene showerupstairs 3pm 001b
        ls "Hmm... slap me..."
        pov "{i}Damn, she's getting into the BDSM stuff.{/i}"
        "<slap>"
        ls "Hng..."
        pov "{i}Nice to see that I get her so horny.{/i}"
        scene showerupstairs 3pm 002b
        ls "Hm... it feels so good... hah... master."
        pov "{i}Damn, she's masturbating and slapping herself.{/i}"
        ls "Au... hah... <slap>"
        pov "{i}I'm curious if she can get herself off with this stuff.{/i}"
        scene showerupstairs 3pm 003b
        ls "Aaaahh... hah... hah..."
        if inc == True:
            pov "{i}So hot. My innocent little sister came with that stuff.{/i}"
        else:
            pov "{i}So hot. Innocent [ls] came with that stuff.{/i}"
        pov "{i}And I got her into it.{/i}"
        ls "Hnngg..."
        $ lsispronBDSM += 1
        $ su15masBDSM = True
        jump showerup15end
    elif lsispronanal >= 4:
        scene showerupstairs 3pm 001a
        ls "If it slowly gets in..."
        pov "{i}Damn, is she trying to do anal on herself?{/i}"
        ls "Hng... careful..."
        pov "{i}I can't believe it!{/i}"
        ls "Hmm..."
        scene showerupstairs 3pm 002a
        ls "Ohh... I feel it inside... ah..."
        pov "{i}Damn, she's masturbating and fingering her asshole.{/i}"
        ls "It feels weird... and... hah... so good."
        pov "{i}I'm curious if she can get herself off with this stuff.{/i}"
        scene showerupstairs 3pm 003a
        ls "Hah... Aaaahh... Hmm..."
        "She's shaking wildly."
        if inc == True:
            pov "{i}So hot. My innocent little sister came with that stuff.{/i}"
        else:
            pov "{i}So hot. Innocent [ls] came with that stuff.{/i}"
        pov "{i}And I got her into it.{/i}"
        ls "Hnngg..."
        $ lsispronanal += 1
        $ su15masanal = True
        jump showerup15end
    elif lsisproninterracial >= 4:
        scene showerupstairs 3pm 001
        ls "Your black dick is rubbing me there, hah..."
        pov "{i}Damn, is she fantasizing about interracial sex?{/i}"
        ls "When he sticks it in... hmm..."
        pov "{i}I wonder with whom she's fantasizing?{/i}"
        scene showerupstairs 3pm 002
        ls "You're inside! Hmm... so big, hah..."
        pov "{i}Damn, she's masturbating and fantasizing about black men.{/i}"
        ls "It's so good... hah... deeper..."
        pov "{i}I'm curious if she can get herself off with this stuff.{/i}"
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            pov "{i}So hot. My innocent little sister came with that stuff.{/i}"
        else:
            pov "{i}So hot. Innocent [ls] came with that stuff.{/i}"
        pov "{i}And I got her into it.{/i}"
        ls "Hah... hah... hah..."
        $ lsisproninterracial += 1
        $ su15masinterracial = True
        jump showerup15end
    elif lsisproninc >= 4:
        scene showerupstairs 3pm 001
        ls "Your dick is rubbing me there, hah... big brother..."
        pov "{i}Damn, is she fantasizing about me?{/i}"
        ls "When he sticks it in... hmm..."
        pov "{i}I can't believe it! She wants me!{/i}"
        scene showerupstairs 3pm 002
        ls "You're inside! Hmm... so big, hah..."
        pov "{i}Damn, she's masturbating and fantasizing about me.{/i}"
        ls "It's forbidden, but so good... hah... deeper..."
        pov "{i}I'm curious if she can get herself off with this stuff.{/i}"
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        pov "{i}So hot. My innocent little sister came with that stuff.{/i}"
        pov "{i}And I got her into it.{/i}"
        ls "Hah... hah... hah..."
        $ lsisproninc += 1
        $ su15masinc = True
        jump showerup15end
    elif lsispronlesbian >= 4:
        scene showerupstairs 3pm 001
        ls "Yes... hah... lick me there..."
        pov "{i}Damn, who is she thinking of?{/i}"
        ls "You're always my best friend... hmm..."
        pov "{i}She has a boyfriend?{/i}"
        scene showerupstairs 3pm 002
        ls "Yes, hah... play with your breasts too... ahh..."
        pov "{i}Damn, she's masturbating and fantasizing about another girl.{/i}"
        ls "Your tongue is so... hah... hah... amazing!"
        pov "{i}I'm curious if she can get herself off with this stuff.{/i}"
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            pov "{i}So hot. My innocent little sister came with that stuff.{/i}"
        else:
            pov "{i}So hot. Innocent [ls] came with that stuff.{/i}"
        pov "{i}And I got her into it.{/i}"
        ls "Hah... hah... hah..."
        $ lsispronlesbian += 1
        $ su15maslesbian = True
        jump showerup15end
    elif lsispronntr >= 4:
        scene showerupstairs 3pm 001
        ls "Yes... hah... look at him, he'll stick it in me... hah..."
        pov "{i}Damn, I don't get it.{/i}"
        ls "He'll fuck me and you have to watch... hmm..."
        pov "{i}She's fantasizing about ntr'ing someone!{/i}"
        scene showerupstairs 3pm 002
        ls "Yes, hah... he's so good and you're the looser [pov]... ahh..."
        pov "{i}Damn, she's masturbating and fantasizing about ntr'ing me. I wonder who fucks her in this?{/i}"
        ls "Please stick it deeper... hah... hah..."
        pov "{i}I'm curious if she can get herself off with this stuff.{/i}"
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            pov "{i}So hot. My innocent little sister came with that stuff.{/i}"
        else:
            pov "{i}So hot. Innocent [ls] came with that stuff.{/i}"
        pov "{i}And I got her into it.{/i}"
        ls "Hah... hah... hah..."
        $ lsispronntr += 1
        $ su15masntr = True
        jump showerup15end
    elif lsispronfemdom >= 4:
        scene showerupstairs 3pm 001
        ls "Yes... hah... lick me, slave... hah..."
        pov "{i}Slave? What's going on?{/i}"
        ls "Lick me faster... hah or I'll spank you... hmm..."
        pov "{i}She's fantasizing about dominating someone!{/i}"
        scene showerupstairs 3pm 002
        ls "No, hah... you aren't allowed to touch your dick... ahh..."
        pov "{i}Damn, she's masturbating and fantasizing about femdom. I wonder who's the slave?{/i}"
        ls "Yes, good boy... hah... hah..."
        pov "{i}I'm curious if she can get herself off with this stuff.{/i}"
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            pov "{i}So hot. My innocent little sister came with that stuff.{/i}"
        else:
            pov "{i}So hot. Innocent [ls] came with that stuff.{/i}"
        pov "{i}And I got her into it.{/i}"
        ls "Hah... hah... hah..."
        $ lsispronfemdom += 1
        $ su15masfemdom = True
        jump showerup15end
    elif lsisprongangbang >= 4:
        scene showerupstairs 3pm 001
        ls "Yes... hah... stick it in... hah..."
        pov "{i}What's going on?{/i}"
        ls "Go on, the others are waiting... hah... hmm..."
        pov "{i}She's fantasizing about getting gangbanged!{/i}"
        scene showerupstairs 3pm 002
        ls "No, hah... wait a second... hm... when he's done... ahh..."
        pov "{i}Damn, she's masturbating and fantasizing about group sex.{/i}"
        ls "Yes, another one? Hah... hah..."
        pov "{i}I'm curious if she can get herself off with this stuff.{/i}"
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            pov "{i}So hot. My innocent little sister came with that stuff.{/i}"
        else:
            pov "{i}So hot. Innocent [ls] came with that stuff.{/i}"
        pov "{i}And I got her into it.{/i}"
        ls "Hah... hah... hah..."
        $ lsisprongangbang += 1
        $ su15masgangbang = True
        jump showerup15end
    else:
        scene showerupstairs 3pm 001
        ls "Yes... hah... your dick is rubbing me there... hah..."
        pov "{i}She's masturbating.{/i}"
        ls "Please stick it in... hah... hmm..."
        pov "{i}She's fantasizing about getting fucked!{/i}"
        scene showerupstairs 3pm 002
        ls "Yes, hah... deeper... ahh..."
        pov "{i}Damn, she's masturbating and fantasizing about getting fucked.{/i}"
        ls "You're so big, hah... faster..."
        scene showerupstairs 3pm 003
        ls "Haaaahh... Ahhh... Hnng..."
        if inc == True:
            pov "{i}So hot. My innocent little sister masturbated and came.{/i}"
        else:
            pov "{i}So hot. Innocent [ls] masturbated and came.{/i}"
        ls "Hah... hah... hah..."
        $ su15masnormal = True
        jump showerup15end

label showerup15end:
    pov "{i}But it's better if I leave now. I can use this \"secret\" another time.{/i}"
    scene black
    $ lilsisrelationship += 1
    $ dtime += 1
    jump showerup