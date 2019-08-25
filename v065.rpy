
label basementnicoleoutingcorruption:
    hide screen locations
    hide screen townl
    scene black
    "You decide to show off [mother] to the other gangmembers."
    scene basement 10pm 015c
    "You sit in the basement with the others waiting for [mother]."
    pov "{i}Today they'll learn that I choosed her to be my slut.{/i}"
    scene basement 10pm 017c
    pov "{i}There she is, sexy as ever.{/i}"
    davide "So you'll bring us something to drink now?"
    mom "Yes."
    scene livingroom 10pm 040
    pov "{i}That outfit is so sexy, I can't wait to use her!{/i}"
    davide "So what do you think about we talked before, Bruce?"
    dad "Huh? I'm not sure yet, sorry..."
    scene livingroom 10pm 041
    mom "The drinks are ready. Do you need something else?"
    pov "{i}Now it's time to show the others that she's mine!{/i}"
    pov "{i}And I'll see if she'd really submitted to me. But how'll Bruce react?{/i}"
    pov "{i}He'll go mad that I stole him his wife.But he'll stay down, because Davide won't allow him to break his gang hierarchy.{/i}"
    if inc == True:
        pov "{i}But I wonder if they'll get shocked when they see what I do with my mom?{/i}"
    pov "{i}Haha, but it's decided already.{/i}"
    pov "I need some service, slut!"
    scene livingroom 10pm 042a
    mom "Huh?"
    dad "What did you say?"
    davide "Hmm?"
    pov "I thought every gang member should have his girl, so I made her my slut!"
    dad "W-What...?"
    pov "And now stop standing there so confused and service me!"
    "You unpack your dick."
    scene livingroom 10pm 043a
    pov "Or did you already forgot about what we spoke? And how you submitted to me?"
    mom "Hnn..."
    dad "How dare you... You can't be serious?"
    davide "Haha, this seems to be great! You surprise me everytime again, [pov]!"
    if inc == True:
        pov "Mom!"
    else:
        pov "[mother]!"
    scene livingroom 10pm 044a
    pov "Yes, down to your place! Now be a good slut."
    mom "Hnn..."
    dad "I have to stop this madness!"
    davide "You'll wait! I want to see if she'll really do it."
    scene livingroom 10pm 045a
    mom "You really want me to do this?"
    if inc == True:
        pov "You decided to become my slut, mom!"
    else:
        pov "You decided to become my slut, [mother]!"
    pov "You won't disappointed me now, so go on and suck on the dick you'd chosen!"
    dad "... no..."
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
    davide "You'll do NOTHING! You know the gang rules! I'll break your bones if you break them!"
    dad "But she's my wife!"
    if inc == True:
        dad "And also his own mother!"
    davide "I can understand his decision, haha. And you'll respect it too."
    pov "Just accept it. You lost! She's mine now."
    dad "What are you..."
    davide "Haha, he's right, Bruce. She's not longer yours now, hahaha."
    scene livingroom 10pm 048a
    pov "{i}She's trembling, but she made her choice, so there is no way to step back for her now.{/i}"
    mom "<suck> <lick>"
    pov "{i}I should praise her so she'll be convinced that she did the right thing to submit to me.{/i}"
    pov "{i}And then she'll be more confident to serve me even more.{/i}"
    pov "{i}I could also spice things up a little bit.{/i}"
    pov "You're doing very good, slut. Your hot lips on my dick is the thing I needed now!"
    call screen basementnicoleoutingcorruptionbj

screen basementnicoleoutingcorruptionbj():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementnicoleoutingcorruptionbj'), Jump('basementnicoleoutingcorruptionbjnormal')) hovered tt.Action ("Let her continue") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 323 action (Hide ('basementnicoleoutingcorruptionbj'), Jump('basementnicoleoutingcorruptionbjdt')) hovered tt.Action ("Help her (deepthroat)") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionbjnormal:
    pov "{i}Hmm, no. She can earn my cum herself and give us all her own show.{/i}"
    $ mombasementcoroutingbjnormal = True
    jump basementnicoleoutingcorruptionbjdt

label basementnicoleoutingcorruptionbjdt:
    pov "{i}It's time that she serve me properly!{/i}"
    if mombasementcoroutingbjnormal == False:
        pov "Let me help you!"
        scene livingroom 10pm 048adt
        mom "Hnng..."
        pov "{i}She's gagging but not fighting back. Very good.{/i}"
    scene livingroom 10pm 047a
    dad "You must blackmailing her. She won't never do something freely."
    davide "Calm down! You lost, he's the winner. It doesn't matter how she became his slut!"
    dad "Oh yes..."
    davide "NO! You'll shut up now!"
    "You form the word \"loser\" to Bruce."
    scene livingroom 10pm 047aa
    davide "But we need to solve another problem now, haha."
    pov "What is it?"
    davide "Bruce have no girl anymore and every gang member should have one, even the ones on the lower end."
    pov "So we'll choose now a girl Bruce can have, since his wife is mine now?"
    davide "Yes, we'll choose one for her so he won't lose her again, hahaha."
    dad "Please, Davide..."
    davide "Shut up!"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 048adt
    else:
        scene livingroom 10pm 048a
    pov "You can be relievied that you made the right decision and give in to me!"
    mom "Hmm..."
    dad "Shut the... grrr..."
    scene livingroom 10pm 047aaa
    davide "So any ideas which girl would fit for this loser? Maybe [miranda], she has very low standards, haha!"
    pov "{i}Haha, [mother] is squeezing me hard. She don't want her to be Bruce's new girl.{/i}"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 049adt
    else:
        scene livingroom 10pm 049a
    pov "Relax, slut. It's not decided yet. And if I even decide so, you'll accept it, because you should know your place!"
    if mombasementcoroutingbjnormal == False:
        mom "Hmm...!"
    else:
        mom "Yes..."
    scene livingroom 10pm 047aaa
    davide "Or someone else?"
    pov "Hmm... a girl with low standards..."
    dad "You can't be serious..."
    pov "What's with the girl I delivered the packages for you? The one in the subway."
    scene town subway ruby
    "What's her name?"
    $ ruby = renpy.input(_("Her name is...")) or _("Ruby")
    scene livingroom 10pm 047aaaa
    davide "You mean [ruby]? Are you serious? She's a junkie."
    davide "She's already half-dead and I don't want to know with how many other junkies she fucked."
    davide "And how many STD's she's having. Urgh... that would be some heavy shit..."
    pov "But maybe the right choice for him, haha."
    dad "Please, [pov]..."
    pov "{i}Oh, he accepted his fate. So I can humiliate him even more.{/i}"
    pov "{i}I could choose [miranda] to be his girl. She's already a slut and [mother] is hating her, so she'll hate Bruce even more.{/i}"
    pov "{i}And also it could spice things up when I decide to have [miranda] and her have fun together, haha.{/i}"
    pov "{i}Or should I choose the subway girl, [ruby]? Then he can't enjoy it but can get relieve when he need to.{/i}"
    pov "{i}Maybe he'll get even ill or get STD's and will lost all of his left pride...{/i}"
    pov "{i}Or he wouldn't be allowed to have any girl for his needs. A grown man that need to masturbate for his relief, haha.{/i}"
    pov "{i}But maybe he could get mad then and do something stupid, like raping someone...{/i}"
    pov "{i}Decisions, hmm...{/i}"
    call screen basementnicoleoutingcorruptionbruce

screen basementnicoleoutingcorruptionbruce():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementnicoleoutingcorruptionbruce'), Jump('basementnicoleoutingcorruptionbrucemiranda')) hovered tt.Action ("He can have [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 775 ypos 123 action (Hide ('basementnicoleoutingcorruptionbruce'), Jump('basementnicoleoutingcorruptionbruceruby')) hovered tt.Action ("He'll take [ruby]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementnicoleoutingcorruptionbruce'), Jump('basementnicoleoutingcorruptionbrucenone')) hovered tt.Action ("He won't be allowed to have a girl") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionbruceruby:
    pov "He's only allowed to do it with [ruby]."
    scene livingroom 10pm 047aaa
    dad "You can't be serious!"
    davide "Haha, I like that cruel boy. So it'll be. You should be happy Bruce. At least you can fuck someone, haha."
    pov "Maybe you'll resist her, but your own hand won't be enough at some point and then you can have fun with her."
    dad "But why?"
    pov "Because I decided it. Oh and something else, when that girl is really so dirty..."
    pov "She isn't allowed to enter the house, I don't want my slut to get ill."
    pov "{i}Oh, now she's sucking me really eager. Is that a agreement with my decision?{/i}"
    $ dadandruby = True
    jump basementnicoleoutingcorruption2

label basementnicoleoutingcorruptionbrucemiranda:
    pov "He can have fun with [miranda] too."
    scene livingroom 10pm 047aaa
    dad "Too?"
    pov "Yes, you can get your relief from her but she'll be free for others to have fun too."
    davide "Ha, a wise decision. And especially because Bruce has a crush on that slut too."
    mom "Hnn...!"
    pov "Oh, someone isn't pleased with my decision?"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 049adt
    else:
        scene livingroom 10pm 049a
    pov "I know you hate her, but you'll accept my decision, slut. Am I right?"
    mom "Hmm..."
    pov "Good!"
    $ dadandmiranda = True
    jump basementnicoleoutingcorruption2

label basementnicoleoutingcorruptionbrucenone:
    pov "He's not allowed to have any girl!"
    scene livingroom 10pm 047aaa
    dad "What?"
    davide "Haha, you can't be serious."
    pov "Oh yes, I am. He's so weak and he makes me angry when I just see him."
    dad "But why?"
    pov "Because I said so. You're a loser and a loser should stay alone."
    davide "Haha, I like that cruel boy. So it'll be."
    dad "But..."
    $ dadalone = True
    jump basementnicoleoutingcorruption2

label basementnicoleoutingcorruption2:
    pov "{i}Now this is decided too and I can relax. And, oh shit, now I can enjoy [mother]'s sucking again.{/i}"
    pov "Oh yes, I'm close my slut!"
    if mombasementcoroutingbjnormal == False:
        scene livingroom 10pm 049adt
    else:
        scene livingroom 10pm 049a
    pov "{i}I need to cum now, but where do I want to put my sperm?{/i}"
    call screen basementnicoleoutingcorruptionbjcum

screen basementnicoleoutingcorruptionbjcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementnicoleoutingcorruptionbjcum'), Jump('basementnicoleoutingcorruptionbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 323 action (Hide ('basementnicoleoutingcorruptionbjcum'), Jump('basementnicoleoutingcorruptionbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionbjcumout:
    pov "I'll cum on your face. Get ready slut!"
    mom "Hmm..."
    scene livingroom 10pm 050o
    pov "Ohhh... yes!"
    "You came on her face."
    scene livingroom 10pm 051o
    mom "Hnn... you're satisfied?"
    pov "{i}Oh, this is something new. But I like it, like a good slut.{/i}"
    pov "Yes, you did a good job, slut!"
    $ basement10pmnicoleoutingcumface = True
    jump basementnicoleoutingcorruption3

label basementnicoleoutingcorruptionbjcumin:
    pov "I'll cum in your mouth. Get ready slut!"
    mom "Hmm..."
    scene livingroom 10pm 048a
    pov "Ohhh... yes!"
    "You came in her mouth."
    scene livingroom 10pm 051i
    mom "Hmm..."
    pov "{i}Oh, she's showing me what I gave her. Like a good slut.{/i}"
    pov "You can swallow it now!"
    scene livingroom 10pm 052i
    mom "<gulp> <gulp>"
    davide "Oh, you tamed her already, haha."
    scene livingroom 10pm 053i
    mom "Aahhh..."
    pov "Yes, you did good. Swallowing all I gave you, good slut!"
    jump basementnicoleoutingcorruption3

label basementnicoleoutingcorruption3:
    pov "Now go and sit on the couch with Bruce, so he can see what he lost, haha."
    davide "Hahaha, this get even better."
    mom "Yes, [pov]."
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 054i
    else:
        scene livingroom 10pm 054o
    dad "What's gotten into you?"
    if inc == True:
        dad "He's your son and you want to be his slut? WTF?"
    else:
        dad "He's the son of your best friend and you want to be his slut? WTF?"
    mom "Hnn..."
    dad "That's not you! Did he blackmail you?"
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 055i
    else:
        scene livingroom 10pm 055o
    davide "That's enough! We made a decision and you'll accept it!"
    dad "But it's not fair!"
    davide "I don't care, it's her decision! And I won't allow that you insult other gang members!"
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 056i
    else:
        scene livingroom 10pm 056o
    dad "So you really want to break all taboos and be with him?"
    dad "You have no idea how disappointed I am. But you're safe, I won't risk all we did..."
    dad "YOU DAMN SLUT!"
    scene livingroom 10pm 057
    pov "STOP!"
    dad "Huh?"
    pov "This will stop now and you'll behave! Remember that I could also tell some things!"
    pov "{i}I won't of course, it could danger the girls, but maybe it'll take effect on him.{/i}"
    dad "..."
    pov "So you understood. And don't forget, you aren't allowed to touch your wife anymore."
    pov "She's mine now and I warn you, don't make any mistakes!"
    dad "..."
    dad "Fuck you!"
    scene livingroom 10pm 058
    dad "I'm out of here!"
    davide "Hahaha, what a great show!"
    davide "Oh and let him go, he'll calm down. He's weak, haha."
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 059i
    else:
        scene livingroom 10pm 059o
    pov "What's wrong? You're all mine now slut, aren't you happy?"
    mom "Hnn..."
    pov "Oh I see, you need a dick!"
    mom "..."
    davide "Or maybe two?"
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 060ai
    else:
        scene livingroom 10pm 060ao
    pov "{i}Is he serious? He want me to share her?{/i}"
    davide "<grin>"
    pov "Hmm..."
    call screen basementnicoleoutingcorruptionshare

screen basementnicoleoutingcorruptionshare():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 767 ypos 123 action (Hide ('basementnicoleoutingcorruptionshare'), Jump('basementnicoleoutingcorruptionshareyes')) hovered tt.Action ("Share her with Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementnicoleoutingcorruptionshare'), Jump('basementnicoleoutingcorruptionshareno')) hovered tt.Action ("Don't share her") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionshareyes:
    pov "Yes, you're right. Two dicks are better then one!"
    davide "Great. You hear that [mother]? You'll serve me too."
    pov "Go in position, slut, so we can start."
    mom "Yes, hnn..."
    pov "{i}Oh, she seems not so happy about being shared.{/i}"
    scene livingroom 10pm 065as
    davide "Hell yes! This will be much fun. Two alphas can have a slut!"
    pov "Haha, you sound like you never had that before."
    davide "With whom should I share a slut? That weak loser Bruce?"
    pov "Then let us enjoy her!"
    scene livingroom 10pm 066s
    pov "{i}This outfit is so perverted. Now I can choose between her pussy or asshole.{/i}"
    davide "Be proud slut. Now you can suck my dick."
    $ basement10pmnicoleoutingshare = True
    call screen basementnicoleoutingcorruptionsharechoose

screen basementnicoleoutingcorruptionsharechoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1475 ypos 123 action (Hide ('basementnicoleoutingcorruptionsharechoose'), Jump('basementnicoleoutingcorruptionsharepussy')) hovered tt.Action ("Fuck her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementnicoleoutingcorruptionsharechoose'), Jump('basementnicoleoutingcorruptionshareass')) hovered tt.Action ("Fuck her ass") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionshareass:
    $ basement10pmnicoleoutingfuckass = True
    pov "I'll give you a good fuck in your ass now, slut! Get yourself ready."
    jump basementnicoleoutingcorruptionsharepussy

label basementnicoleoutingcorruptionsharepussy:
    if basement10pmnicoleoutingfuckass == False:
        pov "I'll give you a good fuck in your pussy now, slut! Get yourself ready."
    davide "Two dicks, you must be in heaven."
    mom "Hnn..."
    pov "{i}She's still not pleased.{/i}"
    pov "Show more appreciation, slut! I'll gave Davide the permission to join us and he should have a good time too!"
    mom "Yes, you're right [pov]. I'm sorry Davide. Please have fun with my mouth."
    davide "Oh yes, I will. Here, have a taste."
    scene livingroom 10pm 068s
    mom "Hmm... <lick>"
    davide "Oh yes, that tongue is amazing. You'll have much fun with that mouth, [pov]."
    pov "{i}Nice. Now she'll submitted even more to me.{/i}"
    pov "Now it's time you get your second dick, slut."
    scene livingroom 10pm 067
    pov "{i}Oh yes, her ass is so sexy.{/i}"
    if inc == True:
        pov "{i}That my mother is presenting herself like that to me. Perfect.{/i}"
    else:
        pov "{i}That [mother] is presenting herself like that to me. Perfect.{/i}"
    pov "{i}She's trembling, waiting for my move. But I need to know how much she need it.{/i}"
    davide "What are you waiting for, [pov]."
    pov "My slut didn't beg for my dick."
    davide "Hahaha, you're serious?"
    if basement10pmnicoleoutingfuckass == True:
        mom "Please [pov]. Please stick your hard dick in my tight asshole."
    else:
        mom "Please [pov]. Please stick your hard dick in my wet pussy."
    davide "Damn, bro!"
    scene livingroom 10pm 070
    mom "Aaahnn..."
    pov "All in!"
    scene livingroom 10pm 070s
    davide "Yes, suck on my cock."
    mom "<suck> <lick>"
    pov "{i}She don't like it to get shared. So she'll be more grateful when we're alone again.{/i}"
    pov "{i}And she'll be more submissive to avoid sharing. But she'll still accept my decisions.{/i}"
    pov "{i}She'll be the best slut ever!{/i}"
    if basement10pmnicoleoutingfuckass == True:
        pov "Your tight asshole is like heaven, slut."
    else:
        pov "Your wet pussy is like heaven, slut."
    davide "Her mouth is also very good, haha."
    scene livingroom 10pm 071s
    davide "Perfect, she's working on my dick so eagerly because her hole is stuffed so good, haha."
    pov "Yes, she's doing good. And my slut learn to serve more dicks than one good also, haha."
    davide "So this mouth will taste my dick again?"
    pov "We'll see."
    mom "Hnn... hnn..."
    davide "Oh, your slut likes the idea too."
    pov "Yes, haha."
    pov "{i}Oh no, she don't, but no one care.{/i}"
    davide "I need to finish soon, her mouth is too good."
    pov "Me too."
    scene livingroom 10pm 069s
    davide "Get it deep now, ha."
    mom "Hnn..."
    davide "I really appreciate that bro. It was a good decision to choose you for the gang."
    davide "You'll be able to do great things in the future."
    pov "Well, we'll see, haha."
    davide "Oh yes, I'm cumming, slut!"
    davide "Haaa, haaa...!"
    mom "Hmm..."
    pov "Damn, I'm so close too. She's gotten so clingy!"
    scene livingroom 10pm 070
    call screen basementnicoleoutingcorruptionsharecum

screen basementnicoleoutingcorruptionsharecum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementnicoleoutingcorruptionsharecum'), Jump('basementnicoleoutingcorruptionsharecuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1675 ypos 123 action (Hide ('basementnicoleoutingcorruptionsharecum'), Jump('basementnicoleoutingcorruptionshareoutside')) hovered tt.Action ("Cum over her ass") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionsharecuminside:
    if basement10pmnicoleoutingfuckass == True:
        pov "I'll cum in your ass, slut."
    else:
        pov "I'll cum in your pussy, slut."
    mom "Hmm..."
    pov "Ah, hnnn..."
    "You spurt your sperm inside her."
    pov "Oh, I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh, yes, you're right, haha."
    if basement10pmnicoleoutingfuckass == True:
        scene livingroom 10pm 072ia
    else:
        scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, slut?"
    mom "Yes, [pov]. I like it when you put your sperm inside me."
    pov "Good slut!"
    scene livingroom 10pm 072sof
    davide "Yes, very good. She also missed to drink just a little sperm."
    pov "Maybe something we need to train more, haha."
    davide "Oh she did already very fine. You're lucky with this slut, haha."
    jump basementnicoleoutingcorruptionshareend

label basementnicoleoutingcorruptionshareoutside:
    pov "I'll cum on your ass, slut."
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
    mom "Yes, [pov]. I like it when you put your sperm on me."
    pov "Good slut!"
    scene livingroom 10pm 072sof
    davide "Yes, very good. She also missed to drink just a little sperm."
    pov "Maybe something we need to train more, haha."
    davide "Oh she did already very fine. You're lucky with this slut, haha."
    jump basementnicoleoutingcorruptionshareend

label basementnicoleoutingcorruptionshareend:
    scene livingroom 10pm 062b
    davide "I'll go now, have some drinks and maybe I'll find Bruce and can more fun with him, haha."
    davide "Have much more fun with your slut, [pov]."
    pov "I'm done. I came twice and she had much fun too. And showing Bruce his place."
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
    pov "No, sorry Davide, but I don't think so."
    pov "My slut needs to get used more to my dick."
    if basement10pmnicoleoutingcumface == False:
        scene livingroom 10pm 061ai
    else:
        scene livingroom 10pm 061ao
    davide "Oh, you're serious."
    pov "Yes, I am."
    davide "Oh, OK. Normally I would just take what I want, but I appreciate how you'd handle Bruce..."
    davide "So you can have your fun with her alone."
    scene livingroom 10pm 062b
    davide "I'll go now, have some drinks and maybe I'll find Bruce and can more fun with him, haha."
    davide "Have much more fun with your slut, [pov]."
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
    pov "So it's time to pick a hole. Which one do you prefer?"
    mom "My opinion doesn't matter, I'm just your slut."
    pov "Oh I see. You start to like your submissive role."
    if inc == True:
        pov "That's good. I dreamt of making you my slut, mom."
    else:
        pov "That's good. I dreamt of making you my slut, [mother]."
    mom "Hmm..."
    pov "{i}So, which hole should I use now?{/i}"
    call screen basementnicoleoutingcorruptionsharenochoose

screen basementnicoleoutingcorruptionsharenochoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementnicoleoutingcorruptionsharenochoose'), Jump('basementnicoleoutingcorruptionsharenochooseass')) hovered tt.Action ("Fuck her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementnicoleoutingcorruptionsharenochoose'), Jump('basementnicoleoutingcorruptionsharenochoosepussy')) hovered tt.Action ("Fuck her pussy") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionsharenochooseass:
    $ basement10pmnicoleoutingfuckass = True
    pov "I'll need to fuck your ass now, slut! Get yourself ready."
    jump basementnicoleoutingcorruptionsharenochoosepussy

label basementnicoleoutingcorruptionsharenochoosepussy:
    if basement10pmnicoleoutingfuckass == False:
        pov "I'll need to fuck your pussy now, slut! Get yourself ready."
    mom "Hmm... yes please fuck me."
    scene livingroom 10pm 067
    pov "Oh yes, seeing my dick so near your hole is driving me crazy."
    pov "And it's all mine now, no Bruce who can disturb us anymore."
    mom "Hnn..."
    pov "You can't wait any longer, slut?"
    mom "Please stick it in, [pov]."
    if inc == True:
        pov "As you wish, slutty mom."
    else:
        pov "As you wish, slutty [mother]."
    scene livingroom 10pm 070
    mom "AAAAHNN..."
    pov "All in!"
    pov "That view is so hot, I could fuck you everyday. Maybe I'll fuck you everyday."
    pov "Would you like to get fucked everyday by me, slut?"
    mom "Hmm... hah..."
    pov "{i}Hmm... she isn't so eager than before, but I think I know the reason.{/i}"
    scene livingroom 10pm 068
    pov "You tried to play with me. Playing the eager slut to stop me talking about that loser Bruce."
    mom "No... you're wrong... hah..."
    pov "I know I'm right. You picked that loser to become your husband and..."
    pov "now you're angry because you saw how lower he got. Losing you to me without fighting."
    pov "You realize that I'm better than him like I told you."
    if inc == True:
        pov "Your own son is the best husband for you."
    else:
        pov "The son of your best friend is the best husband for you."
    mom "Hnn..."
    pov "And you know I'm the only one who has the balls to end this farce and bring our normal life back."
    pov "But this time without Bruce!"
    pov "And you being still my slut of course!"
    mom "Hnn..."
    pov "Do you think you just can stop to be my slut when this all is over?"
    if inc == True:
        pov "No, you're my slut for life now and we'll have very much sex together, mom!"
    else:
        pov "No, you're my slut for life now and we'll have very much sex together, [mother]!"
    mom "Hnn... hah... ahhh..."
    pov "{i}Wow, she clinging on me and shaking. Does she like the idea?{/i}"
    pov "Are you getting an orgasm, slut?"
    mom "Yes, [pov]. Yes, YES! HAAHH, [pov]!"
    pov "Damn..."
    pov "{i}This pushed me over the edge too...{/i}"
    call screen basementnicoleoutingcorruptionsharenocumchoose

screen basementnicoleoutingcorruptionsharenocumchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementnicoleoutingcorruptionsharenocumchoose'), Jump('basementnicoleoutingcorruptionsharenocuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementnicoleoutingcorruptionsharenocumchoose'), Jump('basementnicoleoutingcorruptionsharenocumoutside')) hovered tt.Action ("Cum over her ass") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingcorruptionsharenocuminside:
    if basement10pmnicoleoutingfuckass == True:
        pov "I'll cum in your ass, slut."
    else:
        pov "I'll cum in your pussy, slut."
    mom "Hmm..."
    pov "Ah, hnnn..."
    "You spurt your sperm inside her."
    if basement10pmnicoleoutingfuckass == True:
        scene livingroom 10pm 072ia
    else:
        scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, slut?"
    mom "Yes, [pov]. I like it when you put your sperm inside me."
    if inc == True:
        pov "And I love to deposit my sperm inside you, mom."
    else:
        pov "And I love to deposit my sperm inside you, [mother]."
    mom "Hnn..."
    $ basement10pmnicoleoutingfuckass = False
    jump basementnicoleoutingcorruptionsharenoend

label basementnicoleoutingcorruptionsharenocumoutside:
    pov "I'll cum on your ass, slut."
    mom "Hmm..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    "You spray your sperm over her ass."
    scene livingroom 10pm 072o
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, slut?"
    mom "Yes, [pov]. I like it when you put your sperm on me."
    pov "And I love to mark you as mine."
    $ basement10pmnicoleoutingfuckass = False
    jump basementnicoleoutingcorruptionsharenoend

label basementnicoleoutingcorruptionsharenoend:
    mom "Hah... hah... you're satisfied with me?"
    pov "Oh yes, I am."
    pov "I came twice and you had your fun too."
    pov "But I'm done for now and we'll continue our fun next time."
    scene black
    "You leave the basement and go to bed."
    $ basement10pmnicoleouting = True
    $ basement10pmnicoleoutingfuckass = False
    $ basement10pmnicoleoutingcumface = False
    jump skip

label basementnicoleoutingcorruptionNTR:
    davide "Hohoho, wait a second."
    pov "Hm...?"
    dad "Yes I told you it's wrong."
    scene livingroom 10pm 047aa
    davide "This isn't what I meant."
    davide "I'm the boss here so it would be only fine to let me test your slut first?"
    pov "{i}Oh shit, he's serious. What should I do?{/i}"
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
    pov "{i}Damn... that asshole.{/i}"
    pov "Yes, Davide."
    davide "Good. I'm close slut, swallow it all down."
    mom "<suck> yes..."
    davide "HNN, haha..."
    mom "<gulp> <gulp>"
    davide "Your slut has the best mouth, enjoy her like I did!"
    mom "T... thank you."
    jump basementnicoleoutingcorruption5



label basementcassandraoutingcorruption:
    hide screen locations
    hide screen townl
    scene black
    pov "{i}It's time to let the other's now that [bs] is my slut.{/i}"
    "You go down to the basement with [bs] and le her change when the others arrive."
    scene livingroom 10pm 079
    davide "So what's the important thing you want to show us today?"
    pov "It's something special that'll change some things in the gang further."
    dad "I have a bad feeling."
    davide "He already stole your wife, what could be worse? Haha."
    mom "I don't think so, I think [pov] will show us something good."
    pov "{i}Haha, yes, it'll good for me at least.{/i}"
    pov "Come out slut!"
    scene livingroom 10pm 080
    bs "Hello everyone."
    pov "Oh, yes. You choose a very sexy outfit, slut."
    pov "{i}And she's still eager to do everything right with serving the drinks, haha.{/i}"
    pov "{i}I wonder when she'll realize that her main reason to be here is something else.{/i}"
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
    pov "{i}Haha, Davide is confused. Did I really do here something new, by having more than one slut?{/i}"
    scene livingroom 10pm 083c
    dad "How can you allow this? She's your daughter."
    pov "{i}As expected. Weak Bruce has to ask his wife to interfere. But sh can help you, she's my slut too.{/i}"
    dad "I already accepted all the other humiliations, but this is going too far, don't you think so?"
    mom "Hnn..."
    scene livingroom 10pm 084c
    mom "Why is she here? I thought I am your slut?"
    dad "Ehhh?"
    davide "Hehe... hahaha..."
    scene livingroom 10pm 085c
    bs "What's going on here?"
    scene livingroom 10pm 082c
    pov "Yes, you're still my slut, but [bs] is my other slut now too."
    pov "I could get boring with just one slut, so I have you two now."
    if inc == True:
        dad "But she's your sister!"
    else:
        dad "But you know her all your life!"
    pov "Yes and that's a good reason I should be the one, taking care of her."
    mom "But..."
    pov "No more backtalking [mother]! You'll share your slut-status with her now."
    scene livingroom 10pm 086c
    if inc == True:
        bs "Mom is your slut too?"
    else:
        bs "My mom is your slut too?"
    pov "Yes and you two doing good."
    pov "And you'll have to give your best to show me which one can be a better slut for me."
    pov "{i}That little competition will give me so much fun, haha.{/i}"
    bs "Hnn..."
    pov "Now go on and show us what I teached you."
    bs "Yes, [pov]."
    scene livingroom 10pm 087c
    bs "See, it's easy."
    davide "Ehh?"
    dad "No..."
    pov "{i}Why is Bruce so surprised? Maybe his view is too good?{/i}"
    pov "{i}Haha, Davide's face. He's so confused asking himself why she's acting like a waitress all the time.{/i}"
    pov "{i}And I wonder too why she's still in that role, maybe she's so nervous?{/i}"
    scene livingroom 10pm 088c
    if inc == True:
        bs "Did I do everything good, brother?"
    else:
        bs "Did I do everything good, [pov]?"
    pov "Yes, slut. You placed the try on the table without spilling any of the drinks."
    bs "<giggle>"
    pov "{i}Hahaha, they're all so damn confused. Time to get to the main dish.{/i}"
    pov "Something cames up my mind. I wonder if the other know about your decorations, you wear under this?"
    pov "So I think you should show us."
    mom "Decorations?"
    scene livingroom 10pm 089c
    bs "You mean...? I should show them...?"
    pov "Yes! It's already almost visible, but I think we all should have a better look."
    dad "What do he mean with decorations?"
    pov "Just do it slut!"
    bs "Yes [pov]."
    scene livingroom 10pm 090c
    bs "Here you can see my decorations, hnn..."
    davide "Hell yes, this hot titties!"
    scene livingroom 10pm 091c
    dad "Aaahh..."
    davide "What wonderful decorations you have!"
    mom "Hnn...!"
    pov "Don't stare, Bruce, hahaha..."
    jump basementcassandraoutingcorruptionshare


label basementcassandraoutingcorruptionshare:
    pov "{i}Now it's time for even more fun. But who'll serve whom?{/i}"
    call screen basementcassandraoutingcorruptionsharechoose

screen basementcassandraoutingcorruptionsharechoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 667 ypos 123 action (Hide ('basementcassandraoutingcorruptionsharechoose'), Jump('basementcassandraoutingcorruptionsharecspov')) hovered tt.Action ("[bs] serve me, [mother] serve Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 800 ypos 123 action (Hide ('basementcassandraoutingcorruptionsharechoose'), Jump('basementcassandraoutingcorruptionsharenpov')) hovered tt.Action ("[mother] serve me, [bs] serve Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 975 ypos 123 action (Hide ('basementcassandraoutingcorruptionsharechoose'), Jump('basementcassandraoutingcorruptionsharecspovonly')) hovered tt.Action ("[bs] serve me, Davide get's nobody") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementcassandraoutingcorruptionsharecspov:
    $ basement10cassandraoutingnshare = True
    pov "{i}[bs] will serve me now and [mother] serve Davide, so he can have fun too.{/i}"
    pov "{i}And he'll see that I'm accept his higher position... for now.{/i}"
    pov "Come here and get on your knees, [bs]! I need some service now!"
    scene livingroom 10pm 093ns
    bs "You mean now?"
    pov "Yes, I know what I said."
    bs "But... they'll still sitting there..."
    pov "I know. Now stop talking and do your duty. I won't start another discussion about this!"
    pov "Haha, and I see you too Davide, don't worry."
    bs "O... OK, [pov]."
    scene livingroom 10pm 092cs
    bs "<suck> <lick>"
    pov "Good, I see you know your place slut."
    pov "Now give your best and just ignore the others. You must learn to follow my orders."
    bs "Y... yes [pov]. <lick>"
    scene livingroom 10pm 094ns
    pov "And you'll serve Davide now, [mother]. It's rude to let him sit there alone."
    mom "Yes, of course [pov]."
    dad "Grr...."
    davide "Do not even think about to say something, Bruce!"
    dad "Hnn..."
    scene livingroom 10pm 093cs
    bs "<lick> <lick>"
    pov "And you're keep working on me, good slut."
    if inc == True:
        bs "Thank you, brother."
    else:
        bs "Thank you, [pov]."
    pov "You'll learn fast how we do this here and you'll have fun too."
    bs "Hmm..."
    pov "{i}Damn, this is working out so good.{/i}"
    scene livingroom 10pm 095ns
    pov "And you're happy too?"
    davide "Look at me, crybaby!"
    pov "{i}Oh, he's bullying Bruce again. Haha, poor Bruce.{/i}"
    if inc == True:
        pov "{i}And mom can learn that she's isn't alone anymore and need to be a better slut.{/i}"
    else:
        pov "{i}And [mother] can learn that she's isn't alone anymore and need to be a better slut.{/i}"
    scene livingroom 10pm 093cs
    if inc == True:
        pov "And you're giving your best too, big sis?"
        bs "Yes, I try brother."
    else:
        pov "And you're giving your best too, [bs]?"
        bs "Yes, I try [pov]."
    if casbjdt >= 2:
        bs "Should I go more down on you?"
        pov "You mean deepthroat?"
        bs "Yes, you want me doing it?"
        pov "What a nice slut you are, caring that much for me."
        call screen basementcassandraoutingcorruptioncasbj
    else:
        jump basementcassandraoutingcorruptioncasbjnormal

screen basementcassandraoutingcorruptioncasbj():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementcassandraoutingcorruptioncasbj'), Jump('basementcassandraoutingcorruptioncasbjdt')) hovered tt.Action ("Deepthroat me") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementcassandraoutingcorruptioncasbj'), Jump('basementcassandraoutingcorruptioncasbjnormal')) hovered tt.Action ("Give me a normal blowjob") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementcassandraoutingcorruptioncasbjdt:
    pov "Yes, I want you to deepthroat me, slut."
    bs "Okay... [pov]."
    scene livingroom 10pm 095dtcs
    pov "Oh yes, work your way down on me."
    bs "Hnng... <suck> <choke>"
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 096ns
        davide "You have even more good ideas [pov]. It seems I really underestimated you, haha."
        mom "<suck> <lick>"
        pov "So my other slut is doing a good job on you?"
        davide "Haha, you know her mouth so you know the answer."
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
        pov "{i}Oh poor Bruce is crying... He got even weaker.{/i}"
        davide "Swallow my spunk!"
        mom "Hnn... <gulp>"
        pov "{i}Hmm, he already came, so [mother] did a good job.{/i}"
        pov "{i}But thinking of that, [bs] is getting me close too.{/i}"
    scene livingroom 10pm 096dtcs
    pov "I'm close and will cum now slut."
    jump basementcassandraoutingcorruptioncasbjcum

label basementcassandraoutingcorruptioncasbjnormal:
    pov "Just give me a normal blowjob, slut."
    bs "Okay... [pov]."
    scene livingroom 10pm 094cs
    bs "<suck> <lick>"
    pov "Oh yes, just like that."
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 096ns
        davide "You have even more good ideas [pov]. It seems I really underestimated you, haha."
        mom "<suck> <lick>"
        pov "So my other slut is doing a good job on you?"
        davide "Haha, you know her mouth so you know the answer."
    pov "You're doing very good, don't worry."
    if inc == True:
        pov "Not as good as mom, but you can get better, I'm sure."
    else:
        pov "Not as good as your mom, but you can get better, I'm sure."
    bs "Hmm... <suck>"
    scene livingroom 10pm 095ics
    pov "Ohh, this is nice."
    pov "{i}She pleasing my tip, that's something new.{/i}"
    bs "Hnn... <lick>"
    if basement10cassandraoutingnshare == True:
        scene livingroom 10pm 097cns
        davide "Hah... yes, suck it slut!"
        dad "<sob>"
        pov "{i}Oh poor Bruce is crying... He got even weaker.{/i}"
        davide "Swallow my spunk!"
        mom "Hnn... <gulp>"
        pov "{i}Hmm, he already came, so [mother] did a good job.{/i}"
        pov "{i}But thinking of that, [bs] is getting me close too.{/i}"
    scene livingroom 10pm 095ics
    pov "I'm close and will cum now slut."
    jump basementcassandraoutingcorruptioncasbjcum

label basementcassandraoutingcorruptioncasbjcum:
    call screen basementcassandraoutingcorruptioncasbjcumchoose

screen basementcassandraoutingcorruptioncasbjcumchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 567 ypos 123 action (Hide ('basementcassandraoutingcorruptioncasbjcumchoose'), Jump('basementcassandraoutingcorruptioncasbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1375 ypos 123 action (Hide ('basementcassandraoutingcorruptioncasbjcumchoose'), Jump('basementcassandraoutingcorruptioncasbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementcassandraoutingcorruptioncasbjcumin:
    pov "I'll cum in your mouth!"
    bs "Hmm..."
    pov "Aaahhh... yes..."
    "You spray your sperm in her mouth."
    bs "Hnn..."
    scene livingroom 10pm 096ics
    bs "Hnn..."
    pov "{i}Damn, is she smiling?{/i}"
    pov "Good, slut, don't forget to swallow all I gave you."
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
    "You spray your sperm on her face."
    bs "Hnn..."
    scene livingroom 10pm 096ocs
    bs "You came so much on me... hnn..."
    pov "You should be proud. That shows you how much I appreciate your doing."
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
        "After all of you had your fun, except Bruce, you decide to call it a night and leave the basement."
    else:
        "After you had your fun, you decide to call it a night and leave the basement."
    $ basement10cassandraouting = True
    $ basement10cassandraoutingnshare = False
    $ basement10cassandraoutingcshare = False
    jump skip

label basementcassandraoutingcorruptionsharenpov:
    $ basement10cassandraoutingcshare = True
    pov "{i}[mother] will serve me now and [bs] serve Davide, so he can have fun too.{/i}"
    pov "{i}And he'll see that I'm accept his higher position... for now.{/i}"
    scene livingroom 10pm 092ns
    if inc == True:
        pov "Come here and get on your knees, mom! I need some service now!"
    else:
        pov "Come here and get on your knees, [mother]! I need some service now!"
    mom "Huh? Y-yes, [pov]..."
    pov "{i}Haha, I wonder if Bruce will be able to close his mouth again?{/i}"
    scene livingroom 10pm 048a
    mom "<suck> <lick>"
    pov "Good, you know how to serve."
    bs "Huh?"
    scene livingroom 10pm 093ns
    if inc == True:
        bs "Mom is sucking on your dick?"
    else:
        bs "My mother is sucking on your dick?"
    pov "Yes, I haven chosen her to serve me."
    pov "{i}Haha, Davide can't wait.{/i}"
    pov "And you'll serve Davide with your mouth."
    bs "D-Davide? But I thought..."
    pov "Stop! You're not here to think, you're here to serve."
    pov "So do what I told you and show me that you can be a good slut."
    bs "Hnn... yes [pov]."
    scene livingroom 10pm 094ncs
    bs "I'm sorry that I hesitated, Davide. I'll serve you good."
    davide "Oh yes, I'm sure you will. Especially your mouth, haha."
    pov "{i}That'll show her that she need to give her best to please me as a slut and has competition too.{/i}"
    dad "This needs to... stop..."
    davide "Shut up Bruce!"
    scene livingroom 10pm 048a
    pov "And you're proud that I choose you to serve me?"
    mom "Hnn..."
    if inc == True:
        pov "You should be, mom! You and [bs] will serve me good and everything will stay in the family."
    else:
        pov "You should be, [mother]! You and [bs] will serve me good and everything will stay in your family."
    mom "Hmm..."
    pov "I need to hear it from you."
    mom "I... I'm pround you'd chosen me, [pov]."
    pov "Good slut."
    pov "{i}How should I let her continue? Should she get me off on her own or should I help her?{/i}"
    call screen basementcassandraoutingcorruptionnicbj

screen basementcassandraoutingcorruptionnicbj():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementcassandraoutingcorruptionnicbj'), Jump('basementcassandraoutingcorruptionnicbjdt')) hovered tt.Action ("Help her (deethroat)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementcassandraoutingcorruptionnicbj'), Jump('basementcassandraoutingcorruptionnicbjnormal')) hovered tt.Action ("Let her continue") focus_mask True


    frame:
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
    pov "{i}Oh, he's bullying Bruce again. Haha, poor Bruce.{/i}"
    scene livingroom 10pm 048adt
    if inc == True:
        pov "You hear that slut? Everyone is happy with you and big sis serving us."
    else:
        pov "You hear that slut? Everyone is happy with you and your daughter serving us."
    mom "Hnn..."
    pov "Oh, so you're not convinced yet? You'll be very soon."
    scene livingroom 10pm 096ncs
    davide "You have even more good ideas [pov]. It seems I really underestimated you, haha."
    bs "<suck> <lick>"
    pov "So my other slut is doing a good job on you?"
    davide "Haha, you know her mouth so you know the answer."
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
    pov "{i}Oh poor Bruce is crying... He got even weaker.{/i}"
    davide "Swallow my spunk!"
    bs "Hnn... <gulp>"
    pov "{i}Hmm, he already came, so [bs] did a good job.{/i}"
    pov "{i}But thinking of that, [mother] is getting me close too.{/i}"
    scene livingroom 10pm 049adt
    pov "I'm close and will cum now slut."
    call screen basementcassandraoutingcorruptionnicbjcum

label basementcassandraoutingcorruptionnicbjnormal:
    pov "Just continue what you're doing, slut."
    mom "Okay... [pov]."
    scene livingroom 10pm 095ncs
    davide "Oh yes, that's how I like it. Make it wet before it goes deep in your mouth."
    davide "Look how good she can serve, Bruce!"
    dad "No... this is wrong..."
    pov "{i}Oh, he's bullying Bruce again. Haha, poor Bruce.{/i}"
    scene livingroom 10pm 049a
    if inc == True:
        pov "You hear that slut? Everyone is happy with you and big sis serving us."
    else:
        pov "You hear that slut? Everyone is happy with you and your daughter serving us."
    mom "Hnn..."
    pov "Oh, so you're not convinced yet? You'll be very soon."
    scene livingroom 10pm 096ncs
    davide "You have even more good ideas [pov]. It seems I really underestimated you, haha."
    bs "<suck> <lick>"
    pov "So my other slut is doing a good job on you?"
    davide "Haha, you know her mouth so you know the answer."
    scene livingroom 10pm 049a
    pov "You're doing very good, don't worry."
    mom "Hmm... <lick>"
    scene livingroom 10pm 097ncs
    davide "Hah... yes, suck it slut!"
    dad "<sob>"
    pov "{i}Oh poor Bruce is crying... He got even weaker.{/i}"
    davide "Swallow my spunk!"
    bs "Hnn... <gulp>"
    pov "{i}Hmm, he already came, so [bs] did a good job.{/i}"
    pov "{i}But thinking of that, [mother] is getting me close too.{/i}"
    scene livingroom 10pm 048a
    pov "I'm close and will cum now slut."
    call screen basementcassandraoutingcorruptionnicbjcum




screen basementcassandraoutingcorruptionnicbjcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementcassandraoutingcorruptionnicbjcum'), Jump('basementcassandraoutingcorruptionnicbjcumin')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementcassandraoutingcorruptionnicbjcum'), Jump('basementcassandraoutingcorruptionnicbjcumout')) hovered tt.Action ("Cum on her face") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementcassandraoutingcorruptionnicbjcumin:
    pov "I'll cum in your mouth!"
    mom "Hmm..."
    pov "Aaahhh... yes..."
    "You spray your sperm in her mouth."
    mom "Hnn..."
    scene livingroom 10pm 051i
    mom "Hnn..."
    pov "Good, slut, don't forget to swallow all I gave you."
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
    davide "Even if I wished she would be your real daughter."
    jump basementcassandraoutingcorruptionend

label basementcassandraoutingcorruptionnicbjcumout:
    pov "I'll cum on your face!"
    mom "Hmm..."
    pov "Aaahhh... yes..."
    scene livingroom 10pm 050o
    "You spray your sperm on her face."
    mom "Hnn..."
    scene livingroom 10pm 051o
    mom "You came so much on me... hnn..."
    pov "You should be proud. That shows you how much I appreciate your doing."
    mom "Hmm..."
    scene livingroom 10pm 098ncs
    davide "Look at her Bruce! She swallowed it all."
    bs "Hah... hah..."
    davide "You can be proud of your step-daughter, haha."
    davide "Even if I wished she would be your real daughter."
    jump basementcassandraoutingcorruptionend


label basementcassandraoutingcorruptionsharecspovonly:
    pov "{i}[bs] will serve me now and [mother] will have to watch.{/i}"
    pov "Come here and get on your knees, [bs]! I need some service now!"
    scene livingroom 10pm 093ns
    bs "You mean now?"
    pov "Yes, I know what I said."
    bs "But... they'll still sitting there..."
    pov "I know. Now stop talking and do your duty. I won't start another discussion about this!"
    pov "I see you want to have fun too Davide, but I must disappoint you."
    pov "I need [mother] to watch this, so she can accept it better."
    davide "Hnnn, this make sense. You can have your way... this time..."
    bs "O... OK, [pov]."
    scene livingroom 10pm 092cs
    bs "<suck> <lick>"
    pov "Good, I see you know your place slut."
    pov "Now give your best and just ignore the others. You must learn to follow my orders."
    bs "Y... yes [pov]. <lick>"
    scene livingroom 10pm 094ns
    pov "And make sure you watch closely and don't miss anything, [mother]."
    dad "You don't need to do this."
    davide "Shut up Bruce and enjoy the show!"
    mom "Y- yes [pov]."
    scene livingroom 10pm 093cs
    bs "<lick> <lick>"
    pov "And you're keep working on me, good slut."
    if inc == True:
        bs "Thank you, brother."
    else:
        bs "Thank you, [pov]."
    pov "You'll learn fast how we do this here and you'll have fun too."
    bs "Hmm..."
    pov "{i}Damn, this is working out so good.{/i}"
    scene livingroom 10pm 093cs
    if inc == True:
        pov "And you're giving your best, big sis?"
        bs "Yes, I try brother."
    else:
        pov "And you're giving your best, [bs]?"
        bs "Yes, I try [pov]."
    if casbjdt >= 2:
        bs "Should I go more down on you?"
        pov "You mean deepthroat?"
        bs "Yes, you want me doing it?"
        pov "What a nice slut you are, caring that much for me."
        call screen basementcassandraoutingcorruptioncasbj
    else:
        jump basementcassandraoutingcorruptioncasbjnormal


label basementcassandraoutingcorruptionfail:
    hide screen locations
    hide screen townl
    scene black
    pov "{i}It's time to let the other's now that [bs] is my slut.{/i}"
    "You go down to the basement with [bs] and le her change when the others arrive."
    scene livingroom 10pm 079
    davide "So what's the important thing you want to show us today?"
    pov "It's something special that'll change some things in the gang further."
    dad "I have a bad feeling."
    mom "I don't think so, I think [pov] will show us something good."
    pov "{i}Haha, yes, it'll good for me at least.{/i}"
    pov "Come out slut!"
    scene livingroom 10pm 080
    bs "Hello everyone."
    pov "Oh, yes. You choose a very sexy outfit, slut."
    pov "{i}And she's still eager to do everything right with serving the drinks, haha.{/i}"
    pov "{i}I wonder when she'll realize that her main reason to be here is something else.{/i}"
    scene livingroom 10pm 081
    dad "..."
    mom "..."
    davide "... hahahaha..."
    bs "Guys?"
    pov "I know she's hot, but you can calm down, haha."
    scene livingroom 10pm 082l
    mom "What the hell you think you're doing [bs]!"
    davide "..."
    pov "Huh?"
    mom "Now you're got yourself into real trouble, young lady!"
    pov "{i}Shit. This isn't the way it's suppose to be.{/i}"
    scene livingroom 10pm 083l
    mom "And you're into big trouble too."
    if inc == True:
        mom "Talking your big sister into this."
    else:
        mom "Talking my daughter into this."
    mom "What are you thinking, making her your slut?"
    if mombasementcorsecond == True:
        pov "But you're my slut too."
        mom "How dare you, I'll kick you out of my house if you say that again!"
        pov "{i}Damn, she already gave in to me, but maybe she don't want to [bs] know about it.{/i}"
    pov "I'm sorry."
    mom "You better be."
    scene livingroom 10pm 084l
    mom "Come and put that damn tray away! You're dressed like a slut!"
    pov "{i}Say the woman dresses as a slut too, haha. This could be funny when she won't cockblocking me.{/i}"
    if mombasementcorsecond == True:
        pov "{i}But I wonder why she's getting so angry? Maybe I should have do her outing first, so everyone knows that she's my slut already.{/i}"
    else:
        pov "{i}I need to think of something so I can have [bs] as my slut down here.{/i}"
    scene livingroom 10pm 085l
    bs "I'm sorry mom."
    mom "Oh yes, you'll be sorry when I'm done with you. Come with me now, in your room."
    bs "I really thought I could do this."
    mom "You better forgot about this! I'll deal with [pov] later."
    scene livingroom 10pm 086l
    "After they left the basement."
    davide "It's all your fault, asshole!"
    dad "What? You're serious?"
    davide "She's your wife and you let her interfere. A real man had shown her her place."
    pov "{i}Hmm... I wonder why Davide didn't do anything then?{/i}"
    scene livingroom 10pm 087l
    dad "But he's the one bringing [bs] down here."
    davide "Yes and it's his right and your annoying wife should respect this!"
    dad "But you saw how angy that made her."
    davide "I don't care about your excuses!"
    scene livingroom 10pm 088l
    davide "You'll go now after them and get things right."
    davide "I want to see that hot chick to as a part of our gang."
    dad "What are you saying?"
    davide "Stop talking, loser! Do your duty now and go!"
    dad "But..."
    davide "GO!"
    scene livingroom 10pm 089l
    "Bruce went after them."
    davide "I really appreciate your effort bringing such a hot girl in the gang, bro!"
    pov "Well, but it didn't play out as it was planned."
    scene livingroom 10pm 090l
    davide "No problem for now, the idea alone was fantastic."
    davide "I'm sure it'll work out at a time and then I have another reason to have my fun with that loser Bruce, haha."
    pov "{i}Oh he's favourite hobby, bullying Bruce.{/i}"
    scene livingroom 10pm 091l
    davide "But you better think of a plan \"B\". I'm sure Bruce will chicken out so you have to fix it."
    pov "{i}Well, his mood changed fast.{/i}"
    pov "Yes, don't worry. I can fix this."
    scene black
    $ basement10cassandraoutingfail = True
    "Disappointed you leave the basement."
    jump skip



label irinadatetemple:
    hide screen locations
    hide screen townl
    show screen phone
    $ activateirinadate = False
    if messageirina == 2:
        $ messageirina = 0
    scene black
    "You sent a positive reply to Irina."
    "You decide to meet at the restaurant."
    if irinadatetemplefirst == True:
        jump irinadatetemplemore
    scene date 10pm 001b
    irina "Hey [pov]!"
    pov "Oh, hey [irina]."
    pov "{i}Wow, this dress is damn hot.{/i}"
    irina "So I see you like my dress."
    pov "Oh yes, very sexy."
    scene date 10pm 002b
    pov "{i}It's so short and her long, bare legs, and showing her naked feet.{/i}"
    pov "{i}She really know how to dress to make her date go wild, haha.{/i}"
    scene date 10pm 001b
    irina "So I gave you a good first impression? <giggle>"
    pov "Oh yeah. I'm positive surprised."
    irina "But you're looking good too, like a gentleman with your fine clothing."
    pov "So we can approve both to each others clothing, haha."
    irina "Haha, yes..."
    call screen irinadatetemplegreet

screen irinadatetemplegreet():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 867 ypos 123 action (Hide ('irinadatetemplegreet'), Jump('irinadatetemplegreetcor')) hovered tt.Action ("Let her turn around [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1375 ypos 123 action (Hide ('irinadatetemplegreet'), Jump('irinadatetemplegreetlove')) hovered tt.Action ("Kiss her hand [lv1]") focus_mask True


    frame:
        xalign .5
        text tt.value


label irinadatetemplegreetcor:
    pov "How about you turn around and show me the rest of your dress?"
    irina "OK."
    scene date 10pm 003bc
    pov "{i}It's so damn short. I'll have much fun with her.{/i}"
    pov "It's very nice."
    irina "I'm glad you like it."
    $ irinacorruption += 1
    jump irinadatetemple2

label irinadatetemplegreetlove:
    scene date 10pm 003bl
    pov "Come here, my lady."
    pov "<kiss>"
    irina "Ohh... <giggle>"
    irina "You're the first guy that ever kissed my hand."
    $ irinalove += 1
    jump irinadatetemple2

label irinadatetemple2:
    scene date 21pm 002
    "Waitress" "Your table is ready. If you please follow me."
    call screen irinadatetemplewalk

screen irinadatetemplewalk():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 667 ypos 123 action (Hide ('irinadatetemplewalk'), Jump('irinadatetemplewalkcor')) hovered tt.Action ("Grope [irina] [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1175 ypos 123 action (Hide ('irinadatetemplewalk'), Jump('irinadatetemplewalklove')) hovered tt.Action ("Put your arm around her [lv1]") focus_mask True


    frame:
        xalign .5
        text tt.value

label irinadatetemplewalkcor:
    pov "Come [irina]."
    scene date 10pm 004bc
    irina "Huh? So you can't wait? <giggle>"
    pov "Your ass is made for groping."
    irina "<giggle>"
    $ irinacorruption += 1
    jump irinadatetemple3

label irinadatetemplewalklove:
    pov "Come [irina]."
    scene date 10pm 004bl
    irina "Oh? How nice. <giggle>"
    pov "Yes, a lady like you need someone to hold on."
    irina "<giggle>"
    $ irinalove += 1
    jump irinadatetemple3

label irinadatetemple3:
    scene date 10pm 005b
    irina "I didn't know that they're so big."
    pov "{i}I love this decorations. Everyone stops by and I can admire her beauty.{/i}"
    pov "{i}How hot she is in this dress. And almost naked.{/i}"
    scene date 10pm 006bc
    irina "It's very elegant and classy here. I never was at such a place before."
    call screen irinadatetemplesit

screen irinadatetemplesit():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 767 ypos 123 action (Hide ('irinadatetemplesit'), Jump('irinadatetemplesitnothing')) hovered tt.Action ("Do nothing") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1375 ypos 123 action (Hide ('irinadatetemplesit'), Jump('irinadatetemplesitlove')) hovered tt.Action ("Be a gentleman [lv1]") focus_mask True


    frame:
        xalign .5
        text tt.value

label irinadatetemplesitnothing:
    pov "So you see how special you're to me. Let's sit."
    irina "Yes. <giggle>"
    jump irinadatetemple4

label irinadatetemplesitlove:
    pov "Wait!"
    irina "Huh?"
    scene date 10pm 006bl
    pov "When it's so classy I need to do this right too."
    irina "Oh, this is so nice of you, [pov]!"
    pov "Please have a sit, my lady."
    irina "<giggle>"
    $ irinalove += 1
    jump irinadatetemple4

label irinadatetemple4:
    scene date 10pm 007b
    pov "Let me ask you something."
    irina "Go on."
    pov "I wonder why you're so interested in me? I'm just a guy like others, but you behave around me like I would be someone special."
    irina "You're special. <giggle>"
    if irinacorruption >= irinalove:
        irina "You're like a typical guy, but still better as the guys here. There total machos."
    else:
        irina "You're not like a typical guy, you're more a gentleman. Guys here are total machos."
    pov "Like treat girls like they're property and such shit?"
    irina "Yes. And even worse, like sluts. I never met a guy nice like you."
    irina "I dream of finding a guy like you and leave with him this shithole to have a normal life."
    pov "So you hate it here?"
    irina "Yes, and there no perspectives here, no jobs, unless you want to be a criminal."
    pov "Oh, so bad."
    pov "But you're still very positive for this shit around you."
    irina "Yes, being sad isn't something that fits me."
    irina "And I love it to be spontaneous and adventurous."
    irina "That's also a reason, why [bs] and I are so good friends."
    pov "Oh, that makes sense."
    irina "And I love the life!"
    if inc == True:
        irina "And hot brothers of [bs]. <giggle>"
    else:
        irina "And hot friends of [bs]. <giggle>"
    call screen irinadatetemplebehaviour

screen irinadatetemplebehaviour():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 567 ypos 123 action (Hide ('irinadatetemplebehaviour'), Jump('irinadatetemplebehaviourcor')) hovered tt.Action ("Use her dream [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1275 ypos 123 action (Hide ('irinadatetemplebehaviour'), Jump('irinadatetemplebehaviourlove')) hovered tt.Action ("Be nice to her [lv1]") focus_mask True


    frame:
        xalign .5
        text tt.value

label irinadatetemplebehaviourcor:
    pov "So you're lucky. I can be that special guy saving you."
    irina "<giggle> I knew it."
    pov "But we need to hide our great plans for now, they're many haters out there."
    irina "Oh..."
    pov "And so it's better I'll behave just like another guy for some time."
    scene date 10pm 007bc
    irina "You mean like treat me like a slut?"
    pov "You're no slut to me, but yes, I have to play the macho. For some time."
    irina "Oh..."
    pov "But you can trust your instinct, you've chosen right. We'll leave this shithole for sure. Together!"
    pov "{i}When you're my slut, of course, haha.{/i}"
    irina "O... okay [pov]. I think you're trustable."
    if inc == True:
        irina "You're still the brother of [bs]."
    else:
        irina "[bs] knows you for so long."
    $ irinacorruption += 1
    jump irinadatetemplewine

label irinadatetemplebehaviourlove:
    pov "So you're lucky. I can be that special guy saving you."
    irina "<giggle> I knew it."
    pov "I'll treat you like a lady all the time. You need to learn something else than the bad places."
    scene date 10pm 007bl
    irina "Aww... <giggle>"
    pov "You'll be buried under compliments and learn the gentle side of love."
    irina "Oh, please never stop talking so nice to me."
    pov "I would, but we're here to eat too, haha."
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
    pov "Haha, slowly. It's no need to get drunk."
    scene date 10pm 010bc
    irina "I'm still a little nervous."
    pov "Don't be."
    call screen irinadatetemplepanties

screen irinadatetemplepanties():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 567 ypos 123 action (Hide ('irinadatetemplepanties'), Jump('irinadatetemplepantiescor')) hovered tt.Action ("Challenge her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1275 ypos 123 action (Hide ('irinadatetemplepanties'), Jump('irinadatetemplepantiesnothing')) hovered tt.Action ("Do nothing") focus_mask True


    frame:
        xalign .5
        text tt.value


label irinadatetemplepantiescor:
    pov "I have a idea to distract you from your nervousness."
    pov "And it's spontaneous and adventurous, so perfect for you."
    irina "What is it?"
    pov "Give me your panties!"
    irina "R-right now?"
    pov "Yes, the danger will let you forget your nervousness and you can show me that you're a good girl."
    scene date 10pm 011bc
    irina "Hmm... I still can trust you? You won't do anything bad out of this situation?"
    pov "Of course not! It'll be our secret."
    scene date 10pm 012bc
    pov "And I always wanted to have your panties, haha."
    irina "Hnn..."
    pov "{i}Did she really do it? I need to check it.{/i}"
    scene date 10pm 015bc
    pov "{i}Oh shit, she did it. And her panties are here on the floor.{/i}"
    "You take her panties."
    pov "{i}Sitting here naked just to prove me that she can be a good girl.{/i}"
    scene date 10pm 013bc
    pov "Oh..."
    "Waitress" "This is for you."
    pov "{i}Ha, [irina] is confused. Does she really think I'll tell something? When we can have so much more fun instead.{/i}"
    irina "T-thank you."
    scene date 10pm 014bc
    "Waitress" "And yours, Sir."
    pov "Thank you."
    pov "{i}Haha, I bet [irina] want her to go fast, she's still uneasy.{/i}"
    scene date 10pm 016bc
    pov "You can be glad, you're a good girl."
    irina "Hn... thank you."
    pov "See, I bet you're not nervous about our date anymore."
    irina "No..."
    pov "Good, enjoy your meal."
    irina "Thank you."
    $ irinacorruption += 1
    $ irinadatetemplepantyoff = True
    jump irinadatetempleconversation

label irinadatetemplepantiesnothing:
    pov "There's really no need to be nervous around me, just be yourself."
    pov "I already decided to go out with you [irina]."
    scene date 10pm 010bl
    irina "Yes, I'll try. <giggle>"
    pov "See, your lovely smile is back."
    irina "You're so sweet, I still can't believe it."
    pov "Then don't wake up!"
    irina "Haha..."
    scene date 10pm 013bl
    irina "Oh that looks tasty."
    "Waitress" "This is for you."
    pov "For you just the best food [irina]."
    scene date 10pm 014bl
    "Waitress" "And yours, Sir."
    pov "Thank you."
    pov "{i}She has her fun, being treated like a lady from others too.{/i}"
    scene date 10pm 015bl
    pov "Feeling special?"
    irina "It's just amazing. She's so nice to me and the food looks so tasty."
    pov "All the special things for my lovely date."
    irina "Let's enjoy the food."
    pov "Yes."
    jump irinadatetempleconversation


label irinadatetempleconversation:
    call screen irinadatetempleconversation2

screen irinadatetempleconversation2():

    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 567 ypos 123 action (Hide ('irinadatetempleconversation2'), Jump('irinadatetempleconversationcor')) hovered tt.Action ("Treat her like a slut [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 1275 ypos 123 action (Hide ('irinadatetempleconversation2'), Jump('irinadatetempleconversationlove')) hovered tt.Action ("Treat her like a lady [lv1]") focus_mask True


    frame:
        xalign .5
        text tt.value

label irinadatetempleconversationcor:
    scene date 10pm 017bc
    "You have a long talk while eating."
    "You direct the conversation into explaining her why she needs to be a good girl for you."
    $ irinacorruption += 1
    if irinadatetemplefirst == True:
        jump irinadatetemplerewardsecond
    else:
        jump irinadatetempleleave

label irinadatetempleconversationlove:
    scene date 10pm 016bl
    "You have a long talk while eating."
    "You admire her and giving her much compliments."
    $ irinalove += 1
    if irinadatetemplefirst == True:
        jump irinadatetemplerewardsecond
    else:
        jump irinadatetempleleave

label irinadatetempleleave:
    scene black
    "After eating you leave the restaurant together and take a taxi to her home."
    "You decide to bring her back to her house, since you realize that she's living near to yourself."
    scene date 10pm 030
    irina "Now we're here. This is my parents house."
    pov "Oh you're living still at home? Just like me, haha."
    irina "Yes, I don't have the money to live alone."
    pov "Soon, haha."
    irina "<giggle>"
    if irinacorruption >= irinalove:
        scene date 10pm 031c
    else:
        scene date 10pm 031l
    pov "So now it's the time you invite me to your room?"
    irina "You mean right now?"
    pov "Yes, wouldn't that be nice?"
    irina "Hmm... but my parents still at home."
    if NTR == True and irinarelationship <= 5:
        jump irinadatetempleNTR
    if irinacorruption >= irinalove:
        scene date 10pm 032c
    else:
        scene date 10pm 032l
    pov "So it's a \"no\"?"
    irina "I'm sorry [pov], but my father would get very mad if I would do that."
    pov "Oh, I can understand why, haha."
    irina "I never bring a man at home, father would kill you."
    if irinacorruption >= irinalove:
        scene date 10pm 033c
    else:
        scene date 10pm 033l
    irina "But I promise I'll make up to you another time <giggle>"
    irina "The date was so nice, you really deserve a treat."
    pov "Oh, sounds promising."
    jump irinadatetemplerewardsecond

label irinadatetemplerewardsecond:
    if NTR == True and irinarelationship <= 5:
        jump irinadatetempleNTR
    if irinacorruption >= irinalove:
        scene date 10pm 032c
    else:
        scene date 10pm 032l
    irina "<giggle>"
    if irinadaterewardcheekfirst == False and irinalove >= irinacorruption:
        jump irinadaterewardcheek
    if irinadaterewardfkissfirst == False and irinalove >= irinacorruption and irinalove >= 10:
        jump irinadaterewardfkiss
    if irinadaterewarddickgrabfirst == False and irinalove >= irinacorruption and irinalove >= 20:
        jump irinadaterewarddickgrab
    if irinadaterewardflashfirst == False and irinalove >= irinacorruption and irinalove >= 30:
        jump irinadaterewardflash
    if irinadaterewardhandjobfirst == False and irinalove >= irinacorruption and irinalove >= 40:
        jump irinadaterewardhandjob
    if irinadaterewardblowjobfirst == False and irinalove >= irinacorruption and irinalove >= 50:
        jump irinadaterewardblowjob
    call screen irinadatetemplereward

screen irinadatetemplereward():
    default tt = Tooltip (" ")

    fixed:

        if irinacorruption >= 1:
            imagebutton auto "gui/icons/icon_french_kiss_corruption_%s.png" xpos 1467 ypos 123 action (Hide ('irinadatetemplereward'), Jump('irinadatetemplerewardfkiss')) hovered tt.Action ("French kiss her [cr1]") focus_mask True
        if irinacorruption >= 10:
            imagebutton auto "gui/icons/icon_fondle_tits_%s.png" xpos 1467 ypos 223 action (Hide ('irinadatetemplereward'), Jump('irinadatetemplerewardgrope')) hovered tt.Action ("Grope her tits [cr1]") focus_mask True
        if irinacorruption >= 20:
            imagebutton auto "gui/icons/icon_finger_corruption_%s.png" xpos 1467 ypos 323 action (Hide ('irinadatetemplereward'), Jump('irinadatetemplerewardfinger')) hovered tt.Action ("Finger her [cr1]") focus_mask True
        if irinacorruption >= 30:
            imagebutton auto "gui/icons/icon_handjob_corruption_%s.png" xpos 1467 ypos 423 action (Hide ('irinadatetemplereward'), Jump('irinadatetemplerewardhandjob')) hovered tt.Action ("Demand a handjob [cr1]") focus_mask True
        if irinacorruption >= 40:
            imagebutton auto "gui/icons/icon_blowjob_corruption_%s.png" xpos 1467 ypos 523 action (Hide ('irinadatetemplereward'), Jump('irinadatetemplerewardblowjob')) hovered tt.Action ("Demand a blowjob [cr1]") focus_mask True
        if irinacorruption >= 50:
            imagebutton auto "gui/icons/icon_sex_corruption_%s.png" xpos 1467 ypos 623 action (Hide ('irinadatetemplereward'), Jump('irinadatetemplerewardsex')) hovered tt.Action ("Fuck her [cr1]") focus_mask True

        if irinadaterewardcheekfirst == True:
            imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 441 ypos 123 action (Hide ('irinadatetemplereward'), Jump('irinadaterewardcheek')) hovered tt.Action ("Ask for a kiss [lv1]") focus_mask True
        if irinadaterewardfkissfirst == True and irinalove >= 10:
            imagebutton auto "gui/icons/icon_french_kiss_love_%s.png" xpos 441 ypos 223 action (Hide ('irinadatetemplereward'), Jump('irinadaterewardfkiss')) hovered tt.Action ("Ask for a french kiss [lv1]") focus_mask True
        if irinadaterewarddickgrabfirst == True and irinalove >= 20:
            imagebutton auto "gui/icons/icon_unihand_love_%s.png" xpos 441 ypos 323 action (Hide ('irinadatetemplereward'), Jump('irinadaterewarddickgrab')) hovered tt.Action ("Ask for a touch [lv1]") focus_mask True
        if irinadaterewardflashfirst == True and irinalove >= 30:
            imagebutton auto "gui/icons/icon_hug_%s.png" xpos 441 ypos 423 action (Hide ('irinadatetemplereward'), Jump('irinadaterewardflash')) hovered tt.Action ("Ask for a flash [lv1]") focus_mask True
        if irinadaterewardhandjobfirst == True and irinalove >= 40:
            imagebutton auto "gui/icons/icon_handjob_love_%s.png" xpos 441 ypos 523 action (Hide ('irinadatetemplereward'), Jump('irinadaterewardhandjob')) hovered tt.Action ("Ask for a handjob [lv1]") focus_mask True
        if irinadaterewardblowjobfirst == True and irinalove >= 50:
            imagebutton auto "gui/icons/icon_mouth_love_%s.png" xpos 441 ypos 623 action (Hide ('irinadatetemplereward'), Jump('irinadaterewardblowjob')) hovered tt.Action ("Ask for a blowjob [lv1]") focus_mask True


    frame:
        xalign .5
        text tt.value

label irinadatetemplerewardfkiss:
    pov "I need a reward."
    irina "Huh?"
    scene date 10pm 035c
    pov "<kiss>"
    "You give her a french kiss."
    irina "Hmm..."
    scene date 10pm 036c
    irina "Hnn... why did you do that?"
    pov "Because I want to kiss you."
    irina "But my parents..."
    pov "You want to be a good girl. So you need to reward me after a good date."
    pov "Don't you think so?"
    irina "Hnn... yes... you're right."
    pov "Good girl."
    jump irinadatetemplecorruptionend

label irinadatetemplerewardgrope:
    pov "I need a reward."
    irina "Huh?"
    scene date 10pm 070c
    irina "Hah!"
    pov "I need to feel them. They teased me all the time."
    scene date 10pm 071c
    irina "Please stop [pov]. My father will caught us."
    pov "No he won't. Just stay still and let me enjoy your tits a little longer."
    scene date 10pm 072c
    irina "Hnn..."
    pov "See? You like my touching too."
    irina "Yes, [pov]."
    pov "I'd love to play with them all day, but you're right and we'll stop here."
    jump irinadatetemplecorruptionend

label irinadatetemplerewardfinger:
    pov "I need a reward."
    irina "Huh? Wait!"
    scene date 10pm 075c
    pov "Gotcha!"
    irina "Hnn... not there!"
    pov "Oh yes, that's exact the right spot I want to be right now."
    pov "And your wetness shows me that you like it too."
    scene date 10pm 076c
    irina "Hah... yes, but..."
    pov "Yes? So I'm right. You want to feel me too."
    irina "Hah... [pov]!"
    scene date 10pm 077c
    pov "Good, relax and enjoy it."
    pov "Feel my fingers do their work."
    scene date 10pm 078c
    irina "Hah... hah..."
    pov "You're a good girl, letting me feel you up."
    irina "Hah... hnn...!"
    scene date 10pm 079c
    pov "And you enjoyed my touch a little too much, haha."
    pov "I can't wait for the day when my dick enter your pussy."
    irina "Hnn..."
    pov "Dream of my touch [irina]!"
    irina "Yes, I will, hah..."
    jump irinadatetemplecorruptionend

label irinadatetemplerewardhandjob:
    pov "I need a reward."
    irina "Huh? What?"
    scene date 10pm 038c
    pov "Please help me with my problem. I had a boner all the time."
    irina "We can't do that. It's too risky."
    pov "I need this now. Be a good girl and help me."
    scene date 10pm 039c
    pov "You also love the thrill of it, doing this in a risky situation."
    irina "Hnn...!"
    pov "Reward me for having a good time, prove yourself to me."
    irina "Hmm..."
    scene date 10pm 040c
    pov "Good, rub me fast and hard and I'll cum in no time."
    irina "Y-yes..."
    pov "You can do it, my dick will melt from the touch of your soft fingers."
    irina "You're so hard."
    scene date 10pm 041c
    pov "You can feel my trembling too, I'm very close. You know how to please me right."
    irina "Hmm..."
    pov "I'm glad I found a girl like you, knowing what I need."
    irina "Hmm... thank you... [pov]."
    scene date 10pm 042c
    pov "HNNG!"
    pov "Yes, that's my girl."
    irina "Hmm..."
    pov "Milk me all dry."
    scene date 10pm 043c
    pov "Oh yes, very nice. And you can feel my appreciation on you."
    irina "Hah, so hot."
    pov "Keep it as a reward for us having this good date."
    irina "Hmm... I will."
    pov "It's time for me to got now."
    jump irinadatetemplecorruptionend

label irinadatetemplerewardblowjob:
    pov "I need a reward."
    irina "Huh? You really want me to?"
    scene date 10pm 045c
    pov "Yes, I need to feel your mouth now."
    irina "But this is a way to risky. If we get caught now!"
    pov "Your father will understand. I bet he also got a reward after a date when he was young."
    scene date 10pm 048c
    irina "You're unbelievable..."
    pov "And you're a good girl, doing what i ask you."
    irina "<suck> <lick>"
    pov "Oh yes, just like that."
    call screen irinadatetempleblowjobhelp

screen irinadatetempleblowjobhelp():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1467 ypos 123 action (Hide ('irinadatetempleblowjobhelp'), Jump('irinadatetempleblowjobdt')) hovered tt.Action ("Help her (deepthroat)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('irinadatetempleblowjobhelp'), Jump('irinadatetempleblowjobnormal')) hovered tt.Action ("Let her continue") focus_mask True


    frame:
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
    pov "Good, very good. Your pleasing is perfect, [irina]."
    irina "Hnn..."
    pov "Hold it deep just a little longer!"
    jump irinadatetempleblowjobcum

label irinadatetempleblowjobnormal:
    pov "You better get me off fast, I know you can do it!"
    irina "Hmm... <suck> <lick>"
    pov "I like your style, rubbing the shaft and licking the tip."
    irina "Hnn..."
    pov "That will let me cum in no time!"
    jump irinadatetempleblowjobcum

label irinadatetempleblowjobcum:
    call screen irinadatetempleblowjobcumchoose

screen irinadatetempleblowjobcumchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1467 ypos 123 action (Hide ('irinadatetempleblowjobcumchoose'), Jump('irinadatetempleblowjobcuminside')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('irinadatetempleblowjobcumchoose'), Jump('irinadatetempleblowjobcumoutside')) hovered tt.Action ("Cum on her face") focus_mask True


    frame:
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
    pov "That was very good. Now swallow my reward."
    irina "Yesh... [pov]."
    scene date 10pm 053ci
    irina "<gulp> <gulp>"
    pov "Good girl. So you can taste your good work too."
    irina "Hmm..."
    pov "You can be proud, I loved my reward [irina]."
    irina "Thank you [pov]."
    pov "It's time to leave."
    jump irinadatetemplecorruptionend

label irinadatetempleblowjobcumoutside:
    pov "I'm close, I need to cum on your face."
    scene date 10pm 051co
    pov "Oh yes! HNNG!"
    irina "Hmm..."
    pov "You let me cum so much."
    scene date 10pm 052co
    irina "Hah... hah..."
    pov "You did very good. I came so much because of your good work."
    irina "Yes, it's very much... and so hot..."
    pov "So I marked you, you can be proud to be my girl."
    irina "Hmm... I am [pov]."
    pov "Me too [irina]. But it's time to leave."
    jump irinadatetemplecorruptionend

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
    pov "Waiting all the time for me to get claimed."
    irina "Claimed?"
    scene date 10pm 062c
    pov "You know exactly what I mean."
    irina "Is... is that your dick [pov]?"
    pov "Yes. And I'll claim your ass now. Claiming your pussy is something for another place."
    pov "But claiming your ass out here is the right thing."
    irina "Y... you're joking... haha..."
    scene date 10pm 063c
    irina "Hah... Aaahnn..."
    pov "So you like my joke?"
    irina "Hah... you really did it... hah..."
    pov "You're so tight. You really need to be claimed."
    scene date 10pm 064c
    irina "Hah... I'm scared [pov]..."
    pov "You don't need to. You're so tight I won't last long, haha."
    irina "Hah... hah... fucking me here like that."
    pov "So you like it?"
    irina "Hah... yes..."
    scene date 10pm 065c
    pov "Then I'll give my best to let you enjoy it too!"
    irina "Aahh... hah..."
    pov "You're trembling. This is getting you off?"
    irina "Yes, hah... I'm getting close [pov]."
    pov "Then have your fun, I'll follow you soon."
    "You fuck her faster and harder."
    scene date 10pm 066c
    irina "Oh my god [pov]. Hah... hah..."
    pov "You're a good girl, spontaneous and adventurous."
    irina "Hah... hah..."
    pov "Imagine we'd get caught now. Your dad will see his little girl getting her ass claimed."
    pov "Right on his front door."
    irina "Aaahh... hah... [pov]!"
    pov "You're coming?"
    irina "Yes, hah... aahhh..."
    pov "Dirty girl, haha."
    call screen irinadatetemplerewardsexcum

screen irinadatetemplerewardsexcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('irinadatetemplerewardsexcum'), Jump('irinadatetemplerewardsexcuminside')) hovered tt.Action ("Cum in her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1367 ypos 123 action (Hide ('irinadatetemplerewardsexcum'), Jump('irinadatetemplerewardsexcumoutside')) hovered tt.Action ("Cum on her ass") focus_mask True


    frame:
        xalign .5
        text tt.value

label irinadatetemplerewardsexcuminside:
    pov "I'll cum too!"
    pov "Aaahh... receive my spunk."
    irina "Hah... hnn..."
    "You pump your sperm in her asshole."
    scene date 10pm 067ci
    pov "Yes, I came so much. But I claimed you good."
    irina "Hah... hah... so hot inside me."
    pov "Your hot ass milked me good."
    irina "Hmm... hah..."
    pov "I can't wait to have more fun with you, but now I need to recover."
    irina "Hah... me too..."
    jump irinadatetemplecorruptionend

label irinadatetemplerewardsexcumoutside:
    pov "I'll cum too!"
    pov "Aaahh... receive my spunk."
    irina "Hah... hnn..."
    "You spray your sperm on her ass."
    scene date 10pm 067co
    pov "Yes, I came so much. But I claimed you good."
    irina "Hah... hah... I feel it so hot on me."
    pov "Your hot ass made me cum good."
    irina "Hmm... hah..."
    pov "I can't wait to have more fun with you, but now I need to recover."
    irina "Hah... me too..."
    jump irinadatetemplecorruptionend


label irinadatetemplecorruptionend:
    pov "Have a good night."
    irina "You too."
    scene black
    $ irinacorruption += 1
    $ irinadatetempledt = False
    $ irinadatetemplefirst = True
    "You leave her and go home."
    jump skip

label irinadatetempleNTR:
    if irinadatetemplefirst == True:
        scene black
        "You went back with her to her house."
    irina "Huh?"
    scene date 10pm 030n
    if frankfirstmeet == True:
        "You see Frank coming out of the front door."
        frank "[irina]."
    else:
        "You see a man coming out of the front door."
        "Man" "[irina]."
    irina "Da-... Frank."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene date 10pm 031n
    irina "What are you doing here?"
    frank "I was searching for you. And I had a talk with your parents."
    irina "With my parents, why?"
    frank "We need to discuss something urgent about your work."
    pov "{i}She seems to be nervous.{/i}"
    scene date 10pm 032n
    irina "Ahh, about my work. Then it's good."
    frank "Yes, as I said. And it's urgent."
    irina "I understand."
    pov "{i}Now her nervousness is gone. I wonder what was the reason?{/i}"
    scene date 10pm 033n
    irina "I need to talk with my boss about my work now."
    irina "I'm sure you can understand that we need to sperate now."
    pov "Oh, okay."
    scene date 10pm 034n
    irina "I'll make it up to you another time [pov]."
    pov "Okay. Then I'll leave now and let you have your urgent talk."
    irina "Thank you for understanding."
    scene date 10pm 036n
    "You go down the street."
    irina "Bye [pov]."
    if frankfirstmeet == True:
        pov "{i}Damn, why has Frank to disturb us now?{/i}"
    else:
        pov "{i}Damn, why has her boss to disturb us now?{/i}"
    pov "{i}But somethings is strange with them needing to talk now.{/i}"
    pov "{i}Or I am just wrong here?{/i}"
    call screen irinadatetemplentrchoose

screen irinadatetemplentrchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 967 ypos 123 action (Hide ('irinadatetemplentrchoose'), Jump('irinadatetemplentrchoosespy')) hovered tt.Action ("Spy on them") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1167 ypos 123 action (Hide ('irinadatetemplentrchoose'), Jump('irinadatetemplentrchoosego')) hovered tt.Action ("Go home") focus_mask True


    frame:
        xalign .5
        text tt.value

label irinadatetemplentrchoosego:
    pov "{i}I'm sure that's just my imagination. They'll just have their talk.{/i}"
    "You go home."
    $ irinadatetemplefirst = True
    jump skip

label irinadatetemplentrchoosespy:
    pov "{i}No, I need to know what's going on there. I'll spy on them.{/i}"
    scene black
    "You wait around the corner until they left the front door."
    scene date 10pm 037n
    pov "{i}I can hear their voices from the back.{/i}"
    pov "{i}Let's see why there are in the back.{/i}"
    scene date 10pm 038n
    pov "{i}Oh...{/i}"
    frank "What were you thinking? Going on a date, instead of meeting with me?"
    irina "I'm sorry, Daddy. I really forgot our meeting."
    pov "{i}Daddy? I'm sure he isn't her dad, so it's just that weirdo's fetish?{/i}"
    frank "I'm hard and I need my relief. So you'll give your best now."
    irina "Yes... I'll give my best to suck you off, but please calm down, daddy."
    frank "You better do or I'll tell you dad next time how a bad girl you are."
    irina "No, please don't. I'll do everything."
    pov "{i}So that's the case. He's blackmailing her. I wonder what's her secret.{/i}"
    frank "Go on!"
    scene date 10pm 039n
    irina "Hmpf... <suck> <choke>"
    frank "And don't forget about our other deal. I want your friend becoming my babygirl."
    frank "And you'll make this happen!"
    irina "Yesh... <choke>"
    pov "{i}Are they talking about [bs]?{/i}"
    frank "You'll better hurry with preparing her for me. I can't wait to put my sperm in her."
    irina "Yesh, daddy... <choke>"
    pov "{i}So they work together to get [bs] ready for him. And [irina] is forced to help him.{/i}"
    scene date 10pm 040n
    frank "Oh yes! Swallow my sperm, my little girl!"
    irina "Hnng...! <gulp> <gulp>"
    frank "Receive your milk from daddy."
    irina "Hnn..."
    pov "{i}Weirdo!{/i}"
    scene date 10pm 041n
    frank "You did good, so I'll forgive you this time."
    irina "Thank you."
    irina "And thank you for your milk, daddy."
    frank "Don't forget about our deal! You can go in now."
    irina "Yes..."
    pov "{i}He's about to leaving. I need to leave before him.{/i}"
    scene black
    "You go home, with knowing a new secret."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    $ irinadatetemplefirst = True
    $ irinadatetemplentr = True
    jump skip

label irinadatetemplemore:
    scene date 10pm 007b
    "You have another date with her."
    jump irinadatetempleconversation
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
