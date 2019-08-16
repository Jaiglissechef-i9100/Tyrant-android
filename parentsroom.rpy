#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. Time Location - Featured - Scenes
#----- End List -----

#----- Edited -----
label proom19watch:
    hide screen locations
    scene main 7pm parents room
    mom "Ahhh... ahhh... ahhh..."
    if inc == True:
        povi "Wow, Mom and dad are fucking."
    else:
        povi "Wow, [mother] and Bruce are fucking."
    mom "Harder... please harder..."
    povi "She seems to be enjoying it."
    povi "Getting a hard ride like that."
    mom "Oh my god, yes. I can feel your hard dick."
    $ proom19fuck = True
    jump parentsroom

#----- Custom -----
screen proom19watchalternatechoice:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('proom19watchalternatechoice'), Jump('proom19watchaltlove')) hovered tt.Action ("Let her sleep [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('proom19watchalternatechoice'), Jump('proom19watchaltcorruption')) hovered tt.Action ("Play with her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('proom19watchalternatechoice'), Jump('proom19watchaltnosexbruce')) hovered tt.Action ("Play with her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom19watchalternate:
    hide screen locations
    call screen proom19watchalternatechoice

label proom19watchaltcorruption:
    scene edited parentsroom nosexbruce
    "You step into the doorway. They don't notice you."
    dad "Come on [mother]... I really need this! You're my wife!"
    if inc == True:
        mom "I've told you already, my pussy belongs to our son now! All of me does. You should be happy I'm letting you watch while I get dressed."
    else:
        mom "I've told you already, my pussy belongs to [pov] now! All of me does. You should be happy I'm letting you watch while I get dressed."
    dad "Seriously?!? You're really doing this? I can't believe this is what you want!"
    scene edited parentsroom nosexbruce2
    "[mother] turns her head and looks right at you."
    mom "Oh I want it sooooo badly!"
    povi "I guess she did notice me. I never knew she'd like punishing Bruce so much. It's fucking hot!"
    "You mouth the words \"Good Girl\" to her."
    scene edited parentsroom nosexbruce
    dad "Please honey! Don't do this."
    mom "Your begging is bumming me out. Leave!"
    povi "Damn! That's harsh."
    "You leave Bruce to his humiliation and head back to your room."
    jump mcroom

label proom19watchaltlove:
    scene edited parentsroom nosexbruce
    "You step into the doorway. They don't notice you."
    dad "Come on [mother]... I really need this! You're my wife!"
    if inc == True:
        mom "I've told you already, I don't love you like that anymore. My heart belongs to my son now. Please don't sit there and beg like this. It's embarressing."
    else:
        mom "I've told you already, I don't love you like that anymore. My heart belongs to [pov] now. Please don't sit there and beg like this. It's embarressing."
    dad "Seriously?!? You're really doing this? I can't believe this is what you want!"
    scene edited parentsroom nosexbruce2
    "[mother] turns her head and looks right at you."
    mom "Oh hey, sweetie! I thought that was you! Do you need anything my love?"
    povi "I guess she did notice me."
    pov "Not right now, I was just checking in."
    pov "Okay dear. I'll see you downstairs in a bit."
    scene edited parentsroom nosexbruce
    dad "I can't believe this... <sobs>"
    mom "Please just go Bruce..."
    povi "Damn! He's really taking this hard."
    "You leave them to work this out and head back to your room."
    jump mcroom

label proom19watchaltnosexbruce:
    scene edited parentsroom nosexbruce
    "You step into the doorway. They don't notice you."
    dad "Come on [mother]... I really need this! You're my wife!"
    if inc == True:
        mom "I've told you already, that's not what my son wants! I'm not going to have sex with you. You should be happy I'm letting you watch while I get dressed."
    else:
        mom "I've told you already, that's not what [pov] wants! I'm not going to have sex with you. You should be happy I'm letting you watch while I get dressed."
    dad "Seriously?!? You're really doing this? I can't believe this is what you want!"
    scene edited parentsroom nosexbruce2
    "[mother] turns her head and looks right at you."
    mom "Well it is what I want!"
    povi "I guess she did notice me. I never knew she'd be punishing Bruce so much. It's pretty hot!"
    "You mouth the words \"Good Girl\" to her."
    scene edited parentsroom nosexbruce
    dad "Please honey! Don't do this."
    mom "Your just not gettings it. Please leave now."
    povi "Damn! That's harsh."
    "You leave them and head back to your room."
    jump mcroom

label proomlooktits:
    hide screen locations
    scene parentsroom 8pm 002a
    povi "Her big breasts never fail to amaze me."
    jump parentsroom

label proomlookcrotch:
    hide screen locations
    scene parentsroom 8pm 002b
    povi "I seriouslly love her choice in panties!"
    povi "Hopefully I'll get her to let me see what lies underneath."
    jump parentsroom

label proomlookpicture:
    hide screen locations
    scene parentsroom 8pm 002c
    povi "Another of those kinky pictures. The girl is damn hot."
    povi "I wonder where they got them?"
    jump parentsroom

label proomtalk:
    hide screen locations
    if proom8pm == True:
        jump proom8repeat1
    if inc == True:
        pov "Hi mom!"
    else:
        pov "Hi [mother]!"
    scene parentsroom 8pm 003
    if momrelationship < 30 and momntr == True:
        $ randomnum = renpy.random.randint(1,2)
        if randomnum == 1:
            jump nicoleshakylroom
        elif randomnum == 2:
            " "
    mom "Eh?"
    mom "What are you doing here [pov]? Don't you see that I'm changing?"
    pov "Yes I see that. But I didn't do it on purpose."
    pov "I had no idea that's what you were doing before I got here."
    scene parentsroom 8pm 004
    mom "Oh, of course not. It's not like I told you what I going to be doing."
    mom "Sorry about that."
    if inc == True:
        mom "So this is your dad's and my room."
    else:
        mom "So this is Bruce's and my room."
    pov "It seems a little small."
    mom "We only need it for sleeping and changing in."
    pov "Makes sense. I noticed you have another kinky picutre up here as well. And this one is the most perverted of all, haha."
    scene parentsroom 8pm 005
    mom "You mean...? Yeah, you're right."
    pov "You even can see her pussy."
    mom "Hmm..."
    scene parentsroom 8pm 004
    if inc == True:
        mom "Your dad and I decided that this one shouldn't be seen by your sisters."
    else:
        mom "Bruce and I decided that this one shouldn't be seen by our daughters."
    mom "But it's still art, right?"
    pov "Haha, yes it is. I might like this one the best out of the rest of them."
    mom "Mmm..."
    pov "So you're trying on some new stockings for later?"
    mom "Yes I want to change something with that outfit."
    jump prcinc

label prcinc:
    call screen prcinc1

screen prcinc1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('prcinc1'), Jump('proom8love')) hovered tt.Action ("Answer to improve Love [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('prcinc1'), Jump('proom8cor')) hovered tt.Action ("Answer to improve Corruption [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom8love:
    pov "That's a good idea!"
    scene parentsroom 8pm 006a
    mom "Thank you."
    pov "I think it will make the whole outfit look even better."
    pov "Which I didn't even think was possible."
    mom "What do you mean...?"
    if inc == True:
        pov "You're so damn beautiful mom. You're hot body packed into those tight clothes. Like a gift begging to be unwrapped."
    else:
        pov "You're so damn beautiful [mother]. You're hot body packed into those tight clothes. Like a gift begging to be unwrapped."
    scene parentsroom 8pm 007a
    mom "Oh...?"
    mom "Well, Th... thank you [pov]."
    if inc == True:
        pov "No need to be shy. I'm proud that my mom is such a beauty."
    else:
        pov "No need to be shy, [mother]. I'm proud that you're such a beauty."
    mom "..."
    mom "Isn't that... wrong?"
    pov "I don't think so."
    pov "I can't wait to see you later."
    mom "..."
    $ momrelationship += 1
    $ momlove += 1
    $ proom8pm = True
    $ dtime += 1
    jump parentsroom

label proom8cor:
    pov "That's a good idea! You need to look even more slutty!"
    scene parentsroom 8pm 006b
    mom "What...?"
    pov "You're just doing your best to look and act the part of a depraved gang wife."
    mom "But I wasn't suppose to..."
    if droom7momlookcor == True:
        pov "Maybe not, but you are forgetting about something we talked about."
        mom "Eh?"
        pov "Playing our roles correctly, the woman should do what the man decides is best for her."
        mom "I'm not sure..."
        pov "Well I am, Remove you hands."
        mom "..."
        scene parentsroom 8pm 007b
        mom "I don't understand why this is necessary."
        pov "Because I want to see them. The hot tits of a sexy woman."
        mom "Hmm..."
        scene parentsroom 8pm 008b
        if inc == True:
            pov "Dad is such a lucky bastard! I bet he can't wait to get his hands on them anytime you're around."
            mom "What are you talking about? Watch your language, son!"
        else:
            pov "Bruce is such a lucky bastard! I bet he can't wait to get his hands on them anytime you're around."
            mom "What are you talking about? Watch your language, [pov]!"
        pov "No I don't think I will! I want to knead them and play with them. To own them."
        mom "Hnn... No, that's wrong."
        scene parentsroom 8pm 009b
        pov "Maybe it's normally wrong. But in our situation, it's definitely not!"
        mom "But..."
        pov "Quiet now! It was your wish that I participate and so I am."
        pov "So you'll have to play along too, or I won't do it anymore."
        mom "Okay... it's still not right but I won't complain anymore."
        pov "Good girl."
        mom "Hmm..."
        $ momrelationship += 1
        $ momcorruption += 1
        $ proom8pm = True
        $ dtime += 1
        jump parentsroom
    else:
        pov "Maybe, but it's still a good idea and I still can't wait to see how you'll look in that outfit later."
        mom "Hmm..."
        $ momrelationship += 1
        $ momcorruption += 1
        $ proom8pm = True
        $ dtime += 1
        jump parentsroom

label proom24closer:
    hide screen locations
    scene parentsroom 0am 002
    if inc == True:
        povi "Mom's sleeping."
    else:
        povi "[mother]'s sleeping."
    povi "Damn, she's so sexy. Maybe I could play around a little with her?"
    jump pr24dec

label pr24dec:
    scene parentsroom 0am 002
    call screen pr24dec1

screen pr24dec1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('pr24dec1'), Jump('proom24love')) hovered tt.Action ("Let her sleep [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('pr24dec1'), Jump('proom24cor')) hovered tt.Action ("Play with her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom24love:
    povi "No. I can't do that. She had a long day, I should let her sleep."
    povi "She was so tired she didn't even undress fully or cover up."
    scene parentsroom 0am 007
    "You cover her up."
    povi "Much better. No need for her to catch a cold or worse."
    povi "Hopefully she can get some rest tonight."
    $ momlove += 1
    $ dtime += 1
    jump parentsroom

label proom24cor:
    povi "What should I do with her? I could touch her, maybe jerk off too?"
    jump pr24dcor

label pr24dcor:
    call screen pr24dcor1

screen pr24dcor1():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" action (Hide('pr24dcor1'), Jump('proom24ass')) hovered tt.Action ("Play with her ass [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_red_%s.png" action (Hide('pr24dcor1'), Jump('proom24feet')) hovered tt.Action ("Play with her feet [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label proom24ass:
    scene parentsroom 0am 003a
    povi "I can't wait. I want to play with her hot ass."
    povi "It's so damn beautiful and curvy. Might as well see what it feels like now!"
    scene parentsroom 0am 004a
    povi "Oh my god! I'm touching her ass cheeks."
    povi "And they're so soft and warm. Maybe I should rub my dick between them?"
    mom "Hmm..."
    povi "She reacted to my touch. But she's still sleeping."
    povi "I shouldn't over do it this time. I'll just jerk off, but I'll have to be quiet."
    scene parentsroom 0am 005a
    povi "She's so damn sexy. That hot body, slender and curvy in all the right places."
    povi "I wonder if she works out too?"
    povi "This make me so horny, I can't take it any longer. I think I'm going to cum on her ass!"
    scene parentsroom 0am 006a
    pov "Hnnng..."
    mom "Hmm..."
    povi "Damn, I'll have to be more quiet!"
    if inc == True:
        povi "Don't wake up mom while I cum on you!"
        povi "Keep dreaming about making love with your son, hehe."
    else:
        povi "Don't wake up [pov] while I cum on you!"
        povi "Keep dreaming about making love with me, hehe."
    povi "Wow, that was so good."
    $ momcorruption += 1
    $ dtime += 1
    jump parentsroom

label proom24feet:
    scene parentsroom 0am 003b
    povi "I can't wait. I want to play with her sexy feet."
    povi "They're so tender and good looking in those stockings."
    scene parentsroom 0am 004b
    povi "Oh my god! I'm touching her sexy feet."
    povi "And they're so soft and warm. Maybe I should rub my dick between them?"
    mom "Hmm..."
    povi "She reacted to my touch. But she's still sleeping."
    povi "I shouldn't over do it this time. I'll just jerk off, but I'll have to be quiet."
    scene parentsroom 0am 005b
    povi "She's so damn sexy. These stocking feel amazing."
    povi "And the warmth of her feet. That soft feel against my hands."
    povi "This is making me so horny, I can't take it any longer. I'll cum on her feet!"
    scene parentsroom 0am 006b
    pov "Hnnng..."
    mom "Hmm..."
    povi "Damn, I'll have to be more quiet!"
    if inc == True:
        povi "Don't wake up mom while I cum on you!"
        povi "Keep dreaming about making love with your son, hehe."
    else:
        povi "Don't wake up [pov] while I cum on you!"
        povi "Keep dreaming about making love with me, hehe."
    povi "Wow, that was so good."
    $ momcorruption += 1
    $ dtime += 1
    jump parentsroom

#----- Custom Event Cassandra and MC -----
screen mccassandra6pmchoice:
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('mccassandra6pmchoice'), SetVariable('mccassandra6pmlove', True), Return(None)) hovered tt.Action ("Love") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('mccassandra6pmchoice'), SetVariable('mccassandra6pmlove', False), Return(None)) hovered tt.Action ("Corruption") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value at center

label mccassandra6pmevent:
    if cassandmcparentsroom == True:
        jump mccassandra6pmeventrepeat
    hide screen locations
    bs "Hey, [pov] are you out there?"
    if inc == True:
        povi "Was that [bs] in mom and dad's room?"
    else:
        povi "Was that [bs] in [mother] and Bruce's room?"
    pov "Yeah, I'm out here..."
    povi "But what is she doing in there?"
    "You go to open the door, but she beats you to it."
    scene edited parentsroom 6pm 001
    call screen mccassandra6pmchoice
    if mccassandra6pmlove == True:
        pov "What's going on [bs]? Why are you in here?"
        scene edited parentsroom 6pm 001shh
        bs "Shhh... we need to be quiet"
        "You both talk in hushed tones..."
        scene edited parentsroom 6pm 001
        bs "Now get in here, I want to show you something."
        povi "Ok... what is she up to?"
    else:
        pov "What do you think you're doing in here [bs]?"
        scene edited parentsroom 6pm 001shh
        bs "Shhh... we need to be quiet"
        "You both talk in hushed tones..."
        scene edited parentsroom 6pm 001
        bs "Now I'm going to show you why I'm in here, so get in."
        povi "Don't have to tell me twice..."
    scene edited parentsroom 6pm 002
    if mccassandra6pmlove == True:
        povi "Whoa, I like this outfit!"
        bs "<giggles> I think someone likes my sweater..."
    else:
        pov "Now that is what I'm talking about!"
        bs "<giggles> I'm glad you like my sweater."
    "She sits down on the bed, looking at you while she bites the edge of her lower lip."
    scene edited parentsroom 6pm 003
    if mccassandra6pmlove == True:
        pov "So... I take it we're missing dinner."
        bs "I thought we could do something else..."
    else:
        pov "I see we're skipping dinner then..."
        bs "Exactly what I was thinking."
    scene edited parentsroom 6pm 004
    if mccassandra6pmlove == True:
        bs "Why don't you relax a little?"
        if inc == True:
            pov "Our parents are just right down the hall!"
        else:
            pov "Your parents are just right down the hall!"
        bs "It's ok, we'll be quick..."
    else:
        bs "Why don't you relax a little?"
        if inc == True:
            pov "Well to be honest, the idea of our parents just down the hall has got me a bit excited."
        else:
            pov "Well to be honest, the idea of your parents just down the hall has got me a bit excited."
        bs "Just a bit excited..."
    scene edited parentsroom 6pm 005
    if mccassandra6pmlove == True:
        bs "Now take that out so we can play!"
        pov "Seriously, you want to do that here, right now?"
    else:
        bs "Looks like you're more than a little excited to me."
        pov "Maybe, why don't you help me get really excited?"
    scene edited parentsroom 6pm 006
    if mccassandra6pmlove == True:
        bs "Does this answer your question?"
        pov "Well, yeah. I think that's definitely an answer. Do you really think we won't get caught?"
        if inc == True:
            bs "I think it doesn't matter if we do. You already outed me to mom and dad."
        else:
            bs "I think it doesn't matter if we do. You already outed me to [mother] and Bruce."
        pov "Yeah, but [ls] doesn't know about us yet."
        bs "True but don't you think it's kind of fun sneaking around like this?"
    else:
        bs "Does this help you get excited?"
        if inc == True:
            pov "Definitely, and the idea of our parent's walking in on us is getting me pretty excited too."
            bs "Oh yeah? You want them to catch us?"
            pov "Well either way it won't matter. I've already claimed you. But yeah, I think it would be great of they saw me fucking my sister on their bed."
        else:
            pov "Definitely, and the idea of your parent's walking in on us is getting me pretty excited too."
            bs "Oh yeah? You want them to catch us?"
            pov "Well either way it won't matter. I've already claimed you. But yeah, I think it would be great of they saw me fucking their daughter on their bed."
    scene edited parentsroom 6pm 007
    if mccassandra6pmlove == True:
        pov "Well, if you put it like that, then ya. I do find it exciting."
        bs "Good, because it would pretty much be criminal if you left me hang like this."
        pov "I would never do that!"
    else:
        bs "Yeah, you want them to catch you balls deep in this tight, wet pussy?"
        if inc == True:
            pov "Sure do. I want them to watch their daughter getting pounded hard, begging for her brother's big dick."
        else:
            pov "Sure do. I want them to watch their daughter getting pounded hard, begging for my big dick."
        bs "Speaking of big dicks, why don't you whip that monster out and let me get to work on it?"
    scene edited parentsroom 6pm 008
    if mccassandra6pmlove == True:
        bs "Just what I wanted to hear! Now take that monster out and let me play with it!"
        pov "Oh yeah, you want to play with this?"
        "You grab your hard dick through your pants and tease her a bit."
        bs "Yeah, that's exactly what I want!"
        pov "Then I want to you ask me nicely..."
        if inc == True:
            bs "Please, little brother... Please pull out your magnificent cock and let your big sister play with it."
        else:
            bs "Please, [pov]... Please pull out your magnificent cock and let me play with it."
    else:
        pov "I told you that you needed to bet for it. I haven't heard any begging yet..."
        bs "Please daddy, please let me see your fat cock! I want it! I need it! Please!"
        pov "Now that's a good girl. And good girls get rewarded."
        "You unzip your pants let you cock hang free."
    scene edited parentsroom 6pm 009
    if mccassandra6pmlove == True:
        "You unzip your jeans and pull out your cock. Her hand rushes up and grabs it."
        pov "Hey! Be careful there! That thing is attached you know!"
        bs "Hnnng... Yes it is."
    else:
        "[bs] reaches her hand out and grabs your cock firmly."
        pov "Hey! Be careful there! That thing is attached you know!"
        bs "Sorry... I just couldn't help it."
        pov "Well if you just couldn't help then... I guess it's ok. Haha."
        pov "But if you're going to want to do more than touch it, then you know the drill."
    if mccassandra6pmlove == True:
        scene edited parentsroom 6pm 010lov
        pov "So what else do you want to do with it?"
        bs "Can I taste it now?"
        pov "Haven't you had enough of that already?"
        bs "No! Never! So can I?"
    else:
        scene edited parentsroom 6pm 010cor
        bs "Please daddy, can I taste it? I really really want to taste it please!"
        pov "Good girl, asking politely. You may taste it."
    scene edited parentsroom 6pm 011
    if mccassandra6pmlove == True:
        "She bends down and opens her mouth, but obediently waits for your response."
        pov "Since you asked nicely..."
    else:
        "She bends down and opens her mouth, but obediently waits for your command."
        pov "Good girls get rewards. Go on."
    scene edited parentsroom 6pm 012
    if mccassandra6pmlove == True:
        bs "Yummmm... <suck> <lick>"
        pov "Whoa, you're really going at it! I like it!"
        bs "Mmhmmm! <suck>"
    else:
        bs "Mmmm... <suck> <lick>"
        pov "That's good... Hmmm..."
    scene edited parentsroom 6pm 013
    if mccassandra6pmlove == True:
        "She takes you deeper, her tongue cradling the shaft of your cock."
        pov "Oh god [bs], that feels amazing... Hah... yeah..."
        bs "<suck> Hnng... <lick> Hmmm..."
        "It doesn't take her long to give you that familiar sensation in your balls."
        pov "Oh... shit... I'm getting close."
        "She quickly removes her mouth from your cock and sits up."
    else:
        "She takes you deeper, her tongue cradling the shaft of your cock."
        pov "Oh fuck yes [bs], that feels amazing... Hah... yeah..."
        bs "<suck> Hnng... <lick> Hmmm..."
        "It doesn't take her long to give you that familiar sensation in your balls."
        pov "Oh... shit... I'm getting close."
        "She quickly removes her mouth from your cock and sits up."
    scene edited parentsroom 6pm 014
    if mccassandra6pmlove == True:
        pov "Hey! What gives?! That's just cruel doing something like that!"
        bs "<giggle> It's not that. I just had somewhere else I wanted you to finish..."
        "She leans back and guides your cock to her wet entrance."
    else:
        pov "Hey, What the hell do you think you're doing. I was so close!"
        bs "<giggle> I have somewhere else I want you to finish..."
        "She leans back and guides your cock to her wet entrance."
    scene edited parentsroom 6pm 015
    if mccassandra6pmlove == True:
        bs "I want you to cum inside me."
        pov "Are you sure?"
        bs "Yes, I want feel you as you drench my wet pussy with your sperm."
    else:
        bs "Please cum inside me! Please cum inside my tight wet pussy."
        pov "Good girl, you remembered to ask nicely."
    scene edited parentsroom 6pm 016
    if mccassandra6pmlove == True:
        "You shove your cock inside. It only takes a few hard strokes until you're ready to blow your load."
        povi "This is so hot!"
        bs "I can feel you, you're about to cum aren't you?"
        pov "Yes, I'm going to cum!"
        bs "Do it [pov]! Cum inside me! Fill me up!"
    else:
        "You shove your cock inside. It only takes a few hard strokes until you're ready to blow your load."
        povi "This is so fucking hot!"
        bs "I can feel you, you're about to cum aren't you?"
        pov "Yes, I'm going to cum!"
        bs "Please do it [pov]! Please cum deep inside me! Fill me up!"
    scene edited parentsroom 6pm 017
    with vpunch
    if mccassandra6pmlove == True:
        pov "Hunngh!"
        bs "Oh wow, I can feel it!"
        bs "I feel you spraying inside me. I love it!"
        "She reaches up and pulls you close to her."
    else:
        pov "Hunngh!"
        bs "Oh shit! I can feel it!"
        bs "I feel you spraying inside me. I love it!"
        "She reaches up and pulls you close to her."
    scene edited parentsroom 6pm 018
    if mccassandra6pmlove == True:
        bs "Keep going! I'm close too..."
        povi "I just came, but I'm not going to let her down now."
        "You push through the sensitivety of your still swollen member and start pushing inside her again."
        pov "You're..."
        with vpunch
        pov "so..."
        with vpunch
        pov "wet!"
        with vpunch
        bs "Yes, oh yes!"
        with vpunch
        bs "Right... gah... there!"
        with vpunch
        bs "I'm cumming!"
    else:
        bs "Please fuck me! I'm close too..."
        povi "I just came, but I'm not going to stop now."
        "You push through the sensitivety of your still swollen member and start fucking her hard."
        pov "You're..."
        with vpunch
        pov "so fucking..."
        with vpunch
        pov "wet!"
        with vpunch
        bs "Yes, oh fuck!"
        with vpunch
        bs "Right... gah... there!"
        with vpunch
        bs "I'm cumming!"
    scene edited parentsroom 6pm 019
    with vpunch
    if mccassandra6pmlove == True:
        bs "FUU...HNNG!"
        "You feel her convulse and squeeze your cock as she climaxes."
        "You keep yourself pressed deep inside her, pressing your hips firmly against hers."
        bs "Huhhh... hah... oh..."
        "She lets out sweet little moans as her orgasm slowly subsides."
    else:
        bs "FUU...HNNG!"
        "You feel her convulse and squeeze your cock as she climaxes."
        "You keep yourself pressed deep inside her, pressing your hips firmly against hers."
        bs "Huhhh... hah... oh..."
        "She lets out little moans as her orgasm slowly subsides."
    if nicolereddresswear == True:
        scene main 6pm 6pm dining roomncc1
    elif nicolebabydollwear == True:
        scene main 6pm 6pm dining roomncc2
    elif nicolesweaterpantswear == True:
        scene main 6pm 6pm dining roomncl1
    elif nicolerobewear == True:
        scene main 6pm 6pm dining roomncl2
    else:
        scene main 6pm 6pm dining room
    dad "Did you hear something just now, sounded like moaning?"
    mom "I think I heard something too."
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
    if inc == True:
        mom "[ls] will you go and get your brother and sister? They're late for dinner."
    else:
        mom "[ls] will you go and get [pov] and [bs]? They're late for dinner."
    scene diningroom 6pm 008
    ls "Sure mom, I'll go get them."
    scene edited parentsroom 6pm 020
    if mccassandra6pmlove == True:
        ls "Hey there you guys ar... oh!"
        "[ls]'s intrusion goes unnoticed as you two continue to enjoy your post-coital bliss."
        bs "Hnnn... I just want to stay like this forever."
        pov "I could live with that."
        bs "<giggle>"
        ls "<whisper> I'll just leave you two alone... for now."
        scene black
        "She runs off to explain that you two are going to need a little bit longer to \"get ready\"."
        "You two finally pull yourselves together and leave the room."
    else:
        ls "Hey there you guy ar... oh!"
        "[ls]'s intrusion goes unnoticed as you two continue to enjoy the feeling after a great fuck."
        bs "Hnnn... I want that dick inside me forever."
        pov "I could live with that."
        bs "<giggle>"
        ls "<whisper> I'll just leave you two alone... for now."
        scene black
        "She runs off to explain that you two are going to need a little bit longer to \"get ready\"."
        "You two finally pull yourselves together and leave the room."
    $ mccassandra6pmlove = False
    $ cassandmcparentsroom = True
    $ dtime += 1
    jump parentsroom

#----- Custom Event -----
label mccassandra6pmeventrepeat:
    hide screen locations
    bs "Hey, [pov] are you out there?"
    if inc == True:
        povi "What is [bs] doing in mom and dad's room again?"
    else:
        povi "What is [bs] doing in [mother] and Bruce's room?"
    pov "Yeah, I'm out here..."
    povi "Does she want to play around again?"
    "You go to open the door, but she beats you to it."
    scene edited parentsroom 6pm 001
    call screen mccassandra6pmchoice
    if mccassandra6pmlove == True:
        pov "What's going on [bs]? Why are you doing in here again?"
        scene edited parentsroom 6pm 001shh
        bs "Shhh... we need to be quiet"
        "You both talk in hushed tones..."
        scene edited parentsroom 6pm 001
        bs "Now get in here, I want to fool around in here again."
        povi "Ok..."
    else:
        pov "What do you think you're doing in here again, [bs]?"
        scene edited parentsroom 6pm 001shh
        bs "Shhh... we need to be quiet"
        "You both talk in hushed tones..."
        scene edited parentsroom 6pm 001
        bs "Now I'm going to show you why I'm in here, so get in."
        povi "Don't have to tell me twice..."
    scene edited parentsroom 6pm 002
    if mccassandra6pmlove == True:
        povi "I still really like this outfit!"
        bs "<giggles> Someone still likes my sweater..."
    else:
        pov "I still like that sweater."
        bs "<giggles> I'm glad."
    "She sits down on the bed, looking at you while she bites the edge of her lower lip."
    scene edited parentsroom 6pm 003
    if mccassandra6pmlove == True:
        pov "So... I take it we're missing dinner again."
        bs "Definitely..."
    else:
        pov "I see we're skipping dinner again..."
        bs "Exactly what I was thinking."
    scene edited parentsroom 6pm 004
    if mccassandra6pmlove == True:
        bs "Still having a hard time relaxing?"
        if inc == True:
            pov "Our parents are still just down the hall..."
        else:
            pov "Your parents are still just down the hall..."
        bs "It's ok, we'll be quick..."
    else:
        bs "Still having a hard time relaxing?"
        if inc == True:
            pov "I still like the idea of our parents just down the hall, it has got me a bit excited."
        else:
            pov "I still like the idea of your parents just down the hall, it has got me a bit excited."
        bs "Just a bit excited?"
    scene edited parentsroom 6pm 005
    if mccassandra6pmlove == True:
        bs "Now take that out so we can play again!"
        pov "Alright, you convinced me..."
        povi "Not that I really needed a lot of convincing here."
    else:
        bs "Looks like you're more than a little excited to me."
        pov "True, let's see if you can kick it up a notch."
    scene edited parentsroom 6pm 006
    if mccassandra6pmlove == True:
        "You start to unzip your pants."
        pov "I see you're enjoying sneaking around like this again."
        if inc == True:
            bs "Well after you outed me to mom and dad as your \"slut\" I just thought I should keep acting the part."
        else:
            bs "Well after you outed me to my mom and dad as your \"slut\" I just thought I should keep acting the part."
        pov "Hehe, well if that's what you want, then I'm certainly ok with that. But [ls] still doesn't know about us."
        bs "True, but don't you think it's kind of fun sneaking around like this anyway?"
    else:
        bs "Does this help you get excited?"
        if inc == True:
            pov "Definitely, and the idea of our parent's walking in on us is getting me pretty excited too."
            bs "Oh yeah? You want them to catch us?"
            pov "Well either way it won't matter. I've already claimed you. But yeah, I think it would be great of they saw me fucking my sister on their bed."
        else:
            pov "Definitely, and the idea of your parent's walking in on us is getting me pretty excited too."
            bs "Oh yeah? You want them to catch us?"
            pov "Well either way it won't matter. I've already claimed you. But yeah, I think it would be great of they saw me fucking their daughter on their bed."
    scene edited parentsroom 6pm 007
    if mccassandra6pmlove == True:
        pov "Well, if you put it like that, then ya. I do find it exciting."
        bs "Good, because it would pretty much be criminal if you left me hang like this."
        pov "I would never do that!"
    else:
        bs "Yeah, you want them to catch you balls deep in this tight, wet pussy?"
        if inc == True:
            pov "Yes I do. I want them to watch their daughter getting pounded hard, begging for her brother's big dick."
        else:
            pov "Yes I do. I want them to watch their daughter getting pounded hard, begging for my big dick."
        bs "Speaking of big dicks, why don't you whip that monster out and let me get to work on it?"
    scene edited parentsroom 6pm 008
    if mccassandra6pmlove == True:
        bs "Just what I wanted to hear! Now take that monster out and let me play with it!"
        pov "Oh yeah, you want to play with this?"
        "You grab your hard dick through your pants and tease her a bit."
        bs "Yeah, that's exactly what I want!"
        pov "Then I want to you ask me nicely..."
        if inc == True:
            bs "Please, little brother... Please pull out your magnificent cock and let your big sister play with it."
        else:
            bs "Please, [pov]... Please pull out your magnificent cock and let me play with it."
    else:
        pov "I told you that you needed to bet for it. I haven't heard any begging yet..."
        bs "Please daddy, please let me see your fat cock! I want it! I need it! Please!"
        pov "Now that's a good girl. And good girls get rewarded."
        "You unzip your pants let you cock hang free."
    scene edited parentsroom 6pm 009
    if mccassandra6pmlove == True:
        "You unzip your jeans and pull out your cock. Her hand rushes up and grabs it."
        pov "Hey! Be careful there! That thing is attached you know!"
        bs "Hnnng... Yes it is."
    else:
        "[bs] reaches her hand out and grabs your cock firmly."
        pov "Hey! Be careful there! That thing is attached you know!"
        bs "Sorry... I just couldn't help it."
        pov "Well if you just couldn't help then... I guess it's ok. Haha."
        pov "But if you're going to want to do more than touch it, then you know the drill."
    if mccassandra6pmlove == True:
        scene edited parentsroom 6pm 010lov
        pov "So what else do you want to do with it?"
        bs "Can I taste it now?"
        pov "Haven't you had enough of that already?"
        bs "No! Never! So can I?"
    else:
        scene edited parentsroom 6pm 010cor
        bs "Please daddy, can I taste it? I really really want to taste it please!"
        pov "Good girl, asking politely. You may taste it."
    scene edited parentsroom 6pm 011
    if mccassandra6pmlove == True:
        "She bends down and opens her mouth, but obediently waits for your response."
        pov "Since you asked nicely..."
    else:
        "She bends down and opens her mouth, but obediently waits for your command."
        pov "Good girls get rewards. Go on."
    scene edited parentsroom 6pm 012
    if mccassandra6pmlove == True:
        bs "Yummmm... <suck> <lick>"
        pov "Whoa, you're really going at it! I like it!"
        bs "Mmhmmm! <suck>"
    else:
        bs "Mmmm... <suck> <lick>"
        pov "That's good... Hmmm..."
    scene edited parentsroom 6pm 013
    if mccassandra6pmlove == True:
        "She takes you deeper, her tongue cradling the shaft of your cock."
        pov "Oh god [bs], that feels amazing... Hah... yeah..."
        bs "<suck> Hnng... <lick> Hmmm..."
        "It doesn't take her long to give you that familiar sensation in your balls."
        pov "Oh... shit... I'm getting close."
        "She quickly removes her mouth from your cock and sits up."
    else:
        "She takes you deeper, her tongue cradling the shaft of your cock."
        pov "Oh fuck yes [bs], that feels amazing... Hah... yeah..."
        bs "<suck> Hnng... <lick> Hmmm..."
        "It doesn't take her long to give you that familiar sensation in your balls."
        pov "Oh... shit... I'm getting close."
        "She quickly removes her mouth from your cock and sits up."
    scene edited parentsroom 6pm 014
    if mccassandra6pmlove == True:
        pov "Hey! What gives?! That's just cruel doing something like that!"
        bs "<giggle> It's not that. I just had somewhere else I wanted you to finish..."
        "She leans back and guides your cock to her wet entrance."
    else:
        pov "Hey, What the hell do you think you're doing. I was so close!"
        bs "<giggle> I have somewhere else I want you to finish..."
        "She leans back and guides your cock to her wet entrance."
    scene edited parentsroom 6pm 015
    if mccassandra6pmlove == True:
        bs "I want you to cum inside me."
        pov "Are you sure?"
        bs "Yes, I want feel you as you drench my wet pussy with your sperm."
    else:
        bs "Please cum inside me! Please cum inside my tight wet pussy."
        pov "Good girl, you remembered to ask nicely."
    scene edited parentsroom 6pm 016
    if mccassandra6pmlove == True:
        "You shove your cock inside. It only takes a few hard strokes until you're ready to blow your load."
        povi "This is so hot!"
        bs "I can feel you, you're about to cum aren't you?"
        pov "Yes, I'm going to cum!"
        bs "Do it [pov]! Cum inside me! Fill me up!"
    else:
        "You shove your cock inside. It only takes a few hard strokes until you're ready to blow your load."
        povi "This is so fucking hot!"
        bs "I can feel you, you're about to cum aren't you?"
        pov "Yes, I'm going to cum!"
        bs "Please do it [pov]! Please cum deep inside me! Fill me up!"
    scene edited parentsroom 6pm 017
    with vpunch
    if mccassandra6pmlove == True:
        pov "Hunngh!"
        bs "Oh wow, I can feel it!"
        bs "I feel you spraying inside me. I love it!"
        "She reaches up and pulls you close to her."
    else:
        pov "Hunngh!"
        bs "Oh shit! I can feel it!"
        bs "I feel you spraying inside me. I love it!"
        "She reaches up and pulls you close to her."
    scene edited parentsroom 6pm 018
    if mccassandra6pmlove == True:
        bs "Keep going! I'm close too..."
        povi "I just came, but I'm not going to let her down now."
        "You push through the sensitivety of your still swollen member and start pushing inside her again."
        pov "You're..."
        with vpunch
        pov "so..."
        with vpunch
        pov "wet!"
        with vpunch
        bs "Yes, oh yes!"
        with vpunch
        bs "Right... gah... there!"
        with vpunch
        bs "I'm cumming!"
    else:
        bs "Please fuck me! I'm close too..."
        povi "I just came, but I'm not going to stop now."
        "You push through the sensitivety of your still swollen member and start fucking her hard."
        pov "You're..."
        with vpunch
        pov "so fucking..."
        with vpunch
        pov "wet!"
        with vpunch
        bs "Yes, oh fuck!"
        with vpunch
        bs "Right... gah... there!"
        with vpunch
        bs "I'm cumming!"
    scene edited parentsroom 6pm 019
    with vpunch
    if mccassandra6pmlove == True:
        bs "FUU...HNNG!"
        "You feel her convulse and squeeze your cock as she climaxes."
        "You keep yourself pressed deep inside her, pressing your hips firmly against hers."
        bs "Huhhh... hah... oh..."
        "She lets out sweet little moans as her orgasm slowly subsides."
    else:
        bs "FUU...HNNG!"
        "You feel her convulse and squeeze your cock as she climaxes."
        "You keep yourself pressed deep inside her, pressing your hips firmly against hers."
        bs "Huhhh... hah... oh..."
        "She lets out little moans as her orgasm slowly subsides."
    if nicolereddresswear == True:
        scene main 6pm 6pm dining roomncc1
    elif nicolebabydollwear == True:
        scene main 6pm 6pm dining roomncc2
    elif nicolesweaterpantswear == True:
        scene main 6pm 6pm dining roomncl1
    elif nicolerobewear == True:
        scene main 6pm 6pm dining roomncl2
    else:
        scene main 6pm 6pm dining room
    dad "Did you hear something just now, sounded like moaning?"
    mom "I think I heard something too."
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
    if inc == True:
        mom "[ls] will you go and get your brother and sister? They're late for dinner again."
    else:
        mom "[ls] will you go and get [pov] and [bs]? They're late for dinner again."
    scene diningroom 6pm 008
    ls "Sure mom, I'll go get them."
    scene edited parentsroom 6pm 020repeat
    if mccassandra6pmlove == True:
        "[ls]'s presence goes unnoticed as you two continue to enjoy your post-coital bliss."
        bs "Hnnn... I just want to stay like this forever."
        pov "I could live with that."
        bs "<giggle>"
        ls "<whisper> Thought I would find you there here again."
        scene black
        "She runs off to explain that you two are going to need a little bit longer to \"get ready\"."
        "You two finally pull yourselves together and leave the room."
    else:
        "[ls]'s presence goes unnoticed as you two continue to enjoy the feeling after a great fuck."
        bs "Hnnn... I want that dick inside me forever."
        pov "I could live with that."
        bs "<giggle>"
        ls "<whisper> I'll just leave you two alone... for now."
        scene black
        "She runs off to explain that you two are going to need a little bit longer to \"get ready\"."
        "You two finally pull yourselves together and leave the room."
    $ mccassandra6pmlove = False
    $ dtime += 1
    jump parentsroom
