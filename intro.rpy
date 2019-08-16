

label intro:
    if gamemusic == True:
        stop music fadeout 2
        play music "music/intro.mp3"
    scene black
    window show
    n "You're a young man who returns from his year as an exchange student. It was your last year of school and you come home to find a job."
    if inc == True:
        n "Now your driving in a taxi to a new address, after you learned that your family moved."
    else:
        n "Now your driving in a taxi to a new address, after you learned that the family you lived with moved."
    window hide
    nvl clear
    scene intro 000
    $ pov = renpy.input(_("So what is your first name?")) or _("Sam")
    pov "{i}Finally the last miles from returning home after not seeing them for over a year.{/i}"
    pov "{i}At first I have to teach them how to use Skype correctly. Even when it's somewhat unrealistic that they couldn't get it working.{/i}"
    pov "{i}I mean they aren't that stupid.{/i}"
    pov "{i}But I can't even be mad at them after staying away from home so long.{/i}"
    scene intro mom intro
    if inc == True:
        pov "{i}I wonder how mom's doing? Is she still mothering us all?{/i}"
        "So what's your mom's name?"
        $ mother = renpy.input(_("You'll call her mom, but it's need when others call her.")) or _("Nicole")
    else:
        pov "{i}I wonder how's mom's best friend doing? Is she still mothering us all?{/i}"
        $ mother = renpy.input(_("So what's the name of your mom's childhood friend?")) or _("Nicole")
    pov "{i}And I miss her so much.{/i}"
    scene intro lil sis intro
    if inc == True:
        pov "{i}Lil' sis'? Still hanging' around me all the time, trying to impress.{/i}"
    else:
        pov "{i}And her youngest daughter? Still hanging' around me all the time, trying to impress.{/i}"
    pov "{i}I sometimes wonder if she wants to be a boy.{/i}"
    if inc == True:
        $ ls = renpy.input(_("So what's your little sister's name?")) or _("Alexis")
    else:
        $ ls = renpy.input(_("So what's your younger childhood friends name?")) or _("Alexis")
    pov "{i}It'll be fun to make a little fool of her again, when she try's to impress me again.{/i}"
    scene intro big sis intro
    if inc == True:
        pov "{i}And then there is big sis'.{/i}"
        $ bs = renpy.input(_("So what's your big sister's name?")) or _("Cassandra")
    else:
        pov "{i}And then there is the older friend'.{/i}"
        $ bs = renpy.input(_("So what's your older childhood friends name?")) or _("Cassandra")
    pov "{i}I wonder if she will still denounce me as a little pervert.{/i}"
    pov "{i}But maybe her hate is gone after my long absence.{/i}"
    scene black
    if inc == True:
        pov "{i}And dad. Takes such care of us all. I wonder how it would be if he wasn't only our step-dad?{/i}"
    else:
        pov "{i}And their dad. Takes such care of us all. I wonder how it would be if he was my real dad?{/i}"
    "Driver" "Hey wake up!"
    pov "What...?"
    pov "{i}I was asleep?{/i}"
    pov "Oh sorry. Here's your money."
    window show
    n "You can skip the intro, but it this is your first time playing the game it's not recommenend"
    n "Do you want to skip the intro?"
    menu:
        "Yes":
            jump tutorial
        "No":

            pass
    window hide
    nvl clear    
    scene intro 001
    pov "{i}Oh...? Are they...?{/i}"
    pov "{i}Wow... They've changed...{/i}"
    pov "{i}But what's with the weird house. It looks somewhat cheap.{/i}"
    scene intro 002
    pov "{i}Oh they saw me.{/i}"
    mom "[pov]!"
    ls "Finally you've arrived."
    pov "{i}But what are they wearing? It's somewhat revealing.{/i}"
    if inc == True:
        pov "{i}I never thought mom would show such cleavage in public.{/i}"
    else:
        pov "{i}I never thought [mother] would show such cleavage in public.{/i}"
    scene intro 003
    if inc == True:
        ls "Brother!"
    else:
        ls "[pov]!"
    pov "[ls]!"
    pov "{i}She's wearing makeup. Finally growing up.{/i}"
    scene intro 004
    ls "I missed you so much!"
    if inc == True:
        pov "I missed you too, lil' sister."
    else:
        pov "I missed you too, [ls]."
    ls "We have so much to catch up on."
    pov "But you still had [bs]?"
    ls "No. She isn't fun like you."
    scene intro 005
    mom "Now it's my turn. I'm so proud."
    if inc == True:
        pov "Oh, mom."
        scene intro 006
        mom "My only son finished his schooling overseas. Making his mother so proud."
        pov "Calm down mom. It wasn't that hard. I'm not a little boy anymore."
    else:
        pov "Oh, [mother]."
        scene intro 006
        mom "The only son of my best friend finished his schooling overseas. Making his mother and me so proud."
        pov "Calm down [mother]. It wasn't that hard. I'm not a little boy anymore."
    mom "I missed you so much. It's so good that you'll be staying around now and can help us."
    pov "Yes I can. Don't worry. I missed you too."
    scene intro 007
    mom "Come on in. We'll show you our new home."
    pov "{i}I wonder why they ended up here. But I can't talk bad about it otherwise or they would get very angry.{/i}"
    pov "Sure!"
    ls "Come on [pov]!"
    pov "And where is [bs]?"
    mom "Oh she's with her boyfriend in town. You'll meet her later."
    if inc == True:
        pov "Typical big sister."
    else:
        pov "Typical [bs]."
    scene intro 008
    pov "{i}With her boyfriend... He'll loose her to me, hahaha.{/i}"
    ls "Are you coming?"
    mom "Yes, relax. No need to hurry."
    scene intro 009
    pov "{i}What a view! Showing off that great cleavage.{/i}"
    pov "{i}I wonder what happened that's made her so open now?{/i}"
    scene intro 010
    mom "Let's go in."
    pov "Okay."
    scene intro 011
    pov "{i}And that curvy ass. I want to grab it!{/i}"
    pov "{i}Damn. She's so sexy right now!{/i}"
    scene intro 012
    pov "What...?"
    mom "Hnnn..."
    pov "{i}What's with the picture?{/i}"
    scene intro 013
    pov "{i}Was it taken in a strip club? It's like porn.{/i}"
    pov "{i}In the living room. Who would hang something perverted there?{/i}"
    if inc == True:
        pov "{i}Mom would never allow that!{/i}"
    else:
        pov "{i}[mother] would never allow that!{/i}"
    scene intro 014
    pov "Ahem... is that...?"
    if inc == True:
        mom "Your dad hung it up. He's into these things lately."
    else:
        mom "Bruce hung it up. He's into these things lately."
    pov "And you're okay with that...?"
    ls "She isn't even naked. And dad calls it art, but mom is so prudish. <giggle>"
    mom "Hnn..."
    scene intro 015
    mom "I'll explain it! But let's go to the kitchen!"
    pov "To the kitchen?"
    mom "Yes! No need to stay here."
    ls "Hihihi..."
    scene intro 016
    pov "Oh the dining room."
    mom "It's wonderful isn't it?"
    pov "And a \"normal\" picture in there."
    mom "Yes, I like it too."
    scene intro 017
    mom "Come on. Next room is the kitchen."
    pov "{i}Hmm... is [ls] trying to give me a hint?{/i}"
    scene intro 018
    pov "Holy...!"
    pov "{i}Another perverted picture. And this time in BDSM style.{/i}"
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
    pov "{i}Damn. How can I prevent a boner when I see these hot pictures all the time.{/i}"
    scene intro 020
    mom "So tell me how you liked your school? You had a good graduation, that made me proud."
    pov "It was okay. All the schools are the same... boring!"
    mom "Haha, you don't need to play it cool. You're an adult now."
    pov "Haha, yes."
    mom "We'll talk more later, I have to go soon but first there is something urgent to talk about."
    pov "Urgent?"
    scene intro 021
    mom "Yes, it's about living in this house, a downgrade from our old one and what's the reason for it."
    if inc == True:
        mom "Your dad will introduce you further tonight, but this I can tell you now."
    else:
        mom "Bruce will introduce you further tonight, but this I can tell you now."
    pov "Did he lose his job?"
    mom "No, he's doing something that will bring him a much higher rank and us a good pension plan."
    mom "We're living with him \"undercover\" for almost a year in this house and this will soon come to an end."
    pov "But he was only a patrolman?"
    mom "Yes, but they gave him a chance and he took it, for the best of our family."
    pov "So who's he going to catch with this camouflage?"
    scene intro 022
    mom "The good thing is there aren't really dangerous criminals, the bad thing is there are \"white trash\" criminals."
    mom "Perverted macho's. That's the reason for the pictures in the house. They like this garbage."
    pov "And you changed you're appearance too?"
    mom "Yes, we all decided to help him with this. It's all for a better outcome."
    mom "And it's essential for all our safeties that you play along with that. At least until he speaks with you."
    mom "If they reveal him to be a cop they could hurt us all really bad."
    if inc == True:
        pov "Hmm... I'm a bit surprised that dad set you up in that kind of danger."
    else:
        pov "Hmm... I'm a bit surprised that Bruce set you up in that kind of danger."
    pov "But if you've covered nearly a year, I won't mess it up."
    scene intro 023
    mom "Good! I knew we could count on you."
    pov "That's the reason that your wear this revealing clothes?"
    mom "Yes... It was unpleasant at the beginning, but I got used to it. And it could be worse."
    mom "And we managed to hold [ls] out of the most, she has to stay in her room at night when they come by."
    pov "Oh, so she's changing as she grows up."
    mom "Haha, yes. I won't allow it to get her involved with that scum."
    pov "And [bs]?"
    mom "She's an adult. She can watch on her own and her boyfriend isn't one of them."
    pov "Her boyfriend?"
    scene intro 024
    mom "Yes a nice boy, very handsome. I'm glad she found someone."
    pov "..."
    mom "So it would also be a good time that you found a girlfriend too, don't you think?"
    pov "Why? I have a fine hot girl here!"
    scene intro 025a
    mom "What...?"
    pov "Letting me have a good view of her fine boobs and shaking her ass!"
    mom "You're talking about me?"
    pov "Of course! Wouldn't it be great if we had some intimate fun together?"
    mom "What's gotten into you...?"
    pov "Hahaha. I'm a good trashy, macho, aren't I?"
    scene intro 025b
    mom "Hnn... you're joking?"
    pov "You believed that?"
    mom "..."
    if inc == True:
        mom "It was good, but don't talk about that incest thing. I don't like that, it's too strange!"
        pov "{i}Damn it. I hoped it would work.{/i}"
        pov "Okay, sorry mom."
    else:
        mom "It was good, but don't talk about that thing. I don't like that, it's too strange!"
        pov "{i}Damn it. I hoped it would work.{/i}"
        pov "Okay, sorry [mother]."
    scene intro 026
    ls "You done talking?"
    ls "I want to show [pov] his room. So he can move in and we can do something together."
    pov "{i}\"Do something together...\" Damn, I must get rid of these thoughts.{/i}"
    scene intro 027
    ls "His \"small\" but \"cozy\" room. In this modest home, hihi."
    pov "So you got the bigger room?"
    ls "Yes because now I'm the better one."
    pov "Haha, you wish..."
    ls "You'll see! <giggle>"
    scene intro 028
    if inc == True:
        mom "How about you let him relax? Tonight is his first meeting with dad and his first time playing along."
    else:
        mom "How about you let him relax? Tonight is his first meeting with Bruce and his first time playing along."
    ls "Oh come on. He isn't a baby anymore, hihihi."
    pov "Hey..."
    mom "Okay. But you'll stay at home until I come back from town, okay?"
    ls "Yes mom!"
    mom "Good, I'm counting on you."
    ls "Mom!"
    scene intro 029
    if inc == True:
        ls "Then come with me, big brother. I'll show you the way."
        mom "I'll be in town for a while. You can stay with your sister."
    else:
        ls "Then come with me, [pov]. I'll show you the way."
        mom "I'll be in town for a while. You can stay with [ls]."
    mom "And please keep in mind what we're talking about."
    ls "I'm not sure he can do it. Maybe you need to explain it very slowly again."
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
    ls "But I'm so cozy, maybe I can occupy it too. You can sleep outside, don't you think?"
    pov "Haha... haha..."
    pov "I must say, you've changed so much. I was very surprised."
    ls "Yes, I'm a big girl now. You missed much while you were away?"
    pov "Oh, you have you're first boyfriend?"
    ls "Haha, no... I didn't mean that..."
    pov "{i}Damn she grown up to be such a hot girl, unbelievable.{/i}"
    scene intro 031
    pov "{i}She's gotten so beautiful and showing me her lewd tongue.{/i}"
    scene intro 032
    pov "{i}Her boobs have grown so much. I want to squeeze them.{/i}"
    scene intro 033
    pov "{i}Those cute little sexy feet. So lick-able.{/i}"
    scene intro 034
    ls "Huh...?"
    pov "What's wrong?"
    ls "Why are you staring at me like that?"
    pov "Like what...?"
    ls "Like a pervert!"
    pov "{i}Haha, you're so right.{/i}"
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
    pov "Oh I wasn't up to that. I just saw you last time a year before."
    if inc == True:
        pov "{i}Damn it! At least she doesn't seem to stay against it, just worried that it's forbidden.{/i}"
    else:
        pov "{i}Damn it! At least she doesn't seem to stay against it, it's just wrong for her.{/i}"
    ls "I need to go now!"
    pov "Wait!"
    scene intro 036
    pov "..."
    pov "{i}The good thing is I have time to work on her now, haha.{/i}"
    pov "Yawn..."
    pov "{i}Damn it. I'm really tired.{/i}"
    if inc == True:
        pov "{i}But I'm so damn curious what will happen tonight. What is dad up to. Becoming an undercover cop, what the fuck?{/i}"
        pov "{i}And mom playing along with all this perverted shit? Nude, perverted pictures in the house?{/i}"
    else:
        pov "{i}But I'm so damn curious what will happen tonight. What is Bruce up to. Becoming an undercover cop, what the fuck?{/i}"
        pov "{i}And [mother] playing along with all this perverted shit? Nude, perverted pictures in the house?{/i}"
    pov "{i}I must have missed a lot! Good thing that [ls] stayed innocent.{/i}"
    pov "{i}And I wonder how [bs] plays along with all of this?{/i}"
    pov "YAWN..."
    scene black
    "You fall asleep."
    "Some time later..."
    "KNOCK! KNOCK! KNOCK!"
    pov "{i}WTF?{/i}"
    pov "Yes, who's there?"
    ls "Open the door [pov]. No need to sleep any more."
    pov "{i}Damn it.{/i}"
    scene intro 037
    pov "What are you wearing?"
    ls "It's my sleepwear, stupid!"
    pov "But... what time is it?"
    ls "It's already night. I was about to go to sleep, but you have a date right now."
    pov "A date... with you?"
    scene intro 038
    ls "Got some brain damage?"
    ls "Hello! What did you talk about with mom before?"
    pov "Oh...!"
    pov "Yes you're right. Thank you for waking me."
    scene intro 039
    ls "I don't envy you. I bet it's damn boring, because I'm not there, hihi."
    ls "And mom told me that dad's friends are stupid idiots too."
    pov "..."
    pov "{i}Damn. I can't take my eyes off her. Even without makeup she's damn sexy.{/i}"
    pov "{i}And her cute belly.{/i}"
    scene intro 041
    ls "You did it again."
    pov "It's your fault wearing such sleepwear, haha."
    ls "Hmpf..."
    scene intro 042
    pov "{i}Hmm... I hope she won't get too mad at me.{/i}"
    scene black
    if gamemusic == True:
        stop music fadeout 1
        play music "music/NTR.mp3"
    if inc == True:
        "You go downstairs to meet with your dad."
        scene intro 043
        pov "{i}WTF? Mom? What's she wearing?{/i}"
    else:
        "You go downstairs to meet with them."
        scene intro 043
        pov "{i}WTF? [mother]? What's she wearing?{/i}"
        pov "{i}And these creepy dudes?{/i}"
    scene intro 044
    if inc == True:
        dad "There he is! My son!"
    else:
        dad "There he is!"
    mom "Oh you're here [pov]."
    pov "..."
    dad "Oh you seem surprised?"
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
        pov "{i}What the hell? Dad even got a tattoo for his undercover role?{/i}"
    else:
        dad "Becoming so strong. Like my son when I would had one, hahaha."
        pov "{i}What the hell? Bruce even got a tattoo for his undercover role?{/i}"
    pov "Yeah..."
    dad "Let me introduce you to my friends. You're really need to know them."
    scene intro 047
    dad "On your right is \"Steve\", the muscle mountain."
    steve "Hey bro!"
    dad "And sitting with [mother] is \"Davide\", who is very proud of his name."
    davide "Yeah I'm a very famous guy."
    pov "{i}Davide? You must be kidding...{/i}"
    pov "Hey..."
    mom "No need to be shy [pov]. They're good friends of mine too."
    if inc == True:
        pov "{i}Damn mom, what's gotten into you. You can't be playing this slutty.{/i}"
    else:
        pov "{i}Damn [mother], what's gotten into you. You can't be playing this slutty.{/i}"
    pov "{i}Are you drunk or on drugs? I can't believe this!{/i}"
    scene intro 048a
    pov "{i}Her boobs are even more exposed. Almost falling out of that dress.{/i}"
    scene intro 048b
    pov "{i}And that tiny string. Almost covering her pussy. Damn, she's shaved?{/i}"
    bs "Hey everyone!"
    scene intro 049
    pov "{i}Oh my god! Is that [bs]?{/i}"
    dad "Oh hey honey, you're back."
    if inc == True:
        mom "Look, you're brother is here."
    else:
        mom "Look, who's here."
    scene intro 050
    if inc == True:
        bs "Oh, hello stupid brother!"
    else:
        bs "Oh, hello stupid!"
    pov "Hey... [bs]"
    pov "{i}Damn, she's so slutty too.{/i}"
    bs "Stop staring, pervert!"
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
    pov "{i}I think she's showing a little to much effort in this role-play.{/i}"
    scene intro 052
    bs "So I came at the right moment."
    bs "Hey there, handsome guys."
    scene intro 053
    steve "Hey there, hot chick!"
    davide "Yes, she's just like her mom. The same curves!"
    pov "{i}What the fuck!{/i}"
    scene intro 054
    if inc == True:
        pov "{i}This asshole is groping mom's tits!{/i}"
        pov "{i}And mom doesn't care? What the hell is going on here?{/i}"
    else:
        pov "{i}This asshole is groping [mother]'s tits!{/i}"
        pov "{i}And she doesn't care? What the hell is going on here?{/i}"
    scene intro 055
    mom "Oh...?"
    davide "Yes not as fine boobs as her mother, but there are ways to help with that."
    if inc == True:
        pov "{i}They must have given her something. Letting her tits get groped by one of dad's \"friends\". Always so prudish and now something like this?{/i}"
        pov "{i}But dad wouldn't do such a thing to her! But why doesn't he interfere? That can't be part of their undercover role!{/i}"
    else:
        pov "{i}They must have given her something. Letting her tits get groped by one of Bruce's \"friends\". Always so prudish and now something like this?{/i}"
        pov "{i}But Bruce wouldn't do such a thing to her! But why doesn't he interfere? That can't be part of their undercover role!{/i}"
    scene intro 056
    mom "You're a little bit too touchy."
    davide "Oh, I didn't notice, hahaha."
    dad "Hahaha, no problem, dude. You're just heavy drunk!"
    pov "{i}Are you fucking kidding me?{/i}"
    scene intro 057
    bs "Oh you're having fun with alcohol and stuff without me?"
    bs "That's not fair, haha."
    pov "{i}Hm... normally that would fit on [bs]. But with this scum?{/i}"
    scene intro 058
    bs "Please let me stay with you this time, daddy!"
    steve "Yes it would be more fun with your hot daughter too."
    davide "I'll stay with [mother], haha."
    mom "Oh, you..."
    dad "We talked about this. When you can fulfill your duties finally we'll see."
    bs "But! Please daddy...!"
    dad "No! Now go to your room and don't bother us anymore!"
    scene intro 059
    bs "Hmpf..."
    steve "Wohoo, chica!"
    mom "Don't be mad about your dad [bs]."
    pov "{i}At least something seems right.{/i}"
    pov "{i}Her changes made her so damn sexy! I must know what happened, hell yeah!{/i}"
    davide "How about you bring us some drinks, bitch!"
    mom "Okay..."
    pov "{i}WHAT?!{/i}"
    scene intro 060
    davide "*slap* Move that ass!"
    mom "Hah..."
    pov "What the fuck is wrong with you, MOTHERFUCKER!"
    scene intro 061
    davide "What...?"
    mom "Oh no... [pov]!"
    steve "Huh?"
    scene intro 062
    davide "What did you say, you little fucker?"
    davide "I'll rip your legs off!"
    steve "You're fucked boy!"
    mom "Please calm down. He just didn't know."
    dad "I'll clarify it!"
    scene intro 063
    pov "Huh?"
    with vpunch
    scene black
    "You got knocked out."
    pov "..."
    dad "Oh, you're coming back."
    scene intro 065
    if inc == True:
        pov "What... You punched me dad!"
    else:
        pov "What... You punched me!"
    dad "Yes, for your own safety."
    pov "What are you talking. This wasn't right and you did nothing."
    if inc == True:
        dad "I thought your mom explained it clearly to you!"
    else:
        dad "I thought [mother] explained it clearly to you!"
    pov "She talked to me, but these things..."
    scene intro 064
    if inc == True:
        dad "These things are necessary and your mom knows that and supports me on this."
        dad "If I didn't take care of you, Davide would have. And then you would have woke up in the hospital, you're lucky."
        pov "But he touched mom!"
    else:
        dad "These things are necessary and [mother] knows that and supports me on this."
        dad "If I didn't take care of you, Davide would have. And then you would have woke up in the hospital, you're lucky."
        pov "But he touched her!"
    dad "Yes he did. But these are things that happen when you're drunk with your friends."
    pov "But..."
    dad "I know these guys are scum and normal people would avoid them. But it's my work so it has to be done."
    if inc == True:
        pov "But mom..."
        dad "Your mom agreed to this stuff and we've done our best to keep your sisters out of it."
    else:
        pov "But [mother]..."
        dad "[mother] agreed to this stuff and we've done our best to keep our daughters out of it."
    pov "{i}He must be insane...{/i}"
    dad "So now pay attention, this is IMPORTANT."
    dad "We, I and [mother] knew that it would be hard to accept for you, so it was a good coincidence that you were away this year."
    if inc == True:
        pov "{i}Are you serious, mom would support this?{/i}"
        dad "But know you're here and with this behavior you'll bring the whole family into danger. Me, your mom and even your sisters."
        pov "{i}Oh shit, he has a point.{/i}"
        dad "So I hoped you would join our play as the son that would fit in with a father in this playing."
    else:
        pov "{i}Are you serious, [mother] would support this?{/i}"
        dad "But know you're here and with this behavior you'll bring my whole family into danger. Me, [mother] and even my daughters."
        pov "{i}Oh shit, he has a point.{/i}"
        dad "So I hoped you would join our play as the wannabe son that would fit in with me in this playing."
    pov "A macho scum asshole?"
    dad "Yes, that would be the right description!"
    pov "Treating women like shit and playing god?"
    dad "It would be just a play. It would just be when my friends are around."
    dad "And when you don't want to participate stay away until we end this."
    dad "It won't last long anymore. We'll get results soon."
    pov "Soon?"
    scene intro 066
    dad "Don't you understand? If we ruin it they'll kill us!"
    if inc == True:
        dad "Or do worse to your mom and sisters."
        pov "I understand that but I still don't understand why you brought them into this position."
        dad "Me and your mom decided this."
        pov "Mom decided to bring my sisters into danger?"
    else:
        dad "Or do worse to [mother] and our daughters."
        pov "I understand that but I still don't understand why you brought them into this position."
        dad "Me and [mother] decided this."
        pov "[mother] decided to bring your daughters into danger?"
    dad "That's enough! You'll play along or we'll have to kick you out of the house."
    pov "{i}I can't still believe it.{/i}"
    dad "You'll help around the house and get your own money, I can't give you anything."
    dad "But you finished school so I'm sure you'll find a job. Staying poor isn't easy but you can do this for the family."
    pov "{i}Maybe I should play along, I can't reveal his cover, for the sake of the rest, but it would be even worse if they really kick me out.{/i}"
    pov "Calm down. I'll think about this."
    scene intro 067
    dad "Good! It's good that you're beginning to understand."
    dad "It wasn't planned for it to go this way, but now we have to deal with it."
    pov "So you aren't the boss of your little gang?"
    dad "Don't make fun of me! I and [mother] decide to take this chance for our best and the best of the family."
    pov "{i}He seems to be sad but I'm not sure that he isn't just playing. Maybe he enjoys his undercover game a little too much.{/i}"
    if inc == True:
        pov "{i}And he mustn't even have too bad a conscience, we aren't his kids, he's just the step-dad.{/i}"
        pov "{i}He could even take advantage of one of my sisters, even if I don't think he isn't into young girls.{/i}"
    pov "{i}So I'll have to stay aware and pretend to play his little game.{/i}"
    dad "Davide is the boss, Steve and I are his hands. And Steve isn't such a bad guy."
    pov "So the boss has some privileges?"
    dad "What do you mean?"
    pov "You know exactly what I mean!"
    if inc == True:
        dad "There is nothing between your mom and him. They just joke around sometimes."
    else:
        dad "There is nothing between [mother] and him. They just joke around sometimes."
    pov "{i}Enough of this shit! No one will believe you this is bullshit!{/i}"
    pov "Okay. I understand. I'll see if I play along or participate. Please give me the night to think about it."
    scene intro 068
    dad "Good! I'm glad that I can count on you!"
    dad "I really could use your help and it would be a waste to kick you out."
    pov "Okay?"
    dad "Everything will be fine after this job and we'll be very rich."
    scene intro 069
    dad "I need to get something from my car."
    dad "It's better if you go to bed and think about everything."
    if inc == True:
        pov "Okay... dad..."
        dad "I'm proud of you... Son!"
    else:
        pov "Okay... Bruce..."
        dad "I'm proud of you!"
    scene intro 070
    "You go back upstairs to your room."
    "Your brain full of fucks."
    if NTR == True:
        pov "{i}Hmm... is there something coming from the basement?{/i}"
        mom "Aaahh... hah... hah..."
        if inc == True:
            pov "{i}WTF? Is that mom's voice?{/i}"
        else:
            pov "{i}WTF? Is that [mother]'s voice?{/i}"
        scene intro 071
        pov "{i}I need to check!{/i}"
        pov "{i}Damn, it won't open. But I need to get in!{/i}"
        pov "{i}I don't hear anything anymore... Was I wrong?{/i}"
        if inc == True:
            pov "{i}Dad is coming back. Better leave it alone for now!{/i}"
        else:
            pov "{i}Bruce is coming back. Better leave it alone for now!{/i}"
    jump tutorial