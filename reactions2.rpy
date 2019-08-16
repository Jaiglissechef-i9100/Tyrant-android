#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

label casreacdatecor:
    hide screen locations
    scene kitchen 9am 004a
    povi "She's drinking that shake again."
    povi "I wonder what she'll have to say about what happened."
    scene kitchen 9am 005r
    bs "Oh hey [pov]."
    pov "Hello [bs]! You know why I'm here?"
    bs "Th... the mall..."
    pov "Yes... we need to talk!"
    if d5rccor == True and d5rccorfuck == False and d5rcbjsw == False and d5rcbjout == False and d5rcbjdt == False:
        scene kitchen 9am 006rc
        bs "How dare you...?"
        pov "What...?"
        bs "You tricked me and used me while we were in public."
        pov "What? Now I'm the bad one? You liked it too!"
        bs "I was playing along while the crowd was on your side. And then you tried to rape me!"
        pov "Wait, are you serious? We played around and you loved the attention."
        povi "Damn, it did go further than I though it would but now she's blaming me?"
        scene kitchen 9am 007rc
        bs "I don't want to talk with you about it ever again!"
        pov "But..."
        bs "Cut it out! You just used me and I don't want to hear your excuses."
        povi "Damn, I was sure I could get her to do more."
        scene black
        "[bs] leaves the room."
        jump casreacend
    scene kitchen 9am 008rc
    bs "It was a mistake!"
    pov "What...?"
    bs "I was overwhelmed by the situation and gave in, but it's not what I really wanted."
    povi "Is she serious?"
    if d5rccorfuck == True:
        povi "She let me fuck her and now she pretends that she got overwhelmed by the situation?"
    elif d5rcbjsw == True or d5rcbjout == True or d5rcbjdt == True:
        povi "She gave me a blowjob and now she pretends that she got overwhelmed by the situation?"
    elif d5rclovefuck == True:
        povi "She asked me to fuck her and now she pretends that she got overwhelmed by the situation?"
    pov "Don't give me that crap. I know exactly what \"WE\" did together!"
    bs "You don't understand..."
    scene kitchen 9am 009rc
    pov "Oh I understand it very well."
    pov "Maybe it wasn't planned but you liked it a bit too much and now you don't want to admit it."
    bs "Hnn..."
    pov "And you liked the fame and attention you got there, standing in the spotlight!"
    if d5rcbjsw == True or d5rcbjout == True or d5rcbjdt == True:
        pov "And you even rewarded me with a blowjob after all!"
    bs "You're wrong! I just drifted away! I know now that it was a mistake."
    scene kitchen 9am 010rc
    pov "Stop lying to yourself [bs]!"
    if inc == True:
        if d5rccorfuck == True:
            pov "You even let me fuck you and you came so hard!"
            pov "You had sex with your evil little brother and liked it. Saying the \"situation\" made you do it was just too perfect of an excuse to pass up for you."
        else:
            pov "You gave me a blowjob when we were all alone!"
            pov "You rewarded your evil little brother and liked it. Saying the \"situation\" made you do it was just too perfect of an excuse to pass up for you."
    else:
        if d5rccorfuck == True:
            pov "You even let me fuck you and you came so hard!"
            pov "You had sex with the evil friend and liked it. Saying the \"situation\" made you do it was just too perfect of an excuse to pass up for you."
        else:
            pov "You gave me a blowjob when we were all alone!"
            pov "You rewarded me, the evil friend and liked it. Saying the \"situation\" made you do it was just too perfect of an excuse to pass up for you."
    pov "You also betrayed your boyfriend without a second thought."
    bs "Please stop..."
    pov "No, I won't! We both know the truth, you just won't admit it."
    if inc == True:
        pov "You got very excited by the fact that your little brother took the lead and dominated you!"
    else:
        pov "You got very excited by the fact that I took the lead and dominated you!"
    scene kitchen 9am 011rc
    pov "You welcomed it after the other guys, like the ones in the gang, ignored you. And your loser boyfriend can't handle your desires!"
    bs "No, you're..."
    pov "Shut up! You already lost, I won! I'll take care of you now!"
    scene kitchen 9am 012rc
    if d5rccorfuck == True and cdate5finside == True:
        pov "I'll continue to put my sperm in you until you admit it and become my girl!"
    elif d5rccorfuck == True and cdate5finside == False:
        pov "Next time I'll put my sperm inside you and continue until you admit it and become my girl!"
    elif d5rccorfuck == False:
        pov "Next time I'll fuck you and put my sperm inside you until you admit it and become my girl!"
    bs "Hnn..."
    if inc == True:
        pov "I bet you're excited already by the idea of your little brother taking you after all this years!"
    else:
        pov "I bet you're excited already by the idea of your childhood friend taking you after all this years!"
    scene kitchen 9am 013rc
    bs "Hah..."
    pov "I knew it! Just don't fight it anymore and give in!"
    bs "Hnn..."
    pov "And if you're a good girl you'll get rewarded and you know that I can do it much better then your looser boyfriend."
    bs "Hah..."
    pov "Is that the moaning of agreement, haha?"
    scene kitchen 9am 014rc
    bs "I... it's wrong, but also... I... must go..."
    pov "I don't need to push you, soon you'll be ready..."
    bs "I'm so confused..."
    povi "Soon... I just need to prepare her a little more."
    scene black
    "[bs] leaves the room."
    $ d5corruption = True
    $ casreaccor = True
    jump casreacend

label casreacdatelove:
    hide screen locations
    scene kitchen 9am 004a
    povi "She's drinking that shake again."
    povi "I wonder what she'll have to say about what happened."
    scene kitchen 9am 005r
    bs "Oh hey [pov]."
    pov "Hello [bs]! You know why I'm here?"
    bs "Th... the mall..."
    pov "Yes... we need to talk!"
    scene kitchen 9am 006rl
    bs "I did something wrong. I'm so sorry."
    povi "Oh, I didn't think she's be so worried abou it."
    pov "You don't need to apologize, I was involved there too you know."
    bs "The whole situation overwhelmed me and it went too far."
    bs "I gave you the wrong impression when we did that. It was just wrong."
    if inc == True:
        bs "I still can't believe what we did, we're siblings."
    pov "But..."
    bs "I know you're probably angry with me now, but we need to forget it, please!"
    pov "But it felt like you have feelings for me too. Maybe we just need to go a little more slowly. Explore these feeling?"
    bs "No, I beg you. Don't make it even weirder."
    if d5rclove == True or d5rclovem == True:
        if d5rclovem == True:
            bs "Even Martin saw us and I had a hard time to explain it to him."
        scene kitchen 9am 010rl
        bs "Don't make me beg anymore. Please, let's just forget it."
        pov "..."
        povi "Damn and I thought she had feelings for me. Maybe I was wrong."
        if d5rclovem == False:
            bs "And please don't talk with Martin about it."
        pov "..."
        scene black
        "[bs] leaves the room."
        jump casreacend
    else:
        pov "Oh, I won't give up that easily!"
        scene kitchen 9am 008rl
        bs "Huh?"
        pov "The way you touched me there and let me touch you, I know there's more."
        pov "We had something special there, even though we were in the middle of a crowd of people, it was only the two of us."
        bs "Hnn..."
        pov "Even your boyfriend couldn't interrupt us, you decided that yourself."
        bs "..."
        scene kitchen 9am 009rl
        if inc == True:
            pov "I love you big sis. And I don't care that we're siblings. You're the one I choose."
        else:
            pov "I love you [bs]. And I don't care that your mom would go crazy. You're the one I choose."
        bs "But..."
        pov "Ssshh... Forget about the others. It's just you and me!"
        pov "Forget about the past even, this is a chance to start over. Just the two of us exploring our love."
        bs "Hmm..."
        pov "But I won't push or force you into something you don't want. You'll choose the pace, I can wait!"
        if d5rclovefuck == True:
            pov "I know you felt it, when I was inside you. It was just you and me in there. Two lovers."
        bs "Hnnng..."
        pov "I can feel you shaking. I hope I didn't frighten you. Please don't be scared of me."
        bs "I... am not frightened. I... just... I didn't think you could be such a..."
        if inc == True:
            pov "A good brother who's totally in love with his big sis?"
        else:
            pov "A good friend who's totally in love with you?"
        scene kitchen 9am 010rl
        bs "I.. I need some... time..."
        pov "As I said before, no need to rush things. Take all the time you need. I think you'll find those feelings are there for me too."
        bs "I... I'm so confused..."
        pov "It's ok."
        scene black
        "[bs] leaves the room."
        $ d5love = True
        $ casreaclove = True
        jump casreacend

label casreacdatentr:
    hide screen locations
    scene kitchen 9am 004a
    povi "She's drinking that shake again."
    povi "I wonder what she'll have to say about what happened."
    scene kitchen 9am 005r
    bs "Oh hey [pov]."
    pov "Hello [bs]! You know why I'm here?"
    scene kitchen 9am 006rn
    bs "You want to apologize that you were such a loser at the mall?"
    pov "What? At first you did't want me there and now I'm the loser?"
    bs "If you were a real man you would have interfered and took his place at the shoot."
    pov "What...?"
    scene kitchen 9am 007rn
    bs "But instead he took the initiative and took me for his own pleasure."
    bs "Like a real man, not like you or my loser boyfriend Martin."
    povi "Wow, what's gotten into her?"
    bs "So he got to fuck me in front of all those people, regardless of consequences!"
    bs "It felt so good to submit to the will of a such a strong man!"
    povi "She likes to get dominated?"
    scene kitchen 9am 008rn
    bs "Something that a loser like you could never do!"
    if cassandra_revenge == True:
        povi "She has the look in her eyes again. I think she's trying to find someone to blame. Sadly that's me."
    call screen casreacdatentrch

screen casreacdatentrch():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('casreacdatentrch'), Jump('casreacdatentrapp')) hovered tt.Action ("I don't care") focus_mask True
        if cassandra_ntr == True:
            imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('casreacdatentrch'), Jump('casreacdatentrdisapp')) hovered tt.Action ("Let her be angry with you") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('casreacdatentrch'), Jump('casreacdatentrdisapp')) hovered tt.Action ("You're a slut") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label casreacdatentrapp:
    pov "I don't care about what happened there."
    pov "That's great if you had fun getting fucked like that."
    bs "Yes I did. And to watch a loser like you just standing there."
    povi "She can't stop. She wants me to suffer but I just don't care."
    povi "But maybe she's disappointed that I didn't take his place?"
    pov "Yeah, yeah. Whatever."
    bs "Get some balls, pussy!"
    scene black
    "You leave the kitchen, not giving her much satisfaction."
    $ casreacntr = True
    jump casreacend

label casreacdatentrdisapp:
    if cassandra_revenge == True:
        povi "I don't want her to hate me, but she needs something to hate right now. She was raped. I can do that at least for. I can be a target for her anger."
    pov "You're just a slut, letting yourself get fucked by some stranger in the hopes of feeling special in front of a bunch of sheep."
    scene kitchen 9am 009rn
    bs "Fuck you! You're just disappointed that you missed your chance."
    pov "Says the slut..."
    bs "You loser! You're not a real man and you'll never be."
    if cassandra_revenge == True:
        povi "I don't know how far to push this..."
    pov "Maybe I should tell Martin what you did?"
    bs "Haha, do it. He would never believe you!"
    pov "Oh, but there are many witnesses."
    bs "I don't care. He won't leave me, he's mine and he knows that!"
    povi "Is she maybe disappointed that I didn't take his place?"
    pov "I won't forget that."
    bs "Oh I'm sure you won't."
    scene black
    if cassandra_revenge == True:
        "You leave the kitchen, succeeding in making her hate you more."
    else:
        "You leave the kitchen, not giving her much satisfaction."
    $ casreacntr = True
    jump casreacend

label casreacend:
    $ d5rccor = False
    $ d5rccorfuck = False
    $ d5rcbjsw = False
    $ d5rcbjout = False
    $ d5rcbjdt = False
    $ d5rclove = False
    $ d5rclovefuck = False
    $ d5rclovef = False
    $ d5rclovem = False
    $ d5rcntr = False
    $ dtime = 10
    jump kitchen
