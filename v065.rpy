#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. Time Location - Featured - Scenes
#----- End List -----

#----- Custom Love/Corruption Menu for Nicole Outing -----
label basementnicoleoutinglanding:
    call screen basementnicoleoutinglovcorchoice

#----- Custom choice used above -----
screen basementnicoleoutinglovcorchoice():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if mombasementlovesecond == True:
            imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('basementnicoleoutinglovcorchoice'), Jump('basementnicoleoutinglovelanding')) hovered tt.Action ("Love") focus_mask True
        if mombasementcorsecond == True:
            imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('basementnicoleoutinglovcorchoice'), Jump('basementnicoleoutingcorruptionlanding')) hovered tt.Action ("Corruption") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutinglovelanding:
    call screen basementnicoleoutinglovechoices

#----- Custom Love Choices -----
screen basementnicoleoutinglovechoices():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('basementnicoleoutinglovechoices'), Jump('basementnicoleoutinglove')) hovered tt.Action ("Love") focus_mask True
        imagebutton auto "images/edited/gui/vice/icon_love_%s.png" action (Hide('basementnicoleoutinglovechoices'), Jump('basementnicoleoutingcorlove')) hovered tt.Action ("Corruption to Love") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionlanding:
    call screen basementnicoleoutingcorruptionchoices

#----- Custom Corruption Choices -----
screen basementnicoleoutingcorruptionchoices():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('basementnicoleoutingcorruptionchoices'), Jump('basementnicoleoutingcorruption')) hovered tt.Action ("Corruption") focus_mask True
        imagebutton auto "images/edited/gui/vice/icon_corruption_%s.png" action (Hide('basementnicoleoutingcorruptionchoices'), Jump('basementnicoleoutinglovecor')) hovered tt.Action ("Love to Corruption") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Outing Nicole to the Gang -----
label basementnicoleoutingcorruption:
    hide screen locations
    hide screen townl
    scene black
    "You decide it's time to introduce [mother] as your girl to the other gangmembers."
    scene basement 10pm 015c
    "You sit in the basement with the others, waiting for [mother] to show up."
    povi "It's time they learn that she is my slut now."
    scene basement 10pm 017c
    povi "There she is. Sexy as ever."
    davide "God damn. Took you long enough. Are you going to bring us some drinks now?"
    mom "Yes."
    scene livingroom 10pm 040
    povi "That outfit is so sexy. I can't wait to use her!"
    davide "So what do you think about what we talked about earlier, Bruce?"
    dad "Huh? I'm not sure yet, sorry..."
    scene livingroom 10pm 041
    mom "The drinks are ready. Do you need anything else?"
    povi "Now it's time to show the others that she's mine!"
    povi "We'll also be able to see if she's really submitted to me. I wonder how Bruce will react?"
    povi "I get he's going to go fucking ballistic with me stealing his wife like this. But he won't do shit. Besides, Davide won't let Bruce fuck with someone higher in the gang than he is."
    if inc == True:
        povi "I wonder if they'll be shocked seeing what I do with my mom?"
    povi "Oh well, it's decided already."
    pov "I need some service, slut!"
    scene livingroom 10pm 042a
    mom "Huh?"
    dad "What did you say?"
    davide "Hmm?"
    pov "I was told every gang member should make some bitch his personal girl, so I made her my slut!"
    dad "W-What...?"
    pov "[mother] stop standing around with that confused look on your face and service me!"
    "You pull your dick out."
    scene livingroom 10pm 043a
    pov "Or have you already forgotten you're promise to submit to me?"
    mom "Hnng..."
    dad "How dare you... You can't be serious?"
    davide "Haha, this is so fuckin' great! You surprise me everytime, [pov]!"
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    scene livingroom 10pm 044a
    pov "Be a good slut and get on your knees! You have work to do."
    mom "Hnn..."
    dad "Stop this madness! [pov]!"
    davide "Shut the fuck up! I want to see if she'll really do it."
    scene livingroom 10pm 045a
    mom "You really want me to do this?"
    if inc == True:
        pov "You decided to become my slut, mom! You're the one that wants this."
    else:
        pov "You decided to become my slut, [mother]! You're the one that wants this."
    pov "You don't want disappointed me now, so go on and suck on the dick you've chosen!"
    dad "No... no..."
    if NTR == True and momrelationship <= 5:
        jump basementnicoleoutingcorruptionNTR
    else:
        jump basementnicoleoutingcorruption5

label basementnicoleoutingcorruption5:
    scene livingroom 10pm 046a
    pov "Good slut!"
    mom "<suck>"
    dad "This can't be... No!"
    davide "Hahahaha... you're the man [pov]!"
    scene livingroom 10pm 047a
    dad "I'll kill you!"
    davide "You'll do NOTHING bitch! You know the rules! I'll break your bones if you pull this shit!"
    dad "But she's my wife!"
    if inc == True:
        dad "And his mother!"
    davide "That doesn't matter. He's made his choice. I can understand his decision, haha. And you're going to respect it too."
    pov "Just accept it. You lost! She's mine now."
    dad "What are you..."
    davide "Haha, he's right, Bruce. She's no longer yours now, hahaha."
    scene livingroom 10pm 048a
    povi "She's trembling, but she made her choice. There is no way to turning back for her now."
    mom "<suck> <lick>"
    povi "Probably want to reinforce her choice with some praise. I want her to know this was the right choice."
    povi "And then she'll be more confident when serving me later."
    povi "I could also spice things up a little bit."
    pov "You're doing very good, slut. Your hot lips on my dick is just the thing I needed!"
    call screen basementnicoleoutingcorruptionbj

screen basementnicoleoutingcorruptionbj():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionbj'), Jump('basementnicoleoutingcorruptionbjnormal')) hovered tt.Action ("Let her continue") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionbj'), Jump('basementnicoleoutingcorruptionbjdt')) hovered tt.Action ("Help her (deepthroat)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionbjnormal:
    povi "Hmm, no. I'll let her do the work on her own. She's very good at this."
    $ mombasementcoroutingbjnormal = True
    jump basementnicoleoutingcorruptionbjdt

label basementnicoleoutingcorruptionbjdt:
    povi "I want more than just a simple blow-job!"
    if mombasementcoroutingbjnormal == False:
        pov "Let me help you!"
        scene livingroom 10pm 048adt
        mom "Hnng..."
        povi "She's gagging but not fighting back. Very good."
    scene livingroom 10pm 047a
    dad "You must be blackmailing her. She won't never do something like this of her own free will."
    davide "Calm down! You've lost, he's the winner. It doesn't matter how she became his slut!"
    dad "But..."
    davide "NO! You're going to shut the fuck up now! For real this time!"
    "You form the word \"loser\" to Bruce."
    scene livingroom 10pm 047aa
    davide "But we have another problem to solve now, haha."
    pov "Oh yeah, what is that?"
    davide "Bruce doesn't have a girl anymore and every gang member should have one. Even the shitty ones."
    pov "So we need to pick a girl for Bruce, since his wife is mine now?"
    davide "Exactly! We'll pick a suitable girl for him so he won't lose her again, hahaha."
    dad "Please, Davide..."
    davide "Shut up!"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 048adt
    else:
        scene livingroom 10pm 048a
    pov "Seems like you made the right decision to give in to me!"
    mom "Hmm..."
    dad "Shut the... grrr..."
    scene livingroom 10pm 047aaa
    davide "So any thoughts on which bitch would be a good fit for this loser? Maybe [miranda], she has very low standards, haha!"
    povi "Haha, [mother] is squeezing me hard. She doesn't want her to be Bruce's new girl. She really hates her!"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 049adt
    else:
        scene livingroom 10pm 049a
    pov "Relax, slut. No one's made any decisions yet. And even if I decide she's the one then you'll accept it, because you know your place! Right?"
    if mombasementcoroutingbjnormal == False:
        mom "Hmm...!"
    else:
        mom "Yes..."
    scene livingroom 10pm 047aaa
    davide "Can you think of anyone else?"
    pov "Hmm... a girl with low standards..."
    dad "You can't be serious..."
    pov "What's with that girl I delivered the packages to for you? The one in the subway."
    if rubyfirstmeet == False:
        scene town subway ruby
        "What's her name?"
        $ rubyname = renpy.input(_("Her name is...")) or _("Ruby")
        $ rubyname = rubyname.strip()
        if rubyname == "":
            $ lsname = "Ruby"
        $ rubyfirstmeet = True #----- added -----
    scene livingroom 10pm 047aaaa
    davide "You mean [ruby]? Really? She's a junkie."
    davide "She's already half-dead and I don't want to know with how many other junkies she fucked."
    davide "Not to mention how many STDs she's got. Fuck... that would be some heavy shit..."
    pov "But that might just be the right choice for him, haha."
    dad "Please, [pov]..."
    povi "Oh shit, he's begging me. I could humiliate him even more."
    povi "I could choose [miranda] to be his girl. She's already a slut and [mother] hates her, so she'll hate Bruce even more."
    povi "And also it could spice things up when I decide to have [miranda] and [mother] have fun together, haha."
    povi "Or should I choose the subway girl, [ruby]? I mean any port in a storm, right?"
    povi "He might even get ill or an STD. I'm fairly certain that would break him completely..."
    povi "Or maybe he shouldn't be allowed to have any girl. He'd be left to his own hand for pleasure, haha."
    povi "But might push him over the edge and he could do something stupid, like raping someone."
    povi "Decisions, hmm..."
    call screen basementnicoleoutingcorruptionbruce

screen basementnicoleoutingcorruptionbruce():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionbruce'), Jump('basementnicoleoutingcorruptionbrucemiranda')) hovered tt.Action ("He can have [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionbruce'), Jump('basementnicoleoutingcorruptionbruceruby')) hovered tt.Action ("He'll take [ruby]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionbruce'), Jump('basementnicoleoutingcorruptionbrucenone')) hovered tt.Action ("No girl for you!") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionbruceruby:
    pov "He can have [ruby]. But only [ruby]!"
    scene livingroom 10pm 047aaa
    dad "You can't be serious!"
    davide "Haha, I like that. You're a cruel boy. So be it. You should be happy Bruce. At least you can fuck someone, haha."
    pov "I mean you don't have to fuck her if you don't want to. But then it's just your hand to keep you company."
    dad "But why?"
    pov "Because I can. Oh, one other thing. Unless you clean that girl up..."
    pov "She isn't allowed to enter the house. I don't want my slut getting ill."
    povi "Wow, now she's really sucking hard. Is that her way of agreeing with my decision?"
    $ dadandruby = True
    jump basementnicoleoutingcorruption2

label basementnicoleoutingcorruptionbrucemiranda:
    pov "He can have some fun with [miranda] too."
    scene livingroom 10pm 047aaa
    dad "Too?"
    pov "Yes, you can get some relief from her, but she'll be free for others to have fun with too."
    davide "Ha, a wise decision. And that works out for Bruce, since he has a crush on that slut too."
    mom "Hnn...!"
    pov "Oh, someone isn't pleased with my decision?"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 049adt
    else:
        scene livingroom 10pm 049a
    pov "I know you hate her, but you're going accept my decision, slut. Right?"
    mom "Hmm..."
    pov "Good!"
    $ dadandmiranda = True
    jump basementnicoleoutingcorruption2

label basementnicoleoutingcorruptionbrucenone:
    pov "He's not allowed to have any girl!"
    scene livingroom 10pm 047aaa
    dad "What?"
    davide "Haha, you can't be serious."
    pov "Oh yes, I am. He's so weak and he makes me angry just looking at him."
    dad "But why?"
    pov "Because I said so. You're a loser and until you so something to deserve it, no pussy for you!"
    davide "Haha, I like that. You're cruel boy. So be it."
    dad "But..."
    $ dadalone = True
    jump basementnicoleoutingcorruption2

label basementnicoleoutingcorruption2:
    povi "Now that this is decided, I can relax. I can really enjoy [mother]'s sucking my cock again."
    pov "Oh yes, I'm close slut!"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 049adt
    else:
        scene livingroom 10pm 049a
    povi "I need to cum, but where do I want to put it?"
    call screen basementnicoleoutingcorruptionbjcum

screen basementnicoleoutingcorruptionbjcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionbjcum'), Jump('basementnicoleoutingcorruptionbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionbjcum'), Jump('basementnicoleoutingcorruptionbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionbjcumout:
    pov "I'm going to cover you face. Get ready slut!"
    mom "Hmm..."
    scene livingroom 10pm 050o
    pov "Ohhh... yes!"
    "You come all over her face."
    scene livingroom 10pm 051o
    mom "Hnn... are you satisfied? Did I do a good job?"
    povi "Oh, this is something new. But I like it, like a good slut."
    pov "Yes, you did a good job, slut!"
    $ basement10pmnicoleoutingcumface = True
    jump basementnicoleoutingcorruption3

label basementnicoleoutingcorruptionbjcumin:
    pov "I'm going to cum in your mouth. Get ready slut!"
    mom "Hmm..."
    scene livingroom 10pm 048a
    pov "Ohhh... yes!"
    "You come in her mouth."
    scene livingroom 10pm 051i
    mom "Hmm..."
    povi "Oh, she's showing it back to me. Like a good slut."
    pov "You can swallow it now!"
    scene livingroom 10pm 052i
    mom "<gulp> <gulp>"
    davide "Damn, you've tamed her already, haha."
    scene livingroom 10pm 053i
    mom "Aahhh..."
    pov "Yes, you did good. Swallowing it all like the hot slut you are!"
    jump basementnicoleoutingcorruption3

label basementnicoleoutingcorruption3:
    pov "Now go and sit on the couch with Bruce, so he can see what he lost, haha."
    davide "Hahaha, this is getting even better."
    mom "Yes, [pov]."
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 054i
    else:
        scene livingroom 10pm 054o
    dad "What's gotten into you?"
    if inc == True:
        dad "He's your son and you want to be his slut? What the fuck is wrong with you?"
    else:
        dad "He's the son of your best friend and you want to be his slut? What the fuck is wrong with you?"
    mom "Hnn..."
    dad "That's not you! Did he blackmail you?"
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 055i
    else:
        scene livingroom 10pm 055o
    davide "That's enough! We made a decision and you're going to accept it!"
    dad "But it's not fair!"
    davide "Fuck fair! I don't care, it's her decision! And I'm not going to allow some low ranked bitch to rant and rave in front of his superiors!"
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 056i
    else:
        scene livingroom 10pm 056o
    dad "So you really want to break all the taboos and be with him?"
    dad "You have no idea how disappointed I am. But you're safe, I'm not going to risk all we did..."
    povi "Shit Bruce! You do realize Davide it right here! Why not just tell him you're a fucking cop why don't you?!"
    dad "YOU DAMN SLUT!"
    scene livingroom 10pm 057
    pov "STOP!"
    dad "Huh?"
    pov "This is going to stop now and you're going behave like a god damned man with some dignity! I know what you are Bruce! Don't forget it!"
    povi "I'm not going to say shit, it could put the girls in danger, but maybe I can get him to calm the fuck down."
    "You give him a knowing glance and he shuts up for moment."
    dad "..."
    pov "So, not that you understand, just don't forget... you're not allowed to touch your wife anymore."
    pov "She's mine now and I warn you, press me on the issue and you're regret it!"
    dad "..."
    dad "Fuck you!"
    scene livingroom 10pm 058
    dad "I'm out of here!"
    davide "Hahaha, what a great show!"
    davide "Let him go, he'll calm down. He's weak, haha."
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 059i
    else:
        scene livingroom 10pm 059o
    if inc == True:
        pov "What's wrong mom? You're all mine now slut, aren't you happy?"
    else:
        pov "What's wrong [mother]? You're all mine now slut, aren't you happy?"
    mom "Hnn..."
    pov "Oh I see, you need a dick!"
    mom "..."
    davide "Or maybe two?"
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 060ai
    else:
        scene livingroom 10pm 060ao
    povi "Is he serious? He wants me to share her?"
    davide "<grin>"
    pov "Hmm..."
    call screen basementnicoleoutingcorruptionshare

screen basementnicoleoutingcorruptionshare():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionshare'), Jump('basementnicoleoutingcorruptionshareyes')) hovered tt.Action ("Share her with Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionshare'), Jump('basementnicoleoutingcorruptionshareno')) hovered tt.Action ("Don't share her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionshareyes:
    pov "Yeah, I guess you're right. Two dicks are better then one!"
    davide "Great. You hear that [mother]? You're going to serve me too."
    pov "Get in position, slut, so we can start."
    mom "Yes, hnn..."
    povi "Oh, she doesn't seem to happy about being shared."
    scene livingroom 10pm 065as
    davide "Hell yes! This will be so much fun. Two alphas spliting a slut!"
    pov "Haha, you sound like you never had that before."
    davide "Do you see any other Alpha's here? You think that weak loser Bruce is an Alpha? Fuck no!"
    pov "Then let's enjoy her!"
    scene livingroom 10pm 066s
    povi "This outfit is so perfect. I can choose between her pussy or asshole."
    davide "Be proud slut. Now you can suck my dick."
    $ basement10pmnicoleoutingshare = True
    call screen basementnicoleoutingcorruptionsharechoose

screen basementnicoleoutingcorruptionsharechoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionsharechoose'), Jump('basementnicoleoutingcorruptionsharepussy')) hovered tt.Action ("Fuck her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionsharechoose'), Jump('basementnicoleoutingcorruptionshareass')) hovered tt.Action ("Fuck her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionshareass:
    $ basement10pmnicoleoutingfuckass = True
    pov "I'll give you a good fuck in your ass now, slut! Get ready."
    jump basementnicoleoutingcorruptionsharepussy

label basementnicoleoutingcorruptionsharepussy:
    if basement10pmnicoleoutingfuckass == False:
        pov "I'll give you a good fuck in your pussy now, slut! Get ready."
    davide "Two dicks, you must be in heaven."
    mom "Hnn..."
    povi "She's still not very pleased about this."
    pov "Show us some more appreciation, slut! I gave Davide permission to join us so he should have a good time too!"
    mom "Yes, you're right [pov]. I'm sorry Davide. Please use my mouth."
    davide "Oh, I will. Here, have a taste."
    scene livingroom 10pm 068s
    mom "Hmm... <lick>"
    davide "Oh yes, that tongue is amazing. You'll have so much fun with this mouth, [pov]."
    povi "Nice. Now she's submitting even more to me."
    pov "Now it's time you get your second dick, slut."
    scene livingroom 10pm 067
    povi "Oh yes, her ass is so sexy."
    if inc == True:
        povi "My mother is presenting herself to me, perfect little world we live in."
    else:
        povi "[mother] is presenting herself to me, perfect little world we live in."
    povi "She's trembling, waiting for my move. But I need to know how much she wants it."
    davide "What are you waiting for, [pov]."
    pov "My slut didn't beg for my dick, yet."
    davide "Hahaha, you're serious?"
    if basement10pmnicoleoutingfuckass == True:
        mom "Please [pov]. Please stick your hard dick in my tight asshole."
    else:
        mom "Please [pov]. Please stick your hard dick in my wet pussy."
    davide "Damn, bro!"
    pov "Much better!"
    scene livingroom 10pm 070
    mom "Aaahnn..."
    pov "All in!"
    scene livingroom 10pm 070s
    davide "Yes, suck on my cock."
    mom "<suck> <lick>"
    povi "She doesn't like being shared. She'll be even more willing when we're alone next time."
    povi "And she'll be more submissive to avoid sharing. But either way she accepts my decisions."
    povi "She'll be the best slut ever!"
    if basement10pmnicoleoutingfuckass == True:
        pov "Your tight asshole is like heaven, slut."
    else:
        pov "Your wet pussy is like heaven, slut."
    davide "Her mouth is also fucking great, haha."
    scene livingroom 10pm 071s
    davide "Perfect, she's working on my dick so eagerly since you've stuffed so good, haha."
    pov "Yes, she's doing well. And my slut will learn that serving more than one dick is a good thing, haha."
    davide "So this mouth will taste my dick again?"
    pov "We'll see."
    mom "Hnn... hnn..."
    davide "Oh, your slut likes the idea too."
    pov "Yes, haha."
    povi "She doesn't, but who cares. Let him have some fun, for now."
    davide "I need to finish soon, her mouth is too good."
    pov "Me too."
    scene livingroom 10pm 069s
    davide "Get it deep now, ha."
    mom "Hnn..."
    davide "I really appreciate this bro. It was a good decision to bring you into the fold."
    davide "You're going to do great things in the future."
    pov "Well, we'll see, haha."
    davide "Oh yes, I'm cumming, slut!"
    davide "Haaa, haaa...!"
    mom "Hmm..."
    pov "Damn, I'm so close too. She's gotten so clingy!"
    scene livingroom 10pm 070
    call screen basementnicoleoutingcorruptionsharecum

screen basementnicoleoutingcorruptionsharecum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionsharecum'), Jump('basementnicoleoutingcorruptionsharecuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionsharecum'), Jump('basementnicoleoutingcorruptionshareoutside')) hovered tt.Action ("Cum over her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionsharecuminside:
    if basement10pmnicoleoutingfuckass == True:
        pov "I'm cumming in your ass, slut."
    else:
        pov "I'm cumming in your pussy, slut."
    mom "Hmm..."
    pov "Ah, hnnn..."
    "You spurt your sperm inside her."
    pov "Oh, I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh, yeah, you're right, haha."
    if basement10pmnicoleoutingfuckass == True:
        scene livingroom 10pm 072ia
    else:
        scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, slut?"
    mom "Yes, [pov]. I love it when you put your sperm inside me."
    pov "Good slut!"
    scene livingroom 10pm 072sof
    davide "Yes, very good. She did manage to miss a little sperm on this end though."
    pov "Maybe something we need to train more, haha."
    davide "Oh she did fine already. You're a lucky bastard with this slut as your personal cum-dumpster, haha."
    jump basementnicoleoutingcorruptionshareend

label basementnicoleoutingcorruptionshareoutside:
    pov "I'm cumming on your ass, slut."
    mom "Hmm..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    "You spray your sperm over her ass."
    pov "Oh, I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh, yes, you're right, haha."
    scene livingroom 10pm 072o
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, slut?"
    mom "Yes, [pov]. I love it when you cover me with your sperm."
    pov "Good slut!"
    scene livingroom 10pm 072sof
    davide "Yes, very good. She did manage to miss a little sperm on this end though."
    pov "Maybe something we need to train more, haha."
    davide "Oh she did fine already. You're a lucky bastard with this slut as your personal cum-dumpster, haha."
    jump basementnicoleoutingcorruptionshareend

label basementnicoleoutingcorruptionshareend:
    scene livingroom 10pm 062b
    davide "I'm going to go now. Maybe I'll have some drinks and find Bruce, give him some more shit! Haha."
    davide "Be sure to have plenty of fun with your slut, [pov]."
    pov "I'm done. I came twice and she had fun too."
    pov "The best part is showing Bruce his place, finally."
    davide "Haha, yes."
    pov "You did good slut. Look forward to more fun."
    mom "Yes..."
    scene black
    "You leave the basement and go to bed."
    $ basement10pmnicoleouting = True
    $ basement10pmnicoleoutingfuckass = False
    $ basement10pmnicoleoutingcumface = False
    jump skip

label basementnicoleoutingcorruptionshareno:
    pov "Sorry Davide, but I don't think so."
    pov "My slut needs to get used to my dick on it's own."
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 061ai
    else:
        scene livingroom 10pm 061ao
    davide "Oh, you're serious."
    pov "Yes, I am."
    davide "Okay. Normally I would just take what I want, but I can appreciate how you handled Bruce..."
    davide "So you can have your fun with her alone."
    scene livingroom 10pm 062b
    davide "I'm going to go now. Maybe I'll have some drinks and find Bruce, give him some more shit! Haha."
    davide "Be sure to have plenty of fun with your slut, [pov]."
    pov "Oh yes, I will!"
    scene livingroom 10pm 065a
    pov "Oh you get yourself ready to get fucked."
    mom "Yes, please fuck me [pov]."
    if inc == True:
        pov "You have no idea how horny you make me, asking me to fuck you, mom."
    else:
        pov "You have no idea how horny you make me, asking me to fuck you, [mother]."
    pov "Presenting me your ass like that."
    mom "Hmm..."
    scene livingroom 10pm 066
    pov "It's time to pick a hole. Which one do you prefer?"
    mom "My opinion doesn't matter, I'm just your slut."
    pov "Oh I see. You're starting to like your submissive role."
    if inc == True:
        pov "That's good. I dreamt of making you my slut for a while now, mom."
    else:
        pov "That's good. I dreamt of making you my slut for a while now, [mother]."
    mom "Hmm..."
    povi "So, which hole should I use now?"
    call screen basementnicoleoutingcorruptionsharenochoose

screen basementnicoleoutingcorruptionsharenochoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionsharenochoose'), Jump('basementnicoleoutingcorruptionsharenochooseass')) hovered tt.Action ("Fuck her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionsharenochoose'), Jump('basementnicoleoutingcorruptionsharenochoosepussy')) hovered tt.Action ("Fuck her pussy") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionsharenochooseass:
    $ basement10pmnicoleoutingfuckass = True
    pov "I need to fuck your ass now, slut! Get ready."
    jump basementnicoleoutingcorruptionsharenochoosepussy

label basementnicoleoutingcorruptionsharenochoosepussy:
    if basement10pmnicoleoutingfuckass == False:
        pov "I need to fuck your pussy now, slut! Get ready."
    mom "Hmm... yes please fuck me."
    scene livingroom 10pm 067
    pov "God I love seeing my cock so close to your wet dripping hole."
    pov "And it's all mine now, Bruce can't disturb us anymore."
    mom "Hnng..."
    pov "You can't wait any longer can you, slut?"
    mom "Please stick it in, [pov]."
    if inc == True:
        pov "As you wish, slutty mom."
    else:
        pov "As you wish, slutty [mother]."
    scene livingroom 10pm 070
    mom "AAAAHNN..."
    pov "All in!"
    pov "That view is so hot, I could fuck you everyday. Maybe I will fuck you everyday."
    pov "Would you like to get fucked everyday by me, slut?"
    mom "Hmm... hah..."
    povi "Hmm... she doesn't seem to be as eager as she was before. I think I know the reason."
    scene livingroom 10pm 068
    pov "I think you were playing be before... Pretending to be the slut I wanted so I would stop talking about Bruce."
    mom "No... you're wrong... hah..."
    pov "You picked that loser to become your husband and now you're angry because you saw how much lower he got."
    pov "Losing you to me without fighting."
    mom "Hnng... I... Mmm..."
    pov "You've finally realized that how wrong you were about him."
    if inc == True:
        pov "Your own son is a better husband for you."
    else:
        pov "The son of your best friend is a better husband for you."
    mom "Hnn... Please... don't... huh... stop."
    pov "And you know I'm the only one who has the balls to end this farce and bring our normal life back."
    pov "But this time without Bruce!"
    with vpunch
    mom "Hnng!"
    "You punctuate your words with deep hard thrusts inside her."
    pov "And you'll be my slut forever!"
    with vpunch
    mom "Hnn... Hmm..."
    pov "You don't want to stop being my slut when this is over right?"
    with vpunch
    mom "No... Hnng..."
    if inc == True:
        pov "No, you're my slut for life now and we'll have so much sex together, mom!"
    else:
        pov "No, you're my slut for life now and we'll have so much sex together, [mother]!"
    with vpunch
    mom "Hnn... hah... ahhh..."
    povi "Wow, she's gotten way tight inside and is shaking. Seems like she liked the idea."
    pov "Are you going to orgasm, slut?"
    mom "Yes, [pov]. Yes, YES! HAAHH, [pov]!"
    pov "Damn..."
    povi "Me too..."
    call screen basementnicoleoutingcorruptionsharenocumchoose

screen basementnicoleoutingcorruptionsharenocumchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionsharenocumchoose'), Jump('basementnicoleoutingcorruptionsharenocuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorruptionsharenocumchoose'), Jump('basementnicoleoutingcorruptionsharenocumoutside')) hovered tt.Action ("Cum over her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionsharenocuminside:
    if basement10pmnicoleoutingfuckass == True:
        pov "I'll cum in your ass, slut."
        mom "Hmm... fill my ass!"
    else:
        pov "I'll cum in your pussy, slut."
        mom "Hmm... fill my pussy!"
    pov "Ah, hnnn..."
    "You spurt your cum deep inside her."
    if basement10pmnicoleoutingfuckass == True:
        scene livingroom 10pm 072ia
    else:
        scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, slut?"
    mom "Yes, [pov]. I love it when you put your sperm inside me."
    if inc == True:
        pov "I do too, mom."
    else:
        pov "I do too, [mother]."
    mom "Hnn..."
    $ basement10pmnicoleoutingfuckass = False
    jump basementnicoleoutingcorruptionsharenoend

label basementnicoleoutingcorruptionsharenocumoutside:
    pov "I'll cum on your ass, slut."
    mom "Hmm..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    "You spray your cum all over her ass."
    scene livingroom 10pm 072o
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, slut?"
    mom "Yes, [pov]. I love it when you cum on me."
    pov "I do too."
    $ basement10pmnicoleoutingfuckass = False
    jump basementnicoleoutingcorruptionsharenoend

label basementnicoleoutingcorruptionsharenoend:
    mom "Hah... hah... were you satisfied with me? Did I do good?"
    pov "Oh yes, I am. You did great."
    pov "I came twice and you had fun too."
    pov "But I'm beat, we'll continue our fun soon."
    mom "Hnng..."
    scene black
    "You leave the basement and go to bed."
    $ basement10pmnicoleouting = True
    $ basement10pmnicoleoutingfuckass = False
    $ basement10pmnicoleoutingcumface = False
    jump skip

#----- Outing Nicole to the Gang - Custom Cor to Love -----
label basementnicoleoutingcorlove: #----- Custom Cor to Love - Nicole Outing -----
    hide screen locations
    hide screen townl
    scene black
    "You decide it's time to introduce [mother] as your girl to the other gangmembers."
    scene basement 10pm 015c
    "You sit in the basement with the others, waiting for [mother] to get dressed."
    povi "This should go just like we planned. It's going to be tough on Bruce, but this is the best way given our situation."
    scene basement 10pm 017c
    povi "There she is. I can't get over that dress. So sexy."
    davide "God damn. Took you long enough. Are you going to bring us some drinks now?"
    mom "Yes."
    scene livingroom 10pm 040
    povi "That outfit is so amazing. Focus [pov]! You need to focus."
    davide "So what do you think about what we talked about earlier, Bruce?"
    dad "Huh? I'm not sure yet, sorry..."
    scene livingroom 10pm 041
    mom "The drinks are ready. Do you need anything else?"
    povi "Now it's time to show the others that she's mine. We play this right and she won't need to worry about Davide or the gang anymore."
    povi "I wonder how Bruce will react? We'll play off of Davide's disdain for him."
    povi "I get he's going to go fucking ballistic with me stealing his wife like this. But he won't do anything. Davide won't let Bruce mess with someone higher in the gang than he is."
    if inc == True:
        povi "I wonder if they'll be shocked seeing what I do with my mom?"
    povi "Well, here we go."
    pov "I need some service, slut!"
    scene livingroom 10pm 042a
    mom "Huh?"
    dad "What did you say?"
    davide "Hmm?"
    pov "I was told every gang member should make some bitch his personal girl, so I made her my slut!"
    dad "W-What...?"
    pov "[mother] stop standing around with that confused look on your face and service me!"
    "You pull your dick out."
    scene livingroom 10pm 043a
    pov "Or have you already forgotten you're promise to submit to me?"
    povi "I feel like an ass, treating her like this, but I think this going to work."
    mom "Hnng..."
    dad "How dare you... You can't be serious?"
    davide "Haha, this is so fuckin' great! You surprise me everytime, [pov]!"
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    scene livingroom 10pm 044a
    pov "Be a good slut and get on your knees! You have work to do."
    mom "Hnn..."
    dad "Stop this madness! [pov]!"
    davide "Shut the fuck up! I want to see if she'll really do it."
    scene livingroom 10pm 045a
    mom "You really want me to do this?"
    povi "Wow, either she's a great actor or she's having second thoughts. I better just keep going."
    if inc == True:
        pov "You decided to become my slut, mom! You're the one that wants this."
    else:
        pov "You decided to become my slut, [mother]! You're the one that wants this."
    pov "You don't want disappointed me now, so go on and suck on the dick you've chosen!"
    dad "No... no..."
    if NTR == True and momrelationship <= 5:
        jump basementnicoleoutingcorloveNTR
    else:
        jump basementnicoleoutingcorlove5

label basementnicoleoutingcorlove5: #----- Custom Cor to Love - Nicole Outing -----
    scene livingroom 10pm 046a
    pov "Good slut!"
    mom "<suck>"
    dad "This can't be... No!"
    davide "Hahahaha... you're the man [pov]!"
    scene livingroom 10pm 047a
    dad "I'll kill you!"
    povi "I would want to kill me too. But you put her in this position. And I'm the only one willing to do what it takes to get her out if it."
    davide "You'll do NOTHING bitch! You know the rules! I'll break your bones if you pull this shit!"
    dad "But she's my wife!"
    if inc == True:
        dad "And his mother!"
        povi "She sucked hard when he said that..."
    davide "That doesn't matter. He's made his choice. I can understand his decision, haha. And you're going to respect it too."
    pov "Just accept it. You lost! She's mine now."
    dad "What are you..."
    davide "Haha, he's right, Bruce. She's no longer yours now, hahaha."
    scene livingroom 10pm 048a
    povi "She's trembling, but she stuck with it. There is no way to turning back for us now."
    mom "<suck> <lick>"
    povi "Probably want to reinforce her with some praise. I want her to know this was the right choice."
    povi "We're going to get through this. We just need to make clear that you're mine in their eyes."
    pov "You're doing very good, slut. Your hot lips on my dick is just the thing I needed!"
    call screen basementnicoleoutingcorlovebj

screen basementnicoleoutingcorlovebj(): #----- Custom Cor to Love - Nicole Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovebj'), Jump('basementnicoleoutingcorlovebjnormal')) hovered tt.Action ("Let her continue") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovebj'), Jump('basementnicoleoutingcorlovebjdt')) hovered tt.Action ("Help her (deepthroat)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorlovebjnormal: #----- Custom Cor to Love - Nicole Outing -----
    povi "I think this is really working. I'll let her finish up and we'll go from there."
    $ mombasementcoroutingbjnormal = True
    jump basementnicoleoutingcorlovebjdt

label basementnicoleoutingcorlovebjdt: #----- Custom Cor to Love - Nicole Outing -----
    povi "I don't know if Davide is buying it completely. He appreciates aggressive actions. Let's see if this helps convince him."
    if mombasementcoroutingbjnormal == False:
        pov "Let me help you!"
        scene livingroom 10pm 048adt
        mom "Hnng..."
        povi "She's gagging but not fighting back. That's good. She's not being hurt hopefully."
    scene livingroom 10pm 047a
    dad "You must be blackmailing her. She won't never do something like this of her own free will."
    davide "Calm down! You've lost, he's the winner. It doesn't matter how she became his slut!"
    dad "But..."
    davide "NO! You're going to shut the fuck up now! For real this time!"
    "You almost form the word \"Sorry\" to Bruce, but realize it's not going to help the situation."
    scene livingroom 10pm 047aa
    davide "But we have another problem to solve now, haha."
    pov "Oh yeah, what is that?"
    povi "Shit, what is he worried about now?"
    davide "Bruce doesn't have a girl anymore and every gang member should have one. Even the shitty ones."
    pov "So we need to pick a girl for Bruce, since his wife is mine now?"
    davide "Exactly! We'll pick a suitable girl for him so he won't lose her again, hahaha."
    povi "Perfect, he's accepting that [mother] is mine now. This is going to work!"
    dad "Please, Davide..."
    davide "Shut up!"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 048adt
    else:
        scene livingroom 10pm 048a
    pov "Seems like you made the right decision to give in to me!"
    mom "Hmm..."
    dad "Shut the... grrr..."
    scene livingroom 10pm 047aaa
    davide "So any thoughts on which bitch would be a good fit for this loser? Maybe [miranda], she has very low standards, haha!"
    povi "Oh, [mother] is squeezing me hard. She doesn't want her to be Bruce's new girl. She really hates her..."
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 049adt
    else:
        scene livingroom 10pm 049a
    pov "Relax, slut. No one's made any decisions yet. And even if I decide she's the one then you'll accept it, because you know your place! Right?"
    povi "Sorry, but we need to do something to make Bruce accept this. It might be enough to let him fuck his crush."
    if mombasementcoroutingbjnormal == False:
        mom "Hmm...!"
    else:
        mom "Yes..."
    scene livingroom 10pm 047aaa
    davide "Can you think of anyone else?"
    pov "Hmm... a girl with low standards..."
    dad "You can't be serious..."
    pov "What's with that girl I delivered the packages to for you? The one in the subway."
    if rubyfirstmeet == False:
        scene town subway ruby
        "What's her name?"
        $ rubyname = renpy.input(_("Her name is...")) or _("Ruby")
        $ rubyname = rubyname.strip()
        if rubyname == "":
            $ lsname = "Ruby"
        $ rubyfirstmeet = True #----- added -----
    scene livingroom 10pm 047aaaa
    davide "You mean [ruby]? Really? She's a junkie."
    davide "She's already half-dead and I don't want to know with how many other junkies she fucked."
    davide "Not to mention how many STDs she's got. Fuck... that would be some heavy shit..."
    pov "But that might just be the right choice for him, haha."
    povi "Sorry Bruce. I have to play this up big."
    dad "Please, [pov]..."
    povi "Oh man, he's begging me. That's just sad."
    povi "I could choose [miranda] to be his girl. She's already a slut. But [mother] hates her, so she might be angry at me for choosing her."
    povi "But on the other hand, it could spice things up if I decide to have [miranda] and [mother] have fun together..."
    povi "Or should I choose the subway girl, [ruby]? I mean any port in a storm, right?"
    povi "But he could get ill or an STD. I'm fairly certain that would break him completely."
    povi "Or maybe he shouldn't be allowed to have any girl. That would be some motivation to end this crap quickly."
    povi "But might push him over the edge and he could do something stupid, like raping someone."
    povi "What should I do?"
    call screen basementnicoleoutingcorlovebruce

screen basementnicoleoutingcorlovebruce(): #----- Custom Cor to Love - Nicole Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovebruce'), Jump('basementnicoleoutingcorlovebrucemiranda')) hovered tt.Action ("He can have [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovebruce'), Jump('basementnicoleoutingcorlovebruceruby')) hovered tt.Action ("He'll take [ruby]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovebruce'), Jump('basementnicoleoutingcorlovebrucenone')) hovered tt.Action ("No girl for you!") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorlovebruceruby: #----- Custom Cor to Love - Nicole Outing -----
    pov "He can have [ruby]. But only [ruby]!"
    povi "He was just so hurt. I can't leave him with nothing."
    scene livingroom 10pm 047aaa
    dad "You can't be serious!"
    davide "Haha, I like that. You're a cruel boy. So be it. You should be happy Bruce. At least you can fuck someone, haha."
    pov "I mean you don't have to fuck her if you don't want to. But then it's just your hand to keep you company."
    dad "But why?"
    pov "Because I can. Oh, one other thing. Unless you clean that girl up..."
    pov "She isn't allowed to enter the house. I don't want my slut getting ill."
    povi "Wow, now she's really sucking hard. Is that her way of agreeing with my decision?"
    $ dadandruby = True
    jump basementnicoleoutingcorlove2

label basementnicoleoutingcorlovebrucemiranda: #----- Custom Cor to Love - Nicole Outing -----
    pov "He can have some fun with [miranda] too."
    povi "He was just so hurt. I can't leave him with nothing."
    scene livingroom 10pm 047aaa
    dad "Too?"
    pov "Yes, you can get some relief from her, but she'll be free for others to have fun with too."
    davide "Ha, a wise decision. And that works out for Bruce, since he has a crush on that slut too."
    mom "Hnn...!"
    pov "Oh, someone isn't pleased with my decision?"
    povi "Sorry, I know you hate her, but he looks like he was about to do something studid. I had to give him something, but I don't want him getting too confortable..."
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 049adt
    else:
        scene livingroom 10pm 049a
    pov "I know you hate her, but you're going accept my decision, slut. Right?"
    mom "Hmm..."
    pov "Good!"
    $ dadandmiranda = True
    jump basementnicoleoutingcorlove2

label basementnicoleoutingcorlovebrucenone: #----- Custom Cor to Love - Nicole Outing -----
    pov "He's not allowed to have any girl!"
    povi "I'm going to push him hard. Get him to end this situation soon."
    scene livingroom 10pm 047aaa
    dad "What?"
    davide "Haha, you can't be serious."
    pov "Oh yes, I am. He's so weak and he makes me angry just looking at him."
    dad "But why?"
    pov "Because I said so. You're a loser and until you so something to deserve it, no pussy for you!"
    davide "Haha, I like that. You're cruel boy. So be it."
    dad "But..."
    $ dadalone = True
    jump basementnicoleoutingcorlove2

label basementnicoleoutingcorlove2: #----- Custom Cor to Love - Nicole Outing -----
    povi "Oh god, I can't ignore [mother]'s sucking anymore."
    pov "Oh yes, I'm close slut!"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 049adt
    else:
        scene livingroom 10pm 049a
    povi "I need to cum..."
    call screen basementnicoleoutingcorlovebjcum

screen basementnicoleoutingcorlovebjcum(): #----- Custom Cor to Love - Nicole Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovebjcum'), Jump('basementnicoleoutingcorlovebjcumout')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovebjcum'), Jump('basementnicoleoutingcorlovebjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorlovebjcumout: #----- Custom Cor to Love - Nicole Outing -----
    pov "I'm going to cover you face. Get ready slut!"
    mom "Hmm..."
    scene livingroom 10pm 050o
    pov "Ohhh... yes!"
    "You come all over her face."
    scene livingroom 10pm 051o
    mom "Hnn... are you satisfied? Did I do a good job?"
    povi "Oh, this is something new. I was just trying to make it good for Davide, but she's really gotten into the role."
    pov "Yes, you did a good job, slut!"
    $ basement10pmnicoleoutingcumface = True
    jump basementnicoleoutingcorlove3

label basementnicoleoutingcorlovebjcumin: #----- Custom Cor to Love - Nicole Outing -----
    pov "I'm going to cum in your mouth. Get ready slut!"
    mom "Hmm..."
    scene livingroom 10pm 048a
    pov "Ohhh... yes!"
    "You come in her mouth."
    scene livingroom 10pm 051i
    mom "Hmm..."
    povi "Oh, this is something new. I was just trying to make it good for Davide, but she's really gotten into the role."
    pov "You can swallow it now!"
    scene livingroom 10pm 052i
    mom "<gulp> <gulp>"
    davide "Damn, you've tamed her already, haha."
    scene livingroom 10pm 053i
    mom "Aahhh..."
    pov "Yes, you did good. Swallowing it all like the hot slut you are!"
    jump basementnicoleoutingcorlove3

label basementnicoleoutingcorlove3: #----- Custom Cor to Love - Nicole Outing -----
    pov "Now go and sit on the couch with Bruce, so he can see what he lost, haha."
    davide "Hahaha, this is getting even better."
    povi "Davide is eating this up. Just one more push."
    mom "Yes, [pov]."
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 054i
    else:
        scene livingroom 10pm 054o
    dad "What's gotten into you?"
    if inc == True:
        dad "He's your son and you want to be his slut? What the fuck is wrong with you?"
    else:
        dad "He's the son of your best friend and you want to be his slut? What the fuck is wrong with you?"
    mom "Hnn..."
    dad "That's not you! Did he blackmail you?"
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 055i
    else:
        scene livingroom 10pm 055o
    davide "That's enough! We made a decision and you're going to accept it!"
    dad "But it's not fair!"
    davide "Fuck fair! I don't care, it's her decision! And I'm not going to allow some low ranked bitch to rant and rave in front of his superiors!"
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 056i
    else:
        scene livingroom 10pm 056o
    dad "So you really want to break all the taboos and be with him?"
    dad "You have no idea how disappointed I am. But you're safe, I'm not going to risk all we did..."
    povi "Shit Bruce! You do realize Davide it right here! Why not just tell him you're a cop why don't you?!"
    dad "YOU DAMN SLUT!"
    povi "I better shut him down quick!"
    scene livingroom 10pm 057
    pov "STOP!"
    dad "Huh?"
    pov "This is going to stop now and you're going behave like a god damned man with some dignity! I know what you are Bruce! Don't forget it!"
    povi "I'm not going to say anything, it could put the girls in danger, but maybe I can get him to calm the down."
    "You give him a knowing glance and he shuts up for moment."
    dad "..."
    pov "So, not that you understand, just don't forget... you're not allowed to touch your wife anymore."
    pov "She's mine now and I warn you, press me on the issue and you're regret it!"
    dad "..."
    dad "Fuck you!"
    scene livingroom 10pm 058
    dad "I'm out of here!"
    davide "Hahaha, what a great show!"
    davide "Let him go, he'll calm down. He's weak, haha."
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 059i
    else:
        scene livingroom 10pm 059o
    if inc == True:
        pov "What's wrong mom? You're all mine now slut, aren't you happy?"
    else:
        pov "What's wrong [mother]? You're all mine now slut, aren't you happy?"
    povi "I know this was rough, but it worked. He sees you as mine now. We can get free of him."
    mom "Hnn..."
    pov "Oh I see, you need a dick!"
    povi "When Davide leaves we can end this for tonight and regroup."
    mom "..."
    davide "Or maybe two?"
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 060ai
    else:
        scene livingroom 10pm 060ao
    povi "Is he serious? He wants me to share her?"
    davide "<grin>"
    pov "..."
    call screen basementnicoleoutingcorloveshare

screen basementnicoleoutingcorloveshare(): #----- Custom Cor to Love - Nicole Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorloveshare'), Jump('basementnicoleoutingcorloveshareyes')) hovered tt.Action ("Share her with Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorloveshare'), Jump('basementnicoleoutingcorloveshareno')) hovered tt.Action ("Don't share her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorloveshareyes: #----- Custom Cor to Love - Nicole Outing -----
    povi "God damn it, he's got to be testing me. Seeing if I'll let him play with her still. He is still the leader... for now."
    pov "Yeah, I guess you're right. Two dicks are better then one!"
    davide "Great. You hear that [mother]? You're going to serve me too."
    pov "Get in position, slut, so we can start."
    povi "I'm sorry."
    mom "Yes, hnn..."
    povi "She doesn't seem to happy about being shared, but I think she understands we need to convince him more still."
    scene livingroom 10pm 065as
    davide "Hell yes! This will be so much fun. Two alphas spliting a slut!"
    pov "Haha, you sound like you never had that before."
    davide "Do you see any other Alpha's here? You think that weak loser Bruce is an Alpha? Fuck no!"
    pov "Then let's enjoy her!"
    povi "I'll position myself behind so he'll have to settle for a blow-job."
    scene livingroom 10pm 066s
    davide "Be proud slut. Now you can suck my dick."
    povi "Good, it worked."
    $ basement10pmnicoleoutingshare = True
    call screen basementnicoleoutingcorlovesharechoose

screen basementnicoleoutingcorlovesharechoose(): #----- Custom Cor to Love - Nicole Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovesharechoose'), Jump('basementnicoleoutingcorlovesharepussy')) hovered tt.Action ("Fuck her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovesharechoose'), Jump('basementnicoleoutingcorloveshareass')) hovered tt.Action ("Fuck her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorloveshareass: #----- Custom Cor to Love - Nicole Outing -----
    $ basement10pmnicoleoutingfuckass = True
    pov "I'll give you a good fuck in your ass now, slut! Get ready."
    jump basementnicoleoutingcorlovesharepussy

label basementnicoleoutingcorlovesharepussy: #----- Custom Cor to Love - Nicole Outing -----
    if basement10pmnicoleoutingfuckass == False:
        pov "I'll give you a good fuck in your pussy now, slut! Get ready."
    davide "Two dicks, you must be in heaven."
    povi "Shut up Davide."
    mom "Hnn..."
    povi "She's still not very pleased about this. Me niether, but we need to keep him happy so he doesn't  things."
    pov "Show us some more appreciation, slut! I gave Davide permission to join us so he should have a good time too!"
    mom "Yes, you're right [pov]. I'm sorry Davide. Please use my mouth."
    davide "Oh, I will. Here, have a taste."
    scene livingroom 10pm 068s
    mom "Hmm... <lick>"
    davide "Oh yes, that tongue is amazing. You'll have so much fun with this mouth, [pov]."
    povi "I'm sorry [mother]. Please endure it just a bit longer. We'll be free of him soon enough."
    pov "Now it's time you get your second dick, slut."
    scene livingroom 10pm 067
    povi "I can't help it, but her ass is so sexy."
    if inc == True:
        povi "I'd have to be out of my mind not be turned on by my mother presenting herself to me like this."
    else:
        povi "I'd have to be out of my mind not be turned on by [mother] presenting herself to me like this."
    povi "She's trembling, waiting for my move. But I need to know how much she wants it."
    davide "What are you waiting for, [pov]."
    povi "Davide appreciates power plays. I know what do to push this more in our favor."
    pov "My slut didn't beg for my dick, yet."
    davide "Hahaha, you're serious?"
    if basement10pmnicoleoutingfuckass == True:
        mom "Please [pov]. Please stick your hard dick in my tight asshole."
    else:
        mom "Please [pov]. Please stick your hard dick in my wet pussy."
    povi "Holy shit, she must have picked up on what I was doing... Or maybe she just really want's it."
    davide "Damn, bro!"
    pov "Much better!"
    scene livingroom 10pm 070
    mom "Aaahnn..."
    pov "All in!"
    scene livingroom 10pm 070s
    davide "Yes, suck on my cock."
    mom "<suck> <lick>"
    povi "This is going to work. Hopefully this will be the last time I have to \"share\" her, but if we control the encounters, that is at least progress."
    povi "Then we can focus on getting this all to end."
    if basement10pmnicoleoutingfuckass == True:
        pov "Your tight asshole is like heaven, slut."
    else:
        pov "Your wet pussy is like heaven, slut."
    davide "Her mouth is also fucking great, haha."
    scene livingroom 10pm 071s
    davide "Perfect, she's working on my dick so eagerly since you've stuffed so good, haha."
    pov "Yes, she's doing well. And my slut will learn that serving more than one dick is a good thing, haha."
    davide "So this mouth will taste my dick again?"
    pov "We'll see."
    mom "Hnn... hnn..."
    davide "Oh, your slut likes the idea too."
    pov "Yes, haha."
    povi "She doesn't. Let him imagine it though, it works in our favor."
    davide "I need to finish soon, her mouth is too good."
    pov "Me too."
    scene livingroom 10pm 069s
    davide "Get it deep now, ha."
    mom "Hnn..."
    davide "I really appreciate this bro. It was a good decision to bring you into the fold."
    davide "You're going to do great things in the future."
    pov "Well, we'll see, haha."
    davide "Oh yes, I'm cumming, slut!"
    davide "Haaa, haaa...!"
    mom "Hmm..."
    pov "Damn, I'm so close too. She's gotten so clingy!"
    scene livingroom 10pm 070
    call screen basementnicoleoutingcorlovesharecum

screen basementnicoleoutingcorlovesharecum(): #----- Custom Cor to Love - Nicole Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovesharecum'), Jump('basementnicoleoutingcorlovesharecuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovesharecum'), Jump('basementnicoleoutingcorloveshareoutside')) hovered tt.Action ("Cum over her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorlovesharecuminside: #----- Custom Cor to Love - Nicole Outing -----
    if basement10pmnicoleoutingfuckass == True:
        pov "I'm cumming in your ass, slut."
    else:
        pov "I'm cumming in your pussy, slut."
    mom "Hmm..."
    pov "Ah, hnnn..."
    "You spurt your sperm inside her."
    pov "Oh, I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh, yeah, you're right, haha."
    if basement10pmnicoleoutingfuckass == True:
        scene livingroom 10pm 072ia
    else:
        scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, slut?"
    mom "Yes, [pov]. I love it when you put your sperm inside me."
    pov "Good slut!"
    scene livingroom 10pm 072sof
    davide "Yes, very good. She did manage to miss a little sperm on this end though."
    pov "Maybe something we need to train more, haha."
    povi "Fat chance of that, just got to keep him on the line."
    davide "Oh she did fine already. You're a lucky bastard with this slut as your personal cum-dumpster, haha."
    jump basementnicoleoutingcorloveshareend

label basementnicoleoutingcorloveshareoutside: #----- Custom Cor to Love - Nicole Outing -----
    pov "I'm cumming on your ass, slut."
    mom "Hmm..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    "You spray your sperm over her ass."
    pov "Oh, I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh, yes, you're right, haha."
    scene livingroom 10pm 072o
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, slut?"
    mom "Yes, [pov]. I love it when you cover me with your sperm."
    pov "Good slut!"
    scene livingroom 10pm 072sof
    davide "Yes, very good. She did manage to miss a little sperm on this end though."
    pov "Maybe something we need to train more, haha."
    povi "Fat chance of that, just got to keep him on the line."
    davide "Oh she did fine already. You're a lucky bastard with this slut as your personal cum-dumpster, haha."
    jump basementnicoleoutingcorloveshareend

label basementnicoleoutingcorloveshareend: #----- Custom Cor to Love - Nicole Outing -----
    scene livingroom 10pm 062b
    davide "I'm going to go now. Maybe I'll have some drinks and find Bruce, give him some more shit! Haha."
    davide "Be sure to have plenty of fun with your slut, [pov]."
    pov "I'm done. I came twice and she had fun too."
    pov "The best part is showing Bruce his place, finally."
    davide "Haha, yes."
    pov "You did good slut. Look forward to more fun."
    mom "Yes..."
    pov "<whisper> I think it worked!"
    mom "<whisper> Me too. Thank you so much!"
    scene black
    "You two leave the basement and go to bed."
    $ basement10pmnicoleouting = True
    $ basement10pmnicoleoutingfuckass = False
    $ basement10pmnicoleoutingcumface = False
    jump skip

label basementnicoleoutingcorloveshareno: #----- Custom Cor to Love - Nicole Outing -----
    pov "Sorry Davide, but I don't think so."
    pov "My slut needs to get used to my dick on it's own."
    povi "I need to press the issue that she is mine. So he'll actually leave her alone."
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 061ai
    else:
        scene livingroom 10pm 061ao
    davide "Oh, you're serious."
    pov "Yes, I am."
    davide "Okay. Normally I would just take what I want, but I can appreciate how you handled Bruce..."
    davide "So you can have your fun with her alone."
    scene livingroom 10pm 062b
    davide "I'm going to go now. Maybe I'll have some drinks and find Bruce, give him some more shit! Haha."
    davide "Be sure to have plenty of fun with your slut, [pov]."
    pov "Oh yes, I will!"
    scene livingroom 10pm 065a
    pov "Ok, he's gone now. You can get up. We did it!"
    mom "Hmmm... I don't think I want to get up yet."
    pov "What do you mean?"
    if inc == True:
        mom "Please, fuck me son."
        pov "You have no idea how hot that is, asking me to fuck you, mom."
    else:
        mom "Please, fuck me [pov]."
        pov "You have no idea how how hot that is, asking me to fuck you, [mother]."
    mom "Why do you think I said it like that? <giggle>."
    pov "Presenting me your ass like that..."
    mom "Hmm... You like this don't you? Being in charge. Owning me."
    pov "Oh indeed I do!"
    scene livingroom 10pm 066
    pov "It's time to pick a hole. Which one do you prefer?"
    mom "My opinion doesn't matter, I'm just your slut."
    pov "Oh I see. You're starting to like your submissive role."
    if inc == True:
        pov "I've dreamt of making you my mine for a while now, mom."
    else:
        pov "I've dreamt of making you my mine for a while now, [mother]."
    mom "Hmm... Do it!"
    povi "So, which hole should I use now?"
    call screen basementnicoleoutingcorlovesharenochoose

screen basementnicoleoutingcorlovesharenochoose(): #----- Custom Cor to Love - Nicole Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovesharenochoose'), Jump('basementnicoleoutingcorlovesharenochooseass')) hovered tt.Action ("Fuck her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovesharenochoose'), Jump('basementnicoleoutingcorlovesharenochoosepussy')) hovered tt.Action ("Fuck her pussy") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorlovesharenochooseass: #----- Custom Cor to Love - Nicole Outing -----
    $ basement10pmnicoleoutingfuckass = True
    pov "I want to fuck your ass now! Get ready."
    jump basementnicoleoutingcorlovesharenochoosepussy

label basementnicoleoutingcorlovesharenochoosepussy: #----- Custom Cor to Love - Nicole Outing -----
    if basement10pmnicoleoutingfuckass == False:
        pov "I want to fuck your pussy now! Get ready."
    mom "Hmm... yes please fuck me."
    scene livingroom 10pm 067
    pov "God I love seeing my cock so close to your wet dripping hole."
    pov "And it's all mine now, Davide or Bruce can't disturb us anymore."
    mom "Hnng..."
    pov "You can't wait any longer can you?"
    mom "Please stick it in, [pov]."
    if inc == True:
        pov "As you wish, naughty mom."
    else:
        pov "As you wish, naughty [mother]."
    scene livingroom 10pm 070
    mom "AAAAHNN..."
    pov "All in!"
    pov "That view is so hot, I could do this everyday. Maybe we will do this everyday."
    if inc == True:
        pov "Would you like to get fucked everyday by me, mom?"
    else:
        pov "Would you like to get fucked everyday by me, [mother]?"
    mom "Hmm... hah..."
    povi "Hmm... she's squeezing even harder now. I'll take that as a yes."
    scene livingroom 10pm 068
    pov "I think you like that before... Humiliating Bruce like that."
    mom "No... you're wrong... hah..."
    pov "You picked that loser to become your husband and now you want to make him suffer."
    mom "Hnng... I... Mmm..."
    pov "it's ok. He never should have put you in that situtation in the first place."
    if inc == True:
        pov "Your own son is a better husband for you."
    else:
        pov "The son of your best friend is a better husband for you."
    mom "Hnn... Please... don't... huh... stop."
    pov "And you know I'm the only one who has the balls to end this farce and bring our normal life back."
    pov "But this time without Bruce!"
    with vpunch
    mom "Hnng!"
    "You punctuate your words with deep hard thrusts inside her."
    pov "And you'll be mine forever!"
    with vpunch
    mom "Hnn... Hmm..."
    pov "You don't want to stop being mine when this is over right?"
    with vpunch
    mom "No... Hnng..."
    if inc == True:
        pov "No, you're mine for life now and we'll have so much sex together, mom!"
    else:
        pov "No, you're mine for life now and we'll have so much sex together, [mother]!"
    with vpunch
    mom "Hnn... hah... ahhh..."
    povi "Wow, she's gotten way tight inside and is shaking. Seems like she really likes the idea."
    pov "Are you going to orgasm?"
    mom "Yes, [pov]. Yes, YES! HAAHH, [pov]!"
    povi "Me too..."
    call screen basementnicoleoutingcorlovesharenocumchoose

screen basementnicoleoutingcorlovesharenocumchoose(): #----- Custom Cor to Love - Nicole Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovesharenocumchoose'), Jump('basementnicoleoutingcorlovesharenocuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementnicoleoutingcorlovesharenocumchoose'), Jump('basementnicoleoutingcorlovesharenocumoutside')) hovered tt.Action ("Cum over her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingcorlovesharenocuminside: #----- Custom Cor to Love - Nicole Outing -----
    if basement10pmnicoleoutingfuckass == True:
        pov "I'm going to cum in your ass."
        mom "Please, fill my ass!"
    else:
        pov "I'm going to cum in your pussy."
        mom "Please, fill my pussy!"
    mom "Hmm..."
    pov "Ah, hnnn..."
    "You spurt your cum deep inside her."
    if basement10pmnicoleoutingfuckass == True:
        scene livingroom 10pm 072ia
    else:
        scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked that?"
    mom "Yes, [pov]. I love it when you cum inside me."
    if inc == True:
        pov "I do too, mom."
    else:
        pov "I do too, [mother]."
    mom "Hnn..."
    $ basement10pmnicoleoutingfuckass = False
    jump basementnicoleoutingcorlovesharenoend

label basementnicoleoutingcorlovesharenocumoutside: #----- Custom Cor to Love - Nicole Outing -----
    pov "I'm going to cum on your ass."
    mom "Hmm..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    "You spray your sperm over her ass."
    scene livingroom 10pm 072o
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked that?"
    mom "Yes, [pov]. I love it when you cover my body with your sperm."
    pov "And I love to mark you all over with it."
    $ basement10pmnicoleoutingfuckass = False
    jump basementnicoleoutingcorlovesharenoend

label basementnicoleoutingcorlovesharenoend: #----- Custom Cor to Love - Nicole Outing -----
    mom "Hah... hah... Do you really think it worked?"
    pov "Oh yes, I do."
    if inc == True:
        mom "I love you, [pov]."
    else:
        mom "I love you, son."
    pov "I love you too."
    scene black
    "You two leave the basement and go to bed."
    $ basement10pmnicoleouting = True
    $ basement10pmnicoleoutingfuckass = False
    $ basement10pmnicoleoutingcumface = False
    jump skip

#----- Outing Nicole to the Gang ----- Darker Paths -----
label basementnicoleoutingcorruptionNTR:
    call screen checkdarkerpaths_nicole
    davide "Hohoho, wait a second."
    pov "Hm...?"
    dad "Yes I told you it's wrong."
    scene livingroom 10pm 047aa
    davide "This isn't what I meant."
    davide "I'm the boss here so it would be only fine to let me test your slut first?"
    if nicole_voyeur == True:
        povi "Yeah, that's fine. Share and share alike right?"
    elif nicole_ntr == True:
        povi "Oh shit, he's serious. What should I do? I can't stop him!"
    elif nicole_revenge == True:
        povi "Oh shit, he's serious. God dammit! I thought we had this!"
    else: #----- Nicole_sadist -----
        povi "Oh shit, he's serious. I guess I can share. For now."
    davide "Come here slut, work on my dick first!"
    mom "Yes, Davide."
    dad "But I... I thought."
    davide "Shut up, loser!"
    scene basement 10pm 020c
    davide "You see this, Bruce. Your wife is now everybodys slut!"
    mom "<suck> <lick>"
    dad "Yes, Davide."
    davide "And you slut will swallow my spunk now and then you can go back to [pov]."
    mom "Yes, Davide."
    scene basement 10pm 021c
    davide "This is how it works! You can have your slut but you'll share her with me."
    if nicole_voyeur == True:
        povi "No problem! The more the merrier I say."
    elif nicole_ntr == True:
        povi "Damn... that asshole."
    elif nicole_revenge == True:
        povi "Shit. I'm going to kill this fucker after all!"
    else: #----- Nicole_sadist -----
        povi "I can deal with that. But I'm not going to be nice about it. I'll just take it out on her. Haha."
    pov "Yes, Davide."
    davide "Good. I'm close slut, swallow it all down."
    mom "<suck> yes..."
    davide "HNN, haha..."
    mom "<gulp> <gulp>"
    davide "Your slut has the best mouth, enjoy her like I did!"
    mom "T... thank you."
    jump basementnicoleoutingcorruption5

#----- Outing Nicole to the Gang - Darker Paths - Cor to Love -----
label basementnicoleoutingcorloveNTR:
    call screen checkdarkerpaths_nicole
    davide "Hohoho, wait a second."
    pov "Hm...?"
    dad "Yes I told you it's wrong."
    scene livingroom 10pm 047aa
    davide "This isn't what I meant."
    davide "I'm the boss here so it would be only fine to let me test your slut first?"
    if nicole_voyeur == True:
        povi "Yeah, that's fine. Share and share alike right?"
    elif nicole_ntr == True:
        povi "Oh shit, he's serious. What should I do? I can't stop him!"
    elif nicole_revenge == True:
        povi "Oh shit, he's serious. God dammit! I thought we had this!"
    else: #----- Nicole_sadist -----
        povi "Oh shit, he's serious. I guess I can share. For now."
    davide "Come here slut, work on my dick first!"
    mom "Yes, Davide."
    dad "But I... I thought."
    davide "Shut up, loser!"
    scene basement 10pm 020c
    davide "You see this, Bruce. Your wife is now everybodys slut!"
    mom "<suck> <lick>"
    dad "Yes, Davide."
    davide "And you slut will swallow my spunk now and then you can go back to [pov]."
    mom "Yes, Davide."
    scene basement 10pm 021c
    davide "This is how it works! You can have your slut but you'll share her with me."
    if nicole_voyeur == True:
        povi "No problem! The more the merrier I say."
    elif nicole_ntr == True:
        povi "Damn... that asshole."
    elif nicole_revenge == True:
        povi "Shit. I'm going to kill this fucker after all!"
    else: #----- Nicole_sadist -----
        povi "I can deal with that. But I'm not going to be nice about it. I'll just take it out on her. Haha."
    pov "Fine."
    povi "This isn't ideal, but it's progress. We'll get him in line soon."
    davide "Good. I'm close slut, swallow it all down."
    mom "<suck> yes..."
    davide "HNN, haha..."
    mom "<gulp> <gulp>"
    davide "Your slut has the best mouth, enjoy her like I did!"
    mom "T... thank you."
    jump basementnicoleoutingcorlove5

#----- Outing Cassandra to the Gang Landing -----
label basementcassandraoutingcorlovemenu:
    call screen basementcassandraoutingcorlovechoice

screen basementcassandraoutingcorlovechoice():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('basementcassandraoutingcorlovechoice'), Jump('basementcassandraoutingcorlove')) hovered tt.Action ("Love") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('basementcassandraoutingcorlovechoice'), Jump('basementcassandraoutingcorruption')) hovered tt.Action ("Corruption") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Outing Cassandra to the Gang -----
label basementcassandraoutingcorruption:
    hide screen locations
    hide screen townl
    scene black
    povi "It's time to let the other's know that [bs] is my slut."
    "You go down to the basement with [bs] and let her change before the others arrive."
    scene livingroom 10pm 079
    davide "So what's the damn important thing you want to show us today?"
    pov "It's something special that'll change things around here a bit."
    dad "I have a bad feeling."
    mom "I don't think you need to be worried. I'm sure whatever [pov] has in mind is good."
    povi "Haha, yes, it's good for me at least."
    pov "Come out slut!"
    scene livingroom 10pm 080
    bs "Hello everyone."
    pov "You chose a very sexy outfit, slut."
    povi "And she's still eager about serving the drinks, haha."
    povi "I wonder when she'll realize it is only one of the many \"services\" she'll be providing?"
    scene livingroom 10pm 081
    dad "..."
    mom "..."
    davide "... hahahaha..."
    bs "Guys?"
    pov "I know she's hot, but you can calm down, haha."
    scene livingroom 10pm 082c
    dad "You can't be serious!"
    pov "Why not? She's just another slut for me."
    mom "But..."
    davide "Hmm?"
    povi "Haha, Davide is confused. Did I really do something new here? Having more than one slut?"
    scene livingroom 10pm 083c
    dad "How can you allow this? She's your daughter."
    povi "As expected. Weak little Bruce has to ask his wife to step in and fix things. But she can't help you, she's my slut too."
    dad "I've already accepted all the other humiliations, but this is going too far, don't you think?"
    mom "Hnn..."
    scene livingroom 10pm 084c
    mom "Why is she here? I thought I was your slut?"
    dad "Ehhh?"
    davide "Hehe... hahaha..."
    scene livingroom 10pm 085c
    bs "What's going on here?"
    scene livingroom 10pm 082c
    if inc == True:
        pov "You're still my slut, mom. And [bs] is my slut now as well."
    else:
        pov "You're still my slut, [mother]. And [bs] is my slut now as well."
    pov "I could get bored with just one slut, so I have two of you now."
    if inc == True:
        dad "But she's your sister!"
    else:
        dad "But she's my daughter!"
    pov "Yes, she is. That's just one of the many reasons I should be the one taking care of her."
    mom "But..."
    pov "No more of that [mother]! You'll share your slut-status with her now."
    scene livingroom 10pm 086c
    if inc == True:
        bs "Mom is your slut too?"
    else:
        bs "My mom is your slut too?"
    pov "Yes and you two are truly two of a kind when it comes to pleasing me!"
    pov "But now you'll each have to prove to me who truly is my best slut."
    povi "A little competition could be a lot of fun, haha."
    bs "Hnn..."
    pov "Now go on and show us what I taught you."
    bs "Yes, [pov]."
    scene livingroom 10pm 087c
    bs "See, it's easy."
    davide "Ehh?"
    dad "No..."
    povi "That look on Bruce's face! Priceless! Maybe the view is too good for him to handle."
    povi "Haha, Davide's face too! He's so confused about why she's acting like a waitress. I might have put too much emphasis on that part of our training earlier."
    povi "And I wonder why she's still acting like one. Is she nervous?"
    scene livingroom 10pm 088c
    if inc == True:
        bs "Did I do everything to your liking, brother?"
    else:
        bs "Did I do everything to your liking, [pov]?"
    pov "Yes, slut. You placed the tray on the table without spilling any of the drinks."
    bs "<giggle>"
    povi "Hahaha, they're all so damn confused. Time for the main event."
    pov "Something else comes to mind though. I wonder if the others know about your other decorations. The ones you wear under your dress?"
    pov "I think you should show them to us."
    mom "Decorations?"
    scene livingroom 10pm 089c
    bs "You mean...? I should show them to everyone?"
    pov "Yes! They are already almost visible, but I think we all should get a better look."
    dad "What does he mean, decorations?"
    pov "Do it slut! You know you want to..."
    bs "Yes [pov]."
    scene livingroom 10pm 090c
    bs "These are my decorations, hnn..."
    davide "Hell yes, those are some fine ass titties!"
    scene livingroom 10pm 091c
    dad "Aaahh..."
    davide "And what wonderful decorations you have!"
    mom "Hnn...!"
    pov "Don't stare, Bruce, hahaha..."
    jump basementcassandraoutingcorruptionshare

label basementcassandraoutingcorruptionshare:
    povi "Now it's time for even more fun. But who'll serve whom?"
    call screen basementcassandraoutingcorruptionsharechoose

screen basementcassandraoutingcorruptionsharechoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptionsharechoose'), Jump('basementcassandraoutingcorruptionsharecspov')) hovered tt.Action ("[bs] serve me, [mother] serve Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptionsharechoose'), Jump('basementcassandraoutingcorruptionsharenpov')) hovered tt.Action ("[mother] serve me, [bs] serve Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptionsharechoose'), Jump('basementcassandraoutingcorruptionsharecspovonly')) hovered tt.Action ("[bs] serve me, Davide get's nobody") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorruptionsharecspov:
    $ basement10cassandraoutingnshare = True
    povi "[bs] will serve me now and [mother] serve Davide, so he can have fun too."
    povi "That way he'll see that I'm accepting his higher position... for now."
    pov "Come here and get on your knees, [bs]! I need some service now!"
    scene livingroom 10pm 093ns
    bs "You mean... now?"
    pov "Yes, I know what I said. Get over here."
    bs "But... they'll still sitting there..."
    pov "I know. Now stop talking and do your duty. I told you that you'd have to do this in front of the others, so start sucking!"
    pov "Haha, and don't worry Davide, I'll see you have a little fun too."
    bs "O... OK, [pov]."
    scene livingroom 10pm 092cs
    bs "<suck> <lick>"
    pov "Good, I see that you know your place slut."
    pov "Now give it your best and just ignore the others. You need to learn to follow my orders without question."
    bs "Y... yes [pov]. <lick>"
    scene livingroom 10pm 094ns
    pov "And you'll serve Davide now, [mother]. It's rude to let him sit there alone."
    mom "Yes, of course [pov]."
    dad "Grr...."
    davide "Do not even think about to saying something, Bruce!"
    dad "..."
    scene livingroom 10pm 093cs
    bs "<lick> <lick>"
    pov "Your mouth is as great as ever, slut."
    if inc == True:
        bs "Thank you, brother."
    else:
        bs "Thank you, [pov]."
    pov "You'll learn fast how we do things here and there is no reason you can't have some fun too."
    bs "Hmm..."
    povi "Damn, this is working out perfectly."
    scene livingroom 10pm 095ns
    pov "And you're happy too?"
    davide "Look at me, crybaby!"
    povi "Oh, he's bullying Bruce again. Haha, poor Bruce."
    if inc == True:
        povi "Mom needs to learn that she's not my only slut and if she doesn't want to be shared with the other, she needs to do a better job of pleasing me."
    else:
        povi "[mother] needs to learn that she's not my only slut and if she doesn't want to be shared with the other, she needs to do a better job of pleasing me."
    scene livingroom 10pm 093cs
    if inc == True:
        pov "And you're giving your best too, right big sis?"
        bs "Yes, I try brother."
    else:
        pov "And you're giving your best too, right [bs]?"
        bs "Yes, I try [pov]."
    if casbjdt >= 2:
        bs "Do you want me to deepthroat you?"
        pov "Are you offering?"
        bs "Yes, do you want me to do it?"
        pov "What a nice slut you are, caring that much for me."
        call screen basementcassandraoutingcorruptioncasbj
    else:
        jump basementcassandraoutingcorruptioncasbjnormal

screen basementcassandraoutingcorruptioncasbj():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptioncasbj'), Jump('basementcassandraoutingcorruptioncasbjdt')) hovered tt.Action ("Deepthroat me") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptioncasbj'), Jump('basementcassandraoutingcorruptioncasbjnormal')) hovered tt.Action ("Give me a normal blowjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorruptioncasbjdt:
    pov "Yes, I want you to deepthroat me, slut."
    bs "Okay... [pov]."
    scene livingroom 10pm 095dtcs
    pov "Oh fuck, work your way down my cock."
    bs "Hnng... <suck> <choke>"
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 096ns
        davide "You have the best ideas [pov]. It seems that I've really underestimated you, haha."
        mom "<suck> <lick>"
        pov "So my other slut is doing a good job on you?"
        davide "Haha, you know how good her mouth is, so you know the answer."
    scene livingroom 10pm 095dtcs
    pov "You're doing very good, don't worry."
    if inc == True:
        pov "Not as good as mom, but you can get better, I'm sure."
    else:
        pov "Not as good as your mom, but you can get better, I'm sure."
    bs "Hmm... <suck>"
    pov "I think it's time you take me deeper, slut."
    bs "Hmm..."
    scene livingroom 10pm 096dtcs
    bs "<suck> <choke>"
    pov "Oh yes, very good."
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 097cns
        davide "Hah... yes, suck it slut!"
        dad "<sob>"
        povi "Oh poor Bruce is crying... What a fucking loser."
        davide "Swallow my spunk!"
        mom "Hnn... <gulp>"
        povi "Hmm, he already came, so [mother] won this round."
        povi "But [bs] isn't far behind. I'm getting close too."
    scene livingroom 10pm 096dtcs
    pov "I'm going to cum now slut."
    jump basementcassandraoutingcorruptioncasbjcum

label basementcassandraoutingcorruptioncasbjnormal:
    pov "While I appreciate the thought, I'd like you do just keep going for now, slut."
    bs "Okay... [pov]."
    scene livingroom 10pm 094cs
    bs "<suck> <lick>"
    pov "Oh yes, just like that."
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 096ns
        davide "You have the best ideas [pov]. It seems that I've really underestimated you, haha."
        mom "<suck> <lick>"
        pov "So my other slut is doing a good job on you?"
        davide "Haha, you know how good her mouth is, so you know the answer."
    pov "You're doing very good, don't worry."
    if inc == True:
        pov "Not as good as mom, but you can get better, I'm sure."
    else:
        pov "Not as good as your mom, but you can get better, I'm sure."
    bs "Hmm... <suck>"
    scene livingroom 10pm 095ics
    pov "Ohh, this is nice."
    povi "She teasing the tip, that's new for her."
    bs "Hnn... <lick>"
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 097cns
        davide "Hah... yes, suck it slut!"
        dad "<sob>"
        povi "Oh poor Bruce is crying... What a fucking loser."
        davide "Swallow my spunk!"
        mom "Hnn... <gulp>"
        povi "Hmm, he already came, so [mother] won this round."
        povi "But [bs] isn't far behind. I'm getting close too."
    scene livingroom 10pm 095ics
    pov "I'm going to cum now slut."
    jump basementcassandraoutingcorruptioncasbjcum

label basementcassandraoutingcorruptioncasbjcum:
    call screen basementcassandraoutingcorruptioncasbjcumchoose

screen basementcassandraoutingcorruptioncasbjcumchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptioncasbjcumchoose'), Jump('basementcassandraoutingcorruptioncasbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptioncasbjcumchoose'), Jump('basementcassandraoutingcorruptioncasbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorruptioncasbjcumin:
    pov "I'll cum in your mouth!"
    bs "Hmm..."
    pov "Aaahhh... yes..."
    "You spray your cum inside her mouth."
    bs "Hnn..."
    scene livingroom 10pm 096ics
    bs "Hnn..."
    povi "Damn, is she smiling?"
    pov "Good, slut, don't forget to swallow it all. It would be rude otherwise."
    bs "Yesh... <gulp>"
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 098cns
        davide "Look at her Bruce! She swallowed it all."
        mom "Hah... hah..."
        davide "You can be proud of your wife, haha."
        jump basementcassandraoutingcorruptionend
    else:
        jump basementcassandraoutingcorruptionend

label basementcassandraoutingcorruptioncasbjcumout:
    pov "I'll cum on your face!"
    bs "Hmm..."
    pov "Aaahhh... yes..."
    scene livingroom 10pm 095ocs
    "You spray your cum on her face."
    bs "Hnn..."
    scene livingroom 10pm 096ocs
    bs "You came so much on me... hnn..."
    pov "You should be proud. That shows you how much I appreciate what you were doing."
    bs "Hmm..."
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 098cns
        davide "Look at her Bruce! She swallowed it all."
        mom "Hah... hah..."
        davide "You can be proud of your wife, haha."
        jump basementcassandraoutingcorruptionend
    else:
        jump basementcassandraoutingcorruptionend

label basementcassandraoutingcorruptionend:
    scene black
    if basement10cassandraoutingnshare == True or basement10cassandraoutingcshare == True:
        "After you've all had your fun, except Bruce, you decide to call it a night and leave the basement."
    else:
        "After you've had your fun, you decide to call it a night and leave the basement."
    $ basement10cassandraouting = True
    $ basement10cassandraoutingnshare = False
    $ basement10cassandraoutingcshare = False
    jump skip

label basementcassandraoutingcorruptionsharenpov:
    $ basement10cassandraoutingcshare = True
    povi "[mother] will serve me now and [bs] can serve Davide, so he can have fun too."
    povi "That way he'll see that I'm accepting his higher position... for now."
    scene livingroom 10pm 092ns
    if inc == True:
        pov "Come here and get on your knees, mom! I need some service now!"
    else:
        pov "Come here and get on your knees, [mother]! I need some service now!"
    mom "Huh? Y-yes, [pov]..."
    povi "Haha, I wonder if Bruce will be able to keep his mouth closed this time?"
    scene livingroom 10pm 048a
    mom "<suck> <lick>"
    pov "Good, you know how to serve."
    bs "Huh?"
    scene livingroom 10pm 093ns
    if inc == True:
        bs "Mom is sucking on your dick?"
    else:
        bs "My mother is sucking on your dick?"
    pov "Yes, I haven chosen her to serve me tonight."
    povi "Haha, Davide can't wait."
    pov "And you'll serve Davide with your mouth."
    bs "D-Davide? But I thought..."
    pov "Stop! You're not here to think, you're here to serve."
    pov "So do what I told you to do and show me that you can be a good slut."
    bs "Hnn... yes [pov]."
    scene livingroom 10pm 094ncs
    bs "I'm sorry that I hesitated, Davide. I'll serve you good."
    davide "Oh yes, I'm sure you will. Especially a mouth like yours, haha."
    povi "That'll show her that she needs to give it her best to please me as a slut is she doesn't want to be shared with the others."
    dad "This needs to... stop..."
    davide "Shut up Bruce!"
    scene livingroom 10pm 048a
    pov "Are you're proud that I chose you to serve me?"
    mom "Hnn..."
    if inc == True:
        pov "You should be, mom! You and [bs] will serve me well and we'll keep everything in the family."
    else:
        pov "You should be, [mother]! You and [bs] will serve me well and we'll keep everything in the your family."
    mom "Hmm..."
    pov "I need to hear it from you."
    mom "I... I'm pround you'd chosen me, [pov]."
    pov "Good slut."
    povi "How should I let her continue? Should she get me off on her own or should I help her?"
    call screen basementcassandraoutingcorruptionnicbj

screen basementcassandraoutingcorruptionnicbj():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptionnicbj'), Jump('basementcassandraoutingcorruptionnicbjdt')) hovered tt.Action ("Help her (deethroat)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptionnicbj'), Jump('basementcassandraoutingcorruptionnicbjnormal')) hovered tt.Action ("Let her continue") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorruptionnicbjdt:
    pov "Let me help you, slut!"
    scene livingroom 10pm 048adt
    mom "Hnn... <suck> <choke>"
    pov "I need you to take me deep."
    scene livingroom 10pm 095ncs
    davide "Oh yes, that's how I like it. Make it wet before it goes deep in your mouth."
    davide "Look how good she can serve, Bruce!"
    dad "No... this is wrong..."
    povi "Oh, he's bullying Bruce again. Haha, poor Bruce."
    scene livingroom 10pm 048adt
    if inc == True:
        pov "You hear that slut? Everyone is happy with you and big sis serving us."
    else:
        pov "You hear that slut? Everyone is happy with you and your daughter serving us."
    mom "Hnn..."
    pov "Oh, so you're not convinced yet? You will be, soon."
    scene livingroom 10pm 096ncs
    davide "You have the best ideas [pov]. It seems that I've really underestimated you, haha."
    bs "<suck> <lick>"
    pov "So my other slut is doing a good job on you?"
    davide "Haha, you know how good her mouth is, so you know the answer."
    scene livingroom 10pm 048adt
    pov "You're doing very good, don't worry."
    mom "Hmm... <choke>"
    pov "I think it's time you take me deeper, slut."
    mom "Hmm..."
    scene livingroom 10pm 049adt
    mom "<suck> <choke>"
    pov "Oh yes, very good."
    scene livingroom 10pm 097ncs
    davide "Hah... yes, suck it slut!"
    dad "<sob>"
    povi "Oh poor Bruce is crying... What a fucking loser."
    davide "Swallow my spunk!"
    bs "Hnn... <gulp>"
    povi "Hmm, he already came, so [bs] did a good job."
    povi "But thinking of that, [mother] is getting me close too."
    scene livingroom 10pm 049adt
    pov "I'm going to cum now slut."
    call screen basementcassandraoutingcorruptionnicbjcum

label basementcassandraoutingcorruptionnicbjnormal:
    pov "Just continue what you're doing, slut."
    mom "Okay... [pov]."
    scene livingroom 10pm 095ncs
    davide "Oh yes, that's how I like it. Make it wet before it goes deep in your mouth."
    davide "Look how good she can serve, Bruce!"
    dad "No... this is wrong..."
    povi "Oh, he's bullying Bruce again. Haha, poor Bruce."
    scene livingroom 10pm 049a
    if inc == True:
        pov "You hear that slut? Everyone is happy with you and big sis serving us."
    else:
        pov "You hear that slut? Everyone is happy with you and your daughter serving us."
    mom "Hnn..."
    pov "Oh, so you're not convinced yet? You will be, soon."
    scene livingroom 10pm 096ncs
    davide "You have the best ideas [pov]. It seems that I've really underestimated you, haha."
    bs "<suck> <lick>"
    pov "So my other slut is doing a good job on you?"
    davide "Haha, you know how good her mouth is, so you know the answer."
    scene livingroom 10pm 049a
    pov "You're doing very good, don't worry."
    mom "Hmm... <lick>"
    scene livingroom 10pm 097ncs
    davide "Hah... yes, suck it slut!"
    dad "<sob>"
    povi "Oh poor Bruce is crying... He got even weaker."
    davide "Swallow my spunk!"
    bs "Hnn... <gulp>"
    povi "Hmm, he already came, so [bs] did a good job."
    povi "But thinking of that, [mother] is getting me close too."
    scene livingroom 10pm 048a
    pov "I'm going to cum now slut."
    call screen basementcassandraoutingcorruptionnicbjcum

screen basementcassandraoutingcorruptionnicbjcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptionnicbjcum'), Jump('basementcassandraoutingcorruptionnicbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorruptionnicbjcum'), Jump('basementcassandraoutingcorruptionnicbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorruptionnicbjcumin:
    pov "I'll cum in your mouth!"
    mom "Hmm..."
    pov "Aaahhh... yes..."
    "You spray your cum inside her mouth."
    mom "Hnn..."
    scene livingroom 10pm 051i
    mom "Hnn..."
    pov "Good, slut, don't forget to swallow all. It would be rude otherwise."
    mom "Yesh... <gulp>"
    scene livingroom 10pm 052i
    mom "<gulp> <gulp>"
    scene livingroom 10pm 053i
    mom "Haaah..."
    pov "Good slut."
    scene livingroom 10pm 098ncs
    davide "Look at her Bruce! She swallowed it all."
    bs "Hah... hah..."
    davide "You can be proud of your step-daughter, haha."
    davide "Even if I wished she was your real daughter."
    jump basementcassandraoutingcorruptionend

label basementcassandraoutingcorruptionnicbjcumout:
    pov "I'll cum on your face!"
    mom "Hmm..."
    pov "Aaahhh... yes..."
    scene livingroom 10pm 050o
    "You spray your cum all over her face."
    mom "Hnn..."
    scene livingroom 10pm 051o
    mom "You came so much on me... hnn..."
    pov "You should be proud. That shows you how much I appreciate what you were doing."
    mom "Hmm..."
    scene livingroom 10pm 098ncs
    davide "Look at her Bruce! She swallowed it all."
    bs "Hah... hah..."
    davide "You can be proud of your step-daughter, haha."
    davide "Even if I wished she was your real daughter."
    jump basementcassandraoutingcorruptionend

label basementcassandraoutingcorruptionsharecspovonly:
    povi "[bs] will serve me now and [mother] will have to watch."
    pov "Come here and get on your knees, [bs]! I need some service now!"
    scene livingroom 10pm 093ns
    bs "You mean... now?"
    pov "Yes, I know what I said. Get over here."
    bs "But... they'll still sitting there..."
    pov "I know. Now stop talking and do your duty. I told you that you'd have to do this in front of the others, so start sucking!"
    pov "I see you want to have fun too Davide, but I'm afriad I must disappoint you."
    pov "I need [mother] to pay close attention to this."
    davide "Hnnn, that make sense. You can have your way... this time..."
    povi "We'll see about that."
    bs "O... OK, [pov]."
    scene livingroom 10pm 092cs
    bs "<suck> <lick>"
    pov "Good, I see that you know your place slut."
    pov "Now give it your best and just ignore the others. You need to learn to follow my orders without question."
    bs "Y... yes [pov]. <lick>"
    scene livingroom 10pm 094ns
    pov "And make sure you watch closely and don't miss anything, [mother]."
    dad "You don't need to do this."
    davide "Shut up Bruce and enjoy the show!"
    mom "Y- yes [pov]."
    scene livingroom 10pm 093cs
    bs "<lick> <lick>"
    pov "Your mouth is as great as ever, slut."
    if inc == True:
        bs "Thank you, brother."
    else:
        bs "Thank you, [pov]."
    pov "You'll learn fast how we do things here and there is no reason you can't have some fun too."
    bs "Hmm..."
    povi "Damn, this is working out perfectly."
    scene livingroom 10pm 093cs
    if inc == True:
        pov "And you're giving your best too, right big sis?"
        bs "Yes, I try brother."
    else:
        pov "And you're giving your best too, right [bs]?"
        bs "Yes, I try [pov]."
    if casbjdt >= 2:
        bs "Do you want me to deepthroat you?"
        pov "Are you offering?"
        bs "Yes, do you want me to do it?"
        pov "What a nice slut you are, caring that much for me."
        call screen basementcassandraoutingcorruptioncasbj
    else:
        jump basementcassandraoutingcorruptioncasbjnormal

#----- Outing Cassandra to the Gang - Cor to Love -----
label basementcassandraoutingcorlove: #------ Custom - Cor to Love - Cassandra Outing -----
    hide screen locations
    hide screen townl
    scene black
    povi "It's time to let the other's know that [bs] is my girl."
    povi "It will be easier to be together if we don't have to hide it."
    "You go down to the basement with [bs] and let her change before the others arrive."
    scene livingroom 10pm 079
    davide "So what's the damn important thing you want to show us today?"
    pov "It's something special that'll change things around here a bit."
    dad "I have a bad feeling."
    mom "I don't think you need to be worried. I'm sure whatever [pov] has in mind is good."
    povi "Well, you say that... Still I need to play this out like I'm a tough as nails gang member to get Davide behind this."
    pov "Come out slut!"
    scene livingroom 10pm 080
    bs "Hello everyone."
    pov "You chose a very sexy outfit, slut."
    povi "And she's still eager about serving the drinks. That's good."
    povi "Soon we'll be through with this and she'll only have to \"serve\" me when she wants to."
    scene livingroom 10pm 081
    dad "..."
    mom "..."
    davide "... hahahaha..."
    bs "Guys?"
    pov "I know she's hot, but you can calm down, haha."
    scene livingroom 10pm 082c
    dad "You can't be serious!"
    pov "Why not? She's just another slut for me."
    mom "But..."
    davide "Hmm?"
    povi "Haha, Davide is confused. Did I really do something new here? Having more than one slut?"
    scene livingroom 10pm 083c
    dad "How can you allow this? She's your daughter."
    povi "As expected, Bruce has to ask his wife to step in and fix things. But she can't help you, she's my girl too."
    dad "I've already accepted all the other humiliations, but this is going too far, don't you think?"
    mom "Hnn..."
    scene livingroom 10pm 084c
    mom "Why is she here? I thought I was your slut?"
    povi "She's doing great. Just as we worked out. Now if [bs] does well then we should be free and clear for now."
    dad "Ehhh?"
    davide "Hehe... hahaha..."
    scene livingroom 10pm 085c
    bs "What's going on here?"
    scene livingroom 10pm 082c
    if inc == True:
        pov "You're still my slut, mom. And [bs] is my slut now as well."
    else:
        pov "You're still my slut, [mother]. And [bs] is my slut now as well."
    pov "I could get bored with just one slut, so I have two of you now."
    if inc == True:
        dad "But she's your sister!"
    else:
        dad "But she's my daughter!"
    pov "Yes, she is. That's just one of the many reasons I should be the one taking care of her."
    mom "But..."
    pov "No more of that [mother]! You'll share your slut-status with her now."
    scene livingroom 10pm 086c
    if inc == True:
        bs "Mom is your slut too?"
    else:
        bs "My mom is your slut too?"
    pov "Yes and you both are truly two of a kind when it comes to pleasing me!"
    pov "But now you'll each have to prove to me who truly is my best slut."
    povi "That sets it up so that they are competing with each other in Davide's eyes."
    povi "He'll let them service me to \"fight\" it out because he likes that kind of shit. Look at how he treats [miranda] and [mother]."
    bs "Hnn..."
    pov "Now go on and show us what I taught you."
    bs "Yes, [pov]."
    scene livingroom 10pm 087c
    bs "See, it's easy."
    davide "Ehh?"
    dad "No..."
    povi "He's so confused as to why she's acting like a waitress. I might have put too much emphasis on that part of our training earlier."
    povi "Just keep it up [bs] and we'll get through this."
    scene livingroom 10pm 088c
    if inc == True:
        bs "Did I do everything to your liking, brother?"
    else:
        bs "Did I do everything to your liking, [pov]?"
    pov "Yes, slut. You placed the tray on the table without spilling any of the drinks."
    bs "<giggle>"
    povi "They're all so confused, now is as good a time as any for the main event. We really need to cement the idea that they are mine."
    pov "Something else comes to mind though. I wonder if the others know about your other decorations. The ones you wear under your dress?"
    pov "I think you should show them to us."
    mom "Decorations?"
    scene livingroom 10pm 089c
    bs "You mean...? I should show them to everyone?"
    pov "Yes! They are already almost visible, but I think we all should get a better look."
    dad "What does he mean, decorations?"
    pov "Do it slut! You know you want to..."
    bs "Yes [pov]."
    scene livingroom 10pm 090c
    bs "These are my decorations, hnn..."
    davide "Hell yes, those are some fine ass titties!"
    scene livingroom 10pm 091c
    dad "Aaahh..."
    davide "And what wonderful decorations you have!"
    mom "Hnn...!"
    pov "Don't stare, Bruce, hahaha..."
    jump basementcassandraoutingcorloveshare

label basementcassandraoutingcorloveshare: #------ Custom - Cor to Love - Cassandra Outing -----
    povi "Ok, Davide seems to be buying it, but I might have to let him have a little fun this time around..."
    call screen basementcassandraoutingcorlovesharechoose

screen basementcassandraoutingcorlovesharechoose(): #------ Custom - Cor to Love - Cassandra Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovesharechoose'), Jump('basementcassandraoutingcorlovesharecspov')) hovered tt.Action ("[bs] serve me, [mother] serve Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovesharechoose'), Jump('basementcassandraoutingcorlovesharenpov')) hovered tt.Action ("[mother] serve me, [bs] serve Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovesharechoose'), Jump('basementcassandraoutingcorlovesharecspovonly')) hovered tt.Action ("[bs] serve me, Davide get's nobody") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorlovesharecspov: #------ Custom - Cor to Love - Cassandra Outing -----
    $ basement10cassandraoutingnshare = True
    povi "[bs] will serve me now and [mother] will serve Davide."
    povi "That way he'll see is as me accepting his higher position... for now."
    pov "Come here and get on your knees, [bs]! I need some service now!"
    scene livingroom 10pm 093ns
    bs "You mean... now?"
    pov "Yes, I know what I said. Get over here."
    bs "But... they'll still sitting there..."
    pov "I know. Now stop talking and do your duty. I told you that you'd have to do this in front of the others, so start sucking!"
    pov "Haha, and don't worry Davide, I'll see you have a little fun too."
    bs "O... OK, [pov]."
    scene livingroom 10pm 092cs
    bs "<suck> <lick>"
    pov "Good, I see that you know your place slut."
    pov "Now give it your best and just ignore the others. You need to learn to follow my orders without question."
    bs "Y... yes [pov]. <lick>"
    scene livingroom 10pm 094ns
    pov "And you'll serve Davide now, [mother]. It's rude to let him sit there alone."
    mom "Yes, of course [pov]."
    povi "I'm sorry I had to have you do this, but he needs to get behind this and that means making him happy right now."
    dad "Grr...."
    davide "Do not even think about to saying something, Bruce!"
    dad "..."
    scene livingroom 10pm 093cs
    bs "<lick> <lick>"
    pov "Your mouth is as great as ever, slut."
    if inc == True:
        bs "Thank you, brother."
    else:
        bs "Thank you, [pov]."
    pov "You'll learn fast how we do things here and there is no reason you can't have some fun too."
    bs "Hmm..."
    povi "Damn, this is working out perfectly."
    scene livingroom 10pm 095ns
    pov "And you're happy too?"
    davide "Look at me, crybaby!"
    povi "Oh, he's bullying Bruce again..."
    scene livingroom 10pm 093cs
    if inc == True:
        pov "And you're giving your best too, right big sis?"
        bs "Yes, I try brother."
    else:
        pov "And you're giving your best too, right [bs]?"
        bs "Yes, I try [pov]."
    if casbjdt >= 2:
        bs "Do you want me to deepthroat you?"
        pov "Are you offering?"
        bs "Yes, do you want me to do it?"
        pov "What a nice slut you are, caring that much for me."
        call screen basementcassandraoutingcorlovecasbj
    else:
        jump basementcassandraoutingcorlovecasbjnormal

screen basementcassandraoutingcorlovecasbj(): #------ Custom - Cor to Love - Cassandra Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovecasbj'), Jump('basementcassandraoutingcorlovecasbjdt')) hovered tt.Action ("Deepthroat me") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovecasbj'), Jump('basementcassandraoutingcorlovecasbjnormal')) hovered tt.Action ("Give me a normal blowjob") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorlovecasbjdt: #------ Custom - Cor to Love - Cassandra Outing -----
    povi "This wasn't part of the plan, but I would be crazy to turn that down."
    pov "Yes, I want you to deepthroat me, slut."
    bs "Okay... [pov]."
    scene livingroom 10pm 095dtcs
    pov "Oh fuck, work your way down my cock."
    bs "Hnng... <suck> <choke>"
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 096ns
        davide "You have the best ideas [pov]. It seems that I've really underestimated you, haha."
        mom "<suck> <lick>"
        pov "So my other slut is doing a good job on you?"
        davide "Haha, you know how good her mouth is, so you know the answer."
        povi "I do, but don't get used to it. We're going to get you out our lives soon!"
    scene livingroom 10pm 095dtcs
    pov "You're doing very good, don't worry."
    if inc == True:
        pov "Not as good as mom, but you can get better, I'm sure."
    else:
        pov "Not as good as your mom, but you can get better, I'm sure."
    bs "Hmm... <suck>"
    pov "I think it's time you take me deeper, slut."
    bs "Hmm..."
    scene livingroom 10pm 096dtcs
    bs "<suck> <choke>"
    pov "Oh yes, very good."
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 097cns
        davide "Hah... yes, suck it slut!"
        dad "<sob>"
        povi "Holy shit, Bruce if crying now?"
        davide "Swallow my spunk!"
        mom "Hnn... <gulp>"
    scene livingroom 10pm 096dtcs
    pov "I'm going to cum slut."
    jump basementcassandraoutingcorlovecasbjcum

label basementcassandraoutingcorlovecasbjnormal: #------ Custom - Cor to Love - Cassandra Outing -----
    pov "While I appreciate the thought, I'd like you do just keep going for now, slut."
    povi "No need to go crazy. I don't want Davide getting ideas."
    bs "Okay... [pov]."
    scene livingroom 10pm 094cs
    bs "<suck> <lick>"
    pov "Oh yes, just like that."
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 096ns
        davide "You have the best ideas [pov]. It seems that I've really underestimated you, haha."
        mom "<suck> <lick>"
        pov "So my other slut is doing a good job on you?"
        davide "Haha, you know how good her mouth is, so you know the answer."
        povi "I do, but don't get used to it. We're going to get you out our lives soon!"
    pov "You're doing very good, don't worry."
    if inc == True:
        pov "Not as good as mom, but you can get better, I'm sure."
    else:
        pov "Not as good as your mom, but you can get better, I'm sure."
    bs "Hmm... <suck>"
    scene livingroom 10pm 095ics
    pov "Ohh, this is nice."
    povi "She teasing the tip, that's new for her."
    bs "Hnn... <lick>"
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 097cns
        davide "Hah... yes, suck it slut!"
        dad "<sob>"
        povi "Holy shit, Bruce if crying now?"
        davide "Swallow my spunk!"
        mom "Hnn... <gulp>"
    scene livingroom 10pm 095ics
    pov "I'm going to cum slut."
    jump basementcassandraoutingcorlovecasbjcum

label basementcassandraoutingcorlovecasbjcum: #------ Custom - Cor to Love - Cassandra Outing -----
    call screen basementcassandraoutingcorlovecasbjcumchoose

screen basementcassandraoutingcorlovecasbjcumchoose(): #------ Custom - Cor to Love - Cassandra Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovecasbjcumchoose'), Jump('basementcassandraoutingcorlovecasbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovecasbjcumchoose'), Jump('basementcassandraoutingcorlovecasbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorlovecasbjcumin: #------ Custom - Cor to Love - Cassandra Outing -----
    pov "I'll cum in your mouth!"
    bs "Hmm..."
    pov "Aaahhh... yes..."
    "You spray your cum inside her mouth."
    bs "Hnn..."
    scene livingroom 10pm 096ics
    bs "Hnn..."
    povi "Damn, is she smiling?"
    pov "Good, slut, don't forget to swallow it all. It would be rude otherwise."
    bs "Yesh... <gulp>"
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 098cns
        davide "Look at her Bruce! She swallowed it all."
        mom "Hah... hah..."
        davide "You can be proud of your wife, haha."
        jump basementcassandraoutingcorloveend
    else:
        jump basementcassandraoutingcorloveend

label basementcassandraoutingcorlovecasbjcumout: #------ Custom - Cor to Love - Cassandra Outing -----
    pov "I'll cum on your face!"
    bs "Hmm..."
    pov "Aaahhh... yes..."
    scene livingroom 10pm 095ocs
    "You spray your cum on her face."
    bs "Hnn..."
    scene livingroom 10pm 096ocs
    bs "You came so much on me... hnn..."
    pov "You should be proud. That shows you how much I appreciate what you were doing."
    bs "Hmm..."
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 098cns
        davide "Look at her Bruce! She swallowed it all."
        mom "Hah... hah..."
        davide "You can be proud of your wife, haha."
        jump basementcassandraoutingcorloveend
    else:
        jump basementcassandraoutingcorloveend

label basementcassandraoutingcorloveend: #------ Custom - Cor to Love - Cassandra Outing -----
    scene black
    povi "I think this worked! One step closer to fixing the crap Bruce caused for this family."
    if basement10cassandraoutingnshare == True or basement10cassandraoutingcshare == True:
        "After you've all had your fun, except Bruce, you decide to call it a night and leave the basement."
    else:
        "After you've had your fun, you decide to call it a night and leave the basement."
    $ basement10cassandraouting = True
    $ basement10cassandraoutingnshare = False
    $ basement10cassandraoutingcshare = False
    jump skip

label basementcassandraoutingcorlovesharenpov: #------ Custom - Cor to Love - Cassandra Outing -----
    $ basement10cassandraoutingcshare = True
    povi "[mother] will serve me now and [bs] will serve Davide."
    povi "That way he'll see is as me accepting his higher position... for now."
    scene livingroom 10pm 092ns
    if inc == True:
        pov "Come here and get on your knees, mom! I need some service now!"
    else:
        pov "Come here and get on your knees, [mother]! I need some service now!"
    mom "Huh? Y-yes, [pov]..."
    povi "Hopefully Bruce doesn't freak out this time."
    scene livingroom 10pm 048a
    mom "<suck> <lick>"
    pov "Good, I see that you know your place slut."
    bs "Huh?"
    scene livingroom 10pm 093ns
    if inc == True:
        bs "Mom is sucking on your dick?"
    else:
        bs "My mother is sucking on your dick?"
    pov "Yes, I haven chosen her to serve me tonight."
    povi "Davide it eating this up."
    pov "And you'll serve Davide with your mouth."
    povi "I know she volunteered to do this so [mother] didn't have to, but I still feel about about it. Well, let's play this out."
    bs "D-Davide? But I thought..."
    pov "Stop! You're not here to think, you're here to serve."
    pov "So do what I told you to do and show me that you can be a good slut."
    bs "Hnn... yes [pov]."
    scene livingroom 10pm 094ncs
    bs "I'm sorry that I hesitated, Davide. I'll serve you good."
    davide "Oh yes, I'm sure you will. Especially a mouth like yours, haha."
    dad "This needs to... stop..."
    davide "Shut up Bruce!"
    scene livingroom 10pm 048a
    pov "Are you're proud that I chose you to serve me?"
    mom "Hnn..."
    if inc == True:
        pov "You should be, mom! You and [bs] will serve me well and we'll keep everything in the family."
    else:
        pov "You should be, [mother]! You and [bs] will serve me well and we'll keep everything in the your family."
    mom "Hmm..."
    pov "I need to hear it from you."
    mom "I... I'm pround you'd chosen me, [pov]."
    pov "Good slut."
    povi "How should I let her continue? Should she get me off on her own or should I help her?"
    call screen basementcassandraoutingcorlovenicbj

screen basementcassandraoutingcorlovenicbj(): #------ Custom - Cor to Love - Cassandra Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovenicbj'), Jump('basementcassandraoutingcorlovenicbjdt')) hovered tt.Action ("Help her (deethroat)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovenicbj'), Jump('basementcassandraoutingcorlovenicbjnormal')) hovered tt.Action ("Let her continue") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorlovenicbjdt: #------ Custom - Cor to Love - Cassandra Outing -----
    povi "Davide is all about the alpha male, doesn't get more alpha than this."
    pov "Let me help you, slut!"
    scene livingroom 10pm 048adt
    mom "Hnn... <suck> <choke>"
    pov "I need you to take me deep."
    scene livingroom 10pm 095ncs
    davide "Oh yes, that's how I like it. Make it wet before it goes deep in your mouth."
    davide "Look how good she can serve, Bruce!"
    dad "No... this is wrong..."
    povi "Oh, he's bullying Bruce again..."
    scene livingroom 10pm 048adt
    if inc == True:
        pov "You hear that slut? Everyone is happy with you and big sis serving us."
    else:
        pov "You hear that slut? Everyone is happy with you and your daughter serving us."
    mom "Hnn..."
    pov "Oh, so you're not convinced yet? You will be, soon."
    scene livingroom 10pm 096ncs
    davide "You have the best ideas [pov]. It seems that I've really underestimated you, haha."
    bs "<suck> <lick>"
    pov "So my other slut is doing a good job on you?"
    davide "Haha, you know how good her mouth is, so you know the answer."
    povi "I do, but don't get used to it. We're going to get you out our lives soon!"
    scene livingroom 10pm 048adt
    pov "You're doing very good, don't worry."
    mom "Hmm... <choke>"
    pov "I think it's time you take me deeper, slut."
    mom "Hmm..."
    scene livingroom 10pm 049adt
    mom "<suck> <choke>"
    pov "Oh yes, very good."
    scene livingroom 10pm 097ncs
    davide "Hah... yes, suck it slut!"
    dad "<sob>"
    povi "Holy shit, Bruce is crying now?"
    davide "Swallow my spunk!"
    bs "Hnn... <gulp>"
    scene livingroom 10pm 049adt
    pov "I'm going to cum slut."
    call screen basementcassandraoutingcorlovenicbjcum

label basementcassandraoutingcorlovenicbjnormal: #------ Custom - Cor to Love - Cassandra Outing -----
    pov "Just continue what you're doing, slut."
    mom "Okay... [pov]."
    scene livingroom 10pm 095ncs
    davide "Oh yes, that's how I like it. Make it wet before it goes deep in your mouth."
    davide "Look how good she can serve, Bruce!"
    dad "No... this is wrong..."
    povi "Oh, he's bullying Bruce again..."
    scene livingroom 10pm 049a
    if inc == True:
        pov "You hear that slut? Everyone is happy with you and big sis serving us."
    else:
        pov "You hear that slut? Everyone is happy with you and your daughter serving us."
    mom "Hnn..."
    pov "Oh, so you're not convinced yet? You will be, soon."
    scene livingroom 10pm 096ncs
    davide "You have the best ideas [pov]. It seems that I've really underestimated you, haha."
    bs "<suck> <lick>"
    pov "So my other slut is doing a good job on you?"
    davide "Haha, you know how good her mouth is, so you know the answer."
    povi "I do, but don't get used to it. We're going to get you out our lives soon!"
    scene livingroom 10pm 049a
    pov "You're doing very good, don't worry."
    mom "Hmm... <lick>"
    scene livingroom 10pm 097ncs
    davide "Hah... yes, suck it slut!"
    dad "<sob>"
    povi "Holy shit, Bruce is crying now?"
    davide "Swallow my spunk!"
    bs "Hnn... <gulp>"
    scene livingroom 10pm 048a
    pov "I'm going to cum slut."
    call screen basementcassandraoutingcorlovenicbjcum

screen basementcassandraoutingcorlovenicbjcum(): #------ Custom - Cor to Love - Cassandra Outing -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovenicbjcum'), Jump('basementcassandraoutingcorlovenicbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('basementcassandraoutingcorlovenicbjcum'), Jump('basementcassandraoutingcorlovenicbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementcassandraoutingcorlovenicbjcumin: #------ Custom - Cor to Love - Cassandra Outing -----
    pov "I'll cum in your mouth!"
    mom "Hmm..."
    pov "Aaahhh... yes..."
    "You spray your cum inside her mouth."
    mom "Hnn..."
    scene livingroom 10pm 051i
    mom "Hnn..."
    pov "Good, slut, don't forget to swallow all. It would be rude otherwise."
    mom "Yesh... <gulp>"
    scene livingroom 10pm 052i
    mom "<gulp> <gulp>"
    scene livingroom 10pm 053i
    mom "Haaah..."
    pov "Good slut."
    scene livingroom 10pm 098ncs
    davide "Look at her Bruce! She swallowed it all."
    bs "Hah... hah..."
    davide "You can be proud of your step-daughter, haha."
    davide "Even if I wished she was your real daughter."
    jump basementcassandraoutingcorloveend

label basementcassandraoutingcorlovenicbjcumout: #------ Custom - Cor to Love - Cassandra Outing -----
    pov "I'll cum on your face!"
    mom "Hmm..."
    pov "Aaahhh... yes..."
    scene livingroom 10pm 050o
    "You spray your cum all over her face."
    mom "Hnn..."
    scene livingroom 10pm 051o
    mom "You came so much on me... hnn..."
    pov "You should be proud. That shows you how much I appreciate what you were doing."
    mom "Hmm..."
    scene livingroom 10pm 098ncs
    davide "Look at her Bruce! She swallowed it all."
    bs "Hah... hah..."
    davide "You can be proud of your step-daughter, haha."
    davide "Even if I wished she was your real daughter."
    jump basementcassandraoutingcorloveend

label basementcassandraoutingcorlovesharecspovonly: #------ Custom - Cor to Love - Cassandra Outing -----
    povi "I think I can get away with just [bs] serving me now and have [mother] sit and watch."
    pov "Come here and get on your knees, [bs]! I need some service now!"
    scene livingroom 10pm 093ns
    bs "You mean... now?"
    pov "Yes, I know what I said. Get over here."
    bs "But... they'll still sitting there..."
    pov "I know. Now stop talking and do your duty. I told you that you'd have to do this in front of the others, so start sucking!"
    pov "I see you want to have fun too Davide, but I'm afriad I must disappoint you."
    pov "I need [mother] to pay close attention to this."
    davide "Hnnn, that make sense. You can have your way... this time..."
    povi "We'll see about that. We'll be rid of you soon enough!"
    bs "O... OK, [pov]."
    scene livingroom 10pm 092cs
    bs "<suck> <lick>"
    pov "Good, I see that you know your place slut."
    pov "Now give it your best and just ignore the others. You need to learn to follow my orders without question."
    bs "Y... yes [pov]. <lick>"
    scene livingroom 10pm 094ns
    pov "And make sure you watch closely and don't miss anything, [mother]."
    dad "You don't need to do this."
    davide "Shut up Bruce and enjoy the show!"
    mom "Y- yes [pov]."
    povi "Davide doesn't have a clue that we're playing him."
    scene livingroom 10pm 093cs
    bs "<lick> <lick>"
    pov "Your mouth is as great as ever, slut."
    if inc == True:
        bs "Thank you, brother."
    else:
        bs "Thank you, [pov]."
    pov "You'll learn fast how we do things here and there is no reason you can't have some fun too."
    bs "Hmm..."
    povi "Damn, this is working out perfectly."
    scene livingroom 10pm 093cs
    if inc == True:
        pov "And you're giving your best too, right big sis?"
        bs "Yes, I try brother."
    else:
        pov "And you're giving your best too, right [bs]?"
        bs "Yes, I try [pov]."
    if casbjdt >= 2:
        bs "Do you want me to deepthroat you?"
        pov "Are you offering?"
        bs "Yes, do you want me to do it?"
        pov "What a nice slut you are, caring that much for me."
        call screen basementcassandraoutingcorlovecasbj
    else:
        jump basementcassandraoutingcorlovecasbjnormal

#----- Custom landing for Cassandra Outing to the Gang -----
label basementcassandraoutingfaillanding:
    call screen basementcassandracorruptionoutingmenu

screen basementcassandracorruptionoutingmenu():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('basementcassandracorruptionoutingmenu'), Jump('basementcassandraoutingcorlovefail')) hovered tt.Action ("Love") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('basementcassandracorruptionoutingmenu'), Jump('basementcassandraoutingcorruptionfail')) hovered tt.Action ("Corruption") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Outing Cassandra to the Gang ----- Fail -----
label basementcassandraoutingcorruptionfail:
    hide screen locations
    hide screen townl
    scene black
    povi "It's time to let the other's know that [bs] is my slut."
    "You go down to the basement with [bs] and let her change before the others arrive."
    scene livingroom 10pm 079
    davide "So what's the damn important thing you want to show us today?"
    pov "It's something special that'll change things around here a bit."
    dad "I have a bad feeling."
    mom "I don't think you need to be worried. I'm sure whatever [pov] has in mind is good."
    povi "Haha, yes, it's good for me at least."
    pov "Come out slut!"
    scene livingroom 10pm 080
    bs "Hello everyone."
    pov "You chose a very sexy outfit, slut."
    povi "And she's still eager about serving the drinks, haha."
    povi "I wonder when she'll realize it is only one of the many \"services\" she'll be providing."
    scene livingroom 10pm 081
    dad "..."
    mom "..."
    davide "... hahahaha..."
    bs "Guys?"
    pov "I know she's hot, but you can calm down, haha."
    scene livingroom 10pm 082l
    mom "What the hell do you think you're doing [bs]?!"
    davide "..."
    pov "Huh?"
    mom "Now you're got yourself into some real trouble, young lady!"
    povi "Shit. This isn't the way I had planned."
    scene livingroom 10pm 083l
    mom "And you're in big trouble too, mister!"
    if inc == True:
        mom "Talking your big sister into this shit."
    else:
        mom "Talking my daughter into this shit."
    mom "What are you thinking, making her your slut?"
    if mombasementcorsecond == True:
        pov "What are you talking about?! You're my slut too. Remember the other night?!"
        mom "How dare you, I'll kick you out of my house if you spread lies like around!"
        povi "Damn, she already submitted earlier, but she gets so defensive around others. She must not be willing to admit it in front of [bs] yet."
    pov "I'm sorry..."
    mom "You better be."
    scene livingroom 10pm 084l
    mom "Come over here and put that damn tray down! You're dressed like a slut!"
    povi "Says the woman dressed as a giant slut too, haha. This would be funny if she wasn't cockblocking me."
    if mombasementcorsecond == True:
        povi "I wonder why she's getting so angry? Maybe I should have outed [mother] first, so everyone already knew she was my slut."
    else:
        povi "I need to think of something else, so I can have [bs] down here as my slut. Maybe I should try to corrupt [mother] more in the basement."
    scene livingroom 10pm 085l
    bs "I'm sorry mom."
    mom "Oh, you'll be sorry when I'm done with you! Come with me right now. You're going back to your room."
    bs "I really thought I could do this."
    mom "You better forgot about this! I'll deal with [pov] later."
    scene livingroom 10pm 086l
    "After they leave the basement..."
    davide "This is all your fault, asshole!"
    dad "What? You're serious?"
    davide "She's your wife and you let her interfere. A real man would have put her in her place."
    povi "Hmm... I wonder why Davide didn't do anything then?"
    scene livingroom 10pm 087l
    dad "But he's the one who brought [bs] down here."
    davide "Yes he did. And it's his damn right as a member of this gang and your bitch of a wife should respect that!"
    dad "But you saw how antgy that made her."
    davide "I don't care about your excuses!"
    scene livingroom 10pm 088l
    davide "You're going to go after them now and make things right."
    davide "I want to see that hot piece of ass become a part of our gang right away!"
    dad "What are you saying?"
    davide "Stop talking, loser! Do your duty now and go!"
    dad "But..."
    davide "GO!"
    scene livingroom 10pm 089l
    "Bruce goes after them."
    davide "God damn, the balls on you kid! I really appreciate you trying bringing [bs] into the gang, bro!"
    if inc == True:
        davide "Your mother just keeps getting in the way."
    else:
        davide "Her mother just keeps getting in the way."
    pov "Well, but it didn't play out as it was planned..."
    scene livingroom 10pm 090l
    davide "No worries for now. The idea alone was fantastic."
    davide "I'm sure it'll work out in time and then I'll have another reason to give that loser Bruce shit, haha."
    povi "His favourite hobby... bullying Bruce."
    scene livingroom 10pm 091l
    davide "But you better think of a plan \"B\", just in case. I'm sure Bruce will chicken out up there, so you're going to have to fix it on your own."
    povi "Well, his mood changed fast."
    pov "Yeah, don't worry about it. I can fix this."
    scene black
    $ basement10cassandraoutingfail = True
    "Disappointed you leave the basement."
    jump skip

#----- Outing Cassandra to the Gang - Fail - Cor to Love -----
label basementcassandraoutingcorlovefail:
    hide screen locations
    hide screen townl
    scene black
    povi "It's time to let the other's know that [bs] is my girl."
    povi "It will be easier to be together if we don't have to hide it."
    "You go down to the basement with [bs] and let her change before the others arrive."
    scene livingroom 10pm 079
    davide "So what's the damn important thing you want to show us today?"
    pov "It's something special that'll change things around here a bit."
    dad "I have a bad feeling."
    mom "I don't think you need to be worried. I'm sure whatever [pov] has in mind is good."
    povi "Well, you say that... Still I need to play this out like I'm a tough as nails gang member to get Davide behind this."
    pov "Come out slut!"
    scene livingroom 10pm 080
    bs "Hello everyone."
    pov "You chose a very sexy outfit, slut."
    povi "And she's still eager about serving the drinks. That's good."
    povi "Soon we'll be through with this and she'll only have to \"serve\" me when she wants to."
    scene livingroom 10pm 081
    dad "..."
    mom "..."
    davide "... hahahaha..."
    bs "Guys?"
    pov "I know she's hot, but you can calm down, haha."
    scene livingroom 10pm 082l
    mom "What the hell do you think you're doing [bs]?!"
    davide "..."
    pov "Huh?"
    mom "Now you're got yourself into some real trouble, young lady!"
    povi "Shit. This isn't the way I had planned."
    scene livingroom 10pm 083l
    mom "And you're in big trouble too, mister!"
    if inc == True:
        mom "Talking your big sister into this shit."
    else:
        mom "Talking my daughter into this shit."
    mom "What are you thinking, making her your slut?"
    povi "I'm trying to protect her from the gang by claimnig her first. You're messing this all up!"
    if mombasementcorsecond == True:
        pov "What are you talking about?! You're my slut too. Remember the other night?!"
        povi "Maybe that will keep her quiet."
        mom "How dare you, I'll kick you out of my house if you spread lies like around!"
        povi "Damn, she already submitted earlier, but she gets so defensive around others. She must not be willing to admit it in front of [bs] yet."
    pov "I'm sorry..."
    mom "You better be."
    scene livingroom 10pm 084l
    mom "Come over here and put that damn tray down! You're dressed like a slut!"
    povi "Says the woman dressed just as slutty. This would almost be funny if she wasn't ruining it all."
    if mombasementcorsecond == True:
        povi "I can get why she's so angry. Maybe I should have talked to her first, so she already knew what I was trying to do. Probably would have helped."
    else:
        povi "I need to think of something else, so I protect [bs] from the gang. Maybe I should try to corrupt [mother] more in the basement."
    scene livingroom 10pm 085l
    bs "I'm sorry mom."
    mom "Oh, you'll be sorry when I'm done with you! Come with me right now. You're going back to your room."
    bs "I really thought I could do this."
    mom "You better forgot about this! I'll deal with [pov] later."
    scene livingroom 10pm 086l
    "After they leave the basement..."
    davide "This is all your fault, asshole!"
    dad "What? You're serious?"
    davide "She's your wife and you let her interfere. A real man would have put her in her place."
    povi "Hmm... I wonder why Davide didn't do anything then?"
    scene livingroom 10pm 087l
    dad "But he's the one who brought [bs] down here."
    davide "Yes he did. And it's his damn right as a member of this gang and your bitch of a wife should respect that!"
    dad "But you saw how antgy that made her."
    davide "I don't care about your excuses!"
    scene livingroom 10pm 088l
    davide "You're going to go after them now and make things right."
    davide "I want to see that hot piece of ass become a part of our gang right away!"
    dad "What are you saying?"
    davide "Stop talking, loser! Do your duty now and go!"
    dad "But..."
    davide "GO!"
    scene livingroom 10pm 089l
    "Bruce goes after them."
    davide "God damn, the balls on you kid! I really appreciate you trying bringing [bs] into the gang, bro!"
    if inc == True:
        davide "Your mother just keeps getting in the way."
    else:
        davide "Her mother just keeps getting in the way."
    povi "Better keep playing along for now."
    pov "Well, but it didn't play out as it was planned..."
    scene livingroom 10pm 090l
    davide "No worries for now. The idea alone was fantastic."
    davide "I'm sure it'll work out in time and then I'll have another reason to give that loser Bruce shit, haha."
    povi "His favourite hobby... bullying Bruce."
    scene livingroom 10pm 091l
    davide "But you better think of a plan \"B\", just in case. I'm sure Bruce will chicken out up there, so you're going to have to fix it on your own."
    povi "Well, his mood changed fast."
    pov "Yeah, don't worry about it. I can fix this."
    scene black
    $ basement10cassandraoutingfail = True
    "Disappointed you leave the basement."
    jump skip

#----- Date with Irina -----
label irinadatetemple:
    hide screen locations
    hide screen townl
    #----- added 0.7 -----
    show screen phone
    $ activateirinadate = False
    if messageirina == 2:
        $ messageirina = 0
    #-----
    scene black
    "You decide on meeting at the restaurant."
    if irinadatetemplefirst == True:
        menu:
            "View First Date Again":
                pass
            "Repeat Date":
                jump irinadatetemplemore
    scene date 10pm 001b
    irina "Hey [pov]!"
    pov "Oh, hey [irina]."
    povi "Wow, that dress looks amazing."
    irina "I see you like my dress."
    pov "Oh yes, very sexy."
    scene date 10pm 002b
    povi "It's so short and with her long, bare legs... just magnificent!"
    povi "She really knows how to dress to make her date go wild, haha."
    scene date 10pm 001b
    irina "So I think I can safely say this is a good start to our date! <giggle>"
    pov "Oh yeah, absolutely."
    irina "And you're looking good too, like a real gentleman in those fine clothes."
    pov "Well, I guess it's good that we both like each other's outfit, haha."
    irina "Haha, yes..."
    call screen irinadatetemplegreet

screen irinadatetemplegreet():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('irinadatetemplegreet'), Jump('irinadatetemplegreetcor')) hovered tt.Action ("Let her turn around [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('irinadatetemplegreet'), Jump('irinadatetemplegreetlove')) hovered tt.Action ("Kiss her hand [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplegreetcor:
    pov "How about you turn around and show me the rest of your dress?"
    irina "Okay."
    scene date 10pm 003bc
    povi "It's so damn short. Just perfect for a bit of fun."
    pov "That's very nice."
    irina "I'm glad you like it."
    $ irinacorruption += 1
    jump irinadatetemple2

label irinadatetemplegreetlove:
    scene date 10pm 003bl
    pov "Come here, beautiful."
    pov "<kiss>"
    irina "Ohh... <giggle>"
    irina "You're the first guy that ever kissed my hand."
    $ irinalove += 1
    jump irinadatetemple2

label irinadatetemple2:
    scene date 21pm 002
    "Waitress" "Your table is ready. If you'll please follow me."
    call screen irinadatetemplewalk

screen irinadatetemplewalk():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('irinadatetemplewalk'), Jump('irinadatetemplewalkcor')) hovered tt.Action ("Grope [irina] [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('irinadatetemplewalk'), Jump('irinadatetemplewalklove')) hovered tt.Action ("Put your arm around her [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplewalkcor:
    pov "Come, [irina]."
    scene date 10pm 004bc
    irina "Huh? So you can't wait? <giggle>"
    pov "Your ass is made for these hands."
    irina "<giggle>"
    $ irinacorruption += 1
    jump irinadatetemple3

label irinadatetemplewalklove:
    pov "Shall we, [irina]?"
    scene date 10pm 004bl
    irina "Oh? How nice. <giggle>"
    pov "For the both of us. I'm the lucky one with a beautiful girl accompanying me."
    irina "<giggle>"
    $ irinalove += 1
    jump irinadatetemple3

label irinadatetemple3:
    scene date 10pm 005b
    irina "I didn't know that they're so big."
    povi "I love this decorations. Everyone stops and looks at, which gives me the perfect chance to admire her beauty."
    povi "How hot she is in this dress. She's practically naked."
    scene date 10pm 006bc
    irina "It's very elegant here. I've never been to such a classy place before."
    call screen irinadatetemplesit

screen irinadatetemplesit():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetemplesit'), Jump('irinadatetemplesitnothing')) hovered tt.Action ("Do nothing") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('irinadatetemplesit'), Jump('irinadatetemplesitlove')) hovered tt.Action ("Be a gentleman [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplesitnothing:
    pov "A special place for a special woman. Let's sit."
    irina "Okay. <giggle>"
    jump irinadatetemple4

label irinadatetemplesitlove:
    pov "Wait!"
    irina "Huh?"
    scene date 10pm 006bl
    pov "Please, let me..."
    irina "Oh, that is so nice of you, [pov]!"
    pov "Not at all."
    irina "<giggle>"
    $ irinalove += 1
    jump irinadatetemple4

label irinadatetemple4:
    scene date 10pm 007b
    pov "Let me ask you something."
    irina "Go on."
    pov "I wonder why you're so interested in me? I'm just a regular guy like the others around here. But you behave around me like I am someone special."
    pov "Don't get me wrong, it's pretty great. It's just not something I'm used to."
    irina "You are special. <giggle>"
    if irinacorruption >= irinalove:
        irina "You may seem like the typical guy, but you're way better than any of the other guys here. There total machos."
    else:
        irina "You're not like a typical guy, you're more of a gentleman. Guys here are total machos."
    pov "Like treating girls like they're property and shit like that?"
    irina "Yeah, or even worse, like sluts. I never met a guy as nice as you are."
    irina "I dream of finding a guy like you and leaving this shithole with him to have a normal life far away from here."
    pov "So you hate it here?"
    irina "Yes, and there no real perspectives here. No good jobs, unless you want to be a criminal."
    pov "Oh, yeah that sucks."
    pov "I'm impressed though. You always seem to have a good attitude despite all of that."
    irina "Yeah, being sad just isn't something I do."
    irina "I love to be spontaneous and adventurous."
    irina "That's one of the many reasons why [bs] and I are such good friends."
    pov "That makes sense."
    irina "I guess I just love living my life even if it's... demanding at times."
    if inc == True:
        irina "And I might just be in love with [bs]'s hot brother. <giggle>"
    else:
        irina "And I might just be in love with [bs]'s hot friend. <giggle>"
    call screen irinadatetemplebehaviour

screen irinadatetemplebehaviour():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('irinadatetemplebehaviour'), Jump('irinadatetemplebehaviourcor')) hovered tt.Action ("Use her dream [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('irinadatetemplebehaviour'), Jump('irinadatetemplebehaviourlove')) hovered tt.Action ("Be nice to her [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplebehaviourcor:
    pov "I think it's fate that we met [irina]. I think I can be that guy to save you from all of this."
    irina "<giggle> I knew it."
    pov "It's not going to be easy. We might have to keep our plans a secret for a while. We're going through some things at home and it's going to take some time to take care of that."
    irina "Oh... I'm sorry to hear that."
    pov "Yeah, I kinda need to act like a macho guy when I'm around there. It's important. Even around you."
    scene date 10pm 007bc
    irina "You mean treating me like a slut?"
    pov "You're no slut to me, but yes. I have to play the macho guy for a while."
    irina "Oh..."
    pov "But don't worry. We'll leave this shithole together! I won't let you down like the other have."
    povi "But we won't leave until you're my slut, of course, haha."
    irina "O... okay [pov]. I trust you."
    if inc == True:
        irina "You're [bs]'s brother after all."
    else:
        irina "You're [bs]'s friend after all."
    $ irinacorruption += 1
    jump irinadatetemplewine

label irinadatetemplebehaviourlove:
    pov "You know. I think we can save each other from this place."
    irina "Really? <giggle> I knew it."
    pov "I'll treat you like a proper woman. It shouldn't feel so strange to have someone kiss your hand or pull your chair out for you. That's just being a gentleman."
    scene date 10pm 007bl
    irina "Aww... <giggle>"
    pov "You'll be showered with compliments and the gentle side of love."
    irina "Oh, please! Never stop sweet talking to me."
    pov "I can do that if you want, but we're here to eat too, haha."
    irina "You're right, haha."
    $ irinalove += 1
    jump irinadatetemplewine

label irinadatetemplewine:
    scene date 10pm 008b
    irina "Cheers!"
    pov "To us!"
    irina "Yes. <giggle>"
    scene date 10pm 009b
    irina "<gulp> <gulp>"
    pov "Haha, you can take is slow if you want. I'm not going anywhere."
    scene date 10pm 010bc
    irina "I'm still a little nervous."
    pov "Don't be."
    call screen irinadatetemplepanties

screen irinadatetemplepanties():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('irinadatetemplepanties'), Jump('irinadatetemplepantiescor')) hovered tt.Action ("Challenge her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetemplepanties'), Jump('irinadatetemplepantiesnothing')) hovered tt.Action ("Do nothing") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplepantiescor:
    pov "I have a sure proof way to get rid of those nerves."
    pov "It's spontaneous and adventurous too, so it's perfect for you."
    irina "What is it?"
    pov "Give me your panties!"
    irina "R-right now?"
    pov "Yup. Guaranteed to brush those nerve away and a great opportunity to show me that you're a good girl."
    scene date 10pm 011bc
    irina "Hmm... I don't know. Maybe I shouldn't trust you after all. You wouldn't be trying to take advanage of me, would you?"
    pov "Of course not! It'll be our secret. And it's completely up to you. I'm just offering a chance to do something... exciting."
    scene date 10pm 012bc
    pov "Besides, it's an pretty roundabout way to get into your panties, haha."
    irina "Hnn..."
    povi "Did she really just do it? I need to check it."
    scene date 10pm 015bc
    povi "Oh shit, she did it. And her panties are there on the floor."
    "You pick up her panties."
    povi "Sitting there naked just to prove me that she can be a good girl. I might really like her."
    scene date 10pm 013bc
    pov "Oh..."
    "Waitress" "This is for you."
    povi "Ha, [irina] looks nervous again. Does she really think I'll say something? Nah, we are going to have so much more fun."
    irina "T-thank you."
    scene date 10pm 014bc
    "Waitress" "And yours, Sir."
    pov "Thank you."
    povi "[irina] clearly can't wait for the waitress to leave. I wonder if she's embarrassed about taking her panties off."
    scene date 10pm 016bc
    pov "Well that clinches it, you're definitely a good girl. And brave! I didn't think you'd do it."
    irina "Hnng... thank you."
    pov "See, I bet you're not nervous about our date anymore."
    irina "Nope..."
    pov "Good, now let's enjoy our meal."
    irina "Okay... thank you."
    $ irinacorruption += 1
    $ irinadatetemplepantyoff = True
    jump irinadatetempleconversation

label irinadatetemplepantiesnothing:
    pov "There's really no need to be nervous around me, just be yourself."
    pov "You already won my heart [irina]. The hard work is over, haha!"
    scene date 10pm 010bl
    irina "Okay, I'll try. <giggle>"
    pov "See, your lovely smile is back now."
    irina "You're so sweet, I still can't believe it."
    pov "Well you better believe it! It's here to stay."
    irina "Haha..."
    scene date 10pm 013bl
    irina "Oh that looks tasty."
    "Waitress" "This is for you."
    pov "Only the best for us tonight, [irina]."
    scene date 10pm 014bl
    "Waitress" "And yours, Sir."
    pov "Thank you."
    povi "She's really having fun. She's finally being treated like a lady. I'm glad."
    scene date 10pm 015bl
    pov "Feeling special yet?"
    irina "It's just amazing. She was so nice to me and the food looks so tasty."
    pov "I'm glad you're having a good time. You deserve it!"
    irina "Let's eat."
    pov "Yes let's."
    jump irinadatetempleconversation

label irinadatetempleconversation:
    call screen irinadatetempleconversation2

screen irinadatetempleconversation2():

    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('irinadatetempleconversation2'), Jump('irinadatetempleconversationcor')) hovered tt.Action ("Treat her like a slut [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('irinadatetempleconversation2'), Jump('irinadatetempleconversationlove')) hovered tt.Action ("Treat her like a lady [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetempleconversationcor:
    scene date 10pm 017bc
    "You two enjoy a long talk while eating."
    "You direct the conversation around reasons she needs to be a good girl for you."
    $ irinacorruption += 1
    if irinadatetemplefirst == True:
        jump irinadatetemplerewardsecond
    else:
        jump irinadatetempleleave

label irinadatetempleconversationlove:
    scene date 10pm 016bl
    "You two enjoy a long talk while eating."
    "You happily hear more about her life and take every opportunity to lavish her with compliments."
    $ irinalove += 1
    if irinadatetemplefirst == True:
        jump irinadatetemplerewardsecond
    else:
        jump irinadatetempleleave

label irinadatetempleleave:
    scene black
    "After eating you two leave the restaurant together and take a taxi to her home."
    "You didn't realize she lives so close to you. You pay the taxi driver and walk her to the door."
    scene date 10pm 030
    irina "We made it! This is my parent's house."
    pov "Oh you're living still at home? Just like me, haha."
    irina "Yeah, I don't have the money to live alone."
    pov "Maybe we can change that soon, haha. Although you wouldn't be living alone."
    irina "<giggle>"
    if irinacorruption >= irinalove:
        scene date 10pm 031c
    else:
        scene date 10pm 031l
    irina "So... I really want to invite you to my room..."
    pov "Well if it helps, I'm going to say yes if you do."
    irina "You mean right now?"
    pov "Yes, didn't you mean now?"
    irina "Hmm... but my parents still at home."
    if NTR == True and irinarelationship <= 5:
        jump irinadatetempleNTR
    if irinacorruption >= irinalove:
        scene date 10pm 032c
    else:
        scene date 10pm 032l
    pov "So is that a \"no\"?"
    irina "I'm sorry [pov], but my father would get very mad if he caught us."
    pov "Oh, I can understand that, haha."
    irina "I never brings guys home, father would kill you."
    if irinacorruption >= irinalove:
        scene date 10pm 033c
    else:
        scene date 10pm 033l
    irina "But I promise I'll make up to you another time <giggle>"
    irina "The date was so nice, you really deserve a reward though."
    pov "Oh, that sounds intriguing."
    jump irinadatetemplerewardsecond

#----- Edited -----
label irinadatetemplerewardsecond:
    if NTR == True and irinarelationship <= 5:
        jump irinadatetempleNTR
    if irinacorruption >= irinalove:
        scene date 10pm 032c
        irina "<giggle>"
        call screen irinadatetemplereward
    else:
        scene date 10pm 032l
        irina "<giggle>"
        call screen irinadatetemplerewardlove #----- Custom -----

screen irinadatetemplereward():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        if irinacorruption >= 1:
            imagebutton auto "gui/icons/icon_french_kiss_corruption_%s.png" action (Hide('irinadatetemplereward'), Jump('irinadatetemplerewardfkiss')) hovered tt.Action ("French kiss her [cr1]") focus_mask True
        if irinacorruption >= 10:
            imagebutton auto "gui/icons/icon_fondle_tits_%s.png" action (Hide('irinadatetemplereward'), Jump('irinadatetemplerewardgrope')) hovered tt.Action ("Grope her tits [cr1]") focus_mask True
        if irinacorruption >= 20:
            imagebutton auto "gui/icons/icon_finger_corruption_%s.png" action (Hide('irinadatetemplereward'), Jump('irinadatetemplerewardfinger')) hovered tt.Action ("Finger her [cr1]") focus_mask True
        if irinacorruption >= 30:
            imagebutton auto "gui/icons/icon_handjob_corruption_%s.png" action (Hide('irinadatetemplereward'), Jump('irinadatetemplerewardhandjob')) hovered tt.Action ("Demand a handjob [cr1]") focus_mask True
        if irinacorruption >= 40:
            imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" action (Hide('irinadatetemplereward'), Jump('irinadatetemplerewardblowjob')) hovered tt.Action ("Demand a blowjob [cr1]") focus_mask True
        if irinacorruption >= 50:
            imagebutton auto "gui/icons/icon_sex_corruption_%s.png" action (Hide('irinadatetemplereward'), Jump('irinadatetemplerewardsex')) hovered tt.Action ("Fuck her [cr1]") focus_mask True
        #----- Custom -----
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('irinadatetemplereward'), Jump('irinadatetemplecorruptionend')) hovered tt.Action ("End Date") focus_mask True

    hbox xalign .5 yalign .3:

        if irinacorruption >= 1:
            imagebutton auto "images/edited/gui/vice/icon_mouth_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardcheekcor')) hovered tt.Action ("Kiss her [lv1]") focus_mask True
        if irinacorruption >= 10:
            imagebutton auto "images/edited/gui/vice/icon_french_kiss_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardfkisscor')) hovered tt.Action ("Kiss her more [lv1]") focus_mask True
        if irinacorruption >= 20:
            imagebutton auto "images/edited/gui/vice/icon_unihand_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewarddickgrabcor')) hovered tt.Action ("Dick Grab [lv1]") focus_mask True
        if irinacorruption >= 30:
            imagebutton auto "images/edited/gui/vice/icon_hug_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardflashcor')) hovered tt.Action ("Flash [lv1]") focus_mask True
        if irinacorruption >= 40:
            imagebutton auto "images/edited/gui/vice/icon_handjob_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardhandjobcor')) hovered tt.Action ("Handjob [lv1]") focus_mask True
        if irinacorruption >= 50:
            imagebutton auto "images/edited/gui/vice/icon_blowjob_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardblowjobcor')) hovered tt.Action ("Blowjob [lv1]") focus_mask True
        #----- Custom -----
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadateloveendcor')) hovered tt.Action ("End Date") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplerewardfkiss:
    pov "I think you need this."
    irina "Huh?"
    scene date 10pm 035c
    pov "<kiss>"
    "You two french kiss."
    irina "Hmm..."
    scene date 10pm 036c
    irina "Hnn... why did you do that?"
    pov "Because I wanted to kiss you."
    irina "But my parents..."
    pov "You want to be a good girl, right. So you need to reward me after a good date."
    pov "Don't you think so?"
    irina "Hnn... yes... you're right."
    pov "Good girl."
    #jump irinadatetemplecorruptionend
    call screen irinadatetemplereward

label irinadatetemplerewardgrope:
    pov "Let's have a little fun."
    irina "Huh?"
    scene date 10pm 070c
    irina "Hah!"
    pov "I needed to feel them. They've been teasing me all night."
    scene date 10pm 071c
    irina "Please stop [pov]. My father could catch us..."
    pov "No, he won't. Just stay still and let me enjoy your tits a while longer."
    scene date 10pm 072c
    irina "Hnn..."
    pov "See? You like my touching too."
    irina "Yes, [pov]."
    pov "I'd love to play with them all day, but you're right and we'll stop here."
    #jump irinadatetemplecorruptionend
    call screen irinadatetemplereward

label irinadatetemplerewardfinger:
    pov "I think you need a reward."
    irina "Huh? Wait!"
    scene date 10pm 075c
    pov "Gotcha!"
    irina "Hnn... not there!"
    pov "Oh yes, that's exact the spot I want to be right now."
    pov "And judging from how wet you are, I'm sure you like it too."
    scene date 10pm 076c
    irina "Hah... yes, but..."
    pov "Yes? So I'm right. You want to feel me too."
    irina "Hah... [pov]!"
    scene date 10pm 077c
    pov "Good, relax and enjoy it."
    pov "Let my fingers do their work."
    scene date 10pm 078c
    irina "Hah... hah..."
    pov "You're a good girl, letting me feel you up like this."
    irina "Hah... hnn...!"
    scene date 10pm 079c
    pov "And you enjoyed my touch a little too much, haha."
    pov "I can't wait for the day when my dick enter your pussy."
    irina "Hnn..."
    pov "Dream of my touch [irina]!"
    irina "Yes, I will, hah..."
    #jump irinadatetemplecorruptionend
    call screen irinadatetemplereward

label irinadatetemplerewardhandjob:
    pov "I need some help."
    irina "Huh? What?"
    scene date 10pm 038c
    pov "Please help me with my problem. I've had a boner this whole time."
    irina "We can't do that. It's too risky."
    pov "I need this. Be a good girl and help me."
    scene date 10pm 039c
    pov "I seem to remember someone claiming she was adventurous. Seems like you'd enjoy a little risky business."
    irina "Hnn...!"
    pov "Reward me for having a good time, prove yourself to me."
    irina "Hmm..."
    scene date 10pm 040c
    pov "Good, rub me fast and hard and I'll cum in no time."
    irina "Y-yes..."
    pov "You can do it, my dick will melt from the touch of your soft fingers."
    irina "You're so hard."
    scene date 10pm 041c
    pov "You can feel me trembling too, I'm very close. You know how to please me so well."
    irina "Hmm..."
    pov "I'm glad I found a girl like you. One who knows what I need."
    irina "Hmm... thank you... [pov]."
    scene date 10pm 042c
    pov "HNNG!"
    pov "Yes, that's my girl."
    irina "Hmm..."
    pov "Milk me all dry."
    scene date 10pm 043c
    pov "Oh yes, very nice."
    irina "Hah, so hot."
    pov "Think of it as a reward for us having this great date."
    irina "Hmm... I will."
    #jump irinadatetemplecorruptionend
    call screen irinadatetemplereward

label irinadatetemplerewardblowjob:
    pov "I want to feel your mouth around my cock."
    irina "Huh? You really want me to?"
    scene date 10pm 045c
    pov "Yes, I need to feel your mouth now."
    irina "But this is a way too risky. If we get caught, there will be hell to pay!"
    pov "Your father will understand. I bet got rewards after a date when he was young."
    scene date 10pm 048c
    irina "You're unbelievable..."
    pov "And you're a good girl, doing what I ask of you."
    irina "<suck> <lick>"
    pov "Oh yes, just like that."
    call screen irinadatetempleblowjobhelp

screen irinadatetempleblowjobhelp():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetempleblowjobhelp'), Jump('irinadatetempleblowjobdt')) hovered tt.Action ("Help her (deepthroat)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetempleblowjobhelp'), Jump('irinadatetempleblowjobnormal')) hovered tt.Action ("Let her continue") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetempleblowjobdt:
    $ irinadatetempledt = True
    pov "Let me help you!"
    scene date 10pm 049cdt
    irina "Hng..."
    pov "Don't fight back! Let me guide you and I'll finish in no time."
    irina "Hnn..."
    pov "Be my good girl."
    scene date 10pm 050cdt
    irina "Hmm... <suck> <choke>"
    pov "Good, very good. Your throat is perfect, [irina]."
    irina "Hnn..."
    pov "Hold it deep just a little longer!"
    jump irinadatetempleblowjobcum

label irinadatetempleblowjobnormal:
    pov "You're going to get me off quick! I know you can do it!"
    irina "Hmm... <suck> <lick>"
    pov "I like your style, rubbing the shaft and licking the tip."
    irina "Hnn..."
    pov "That will make me cum in no time!"
    jump irinadatetempleblowjobcum

label irinadatetempleblowjobcum:
    call screen irinadatetempleblowjobcumchoose

screen irinadatetempleblowjobcumchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetempleblowjobcumchoose'), Jump('irinadatetempleblowjobcuminside')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetempleblowjobcumchoose'), Jump('irinadatetempleblowjobcumoutside')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetempleblowjobcuminside:
    pov "I'm close, I need to cum in your mouth."
    if irinadatetempledt == True:
        scene date 10pm 051cdti
    else:
        scene date 10pm 050c
    pov "Oh yes! HNNG!"
    irina "Hnn..."
    pov "Suck it all out of me."
    scene date 10pm 052ci
    irina "Hah... hah..."
    pov "That was very good. Now swallow it."
    irina "Yesh... [pov]."
    scene date 10pm 053ci
    irina "<gulp> <gulp>"
    pov "Good girl. Did you like that taste?"
    irina "Hmm..."
    pov "You can be proud, I loved my reward [irina]."
    irina "Thank you [pov]."
    #jump irinadatetemplecorruptionend
    call screen irinadatetemplereward

label irinadatetempleblowjobcumoutside:
    pov "I'm close, I want to cum on your face."
    scene date 10pm 051co
    pov "Oh yes! HNNG!"
    irina "Hmm..."
    pov "You made me cum so much."
    scene date 10pm 052co
    irina "Hah... hah..."
    pov "You did very good."
    irina "Yeah, that's a lot... and so hot..."
    pov "I marked you now. You can be proud to be my girl."
    irina "Hmm... I am [pov]."
    pov "Me too [irina]."
    #jump irinadatetemplecorruptionend
    call screen irinadatetemplereward

label irinadatetemplerewardsex:
    pov "Turn around, I need to adore you more."
    scene date 10pm 060c
    irina "What are you up to?"
    pov "I need to see your hot body in that short dress."
    irina "But we're together all the time."
    pov "Ssshhh..."
    scene date 10pm 061c
    pov "Your hot ass, with your beautiful long legs."
    irina "Hmm..."
    pov "Waiting for me to claim you."
    irina "Claim?"
    scene date 10pm 062c
    pov "You know exactly what I mean."
    irina "Is... is that your dick [pov]?"
    pov "Yes. And I'm going to claim your ass now. Claiming your pussy is something for another time."
    irina "Y... you're joking... haha..."
    scene date 10pm 063c
    irina "Hah... Aaahnn..."
    pov "Do you like my joke?"
    irina "Hah... you really did it... hah..."
    pov "You're so tight. You really needed this."
    scene date 10pm 064c
    irina "Hah... I'm scared [pov]..."
    pov "You don't need to be. You're so tight I won't last long, haha."
    irina "Hah... hah... fucking me here like that."
    pov "You like it?"
    irina "Hah... yes..."
    scene date 10pm 065c
    pov "Then I'll give my best so can you enjoy it too!"
    irina "Aahh... hah..."
    pov "You're trembling. Is this getting you off?"
    irina "Yes, hah... I'm getting close [pov]."
    pov "Do it! I'll follow you soon."
    "You fuck her faster and harder."
    scene date 10pm 066c
    irina "Oh my god [pov]. Hah... hah..."
    pov "You're a good girl, spontaneous and adventurous."
    irina "Hah... hah..."
    pov "Imagine if we did get caught right now. Your dad would see his little girl getting her ass rammed."
    pov "Right on his front door."
    irina "Aaahh... hah... [pov]!"
    pov "You're coming?"
    irina "Yes, hah... aahhh..."
    pov "Dirty girl, haha."
    call screen irinadatetemplerewardsexcum

screen irinadatetemplerewardsexcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetemplerewardsexcum'), Jump('irinadatetemplerewardsexcuminside')) hovered tt.Action ("Cum in her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetemplerewardsexcum'), Jump('irinadatetemplerewardsexcumoutside')) hovered tt.Action ("Cum on her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplerewardsexcuminside:
    pov "I'll cum too!"
    pov "Aaahh... I'm going to fill you up."
    irina "Hah... hnn..."
    "You pump your sperm in her asshole."
    scene date 10pm 067ci
    pov "I came so much."
    irina "Hah... hah... so hot inside me."
    pov "Your hot ass milked me good."
    irina "Hmm... hah..."
    pov "I can't wait to have more fun with you, but now I need to recover."
    irina "Hah... me too..."
    #jump irinadatetemplecorruptionend
    call screen irinadatetemplereward

label irinadatetemplerewardsexcumoutside:
    pov "I'll cum too!"
    pov "Aaahh... I'll cover your ass."
    irina "Hah... hnn..."
    "You spray your sperm on her ass."
    scene date 10pm 067co
    pov "Yes, I came so much."
    irina "Hah... hah... I feel it. So hot."
    pov "Your hot ass made me cum real good."
    irina "Hmm... hah..."
    pov "I can't wait to have more fun with you, but now I need to recover."
    irina "Hah... me too..."
    #jump irinadatetemplecorruptionend
    call screen irinadatetemplereward

label irinadatetemplecorruptionend:
    pov "We need to do this again!"
    irina "Yeah we do!"
    pov "Have a good night."
    irina "You too."
    scene black
    $ irinacorruption += 1
    $ irinadatetempledt = False
    $ irinadatetemplefirst = True
    "You leave her and go home."
    jump skip

#----- Custom - Irina Date - Cor to Love -----
screen irinadatetemplerewardlove(): #----- Cor to Love - Irina Date -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        if irinalove >= 1:
            imagebutton auto "images/edited/gui/vice/icon_french_kiss_corruption_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadatetemplerewardfkisslove')) hovered tt.Action ("French kiss her [lv1]") focus_mask True
        if irinalove >= 10:
            imagebutton auto "images/edited/gui/vice/icon_fondle_tits_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadatetemplerewardgropelove')) hovered tt.Action ("Grope her tits [lv1]") focus_mask True
        if irinalove >= 20:
            imagebutton auto "images/edited/gui/vice/icon_finger_corruption_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadatetemplerewardfingerlove')) hovered tt.Action ("Finger her [lv1]") focus_mask True
        if irinalove >= 30:
            imagebutton auto "images/edited/gui/vice/icon_handjob_corruption_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadatetemplerewardhandjoblove')) hovered tt.Action ("Demand a handjob [lv1]") focus_mask True
        if irinalove >= 40:
            imagebutton auto "images/edited/gui/vice/icon_blowjob_corruption_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadatetemplerewardblowjoblove')) hovered tt.Action ("Demand a blowjob [lv1]") focus_mask True
        if irinalove >= 50:
            imagebutton auto "images/edited/gui/vice/icon_sex_corruption_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadatetemplerewardsexlove')) hovered tt.Action ("Fuck her [lv1]") focus_mask True
        #----- Custom
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadatetemplecorruptionendlove')) hovered tt.Action ("End Date") focus_mask True

    hbox xalign .5 yalign .3:

        if irinalove >= 1:
            imagebutton auto "gui/icons/icon_mouth_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardcheek')) hovered tt.Action ("Kiss her [lv1]") focus_mask True
        if irinalove >= 10:
            imagebutton auto "gui/icons/icon_french_kiss_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardfkiss')) hovered tt.Action ("Kiss her more [lv1]") focus_mask True
        if irinalove >= 20:
            imagebutton auto "gui/icons/icon_unihand_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewarddickgrab')) hovered tt.Action ("Dick Grab [lv1]") focus_mask True
        if irinalove >= 30:
            imagebutton auto "gui/icons/icon_hug_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardflash')) hovered tt.Action ("Flash [lv1]") focus_mask True
        if irinalove >= 40:
            imagebutton auto "gui/icons/icon_handjob_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardhandjob')) hovered tt.Action ("Handjob [lv1]") focus_mask True
        if irinalove >= 50:
            imagebutton auto "images/edited/gui/icons/icon_blowjob_love_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadaterewardblowjob')) hovered tt.Action ("Blowjob [lv1]") focus_mask True
        #----- Custom
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('irinadatetemplerewardlove'), Jump('irinadateloveend')) hovered tt.Action ("End Date") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplerewardfkisslove: #----- Cor to Love - Irina Date -----
    irina "You need a reward."
    pov "Huh?"
    irina "Kiss me."
    scene date 10pm 035c
    pov "<kiss>"
    "You give her a french kiss."
    irina "Hmm..."
    scene date 10pm 036c
    irina "Hnn... that was real nice."
    pov "I've been wanting to kiss you."
    irina "I would like to keep going, but my parents..."
    pov "It's ok. I totally understand."
    irina "Hnn... well... maybe we can do a bit more..."
    #jump irinadatetemplecorruptionendlove
    call screen irinadatetemplerewardlove

label irinadatetemplerewardgropelove: #----- Cor to Love - Irina Date -----
    irina "I want you to touch feel them."
    pov "Them?"
    irina "You've been staring at them all night. <giggle>"
    scene date 10pm 070c
    irina "Hah!"
    scene date 10pm 072c
    pov "I love the way they feel. They were teasing me all night behind that dress."
    scene date 10pm 071c
    irina "Maybe we should stop [pov]. My father could catch us..."
    pov "He won't. We'll be quiet. Now let's enjoy your tits together a little longer."
    scene date 10pm 070c
    irina "Hnn..."
    scene date 10pm 072c
    pov "See? You like my touching too."
    irina "Yes, [pov]."
    pov "I'd love to play with them all day, but you're right, we'll stop here."
    #jump irinadatetemplecorruptionendlove
    call screen irinadatetemplerewardlove

label irinadatetemplerewardfingerlove: #----- Cor to Love - Irina Date -----
    irina "Touch me..."
    pov "Huh?."
    irina "Feel how wet I am."
    scene date 10pm 075c
    pov "Wow!"
    irina "Hnn... see how excited you get me?"
    pov "Oh yes, I feel the same way baby."
    scene date 10pm 076c
    irina "Hah... yes, that feels good..."
    pov "I'm glad. You want to feel wonderful everytime you're with me."
    irina "Hah... [pov]!"
    scene date 10pm 077c
    pov "I'm going deeper now."
    irina "Hmmm... so deep..."
    pov "Just let my fingers do their work. You're going to feel real good."
    scene date 10pm 078c
    irina "Hah... hah..."
    pov "I love how you feel inside. So wet and warm."
    irina "Hah... hnn...!"
    scene date 10pm 079c
    pov "Oh wow! You're dripping down there."
    irina "Hnn..."
    pov "Did that feel good [irina]?"
    irina "Yes, it was great, hah..."
    #jump irinadatetemplecorruptionendlove
    call screen irinadatetemplerewardlove

label irinadatetemplerewardhandjoblove: #----- Cor to Love - Irina Date -----
    irina "I need to feel you."
    pov "Feel me?."
    irina "Here!"
    scene date 10pm 038c
    pov "Oh! Yeah, you got me real excited."
    irina "I could help you with that, but it's risky..."
    scene date 10pm 039c
    pov "I'll try to be quiet if you want to risk it together."
    irina "Hnng!"
    pov "We don't have to if you don't want to of course. I just thought it might be a bit fun, the thrill of getting caught and all..."
    irina "Hmm... okay, let's do it."
    scene date 10pm 040c
    pov "Good, rub me fast and hard and I'll cum in no time."
    irina "Y-yes..."
    pov "You can do it, my dick will melt from the touch of your soft fingers."
    irina "You're so hard."
    scene date 10pm 041c
    pov "You can feel me trembling too, I'm very close. You really good a this."
    irina "Hmm..."
    pov "I'm glad I found a girl like you, as crazy as I am."
    irina "Hmm... thank you... [pov]."
    scene date 10pm 042c
    pov "HNNG!"
    pov "Yes, that's my girl."
    irina "Hmm..."
    pov "Milk me all dry."
    scene date 10pm 043c
    pov "Oh yes, that felt so good."
    irina "Hah, so hot."
    pov "Think of it as a reward for us having this good date, haha."
    irina "Hmm... I will. <giggle>"
    #jump irinadatetemplecorruptionendlove
    call screen irinadatetemplerewardlove

label irinadatetemplerewardblowjoblove: #----- Cor to Love - Irina Date -----
    pov "Do you think... Maybe, I could get a blow-job?"
    irina "Huh? You really want me to?"
    scene date 10pm 045c
    pov "Yes, I need to feel your mouth around my shaft."
    irina "But it could be real risky... What if we got caught?"
    pov "It's that part of the fun?"
    scene date 10pm 048c
    irina "You're unbelievable..."
    pov "And you're right there with me! This is crazy."
    irina "<suck> <lick>"
    pov "Oh yes, just like that."
    call screen irinadatetempleblowjobhelplove

screen irinadatetempleblowjobhelplove(): #----- Cor to Love - Irina Date -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetempleblowjobhelplove'), Jump('irinadatetempleblowjobdtlove')) hovered tt.Action ("Help her (deepthroat)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetempleblowjobhelplove'), Jump('irinadatetempleblowjobnormallove')) hovered tt.Action ("Let her continue") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetempleblowjobdtlove: #----- Cor to Love - Irina Date -----
    $ irinadatetempledt = True
    pov "Let me help you!"
    scene date 10pm 049cdt
    irina "Hng..."
    pov "I'll finish in no time like this."
    irina "Hnn..."
    pov "Oh good girl!"
    scene date 10pm 050cdt
    irina "Hmm... <suck> <choke>"
    pov "Good, very good. This is perfect, [irina]."
    irina "Hnn..."
    pov "Hold it deep just a little longer!"
    jump irinadatetempleblowjobcumlove

label irinadatetempleblowjobnormallove: #----- Cor to Love - Irina Date -----
    pov "I'm sure you'll get me off fast, I know you can do it!"
    irina "Hmm... <suck> <lick>"
    pov "I like your style, rubbing the shaft and licking the tip."
    irina "Hnn..."
    pov "That will help me cum in no time!"
    jump irinadatetempleblowjobcumlove

label irinadatetempleblowjobcumlove: #----- Cor to Love - Irina Date -----
    call screen irinadatetempleblowjobcumchooselove

screen irinadatetempleblowjobcumchooselove(): #----- Cor to Love - Irina Date -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetempleblowjobcumchooselove'), Jump('irinadatetempleblowjobcuminsidelove')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetempleblowjobcumchooselove'), Jump('irinadatetempleblowjobcumoutsidelove')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetempleblowjobcuminsidelove: #----- Cor to Love - Irina Date -----
    pov "I'm close, can I cum in your mouth?"
    irina "Mmhmm!"
    if irinadatetempledt == True:
        scene date 10pm 051cdti
    else:
        scene date 10pm 050c
    pov "Oh yes! HNNG!"
    irina "Hnn..."
    pov "You're sucking it all out of me."
    scene date 10pm 052ci
    irina "Hah... hah..."
    pov "That was soooo good. Now swallow it."
    irina "Yesh... [pov]."
    scene date 10pm 053ci
    irina "<gulp> <gulp>"
    pov "Good girl. Did you like your treat?"
    irina "Hmm... I love it..."
    pov "I loved it to [irina]."
    irina "Thank you [pov]."
    #jump irinadatetemplecorruptionendlove
    call screen irinadatetemplerewardlove

label irinadatetempleblowjobcumoutsidelove: #----- Cor to Love - Irina Date -----
    pov "I'm close, I'm going to cum on your face."
    scene date 10pm 051co
    pov "Oh yes! HNNG!"
    irina "Hmm..."
    pov "You made me cum so much."
    scene date 10pm 052co
    irina "Hah... hah..."
    pov "You did soooo good."
    irina "Wow, it's a lot... and so hot..."
    pov "Sorry I got it all over."
    irina "Hmm... I not [pov]."
    pov "I'm glad [irina]. Thanks."
    #jump irinadatetemplecorruptionendlove
    call screen irinadatetemplerewardlove

label irinadatetemplerewardsexlove: #----- Cor to Love - Irina Date -----
    irina "I think you'd like a different view..."
    scene date 10pm 060c
    irina "What are you thinking about?"
    pov "Your hot body in that short dress."
    irina "But we're together all the time... You've seen this. <giggle>"
    pov "Ssshhh... Let me enjoy this. Haha."
    scene date 10pm 061c
    pov "Your hot ass, with your beautiful long legs..."
    irina "Hmm..."
    pov "I don't think I can hold back anymore..."
    irina "Why should you?"
    scene date 10pm 062c
    pov "Can you feel that?"
    irina "Is... is that your dick [pov]?"
    pov "Yes. can you imagine it deep inside your ass? Thrusting in and out, in and out."
    pov "Claiming you for my own..."
    irina "Hmm... we don't have to imagine... right?"
    "You take her cue and thrust yourself inside her."
    scene date 10pm 063c
    irina "Hah... Aaahnn..."
    pov "This is what wanted right?"
    irina "Hah... you really did it... hah..."
    pov "You're so tight."
    scene date 10pm 064c
    irina "Hah... feels so good [pov]..."
    pov "You're so tight I won't last long."
    irina "Hah... hah... fucking me here like that... hot..."
    pov "So you like it?"
    irina "Hah... yes..."
    scene date 10pm 065c
    pov "I'll be sure to give you my best!"
    irina "Aahh... hah..."
    pov "You're trembling. This getting you off?"
    irina "Yes, hah... I'm getting close [pov]."
    "You fuck her faster and harder."
    scene date 10pm 066c
    irina "Oh my god [pov]. Hah... hah..."
    pov "You're a good girl, spontaneous and adventurous."
    irina "Hah... hah..."
    pov "Imagine if we'd got caught right now. Your dad would see his little girl getting her ass claimed."
    pov "Right on his front door..."
    irina "Aaahh... hah... [pov]!"
    pov "You're coming?"
    irina "Yes, hah... aahhh..."
    pov "Naughty girl, haha."
    call screen irinadatetemplerewardsexcumlove

screen irinadatetemplerewardsexcumlove(): #----- Cor to Love - Irina Date -----
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetemplerewardsexcumlove'), Jump('irinadatetemplerewardsexcuminsidelove')) hovered tt.Action ("Cum in her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetemplerewardsexcumlove'), Jump('irinadatetemplerewardsexcumoutsidelove')) hovered tt.Action ("Cum on her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplerewardsexcuminsidelove: #----- Cor to Love - Irina Date -----
    pov "I'll cum too!"
    pov "Aaahh... here it comes!"
    irina "Hah... hnn..."
    "You pump your sperm into her asshole."
    scene date 10pm 067ci
    pov "Wow, I came so much."
    irina "Hah... hah... so hot inside me."
    pov "Your hot ass milked me good."
    irina "Hmm... hah..."
    pov "I can't wait to have more fun with you, but now I need to recover."
    irina "Hah... me too..."
    #jump irinadatetemplecorruptionendlove
    call screen irinadatetemplerewardlove

label irinadatetemplerewardsexcumoutsidelove: #----- Cor to Love - Irina Date -----
    pov "I'll cum too!"
    pov "Aaahh... here it comes!"
    irina "Hah... hnn..."
    "You spray your sperm on her ass."
    scene date 10pm 067co
    pov "Wow, I came so much."
    irina "Hah... hah... I feel it... so hot on me."
    pov "Your hot ass made me cum good."
    irina "Hmm... hah..."
    pov "I can't wait to have more fun with you, but now I need to recover."
    irina "Hah... me too..."
    #jump irinadatetemplecorruptionendlove
    call screen irinadatetemplerewardlove

label irinadatetemplecorruptionendlove: #----- Cor to Love - Irina Date -----
    irina "I can't wait to do this again!"
    pov "Me too! have a good night."
    irina "You too."
    scene black
    $ irinalove += 1
    $ irinadatetempledt = False
    $ irinadatetemplefirst = True
    "You leave her and go home."
    jump skip

#----- Irina Date ----- Darker Paths -----
label irinadatetempleNTR:
    if irinadatetemplefirst == True:
        scene black
        "You go back with her to her house."
    irina "Huh?"
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    call screen checkdarkerpaths_irina
    scene date 10pm 030n
    if frankfirstmeet == True:
        "You see Frank coming out of the front door."
        frank "[irina]."
    else:
        "You see a man coming out of the front door."
        "Man" "[irina]."
    irina "Da-... Boss..."
    scene date 10pm 031n
    irina "What are you doing here?"
    frank "I was looking for you. You weren't here so I had a talk with your parents."
    irina "With my parents, why?"
    frank "We need to discuss something urgent about your work."
    povi "She seems to be nervous."
    scene date 10pm 032n
    irina "Ahh, about my work. I see."
    frank "Yes, as I said, it's urgent."
    irina "I understand."
    povi "Now her nervousness is just gone. I wonder what's really going on here?"
    scene date 10pm 033n
    irina "I need to talk with my boss about my work now."
    irina "I'm sorry, but we need to call it a night. I hope you understand."
    pov "Oh, okay."
    scene date 10pm 034n
    irina "I'll make it up to you another time [pov]."
    pov "Okay then, I'll leave now and leave you two to talk."
    irina "Thank you for understanding."
    scene date 10pm 036n
    "You start heading down the street."
    irina "Bye [pov]."
    if frankfirstmeet == True:
        povi "Damn, why has Frank here now?"
    else:
        povi "Damn, why has her boss here now?"
    povi "Something is strange with him needing to talk now."
    povi "Or I am just being paranoid?"
    call screen irinadatetemplentrchoose

screen irinadatetemplentrchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetemplentrchoose'), Jump('irinadatetemplentrchoosespy')) hovered tt.Action ("Spy on them") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('irinadatetemplentrchoose'), Jump('irinadatetemplentrchoosego')) hovered tt.Action ("Go home") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label irinadatetemplentrchoosego:
    povi "I'm sure that's just my imagination. They'll just have their talk."
    "You go home."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ irinadatetemplefirst = True
    jump skip

label irinadatetemplentrchoosespy:
    povi "No, I need to know what's going on there. I'll stay and watch."
    scene black
    "You wait around the corner until they leave the porch."
    scene date 10pm 037n
    povi "I can hear their voices from around the back."
    povi "Let's see why there are back there."
    scene date 10pm 038n
    if irina_voyeur == True:
        povi "Oh..."
    elif irina_ntr == True:
        povi "No!"
    elif irina_revenge == True:
        povi "Wait... What?"
    else: #----- Irina_sadist -----
        povi "Interesting..."
    frank "What were you thinking? Going on a date, instead of meeting with me?"
    irina "I'm sorry, Daddy. I really forgot about our \"meeting\"."
    if irina_voyeur == True:
        povi "Daddy? What a kinky guy. I can dig that."
    elif irina_ntr == True:
        povi "Daddy? I'm sure he isn't her dad, so is that this weirdo's fetish?"
    elif irina_revenge == True:
        povi "Daddy? I'm sure he isn't her dad, so it's just that weirdo's fetish? I can't let him do this to her."
    else: #----- Irina_sadist -----
        povi "Daddy? I'm sure he isn't her dad. Must be his fetish."
    frank "I'm hard and I need my relief. So you'll give it your best now."
    irina "Yes... I'll give my best to suck you off, but please calm down, daddy."
    frank "You better or next time I'll tell you dad what a bad girl you are."
    irina "No, please don't. I'll do it."
    if irina_voyeur == True:
        povi "So if that's the case, he's blackmailing her. I prefer a mutual respect between consenting adults, but it happens. Poor girl."
    elif irina_ntr == True:
        povi "So if that's the case, he's blackmailing her. I wonder what's her secret is. I can't stop him though. He's a big man."
    elif irina_revenge == True:
        povi "So if that's the case, he's blackmailing her. I'm not going to let this stand. I'll find a way to stop him."
    else: #----- Irina_sadist -----
        povi "So if that's the case, he's blackmailing her. I wonder what's her secret is. I like his style."
    frank "Go on!"
    scene date 10pm 039n
    irina "Hmpf... <suck> <choke>"
    frank "And don't forget about our other deal. I want your friend to become my next babygirl."
    frank "And you'll make it happen!"
    irina "Yesh... <choke>"
    if irina_voyeur == True:
        povi "Are they talking about [bs]? I can understand that, she's gorgeous."
    elif irina_ntr == True:
        povi "Are they talking about [bs]? Not her too!!!"
    elif irina_revenge == True:
        povi "Are they talking about [bs]? Like hell! I won't let that happen!"
    else: #----- Irina_sadist -----
        povi "Are they talking about [bs]? Nice!"
    frank "You better hurry with preparing her for me. I can't wait to put my sperm inside her."
    irina "Yesh, daddy... <choke>"
    if irina_voyeur == True:
        povi "So they working together to get [bs] ready for him. But [irina] is being forced to help him. Not cool."
    elif irina_ntr == True:
        povi "So they working together to get [bs] ready for him. But [irina] is being forced to help him. I can't believe this!"
    elif irina_revenge == True:
        povi "So they working together to get [bs] ready for him. But [irina] is being forced to help him. That fat bastard!"
    else: #----- Irina_sadist -----
        povi "So they working together to get [bs] ready for him. But [irina] is being forced to help him. I can learn something from this guy. He has dreams and is willing to do whatever it takes. I respect that."
    scene date 10pm 040n
    frank "Oh yes! Swallow my sperm, my little girl!"
    irina "Hnng...! <gulp> <gulp>"
    frank "Enjoy your milk from daddy."
    irina "Hnn..."
    if irina_voyeur == True:
        povi "Well this is nice at least."
    elif irina_ntr == True:
        povi "Noooo!"
    elif irina_revenge == True:
        povi "Asshole! He's going to pay for all of this!"
    else: #----- Irina_sadist -----
        povi "Haha! Nice!"
    scene date 10pm 041n
    frank "You did good, so I'll forgive you this time."
    irina "Thank you."
    irina "And thank you for your milk, daddy."
    frank "Don't forget about our deal! You can go in now."
    irina "Yes..."
    povi "Crap, He's about to leave. I better get out of here before I get caught."
    scene black
    if frankfirstmeet == True:
        "You go home, learning something new about [irina] and Frank."
    else:
        "You go home, learning something new about [irina] and her boss."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ irinadatetemplefirst = True
    $ irinadatetemplentr = True
    jump skip

#----- Repeat Date with Irina -----
label irinadatetemplemore:
    scene date 10pm 007b
    "You have another date with [irina]."
    jump irinadatetempleconversation
