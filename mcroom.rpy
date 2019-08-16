


label hardntron:
    hide screen locations
    $ hardntr = True
    $ momntr = True
    $ lilsisntr = True
    $ bigsisntr = True
    $ irinantr = True
    $ katentr = True
    $ vivianntr = True
    $ susanntr = True
    "The hard mode is now on!"
    jump mcroom

label hardntroff:
    hide screen locations
    $ hardntr = False
    "The hard mode is now off!"
    jump mcroom


label alexismcroomsurprise:
    scene black
    $ lilsisrelationship += 1
    "You feel something in your sleep."
    pov "{i}There's something on me? What's happening?{/i}"
    "You wake up and open your eyes."
    scene mcroom 6am 001
    pov "Huh?"
    ls "<giggle>"
    if inc == True:
        pov "Lil sis?"
        ls "Hi brother."
    else:
        pov "[ls]?"
        ls "Hi [pov]."
    if mcroom6amfirst == True:
        pov "You need to kiss me again?"
    else:
        pov "What are you doing here?"
        ls "I woke up and missed you so I came to see you."
        pov "So you're here now."
    ls "Yes. <giggle>"
    if mcroom6amfirst == True:
        pov "You watched me sleeping again?"
        pov "And kissed me?"
    else:
        pov "Wait, you're still here some time longer?"
        pov "You watched me sleeping?"
        ls "Yes and I felt the urge to kiss you. <giggle>"
        pov "You kissed me while I was asleep?"
    ls "Yes like that!"
    scene mcroom 6am 003
    ls "<kiss>"
    pov "{i}Nice. What a good start to the day.{/i}"
    ls "Hmm..."
    pov "{i}Oh and she even let her eyes open while kissing.{/i}"
    scene mcroom 6am 006
    ls "You liked my kiss?"
    pov "Of course! I like every kiss I get from you."
    ls "That's good, because I want to give you many more."
    pov "{i}Wait? Is this real? Or I am still dreaming?{/i}"
    scene mcroom 6am 004
    if inc == True:
        ls "Is something wrong brother?"
    else:
        ls "Is something wrong [pov]?"
    pov "No nothing, I was just thinking. And I remembered something."
    if mcroom6amfirst == True:
        pov "{i}And my morning wood is back again.{/i}"
        pov "Ehm. You feel me poking you again?"
    else:
        pov "{i}It's morning, so I have morning wood. And she's sitting right on it. But why didn't she mention it?{/i}"
        pov "Ehm. You didn't say something. Didn't you feel something while you are sitting on me?"
    scene mcroom 6am 001
    if mcroom6amfirst == True:
        ls "Your penis is poking me again. <giggle>"
        pov "{i}What the hell?{/i}"
        ls "I'll get used to that feeling while sitting on you <giggle>."
    else:
        ls "You talk about your hard penis?"
        pov "{i}What the hell?{/i}"
        ls "Yes I noticed it poking at my crotch, but you're still sleeping so you couldn't do much about it."
        ls "I tried not to break it <giggle>."
    scene mcroom 6am 005
    pov "And it didn't bother you?"
    ls "Haha, should I be scared of it?"
    if mcroom6amfirst == True:
        pov "{i}Wow, she's so active again. She seems to enjoy it more and more.{/i}"
    else:
        pov "{i}Wow, she's so active this morning and not shy. What a nice surprise.{/i}"
    pov "{i}But now I'm so damn horny and her kissing makes it worse.{/i}"
    ls "Time for another kiss!"
    scene mcroom 6am 003
    ls "<kiss>"
    pov "{i}Damn this is so hot. I want more but it could scare her.{/i}"
    call screen mcroom6amchoose

screen mcroom6amchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_love_%s.png" xpos 290 ypos 370 action (Hide ('mcroom6amchoose'), Jump('mcroom6amkisslove')) hovered tt.Action ("Just let her kiss you [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" xpos 1650 ypos 370 action (Hide ('mcroom6amchoose'), Jump('mcroom6amkisscor')) hovered tt.Action ("French kiss her [cr1]") focus_mask True


    frame:
        xalign .5
        text tt.value


label mcroom6amkisslove:
    $ lilsislove += 1
    pov "{i}When she wants to kiss me I won't try something and just enjoy her kiss.{/i}"
    ls "<kiss>"
    ls "Hmm..."
    scene mcroom 6am 002
    ls "This is so much fun."
    pov "Then I'm happy you chose this activity."
    ls "<giggle>"
    ls "You earned another one."
    scene mcroom 6am 003
    ls "<kiss>"
    pov "{i}This gets even better.{/i}"
    scene mcroom 6am 002
    ls "I don't want to stop."
    ls "<giggle>"
    pov "Then don't."
    if inc == True:
        ls "I like you so much big brother!"
    else:
        ls "I like you so much [pov]!"
    pov "I like you too."
    scene mcroom 6am 011
    ls "I need to go now."
    pov "Ohh..."
    ls "But stay aware. You can get kissed more often when you sleep."
    ls "<kiss> <giggle>"
    $ mcroom6amfirst = True
    if d9rnntri == True or d9rnntr == True or d9rncor == True or d9rncorf == True or d9rnlove == True or d9rnlovef == True or b9rnntr == True or b9rnntrmir == True or b9rnlove == True or b9rncor == True:
        $ dtime = 62
        jump nicolereac
    else:
        $ dtime = 7
        jump mcroom



label mcroom6amkisscor:
    $ lilsiscorruption += 1
    "You want more and it's time for a french kiss."
    scene mcroom 6am 007
    ls "Hnn...?"
    "She tries to break the kiss."
    pov "{i}No way. I want more.{/i}"
    scene mcroom 6am 008
    "You hold her tight while you explore her mouth."
    pov "<kiss> <lick>"
    ls "Hnn..."
    "She starts trembling."
    scene mcroom 6am 009
    if mcroom6amfirst == True:
        ls "Hah! You did it again... with your tongue..."
    else:
        ls "Hah! You... your tongue was inside..."
    pov "Yes, your kisses and sitting on my boner made me so horny that I needed more."
    if mcroom6amfirst == True:
        ls "You surprised me again. Sticking your tongue in my mouth."
        pov "Yes you need to get used to french kissing."
    else:
        ls "You... surprised me! Your tongue was in my mouth."
        pov "Yes, I gave you a french kiss. It's just a better kiss."
    pov "And your tongue tastes really good."
    ls "But..."
    pov "Don't be sad. You love kissing and I want to teach you better kissing."
    pov "And you're ready for it. I noticed that."
    scene mcroom 6am 010
    if mcroom6amfirst == True:
        ls "Another french kiss..."
        pov "I'm just trying to conquer your mouth, haha."
    else:
        ls "..."
        ls "A french kiss..."
    pov "{i}She's confused. She seemed to like it, but won't admit it.{/i}"
    ls "I... I need to go."
    scene mcroom 6am 012
    "She leaves in a hurry."
    pov "{i}Haha, it was too much for her, but she'll get used too it.{/i}"
    $ mcroom6amfirst = True
    if d9rnntri == True or d9rnntr == True or d9rncor == True or d9rncorf == True or d9rnlove == True or d9rnlovef == True or b9rnntr == True or b9rnntrmir == True or b9rnlove == True or b9rncor == True:
        $ dtime = 62
        jump nicolereac
    else:
        $ dtime = 7
        jump mcroom


label mcroom17yesmessy:
    hide screen locations
    scene main 5pm mc room b
    ls "Geez! At least it's not so much."
    pov "Oh you came to fulfill your duty?"
    ls "Yes as I promised big brother."
    pov "Good you can start then."
    ls "Geez!"
    scene mcroom 5pm 003b
    ls "Why are they so far under the bed?"
    pov "{i}It's better that you don't know.{/i}"
    ls "Ah I have them."
    scene mcroom 5pm 004b
    ls "And now this one."
    pov "..."
    ls "That should be easy."
    if prongangbang == True:
        scene mcroom 5pm 005gb
        $ lsisprongangbang += 1
        "Girl" "Oh yes fuck me harder! Give me all your dicks!"
    elif pronBDSM == True:
        scene mcroom 5pm 005bdsm
        "Girl" "Please master! I'll be obedient!"
        $ lsispronBDSM += 1
    elif proninc == True:
        scene mcroom 5pm 005inc
        $ lsisproninc += 1
        "Girl" "I love you brother! I know it's forbidden but please fuck me more!"
    elif proninterracial == True:
        scene mcroom 5pm 005int
        $ lsisproninterracial += 1
        "Girl" "Oh my god! You're so big!"
    elif pronlesbian == True:
        scene mcroom 5pm 005les
        $ lsispronlesbian += 1
        "Girl" "You taste so good! I won't stop!"
    elif pronntr == True:
        scene mcroom 5pm 005ntr
        $ lsispronntr += 1
        "Boy" "Oh no Tracy, why you do this with him? I thought you loved me."
    elif pronanal == True:
        scene mcroom 5pm 005anal
        $ lsispronanal += 1
        "Girl" "Oh my god! You're in my asshole!"
    elif pronfemdom == True:
        scene mcroom 5pm 005femdom
        "Girl" "Yes, be a good slave!"
        $ lsispronfemdom += 1
    else:
        jump mcroom17nopron
    ls "Ohh...?"
    ls "..."
    scene mcroom 5pm 006b
    ls "I... I need to go now."
    pov "But wait..."
    if lsispronlesbian >= 4 and irinafirstmeet == True and irinalove >= 20 and lesbiandate1 == False or lsispronlesbian >= 4 and irinafirstmeet == True and irinacorruption >= 20 and lesbiandate1 == False:
        jump mcroomlesbian
    ls "Your room is clean."
    if prongangbang == True:
        scene mcroom 5pm 007gb
    elif pronBDSM == True:
        scene mcroom 5pm 007bdsm
    elif proninc == True:
        scene mcroom 5pm 007inc
    elif proninterracial == True:
        scene mcroom 5pm 007int
    elif pronlesbian == True:
        scene mcroom 5pm 007les
    elif pronntr == True:
        scene mcroom 5pm 007ntr
    elif pronanal == True:
        scene mcroom 5pm 007anal
    elif pronfemdom == True:
        scene mcroom 5pm 007femdom
    pov "{i}Ha, that worked perfectly.{/i}"
    $ lilsisrelationship += 1
    $ mcroom17sawpron += 1
    $ setuppron = False
    $ vdroom13lilsisbetlost = False
    $ prongangbang = False
    $ pronBDSM = False
    $ proninc = False
    $ proninterracial = False
    $ pronlesbian = False
    $ pronntr = False
    $ dtime = 18
    jump mcroom

label mcroom17nopron:
    hide screen locations
    scene mcroom 5pm 005b
    ls "Slowly so the laptop doesn't brake."
    ls "So..."
    scene mcroom 5pm 002a
    ls "I'm done with cleaning your room."
    pov "Yes I see that. Good work [ls]."
    ls "See you later, dummy."
    $ lilsisrelationship += 1
    $ setupnopron = False
    $ vdroom13lilsisbetlost = False
    $ dtime = 18
    jump mcroom

label mcroom17nomessy:
    hide screen locations
    scene main 5pm mc room a
    ls "What is this? Your room is already clean."
    pov "I know. I just wanted to see if you would come to fulfill your duty."
    ls "Of course, I promised."
    ls "So what now?"
    pov "Since you have nothing to clean you could be thankful that you get your homework nearly for free."
    scene mcroom 5pm 002a
    ls "Thankful...?"
    pov "I'm better than you, admit it!"
    ls "..."
    ls "Fine! You're better then me [pov]."
    pov "Hahaha, I knew it the whole time."
    ls "This time..."
    $ lilsisrelationship += 1
    $ dtime = 18
    $ vdroom13lilsisbetlost = False
    jump mcroom


label mcroomwonbetprep:
    hide screen locations
    scene main mc room day
    pov "{i}Hmm... [ls] will come soon to clean my room. But it's already clean.{/i}"
    scene main mc room2 day
    pov "{i}She won't have anything to do in this state.{/i}"
    pov "{i}Maybe I should mess my room a little so she won't have my help for free.{/i}"
    pov "{i}Yes it's a good idea. I'll start with some clothes.{/i}"
    scene main mc room day
    pov "{i}Hm... maybe I could leave my laptop on. Then she will have to see what I want to show her.{/i}"
    pov "{i}And it could be nice to see how she would react to something naughty.{/i}"
    pov "{i}Oh yes. That could be fun.{/i}"
    jump mcwbp

label mcwbp:
    scene mcroom 5pm 007b
    call screen mcwbp1

screen mcwbp1():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 936 ypos 308 action (Hide('mcwbp1'), Jump('mcroomsetupporn')) hovered tt.Action ("Set up some porn") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1632 ypos 218 action (Hide('mcwbp1'), Jump('mcroomnosetupporn')) hovered tt.Action ("Don't do it") focus_mask True
        frame:
            xalign .5
            text tt.value

label mcroomnosetupporn:
    scene main mc room day
    pov "{i}No. I won't do it. I don't won't her to see that dirty stuff.{/i}"
    pov "{i}Putting away the clothes is enough.{/i}"
    $ setupnopron = True
    $ dtime += 1
    jump mcroom

label mcroomsetupporn:
    scene mcroom 5pm 007b
    pov "{i}What should I choose?{/i}"
    if inc == True:
        pov "{i}What should I wake little sisters interest with?{/i}"
    else:
        pov "{i}What should I wake [ls] interest with?{/i}"
    jump mcsup

label mcsup:
    call screen mcsup1

screen mcsup1():
    default tt = Tooltip (" ")
    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 539 ypos 126 action (Hide('mcsup1'), Jump('mcroomsetupgb')) hovered tt.Action ("Gang Bang") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 932 ypos 126 action (Hide('mcsup1'), Jump('mcroomsetupbdsm')) hovered tt.Action ("BDSM") focus_mask True
        if inc == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1382 ypos 126 action (Hide('mcsup1'), Jump('mcroomsetupinc')) hovered tt.Action ("Incest") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 539 ypos 537 action (Hide('mcsup1'), Jump('mcroomsetupint')) hovered tt.Action ("Interracial") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 932 ypos 537 action (Hide('mcsup1'), Jump('mcroomsetuples')) hovered tt.Action ("Lesbian") focus_mask True
        if NTR == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1382 ypos 537 action (Hide('mcsup1'), Jump('mcroomsetupntr')) hovered tt.Action ("NTR") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" xpos 1632 ypos 218 action (Hide('mcsup1'), Jump('mcroomnosetupporn1')) hovered tt.Action ("Not the right things for me") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 537 ypos 308 action (Hide('mcsup1'), Jump('mcroomsetupanal')) hovered tt.Action ("Anal") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 932 ypos 308 action (Hide('mcsup1'), Jump('mcroomsetupfemdom')) hovered tt.Action ("Femdom") focus_mask True
        frame:
            xalign .5
            text tt.value

label mcroomsetupgb:
    scene mcroom 5pm 007gb
    "Girl" "Oh yes fuck me harder! Give me all your dicks!"
    pov "{i}Oh yes that'll do it.{/i}"
    pov "{i}Now I have to wait for her.{/i}"
    $ setuppron = True
    $ prongangbang = True
    $ dtime += 1
    jump mcroom

label mcroomsetupbdsm:
    scene mcroom 5pm 007bdsm
    "Girl" "Please master! I'll be obedient!"
    pov "{i}Oh yes that'll do it.{/i}"
    pov "{i}Now I have to wait for her.{/i}"
    $ setuppron = True
    $ pronBDSM = True
    $ dtime += 1
    jump mcroom

label mcroomsetupinc:
    scene mcroom 5pm 007inc
    "Girl" "I love you brother! I know it's forbidden but please fuck me more!"
    pov "{i}Oh yes that'll do it.{/i}"
    pov "{i}Now I have to wait for her.{/i}"
    $ setuppron = True
    $ proninc = True
    $ dtime += 1
    jump mcroom

label mcroomsetupint:
    scene mcroom 5pm 007int
    "Girl" "Oh my god! You're so big!"
    pov "{i}Oh yes that'll do it.{/i}"
    pov "{i}Now I have to wait for her.{/i}"
    $ setuppron = True
    $ proninterracial = True
    $ dtime += 1
    jump mcroom

label mcroomsetuples:
    scene mcroom 5pm 007les
    "Girl" "You taste so good! I won't ever stop!"
    pov "{i}Oh yes that'll do it.{/i}"
    pov "{i}Now I have to wait for her.{/i}"
    $ setuppron = True
    $ pronlesbian = True
    $ dtime += 1
    jump mcroom

label mcroomsetupntr:
    scene mcroom 5pm 007ntr
    "Boy" "Oh no Tracy, why you do this with him? I thought you loved me."
    pov "{i}Oh yes that'll do it.{/i}"
    pov "{i}Now I have to wait for her.{/i}"
    $ setuppron = True
    $ pronntr = True
    $ dtime += 1
    jump mcroom

label mcroomnosetupporn1:
    scene main mc room day
    pov "{i}There's nothing that I would show her.{/i}"
    pov "{i}Putting away the clothes is enough.{/i}"
    $ setupnopron = True
    $ dtime += 1
    jump mcroom

label mcroomsetupanal:
    hide screen locations
    scene mcroom 5pm 007anal
    "Girl" "Oh my god! You're in my asshole!"
    pov "{i}Oh yes that will do it.{/i}"
    pov "{i}Now I have to wait for her.{/i}"
    $ setuppron = True
    $ pronanal = True
    $ dtime += 1
    jump mcroom

label mcroomsetupfemdom:
    hide screen locations
    scene mcroom 5pm 007femdom
    "Girl" "Yes, be a good slave!"
    pov "{i}Oh yes that will do it.{/i}"
    pov "{i}Now I have to wait for her.{/i}"
    $ setuppron = True
    $ pronfemdom = True
    $ dtime += 1
    jump mcroom


label mcroomlesbian:
    hide screen locations
    scene mcroom 5pm 020
    irina "Hey!"
    ls "Oh..."
    pov "Oh hey [irina]. What a nice surprise."
    irina "I was around with [bs] and I thought I would visit you. What are you doing?"
    pov "Nothing special."
    ls "No, no... nothing..."
    irina "Haha, you're such bad liars. Let me see..."
    scene mcroom 5pm 021
    ls "Nooo..."
    irina "Oh, so you're watching something."
    ls "No it's nothing for your eyes!"
    irina "Oh, come on. I need to know!"
    scene mcroom 5pm 022
    irina "Oh? Hahaha..."
    irina "I know this one!"
    pov "What...?"
    ls "Huh?"
    scene mcroom 5pm 023
    if inc == True:
        irina "You're watching lesbian porn with your little sister?"
    else:
        irina "You're watching lesbian porn with her?"
    pov "Um, I wanted to see if she is interested in something."
    pov "{i}And I would love to see her becoming a lesbian.{/i}"
    scene mcroom 5pm 024
    if inc == True:
        irina "So you like watching lesbian porn with your big brother?"
    else:
        irina "So you like watching lesbian porn with him?"
    ls "Hnng..."
    pov "{i}Haha, she's so confused. She's to embarrassed to tell her that I forced her to do it.{/i}"
    irina "I didn't know that you're into that stuff?"
    scene mcroom 5pm 025
    irina "That is so damn cute."
    if inc == True:
        irina "That you share something intimate with your little sister."
    else:
        irina "That you share something intimate with her."
    irina "She can be so proud."
    ls "Hnn..."
    pov "{i}[irina] speaks so open about that stuff and [ls] getting more and more confused.{/i}"
    irina "But I'm also here because of you, [pov]."
    pov "Oh, I get the hint!"
    if irinacorruption > irinalove:
        scene mcroom 5pm 026b
        pov "Come here, my girl!"
        "You give her a french kiss."
        irina "Hmm... <kiss>"
        ls "Oh..."
    else:
        scene mcroom 5pm 026a
        irina "Come here, [pov]!"
        "She gives you a french kiss."
        irina "Hmm... <kiss>"
        ls "Oh..."
    "You two kiss for a while."
    scene mcroom 5pm 027
    "[ls] is about to leaving your room."
    pov "{i}She seems to be sad?{/i}"
    irina "Where do you think you're going?"
    scene mcroom 5pm 028
    ls "Huh?"
    irina "You're trying to sneak away?"
    ls "I... just don't want to... disturb you..."
    irina "But you aren't... !"
    scene mcroom 5pm 029
    irina "You won't leave us!"
    ls "Huh, but...?"
    pov "{i}What is she up to?{/i}"
    irina "I need to know more!"
    pov "{i}Oh...{/i}"
    scene mcroom 5pm 030
    irina "So... how long have you been into that stuff?"
    ls "Stuff...?"
    irina "I still can't believe that [bs]'s little sister is a lesbian."
    ls "But I..."
    pov "She's new to it."
    irina "Oh then I hope you like it, because you're so damn cute."
    ls "Hnn..."
    pov "{i}What? Really?{/i}"
    irina "So you haven't found a girlfriend yet?"
    ls "N... no..."
    scene mcroom 5pm 031
    ls "Hnn..."
    pov "{i}Is she playing with [ls]?{/i}"
    irina "What a shame. A girl would be so happy to be with you. Touching your smooth skin."
    ls "Hnn..."
    pov "{i}She's really flirting with her!{/i}"
    irina "When I think I could be the happy one, after the things your sister told me."
    ls "Huh?"
    pov "What did she tell you?"
    irina "That [ls] want to hang out with us, because she thinks I'm so cool."
    scene mcroom 5pm 032
    ls "She told you that?"
    irina "Haha, yes. But don't worry, I'm flattered!"
    ls "But it wasn't meant to..."
    irina "Oh but I think so. That could be a way to start."
    ls "To start...?"
    scene mcroom 5pm 033
    ls "Hnn?"
    irina "<kiss>"
    pov "{i}Wow, [irina] is kissing her! Is she maybe bisexual?{/i}"
    ls "Hmm..."
    pov "{i}But [ls] isn't struggling. Maybe [irina] was right and she really likes her.{/i}"
    scene mcroom 5pm 034
    ls "<kiss> Hnn..."
    pov "{i}Wow! [ls] is kissing her back now. So showing her the porn seems to work.{/i}"
    pov "{i}And I have something really nice to watch.{/i}"
    scene mcroom 5pm 035
    ls "Hah..."
    ls "You kissed me..."
    irina "Yes, I couldn't hold back. But it seems you liked it, didn't you?"
    ls "Y... yes. I... liked it..."
    pov "{i}She's so damn confused, but this is also damn hot, haha.{/i}"
    irina "And you're happy that I was the one kissing you?"
    ls "Yes... I got kissed... by a girl..."
    irina "Oh come here, kitty."
    scene mcroom 5pm 036
    ls "Hnn..."
    irina "<kiss> <kiss>"
    irina "That soft skin needs to be plastered with kisses."
    ls "Hnng..."
    pov "{i}Is she trying to thank me? Or is she ashamed that I'm watching?{/i}"
    pov "{i}But I never thought that [irina] could do such a thing?{/i}"
    pov "{i}I hope she's not just playing with her, maybe to prove something.{/i}"
    pov "{i}But maybe she's really bisexual and maybe I get a chance to watch them more.{/i}"
    scene mcroom 5pm 037
    irina "<whisper> ..."
    ls "Oh..."
    pov "{i}What's she whispering? I can't hear it.{/i}"
    irina "<whisper> ..."
    ls "Oh... Oh!"
    pov "{i}Damn, is it something kinky? I want to know!{/i}"
    scene mcroom 5pm 038
    irina "So what do you think?"
    ls "Yes... I want to..."
    pov "{i}Damn it! Tell me too!{/i}"
    irina "Great! I'm really excited."
    scene mcroom 5pm 039
    irina "But you weren't very gentlemanly."
    pov "I... that happened so suddenly."
    irina "Haha, I'm just joking around. Most men like to watch."
    ls "To watch...?"
    irina "Nothing serious..."
    ls "I... need to go now... something urgent came up..."
    pov "{i}She's trembling. Did she get horny?{/i}"
    irina "No problem. I need to go also, I bet your big sister is raging down there."
    scene mcroom 5pm 040
    pov "What did you tell her? I couldn't hear it."
    irina "Ha, should I tell you? Are you so interested in lesbians?"
    pov "When you participate. Of course!"
    irina "I told her where we meet again to continue our fun. And if you're a good boy I'll tell you too."
    pov "What? But..."
    irina "<giggle>"
    scene black
    pov "{i}I'm sure she'll tell me. She has to!{/i}"
    $ dtime += 1
    $ lesbiandate1 = True
    jump mcroom




label gamemusicon:
    $ gamemusic = True
    stop bgm fadeout 1
    play music "music/default.mp3"
    jump mcroom

label gamemusicoff:
    $ gamemusic = False
    stop music fadeout 1
    jump mcroom