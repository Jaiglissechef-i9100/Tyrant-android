
label basementnicoleoutinglove:
    hide screen locations
    hide screen townl
    scene black
    "You decide to show off [mother] to the other gangmembers."
    scene basement 10pm 015c
    "You sit in the basement with the others waiting for [mother]."
    pov "{i}Today we want to let them know that we're together now.{/i}"
    scene basement 10pm 017c
    pov "{i}There she is, sexy as ever.{/i}"
    davide "So you'll bring us something to drink now?"
    mom "Yes."
    scene livingroom 10pm 040
    pov "{i}That outfit is so sexy, I can't wait to have fun together again!{/i}"
    davide "So what do you think about we talked before, Bruce?"
    dad "Huh? I'm not sure yet, sorry..."
    scene livingroom 10pm 041
    mom "The drinks are ready. Do you need something else?"
    mom "No...?"
    mom "So I have something to announce."
    pov "{i}Oh she's starting it.{/i}"
    scene livingroom 10pm 042b
    mom "I have choosen someone else to be with from now on!"
    scene livingroom 10pm 043b
    mom "As it turned out he became a fine young man."
    mom "Like the perfect man for me."
    pov "{i}Wow. She's really in love with me.{/i}"
    dad "What?"
    scene livingroom 10pm 044b
    mom "With me supporting him, he'll be even a better helper for the gang."
    pov "{i}Oh my god. She's teasing me so good.{/i}"
    mom "Aren't you with me, [pov]?"
    pov "Oh yes... You're so right."
    scene livingroom 10pm 045b
    "She's rubbing her ass softly on your crotch."
    pov "{i}And now she shows them that she's serious.{/i}"
    mom "I hope you'll accept this as my choice, I'm sure you'll find other partners for yourself."
    dad "<gulp>"
    scene livingroom 10pm 046b
    mom "Don't look so confused [pov]. I think you like my little surprise. <giggle>"
    pov "{i}This is so hot. She told them and shows them aggressive that she choose me over Bruce.{/i}"
    mom "<whisper> And I can feel your boner."
    pov "<whisper> I coudn't withstand that teasing."
    mom "<whisper> Don't worry. It's what I wanted."
    pov "{i}Oh yes, yes, yes...{/i}"
    scene livingroom 10pm 047b
    "She rub her ass more on you."
    mom "I need to find a better position to sit. <giggle>"
    dad "..."
    davide "..."
    pov "{i}She's playing with me. I love it!{/i}"
    mom "So, are you accepting my choice?"
    scene livingroom 10pm 054b
    davide "I'm fine with that. I'll find another slut in no time, haha."
    if inc == True:
        davide "And I need to know if you're really stay in a sexual relationship with your son."
    else:
        davide "And I need to know if you're really stay in a sexual relationship with the son of your best friend."
    dad "You... he did something with her. Maybe he drugged her!"
    davide "Shut up, Bruce. You know that she's serious."
    dad "I'll kill that little bastard!"
    scene livingroom 10pm 055b
    davide "You'll do NOTHING! You know the gang rules! I'll break your bones if you break them!"
    dad "But she's my wife!"
    if inc == True:
        dad "And also his own mother!"
    davide "I can understand their decision, haha. And you'll respect it too."
    mom "Just accept it. You had your chance. I'd choosen better."
    dad "What are you..."
    davide "Haha, she's right, Bruce. You had your chance but now you'll be replaced, hahaha."
    scene livingroom 10pm 047aa
    davide "But we need to solve another problem now, haha."
    pov "What is it?"
    davide "Bruce have no girl anymore and every gang member should have one, even the ones on the lower end."
    mom "So we'll choose now a girl Bruce can have, since he can't be with me any longer?"
    davide "Yes, we'll choose one for her so he won't lose her again, hahaha."
    dad "Please, Davide..."
    davide "Shut up!"
    scene livingroom 10pm 047aaa
    davide "So any ideas which girl would fit for this loser? Maybe [miranda], she has very low standards, haha!"
    mom "You can't be serious!"
    pov "{i}Oh, does [mother] hate her so much?{/i}"
    davide "Haha, relax, it's not decided yet. But you'll accept our decision like we accept yours."
    mom "Hmm..."
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
    pov "{i}Oh, he accepted his fate.{/i}"
    pov "{i}I could choose [miranda] to be his girl. She's already a slut and [mother] is hating her, so Bruce won't have a chance to get her back.{/i}"
    pov "{i}Or should I choose the subway girl, [ruby]? Then he can't enjoy it but can get relieve when he need to.{/i}"
    pov "{i}Maybe he'll get even ill or get STD's and will lost all of his left pride...{/i}"
    pov "{i}Or he wouldn't be allowed to have any girl for his needs. A grown man that need to masturbate for his relief, haha.{/i}"
    pov "{i}But maybe he could get mad then and do something stupid, like raping someone...{/i}"
    pov "{i}Decisions, hmm...{/i}"
    call screen basementnicoleoutinglovebruce

screen basementnicoleoutinglovebruce():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementnicoleoutinglovebruce'), Jump('basementnicoleoutinglovebrucemiranda')) hovered tt.Action ("He can have [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 775 ypos 123 action (Hide ('basementnicoleoutinglovebruce'), Jump('basementnicoleoutinglovebruceruby')) hovered tt.Action ("He'll take [ruby]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementnicoleoutinglovebruce'), Jump('basementnicoleoutinglovebrucenone')) hovered tt.Action ("He won't be allowed to have a girl") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutinglovebruceruby:
    pov "He's only allowed to do it with [ruby]."
    scene livingroom 10pm 047aaa
    dad "You can't be serious!"
    davide "Haha, I like that cruel boy. So it'll be. You should be happy Bruce. At least you can fuck someone, haha."
    pov "Maybe you'll resist her, but your own hand won't be enough at some point and then you can have fun with her."
    dad "But why?"
    pov "Because I decided it. Oh and something else, when that girl is really so dirty..."
    mom "She isn't allowed to enter the house, the girl is so dirty and I don't want to get ill."
    $ dadandruby = True
    jump basementnicoleoutinglove2

label basementnicoleoutinglovebrucemiranda:
    pov "He can have fun with [miranda] too."
    scene livingroom 10pm 047aaa
    dad "Too?"
    pov "Yes, you can get your relief from her but she'll be free for others to have fun too."
    mom "Others, I hope you aren't after her too?"
    pov "No, but Davide seems to like her too."
    davide "Ha, a wise decision. And especially because Bruce has a crush on that slut too."
    mom "Hnn...!"
    pov "I know you don't like it that much."
    pov "But please trust me here."
    mom "OK."
    pov "Good!"
    $ dadandmiranda = True
    jump basementnicoleoutinglove2

label basementnicoleoutinglovebrucenone:
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
    jump basementnicoleoutinglove2

label basementnicoleoutinglove2:
    scene livingroom 10pm 056b
    dad "What's gotten into you?"
    if inc == True:
        dad "He's your son and you want to be his girl? WTF?"
    else:
        dad "He's the son of your best friend and you want to be his girl? WTF?"
    mom "Yes..."
    dad "That's not you! Did he blackmail you?"
    davide "That's enough! We made a decision and you'll accept it!"
    dad "But it's not fair!"
    davide "I don't care, it's her decision! And I won't allow that you insult other gang members!"
    dad "So you really want to break all taboos and be with him?"
    dad "You have no idea how disappointed I am. But you're safe, I won't risk all we did..."
    dad "YOU DAMN SLUT!"
    scene livingroom 10pm 057b
    pov "STOP!"
    dad "Huh?"
    pov "This will stop now and you'll behave! Remember that I could also tell some things!"
    pov "{i}I won't of course, it could danger the girls, but maybe it'll take effect on him.{/i}"
    dad "..."
    pov "So you understood. And don't forget, you aren't allowed to touch your wife anymore."
    pov "We're now together and I warn you, don't make any mistakes!"
    dad "..."
    dad "Fuck you!"
    scene livingroom 10pm 058b
    dad "I'm out of here!"
    davide "Hahaha, what a great show!"
    davide "Oh and let him go, he'll calm down. He's weak, haha."
    scene livingroom 10pm 059b
    davide "So, what to do now?"
    mom "Hmm..."
    mom "[pov] has a boner and I need to help him with that now."
    pov "{i}What? Did she really said that?{/i}"
    davide "Maybe you could help me with my boner too, haha."
    mom "Maybe... it's [pov]'s decision."
    pov "{i}Wait... Davide want to join in and [mother] will accept my decision.{/i}"
    pov "{i}She's so much in love with me that she'll trust me all on that.{/i}"
    call screen basementnicoleoutingloveshare

screen basementnicoleoutingloveshare():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 767 ypos 123 action (Hide ('basementnicoleoutingloveshare'), Jump('basementnicoleoutingloveshareyes')) hovered tt.Action ("Share her with Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementnicoleoutingloveshare'), Jump('basementnicoleoutingloveshareno')) hovered tt.Action ("Don't share her") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingloveshareyes:
    pov "Are you really okay with that, [mother]?"
    mom "Yes, if you like that too [pov]."
    davide "Great. Then we all can have fun."
    scene livingroom 10pm 065bs
    mom "Then come on, show me what you got. <giggle>"
    pov "{i}I can't believe it. She doesn't care that I'll share her. And it seems that she even like it.{/i}"
    mom "Two strong men taking me..."
    pov "This is so hot."
    davide "You're a lucky guy [pov]."
    $ basement10pmnicoleoutingshare = True
    scene livingroom 10pm 066s
    davide "I'll go along with a blowjob. So you can ride your slut properly."
    pov "Oh, she's not my sl..."
    mom "Yes, I'm his slut! Everyone knows that gangmembers girls are just sluts."
    pov "{i}Oh... Then I'll play that game.{/i}"
    pov "I can't wait to fuck you, slut."
    scene livingroom 10pm 067
    pov "You're so wet."
    mom "Please stop teasing me."
    davide "Of course she's wet, she can have two dicks, haha."
    "You rub your dick on her pussy."
    mom "Hah... hnn... please fuck me now [pov]."
    pov "{i}I'n not sure I like it when she's playing the slut. But for now we have to do this.{/i}"
    scene livingroom 10pm 068s
    davide "Yes, begin with a good licking."
    mom "Hmm... <lick>"
    davide "Oh yes, that tongue is amazing. You'll have much fun with that mouth, [pov]."
    scene livingroom 10pm 070
    mom "Aaahnn..."
    pov "All in! You like my surprise?"
    mom "Hah, hah... yes..."
    scene livingroom 10pm 070s
    davide "Yes, suck on my cock."
    mom "<suck> <lick>"
    pov "Oh I love it so much to fuck you!"
    davide "Her mouth is also very good, haha."
    scene livingroom 10pm 071s
    davide "Perfect, she's working on my dick so eagerly because her hole is stuffed so good, haha."
    pov "Yes, she's doing good. My \"slut\" is a good fuck. And she seems to like it too."
    davide "So this mouth will taste my dick again?"
    pov "We'll see."
    mom "Hnn... hnn..."
    davide "Oh, your slut likes the idea too."
    pov "Yes, haha."
    pov "{i}Maybe, but I'm not sure if I'll share her again.{/i}"
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
    call screen basementnicoleoutingloveshareyescumchoose

screen basementnicoleoutingloveshareyescumchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementnicoleoutingloveshareyescumchoose'), Jump('basementnicoleoutingloveshareyescuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementnicoleoutingloveshareyescumchoose'), Jump('basementnicoleoutingloveshareyescumoutside')) hovered tt.Action ("Cum over her ass") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutingloveshareyescuminside:
    pov "I need to cum inside you."
    mom "Hmm... yes..."
    pov "Ah, hnnn..."
    "You spurt your sperm inside her."
    pov "Oh, I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh, yes, you're right, haha."
    scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked it, \"slut\"?"
    mom "Yes, [pov]. I like it when you put your sperm inside me."
    pov "Good."
    scene livingroom 10pm 072sof
    davide "Yes, very good. She also missed to drink just a little sperm."
    pov "Alright with you, [mother]."
    mom "Yes, hah... I'm good [pov]."
    davide "Oh she did already very fine. You're lucky with this slut, haha."
    jump basementnicoleoutingloveshareend

label basementnicoleoutingloveshareyescumoutside:
    pov "I'll cum on your ass"
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
    pov "You liked it, \"slut\"?"
    mom "Yes, [pov]. I like it when you put your sperm on me."
    pov "Good."
    scene livingroom 10pm 072sof
    davide "Yes, very good. She also missed to drink just a little sperm."
    pov "Alright with you, [mother]."
    mom "Yes, hah... I'm good [pov]."
    davide "Oh she did already very fine. You're lucky with this slut, haha."
    jump basementnicoleoutingloveshareend

label basementnicoleoutingloveshareend:
    scene livingroom 10pm 062b
    davide "I'll go now, have some drinks and maybe I'll find Bruce and can more fun with him, haha."
    davide "Have much more fun with your slut, [pov]."
    pov "I'm done. I came and she had much fun too. And showing Bruce his place."
    davide "Haha, yes."
    pov "That was so hot. I can't wait to have more fun with you."
    mom "Yes..."
    scene black
    "You leave the basement and go to bed."
    $ basement10pmnicoleouting = True
    jump skip


label basementnicoleoutingloveshareno:
    pov "No, sorry Davide, but I don't think so."
    pov "I need some private time with her."
    scene livingroom 10pm 061b
    davide "Oh, you're serious."
    pov "Yes, I am."
    davide "Oh, OK. Normally I would just take what I want, but I appreciate how you'd handle Bruce..."
    davide "So you can have your fun with her alone."
    scene livingroom 10pm 062b
    davide "I'll go now, have some drinks and maybe I'll find Bruce and can more fun with him, haha."
    davide "Have much more fun with your slut, [pov]."
    pov "Oh yes, I will!"
    pov "<whisper> You're not my slut, you're my lover of course."
    mom "<whisper> You're so sweet. Don't worry, I know how manly he needs to be."
    scene livingroom 10pm 065b
    mom "Come on [pov]. Don't let me wait any longer."
    if inc == True:
        pov "Yes, mom."
    else:
        pov "Yes, [mother]."
    mom "I want you too feel me inside again!"
    pov "And I can't wait after your hot teasing."
    scene livingroom 10pm 066
    "You walk over to her."
    pov "So you got horny after our coming out?"
    mom "Yes... feeling your big boner while telling them. Feeling how much you want me."
    if inc == True:
        pov "I'll never refuse you, mom!"
    else:
        pov "I'll never refuse you, [mother]!"
    mom "<giggle> Then stick it in, [pov]."
    scene livingroom 10pm 067
    pov "You're so wet."
    mom "Please stop teasing me."
    pov "You teased me all the time before. Now it's my turn, haha."
    "You rub your dick on her pussy."
    mom "Please... fuck me already, [pov]."
    if inc == True:
        pov "As you wish, mom!"
    else:
        pov "As you wish, [mother]!"
    scene livingroom 10pm 070
    mom "Aahhh... yes!"
    pov "Ohh... I could slide all in."
    mom "And I can feel you so deep in me!"
    scene livingroom 10pm 068
    mom "Ohh, hah... you're so wild."
    pov "I can't stand it. I love you so much!"
    mom "I love you too, I love you so much [pov]!"
    pov "I want to stay together with you all my life."
    mom "Oh hah, I want that too."
    pov "But others knew now about it..."
    mom "I don't care anymore. Everyone can know. I just, hah, want to be with you."
    pov "Oh yes, this is like heaven."
    mom "We'll get through this gang life. And when it's over we'll find a way to stay together."
    if inc == True:
        pov "Oh yes, I'm so close, mom!"
    else:
        pov "Oh yes, I'm so close, [mother]!"
    mom "Me too, let's cum together, hah..."
    call screen basementnicoleoutinglovesharenocumchoose

screen basementnicoleoutinglovesharenocumchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('basementnicoleoutinglovesharenocumchoose'), Jump('basementnicoleoutinglovesharenocuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('basementnicoleoutinglovesharenocumchoose'), Jump('basementnicoleoutinglovesharenocumoutside')) hovered tt.Action ("Cum over her ass") focus_mask True


    frame:
        xalign .5
        text tt.value

label basementnicoleoutinglovesharenocuminside:
    pov "I... I want to cum inside you!"
    mom "Yes, hah... cum inside me..."
    scene livingroom 10pm 070
    pov "Ah, hnnn..."
    "You spurt your sperm inside her."
    mom "AAAAHH... yes..."
    scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah... so much of your sperm is inside me."
    pov "You're the reason I can produce so much."
    jump basementnicoleoutinglovesharenoend

label basementnicoleoutinglovesharenocumoutside:
    pov "I'll cum over your ass."
    mom "Yes... do it... hah..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    "You spray your sperm over her ass."
    scene livingroom 10pm 072o
    pov "What a wonderful view."
    mom "Hah... hah... so much of your sperm over my ass."
    pov "You're the reason I can produce so much."
    jump basementnicoleoutinglovesharenoend

label basementnicoleoutinglovesharenoend:
    mom "Hah... hah... I needed that."
    pov "And me also, of course."
    mom "I love you [pov]."
    pov "I love you too."
    scene black
    "You leave the basement and go to bed."
    $ basement10pmnicoleouting = True
    jump skip


label showerd15fuckslut:
    $ shower15corthird = True
    pov "Haha that's a nice joke."
    mom "Huh?"
    pov "It was nice of you, playing the innocent, it made me very hard."
    pov "But it's enough. I need to fuck my slut now."
    mom "But... someone can see us here..."
    pov "Oh I don't care! Everyone knew already that you're my slut."
    if inc == True:
        mom "But your sisters could catch us."
    else:
        mom "But my daughters could catch us."
    if basement10cassandraouting == True:
        pov "Hmm, you're right. And [bs] could join us then, haha."
        mom "Hnn..."
    pov "I don't care, spin around so I can choose a hole."
    mom "But..."
    pov "NOW, SLUT!"
    mom "Yes... I'm sorry [pov]..."
    scene showerdownstairs 3pm 029x
    pov "So, which hole should I choose?"
    mom "It's up to you [pov]..."
    call screen showerd15fuckslutchoose

screen showerd15fuckslutchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 667 ypos 123 action (Hide ('showerd15fuckslutchoose'), Jump('showerd15fuckslutpussy')) hovered tt.Action ("Fuck her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('showerd15fuckslutchoose'), Jump('showerd15fuckslutass')) hovered tt.Action ("Fuck her ass") focus_mask True


    frame:
        xalign .5
        text tt.value

label showerd15fuckslutass:
    $ showerd15corass = True
    jump showerd15fuckslutpussy

label showerd15fuckslutpussy:
    if showerd15corass == False:
        pov "I'll fuck your pussy."
        mom "Yes, fuck me."
        scene showerdownstairs 3pm 030xap
        "You stick your dick in her pussy."
    else:
        pov "I'll fuck your ass."
        mom "Yes, fuck me."
        scene showerdownstairs 3pm 030xaa
        "You stick your dick in her ass."
    mom "Ahh..."
    pov "You're so wet. I knew you need that now."
    mom "Hnn..."
    if showerd15corass == False:
        scene showerdownstairs 3pm 031xap
        pov "Your tight pussy is craving for my dick."
    else:
        scene showerdownstairs 3pm 031xaa
        pov "Your tight ass is craving for my dick."
    mom "Hnn... hah..."
    pov "You're happy now that I didn't stop! Aren't you, slut?"
    mom "Hah...hah... hnn..."
    pov "{i}She's ignoring me. She needs more training.{/i}"
    "You start to fuck her harder!"
    pov "Aren't I'm right? Answer me!"
    scene showerdownstairs 3pm 032xa
    mom "Yes! I awaited it! Fuck me more."
    pov "Good answer."
    mom "Hah... hah... not so rough..."
    pov "{i}I think she said it only to please me. But I want her to submit and learn to like it.{/i}"
    pov "Then it's easy to you to cum for me!"
    mom "Hah... cum for you...?"
    pov "Yes, when you awaited it so much you can show me your orgasm."
    pov "{i}She's tightening. I'm sure I catched her lie.{/i}"
    pov "{i}She's still afraid to get catched, so she want me to finish fast.{/i}"
    "You fuck her even harder and rougher."
    scene showerdownstairs 3pm 033xa
    mom "Ahh... haah... haah..."
    pov "Cum for me slut! Show me how much you like it!"
    mom "Hnn... I'm close... I'll cum any moment..."
    pov "{i}Wait, but she isn't shaking and getting tighter like she does when she cums.{/i}"
    pov "{i}Does she really trying to trick me? Oh no, slut, I'm not stupid.{/i}"
    if showerd15corass == False:
        scene showerdownstairs 3pm 034xap
    else:
        scene showerdownstairs 3pm 034xaa
    mom "OHHH... yes... I'm cumming..."
    pov "Hahaha..."
    mom "Hah... why are you laughing...?"
    pov "I thought you'll do better slut. Try to trick me because you want to end this fast."
    mom "What...? No..."
    pov "You're still afraid that we'll get caught, but I don't care. You came before and this was no orgasm."
    mom "No, you're wrong..."
    if showerd15corass == False:
        scene showerdownstairs 3pm 035xap
    else:
        scene showerdownstairs 3pm 035xaa
    pov "Shut up! We'll fuck until you'll enjoy a real orgasm. And when it takes time until dinner."
    "You grab her hair."
    mom "I'll do everything to please, but please stop it. Not here..."
    pov "No! You need to learn your place, slut. Lying to me like that. Take it as your punishment!"
    mom "Hah... I'm sorry... please..."
    "You take her rougher."
    mom "Hnn... hah... hah..."
    pov "Maybe you need some help to come in that risky situation!"
    mom "What... hah..."
    scene showerdownstairs 3pm 036xa
    pov "I want you to tell me what you are and how much you like it."
    mom "Hah... I'm your slut and I like to get fucked by your dick."
    pov "Again, louder!"
    mom "Hah... but... someone could hear me..."
    pov "You're right, [bs] will come home soon, so you better hurry."
    pov "You can do it now or we'll continue until you did it, your choice!"
    mom "Hah... ahh..."
    pov "You need to cum for real, slut!"
    mom "But..."
    pov "You decided to be my slut, so act like you promised."
    mom "Hah... hnng..."
    mom "I'M YOUR SLUT! YOU FUCK ME LIKE A WHORE!"
    mom "I LOVE YOUR DICK INSIDE MY PUSSY, CLAIMING ME AS YOURS!"
    mom "AHHH...HAH..."
    pov "{i}This time she's shaking right, she's cumming hard. This risky situation gave her the kick.{/i}"
    pov "Good girl!"
    mom "Hah... hah..."
    pov "I'm close to cum too."
    call screen showerd15fuckslutcumchoose

screen showerd15fuckslutcumchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('showerd15fuckslutcumchoose'), Jump('showerd15fuckslutcuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 667 ypos 123 action (Hide ('showerd15fuckslutcumchoose'), Jump('showerd15fuckslutcumout')) hovered tt.Action ("Cum on her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 967 ypos 123 action (Hide ('showerd15fuckslutcumchoose'), Jump('showerd15fuckslutcummouth')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('showerd15fuckslutcumchoose'), Jump('showerd15fuckslutcumface')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        xalign .5
        text tt.value

label showerd15fuckslutcuminside:
    if showerd15corass == True:
        scene showerdownstairs 3pm 037xaa
        pov "I'll cum in your ass."
        mom "Yes [pov]. Spray your sperm in me."
        pov "{i}Good, she's submissive again.{/i}"
        pov "AHH...HNNG...!"
        "You cum in her ass."
        mom "Hnn..."
        pov "So good, now stay bent over and let me see."
        scene showerdownstairs 3pm 038xao
        mom "Hmm..."
        pov "I came so much from our hot fucking."
        scene showerdownstairs 3pm 042xar
        pov "And you had your fun too. Next time you'll be a good slut and just trust me and do what I say."
        mom "Y...yes [pov]."
        pov "Now you can finish your cleaning."
        jump showerd15fuckslutend
    else:
        scene showerdownstairs 3pm 037xap
        pov "I'll cum in your pussy."
        mom "Yes [pov]. Spray your sperm in me."
        pov "{i}Good, she's submissive again.{/i}"
        pov "AHH...HNNG...!"
        "You cum in her pussy."
        mom "Hnn..."
        pov "So good, now stay bent over and let me see."
        scene showerdownstairs 3pm 038xai
        mom "Hmm..."
        pov "I came so much from our hot fucking."
        scene showerdownstairs 3pm 042xar
        pov "And you had your fun too. Next time you'll be a good slut and just trust me and do what I say."
        mom "Y...yes [pov]."
        pov "Now you can finish your cleaning."
        jump showerd15fuckslutend

label showerd15fuckslutcumout:
    if showerd15corass == True:
        scene showerdownstairs 3pm 037xaa
    else:
        scene showerdownstairs 3pm 037xap
    pov "I'll cum on your ass."
    mom "Yes [pov]. Spray your sperm on me."
    pov "{i}Good, she's submissive again.{/i}"
    scene showerdownstairs 3pm 038xab
    pov "AHH...HNNG...!"
    "You cum on her ass."
    mom "Hnn..."
    pov "I came so much from our hot fucking."
    scene showerdownstairs 3pm 042xar
    pov "And you had your fun too. Next time you'll be a good slut and just trust me and do what I say."
    mom "Y...yes [pov]."
    pov "Now you can finish your cleaning."
    jump showerd15fuckslutend

label showerd15fuckslutcummouth:
    pov "Get on your knees, I want to cum in your mouth."
    mom "Yes."
    scene showerdownstairs 3pm 038xaf
    pov "Suck on my dick and receive my sperm."
    mom "And then I'll show you how much you gave me, before I swallow."
    pov "Very good. You came back to your senses and remember how I like my slut."
    mom "Yes, I did."
    scene showerdownstairs 3pm 039xam
    pov "Here, taste it."
    mom "Hmm... <suck> <lick>"
    pov "Oh yes, like that. AHHH...HNNG..."
    "You cum in her mouth."
    mom "Hnng..."
    scene showerdownstairs 3pm 040xam
    mom "Ahh..."
    pov "Good."
    pov "{i}I came so much, she couldn't catch it all.{/i}"
    scene showerdownstairs 3pm 041xam
    mom "<gulp>"
    pov "Maybe I'll oversee your disobedience this time, because you came back to your place."
    pov "But if you'll disobey next time again, you'll have to scream again."
    pov "{i}I'll wonder if she maybe get used to it and choose to scream next time again?{/i}"
    scene showerdownstairs 3pm 042xam
    mom "Ahhh..."
    pov "Very good. Now one thing is missing."
    mom "Thank you for your tasty sperm... [pov]..."
    pov "And...?"
    mom "Thank you for fucking me so good until I came too."
    scene showerdownstairs 3pm 043xam
    pov "Yes, you had your fun too. Next time you'll be a good slut and just trust me and do what I say."
    mom "Y...yes [pov]."
    pov "Now you can finish your cleaning."
    jump showerd15fuckslutend

label showerd15fuckslutcumface:
    pov "Get on your knees, I want to cum on your face."
    mom "Yes."
    scene showerdownstairs 3pm 038xaf
    pov "Get ready to get plastered."
    mom "Yes, thank you for give me a warning."
    pov "Very good. You came back to your senses and remember how I like my slut."
    mom "Yes, I did."
    scene showerdownstairs 3pm 039xaf
    pov "Oh yes. AHHH...HNNG..."
    "You cum on her face."
    mom "Hnng..."
    scene showerdownstairs 3pm 040xaf
    mom "Ahh..."
    pov "Good."
    pov "{i}I came so much, all over it.{/i}"
    pov "You're looking so hot, covered in my sperm."
    mom "Hmm..."
    scene showerdownstairs 3pm 041xaf
    pov "Maybe I'll oversee your disobedience this time, because you came back to your place."
    pov "But if you'll disobey next time again, you'll have to scream again."
    pov "{i}I'll wonder if she maybe get used to it and choose to scream next time again?{/i}"
    mom "Thank you for cumming all over me... [pov]..."
    pov "Very good. Now one thing is missing."
    mom "Thank you for fucking me so good until I came too."
    scene showerdownstairs 3pm 042xaf
    pov "Yes, you had your fun too. Next time you'll be a good slut and just trust me and do what I say."
    mom "Y...yes [pov]."
    pov "Now you can finish your cleaning."
    jump showerd15fuckslutend

label showerd15fuckslutend:
    scene black
    "You leave the shower."
    $ momcorruption += 1
    $ dtime += 1
    $ showerd15corass = False
    jump showerdown


label showerd15fucklove:
    $ shower15lovethird = True
    scene showerdownstairs 3pm 029xb
    pov "Huh?"
    "She removed her hands."
    pov "Why did you stop? Did I do something wrong?"
    mom "Haha, no. Turn around [pov]."
    "You turn around."
    scene showerdownstairs 3pm 031xb
    mom "You did everything right. And I'm glad that you're got this hard for me."
    pov "So, then what now."
    mom "I was thinking..."
    scene showerdownstairs 3pm 030xb
    "She moves her hand over your chest the way down."
    mom "...after we had our coming out and the people who need to know it are informed..."
    pov "So..."
    pov "{i}I have already an idea what she want. But I'll let her this moment.{/i}"
    scene showerdownstairs 3pm 032xb
    mom "...I think we could do something more."
    "She's pressing your dick on her pussy."
    pov "Are you sure? You want us to fuck here in the shower?"
    mom "Yes, please take me [pov]! Love me!"
    scene showerdownstairs 3pm 033xb
    "You hold her and stick your dick inside her pussy."
    mom "Ahh... yes..."
    if inc == True:
        pov "You're so naughty, mom."
        scene showerdownstairs 3pm 034xb
        mom "And you're so perverted, fucking your mother in the shower! <giggle>"
    else:
        pov "You're so naughty, [mother]."
        scene showerdownstairs 3pm 034xb
        mom "And you're so perverted, fucking your mothers best friend in the shower! <giggle>"
    pov "{i}I can't believe it, she's so happy.{/i}"
    pov "You know how you turn me on."
    pov "But I want to do something else too."
    scene showerdownstairs 3pm 035xb
    pov "<suck>"
    "You suck on her nipple."
    mom "Ohh... hah... [pov]!"
    pov "Like a baby sucking on his mom's titties. Craving for the milk."
    if inc == True:
        pov "Like I sucked on your titties. And drank your milk."
    mom "Ohh... hah... that's so wrong, but so hot..."
    scene showerdownstairs 3pm 036xb
    mom "I'm so happy that I can share this time with you. Let's make even more memories."
    pov "What...? You talk like you'll die soon..."
    mom "No, hah... But you'll leave me for a younger girl... Somenone you'll spend your life with..."
    mom "And so I want to enjoy every single moment as much as possible."
    pov "Haha, you're crazy! I waited all my life for this, there's no way I'll abandon you!"
    pov "Maybe you're so confused because you're so horny. Let's test something."
    mom "What do you... hah... mean?"
    "You fuck her faster."
    pov "Maybe an orgasm will calm you down, haha."
    mom "Oh... [pov]... so good..."
    scene showerdownstairs 3pm 038xb
    mom "Ahhh... ohhh... I'm so close..."
    if inc == True:
        pov "Cum for me, mom!"
        pov "Accept the pleasure your son wants to give you."
    else:
        pov "Cum for me, [mother]!"
        pov "Accept the pleasure I want to give you."
    mom "Oh, [pov]! AHHH...HAAHHH, I'm cumming!"
    "She's shaking wildly and cum on your dick."
    scene showerdownstairs 3pm 037xb
    mom "Hah... hah... that was amazing!"
    pov "Yes, <suck> and I hope your weird thoughts are going away now."
    mom "Not at all, but you proved your point, hah..."
    pov "Then how about this?!"
    scene showerdownstairs 3pm 040xb
    mom "Ahh, wait... you're so deep... I came only a few seconds before."
    pov "Good, then you can cum again!"
    mom "Oh, what are you doing with me [pov]. You fuck me like I'm a young girl."
    pov "And I love it seeing you like this!"
    mom "Oh god, I'm close again... hah... hah..."
    pov "Then cum for me again, I want you to!"
    mom "Yes, YES! I love you [pov]! I lOVE YOU SO MUCH! I'M CUMMING AGAIN! AHHH..."
    pov "I'm so close too. I'll cum every moment."
    mom "Then, hah... do it... Cum where you want... just cum for me!"
    pov "{i}She's so excited, she'll let me choose where I want, but where do I want to cum?{/i}"
    call screen shower15dfucklovecumchoose

screen shower15dfucklovecumchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 123 action (Hide ('shower15dfucklovecumchoose'), Jump('shower15dfucklovecuminside')) hovered tt.Action ("I want to cum inside you") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 123 action (Hide ('shower15dfucklovecumchoose'), Jump('shower15dfucklovecumoutside')) hovered tt.Action ("I want to cum outside") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 467 ypos 323 action (Hide ('shower15dfucklovecumchoose'), Jump('shower15dfucklovecumtits')) hovered tt.Action ("I want to cum on your tits") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1175 ypos 323 action (Hide ('shower15dfucklovecumchoose'), Jump('shower15dfucklovecummouth')) hovered tt.Action ("I want to cum in your mouth") focus_mask True

    frame:
        xalign .5
        text tt.value

label shower15dfucklovecuminside:
    if inc == True:
        pov "I want to cum inside you, mom!"
    else:
        pov "I want to cum inside you, [mother]!"
    mom "Yes, cum inside me. Let's cum together!"
    scene showerdownstairs 3pm 041xbi
    pov "HNNG..."
    "You spray your sperm in her pussy."
    mom "Ahhh... so hot."
    "She's shaking while she's having her second orgasm."
    pov "Oh yes, I needed that."
    mom "You came so much, deep inside me."
    if inc == True:
        pov "I love you, mom."
        mom "I love you too, my son."
    else:
        pov "I love you, [mother]."
        mom "I love you too, [pov]."
    "You let her down."
    scene showerdownstairs 3pm 042xbi
    mom "There so much of your sperm. It's dripping out of me, like a waterfall."
    pov "Oh, I came really that much? So we're very compatible."
    mom "Yes I understand now where you point at."
    jump showerd15fuckloveend

label shower15dfucklovecumoutside:
    pov "I'll cum outside."
    mom "Yes, then spray it on me. Let's enjoy our orgasms together."
    scene showerdownstairs 3pm 041xbo
    pov "HNNG..."
    "You spray your sperm on her belly."
    mom "Ahhh... so hot."
    "She's shaking while she's having her second orgasm."
    pov "Oh yes, I needed that."
    mom "There's so much sperm on my belly now."
    pov "Oh, I came really that much? So we're very compatible."
    mom "Yes I understand now where you point at."
    if inc == True:
        pov "I love you, mom."
        mom "I love you too, my son."
    else:
        pov "I love you, [mother]."
        mom "I love you too, [pov]."
    jump showerd15fuckloveend

label shower15dfucklovecumtits:
    if inc == True:
        pov "I want to cum on your beautiful tits, mom!"
    else:
        pov "I want to cum on your beautiful tits, [mother]!"
    mom "Yes, let's do it."
    scene showerdownstairs 3pm 042xbmt
    mom "Show me how much you have for me."
    pov "You're so hot. Doing all this kinky stuff together."
    mom "All for you my love."
    pov "Oh, I'm cumming, HNNG..."
    scene showerdownstairs 3pm 042xbt
    "You spray your sperm all over her tits."
    mom "I can feel it, so much and so hot."
    pov "That hot view is helping very much!"
    scene showerdownstairs 3pm 043xbt
    mom "I can feel how good your relieve was directly on my breasts. <giggle>"
    pov "Oh, I came really that much? So we're very compatible."
    mom "Yes I understand now where you point at."
    if inc == True:
        pov "I love you, mom."
        mom "I love you too, my son."
    else:
        pov "I love you, [mother]."
        mom "I love you too, [pov]."
    jump showerd15fuckloveend

label shower15dfucklovecummouth:
    if inc == True:
        pov "I want to cum in your beautiful mouth, mom!"
    else:
        pov "I want to cum in your beautiful mouth, [mother]!"
    mom "Yes, let's do it."
    scene showerdownstairs 3pm 042xbmt
    mom "Show me how much you have for me."
    pov "You're so hot. Doing all this kinky stuff together."
    mom "All for you my love."
    pov "Oh, I'm cumming, HNNG..."
    scene showerdownstairs 3pm 043xbm
    mom "Ahh..."
    pov "So hot..."
    "She catch your sperm with her mouth."
    scene showerdownstairs 3pm 044xbm
    mom "Ahh..."
    pov "I can't believe it. You go even this far. Amazing!"
    mom "<giggle>"
    scene showerdownstairs 3pm 045xbm
    mom "<gulp> You liked it?"
    pov "Haha, you still know the answer."
    mom "Yes, and I'm happy that I made you happy too."
    pov "So then we're very compatible."
    mom "Yes I understand now where you point at."
    if inc == True:
        pov "I love you, mom."
        mom "I love you too, my son."
    else:
        pov "I love you, [mother]."
        mom "I love you too, [pov]."
    jump showerd15fuckloveend

label showerd15fuckloveend:
    mom "I'm not happy to say this now, but I have to clean myself again."
    pov "Yes, I know. The others will come home soon. I'll leave you alone now."
    mom "But [pov]!"
    pov "Hmm...?"
    mom "Promise me that we'll do this again."
    pov "Having sex in the shower?"
    mom "Having sex, <giggle>"
    pov "Haha, of course!"
    scene black
    "You leave the shower."
    $ momlove += 1
    $ dtime += 1
    jump showerdown
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
