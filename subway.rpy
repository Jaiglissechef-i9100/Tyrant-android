

label subwaydeliever:
    hide screen townl
    scene town subway 3pm 002
    pov "{i}This must be the package I need to deliver.{/i}"
    pov "Hey!"
    scene town subway 3pm 003
    "Receiver" "What do you want?"
    pov "{i}Oh, it's a girl! I wonder if she's a member in the gang too?{/i}"
    pov "I got a package to deliver."
    "Girl" "You got this from Davide?"
    pov "Yes."
    scene town subway 3pm 005
    "Girl" "Give it to me."
    pov "{i}Wow, she must be in a bad mood.{/i}"
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
    pov "{i}Wow, really a bad mood.{/i}"
    pov "Ok, ok."
    $ jobdone += 1
    $ dtime += 1
    jump subway


label nicoleweekendntr:
    hide screen locations
    $ messagenicolentr = 2
    scene black
    "You make your way to the subway station."
    scene weekend 10pm 000n
    pov "{i}There she is.{/i}"
    pov "{i}But wait... That's the guy that chased her at our date!{/i}"
    pov "{i}It seems like they're discussing something, maybe I can hear something.{/i}"
    "You go a little closer."
    scene weekend 10pm 001n
    "Peter" "You broke our deal! And you try to avoid me."
    if ndate21ntrsex == True:
        mom "You fucked me at my date. You said we're even now."
        "Peter" "But you continiued to break our deal."
    pov "{i}What? They had a deal? So she lied at me all the time.{/i}"
    mom "It wasn't my fault!"
    "Peter" "You're a liar and I'm sick of your lies."
    scene weekend 10pm 002n
    mom "Huh? Who's that?"
    "Peter" "Someone that'll help me to punish you for your new mistakes."
    mom "You can't be serious."
    "Peter" "Oh yes, I am."
    scene weekend 10pm 003n
    "Peter" "Come with us."
    mom "No, please! Can't we find another solution."
    pov "{i}Damn what they're up to. Are they going to kill her?{/i}"
    "Other guy" "I'm sure that slut will enjoy her punishment more then she should!"
    "Peter" "I hope not!"
    scene weekend 10pm 004n
    pov "{i}I have to do something. I need to follow them.{/i}"
    pov "{i}But what did the guy mean with \"enjoy her punishment\"?{/i}"
    scene weekend 10pm 005n
    pov "{i}Oh... Are they going to punish her in another way?{/i}"
    scene weekend 10pm 006n
    pov "{i}There they are. And my place is dark so they won't see me.{/i}"
    "Peter" "You know exactly that you get punished for your mistakes."
    "Peter" "I have the suspicion that you do this on purpose."
    mom "No..."
    "Other guy" "What a poor denying, haha."
    pov "{i}No, She isn't such a slut, isn't she?{/i}"
    scene weekend 10pm 007n
    "Other guy" "Down with you, time for punishment."
    "Peter" "You'll maybe enjoy his punishment, but I'll be rough so you have to suffer, slut!"
    pov "{i}What, that could be have a bad ending for her.{/i}"
    pov "{i}But maybe these guys are somewhat right, she lied to me also. So maybe she deserves it.{/i}"
    call screen nicoleweekendntrinter

screen nicoleweekendntrinter():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1517 ypos 305 action (Hide ('nicoleweekendntrinter'), Jump('nicoleweekendntrstop')) hovered tt.Action ("Interfere") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1517 ypos 509 action (Hide ('nicoleweekendntrinter'), Jump('nicoleweekendntrsex')) hovered tt.Action ("Let it happen") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicoleweekendntrstop:
    pov "{i}I need to help her. It doesn't matter what she may did.{/i}"
    pov "{i}I won't stand these two guys, but it's dark here so maybe I can trick them.{/i}"
    pov "FREEZE! I think I found them, they're over here!"
    scene weekend 10pm 008bn
    "Other guy" "Damn, the cops!"
    "Peter" "Not now! Shit, run!"
    "They start to run away at the other way out of this corner."
    scene weekend 10pm 009bn
    mom "[pov!]"
    if inc == True:
        pov "Hi mom."
    else:
        pov "Hi [mother]."
    mom "What are you doing here? And where's the police?"
    scene weekend 10pm 010bn
    mom "Oh, I understand. There is no police. You tricked them and saved me."
    pov "Yes, you send your message accidentally to me, so I came to check on you."
    mom "Oh that's so sweet [pov]."
    pov "But your talking with them confused me."
    scene weekend 10pm 011bn
    mom "Come here, let me hug you!"
    mom "Don't give any attention to the things they say. They are liars and gangsters."
    pov "{i}She still won't tell me the truth, but at least she's save.{/i}"
    mom "I'm so glad I have you!"
    if susanfirstmeet == True:
        susan "There you are [mother]!"
    else:
        "Woman" "There you are [mother]!"
    scene weekend 10pm 012bn
    if susanfirstmeet == False:
        $ susan = renpy.input(_("Her name is...")) or _("Susan")
    mom "[susan], you're here too."
    susan "I waited for you but then I came here to check on you."
    mom "Something bad was about to happen but he rescued me."
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
    susan "Why not, he likes to rescue older women."
    pov "Ähem..."
    scene weekend 10pm 014bn
    mom "Sorry [pov]. But I need to take her to her home. She's drunk."
    susan "I'm not. I just admire that tasty boy."
    mom "We'll meet on monday again. And I won't forget your help."
    if inc == True:
        pov "Bye mom."
    else:
        pov "Bye [mother]."
    pov "Bye [susan]."
    susan "Bye my tough boy!"
    $ susanfirstmeet = True
    scene black
    "You go back home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrsex:
    pov "{i}No, I won't help her this time. When she's a bad liar, she can endure her punishment.{/i}"
    scene weekend 10pm 008n
    "Other guy" "Come here, slut. Receive your loving dick!"
    mom "HNNG... <choke>"
    scene weekend 10pm 009n
    "Peter" "<slap> You slut needs a good spanking."
    mom "Hnn... hnng..."
    pov "{i}Damn, they're rough, maybe it's really to much.{/i}"
    call screen nicoleweekendntrlikechoose

screen nicoleweekendntrlikechoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1590 ypos 309 action (Hide ('nicoleweekendntrlikechoose'), Jump('nicoleweekendntrlike')) hovered tt.Action ("I Like NTR") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1590 ypos 513 action (Hide ('nicoleweekendntrlikechoose'), Jump('nicoleweekendntrdislike')) hovered tt.Action ("I hate NTR") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicoleweekendntrdislike:
    pov "{i}They're definitely too rough. It's like they raping her.{/i}"
    pov "{i}I should have do something. I'm such an idiot!{/i}"
    scene weekend 10pm 010n
    "Peter" "Look at this slut. She's getting wet."
    mom "<choke> Hnng..."
    "Other guy" "Her choking on my dick was so hot, I'm about to cum!"
    mom "Hah... hah..."
    "Other guys" "Take my spunk in your lovely face, slut!"
    "Peter" "I bet she waited impatient for it!"
    pov "{i}That damn assholes!{/i}"
    scene weekend 10pm 011n
    "Hobo" "Hey guys. I see what you're doing here and I wonder I can join the fun?"
    pov "{i}What, who's that guy? I think I saw him before.{/i}"
    "Other guy" "Sure. I'm done here, the slut did a good job."
    "Hobo" "Yes, I saw that, but I can teach her even better."
    "Peter" "Then go on and take his place."
    mom "You can't be serious..."
    "Hobo" "So you're a real slut? Waiting for the next dick with sperm on your face!"
    pov "{i}They can't be serious.{/i}"
    scene weekend 10pm 012n
    "Hobo" "I'll teach you a properly deepthroat."
    mom "<choke> HNNG...!"
    "Peter" "Good. She needs a hard punishment."
    pov "{i}Damn, he's fucking her mouth!{/i}"
    jump nicoleweekendntrsusan

label nicoleweekendntrsusan:
    if susanfirstmeet == True:
        susan "[mother], you there?"
    else:
        "Woman" "[mother], you there?"
    "Peter" "Damn, someone is coming. It's your lucky day, slut!"
    "Hobo" "What a pity. So I have to teach you an other time more!"
    "Peter" "Let's run!"
    pov "{i}Good, she get's help.{/i}"
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    pov "{i}[mother] got abused and I decided to watch. I feel so helpless.{/i}"
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
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrlike:
    pov "{i}Ha, it's the right punishment for her.{/i}"
    scene weekend 10pm 010n
    "Peter" "Look at this slut. She's getting wet."
    mom "<choke> Hnng..."
    "Other guy" "Her choking on my dick was so hot, I'm about to cum!"
    mom "Hah... hah..."
    "Other guys" "Take my spunk in your lovely face, slut!"
    "Peter" "I bet she waited impatient for it!"
    pov "{i}Wait? She's getting wet. So she's really a slut.{/i}"
    scene weekend 10pm 011n
    "Hobo" "Hey guys. I see what you're doing here and I wonder I can join the fun?"
    pov "{i}What, who's that guy? I think I saw him before.{/i}"
    "Other guy" "Sure. I'm done here, the slut did a good job."
    "Hobo" "Yes, I saw that, but I can teach her even better."
    "Peter" "Then go on and take his place."
    mom "You can't be serious..."
    "Hobo" "So you're a real slut? Waiting for the next dick with sperm on your face!"
    pov "{i}Hah, they're serious.{/i}"
    scene weekend 10pm 012n
    "Hobo" "I'll teach you a properly deepthroat."
    mom "<choke> HNNG...!"
    "Peter" "Good. She needs a hard punishment."
    pov "{i}Damn, he's fucking her mouth! But that gaves me an idea.{/i}"
    call screen nicoleweekendntrjoinchoose

screen nicoleweekendntrjoinchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1590 ypos 309 action (Hide ('nicoleweekendntrjoinchoose'), Jump('nicoleweekendntrjoin')) hovered tt.Action ("Join too [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 513 action (Hide ('nicoleweekendntrjoinchoose'), Jump('nicoleweekendntrnojoin')) hovered tt.Action ("Forget the idea") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicoleweekendntrnojoin:
    pov "{i}No, that was a bad idea, I'll just watch.{/i}"
    if susanfirstmeet == True:
        susan "[mother], you there?"
    else:
        "Woman" "[mother], you there?"
    "Peter" "Damn, someone is coming. It's your lucky day, slut!"
    "Hobo" "What a pity. So I have to teach you an other time more!"
    "Peter" "Let's run!"
    pov "{i}Damn, she get's help.{/i}"
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    pov "{i}[mother] got abused and I decided to watch. It's like I got revenge.{/i}"
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
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrjoin:
    $ momcorruption += 1
    $ nicoleweekendntrjoin = True
    pov "{i}When that Hobo can join I can join too.{/i}"
    pov "{i}I'll just need to fake my voice. And then I can have revenge too.{/i}"
    scene weekend 10pm 013n
    mom "<choke> Urgh!"
    pov "<with a faked voice> Hey bro, can I have fun too?"
    "Peter" "Damn, you have many admirers today slut!"
    scene weekend 10pm 014n
    "Peter" "Everyone wants to use you. like the cum-dumpster you are."
    "Peter" "Of course you can have your turn. I was about to leave anyway."
    "Peter" "You hear slut. So this will be maybe your last dick today, haha."
    mom "Hnng... Urgh! Urgh!"
    "Hobo" "Good, hold it deep slut."
    pov "<with a faked voice> Thank you bro!"
    scene weekend 10pm 015n
    pov "{i}Damn, he wasn't lying. She's already very wet. So she's enjoying her abuse.{/i}"
    pov "{i}Then I mustn't feel bad to have my fun with her too.{/i}"
    pov "{i}But which hole should I use?{/i}"
    call screen nicoleweekendntrfuck

screen nicoleweekendntrfuck():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 309 action (Hide ('nicoleweekendntrfuck'), Jump('nicoleweekendntrfuckp')) hovered tt.Action ("Fuck her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 513 action (Hide ('nicoleweekendntrfuck'), Jump('nicoleweekendntrfucka')) hovered tt.Action ("Fuck her asshole") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicoleweekendntrfuckp:
    $ nicoleweekendntrpussy = True
    jump nicoleweekendntrfucka

label nicoleweekendntrfucka:
    if nicoleweekendntrpussy == True:
        pov "{i}I'll go for her pussy. With her legs closed she'll be very tight.{/i}"
    else:
        pov "{i}I'll go for her ass. With her legs closed she'll be very tight.{/i}"
    scene weekend 10pm 016n
    mom "<choke> Urgh! Urgh!"
    "Hobo" "Stop fighting, slut!"
    pov "{i}She's having a hard time there, but she'll feel better when she feel my dick inside her.{/i}"
    scene weekend 10pm 017n
    if nicoleweekendntrpussy == True:
        "You enter her pussy."
        mom "Hnng... Urgh!"
        pov "{i}Oh her wet pussy is clinging on me. And it's so tight. This will be a good fuck!{/i}"
    else:
        "You enter her asshole."
        mom "Hnng... Urgh!"
        pov "{i}Oh her asshole is clinging on me. And it's so tight. This will be a good fuck!{/i}"
    "You fuck her rough."
    mom "Hnng... Hnn..."
    pov "{i}This is so damn good, her fighting body will make me cum in no time.{/i}"
    "Hobo" "This slut is a good fuck, isn't she?"
    pov "{i}But maybe I should go a step further to get the ultimate revenge. She's helpless and busy, so she won't complain.{/i}"
    jump nicoleweekendntrtell

label nicoleweekendntrtell:
    call screen nicoleweekendntrtellchoose

screen nicoleweekendntrtellchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1590 ypos 309 action (Hide ('nicoleweekendntrtellchoose'), Jump('nicoleweekendntryesreveal')) hovered tt.Action ("Reveal yourself") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1590 ypos 513 action (Hide ('nicoleweekendntrtellchoose'), Jump('nicoleweekendntrnoreveal')) hovered tt.Action ("Don't") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicoleweekendntrnoreveal:
    pov "{i}No, I'll stay silent. She mustn't know that I'm fucking her.{/i}"
    scene weekend 10pm 018n
    mom "Hnng...? <choke> HNNG..!"
    "Hobo" "Oh, she's going crazy. You love my dick that much?"
    if nicoleweekendntrpussy == True:
        pov "{i}Damn, her pussy is so greedy. I'm about to cum!{/i}"
    else:
        pov "{i}Damn, her asshole is so greedy. I'm about to cum.{/i}"
    call screen nicoleweekendntrcumnorevealchoose

screen nicoleweekendntrcumnorevealchoose():
    default tt = Tooltip (" ")

    fixed:
        if nicoleweekendntrpussy == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 309 action (Hide ('nicoleweekendntrcumnorevealchoose'), Jump('nicoleweekendntrcumnorevealinsidep')) hovered tt.Action ("Cum inside her pussy") focus_mask True
        if nicoleweekendntrpussy == False:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 309 action (Hide ('nicoleweekendntrcumnorevealchoose'), Jump('nicoleweekendntrcumnorevealinsidea')) hovered tt.Action ("Cum inside her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 513 action (Hide ('nicoleweekendntrcumnorevealchoose'), Jump('nicoleweekendntrcumnorevealoutside')) hovered tt.Action ("Cum outside") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicoleweekendntrcumnorevealinsidep:
    if inc == True:
        pov "{i}I'll cum inside your wet pussy, mom!{/i}"
    else:
        pov "{i}I'll cum inside your wet pussy, [mother]!{/i}"
    mom "HNNG! HMM!"
    "Hobo" "Oh this wild slut will make me cum too."
    "You release your sperm in her pussy."
    pov "{i}Hnng! Yes!{/i}"
    scene weekend 10pm 019nip
    pov "{i}Oh yes, I came so much!{/i}"
    mom "Hnn... hnn..."
    pov "{i}She loved it.{/i}"
    scene weekend 10pm 020n
    mom "<spit> Urgh! Hah..."
    "Hobo" "You're supposed to swallow it! Bad Slut!"
    pov "{i}Ha, he came so much, she's still choking on it.{/i}"
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    pov "{i}Let's run.{/i}"
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    pov "{i}I and other guys happened, haha.{/i}"
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
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrcumnorevealinsidea:
    if inc == True:
        pov "{i}I'll cum inside your asshole, mom!{/i}"
    else:
        pov "{i}I'll cum inside your asshole, [mother]!{/i}"
    mom "HNNG! HMM!"
    "Hobo" "Oh this wild slut will make me cum too."
    "You release your sperm in her asshole."
    pov "{i}Hnng! Yes!{/i}"
    scene weekend 10pm 019nia
    pov "{i}Oh yes, I came so much!{/i}"
    mom "Hnn... hnn..."
    pov "{i}She loved it.{/i}"
    scene weekend 10pm 020n
    mom "<spit> Urgh! Hah..."
    "Hobo" "You're supposed to swallow it! Bad Slut!"
    pov "{i}Ha, he came so much, she's still choking on it.{/i}"
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    pov "{i}Let's run.{/i}"
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    pov "{i}I and other guys happened, haha.{/i}"
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
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrcumnorevealoutside:
    if inc == True:
        pov "{i}I'll cum on your ass, mom!{/i}"
    else:
        pov "{i}I'll cum on your ass, [mother]!{/i}"
    mom "HNNG! HMM!"
    "Hobo" "Oh this wild slut will make me cum too."
    scene weekend 10pm 019no
    "You release your sperm on her ass."
    pov "{i}Hnng! Yes!{/i}"
    pov "{i}Oh yes, I came so much!{/i}"
    mom "Hnn... hnn..."
    pov "{i}She loved it.{/i}"
    scene weekend 10pm 020n
    mom "<spit> Urgh! Hah..."
    "Hobo" "You're supposed to swallow it! Bad Slut!"
    pov "{i}Ha, he came so much, she's still choking on it.{/i}"
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    pov "{i}Let's run.{/i}"
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    pov "{i}I and other guys happened, haha.{/i}"
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
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose


label nicoleweekendntryesreveal:
    pov "{i}I'll reveal myself and watch how she go crazy.{/i}"
    pov "Yes, I know that slut. She's really a good fuck!"
    $ nicoleweekendntrreveal = True
    scene weekend 10pm 018n
    mom "Hnng...? <choke> HNNG..!"
    "Hobo" "Oh, she's going crazy. So she isn't happy that you do her?"
    pov "Haha, no. But what can she do, her mouth is busy, haha."
    "Hobo" "Haha, you're damn right."
    if nicoleweekendntrpussy == True:
        pov "Damn, her pussy is so greedy. I'm about to cum!"
    else:
        pov "Damn, her asshole is so greedy. I'm about to cum."
    call screen nicoleweekendntrcumrevealchoose

screen nicoleweekendntrcumrevealchoose():
    default tt = Tooltip (" ")

    fixed:
        if nicoleweekendntrpussy == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 309 action (Hide ('nicoleweekendntrcumrevealchoose'), Jump('nicoleweekendntrcumrevealinsidep')) hovered tt.Action ("Cum inside her pussy") focus_mask True
        if nicoleweekendntrpussy == False:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 309 action (Hide ('nicoleweekendntrcumrevealchoose'), Jump('nicoleweekendntrcumrevealinsidea')) hovered tt.Action ("Cum inside her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1590 ypos 513 action (Hide ('nicoleweekendntrcumrevealchoose'), Jump('nicoleweekendntrcumrevealoutside')) hovered tt.Action ("Cum outside") focus_mask True


    frame:
        xalign .5
        text tt.value

label nicoleweekendntrcumrevealinsidep:
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
    pov "{i}Ha, he came so much, she's still choking on it.{/i}"
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    pov "Let's run."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    pov "{i}I and other guys happened, haha.{/i}"
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
        mom "I can't believe he did this to me."
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrcumrevealinsidea:
    pov "I'll cum inside your asshole, slut!"
    mom "HNNG! HMM!"
    "Hobo" "Oh this wild slut will make me cum too."
    "You release your sperm in her asshole."
    pov "Hnng! Yes!"
    scene weekend 10pm 019nia
    pov "Oh yes, I came so much!"
    mom "Hnn... hnn..."
    pov "You loved it, didn't you slut!"
    scene weekend 10pm 020n
    mom "<spit> Urgh! Hah..."
    "Hobo" "You're supposed to swallow it! Bad Slut!"
    pov "{i}Ha, he came so much, she's still choking on it.{/i}"
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    pov "Let's run."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    pov "{i}I and other guys happened, haha.{/i}"
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
        mom "I can't believe he did this to me."
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label nicoleweekendntrcumrevealoutside:
    pov "I'll cum on your ass, slut!"
    mom "HNNG! HMM!"
    "Hobo" "Oh this wild slut will make me cum too."
    scene weekend 10pm 019no
    "You spray your sperm over her ass."
    pov "Hnng! Yes!"
    pov "Oh yes, I came so much!"
    mom "Hnn... hnn..."
    pov "You loved it, didn't you slut!"
    scene weekend 10pm 020n
    mom "<spit> Urgh! Hah..."
    "Hobo" "You're supposed to swallow it! Bad Slut!"
    pov "{i}Ha, he came so much, she's still choking on it.{/i}"
    if susanfirstmeet == True:
        susan "Hey, what are you doing over there?"
    else:
        "Woman" "Hey, what are you doing over there?"
    "Hobo" "Shit, someone is coming. Good I'm finished."
    pov "Let's run."
    scene weekend 10pm 021n
    mom "Hah... hah..."
    if susanfirstmeet == True:
        susan "Oh no, what happened?"
    else:
        "Woman" "Oh no, what happened?"
    pov "{i}I and other guys happened, haha.{/i}"
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
        mom "I can't believe he did this to me."
    scene black
    "They're gone. You go also home."
    $ weekendactivities += 1
    $ nicoleweekendntrevent = True
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose