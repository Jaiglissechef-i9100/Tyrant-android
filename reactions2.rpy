
label casreacdatecor:
    hide screen locations
    scene kitchen 9am 004a
    pov "{i}She's drinking her stuff again.{/i}"
    pov "{i}I wonder what she'll have to say about what happened.{/i}"
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
        bs "I played along while the crowd was on your side. And then you tried to rape me!"
        pov "Wait, are you serious? We played around and you loved the attention."
        pov "{i}Damn, it went really wrong but now she's so aggressive?{/i}"
        scene kitchen 9am 007rc
        bs "I don't want to talk with you about it ever again!"
        pov "But..."
        bs "Cut it out! You tried bad moves on me and I don't want to hear your excuses."
        pov "{i}Damn, I was sure I could get her to do more.{/i}"
        scene black
        "[bs] leaves the room."
        jump casreacend
    scene kitchen 9am 008rc
    bs "It was a mistake!"
    pov "What...?"
    bs "I was overwhelmed by the situation and gave in, but it's nothing I really wanted."
    pov "{i}Is she serious?{/i}"
    if d5rccorfuck == True:
        pov "{i}She let me fuck her and now she pretends that she got overwhelmed by the situation?{/i}"
    elif d5rcbjsw == True or d5rcbjout == True or d5rcbjdt == True:
        pov "{i}She gave me a blowjob and now she pretends that she got overwhelmed by the situation?{/i}"
    pov "Don't talk bullshit I know exactly what \"WE\" did together!"
    bs "You don't understand..."
    scene kitchen 9am 009rc
    pov "Oh I understand very well."
    pov "Maybe it wasn't planned but you liked it a bit too much and now you don't want to admit it."
    bs "Hnn..."
    pov "And the fame and attention you got there, standing in the spotlight!"
    if d5rcbjsw == True or d5rcbjout == True or d5rcbjdt == True:
        pov "And you even rewarded me with a blowjob after all!"
    bs "You're wrong! I just drifted away! I know now that it was a mistake."
    scene kitchen 9am 010rc
    pov "Haha, stop betraying yourself [bs]!"
    if inc == True:
        if d5rccorfuck == True:
            pov "You even let me fuck you and you came hard!"
            pov "You had sex with your evil little brother and the excuse of the situation was just perfect for you."
        else:
            pov "You gave me a blowjob when we're all alone!"
            pov "You rewarded your evil little brother and the excuse of the situation was just perfect for you."
    else:
        if d5rccorfuck == True:
            pov "You even let me fuck you and you came hard!"
            pov "You had sex with me, the evil friend and the excuse of the situation was just perfect for you."
        else:
            pov "You gave me a blowjob when we're all alone!"
            pov "You rewarded me, the evil friend and the excuse of the situation was just perfect for you."
    pov "You also betrayed your boyfriend without a second withstanding."
    bs "Please stop..."
    pov "No, I won't! We both know the truth, you just won't admit it."
    if inc == True:
        pov "You got very excited by the fact that your little brother took the lead and dominated you!"
    else:
        pov "You got very excited by the fact that I took the lead and dominated you!"
    scene kitchen 9am 011rc
    pov "You welcomed it after the other cool guys, like the one in the gang ignore you. And your loser boyfriend can't withstand against you!"
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
        pov "I bet you're excited already by the idea that your little brother take you after all this years!"
    else:
        pov "I bet you're excited already by the idea that your childhood friend take you after all this years!"
    scene kitchen 9am 013rc
    bs "Hah..."
    pov "I knew it! Just don't fight it anymore and give yourself in!"
    bs "Hnn..."
    pov "And if you're a good girl you'll get rewarded and you know that I can do it much better then your looser boyfriend."
    bs "Hah..."
    pov "Is that the moaning of agreement, haha?"
    scene kitchen 9am 014rc
    bs "I... it's wrong, but also... I... must go..."
    pov "I don't need to push you, soon you'll be ready..."
    bs "I'm so confused..."
    pov "{i}Soon... I just need to prepare her a little more.{/i}"
    scene black
    "[bs] leaves the room."
    $ d5corruption = True
    $ casreaccor = True
    jump casreacend

label casreacdatelove:
    hide screen locations
    scene kitchen 9am 004a
    pov "{i}She's drinking her stuff again.{/i}"
    pov "{i}I wonder what she'll have to say about what happened.{/i}"
    scene kitchen 9am 005r
    bs "Oh hey [pov]."
    pov "Hello [bs]! You know why I'm here?"
    bs "Th... the mall..."
    pov "Yes... we need to talk!"
    scene kitchen 9am 006rl
    bs "I did something wrong. I'm so sorry."
    pov "{i}Oh she's still affected from it.{/i}"
    pov "You don't need to excuse yourself, I was involved there too."
    bs "The whole situation overwhelmed me and it went too far."
    bs "I gave you the wrong impression when we did that. It was just wrong."
    if inc == True:
        bs "I still can't believe what we did as siblings."
    pov "But..."
    bs "I know you're maybe angry but we need to forget it, please!"
    pov "But it felt like you have feelings for me, maybe we just need to get it on more slowly."
    bs "No, I beg you. Don't make it even weirder."
    if d5rclove == True or d5rclovem == True:
        if d5rclovem == True:
            bs "Even Martin saw us and I had big problems to explain it to him."
        scene kitchen 9am 010rl
        bs "Don't make me beg anymore. Please let us just forget it."
        pov "..."
        pov "{i}Damn and I thought she had feelings for me. Maybe I should wake her feelings more.{/i}"
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
        pov "We built our special place there, in the middle of a crowd of people, but still only the two of us."
        bs "Hnn..."
        pov "Even your boyfriend couldn't interrupt us, you decided that there."
        bs "..."
        scene kitchen 9am 009rl
        if inc == True:
            pov "I love you big sis. And I don't care that we're siblings. You're the one I choose."
        else:
            pov "I love you [bs]. And I don't care that your mom would go crazy. You're the one I choose."
        bs "But..."
        pov "Ssshh... Forget about the others. It's just you and me!"
        pov "Forget even about the past, this is like a restart, just the two of us exploring our love."
        bs "Hmm..."
        pov "But I won't push or force you into something. You'll choose your pace, I can wait!"
        pov "I can feel you shaking and I hope I didn't frighten you. Never be scared of me!"
        bs "I... am not frightened. I... just... I didn't think you could be so..."
        if inc == True:
            pov "A nice brother who's totally in love with his big sis?"
        else:
            pov "A nice friend who's totally in love with you?"
        scene kitchen 9am 010rl
        bs "I.. I need some... time..."
        pov "As I said before, no need to rush things. I know you feel something for me and that you'll just need some time to admit it to yourself."
        bs "I... I'm so confused..."
        pov "That's what love does."
        scene black
        "[bs] leaves the room."
        $ d5love = True
        $ casreaclove = True
        jump casreacend

label casreacdatentr:
    hide screen locations
    scene kitchen 9am 004a
    pov "{i}She's drinking her stuff again.{/i}"
    pov "{i}I wonder what she'll have to say about what happened.{/i}"
    scene kitchen 9am 005r
    bs "Oh hey [pov]."
    pov "Hello [bs]! You know why I'm here?"
    scene kitchen 9am 006rn
    bs "You want to apologize that you're such a looser at the mall?"
    pov "What? You don't want me there and now I'm the looser?"
    bs "If you're a real man you'd interfere and take his place at the shoot."
    pov "What...?"
    scene kitchen 9am 007rn
    bs "But he took the initiative and took me for his pleasure."
    bs "Like a real man, not like you or my looser boyfriend Martin."
    pov "{i}Wow, what's gotten into her?{/i}"
    bs "And then he fucked me in front of all those people, regardless of consequences!"
    bs "To this real man I had no other choice then to submit!"
    pov "{i}She likes it to get dominated?{/i}"
    scene kitchen 9am 008rn
    bs "Something that a looser like you could never do!"
    call screen casreacdatentrch

screen casreacdatentrch():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 1289 ypos 273 action (Hide('casreacdatentrch'), Jump('casreacdatentrapp')) hovered tt.Action ("I don't care") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 816 ypos 273 action (Hide('casreacdatentrch'), Jump('casreacdatentrdisapp')) hovered tt.Action ("You're a slut") focus_mask True
        frame:
            xalign .5
            text tt.value

label casreacdatentrapp:
    pov "I don't care about what happened there. If you had your fun getting fucked like that."
    bs "Yes I did. And to see a looser like you just standing there."
    pov "{i}She can't stop. She wants me to suffer but I just don't care.{/i}"
    pov "{i}But maybe she's disappointed that I didn't take his place?{/i}"
    pov "Yeah, yeah. Whatever."
    bs "Get some balls, pussy!"
    scene black
    "You leave the kitchen, not giving her much satisfaction."
    $ casreacntr = True
    jump casreacend

label casreacdatentrdisapp:
    pov "You're just a slut, letting yourself get fucked by some stranger to feel special in front of the people."
    scene kitchen 9am 009rn
    bs "Fuck you! You're just disappointed that you missed your chance."
    pov "Says the slut..."
    bs "You looser! You're not a real man and you'll never be."
    pov "Maybe I should tell Martin what you did?"
    bs "Haha, just go on. He would never believe you!"
    pov "Oh there are many witnesses."
    bs "I don't care. He won't leave me, he's mine and he knows that!"
    pov "{i}Is she maybe disappointed that I didn't take his place?{/i}"
    pov "I won't forget that."
    bs "Oh I'm sure you won't."
    scene black
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
    $ d5rclovef = False
    $ d5rclovem = False
    $ d5rcntr = False
    $ dtime = 10
    jump kitchen