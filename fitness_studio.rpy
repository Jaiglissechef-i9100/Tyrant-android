#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 9am Fitness Studio - MC, Nicole, Vivian - Love, Corruption
# 2. 4pm Fitness Studio - Cassandra, Irina, Kate, MC - Love, Corruption, Custom
# 3, 5pm Fitness Studio - Cassandra, Irina - Love, Corruption, Darker Paths
#----- End List -----

label fitness9am:
    hide screen townl
    $ fitnessnicfirst = True
    "You arrive at the fitness studio and change your clothes. Then you go to the main room."
    scene town fitness 9am 001
    if vivianfirstmeet == True:
        if inc == True:
            povi "Oh, there is mom and [vivian] training together."
        else:
            povi "Oh, there is [mother] and [vivian] training together."
    else:
        if inc == True:
            povi "Oh, there is mom and another woman training together."
        else:
            povi "Oh, there is [mother] and another woman training together."
    "You go closer."
    scene town fitness 9am 002
    if vivianfirstmeet == True:
        vivian "Oh hey [pov]."
    else:
        "Woman" "Hello?"
    mom "Who is it?"
    scene town fitness 9am 003
    mom "Oh, hello [pov]."
    pov "Hey, you two."
    if inc == True:
        pov "So this is what you run off to in the mornings, mom?"
    else:
        pov "So this is what you run off to in the mornings, [mother]?"
    scene town fitness 9am 004
    if vivianfirstmeet == True:
        vivian "You came here to workout too?"
        pov "Of course, I have to stay in shape to keep up with you!"
        vivian "Oh you're such a strong young man, doesn't look like you need workout much."
        pov "Well, you got me. I'm just here for the hot women, haha."
        vivian "Well, I'm here."
        mom "[vivian]!"
        if inc == True:
            pov "Don't worry, I thinking you're hot too mom!"
        else:
            pov "Don't worry, I thinking you're hot too [pov]!"
        mom "Hnnn..."
        vivian "Haha, I'm just teasing him."
    else:
        if inc == True:
            "Woman" "So you're [mother]'s son?"
        else:
            "Woman" "So you're the boy that lives with [mother]'s family?"
        pov "Yes and you are?"
        $ vivianname = renpy.input(_("My name is...")) or _("Vivian")
        $ vivianname = vivianname.strip()
        if vivianname == "":
            $ vivianname = "Vivian"
        $ vivianfirstmeet = True
        pov "Nice to meet you, [vivian]."
        vivian "Ditto."
    scene town fitness 9am 005
    vivian "Oh there's somebody I know. I need to talk to her."
    vivian "Wait just a second please!"
    scene town fitness 9am 006
    mom "You're not going to leave me now right? We're in the middle of stretching."
    vivian "I'm so sorry, it's urgent."
    mom "Who is it?"
    vivian "You don't know her, yet."
    scene town fitness 9am 007
    vivian "But could you take my place real quick. You just need to hold her feet."
    mom "You're really going to leave me..."
    vivian "You're in good hands, so it's no problem."
    vivian "Come here [pov]."
    scene town fitness 9am 008
    "You hold her legs."
    mom "Ok, please don't goof around though, alright?"
    if inc == True:
        pov "Haha, of course mom."
    else:
        pov "Haha, of course [mother]."
    povi "What a nice view."
    scene town fitness 9am 009
    mom "Good, just hold my legs straight up."
    pov "I won't let you fall."
    pov "Do you workout often?"
    mom "Pretty much every morning, but just for a short time."
    mom "More to help me have a relaxed start to the day rather than working out."
    pov "Oh...?"
    scene town fitness 9am 010
    mom "What's up?"
    pov "The women [vivian] went to meet. She's waving at me."
    mom "Who is it? Do you know her?"
    if mirandafirstmeet == True:
        pov "Yes it's [miranda]."
    else:
        pov "No, I have no idea who the blonde woman is."
        mom "Blonde? Does she have shoulder length hair and a bigger chest?"
        pov "Yes, do you know her?"
    scene town fitness 9am 011b
    if mirandafirstmeet == True:
        mom "[miranda], that slut!"
    else:
        mom"That slut!"
    if inc == True:
        pov "Wow, calm down, mom."
    else:
        pov "Wow, calm down, [mother]."
    mom "She's just a dumb whore!"
    pov "Haha, I know a better way to use your anger."
    scene town fitness 9am 012
    mom "Hah!"
    pov "Try to hold yourself up now."
    mom "What are you doing?"
    pov "Using that anger to hold your postition. It can help your training more."
    mom "OK."
    scene town fitness 9am 013
    pov "And now do the first posititon again."
    mom "Hnng..."
    pov "It's not too hard, right?"
    mom "No, it's just something new."
    scene town fitness 9am 012
    pov "And we're back now."
    mom "Hnn... hnn..."
    povi "Damn, her moaning isn't making this easier. And her pants are so tight."
    povi "Wait? Is that a camel toe?"
    mom "Is something wrong?"
    scene town fitness 9am 013
    pov "I was just thinking about something you can do with your leg's spread."
    mom "What?"
    povi "Oh shit. Did I say that out loud?"
    scene town fitness 9am 014
    mom "It's probably best if we stop here."
    pov "I didn't want to... I'm sorry."
    mom "Thinking about that kind of stuff while you're helping me."
    pov "It was just for a second."
    pov "You look so good in these pants..."
    mom "..."
    pov "Let me make it up to you, please?"
    scene town fitness 9am 015a
    mom "What are you doing?"
    pov "You'll see!"
    "You remove her shoes."
    scene town fitness 9am 016a
    mom "You can't be serious."
    pov "Yes I am. Training without shoes is also better for your feet."
    mom "But I said that we stop training..."
    pov "Oh we are done training. But I know a good way to deal with angry people."
    mom "I don't get..."
    scene town fitness 9am 017a
    mom "Hahaha... what?"
    "You tickle her feet."
    if inc == True:
        pov "See, angry mom isn't angry anymore."
    else:
        pov "See, angry [mother] isn't angry anymore."
    mom "That is... haha... cheating..."
    pov "I don't remember there being any rules to tickling! Mwa ha ha ha!"
    mom "I'm... haha... never... surrender... haha!"
    scene town fitness 9am 018a
    pov "So, we're good now?"
    if inc == True:
        mom "Haha, how could I disagree with my clever son."
    else:
        mom "Haha, how could I disagree with that clever boy."
    pov "It's nice to hear you laugh like that again. We don't get to do that at home as much as we should."
    mom "Well you had your fun too!"
    pov "Haha, yes I did."
    pov "Let's stretch your feet though while they are out. Those shoes have them confined all the time. I'm sure they need it."
    mom "Haha, OK."
    scene town fitness 9am 019a
    pov "Good, now pull the toes together and then stretch them again."
    mom "Like this?"
    pov "Yup. just like that."
    povi "Although it's not helping that you're so near my boner."
    povi "Oh crap! She's about to pull my pants down with her rubbing feet like that."
    povi "I should warn her."
    pov "Hey mom..."
    scene town fitness 9am 021a
    "And then it happened."
    mom "Huh? What?"
    povi "Her feet are on my dick. Touching it directly."
    mom "Is that what I think it is?"
    mom "Let go of my feet!"
    scene town fitness 9am 020a
    mom "Are you crazy [pov]?"
    pov "I was trying to warn you. I didn't do it on purpose."
    mom "You're such a pervert. Doing this to me in public. I just can't believe it!"
    if inc == True:
        pov "But mom..."
    else:
        pov "But [mother]..."
    scene town fitness 9am 023a
    mom "This was a mistake letting you help me."
    pov "Wait, I can explain..."
    mom "No! I'm leaving."
    scene town fitness 9am 024a
    povi "She left her shoes behind."
    povi "Seriously, why does this stuff always happen to me?"
    povi "Maybe I should follow her in a bit and try to talk this out with her."
    povi "I can bring her her shoes too."
    scene town fitness 9am 025
    povi "Damn, she's already gone to the locker rooms."
    povi "Should I follow her?"
    scene town fitness 9am 026
    povi "It's risky to go into the women's locker room, but I need to clear the air with her."
    povi "I hope that little gym gremlin doesn't catch me."
    "You enter the locker room."
    scene town fitness 9am 027
    povi "What the...?"
    povi "So was this the urgent thing... making out!"
    if inc == True:
        povi "While normally I would be happy to stay and watch, I need to find my mom."
    else:
        povi "While normally I would be happy to stay and watch, I need to find [pov]."
    scene town fitness 9am 029
    povi "There she is. Is she crying?"
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    povi "No reaction."
    scene town fitness 9am 030
    if inc == True:
        pov "Mom, I'm sorry."
    else:
        pov "[mother], I'm sorry."
    mom "Just leave [pov]."
    pov "No! I'm not going to leave until you've at least hear me out. Then you can sit here and hate me if you want to."
    mom "You're even in the women's locker room, you pervert."
    scene town fitness 9am 031a
    pov "That's what I want to talk to you about!"
    pov "Is that the reason? The reason you are crying? I swear it was an accident!"
    mom "It's just..."
    pov "I'm really sorry about that. I truly am! But I swear it wasn't on purpose!"
    scene town fitness 9am 032
    mom "You had a boner."
    pov "Ok, well yes I did. It's not an excuse, but I just couldn't help it. I'm in a fitness studio with so beautiful women, like you."
    mom "And I touched it."
    pov "By accident. The stretches were pulling at my pants and they were falling down."
    pov "That's what I started to tell you when it all happened. If I had just been quicker, then this never would have been an issue."
    pov "I'm sorry. I would never try anything like that with you in public without your permission."
    pov "I don't want people gossiping about you or me. That's that last thing I would want."
    mom "But..."
    pov "You know me, you've seen that I'm not like that..."
    scene town fitness 9am 033
    if inc == True:
        pov "You're my mom and I love you."
    else:
        pov "You're my mom best friend and I love you."
    pov "I would never do anything on purpose that would make you feel bad."
    pov "You know that."
    scene town fitness 9am 034a
    mom "Maybe you're right. Maybe it really was just an accident."
    pov "I'm telling you, it really was."
    mom "I'm sorry that I accused you of doing it on purpose."
    if inc == True:
        pov "No problem, mom. Really. This was my fault too."
    else:
        pov "No problem, [mother]. Really. This was my fault too."
    mom "I'm also sorry I called you a pervert... twice."
    pov "Hehe, well I'm not a saint, but I promise, I'm not a monster either"
    mom "Ha... ok."
    vivian "Ohh, hah, more you slut!"
    scene town fitness 9am 035
    mom "Huh?"
    pov "Oh their still going at it, I forgot about them."
    mom "They're still doing it?"
    pov "It seems so."
    vivian "Yes, right there, hah, hah..."
    scene town fitness 9am 034b
    mom "I'm sorry you need to hear them."
    pov "It isn't your fault."
    pov "If I wasn't such an idiot you wouldn't be here now either."
    mom "Hmm..."
    vivian "Hah... Ahhh..."
    if inc == True:
        pov "Come here, mom."
    else:
        pov "Come here, [mother]."
    scene town fitness 9am 036
    mom "Please just hold me."
    vivian "AAHH... stop it you slut!"
    "[mother] relaxes in your arms."
    pov "You're twitching. Is everything alright?"
    mom "I just feel a little hot."
    scene town fitness 9am 037
    "She look up and start staring in your eyes."
    mom "..."
    pov "..."
    scene town fitness 9am 038
    mom "Hnng..."
    povi "What is she up to? Staring at me so deeply..."
    vivian "Hah, hah, hah."
    povi "Maybe the moaning is turning her on?"
    scene town fitness 9am 039
    mom "<kiss>"
    povi "She's kissing me. It must be the moaning getting her worked up."
    scene town fitness 9am 040a
    povi "And what's with that staring now? Am I supposed to do be something?"
    mom "..."
    povi "Her body is really burning. That adrenaline and the moaning must have caused it."
    povi "She needs to let some of that pent up energy go. So what should I do?"
    call screen fitness9amnicchoose

screen fitness9amnicchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('fitness9amnicchoose'), Jump('fitness9amniccor')) hovered tt.Action ("Go further [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('fitness9amnicchoose'), Jump('fitness9amniclove')) hovered tt.Action ("Wait [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label fitness9amniclove:
    $ momlove += 1
    povi "So what now?"
    scene town fitness 9am 041a
    mom "<kiss>"
    povi "Wow, she's taking the lead. French kissing me even."
    povi "Clinging to me like that on me and playing with my tongue."
    povi "And now my boner is back... That didn't take long."
    "She kisses you for a while."
    "Eventually your hips start grinding together while you kiss."
    scene town fitness 9am 043a
    mom "Hmm..."
    povi "That smiling, so wonderful."
    povi "And she seems like she's totally lost in her thoughts, just staring in my eyes."
    if inc == True:
        pov "I love you mom."
    else:
        pov "I love you [mother]."
    scene town fitness 9am 042a
    mom "Huh? [pov]?"
    pov "I love you."
    mom "What have I done? I'm so sorry [pov]."
    pov "It's alright. I liked it."
    mom "I'm sorry, but you should leave now."
    mom "Before we do something we regret."
    pov "But..."
    mom "Please [pov]."
    pov "OK."
    scene black
    povi "\"Before we do something we regret\". So she wanted to do even more?"
    "You leave the locker room, change back into your street clothes and leave the fitness studio."
    $ dtime += 1
    jump town

label fitness9amniccor:
    $ momcorruption += 1
    pov "Come here!"
    scene town fitness 9am 040b
    mom "Hnng!"
    "You touch her belly and caress her stomach."
    mom "Hnn... hnn..."
    "You kiss her wildly."
    scene town fitness 9am 042b
    mom "Huh? HNNG!"
    "She seems to struggle at first, but quickly gives in and kisses you back."
    povi "You gone this far, I'll finish it for you."
    scene town fitness 9am 041b
    "You rub her pussy through her pants."
    povi "Wow. She's already wet. Hearing all the action before really got to her. Or was it me?"
    "She starts twitching more and more."
    scene town fitness 9am 043b
    mom "Hah... Stop..."
    pov "Sshhh... you need to be quiet. You don't want to be caught by your friend?"
    mom "Hnn... Don't... Stop..."
    pov "You're got turned on from hearing them having fun with each other, didn't you?"
    pov "And you're so wet."
    mom "Hnn..."
    scene town fitness 9am 044b
    pov "Good, relax. You're like a bitch in heat that needs relief!"
    mom "Hah... Hnn..."
    pov "I can understand that, being touched by a young man like me."
    mom "Hnn..."
    pov "I don't judge you, but I can't let you leave until you came."
    pov "A bitch in heat could hurt themselves and I won't allow that."
    pov "So I need to help you."
    pov "And more importantly, you want me to help you."
    mom "Hnng... Hnn..."
    povi "She'll be done in no time. Maybe it's the thrill of getting caught."
    if inc == True:
        pov "Or maybe enjoying the feeling that your son is taking care of your needs."
    else:
        pov "Or maybe enjoying the feeling that your best friend's son is taking care of your needs."
    scene town fitness 9am 045b
    mom "HNNG!"
    povi "Looks like that was the missing trigger!"
    pov "Cum good for me."
    mom "HNNN!"
    povi "It seems like she came very hard."
    scene town fitness 9am 047b
    pov "You needed this, didn't you?"
    pov "All that pent up stress!"
    mom "Hnn..."
    if inc == True:
        pov "You're a good mom for letting me help you with your problem."
    else:
        pov "You're a good girl for letting me help you with your problem."
    mom "Th...Thank you, but you need to leave now."
    pov "Sure, my sexy bitch in heat."
    mom "Hnn..."
    povi "I had my fun, I shouldn't try too much right now."
    scene black
    "You leave the locker room, change back and leave the fitness studio."
    $ dtime += 1
    jump town

label fitness_studio:
    hide screen townl
    if fitnessfirst == True and fitnessmember == True:
        jump fitnessrepeat
    if fitnessfirst == True and fitnessmember == False:
        jump fitnessnoentry
    scene town fitness 4pm 002
    povi "Oh they seem to be having fun."
    bs "And he thought he was sooo funny, haha."
    irina "Oh yeah, he's an idiot."
    povi "Are they talking about me? Nah, I don't think so."
    jump fitnessrunass

label fitnessrunass:
    scene town fitness 4pm 002
    call screen fitnessrunasspeek

screen fitnessrunasspeek():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('fitnessrunasspeek'), Jump('fitnessrunassir')) hovered tt.Action ("Look at [irina]'s ass") focus_mask True
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('fitnessrunasspeek'), Jump('fitnessrunasscas')) hovered tt.Action ("Look at [bs]'s ass") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('fitnessrunasspeek'), Jump('fitnessrunfirst')) hovered tt.Action ("Stop") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label fitnessrunassir:
    scene town fitness 4pm 003b
    povi "Yes, that firm ass."
    jump fitnessrunass

label fitnessrunasscas:
    scene town fitness 4pm 003a
    povi "Yes, that firm ass."
    jump fitnessrunass

label fitnessrunfirst:
    scene town fitness 4pm 004b
    bs "Oh look who's here."
    irina "What a nice surprise!"
    pov "Hey you two."
    irina "Do you want to train too?"
    scene town fitness 4pm 005b
    bs "Haha, he isn't for training, He just wants to watch us."
    irina "Oh come on, give him a chance."
    bs "I bet he hasn't even payed the fee!"
    pov "Fee?"
    scene town fitness 4pm 006b
    bs "Haha, did you think you could train here for free?"
    irina "There! Look behind you!"
    scene town fitness 4pm 007b
    povi "Oh damn, haha. He's small, but has muscles. Creepy!"
    "Guy" "So you're here to train or just watch girls?"
    pov "Depends on which costs more?"
    irina "<giggle>"
    povi "He doesn't seem to get the joke."
    pov "To train, but it's my first time here."
    "Guy" "You seem to know him already."
    if inc == True:
        irina "He's [bs]'s little brother."
    else:
        irina "He's a friend of [bs]."
    scene town fitness 4pm 008b
    "Guy" "Oh I see. So I can give you a discount."
    "Guy " "For $100 you can train here for 3 months."
    povi "$100. Is it worth it? I'm sure I could have a lot of fun here."
    call screen fitnesspay

screen fitnesspay():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if money >= 100:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnesspay'), Jump('fitnessrun2')) hovered tt.Action ("Pay") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('fitnesspay'), Jump('fitnessabort')) hovered tt.Action ("Don't pay") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label fitnessrun2:
    $ fitnessfirst = True
    $ money -= 100
    $ fitnessmember = True
    scene town fitness 4pm 009b
    "Guy" "OK. You can find the men's locker room this way. The men's showers are behind them."
    pov "Thank you."
    povi "Now I can train and watch hot girls, haha."
    jump fitnessrepeat

label fitnessabort:
    pov "No, sorry. I'm out of here."
    "Guy" "So be it."
    $ fitnessfirst = True
    $ dtime += 1
    jump town

label fitnessnoentry:
    scene town fitness 4pm 002
    "Guy" "Hey, are you here now to pay for training?"
    scene town fitness 4pm 010b
    call screen fitnesspay

label fitnessrepeat:
    scene black
    "You go change in the locker room."
    "Then you go to the training room."
    scene town fitness 4pm 012b
    povi "They're training all the time."
    povi "Time for some fun."
    call screen fitnesschoose1

screen fitnesschoose1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnesschoose1'), Jump('fitnessbs')) hovered tt.Action ("Go to [bs]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnesschoose1'), Jump('fitnessirina')) hovered tt.Action ("Go to [irina]") focus_mask True
        if katefirstmeet == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnesschoose1'), Jump('fitnesskate')) hovered tt.Action ("Go to [kate]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom Scene -----
label fitnesskate:
    $ irinarelationship += 1
    scene town fitness 4pm 004 #----- Notice Kate -----
    "<Wham!>"
    with vpunch
    povi "What is that?"
    "You move in closer to get a better look."
    scene town fitness 4pm 004a #----- Better Look -----
    "<Whomp!>"
    with vpunch
    povi "That's [kate]. She's using the heavy bag. I wonder where she learned to box?"
    scene town fitness 4pm 005a #----- Even Closer -----
    "<Wham!>"
    with vpunch
    povi "She's so focused, that she hasn't even noticed me yet."
    scene town fitness 4pm 006a #----- Behind Her -----
    "You move around back and watch her beat on the bag for a while."
    "<Whomp!>"
    with vpunch
    povi "She's really good."
    scene town fitness 4pm 007a #----- Her Behind -----
    "<Wham!>"
    with vpunch
    povi "She's very fit!"
    "<Whomp!>"
    with vpunch
    povi "I've probably been staring long enough... I should say something."
    call screen fitnesskatesayhello

screen fitnesskatesayhello():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('fitnesskatesayhello'), SetVariable("katelove",katelove+1), Jump('fitnesskatelove')) hovered tt.Action ("Love") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('fitnesskatesayhello'), SetVariable("katecorruption",katecorruption+1), Jump('fitnesskatecorruption')) hovered tt.Action ("Corruption") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label fitnesskatelove:
    $ fitnesskatemood = True
    jump fitnesskatecorruption

label fitnesskatecorruption:
    if fitnesskatemood == True:
        pov "Hey [kate]! I didn't know you are a boxer! You're really good!"
    else:
        pov "I didn't know you are a boxer [kate]. How about you get on your knees and give me two blows to the head?"
    if katelove > katecorruption:
        scene town fitness 4pm 008a #----- Kate Love -----
        kate "Hey [pov]! Thanks. I've been boxing with my father since I was a little girl."
        pov "That's awesome. Maybe I can get you so show me a few pointers sometime."
        kate "You don't have to twist my arm to beat on you a little. <giggle>"
        pov "Sweet! Well just let me know when a good time is and I'll be here."
        kate "Will do. Am I going to see you later at the club [pov]?"
        pov "I certainly wouldn't mind it, but what would your boyfriend think?"
        kate "Doesn't matter. I can be friends with who I want to be friends with."
        pov "Well ok then0, [kate]. I guess I'll see you there."
        kate "Good."
    else:
        scene town fitness 4pm 009a #----- Kate Corruption -----
        kate "[pov]! You wish. I'm just as likely to bite that \"head\" off while I'm down there."
        pov "That would mean you're planning to have your mouth around it first. Damn, [kate]! Buy dinner first why don't you?!"
        kate "Ha... ha... What do you want [pov]?"
        pov "Actually, I wanted you to show me a thing or two about boxing. I was watching you and you're good. I could use some pointers."
        kate "If it means you'll leave me alone, sure [pov]. I'll let you know when I have some free time."
        pov "Thanks, [kate]. I look forward to it... and those tight as gym clothes!"
        kate "You just don't give up do you?"
        pov "Not my style."
        kate "...I like that. Goodbye now."
        pov "Later, [kate]."
    "You leave [kate] to her boxing and head to the lockers to get cleaned up before leaving the gym."
    if katemeetgym == False:
        $ katemeetgym = True
    $ fitnesskatemood = False
    $ dtime += 1
    jump town

#----- Custom Scene -----
label fitnessirina:
    scene town fitness 4pm 013b #Irina running on treadmill, view from behind
    $ irinarelationship += 1
    povi "I think I'll join [irina] this time."
    povi "That view is just breathtaking! She should always be wearing spandex."
    "You hop up on the treadmill next to [irina] and set it to her speed."
    scene town fitness 4pm 014b #Irina running on treadmill, view from the side, irina looking at mc, neutral smile
    pov "Hey [irina], do you mind if I join you?"
    irina "[pov]! I didn't know you were working out at time too. What a nice surprise."
    pov "Well now that I know you're here, it's my favorite time to workout!"
    irina "Haha, you're so sweet!"
    scene town fitness 4pm 015b #view of the false sky in the window
    pov "Plus look at this view! No one likes painted skies as much as I do."
    scene town fitness 4pm 016b #Irina running on treadmill, view from the side, irina looking at window, talking
    irina "What... really."
    "You chuckle a little waiting for her to realize you're joking."
    irina "Oh you're kidding! Haha!"
    irina "Yeah they had to do that because it's just a dirty alley out of those windows."
    pov "Ouch, doesn't seem like planning ahead was high on their priority when making this place then."
    irina "Yeah, I heard they got this place for cheap and just renovated it into a gym."
    scene town fitness 4pm 017b #Cassandra, view from the side, looking at her working out
    if inc == True:
        povi "Big sis is working hard too. Needs to stay in shape if she's going to be a big influencer like she wants."
    else:
        povi "[bs] is working hard too. Needs to stay in shape if she's going to be a big influencer like she wants."
    povi "Although she doesn't seem to be doing the exercises quite right, maybe next time I'll offer my help."
    scene town fitness 4pm 018b #Irina running on treadmill, view from the side, irina looking at mc, talking to mc
    irina "[pov], whatcha looking at over there? <giggle>"
    pov "Sorry about that [irina]. I just noticed [bs] was doing her exercise wrong. I didn't want her hurting herself."
    irina "Awww... See you are the nicest guy around town! I'm glad we're friends now."
    irina "Plus it's funny to watch [bs] squirm whenever we're together!"
    pov "Haha! Yeah, that never gets old."
    scene town fitness 4pm 019b #Irina standing in front of Cassandra, talking to mc, pointing at showers
    "[irina] shuts off her treadmill and hops off once it stops."
    irina "I'm sorry to cut our conversation short, but I have to get ready for tonight so I need to go shower and get home."
    pov "That's ok. I understand. If you don't mind me asking, what are you doing tonight?"
    irina "Not at all. [bs] and I are going to the club tonight as usual."
    irina "Maybe I'll see you there?"
    pov "Yeah, if I can get away from the house, I'll be there!"
    irina "Great, I hope to see you soon, handsome!"
    scene town fitness 4pm 020b #Cassandra, view from the side, looking at her working out, laying back on the bench
    "[irina] heads towards the locker rooms."
    "You notices the [bs] has stopped working out and seems to be trying extra hard to ignore you."
    povi "I wonder if she's upset about [irina] and I talking."
    scene town fitness 4pm 021bc #Irina entering showers, neutral walk into the locker room
    "You look over the locker rooms."
    povi "Seriously, she is built like some sort of sex goddess."
    if irinacorruption >= 30 and irinacorruption > irinalove or irinalove >= 40 and irinalove > irinacorruption:
        scene town fitness 4pm 021b #Irina entering showers, sexy pose, looking back at you
        irina "[pov]! You really should come party with us. I'm going to wear something special for you..."
        "She gives you a wink and heads into the locker room."
        scene town fitness 4pm 022 #empty entrance to the locker rooms
        povi "Hot damn! I can't wait so see what she's going to be wearing!"
        povi "Well, I better check on [bs] and see if she still needs some help."
        pov "Hey [bs]..."
        scene town fitness 4pm 023c #Cassandra running into the locker rooms
        povi "I wonder why she's running in there like that?"
        povi "I should go check on her and see what's going on."
        call screen fitnessfollowcas
    else:
        scene town fitness 4pm 022 #empty entrance to the locker rooms
        povi "Well, I better check on [bs] and see if she still needs some help."
        pov "Hey [bs]..."
        scene town fitness 4pm 023c #Cassandra running into the locker rooms
        povi "I wonder why she's running in there like that?"
        povi "I should go check on her and see what's going on."
        call screen fitnessfollowcas

label fitnessbs:
    scene town fitness 4pm 013c
    $ bigsisrelationship += 1
    bs "Hnng..."
    povi "Oh she's training her stomach muscles. But she's not doing it very well."
    scene town fitness 4pm 014c
    bs "Hah [pov]. Don't scare me like that!"
    pov "Why? I was just watching you."
    scene town fitness 4pm 015c
    bs "I can train without being watched, thank you..."
    pov "You're training your abs right? I'm pretty sure you're not doing it well."
    bs "What are you talking about?"
    pov "Your legs, you need to work them more."
    pov "I can help you with that."
    scene town fitness 4pm 016c
    pov "See? They need to be in a straight line."
    bs "What are you...? Stop it."
    pov "I'm just helping you, start by bending forward."
    if bigsiscorruption < 20 and bigsiscorruption > bigsislove or bigsislove < 30 and bigsislove > bigsiscorruption:
        jump fitnessbsend1
    scene town fitness 4pm 018c
    bs "But you're hands are on my thighs."
    if inc == True:
        pov "Relax sis."
    else:
        pov "Relax [bs]."
    pov "We've already had so much fun together, so this won't hurt anyone."
    if cdate5bj == True or cdate5fuck == True or cdate5hj == True:
        pov "And we already experienced so much together at the mall."
    bs "But..."
    scene town fitness 4pm 019c
    pov "Go on, start bending forward and remember to push yourself. I'll watch out to make sure you won't hurt yourself."
    bs "But you can't... hah..."
    povi "Wow, did she let out a moan? But I'm barely near her pussy."
    scene town fitness 4pm 020c
    bs "Can you please stop it now?"
    pov "Wait, I was barely touching your legs and you start moaning?"
    pov "And now you're telling me to stop?"
    bs "It, it was just..."
    pov "I know what the reason was, no need to deny it."
    povi "I wonder why she's so confused today?"
    scene town fitness 4pm 021c
    pov "We both know that you like how I take care of you right?"
    if inc == True:
        pov "Your brother is taking care of you."
    else:
        pov "I'm taking care of you."
    bs "You misunderstand..."
    pov "Why are you doing this alone anyway?"
    pov "[irina] doesn't seem to notice your mistakes at training."
    if martinfirstmeet == True:
        pov "Even your boyfriend isn't helping, you must be so disappointed."
    pov "So you can be happy to have me now."
    bs "Hnn..."
    scene town fitness 4pm 022c
    bs "I... need to go... now."
    pov "So you're done training?"
    bs "I... can't."
    if bigsiscorruption > bigsislove:
        pov "But I wanted to train with you now that why I'm here!"
    else:
        pov "And I thought I could be of help to you."
    if cdate5bj == True or cdate5fuck == True or cdate5hj == True:
        bs "I'm sorry."
    bs "..."
    scene town fitness 4pm 023c
    povi "She seems to be in a hurry. It must be very embarrassing for her to be moaning like that so suddenly."
    povi "Maybe she was thinking dirty thoughts while we're training."
    povi "Should I follow her and find out why?"
    scene town fitness 4pm 023ca
    povi "[irina] is gone too. But I didn't notice it."
    povi "Maybe she was offended that I trained with [bs] instead of her."
    call screen fitnessfollowcas

screen fitnessfollowcas():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_tickle_%s.png" action (Hide('fitnessfollowcas'), Jump('fitnesslockercas')) hovered tt.Action ("Follow her") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('fitnessfollowcas'), Jump('fitnesshome')) hovered tt.Action ("Leave") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label fitnesslockercas:
    povi "I'll follow her. Maybe we can have more fun together in there."
    "You decide to follow her into the women's locker room."
    scene town fitness 4pm 024c
    povi "There she is. Still in a hurry it seems."
    "You get closer silently."
    scene town fitness 4pm 025c
    povi "So what to do now?"
    call screen fitnesslockercaschoose

screen fitnesslockercaschoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('fitnesslockercaschoose'), Jump('fitnesslockercascor')) hovered tt.Action ("Grab her ass [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('fitnesslockercaschoose'), Jump('fitnesslockercaslove')) hovered tt.Action ("Let her know you're here [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label fitnesslockercascor:
    scene town fitness 4pm 026cc
    $ bigsiscorruption += 1
    povi "Her firm, hot ass. All mine!"
    bs "Hah..."
    scene town fitness 4pm 027cc
    bs "Are you crazy...?"
    pov "No. I just wanted to do it and I'm here to have fun with you."
    bs "You're in the women's locker room!"
    pov "Well duh, you're running away like a bitch in heat so I'm here to help you!"
    bs "You can't be serious!"
    pov "Yes I am, come here."
    scene town fitness 4pm 028cc
    pov "Yes, bend over like that and we can have fun together!"
    bs "Hah... stop..."
    if cdate5fuck == True:
        pov "Almost like last time when I fucked you in the mall. But now I can see your beautiful ass."
    bs "You idiot."
    if bigsisrelationship <= 5 and NTR == True:
        jump fitnesscasntr
    scene town fitness 4pm 029cc
    povi "Damn, She acts like she's putting up a fight, but I know she's horny. She's definitely just grinding against me more than trying to actually get away."
    if bigsiscorruption < 50:
        jump fitnesslockercasbend
    pov "Yes tease me more with your hot ass!"
    bs "No... not now, stupid."
    povi "Wait what...? Wow!"
    scene town fitness 4pm 030cc
    bs "We can't do this right here. [irina] is in the shower and will catch us."
    pov "So no fucking right here. Damn."
    bs "Hnn..."
    pov "You're dissapointed?"
    if inc == True:
        pov "That you won't get your brothers dick?"
    else:
        pov "That you won't get my dick?"
    bs "Stop talking shit..."
    pov "Haha, you're so confused when you're horny. Then you can help me another way."
    scene town fitness 4pm 031cc
    "You lay your hand on her shoulder and try to push her down."
    bs "Hnn..."
    pov "Come on, getting me all horny with your moaning and ass shaking."
    "She lets you push her down."
    scene town fitness 4pm 032cc
    bs "You don't really want me to..."
    pov "Oh yes I do! I know you'll take care of me!"
    if inc == True:
        "Or do you want to explain to [irina] why your little brother has a huge boner when she comes back from the shower?"
    else:
        "Or do you want to explain to [irina] why I have a huge boner when she comes back from the shower?"
    bs "No..."
    scene town fitness 4pm 033cc
    pov "Then hurry up and help me before she comes back."
    bs "..."
    if cdate5bj == True:
        pov "You already did it before and it was sooooo good."
    if cdate5fuck == True:
        pov "We already fucked this is nothing compared to that."
    pov "Come on, I nkow you want to."
    scene town fitness 4pm 034cc
    bs "Hnn..."
    pov "Go on, I need to feel your lips around my cock!"
    bs "I'll do it. But just to prevent [irina] from getting suspicious."
    pov "Whatever you want to tell yourself works for me, just do it!"
    povi "What a lame excuse, haha."
    scene town fitness 4pm 035cc
    image hjcas_fitness = Movie(channel="hjcas_fitness", play="images/anim/hjcas_fitness.webm")
    scene hjcas_fitness with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    pov "Oh yes, good. really stroke it!"
    "You grab her head."
    if cdate5bj == True:
        pov "I know you want to taste my big dick again."
    else:
        pov "I know you want to taste my big dick."
    bs "Hnn..."
    scene town fitness 4pm 036cc
    bs "<lick>"
    pov "Oh yes..."
    povi "That gentle touch of her tongue."
    pov "Now stop hesitating and go on, we don't have much time."
    scene town fitness 4pm 037cc
    bs "<suck> Hnn..."
    if inc == True:
        pov "Yes, taste your brothers cock that's getting so hard because of you."
    else:
        pov "Yes, taste my cock that's getting so hard because of you."
    bs "<lick> <suck>"
    povi "So good. Now her tongue is helping."
    povi "But should I help her or let her do it all on her own?"
    if casbjdt > 0:
        povi "Or I could train her with more deepthroating."
    call screen fitnesslockercasbjchoose

screen fitnesslockercasbjchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnesslockercasbjchoose'), Jump('fitnesslockercasbjnormal')) hovered tt.Action ("Let her do it") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('fitnesslockercasbjchoose'), Jump('fitnesslockercasbjdt')) hovered tt.Action ("Help her train deepthroating [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label fitnesslockercasbjnormal:
    povi "I'll let her surprise me and see what she can do."
    scene town fitness 4pm 038cc
    bs "<suck> <suck> Hnn..."
    pov "Oh yes like that."
    povi "Damn she's putting effort in it. I'm sure she likes it."
    if inc == True:
        pov "You're doing good, sis."
    else:
        pov "You're doing good, [bs]."
    pov "I'll cum in no time when you show me more of your slutty self."
    bs "HNG... <suck>"
    povi "Oh my dick in her mouth stopped her from complaining."
    scene town fitness 4pm 039cc
    pov "Oh, your tongue is doing that thing, like a real slut."
    bs "Are you about to finish now?"
    pov "Soon, but some dirty talk could speed me up."
    bs "Hmm..."
    povi "I wonder if she'll do it?"
    if inc == True:
        bs "Please cum in my mouth brother!"
    else:
        bs "Please cum in my mouth [pov]!"
    bs "Let me taste your sperm."
    pov "Damn. Now you'll get rewarded very soon!"
    povi "That worked out fantastic."
    bs "You're right! I need to taste your cock!"
    pov "That's too much! I'm going to cum..."
    scene town fitness 4pm 040cc
    pov "HNNG..."
    "You spray your sperm in her mouth."
    bs "Hmm..."
    pov "Enjoy your treat!"
    bs "<swallow> <gulp>"
    jump fitnesslockercasbjend

label fitnesslockercasbjdt:
    $ bigsiscorruption += 1
    if casbjdt > 0:
        jump fitnesslockercasbjdt2
    scene town fitness 4pm 038ccc
    bs "Huh?"
    pov "Let me help you!"
    "You press her head on your dick."
    "She's fighting back."
    scene town fitness 4pm 039ccc
    pov "Stop fighting! You should be learning this too!"
    pov "And it'll speed everything up!"
    bs "Hnng..."
    "You press her harder."
    scene town fitness 4pm 040ccct
    "You shove your dick deep in her throat."
    bs "<choke> HNNG..."
    pov "Very good. Just as I said, I'll cum in no time now."
    pov "And it'll give you a good training for future sessions, haha."
    bs "<choke> HNNG..."
    scene town fitness 4pm 041ccct
    "You start to fuck her face slowly."
    bs "<choke> Hng... hng..."
    pov "See? I can only do it slowly because your mouth isn't trained."
    "She slowly stops fighting."
    pov "You like that don't you?"
    if inc == True:
        pov "Getting used by your brother!"
    else:
        pov "Getting used by someone you've known such a long time."
    bs "<choke> Hng... hng..."
    pov "I'll cum soon, I'll spray it deep in your throat. So don't choke on it."
    bs "..."
    pov "Oh yes..."
    scene town fitness 4pm 042ccct
    pov "HNNG...!"
    "You spray your sperm down her throat."
    bs "<swallow> <gulp> <choke>"
    pov "Yes, you're a good girl!"
    bs "Hnn..."
    $ casbjdt += 1
    jump fitnesslockercasbjend

label fitnesslockercasbjdt2:
    scene town fitness 4pm 038ccc
    bs "Huh?"
    pov "Let me help you!"
    "You press her head on your dick."
    "She's fighting back."
    scene town fitness 4pm 039ccc
    pov "Stop fighting! You already did it before!"
    pov "And it'll speed everything up!"
    bs "Hnng..."
    pov "It's time for more training."
    scene town fitness 4pm 040ccc
    pov "Huh?"
    bs "<choke> HNNG..."
    pov "Good. You agreed with me."
    povi "Wow! She's deepthroating my dick all on her own."
    pov "Very good. Just as I said, I'll cum in no time."
    pov "And your already doing it better than last time."
    bs "<choke> HNNG..."
    scene town fitness 4pm 041ccc
    "She's fucking your dick with her face on her own."
    pov "Holy shit! This is a great surprise!"
    bs "<choke> Hng... hng..."
    pov "You really like this don't you?"
    if inc == True:
        pov "Getting used by your brother!"
    else:
        pov "Getting used by someone you've known such a long time."
    bs "<choke> Hng... hng..."
    pov "I'll cum soon, I'll spray it deep in your throat. So don't choke on it."
    bs "..."
    pov "Oh yes..."
    scene town fitness 4pm 042ccc
    pov "HNNG...!"
    "You spray your sperm down her throat."
    bs "<swallow> <gulp> <choke>"
    pov "Yes, you're a good girl! Deepthroating me like a real pro!"
    bs "Hnn..."
    $ casbjdt += 1
    jump fitnesslockercasbjend

label fitnesslockercasbjend:
    if casbjdt == 1:
        scene town fitness 4pm 043ct
    else:
        scene town fitness 4pm 043c
    pov "That was very good."
    bs "That was humiliating..."
    pov "Because you sucked my dick?"
    pov "Or because you liked it so much?"
    if inc == True:
        pov "Helping your brother to get off."
    else:
        pov "Helping me get off."
    bs "..."
    bs "I did what you wanted, please leave now before [irina] catches us."
    povi "Wow, she's just given in. She's all mine now."
    if inc == True:
        pov "OK. Until next time, big sis."
    else:
        pov "OK. Until next time, [bs],"
    scene black
    "You leave the fitness studio."
    $ dtime += 1
    jump town

label fitnesslockercasbend:
    bs "I said stop it you damn asshole!"
    povi "Damn, maybe I was too optimistic! She really needs more corruption..."
    "[bs] is about to scream."
    povi "Damn, better run."
    scene black
    "You leave the fitness studio before someone catches you in the women's locker room."
    $ dtime += 1
    jump town

label fitnesshome:
    povi "I don't want to follow her now."
    scene black
    "You change back into your street clothes and leave the fitness studio."
    $ dtime += 1
    jump town

label fitnessbsend1:
    scene town fitness 4pm 017c
    bs "Stop touching me there, you idiot!"
    pov "Why? I'm only holding your legs?"
    bs "I can do it myself."
    pov "But..."
    bs "I said no!"
    "You remove your hands."
    povi "Damn, she isn't ready for that."
    "You turn around."
    scene town fitness 4pm 023ca
    povi "Huh? When did [irina] leave?"
    scene black
    "You decide to leave as well."
    $ dtime += 1
    jump town

label fitnesslockercaslove:
    $ bigsislove += 1
    pov "Hm..."
    scene town fitness 4pm 027cc
    bs "Oh? You're here?"
    pov "Well yeah, I followed you."
    bs "But why?"
    pov "I noticed that you left in a hurry and I came to see if you're alright."
    scene town fitness 4pm 028cl
    pov "I was worried."
    bs "I... think I'm alright."
    pov "There is no need to hide it, I can see it in your eyes."
    pov "Come here."
    scene town fitness 4pm 029cl
    bs "Oh [pov]..."
    pov "As I thought. You're having trouble dealing with some of your feelings aren't you."
    bs "How... you want to... help?"
    pov "You already know it, you're trembling."
    scene town fitness 4pm 030cl
    bs "Why is this... happening?"
    pov "Because I choose you."
    if cdate5hj == True:
        pov "And I told you this before."
    if inc == True:
        pov "I love you, big sis."
    else:
        pov "I love you [bs]."
    pov "I know exactly what you need, just let me help you."
    image kisscas_fitness = Movie(channel="kisscas_fitness", play="images/anim/kisscas_fitness.webm", loops=0)
    scene kisscas_fitness with dissolve:
        size (config.screen_width, config.screen_height)
    pov "<kiss>"
    bs "Hnn..."
    "She holds you tight while you kiss her."
    scene town fitness 4pm 032cl
    bs "Hah..."
    pov "See, isn't this what you wanted to do?"
    bs "Hnn..."
    pov "You can give in to your yourself, I know you've waited for this all your life."
    pov "We can stay together forever, I'll never leave you."
    if inc == True:
        pov "We're tied as siblings."
        bs "Oh brother."
    else:
        bs "Oh [pov]."
    scene town fitness 4pm 033cl
    pov "<kiss> <kiss>"
    bs "Hnng..."
    pov "You taste so good, I want to kiss your whole body."
    bs "Hnn..."
    irina "[bs] you there?"
    povi "Oh crap!"
    "You seperate quickly."
    scene town fitness 4pm 034cl
    irina "Oh [pov], what's going on here?"
    scene town fitness 4pm 035cl
    bs "No... nothing..."
    pov "I had to ask [bs] something urgent."
    irina "Oh, OK. I need to go now, you coming with me [bs]?"
    if bigsisrelationship <= 5 and NTR == True:
        jump fitnesscasntr
    if bigsislove <= 50:
        jump fitnesslockercasloveend
    scene town fitness 4pm 036cl
    bs "Sorry [irina], I need to take a shower now."
    bs "I'll go home later."
    povi "Oh, did she wink at me? Does she want me to follow her?"
    scene town fitness 4pm 037cl
    irina "What's wrong [pov]? Shouldn't you leave the locker room so [bs] can change?"
    pov "Oh, yes... haha."
    povi "I'll wait until [irina] is gone and then sneak back into the shower."
    povi "I'm pretty sure that [bs] wants me to join her."
    irina "[pov]!"
    pov "Oh, sorry."
    scene black
    "You leave the women's locker room."
    "After some time you think you see [irina] leaving. You undress and go into the showers."
    scene town fitness shower 5pm 001
    povi "Well I guess it's time to see if I was right."
    call screen fitnessshowercaslovechoose

screen fitnessshowercaslovechoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnessshowercaslovechoose'), Jump('fitnessshowerback')) hovered tt.Action ("Check the shower in the back") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnessshowercaslovechoose'), Jump('fitnessshowerfront')) hovered tt.Action ("Check the shower in the front") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label fitnessshowerback:
    scene town fitness shower 5pm 005
    povi "Let's check this one."
    scene town fitness shower 5pm 006
    povi "Oh yes. I'm right."
    scene town fitness shower 5pm 007
    bs "[pov]! What are you doing here?"
    povi "Oh shit, she wasn't waiting for me? That can't be true."
    bs "What took you so long?"
    povi "Oh yes, thank god."
    bs "Come here."
    scene town fitness shower 5pm 008
    bs "<kiss> Hnn..."
    povi "Yes, perfect!"
    if inc == True:
        povi "I'm all naked with my big sis in the shower and she's excited too."
    else:
        povi "I'm all naked with [bs] in the shower and she's excited too."
    "You french kiss for sometime."
    scene town fitness shower 5pm 009
    if inc == True:
        bs "Please kiss me more brother."
    else:
        bs "Please kiss me more [pov]."
    bs "Please never stop."
    pov "Oh I can do that [bs]."
    pov "But as I said before, the other parts of your body need to be kissed too."
    bs "Oh... I'm... excited."
    scene town fitness shower 5pm 011
    pov "Your beautiful breasts need some attention too."
    bs "Please don't make me wait..."
    pov "So I was right, you wanted this for a long time now?"
    if inc == True:
        bs "Yes... please kiss me brother."
    else:
        bs "Yes... please kiss me [pov]."
    scene town fitness shower 5pm 012
    bs "Hah..."
    pov "They're so big and firm."
    pov "I love them. I would have loved them any way there were though, they are attached to the woman I love!"
    bs "You're so sweet."
    pov "Your nipples seem to like kisses too."
    scene town fitness shower 5pm 013
    bs "Hah... what are you doing with me...?"
    pov "I'm going to help you fall in love with me even more."
    bs "Hnn..."
    pov "Time for more."
    scene town fitness shower 5pm 014
    pov "<kiss> <lick>"
    bs "Oh my god! Your lips!"
    "You suck on her nipples like an eager baby needing to suckle."
    bs "Oh... hah... more!"
    povi "So that's one of her weak spots."
    scene town fitness shower 5pm 015
    bs "Oh... ohhh..."
    povi "She's really enjoying it. I wonder if she's really falling for me or she's just likes how it feels?"
    povi "We've always been close, but this is all new to me too."
    if inc == True:
        bs "Hah... bro... bro..."
    else:
        bs "Hah... [pov]... [pov]..."
    scene town fitness shower 5pm 016
    "You go lower."
    bs "Hah, not my belly..."
    pov "<kiss> <kiss>"
    bs "It feels so good, but it tickles so much."
    pov "I'm only stopping for a moment, on my way lower. I have to kiss you there too as it's part of your body."
    bs "Ohh, haha... hah..."
    scene town fitness shower 5pm 017
    "You reach your destination."
    pov "<kiss> <lick>"
    bs "Oh yes, yes! More!"
    scene town fitness shower 5pm 018
    "You lick her clit faster."
    bs "Hnng... hnng..."
    pov "You taste so good, [bs]!"
    bs "Hah... Oh god."
    povi "She's enjoying it so much I think it's time for more."
    scene town fitness shower 5pm 019
    "You stand up and point your dick at her pussy."
    "[bs] is trembling."
    scene town fitness shower 5pm 021
    bs "You want to...?"
    if inc == True:
        pov "Yes I want to be inside you, big sis."
    else:
        pov "Yes, I want to be inside you, [bs]."
    bs "..."
    bs "Please not here."
    pov "Oh..."
    scene town fitness shower 5pm 020
    "You rub your dick on her clit."
    pov "So how about this instead?"
    bs "Yes, hnn..."
    scene town fitness shower 5pm 022
    bs "This feels so good, keep doing it."
    pov "Yes it does, being so intimate with you."
    bs "I need more!"
    scene town fitness shower 5pm 023
    "She comes closer."
    pov "Oh more kisses?"
    if inc == True:
        pov "As you wish, big sis."
    else:
        pov "As you wish, [bs]."
    scene town fitness shower 5pm 024
    "You french kiss each other wildly."
    bs "Hmm... <lick>"
    pov "<lick> <lick>"
    pov "I've waited so long for this."
    if inc == True:
        bs "I'm glad you're so stubborn, little brother."
    else:
        bs "I'm glad you're so stubborn, [pov]."
    scene town fitness shower 5pm 020
    "You rub your dick on her clit even faster."
    bs "Hah... more!"
    pov "I think I'm about to cum."
    bs "Me too. Spray it on me."
    scene town fitness shower 5pm 025
    bs "Hah... hah... I'm there..."
    if inc == True:
        pov "Then cum for me, big sis!"
        bs "Hah, brother, hold me tight!"
    else:
        pov "Then cum for me [bs]!"
        bs "Hah, [pov], hold me tight!"
    bs "AAAHHH...!"
    "You can't hold out any longer."
    scene town fitness shower 5pm 026
    pov "HAH!"
    bs "Ah, I can feel your sperm on my pussy."
    pov "This is so good."
    scene town fitness shower 5pm 027
    bs "We came together."
    pov "Yes, hah. It feels good that I could do this with you."
    bs "I needed this too."
    if inc == True:
        pov "I love you, big sis."
    else:
        pov "I love you, [bs]."
    scene town fitness shower 5pm 028
    bs "Hnn..."
    pov "You can admit it too, there's no need to hide it anymore."
    bs "I... I..."
    bs "I'm sorry, [pov]."
    scene black
    "She ran away."
    povi "Hm... maybe it's too soon for her to admit it. But I'm on the right path with her."
    "You assume that she left the fitness studio, so you go too."
    $ dtime += 1
    jump town

#----- edited scene -----
label fitnessshowerfront:
    if irinalove or irinacorruption >= 40:
        scene town fitness shower 6pm 001 #Irina showering looking up
        povi "Holy shit! It's [irina]!"
        povi "I thought she left. God that body is amazing!"
        scene town fitness shower 6pm 002 #Irina showering looking up, one leg back
        povi "I know I'm risking her seeing me, but I just can't look away."
        povi "Those legs just won't quit!"
        scene town fitness shower 6pm 003 #Irina showering looking at MC
        irina "So do you like what you see, [pov]"
        povi "Shit..."
        pov "Honestly... yes I do."
        scene town fitness shower 6pm 004 #Irina showering looking at MC, body turned for full view
        irina "So, what are you doing in the women's showers?"
        irina "You're not looking for [bs] are you?"
        povi "Wow, she's either really good at guessing or saw more than she let on earlier."
        call screen fitnessshoweririnachoose
    else:
        scene town fitness shower 5pm 002
        povi "I'm so excited."
        scene town fitness shower 5pm 003
        povi "Holy shit! Urg! I need to leave fast before she notices me."
        scene town fitness shower 5pm 004
        povi "So there is only one occupied shower left. That one has to be her."
        jump fitnessshowerback

screen fitnessshoweririnachoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnessshoweririnachoose'), Jump('fitnessshowercassandra')) hovered tt.Action ("Looking for [bs]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('fitnessshoweririnachoose'), Jump('fitnessshoweririna')) hovered tt.Action ("Looking for [irina]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- edited scene -----
label fitnessshowercassandra:
    $ fitnessshowercas = True
    jump fitnessshowerfrontpart2
#----- edited scene -----
label fitnessshoweririna:
    $ fitnessshoweriri = True
    jump fitnessshowerfrontpart2
#----- edited scene -----
label fitnessshowerfrontpart2:
    if fitnessshowercas == True:
        scene town fitness shower 6pm 005 #Irina showering looking at MC, body turned for full view, close up lip bite
        pov "Yeah, I was looking for [bs]. I had something important to tell her."
        irina "Well, I don't know what's so important, that you felt like you needed to invade the women's shower stalls."
    else:
        scene town fitness shower 6pm 005b #Irina showering looking at MC, body turned for full view, close up smile
        pov "No, I was looking for you! I had something important to tell you."
        irina "Well, I don't know what's so important, that you felt like you needed to invade the women's shower stalls."
    scene town fitness shower 6pm 006b #Irina showering looking at MC, body turned, view from above, hand on MC
    irina "Maybe you will give me a hint, if I ask nicely."
    pov "You know I'm having the hardest time remembering..."
    scene town fitness shower 6pm 008b #Irina showering looking at MC, body turned, view from above, kissing MC
    "She interupts you with a kiss. It quickly becomes passionate between you two"
    scene town fitness shower 6pm 007b #Irina showering looking at MC, body turned for full view, close up finger in mouth
    irina "So what do you think? Was that nice enough for you?"
    pov "[irina] I'm fairly certain that would by nice enough for anybody!"
    pov "But if I'm being honest, I can't remember much of anything else right now..."
    irina "Haha! Well how about you come back to see me when you do?"
    scene town fitness shower 6pm 006b #Irina showering looking at MC, body turned, view from above, hand on MC
    with vpunch
    "With that she teasingly pushes you out of the stall and gives you a wink just before closing the curtain."
    scene black
    povi "Hot damn! We really need to get together more!"
    $ fitnessshowercas = False
    $ fitnessshoweriri = False
    jump fitnessshowerback

label fitnesslockercasloveend:
    bs "Yes."
    scene town fitness 4pm 036cl
    bs "I need to go, sorry [pov]."
    povi "Why is she sorry?"
    pov "No problem [bs]."
    povi "Why would I be upset after I got so far.."
    scene town fitness 4pm 037cl
    irina "[pov]?"
    pov "Huh?"
    irina "We need to change so we can go, you need to leave."
    pov "Oh you're right, sorry."
    scene black
    "They'll be gone soon so you leave the fitness studio."
    $ dtime += 1
    jump town

label fitnesscasntr:
    bs "I need to take a shower now!"
    scene black
    "She left in a hurry to the showers."
    povi "Hm, I'll follow her in a few minutes, so we can have more fun."
    "You wait a few minutes, get undressed and go into the showers."
    "Hnng... ohhh..."
    povi "Wait a moment, that's [bs] voice!"
    "You spy around the corner."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene town fitness shower 5pm 001n
    call screen checkdarkerpaths_cassandra
    jump fitnesscasntrstart

label fitnesscasntrstart:
    if cassandra_ntr == True or cassandra_voyeur == True:
        if cassandra_voyeur == True:
            povi "Oh she has a guest and it's Davide."
            bs "Hah, you promised me you'd go... slow... AHH!"
            davide "Shut up slut! You agreed to take my dick!"
            bs "Hah, but..."
            davide "Your hole needs to be widened!"
        else:
            povi "What the hell is Davide doing here?"
            bs "Hah, you promised me you'd go... slow... AHH!"
            davide "Shut up slut! You agreed to take my dick!"
            bs "Hah, but..."
            davide "Your hole needs to be widened!"
    else:
        if cassandra_revenge == True:
            povi "What the hell is Davide doing here? I fucking hate that guy."
            bs "Hah, you promised you'd let me go... please don't... AHH!"
            davide "Shut up slut! You agreed to do what I told you!"
            bs "Hah, but it wasn't supposed..."
            davide "Your hole needs to be widened!"
        else:
            povi "What is Davide doing here? That playa is everywhere!"
            bs "Hah, you promised you'd let me go... please don't... AHH!"
            davide "Shut up slut! You agreed to do what I told you!"
            bs "Hah, but it wasn't supposed..."
            davide "Your hole needs to be widened!"
    scene town fitness shower 5pm 002n
    bs "AAHH, you're crazy!"
    if cassandra_ntr == True or cassandra_voyeur == True:
        if cassandra_voyeur == True:
            povi "He's piercing her good!"
            davide "You love that, don't you?"
            bs "You're too big... hah..."
            davide "Then I have to fuck you harder so you can enjoy it more!"
            bs "Hah, aah wait..."
        else:
            povi "No, why is she doing this?!"
            davide "You love that, don't you?"
            bs "You're too big... hah..."
            davide "Then I have to fuck you harder so you can enjoy it more!"
            bs "Hah, aah wait..."
    else:
        if cassandra_revenge == True:
            povi "He's hurting her! This has to stop."
            davide "You love that, don't you?"
            bs "No I don't, You're too big... hah..."
            davide "Then I'll have to fuck you harder so you can really start to enjoy it!"
            bs "Hah, aah wait... No!"
        else:
            povi "He's forcing her? That's what happens when you don't train your sluts well enough."
            davide "You love that, don't you?"
            bs "No I don't, You're too big... hah..."
            davide "Then I'll have to fuck you harder so you can really start to enjoy it!"
            bs "Hah, aah wait... No!"
    if cassandra_ntr == True or cassandra_voyeur == True:
        if cassandra_voyeur == True:
            povi "He's so lucky. Having so much fun!"
            scene town fitness shower 5pm 003n
            bs "Hah, hah, hah..."
            davide "As I thought, you're just another whore craving for my dick!"
            bs "I just... we made a deal..."
            davide "You really think you can satisfy me with just a fuck?"
            povi "What's going on?"
            bs "But you said..."
            davide "Then you have to put more effort in it!"
            bs "I really want to know what's going on in the basement!"
            davide "And I really need to penetrate you more!"
        else:
            povi "I can't stop watching..."
            scene town fitness shower 5pm 003n
            bs "Hah, hah, hah..."
            davide "As I thought, you're just another whore craving for my dick!"
            bs "I just... we made a deal..."
            davide "You really think you can satisfy me with just a fuck?"
            povi "What's going on?"
            bs "But you said..."
            davide "Then you have to put more effort in it!"
            bs "I really want to know what's going on in the basement!"
            davide "And I really need to penetrate you more!"
    else:
        if cassandra_revenge == True:
            povi "Didn't you hear her?"
            scene town fitness shower 5pm 003n
            bs "Hah, ouch, fuck..."
            davide "As I thought, you're just another whore craving for my dick!"
            bs "Fuck you! I just... we made a deal..."
            davide "You really think you could have satisfied me with just a handjob?"
            povi "What's going on?"
            bs "But you said..."
            davide "Well, you,re gonna have to put more effort in it!"
            bs "I really want to know what's going on in the basement!"
            davide "And I really need to penetrate you more!"
        else:
            if inc == True:
                povi "I don't think he's going to stop now sis. Haha!"
            else:
                povi "I don't think he's going to stop now [bs]. Haha!"
            scene town fitness shower 5pm 003n
            bs "Hah, ouch, fuck..."
            davide "As I thought, you're just another whore craving for my dick!"
            bs "Fuck you! I just... we made a deal..."
            davide "You really think you could have satisfied me with just a handjob?"
            povi "That's true, bitch should know better."
            bs "But you said..."
            davide "Well, you,re gonna have to put more effort in it!"
            bs "I really want to know what's going on in the basement!"
            davide "And I really need to penetrate you more!"
    scene town fitness shower 5pm 004n
    bs "Ahh, ahh..."
    if cassandra_ntr == True or cassandra_voyeur == True:
        if cassandra_voyeur == True:
            povi "She's letting him fuck her for access to the basement?"
            povi "I'm sure he tricked her. But it's a good thing to know that."
        else:
            povi "She's letting him fuck her for access to the basement?"
            povi "I'm sure he tricked her. I can't believe she would knowingly let him do that."
    else:
        if cassandra_revenge == True:
            povi "She was doing this for access to the basement?"
            povi "I'm sure he tricked her. She woudn't be that desperate to see the basement, right?"
        else:
            povi "She was doing all this just for access to the basement?"
            povi "Fucking slut is desperate to get down there! I could use that later."
    davide "That's your weak spot, isn't it?"
    bs "Ohhh... ahhh..."
    davide "Your slutty body needs that hard pounding!"
    if cassandra_revenge == True:
        povi "Don't talk like that you damn..."
    if cassandra_sadist == True:
        povi "I may not like the dude, but he's right."
    davide "Say hello to our guest!"
    bs "Hah, what...?"
    povi "Damn, did he noticed me?"
    davide "You can come out [pov], I know you're watching."
    scene town fitness shower 5pm 005n
    "You reveal yourself."
    bs "HNNG...!"
    davide "Oh come on, you're gonna love being watched while you get fucked."
    if inc == True:
        davide "Especially by your brother!"
    else:
        davide "Especially by your friend!"
    bs "Hnn... no..."
    if cassandra_ntr == True or cassandra_voyeur == True:
        if cassandra_voyeur == True:
            if cdate5bj == True or cdate5fuck == True or cdate5hj == True:
                pov "Yeah, she gets excited when she has an audience."
            else:
                pov "I wasn't sure at first, but know I can see it now."
            if inc == True:
                davide "See? Your brother is with me."
            else:
                davide "See? [pov] is with me."
        else:
            if cdate5bj == True or cdate5fuck == True or cdate5hj == True:
                povi "She did seem to enjoy having an audience before..."
            else:
                pov "I don't know if he's really into this."
            if inc == True:
                davide "Trust me, she likes having her brother watch her."
            else:
                davide "Trust me, she likes having you watch her."
    else:
        if cassandra_revenge == True:
            pov "Fuck you Davide..."
            davide "Oh come on, don't be mad. I know you love to watch her getting fucked."
        else:
            if cdate5bj == True or cdate5fuck == True or cdate5hj == True:
                pov "Yeah, the bitch gets excited when she has an audience."
            else:
                pov "I wasn't sure at first, but know I can see it now."
            if inc == True:
                davide "See? Your brother is with me."
            else:
                davide "See? [pov] is with me."
    davide "And I bet you'd love to have even more of an audience but sadly no one else is here."
    if cassandra_ntr == True or cassandra_voyeur == True:
        bs "Hnng..."
        scene town fitness shower 5pm 006n
        davide "No need to deny it anymore, you're getting so damn tight."
        bs "Hah, hah, wait..."
        davide "Let's show him your wet and naughty hole!"
        bs "You... hah... AHH... AHHH!"
        davide "You're about to cum, slut?"
        bs "Hah... yes...!"
        davide "You're not allowed to!"
        scene town fitness shower 5pm 007n
        davide "Get ready for my spunk bitch!"
        bs "But I was so... close..."
        davide "I don't care, your cumming wasn't part of the deal."
        if cassandra_voyeur == True:
            povi "Hm, he's dominating her and showing her her place."
        else:
            povi "I just don't think I can do anything to stop him."
    else:
        bs "Please stop... Hnng..."
        scene town fitness shower 5pm 006n
        davide "No need to deny it anymore, you're getting so damn tight."
        bs "No I'm fucking not... Get the fuck out of me!"
        davide "Let's show him your wet and naughty hole!"
        bs "You... hah... Fucking... AHH... Asshole!!! AHHH!"
        davide "You're about to cum, slut?"
        bs "Never...!"
        davide "Yes you are you dirty bitch! Well it doesn't matter, you're not allowed to!"
        scene town fitness shower 5pm 007n
        davide "Get ready for my spunk bitch!"
        bs "No, get away from me!"
        davide "I don't care what you say cunt! I'm going to cover that fiesty face with my cum."
        if cassandra_revenge == True:
            povi "That asshole! He tricked her, abused her and now he's gonna humiliate her."
        else:
            povi "I have to say, that fucker has style. I can't deny that."
    davide "Get yourself ready!"
    scene town fitness shower 5pm 008n
    davide "ARG! Take it you dirty slut!"
    bs "Hnng..."
    scene town fitness shower 5pm 009n
    davide "Hah...!"
    if cassandra_ntr == True or cassandra_voyeur == True:
        if cassandra_voyeur == True:
            pov "Nice!"
        else:
            pov "Nooo!"
    else:
        if cassandra_revenge == True:
            povi "God damn it! I'm going to kill him!"
        else:
            pov "Nice! Don't worry [bs], I'll do the honors next time."
    davide "Now I relieved myself I'll take your suggestion under advisement!"
    bs "But I thought we made a deal?"
    davide "And I don't give a fuck! Maybe I'll let you try to convice me again sometime."
    bs "But..."
    davide "Shut up slut! Enjoy my spunk and learn your place!"
    if cassandra_ntr == True or cassandra_voyeur == True:
        if cassandra_voyeur == True:
            povi "That's a nice trick! Maybe that's something I can do too."
        else:
            povi "He's just too strong... I can't do anything!"
    else:
        if cassandra_revenge == True:
            povi "I knew it! He treats her like a whore!"
        else:
            povi "Bitch needs to get that shit into writing before hand. Everyone knows that."
    scene town fitness shower 5pm 010n
    davide "You're still enjoying the show, haha."
    davide "I bet you're waiting to get your turn now, the bitch is still in heat."
    if cassandra_voyeur == True or cassandra_sadist == True:
        pov "Hmm..."
    bs "Noo..."
    davide "But you're not allowed. We'll leave her now so she can rub my spunk all over herself."
    if cassandra_ntr == True or cassandra_voyeur == True:
        if cassandra_voyeur == True:
            pov "Haha!"
        else:
            pov "..."
    else:
        if cassandra_revenge == True:
            povi "What are you thinking, you damn asshole! Kick Davide's ass!!! Do something [pov]!"
        else:
            pov "Fuck that \"allowed\" shit, I don't want your diseased cum near me. I ain't fucking your sloppy seconds."
    scene black
    "Davide drags you out of the shower."
    davide "Go home [pov]. There's nothing more to do for you here."
    if cassandra_revenge == True or cassandra_sadist == True:
        "You can't beat him in a fight yet, so you leave the fitness studio."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ dtime += 1
    jump town
