#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. Time Location - Featured - Scenes
#----- End List -----

#----- Nicole Basement Outing Event Love Version ----- DONE
label basementnicoleoutinglove:
    hide screen locations
    hide screen townl
    scene black
    "You decide it's time to introduce [mother] as your girl to the other gangmembers."
    scene basement 10pm 015c
    "You sit in the basement with the others waiting for [mother]."
    povi "Well today is the day. We're finally going to let them know that we're together now."
    scene basement 10pm 017c
    povi "There she is, dead sexy and beautiful as ever."
    davide "Finally, are you here to get us some drinks?"
    mom "Yes."
    scene livingroom 10pm 040
    povi "That outfit stuns me everytime, I can't wait to let this all out in the open!"
    davide "So Bruce, what do you think about what we were discussing before?"
    dad "Huh? Well I'm not sure yet, sorry..."
    scene livingroom 10pm 041
    mom "The drinks are ready. Do you need anything else?"
    "She waits a moment for anyone to speak up. No one does."
    mom "No? Well then..."
    mom "I have something to announce."
    povi "Oh, she must be eager to get this over with too."
    scene livingroom 10pm 042b
    mom "I have choosen to with someone else from now on!"
    scene livingroom 10pm 043b
    mom "He's grown up to be an amazing young man."
    mom "And we are a perfect fit for each other."
    povi "I feel the exact same way. I love her."
    dad "What?"
    scene livingroom 10pm 044b
    mom "With me supporting him, I'm certain he'll rise to new heights with in the gang."
    povi "Oh my god. She's not wearing panties with that outfit."
    mom "Wouldn't you agree, [pov]?"
    pov "Oh yes... I couldn't agree with you more."
    scene livingroom 10pm 045b
    "She's rubbing her ass softly against your crotch."
    povi "And with that, there should be little doubt left that she's being serious."
    mom "I hope you'll accept this as my choice Bruce. I'm sure you'll find another partner for yourself."
    dad "<gulp>"
    scene livingroom 10pm 046b
    mom "Don't look so confused [pov]. I told you this was what I wanted. I hope you like my little surprise announcement. <giggle>"
    povi "This is so hot. We don't have to hide our feelings anymore. I just hope Bruce can accept it. He had lost her well before I had returned by putting her in this position in the first place."
    mom "<whisper> I can feel your boner, by the way. Hnng..."
    pov "<whisper> I coudn't help be to tease you a little bit. It's so exciting."
    mom "<whisper> You reacted just like I hoped you would."
    povi "Oh yes, yes, yes..."
    scene livingroom 10pm 047b
    "She grinds her ass on you even more."
    mom "This seat is soooo hard. It's tough to find a comfortable spot. <giggle>"
    dad "..."
    davide "..."
    povi "She's using me to toy with them. I love it!"
    mom "Are there any objections with my choice?"
    scene livingroom 10pm 054b
    davide "I'm fine with it. [pov] more than pulls he weight around here. I'll find another slut in no time, haha."
    if inc == True:
        davide "And I just got see if you'd really stay in a sexual relationship with your son. That's like some \"reality tv\" bullshit right there! And I ain't even paying for cable!"
    else:
        davide "And I just got see if you'd really stay in a sexual relationship with your best friend's son. That's like some \"reality tv\" bullshit right there! And I ain't even paying for cable!"
    dad "You... He did something to her! Maybe he drugged her!"
    davide "Shut up, Bruce. You know that she's ain't on drugs! She's just being serious finally."
    dad "I'll kill that little bastard!"
    scene livingroom 10pm 055b
    davide "You'll do NOTHING! You know the gang rules! I'll fucking break you if you even think of breaking the rules!"
    dad "But she's my wife!"
    if inc == True:
        dad "And his mother for fuck sakes!"
    davide "I'm man enough to respect their decision, haha. And you'll respect it too."
    mom "Just accept it Bruce. You had your chance. I'm not staying in a relationship that hurts me everyday any longer."
    dad "What are you..."
    davide "Haha, she's right, Bruce. You had your chance but now you've been replaced, hahaha."
    scene livingroom 10pm 047aa
    davide "But we need to solve another problem now, haha."
    pov "What is that, Davide?"
    davide "Bruce have no girl anymore and every gang member should have at least one, even the ones at the bottom."
    mom "So we'll choose a new girl Bruce can have, since he can't be with me any longer."
    davide "Yes, we'll choose one suited for him this time. Some one actually in his league. So he won't lose her again, hahaha."
    dad "Please, Davide..."
    davide "Shut the fuck up you whiny bitch!"
    scene livingroom 10pm 047aaa
    davide "So any ideas which girl would be good fit for this loser? Maybe [miranda], she has very low standards, haha!"
    mom "You can't be serious!"
    povi "Damn, [mother] really hate her that much?"
    davide "Haha, relax. Nothing decided yet. But you'll accept our decision just like we accept yours."
    mom "Hmm..."
    davide "Is there someone else?"
    pov "Hmm... a girl with low standards..."
    dad "You can't be serious about all this..."
    pov "What's the deal with the girl I delivered the packages for you? The one in the subway."
    if rubyfirstmeet == False: #----- Custom -----
        scene town subway ruby
        "What's her name?"
        $ rubyname = renpy.input(_("Her name is...")) or _("Ruby")
        $ rubyname = rubyname.strip()
        if rubyname == "":
            $ rubyname = "Ruby"
        $ ruby = Character("[rubyname]", who_color="#ea9aff", what_color="#ea9aff")
    scene livingroom 10pm 047aaaa
    davide "You mean [ruby]? Haha! She's a fucking junkie. Like the serious shit, not just our candy."
    davide "She's already half-dead and I don't want to know with how many other junkies she fucked."
    davide "Or how many STD's that bitch carries. Urgh... that would be some heavy shit..."
    "There is a part of you that seriously wants revenge against Bruce for creating this fucked up situation in the first place."
    pov "But maybe that's just the right choice for him, haha."
    dad "Please, [pov]..."
    povi "Is he begging me now?"
    povi "I could choose [miranda] to be his girl. She's already a slut for the gang and even though [mother] hates her, I know Bruce has a bit of crush on her already."
    povi "Or I could choose the subway girl, [ruby]? He won't like it, but I doubt he'll turn her away after it's been long enough to miss the company of a woman."
    povi "But he could also get an STD or seriously ill from that shit. I think that would break him completly... It might even be what he deserves, but am I that cruel?"
    povi "Or maybe he needs to learn a real lesson. No girl at all to help him relieve himself. Bring back to the sexual stone age. Masterbation only."
    povi "Honestly, that might be too much. He might get angry enough to do something stupid, like raping someone for real..."
    povi "Decisions, hmm..."
    call screen basementnicoleoutinglovebruce

screen basementnicoleoutinglovebruce():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovebruce'), Jump('basementnicoleoutinglovebrucemiranda')) hovered tt.Action ("He can have [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovebruce'), Jump('basementnicoleoutinglovebruceruby')) hovered tt.Action ("He'll take [ruby]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovebruce'), Jump('basementnicoleoutinglovebrucenone')) hovered tt.Action ("He's not allowed to have any girl") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutinglovebruceruby:
    pov "Bruce can have [ruby]."
    scene livingroom 10pm 047aaa
    dad "You can't be serious!"
    davide "Haha, you're a cruel S.O.B. I like it! So be it. You should be happy Bruce. At least you still get to fuck someone, haha."
    pov "Of course you don't have to fuck her... But your own hand won't be enough at some point and then we'll see how much resolve you really have."
    dad "But why?"
    pov "You deserve it. Oh and something else, while that girl is so filthy..."
    mom "She isn't allowed to enter the house. I don't want her spreading anything to the rest of us."
    $ dadandruby = True
    jump basementnicoleoutinglove2

label basementnicoleoutinglovebrucemiranda:
    pov "Bruce is allowed to play with [miranda] too."
    scene livingroom 10pm 047aaa
    dad "Too?"
    pov "Yes, you get find some relief with her but she'll be free for the others to have fun with too."
    mom "Others?"
    povi "Is that jealousy I'm hearing?"
    mom "I hope you aren't after her too?!"
    pov "No, but Davide seems to like her too."
    davide "Ha, a wise decision. And it helps that Bruce has a crush on that slut too."
    mom "Hmph!"
    pov "I know you don't like her, but you need trust me here. It's going to be just fine."
    mom "Okay."
    pov "Good!"
    $ dadandmiranda = True
    jump basementnicoleoutinglove2

label basementnicoleoutinglovebrucenone:
    pov "He's not allowed to have any girl!"
    scene livingroom 10pm 047aaa
    dad "What?"
    davide "Haha, you can't be serious."
    pov "Oh yes, I am. He's so weak and he makes me angry just looking at him."
    dad "But why?"
    pov "Because you haven't earned it. And until you do that's just how it's going to be Bruce. Wake the fuck up and do something to earn some pussy!"
    pov "Otherwise you'll onlu have you hand to comfort you on the long nights alone down here."
    davide "Haha, I like that cruel boy. So it'll be."
    dad "But..."
    $ dadalone = True
    jump basementnicoleoutinglove2

label basementnicoleoutinglove2:
    scene livingroom 10pm 056b
    "Bruce stands up and starts into one last plea."
    dad "What's gotten into you?"
    if inc == True:
        dad "He's your son and you want to be his girl? What the actual fuck?"
    else:
        dad "He's the son of your best friend and you want to be his girl? What the actual fuck?"
    mom "Yes..."
    dad "That's not you! Did he blackmail you? Did he threaten you?"
    davide "That's enough! We made a decision and you'll accept it!"
    dad "But it's not fair!"
    davide "I don't care, it's her decision! And I won't allow you to insult other gang members that are above your ass!"
    dad "So you really want to break all taboos and be with him?"
    dad "You have no idea how disappointed I am."
    dad "But I guess you're safe, I won't risk all we did..."
    dad "YOU DAMN SLUT!"
    scene livingroom 10pm 057b
    pov "SHUT THE FUCK UP BRUCE!"
    dad "Huh?"
    pov "This shit is going to stop now and you're going to fall into fucking line! Don't forget, I know things about you! Things I know you don't want to get out into the open."
    povi "I won't of course, it could put the girls in danger. But maybe this will get him to stop and think for a moment."
    dad "..."
    pov "So are we on the same page now? You understand that you're not aren't allowed to touch your wife anymore, right?"
    pov "We're together now and I warn you, don't make me show you what I can do to fuck your life up!"
    dad "..."
    dad "Fuck you!"
    scene livingroom 10pm 058b
    dad "I'm out of here!"
    davide "Hahaha, what a great show!"
    davide "Let him go, he needs to calm the fuck down. What a pussy, haha."
    scene livingroom 10pm 059b
    davide "So, what to do now?"
    mom "Hmm..."
    mom "[pov] has a boner and I need to help him with that now."
    povi "What? Did she really said that?"
    davide "Maybe you could help me with my boner too, haha."
    mom "That's... it's [pov]'s decision."
    povi "Wait... Davide wants to join in and [mother] just left it up to me?"
    povi "She really trusts me so much so that she's willing to do something I know she doesn't want to do, if I think we needs to. "
    povi "I won't let her down. The question now is, do I need to let Davide join us to seal this deal or can I tell him to fuck off too?"
    call screen basementnicoleoutingloveshare

screen basementnicoleoutingloveshare():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutingloveshare'), Jump('basementnicoleoutingloveshareyes')) hovered tt.Action ("Share her with Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutingloveshare'), Jump('basementnicoleoutingloveshareno')) hovered tt.Action ("Don't share her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingloveshareyes:
    scene livingroom 10pm 046b
    pov "Are you really okay with that, [mother]?"
    mom "<whisper> If we play along maybe Davide will be more likely to leave us alone in the future."
    pov "<whisper> Ok, we'll play along then."
    "She looks back to Davide."
    scene livingroom 10pm 059b
    mom "I am if that is what you want, [pov]."
    davide "Great. Let's have some fun then."
    scene livingroom 10pm 065bs
    mom "Well come on, show me what you got. <giggle>"
    povi "I don't like this, but she's right. Davide is pretty easy to manipulate. Play to his ego and he gets very predictable."
    mom "Two strong men taking me..."
    pov "This is so hot."
    davide "You're a lucky guy [pov]."
    $ basement10pmnicoleoutingshare = True
    scene livingroom 10pm 066s
    davide "How about I get a blowjob, so you can ride your slut properly."
    pov "Oh, she's not my sl..."
    mom "Yes, I'm his slut! Everyone knows that gangmember's girls are just sluts."
    povi "I guess we're really laying it on thick for him. I can do that."
    pov "I can't wait to fuck you, slut."
    scene livingroom 10pm 067
    pov "God, you're so wet."
    mom "Please! Stop teasing me. I need you inside me [pov]!"
    davide "Of course she's wet, she get's two dicks to play with, haha."
    "You rub your dick on the hot, wet folds of her pussy."
    mom "Hah... hnng... please fuck me now [pov]."
    povi "I'm not sure I like her having to act like a slut with Davide around, but for now we might just need to go with it."
    scene livingroom 10pm 068s
    davide "Yes, that's it. Use your tongue!"
    mom "Hmm... <lick>"
    davide "Oh hell yeah! That tongue is amazing. You're going to have so much fun with that mouth, [pov]."
    scene livingroom 10pm 070
    mom "Aaahnn..."
    with vpunch
    pov "All in! You like my surprise?"
    mom "Hah, hah... yes..."
    scene livingroom 10pm 070s
    davide "Yes, suck on my cock."
    mom "<suck> <lick>"
    pov "I love fucking you!"
    davide "Her mouth is fantastic, haha."
    scene livingroom 10pm 071s
    davide "This is perfect! She's working my dick so eagerly because her hole is being treated properly, haha."
    pov "My \"slut\" is a great fuck. She seems to really like it too."
    davide "So is this mouth going taste my dick again?"
    povi "Not if I can help it."
    pov "We'll see."
    mom "Hnn... hnn..."
    davide "Oh, your slut likes the idea too."
    pov "Haha."
    povi "I don't think so buddy. We're going to play you for what we need to get out this and then you'll never see us again!"
    davide "I need to finish soon, her mouth is too good."
    pov "Me too."
    scene livingroom 10pm 069s
    davide "Get it deep now, ha."
    mom "Hnn..."
    davide "I really appreciate this bro. It was a good decision to let you join the gang."
    davide "You'll be able to do great things for us in the future."
    pov "Damn straight!"
    davide "Oh yes, I'm cumming, slut!"
    davide "Haaa, haaa...!"
    mom "Hmm..."
    pov "Damn, I'm so close too. She's gotten so damn tight!"
    scene livingroom 10pm 070
    call screen basementnicoleoutingloveshareyescumchoose

screen basementnicoleoutingloveshareyescumchoose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutingloveshareyescumchoose'), Jump('basementnicoleoutingloveshareyescuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutingloveshareyescumchoose'), Jump('basementnicoleoutingloveshareyescumoutside')) hovered tt.Action ("Cum over her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingloveshareyescuminside:
    pov "I'm going to cum inside you."
    mom "Hmm... yes... oh god yes!"
    pov "Ah, hnnn..."
    with vpunch
    "You cum fills her eager pussy."
    pov "I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh yeah, you're right, haha."
    scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked that, \"slut\"?"
    mom "Yes, [pov]. I like it when you cum inside me."
    pov "Good."
    scene livingroom 10pm 072sof
    davide "Yes, very good."
    pov "You good, [mother]."
    mom "Yes, hah... I'm good [pov]."
    davide "Oh she did very good. You're lucky to have this slut as your own, haha."
    jump basementnicoleoutingloveshareend

label basementnicoleoutingloveshareyescumoutside:
    pov "I'm going to cum on your ass."
    mom "Hmm..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    with vpunch
    "You spray your sperm over her ass."
    pov "I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh yeah, you're right, haha."
    scene livingroom 10pm 072o
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked that, \"slut\"?"
    mom "Yes, [pov]. I like the way your hot cum feels on me."
    pov "Good."
    scene livingroom 10pm 072sof
    davide "Yes, very good."
    pov "You good, [mother]."
    mom "Yes, hah... I'm good [pov]."
    davide "Oh she did very good. You're lucky to have this slut as your own, haha."
    jump basementnicoleoutingloveshareend

label basementnicoleoutingloveshareend:
    scene livingroom 10pm 062b
    davide "I'm out! Gonna have some drinks and maybe find Bruce and give him some more shit, haha."
    davide "I hope you have much more fun with your slut, [pov]."
    pov "Oh I will! The best part was putting Bruce in his place."
    davide "Haha, yes."
    "Davide heads out the back, leaving you two alone. You sit down on the chair behind you and catch your breath."
    scene livingroom 10pm 045a
    "[mother] gets up and kneels down in front of you."
    mom "I'm so sorry sweetie."
    pov "For what?"
    mom "I was just acting like that with Davide. I hate that man!"
    mom "I hate him so much, but we have to make him believe the lie. That we are going to help him. I know that can't be easy for you to see."
    pov "It's not easy. I hate it too. I don't want him anywhere near us, let alone getting his dick sucked off by you. And I did nothing. No worse, I encouraged it."
    "A look of shame covers her face and she seems as though she might cry at any moment."
    if inc == True:
        pov "Don't cry mom. Really, it's going to be ok. I promise. We did what we had too and soon all of this will be behind us."
    else:
        pov "Don't cry [mother]. Really, it's going to be ok. I promise. We did what we had too and soon all of this will be behind us."
    mom "I know sweetie. You know how much I love you, right? Just you."
    pov "I do. I love you too."
    "It's then you notice she's been holding on your still hard cock this whole time. A little smile replaces your serious expression."
    "She sees your smile and notices where your eyes are focused..."
    scene livingroom 10pm 049a
    mom "<lick> So... we're alone now and you're still... ready to go."
    pov "Is that a question or are you just making an observation? Haha!"
    mom "<lick> Well, I need to get a bad tastes out of my mouth and I think this is just what I need. So how about you help a girl out?"
    pov "Always willing to help a girl in need."
    scene livingroom 10pm 048a
    mom "Hmmm! <suck> <lick>"
    pov "Feels so good. I love the way you flick the tip with your tongue."
    mom "<lick> Hnng..."
    scene livingroom 10pm 046a
    pov "Oh god that's good."
    mom "<suck> Mmmm."
    scene livingroom 10pm 048a
    "She contently sucks your cock until finally you're ready for a release."
    scene livingroom 10pm 046a
    if inc == True:
        pov "I'm getting close mom!"
    else:
        pov "I'm getting close [mother]!"
    mom "Mm-Hmm! <suck>"
    "She sucks harder, her tongue milking your cock, seeking a creamy reward."
    scene livingroom 10pm 048adt
    pov "Oh yeah! I'm cumming! Hnngh!"
    with vpunch
    mom "Hnng! <suck>"
    with vpunch
    "Your cum fills her mouth as she greedily sucks it from your cock. You eventually let your hand fall back down and she looks up to you."
    scene livingroom 10pm 051i
    pov "I love it when you show me what I've given you."
    pov "You can swallow it whenever you're ready."
    scene livingroom 10pm 052i
    mom "Mmmm! <gulp>"
    "She savors the bitter taste as she swallows it all."
    scene livingroom 10pm 053i
    pov "That was so hot. I can't wait to have more fun with you."
    mom "Me too."
    scene black
    "You leave two leave the basement and go to your beds."
    $ basement10pmnicoleouting = True
    jump skip

label basementnicoleoutingloveshareno:
    pov "No Davide, I don't think so."
    pov "She's not going to be shared anymore."
    scene livingroom 10pm 061b
    davide "Oh, you're serious."
    pov "Yes, I am."
    davide "Well fuck me... I normally would just take what I wanted, but I can really appreciate how you've handled Bruce..."
    davide "So you can have your fun with her alone. She's yours now after all"
    scene livingroom 10pm 062b
    davide "I'm going to bounce. Maybe have some drinks and find Bruce so I can have some more fun with him, haha."
    davide "Have fun with your slut, [pov]."
    pov "Oh yes, I will!"
    pov "<whisper> Sorry, I didn't want to call you that to him. You not a slut, you're my lover of course."
    mom "<whisper> You're so sweet, but don't worry, I know how macho he needs to be."
    scene livingroom 10pm 065b
    mom "Come on [pov]. Don't make me wait any longer lover."
    if inc == True:
        pov "Yes, mom."
    else:
        pov "Yes, [mother]."
    mom "I want to feel you inside me again!"
    pov "I can't wait after all that hot teasing you did."
    scene livingroom 10pm 066
    "You walk over to her."
    pov "So did this really turn you on?"
    mom "Oh yes... feeling your big boner while we were telling them. Feeling how much you want me."
    if inc == True:
        pov "I want you so much, mom!"
    else:
        pov "I want you so much, [mother]!"
    mom "<giggle> Then stick it in, [pov]."
    scene livingroom 10pm 067
    pov "You're so wet."
    mom "Please stop teasing me."
    pov "You teased me all night! Now it's my turn, haha."
    "You rub your dick on her the wet folds of her pussy."
    mom "Please... fuck me already, [pov]."
    if inc == True:
        pov "As you wish, mom!"
    else:
        pov "As you wish, [mother]!"
    scene livingroom 10pm 070
    mom "Aahhh... yes!"
    pov "Ohh... it slide all the way in."
    mom "I can feel you so deep inside me!"
    scene livingroom 10pm 068
    mom "Ohh, hah... you're so wild tonight. It feels great!"
    with vpunch
    pov "I can't help it. I love you so much!"
    with vpunch
    mom "I love you too, I love you so much [pov]!"
    with vpunch
    pov "I want to always be together from now on."
    mom "Oh hah, I want that too."
    pov "But what if they tell other people about us... outside the family?"
    mom "I don't care anymore. Everyone can know. I just, hah, want to be with you."
    pov "Oh yes, this is like heaven."
    mom "We just need to make it through this. And when it's over we'll find a way to stay together."
    if inc == True:
        pov "Oh yes, I'm so close, mom!"
    else:
        pov "Oh yes, I'm so close, [mother]!"
    mom "Me too, let's cum together, hah..."
    call screen basementnicoleoutinglovesharenocumchoose

screen basementnicoleoutinglovesharenocumchoose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovesharenocumchoose'), Jump('basementnicoleoutinglovesharenocuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovesharenocumchoose'), Jump('basementnicoleoutinglovesharenocumoutside')) hovered tt.Action ("Cum over her ass") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutinglovesharenocuminside:
    pov "I... I want to cum inside you!"
    mom "Yes, hah... cum inside me..."
    scene livingroom 10pm 070
    pov "Ah, hnnn..."
    with vpunch
    "You spurt your sperm inside her."
    mom "AAAAHH... yes..."
    with vpunch
    scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah... so much of your sperm is inside me."
    pov "You're the one who turned me on that much!"
    jump basementnicoleoutinglovesharenoend

label basementnicoleoutinglovesharenocumoutside:
    pov "I'll cum over your ass."
    mom "Yes... do it... hah..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    "You spray your sperm over her ass."
    scene livingroom 10pm 072o
    pov "What a wonderful view."
    mom "Hah... hah... I can feel so much hot cum on my ass."
    pov "You're the one who turned me on that much!"
    jump basementnicoleoutinglovesharenoend

label basementnicoleoutinglovesharenoend:
    mom "Hah... hah... I needed that."
    pov "Me too. Holy shit that was hot."
    mom "I love you [pov]."
    pov "I love you too."
    scene black
    "You leave two leave the basement and go to your beds."
    $ basement10pmnicoleouting = True
    jump skip

#----- Nicole Basement Outing Custom Event Love to corruption Version ----- DONE
label basementnicoleoutinglovecor:
    hide screen locations
    hide screen townl
    scene black
    "You decide it's time to introduce [mother] as your girl to the other gangmembers."
    scene basement 10pm 015c
    "You sit in the basement with the others waiting for [mother]."
    povi "Well today is the day. We're finally going to let these assholes know that we're together now."
    scene basement 10pm 017c
    povi "There she is, so fucking sexy."
    davide "Finally, are you here to get us some drinks?"
    mom "Yes."
    scene livingroom 10pm 040
    povi "That outfit excites me everytime, I can't wait to let this all out in the open!"
    davide "So Bruce, what do you think about what we were discussing before?"
    dad "Huh? Well I'm not sure yet, sorry..."
    scene livingroom 10pm 041
    mom "The drinks are ready. Do you need anything else?"
    "She waits a moment for anyone to speak up. No one does."
    mom "No? Well then..."
    mom "I have something to announce."
    povi "Oh, she must be eager to get this over with too."
    scene livingroom 10pm 042b
    mom "I have choosen to with someone else from now on!"
    scene livingroom 10pm 043b
    mom "He's grown up to be an amazingly hot young man."
    mom "And we are a perfect fit for each other."
    povi "Yes we are!"
    dad "What?"
    scene livingroom 10pm 044b
    mom "With me supporting him, I'm certain he'll rise to new heights with in the gang."
    povi "She's not wearing panties with that outfit. What a naughty girl!"
    mom "Wouldn't you agree, [pov]?"
    pov "Oh yes... I couldn't agree with you more."
    scene livingroom 10pm 045b
    "She's rubbing her ass softly against your crotch."
    povi "With her grinding her ass on me like that, there should be little doubt left that she's being serious."
    mom "You're going to have to accept this as my choice Bruce. I'm sure you'll find something else for yourself."
    dad "<gulp>"
    scene livingroom 10pm 046b
    mom "I can tell you're getting excited too [pov]. I hope you like my little surprise announcement. <giggle>"
    povi "This is so hot. We don't have to hide anymore. And Bruce is going to accept it if he knows what's best for him."
    mom "<whisper> I can feel your boner, by the way. Hnng..."
    pov "<whisper> I thought it would be fun to tease you a little bit. It's so exciting."
    mom "<whisper> You reacted just like I hoped you would."
    povi "Oh yes, yes, yes..."
    scene livingroom 10pm 047b
    "She grinds her ass on you even more."
    mom "This seat is soooo hard. It's tough to find a comfortable spot. <giggle>"
    dad "..."
    davide "..."
    povi "She's using me to toy with them. I love it!"
    mom "Are there any objections?"
    scene livingroom 10pm 054b
    davide "I'm fine with it. [pov] more than pulls he weight around here. I'll find another slut in no time, haha."
    if inc == True:
        davide "And I just got see if you'd really stay in a sexual relationship with your son. That's like some \"reality tv\" bullshit right there! And I ain't even paying for cable!"
    else:
        davide "And I just got see if you'd really stay in a sexual relationship with your best friend's son. That's like some \"reality tv\" bullshit right there! And I ain't even paying for cable!"
    dad "You... He did something to her! Maybe he drugged her!"
    davide "Shut up, Bruce. You know that she's ain't on drugs! She's just being serious finally."
    dad "I'll kill that little bastard!"
    scene livingroom 10pm 055b
    davide "You'll do NOTHING! You know the gang rules! I'll fucking break you if you even think of breaking the rules!"
    dad "But she's my wife!"
    if inc == True:
        dad "And his mother for fuck sakes!"
    davide "I'm man enough to respect their decision, haha. And you'll respect it too."
    mom "Just accept it Bruce. You had your chance. I need a real man in my life. Someone that can really satisfy me."
    dad "What are you..."
    davide "Haha, she's right, Bruce. You had your chance but now you've been replaced, hahaha."
    scene livingroom 10pm 047aa
    davide "But we need to solve another problem now, haha."
    pov "What is that, Davide?"
    davide "Bruce have no girl anymore and every gang member should have at least one, even the ones at the bottom."
    mom "So we'll choose a new girl Bruce can have, since he can't be with me any longer."
    davide "Yes, we'll choose one suited for him this time. Some one actually in his league. So he won't lose her again, hahaha."
    dad "Please, Davide..."
    davide "Shut the fuck up you whiny bitch!"
    scene livingroom 10pm 047aaa
    davide "So any ideas which girl would be good fit for this loser? Maybe [miranda], she has very low standards, haha!"
    mom "You can't be serious!"
    povi "Damn, [mother] really hate her that much?"
    davide "Haha, relax. Nothing decided yet. But you'll accept our decision just like we accept yours."
    mom "Hmm..."
    davide "Is there someone else?"
    pov "Hmm... a girl with low standards..."
    dad "You can't be serious about all this..."
    pov "What's the deal with the girl I delivered the packages for you? The one in the subway."
    if rubyfirstmeet == False: #----- Custom -----
        scene town subway ruby
        "What's her name?"
        $ rubyname = renpy.input(_("Her name is...")) or _("Ruby")
        $ rubyname = rubyname.strip()
        if rubyname == "":
            $ rubyname = "Ruby"
        $ ruby = Character("[rubyname]", who_color="#ea9aff", what_color="#ea9aff")
    scene livingroom 10pm 047aaaa
    davide "You mean [ruby]? Haha! She's a fucking junkie. Like the serious shit, not just our candy."
    davide "She's already half-dead and I don't want to know with how many other junkies she fucked."
    davide "Or how many STD's that bitch carries. Urgh... that would be some heavy shit..."
    "There is a part of you that seriously wants revenge against Bruce for creating this fucked up situation in the first place."
    pov "But maybe that's just the right choice for him, haha."
    dad "Please, [pov]..."
    povi "Haha! He's beggin me now! Pathetic."
    povi "I could choose [miranda] to be his girl. She's already a slut for the gang and even though [mother] hates her, I know Bruce has a bit of crush on her already."
    povi "Or I could choose the subway girl, [ruby]? He won't like it, but I doubt he'll turn her away after it's been long enough to miss the company of a woman."
    povi "Maybe he'll get an STD or seriously ill from that shit. I think that would break him completly... It's more than he deserves!"
    povi "Or maybe he needs to learn a real lesson. No girl at all to help him relieve himself. Bring back to the sexual stone age. Masterbation only."
    povi "Honestly, that might be too much. He might get angry enough to do something stupid, like raping someone for real..."
    povi "Decisions, hmm..."
    call screen basementnicoleoutinglovebrucecor

screen basementnicoleoutinglovebrucecor():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovebrucecor'), Jump('basementnicoleoutinglovebrucemirandacor')) hovered tt.Action ("He can have [miranda]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovebrucecor'), Jump('basementnicoleoutinglovebrucerubycor')) hovered tt.Action ("He'll take [ruby]") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovebrucecor'), Jump('basementnicoleoutinglovebrucenonecor')) hovered tt.Action ("He's not allowed to have any girl") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutinglovebrucerubycor:
    pov "Bruce can have [ruby]."
    scene livingroom 10pm 047aaa
    dad "You can't be serious!"
    davide "Haha, you're a cruel S.O.B. I like it! So be it. You should be happy Bruce. At least you still get to fuck someone, haha."
    pov "Of course you don't have to fuck her... But your own hand won't be enough at some point and then we'll see how much resolve you really have."
    dad "But why?"
    pov "You deserve it. Oh and something else, while that girl is so filthy..."
    mom "She isn't allowed to enter the house. I don't want her spreading anything to the rest of us."
    $ dadandruby = True
    jump basementnicoleoutinglove2cor

label basementnicoleoutinglovebrucemirandacor:
    pov "Bruce is allowed to play with [miranda] too."
    scene livingroom 10pm 047aaa
    dad "Too?"
    pov "Yes, you get find some relief with her but she'll be free for the others to have fun with too."
    mom "Others?"
    povi "Is that jealousy I'm hearing?"
    mom "I hope you aren't after her too?!"
    pov "No, but Davide seems to like her too."
    davide "Ha, a wise decision. And it helps that Bruce has a crush on that slut too."
    mom "Hmph!"
    pov "I know you don't like her, but you're going to do what I say slut. It's going to be just fine."
    mom "Okay..."
    pov "Good!"
    $ dadandmiranda = True
    jump basementnicoleoutinglove2cor

label basementnicoleoutinglovebrucenonecor:
    pov "He's not allowed to have any girl!"
    scene livingroom 10pm 047aaa
    dad "What?"
    davide "Haha, you can't be serious."
    pov "Oh yes, I am. He's so weak and he makes me angry just looking at him."
    dad "But why?"
    pov "Because you haven't earned it. And until you do that's just how it's going to be Bruce. Wake the fuck up and do something to earn some pussy!"
    pov "Otherwise you'll onlu have you hand to comfort you on the long nights alone down here."
    davide "Haha, I like that cruel boy. So it'll be."
    dad "But..."
    $ dadalone = True
    jump basementnicoleoutinglove2cor

label basementnicoleoutinglove2cor:
    scene livingroom 10pm 056b
    "Bruce stands up and starts into one last plea."
    dad "What's gotten into you?"
    if inc == True:
        dad "He's your son and you want to be his slut? What the actual fuck?"
    else:
        dad "He's the son of your best friend and you want to be his slut? What the actual fuck?"
    mom "Yes..."
    dad "That's not you! Did he blackmail you? Did he threaten you?"
    davide "That's enough! We made a decision and you'll accept it!"
    dad "But it's not fair!"
    davide "I don't care, it's her decision! And I won't allow you to insult other gang members that are above your ass!"
    dad "So you really want to break all taboos and be with him?"
    dad "You have no idea how disappointed I am."
    dad "But I guess you're safe, I won't risk all we did..."
    dad "YOU DAMN SLUT!"
    scene livingroom 10pm 057b
    pov "SHUT THE FUCK UP BRUCE!"
    dad "Huh?"
    pov "This shit is going to stop now and you're going to fall into fucking line! Don't forget, I know things about you! Things I know you don't want to get out into the open."
    povi "I won't of course, it could put the girls in danger. This should get him to stop and think for a moment."
    dad "..."
    pov "So are we on the same page now? You understand that you're not aren't allowed to touch your wife anymore, right?"
    pov "We're together now and I warn you, don't make me show you what I can do to fuck your life up!"
    dad "..."
    dad "Fuck you!"
    scene livingroom 10pm 058b
    dad "I'm out of here!"
    davide "Hahaha, what a great show!"
    davide "Let him go, he needs to calm the fuck down. What a pussy, haha."
    scene livingroom 10pm 059b
    davide "So, what to do now?"
    mom "Hmm..."
    mom "[pov] has a boner and I need to help him get off now."
    povi "Did she really said that? Awesome"
    davide "Maybe you could help me with my boner too, haha."
    mom "That's... it's [pov]'s decision."
    povi "Wait... Davide wants to join in and [mother] just left it up to me?"
    povi "She being so submissive now. Letting me decided if I want the share her or not."
    povi "The question now is, do I need to let Davide join us to seal this deal or can I tell him to fuck off too?"
    call screen basementnicoleoutinglovesharecor

screen basementnicoleoutinglovesharecor():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovesharecor'), Jump('basementnicoleoutingloveshareyescor')) hovered tt.Action ("Share her with Davide") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovesharecor'), Jump('basementnicoleoutinglovesharenocor')) hovered tt.Action ("Don't share her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingloveshareyescor:
    scene livingroom 10pm 046b
    pov "Are you ready to help him out too, [mother]?"
    "She looks back to Davide."
    scene livingroom 10pm 059b
    mom "I am if that is what you want, [pov]."
    davide "Great. Let's have some fun then."
    scene livingroom 10pm 065bs
    mom "Well come on, show me what you got. <giggle>"
    povi "Davide is so easy to manipulate. Play to his ego and he gets very predictable."
    mom "Two strong men taking me..."
    pov "This is so hot."
    davide "You're a lucky guy [pov]."
    $ basement10pmnicoleoutingshare = True
    scene livingroom 10pm 066s
    davide "How about I get a blowjob, so you can ride your slut properly."
    pov "I wouldn't have it any other way! [mother] tell me what you are..."
    mom "I'm big fucking slut! Everyone knows that gangmember's girls are just dirty sluts."
    povi "She's really getting into this."
    pov "I can't wait to fuck you, slut."
    scene livingroom 10pm 067
    pov "God, you're so damn wet."
    mom "Please! Stop teasing me. I need your hard cock inside me [pov]!"
    davide "Of course she's wet, she get's two dicks to play with, haha."
    "You rub your dick on the hot, wet folds of her pussy."
    mom "Hah... hnng... please fuck me now [pov]."
    povi "I love that she's acting like slut even with Davide around. She doesn't want to let me down."
    scene livingroom 10pm 068s
    davide "Yes, that's it. Use your tongue!"
    mom "Hmm... <lick>"
    davide "Oh hell yeah! That tongue is amazing. You're going to have so much fun with that mouth, [pov]."
    scene livingroom 10pm 070
    mom "Aaahnn..."
    with vpunch
    pov "All in! You like my surprise?"
    mom "Hah, hah... yes..."
    scene livingroom 10pm 070s
    davide "Yes, suck on my cock."
    mom "<suck> <lick>"
    pov "I love fucking you!"
    davide "Her mouth is fantastic, haha."
    scene livingroom 10pm 071s
    davide "This is perfect! She's working my dick so eagerly because her hole is being treated properly, haha."
    pov "My \"slut\" is a great fuck. She seems to really like it too."
    davide "So is this mouth going taste my dick again?"
    povi "Maybe, depends if I still need anything from you."
    pov "We'll see."
    mom "Hnn... hnn..."
    davide "Oh, your slut likes the idea too."
    pov "Haha."
    povi "Meh. I'm sure she's just trying to please me more than anything, but whatever you want to tell yourself Davide."
    davide "I need to finish soon, her mouth is too good."
    pov "Me too."
    scene livingroom 10pm 069s
    davide "Get it deep now, ha."
    mom "Hnn..."
    davide "I really appreciate this bro. It was a good decision to let you join the gang."
    davide "You'll be able to do great things for us in the future."
    pov "Damn straight!"
    davide "Oh yes, I'm cumming, slut!"
    davide "Haaa, haaa...!"
    mom "Hmm..."
    pov "Damn, I'm so close too. She's gotten so damn tight!"
    scene livingroom 10pm 070
    call screen basementnicoleoutingloveshareyescumchoosecor

screen basementnicoleoutingloveshareyescumchoosecor():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutingloveshareyescumchoosecor'), Jump('basementnicoleoutingloveshareyescuminsidecor')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutingloveshareyescumchoosecor'), Jump('basementnicoleoutingloveshareyescumoutsidecor')) hovered tt.Action ("Cum over her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutingloveshareyescuminsidecor:
    pov "I'm going to cum inside you."
    mom "Hmm... yes... oh god yes!"
    pov "Ah, hnnn..."
    with vpunch
    "You cum fills her eager pussy."
    pov "I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh yeah, you're right, haha."
    scene livingroom 10pm 072ip
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked that, \"slut\"?"
    mom "Yes, [pov]. I like it when you cum inside me."
    pov "Good."
    scene livingroom 10pm 072sof
    davide "Yes, very good."
    pov "You good, [mother]."
    mom "Yes, hah... I'm good [pov]."
    davide "Oh she did very good. You're lucky to have this slut as your own, haha."
    jump basementnicoleoutingloveshareendcor

label basementnicoleoutingloveshareyescumoutsidecor:
    pov "I'm going to cum on your ass."
    mom "Hmm..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    with vpunch
    "You spray your sperm over her ass."
    pov "I could do this everyday."
    davide "Haha, you can do it everyday."
    pov "Oh yeah, you're right, haha."
    scene livingroom 10pm 072o
    pov "What a wonderful view."
    mom "Hah... hah..."
    pov "You liked that, \"slut\"?"
    mom "Yes, [pov]. I like the way your hot cum feels on me."
    pov "Good."
    scene livingroom 10pm 072sof
    davide "Yes, very good."
    pov "You good, [mother]."
    mom "Yes, hah... I'm good [pov]."
    davide "Oh she did very good. You're lucky to have this slut as your own, haha."
    jump basementnicoleoutingloveshareendcor

label basementnicoleoutingloveshareendcor:
    scene livingroom 10pm 062b
    davide "I'm out! Gonna have some drinks and maybe find Bruce and give him some more shit, haha."
    davide "I hope you have much more fun with your slut, [pov]."
    pov "Oh I will! The best part was putting Bruce in his place."
    davide "Haha, yes."
    "Davide heads out the back, leaving you two alone. You sit down on the chair behind you and catch your breath."
    scene livingroom 10pm 045a
    "[mother] gets up and kneels down in front of you."
    mom "I'm so sorry [pov]."
    pov "For what?"
    mom "I was just acting like that with Davide. I hate that man!"
    mom "I hate him so much, but we have to make him believe the lie. That we are going to help him. Then we can do what you said and take him out when we're ready."
    pov "That's fine. I know you don't care for that asshole. Soon he'll be ancient history."
    "You notice she's been holding on your still hard cock this whole time. A smile replaces your serious expression."
    "She sees your smile and notices where your eyes are focused..."
    scene livingroom 10pm 049a
    mom "<lick> So... we're alone now and you're still... ready to go."
    pov "Is that a question or are you just making an observation? Haha!"
    mom "<lick> Well, I need to get a bad tastes out of my mouth and I think this is just what I need. So how about you help a girl out?"
    pov "Always willing to help a girl in need. You're such a good little whore."
    scene livingroom 10pm 048a
    mom "Hmmm! <suck> <lick>"
    pov "Feels so good. I love the way you flick the tip with your tongue."
    mom "<lick> Hnng..."
    scene livingroom 10pm 046a
    pov "Oh god that's good."
    mom "<suck> Mmmm."
    scene livingroom 10pm 048a
    "She contently sucks your cock until finally you're ready for a release."
    scene livingroom 10pm 046a
    if inc == True:
        pov "I'm getting close mom!"
    else:
        pov "I'm getting close [mother]!"
    mom "Mm-Hmm! <suck>"
    "She sucks harder, her tongue milking your cock, seeking a creamy reward."
    scene livingroom 10pm 048adt
    pov "Oh yeah! I'm cumming! Hnngh!"
    with vpunch
    mom "Hnng! <suck>"
    with vpunch
    "Your cum fills her mouth as she greedily sucks it from your cock. You eventually let your hand fall back down and she looks up to you."
    scene livingroom 10pm 051i
    pov "I love it when you show me what I've given you slut."
    pov "You can swallow it now."
    scene livingroom 10pm 052i
    mom "Mmmm! <gulp>"
    "She savors the bitter taste as she swallows it all."
    scene livingroom 10pm 053i
    pov "That was so hot. I can't wait to have more fun with my personal slut."
    mom "Me too."
    scene black
    "You leave two leave the basement and go to your beds."
    $ basement10pmnicoleouting = True
    jump skip

label basementnicoleoutinglovesharenocor:
    pov "No Davide, I don't think so."
    pov "She's not going to be shared anymore."
    scene livingroom 10pm 061b
    davide "Oh, you're serious."
    pov "Yes, I am."
    davide "Well fuck me... I normally would just take what I wanted, but I can really appreciate how you've handled Bruce..."
    davide "So you can have your fun with her alone. She's yours now after all"
    scene livingroom 10pm 062b
    davide "I'm going to bounce. Maybe have some drinks and find Bruce so I can have some more fun with him, haha."
    davide "Have fun with your slut, [pov]."
    pov "Oh yes, I will!"
    scene livingroom 10pm 065b
    mom "Come on [pov]. Don't make my wet pussy wait any longer."
    if inc == True:
        pov "Yes, mom."
    else:
        pov "Yes, [mother]."
    mom "I want to feel you inside me again!"
    pov "I can't wait after all that hot teasing you did."
    scene livingroom 10pm 066
    "You walk over to her."
    pov "So tell me what turne you on so much slut."
    mom "Feeling your hard cock while we were telling them. Feeling how much you want me."
    if inc == True:
        pov "I do want you, mom."
    else:
        pov "I do want you, [mother]."
    mom "<giggle> Then stick it in, [pov]."
    scene livingroom 10pm 067
    pov "You're so fucking wet."
    mom "Please stop teasing me."
    pov "You teased me all night slut! Now it's my turn, haha."
    "You rub your dick on her the wet folds of her pussy."
    mom "Please... fuck me already, [pov]."
    if inc == True:
        pov "As you wish, mom!"
    else:
        pov "As you wish, [mother]!"
    scene livingroom 10pm 070
    mom "Aahhh... yes!"
    pov "Ohh... it slide all the way in."
    mom "I can feel you so deep inside me!"
    scene livingroom 10pm 068
    mom "Ohh, hah... you're so wild tonight."
    with vpunch
    pov "I can't help it. It feels great to be with a slut that knows what she wants!"
    with vpunch
    mom "I love this, I love fucking you so much [pov]!"
    with vpunch
    pov "I want to fuck you all the time now."
    mom "Oh hah, I want that too."
    pov "But then other people could find out about us... people outside the family."
    mom "I don't care anymore. Everyone can know that I'm your slut. Your personal cock sleave!"
    pov "That's my good girl."
    if inc == True:
        pov "I'm so close, mom!"
    else:
        pov "I'm so close, [mother]!"
    mom "Me too, cum for me, hah..."
    call screen basementnicoleoutinglovesharenocumchoosecor

screen basementnicoleoutinglovesharenocumchoosecor():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovesharenocumchoosecor'), Jump('basementnicoleoutinglovesharenocuminsidecor')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('basementnicoleoutinglovesharenocumchoosecor'), Jump('basementnicoleoutinglovesharenocumoutsidecor')) hovered tt.Action ("Cum over her ass") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basementnicoleoutinglovesharenocuminsidecor:
    pov "I'm going to cum inside you!"
    mom "Yes, hah... cum inside me..."
    scene livingroom 10pm 070
    pov "Ah, hnnn..."
    with vpunch
    "You spurt your sperm inside her."
    mom "AAAAHH... yes..."
    with vpunch
    scene livingroom 10pm 072ip
    pov "What a wonderful view slut."
    mom "Hah... hah... so much of your sperm is inside me."
    jump basementnicoleoutinglovesharenoendcor

label basementnicoleoutinglovesharenocumoutsidecor:
    pov "I'll cum over your ass."
    mom "Yes... do it... hah..."
    scene livingroom 10pm 071o
    pov "Ah, hnnn..."
    "You spray your sperm over her ass."
    scene livingroom 10pm 072o
    pov "What a wonderful view slut."
    mom "Hah... hah... I can feel so much hot cum on my ass."
    jump basementnicoleoutinglovesharenoendcor

label basementnicoleoutinglovesharenoendcor:
    pov "I needed that."
    mom "Hah... hah... I needed that too."
    pov "You can clean yourself up for tonight. I'm done with you for now."
    mom "Oh...Okay. Thank you [pov]."
    scene black
    "You leave two leave the basement and go to your beds."
    $ basement10pmnicoleouting = True
    jump skip

#----- Nicole Downstairs Shower Third Corruption Event ----- DONE
label showerd15fuckslut:
    $ shower15corthird = True
    pov "Haha! That's funny!"
    mom "Huh?"
    pov "It's ok to play innocent, but don't pretend to be stupid too."
    pov "I need to fuck my slut now."
    mom "But... someone could see us here..."
    pov "I don't care! Everyone already know that you're my slut."
    if inc == True:
        mom "But your sisters could catch us..."
    else:
        mom "But my daughters could catch us..."
    if basement10cassandraouting == True:
        pov "Hmm, you're right. And then [bs] could join us then, haha."
        mom "Hnn..."
    else:
        pov "I don't care. Neither should you."
    pov "Now turn around so I can choose a hole."
    mom "But..."
    pov "NOW, SLUT!"
    mom "Yes... I'm sorry [pov]..."
    scene showerdownstairs 3pm 029x
    pov "So, which hole should I choose?"
    mom "It's up to you [pov]..."
    call screen showerd15fuckslutchoose

screen showerd15fuckslutchoose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('showerd15fuckslutchoose'), Jump('showerd15fuckslutpussy')) hovered tt.Action ("Fuck her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('showerd15fuckslutchoose'), Jump('showerd15fuckslutass')) hovered tt.Action ("Fuck her ass") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerd15fuckslutass:
    $ showerd15corass = True
    jump showerd15fuckslutpussy

label showerd15fuckslutpussy:
    if showerd15corass == False:
        pov "I'll fuck your pussy this time."
        mom "Yes, fuck me."
        scene showerdownstairs 3pm 030xap
        "You stick your dick in her pussy."
    else:
        pov "I'll fuck your ass this time."
        mom "Yes, fuck me."
        scene showerdownstairs 3pm 030xaa
        "You stick your dick in her ass."
    mom "Ahh..."
    pov "You're so wet. I knew you wanted it."
    mom "Hnn..."
    if showerd15corass == False:
        scene showerdownstairs 3pm 031xap
        pov "Your tight pussy is craving my dick."
    else:
        scene showerdownstairs 3pm 031xaa
        pov "Your tight ass is craving my dick."
    mom "Hnn... hah..."
    pov "You're happy now that I didn't stop! Aren't you, slut? Why do you keep pretending you don't want this?"
    mom "Hah...hah... hnn..."
    povi "She just won't be honest with herself."
    "You start to fuck her harder!"
    pov "I'm right, aren't I? Answer me!"
    scene showerdownstairs 3pm 032xa
    mom "Yes! I want it! Fuck me more!"
    pov "Good answer."
    mom "Hah... hah... not so rough..."
    povi "She's still being timid. I can't have that if we're both to have a good time here."
    pov "Then I want you to cum for me!"
    mom "Hah... cum for you...?"
    pov "Yes, if you've been as eager as I have been for this, then it should be easy enough."
    povi "I think she's still afraid to get caught, so she just wants me to finish quickly. That's not going to work for me."
    "You fuck her even harder and rougher."
    scene showerdownstairs 3pm 033xa
    mom "Ahh... haah... haah..."
    pov "Cum for me slut! Show me how much you like it!"
    mom "Hnn... I'm close... I'm going cum any moment..."
    povi "She's not shaking or getting tighter like she usually does. She's lying."
    povi "Does she really think she's tricking me? Sad, just sad."
    if showerd15corass == False:
        scene showerdownstairs 3pm 034xap
    else:
        scene showerdownstairs 3pm 034xaa
    mom "OHHH... yes... I'm cumming..."
    pov "Hahaha..."
    mom "Hah... why are you laughing...?"
    pov "I thought you'd at least try to fake it better than that slut! We aren't going to rush this just because you're afraid of getting caught."
    mom "What...? No..."
    pov "I've felt your ograsms before... That was no orgasm."
    mom "No, you're wrong..."
    if showerd15corass == False:
        scene showerdownstairs 3pm 035xap
    else:
        scene showerdownstairs 3pm 035xaa
    pov "We're going to fuck long and hard until you cum properly. Even if it takes us all night!"
    "You grab her hair."
    mom "Please! I want to make you happy, but not here..."
    pov "Why do you pretend still?! This is hardly something new."
    mom "Hah... I'm sorry... please..."
    "You take her rougher."
    mom "Hnn... hah... hah..."
    pov "Or maybe you want to make things even more risky?"
    mom "What... hah..."
    "You thrust into her harder."
    pov "You're not stopping me. Not really, just meager protests about getting caught. You've never said you wanted to stop..."
    with vpunch
    mom "Hnng!"
    with vpunch
    scene showerdownstairs 3pm 036xa
    pov "I want you to tell me what you are and how much you like it."
    mom "Hah... I'm your slut and I like getting fucked by your dick."
    pov "Again, louder!"
    mom "Hah... but... someone could hear me..."
    pov "You're right, [bs] will be home soon, so you better hurry."
    pov "We're going to keep going until you say it louder anyway! So you might as well let it all out now."
    mom "Hah... ahh..."
    pov "You need to cum for real, slut!"
    mom "But..."
    pov "You were the one that decided to be my slut, so act like it!"
    mom "Hah... hnng..."
    mom "I'M YOUR SLUT! YOU FUCK ME LIKE A WHORE! I LOVE IT!"
    if showerd15corass == False:
        mom "I LOVE YOUR HARD COCK INSIDE MY PUSSY, CLAIMING ME AS YOURS!"
    else:
        mom "I LOVE YOUR HARD COCK INSIDE MY ASS, CLAIMING ME AS YOURS!"
    mom "AHHH...HAH..."
    povi "This time she's shaking like a good slut."
    pov "Good girl!"
    mom "Hah... hah..."
    pov "I'm close to cumming too."
    call screen showerd15fuckslutcumchoose

screen showerd15fuckslutcumchoose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('showerd15fuckslutcumchoose'), Jump('showerd15fuckslutcuminside')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('showerd15fuckslutcumchoose'), Jump('showerd15fuckslutcumout')) hovered tt.Action ("Cum on her ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('showerd15fuckslutcumchoose'), Jump('showerd15fuckslutcummouth')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('showerd15fuckslutcumchoose'), Jump('showerd15fuckslutcumface')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label showerd15fuckslutcuminside:
    if showerd15corass == True:
        scene showerdownstairs 3pm 037xaa
        pov "I'm going to cum in your ass."
        mom "Yes [pov]. Fill my ass with your hot cum!"
        povi "Good, she's submissive again."
        pov "AHH...HNNG...!"
        with vpunch
        "You cum in her ass."
        mom "Hnn..."
        with vpunch
        pov "So good, now let me take a good look."
        scene showerdownstairs 3pm 038xao
        mom "Hmm..."
        pov "There's so much cum... You did good girl."
        mom "Hnng... Thank you."
        scene showerdownstairs 3pm 042xar
        pov "Next time just be a good slut and do what I say. Trust me and we'll both have plenty of fun."
        mom "Y...yes [pov]."
        pov "Now you can finish your shower if you want."
        jump showerd15fuckslutend
    else:
        scene showerdownstairs 3pm 037xap
        pov "I'm going to cum in your pussy."
        mom "Yes [pov]. Fill my womb with your hot cum!"
        povi "Good, she's submissive again."
        pov "AHH...HNNG...!"
        with vpunch
        "You cum in her pussy."
        mom "Hnn..."
        with vpunch
        pov "So good, now let me take a good look."
        scene showerdownstairs 3pm 038xai
        mom "Hmm..."
        pov "There's so much cum... You did good girl."
        mom "Hnng... Thank you."
        scene showerdownstairs 3pm 042xar
        pov "Next time just be a good slut and do what I say. Trust me and we'll both have plenty of fun."
        mom "Y...yes [pov]."
        pov "Now you can finish your shower if you want."
        jump showerd15fuckslutend

label showerd15fuckslutcumout:
    if showerd15corass == True:
        scene showerdownstairs 3pm 037xaa
    else:
        scene showerdownstairs 3pm 037xap
    pov "I'm going to cum on your ass."
    mom "Yes [pov]. Cover my ass with your hot cum!"
    povi "Good, she's submissive again."
    scene showerdownstairs 3pm 038xab
    pov "AHH...HNNG...!"
    with vpunch
    "You cum on her ass."
    mom "Hnng..."
    with vpunch
    pov "So good, now let me take a good look."
    scene showerdownstairs 3pm 042xar
    pov "That's a beautiful sight."
    pov "Next time just be a good slut and do what I say. Trust me and we'll both have plenty of fun."
    mom "Y...yes [pov]."
    pov "Now you can finish your shower if you want."
    jump showerd15fuckslutend

label showerd15fuckslutcummouth:
    pov "Get on your knees, I want to cum in your mouth."
    mom "Okay."
    scene showerdownstairs 3pm 038xaf
    pov "Do your best to make it something I'll never forget."
    mom "And then I'll show you how much you gave me, before I swallow it."
    pov "Very good. You're back to your senses. That's just how I like my slut."
    mom "Yes, I'm sorry about before. I'll stop trying to... hold back."
    pov "That's good to hear."
    scene showerdownstairs 3pm 039xam
    pov "Now, taste it."
    mom "Hmm... <suck> <lick>"
    pov "Oh yes, like that."
    mom "Mmmm... <lick> <suck>"
    pov "I'm going to cum!"
    pov "AHHH...HNNG..."
    with vpunch
    "You cum in her mouth."
    mom "Hnng..."
    with vpunch
    scene showerdownstairs 3pm 040xam
    mom "Ahh..."
    pov "Good."
    povi "I came so much, she couldn't hold it all."
    scene showerdownstairs 3pm 041xam
    mom "<gulp>"
    pov "I think I'll ignore your reluctance this time, because you came back to your senses."
    pov "But if this keeps happening then we're going to have to keep going until scream even more next time."
    povi "Then again, maybe she'll start screaming on her own next time."
    scene showerdownstairs 3pm 042xam
    mom "Ahhh..."
    pov "Very good. Now I just need to hear one last thing from my slut."
    mom "Thank you for your tasty sperm... [pov]..."
    pov "And...?"
    mom "Thank you for fucking me so good and hard until I came all over your big dick."
    scene showerdownstairs 3pm 043xam
    pov "You're welcome, and next time just be a good slut and do what I say."
    pov "Trust me and we'll both have plenty of fun."
    mom "Y...yes [pov]."
    pov "Now you can finish your shower if you want."
    jump showerd15fuckslutend

label showerd15fuckslutcumface:
    pov "Get on your knees, I want to cum on your face."
    mom "Yes [pov]."
    scene showerdownstairs 3pm 038xaf
    pov "Get ready to get plastered with cum."
    mom "I'm ready, thank you for giving me a warning."
    pov "Very good. You're back to your senses. That's just how I like my slut."
    mom "Yes, I'm sorry about before. I'll stop trying to... hold back."
    pov "That's good to hear."
    scene showerdownstairs 3pm 039xaf
    pov "Here is comes. AHHH...HNNG..."
    with vpunch
    "You cum on her face."
    mom "Hnng..."
    with vpunch
    scene showerdownstairs 3pm 040xaf
    mom "Ahh..."
    pov "So Good."
    povi "I came so much, it's all over her face."
    pov "You look so hot, covered in my sperm."
    mom "Hmm..."
    scene showerdownstairs 3pm 041xaf
    pov "I think I'll ignore your reluctance this time, because you came back to your senses."
    pov "But if this keeps happening then we're going to have to keep going until scream even more next time."
    povi "Then again, maybe she'll start screaming on her own next time."
    mom "Thank you for cumming all over me... [pov]..."
    pov "Very good. Now I just need to hear one last thing from my slut."
    mom "Thank you for fucking me so good and hard until I came all over your big dick."
    scene showerdownstairs 3pm 042xaf
    pov "You're welcome, and next time just be a good slut and do what I say."
    pov "Trust me and we'll both have plenty of fun."
    mom "Y...yes [pov]."
    pov "Now you can finish your shower if you want."
    jump showerd15fuckslutend

label showerd15fuckslutend:
    scene black
    "You leave the shower."
    $ momcorruption += 1
    $ dtime += 1
    $ showerd15corass = False
    jump showerdown

#----- Nicole Downstairs Shower Third Love Event ----- DONE
label showerd15fucklove:
    $ shower15lovethird = True
    scene showerdownstairs 3pm 029xb
    pov "Huh?"
    "She removed her hands."
    pov "Why did you stop? Did I do something wrong?"
    mom "Haha, no. Turn around [pov]."
    "You turn around."
    scene showerdownstairs 3pm 031xb
    mom "You did everything right. And I'm glad that you've gotten this hard for me."
    pov "Okay, so now what?"
    mom "I was thinking..."
    scene showerdownstairs 3pm 030xb
    "She moves her hand over your chest the way down."
    mom "...since we've come out to the gang and everyone that needs know about our relationship does..."
    pov "Yes?"
    povi "I have already an idea what she wants. But I want to hear her say it."
    scene showerdownstairs 3pm 032xb
    mom "...we could do something... more this time."
    "She's pressing your dick against her pussy."
    pov "Are you saying you want us to have sex, here in the shower?"
    mom "Yes, please take me [pov]! Make love to me!"
    scene showerdownstairs 3pm 033xb
    "You hold her up as you slide your dick inside her pussy."
    mom "Ahh... yes..."
    if inc == True:
        pov "You're so naughty, mom."
        scene showerdownstairs 3pm 034xb
        mom "Look who's talking, fucking your own mother in the shower! <giggle>"
        pov "Hey hey! Language! You kiss your son with that mouth?"
    else:
        pov "You're so naughty, [mother]."
        scene showerdownstairs 3pm 034xb
        mom "Look who's talking, fucking your mother's best friend in the shower! <giggle>"
        pov "Hey hey! Language! You kiss your daughters with that mouth?"
    pov "I though you said you wanted to \"make love\" and now you say we're fucking?"
    mom "Haha! You better believe it. I'm sure we'll have plenty of time for both ways later."
    povi "I can't believe how happy she is."
    pov "I want to do something. I hope you don't mind..."
    mom "Do it... Whatever you want to do, is what I want to do."
    scene showerdownstairs 3pm 035xb
    pov "<suck>"
    "You suck on her nipple."
    mom "Ohh... hah... [pov]!"
    mom "You're not going to get any milk you know. I'm not pregnant... yet..."
    if inc == True:
        pov "Well maybe that's something we should work on... mom."
    else:
        pov "Well maybe that's something we should work on... [mother]."
    mom "Ohh... hah... that's so wrong, but so hot..."
    scene showerdownstairs 3pm 036xb
    mom "I'm so happy that I can get to share this time with you. Let's make lots of great memories together."
    pov "What are you talking about...? You acting like you're gonna die soon..."
    mom "That's not what, hah... I mean. But eventually you're going to want to leave me for a younger girl. Hnng... Someone you'll spend your life with..."
    mom "So I want to enjoy every single moment as much as possible."
    pov "Haha, you're crazy! I waited all my life for this, there's no way I'm leaving you!"
    pov "Maybe you're confused because you're so horny? Let's test something."
    mom "What do you... hah... mean?"
    "You fuck her faster."
    pov "Maybe an orgasm will clear your head, haha."
    mom "Oh... [pov]... so good..."
    scene showerdownstairs 3pm 038xb
    mom "Ahhh... ohhh... I'm so close..."
    if inc == True:
        pov "Cum for me, mom!"
        pov "You're just going to have to accept that your son is here to stay!"
    else:
        pov "Cum for me, [mother]!"
        pov "You're just going to have to accept that I'm here to stay!"
    mom "Oh, [pov]! AHHH...HAAHHH, I'm cumming!"
    with vpunch
    "She's shaking wildly and cum on your dick."
    scene showerdownstairs 3pm 037xb
    mom "Hah... hah... that was amazing!"
    pov "Yes, <suck> it was. But I hope those crazy thoughts of me abandoning you are going away now."
    mom "Not completely, but you proved your point, hah..."
    pov "Then how about this?!"
    scene showerdownstairs 3pm 040xb
    "You pick her up and start fucking her again."
    mom "Ahh, wait... you're so deep... I'm sensitive from coming earlier."
    pov "Good, then you can cum again!"
    mom "Oh, what are you doing with me [pov]. You fucking me like I'm a young girl."
    pov "You seem to be keeping up just fine!"
    mom "Oh god, I'm close again... hah... hah..."
    pov "Then cum for me again, I want you to!"
    mom "Yes, YES! I love you [pov]! I lOVE YOU SO MUCH! I'M CUMMING AGAIN! AHHH..."
    with vpunch
    pov "I'm so close too. I'll cum at any moment."
    mom "Then, hah... do it... Cum where ever you want... just cum for me!"
    povi "She's letting me choose where I want cum. Fantastic!"
    call screen shower15dfucklovecumchoose

screen shower15dfucklovecumchoose():
    default tt = Tooltip (" ")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('shower15dfucklovecumchoose'), Jump('shower15dfucklovecuminside')) hovered tt.Action ("I want to cum inside you") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('shower15dfucklovecumchoose'), Jump('shower15dfucklovecumoutside')) hovered tt.Action ("I want to cum on you") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('shower15dfucklovecumchoose'), Jump('shower15dfucklovecumtits')) hovered tt.Action ("I want to cum on your tits") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide ('shower15dfucklovecumchoose'), Jump('shower15dfucklovecummouth')) hovered tt.Action ("I want to cum in your mouth") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label shower15dfucklovecuminside:
    if inc == True:
        pov "I want to cum inside you, mom!"
    else:
        pov "I want to cum inside you, [mother]!"
    mom "Yes, cum inside me. Fill me up with your hot cum!"
    scene showerdownstairs 3pm 041xbi
    pov "HNNG..."
    with vpunch
    "You blast hot cum into her pussy."
    mom "Ahhh... so hot."
    with vpunch
    "Her entire body is shaking while she orgasms."
    pov "Oh man, I needed that."
    mom "You came so much, I can feel it deep inside me."
    if inc == True:
        pov "I love you, mom."
        mom "I love you too, my son."
    else:
        pov "I love you, [mother]."
        mom "I love you too, [pov]."
    "You let her down gently."
    scene showerdownstairs 3pm 042xbi
    mom "I just can't get over how much you came. It's dripping all over my legs. <giggle>"
    pov "What can I say? You're amazing and it drives me wild!"
    mom "Same here my love."
    jump showerd15fuckloveend

label shower15dfucklovecumoutside:
    pov "I'll cum on your stomach."
    mom "Yes, cover me!"
    scene showerdownstairs 3pm 041xbo
    pov "HNNG..."
    with vpunch
    "You spray your sperm on her belly."
    mom "Ahhh... so hot."
    with vpunch
    "Her entire body is shaking while she orgasms."
    pov "Oh man, I needed that."
    mom "There's so much sperm on my belly now."
    pov "What can I say? You're amazing and it drives me wild!"
    mom "Same here."
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
    mom "Then do it my love!"
    scene showerdownstairs 3pm 042xbmt
    mom "Show me how much you have for me."
    pov "You're so hot doing all these kinky things with me."
    mom "All for you my love."
    pov "Oh, I'm cumming, HNNG..."
    scene showerdownstairs 3pm 042xbt
    "You spray your sperm all over her tits."
    with vpunch
    mom "I can feel it, there's so much and it's so warm."
    pov "That hot view is helping very much!"
    scene showerdownstairs 3pm 043xbt
    mom "I still can't believe how much cum is covering my breasts right now. <giggle>"
    pov "What can I say? You're amazing and it drives me wild!"
    mom "Same here."
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
    mom "Do it!"
    scene showerdownstairs 3pm 042xbmt
    mom "Show me how much you have for me."
    pov "You're so hot doing all these kinky things with me."
    mom "All for you my love."
    pov "Oh, I'm cumming, HNNG..."
    scene showerdownstairs 3pm 043xbm
    mom "Ahh..."
    pov "So hot..."
    "You spray hot cum into her mouth."
    scene showerdownstairs 3pm 044xbm
    with vpunch
    mom "Ahh..."
    pov "I love it when you show it to me before swallowing it!"
    mom "<giggle>"
    scene showerdownstairs 3pm 045xbm
    mom "<gulp> Did I do good?"
    pov "Haha, you know you did!."
    mom "Yeah, but I'm very happy that I made you so happy too."
    pov "What can I say? You're amazing and it drives me wild!"
    mom "Same here."
    if inc == True:
        pov "I love you, mom."
        mom "I love you too, my son."
    else:
        pov "I love you, [mother]."
        mom "I love you too, [pov]."
    jump showerd15fuckloveend

label showerd15fuckloveend:
    mom "Sadly, I should probably clean myself again."
    pov "Yeah, I know. The others will be home soon. I guess I better let you finish up."
    mom "But [pov]!"
    pov "Hmm...?"
    mom "Promise me that we'll do this again."
    pov "Have sex in the shower?"
    mom "Have sex anywhere, <giggle>"
    pov "Haha, of course!"
    scene black
    "You leave the shower."
    $ momlove += 1
    $ dtime += 1
    jump showerdown
