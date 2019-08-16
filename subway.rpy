#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. Time Location - Featured - Scenes
#----- End List -----

label subwaydeliever:
    hide screen townl
    scene town subway 3pm 002
    povi "This must be person I need to deliver the package to."
    pov "Hey!"
    scene town subway 3pm 003
    "Receiver" "What do you want?"
    povi "Oh, it's a girl! I wonder if she's a member of the gang too?"
    pov "I got a package to deliver."
    "Girl" "You got this from Davide?"
    pov "Yes."
    scene town subway 3pm 005
    "Girl" "Give it to me."
    povi "Wow, she must be in a bad mood."
    pov "Here!"
    $ package -= 1
    scene town subway 3pm 006
    "Girl" "Yes, this is it."
    pov "Do you know what's in it?"
    "Girl" "It's none of your business!"
    scene town subway 3pm 007
    "Girl" "Here take this!"
    $ money += 75
    "You got 75$."
    pov "Nice, thanks."
    scene town subway 3pm 004
    "Girl" "You can go now!"
    povi "Wow, really a bad mood."
    pov "Ok, ok."
    $ jobdone += 1
    $ dtime += 1
    jump subway

#----- Nicole NTR Event ----- Done
label nicoleweekendntr:
    hide screen locations
    scene black
    "You make your way to the subway station."
    scene weekend 10pm 000n
    povi "There she is."
    povi "Wait... Isn't that the guy that chased us on our date!"
    povi "It seems like they're discussing something important. I wonder what it's about."
    "You go a little closer."
    scene weekend 10pm 001n
    "Peter" "You broke the deal, bitch! On top of that you made me chase you all over town."
    if ndate21ntrsex == True:
        mom "You fucked me on while I was on a date. You said my debt was paid!"
        "Peter" "That was before you made this so difficult."
        povi "What debt? They had a deal? So she lied at me all the time."
    else:
        mom "You tried to fuck me on while I was on a date. You said my debt was paid before!"
        "Peter" "That was before you made this so difficult."
        povi "What debt? And they had a deal? Did she lie to me before?"
    mom "It wasn't my fault!"
    "Peter" "You're a whore and a liar. I'm sick of the lies, but I can still use the whore..."
    scene weekend 10pm 002n
    mom "Huh? Who's that?"
    "Peter" "Someone that is going to help me to punish you for your mistakes."
    mom "You can't be serious."
    "Peter" "Oh yes, I am."
    scene weekend 10pm 003n
    "Peter" "Come with us."
    mom "No, please! Can't we work something else out?"
    povi "Damn what they're up to. Are they going to kill her?"
    "Other guy" "I'm sure the slut will enjoy her punishment more then she should!"
    "Peter" "I hope not!"
    scene weekend 10pm 004n
    povi "I have to do something. I need to follow them."
    povi "But what did the guy mean with \"enjoy her punishment\"?"
    scene weekend 10pm 005n
    povi "Oh... Are going to rape her?"
    scene weekend 10pm 006n
    povi "There they are. I don't think they can see me yet."
    "Peter" "You know exactly what happens when you need to be punished for failing to make good on your debts."
    "Peter" "I have a sneaking suspicion that you do this on purpose."
    mom "No..."
    "Other guy" "Yeah, that sure sounded convincing... haha."
    povi "No, She isn't some slut begging for it, is she?"
    scene weekend 10pm 007n
    "Other guy" "Get on the floor bitch! It's time for your punishment."
    "Peter" "You might enjoy this, but I'm going to be so rough you're going to suffer before we're done, slut!"
    povi "That doesn't sound good at all."
    povi "I still can't believe she lied to me after all that we've been going through recently."
    call screen nicoleweekendntrinter

screen nicoleweekendntrinter():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrinter'), Jump('nicoleweekendntrstop')) hovered tt.Action ("Interfere") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrinter'), Jump('nicoleweekenddarkpath')) hovered tt.Action ("Follow Darker Paths") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicoleweekendntrstop:
    povi "I'm going to help her. It doesn't matter what she may or may not have done."
    povi "I don't think I can take both of these guys, but it's dark in here so maybe I can trick them into leaving."
    pov "FREEZE! POLICE! I think I found them, they're over here fellas!"
    scene weekend 10pm 008bn
    "Other guy" "Damn, the cops!"
    "Peter" "Not now! Fuck! Run!"
    "They tear off around the other corner trying to get away."
    scene weekend 10pm 009bn
    mom "[pov!]"
    if inc == True:
        pov "Hey mom."
    else:
        pov "Hey [mother]."
    mom "What are you doing here? And where's the police?"
    scene weekend 10pm 010bn
    mom "Wait, what that you? Wow, you saved me."
    pov "Well yeah, I'm not going to let anyone hurt you."
    pov "Besides, I think you sent a message to me accidentally, so I came to check on you."
    mom "Oh that's so sweet [pov]."
    pov "But I still don't understand why you were talking to them in the first place."
    pov "And what is this debt and deal they were talking about?"
    scene weekend 10pm 011bn
    mom "Come here, let me hug you!"
    if ndate21 == True:
        if ndate21ntrsex == True:
            mom "Well you know what Peter did to me while we were on our date..."
            mom "Well after our first date, I found out that Davide whored me out to Peter as part of a some debt he owe them."
        else:
            mom "I told you before that Peter was the leader of an opposing gang, right?"
            mom "Well after our first date, I found out that Davide tried to whore me out to Peter as part of a some debt he owe them."
        pov "That motherfucker!"
        if vivianfirstmeet == True:
            mom "So I talked to Vivian"
        else:
            mom "So I talked to the bartender from where I work."
        mom "She has connections and spoke to Peter. He gave me a deal."
        if ndate21ntrsex == True:
            mom "He said since he fucked me already, the debt between Davide and him was paid. But he also said I owed him for running from him."
            mom "And then he said I had to pay him $100 dollars every week to keep him from doing that to me again."
        else:
            mom "If I paid him $200 dollars every weekend then the debt would be cleared and I would be safe for the next week."
        pov "That's ridiculous! Davide owes that asshole, not you!"
        mom "It doesn't matter. Davide used me as payment, so in Peter's eyes, the debt is mine..."
        mom "Well I paid him this week, but now he's claiming I never paid him. He tracked me down somehow and that's probably when you first say us talking."
        mom "I'm just so glad you came when you did. I love you, sweetie!"
    else:
        povi "She still won't tell me the truth, but at least she's safe."
        mom "I'm so glad I have you!"
    if susanfirstmeet == True:
        susan "There you are [mother]!"
    else:
        "Woman" "There you are [mother]!"
    scene weekend 10pm 012bn
    if susanfirstmeet == False:
        $ susanname = renpy.input(_("Her name is...")) or _("Susan")
        $ susanname = susanname.strip()
        if susanname == "":
            $ susanname = "Susan"
    mom "[susan], you're here too?"
    susan "I waited for you but when you didn't show up, I came here to check on you."
    mom "I'm sorry [susan]. Something real bad almost happened, but [pov] rescued me!"
    scene weekend 10pm 013bn
    if susanfirstmeet == True:
        susan "Oh I know him."
        if inc == True:
            susan "It's your son."
        else:
            susan "It's the young man that lives with you."
    else:
        susan "Who is this young man?"
        if inc == True:
            mom "He's my son [pov]."
        else:
            mom "He's living with us, it's [pov]."
    susan "I wish such a young, strong boy would rescue an old lady like me!"
    mom "[susan]! Are you drunk! Stop flirting with him."
    mom "You can't be serious!"
    susan "Why not, if he likes to rescue to older women then..."
    pov "Ahem... Ladies..."
    scene weekend 10pm 014bn
    mom "Sorry [pov]. I think I better take her home. She's clearly drunk."
    susan "No I'm not. I just admire courage in a young man is all."
    mom "I'm trying to pick up some extra shifts at the club this weekend, so sadly you might not see much of me until Monday."
    mom "But thank you so much [pov]. And promise, I won't forget your help today."
    if inc == True:
        pov "Bye mom."
    else:
        pov "Bye [mother]."
    pov "Bye [susan]."
    susan "Bye my strapping young lad!"
    $ susanfirstmeet = True
    scene black
    "You go back home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

#----- Custom -----
label nicoleweekenddarkpath:
    call screen checkdarkerpaths_nicole
    jump nicoleweekendntrsex

label nicoleweekendntrsex:
    if nicole_voyeur == True:
        povi "No, I won't be helping her this time. If she's going to lie to me like that then she can endure her punishment on her own."
    elif nicole_ntr == True:
        povi "I don't think there is anything I can do to help her. There are two of them!"
    elif nicole_revenge == True:
        povi "There are two of them and if I try to help them and fail, there is no telling what they will do to her."
        povi "I better watch them for now and look for an opportunity to help her."
    else:
        povi "No, I won't be helping her this time. If she's going to lie to me like that then she can endure her punishment on her own."
    scene weekend 10pm 008n
    "Other guy" "Come here, slut. Time to open that dick loving mouth of yours!"
    mom "HNNG... <choke>"
    scene weekend 10pm 009n
    "Peter" "<slap> Slut, you needs a good spanking."
    mom "Hnn... hnng..."
    if nicole_voyeur == True:
        povi "Damn, they're being rough with her already, maybe it's really too much."
    elif nicole_ntr == True:
        povi "Damn it. They're starting already. I don't want to see this, but I can't just walk away either."
    elif nicole_revenge == True:
        povi "God damn it! They are treating her so roughly. I need to find a way to stop this before she really get's hurt!"
    else:
        povi "Damn, they're being rough with her already. The harder the better I say."
    call screen nicoleweekendntrlikechoose

#----- Edited -----
screen nicoleweekendntrlikechoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('nicoleweekendntrlikechoose'), Jump('nicoleweekendntrlike')) hovered tt.Action ("Long Path") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('nicoleweekendntrlikechoose'), Jump('nicoleweekendntrdislike')) hovered tt.Action ("Short Path") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Short Path ----- Done
label nicoleweekendntrdislike:
    if nicole_voyeur == True:
        povi "They're definitely too rough. It's like they raping her."
        povi "Maybe I should have done something before, but still pretty damn hot."
    elif nicole_ntr == True:
        povi "They're doing whatever they want with her."
        povi "I hate these guys! She's mine!"
    elif nicole_revenge == True:
        povi "They are raping her! What if they don't stop there?"
        povi "I should have done something earlier. I'm such an idiot!"
    else:
        povi "They're raping her."
        povi "Maybe I should have done something before, but still pretty damn hot."
    scene weekend 10pm 010n
    "Peter" "Look at this slut. She's getting so fucking wet."
    mom "<choke> Hnng..."
    "Other guy" "Her choking on my dick was so hot, I'm about to cum!"
    mom "Hah... hah..."
    "Other guys" "Take my spunk all over your lovely face, slut!"
    "Peter" "I bet she just couldn't wait for that!"
    if nicole_ntr == True or nicole_revenge == True:
        povi "Those damn assholes!"
    scene weekend 10pm 011n
    "Hobo" "Hey guys. I see what you're doing here and I wonder I can join in on the fun?"
    povi "What? Who's that guy? I think I've seen him before though."
    "Other guy" "Sure. I'm all done here, the slut did a real good job."
    "Hobo" "Haha, I saw that, but I think I can teach her how to be even better."
    "Peter" "Then go on and take his place."
    if nicole_revenge == True:
        mom "Please, just stop... I don't want this!"
        "Hobo" "You're not a very nice slut! You should be waiting for the next dick you can please!"
        povi "Like fucking hell she should. That's it Hobo, you just made the list!"
    if nicole_sadist == True:
        mom "Please, just stop... I don't want this!"
        "Hobo" "You're not a very nice slut! You should be waiting for the next dick you can please!"
        povi "He's right about that. She should be."
    else:
        mom "You can't be serious..."
        "Hobo" "So you're a real slut? Waiting for the next dick with sperm on your face!"
        if nicole_voyeur == True:
            povi "Hah, they're serious."
        else:
            povi "They can't be serious."
    scene weekend 10pm 012n
    "Hobo" "I'm going to teach you how to properly deepthroat a cock."
    mom "<choke> HNNG...!"
    "Peter" "Good. She needs to be punished like the disobedient slut she is!"
    if nicole_voyeur == True or nicole_sadist == True:
        povi "Damn, he's fucking her mouth! But that gaves me an idea."
    else:
        povi "Damn, he's fucking her mouth!"
    jump nicoleweekendntrsusan

label nicoleweekendntrsusan:
    if susanfirstmeet == True:
        susan "[mother], you there?"
    else:
        "Woman" "[mother], you there?"
    "Peter" "God damn it, someone is coming. It's your lucky day, slut!"
    "Hobo" "What a pity. I'll have to teach you another time!"
    "Peter" "Let's get out of here!"
    if nicole_voyeur == True:
        povi "Damn! Way to ruin the fun! I think she was starting to really get into it."
    elif nicole_ntr == True:
        povi "Good, she's getting help."
    elif nicole_revenge == True:
        povi "Oh thank God! she's getting some help."
    else:
        povi "Damn! Way to ruin the fun! I think she was starting to really get into it."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    if nicole_voyeur == True:
        povi "[mother] was finally getting some really action, like the slut wanted and you interupted!"
    elif nicole_ntr == True:
        povi "[mother] got abused and I decided to watch. I feel so helpless."
    elif nicole_revenge == True:
        povi "[mother] got raped and I wasn't able to stop it! I'm going to end Peter!"
    else:
        povi "[mother] got raped and I was enjoying every minute of it!"
    scene weekend 10pm 022n
    if susanfirstmeet == True:
        susan "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        susan "Let me help you and then we'll search for your pants."
    else:
        "Woman" "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        "Woman" "Let me help you and then we'll search for your pants."
    scene weekend 10pm 023n
    if susanfirstmeet == True:
        susan "Who were they?"
        mom "Just some assholes. I'll tell you later."
        susan "Calm down, you're safe now."
    else:
        "Woman" "Who were they?"
        mom "Just some assholes. I'll tell you later."
        "Woman" "Calm down, you're safe now."
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

#----- Long Path ----- Done
label nicoleweekendntrlike:
    if nicole_voyeur == True:
        povi "Ha, it's the right punishment for her."
    elif nicole_ntr == True:
        povi "I wish that was me."
    elif nicole_revenge == True:
        povi "There are two of them and if I try to help them and fail, there is no telling what they will do to her."
    else:
        povi "Ha, it's the right punishment for her."
    scene weekend 10pm 010n
    "Peter" "Look at this slut. She's getting so fucking wet."
    mom "<choke> Hnng..."
    "Other guy" "Her choking on my dick was so hot, I'm about to cum!"
    mom "Hah... hah..."
    "Other guys" "Take my spunk all over your lovely face, slut!"
    "Peter" "I bet she just couldn't wait for that!"
    if nicole_voyeur == True:
        povi "Wait? She's getting wet. So she's really a slut."
    elif nicole_ntr == True:
        povi "Wait? She's getting wet. So she's really a slut..."
    elif nicole_revenge == True:
        povi "Right, Peter. I'm sure she's so wet for you... Fucking idiot."
    else:
        povi "Wait? She's getting wet? So she's really a slut."
    scene weekend 10pm 011n
    "Hobo" "Hey guys. I see what you're doing here and I wonder I can join in on the fun?"
    povi "What? Who's that guy? I think I've seen him before though."
    "Other guy" "Sure. I'm all done here, the slut did a real good job."
    "Hobo" "Haha, I saw that, but I think I can teach her how to be even better."
    "Peter" "Then go on and take his place."
    if nicole_revenge == True:
        mom "Please, just stop... I don't want this!"
        "Hobo" "You're not a very nice slut! You should be waiting for the next dick you can please!"
        povi "Like fucking hell she should. That's it Hobo, you just made the list!"
    elif nicole_sadist == True:
        mom "Please, just stop... I don't want this!"
        "Hobo" "You're not a very nice slut! You should be waiting for the next dick you can please!"
        povi "He's right about that. She should be."
    else:
        mom "You can't be serious..."
        "Hobo" "So you're a real slut? Waiting for the next dick with sperm on your face!"
        if nicole_voyeur == True:
            povi "Hah, they're serious."
        else:
            povi "They can't be serious."
    scene weekend 10pm 012n
    "Hobo" "I'm going to teach you how to properly deepthroat a cock."
    mom "<choke> HNNG...!"
    "Peter" "Good. She needs to be punished like the disobedient slut she is!"
    if nicole_voyeur == True or nicole_sadist == True:
        povi "Damn, he's fucking her mouth! That gaves me an idea..."
    else:
        povi "Damn, he's fucking her mouth!"
    call screen nicoleweekendntrjoinchoose

screen nicoleweekendntrjoinchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('nicoleweekendntrjoinchoose'), Jump('nicoleweekendntrjoin')) hovered tt.Action ("Join too [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrjoinchoose'), Jump('nicoleweekendntrnojoin')) hovered tt.Action ("Forget the idea") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicoleweekendntrnojoin:
    if nicole_voyeur == True:
        povi "No, not this time. I think I'll just watch."
    elif nicole_ntr == True:
        povi "No, that was a bad idea, I'll just watch."
    elif nicole_revenge == True:
        povi "I can't do that to her. She's already been through so much."
    else:
        povi "No, not this time. I think I'll just watch and enjoy watching her get used like that."
    if susanfirstmeet == True:
        susan "[mother], you there?"
    else:
        "Woman" "[mother], you there?"
    "Peter" "God damn it, someone is coming. It's your lucky day, slut!"
    "Hobo" "What a pity. I'll have to teach you another time!"
    "Peter" "Let's get out of here!"
    if nicole_voyeur == True:
        povi "Damn! Way to ruin the fun! I think she was starting to really get into it."
    elif nicole_ntr == True:
        povi "Good, she's getting help."
    elif nicole_revenge == True:
        povi "Oh thank God! she's getting some help."
    else:
        povi "Damn! Way to ruin the fun! I think she was starting to really get into it."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    if nicole_voyeur == True:
        povi "[mother] was finally getting some really action, like the slut wanted and you interupted!"
    elif nicole_ntr == True:
        povi "[mother] got abused and I decided to watch. I feel so helpless."
    elif nicole_revenge == True:
        povi "[mother] got raped and I wasn't able to stop it! I'm going to end Peter!"
    else:
        povi "[mother] got raped and I was enjoying every minute of it!"
    scene weekend 10pm 022n
    if susanfirstmeet == True:
        susan "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        susan "Let me help you and then we'll search for your pants."
    else:
        "Woman" "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        susan "Let me help you and then we'll search for your pants."
    scene weekend 10pm 023n
    if susanfirstmeet == True:
        susan "Who were they?"
        mom "Just some assholes. I'll tell you later."
        susan "Calm down, you're safe now."
    else:
        "Woman" "Who were they?"
        mom "Just some assholes. I'll tell you later."
        "Woman" "Calm down, you're safe now."
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrjoin:
    $ momcorruption += 1
    $ nicoleweekendntrjoin = True
    if nicole_voyeur == True:
        povi "If that Hobo can join in, then I'm pretty sure I can get them to let me join too."
        povi "I'll try to disguise my voice so she doesn't recognize me. Then I can get back at her for lying to me."
    elif nicole_ntr == True:
        povi "If that Hobo can join in, then I'm pretty sure I can get them to let me join too."
        povi "I'll try to disguise my voice so she doesn't recognize me. I don't want her getting made at me."
    elif nicole_revenge == True:
        povi "Maybe when they let that Hobo join in, I can get them to let me join in too."
        povi "There is nothing I can do to help her from here if anything gets even worse for her."
        povi "I'll try to disguise my voice though. So she doesn't recognize me. Given what I'll need to do, it's probably for the best."
    else:
        povi "Maybe when they let that Hobo join in, I can get them to let me join in too."
        povi "I'll try to disguise my voice so she doesn't recognize me. Then I can get back at her for lying to me."
    scene weekend 10pm 013n
    mom "<choke> Urgh!"
    pov "<with a fake voice> Hey bro, can I have some fun too?"
    "Peter" "Damn, you have so many admirers today slut!"
    scene weekend 10pm 014n
    "Peter" "Everyone wants to use you. Like the cum-dumpster you are."
    "Peter" "Of course you can have your turn. I was about to leave anyway."
    "Peter" "You hear that slut? Maybe this will be your last dick today, haha. Maybe not."
    mom "Hnng... Urgh! Urgh!"
    "Hobo" "Good, hold it deep slut."
    pov "<with a fake voice> Thank you bro!"
    scene weekend 10pm 015n
    if nicole_voyeur == True:
        povi "Damn, he wasn't lying. She's already very wet. So maybe she is enjoying this abuse."
        povi "Then I don't think I need to feel bad about having my fun with her too."
        povi "But which hole should I use?"
    elif nicole_ntr == True:
        povi "Damn, he wasn't lying. She's already very wet. So maybe she is enjoying this abuse."
        povi "I can't believe she's such a whore. I'm going to enjoy this then!"
        povi "But which hole should I use?"
    elif nicole_revenge == True:
        povi "Damn, he wasn't lying. She is very wet. But that's to be expected with you have sex. Willingly or not."
        povi "It's a natural reaction, even when someone is being raped."
        povi "But of course these jackasses assume it's because their such amazing \"sex gods\" or some shit like that."
        povi "Dumb fuckers. But I need to actually join in or they will know I'm lying. I'm sorry [mother]..."
    else:
        povi "Damn, he wasn't lying. She is very wet. But that's to be expected with you have sex. Willingly or not."
        povi "It's a natural reaction, even when someone is being raped."
        povi "All the better for me! Now which hole should I use?"
    call screen nicoleweekendntrfuck

screen nicoleweekendntrfuck():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrfuck'), Jump('nicoleweekendntrfuckp')) hovered tt.Action ("Fuck her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrfuck'), Jump('nicoleweekendntrfucka')) hovered tt.Action ("Fuck her asshole") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicoleweekendntrfuckp:
    $ nicoleweekendntrpussy = True
    jump nicoleweekendntrfucka

label nicoleweekendntrfucka:
    if nicole_voyeur == True:
        if nicoleweekendntrpussy == True:
            povi "I'm going to fuck her pussy. With her legs closed like that, she'll be very tight."
        else:
            povi "I'm going to fuck her ass. With her legs closed like that, she'll be very tight."
        povi "I'm sure the slut will love it either way!"
    elif nicole_ntr == True:
        if nicoleweekendntrpussy == True:
            povi "I can't believe I'm doing this! I'm going to fuck her pussy."
        else:
            povi "I can't believe I'm doing this! I'm going to fuck her ass."
        povi "I'm sure the slut will love it either way!"
    elif nicole_revenge == True:
        if nicoleweekendntrpussy == True:
            if inc == True:
                povi "I'm sorry mom, I can't resist that pussy. In this position I know it's going to be tight."
            else:
                povi "I'm sorry [mother], I can't resist that pussy. In this position I know it's going to be tight."
        else:
            if inc == True:
                povi "I'm sorry mom, I can't resist that ass. In this position I know it's going to be tight."
            else:
                povi "I'm sorry [mother], I can't resist that ass. In this position I know it's going to be tight."
        povi "I need to look for an opportunity to get her out of here."
    else:
        if nicoleweekendntrpussy == True:
            povi "I'm going to fuck her pussy. With her legs closed like that, she'll be very tight."
        else:
            povi "I'm going to fuck her ass. With her legs closed like that, she'll be very tight."
    scene weekend 10pm 016n
    mom "<choke> Urgh! Urgh!"
    "Hobo" "Stop fighting, slut!"
    if nicole_voyeur == True:
        povi "She's having a hard time up there, but she'll feel better when she feels my dick inside her."
    elif nicole_ntr == True:
        povi "He's being so rough up there. I wonder what she's do if she know it was my dick entering her?"
    elif nicole_revenge == True:
        povi "That fucking hobo. I going to kick his ass. Hopefully she doesn't realize it's me fucking her back here."
    else:
        povi "She's having a hard time up there, but she'll feel better when she feels my dick inside her."
    scene weekend 10pm 017n
    if nicoleweekendntrpussy == True:
        "You enter her pussy."
        mom "Hnng... Urgh!"
        if nicole_voyeur == True:
            povi "Oh her wet pussy is clinging onto me. And it's so tight. This is going to be a good fuck!"
            "You fuck her pussy roughly."
            mom "Hnng... Hnn..."
            povi "This is so damn good, her fighting just makes me want to cum faster."
            "Hobo" "This slut is a good fuck, isn't she?"
            povi "Maybe I should go a step further to get the ultimate revenge. She's helpless and her mouth is busy, so she can't complain."
        elif nicole_ntr == True:
            povi "Oh wow! Her wet pussy is clinging onto me. And it's so tight. I finally get to be inside her!"
            "You fuck her pussy roughly."
            mom "Hnng... Hnn..."
            povi "This is so damn good, her fighting body will make me cum in no time."
            "Hobo" "This slut is a good fuck, isn't she?"
            povi "Maybe I should let her know it's me fucking her. She's helpless and her mouth is busy, so she can't complain."
        elif nicole_revenge == True:
            povi "Oh shit! Her wet pussy is clinging onto me. And it's so tight. There is no way I'm not going to enjoy this. I'm sorry."
            "You can't help yourself, after a few moments, you start thrusting harder and harder into her pussy."
            mom "Hnng... Hnn..."
            povi "This is so damn good, her fighting body will make me cum in no time."
            "Hobo" "This slut is a good fuck, isn't she?"
            povi "I think she's still scared. I mean who wouldn't be in this situation?"
            povi "Should I let her know it's me? I don't know if that would make her feel better or worse though."
        else:
            povi "Her wet pussy is clinging onto me and it's so tight. This is going to be a good fuck!"
            "You fuck her pussy roughly."
            mom "Hnng... Hnn..."
            povi "This is so damn good, her fighting just makes me want to cum faster."
            "Hobo" "This slut is a good fuck, isn't she?"
            povi "Maybe I should go a step further to get the ultimate revenge. She's helpless and her mouth is busy, so she can't complain."
    else:
        "You enter her asshole."
        mom "Hnng... Urgh!"
        if nicole_voyeur == True:
            povi "Oh her asshole is clinging on me. And it's so tight. This will be a good fuck!"
            "You fuck her ass roughly."
            mom "Hnng... Hnn..."
            povi "This is so damn good, her fighting just make me want to cum faster."
            "Hobo" "This slut is a good fuck, isn't she?"
            povi "Maybe I should go a step further to get the ultimate revenge. She's helpless and her mouth is busy, so she can't complain."
        elif nicole_ntr == True:
            povi "Oh her asshole is clinging on me. And it's so tight. This will be a good fuck!"
            "You fuck her ass roughly."
            mom "Hnng... Hnn..."
            povi "This is so damn good, her fighting body will make me cum in no time."
            "Hobo" "This slut is a good fuck, isn't she?"
            povi "Maybe I should let her know it's me fucking her. She's helpless and her mouth is busy, so she can't complain."
        elif nicole_revenge == True:
            povi "Oh her asshole is clinging on me. And it's so tight. This will be a good fuck!"
            "You can't help yourself, after a few moments, you start thrusting harder and harder into her ass."
            mom "Hnng... Hnn..."
            povi "This is so damn good, her fighting body will make me cum in no time."
            "Hobo" "This slut is a good fuck, isn't she?"
            povi "I think she's still scared. I mean who wouldn't be in this situation?"
            povi "Should I let her know it's me? I don't know if that would make her feel better or worse though."
        else:
            povi "Her asshole is clinging onto me and it's so tight. This is going to be a good fuck!"
            "You fuck her ass roughly."
            mom "Hnng... Hnn..."
            povi "This is so damn good, her fighting just makes me want to cum faster."
            "Hobo" "This slut is a good fuck, isn't she?"
            povi "Maybe I should go a step further to get the ultimate revenge. She's helpless and her mouth is busy, so she can't complain."
    jump nicoleweekendntrtell

label nicoleweekendntrtell:
    call screen nicoleweekendntrtellchoose

screen nicoleweekendntrtellchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('nicoleweekendntrtellchoose'), Jump('nicoleweekendntryesreveal')) hovered tt.Action ("Reveal yourself") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('nicoleweekendntrtellchoose'), Jump('nicoleweekendntrnoreveal')) hovered tt.Action ("Don't") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicoleweekendntrnoreveal:
    if nicole_voyeur == True:
        povi "No, I'll stay silent. I don't want her to know that I'm fucking her."
        scene weekend 10pm 018n
        mom "Hnng...? <choke> HNNG..!"
        "Hobo" "Oh, she's going crazy. You love my dick that much?"
        if nicoleweekendntrpussy == True:
            povi "Damn, her pussy is so greedy. I'm about to cum!"
        else:
            povi "Damn, her asshole is so greedy. I'm about to cum."
    elif nicole_ntr == True:
        pov povi "No, I'll stay silent. I don't want her to know that I'm fucking her."
        scene weekend 10pm 018n
        mom "Hnng...? <choke> HNNG..!"
        "Hobo" "Oh, she's going crazy. You love my dick that much?"
        if nicoleweekendntrpussy == True:
            povi "I can't believe how tight her pussy is. I'm about to cum!"
        else:
            povi "I can't believe how tight her ass is. I'm about to cum."
    elif nicole_revenge == True:
        pov povi "No, I'll stay silent. I don't want her to know that I'm fucking her."
        scene weekend 10pm 018n
        mom "Hnng...? <choke> HNNG..!"
        "Hobo" "Oh, she's going crazy. You love my dick that much?"
        if nicoleweekendntrpussy == True:
            povi "I can't help it, her pussy is squeezing me so tight. I'm about to cum!"
        else:
            povi "I can't help it, her ass is squeezing me so tight. I'm about to cum."
    else:
        povi "No, I'll stay silent. It's better that she doesn't know it's me fucking her."
        scene weekend 10pm 018n
        mom "Hnng...? <choke> HNNG..!"
        "Hobo" "Oh, she's going crazy. You love my dick that much?"
        if nicoleweekendntrpussy == True:
            povi "Damn, her pussy is so greedy. I'm about to cum!"
        else:
            povi "Damn, her asshole is so greedy. I'm about to cum."
    call screen nicoleweekendntrcumnorevealchoose

screen nicoleweekendntrcumnorevealchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if nicoleweekendntrpussy == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrcumnorevealchoose'), Jump('nicoleweekendntrcumnorevealinsidep')) hovered tt.Action ("Cum inside her pussy") focus_mask True
        if nicoleweekendntrpussy == False:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrcumnorevealchoose'), Jump('nicoleweekendntrcumnorevealinsidea')) hovered tt.Action ("Cum inside her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrcumnorevealchoose'), Jump('nicoleweekendntrcumnorevealoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicoleweekendntrcumnorevealinsidep:
    if nicole_voyeur == True:
        if inc == True:
            povi "I'll cum inside your wet pussy, mom!"
        else:
            povi "I'll cum inside your wet pussy, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her pussy."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        povi "She loved it."
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    elif nicole_ntr == True:
        if inc == True:
            povi "I'm cumming inside your wet pussy, mom!"
        else:
            povi "I'm cumming inside your wet pussy, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her pussy."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "Wow, I came so much!"
        mom "Hnn... hnn..."
        povi "She deserved that."
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "I'm surprised a slut like her can't keep up, she's still choking on it."
    elif nicole_revenge == True:
        if inc == True:
            povi "I'm going to cum inside your wet pussy, mom!"
        else:
            povi "I'm going to cum inside your wet pussy, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her pussy."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "I can't believe how much I came!"
        mom "Hnn... hnn..."
        povi "It felt like her pussy was swallowing every drop."
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Damn it. She practically choking on cum, fucking bastard."
    else:
        if inc == True:
            povi "I'll cum inside your wet pussy, mom!"
        else:
            povi "I'll cum inside your wet pussy, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her pussy."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        povi "She loved it. Or she didn't. Doesn't matter. Either way I did!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    if nicole_voyeur == True:
        povi "Let's run."
    elif nicole_ntr == True or nicole_sadist == True:
        povi "I'm out of here."
    else:
        povi "I need to run."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    if nicole_voyeur == True or nicole_sadist == True:
        povi "I and other guys happened, haha."
    elif nicole_voyeur == True:
        povi "I took her for myself for once!"
    else:
        povi "I failed to protect her. I'm sorry."
    scene weekend 10pm 022n
    if susanfirstmeet == True:
        susan "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        susan "Let me help you and then we search your pants."
    else:
        "Woman" "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        "Woman" "Let me help you and then we search your pants."
    scene weekend 10pm 023n
    if susanfirstmeet == True:
        susan "Who were they?"
        mom "Just some assholes. I'll tell you later."
        susan "Calm down, you're save now."
    else:
        "Woman" "Who were they?"
        mom "Just some assholes. I'll tell you later."
        "Woman" "Calm down, you're save now."
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrcumnorevealinsidea:
    if nicole_voyeur == True:
        if inc == True:
            povi "I'll cum inside your asshole, mom!"
        else:
            povi "I'll cum inside your asshole, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her asshole."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        povi "She loved it."
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    elif nicole_ntr == True:
        if inc == True:
            povi "I'm cumming inside your asshole, mom!"
        else:
            povi "I'm cumming inside your asshole, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her asshole."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "Wow, I came so much!"
        mom "Hnn... hnn..."
        povi "She deserved that."
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "I'm surprised a slut like her can't keep up, she's still choking on it."
    elif nicole_revenge == True:
        if inc == True:
            povi "I'm going to cum inside your asshole, mom!"
        else:
            povi "I'm going to cum inside your asshole, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her asshole."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "I can't believe how much I came!"
        mom "Hnn... hnn..."
        povi "It felt like her asshole was swallowing every drop."
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Damn it. She practically choking on cum, fucking bastard."
    else:
        if inc == True:
            povi "I'll cum inside your asshole, mom!"
        else:
            povi "I'll cum inside your asshole, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her asshole."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        povi "She loved it. Or she didn't. Doesn't matter. Either way I did!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    if nicole_voyeur == True:
        povi "Let's run."
    elif nicole_ntr == True or nicole_sadist == True:
        povi "I'm out of here."
    else:
        povi "I need to run."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    if nicole_voyeur == True or nicole_sadist == True:
        povi "I and other guys happened, haha."
    elif nicole_voyeur == True:
        povi "I took her for myself for once!"
    else:
        povi "I failed to protect her. I'm sorry."
    scene weekend 10pm 022n
    if susanfirstmeet == True:
        susan "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        susan "Let me help you and then we search your pants."
    else:
        "Woman" "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        "Woman" "Let me help you and then we search your pants."
    scene weekend 10pm 023n
    if susanfirstmeet == True:
        susan "Who were they?"
        mom "Just some assholes. I'll tell you later."
        susan "Calm down, you're save now."
    else:
        "Woman" "Who were they?"
        mom "Just some assholes. I'll tell you later."
        "Woman" "Calm down, you're save now."
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrcumnorevealoutside:
    if nicole_voyeur == True:
        if inc == True:
            povi "I'll cum on your ass, mom!"
        else:
            povi "I'll cum on your ass, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm on her ass."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        povi "She loved it."
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    elif nicole_ntr == True:
        if inc == True:
            povi "I'm cumming on your ass, mom!"
        else:
            povi "I'm cumming on your ass, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm on her ass."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "Wow, I came so much!"
        mom "Hnn... hnn..."
        povi "She deserved that."
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "I'm surprised a slut like her can't keep up, she's still choking on it."
    elif nicole_revenge == True:
        if inc == True:
            povi "I'm going to cum on your ass, mom!"
        else:
            povi "I'm going to cum on your ass, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm on her ass."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "I can't believe how much I came!"
        mom "Hnn... hnn..."
        povi "Her ass looks great covered with my cum. I'm just sorry it was under these circumstances."
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Damn it. She practically choking on cum, fucking bastard."
    else:
        if inc == True:
            povi "I'll cum on your ass, mom!"
        else:
            povi "I'll cum on your ass, [mother]!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm on her ass."
        povi "Hnng! Yes!"
        scene weekend 10pm 019nip
        povi "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        povi "She loved it. Or she didn't. Doesn't matter. Either way I did!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    if nicole_voyeur == True:
        povi "Let's run."
    elif nicole_ntr == True or nicole_sadist == True:
        povi "I'm out of here."
    else:
        povi "I need to run."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    if nicole_voyeur == True or nicole_sadist == True:
        povi "I and other guys happened, haha."
    elif nicole_voyeur == True:
        povi "I took her for myself for once!"
    else:
        povi "I failed to protect her. I'm sorry."
    scene weekend 10pm 022n
    if susanfirstmeet == True:
        susan "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        susan "Let me help you and then we search your pants."
    else:
        "Woman" "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        "Woman" "Let me help you and then we search your pants."
    scene weekend 10pm 023n
    if susanfirstmeet == True:
        susan "Who were they?"
        mom "Just some assholes. I'll tell you later."
        susan "Calm down, you're save now."
    else:
        "Woman" "Who were they?"
        mom "Just some assholes. I'll tell you later."
        "Woman" "Calm down, you're save now."
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntryesreveal:
    if nicole_voyeur == True:
        povi "I'll reveal myself and watch her go crazy."
        pov "Yes, I know this slut. She's a really good fuck!"
    elif nicole_ntr == True:
        povi "I'll reveal myself so that she know I am fucking her!"
        pov "Yes, I know this whore. She's really like to get around!"
    elif nicole_revenge == True:
        povi "I'll say something so she knows it's me, hopefully it's some measure of comfort..."
        pov "She's amazing. She's a really good fuck!"
        povi "Sorry [mother], I don't want him getting suspicious and doing something worse to you."
    else:
        povi "I'll reveal myself and watch her go crazy."
        pov "I know this slut. She's a really good fuck!"
    $ nicoleweekendntrreveal = True
    scene weekend 10pm 018n
    mom "Hnng...? <choke> HNNG..!"
    if nicole_voyeur == True:
        "Hobo" "Oh, she's going crazy. Seems like she isn't happy that you are doing her?"
        pov "Haha, probably not. But what can she do? Her mouth is busy, haha."
        "Hobo" "Haha, you're damn right."
        if nicoleweekendntrpussy == True:
            pov "Damn, her pussy is so greedy. I'm about to cum!"
        else:
            pov "Damn, her asshole is so greedy. I'm about to cum."
    elif nicole_ntr == True:
        "Hobo" "Oh, she's going crazy. So she isn't happy that you do her?"
        pov "I can't figure out why that is, unless she lied about her feelings for me!"
        "Hobo" "Haha, bitches, am I right?!"
        if nicoleweekendntrpussy == True:
            pov "Damn, her pussy is so fucking tight. I'm about to cum!"
        else:
            pov "Damn, her asshole is so fucking tight. I'm about to cum!"
    elif nicole_revenge == True:
        povi "It might just be my imagination, but it feels like she's pushing her ass back to meet my thrusts now..."
        "Hobo" "Oh wow, she's going crazy. Maybe she's happy to know it you fucking her?"
        pov "Haha, I hope so. She's definitely in good hands!"
        "You give her ass a reassuring squeeze, hoping she'll understand what you're trying to say."
        "But given the extreme situation, you start to doubt it."
        povi "It's the best I could do given the circumstances..."
        "Hobo" "Haha, you're damn right."
        if nicoleweekendntrpussy == True:
            povi "Damn, her pussy is just so tight and wet."
            pov "I'm about to cum!"
        else:
            povi "Damn, her asshole is just so tight."
            pov "I'm about to cum."
    else:
        "Hobo" "Oh, she's going crazy. Seems like she isn't happy that you are doing her!"
        pov "Haha, probably not. But what can she do? Her mouth is busy, haha."
        "Hobo" "Haha, you're damn right."
        if nicoleweekendntrpussy == True:
            pov "Damn, her pussy is so greedy. I'm about to cum!"
        else:
            pov "Damn, her asshole is so greedy. I'm about to cum."
    call screen nicoleweekendntrcumrevealchoose

screen nicoleweekendntrcumrevealchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if nicoleweekendntrpussy == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrcumrevealchoose'), Jump('nicoleweekendntrcumrevealinsidep')) hovered tt.Action ("Cum inside her pussy") focus_mask True
        if nicoleweekendntrpussy == False:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrcumrevealchoose'), Jump('nicoleweekendntrcumrevealinsidea')) hovered tt.Action ("Cum inside her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('nicoleweekendntrcumrevealchoose'), Jump('nicoleweekendntrcumrevealoutside')) hovered tt.Action ("Cum outside") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label nicoleweekendntrcumrevealinsidep:
    if nicole_voyeur == True:
        pov "I'll cum inside your wet pussy, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her pussy."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        pov "You loved it, didn't you slut!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    elif nicole_ntr == True:
        pov "I'm cumming inside your wet pussy, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her pussy."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "Wow, I came so much!"
        mom "Hnn... hnn..."
        pov "You deserved that, didn't you slut!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "I'm surprised a slut like her can't keep up, she's still choking on it."
    elif nicole_revenge == True:
        pov "I'm going to cum inside your wet pussy, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm in her pussy."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "I can't believe how much I came!"
        mom "Hnn... hnn..."
        pov "It feels like you pussy is swallowing every drop!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Damn it. She practically choking on cum, fucking bastard."
    else:
        pov "I'll cum inside your wet pussy, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm into her pussy."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        pov "You loved it, didn't you slut!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    if nicole_voyeur == True:
        pov "Let's run."
    elif nicole_ntr == True or nicole_sadist == True:
        pov "I'm out of here."
    else:
        povi "I need to run."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    if nicole_voyeur == True or nicole_sadist == True:
        povi "I and other guys happened, haha."
    elif nicole_ntr == True:
        povi "I took her for myself for once!"
    else:
        povi "I failed to protect her. I'm sorry."
    scene weekend 10pm 022n
    if susanfirstmeet == True:
        susan "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        susan "Let me help you and then we search your pants."
    else:
        "Woman" "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        "Woman" "Let me help you and then we search your pants."
    scene weekend 10pm 023n
    if susanfirstmeet == True:
        susan "Who were they?"
        mom "Just some assholes. I'll tell you later."
        susan "Calm down, you're save now."
    else:
        "Woman" "Who were they?"
        mom "Just some assholes. I'll tell you later."
        "Woman" "Calm down, you're save now."
    if nicoleweekendntrreveal == True:
        if nicole_voyeur == True:
            mom "I can't believe he did this to me."
        elif nicole_ntr == True or nicole_sadist == True:
            mom "I can't believe he would do this to me."
        else:
            mom "Why... did he do this?"
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrcumrevealinsidea:
    if nicole_voyeur == True:
        pov "I'll cum inside your asshole, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm inside her asshole."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        pov "You loved it, didn't you slut!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    elif nicole_ntr == True:
        pov "I'm cumming inside your asshole, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm inside her asshole."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "Wow, I came so much!"
        mom "Hnn... hnn..."
        pov "You deserved that, didn't you slut!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "I'm surprised a slut like her can't keep up, she's still choking on it."
    elif nicole_revenge == True:
        pov "I'm going to cum inside your asshole, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm inside her asshole."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "I can't believe how much I came!"
        mom "Hnn... hnn..."
        pov "It feels like you ass is swallowing every drop!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Damn it. She practically choking on cum, fucking bastard."
    else:
        pov "I'll cum inside your asshole, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm inside her asshole."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        pov "You loved it, didn't you slut!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    if nicole_voyeur == True:
        pov "Let's run."
    elif nicole_ntr == True or nicole_sadist == True:
        pov "I'm out of here."
    else:
        povi "I need to run."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    if nicole_voyeur == True or nicole_sadist == True:
        povi "I and other guys happened, haha."
    elif nicole_ntr == True:
        povi "I took her for myself for once!"
    else:
        povi "I failed to protect her. I'm sorry."
    scene weekend 10pm 022n
    if susanfirstmeet == True:
        susan "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        susan "Let me help you and then we search your pants."
    else:
        "Woman" "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        "Woman" "Let me help you and then we search your pants."
    scene weekend 10pm 023n
    if susanfirstmeet == True:
        susan "Who were they?"
        mom "Just some assholes. I'll tell you later."
        susan "Calm down, you're save now."
    else:
        "Woman" "Who were they?"
        mom "Just some assholes. I'll tell you later."
        "Woman" "Calm down, you're save now."
    if nicoleweekendntrreveal == True:
        if nicole_voyeur == True:
            mom "I can't believe he did this to me."
        elif nicole_ntr == True or nicole_sadist == True:
            mom "I can't believe he would do this to me."
        else:
            mom "Why... did he do this?"
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrcumrevealoutside:
    if nicole_voyeur == True:
        pov "I'll cum on your ass, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm on her ass."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        pov "You loved it, didn't you slut!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    elif nicole_ntr == True:
        pov "I'm cumming on your ass, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm on her ass."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "Wow, I came so much!"
        mom "Hnn... hnn..."
        pov "You deserved that, didn't you slut!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "I'm surprised a slut like her can't keep up, she's still choking on it."
    elif nicole_revenge == True:
        pov "I'm going to cum on your ass, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm on her ass."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "I can't believe how much I came!"
        mom "Hnn... hnn..."
        pov "Your ass looks great covered with my cum!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Damn it. She practically choking on cum, fucking bastard."
    else:
        pov "I'll cum on your ass, slut!"
        mom "HNNG! HMM!"
        "Hobo" "Oh this wild slut will make me cum too."
        "You release your sperm on her ass."
        pov "Hnng! Yes!"
        scene weekend 10pm 019nip
        pov "Oh yes, I came so much!"
        mom "Hnn... hnn..."
        pov "You loved it, didn't you slut!"
        scene weekend 10pm 020n
        mom "<spit> Urgh! Hah..."
        "Hobo" "You're supposed to swallow it! Bad Slut!"
        povi "Ha, he came so much, she's still choking on it."
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    if nicole_voyeur == True:
        pov "Let's run."
    elif nicole_ntr == True or nicole_sadist == True:
        pov "I'm out of here."
    else:
        povi "I need to run."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    if nicole_voyeur == True or nicole_sadist == True:
        povi "I and other guys happened, haha."
    elif nicole_ntr == True:
        povi "I took her for myself for once!"
    else:
        povi "I failed to protect her. I'm sorry."
    scene weekend 10pm 022n
    if susanfirstmeet == True:
        susan "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        susan "Let me help you and then we search your pants."
    else:
        "Woman" "Are you alright, [mother]?"
        mom "Yes... I'm so glad that you came."
        "Woman" "Let me help you and then we search your pants."
    scene weekend 10pm 023n
    if susanfirstmeet == True:
        susan "Who were they?"
        mom "Just some assholes. I'll tell you later."
        susan "Calm down, you're save now."
    else:
        "Woman" "Who were they?"
        mom "Just some assholes. I'll tell you later."
        "Woman" "Calm down, you're save now."
    if nicoleweekendntrreveal == True:
        if nicole_voyeur == True:
            mom "I can't believe he did this to me."
        elif nicole_ntr == True or nicole_sadist == True:
            mom "I can't believe he would do this to me."
        else:
            mom "Why... did he do this?"
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities >= 3:
        jump weekendskip
    else:
        jump weekendacchoose
