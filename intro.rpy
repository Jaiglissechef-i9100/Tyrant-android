#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label intro: #----- edited -----
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/intro.mp3"
    scene novel_back
    window show
    n "You're a young man returning from a year abroad as an exchange student. It was for your senior year of highschool and now you've come home to find a job."
    if inc == True:
        n "The taxi is taking you to a new address. You learned that your family moved during your exchange program."
    else:
        n "The taxi is taking you to a new address. You learned that the family you lived with moved during your exchange program."
    nvl clear
    window hide

    scene intro 000
    $ povname = renpy.input(_("So what is your first name?")) or _("Sam")
    $ povname = povname.strip()
    if povname == "":
        $ povname = "Sam"
    povi "Just a few more miles and I should be at my new home. I can't believe it's been almost a full year since I talked to everyone beyond letters."
    povi "First things first, I have to teach them how to use Skype correctly. I still can't believe we couldn't get it working even once while I was gone."
    povi "I mean they aren't tech stupid. We should've been able to figure it out."
    povi "I was a bit angry at first, but being so close to seeing everyone again, I can't stay mad."
    scene intro mom intro
    if inc == True:
        povi "I wonder how mom's doing? Is she still mothering everyone like we were little kids?"
        "What's your mom's name?"
        $ nicolename = renpy.input(_("You'll call her mom, but it's need when others call her.")) or _("Nicole")
        $ nicolename = nicolename.strip()
        if nicolename == "":
            $ nicolename = "Nicole"
            $ momname = "Mom"
    else:
        povi "I wonder how's mom's best friend doing? Is she still mothering everyone like we were little kids?"
        $ nicolename = renpy.input(_("What's the name of your mom's childhood friend?")) or _("Nicole")
        $ nicolename = nicolename.strip()
        if nicolename == "":
            $ nicolename = "Nicole"
        else:
            $ momname = nicolename
    povi "I missed her so much."
    scene intro lil sis intro
    if inc == True:
        povi "Lil' sis'? Still hangin' around all the time, trying to impress me?"
    else:
        povi "And her youngest daughter? Still hangin' around all the time, trying to impress me?"
    povi "I sometimes wondered if she thought she was a boy too. She could keep up with any of us."
    if inc == True:
        $ lsname = renpy.input(_("What's your little sister's name?")) or _("Alexis")
        $ lsname = lsname.strip()
        if lsname == "":
            $ lsname = "Alexis"
    else:
        $ lsname = renpy.input(_("What's your younger childhood friends name?")) or _("Alexis")
        $ lsname = lsname.strip()
        if lsname == "":
            $ lsname = "Alexis"
    povi "It'll be fun to tease her again when she trying to impress me."
    scene intro big sis intro
    if inc == True:
        povi "And then there is big sis'."
        $ bsname = renpy.input(_("What's your big sister's name?")) or _("Cassandra")
        $ bsname = bsname.strip()
        if bsname == "":
            $ bsname = "Cassandra"
    else:
        povi "And then there is my older friend'."
        $ bsname = renpy.input(_("What's your older childhood friends name?")) or _("Cassandra")
        $ bsname = bsname.strip()
        if bsname == "":
            $ bsname = "Cassandra"
    povi "I wonder if she will still treat like a little pervert."
    povi "Maybe she's calmed down over the last year."
    scene black
    if inc == True:
        povi "And then there is dad. He took such good care of us all. It was easy to forget he's our step-dad, he loved us as if we were his own children."
    else:
        povi "And then there is their dad. He took such good care of us all. It was easy to forget he wasn't my real dad, he loved me as if I were his own children."
    "Driver" "Hey wake up!"
    pov "What...?"
    povi "I was asleep?"
    pov "Oh sorry. Here's your money."
    window show
    n "You can skip the intro, but it this is your first time playing the game it's not recommenend"
    n "Do you want to skip the intro?"
    menu:
        "Yes":
            nvl clear
            window hide
            jump tutorial
        "No":
            nvl clear
            window hide
            pass
    scene intro 001
    povi "Oh... Is that...?"
    povi "Wow... They've changed..."
    povi "But what's with the weird house. It looks kinda... cheap."
    scene intro 002
    povi "Oh they saw me."
    mom "[pov]!"
    ls "Finally you get here!"
    povi "What are they wearing? They are showing a lot more skin that I remember then doing before."
    if inc == True:
        povi "I never thought mom would show so much cleavage out in public."
    else:
        povi "I never thought [mother] would show so much cleavage out in public."
    scene intro 003
    if inc == True:
        ls "Brother!"
    else:
        ls "[pov]!"
    pov "[ls]!"
    povi "She's wearing makeup. Looks like she's growing up."
    scene intro 004
    ls "I missed you so much!"
    if inc == True:
        pov "I missed you too, lil' sister."
    else:
        pov "I missed you too, [ls]."
    ls "We have so much to catch up on."
    pov "Didn't [bs] keep you entertained while I was gone?"
    ls "No. She isn't fun like you."
    scene intro 005
    mom "Now it's my turn. I'm so proud."
    if inc == True:
        pov "Oh, mom."
        scene intro 006
        mom "My only son has finished his schooling overseas. You make your mother so proud."
        pov "Calm down mom. It wasn't that hard. I'm not a little boy anymore."
    else:
        pov "Oh, [mother]."
        scene intro 006
        mom "My best friend's only son has finished his schooling overseas. You make your mother and I so proud."
        pov "Gah! Calm down [mother]. It wasn't that hard. I'm not a little boy anymore you know."
    mom "I missed you so much. It's so good that you'll be staying with us from now on. Maybe helping out around here."
    pov "Yes I can. Don't worry. I missed you too."
    scene intro 007
    mom "Come on in. We'll show you our new home."
    povi "I wonder why they ended up here. I don't want to make them angry by talking bad about the house though. I should just think of it as cozy not cheap."
    pov "Sure!"
    ls "Come on [pov]!"
    pov "And where is [bs]?"
    mom "Oh she's with her boyfriend in town. You'll meet her later."
    if inc == True:
        pov "Typical big sister."
    else:
        pov "Typical [bs]."
    scene intro 008
    povi "With her boyfriend... we might have to see about that later, hahaha."
    ls "Are you coming?"
    mom "Yes, sorry. No need to rush."
    scene intro 009
    povi "What a view! I didn't really notice her cleavage so much before I left."
    povi "I wonder what happened that's made her dress so openly now?"
    scene intro 010
    mom "Let's go in."
    pov "Okay."
    scene intro 011
    if inc == True:
        povi "Wow, she's got an ass to go with it! Wait, what's wrong with me. Am I checking out my own mother?"
    else:
        povi "Wow, she's got an ass to go with it! Wait, what's wrong with me. Am I checking out [mother]?"
    povi "Damn. But she is so sexy right now!"
    scene intro 012
    povi "What's with that picture?"
    mom "So what do you think of the living room?"
    scene intro 013
    povi "Was it taken in a strip club? It's like porn."
    povi "And right here in the living room. Who would hang something like  there?"
    pov "What...? Oh sorry, I think I was staring a bit."
    mom "Hnnn..."
    if inc == True:
        povi "Mom would never allow that before I left!"
    else:
        povi "[mother] would never allow that before I left!"
    scene intro 014
    pov "Ahem... is that...?"
    if inc == True:
        mom "Your dad hung it up. He's into these things lately."
    else:
        mom "Bruce hung it up. He's into these things lately."
    pov "And you're okay with that...?"
    ls "She isn't even naked. And dad calls it art, but mom is so prudish. <giggle>"
    mom "Hnnn..."
    scene intro 015
    mom "I'll explain later! But let's go to the kitchen!"
    pov "Ok... Let's continue the tour."
    mom "Yes! No need to hang out here all day."
    ls "Hehehe..."
    scene intro 016
    pov "Oh the dining room."
    mom "It's wonderful isn't it?"
    pov "Yes it is. And a \"normal\" picture I see."
    mom "Yes, I like it too."
    scene intro 017
    mom "Come on. Next room is the kitchen."
    povi "Hmm... is [ls] trying to give me a hint?"
    scene intro 018
    pov "Holy...!"
    povi "Another perverted picture. And this time its in a BDSM style."
    if inc == True:
        mom "Again from your dad. Please come to the kitchen."
    else:
        mom "Again from Bruce. Please come to the kitchen."
    pov "But... wow..."
    mom "[pov]..."
    if inc == True:
        pov "Yes, mom."
        scene intro 019
        ls "Mom..."
    else:
        pov "Yes, [mother]."
        scene intro 019
        ls "Mom..."
    pov "Haha, I know..."
    povi "Damn. It's going to be hard for a guy with an active imagination to make it around the house without getting aroused left and right."
    scene intro 020
    mom "So tell me how you liked about your school? You graduated with high honors, right? You made me so proud."
    pov "It was okay. All schools are the same... boring!"
    mom "Haha, you don't need to play it cool. You're an adult now."
    pov "Haha, true."
    mom "We'll talk more later, I have to go soon but first there is something urgent to talk about."
    pov "Urgent?"
    scene intro 021
    mom "Yes, it's about living in this house. I nkow it's a bit of a downgrade from our old one and there is a reason for it."
    if inc == True:
        mom "Your dad will introduce you further tonight, but I can tell you some it now."
    else:
        mom "Bruce will introduce you further tonight, but I can tell you some it now."
    pov "Did he lose his job?"
    mom "No, he's doing something that will grant him a much higher rank and increase his pension plan enough that he could retire soon."
    mom "We've been living with him \"undercover\" for almost a year in this house and hopefully will come to an end very soon."
    pov "But wasn't he only a patrolman?"
    mom "Yes, but they gave him this chance and he took it. He believes it is what's best for our family."
    pov "So who's he going to catch with this ruse?"
    scene intro 022
    mom "The good thing is they aren't really dangerous criminals, the bad thing is that they are \"white trash\" criminals."
    mom "Perverted macho's. That's the reason for the pictures through out the house. They like this garbage."
    pov "And you changed you're appearance too for this?"
    mom "Yes, we all decided to help him with this. It was the safest way to play it."
    mom "And it's essential for everyone's safety that you play along with that. At least until he speaks with you."
    mom "If they find out he's a cop they could hurt us all really bad."
    if inc == True:
        pov "Hmm... I'm a bit surprised that dad put you in that kind of danger."
    else:
        pov "Hmm... I'm a bit surprised that Bruce put you in that kind of danger."
    pov "But if you've covered for him for nearly a year, I won't mess it up."
    scene intro 023
    mom "Good! I knew we could count on you."
    pov "So that is the reason for these revealing clothes you were now?"
    mom "Yes... It was unpleasant at the beginning, but I got used to it. And it could be worse."
    mom "And we managed to keep [ls] out of the most, she has to stay in her room at night when they come by though."
    pov "Oh, that's got to be tough on her while she's growing up."
    mom "True. But I won't allow her to get involved with that scum."
    pov "And [bs]?"
    mom "She's an adult. She can take care of herself and thankfully her boyfriend isn't one of them."
    pov "Her boyfriend? Oh yeah, you mentioned him earlier."
    scene intro 024
    mom "Yeah, he's a nice boy, very handsome. I'm glad she found someone."
    pov "..."
    mom "So do you already have a girlfriend you are keeping in touch with or will you be in the market while you are home?"
    pov "Why? I have a fine ass woman right here!"
    scene intro 025a
    mom "What...?"
    pov "Yeah, she even lets me have a good view of her ample breasts and tight ass!"
    mom "You're talking about me?"
    pov "Of course! Wouldn't it be great have some {i}intimate{/i} fun together?"
    mom "What's gotten into you...?"
    pov "Hahaha. I play a good trashy, macho kind of guy right?!"
    scene intro 025b
    mom "Hnnn... of you were joking?"
    pov "Of course! You didn't believe that stuff did you?"
    mom "..."
    if inc == True:
        mom "It was good, but I'm not sure others would approve. Incest might be a bit too strange! Even for scum like them."
        povi "I don't know, I could of sworn she was biting her lip when I was flirting with her, maybe she liked the idea?"
        pov "Okay, sorry mom."
    else:
        mom "It was good, but I'm not sure others would approve. That might be a bit too strange! Even for scum like them."
        povi "I don't know, I could of sworn she was biting her lip when I was flirting with her, maybe she liked the idea?"
        pov "Okay, sorry [mother]."
    scene intro 026
    ls "You guys done talking?"
    ls "I want to show [pov] his room. So he can move in and we can do something together."
    povi "\"Do something together...\" Damn, I need get these thoughts out of my head. Damn dirty pictures, getting me all exicted."
    scene intro 027
    ls "His \"small\" but \"cozy\" room. In this \"modest\" home, hehe."
    pov "So are you get the bigger room now?"
    ls "Yes because I'm the best child in the house."
    pov "Haha, you wish..."
    ls "You'll see! <giggle>"
    scene intro 028
    if inc == True:
        mom "How about you let him relax? Tonight is his first meeting with dad and his first time playing along."
    else:
        mom "How about you let him relax? Tonight is his first meeting with Bruce and his first time playing along."
    ls "Oh come on. He isn't a baby anymore, are you [pov]? hehehe."
    pov "Hey..."
    mom "Okay. But you need to stay at home until I come back from town, okay?"
    ls "Yes mom!"
    mom "Good, I'm counting on you."
    ls "Mom!"
    scene intro 029
    if inc == True:
        ls "Ok, come with me, big brother. I'll show you the way."
        mom "I'll be in town for a while. You can stay with your sister."
    else:
        ls "Ok, come with me, [pov]. I'll show you the way."
        mom "I'll be in town for a while. You can stay with [ls]."
    mom "And please keep in mind what we talked about."
    ls "I'm not sure he can do it. Maybe you need to explain again. Very slowly this times so he understands..."
    pov "...?"
    ls "<giggle>"
    mom "[ls]!"
    if inc == True:
        pov "Okay, let's go. See you later mom."
    else:
        pov "Okay, let's go. See you later [mother]."
    scene black
    "You walk upstairs to your new room."
    scene intro 030
    ls "And this is your new small bed. Only for \"one\" person!"
    ls "But I'm so cozy, maybe I'll keep this one too. You can sleep outside. Don't you think that's a good idea?"
    pov "Ha... ha... ha..."
    pov "I must say, you've changed so much. I'm very surprised."
    ls "Yes, I'm a big girl now. You missed a lot while you were away."
    pov "I'm sorry about that. So do you have your first boyfriend too?"
    ls "Haha, no... I didn't mean that..."
    povi "Damn she grown up a lot. And she's pretty hot too, unbelievable."
    scene intro 031
    povi "She's prett out going. Although she's still sticking her tongue out at me all the time."
    scene intro 032
    povi "Her boobs have grown so much. I kinda want to squeeze them."
    scene intro 033
    povi "Those cute little feet too..."
    if inc == True:
        povi "Damn it. Maybe mom was right. I need a girlfriend."
    else:
        povi "Damn it. Maybe [mother] was right. I need a girlfriend."
    scene intro 034
    ls "Huh...?"
    pov "What's wrong?"
    ls "Why are you staring at me like that?"
    pov "Like what...?"
    ls "I dont know... like a pervert?!"
    povi "Haha, you're so right."
    pov "I'm just admiring how beautiful you've become."
    scene intro 035
    if inc == True:
        ls "But you're my brother. You shouldn't look at me like that!"
        pov "Why not. You're my beautiful sister. Is there something wrong?"
        ls "It's like boys looking for girlfriends. We're siblings, we aren't allowed to do such things."
    else:
        ls "But I know you since our childhood. You shouldn't look at me like that!"
        pov "Why not. You're my beautiful friend. Is there something wrong?"
        ls "It's like boys looking for girlfriends. We're know each other for so long, so we shouldn't do such things."
    pov "I didn't mean that. It's just been a full year since I saw you last and you've grown so much is all."
    if inc == True:
        povi "Well that is interesting! She doesn't seem to be against the idea completely, just worried that it's forbidden. Not something she doesn't want to do."
    else:
        povi "Well that is interesting! She doesn't seem to be against the idea completely, just worried that it's something we shouldn't do. Not something she doesn't want to do."
    ls "I need to go now!"
    pov "Wait, already!"
    scene intro 036
    pov "..."
    povi "We'll have to see how things go between us. There might be something to explore there."
    pov "Yawn..."
    povi "Damn it. I'm really tired all the sudden. Must be the trip home getting to me."
    if inc == True:
        povi "But I'm so damn curious what will happen tonight. What is dad up to. Becoming an undercover cop, where did that come from?"
        povi "And mom playing along with all this perverted shit? Nude, kinky pictures in the house? I never would have believed it without see it first hand."
    else:
        povi "But I'm so damn curious what will happen tonight. What is Bruce up to. Becoming an undercover cop, where did that come from?"
        povi "And [mother] playing along with all this perverted shit? Nude, kinky pictures in the house? I never would have believed it without see it first hand."
    povi "I must have missed a lot! Good thing that [ls] seems relatively unscathed."
    povi "And I wonder how [bs] plays along with all of this?"
    pov "YAWN..."
    scene black
    "You fall asleep."
    "Some time later..."
    "KNOCK! KNOCK! KNOCK!"
    povi "WTF?"
    pov "Yes, who's there?"
    ls "Open the door [pov]. Get you lazy ass out bed!"
    povi "Damn it."
    scene intro 037
    pov "What are you wearing?"
    ls "It's my pajamas, stupid!"
    pov "But... what time is it?"
    ls "It's already nighttime. I was about to go to sleep, but you have a date right now."
    pov "A date... with you?"
    scene intro 038
    ls "Uh... no. Do you have some brain damage or something?"
    ls "Remember what you talked to mom about before?"
    pov "Oh...!"
    pov "Yes, you're right. Thank you for waking me."
    scene intro 039
    ls "No problem. I don't envy you. I bet it's going to be damn boring, because I'm not there! Hehe."
    ls "And mom told me that dad's friends are stupid idiots too."
    pov "..."
    povi "Damn. I can't take my eyes off her. Even without makeup she's really sexy."
    povi "And her cute belly."
    scene intro 041
    ls "You doing it again..."
    pov "I can't help it! It's totally your fault wearing pajamas like that. Haha!"
    ls "Hmpf..."
    scene intro 042
    povi "Hmm... I hope she won't get too mad at me."
    scene black
    if inc == True:
        "You go downstairs to meet with your dad."
        scene intro 043
        povi "WTF? Mom? What are you wearing?"
    else:
        "You go downstairs to meet with them."
        scene intro 043
        povi "WTF? [mother]? What are you wearing?"
        povi "And who the fuck are these creepy dudes?"
    scene intro 044
    if inc == True:
        dad "There he is! My son!"
    else:
        dad "There he is!"
    mom "Oh you're here [pov]."
    pov "..."
    dad "You seem a bit surprised there boy?"
    scene intro 045
    if inc == True:
        pov "Hey dad."
    else:
        pov "Hey Bruce."
    dad "Come here. Let me see how you've grown up!"
    mom "I'm so proud. He's becoming a fine young man."
    scene intro 046
    if inc == True:
        dad "Becoming so strong. Like father like son, hahaha."
        povi "What the hell? Dad even got a tattoo for his undercover role?"
    else:
        dad "Becoming so strong. Like the son I always wanted, hahaha."
        povi "What the hell? Bruce even got a tattoo for his undercover role?"
    pov "Yeah..."
    dad "Let me introduce you to my friends. You're gonna what to know these guys."
    scene intro 047
    dad "On your right is \"Steve\", the muscle mountain."
    steve "Hey bro!"
    dad "And sitting by [mother] is \"Davide\", who is very proud of his name."
    davide "Hey, I'm a very famous man."
    povi "Davide? You must be kidding..."
    pov "Hey..."
    mom "No need to be shy [pov]. They're good friends of mine too."
    if inc == True:
        povi "Damn mom, what's gotten into you. I know this is just a role, but you're playing slutty way too well."
    else:
        povi "Damn [mother], what's gotten into you. I know this is just a role, but you're playing slutty way too well."
    povi "Are you drunk or on drugs?"
    scene intro 048a
    povi "Her breasts are even more exposed. Practically falling out of that dress."
    scene intro 048b
    povi "And is that tiny string panties?! Barely covering her pussy. Damn, she's shaved?"
    povi "Fuck, there I go again. Shit at this point I might as well just go with it. I'm clearly a bigger pervert than I thought."
    bs "Hey everyone!"
    scene intro 049
    povi "Oh my god! Is that [bs]?"
    dad "Oh hey honey, you're back."
    if inc == True:
        mom "Look, you're brother is here."
    else:
        mom "Look, who's here."
    scene intro 050
    bs "Oh, hello pervert!"
    pov "Hey... [bs]"
    povi "Damn, she's dressed so slutty too."
    bs "Stop staring, [pov]!"
    dad "Hahaha, [bs] has a point."
    if inc == True:
        mom "[pov] is just surprised seeing his sister after a long year."
    else:
        mom "[pov] is just surprised seeing her after a long year."
    bs "Sure..."
    scene intro 051
    bs "Hey daddy!"
    bs "*kiss*"
    dad "Good you're home honey."
    povi "I think she's putting a little too much effort into this role-play."
    scene intro 052
    bs "So I came at just the right moment."
    bs "Hey there, fellas."
    scene intro 053
    steve "Hey there, goodlooking!"
    davide "Yes, she's just like her mom. The same curves!"
    povi "What the fuck!"
    scene intro 054
    if inc == True:
        povi "Is this asshole groping mom's tits!"
        povi "And mom doesn't seem to care? What the hell is going on here?"
    else:
        povi "Is this asshole groping [mother]'s tits!"
        povi "And mom doesn't seem to care? What the hell is going on here?"
    scene intro 055
    mom "Oh...?"
    davide "Not as large as her mother, but there are ways to help with that."
    if inc == True:
        povi "They must have given her something. Letting her tits get groped by one of dad's \"friends\". She was always so conservative before and now something like this?"
        povi "But dad wouldn't do such a thing to her! Why doesn't he interfere? That can't be a part of their undercover role!"
    else:
        povi "They must have given her something. Letting her tits get groped by one of Bruce's \"friends\". She was always so conservative before and now something like this?"
        povi "But Bruce wouldn't do such a thing to her! Why doesn't he interfere? That can't be a part of their undercover role!"
    scene intro 056
    mom "You're being a little bit handsie Davide."
    davide "Oh, I didn't notice, hahaha."
    dad "Hahaha, no problem, dude. You're just heavy drunk, right?!"
    povi "Are you fucking kidding me?"
    scene intro 057
    bs "Oh you're having fun partying without me?"
    bs "That's not fair, haha."
    povi "Hm... normally that would sound more like [bs]. But partying with this scum?"
    scene intro 058
    bs "Please let me stay with you this time, daddy!"
    steve "Yeah, it would be more fun with your hot daughter here too."
    davide "I'll stay with [mother], haha."
    mom "Oh, you..."
    dad "We talked about this. When we have a place for you in the gang we can see then."
    bs "But! Please daddy...!"
    dad "No! Now go to your room and don't bother us anymore!"
    scene intro 059
    bs "Hmpf..."
    steve "Wohoo, chica!"
    mom "Don't be mad about your dad [bs]."
    povi "At least something seems right."
    povi "I nearly forgot who she was with all the changes around here!"
    davide "How about you bring us some drinks, bitch!"
    mom "Okay..."
    povi "WHAT?!"
    scene intro 060
    davide "*slap* Move that ass!"
    mom "Hah..."
    pov "Who the fuck do you think you are, asshole!"
    scene intro 061
    davide "What...?"
    mom "Oh no... [pov]!"
    steve "Huh?"
    scene intro 062
    davide "What did you say, you little fucker?"
    davide "I'll rip your legs off!"
    pov "You're welcome to try, dipshit!"
    steve "Now you're fucked boy!"
    mom "Please calm down. He just didn't know."
    dad "Let me clarify the issue!"
    scene intro 063
    pov "Huh?"
    with vpunch
    scene black
    "You got knocked out."
    pov "..."
    dad "Oh, you're waking up..."
    scene intro 065
    if inc == True:
        pov "What the fuck... You punched me dad!"
    else:
        pov "What the fuck... You punched me!"
    dad "Yes, for your own safety."
    if inc == True:
        pov "What are you talking. That wasn't right how they were treating mom and you did nothing."
    else:
        pov "What are you talking. That wasn't right how they were treating [mother] and you did nothing."
    dad "I thought she explained it clearly to you!"
    pov "She talked to me a bit, but these things..."
    scene intro 064
    if inc == True:
        dad "These things are necessary and your mom knows that and supports me on this."
        dad "If I didn't take care of you just now, Davide would have. And then you would have woke up in the hospital, if you're lucky."
        pov "But he was touching mom like she was some slut off the corner!"
    else:
        dad "These things are necessary and [mother] knows that and supports me on this."
        dad "If I didn't take care of you just now, Davide would have. And then you would have woke up in the hospital, if you're lucky."
        pov "But he was touching [mother] like she was some slut off the corner!"
    dad "Yes he did. But these are things that happen when you're drunk with your friends."
    pov "Seriously, that's your answer when some guy molests your wife in front of you..."
    dad "I know these guys are scum and normal people would avoid them. But it's my work and it has to be done."
    if inc == True:
        pov "But mom..."
        dad "Your mom agreed to this stuff and we've done our best to keep your sisters out of it."
    else:
        pov "But [mother]..."
        dad "[mother] agreed to this stuff and we've done our best to keep our daughters out of it."
    povi "He must be insane..."
    dad "So now pay attention, this is IMPORTANT."
    dad "We, I and [mother] knew that it would be hard for you to accept, so it was a good coincidence that you were away this year."
    if inc == True:
        povi "Are you serious, mom supports this?"
        dad "But now that you're here, behavior like that will bring the whole family trouble. Me, your mom and even your sisters."
        povi "He does has a point... but still."
        dad "So I hope instead you will join us and play the son of a criminal, maybe you can help keep everyone safe too."
    else:
        povi "Are you serious, [mother] supports this?"
        dad "But now that you're here, behavior like that will bring the whole family trouble. Me, [mother] and even my daughters."
        povi "He does has a point... but still."
        dad "So I hope instead you will join us and play the son of a criminal, maybe you can help keep everyone safe too."
    pov "So I should act as a macho scum asshole?"
    dad "Yes, that would be the right description!"
    pov "Treating women like shit and playing god?"
    dad "It would be just an act. And it only needs to be when my \"friends\" are around."
    dad "And if you don't want to participate, we can figure out a place for you to stay away until we end this."
    dad "It won't last long anymore. We're going to get results soon."
    pov "Soon... like how soon?"
    scene intro 066
    dad "Soon! But I need you to understand something. If we ruin this and they find out who we are... they will kill us!"
    if inc == True:
        dad "Or do worse to your mom and sisters."
        pov "I understand that but I still don't understand why you brought them into this position in the first place?!"
        dad "Your mom and I both decided this."
        pov "Mom decided to bring my sisters into danger...?"
    else:
        dad "Or do worse to [mother] and our daughters."
        pov "I understand that but I still don't understand why you brought them into this position in the first place?!"
        dad "[mother] and I both decided this."
        pov "[mother] decided to bring your daughters into danger...?"
    dad "That's enough! This isn't a discussion. Bottom line, you play along or we have to kick you out of the house."
    povi "I can't still believe this shit."
    dad "If you decide to stay, you'll need to help around the house and start earning your own money."
    dad "But were you finished school so I'm sure you'll find a job. Just remember that we are posing as a poor family, you start earn real money you need to keep that to yourself."
    povi "Maybe I should play along, I can't reveal his cover and for the sake of the rest of them. But would it be the worst thing that happened, if they really did kick me out?"
    pov "Look, sorry I freaked out. I'll seriously think about what you've told me. Either way I promise I won't break your cover."
    scene intro 067
    dad "Good! It's good that you're beginning to understand."
    dad "It wasn't planned for it to go this way, but now is it we have to deal with it."
    pov "So... let me get this straight though. You aren't the boss of this little gang runnging out of your house?"
    dad "Don't make fun of me! [mother] and I decide to take this chance because of what it will do for our family when this if over. Its called sacrifice."
    povi "Maybe I should give it a rest. He seems sad enough about this sistuation. Still, I'm not sure that he isn't just playing. Maybe he enjoys his undercover game a little too much."
    if inc == True:
        povi "He's always been a good man, but we aren't his real kids, he is just our step-dad. And I don't know everything about him."
        povi "For all I know he could be trying to take advantage of one of my sisters. If he's willing to do something this crazy, who knows what kind of messed up shit he could be into."
    povi "I think I'll stay and see where this all goes. Pretend to play his little game for now at least."
    dad "Davide is the boss, Steve and I are his right and left hands. And Steve isn't such a bad guy."
    pov "So the boss seem to have some privileges around here..."
    dad "What do you mean?"
    pov "You know exactly what I mean!"
    if inc == True:
        dad "There is nothing between your mother and him. He just likes to joke around sometimes."
    else:
        dad "There is nothing between [mother] and him. He just likes to joke around sometimes."
    povi "I don't know, he doesn't seem to think he was playing when he was touching here like that!"
    pov "Okay. I understand. Just give me the night to think things over."
    scene intro 068
    dad "Good! I'm glad that I can count on you!"
    dad "I really could use your help and it would be a waste to have to kick you out."
    pov "We're okay?"
    dad "Everything will be fine after this job and if everything goes to plan, we'll be able to retire and move somewhere real nice. The whole family!"
    scene intro 069
    dad "I need to get something from my car."
    dad "It's probably better if you go on and go to your room to think about everything."
    if inc == True:
        pov "Okay... dad..."
        dad "I'm proud of you... Son!"
    else:
        pov "Okay... Bruce..."
        dad "I'm proud of you!"
    scene intro 070
    "You go back upstairs to your room."
    "Your brain properly mind fucked."
    if NTR == True:
        povi "Hmm... is there something coming from the basement?"
        mom "Aaahh... hah... hah..."
        if inc == True:
            povi "WTF? Is that mom's voice? Sounds... sexual..."
        else:
            povi "WTF? Is that [mother]'s voice? Sounds... sexual..."
        scene intro 071
        povi "I need to check!"
        povi "Damn, it won't open. But I need to get in!"
        povi "Strange, I don't hear it anymore... Maybe I was wrong?"
        if inc == True:
            povi "Dad is coming back. Better leave it alone for now!"
        else:
            povi "Bruce is coming back. Better leave it alone for now!"
    jump tutorial
