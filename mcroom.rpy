#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 6am MC Room - Alexis, MC - Love, Corruption, Darker Paths
#----- End List -----

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
    $ rubyntr = True
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
    povi "There's something on top of me? What's happening?"
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
        pov "You needed to kiss me again?"
    else:
        pov "What are you doing here?"
        ls "I woke up and missed you so I came to see you."
        pov "So you're here now."
    ls "Yes. <giggle>"
    if mcroom6amfirst == True:
        pov "You watching me sleep again?"
        pov "And kissing me?"
    else:
        pov "Wait, you've been here a while?"
        pov "You watched me sleep?"
        ls "Yes and I felt the urge to kiss you. <giggle>"
        pov "You kissed me while I was asleep?"
    ls "Yes, like that fairy tale!"
    scene mcroom 6am 003
    ls "<kiss>"
    povi "Nice. What a good start to the day."
    ls "Hmm..."
    povi "Oh and she even left her eyes open while kissing."
    scene mcroom 6am 006
    ls "You liked my kiss?"
    pov "Of course! I like every kiss I get from you."
    ls "That's good, because I want to give you many more."
    povi "Wait? Is this real? Or I am still dreaming?"
    scene mcroom 6am 004
    if inc == True:
        ls "Is something wrong brother?"
    else:
        ls "Is something wrong [pov]?"
    pov "No nothing, I was just thinking. And I remembered something."
    if mcroom6amfirst == True:
        povi "And my morning wood is back again."
        pov "Ehm. You feel me poking you again?"
    else:
        povi "It's morning, so I have morning wood. And she's sitting right on it. But why didn't she mention it?"
        pov "Ehm. You didn't say something. Didn't you feel something while you are sitting on me?"
    scene mcroom 6am 001
    if mcroom6amfirst == True:
        ls "Your penis is poking me again. <giggle>"
        povi "What the hell?"
        ls "I'll get used to that feeling when I'm sitting on you <giggle>."
    else:
        ls "Are You talking about your hard penis?"
        povi "What the hell?"
        ls "Yes I noticed it poking at my crotch, but you're still sleeping so you couldn't do much about it."
        ls "I tried not to break it <giggle>."
    scene mcroom 6am 005
    pov "And it doesn't bother you?"
    ls "Haha, should I be scared of it?"
    if mcroom6amfirst == True:
        povi "Wow, she's so active again. She seems to enjoy it more and more."
    else:
        povi "Wow, she's so active this morning and not shy. What a nice surprise."
    povi "But now I'm so damn horny and her kissing makes it worse."
    ls "Time for another kiss!"
    scene mcroom 6am 003
    ls "<kiss>"
    povi "Damn this is so hot. I want more but it could scare her."
    call screen mcroom6amchoose

screen mcroom6amchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('mcroom6amchoose'), Jump('mcroom6amkisslove')) hovered tt.Action ("Just let her kiss you [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('mcroom6amchoose'), Jump('mcroom6amkisscor')) hovered tt.Action ("French kiss her [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label mcroom6amkisslove:
    $ lilsislove += 1
    povi "Well, if she just wants to kiss me, who am I to stop her?"
    ls "<kiss>"
    ls "Hmm..."
    scene mcroom 6am 002
    ls "This is so much fun."
    pov "I'm gald you're enjoying it too."
    ls "<giggle>"
    ls "You earned another one."
    scene mcroom 6am 003
    ls "<kiss>"
    povi "This gets even better."
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
    ls "I need to go now, though."
    pov "Ohh..."
    ls "But watch out, You could be getting kissed more often when you sleep!"
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
    "You wanted more, so it's time for a french kiss."
    scene mcroom 6am 007
    ls "Hnn...?"
    "She was surprised by the french kiss."
    povi "There, that's better."
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
        pov "Don't you like french kissing?"
        ls "Well... I..."
    else:
        ls "You... surprised me! Your tongue was in my mouth."
        pov "Yes, I gave you a french kiss. It's just a better kiss."
    pov "And your tongue tastes really good."
    ls "But..."
    pov "Don't be sad. You love kissing and I want to teach you more about kissing."
    pov "And you're ready for it. I noticed that."
    scene mcroom 6am 010
    if mcroom6amfirst == True:
        ls "Another french kiss..."
        pov "I'm just trying to conquer your mouth, haha."
    else:
        ls "..."
        ls "A french kiss..."
    povi "She's confused. She seemed to like it, but won't admit it."
    ls "I... I need to go."
    scene mcroom 6am 012
    "She leaves in a hurry."
    povi "Haha, maybe that was too much for her. She'll get used too it."
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
    ls "Geez! At least it's not as much of a mess as I thought it would be."
    pov "Oh you came to clean up have you?"
    if inc == True:
        ls "Yes, just as I promised my big brother."
    else:
        ls "Yes, just as I promised you I would."
    pov "Good you can start then."
    ls "Geez!"
    scene mcroom 5pm 003b
    ls "Why are they so far under the bed?"
    povi "It's better that you don't know."
    ls "Ah, I have them."
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
        "Boy" "Oh no Tracy, why are you doing this with him? I thought you loved me."
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
    if lsispronlesbian >= 4 and irinafirstmeet == True and irinalove >= 20 or lsispronlesbian >= 4 and irinafirstmeet == True and irinacorruption >= 20:
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
    povi "Ha, that worked perfectly."
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
    ls "Slowly so the laptop doesn't break."
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
    pov "I know. I just wanted to see if you would actually come and help."
    ls "Of course, I promised."
    ls "So what now?"
    pov "Since, there is nothing to do I guess you can just be happy for getting help on your homework for free."
    scene mcroom 5pm 002a
    ls "Oh ok...?"
    pov "I'm better than you, admit it! Mwa ha ha ha!"
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
    povi "Hmm... [ls] will be here to clean my room soon. But it's already clean."
    scene main mc room2 day
    povi "She won't have anything to do if the room is like this."
    povi "Maybe I should mess my room up a little so she feels like she's helping out like she promised."
    povi "I'll start with putting some clothes on the floor."
    scene main mc room day
    povi "Hm... maybe I could leave my laptop on. Then she will have to see what I want to show her."
    povi "And it could be nice to see how she would react to something naughty."
    povi "That could be fun."
    povi "Damn I'm bored... Maybe I need to find a hobby."
    jump mcwbp

label mcwbp:
    scene mcroom 5pm 007b
    call screen mcwbp1

screen mcwbp1():
    default tt = Tooltip ("")
    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcwbp1'), Jump('mcroomsetupporn')) hovered tt.Action ("Set up some porn") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('mcwbp1'), Jump('mcroomnosetupporn')) hovered tt.Action ("Don't do it") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label mcroomnosetupporn:
    scene main mc room day
    povi "No. I won't do it. I don't want her to see that dirty stuff if she doesn't want to."
    povi "Putting away the clothes is enough."
    $ setupnopron = True
    $ dtime += 1
    jump mcroom

label mcroomsetupporn:
    scene mcroom 5pm 007b
    povi "What should I choose?"
    if inc == True:
        povi "What is going to get my little sister's best reaction?"
    else:
        povi "What is going to get [ls]'s best reaction?"
    jump mcsup

label mcsup:
    call screen mcsup1

screen mcsup1():
    modal True
    default tt = Tooltip ("Select Porn")
    tag mcsuptag

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcsup1'), Jump('mcroomsetupanal')) hovered tt.Action ("Anal") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcsup1'), Jump('mcroomsetupbdsm')) hovered tt.Action ("BDSM") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcsup1'), Jump('mcroomsetupfemdom')) hovered tt.Action ("Femdom") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcsup1'), Jump('mcroomsetupgb')) hovered tt.Action ("Gang Bang") focus_mask True
        if inc == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcsup1'), Jump('mcroomsetupinc')) hovered tt.Action ("Incest") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcsup1'), Jump('mcroomsetupint')) hovered tt.Action ("Interracial") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcsup1'), Jump('mcroomsetuples')) hovered tt.Action ("Lesbian") focus_mask True
        if NTR == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('mcsup1'), Jump('mcroomsetupntr')) hovered tt.Action ("NTR") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('mcsup1'), Jump('mcroomnosetupporn1')) hovered tt.Action ("Nevermind") focus_mask True

        frame:
            if tt.value == "" or tt.value ==" ":
                background None
            xalign .5
            yalign .23
            xanchor .5
            yanchor .23
            xfill True
            yfill True
            xmaximum 252
            ymaximum 63
            text tt.value at center

label mcroomsetupgb:
    scene mcroom 5pm 007gb
    "Girl" "Oh yes fuck me harder! Give me all your dicks!"
    povi "Oh yes that'll do it."
    povi "Now I have to wait for her."
    $ setuppron = True
    $ prongangbang = True
    $ dtime += 1
    jump mcroom

label mcroomsetupbdsm:
    scene mcroom 5pm 007bdsm
    "Girl" "Please master! I'll be obedient!"
    povi "Oh yes that'll do it."
    povi "Now I have to wait for her."
    $ setuppron = True
    $ pronBDSM = True
    $ dtime += 1
    jump mcroom

label mcroomsetupinc:
    scene mcroom 5pm 007inc
    "Girl" "I love you brother! I know it's forbidden but please fuck me more!"
    povi "Oh yes that'll do it."
    povi "Now I have to wait for her."
    $ setuppron = True
    $ proninc = True
    $ dtime += 1
    jump mcroom

label mcroomsetupint:
    scene mcroom 5pm 007int
    "Girl" "Oh my god! You're so big!"
    povi "Oh yes that'll do it."
    povi "Now I have to wait for her."
    $ setuppron = True
    $ proninterracial = True
    $ dtime += 1
    jump mcroom

label mcroomsetuples:
    scene mcroom 5pm 007les
    "Girl" "You taste so good! I won't ever stop!"
    povi "Oh yes that'll do it."
    povi "Now I have to wait for her."
    $ setuppron = True
    $ pronlesbian = True
    $ dtime += 1
    jump mcroom

label mcroomsetupntr:
    scene mcroom 5pm 007ntr
    "Boy" "Oh no Tracy, why you do this with him? I thought you loved me."
    povi "Oh yes that'll do it."
    povi "Now I have to wait for her."
    $ setuppron = True
    $ pronntr = True
    $ dtime += 1
    jump mcroom

label mcroomnosetupporn1:
    scene main mc room day
    povi "No. I won't do it. I don't want her to see that dirty stuff if she doesn't want to."
    povi "Putting away the clothes is enough."
    $ setupnopron = True
    $ dtime += 1
    jump mcroom

label mcroomsetupanal:
    hide screen locations
    scene mcroom 5pm 007anal
    "Girl" "Oh my god! You're in my asshole!"
    povi "Oh yes that will do it."
    povi "Now I have to wait for her."
    $ setuppron = True
    $ pronanal = True
    $ dtime += 1
    jump mcroom

label mcroomsetupfemdom:
    hide screen locations
    scene mcroom 5pm 007femdom
    "Girl" "Yes, be a good slave!"
    povi "Oh yes that will do it."
    povi "Now I have to wait for her."
    $ setuppron = True
    $ pronfemdom = True
    $ dtime += 1
    jump mcroom

label mcroomlesbian:
    hide screen locations
    scene mcroom 5pm 005les
    "You both hear your door suddenly open behind you."
    povi "Oh shit, someone is coming in!"
    irina "Hey [pov], are you in here?"
    scene mcroom 5pm 020
    irina "There you are! I've been looking for you!"
    pov "Oh hey [irina]! Now's not the best time..."
    irina "What are you are two watching?"
    scene mcroom 5pm 022
    "Girl" "Oh my god! You tongue is amazing! Don't stop... hnnn..."
    scene mcroom 5pm 021
    "[ls] tries to cover up the porn playing on laptop with her hand, but it was too late."
    povi "Well, that's that. Caught red handed. Might as well be honest about it."
    pov "We're watching a hot scene I found last night. Want to join us?"
    scene mcroom 5pm 023
    if inc == True:
        povi "Lil sis is a bit stunned it seems. She's just staring at [irina]. Is it because of the lesbian porn?"
    else:
        povi "[ls] is a bit stunned it seems. She's just staring at [irina]. Is it because of the lesbian porn?"
    irina "Oh! You are guys are watching porn together? How kinky! I'm in."
    irina "I think I know this one!"
    scene mcroom 5pm 024
    irina "Do you guys watch this kind of stuff together often [ls]?"
    "[ls] just stares at [irina], unable or unwilling to speak just yet."
    scene mcroom 5pm 025
    povi "Might as well go with it..."
    pov "Yeah.. we watch this stuff all time. No big deal right [ls]? We're all adults here."
    irina "Oh I agree. I think people demonize porn too much. It's just harmless fun!"
    scene mcroom 5pm 022
    "You all watch the video unfold for a while."
    "girl" "Fuck yes! I'm going to cum! Right there! Right there... Hnng... hah... OH GOD!!!"
    scene mcroom 5pm 025
    irina "I do have to say, it's really getting me hot. Watching it with someone."
    "[irina] and [ls] are both looking at you, lust in their eyes"
    "But it is [irina] who makes her move."
    scene mcroom 5pm 026a
    "She kisses you. Shoving her tongue into your mouth. Searching all it's corners and twisting around your own."
    "[ls] just watches in stunned silence. She's barely said a word since [irina] came in. But you can hear her breathing get heavier."
    scene mcroom 5pm 026b
    "You kick it up and notch and dip [irina] in your arms. Taking the lead in the passionate embrace."
    "Your tongues darting into each others mouths. Eager to taste the other."
    ls "Hnnng..."
    scene mcroom 5pm 027
    "[ls] moves towards the door, seemingly in a rush to leave you two alone."
    povi "I heard [ls] moan. I'm pretty sure this was turning her on too. She get's embarrassed easily."
    "You're just about to break the kiss and call out to [ls]... but [irina] beats you to it."
    scene mcroom 5pm 028
    irina "[ls], wait!"
    ls "Huh?"
    scene mcroom 5pm 029
    irina "I know this is probably a bit new for you and we don't know each other very well yet."
    irina "But I don't want you to go just because of me. I barged in on you two and I don't want to spoil your fun!"
    ls "Oh, but we weren't..."
    scene mcroom 5pm 030
    "[irina] gently pulls [ls] back into the room."
    irina "I hope we can become good friends though. In time."
    scene mcroom 5pm 031
    irina "You really are so beautiful [ls]. Do you know that?"
    povi "Wow, is [irina] seducing [ls]?! This could get really interesting!"
    scene mcroom 5pm 032
    ls "You really think so? I mean you're so gorgeous and you think I'm beautiful?"
    irina "I really do. You have a natural beauty that I just can't seem to pull off. I'm jealous."
    povi "That's really working on [ls]. Her face is blushing even."
    irina "[ls] I hope you won't mind, but I just have to do this..."
    ls "Oh...ok."
    "[irina] moves forward and leans in..."
    scene mcroom 5pm 033
    "[irina] kisses [ls] tenderly on her lips. Not just a friendly peck on the mouth, but a real kiss."
    ls "Hmmm. <kiss>"
    irina "<kiss> Mmmm."
    scene mcroom 5pm 035
    irina "Yup, that's what I thought. You're lips are so soft!"
    irina "But there is somewhere else that looks even softer..."
    povi "God damn, I feel like I should be taking notes!"
    scene mcroom 5pm 036
    "[irina] leans in again, this time kissing the side of [ls]'s neck."
    ls "Hnnn..."
    povi "[ls] is really getting into this. She's looking at me, but her eyes aren't really focused on me."
    scene mcroom 5pm 037
    "[irina] makes her way up to [ls]'s ear and sucks it in her mouth."
    ls "Hnng... Hmmm..."
    scene mcroom 5pm 038
    irina "That was really nice [ls]. You taste so sweet."
    ls "Th... thanks. You did too."
    irina "We should do this again sometime."
    ls "Yeah... I'd like that..."
    scene mcroom 5pm 039
    "They both seemed to remember that you're in the room with them still."
    irina "[pov]! You can't be leaving me out of these little private movie nights anymore!"
    irina "Maybe next time we can all have some more fun getting to know each other."
    ls "Hnnn..."
    scene mcroom 5pm 040
    if inc == True:
        "Lil sis leaves the room first."
    else:
        "[ls] leaves the room first."
    irina "I hope you liked that [pov], I thought I could help you warm her up a bit."
    irina "If it works, then you better take me out sometime as a thank you!"
    pov "How about I take you out sometime either way."
    irina "Haha, deal!"
    irina "And after or date... I might invite you out for a surprise."
    povi "Interesting."
    scene black
    "[irina] leaves the room."
    $ irinarelationship += 1
    $ dtime += 1
    $ lesbiandate1 = True #----- added 0.7 -----
    #----- added -----
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

#----- Custom -----
label enablemusic:
    "Default Music Enabled."
    $ gamemusic = True
    stop music fadeout 2
    play music "music/default.mp3"
    jump mcroom

label disablemusic:
    "Default Music Enabled."
    $ gamemusic = False
    stop music fadeout 2
    jump mcroom

label renamecharacters:
    hide screen locations
    menu:
        "Main Character":
            $ povname = renpy.input(_("So what is your first name?")) or _("Sam")
            $ povname = povname.strip()
            if povname == "":
                $ povname = "Sam"
            $ pov = Character("[povname]", who_color="#0066cc", what_color="#ffffff")
            $ povi = Character("[povname]", what_italic=True, who_color="#0066cc", what_color="#ff8000")
            "Main Character renamed to [pov]."
            jump mcroom
        "Nicole":
            if inc == True:
                $ nicolename = renpy.input(_("What's your mom's name?")) or _("Nicole")
                $ nicolename = nicolename.strip()
                $ momname = "Mom"
                if nicolename == "":
                    $ nicolename = "Nicole"
                    $ momname = "Mom"
            else:
                $ nicolename = renpy.input(_("What's the name of your mom's childhood friend?")) or _("Nicole")
                $ nicolename = nicolename.strip()
                if nicolename == "":
                    $ nicolename = "Nicole"
                    $ momname = "Nicole"
                else:
                    $ momname = nicolename
            $ mother = Character("[nicolename]", who_color="#ea9aff", what_color="#ea9aff")
            $ mom = Character("[momname]", who_color="#ea9aff", what_color="#ea9aff")
            "Nicole renamed to [mother]."
            jump mcroom
        "Cassandra":
            if inc == True:
                $ bsname = renpy.input(_("What's your big sister's name?")) or _("Cassandra")
                $ bsname = bsname.strip()
                if bsname == "":
                    $ bsname = "Cassandra"
            else:
                $ bsname = renpy.input(_("What's your older childhood friends name?")) or _("Cassandra")
                $ bsname = bsname.strip()
                if bsname == "":
                    $ bsname = "Cassandra"
            $ bs = Character("[bsname]", who_color="#ea9aff", what_color="#ea9aff")
            "Cassandra renamed to [bs]."
            jump mcroom
        "Alexis":
            if inc == True:
                $ lsname = renpy.input(_("What's your little sister's name?")) or _("Alexis")
                $ lsname = lsname.strip()
                if lsname == "":
                    $ lsname = "Alexis"
            else:
                $ lsname = renpy.input(_("What's your younger childhood friends name?")) or _("Alexis")
                $ lsname = lsname.strip()
                if lsname == "":
                    $ lsname = "Alexis"
            $ ls = Character("[lsname]", who_color="#ea9aff", what_color="#ea9aff")
            "Alexis renamed to [ls]."
            jump mcroom
        "Irina" if irinafirstmeet == True:
            $ irinaname = renpy.input(_("My name is...")) or _("Irina")
            $ irinaname = irinaname.strip()
            if irinaname == "":
                $ irinaname = "Irina"
            $ irina = Character("[irinaname]", who_color="#ea9aff", what_color="#ea9aff")
            "Irina renamed to [irina]."
            jump mcroom
        "Kate" if katefirstmeet == True:
            $ katename = renpy.input(_("Her name is...")) or _("Kate")
            $ katename = katename.strip()
            if katename == "":
                $ katename = "Kate"
            $ kate = Character("[katename]", who_color="#ea9aff", what_color="#ea9aff")
            "Kate renamed to [kate]."
            jump mcroom
        "Miranda" if mirandafirstmeet == True:
            $ mirandaname = renpy.input(_("Her name is...")) or _("Miranda")
            $ mirandaname = mirandaname.strip()
            if mirandaname == "":
                $ mirandaname = "Miranda"
            $ miranda = Character("[mirandaname]", who_color="#ea9aff", what_color="#ea9aff")
            "Miranda renamed to [miranda]."
            jump mcroom
        "Susan" if susanfirstmeet == True:
            $ susanname = renpy.input(_("Her name is...")) or _("Susan")
            $ susanname = susanname.strip()
            if susanname == "":
                $ susanname = "Susan"
            $ susan = Character("[susanname]", who_color="#ea9aff", what_color="#ea9aff")
            "Susan renamed to [susan]."
            jump mcroom
        "Vivian" if vivianfirstmeet == True:
            $ vivianname = renpy.input(_("My name is...")) or _("Vivian")
            $ vivianname = vivianname.strip()
            if vivianname == "":
                $ vivianname = "Vivian"
            $ vivian = Character("[vivianname]", who_color="#ea9aff", what_color="#ea9aff")
            "Vivian renamed to [vivian]."
            jump mcroom
        "Ruby" if rubyfirstmeet == True:
            $ rubyname = renpy.input(_("My name is...")) or _("Ruby")
            $ rubyname = rubyname.strip()
            if rubyname == "":
                $ rubyname = "Ruby"
            $ ruby = Character("[rubyname]", who_color="#ea9aff", what_color="#ea9aff")
            "Ruby renamed to [ruby]."
            jump mcroom
        "All NPC Names Reset to Default":
            if inc == True:
                $ nicolename = "Nicole"
                $ momname = "Mom"
            else:
                $ nicolename = "Nicole"
                $ momname = "Nicole"
            $ mother = Character("[nicolename]", who_color="#ea9aff", what_color="#ea9aff")
            $ mom = Character("[momname]", who_color="#ea9aff", what_color="#ea9aff")
            if inc == True:
                $ dadname = "Dad"
            else:
                $ dadname = "Bruce"
            $ dad = Character("[dadname]", who_color="#ff3533", what_color="#ff3533")
            $ bsname = "Cassandra"
            $ bs = Character("[bsname]", who_color="#ea9aff", what_color="#ea9aff")
            $ lsname = "Alexis"
            $ ls = Character("[lsname]", who_color="#ea9aff", what_color="#ea9aff")
            if irinafirstmeet == True:
                $ irinaname = "Irina"
                $ irina = Character("[irinaname]", who_color="#ea9aff", what_color="#ea9aff")
            if katefirstmeet == True:
                $ katename = "Kate"
                $ kate = Character("[katename]", who_color="#ea9aff", what_color="#ea9aff")
            if mirandafirstmeet == True:
                $ mirandaname = "Miranda"
                $ miranda = Character("[mirandaname]", who_color="#ea9aff", what_color="#ea9aff")
            if susanfirstmeet == True:
                $ susanname = "Susan"
                $ susan = Character("[susanname]", who_color="#ea9aff", what_color="#ea9aff")
            if vivianfirstmeet == True:
                $ vivianname = "Vivian"
                $ vivian = Character("[vivianname]", who_color="#ea9aff", what_color="#ea9aff")
            if rubyfirstmeet == True:
                $ rubyname = "Ruby"
                $ ruby = Character("[rubyname]", who_color="#ea9aff", what_color="#ea9aff")
            "All NPC Names Reset."
            jump mcroom
        "Cancel":
            jump mcroom
