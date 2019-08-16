#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

#----- Event List -----
# 1. 2am Basement - Alexis, Davide - Darker Paths
# 2. 4am Basement - Alexis, MC - Love, Corruption, Twisted
# 3. 9am Basement - Cassandra, MC - Love, Corruption, Twisted
# 4. 4pm Basement - Cassandra, Frank - Darker Paths
# 5. 4pm Basement - Alexis, MC - Love, Corruption, Darker Paths
# 6. 10pm Basement - MC, Nicole - Love, Corruption, Twisted
# 7. 8pm Basement - Bruce, Cassandra - Listen, Darker Paths - Custom
# 8. 4pm Basement - MC, Nicole - Look, Open, Talk
# 9. 11pm/12am Basement - Bruce, Davide, MC, Nicole - Darker Paths - Custom
#----- End List -----

label basement2am:
    hide screen locations
    scene black
    $ dtime = 2
    "You wake up."
    povi "Huh? Did I hear something?"
    povi "No. It was nothing."
    "You fall asleep again."
    with vpunch
    povi "DAMN IT!"
    jump basement2am2

label basement2am2:
    scene black
    call screen basement2am3

screen basement2am3():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_look_%s.png" action (Hide('basement2am3'), Jump('basement2amcont')) hovered tt.Action ("Check it out") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('basement2am3'), Jump('basement2am2sleep')) hovered tt.Action ("Go to sleep") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label basement2am2sleep:
    scene black
    pov "No, I don't care!"
    "You go to sleep again."
    if NTR == True and momrelationship <= 5 or hardntr == True:
        jump kitchen2am
    elif meet4am == True:
        $ dtime = 4
        scene black
        "You woke up."
        povi "It's 4am. I should meet with [ls]."
        jump base4amal
    elif hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard

label basement2amcont:
    scene black
    " \"Make sure you come here again at night time so that I can teach you more!\" "
    povi "I was right. That noise was [ls]."
    povi "I need to know what they're up to."
    "You go to the basement silently."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene basement 2am 001
    povi "What the hell? [ls] is restrained and Davide looks like he's going to fuck her."
    povi "She's even wearing a ball-gag. Is he raping her?"
    davide "Now it's the time you get my big black dick, little slut!"
    davide "Are you happy to loose your anal virginity to me?"
    ls "Yesh... Hm... appy."
    povi "Thank god. At least he's not raping her. But he might still be using the drug, and that's pretty much the same if so."
    povi "Should I show myself or just watch them to see if she's ok?"
    call screen base2amwatch

screen base2amwatch():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base2amwatch'), Jump('base2showlanding')) hovered tt.Action ("Show yourself") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base2amwatch'), Jump('base2hide')) hovered tt.Action ("Watch them secretly") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base2showlanding:
    call screen checkdarkerpaths_alexis
    jump base2show

label base2show:
    povi "I'm not going to hide, they should know that I'm here."
    scene basement 2am 002a
    if alexis_voyeur == True or alexis_sadist == True:
        pov "Hey there, lovebirds!"
    else:
        pov "Davide!"
    ls "Hnng?"
    davide "Oh hey [pov]! You've come just at the right time, the time she sacrifices her anal virginity to me."
    ls "Hmm!"
    if alexis_voyeur == True or alexis_sadist == True:
        pov "Oh, you aren't so happy that I'm here [ls]?"
    else:
        pov "Davide! You drugged man! That's the only way she would agree to this!"
    ls "HNNG!"
    davide "Shut up slut! If he want to watch and learn then let him!"
    if alexis_revenge == True:
        povi "I need to get closer and try to stop this!"
    scene basement 2am 003a
    ls "Hnn..."
    if alexis_voyeur == True:
        pov "But why use this whole elabrate setup?"
        davide "She needs to be restraint when she feel my big dick for her first time."
        davide "It won't be easy to take for her and I don't need her to struggle like crazy."
        pov "And the ball-gag?"
        davide "What do you think? She'll scream like crazy, haha!"
        pov "Somewhat nice seeing her in such a submissive position."
        davide "Want to see something else, come here [pov]!"
    elif alexis_ntr == True:
        pov "Why do you have her tied up like that?"
        davide "She needs to be restraint when she feel my big dick for her first time."
        davide "It won't be easy to take for her and I don't need her to struggle like crazy."
        pov "And the ball-gag?"
        davide "What do you think? She'll scream like crazy, haha!"
        povi "I can't do anything to stop this. What was I thinking showing myself to them?."
        davide "Want to see something else, come here [pov]!"
    elif alexis_revenge == True:
        if inc == True:
            pov "You have her trussed up like this, seriously our mother would be pissed!"
        else:
            pov "You have her trussed up like this, seriously her mother would be pissed!"
        davide "I don't give a fuck! And if you try anything, just remember [ls] here is defenseless..."
        davide "Anyway, She needs to be in restraints when she feels my big dick for the first time."
        davide "It won't be easy for her to take it all and I don't need her struggling like crazy."
        pov "And the ball-gag?"
        davide "What do you think? She'll scream like crazy, haha!"
        pov "Well I'm not going any where Davide. You're going to pay for this!"
        davide "Want to see something else, come here [pov]!"
    else:
        if inc == True:
            pov "I like the elaborate setup! Haha! Our mother would be pissed!"
        else:
            pov "I like the elaborate setup! Haha! Her mother would be pissed!"
        davide "I don't give a fuck! And if you try anything, just remember [ls] here is defenseless..."
        davide "Anyway, She needs to be in restraints when she feels my big dick for the first time."
        davide "It won't be easy for her to take it all and I don't need her struggling like crazy."
        pov "And the ball-gag?"
        davide "What do you think? She'll scream like crazy, haha!"
        pov "Well, it's good you're thinking ahead!"
        davide "Want to see something else, come here [pov]!"
    scene basement 2am 004a
    if alexis_voyeur == True:
        pov "Oh..."
        davide "I already widened her hole a little."
        pov "I see, but it's still too small. I hope you use much lube or it'll be very painful."
        ls "Hnng! Hnng!"
        davide "Relax girl!"
        if inc == True:
            davide "Your brother is making fun of it."
        else:
            davide "[pov] is making fun of it."
        pov "Haha."
        ls "Hmm..."
        davide "I'll use just a small amount because she should really feel the first time she gets pierced."
    elif alexis_voyeur == True:
        pov "Huh..."
        davide "I already widened her hole a little."
        povi "Why the fuck is he showing me this? Just rubbing it all in my face...."
        ls "Hnng! Hnng!"
        davide "Relax girl!"
        if inc == True:
            davide "Your brother is making sure you're ready for me."
        else:
            davide "[pov] is making sure you're ready for me."
        pov "No... I'm..."
        ls "Hmm..."
        davide "I'll use just a small amount because she should really feel the first time she gets pierced."
    elif alexis_revenge == True:
        pov "Davide you piece of shit..."
        davide "I already widened her hole a little."
        pov "You better not hurt her!"
        povi "Seriously, is that the best I can do. I need to get a weapon or something!"
        ls "Hnng! Hnng!"
        davide "Relax girl!"
        if inc == True:
            davide "Your brother isn't going to stop us."
        else:
            davide "[pov] isn't going to stop us."
        pov "..."
        ls "Hmm..."
        davide "I'm only going to use a small amount of lube, because she should feel how she gets pierced."
    else:
        pov "I see you started already."
        davide "I widened her hole a little."
        pov "I see, but it's still too small. Without lube it'll be very painful."
        ls "Hnng! Hnng!"
        davide "Relax girl!"
        if inc == True:
            davide "Your brother isn't going to stop us."
        else:
            davide "[pov] isn't going to stop us."
        pov "..."
        ls "Hmm..."
        davide "But I'm only going to use a small amount of lube, because she should feel it fully when she gets pierced."
    scene basement 2am 005a
    if alexis_voyeur == True:
        pov "Damn, that'll be really a hard ride."
        ls "Hnng?"
        davide "The tip is almost in. Your lubed hole is sucking me slowly in."
        pov "Don't break her, haha."
        davide "She needs to learn to get fucked good."
    elif alexis_ntr == True:
        povi "Damn it! It should be me taking her in the ass."
        ls "Hnng?"
        davide "The tip is almost in. Your lubed hole is sucking me slowly in."
        povi "Fuck you Davide!."
        davide "She needs to learn to get fucked good."
    elif alexis_revenge == True:
        pov "You're going to tear her apart like that... Please! Don't do this."
        ls "Hnng?"
        davide "Please now huh? I thought you were a weak as bitch. Guess I was right."
        davide "The tip is almost in [ls]. Your lubed hole is sucking me slowly in."
        pov "Davide, god damn you!"
        davide "She needs to learn to get fucked good anyway."
    else:
        pov "That'll be really a hard ride."
        ls "Hnng?"
        davide "The tip is almost in. Your lubed hole is sucking me slowly in."
        pov "You're going to break her, haha."
        davide "She needs to learn to get fucked good."
    scene basement 2am 006a
    if alexis_voyeur == True:
        davide "There we go!"
        ls "HNNG!"
        davide "All in!"
        if inc == True:
            povi "Damn! He's balls deep inside my little sister with his big dick."
        else:
            povi "Damn! He's deep inside [ls] with his big dick."
    elif alexis_ntr == True:
        davide "There we go!"
        ls "HNNG!"
        davide "All in!"
        if inc == True:
            povi "Holy shit! He's balls deep inside my little sister. Why is she letting him do this to her?"
        else:
            povi "Holy shit! He's balls deep inside her. Why is she letting him do this to her?"
    elif alexis_revenge == True:
        davide "There we go!"
        ls "HNNG!"
        davide "All in!"
        if inc == True:
            pov "That fucker! I will get back to him for hurting my sister!"
        else:
            pov "That fucker! I will get back to him for hurting [ls]!"
    else:
        davide "There we go!"
        ls "HNNG!"
        davide "All in!"
        if inc == True:
            pov "Damn! He's balls deep inside my little sister with his big dick."
        else:
            pov "Damn! He's deep inside [ls] with his big dick."
    scene basement 2am 007a
    if alexis_voyeur == True or alexis_ntr == True:
        ls "Hnng! Hnng!"
        davide "Oh yes! Your thight asshole is clinging on my dick."
        davide "Your tight ass is a dream!"
        ls "Hnng! Hnng!"
        davide "Stop trying to press me out! I'll mark your asshole, no matter what!"
        if alexis_voyeur == True:
            pov "Oh they're even some tears."
        else:
            povi "I think she's crying a bit..."
        davide "They're needed to show that she's putting some effort in it."
        pov "Hmm, that's also a way to explain..."
        davide "She can bear it. She need to, if she wants to be a good girlfriend."
    else:
        ls "Hnng! Hnng!"
        davide "Oh yes! Your thight asshole is clinging on my dick."
        davide "Your tight ass is a dream!"
        ls "Hnng! Hnng!"
        davide "Stop trying to press me out! I'll mark your asshole, no matter what!"
        if alexis_revenge == True:
            pov "God, she's crying you asshole!"
            davide "They're needed to show that she's putting some effort in it."
            povi "I'll remember that when its time to shove a blade up your ass Davide!"
        else:
            pov "She's crying now. Nice!"
            davide "They're needed to show that she's putting some effort in it."
            povi "Hehe, yeah, I wonder if you'd be so tough Davide if it was your ass getting pierced!"
        davide "She can bear it. She need to, if she wants to be a good girlfriend."
    scene basement 2am 008a
    if alexis_voyeur == True or alexis_ntr == True:
        davide "Much better!"
        ls "Hnn... hnn..."
        if alexis_voyeur == True:
            pov "She seems to be more relaxed."
            davide "Yes, she is. It's like a dream to fuck this small hole!"
        else:
            povi "She's relaxed now. She's giving herself to him even more."
            davide "It's like a dream to fuck this small hole!"
        ls "Hnn... hnn..."
        davide "She's working hard to be my slut!"
        if alexis_voyeur == True:
            povi "Damn it! Lucky bastard!"
        else:
            povi "That should be me fucking her!!!"
        "Davide fucks her faster."
    else:
        davide "Much better!"
        ls "Hnn... hnn..."
        if alexis_revenge == True:
            povi "She looks like she's giving up... I'm so sorry!."
        else:
            povi "She looks like she's giving up... it's about time."
        davide "Yes, she's not even fighting anymore. It's like a dream to fuck this small hole!"
        ls "Hnn... hnn..."
        davide "She's working hard to be my slut!"
        if alexis_revenge == True:
            povi "Fucking bastard!"
        else:
            pov "Looks like it!"
        "Davide fucks her faster."
    scene basement 2am 009a
    if alexis_voyeur == True or alexis_ntr == True or alexis_sadist == True:
        ls "Hgg... hgg..."
        if alexis_voyeur == True:
            pov "Oh she's about to faint. Don't overdo it!"
        elif alexis_sadist == True:
            pov "Oh she's about to faint..."
        else:
            "I think she's going to faint!"
        davide "Hell yeah. She did good work, I'm already at my limit."
        davide "No need to faint, slut! Just endure it a little longer."
        davide "I'm... HNNG! HNNG! Yes, I'm gonna mark you!"
        ls "HGGG..."
    else:
        ls "Hgg... hgg..."
        pov "Fuck Davide! She's about to faint. Just stop it!"
        davide "Hell yeah. She did good work, I'm already at my limit."
        davide "No need to faint, slut! Just endure it a little longer."
        davide "I'm... HNNG! HNNG! Yes, I'm gonna mark you!"
        ls "HGGG..."
    scene basement 2am 010a
    if alexis_voyeur == True or alexis_ntr == True:
        davide "Damn! She can't take it all inside. It's spraying out of her."
        ls "Hnnn..."
        if alexis_voyeur == True:
            povi "And she even got humiliated on her first time."
        else:
            povi "He humiliated her and there was nothing I could do about it."
        davide "Come here and look at this mess."
    else:
        davide "Damn! She can't take it all inside. It's spraying out of her."
        ls "Hnnn..."
        if alexis_revenge == True:
            povi "You don't have to humiliate her too you fucker!"
        else:
            povi "Good choice to humiliate her too!"
        davide "Come here and look at this mess chump!"
    scene basement 2am 011a
    if alexis_voyeur == True:
        pov "Wow! The hole is really wide."
        davide "Yes, she took me deep."
    elif alexis_ntr == True:
        povi "He reamed her!"
    elif alexis_revenge == True:
        pov "There, are you done now you asshole?"
        davide "Yes, she took me deep."
    else:
        pov "Wow! The hole is really wide."
        davide "Yes, she took me deep."
    scene black
    "Davide untied [ls]."
    scene basement 2am 012a
    if alexis_voyeur == True or alexis_ntr == True:
        ls "Did I do well? Are you satisfied with me, lover?"
        davide "Hm... so, so. It could be still better..."
        ls "But I really tried."
        if alexis_voyeur == True:
            povi "Damn, even now he's telling her how he wants her to be."
            povi "And she's already fallen for his bullshit."
        else:
            povi "Damn, even now he's telling her how he wants her to be."
            povi "I can't believe she's just giving herself to him like that."
    else:
        ls "Are we done now? I can go now, you won't hurt anyone right?"
        davide "Hm... you were only so, so. It could be still better..."
        ls "But I really tried."
        if alexis_revenge == True:
            povi "God damn him! Using drugs and threats of violence. I'm going to kill him, I swear!"
            povi "She did nothing to deserve this. No one deserves this."
        else:
            povi "God damn! Using drugs and threats of violence. I will be doing all of that too!"
            povi "She did nothing to deserve this. No one deserves this. That's what makes it so great."
    scene basement 2am 013a
    if alexis_voyeur == True:
        povi "There is so much cum inside her. It's still dripping out."
        povi "She's fixated on him."
        if inc == True:
            povi "She doesn't even seem to care that she's naked in front of her brother with cum dripping out of her asshole."
            ls "Brother?"
        else:
            povi "She doesn't even seem to care that she's naked in front of me with cum dripping out of her asshole."
            ls "[pov]?"
        pov "Hm?"
    else:
        povi "There is so much cum inside her. It's still dripping out."
        povi "She's just staring at him..."
        if inc == True:
            povi "She doesn't even seem to notice that she's naked in front of her brother with cum dripping out of her asshole."
            ls "Brother?"
        else:
            povi "She doesn't even seem to notice that she's naked in front of me with cum dripping out of her asshole."
            ls "[pov]?"
        pov "Hm?"
    scene basement 2am 014a
    if alexis_voyeur == True or alexis_ntr == True:
        davide "What did you think about her perfomance?"
        ls "Did I ruin it?"
        povi "I still can't believe it."
        if alexis_voyeur == True:
            if inc == True:
                pov "No, I think you did good, lil sis."
            else:
                pov "No, I think you did good [ls]."
            davide "Hm, maybe [pov] is right. It was very good for your first time taking a black dick!"
        else:
            pov "..."
    else:
        davide "What did you think about her perfomance?"
        ls "Did I do ok?"
        if alexis_revenge == True:
            povi "I still can't believe this."
            if inc == True:
                pov "You did just fine, lil sis. You protected us."
            else:
                pov "You did just fine, [ls]. You protected us."
                davide "Hm, maybe [pov] is right. It was very good for your first time taking a black dick!"
            pov "Shut up..."
        else:
            if inc == True:
                pov "You did just fine, lil sis."
            else:
                pov "You did just fine, [ls]."
                davide "Hm, maybe [pov] is right. It was very good for your first time taking a black dick!"
            pov "See? I told you so."
    scene basement 2am 015a
    if alexis_voyeur == True or alexis_ntr == True:
        ls "Oh thank you! I did good!"
        davide "Yes, I already said that slut!"
        if alexis_voyeur == True:
            povi "I had no idea she was such a slut!"
        else:
            pov "..."
        ls "I took it in the back for the first time and made my boyfriend happy."
        davide "So you want to be an ass-slut?"
        scene basement 2am 016a
        if inc == True:
            ls "You hear that, brother? I made Davide happy and was a good ass-slut!"
        else:
            ls "You hear that, [pov]? I made Davide happy and was a good ass-slut!"
        povi "And there's the rest of her innocence going away..."
        davide "It's just the adrenaline, slut. You gained it through my sperm. Next time we'll see how you do."
        ls "I'll give my best, lover."
        davide "So you had a fine show [pov], but I think it's time that we leave."
        davide "Bruce and [mother] are still drunk, but I don't want to risk us getting caught."
        davide "It's still too soon to let them know about her."
        ls "Haha, mom will be so mad."
        davide "You go first, [ls] can go a little later."
        pov "OK. No problem. Bye Davide, bye ass-slut, haha."
        ls "Haha..."
        scene black
        "You leave the basement and go back to your room."
        "A while later you hear [ls] going to her room too."
    elif alexis_revenge == True:
        ls "I did good... So you won't hurt anyone?"
        povi "Those drugs really get her out of focus."
        davide "Yes, I already said that slut!"
        pov "..."
        ls "Ok. This is the last time right? I don't have to do this stuff anymore right?"
        davide "What you don't want to be my personal ass-slut?"
        pov "No Davide, she doesn't. She did what you asked. Why don't you leave her alone."
        scene basement 2am 016a
        povi "She seems happy I said something, but with the drugs, she's just acting so weird!"
        if inc == True:
            ls "You hear that, brother? I saved the family!"
        else:
            ls "You hear that, [pov]? I saved my family! And you!"
        povi "And there's goes the rest of her innocence we were trying to protect..."
        davide "That's just the adrenaline, slut. Well talk about this more next time..."
        scene edited basement 2am 016a
        ls "Oh, so there is going to be a next time?"
        davide "Well I think you saw enough [pov], but I think it's time that we leave."
        davide "Bruce and [mother] are still drunk, but I don't want to risk getting caught."
        davide "It's still too soon to let them know about her."
        ls "I don't want them to know..."
        pov "There's not going to be a next time, Davide."
        davide "Haha... We'll see, won't we?"
        scene black
        "You and [ls] leave together."
        "You go to your room after helping [ls] into bed."
    else:
        ls "I did good... So you won't hurt anyone?"
        povi "Those drugs really get her out of focus."
        davide "Yes, I already said that slut!"
        pov "Well done."
        ls "Ok. This is the last time right? I don't have to do this stuff anymore right?"
        davide "What you don't want to be my personal ass-slut?"
        pov "No Davide, she didn't say that. She did what you asked. I'm sure she'll do it again."
        scene basement 2am 016a
        povi "She seems oddly happy I said something, but with the drugs, she's just acting so weird!"
        if inc == True:
            ls "You hear that, brother? I saved the family!"
        else:
            ls "You hear that, [pov]? I saved my family! And you!"
        povi "And there's goes the rest of her innocence..."
        davide "That's just the adrenaline, slut. Well talk about this more next time..."
        scene edited basement 2am 016a
        ls "Oh, so there is going to be a next time?"
        davide "Well, I think you saw enough [pov], but I think it's time that we leave."
        davide "Bruce and [mother] are still drunk, but I don't want to risk getting caught."
        davide "It's still too soon to let them know about her."
        ls "I don't want them to know..."
        pov "I don't know... [ls]. We might have to tell them if you don't behave, right Davide?"
        davide "Haha... We'll see, won't we?"
        scene black
        "You and [ls] leave together."
        "You go to your room after [ls] makes it into bed."
    $ base2amalexisntrfirst = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if NTR == True and momrelationship <= 5 or hardntr == True:
        jump kitchen2am
    elif meet4am == True:
        $ dtime = 4
        scene black
        "You woke up."
        povi "It's 4am. I should meet with [ls]."
        jump base4amal
    elif hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard

label base2hide:
    povi "I need to see this but they don't need to know."
    "You hide silently behind the armchair."
    scene basement 2am 002b
    povi "What? She's spotted me! But she don't do anything to make him notice."
    povi "Is she's okay with me watching?"
    call screen checkdarkerpaths_alexis
    if alexis_voyeur == True or alexis_ntr == True:
        $ base2likentr = True
    else:
        $ base2likentr = False
    jump base2disapprove

label base2disapprove:
    povi "But what's he doing? Deflowering her while she's restraint like a fucktoy?"
    if alexis_revenge == True:
        povi "That damn fucker! She doesn't deserve this!"
    davide "Your tight asshole will love my dick, slut!"
    ls "Hnn..."
    povi "He's deflowering her asshole?!"
    if alexis_revenge == True:
        povi "I wish I could stop it but I'm sure he could beat me to death right now."
        povi "I can't stand against him!"
    davide "There we go, slut!"
    scene basement 2am 003b
    ls "HNNG!"
    scene basement 2am 004b
    davide "All in!"
    ls "HNNG!"
    if alexis_voyeur == True or alexis_sadist == True:
        povi "Damn, did he really go all in with one thrust?"
        povi "Spreading her tight asshole."
    else:
        povi "He's humiliating her. Raping her asshole and she's helpless."
        povi "And even in pain. What did he do to her so she'd let him do that to her? Drugs? Threats?"
    "Davide fucks her faster."
    scene basement 2am 005b
    davide "Perfect. Your tight slut-hole is clinging on my dick!"
    ls "Hnng... hnng..."
    davide "You make me proud. I haven't had such a tight hole since a long time."
    if alexis_revenge == True:
        povi "She's crying! You need to stop asshole!"
    scene basement 2am 006b
    ls "Hnn... hnn..."
    davide "You relaxed yourself now? Good. So I can fuck you faster!"
    povi "She's staring at me again! But I'm not sure what's with her eyes."
    if base2likentr == True:
        povi "Is she sad that I am watching her getting humilated by her \"loving boyfriend\"?"
        if alexis_voyeur == True:
            povi "Haha, but I'm enjoying her performance."
    else:
        povi "Does she want me to rescue her from this humiliation?"
        if alexis_revenge == True:
            povi "But I can't. Please be strong [ls]."
        else:
            povi "But that's the opposite of what I want to do."
    scene basement 2am 007b
    ls "Hgg... hgg..."
    if base2likentr == True:
        povi "Damn, he's plugging her so hard that she's about to faint."
        if alexis_voyeur == True:
            povi "This must be really a good fucking."
    else:
        povi "He's raping her so hard that she's about to faint!"
        if alexis_revenge == True:
            povi "Stop it! You'll break her!"
        else:
            povi "Got to keep it going!"
    davide "AH! I'm cumming, slut! I'll mark you as mine!"
    ls "HGGG!"
    scene basement 2am 008b
    ls "Hnn... hnn..."
    davide "Look at this mess. It's so much, it's spraying out of your tight hole!"
    if base2likentr == True:
        if alexis_voyeur == True:
            povi "He really marked her!"
        else:
            povi "That asshole really marked her!"
    else:
        povi "She's so humiliated! Being used like a fucktoy."
    davide "I can't wait to wide it even more next time."
    scene black
    "Davide unties [ls]."
    scene basement 2am 009b
    if base2likentr == True:
        ls "Did I do well? Are you satisfied with me, lover?"
        davide "Hm... so, so. It could be still better..."
        ls "But I really tried."
        povi "Damn, even now he's telling her how he wants her to be."
        if alexis_ntr == True:
            povi "And she's already fallen for his bullshit."
    else:
        ls "Are we done now? I can go now, you won't hurt anyone right?"
        davide "Hm... you were only so, so. It could be still better..."
        ls "But I really tried."
        if alexis_revenge == True:
            povi "God damn him! Using drugs and threats of violence. I'm going to kill him, I swear!"
            povi "She did nothing to deserve this. No one deserves this."
        else:
            povi "God damn! Using drugs and threats of violence. I will be doing all of that too!"
            povi "She did nothing to deserve this. No one deserves this. That's what makes it so great."
    scene basement 2am 013a
    if base2likentr == True:
        if alexis_voyeur == True:
            povi "And that tight ass pressing his cum out. What a hot view!"
        else:
            povi "And that tight ass pressing his cum out. I can't do anything to help her, he's just so huge!"
        davide "Well if you give your best, you can be a good ass-slut in no time!"
        ls "Then... I'll try..."
    else:
        if alexis_revenge == True:
            povi "He stole her innocence! He must die, soon!"
        else:
            povi "He stole her innocence... That's my job."
        davide "Well if you give your best, you can be a good ass-slut in no time!"
        ls "I don't want..."
    scene basement 2am 010b
    if base2likentr == True:
        ls "Trust me lover, I'll be the best ass-slut!"
        povi "Did she liked it that much or does she just want to do everything for her \"boyfriend\"?"
        davide "Oh with me training you, you'll be one in no time, haha."
        ls "Good, my lover...<giggle>"
    else:
        ls "I'll try better..."
        povi "He already broke her. Brainwashed her with that \"slut-shit\"! It's got to tbe the drugs and the threats!"
        davide "Oh with me training you, you'll be one in no time, haha."
        ls "And then no one get's hurt?"
    scene basement 2am 011b
    if base2likentr == True:
        ls "I'll be the best girlfriend ever for you."
        davide "I would recommend the best slut ever!"
        ls "Then I'll be the best slut ever!"
        if alexis_voyeur == True:
            "Fascinated by the work Davide did to her, you leave them alone."
        else:
            "Horrified by what she and Davide did together behind your back, you leave them alone."
    else:
        povi "Yeah, definitely drugged. She acts so weird on them."
        ls "I'll save them!"
        davide "Exactly, you're a hero that fights with her body!"
        ls "...hero?"
        "Shocked about what you saw you wait until she leaves and then you sneak out after her."
    $ base2likentr = False
    $ base2amalexisntrfirst = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    if NTR == True and momrelationship <= 5 or hardntr == True:
        jump kitchen2am
    elif meet4am == True:
        $ dtime = 4
        scene black
        "You woke up."
        povi "It's 4am. I should meet with [ls]."
        jump base4amal
    if hardntr == False:
        jump stats
    elif hardntr == True:
        jump statshard

label base4amal:
    $ showbasealfirst = True
    scene basement 4am 001
    "You see [ls] waiting eagerly."
    ls "So what is it? Show me!"
    pov "We're going to go into the basement now."
    scene basement 4am 002
    if basealefirst == True:
        ls "But that isn't something special, we've been there already."
        pov "Oh but this time will be special, because we're going to use another way to get in."
        ls "Another way?"
    else:
        ls "Are you kidding me?! How are we going to get in?"
        pov "I'll show you."
    "You unlock the basement door with your key."
    scene basement 4am 003
    ls "Wow! You opened it."
    pov "Yes, the secret room is not secret now!"
    ls "So does this mean you're a gang-member now?"
    pov "Yes, I'm a member now, haha."
    scene basement 4am 004
    ls "Are you really a gang member now. Or did you just steal the key?"
    pov "No, I'm serious. I'm part of the gang now."
    pov "But if you don't believe me, we don't have to do this and you can go back to bed."
    scene basement 4am 005
    ls "No, I believe you! And I don't want to miss this chance."
    pov "Ok then, but we still need to be silent."
    if inc == True:
        ls "And besides, my big brother wouldn't lie to me, would he?"
    else:
        ls "And besides, you wouldn't lie to me, would you?"
    pov "Never, haha."
    scene basement 4am 006
    ls "I'm so special, lalala..."
    pov "What you're doing? Have you gone crazy?"
    ls "<giggle> I'm in the super secret hideout!"
    povi "She's enjoying this a little too much. Haha."
    scene basement 4am 007
    ls "It's just so cool to be here with you. And mom doesn't even know, so I don't get in trouble."
    pov "Yes but we need to keep it that way or we will be in very big trouble."
    if inc == True:
        ls "So my big brother becomes a gang member and the first thing he does is show me the secret hideout..."
    else:
        ls "So you become a gang member and the first thing you do is show me the secret hideout..."
    ls "I feel so special! That means I beat [bs] too!"
    pov "Why is that?"
    ls "She isn't allowed to go down here. <giggle>"
    scene basement 4am 008
    ls "And look at that, a blue drink, so cool."
    pov "You think you're old enough to start drinking yet?"
    ls "Haha, maybe?"
    povi "She's so happy now."
    scene basement 4am 009
    ls "So blue!"
    if basenicfirst == True:
        if inc == True:
            povi "The same as mom, head over heels for a blue drink."
        else:
            povi "The same as [mother], head over heels for a blue drink."
    pov "Don't drink too much or you'll get drunk and we're sure to get caught."
    ls "Don't worry... so blue..."
    scene basement 4am 010
    "She turns around."
    pov "Take care of your drink."
    ls "<giggle> I was thinking..."
    pov "What?"
    ls "There's a changing room..."
    pov "Oh and what's your idea now?"
    povi "I have a good feeling about this."
    scene basement 4am 011
    ls "I want to try something."
    pov "OK. But be careful and don't ruin anything."
    ls "Haha, I'm not stupid."
    pov "Fine."
    ls "I'll surprise you!"
    povi "Or should I help her pick something while she's with me?"
    call screen base4amchoose

screen base4amchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('base4amchoose'), Jump('base4amcor')) hovered tt.Action ("Choose for her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('base4amchoose'), Jump('base4amlove')) hovered tt.Action ("Let her choose [lv1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base4amcor:
    $ lilsiscorruption += 1
    pov "How about I choose something for you?"
    scene basement 4am 012c
    ls "But why? I can do by myself."
    pov "I brought you here with me, even though we could get in trouble if they caught us."
    pov "So I think it's only fair to let me pick something nice for you this time."
    pov "Don't you think that's fair, my special girl wearing the special outfit I pick?"
    ls "Hm... OK."
    pov "And I think there is some makeup in there too. It is a special occasion after all."
    ls "Ok, I'll do it for you."
    scene basement 4am 013
    "You choose something for her."
    ls "This one, but..."
    pov "Just try it on, you might like it. And if you do I have something else for you."
    ls "Something else?"
    pov "Yes it's special as well."
    povi "Maybe it's time to test the sex-drug on her?"
    scene basement 4am 014c
    pov "Wow!"
    if inc == True:
        ls "I feel a little uncomfortable in this, brother."
    else:
        ls "I feel a little uncomfortable in this, [pov]."
    pov "But you look very sexy."
    ls "Hnn..."
    scene basement 4am 015c
    if inc == True:
        pov "I can't believe I have such a hot lil sister."
    else:
        pov "I can't believe that you're so hot, [ls]."
    ls "Why are you talking like that now?"
    pov "Because it's true. You should wear this outfit more often around me."
    ls "Hnn..."
    pov "Now turn around and let me see the back."
    ls "O... OK."
    scene basement 4am 016c
    pov "Ihat is even better."
    ls "What do you mean?"
    pov "You look even hotter from behind."
    ls "Please stop that..."
    pov "But it's true."
    scene basement 4am 017c
    ls "I think we should stop now. You're being so weird."
    pov "Haha, relax [ls]."
    pov "Did you forget the other special thing I have for you?"
    ls "Well, what is it?"
    pov "A very delicious candy."
    scene basement 4am 018cc
    ls "Did you say candy?"
    pov "Yes and I think you can have it now, because you did so well in doing what I wished."
    ls "So you're just playing with me?"
    pov "Haha, you want the candy now?"
    ls "Yes please give it to me."
    pov "Fine. Open your mouth."
    scene basement 4am 019cc
    ls "But why don't you just give me it?"
    pov "You want it or not?"
    ls "OK. Please give me the candy."
    povi "I'm so excited. How will she react? And what can I do with her, after the effects kick in?"
    scene basement 4am 020cc
    ls "Ohh... this does taste good."
    if inc == True:
        ls "Thank you so much, big brother."
    else:
        ls "Thank you so much, [pov]."
    pov "You're welcome."
    povi "I'm sure you'll thank me later in other ways too."
    ls "<giggle> You're so nice."
    scene basement 4am 020c1c
    ls "Something feels funny."
    pov "What is it?"
    ls "I'm feeling... so hot..."
    povi "Oh it started working already. Good."
    ls "And there's another weird feeling."
    pov "Can you describe it?"
    ls "It's like a tickle."
    povi "So the drug is working. Now I need a way to test it."
    pov "I have an idea, I'll can do a check up on you."
    ls "A check up?"
    pov "Yes like a doctor. Trust me, it'll make you feel better."
    ls "..."
    if inc == True:
        pov "I'm your big brother, I know what's good for you."
    else:
        pov "I'm your older friend, I know what's good for you."
    pov " Come with me."
    scene basement 4am 021cc
    ls "I don't get why you stuck me in this thing."
    pov "You said you have a tickle. It's to protect me so you can't kick me accidentally."
    ls "<giggle> So you need to be careful."
    povi "So does the drug make people act dumb, or just more comfortable in certain situations?"
    pov "Ok, I'll check your other side now, but you need to stay quiet, no matter what happens."
    pov "We really don't want to get caught now."
    ls "Ok, you can do it [pov]."
    povi "Yes I can, haha."
    scene basement 4am 022cc
    povi "Laying there all helpless before me."
    povi "Let's see what this drug will do for you now."
    povi "I can't wait."
    "You remove her panties."
    scene basement 4am 023cc
    if inc == True:
        ls "Did something just happen, brother?"
        pov "Why you asking?"
        ls "I feel a little exposed."
        pov "Don't worry, everything is alright, lil sis."
    else:
        ls "Did something just happen, [pov]?"
        pov "Why you asking?"
        ls "I feel a little exposed."
        pov "Don't worry, everything is alright, [ls]."
    pov "She's already wet. Let's see how her body react."
    scene basement 4am 024cc
    "You touch her clit."
    ls "Hnn..."
    ls "Why you're touching me there?"
    pov "I need to find out where you feel the tickle."
    pov "Now be a good girl and stay silent."
    ls "OK. Hnn..."
    povi "Damn, that's almost too easy. She's acting like a doll."
    scene basement 4am 025cc
    ls "Hah..."
    pov "Sshh..."
    ls "Hnng..."
    povi "Her pussy is tight. I can still feel her hymen."
    povi "Maybe it's time to help her break it. With the sex-drug she's sure to enjoy her first time."
    scene basement 4am 026cc
    povi "And she's so damn wet. This drug is very strong. I'll have so much fun with her."
    povi "Let's try something else now."
    scene basement 4am 027cc
    ls "Hah, your finger is... inside me."
    pov "Yes I need to check everywhere."
    if lsispronanal >= 4:
        ls "So deep inside me."
        povi "Her asshole is clinging on my finger."
        povi "Looks like she really enjoyed the anal porn I showed her."
        ls "Hnng..."
        povi "She even don't try to push me out. More like she's sucking me in."
        povi "Maybe this is would be better hole to play in tonight."
    scene basement 4am 028cc
    povi "That gap."
    if lsispronanal >= 4:
        povi "She's already masturbated to anal porn. Her hole is already somewhat elastic."
        povi "I wonder what she shoves into it to have fun."
    scene basement 4am 029cc
    "You also uncover her tits."
    ls "You're already done...?"
    povi "Wow, did she hope for some more?"
    pov "No, I'm just thinking for a second."
    ls "Please make that tickle feeling go away some more."
    if inc == True:
        ls "Help me, big brother."
        povi "I can't believe it. My little sister is asking me to do naughty things with her."
    else:
        ls "Help me [pov]."
        povi "I can't believe it. [ls] is asking me to do naughty things with her."
    povi "So, what to do to help her?"
    call screen base4amcorchoose

screen base4amcorchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base4amcorchoose'), Jump('base4amcorpussy')) hovered tt.Action ("Deflower her pussy") focus_mask True
        if lsispronanal >= 4:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base4amcorchoose'), Jump('base4amcorass')) hovered tt.Action ("Deflower her asshole") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base4amcorchoose'), Jump('base4amcorbj')) hovered tt.Action ("Use her mouth") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base4amcorpussy:
    povi "I think it's time to deflower her. I can't wait any longer!"
    if inc == True:
        pov "I'll help you in a very special way now, lil sis."
    else:
        pov "I'll help you in a very special way now, [ls]."
    pov "Just try to relax and trust me."
    ls "Yes, please help me."
    scene basement 4am 030ccp
    "You push your the tip of your dick slowly into her."
    ls "Hnn... you want to go inside me..."
    if inc == True:
        pov "Yes it's time, lil sis."
    else:
        pov "Yes it's time, [ls]."
    ls "Your penis is so hot."
    povi "Wow, she's so horny and willing."
    pov "I'll deflower you now and then you'll feel much better."
    if inc == True:
        ls "Yes... deflower me... brother."
    else:
        ls "Yes... deflower me... [pov]."
    povi "Damn."
    "You push deeper slowly."
    with vpunch
    "BOOM!"
    pov "What the hell?"
    mom "Ouch!"
    dad "Everything alright?"
    scene basement 4am 031ccp
    povi "This can't be happening right now."
    mom "Did you leave the light on in the basement?"
    dad "No, I don't think so."
    mom "I'll check!"
    dad "Wait a second, you're too drunk and could fall, I'll be down there in a bit anyway. I'll check then."
    $ meet4am = False #----- Might not be needed -----
    jump base4amcorpussygo_landing

label base4amcorass:
    povi "I need to penitrate that asshole now. I can't wait any longer!"
    if inc == True:
        pov "I'll help you in a very special way now, lil sis."
    else:
        pov "I'll help you in a very special way now, [ls]."
    pov "Just try to relax and trust me."
    ls "Yes, please help me."
    scene basement 4am 030cca
    "You push the tip of your dick in her asshole."
    ls "Hnn... You want to go in my asshole."
    if inc == True:
        pov "Yes it's time, lil sis."
    else:
        pov "Yes it's time, [ls]."
    pov "You now already much about it."
    ls "Your penis is so hot."
    povi "Wow, she's so horny and willing."
    pov "I'll take your asshole now and then you'll feel much better."
    ls "My asshole... hah..."
    scene basement 4am 032cca
    "You go deeper slowly."
    ls "Hnng... it's so thick."
    pov "And your tight hole is clinging to me so tightly."
    pov "You waited for this, didn't you?"
    ls "I... yes..."
    pov "Just masturbating about it and playing with your fingers isn't enough."
    if inc == True:
        ls "Yes brother, hah... please do more."
    else:
        ls "Yes [pov], hah... please do more."
    scene basement 4am 033cca
    "You push your dick almost all the way in."
    ls "Hnng... hnng..."
    if inc == True:
        pov "You feel your brother's dick deep inside your asshole?"
        ls "Yes, it's so hot. It's burning me up, brother."
    else:
        pov "You feel my dick deep inside your asshole?"
        ls "Yes, it's so hot. It's burning me up, [pov]."
    pov "I'll start to move now and really fuck you!"
    ls "O... OK. Hnng..."
    scene basement 4am 034cca
    "You fuck her in her asshole."
    ls "Hah... ahhh... hah"
    pov "You like to get fucked in your asshole?"
    ls "Yes... yes, more... please more."
    pov "Then I'll help you to feel even better."
    scene basement 4am 036cca
    "You play with her clit too."
    ls "Hah... hnn... it's so good."
    pov "I'm glad you like it."
    ls "More... please more..."
    povi "She's at her limit, so it's time that I mark her hole for me too."
    pov "You'll cum soon, I want to put my sperm in your asshole too."
    if inc == True:
        ls "Yes brother, hah... put your sperm in me..."
    else:
        ls "Yes [pov], hah... put your sperm in me..."
    povi "Damn, now I know why this drug is so special."
    pov "HNG!"
    "You spray your sperm in her asshole!"
    scene basement 4am 037cca
    ls "I'm... hah... cumming..."
    if inc == True:
        ls "I'm cumming from your dick brother!"
    else:
        ls "I'm cumming from your dick [pov]!"
    pov "Good girl!"
    ls "Hnng... hnng..."
    pov "You're such a very good fuck."
    "You pull your dick out."
    scene basement 4am 038cca
    povi "Look at this mess. Her asshole gaping with my cum dripping out."
    ls "Hnng... hnn..."
    pov "I came so much inside you [ls]."
    ls "Yes I can feel it in me, hah... so hot..."
    "You release her."
    scene basement 4am 040cca
    ls "Hah, hnng..."
    pov "What's wrong [ls]?"
    pov "Did you hurt yourself?"
    ls "My legs are so weak. I can't stand up."
    povi "Damn, that ass-fucking wore her out."
    pov "I'll help you."
    scene basement 4am 041cca
    "You hold her."
    pov "You liked it so much that you're done now?"
    ls "It was so intense!"
    if inc == True:
        pov "So the first time having sex with your brother was a good for you too?"
    else:
        pov "So the first time having sex with me was a good for you too?"
    ls "Y... yes, I liked it a lot!"
    pov "But why are you making that face then?"
    ls "I'm... so tired..."
    pov "Oh, I see."
    pov "I'll bring you back to your bed."
    scene black
    "You bring her to her bed and go back to sleep also."
    $ meet4am = False
    jump skip

label base4amcorbj:
    povi "I want to have fun with her mouth. I can't wait any longer!"
    if inc == True:
        pov "I'll help you in a very special way now, lil sis."
    else:
        pov "I'll help you in a very special way now, [ls]."
    pov "Just try to relax and trust me."
    ls "Yes, please help me."
    scene basement 4am 030ccm
    ls "You want to help me with your penis?"
    pov "Yes I'll stick it in your mouth and it'll help you."
    ls "I don't know."
    if inc == True:
        pov "Just trust me, lil sis."
        ls "OK, brother."
    else:
        pov "Just trust me, [ls]."
        ls "OK, [pov]."
    scene basement 4am 031ccm
    pov "Here, taste it first."
    ls "OK, hm..."
    pov "Yes use also your tongue on it."
    ls "<lick>"
    if inc == True:
        pov "Hng... you're doing very good, lil sis."
    else:
        pov "Hng... you're doing very good, [ls]."
    scene basement 4am 032ccm
    "You hold her head so you can push your dick deeper in."
    ls "Hmpf..."
    pov "Good, suck more on it."
    ls "<suck> <lick>"
    pov "You're doing very good and I bet the tickle feeling is also gone."
    ls "Hnn... yesh..."
    scene basement 4am 033ccm
    pov "Just a little more."
    ls "Hmpf! <choke>"
    pov "It's almost a real deepthroat."
    if inc == True:
        pov "You're doing so good, lil sis."
    else:
        pov "You're doing so good, [ls]."
    ls "<choke> Hnng..."
    "You start to fuck her mouth."
    pov "This is the right thing to cure you."
    scene basement 4am 034ccmm
    ls "Hnng... hnng..."
    pov "Oh, I'm about to cum."
    if inc == True:
        pov "Swallow it all, lil sis."
    else:
        pov "Swallow it all, [ls]."
    ls "HNNG! <choke>"
    pov "HNG! Yes!"
    "You spurt your sperm down her throat."
    ls "<gulp> <gulp>"
    pov "Good, drink it all down."
    scene basement 4am 035ccmm
    ls "Bleh!"
    pov "Was that a little too much?"
    ls "Yes... I could barely swallow it all."
    povi "Oh, she isn't even upset. The drug must make all sexual actions better."
    if inc == True:
        pov "You liked it, getting your brother's sperm?"
    else:
        pov "You liked it, getting my sperm?"
    ls "Yes... so thick..."
    scene basement 4am 036ccm
    pov "Everything alright, you look so weird."
    ls "My jaw hurts..."
    pov "Oh that'll get better. You just need more training."
    ls "More training?"
    pov "Yes it won't hurt anymore when I fuck your mouth more often."
    ls "You want to fuck my mouth more often?"
    pov "Yes it was very good."
    scene basement 4am 037ccm
    if inc == True:
        ls "Then you can do it, brother. When I help you feel good, I feel good too."
    else:
        ls "Then you can do it, [pov]. When I help you feel good, I feel good too."
    pov "You could even become my personal cum-dumpster if you want!"
    ls "Cum-dumpster? <giggle>"
    povi "Damn, she's just going along with anything I say. If someone else used it, they could do this with her too."
    povi "I need to make sure no one else uses the drug on her!"
    pov "Yes, but that's enough for now, we should back. We'll have more fun next time."
    ls "Ok. Let's go."
    scene black
    "You go back to your rooms."
    $ meet4am = False
    jump skip

label base4amlove:
    $ lilsislove += 1
    pov "Then surprise me."
    scene basement 4am 013
    ls "Let's see."
    povi "I wonder what she'll choose?"
    povi "Maybe I'll be lucky and it's something really hot."
    scene basement 4am 014l
    ls "Nice, isn't it?"
    pov "Oh yes, it's beautiful."
    ls "I loved it at first sight!"
    if inc == True:
        pov "It's looks really good on you, lil sis."
    else:
        pov "It's looks really good on you, [ls]."
    scene basement 4am 015l
    povi "Damn, this thing is so transparent."
    povi "I can almost see her nipples. That's damn sexy."
    if inc == True:
        ls "Are you done inspecting me, brother?"
    else:
        ls "Are you done inspecting me, [pov]?"
    pov "Almost."
    scene basement 4am 016l
    ls "That fabric is incredible soft. I'm in love with it."
    pov "Hmm..."
    ls "Is something wrong?"
    call screen base4amlovechoose

screen base4amlovechoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('base4amlovechoose'), Jump('base4amlovetell')) hovered tt.Action ("Tell her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('base4amlovechoose'), Jump('base4amlovemute')) hovered tt.Action ("Don't tell her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base4amlovetell:
    pov "[ls]?"
    ls "What is it?"
    pov "That top is pretty transparent. I almost can see your nipples."
    scene basement 4am 017la
    ls "I know."
    pov "What? You know?"
    ls "Yes, but you understand how much I like this thing, right? It's so soft."
    pov "So you don't care that I can see you?"
    ls "You can't see much, the pattern hides a lot. But I love this thing anyway."
    pov "Yes, you mentioned that."
    ls "Are you making fun of me?"
    pov "No."
    jump base4amlovemute

label base4amlovemute:
    pov "..."
    ls "You want to see my back now?"
    pov "Sure."
    scene basement 4am 017l
    pov "Oh that's also beautiful."
    ls "I like it too."
    scene basement 4am 018l
    povi "Damn, that panties are also transparent. And so hot."
    pov "Those panties look really good on you, [ls]."
    ls "Thank you [pov]."
    scene basement 4am 018la
    ls "So I made a good choice?"
    pov "Not just a good choice, a very good choice."
    ls "<giggle> I'm glad that you like it too."
    povi "You have no idea."
    scene basement 4am 019l
    ls "I should thank you for bringing me here so I could find this little treasure."
    pov "Oh so you're in love with that outfit then?"
    ls "Yes and I plan to keep it. Sleeping in this thing would be the best thing ever."
    pov "But you can't!"
    ls "Why not?"
    pov "They'll notice it's gone and then suspect someone was here."
    scene basement 4am 020l
    if inc == True:
        ls "But wouldn't it be a nice present for the best sister ever?"
        pov "I don't think that's a good idea, lil sis."
    else:
        ls "But wouldn't it be a nice present for the best childhood friend ever?"
        pov "I don't think that's a good idea, [ls]."
    ls "So it's decided. Thank you for the outfit!"
    pov "No! I said you have to leave it here. You just can't keep it."
    ls "And what happens when I go back to my room now with the outfit?"
    pov "I get in trouble with the gang or something worse."
    scene basement 4am 021l
    ls "So you're scared now?"
    pov "What?"
    if inc == True:
        ls "Because your fate is in your little sisters hands now!"
    else:
        ls "Because your fate is in my hands now!"
    pov "You got to be kidding me..."
    ls "You're my victim now! Let's see what I'm gonna do with you."
    pov "Hahaha..."
    scene basement 4am 022l
    "She jumps on you."
    if inc == True:
        ls "So you have to be a nice brother now or you'll get into trouble."
    else:
        ls "So you have to be a nice friend now or you'll get into trouble."
    pov "I give up. Show mercy, haha."
    ls "Good, you've accepted your fate."
    scene basement 4am 023l
    ls "<kiss>"
    pov "Ohh..."
    ls "<kiss> <giggle>"
    scene basement 4am 024l
    ls "<kiss> <kiss>"
    povi "Oh she climbed on top of me and french kissing me. This has gotten her very excited."
    ls "<kiss> Hnn..."
    "You play with her tongue."
    scene basement 4am 025l
    ls "<giggle>"
    ls "I would never hurt my weak little dummy."
    pov "Oh, so I'm weak now, haha."
    ls "Yes, giving up so quickly like that."
    pov "Maybe I tricked you."
    scene basement 4am 026l
    pov "Counterattack!!"
    ls "Huh?"
    pov "<kiss>"
    ls "Hah..."
    "You kiss over her chest."
    ls "Hnn... hah... you dummy..."
    povi "She's in the mood for more."
    scene basement 4am 027l
    pov "<kiss>"
    "You kiss her nipple through the transparent top."
    ls "Hah... Hnn..."
    povi "Her nipples gotten all hard."
    pov "<kiss> <lick>"
    ls "Hnng... hah..."
    scene basement 4am 028l
    ls "Hah... hah..."
    pov "So I understand your plan now."
    ls "My, plan? Hnn..."
    "You pinch her nipple gently."
    ls "Aahh..."
    pov "Calling me weak so I have to show you that I'm not."
    ls "I... hah..."
    if inc == True:
        pov "Your nipples are all hard, lil sis."
    else:
        pov "Your nipples are all hard, [ls]."
    pov "So you liked my counterattack."
    ls "Your... hah..."
    pov "But don't worry, we're not done now."
    pov "And I'm sure you want me to go on..."
    scene basement 4am 029l
    pov "First let me explore your body more."
    ls "Hah... your hand..."
    "You go lower."
    ls "Your hand is going... hah..."
    pov "Should I stop? Maybe I'm going to far for you?"
    if inc == True:
        ls "No brother. Please attack me more, hah..."
        pov "As you wish, lil sis."
    else:
        ls "No [pov]. Please attack me more, hah..."
        pov "As you wish, [ls]."
    scene basement 4am 030l
    "You reached her pussy."
    pov "You're so wet."
    ls "I...know... hah..."
    pov "You sure that you want me to do more?"
    ls "Yes... please..."
    "You start to rub her clit through her panties."
    ls "Hnn... hah..."
    pov "That outfit revealed much more than skin you know. I know the real reason you wanted to wear it."
    ls "What... hah... do you mean?"
    pov "You wanted to be sexy for me."
    ls "Hnn... hah..."
    pov "Please tell me, I want to know if I'm right."
    ls "Yes! I wanted you to see me as a sexy girl."
    pov "I'm very happy now. You want even more?"
    ls "Yes, please more. I'm so close!"
    pov "Then enjoy yourself."
    scene basement 4am 031l
    ls "AAAHHH... HAAH..."
    if inc == True:
        ls "Brother, hah... hah..."
    else:
        ls "[pov], hah... hah..."
    povi "She's having a orgasm from me."
    ls "Hnn... hnn..."
    scene basement 4am 032l
    ls "Hah... hah..."
    pov "Are you ok with all of this?"
    ls "Stop talking, just hold me."
    pov "OK. then I'll hol..."
    if inc == True:
        ls "I love you, brother!"
    else:
        ls "I love you, [pov]!"
    pov "Oh, I understa..."
    if inc == True:
        ls "But I love you, brother!"
        pov "Oh. I love you too, lil sis!"
    else:
        ls "But I love you, [pov]!"
        pov "Oh. I love you too, [ls]!"
    scene basement 4am 033l
    pov "That was a little intense. Are you sure you're alright?"
    ls "Yes... it was just so good."
    pov "Yes and it was. I'm happy I could do that for you."
    ls "You know why I wanted to do this with you?"
    pov "Yes you did this because you love me."
    if inc == True:
        ls "Yes I love you so much, brother!"
    else:
        ls "Yes I love you so much, [pov]!"
    scene basement 4am 034l
    "She pushes you so you fall down."
    pov "What?"
    ls "It's your turn."
    pov "My turn?"
    ls "Now I'll make you feel good too."
    pov "Oh... Ohh!"
    ls "<giggle> Let me see your thing."
    scene basement 4am 035l
    if inc == True:
        ls "Oh, your penis is so big, brother."
    else:
        ls "Oh, your penis is so big, [pov]."
    pov "Then take your time, I don't want you to get hurt."
    ls "So... big..."
    pov "[ls]?"
    scene basement 4am 036l
    ls "Oh, I was just thinking of something. <giggle>"
    pov "What you want to do with my penis?"
    ls "Yes! <giggle>"
    pov "Right now?"
    ls "Maybe...?"
    pov "You'll surprise me."
    ls "Yes, you'll like it."
    scene basement 4am 037l
    if inc == True:
        ls "You like my massage, big brother?"
    else:
        ls "You like my massage, [pov]?"
    pov "Yes, you're hands are very soft."
    ls "Then enjoy it as much as you can. I want to return the good feeling you gave me."
    pov "Oh I will, don't worry."
    ls "<giggle>"
    povi "Damn, that is more I could wished of. I'll cum in no time."
    scene basement 4am 038l
    ls "<kiss>"
    pov "Damn!"
    ls "<giggle> It's twitching so hard, maybe another kiss to calm it down."
    ls "<kiss>"
    pov "That's too much!"
    scene basement 4am 039l
    pov "HNNG!"
    ls "Huh?"
    pov "That... was... so good..."
    ls "I see, you came."
    scene basement 4am 040l
    ls "I'm happy now that we both had a good time."
    pov "Me too."
    ls "So can I keep my outfit now? <giggle>"
    pov "I'm afraid not. It's just to risky. But I can buy you one."
    ls "Great, then we can have more good times together."
    pov "Haha, oh yes."
    ls "It's late, should we got back?"
    if inc == True:
        pov "Yes. and lil sis?"
        ls "Hm...?"
        pov "I love you!"
        ls "Aww... I love you too, big brother."
    else:
        pov "Yes, and [ls]?"
        ls "Hm...?"
        pov "I love you!"
        ls "Aww... I love you too, [pov]."
    scene black
    "You leave the basement together."
    $ meet4am = False
    jump skip

label casbasement:
    hide screen locations
    scene kitchen 9am 020
    if inc == True:
        bs "Hey there sweet brother of mine!"
    else:
        bs "Hey there sweet [pov]!"
    povi "Huh? What's up with her? What is with all that sweet-talk?"
    pov "What's up?"
    bs "I heard you're a gang member now."
    pov "Yes..."
    if bigsiscorruption >= bigsislove:
        scene kitchen 9am 009rc
    else:
        scene kitchen 9am 006rl
    bs "So can I be part of the gang with you?"
    bs "You know that I've wanted this for so long, right?"
    povi "And now the sweet-talk makes sense."
    pov "Hmm..."
    if inc == True:
        bs "Please, you'd be the best brother ever!"
    else:
        bs "Please, you'd be the best friend ever!"
    povi "Is it the time to let her join too or should I make her wait some time longer?"
    call screen casbasementallow

screen casbasementallow():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('casbasementallow'), Jump('casbasementallowyes')) hovered tt.Action ("Let her join") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('casbasementallow'), Jump('casbasementallowno')) hovered tt.Action ("Not now") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label casbasementallowno:
    pov "No, it's to soon."
    bs "But why?"
    pov "You'll get your chance another time."
    bs "Hnn..."
    scene black
    $ dtime += 1
    jump kitchen

label casbasementallowyes:
    pov "OK."
    bs "Really?"
    pov "Yes."
    scene kitchen 9am 021
    bs "Thank you so much."
    pov "But we'll go right now so I can show you everything."
    pov "And it'll be our secret for the time being, until I figure when the best time to reveal this to the others."
    bs "They're all out of the house right now."
    pov "Yep, so let's go."
    if bigsiscorruption >= bigsislove:
        scene kitchen 9am 009rc
    else:
        scene kitchen 9am 006rl
    bs "But I'm still in my underwear."
    pov "There are clothes down there, you can wear something from there."
    bs "Oh, really?"
    pov "Yes, let's go. It's now or never."
    scene kitchen 9am 021
    bs "OK."
    scene black
    "You go to the basement together."
    scene basement 9am 001
    bs "Wow, I can't believe it. I'm in the basement!"
    bs "But it's a little weird down here, with that \"punishment\" corner."
    pov "I'll tell you about that later. I don't know if you're like it or not though."
    bs "Oh..."
    bs "And where are the clothes you mentioned?"
    pov "Back there."
    scene basement 9am 002
    pov "You can change in that little room. I'm sure you'll like that part, there are a ton of different outfits in there."
    bs "So can I choose something?"
    call screen casbaseoutfitchoose

screen casbaseoutfitchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1: #----- Only used the first time ----- Custom Repeat Menu Created -----
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('casbaseoutfitchoose'), Jump('casbasementlove')) hovered tt.Action ("Yes, choose one you like") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('casbaseoutfitchoose'), Jump('casbasementcor')) hovered tt.Action ("No, I'll choose one") focus_mask True
        if basecasfirst == True and bigsiscorruption >= 50: #---- Original -----
            imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('casbaseoutfitchoose'), Jump('casbasementcorfuck_landing')) hovered tt.Action ("No, I'll choose a special one") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label casbasementcor:
    $ bigsiscorruption += 1
    scene basement 9am 003c
    bs "What? But I thought..."
    pov "I just thought it would be a nice way to show me how grateful you are that I made you a part of the gang."
    bs "Hnn..."
    pov "And I'm sure you'll like it too. There're really good things in there."
    bs "O... OK."
    scene black
    "You choose something special for her and she go to change into it."
    scene basement 9am 020c
    bs "You can't be serious."
    pov "Why? You look way sexy in that outfit!"
    bs "I'm almost naked."
    scene basement 9am 021c
    pov "Well sadly, you aren't. Besides, your club outfit is almost the same, so stop complaining."
    bs "But..."
    pov "You wanted me to get you down here and I did. And you get to wear a sexy outfit too."
    pov "So there is no need to be sad."
    bs "Hnn..."
    scene basement 9am 022c
    pov "And you can't deny that you love the attention you'd get in this outfit."
    pov "Seeing your hot long legs in those shoes."
    bs "You want me to wear this thing when others are around?"
    scene basement 9am 024c
    pov "I'm ok with other looking at my girl, so long as they don't touch."
    bs "Hnng..."
    if inc == True:
        pov "And why not show everyone how hot my big sis is?"
    else:
        pov "And why not show everyone how hot you are?"
    pov "Also, it's important to for my girl to obey me..."
    scene basement 9am 023c
    bs "But I'm not your girl!"
    pov "No yet, but soon!"
    if inc == True:
        bs "I'm still your sister!"
    pov "You know that's just a matter of time until you give in and become my girl."
    pov "You want to be part of the gang, become famous, and be with someone that can keep up with you like I can."
    scene basement 9am 025c
    pov "And you know that I can."
    pov "So you can keep denying it if you really want or just admit that I'm right."
    pov "I can handle you much better then your loser boyfriend."
    bs "Hnng..."
    scene basement 9am 026c
    pov "You see the drinks over there? This'll be one of your duties here, serving drinks."
    bs "Serving?"
    pov "Yes that's the role of the women down here. Wearing sexy outfits and serving us."
    povi "And you're be serving me in another way also, but she'll find that out soon enough."
    pov "Now, move your sexy ass there and let's see how you do."
    scene basement 9am 027c
    if inc == True:
        bs "So, mom has to do this when she's here?"
    else:
        bs "So, my mom has to do this when she's here?"
    pov "Yes and she's does it very well, so you'll need to train a bit to be as good as her."
    scene basement 9am 028c
    pov "But I have to prepare some things before she can know that you're a member too."
    pov "So you need to train hard so she has nothing to complain about."
    bs "I... understand."
    povi "Her ass is almost naked. That outfit was a good choice."
    scene basement 9am 029c
    povi "And her long legs in that sexy heels."
    povi "I think she could where these more often."
    scene basement 9am 030c
    bs "So I have to serve drinks to just you or to the other men later too?"
    pov "Oh good, now you're showing some interest."
    pov "We'll see when it's time, but mostly you're my girl, so you'll be serving me."
    bs "Stop that..."
    povi "Ha, she still hasn't realized what is coming."
    scene basement 9am 031c
    povi "That little patch of fabric over her pussy. I can't wait to remove it and put my dick inside her."
    povi "This is making me so horny."
    bs "Stop looking..."
    scene basement 9am 032c
    bs "Stop looking at me like that."
    pov "But you're my girl now. A very good girl, that will soon be a part of our gang, if I decide to let you be."
    pov "Just look at it as a part of your entrance exam."
    bs "Hnn..."
    pov "Now let me show you the main thing about the basement."
    scene basement 9am 034c
    bs "What are these pills? Drugs?"
    pov "Yes, but better. These are sex-drugs!"
    scene basement 9am 035c
    bs "Sex-drugs?"
    pov "Yes. They're for women only. It gives them a strong sex drive."
    pov "They're very popular and we sell them from down here too."
    scene basement 9am 036c
    bs "Well I'm not going take them. You can just forget about it."
    pov "Haha, you really think I need them to have fun with you?"
    bs "What does that mean?"
    pov "I'll make you my girl the normal way, I don't need to \"cheat\"."
    scene basement 9am 037c
    bs "That's a good decision. I won't be your lifeless doll."
    povi "Well, she didn't protest about me making her my girl again. Progress."
    povi "But she'll probably start begging for the drugs when she see them in \"action\"."
    bs "So can we start training now? I still have other things to do today."
    povi "She's back to her ornery self again. Oh well, I'll teach her the lesson she really needs."
    "You walk over to the couch."
    scene basement 9am 038c
    pov "Now it's time to serve me a drink."
    povi "I can't stop staring at her."
    if inc == True:
        povi "I wonder how mom will react when she see her wearing this."
    else:
        povi "I wonder how [mother] will react when she see her wearing this."
    bs "So what you want to drink?"
    pov "Drink?"
    pov "Oh, sure. I think a wine is fine to celebrate your entrance exam."
    scene basement 9am 039c
    povi "Maybe I should skip the whole serving drinks thing and just get to fucking her from behind?"
    povi "What an enormous tease she is in that \"dress\"."
    scene basement 9am 040c
    bs "There's only red wine. Do you like red wine?"
    pov "Yes I do. Among other things!"
    bs "Other things?"
    pov "Hm... Bring the red wine. And you'll need a glass too."
    scene basement 9am 041c
    bs "See? I can do this easy."
    pov "Yes and you look great doing it too."
    bs "Hnng..."
    povi "So what else should I do with her for her entrance exam?"
    call screen casbasementcorchoose

screen casbasementcorchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorchoose'), Jump('casbasementcorbj')) hovered tt.Action ("Use her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorchoose'), Jump('casbasementass')) hovered tt.Action ("Use her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label casbasementcorbj:
    povi "Her blow-jobs are so good... I think it's time for another one."
    "You pull out your dick."
    scene basement 9am 042cb
    bs "What are you doing?"
    pov "Preparing the last step of your exam."
    bs "But..."
    scene basement 9am 043cb
    pov "Come closer, put the try down and serve me like a good girl."
    bs "Hnng..."
    pov "Now that you're my girl, you need to serve me whenever I ask, especially down here."
    pov "And I know that you're eager to show me that your mouth is one of the best reasons to choose you as my girl."
    scene basement 9am 044cb
    bs "Hnn..."
    pov "Oh come on. I know you're only playing at being offended, haha."
    if inc == True:
        pov "I know you much better than you think, big sis."
    else:
        pov "I know you much better than you think, [bs]."
    scene basement 9am 045cb
    bs "Hnn..."
    pov "But it's time to stop playing around and get to work."
    pov "Passing this final step is what you need to do to become a part of the gang."
    pov "And you should be happy that we're doing this while we're alone and the others are not here."
    pov "None of the other guys in the gang would be so... considerate."
    povi "Haha, but that could change very soon, if I choose."
    scene basement 9am 046cb
    pov "How about you show me a little of that excitement you had before?"
    pov "Look, you don't have to do this if you really don't want to. But if you become a part of the gang, the other might do worse, if you're not \"my\" girl."
    bs "Hnn..."
    pov "Show me that I made a good decision here. If you want to become my girl... tell me. Otherwise we'll just call it a day, it's ok."
    bs "I..."
    if inc == True:
        bs "I want to suck your dick, brother. I want to be your girl."
    else:
        bs "I want to suck your dick, [pov]. I want to be your girl."
    pov "Good girl. You can start when you want."
    scene basement 9am 047cb
    pov "I love your warm hands on my dick."
    bs "Hmm..."
    povi "I can't wait to feel her tongue again."
    scene basement 9am 048cb
    bs "<suck> <lick>"
    pov "Yes, that's good."
    if inc == True:
        povi "Now it's time to let my big sister prove that she can give the best blow-jobs."
    else:
        povi "Now it's time to let her prove that she can give the best blow-jobs."
    scene basement 9am 049cb
    bs "Hah... <lick>"
    povi "Oh, she opening her mouth wider to give her tongue more space to play."
    if inc == True:
        pov "Your tongue is the best, big sis."
    else:
        pov "Your tongue is the best, [bs]."
    if deepthroatcount >= 2: #----- if casbjdt >= 2: -----
        jump casbasementdp
    bs "<giggle> I know."
    scene basement 9am 050cb
    pov "Yes, lick it just like that. That's a good girl."
    bs "Hmm... <lick> <lick>"
    pov "You're handling my dick even better with the time."
    pov "I bet you don't put in so much effort when you did this with your boyfriend."
    bs "Hnng..."
    pov "Well, soon to be ex-boyfriend, right?"
    scene basement 9am 051cb
    bs "<suck>"
    pov "Haha, nice trick to avoid saying anything. I can appreciate that."
    bs "Hmm..."
    scene basement 9am 052cb
    pov "Oh you stopped..."
    bs "You know why. <giggle>"
    pov "See, there is another reason why you have to be my girl."
    pov "You know exactly when I'm at my limit and need to cum."
    bs "Yes, now where do you want me to take it."
    povi "Holy shit, she's getting into it!"
    if inc == True:
        pov "You being such a good girl now, big sis."
    else:
        pov "You being such a good girl now, [bs]."
    $ deepthroatcount += 1
    call screen casbasementcorcum

screen casbasementcorcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorcum'), Jump('casbasementcorcumf')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorcum'), Jump('casbasementcorcumm')) hovered tt.Action ("Cum in her mouth") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label casbasementcorcumf:
    $ casbasecumface = True
    pov "I want to spray it on your face."
    if inc == True:
        bs "Ok, brother."
    else:
        bs "Ok, [pov]."
    "She rubs your dick furiously."
    pov "Hah, so good."
    scene basement 9am 053cbo
    pov "Hnng..."
    bs "Hmm..."
    "You cum on her face."
    scene basement 9am 054cbo
    bs "Hnn... are you satisfied now?"
    pov "Yes, my girl. You served me good."
    bs "Hnng..."
    povi "Ha, she still not used to it when I call her that."
    pov "Don't wipe it off... Good girls wear their man's cum with pride!"
    bs "Hmm..."
    jump casbasementcorend

label casbasementcorcumm:
    $ casbasecummouth = True
    pov "I want you to taste my sperm."
    if inc == True:
        bs "Ok, brother."
    else:
        bs "Ok, [pov]."
    "She rubs your dick furiously."
    pov "Hah, so good."
    scene basement 9am 053cbi
    pov "Hnng..."
    bs "Hmm..."
    "You cum in her mouth."
    scene basement 9am 054cbi
    bs "Aah..."
    pov "Good. You know just what I want."
    povi "Wow! Is she smiling?"
    if inc == True:
        pov "Now be a good girl and swallow your brothers cum."
    else:
        pov "Now be a good girl and swallow my cum."
    scene basement 9am 055cbi
    bs "<gulp>"
    povi "She loves to swollow!"
    scene basement 9am 056cbi
    bs "Hnn... are you satisfied now?"
    pov "Yes, my good girl. You served me good."
    bs "Hnng..."
    povi "Ha, she still not used to it when I call her that."
    jump casbasementcorend

label casbasementdp:
    $ casbasecummouth = True
    scene basement 9am 051cbdt
    bs "Hnng... <suck>"
    pov "Oh yes, you know exactly what I like."
    povi "She's deep-throating me on her own. Training her was a good idea."
    scene basement 9am 052cbdt
    pov "Holy shit!"
    bs "<suck> <choke>"
    povi "She took me all in! And all on her own."
    povi "Surprising me like that. I won't last long."
    bs "<suck> <choke>"
    pov "You doing so good."
    scene basement 9am 053cbdt
    if inc == True:
        pov "I'm about to cum, big sis!"
    else:
        pov "I'm about to cum, [bs]!"
    pov "Taking me all in like that feels amazing!"
    bs "<suck> <choke>"
    pov "Just let me spray it all down your throat! Don't choke on it."
    bs "Hmm..."
    pov "Hold it just a moment longer!"
    pov "Hnng..."
    "You spray your sperm down her throat."
    bs "<gulp> <gulp>"
    scene basement 9am 056cbi
    bs "Hah... hah..."
    pov "That was almost perfect."
    bs "Hnn... are you satisfied now?"
    pov "Yes, my girl. You served me good."
    bs "Hnng..."
    povi "Ha, she still not used to it when I call her that."
    $ deepthroatcount = 0
    jump casbasementcorend

#----- Edited -----
label casbasementass:
    povi "Her ass needs a good pounding."
    pov "Just put the tray on the table."
    bs "Yes..."
    scene basement 9am 042cf
    pov "Why you're looking at me like that? You're expecting something?"
    povi "Does she have a clue what I'm up to?"
    bs "And now?"
    scene basement 9am 043cf
    bs "Huh?"
    pov "You know exactly what's happening now, don't you?"
    bs "Hnn..."
    pov "Get over there!"
    scene basement 9am 044cf
    bs "You can't fuck my pussy though! Not yet..."
    pov "Oh, don't worry. I won't."
    povi "She only said I couldn't fuck her pussy. Did she gave me her other option on purpose?"
    scene basement 9am 045cf
    bs "What are you doing? I said you can't!"
    pov "Oh, I won't fuck your pussy. I'm going to fuck that tight asshole!"
    bs "You want to fuck my ass?"
    pov "Yes, you did say that your pussy was off limits right. Just think of this as your extrance exam to the gang."
    scene basement 9am 046cf
    bs "But you can't..."
    pov "Well yes, I can and I will. You're going to let me use you. Because you want it."
    bs "But..."
    pov "I know you can't wait for me to stick my dick inside you!"
    bs "What are you talking about?"
    pov "I just said get over there and you bent over on your own!"
    bs "..."
    scene basement 9am 047cfa
    pov "And don't worry. I'll give you a good pounding, so you can enjoy it too."
    bs "Hnn..."
    pov "But I need you to ask for it now. I need to know that you want me inside you."
    bs "Hnng..."
    pov "Prove to me that I chose correctly, in making you my girl."
    if inc == True:
        bs "Please fuck my ass, brother."
    else:
        bs "Please fuck my ass, [pov]."
    pov "As you wish, my naughty girl."
    scene basement 9am 048cfa
    bs "Hnn..."
    "You press your tip on her asshole."
    pov "Your asshole needs to get used to my big dick."
    bs "Hnn..."
    pov "And I want want you to never forget our first time down here..."
    bs "Hnn..."
    scene basement 9am 049cfa
    with vpunch
    bs "Aaaahhh...!"
    "You ram your dick completely in!"
    pov "Hnn... so tight!"
    bs "Hnng..."
    with vpunch
    if inc == True:
        pov "Just relax your muscles a bit, big sis."
    else:
        pov "Just relax your muscles a bit, [bs]."
    scene basement 9am 050cfa
    with vpunch
    "You start fucking her asshole."
    bs "Hah... hah..."
    with vpunch
    pov "I see you like you're liking your exam?"
    bs "Hah... hnng..."
    with vpunch
    pov "God your ass if so tight. I love it!"
    scene basement 9am 051cfa
    "You release her tits."
    pov "Let them hang free. I love watching them sway as I fuck you."
    bs "Hah... your... big dick..."
    with vpunch
    pov "So you love it how my dick is filling your tight hole?"
    bs "Hah... yes... hng..."
    with vpunch
    scene basement 9am 053cfa
    with vpunch
    "You pound her harder."
    pov "I'm going to cum soon, your tight hole is just too fucking much."
    bs "Hah... hah..."
    with vpunch
    pov "We'll need to fuck many times more so we both can get used to it."
    bs "Hnng..."
    with vpunch
    pov "So where do you want me to put my sperm? Deep inside you or on your ass?"
    bs "Hah... hah... hnng..."
    with vpunch
    pov "Be a good girl now and tell me where to cum!"
    call screen casbasementcorasscum

screen casbasementcorasscum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorasscum'), Jump('casbasementcorassin')) hovered tt.Action ("Cum inside my ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorasscum'), Jump('casbasementcorassout')) hovered tt.Action ("Cum on my ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Edited -----
label casbasementcorassin:
    $ casbasecuminass = True
    bs "Please, cum inside me!"
    pov "Hnng..."
    scene basement 9am 052cfa
    with vpunch
    bs "Ohhh... Hnn..."
    if inc == True:
        pov "You feel my hot sperm spraying inside you, big sis?"
    else:
        pov "You feel my hot sperm spraying inside you, [bs]?"
    bs "Hnng... yes..."
    with vpunch
    pov "Get used to it, you're my personal cum-dumpster from now on."
    bs "Hah... hah..."
    scene basement 9am 053cfai
    pov "Oh yes, I sprayed so much inside you!"
    bs "Hnng!"
    pov "Enjoy it as long as you can, haha."
    bs "Hnn... are you satisfied now?"
    pov "Yes, my girl. You served me well."
    bs "Hnng..."
    povi "Ha, she still doesn't like it when I call her that. For now anyway."
    jump casbasementcorend

label casbasementcorassout:
    $ casbasecumonass = True
    bs "Please, cum on my ass!"
    pov "Hnng..."
    scene basement 9am 053cfao
    bs "Ohhh... Hnn..."
    if inc == True:
        pov "You feel my hot sperm spraying on your ass, big sis?"
    else:
        pov "You feel my hot sperm spraying on your ass, [bs]?"
    bs "Hnng... yes..."
    pov "You're mine now, just like you wanted..."
    scene basement 9am 054cfao
    pov "Wonderful!"
    bs "Hnng..."
    bs "Are you satisfied now?"
    pov "Yes, my girl. You served me well."
    bs "Hnng..."
    povi "Ha, she still doesn't like it when I call her that. For now anyway."
    jump casbasementcorend

label casbasementcorend:
    scene black
    pov "Come, sit with me."
    if casbasecumface == True:
        scene basement 9am 060cf
    else:
        scene basement 9am 060
    pov "You did so good, so let's drink together and celebrate that you passed your exam."
    pov "Aren't you happy?"
    bs "Y... yes... I am."
    pov "You even got a special gift for the occasion."
    if casbasecumface == True:
        scene basement 9am 061cf
    else:
        scene basement 9am 061
    if casbasecumface == True:
        pov "You have my sperm on your face as the proof."
    elif casbasecummouth == True:
        pov "You have  my sperm in your stomach as the proof."
    elif casbasecumonass == True:
        pov "You have my sperm on your ass as the proof."
    elif casbasecuminass == True:
        pov "You have my sperm in your ass as the proof."
    bs "Hnng..."
    pov "Now show me that this is really what you wanted all along and drink your wine."
    bs "..."
    if casbasecumface == True:
        scene basement 9am 062cf
    else:
        scene basement 9am 062
    bs "<gulp> <gulp>"
    povi "I knew it. Still this is a big step towards making her all mine!"
    if casbasecumface == True:
        scene basement 9am 063cf
    else:
        scene basement 9am 063
    pov "Good girl. So how does it feel being part of the gang you wanted to join for so long?"
    bs "F... fine."
    pov "Now you can look forward to much more fun and much more \"serving\" me here."
    bs "Hnng..."
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ basecasfirst = True
    $ casbasecumface = False
    $ casbasecummouth = False
    $ casbasecumonass = False
    $ casbasecuminass = False
    jump kitchen

label casbasementlove:
    $ bigsislove += 1
    scene basement 9am 003l
    bs "Cool!"
    bs "I'm excited to see what I can find."
    scene black
    "She choose something and changed."
    scene basement 9am 020l
    bs "See what I found!"
    pov "Wow..."
    bs "Ha, so you like it too?"
    pov "Oh yes!"
    scene basement 9am 021l
    bs "Me too. I never thought I would find such a cool outfit down here."
    pov "It suits you very well. Very beautiful."
    bs "Sometimes you can be such a charmer!"
    scene basement 9am 022l
    bs "And look at these cool boots."
    bs "With the little ornaments."
    pov "Wow, the pants are really low-cut..."
    scene basement 9am 023l
    bs "<giggle> I wonder why you're complaining?"
    pov "What?"
    bs "You're a boy. Don't you like it?"
    pov "Haha, so you want me to stare?"
    scene basement 9am 024l
    if inc == True:
        bs "Yes I do. This time you're allowed, little brother."
    else:
        bs "Yes I do. This time you're allowed, [pov]."
    pov "And how did I earn the privilege?"
    bs "You brought me down here and I wanted to see it for a long time now."
    pov "True, but not everything down here is a good thing..."
    scene basement 9am 025l
    bs "What do you mean?"
    pov "You saw the kinky stuff in the corner?"
    bs "Yes, I didn't know about that, but I had some thoughts about it."
    pov "I need to figure it all out a bit more still. I want to make sure I don't have share you."
    scene basement 9am 026l
    bs "Oh, you're so cute."
    pov "Are you flirting with me?"
    bs "<giggle>"
    povi "What's gotten into her? Is she really that thankful that I was the one to let her down here?"
    scene basement 9am 027l
    bs "Oh?"
    pov "I see you found the big secret they keep in the basement."
    bs "These small pills laying on the table?"
    pov "Yes."
    scene basement 9am 028l
    bs "But they look like candy?"
    pov "Please don't touch them."
    bs "Why? Are they dangerous?"
    pov "Hm... Not really, but I need to tell you about them first."
    scene basement 9am 029l
    bs "These are drugs? Aren't they?"
    pov "Yes, but they give you a special sort of boost."
    bs "Then why are they bad? <giggle>"
    pov "These are sex-drugs."
    scene basement 9am 030l
    bs "Roofies?"
    pov "Thank god no. But they boost the sex-drive of women and that's why they're so popular."
    bs "And the gang sells them?"
    pov "Yes and sometimes they use them down here too. That's why there's a kinky corner in here."
    if inc == True:
        bs "Even mom and dad?"
    else:
        bs "Even my mom and my dad?"
    pov "Yes..."
    scene basement 9am 031l
    pov "And that's also the reason why they don't want you to come down here."
    bs "And do they have bad side effects?"
    pov "No, surprisingly not. But you could get addicted to it. Become a sex-addict... Not sure if that's a good or a bad thing."
    scene basement 9am 032l
    bs "So these little pills will get my horny instantly?"
    pov "Pretty much. But I'm not sure if I want you to get addicted to it, haha."
    bs "Have you tried them?"
    pov "They work only on women. Besides, men already have an instant sex-drive, haha."
    bs "So only for us women..."
    scene basement 9am 033l
    pov "What...?"
    bs "Hmm..."
    pov "What are you doing? Didn't you understand a word I just said?"
    scene basement 9am 034l
    bs "<giggle>"
    pov "If you swallow that, there's no turning back. At least until you orgasm."
    bs "Hm..."
    pov "So you can stop joking around now..."
    scene basement 9am 035l
    bs "<gulp>"
    pov "..."
    pov "Why did you do that?"
    scene basement 9am 036l
    bs "You still don't get it?"
    pov "Hmm..."
    bs "We're all alone down here and I just took a sex-drug to get horny..."
    pov "<gulp> Oh..."
    povi "This is awesome! She's so into this basement stuff!"
    scene basement 9am 037l
    bs "I wanted to know what it can do and since I'm here with the right person to test it, I thought why not?"
    bs "You fulfilled my wish and so I'll thank you for that now. And if you're right, I'll have fun too."
    bs "<giggle>"
    pov "So did you want to make out with me?"
    if inc == True:
        bs "Yes, brother!"
    else:
        bs "Yes, [pov]!"
    scene basement 9am 038l
    bs "I'll let you choose how you want to please me, <giggle>"
    bs "But please don't overdo it."
    pov "I'll be a gentleman until you beg me for more, haha."
    povi "So, how should I please her?"
    call screen casbasementlovechoose

screen casbasementlovechoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlovechoose'), Jump('casbasementlovekiss')) hovered tt.Action ("Kiss her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlovechoose'), Jump('casbasementlovetits')) hovered tt.Action ("Play with her tits") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label casbasementlovekiss:
    pov "I know exactly what you like."
    scene basement 9am 039lk
    bs "Huh?"
    pov "<kiss>"
    bs "Hmm..."
    "You french kiss her."
    bs "<giggle>"
    scene basement 9am 040lk
    "You continue to play with her tongue."
    bs "Hmm...!"
    pov "<kiss> <lick>"
    scene basement 9am 041lk
    bs "Hah... Hnng..."
    pov "You like it so much. Being held and kissed. Playing with our tongues like this!"
    bs "Yes... you're right."
    pov "<lick> <kiss>"
    bs "Hah, I'm feeling so hot."
    pov "It was your choice to take the drug..."
    bs "Yes... hah... and feels so good."
    scene basement 9am 042lk
    bs "Hah... Hnng..."
    if inc == True:
        bs "Hold me tighter, brother!"
    else:
        bs "Hold me tighter, [pov]!"
    pov "Oh I won't let you go. <lick>"
    bs "Oh god? Hnng..."
    "She's trembling like crazy."
    pov "Oh, so the drug feels that good?"
    bs "HNN... HNNG..."
    povi "Did she really just have an orgasm? Is the drug that good?"
    scene basement 9am 043lk
    bs "Hah... hah..."
    pov "You didn't really...?"
    bs "<giggle> You made me cum from just kissing and licking me."
    pov "Wow! But now you understand that you could go crazy on these things very quickly."
    bs "Yes I do. But you enjoyed that too right?"
    pov "I did, but maybe next time we try it without the drug, I can get you that orgasm on my own!"
    bs "<giggle> Maybe..."
    pov "I love you [bs]."
    scene basement 9am 044lk
    bs "You're such a gentleman. You didn't even take advantage of me in this situation."
    pov "Hmm... Well, I did make you cum, doesn't sort of count as taking advanage?"
    bs "But you held back like I asked."
    povi "I don't get it. Is it that she came and I didn't? What does that matter?"
    bs "Come here [pov]. It's your turn."
    scene basement 9am 045lk
    pov "My turn...?"
    bs "Since you like my mouth and tongue so much I'll reward you with them."
    pov "Oh, you're going to...?"
    bs "Yes, and I can feel your hard dick through your pants."
    scene basement 9am 046lk
    bs "So the drug affected you too, <giggle>"
    pov "It was more your sweet taste and cumming in my arms that did it."
    bs "So big and hard..."
    scene basement 9am 047lk
    bs "It's time you cum too, <giggle>"
    pov "I'm excited to feel your lips and your tongue again."
    scene basement 9am 048lk
    bs "<lick>"
    pov "Oh god yes! Amazing!"
    bs "You're burning hot."
    pov "It's your wet tongue, it's driving me crazy."
    bs "Hmm..."
    scene basement 9am 049lk
    pov "Hah..."
    bs "<lick> <suck>"
    pov "You're doing so good, this is the best reward."
    povi "I didn't know that she could suck so good. Is that a good or bad thing? Fuck it, it's good. Definitely a good thing!"
    bs "Hmm... <slurp>"
    pov "This is too good, I'm going to cum soon if you keep at that pace though!"
    "She starts to lick you faster."
    pov "Watch out or I'll cum in your mouth."
    bs "Hmm..."
    povi "She doesn't seem to mind? Does she want me to cum in her mouth?"
    scene basement 9am 050lk
    pov "This is too much, hnng...!"
    "You cum in her mouth."
    if inc == True:
        pov "Oh yes, big sis!"
    else:
        pov "Oh yes, [bs]!"
    bs "Hmm..."
    bs "<gulp> <gulp>"
    povi "Wow, she's swallowing it."
    scene basement 9am 051lk
    pov "You... you swallowed it."
    bs "Hmm... I wanted to taste you."
    pov "And was it good?"
    bs "Yes."
    if inc == True:
        bs "You taste surprisingly good, little brother."
        pov "I still can't believe it that you sucked me off, big sis."
    else:
        bs "You taste surprisingly good, [pov]."
        pov "I still can't believe it that you sucked me off, [bs]."
    bs "<giggle> You earned it yourself, like I said before."
    pov "Maybe I can earn another one?"
    bs "Haha, maybe..."
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ basecasfirst = True
    jump kitchen

label casbasementlovetits:
    pov "I need to play with your breasts!"
    scene basement 9am 039lt
    bs "Oh! So you like my big boobs do you?"
    pov "Oh yes, they're fantastic."
    pov "And they're so weighty in my hands."
    bs "<giggle> Is that a compliment?"
    pov "More than that, like a profession of love."
    bs "<giggle>"
    pov "Let's undress."
    scene basement 9am 040lt
    if inc == True:
        bs "Relax brother. No need to rip this top. We have time."
    else:
        bs "Relax [pov]. No need to rip this top. We have time."
    pov "There they are. So wonderful."
    bs "You're hands are all over them."
    pov "You'll love it when I kneed and play with them."
    scene basement 9am 041lt
    bs "Hah..."
    pov "See? And your rings are perfect for pull on."
    bs "Hmm..."
    if inc == True:
        pov "Your boobs are really wonderful, big sis."
    else:
        pov "Your boobs are really wonderful, [bs]."
    bs "And your hands are feeling really good too."
    scene basement 9am 042lt
    bs "Hah... hnn..."
    pov "Does it feel that good?"
    bs "You were right. With those drugs, the feeling is intense."
    pov "Then you'll love what I can do to your boobs."
    bs "Yes please, hah... don't stop!"
    scene basement 9am 043lt
    pov "<kiss> <suck>"
    bs "Oh my god! Yes!"
    if inc == True:
        pov "You're trembling, big sis."
    else:
        pov "You're trembling, [bs]."
    bs "I can't believe it, hah... ahhh..."
    bs "More!"
    "You bite her nipple gently."
    bs "Ahhh... hah... hnng..."
    povi "Is the drug so strong that she came from just playing with her tits? Amazing!"
    bs "Hmm... that was so good."
    pov "Man I love your tits, [bs]."
    scene basement 9am 045lt
    bs "You did such a good job with my boobs, I think you've earned a reward."
    pov "A reward? Now I'm curious."
    if inc == True:
        bs "Come to me, brother."
    else:
        bs "Come to me, [pov]."
    scene basement 9am 046lt
    "She has you lay down on the table."
    bs "So it's perfect. You pleasured me with my boobs and now I'll pleasure you with them."
    pov "You mean... a... boob-job?"
    bs "You already know the name for it?"
    if inc == True:
        bs "<giggle> Kinky little brother."
    else:
        bs "<giggle> Kinky [pov]."
    scene basement 9am 047lt
    bs "Your dick is burning between my breasts."
    pov "It's like a dream come true. Feeling them around my cock."
    bs "I want you to enjoy what's coming."
    if inc == True:
        pov "Oh, I will, big sis."
    else:
        pov "Oh, I will, [bs]."
    bs "<giggle>"
    scene basement 9am 048lt
    pov "Ohhh..."
    povi "Feeling her boobs and her tongue on my dick!"
    bs "<lick>"
    pov "You're the best [bs]."
    bs "<kiss> <lick>"
    pov "But at this pace I won't last very much longer... hah..."
    scene basement 9am 049lt
    if inc == True:
        bs "Then you should enjoy your orgasm like I did mine, little brother."
    else:
        bs "Then you should enjoy your orgasm like I did mine, [pov]."
    pov "Oh, I will, hah..."
    "She's kneading her boobs faster on your dick."
    pov "Serious, I'm about to burst. Probably cover your whole body in sperm at this rate!"
    bs "<giggle> So you like it that much?"
    bs "Then spray it all over the boobs you love so much."
    if inc == True:
        pov "Oh big sis!"
        scene basement 9am 050lt
        pov "Sister! Hnng!"
    else:
        pov "Oh [bs]!"
        scene basement 9am 050lt
        pov "[bs]! Hnng!"
    "She closes her eyes quickly."
    bs "Hmm..."
    pov "Ohhh..."
    scene basement 9am 051lt
    bs "So much hot sperm on my boobs. I love it!"
    pov "Wow! You surprised me what you could do with your tits."
    bs "I'm proud to see you liked it that much! <giggle>"
    pov "Maybe you can surprise me more often?"
    bs "Haha, maybe..."
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ basecasfirst = True
    jump kitchen

label casbasementntr:
    $ basecasfrankntr = True
    hide screen locations
    scene black
    "As you enter the basement you hear voices."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene basement 4pm 060ntr
    povi "What is Frank doing here? Who the fuck let him in?"
    frank "Are you ready now? I can't wait all day!"
    bs "Yes, please just wait a second, daddy."
    povi "Daddy? What the fuck is this? A kinky roleplay?"
    scene basement 4pm 061ntr
    bs "Here I am."
    bs "What's with your hand, daddy?"
    frank "That's a sign for you. Get on your knees where you belong!"
    povi "So it's a kinky roleplay and I'm pretty sure I know what she'll have to do when she's on her knees."
    povi "But why is she drunk and with that idiot? I don't get it? Maybe he paid her?"
    if hardntr == False:
        call screen casbasementntrchoose
    else:
        jump casbasementntrwatch

screen casbasementntrchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('casbasementntrchoose'), Jump('casbasementntrinterfere')) hovered tt.Action ("Stop this") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementntrchoose'), Jump('casbasementntrwatch')) hovered tt.Action ("Watch them secretly") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label casbasementntrwatch:
    povi "I need to see what the deal is with this."
    call screen checkdarkerpaths_cassandra
    jump casbasementapp

label casbasementapp:
    scene basement 4pm 062ntr
    bs "Like this daddy? Let me show you what I can do."
    frank "I've heard you can give head like a pro. So let's see if that's true."
    if cassandra_revenge == True:
        povi "What? He can't be serious!"
    else:
        if cassandra_voyeur == True or cassandra_sadist == True:
            povi "What? Now I'm curious too."
        else:
            povi "Why would she blow you? Fat fuck!"
    frank "Come here little minx."
    bs "Yes daddy."
    scene basement 4pm 063ntr
    bs "Hmm... <suck>"
    frank "Oh, not bad."
    if cassandra_revenge == True:
        povi "I can't believe it! He has to be paying a shit ton for this. That fat prick."
    else:
        if cassandra_voyeur == True or cassandra_sadist == True:
            povi "Ha. She's not wasting any time."
        else:
            povi "Why is she doing this? Did he pay her?"
    scene basement 4pm 064ntr
    frank "Good, work on my dick."
    bs "Hnng... <suck>"
    frank "Getting drunk and sucking cocks! You're favorite hobbies, haha!"
    bs "Hm... hnn..."
    if cassandra_revenge == True:
        if inc == True:
            povi "What an asshole. Doing that to my sister."
        else:
            povi "What an asshole. Doing that to her."
    else:
        if cassandra_voyeur == True or cassandra_sadist == True:
            povi "She seems to love getting humiliated by him."
        else:
            povi "He humiliating her and she's just taking it, why? I thought we were getting somewhere. Why would she do this to me?"
    frank "I'll help you!"
    scene basement 4pm 065ntr
    bs "Hnng...! Hmm...!"
    frank "Now it's much better!"
    povi "He's fucking her mouth."
    frank "I'm close! Drink what your daddy gives you!"
    bs "Hmm..."
    frank "Argh! Yes! YES!"
    bs "Hnng... <gulp> <gulp>"
    if cassandra_revenge == True:
        povi "He forced her to swallow it. Messed up!"
    else:
        if cassandra_voyeur == True or cassandra_sadist == True:
            povi "He forced her to swallow it. And I bet she was a good girl and swallowed it all."
        else:
            povi "I can't believe she's swallowing that nasty prick's cum."
    scene basement 4pm 067ntr
    bs "See? I swallowed all, daddy!"
    frank "Not all. My precious cum dripping out of your mouth."
    bs "There was so much."
    frank "I don't care! Next time you'll swallow all or you'll get a hard spanking!"
    if cassandra_revenge == True:
        povi "He's threating her. Now she'll get furious!"
    if cassandra_sadist == True:
        povi "That makes a lot more sense now!"
    bs "OK, I can do better, daddy."
    scene basement 4pm 068ntr
    bs "Oh why is everything spinning around?"
    frank "Because you drank too much, doll!"
    if cassandra_revenge == True:
        frank "Plus that \"candy\" you ate helps out a lot..."
        povi "That piecs of shit! He drugged her!"
    bs "Help me dy..."
    frank "You have to stop drinking that much. This is your fault after all."
    scene basement 4pm 070ntr
    frank "Sweet dreams, little minx."
    bs "Hnn..."
    frank "Always drunk... disgusting..."
    frank "I knew offering you a ride home would be worth my time."
    if cassandra_revenge == True:
        povi "That's how he got here! He just used her and is now leaving her on the floor like that. What a damn asshole!"
    scene basement 4pm 071ntr
    if inc == True:
        pov "Hey, big sis, wake up."
        bs "Hnn..."
        pov "Sis... SISTER, WAKE UP!"
    else:
        pov "Hey, [bs], wake up."
        bs "Hnn..."
        pov "[bs]... WAKE UP!"
    povi "Damn there is no use. She's too drunk."
    if cassandra_sadist == True:
        povi "I'm half tempted to leave the slut down here. If she got found like that..."
        povi "Fuck it. She'll owe me for this. I can use that later."
    else:
        povi "But I need to get her out of here. If she got found like that..."
    if cassandra_revenge == True:
        povi "Argh! That prick used her and all I can do is clean up. I'm going to find a way to make him pay for this!"
    scene black
    "You bring her back to her room."
    $ dtime += 1
    $ cassandra_ntr = False
    $ casbasentrevent = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump kitchen

label casbasementntrinterfere:
    povi "This is not going to happen while I'm here!"
    "You show yourself."
    scene basement 4pm 062sntr
    if inc == True:
        bs "Oh hey, little brother."
    else:
        pov "Oh hey, [pov]."
    frank "You...!"
    pov "That's right Frank! It's me!!!"
    povi "Seriously, what the fuck did I just say? I need to think before I speak sometimes."
    pov "You need to get out of here. She's way too drunk, or do you think it's okay to take advantage of her while she's so drunk?"
    bs "But I want him to do this. He's my daddy. He gave me a candy..."
    povi "That piece of shit gave her one of the sex-drugs!"
    pov "Stop this shit, [bs]."
    frank "I see, I'm not wanted anymore. I'll go."
    pov "Frank, you were never wanted to begin with."
    if inc == True:
        bs "Why you're so mad, brother?"
    else:
        bs "Why you're so mad, [pov]?"
    pov "Enough. You shouldn't be here and especially not drunk."
    bs "But..."
    scene black
    "After Frank has left, you bring [bs] to her room, so she can sleep her drunkenness off."
    "She came in your arms as you carried her. That drug is seriously strong! Just touch can set off an orgasm."
    "What a waste though, no one really got to enjoy that one."
    $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    $ casbasentrevent = True
    jump kitchen

label casbasementrepeat:
    hide screen locations
    scene kitchen 9am 020
    if inc == True:
        bs "Hey there sweet brother of mine!"
    else:
        bs "Hey there sweet [pov]!"
    povi "Huh? What's up with her? What is with all that sweet-talk?"
    pov "What's up?"
    if bigsiscorruption >= bigsislove:
        scene kitchen 9am 009rc
    else:
        scene kitchen 9am 006rl
    bs "Do you want to go hang out in the basement."
    povi "And now the sweet-talk makes sense."
    bs "I had so much fun last time!"
    pov "Hmm..."
    if inc == True:
        bs "Please, you'd be the best brother ever!"
    else:
        bs "Please, you'd be the best friend ever!"
    povi "Should we go play around down there?"
    call screen casbasementallowrep

screen casbasementallowrep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_approve_%s.png" action (Hide('casbasementallowrep'), Jump('casbasementallowyesrep')) hovered tt.Action ("Go to the Basement") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" action (Hide('casbasementallowrep'), Jump('casbasementallownorep')) hovered tt.Action ("Not now") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label casbasementallownorep:
    pov "No, I don't have time right now."
    bs "Damn it! Oh well."
    pov "We'll get a chance to play around together soon."
    bs "Hnn..."
    scene black
    $ dtime += 1
    jump kitchen

label casbasementallowyesrep:
    $ basecasfirst = True
    pov "OK."
    bs "Really?"
    pov "Yes."
    scene kitchen 9am 021
    bs "Thank you so much."
    pov "But we should go right now..."
    bs "They're all out of the house right now."
    pov "Exactly, so let's go."
    if bigsiscorruption >= bigsislove:
        scene kitchen 9am 009rc
    else:
        scene kitchen 9am 006rl
    bs "I'm still in my underwear..."
    pov "You know there are clothes down there, you can wear something when we get there."
    bs "Oh, goodie!"
    pov "Yes, let's go. It's now or never."
    scene kitchen 9am 021
    bs "OK."
    scene black
    "You go to the basement together."
    scene basement 9am 001
    bs "I love coming down here with you!"
    bs "But it's still a little weird down here, with that \"punishment\" corner."
    pov "I don't know, could be fun to try it out together sometime."
    bs "Oh... hnnn."
    bs "Can I go pick an outfit now? Or did you want to pick one for me?"
    scene basement 9am 002
    povi "Do I want to pick something or just let her pick something?"
    call screen casbaseoutfitchooserep

#----- Custom -----
screen casbaseoutfitchooserep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('casbaseoutfitchooserep'), Jump('casbaseoutfitchooseloverep')) hovered tt.Action ("Yes, choose one you like [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('casbaseoutfitchooserep'), Jump('casbaseoutfitchoosecorrep')) hovered tt.Action ("No, I'll choose one [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
#----- Corruption Path -----
label casbaseoutfitchoosecorrep:
    call screen casbaseoutfitchoosecor2rep

#----- Custom -----
screen casbaseoutfitchoosecor2rep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('casbaseoutfitchoosecor2rep'), Jump('casbasementcorrep')) hovered tt.Action ("Fishnet Dress") focus_mask True
        if basecasfirst == True and bigsiscorruption >= 50: #---- Original -----
            imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('casbaseoutfitchoose'), Jump('casbasementcorfuck')) hovered tt.Action ("Fishnet Dress (Special)") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('casbaseoutfitchoosecor2rep'), Jump('casbasementcor2rep')) hovered tt.Action ("Blouse and Low-cut Jeans") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementcorrep: #----- Original Corruption Outfit -----
    $ bigsiscorruption += 1
    scene basement 9am 003c
    bs "Ok, you pick one then!"
    pov "Thanks, that's a nice way to show me how grateful you are that I made you a part of the gang."
    bs "Hnn..."
    pov "And I'm sure you'll like it too. There're really good things in there."
    bs "O... OK."
    scene black
    "You choose something special for her and she go to change into it."
    scene basement 9am 020c
    bs "This one again?"
    pov "Yes that one! You look way sexy in that outfit!"
    bs "I'm almost naked..."
    scene basement 9am 021c
    pov "Yes! Although your club outfit is almost the same, I might choose something different next time."
    bs "Ok..."
    pov "I'm glad you wanted to play down here again. We had a lot of fun last time."
    bs "Hnn..."
    scene basement 9am 022c
    pov "And you can't deny that you love that outfit."
    pov "Seeing your hot long legs in those shoes."
    bs "You still want me to wear this where other people could see me?"
    scene basement 9am 024c
    pov "I'm ok with other guys looking at my girl, so long as they don't touch."
    bs "Hnng..."
    if inc == True:
        pov "And why not show everyone how hot my big sis is?"
    else:
        pov "And why not show everyone how hot you are?"
    pov "Also, it's important to for my girl to obey me..."
    scene basement 9am 023c
    bs "You still want me to be your girl?"
    pov "Of course I do!"
    if inc == True:
        bs "I'm still your sister!"
    pov "You know that's just a matter of time until you give in and become my girl."
    pov "You want to be part of the gang, become famous, and be with someone that can keep up with you like I can."
    scene basement 9am 025c
    pov "And you know that I can."
    pov "So you can keep denying it if you really want or just admit that I'm right."
    pov "I can handle you much better then your loser boyfriend."
    bs "Hnng..."
    scene basement 9am 026c
    pov "Why don't you grab us some drinks again."
    bs "Red wine?"
    pov "Yes that would be be great. I love watching you in that."
    povi "I could do this all day long."
    pov "Now, move your sexy ass over there for me."
    scene basement 9am 027c
    if inc == True:
        bs "So, do you watch mom like that if she's here?"
    else:
        bs "So, do you watch my mom like that if she's here?"
    pov "Yes of course I do. I am a high-ranked gang member after all. It's my right. Why are you jealous?"
    bs "Maybe... a little."
    scene basement 9am 028c
    pov "But you don't need to be jealous, you still going to be my girl."
    bs "I... understand."
    povi "Her ass is almost naked. That outfit was a good choice."
    scene basement 9am 029c
    povi "And her long legs in that sexy heels."
    povi "I think she could where these more often."
    scene basement 9am 030c
    bs "I kind of like serving you drinks, but I don't know if I'll like serving them to the others."
    pov "We'll see about that when it's time, but you're my girl, so you'll mostly be serving me."
    bs "Ok..."
    povi "No complaints about me calling her my girl. That's good."
    scene basement 9am 031c
    povi "That little patch of fabric over her pussy. I can't wait to remove it and put my dick inside her."
    povi "This is making me so horny."
    bs "You like that don't you..."
    scene basement 9am 032c
    bs "...that you can almost see my pussy."
    pov "Yes I do. And that's a very good girl that notices what her man likes. I'm proud of you."
    pov "Maybe next time we'll take that piece out so I can see you pussy in that dress."
    bs "Hnn..."
    pov "Did you want to take a sex-drug this time?"
    scene basement 9am 033c
    bs "I don't think so. I like how they make me feel, but I don't want to get addicted."
    pov "That's a good choice. We don't need them to have our fun anyway."
    scene basement 9am 035c
    bs "No we don't. You are able to boost my drive just fine on your own."
    pov "Wow, are you flirting with me?"
    scene basement 9am 036c
    bs "I would have thought that was obvious."
    pov "Haha, I know! No need to get angry. I was just teasing!"
    pov "I know what my girl wants, I don't need to \"cheat\"."
    scene basement 9am 037c
    bs "That's a good decision. I won't be your lifeless doll."
    povi "Well, she didn't protest about being my girl again. Progress."
    bs "So did you want to play now? I still have other things to do today."
    povi "She's back to her ornery self again. Oh well, we can still have fun."
    "You walk over to the couch."
    scene basement 9am 038c
    pov "Yes, lets start. But I think it's time for drinks first."
    povi "I can't stop staring at her."
    if inc == True:
        povi "I wonder how mom will react when she see her wearing this."
    else:
        povi "I wonder how [mother] will react when she see her wearing this."
    bs "Red wine still?"
    pov "Yes, unless you wanted something different?"
    bs "No, I like that too. And I like how you're staring at me..."
    "She just stands there a while, letting you stare at her for a while."
    scene basement 9am 039c
    povi "God, I love it every time she turns around in that dress!"
    povi "Maybe I should skip the whole serving drinks thing and just get to fucking her from behind?"
    scene basement 9am 040c
    bs "Are you staring at my ass again?"
    pov "Yes..."
    bs "Good."
    scene basement 9am 041c
    if inc == True:
        bs "I'll get you to forget all about mom, when you have me as your girl."
    else:
        bs "I'll get you to forget all about my mom, when you have me as your girl."
    pov "Oh so you are my girl then?"
    bs "Hnng..."
    povi "So what should we do now?"
    call screen casbasementcorchoose

#----- Custom -----
label casbasementcor2rep: #----- Jeans -----
    $ bigsiscorruption += 1
    scene basement 9am 003l
    bs "Cool!"
    bs "I'm excited to see what you will choose."
    scene black
    "You pick something out for her and she goes to get changed."
    scene basement 9am 020l
    bs "I still really like this one!"
    pov "Me too..."
    bs "I'm surprised you didn't go something more... revealing?"
    pov "It's nice to leave a little to the imagination sometimes. Builds anticipation."
    scene basement 9am 021l
    bs "Oh yeah? Are you anticipating something fun is going to happen?"
    pov "Yes and so are you... Otherwise you wouldn't have asked to come down here again."
    bs "Hey, maybe I just wanted to hang out with you!"
    pov "We'll see if that's really what you want soon enough."
    scene basement 9am 022l
    bs "These boots are still my favorite."
    bs "With the little ornaments."
    pov "Those low-cut pants are mine..."
    scene basement 9am 023l
    bs "<giggle> I thought they would be."
    bs "You're a boy. Of course you like them!"
    pov "Haha, so you still want me to stare at you then?"
    scene basement 9am 024l
    if inc == True:
        bs "Yes I do. I know you like to, little brother."
    else:
        bs "Yes I do. I know you like to, [pov]."
    bs "<giggle>"
    "She twirls around to face you."
    scene basement 9am 025l
    if inc == True:
        pov "God sis, you really are such a tease!"
    else:
        pov "God [bs], you really are such a tease!"
    bs "Only for you."
    "She saunters by you, wiggling her cute ass as she walks."
    scene basement 9am 026l
    pov "So are you ready for that something fun we were discussing earlier?"
    bs "<giggle>"
    povi "I love what's gotten into her when she's down here with me."
    scene basement 9am 027l
    bs "Hmm..."
    pov "I see you're thinking about taking another sex-drug aren't you?"
    bs "Maybe, do you want me to?"
    pov "Yes. But only if you want to."
    scene basement 9am 028l
    bs "I do like how they make me feel when you touch me..."
    pov "It's up to you..."
    scene basement 9am 029l
    bs "I wouldn't mind a boost today, if I'm with you to help me take care of the urges."
    pov "Sounds like you want to take one then."
    scene basement 9am 030l
    bs "Would be terrible if I did? I don't want to become addicted."
    pov "I don't think it would hurt anything if you did. Like I said, the side effect are minimal and we're not down here all the time."
    scene basement 9am 031l
    pov "Plus it is nice to be able to make you orgasm with just my lips on yours..."
    bs "Hnng..."
    scene basement 9am 032l
    bs "Ok, I think I'll take one this time. Are you sure it's ok to just take them though? Shouldn't we pay for them?"
    pov "No it's fine. Think of it as a gang member privilege."
    scene basement 9am 033l
    bs "Hmm..."
    pov "There it goes into that cute little mouth of yours. I'm almost jealous."
    scene basement 9am 034l
    bs "<giggle>"
    pov "Good girl."
    bs "Hm..."
    scene basement 9am 035l
    bs "<gulp>"
    pov "..."
    pov "Are you ready?"
    scene basement 9am 036l
    bs "You really do want me don't you?"
    pov "Of course I do..."
    bs "Well we're all alone down here and I just took a sex-drug to get horny..."
    pov "<gulp> Oh..."
    bs "I guess that kind of makes me your girl, for right now at least. <wink>"
    povi "This is awesome! She's so into this basement stuff!"
    scene basement 9am 037l
    bs "I do love being down here with you... You make me feel so safe and loved."
    bs "I want you [pov]."
    bs "<giggle>"
    pov "Good, now are you glad you're my girl?"
    if inc == True:
        bs "Yes, brother!"
    else:
        bs "Yes, [pov]!"
    scene basement 9am 038l
    bs "And I'll let you choose how you want to please me, <giggle>"
    bs "You can do what you want with me."
    pov "Of course I can, you're mine now."
    povi "So, how should I please her?"
    call screen casbasementcor2chooserep

#----- Custom -----
screen casbasementcorchooserep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorchoose'), Jump('casbasementcorbjrep')) hovered tt.Action ("Use her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorchoose'), Jump('casbasementcorassrep')) hovered tt.Action ("Use her ass") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementcorbjrep:
    povi "Her blow-jobs are so good... I think it's time for another one."
    "You pull out your dick."
    scene basement 9am 042cb
    bs "What are you doing?"
    pov "Preparing the last step of your exam."
    bs "But..."
    scene basement 9am 043cb
    pov "Come closer, put the try down and serve me like a good girl."
    bs "Hnng..."
    pov "Now that you're my girl, you need to serve me whenever I ask, especially down here."
    pov "And I know that you're eager to show me that your mouth is one of the best reasons to choose you as my girl."
    scene basement 9am 044cb
    bs "Hnn..."
    pov "Oh come on. I know you're only playing at being offended, haha."
    if inc == True:
        pov "I know you much better than you think, big sis."
    else:
        pov "I know you much better than you think, [bs]."
    scene basement 9am 045cb
    bs "Hnn..."
    pov "But it's time to stop playing around and get to work."
    pov "Passing this final step is what you need to do to become a part of the gang."
    pov "And you should be happy that we're doing this while we're alone and the others are not here."
    pov "None of the other guys in the gang would be so... considerate."
    povi "Haha, but that could change very soon, if I choose."
    scene basement 9am 046cb
    pov "How about you show me a little of that excitement you had before?"
    pov "Look, you don't have to do this if you really don't want to. But if you become a part of the gang, the other might do worse, if you're not \"my\" girl."
    bs "Hnn..."
    pov "Show me that I made a good decision here. If you want to become my girl... tell me. Otherwise we'll just call it a day, it's ok."
    bs "I..."
    if inc == True:
        bs "I want to suck your dick, brother. I want to be your girl."
    else:
        bs "I want to suck your dick, [pov]. I want to be your girl."
    pov "Good girl. You can start when you want."
    scene basement 9am 047cb
    pov "I love your warm hands on my dick."
    bs "Hmm..."
    povi "I can't wait to feel her tongue again."
    scene basement 9am 048cb
    bs "<suck> <lick>"
    pov "Yes, that's good."
    if inc == True:
        povi "Now it's time to let my big sister prove that she can give the best blow-jobs."
    else:
        povi "Now it's time to let her prove that she can give the best blow-jobs."
    scene basement 9am 049cb
    bs "Hah... <lick>"
    povi "Oh, she opening her mouth wider to give her tongue more space to play."
    if inc == True:
        pov "Your tongue is the best, big sis."
    else:
        pov "Your tongue is the best, [bs]."
    if deepthroatcount >= 2: #----- if casbjdt >= 2: -----
        jump casbasementcordprep
    bs "<giggle> I know."
    scene basement 9am 050cb
    pov "Yes, lick it just like that. That's a good girl."
    bs "Hmm... <lick> <lick>"
    pov "You're handling my dick even better with the time."
    pov "I bet you don't put in so much effort when you did this with your boyfriend."
    bs "Hnng..."
    pov "Well, soon to be ex-boyfriend, right?"
    scene basement 9am 051cb
    bs "<suck>"
    pov "Haha, nice trick to avoid saying anything. I can appreciate that."
    bs "Hmm..."
    scene basement 9am 052cb
    pov "Oh you stopped..."
    bs "You know why. <giggle>"
    pov "See, there is another reason why you have to be my girl."
    pov "You know exactly when I'm at my limit and need to cum."
    bs "Yes, now where do you want me to take it."
    povi "Holy shit, she's getting into it!"
    if inc == True:
        pov "You being such a good girl now, big sis."
    else:
        pov "You being such a good girl now, [bs]."
    $ deepthroatcount += 1
    call screen casbasementcorcumrep

#----- Custom -----
screen casbasementcorcumrep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorcumrep'), Jump('casbasementcorcumfrep')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorcumrep'), Jump('casbasementcorcummrep')) hovered tt.Action ("Cum in her mouth") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementcorcumfrep:
    $ casbasecumface = True
    pov "I want to spray it on your face."
    if inc == True:
        bs "Ok, brother."
    else:
        bs "Ok, [pov]."
    "She rubs your dick furiously."
    pov "Hah, so good."
    scene basement 9am 053cbo
    pov "Hnng..."
    bs "Hmm..."
    "You cum on her face."
    scene basement 9am 054cbo
    bs "Hnn... are you satisfied now?"
    pov "Yes, my girl. You served me good."
    bs "Hnng..."
    povi "Ha, she still not used to it when I call her that."
    pov "Don't wipe it off... Good girls wear their man's cum with pride!"
    bs "Hmm..."
    jump casbasementcorendrep

#----- Custom -----
label casbasementcorcummrep:
    $ casbasecummouth = True
    pov "I want you to taste my sperm."
    if inc == True:
        bs "Ok, brother."
    else:
        bs "Ok, [pov]."
    "She rubs your dick furiously."
    pov "Hah, so good."
    scene basement 9am 053cbi
    pov "Hnng..."
    bs "Hmm..."
    "You cum in her mouth."
    scene basement 9am 054cbi
    bs "Aah..."
    pov "Good. You know just what I want."
    povi "Wow! Is she smiling?"
    if inc == True:
        pov "Now be a good girl and swallow your brothers cum."
    else:
        pov "Now be a good girl and swallow my cum."
    scene basement 9am 055cbi
    bs "<gulp>"
    povi "She loves to swollow!"
    scene basement 9am 056cbi
    bs "Hnn... are you satisfied now?"
    pov "Yes, my good girl. You served me good."
    bs "Hnng..."
    povi "Ha, she still not used to it when I call her that."
    jump casbasementcorendrep

#----- Custom -----
label casbasementcordprep:
    $ casbasecummouth = True
    scene basement 9am 051cbdt
    bs "Hnng... <suck>"
    pov "Oh yes, you know exactly what I like."
    povi "She's deep-throating me on her own. Training her was a good idea."
    scene basement 9am 052cbdt
    pov "Holy shit!"
    bs "<suck> <choke>"
    povi "She took me all in! And all on her own."
    povi "Surprising me like that. I won't last long."
    bs "<suck> <choke>"
    pov "You doing so good."
    scene basement 9am 053cbdt
    if inc == True:
        pov "I'm about to cum, big sis!"
    else:
        pov "I'm about to cum, [bs]!"
    pov "Taking me all in like that feels amazing!"
    bs "<suck> <choke>"
    pov "Just let me spray it all down your throat! Don't choke on it."
    bs "Hmm..."
    pov "Hold it just a moment longer!"
    pov "Hnng..."
    "You spray your sperm down her throat."
    bs "<gulp> <gulp>"
    scene basement 9am 056cbi
    bs "Hah... hah..."
    pov "That was almost perfect."
    bs "Hnn... are you satisfied now?"
    pov "Yes, my girl. You served me good."
    bs "Hnng..."
    povi "Ha, she still not used to it when I call her that."
    $ deepthroatcount = 0
    jump casbasementcorendrep

#----- Custom -----
label casbasementcorassrep:
    povi "Her ass needs a good pounding."
    pov "Just put the tray on the table."
    bs "Yes..."
    scene basement 9am 042cf
    pov "Why you're looking at me like that? You're expecting something?"
    povi "Does she have a clue what I'm up to?"
    bs "And now?"
    scene basement 9am 043cf
    bs "Huh?"
    pov "You know exactly what's happening now, don't you?"
    bs "Hnn..."
    pov "Get over there!"
    scene basement 9am 044cf
    bs "You can't fuck my pussy though! Not yet..."
    pov "Oh, don't worry. I won't."
    povi "She only said I couldn't fuck her pussy. Did she gave me her other option on purpose?"
    scene basement 9am 045cf
    bs "What are you doing? I said you can't!"
    pov "Oh, I won't fuck your pussy. I'm going to fuck that tight asshole!"
    bs "You want to fuck my ass?"
    pov "Yes, you did say that your pussy was off limits right. Just think of this as your extrance exam to the gang."
    scene basement 9am 046cf
    bs "But you can't..."
    pov "Well yes, I can and I will. You're going to let me use you. Because you want it."
    bs "But..."
    pov "I know you can't wait for me to stick my dick inside you!"
    bs "What are you talking about?"
    pov "I just said get over there and you bent over on your own!"
    bs "..."
    scene basement 9am 047cfa
    pov "And don't worry. I'll give you a good pounding, so you can enjoy it too."
    bs "Hnn..."
    pov "But I need you to ask for it now. I need to know that you want me inside you."
    bs "Hnng..."
    pov "Prove to me that I chose correctly, in making you my girl."
    if inc == True:
        bs "Please fuck my ass, brother."
    else:
        bs "Please fuck my ass, [pov]."
    pov "As you wish, my naughty girl."
    scene basement 9am 048cfa
    bs "Hnn..."
    "You press your tip on her asshole."
    pov "Your asshole needs to get used to my big dick."
    bs "Hnn..."
    pov "And I want want you to never forget our first time down here..."
    bs "Hnn..."
    scene basement 9am 049cfa
    with vpunch
    bs "Aaaahhh...!"
    "You ram your dick completely in!"
    pov "Hnn... so tight!"
    bs "Hnng..."
    with vpunch
    if inc == True:
        pov "Just relax your muscles a bit, big sis."
    else:
        pov "Just relax your muscles a bit, [bs]."
    scene basement 9am 050cfa
    with vpunch
    "You start fucking her asshole."
    bs "Hah... hah..."
    with vpunch
    pov "I see you like you're liking your exam?"
    bs "Hah... hnng..."
    with vpunch
    pov "God your ass if so tight. I love it!"
    scene basement 9am 051cfa
    with vpunch
    "You release her tits."
    pov "Let them hang free. I love watching them sway as I fuck you."
    bs "Hah... your... big dick..."
    with vpunch
    pov "So you love it how my dick is filling your tight hole?"
    bs "Hah... yes... hng..."
    with vpunch
    scene basement 9am 053cfa
    with vpunch
    "You pound her harder."
    pov "I'm going to cum soon, your tight hole is just too fucking much."
    bs "Hah... hah..."
    with vpunch
    pov "We'll need to fuck many times more so we both can get used to it."
    bs "Hnng..."
    with vpunch
    pov "So where do you want me to put my sperm? Deep inside you or on your ass?"
    bs "Hah... hah... hnng..."
    with vpunch
    pov "Be a good girl now and tell me where to cum!"
    call screen casbasementcorasscumrep

#----- Custom -----
screen casbasementcorasscumrep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorasscumrep'), Jump('casbasementcorassinrep')) hovered tt.Action ("Cum inside my ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcorasscumrep'), Jump('casbasementcorassoutrep')) hovered tt.Action ("Cum on my ass") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementcorassinrep:
    $ casbasecuminass = True
    bs "Please, cum inside me!"
    pov "Hnng..."
    scene basement 9am 052cfa
    with vpunch
    bs "Ohhh... Hnn..."
    if inc == True:
        pov "You feel my hot sperm spraying inside you, big sis?"
    else:
        pov "You feel my hot sperm spraying inside you, [bs]?"
    bs "Hnng... yes..."
    with vpunch
    pov "Get used to it, you're my personal cum-dumpster from now on."
    bs "Hah... hah..."
    scene basement 9am 053cfai
    pov "Oh yes, I sprayed so much inside you!"
    bs "Hnng!"
    pov "Enjoy it as long as you can, haha."
    bs "Hnn... are you satisfied now?"
    pov "Yes, my girl. You served me well."
    bs "Hnng..."
    povi "Ha, she still doesn't like it when I call her that. For now anyway."
    jump casbasementcorendrep

#----- Custom -----
label casbasementcorassoutrep:
    $ casbasecumonass = True
    bs "Please, cum on my ass!"
    pov "Hnng..."
    scene basement 9am 053cfao
    bs "Ohhh... Hnn..."
    if inc == True:
        pov "You feel my hot sperm spraying on your ass, big sis?"
    else:
        pov "You feel my hot sperm spraying on your ass, [bs]?"
    bs "Hnng... yes..."
    pov "You're mine now, just like you wanted..."
    scene basement 9am 054cfao
    pov "Wonderful!"
    bs "Hnng..."
    bs "Are you satisfied now?"
    pov "Yes, my girl. You served me well."
    bs "Hnng..."
    povi "Ha, she still doesn't like it when I call her that. For now anyway."
    jump casbasementcorendrep

#----- Custom -----
label casbasementcorendrep:
    scene black
    pov "Come, sit with me."
    if casbasecumface == True:
        scene basement 9am 060cf
    else:
        scene basement 9am 060
    pov "You did so good, so let's drink together and celebrate that you passed your exam."
    pov "Aren't you happy?"
    bs "Y... yes... I am."
    pov "You even got a special gift for the occasion."
    if casbasecumface == True:
        scene basement 9am 061cf
    else:
        scene basement 9am 061
    if casbasecumface == True:
        pov "You have my sperm on your face as the proof."
    elif casbasecummouth == True:
        pov "You have  my sperm in your stomach as the proof."
    elif casbasecumonass == True:
        pov "You have my sperm on your ass as the proof."
    elif casbasecuminass == True:
        pov "You have my sperm in your ass as the proof."
    bs "Hnng..."
    pov "Now show me that this is really what you wanted all along and drink your wine."
    bs "..."
    if casbasecumface == True:
        scene basement 9am 062cf
    else:
        scene basement 9am 062
    bs "<gulp> <gulp>"
    povi "I knew it. Still this is a big step towards making her all mine!"
    if casbasecumface == True:
        scene basement 9am 063cf
    else:
        scene basement 9am 063
    pov "Good girl. So how does it feel being part of the gang you wanted to join for so long?"
    bs "F... fine."
    pov "Now you can look forward to much more fun and much more \"serving\" me here."
    bs "Hnng..."
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ basecasfirst = True
    $ casbasecumface = False
    $ casbasecummouth = False
    $ casbasecumonass = False
    $ casbasecuminass = False
    jump kitchen

#----- Custom -----
screen casbasementcor2chooserep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcor2chooserep'), Jump('casbasementcor2kissrep')) hovered tt.Action ("Kiss her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementcor2chooserep'), Jump('casbasementcor2titsrep')) hovered tt.Action ("Play with her tits") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementcor2kissrep:
    pov "I know exactly what you like."
    scene basement 9am 039lk
    bs "Yeah baby?"
    pov "<kiss>"
    bs "Hmm..."
    "You french kiss her."
    bs "<giggle>"
    scene basement 9am 040lk
    "You continue to play with her tongue."
    bs "Hmm...!"
    pov "<kiss> <lick>"
    scene basement 9am 041lk
    bs "Hah... Hnng..."
    pov "You like it so much. Being held and kissed. Playing with our tongues like this!"
    bs "Yes... I do!"
    pov "<lick> <kiss>"
    bs "Hah, I'm feeling so hot."
    pov "I'm glad, I want you feeling real good..."
    bs "Yes... hah... I do too... don't stop."
    scene basement 9am 042lk
    bs "Hah... Hnng..."
    if inc == True:
        bs "Hold me tighter, brother!"
    else:
        bs "Hold me tighter, [pov]!"
    pov "Oh I wouldn't let you go even if you wanted me to. <lick>"
    bs "Oh god! Hnng..."
    "She's trembling like crazy."
    pov "Are you ready to cum now?"
    bs "HNN... HNNG..."
    povi "Did she really just have an orgasm? That drug is amazing!"
    scene basement 9am 043lk
    bs "Hah... hah..."
    pov "That's my naughty girl."
    bs "<giggle> You made me cum from just kissing and licking me."
    pov "Of course I did. I promised we would have some fun right?"
    bs "Yes you did. But did you enjoy that too?"
    pov "I did, you were like puddy in my hands. I'll let you think of a nice way to show me your appreciation next time."
    bs "<giggle> Next time..."
    scene basement 9am 044lk
    bs "Maybe I could show you my appreciation right now?"
    pov "Hmm... what did you have in mind?"
    bs "Well, I don't want leave you in a bind."
    "She glances at the raging boner held back by your pants."
    bs "Come here [pov]. It's your turn."
    scene basement 9am 045lk
    pov "My turn...?"
    bs "Since you like my mouth and tongue so much why don't I use them to help you out?"
    pov "I love the way you think, [bs]"
    bs "Good! Wow, I can feel your hard dick through your pants."
    scene basement 9am 046lk
    bs "So I guess the drug affected you too, <giggle>"
    pov "It was more your sweet taste and cumming in my arms that did that."
    bs "So big and hard..."
    scene basement 9am 047lk
    bs "It's time you cum too, <giggle>"
    pov "I'm excited to feel your lips and your tongue again."
    scene basement 9am 048lk
    bs "<lick>"
    pov "Oh god yes! Amazing!"
    bs "You're burning hot."
    pov "It's your wet tongue, it's driving me crazy. Keeping going."
    bs "Hmm..."
    scene basement 9am 049lk
    pov "Hah..."
    bs "<lick> <suck>"
    pov "That's my girl. I love the way you suck cock."
    povi "I didn't know that she could suck so good. Is that a good or bad thing? Fuck it, it's good. Definitely a good thing!"
    bs "Hmm... <slurp>"
    pov "I'm going to cum soon!"
    "She starts to lick you faster."
    pov "I'm going to cum in your mouth."
    bs "Hmm..."
    povi "She's doing exactly as she's told. This is perfect!"
    scene basement 9am 050lk
    pov "Here it comes, hnng...!"
    "You cum in her mouth."
    if inc == True:
        pov "Oh yes, big sis!"
    else:
        pov "Oh yes, [bs]!"
    bs "Hmm..."
    pov "Swallow it all!"
    bs "<gulp> <gulp>"
    scene basement 9am 051lk
    pov "Good girl... you swallowed it all like I asked.."
    bs "Hmm... I wanted to taste you."
    pov "And was it as good as you hoped it would be?"
    bs "Yes."
    if inc == True:
        bs "You taste so good, little brother."
        pov "I'll be sure to give you as much as you want then, big sis."
    else:
        bs "You taste so good, [pov]."
        pov "I'll be sure to give you as much as you want then, [bs]."
    bs "<giggle> So I did good then?"
    pov "So good. Just as I expect from my girl."
    bs "Haha, you wish..."
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ basecasfirst = True
    jump kitchen

#----- Custom -----
label casbasementcor2titsrep:
    pov "I need to play with your breasts!"
    scene basement 9am 039lt
    bs "Oh! So you like my big boobs do you?"
    pov "Oh yes, they're fantastic."
    pov "And they're so weighty in my hands."
    bs "<giggle> Is that a compliment?"
    pov "It is..."
    bs "<giggle>"
    pov "Let's get you undressed now."
    scene basement 9am 040lt
    if inc == True:
        bs "Yes brother. Anything you want..."
    else:
        bs "Yes [pov]. Anything you want..."
    pov "There they are. So wonderful."
    bs "You're hands are all over them. Feels so good."
    pov "Just wait until I really start to kneed and play with them."
    scene basement 9am 041lt
    bs "Hah..."
    pov "See? And your rings are perfect for this."
    bs "Hmm..."
    if inc == True:
        pov "Your tits really are wonderful, big sis."
    else:
        pov "Your tits really are wonderful, [bs]."
    pov "And the are finally all mine!"
    bs "We'll see... Your hands do feel really good..."
    scene basement 9am 042lt
    bs "Hah... hnn..."
    pov "Wow, you're really getting into this. Good girl. Tell me how much you like this."
    bs "You were right. With those drugs, the feeling is intense."
    pov "So you want me to keep going then?"
    bs "Yes please, hah... don't stop!"
    scene basement 9am 043lt
    pov "<kiss> <suck>"
    bs "Oh my god! Yes!"
    if inc == True:
        pov "You're trembling, big sis."
    else:
        pov "You're trembling, [bs]."
    bs "I can't believe it, hah... ahhh..."
    bs "More!"
    pov "If you're a good girl!"
    "You bite her nipple."
    bs "Ahhh... hah... hnng..."
    povi "Amazing! The drug just magnifies everything!"
    bs "Hmm... that was so good."
    pov "God, I love your tits, [bs]."
    scene basement 9am 045lt
    bs "I'm glad, now that they are \"yours\" you better take good care of them."
    pov "Oh I will. I can promise you that."
    if inc == True:
        bs "Come to me, brother."
    else:
        bs "Come to me, [pov]."
    scene basement 9am 046lt
    "She has you lay down on the table."
    bs "So, you pleased me with my boobs and now I'll please you with them."
    pov "I love the way you think [bs]!"
    bs "Are you ready to feel them around your cock?"
    if inc == True:
        bs "<giggle> My kinky little brother."
    else:
        bs "<giggle> My kinky [pov]."
    scene basement 9am 047lt
    bs "Your dick is so hot, between my breasts."
    pov "This is like a dream come true."
    bs "I want you to enjoy this..."
    if inc == True:
        pov "Oh, I will, big sis."
    else:
        pov "Oh, I will, [bs]."
    bs "<giggle>"
    scene basement 9am 048lt
    pov "Ohhh..."
    povi "Feeling her boobs and her tongue on my dick, this is just amazing!"
    bs "<lick>"
    pov "You're so good at this [bs]."
    bs "<kiss> <lick>"
    pov "I'm not going last very much longer... hah..."
    scene basement 9am 049lt
    if inc == True:
        bs "Are you going to cum for me, little brother? Are you going to cover my tits with your seed?"
    else:
        bs "Are you going to cum for me, [bs]? Are you going to cover my tits with your seed?"
    pov "Yes, I'm going to, hah..."
    "She's kneading her boobs faster on your dick."
    pov "Serious, I'm about to burst. I'm probably going to cover your whole body in sperm at this rate!"
    bs "<giggle> So you like it that much?"
    bs "Then spray it all me. Cum for me! Cum baby!"
    if inc == True:
        pov "Oh big sis!"
        scene basement 9am 050lt
        pov "Sister! Hnng!"
    else:
        pov "Oh [bs]!"
        scene basement 9am 050lt
        pov "[bs]! Hnng!"
    "She closes her eyes quickly."
    bs "Hmm..."
    pov "Ohhh..."
    scene basement 9am 051lt
    bs "So much hot sperm on my breats. I love it!"
    pov "Wow! You're such a naugty girl. Don't worry, I'll cover you as much as you want with my sperm."
    bs "I'm glad to see you liked it that much! <giggle>"
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ basecasfirst = True
    jump kitchen

#----- Custom -----
#----- Love Path -----
label casbaseoutfitchooseloverep:
    call screen casbaseoutfitchooselove2rep

#----- Custom -----
screen casbaseoutfitchooselove2rep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('casbaseoutfitchooselove2rep'), Jump('casbasementlove2rep')) hovered tt.Action ("Fishnet Dress") focus_mask True
        if basecasfirst == True and bigsislove >= 50: #---- Original -----
            imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('casbaseoutfitchoose'), Jump('casbasementcorfuck_love')) hovered tt.Action ("Fishnet Dress (Special)") focus_mask True
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('casbaseoutfitchooselove2rep'), Jump('casbasementloverep')) hovered tt.Action ("Blouse and Low-cut Jeans") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementlove2rep:
    $ bigsislove += 1
    scene basement 9am 003c
    bs "Ok, I'm going to pick something you'll really like!"
    pov "I'm really excited to see what you're going to choose."
    bs "Hnn..."
    pov "There are a ton of great outfits in there."
    bs "Oh... OK."
    scene black
    "She goes to choose an outfit and get changed."
    scene basement 9am 020c
    bs "So what do you think? Do you like it?"
    pov "Yes! I love that one! You look amazing!"
    bs "I'm almost naked..."
    scene basement 9am 021c
    pov "Oh, I noticed..."
    bs "Hnnn..."
    pov "I'm glad you wanted to play down here again. We had a lot of fun last time."
    bs "Yeah..."
    scene basement 9am 022c
    pov "You really do look so great in this outfit..."
    pov "It really shows off your amazing legs."
    bs "You still want me to wear this where other people could see me?"
    scene basement 9am 024c
    pov "I think it would be fun. All the guys would be so jealous. What do you think?"
    bs "Hnng..."
    if inc == True:
        pov "And why not show everyone how hot my big sis is?"
    else:
        pov "And why not show everyone how hot you are?"
    bs "Well, if you're with me then I guess that could be fun... It would turn heads, that's for sure."
    scene basement 9am 023c
    bs "So, do you still want me to be your girl?"
    pov "Of course I do!"
    if inc == True:
        bs "I'm still your sister you know..."
    pov "You know that I love you and I'm the one willing to stand up and care for you. We're good together."
    pov "You want to be part of the gang, become famous, and be with someone that can keep up with you like I can."
    scene basement 9am 025c
    bs "Well, the's true..."
    pov "So what do you think? Are you ready to lose that crappy boyfriend of yours yet?"
    bs "Hnng..."
    scene basement 9am 026c
    pov "Did you want something to drink?"
    bs "Let me get it! Do you want red wine again?"
    pov "Yes that would be be great."
    scene basement 9am 027c
    if inc == True:
        bs "So, do you watch mom like that if she's here?"
    else:
        bs "So, do you watch my mom like that if she's here?"
    pov "Sure, I'm not blind. She does have a great body after all. Why? Are you jealous?"
    bs "Maybe... a little."
    scene basement 9am 028c
    pov "Well you don't need to be jealous, you're still going to be my girl."
    bs "Good..."
    povi "Her ass is almost naked. That outfit was a great choice."
    scene basement 9am 029c
    povi "And her long legs in those sexy heels."
    povi "I think she should where those more often."
    scene basement 9am 030c
    bs "I kind of like serving you drinks, but I don't know if I'll like serving them to the others."
    pov "We'll see about that when it's time, but you're my girl, so you'll mostly be serving me when the others are here."
    bs "Ok..."
    povi "Wow, she's letting me call her my girl now. That's great."
    scene basement 9am 031c
    povi "That little patch of fabric over her pussy. I can't wait to remove it and put my dick inside her."
    povi "This is making me so horny."
    bs "You like that don't you..."
    scene basement 9am 032c
    bs "...that you can almost see my pussy."
    pov "Well, yeah. Of course I do. You're so beautiful!"
    pov "Maybe next time we'll take that piece out so I can see you pussy in that dress."
    bs "Hnn..."
    pov "So, did you want to take a sex-drug this time?"
    scene basement 9am 033c
    bs "I don't think so. I like how they make me feel, but I don't want to get addicted."
    pov "That's fine with me. We don't need them to have our fun anyway."
    scene basement 9am 035c
    bs "No we don't. You are able to boost my drive just fine on your own. <giggle>"
    pov "Wow, are you flirting with me?"
    scene basement 9am 036c
    bs "I would have thought that was obvious. I did choose this dress after all!"
    pov "Haha, I know! No need to get angry. I was just teasing!"
    pov "I know what my girl wants, and I don't need to \"cheat\" to get her there."
    scene basement 9am 037c
    bs "Well good! I don't want be your lifeless doll."
    pov "You know I would never do that to you!"
    bs "So did you want to play now? I hope I didn't get all dressed up for nothing!"
    povi "Well, that didn't take long, she's back to her ornery self again. But there is a hint of teasing in her voice. I think she's teasing me."
    "You walk over to the couch."
    scene basement 9am 038c
    pov "Yes, let's get started. But I think it's time for drinks first."
    povi "I can't stop staring at her."
    if inc == True:
        povi "I wonder how mom will react when she see her wearing this."
    else:
        povi "I wonder how [mother] will react when she see her wearing this."
    bs "Red wine still?"
    pov "Yes, unless you wanted something different?"
    bs "No, I like that too. And I like how you're staring at me..."
    "She just stands there a while, letting you stare at her."
    scene basement 9am 039c
    povi "God, I love it every time she turns around in that dress!"
    povi "Maybe I should skip the whole serving drinks thing and just get to fucking her from behind?"
    scene basement 9am 040c
    bs "Are you staring at my ass again?"
    pov "Yes..."
    bs "Good."
    scene basement 9am 041c
    if inc == True:
        bs "I'll get you to forget all about mom, since you have me as your girl."
    else:
        bs "I'll get you to forget all about my mom, since you have me as your girl."
    pov "Oh so you are my girl then?"
    bs "Hnng..."
    povi "So what should we do now?"
    call screen casbasementlove2chooserep

#----- Custom -----
label casbasementloverep:
    $ bigsislove += 1
    scene basement 9am 003l
    bs "Cool!"
    bs "I'm excited to see what I can find."
    scene black
    "She choose something and changed."
    scene basement 9am 020l
    bs "I still really like this one!"
    pov "Wow..."
    bs "Ha, so you still like it too?"
    pov "Oh yes!"
    scene basement 9am 021l
    bs "I never thought I would find such a cool outfit down here."
    pov "It suits you very well. Very beautiful."
    bs "You said that last time, you charmer!"
    pov "Just stating the truth is all."
    scene basement 9am 022l
    bs "These boots are still my favorite."
    bs "With the little ornaments."
    pov "Those low-cut pants are mine..."
    scene basement 9am 023l
    bs "<giggle> I thought they would be."
    bs "You're a boy. Of course you like them!"
    pov "Haha, so you still want me to stare at you then?"
    scene basement 9am 024l
    if inc == True:
        bs "Yes I do. This time you're allowed, little brother."
    else:
        bs "Yes I do. This time you're allowed, [pov]."
    bs "<giggle>"
    "She twirls around to face you."
    scene basement 9am 025l
    if inc == True:
        pov "God sis, you really are just gorgeous!"
    else:
        pov "God [bs], you really are just gorgeous!"
    bs "You're not so bad yourself."
    "She saunters by you, wiggling her cute ass as she walks."
    scene basement 9am 026l
    pov "Are you flirting with me?"
    bs "<giggle>"
    povi "I love what's gotten into her when she's down here with me."
    scene basement 9am 027l
    bs "Oh?"
    pov "I see you're thinking about taking another sex-drug aren't you?"
    bs "Maybe, do you want me to?"
    pov "Yes. But only if you want to."
    scene basement 9am 028l
    bs "I do like how they make me feel when you touch me..."
    pov "It's up to you..."
    scene basement 9am 029l
    bs "I wouldn't mind a boost today, if I'm with you to help me take care of the urges."
    pov "Sounds like you want to take one then."
    scene basement 9am 030l
    bs "Would be terrible if I did? I don't want to become addicted."
    pov "I don't think it would hurt anything if you did. Like I said, the side effect are minimal and we're not down here all the time."
    scene basement 9am 031l
    pov "Plus it is nice to be able to make you orgasm with just my lips on yours..."
    bs "Hnng..."
    scene basement 9am 032l
    bs "Ok, I think I'll take one this time. Are you sure it's ok to just take them though? Shouldn't we pay for them?"
    pov "No it's fine. Think of it as a gang member privilege."
    scene basement 9am 033l
    bs "Hmm..."
    pov "There it goes into that cute little mouth of yours. I'm almost jealous."
    scene basement 9am 034l
    bs "<giggle>"
    pov "You're such a tease!"
    bs "Hm..."
    scene basement 9am 035l
    bs "<gulp>"
    pov "..."
    pov "That's my girl."
    scene basement 9am 036l
    bs "You really do want me as your girl don't do?"
    pov "Of course I do..."
    bs "Well we're all alone down here and I just took a sex-drug to get horny..."
    pov "<gulp> Oh..."
    bs "Kind of makes me your girl, for right now at least. <wink>"
    povi "This is awesome! She's so into this basement stuff!"
    scene basement 9am 037l
    bs "I do love being down here with you... You make me feel so safe and loved."
    bs "Let's have some fun together."
    bs "<giggle>"
    pov "So did you want to make out?"
    if inc == True:
        bs "Yes, brother!"
    else:
        bs "Yes, [pov]!"
    scene basement 9am 038l
    bs "And I'll let you choose how you want to please me, <giggle>"
    bs "But please don't overdo it."
    pov "I'll be a gentleman until you beg me for more, haha."
    povi "So, how should I please her?"
    call screen casbasementlovechooserep

#----- Custom -----
screen casbasementlovechooserep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlovechooserep'), Jump('casbasementlovekissrep')) hovered tt.Action ("Kiss her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlovechooserep'), Jump('casbasementlovetitsrep')) hovered tt.Action ("Play with her tits") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementlovekissrep:
    pov "I know exactly what you like."
    scene basement 9am 039lk
    bs "Huh?"
    pov "<kiss>"
    bs "Hmm..."
    "You french kiss her."
    bs "<giggle>"
    scene basement 9am 040lk
    "You continue to play with her tongue."
    bs "Hmm...!"
    pov "<kiss> <lick>"
    scene basement 9am 041lk
    bs "Hah... Hnng..."
    pov "You like it so much. Being held and kissed. Playing with our tongues like this!"
    bs "Yes... you're right."
    pov "<lick> <kiss>"
    bs "Hah, I'm feeling so hot."
    pov "It was your choice to take the drug..."
    bs "Yes... hah... and feels so good."
    scene basement 9am 042lk
    bs "Hah... Hnng..."
    if inc == True:
        bs "Hold me tighter, brother!"
    else:
        bs "Hold me tighter, [pov]!"
    pov "Oh I won't let you go. <lick>"
    bs "Oh god? Hnng..."
    "She's trembling like crazy."
    pov "Oh, so the drug feels that good?"
    bs "HNN... HNNG..."
    povi "Did she really just have an orgasm? Is the drug that good?"
    scene basement 9am 043lk
    bs "Hah... hah..."
    pov "You didn't really...?"
    bs "<giggle> You made me cum from just kissing and licking me."
    pov "Wow! But now you understand that you could go crazy on these things very quickly."
    bs "Yes I do. But you enjoyed that too right?"
    pov "I did, but maybe next time we try it without the drug, I can get you that orgasm on my own!"
    bs "<giggle> Maybe..."
    pov "I love you [bs]."
    scene basement 9am 044lk
    bs "You're such a gentleman. You didn't even take advantage of me in this situation."
    pov "Hmm... Well, I did make you cum, doesn't sort of count as taking advanage?"
    bs "But you held back like I asked."
    povi "I don't get it. Is it that she came and I didn't? What does that matter?"
    bs "Come here [pov]. It's your turn."
    scene basement 9am 045lk
    pov "My turn...?"
    bs "Since you like my mouth and tongue so much I'll reward you with them."
    pov "Oh, you're going to...?"
    bs "Yes, and I can feel your hard dick through your pants."
    scene basement 9am 046lk
    bs "So the drug affected you too, <giggle>"
    pov "It was more your sweet taste and cumming in my arms that did it."
    bs "So big and hard..."
    scene basement 9am 047lk
    bs "It's time you cum too, <giggle>"
    pov "I'm excited to feel your lips and your tongue again."
    scene basement 9am 048lk
    bs "<lick>"
    pov "Oh god yes! Amazing!"
    bs "You're burning hot."
    pov "It's your wet tongue, it's driving me crazy."
    bs "Hmm..."
    scene basement 9am 049lk
    pov "Hah..."
    bs "<lick> <suck>"
    pov "You're doing so good, this is the best reward."
    povi "I didn't know that she could suck so good. Is that a good or bad thing? Fuck it, it's good. Definitely a good thing!"
    bs "Hmm... <slurp>"
    pov "This is too good, I'm going to cum soon if you keep at that pace though!"
    "She starts to lick you faster."
    pov "Watch out or I'll cum in your mouth."
    bs "Hmm..."
    povi "She doesn't seem to mind? Does she want me to cum in her mouth?"
    scene basement 9am 050lk
    pov "This is too much, hnng...!"
    "You cum in her mouth."
    if inc == True:
        pov "Oh yes, big sis!"
    else:
        pov "Oh yes, [bs]!"
    bs "Hmm..."
    bs "<gulp> <gulp>"
    povi "Wow, she's swallowing it."
    scene basement 9am 051lk
    pov "You... you swallowed it."
    bs "Hmm... I wanted to taste you."
    pov "And was it good?"
    bs "Yes."
    if inc == True:
        bs "You taste surprisingly good, little brother."
        pov "I still can't believe it that you sucked me off, big sis."
    else:
        bs "You taste surprisingly good, [pov]."
        pov "I still can't believe it that you sucked me off, [bs]."
    bs "<giggle> You earned it yourself, like I said before."
    pov "Maybe I can earn another one?"
    bs "Haha, maybe..."
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ basecasfirst = True
    jump kitchen

#----- Custom -----
label casbasementlovetitsrep:
    pov "I need to play with your breasts!"
    scene basement 9am 039lt
    bs "Oh! So you like my big boobs do you?"
    pov "Oh yes, they're fantastic."
    pov "And they're so weighty in my hands."
    bs "<giggle> Is that a compliment?"
    pov "More than that, like a profession of love."
    bs "<giggle>"
    pov "Let's undress."
    scene basement 9am 040lt
    if inc == True:
        bs "Relax brother. No need to rip this top. We have time."
    else:
        bs "Relax [pov]. No need to rip this top. We have time."
    pov "There they are. So wonderful."
    bs "You're hands are all over them."
    pov "You'll love it when I kneed and play with them."
    scene basement 9am 041lt
    bs "Hah..."
    pov "See? And your rings are perfect for pull on."
    bs "Hmm..."
    if inc == True:
        pov "Your boobs are really wonderful, big sis."
    else:
        pov "Your boobs are really wonderful, [bs]."
    bs "And your hands are feeling really good too."
    scene basement 9am 042lt
    bs "Hah... hnn..."
    pov "Does it feel that good?"
    bs "You were right. With those drugs, the feeling is intense."
    pov "Then you'll love what I can do to your boobs."
    bs "Yes please, hah... don't stop!"
    scene basement 9am 043lt
    pov "<kiss> <suck>"
    bs "Oh my god! Yes!"
    if inc == True:
        pov "You're trembling, big sis."
    else:
        pov "You're trembling, [bs]."
    bs "I can't believe it, hah... ahhh..."
    bs "More!"
    "You bite her nipple gently."
    bs "Ahhh... hah... hnng..."
    povi "Is the drug so strong that she came from playing with her tits? Amazing!"
    bs "Hmm... that was so good."
    pov "Man I love your tits, [bs]."
    scene basement 9am 045lt
    bs "You did such a good job with my boobs, I think you've earned a reward."
    pov "A reward? Now I'm curious."
    if inc == True:
        bs "Come to me, brother."
    else:
        bs "Come to me, [pov]."
    scene basement 9am 046lt
    "She has you lay down on the table."
    bs "So it's perfect. You pleasured me with my boobs and now I'll pleasure you with them."
    pov "You mean... a... boob-job?"
    bs "You already know the name for it?"
    if inc == True:
        bs "<giggle> Kinky little brother."
    else:
        bs "<giggle> Kinky [pov]."
    scene basement 9am 047lt
    bs "Your dick is burning between my breasts."
    pov "It's like a dream come true. Feeling them around my cock."
    bs "I want you to enjoy what's coming."
    if inc == True:
        pov "Oh, I will, big sis."
    else:
        pov "Oh, I will, [bs]."
    bs "<giggle>"
    scene basement 9am 048lt
    pov "Ohhh..."
    povi "Feeling her boobs and her tongue on my dick!"
    bs "<lick>"
    pov "You're the best [bs]."
    bs "<kiss> <lick>"
    pov "But at this pace I won't last very much longer... hah..."
    scene basement 9am 049lt
    if inc == True:
        bs "Then you should enjoy your orgasm like I did mine, little brother."
    else:
        bs "Then you should enjoy your orgasm like I did mine, [pov]."
    pov "Oh, I will, hah..."
    "She's kneading her boobs faster on your dick."
    pov "Serious, I'm about to burst. Probably cover your whole body in sperm at this rate!"
    bs "<giggle> So you like it that much?"
    bs "Then spray it all over the boobs you love so much."
    if inc == True:
        pov "Oh big sis!"
        scene basement 9am 050lt
        pov "Sister! Hnng!"
    else:
        pov "Oh [bs]!"
        scene basement 9am 050lt
        pov "[bs]! Hnng!"
    "She closes her eyes quickly."
    bs "Hmm..."
    pov "Ohhh..."
    scene basement 9am 051lt
    bs "So much hot sperm on my boobs. I love it!"
    pov "Wow! You surprised me what you could do with your tits."
    bs "I'm proud to see you liked it that much! <giggle>"
    pov "Maybe you can surprise me more often?"
    bs "Haha, maybe..."
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ basecasfirst = True
    $ casbasecumface = False
    $ casbasecummouth = False
    $ casbasecumonass = False
    $ casbasecuminass = False
    jump kitchen

#----- Custom -----
screen casbasementlove2chooserep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlove2chooserep'), Jump('casbasementlove2bjrep')) hovered tt.Action ("Use her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlove2chooserep'), Jump('casbasementlove2assrep')) hovered tt.Action ("Use her ass") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementlove2bjrep:
    povi "Her blow-jobs are so good... I think it's time for another one."
    "You pull your dick out of your pants."
    scene basement 9am 042cb
    bs "Oh, so do you think you are you doing?"
    pov "Just getting more comfortable."
    bs "Oh..."
    scene basement 9am 043cb
    pov "Why don't you set the try down and come closer?"
    bs "Hnng..."
    pov "Why don't you show my how much you like being my girl."
    scene basement 9am 044cb
    bs "Hnn..."
    pov "Oh come on. I know you're only playing at being offended, haha."
    if inc == True:
        pov "I know you much better than you think, big sis."
    else:
        pov "I know you much better than you think, [bs]."
    scene basement 9am 045cb
    bs "Hnn..."
    pov "But I think it's time to stop playing around and just admit this is what you want."
    pov "You chose that dress yourself and you started calling yourself my girl on your own."
    pov "I want you. And clearly you want me too. Do we have to keep playing these games?"
    "She doesn't say a word, but reaches out and grabs your cock in response"
    scene basement 9am 046cb
    pov "There we go! See, it wasn't that hard. Just let loose a little."
    bs "Hnn..."
    pov "So now that you're there, what do you want to do next?"
    bs "I..."
    if inc == True:
        bs "I want to suck your dick, brother. I want to be your girl."
    else:
        bs "I want to suck your dick, [pov]. I want to be your girl."
    pov "That's good girl. Being honest with yourself finally."
    scene basement 9am 047cb
    pov "I love your warm hands on my dick."
    bs "Hmm..."
    povi "I can't wait to feel her tongue again."
    scene basement 9am 048cb
    bs "<suck> <lick>"
    pov "Yes, that's good."
    if inc == True:
        povi "Now it's time to let my big sister prove that she can give the best blow-jobs."
    else:
        povi "Now it's time to let her prove that she can give the best blow-jobs."
    scene basement 9am 049cb
    bs "Hah... <lick>"
    povi "Oh, she opening her mouth wider to give her tongue more space to play."
    if inc == True:
        pov "Your tongue is the best, big sis."
    else:
        pov "Your tongue is the best, [bs]."
    if deepthroatcount >= 2: #----- if casbjdt >= 2: -----
        jump casbasementlove2dprep
    bs "<giggle> I know."
    scene basement 9am 050cb
    pov "Yes, lick it just like that. That's a good girl."
    bs "Hmm... <lick> <lick>"
    pov "You're really getting good as doing all the things I like."
    pov "I bet you don't put in so much effort when you did this with your boyfriend."
    bs "Hnng..."
    pov "Well, soon to be ex-boyfriend, right?"
    scene basement 9am 051cb
    bs "<suck>"
    pov "Haha, I'll get you to dump that loser soon enough!"
    bs "Hmm..."
    scene basement 9am 052cb
    pov "Oh you stopped..."
    bs "You know why. <giggle>"
    pov "See, there is another reason why you're my girl."
    pov "You know exactly when I'm at my limit and need to cum."
    bs "That's true, so now where do you want me to take it."
    povi "Holy shit, she's really getting into it!"
    if inc == True:
        pov "You being such a good girl now, big sis."
    else:
        pov "You being such a good girl now, [bs]."
    $ deepthroatcount += 1
    call screen casbasementlove2cumrep

#----- Custom -----
screen casbasementlove2cumrep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlove2cumrep'), Jump('casbasementlove2cumfrep')) hovered tt.Action ("Cum on her face") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlove2cumrep'), Jump('casbasementlove2cummrep')) hovered tt.Action ("Cum in her mouth") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementlove2cumfrep:
    $ casbasecumface = True
    pov "I want to spray it on your face."
    if inc == True:
        bs "Ok, brother."
    else:
        bs "Ok, [pov]."
    "She rubs your dick furiously."
    pov "Hah, so good."
    scene basement 9am 053cbo
    pov "Hnng..."
    bs "Hmm..."
    "You cum on her face."
    scene basement 9am 054cbo
    bs "Hnn... did you like that?"
    pov "Yes, my girl. You're amazing!"
    bs "Hnng..."
    pov "But don't wipe it off yet... Good girls wear their man's cum with pride!"
    bs "Hmm..."
    jump casbasementloveendrep

#----- Custom -----
label casbasementlove2cummrep:
    $ casbasecummouth = True
    pov "I want you to taste my sperm."
    if inc == True:
        bs "Ok, brother."
    else:
        bs "Ok, [pov]."
    "She rubs your dick furiously."
    pov "Hah, so good."
    scene basement 9am 053cbi
    pov "Hnng..."
    bs "Hmm..."
    "You cum in her mouth."
    scene basement 9am 054cbi
    bs "Aah..."
    pov "Good. You know just what I want."
    povi "Wow! Is she smiling?"
    if inc == True:
        pov "Now be a good girl and swallow your brothers cum."
    else:
        pov "Now be a good girl and swallow my cum."
    scene basement 9am 055cbi
    bs "<gulp>"
    povi "She loves to swollow!"
    scene basement 9am 056cbi
    bs "Hnn... did you like that?"
    pov "Yes, my girl. You're amazing!"
    bs "Hnng..."
    jump casbasementloveendrep

#----- Custom -----
label casbasementlove2dprep:
    $ casbasecummouth = True
    scene basement 9am 051cbdt
    bs "Hnng... <suck>"
    pov "Oh yes, you know exactly what I like."
    povi "She's deep-throating me on her own."
    scene basement 9am 052cbdt
    pov "Holy shit!"
    bs "<suck> <choke>"
    povi "She took me all in! And all on her own."
    povi "Surprising me like that. I won't last long."
    bs "<suck> <choke>"
    pov "That feels so good!"
    scene basement 9am 053cbdt
    if inc == True:
        pov "I'm about to cum, big sis!"
    else:
        pov "I'm about to cum, [bs]!"
    pov "Taking me all in like that feels amazing!"
    bs "<suck> <choke>"
    pov "Just let me spray it all down your throat!"
    bs "Hmm..."
    pov "Hold it just a moment longer!"
    pov "Hnng..."
    "You spray your sperm down her throat."
    bs "<gulp> <gulp>"
    scene basement 9am 056cbi
    bs "Hah... hah..."
    pov "That was perfect."
    bs "Hnn... you liked that right?"
    pov "Yes, my girl. You're fucking amazing!."
    bs "Hnng..."
    $ deepthroatcount = 0
    jump casbasementloveendrep

#----- Custom -----
label casbasementlove2assrep:
    povi "Her ass needs a good pounding."
    pov "Why don't you put the tray on the table."
    bs "Ok..."
    scene basement 9am 042cf
    pov "So can you guess what I want to do now?"
    "You stare at her ass."
    bs "I think I have an idea..."
    scene basement 9am 043cf
    pov "You know exactly what I want to don't you?"
    pov "Because it's the same thing you want too."
    bs "Hnn..."
    pov "Get over there!"
    scene basement 9am 044cf
    bs "But don't fuck my pussy yet..."
    pov "Oh, don't worry. I won't."
    povi "Well that just leaves one option then."
    scene basement 9am 045cf
    pov "So tell me what you want me to do now..."
    bs "I can't say that!"
    pov "But how am I going to know where to put my cock then?"
    scene basement 9am 046cf
    bs "I want..."
    if inc == True:
        pov "Come on, big sis, what do you want me to do? You can say it."
    else:
        pov "Come on, [bs], what do you want me to do? You can say it."
    bs "I want you to fuck my ass!"
    bs "I want you inside me!"
    pov "There you go! That wasn't so hard was it?"
    scene basement 9am 047cfa
    pov "And don't worry. I'm going to give you a hardest pounding you've ever had. I want you to really enjoy this."
    bs "Hnn..."
    pov "But now I need you to ask for it. I love to hear you say it!"
    bs "Hnng..."
    if inc == True:
        bs "Please fuck my ass, brother."
    else:
        bs "Please fuck my ass, [pov]."
    pov "As you wish, my naughty girl."
    scene basement 9am 048cfa
    bs "Hnn..."
    "You press your tip against her asshole."
    bs "Hnn..."
    pov "I don't want you to forget the time we share down here..."
    bs "Hnn..."
    scene basement 9am 049cfa
    with vpunch
    bs "Aaaahhh...!"
    "You ram your dick completely in!"
    pov "Hnn... so tight!"
    bs "Hnng... Oh god yes!"
    if inc == True:
        pov "Just relax your muscles a bit, big sis."
    else:
        pov "Just relax your muscles a bit, [bs]."
    scene basement 9am 050cfa
    with vpunch
    "You fuck her asshole faster."
    bs "Hah... hah..."
    with vpunch
    pov "It feels like you're enjoying this as much as I am!"
    bs "Hah... hnng..."
    with vpunch
    pov "God your ass if so tight. I love it!"
    scene basement 9am 051cfa
    "You release her tits."
    pov "I love watching your tits sway as I fuck you."
    bs "Hah... your... big dick..."
    with vpunch
    pov "So you love it how my dick is filling your tight hole?"
    bs "Hah... yes... hng... please don't stop!"
    with vpunch
    scene basement 9am 053cfa
    "You pound her harder."
    with vpunch
    pov "I'm going to cum soon, your tight hole is just too fucking much."
    bs "Hah... hah..."
    with vpunch
    pov "We'll need to fuck many times more so we both can get used to it."
    bs "Hnng..."
    with vpunch
    pov "So where do you want me to put my sperm? Deep inside you or on your ass?"
    bs "Hah... hah... hnng..."
    with vpunch
    pov "Be a good girl now and tell me where to cum!"
    call screen casbasementlove2asscumrep

#----- Custom -----
screen casbasementlove2asscumrep():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlove2asscumrep'), Jump('casbasementlove2assinrep')) hovered tt.Action ("Cum inside my ass") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('casbasementlove2asscumrep'), Jump('casbasementlove2assoutrep')) hovered tt.Action ("Cum on my ass") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

#----- Custom -----
label casbasementlove2assinrep:
    $ casbasecuminass = True
    bs "Please, cum inside me!"
    pov "Hnng..."
    scene basement 9am 052cfa
    with vpunch
    bs "Ohhh... Hnn..."
    if inc == True:
        pov "You feel my hot sperm spraying inside you, big sis?"
    else:
        pov "You feel my hot sperm spraying inside you, [bs]?"
    bs "Hnng... yes..."
    with vpunch
    pov "That felt so good. You're ass is amazingly tight!"
    bs "Hah... hah..."
    scene basement 9am 053cfai
    pov "I sprayed so much inside you!"
    bs "Hnng!"
    pov "Enjoy it as long as you can, haha."
    bs "Hnn... That felt so good."
    bs "Hnng..."
    jump casbasementloveendrep

#----- Custom -----
label casbasementlove2assoutrep:
    $ casbasecumonass = True
    bs "Please, cum on my ass!"
    pov "Hnng..."
    scene basement 9am 053cfao
    bs "Ohhh... Hnn..."
    if inc == True:
        pov "You feel my hot sperm spraying on your ass, big sis?"
    else:
        pov "You feel my hot sperm spraying on your ass, [bs]?"
    bs "Hnng... yes..."
    pov "You're mine now, just like you wanted..."
    scene basement 9am 054cfao
    pov "Wonderful!"
    bs "Hnng..."
    bs "That felt so good."
    bs "Hnng..."
    jump casbasementloveendrep

#----- Custom -----
label casbasementloveendrep:
    scene black
    pov "Come, sit with me."
    if casbasecumface == True:
        scene basement 9am 060cf
    else:
        scene basement 9am 060
    pov "You did so good, so let's have those drinks now."
    pov "Aren't you happy?"
    bs "Y... yes... I am."
    pov "You even got a special gift for the occasion."
    if casbasecumface == True:
        scene basement 9am 061cf
    else:
        scene basement 9am 061
    if casbasecumface == True:
        pov "You have my sperm on your face as the proof."
    elif casbasecummouth == True:
        pov "You have  my sperm in your stomach as the proof."
    elif casbasecumonass == True:
        pov "You have my sperm on your ass as the proof."
    elif casbasecuminass == True:
        pov "You have my sperm in your ass as the proof."
    bs "Hnng..."
    if casbasecumface == True:
        scene basement 9am 062cf
    else:
        scene basement 9am 062
    bs "<gulp> <gulp>"
    if casbasecumface == True:
        scene basement 9am 063cf
    else:
        scene basement 9am 063
    pov "I'm so glad you chose that dress. So how does it feel to be my girl?"
    bs "So good. I love it."
    pov "Now you can look forward to having so much more fun with me down here."
    bs "Hnng..."
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ basecasfirst = True
    $ casbasecumface = False
    $ casbasecummouth = False
    $ casbasecumonass = False
    $ casbasecuminass = False
    jump kitchen

label temp:
    hide screen locations
    $ basealefirst = True
    scene basement 4pm 010
    pov "Well, we made it."
    ls "The basement. The \"forbidden\" place. I'm excited!"
    pov "I wonder what they do down here?"
    ls "Let's find out!"
    scene basement 4pm 011
    ls "There's so much alcohol!"
    pov "Please be careful [ls]. We should be quiet. We don't want to get caught down here."
    ls "But there is so much..."
    pov "..."
    scene basement 4pm 012
    ls "Still, I'm not interested in drinking. Otherwise I'd get stupid like you, dummy!"
    pov "I'm not like that when I'm drunk!"
    ls "Haha, you remember the time 4 years ago..."
    pov "...so you've never drunk alcohol, have you?"
    ls "No, I'm not stupid, haha..."
    scene basement 4pm 013
    ls "Look! Is that candy?"
    povi "Candy down here...? Laying out in the open on a table?"
    pov "Wait, let me see..."
    scene basement 4pm 014
    ls "Let me have it!"
    scene basement 4pm 015
    pov "Stop!"
    with vpunch
    "You slap her hand."
    scene basement 4pm 016
    ls "Ouch! Why did you do that?"
    pov "To stop you from eating it. We don't know what it is, but I'm sure it's not just candy."
    ls "But it looks like candy?"
    pov "We don't know that for sure though."
    if adatekiss == True and lilsislove >= 30:
        call screen base4lscandy
    else:
        jump base4p2

screen base4lscandy():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('base4lscandy'), Jump('base4kiss')) hovered tt.Action ("Kiss her [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('base4lscandy'), Jump('base4p2')) hovered tt.Action ("Don't kiss her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base4kiss:
    scene basement 4pm 017k
    $ lilsislove += 1
    pov "<kiss>"
    ls "Hnng...?"
    scene basement 4pm 017k1
    ls "Hmm..."
    "You kiss her longer."
    ls "<kiss>"
    scene basement 4pm 017k2
    ls "Why did you kiss me?"
    pov "To show you that I'm not mad at you."
    pov "But please don't try to take that \"candy\" any more."
    if inc == True:
        ls "Ok, big brother. <giggle>"
    else:
        ls "Ok, [pov]. <giggle>"
    jump base4p2

label base4p2:
    scene basement 4pm 018
    ls "And what's in here?"
    ls "Oh, just a toilet."
    pov "Let me see too."
    scene basement 4pm 019
    pov "Gross, it's quite dirty."
    ls "Look! That's interesting..."
    scene basement 4pm 020
    povi "What did she find now?"
    ls "But why is this here?"
    pov "Let me see."
    scene basement 4pm 021
    povi "A changing room? What are they doing down here?"
    ls "Ugh!"
    ls "<giggle>"
    pov "So are you having fun down here?"
    if inc == True:
        ls "I'm just wondering why mom said I couldn't go in here?"
    else:
        ls "I'm just wondering why my mom said I couldn't go in here?"
    scene basement 4pm 022
    ls "And what's with that?"
    povi "Damn, how did she get over there so fast?"
    pov "That's a vibrator. You know what that is?"
    ls "I know what a vibrator is. But why is it so big?"
    scene basement 4pm 023
    pov "Because some people like to stick bigger things in them?"
    ls "But... this one... And why is it here?"
    pov "I don't know, but maybe we can find out?"
    ls "Hnn..."
    scene basement 4pm 024
    ls "And what are these? I've never seen something like this."
    pov "Well..."
    ls "They look like instruments of torture."
    povi "Well, it's something like that, haha."
    pov "It's something for you."
    scene basement 4pm 025
    ls "For me?"
    pov "Yes, when you're bad you come in here and get tickled to death, haha."
    ls "<giggle>"
    ls "I know you're lying, so what are they for?"
    pov "They're for sex. The woman is tied up there and the man can fuck her."
    scene basement 4pm 026
    ls "For sex? Torture sex?"
    pov "More submissive sex. Some people like that."
    if inc == True:
        ls "I'm so confused, big brother. Why are they here?"
    else:
        ls "I'm so confused, [pov]. Why are they here?"
    pov "I..."
    pov "Oh, there's someone coming. quick let's hide."
    if NTR == True and lilsisrelationship <= 5 and davidemeet == True:
        jump base4ntr
    scene black
    "You both hide behind the bar."
    scene basement 4pm 031
    ls "Ssshhh..."
    povi "I wonder who that is. I always thought they only came down here in the late evenings."
    "You decide to take a peek."
    scene basement 4pm 032
    if inc == True:
        povi "It's mom."
    else:
        povi "It's [mother]."
    povi "And she looks so relaxed."
    mom "Hmm... <hum>"
    scene basement 4pm 033
    mom "<hum>"
    ls "<whisper> Why is she here?"
    pov "<whisper> I don't know..."
    mom "Lalala..."
    scene basement 4pm 034
    ls "<whisper> Huh?"
    "You two are hearing a louder buzzing sound."
    "<buzz>"
    ls "<whisper> What is that?"
    pov "<whisper> Let's take a peek, but very carefully."
    ls "<whisper> Ok."
    scene basement 4pm 035
    ls "<whisper> Slowly..."
    povi "Hmm... this must be an excited adventure for her..."
    if inc == True:
        povi "But now let's see what mom's doing."
    else:
        povi "But now let's see what [mother]'s doing."
    scene basement 4pm 036
    "<buzz>"
    mom "Hmm... hah... yes!"
    povi "Damn, she's riding on that Sybian and fucking herself."
    ls "<whisper> Hnng..."
    scene basement 4pm 038
    povi "Why does she look so sad?"
    pov "<whisper> What's wrong?"
    ls "<whisper> Don't you see what she's doing?"
    pov "..."
    if inc == True:
        ls "<whisper> Mom is masturbating with that thing..."
    else:
        ls "<whisper> My mom is masturbating with that thing..."
    pov "<whisper> And so what?"
    mom "Hah... yes... harder..."
    ls "<whisper> She's doing it like a slut..."
    povi "Wow, oh shit..."
    pov "<whisper> Come here..."
    scene basement 4pm 039
    ls "<whisper> Huh? What are you up to?"
    pov "<whisper> Relax, it will be ok."
    call screen base4lshide

screen base4lshide():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_love_%s.png" action (Hide('base4lshide'), Jump('base4lscalm')) hovered tt.Action ("Calm her down [lv1]") focus_mask True
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('base4lshide'), Jump('base4lsuse')) hovered tt.Action ("Use this situation [cr1]") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base4lscalm:
    scene basement 4pm 039c
    $ lilsislove += 1
    if inc == True:
        pov "<whisper> Calm down, lil sis. It's not your fault."
    else:
        pov "<whisper>Calm down [ls]. It's not your fault."
    pov "<whisper> She may enjoy doing it but it doesn't make her a slut."
    mom "Hah... hnng..."
    "<buzz>"
    if inc == True:
        ls "But she's our mom."
    else:
        ls "But she's my mom."
    pov "<whisper> Sshhh..."
    scene basement 4pm 040
    pov "<whisper> Come here. You're not going to become a slut, just because of that."
    ls "<whisper> But..."
    mom "Aaah... hah... more!"
    if inc == True:
        pov "<whisper> You're my little sister and I love you, so don't worry."
    else:
        pov "<whisper> I know you all my life and I love you, so don't worry."
    pov "<whisper> And I'm the last one who would judge you."
    ls "<whisper> But why is she doing it?"
    scene basement 4pm 041
    pov "<whisper> I don't know [ls]. That's something we need to find out."
    pov "<kiss>"
    pov "<whisper> Also it's pretty normal to have such feelings sometimes."
    ls "<whisper> Hmm..."
    "<buzz>"
    mom "Yes! Hah... Aaahh... Hnng..."
    scene basement 4pm 042
    ls "<kiss>"
    povi "Huh? She's kissing me. And it feels different then the times before."
    ls "<whisper> Hmm..."
    mom "Hnn... hnn..."
    scene basement 4pm 043
    if inc == True:
        povi "Oh my god. My little sister took advantage of the situation and is french kissing me."
    else:
        povi "Oh my god. [ls] took advantage of the situation and is french kissing me."
    ls "<lick> <kiss>"
    if inc == True:
        povi "And mom is masturbating at the same time too. This is heaven."
    else:
        povi "And [mother] is masturbating at the same time too. This is heaven."
    mom "Hah... hah... hah..."
    povi "I wonder what I did to earn something like this? Was it because I was so nice to her?"
    if inc == True:
        povi "Or is she getting horny by mom's moaning?"
    else:
        povi "Or is she getting horny by her mother's moaning?"
    scene basement 4pm 044
    ls "Hmm..."
    ls "<kiss> <lick>"
    povi "Now it's my time to just enjoy it."
    mom "Oh yes... oh yes..."
    if inc == True:
        povi "But lil sis is really kissing me in earnest. That's a little surprising."
    else:
        povi "But [ls] is really kissing me in earnest. That's a little surprising."
    scene basement 4pm 045
    ls "<giggle>"
    povi "Damn, she looks so cute right now."
    "You stare in each others eyes."
    mom "Hah... hah... AAAHHHH...!"
    povi "So she had her fun too it seems."
    ls "<whisper> Huh?"
    "The buzzing sound stops and it goes silent."
    scene basement 4pm 048
    if inc == True:
        ls "<whisper> Mom is leaving."
    else:
        ls "<whisper> My mother is leaving."
    "You got the feeling that [ls] was just overwhelmed by the situation and has now decide to stop it here."
    scene basement 4pm 045
    pov "Let's head on back. The way is clear."
    ls "Did I do something wrong."
    pov "No. It was very nice, but we will have more time later."
    ls "<giggle> So you want more of me."
    if inc == True:
        pov "Yes, because I love you, lil sis."
    else:
        pov "Yes, because I love you, [ls]."
    ls "<giggle>"
    scene black
    $ lilsisrelationship += 1
    "You leave the basement together."
    $ b4ralove = True
    $ dtime += 1
    jump frontdoor

label base4lsuse:
    pov "<whisper> I know you're right, but we need to stay silent."
    $ lilsiscorruption += 1
    ls "<whisper> Hnn..."
    pov "<whisper> She's a slut and I'm pretty sure she won't be the only one in this family."
    "<buzz>"
    mom "Hah... aahhh..."
    scene basement 4pm 040c
    ls "<whisper> What are you doing?"
    pov "<whisper> I'll show you that I'm right. That you're a slut too, you're getting horny from hear her moan."
    mom "Hah... hah... hah..."
    ls "<whisper> But..."
    scene basement 4pm 041c
    pov "<whisper> See? I was right. You nipples are stiff."
    ls "<whisper> No..."
    "<buzz>"
    mom "Hnng... aahh..."
    pov "<whisper> I'm sorry to say it, but you'll probably become a slut too."
    ls "<whisper> Hnng..."
    scene basement 4pm 042c
    pov "<whisper> See? I touch you and you're getting horny!"
    ls "<whisper> Hnng... I'm sorry..."
    pov "<whisper> There is no need to be. Just give in to your feelings."
    ls "<whisper> But... I don't want to be a slut."
    mom "Hah... aaahh... yes!"
    scene basement 4pm 043c
    pov "<whisper> Relax [ls]. You can't deny it. It's your nature."
    ls "<whisper> Hnn..."
    if inc == True:
        pov "<whisper> But you're my little sister and I won't tell anyone. It'll be our secret."
        mom "Hah... hah... hah..."
        pov "<whisper> See? You can have fun as mom does."
    else:
        pov "<whisper> But I know you all your life and I won't tell anyone. It'll be our secret."
        mom "Hah... hah... hah..."
        pov "<whisper> See? You can have fun as your mom does."
    ls "<whisper> But..."
    scene basement 4pm 044c
    ls "<whisper> Hnng...!"
    pov "<whisper> See! You're already wet."
    if inc == True:
        pov "<whisper> So trust your big brother."
    else:
        pov "<whisper> So trust me."
    ls "<whisper> Hmm... if you say so..."
    "<buzz>"
    mom "Harder, hah.. ahh..."
    pov "<whisper> Just give in to how good it feels..."
    if inc == True:
        ls "<whisper> Hnng... your fingers, big brother."
    else:
        ls "<whisper> Hnng... your fingers, [pov]."
    scene basement 4pm 045c
    pov "<whisper> Good, just enjoy it now."
    ls "<whisper> Hnng... hah..."
    pov "<whisper> But you should admit it to yourself or you won't get over it."
    mom "Aaahh... aahhh..."
    ls "<whisper> Admit... hnn... it?"
    pov "<whisper> Yes. Admit it to me and you'll feel much better."
    ls "<whisper> Hnn... but..."
    pov "<whisper> Admit it!"
    if inc == True:
        ls "Big brother... I'm... I'm a..."
    else:
        ls "[pov]... I'm... I'm a..."
    pov "<whisper> Huh?"
    "The buzzing sound stops and it's now silent."
    scene basement 4pm 048
    if inc == True:
        ls "<whisper> Mom is leaving."
    else:
        ls "<whisper> My mother is leaving."
    scene basement 4pm 045c
    povi "Damn, she almost said it."
    if inc == True:
        ls "Mom is gone... we should stop now."
    else:
        ls "My mom is gone... we should stop now."
    pov "Why? You still need to admit it. And you're enjoying it too."
    if inc == True:
        ls "No! Please brother."
    else:
        ls "No! Please [pov]."
    povi "Damn!"
    scene black
    "She frees herself and runs back through the tunnel."
    povi "I'll get her her to admit it soon."
    $ lilsisrelationship += 1
    "You also go back."
    $ b4racor = True
    $ dtime += 1
    jump frontdoor

label base4ntr:
    scene black
    "You hide behind the couch, but [ls] stays behind the bar."
    "Someone enter the room."
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene basement 4pm 031n
    povi "It's Davide. What he's doing here at this time?"
    scene basement 4pm 032n
    if inc == True:
        povi "Oh shit, he's doing something at the bar. I hope he doesn't find lil sis."
    else:
        povi "Oh shit, he's doing something at the bar. I hope he doesn't find [ls]."
    scene basement 4pm 033n
    ls "Buh!"
    davide "Huh?"
    povi "What's she doing?"
    davide "Hahaha, what a nice surprise."
    scene basement 4pm 034n
    davide "How did you get in here [ls]?"
    ls "Oh you remember me? <giggle>"
    davide "How could I forget such a hot chick!"
    ls "I found a way into the basement."
    scene basement 4pm 035n
    davide "So you came here to find out the secrets of the basement?"
    ls "Yes..."
    if davidemeetint == True:
        davide "And now you're alone with a black man. Like in one of your fantasies?"
        ls "Hnn..."
    else:
        davide "And now you're alone here with me. I have an idea about what we can do."
    povi "Damn, he's trying to get it on with her."
    davide "So come here."
    scene basement 4pm 036n
    ls "Huh?"
    davide "Holding such a beauty like you in my arms. This must be my lucky day!"
    ls "<giggle>"
    call screen base4ntrch

screen base4ntrch():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base4ntrch'), Jump('base4ntrin')) hovered tt.Action ("Interfere") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base4ntrch'), Jump('base4ntrpastart')) hovered tt.Action ("Show yourself (Darker Paths)") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base4ntrch'), Jump('base4ntrwa')) hovered tt.Action ("Just watch (Darker Paths)") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base4ntrin:
    povi "I need to do something. I don't like the way this could go."
    "You reveal yourself."
    pov "Hey!"
    scene basement 4pm 037n
    davide "Huh?"
    if inc == True:
        ls "Hey, big brother."
    else:
        ls "Hey, [pov]."
    davide "You're here too."
    pov "Yes I am."
    pov "And I don't like what I see, so we're leaving now."
    scene basement 4pm 038ni
    pov "Come on [ls], let's go."
    ls "Ok..."
    pov "Quick!"
    davide "But what if I \"want\" her to stay with me?"
    pov "We found this place by accident and maybe we shouldn't have been here."
    pov "But I'm sure you can think about what will happen if [mother] finds out that [ls] was here with you!"
    davide "Maybe I don't care!"
    pov "I can see you're bluffing. [ls], come now!"
    scene basement 4pm 039ni
    ls "Bye Davide."
    davide "We'll meet soon, honey."
    pov "Oh, I don't think so."
    scene basement 4pm 040ni
    davide "You'll get yourself into more and more trouble if you don't support the gang."
    pov "I don't care Davide. And I'm going to make sure that you'll never get your hands on her."
    davide "We'll see. This isn't over."
    scene black
    if inc == True:
        "You and your little sister leave the basement."
    else:
        "You and [ls] leave the basement."
    $ dtime += 1
    $ b4rantrdavidei = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump frontdoor

label base4ntrpastart:
    call screen checkdarkerpaths_alexis
    jump base4ntrpa

#----- Edited -----
label base4ntrpa:
    if alexis_voyeur == True:
        povi "I want him to know that I'm here too. Maybe he'll share..."
    elif alexis_ntr == True:
        povi "I want him to know that I'm here. I don't think I can stop him, but maybe he'll leave and I can step in..."
    elif alexis_revenge == True:
        povi "I want him to know that I'm here. I'm not going to let him take advantage of her!"
    else:
        povi "I want him to know that I'm here too."
    "You reveal yourself."
    pov "Hey!"
    scene basement 4pm 037n
    davide "Huh?"
    if inc == True:
        ls "Hey, big brother."
    else:
        ls "Hey, [pov]."
    davide "You're here too."
    pov "Yes I am."
    if alexis_voyeur == True:
        pov "You two having fun?"
        scene basement 4pm 038na
        davide "Yes I'll have to thank you for bringing this cutie here."
        ls "<giggle>"
        if inc == True:
            pov "So you like him too, lil sis?"
        else:
            pov "So you like him too, [ls]?"
        ls "He's so strong. <giggle>"
        davide "And you're so pure, like white chocolate!"
        davide "And it's about time we get to know each other better."
        scene basement 4pm 039na
        ls "Hmm...?"
        davide "<kiss>"
        pov "Ha, that's one way to get to know someone better."
        povi "He surprised her with a french kiss. And she seems to like it."
        scene basement 4pm 040na
        davide "I just had to do that!"
        ls "<giggle>"
        davide "You should come by more often, maybe we find you a girl too [pov]."
        pov "We'll see. That's a nice way to get to know someone, haha."
        davide "Yes, you have to do it fast and direct!"
        ls "I can still taste your saliva, <giggle>"
        scene basement 4pm 041na
        davide "And you'll soon taste some other stuff."
        if davidemeetint == True:
            davide "And you have some special interest in black dicks, I'll teach you so much."
        ls "Hnn..."
        davide "Your holes need to get plugged soon, so you'll be a happy girlfriend!"
        pov "Haha... damn!"
        ls "Hnn..."
        povi "She's so confused."
        davide "And so..."
        scene basement 4pm 042na
        davide "Damn, something is unlocking the basement door."
        ls "Plugged..."
        davide "You should leave now. It's better if we keep this a secret for now!"
        pov "Haha, afraid of [mother]?"
        davide "I won't risk losing my new holes, haha."
        ls "His holes... <giggle>"
        scene basement 4pm 043na
        davide "I'll give you some time to leave."
        davide "Make sure you come here again at night time so that I can teach you more!"
        pov "Come on let's go, [ls]."
        ls "He wants me to be his girlfriend..."
        pov "Haha, relax. Some other time."
    elif alexis_ntr == True:
        povi "I bet that got him!"
        scene basement 4pm 038na
        davide "I'll have to thank you for bringing this cutie here [pov]."
        ls "<giggle>"
        if inc == True:
            povi "Damn't it didn't work! And it looks like she likes him too! No lil sis!!!"
        else:
            povi "Damn't it didn't work! And it looks like she likes him too! No [ls]!!!?"
        ls "You're so strong Davide. <giggle>"
        davide "And you're so pure, like white chocolate!"
        davide "And it's about time we got to know each other better."
        scene basement 4pm 039na
        ls "Hmm...?"
        davide "<kiss>"
        pov "Come on, guys. That's enough. [mother] will get angry if she catches you."
        povi "Seriously, what does Davide have that I don't? Why do they keep falling for his bullshit?"
        scene basement 4pm 040na
        davide "I just had to do that!"
        ls "<giggle>"
        davide "You should come by more often, maybe we find you a girl too [pov]."
        pov "Yeah, well I... Yeah that would be good."
        davide "Yes, you need to be direct with girls like this, let them know you're interested quick or they get scooped up by someone else!"
        ls "I can still taste your saliva, <giggle>"
        scene basement 4pm 041na
        davide "And you'll soon taste some other stuff."
        if davidemeetint == True:
            davide "And you have some special interest in black dicks, I'll teach you so much."
        ls "Hnn..."
        davide "Your holes need to get plugged soon, so you'll be a happy girlfriend!"
        pov "Haha... damn!"
        ls "Hnn..."
        povi "She's so confused. Maybe she's not intested in him after all?"
        davide "And so..."
        scene basement 4pm 042na
        davide "Damn, something is unlocking the basement door."
        ls "Plugged..."
        davide "You should leave now. It's better if we keep this a secret for now!"
        povi "Haha, afraid of [mother]? That's what I thought! I'm not the only one!"
        davide "I won't risk losing my new holes, haha."
        ls "His holes... <giggle>"
        scene basement 4pm 043na
        davide "I'll give you some time to leave."
        davide "Make sure you come here again at night time so that I can teach you more!"
        pov "Come on let's go, [ls]."
        ls "He wants me to be his girlfriend..."
        pov "Yeah, we should talk about that later..."
    elif alexis_revenge == True:
        pov "Everything ok here?"
        scene basement 4pm 038na
        davide "Yeah, it was until you showed up."
        ls "<giggle>"
        if inc == True:
            povi "That laugh seemed little... forced. I wonder what my little sister has gotten into?"
            ls "I'm glad you're here, brother."
            davide "Yeah, me too kid. Just giving ya shit. I was just saying that your sister is so pure, like white chocolate!"
        else:
            povi "That laugh seemed little... forced. I wonder what [ls] has gotten into?"
            ls "I'm glad you're here, [pov]."
            davide "Yeah, me too kid. Just giving ya shit. I was just saying that [ls] here is so pure, like white chocolate!"
        davide "And that it's about time we get to know each other better."
        "[ls] tries to step away from Davide, trying to not make a big deal out of it, but he holds her hips tightly so she can't leave."
        scene basement 4pm 039na
        "Davide quickly pulls [ls] in for a kiss, her hands instictively reach up around his neck, before she realized what she was doing."
        ls "Hmm...?"
        davide "<kiss>"
        povi "Is he sticking his tongue down her mouth? Seriously, this asshole does whatever the hell he wants. That's going to stop, soon."
        scene basement 4pm 040na
        davide "I just had to do that!"
        povi "Why the fuck is he talking to me about it? Is he trying to rub it in?"
        ls "..."
        davide "You should come by more often, maybe we find you a girl too [pov]."
        pov "Yeah, we'll have to see about that..."
        davide "You have to be direct with these bitches!"
        ls "I'm not a..."
        scene basement 4pm 041na
        davide "You're going to be getting more of that from now on."
        if davidemeetint == True:
            davide "I know you have some special interest in black dicks. I'll teach you so much."
        ls "No I..."
        davide "Your holes need to get plugged soon, so you'll be a happy little bitch!"
        pov "Hey Davide, you're going too far! You've had your fun already."
        ls "Yeah..."
        povi "I think she wants to leave, but might be a bit scared or just really confused. I don't think anyone's treated her like that."
        pov "I think it's time we left..."
        scene basement 4pm 042na
        davide "Damn, someone is unlocking the basement door."
        ls "Phewww..."
        davide "You should leave now. It's better if we keep this a secret..."
        pov "Haha, afraid of [mother] are we? Would be a shame if someone told her..."
        davide "Get the fuck out! I won't be risking my new holes, haha."
        ls "Ewww!"
        povi "Yeah she definitely wasn't into it. Just caught her by surpise it seems."
        scene basement 4pm 043na
        davide "I'll give you asholes some time to leave."
        davide "Make sure you come here again at night time so that I can teach you some more!"
        pov "Come on let's go, [ls]."
        ls "Yeah, I'm not coming down here at night..."
        pov "Haha, that sounds like a wise choice. Sorry he's such an asshole."
        ls "It's ok, you were here to stop him."
        povi "I wish I would have stopped him a litte sooner though."
    else: # alexis_sadist
        pov "Everything ok here?"
        scene basement 4pm 038na
        davide "Yeah, it was until you showed up."
        ls "<giggle>"
        if inc == True:
            pov "No need to be a little bitch Davide. I'm not here to spoil you're fun."
            ls "I'm glad you're here, brother."
            davide "Yeah, me too kid. Just giving ya shit. I was just saying that your sister is so pure, like white chocolate!"
        else:
            pov "No need to be a little bitch Davide. I'm not here to spoil you're fun."
            ls "I'm glad you're here, [pov]."
            davide "Yeah, me too kid. Just giving ya shit. I was just saying that [ls] here is so pure, like white chocolate!"
        davide "And that it's about time we get to know each other better."
        "[ls] tries to step away from Davide, trying to not make a big deal out of it, but he holds her hips tightly so she can't leave."
        scene basement 4pm 039na
        "Davide quickly pulls [ls] in for a kiss, her hands instictively reach up around his neck, before she realized what she was doing."
        ls "Hmm...?"
        davide "<kiss>"
        povi "Is he sticking his tongue down her mouth? Seriously, this asshole does whatever the hell he wants. I can respect that."
        scene basement 4pm 040na
        davide "I just had to do that!"
        povi "Why the fuck is he talking to me about it? Focus on the girl you have in your arms asshat."
        ls "..."
        davide "You should come by more often, maybe we find you a girl too [pov]."
        pov "Yeah, that sounds like a plan I can get behind."
        davide "You have to be direct with these bitches!"
        ls "I'm not a..."
        scene basement 4pm 041na
        davide "You're going to be getting more of that from now on."
        if davidemeetint == True:
            davide "I know you have some special interest in black dicks. I'll teach you so much."
        ls "No I..."
        davide "Your holes need to get plugged soon, so you'll be a happy little bitch!"
        pov "Haha! She could use it!"
        ls "Yeah..."
        povi "I think she wants to leave, but might be a bit scared or just really confused. It's good to know she's easily flustered. I can use that."
        pov "So what are we going to do now?"
        scene basement 4pm 042na
        davide "Damn, someone is unlocking the basement door."
        ls "Phewww..."
        davide "You should leave now. It's better if we keep this a secret..."
        pov "Haha, afraid of [mother] are we? Would be a shame if someone told her..."
        davide "Get the fuck out! I won't be risking my new holes, haha."
        ls "Ewww!"
        povi "Yeah she definitely wasn't into it. Just caught her by surpise it seems."
        scene basement 4pm 043na
        davide "I'll give you asholes some time to leave."
        davide "Make sure you come here again at night time so that I can teach you some more!"
        pov "Come on let's go, [ls]."
        ls "Yeah, I'm not coming down here at night..."
        pov "Haha, it could be more fun than you think."
        ls "I'm just glad you were here to stop him."
        povi "Yeah... stop him. That's totally what I was about to do... Bitch please. I was about to watch your ass get pounded and then take you for myself."
    scene black
    "You leave the basement together."
    $ dtime += 1
    $ b4rantrdavidey = True
    $ davidealexisfriends = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump frontdoor

label base4ntrwa:
    povi "It's better that he doesn't know that I'm here."
    povi "I need to see what she was thinking, showing herself like that."
    scene basement 4pm 037nn
    ls "Hmm...?"
    davide "<kiss>"
    povi "Oh shit!"
    call screen checkdarkerpaths_alexis
    if alexis_voyeur == True or alexis_ntr == True:
        jump base4ntrdis
    elif alexis_revenge == True:
        jump base4alerevenge
    else:
        jump base4alesadist

#----- Edited -----
label base4ntrdis:
    $ b4rantrdaviden = True
    scene basement 4pm 038nn
    if alexis_ntr == True:
        povi "She doesn't seem to enjoy getting kissed by him."
        if inc == True:
            povi "That damn asshole. Making out with my little sister."
            ls "Hnng..."
            povi "He just shoved his tongue down her throat!"
        else:
            povi "That damn asshole. Making out with [ls]."
            ls "Hnng..."
            povi "He just shoved his tongue down her throat!"
    else:
        povi "She seems surprised by his kiss."
        if inc == True:
            povi "Wow! He's making out with my little sister."
            ls "Hnng..."
            povi "He just shoved his tongue down her throat!"
        else:
            povi "Wow! He's making out with [ls]."
            ls "Hnng..."
            povi "He just shoved his tongue down her throat!"
    scene basement 4pm 039nn
    if alexis_ntr == True:
        $ b4rantrdavidey = True
        ls "Hah... hah..."
        davide "You're mine now. I've conquered you with this kiss and marked you with my salvia!"
        ls "I... was... hah... conquered..."
        povi "Don't believe this shit! He's trying to trick you."
        davide "Yeah, accept it, cutie!"
        ls "I'm... hah... yours..."
        davide "Good girl!"
    else:
        $ b4rantrdavidey = True
        ls "Hah... hah..."
        davide "You're mine now. I conquered you with this kiss and marked you with my salvia!"
        ls "I... was... hah... conquered..."
        povi "Damn, what an aggressive play. I like it."
        davide "Yeah, accept it, cutie!"
        ls "I'm... hah... yours..."
        davide "Good girl!"
    scene basement 4pm 040nn
    ls "Yes, I'm a good girl. <giggle>"
    davide "It wasn't supposed to go this way, but you'll learn that soon enough."
    if alexis_ntr == True:
        if inc == True:
            povi "No! Stop trying to corrupt my little sister!"
        else:
            povi "No! Stop trying to corrupt her!"
    else:
        povi "She seem to like this game."
    davide "So not that you're mine now, I should start teaching you, shouldn't I?"
    ls "<giggle> And what's my first lesson?"
    if alexis_ntr == True:
        povi "There has to be something I can do to stop this..."
    scene basement 4pm 041nn
    davide "Let's not waste time, you need to meet the toy that'll plug your holes soon!"
    if davidemeetint == True:
        davide "And because I know that you have a weakness for me, I'm sure it'll make you very happy!"
    ls "Your toy?"
    if alexis_ntr == True:
        povi "No, she's so innocent. Don't take that away!"
    else:
        povi "Haha, she's so damn innocent."
    scene basement 4pm 042nn
    davide "Yes my dick will conquer each of your holes and mark them as mine!"
    ls "Ohhh..."
    davide "You're eager to see it, aren't you? You look very interested!"
    scene basement 4pm 043nn
    ls "Oh my god! It's so big!"
    ls "<biting her finger>"
    davide "Now go on and explore it more. You should know what will enter you!"
    if alexis_ntr == True:
        povi "Stop... Please..."
    ls "But it's so big. Wouldn't it hurt?"
    davide "The first time maybe, until your holes are widen enough for it."
    davide "But as soon as I plug you, you'll get addicted."
    ls "Addicted? <giggle>"
    scene basement 4pm 043nnn
    ls "Oh..."
    davide "What's wrong?"
    ls "It's so hard and hot!"
    davide "Yes because it wants to enter you badly."
    scene basement 4pm 044nn
    ls "I'm a little bit scared."
    davide "Of my big cock, haha?"
    ls "It'll never fit inside me..."
    davide "Oh it will. It may not be easy for you, but as a good girl you must endure it."
    ls "Then I I'm going try to be... a good girl..."
    scene basement 4pm 045nn
    davide "Oh shit..."
    ls "What...?"
    davide "Someone is unlocking the basement door!"
    ls "Ohh..."
    if alexis_ntr == True:
        povi "Thank god!"
    else:
        povi "Damn. I would watch this."
    scene basement 4pm 046nn
    davide "I'll go and give you some time to leave. It's better when no one knows that you're here."
    davide "Make sure you come here again at night time so that I can teach you more!"
    ls "Ok. I can do that!"
    davide "Ok, see you then, my girl."
    ls "I hope so, my boy. <giggle>"
    scene basement 4pm 047nn
    if inc == True:
        "Davide goes to the stairs and your little sister leaves the basement."
    else:
        "Davide goes to the stairs and [ls] leaves the basement."
    povi "Why did she do that? She knew that I was here too?"
    scene black
    "After Davide went upstairs you leave the basement too."
    if inc == True:
        "Your little sister was no where to be found."
    else:
        "[ls] was no where to be found."
    $ dtime += 1
    $ davidealexisfriends = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump frontdoor

#----- Added -----
label base4alerevenge:
    $ b4rantrdaviden = True
    scene basement 4pm 038nn
    povi "She doesn't seem to enjoy getting kissed by him."
    if inc == True:
        povi "That damn asshole. Making out with my little sister."
        ls "Omph..."
        povi "He just shoved his tongue down her throat!"
    else:
        povi "That damn asshole. Making out with [ls]."
        ls "Omph..."
        povi "He just shoved his tongue down her throat!"
    scene basement 4pm 039nn
    ls "Hey... stop..."
    davide "You're mine now. I've conquered you with this kiss and marked you with my salvia!"
    ls "No... I wasn't... bleh... conquered..."
    povi " Don't believe this shit! He's trying to trick you."
    davide "Yeah, accept it, cutie!"
    ls "I'm... not... yours..."
    povi "Good she's not falling for it!"
    scene basement 4pm 040nn
    davide "You better start playing along girl, or I'm going to hurt [pov] or maybe [mother]!"
    povi "Davide, you piece of shit! I'm the one that's going to be hurting you soon!"
    ls "Yes, I'm... a good girl."
    davide "It wasn't supposed to go this way, but you'll learn that soon enough."
    if inc == True:
        povi "No! Stop trying to corrupt my little sister!"
    else:
        povi "No! Stop trying to corrupt her!"
    davide "So then you're mine now, I should start teaching you, shouldn't I?"
    ls "I guess so... what do I have to learn?"
    povi "Don't you dare, motherfucker! I'm going get you asshole!"
    scene basement 4pm 041nn
    davide "To not waste my time. You need to be introduced to the toy that'll plug your holes soon!"
    if davidemeetint == True:
        davide "And because I know that you have a weakness for me, I'm sure it'll make you very happy!"
    ls "Your toy?"
    povi "No, she's so innocent. Don't take that away!"
    scene basement 4pm 042nn
    davide "Yes my dick will conquer each of your holes and mark them as mine!"
    ls "..."
    davide "You're eager to see it, aren't you? You look very interested!"
    povi "I'll kill you!"
    scene basement 4pm 043nn
    ls "Whatever you want..."
    ls "<biting her finger>"
    povi "She's doing a good job in making him believe she's into it, but I know she does that when she's uncomfortable."
    davide "Now go on and explore it more. You should know what will enter you!"
    povi "Stop..."
    ls "But it's so big. Wouldn't it hurt?"
    davide "The first time maybe, until your holes are widen enough for it."
    davide "But as soon as I plug you, you'll get addicted."
    ls "Addicted..."
    scene basement 4pm 043nnn
    ls "Oh..."
    davide "What's wrong?"
    ls "It's hard... and warm..."
    davide "Yes because it wants to enter you badly."
    povi "I don't know how much of this I can watch! But I can't leave her alone with him either!"
    scene basement 4pm 044nn
    ls "I'm a little bit scared."
    davide "Of my big cock, haha?"
    ls "I don't want... I don't think it... will fit."
    davide "Oh it will. It may not be easy for you, but as a good girl you must endure it."
    povi "Grrr..."
    ls "A good girl..."
    scene basement 4pm 045nn
    davide "Oh shit..."
    ls "What...?"
    davide "Someone is unlocking the basement door!"
    ls "Ohh..."
    povi "Thank god!"
    scene basement 4pm 046nn
    davide "I'll go and give you some time to leave. It's better when no one knows that you're here."
    davide "Make sure you come here again at night time so that I can teach you more!"
    ls "Just don't hurt anyone, ok?"
    davide "Ok, see you then, my girl."
    ls "...ok."
    povi "That's not good. She doesn't understand how serious this is! She's trying to help, but this is too much!"
    scene basement 4pm 047nn
    if inc == True:
        "Davide goes to the stairs and your little sister leaves the basement."
    else:
        "Davide goes to the stairs and [ls] leaves the basement."
    povi "Why did she do that? She knew that I was here too?"
    scene black
    "After Davide went upstairs you go to leave the basement too."
    "You find [ls] in the tunnel, waiting for you."
    scene basement 4pm 038
    pov "Hey, there you are. Are you ok?"
    if inc == True:
        ls "I'm so sorry big brother!"
    else:
        ls "I'm so sorry [pov]!"
    ls "I had to play along overwise he said he would hurt you."
    pov "Why did you show yourself to him?"
    ls "I just thought you were exaggerating about him..."
    "She looks like's going to start crying at any moment."
    pov "Hey! It's ok. We'll figure something out. I won't let him hurt you."
    if inc == True:
        ls "...ok. Thank you big brother."
    else:
        ls "...ok. Thank you [pov]."
    $ dtime += 1
    $ davidealexisfriends = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump frontdoor

#----- Added -----
label base4alesadist:
    $ b4rantrdaviden = True
    scene basement 4pm 038nn
    povi "She doesn't seem to enjoy getting kissed by him."
    ls "Omph..."
    scene basement 4pm 039nn
    ls "Hey... stop..."
    davide "You're mine now. I've conquered you with this kiss and marked you with my salvia!"
    ls "No... I wasn't... bleh... conquered..."
    povi "I'm pretty sure those are the rules, [ls]"
    davide "Yeah, accept it, cutie!"
    ls "I'm... not... yours..."
    povi "Haha!"
    scene basement 4pm 040nn
    davide "You better start playing along girl, or I'm going to hurt [pov] or maybe [mother]!"
    povi "Hey, don't bring me into this now! Just because you can't control your women."
    ls "Ok, ok! Yes, I'm... a good girl."
    davide "It wasn't supposed to go this way, but you'll learn that soon enough."
    if inc == True:
        povi "Who knew it would be so easy to corrupt my little sister?"
    else:
        povi "Who knew it would be so easy to corrupt [ls]?"
    davide "Since you're mine now, I should start teaching you, shouldn't I?"
    ls "I guess so... what do I have to learn?"
    povi "Hmm... that's a good question. I wonder where he will start?"
    scene basement 4pm 041nn
    davide "To not waste my time. You need to be introduced to the toy that'll plug your holes soon!"
    if davidemeetint == True:
        davide "And because I know that you have a weakness for me, I'm sure it'll make you very happy!"
    ls "Your toy?"
    povi "Well, that makes sense."
    scene basement 4pm 042nn
    davide "Yes my dick will conquer each of your holes and mark them as mine!"
    ls "..."
    davide "You're eager to see it, aren't you? You look very interested!"
    povi "I would say more like mildly interested, but I'm sure in your world Davide, thats a lot more than normal."
    scene basement 4pm 043nn
    ls "Whatever you want..."
    ls "<biting her finger>"
    povi "Haha! She's trying to make him believe it, but I know she does that when she's uncomfortable. Makes this even better."
    davide "Now go on and explore it more. You should know what will enter you!"
    povi "True."
    ls "But it's so big. Wouldn't it hurt?"
    davide "The first time maybe, until your holes get wide enough for it."
    davide "But as soon as I plug you, you'll get addicted."
    ls "Addicted..."
    scene basement 4pm 043nnn
    ls "Oh..."
    davide "What's wrong?"
    ls "It's hard... and warm..."
    davide "Yes because it wants to enter you badly."
    povi "He's taking forever. Just fuck her already!"
    scene basement 4pm 044nn
    ls "I'm a little bit scared."
    davide "Of my big cock, haha?"
    ls "I don't want... I don't think it... will fit."
    davide "Oh it will. It may not be easy for you, but I know you want to be a good girl, so you'll endure it."
    povi "Better..."
    ls "A good girl..."
    scene basement 4pm 045nn
    davide "Oh shit..."
    ls "What...?"
    davide "Someone is unlocking the basement door!"
    ls "Ohh..."
    povi "Seriously?! Talk about anticlimactic."
    scene basement 4pm 046nn
    davide "I'll go and give you some time to leave. It's better when no one knows that you're here."
    davide "Make sure you come here again at night time so that I can teach you more!"
    ls "Just don't hurt anyone, ok?"
    davide "Ok, see you then, my girl."
    ls "...ok."
    povi "Maybe I will see if I can get her to play with me instead."
    scene basement 4pm 047nn
    if inc == True:
        "Davide goes to the stairs and your little sister leaves the basement."
    else:
        "Davide goes to the stairs and [ls] leaves the basement."
    scene black
    "After Davide went upstairs you go to leave the basement too."
    "You find [ls] in the tunnel, waiting for you."
    scene basement 4pm 038
    pov "Hey, there you are."
    if inc == True:
        ls "I'm so sorry big brother!"
    else:
        ls "I'm so sorry [pov]!"
    ls "I had to play along overwise he said he would hurt you."
    pov "Why did you show yourself to him in the first place then?"
    ls "I just thought you were exaggerating about him..."
    "She looks like's going to start crying at any moment."
    pov "Hey! It's ok. We'll figure something out. I won't let him hurt you."
    povi "Unless I get bored..."
    if inc == True:
        ls "...ok. Thank you big brother."
    else:
        ls "...ok. Thank you [pov]."
    $ dtime += 1
    $ davidealexisfriends = True
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump frontdoor

label basementlook:
    hide screen locations
    scene black
    povi "It's no use. I can't see anything."
    jump basement

label basementopen:
    hide screen locations
    scene intro 071
    if NTR == True:
        povi "Damn, locked again. I need to get in there and find out what they're doing."
    else:
        povi "It's locked. Why? Are they hiding something down there?"
    jump basement

label basementtalk:
    hide screen locations
    if inc == True:
        pov "Mom? Are you down there?"
    else:
        pov "[mother]? Are you down there?"
    mom "Yes honey. I'm in the basement."
    pov "Can you let me in? I want to check it out too."
    mom "No! Sorry! But it's the gangs hideout."
    mom "It's only for gang members!"
    pov "What the fuck?"
    if inc == True:
        mom "Sorry [pov], but I had to promise your dad. Your sisters aren't allowed down there either."
    else:
        mom "Sorry [pov], but I had to promise Bruce. My daughters aren't allowed down there either."
    if NTR == True:
        if inc == True:
            povi "I need to get down there and find out what they were doing to my mom the night I came home."
        else:
            povi "I need to get down there and find out what they were doing to [mother] the night I came home."
    elif hardntr == True:
        povi "I have to get down there and find out what happened the night I came home."
    else:
        povi "Seriously, that's messed up."
    povi "But now I just want to know more about that hideout!"
    $ momrelationship += 1
    $ dtime += 1
    $ basementnicole4pmfirst = True
    jump basement

#----- Nicole Basement - Drug/Love/Corruption Event -----
label base10pmnic:
    hide screen locations
    $ basenicfirst = True
    scene basement 10pm 040
    "As you enter the basement [mother] is already waiting for you."
    mom "There you are. I have something for you."
    scene basement 10pm 041
    mom "It's my favourite drink and I want you to taste it too."
    pov "Oh, I haven't seen you drink this before."
    mom "Yes, it's tasty but a little bit too strong and I don't want [bs] or [ls] to try drink it too."
    pov "Oh, I understand."
    scene basement 10pm 043
    mom "See? All blue."
    pov "Hm..."
    povi "A blue drink that has a strong effect. And she wants to drink even more."
    povi "Maybe it's time to use the sex-drug on her, since we're already alone in the basement."
    call screen base10pmnicdrug

screen base10pmnicdrug():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('base10pmnicdrug'), Jump('base10pmnicdrugy')) hovered tt.Action ("Drug her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('base10pmnicdrug'), Jump('base10pmnicdrugn')) hovered tt.Action ("Don't drug her") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmnicdrugy:
    $ momcorruption += 1
    $ momdrug = True
    $ momdrugfirst = True
    povi "I want to test the drug on her."
    pov "What's the name of this drink?"
    scene basement 10pm 042
    mom "Let me see."
    "You put the drug in her glass."
    povi "Good and it's already dissolved because of the carbonic acid in it."
    mom "The name is \"Blue orgasm\". And that's the best name for it!"
    if inc == True:
        pov "Oh you have no idea, mom."
    else:
        pov "Oh you have no idea, [mother]."
    scene basement 10pm 044
    mom "Cheers!"
    "You taste yours too."
    pov "Hm... not bad."
    "She she takes a large drink from hers."
    scene basement 10pm 045
    mom "Oh, so good! What do you think?"
    pov "It's good. Maybe a little sweet, but still okay for me."
    mom "<giggle>"
    mom "I'm glad you like it too."
    scene basement 10pm 046
    mom "Huh?"
    "She drop her glass."
    povi "Damn, did she catch me?"
    mom "Something is wrong?"
    if inc == True:
        pov "What's wrong mom?"
    else:
        pov "What's wrong mother?"
    scene basement 10pm 047
    mom "Oh my god! Urgh!"
    pov "Are you not feel well?"
    mom "My stomach..."
    scene basement 10pm 048
    mom "Excuse me [pov]!"
    povi "Damn, that's not good. Maybe mixing the drug with the drink was a bad idea."
    "She runs into the toilet."
    scene basement 10pm 049
    mom "Barf! Urgh!"
    povi "Well now I fee like a piece of shit. At least she was able to get out of her dress so she won't ruin it."
    if inc == True:
        pov "Are you okay, mom?"
    else:
        pov "Are you okay, [mother]?"
    povi "I need to get closer, she can't hear me."
    scene basement 10pm 050
    mom "Urgh! Urgh!"
    if inc == True:
        pov "Are you okay mom?"
        mom "Yes, I'm so sorry [pov]."
    else:
        pov "Are you okay [mother]?"
        mom "Yes, I'm so sorry [pov]."
    povi "Damn, no fun for us today..."
    povi "Or... I could just try fuck her."
    povi "Because that is obviously the only other choice here..."
    call screen base10pmnictfchoose

screen base10pmnictfchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('base10pmnictfchoose'), Jump('base10pmnicdrugf')) hovered tt.Action ("Take advantage and fuck her [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('base10pmnictfchoose'), Jump('base10pmnicdrugnf')) hovered tt.Action ("Leave her alone") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmnicdrugnf:
    povi "No, that would be too cruel."
    pov "Are you okay? Can I do something for you?"
    mom "No, it's alright [pov]. I just need some more time."
    mom "And I'm really sorry! I don't know why this happening now."
    pov "It's ok. Please tell me if you need something."
    mom "I will. But you can go now if you want, I'm feeling a little uncomfortable with that situation right now."
    pov "OK. Get well."
    scene black
    "You leave the basement."
    jump basement

label base10pmnicdrugf:
    $ momcorruption += 1
    $ momtoiletfuck = True
    povi "I'll have my fun with her now. She's not in much of a position to stop me really."
    scene basement 10pm 051
    "You pull her g-string down."
    mom "What's happening? Something feel weird."
    if inc == True:
        pov "I don't know mom. Nothing happened."
    else:
        pov "I don't know [mother]. Nothing happened."
    mom "But... Urgh! Barf!"
    povi "Good, she's distracted again."
    scene basement 10pm 052
    "You pull your dick out."
    povi "So it's my time to have some fun with her! It is my right as a gangmember!"
    povi "But which hole should I choose?"
    call screen base10pmnictfhole

screen base10pmnictfhole():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnictfhole'), Jump('base10pmnictfpussy')) hovered tt.Action ("Fuck her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnictfhole'), Jump('base10pmnictfass')) hovered tt.Action ("Fuck her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmnictfass:
    povi "I need to do fuck her asshole!"
    $ momtoiletfuckass = True
    jump base10pmnictfpussy

label base10pmnictfpussy:
    if momtoiletfuckass == False:
        povi "I need to do fuck her pussy!"
    scene basement 10pm 053
    mom "AHH!"
    if momtoiletfuckass == False:
        povi "Damn, she's so wet, I could slide so easy in her."
    mom "What are you...?"
    scene basement 10pm 054
    mom "Are you crazy? You're fucking me."
    if inc == True:
        pov "I couldn't resist mom. I was so horny all day."
    else:
        pov "I couldn't resist [mother]. I was so horny all day."
    mom "Oh baby we can't do that! Uhh...haa..."
    pov "I can't help it!"
    scene basement 10pm 055
    pov "And now be a good lower gangmember and enjoy the fucking!"
    mom "God yes! Please don't stop! Urgh!"
    pov "You're getting damn tight."
    if inc == True:
        pov "You're enjoying this secretly, don't you, mom?"
    else:
        pov "You're enjoying this secretly, don't you, [mother]?"
    mom "You're so mean baby."
    povi "I wonder if a rest of the drug still working?"
    "You fuck her faster."
    mom "Hah... hah..."
    pov "As I thought. You like to be fucked that way."
    mom "Yes... hah..."
    scene basement 10pm 056
    mom "Please don't stop baby. Fuck me harder, hah."
    pov "There's no way I'm stopping now. I can feel your enjoyment."
    mom "Hah, you're not wrong... don't stop, hnn..."
    povi "She's getting even more tight. She'll cum soon."
    mom "Hah, hah, [pov]."
    scene basement 10pm 057
    mom "AAHHH! HAAAH!"
    if inc == True:
        pov "Yes cum with me, mom!"
    else:
        pov "Yes cum with me, [mother]!"
    povi "I need to cum also, but where to put my sperm?"
    call screen base10pmnictfcchoose

screen base10pmnictfcchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        if momtoiletfuckass == True:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnictfcchoose'), Jump('base10pmnictfcass')) hovered tt.Action ("Cum in her ass") focus_mask True
        else:
            imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnictfcchoose'), Jump('base10pmnictfcpussy')) hovered tt.Action ("Cum in her pussy") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnictfcchoose'), Jump('base10pmnictfonass')) hovered tt.Action ("Cum on her ass") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmnictfonass:
    scene basement 10pm 058a
    if inc == True:
        pov "I'm going to mark you now, mom!"
    else:
        pov "I'm going to you now, [mother]!"
    pov "HNG!"
    mom "Ah, hah... hah..."
    pov "That was a good reward for being a gangmember, don't you think?"
    mom "Hng... hah..."
    pov "You came so hard!"
    scene basement 10pm 059a
    pov "Oh yes, I marked you good."
    mom "Hnn... Urgh!"
    jump base10pmnictfend

label base10pmnictfcass:
    scene basement 10pm 058b
    if inc == True:
        pov "Yes, take my sperm, mom!"
    else:
        pov "Yes, take my sperm, [mother]!"
    pov "HNG!"
    mom "Ah, hah... hah..."
    pov "That was a good reward for being a gangmember, don't you think?"
    mom "Hng... hah..."
    pov "You came so hard!"
    scene basement 10pm 059b
    pov "Oh yes, I came deep in your ass."
    mom "Hnn... Urgh!"
    jump base10pmnictfend

label base10pmnictfcpussy:
    scene basement 10pm 058b
    if inc == True:
        pov "Yes, take my seed, mom!"
    else:
        pov "Yes, take my seed, [mother]!"
    pov "HNG!"
    mom "Ah, hah... hah..."
    pov "That was a good reward for being a gangmember, don't you think?"
    mom "Hng... hah..."
    pov "You came so hard!"
    scene basement 10pm 059c
    pov "Oh yes, I creampied you good."
    mom "Hnn... Urgh!"
    jump base10pmnictfend

label base10pmnictfend:
    povi "She's still not doing any better, but that was good fun!"
    povi "But I should probably go now. She might get angry when she's feeling better."
    scene black
    "You leave the basement."
    $ momtoiletfuckass = False
    $ dtime += 1
    jump lroom

label base10pmnicdrugn:
    povi "No, I want to spend my time with her when she isn't drugged or having to pretend to be something she's not."
    povi "I don't need them to get into her heart."
    scene basement 10pm 044
    mom "Cheers!"
    "You taste yours too."
    pov "Hm... not bad."
    "She drank much from her glass."
    scene basement 10pm 045
    mom "Oh, so good! What do you think?"
    pov "It's good. Maybe a little too sweet, but still okay for me."
    mom "<giggle>"
    mom "I'm glad you like it too."
    if momcorruption >= momlove:
        jump base10pmniccor
    else:
        jump base10pmniclove

label base10pmniccor:
    pov "I have a idea. I want you to do something for me."
    scene basement 10pm 047c
    mom "What is it?"
    pov "Well, seeing as I'm a high-ranked gang member now, you really should be wearing something nicer for me now."
    mom "Wearing something nicer"
    pov "I'm sure there are plenty of nice outfits in that changing room."
    scene basement 10pm 048c
    mom "But I only wear them..."
    pov "I am gang member now, so you can wear them when I'm around too."
    mom "But..."
    pov "Don't worry, I'll choose something hot and sexy for you!"
    mom "I don't think..."
    pov "I know you want to, you're just a little bit confused right now."
    pov "So I'll help you."
    scene basement 10pm 049c
    pov "As a higher-ranked gang member I order you to do it."
    mom "You can't be serious."
    pov "Oh course I am. Beside the fact that you want to... now you need to."
    pov "Otherwise you'll be disobeying me and there will concsequences..."
    mom "Hm... I'll do it."
    pov "See? I knew you'd want to do it."
    scene basement 10pm 050c
    mom "Let me see..."
    pov "Oh I found something."
    pov "I choose..."
    call screen base10pmniccoroutfitchoose

#----- Edited Scene -----
screen base10pmniccoroutfitchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_red_%s.png" action (Hide('base10pmniccoroutfitchoose'), Jump('base10pmnicred')) hovered tt.Action ("Red Dress") focus_mask True
        imagebutton auto "gui/icons/icon_school_%s.png" action (Hide('base10pmniccoroutfitchoose'), Jump('base10pmnicschool')) hovered tt.Action ("School Girl") focus_mask True
        imagebutton auto "gui/icons/icon_angel_%s.png" action (Hide('base10pmniccoroutfitchoose'), Jump('base10pmnicangelcor')) hovered tt.Action ("Angel") focus_mask True
        imagebutton auto "gui/icons/icon_bunny_%s.png" action (Hide('base10pmniccoroutfitchoose'), Jump('base10pmnicbunnycor')) hovered tt.Action ("Bunny") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmnicred:
    $ base10pmnicred = True
    jump base10pmnicstart

label base10pmnicschool:
    $ base10pmnicred = False
    jump base10pmnicstart

label base10pmnicstart:
    pov "Go on, don't make me wait."
    mom "O... okay..."
    if base10pmnicred == True:
        scene basement 10pm 051cb
        mom "Is this what you wanted?"
        if inc == True:
            pov "Wow mom! You're a killer! That dress is so hot!"
        else:
            pov "Wow [mother]! You're a killer! That dress is so hot!"
        mom "Hnng..."
    else:
        scene basement 10pm 051ca
        mom "I look like a slut!"
        if inc == True:
            pov "Yes mom! But like a very sexy slut!"
        else:
            pov "Yes [mother]! But like a very sexy slut!"
        mom "Hnng..."
    pov "Come here!"
    if base10pmnicred == True:
        scene basement 10pm 052cb
    else:
        scene basement 10pm 052ca
    pov "Don't worrry, what happens here, stays here. I won't tell anyone. This is just between us."
    mom "..."
    pov "Besides, I don't want the other idiots to know about what fun we're going to have here together."
    mom "Fun..."
    if inc == True:
        mom "Humiliating your mom with slutty outfits."
    else:
        mom "Humiliating me with slutty outfits."
    pov "You're not slutty, you're extremely sexy. And you have nothing to be humilated about."
    pov "Besides, I know you haven't worn these outfits for the others. You wouldn't allow it."
    if inc == True:
        pov "So it's still just in the family."
    else:
        pov "So it's still just between us."
    pov "And I won't make you something you don't want to do. You know that."
    povi "At least for now, haha."
    mom "Hm... maybe it's ok..."
    pov "See? And now let me see a bit more."
    if base10pmnicred == True:
        scene basement 10pm 053cb
    else:
        scene basement 10pm 053ca
    pov "Incredible. You look like a model."
    mom "..."
    if inc == True:
        pov "Your legs are very beautiful, mom."
    else:
        pov "Your legs are very beautiful, [mother]."
    if base10pmnicred == True:
        scene basement 10pm 054cb
    else:
        scene basement 10pm 054ca
    mom "Hnn..."
    mom "Thank you."
    pov "I would prefer another sort of \"Thank you\", but that will work for now. No need to be shy with me."
    mom "Th... thank you."
    pov "I love the way this outfit accents your beautiful breast, shows enough to keep you interest, but not too much to spoil the fun."
    mom "Isn't that... a little too much..."
    pov "I don't this so. Besides it's the truth."
    mom "T... thank you again."
    pov "Good girl!"
    pov "Now come sit with me."
    if base10pmnicred == True:
        scene basement 10pm 055cb
    else:
        scene basement 10pm 055ca
    povi "Hm... She chose the armchair instead of sitting by me."
    povi "Maybe I need to help her open up some more."
    if inc == True:
        pov "Are you afraid of me, mom?"
    else:
        pov "Are you afraid of me, [mother]?"
    mom "Should I be?"
    pov "Haha! No, you never need to be afraid of me. I'm not going to do anything to you without your permission."
    pov "But I'll admit... it's hard not to when you're wearing something so sexy."
    if base10pmnicred == True:
        scene basement 10pm 056cb
    else:
        scene basement 10pm 056ca
    mom "I don't know if you should be saying such things to me though."
    if inc == True:
        mom "You're still my son."
    else:
        mom "You're still the son of my best friend."
    pov "You told me to honest with you. When I'm with someone as beautiful as you are, its hard not to just shout out praises!"
    mom "Hnn..."
    pov "This outfit would even be good for a date sometime."
    mom "Hm..."
    povi "Is she flustered? Looks like I'm going about this the right way."
    pov "But if it's too much, you could always just take it off..."
    if base10pmnicred == True:
        scene basement 10pm 057cb
    else:
        scene basement 10pm 057ca
    mom "What?"
    pov "Haha, I'm kidding. But I certainly wouldn't argue if you did!"
    mom "Stop that..."
    pov "Haha, see there, you laughed a little! But that did gave me another idea..."
    pov "You could dance a little for me."
    mom "What?"
    pov "Here on the table. It's the perfect way to showcase how great you look."
    if base10pmnicred == True:
        scene basement 10pm 058cb
    else:
        scene basement 10pm 058ca
    mom "Hnn... I'll do it. But I'm not a stripper."
    if inc == True:
        pov "Of course, mom."
    else:
        pov "Of course, [mother]."
    povi "Wow, she's really starting to like it. She's just going with things now."
    if base10pmnicred == True:
        scene basement 10pm 059cb
    else:
        scene basement 10pm 059ca
    povi "Oh my god. I can't wait."
    mom "You're not going to try anything crazy right?"
    pov "No, you'll choose what you want to do."
    povi "It's interesting how she asks things like that. Like she expects to be mistreated.?"
    povi "Like she has to do things against her will and perhaps that's a way to justify things like this."
    if base10pmnicred == True:
        scene basement 10pm 060cb
    else:
        scene basement 10pm 060ca
    pov "Wow..."
    if inc == True:
        pov "A good start, mom."
    else:
        pov "A good start, [mother]."
    mom "Hnn..."
    povi "Seriously, she's so stacked. And those little panties look great!"
    if base10pmnicred == True:
        scene basement 10pm 061cb
    else:
        scene basement 10pm 061ca
    pov "Wow, that top looks like it's about to burst. Feel free to let somethings loose if you want."
    mom "Hnng..."
    if inc == True:
        pov "You're a natural at this! I know you said you're not a stripper but you could be if you wanted to, mom."
    else:
        pov "You're a natural at this! I know you said you're not a stripper but you could be if you wanted to, [mother]."
    pov "This sort of fun isn't so bad, don't you think so?"
    mom "Hmm..."
    povi "She's really getting into this."
    if base10pmnicred == True:
        scene basement 10pm 062cb
    else:
        scene basement 10pm 062ca
    mom "Hnn..."
    povi "Wow that's sexy."
    pov "Amazing, just amazing."
    if base10pmnicred == True:
        scene basement 10pm 063cb
    else:
        scene basement 10pm 063ca
    pov "I feel really like a real V.I.P. here!"
    if inc == True:
        pov "You're very important to me too, mom."
    else:
        pov "You're very important to me too, [mother]."
    mom "Thank you [pov]."
    povi "Good, she's getting it now. That should help have much more fun."
    if base10pmnicred == True:
        scene basement 10pm 064cb
    else:
        scene basement 10pm 064ca
    povi "What a delightully lewd view."
    if inc == True:
        pov "I'm so proud of you, mom. Trying new things like this. So much fun!"
    else:
        pov "I'm so proud of you, [mother]. Trying new things like this. So much fun!"
    pov "I'd say you've found a new talent!"
    mom "You really liked it [pov]?"
    pov "You have no idea!"
    povi "But it's time to show her how much I like it."
    if base10pmnicred == True:
        scene basement 10pm 065cb
    else:
        scene basement 10pm 065ca
    mom "What are you doing?"
    pov "I'll show you how much I like your dancing."
    mom "But you... you..."
    "You release your dick."
    if base10pmnicred == True:
        scene basement 10pm 066cb
    else:
        scene basement 10pm 066ca
    pov "See? I like your dancing very much."
    mom "You... took out your... penis..."
    pov "Yes and the way you're looking at it tells me you don't really mind that I did."
    mom "It's... not... <stare>"
    if base10pmnicred == True:
        scene basement 10pm 067cb
    else:
        scene basement 10pm 067ca
    if inc == True:
        pov "So how about a deal, mom?"
    else:
        pov "So how about a deal, [mother]?"
    pov "I know you want to taste it, but you likely won't admit it just yet."
    pov "And that's ok. But I can give you something in return, if you are interested."
    mom "..."
    pov "You don't want to be everybodys \"darling\" in the gang and from what I have seen, Bruce won't stand up for you."
    pov "I don't know why, but he's just not strong enough. You know that."
    pov "Davide won't help you either, not that we want his help anyway. There will alway be strings attached."
    pov "So no matter what, I'm going to help you. I care about you and what happens to you."
    pov "That's never going to change. No matter what you decided to do."
    pov "I will talk davide and work out something, where they leave you and the girls alone."
    pov "But if you wanted to show me how much you appreciate my help..."
    if base10pmnicred == True:
        scene basement 10pm 068cb
    else:
        scene basement 10pm 068ca
    povi "Oh she's thinking..."
    pov "And it would be our secret of course. No one else would ever know."
    mom "Hnn..."
    if base10pmnicred == True:
        scene basement 10pm 069cbbj
    else:
        scene basement 10pm 069cabj
    pov "Very good. You're such a good girl."
    mom "Please don't tell anyone."
    pov "Of course not. Just as I said, it'll be our dirty little secret."
    povi "Damn, I can't believe I talked her into this."
    if inc == True:
        povi "My own mom is pleasuring me.."
    else:
        povi "My mom's best friend is pleasuring me."
    if base10pmnicred == True:
        scene basement 10pm 070cbbj
    else:
        scene basement 10pm 070cabj
    povi "Such beautiful eyes."
    if inc == True:
        pov "This is so good mom."
    else:
        pov "This is so good [mother]."
    mom "<lick>"
    pov "You're tongue is amazing."
    mom "I really appreciate all you do."
    pov "I'm happy to help out now that I'm home."
    if base10pmnicred == True:
        scene basement 10pm 071cbbj
    else:
        scene basement 10pm 071cabj
    pov "Oh yes!"
    mom "<suck>"
    pov "Take it in your mouth! Give me a good blowjob."
    mom "Hm... <suck>"
    if base10pmnicred == True:
        scene basement 10pm 072cbbj
    else:
        scene basement 10pm 072cabj
    pov "Ohh..."
    if inc == True:
        pov "You're so good to me, mom!"
    else:
        pov "You're so good to me, [mother]!"
    mom "<suck> <lick>"
    povi "Amazing! But should I help her?"
    call screen base10nicbjchoose

screen base10nicbjchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_corruption_%s.png" action (Hide('base10nicbjchoose'), Jump('base10pmnicdp')) hovered tt.Action ("Help her (deepthroat) [cr1]") focus_mask True
        imagebutton auto "gui/icons/icon_abort_%s.png" action (Hide('base10nicbjchoose'), Jump('base10pmnicbj')) hovered tt.Action ("Let her be") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmnicdp:
    pov "Here, let me help you!"
    if base10pmnicred == True:
        scene basement 10pm 072cbbjdp
    else:
        scene basement 10pm 072cabjdp
    mom "Hnng?"
    if inc == True:
        pov "Be a good mom and let me help you."
    else:
        pov "Be a good girl and let me help you."
    pov "I love a woman that can take all of me in her mouth."
    if base10pmnicred == True:
        image dtred_basement = Movie(channel="dtred_basement", play="images/anim/dtred_basement.webm")
        scene dtred_basement with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        image dt_basement = Movie(channel="dt_basement", play="images/anim/dt_basement.webm")
        scene dt_basement with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    pov "Good! Take me deep."
    mom "Hmm... <suck>"
    if inc == True:
        pov "I'm in heaven. My mom is deepthroating me!"
        pov "Youl make me very happy, mom."
        pov "Fulfilling your son's wish."
    else:
        pov "I'm in heaven. [mother] is deepthroating me!"
        pov "You make me very happy, [mother]."
        pov "Fulfilling my wish."
    if base10pmnicred == True:
        scene basement 10pm 074cbbjdp
    else:
        scene basement 10pm 074cabjdp
    povi "Oh yes, she can take it even deeper."
    mom "<suck> <choke>"
    pov "That is so hot. Endure it just a little bit longer. I'll cum very soon."
    if inc == True:
        povi "Deep in my mom's throat!"
        pov "Oh yes, HNG!"
        pov "I'm cumming! I'm cumming in your throat, mom!"
    else:
        povi "Deep in [mother]'s throat!"
        pov "Oh yes, HNG!"
        pov "I'm cumming! I'm cumming in your throat, [mother]!"
    mom "HNNG! <gulp> <gulp>"
    pov "Yes good. Swallow it all!"
    if base10pmnicred == True:
        scene basement 10pm 075cbbjdp
    else:
        scene basement 10pm 075cabjdp
    mom "Are you crazy? I could have choked!"
    pov "Don't play the innocent! As I pressed you down, you don't struggle."
    mom "Well... no. But you didn't ask!"
    pov "That is true. I'll be sure to ask you next time."
    if inc == True:
        pov "But it was amazing, mom."
    else:
        pov "But it was amazing, [mother]."
    pov "You did so well..."
    mom "Hnn..."
    mom "And you're going to help me, [pov]?"
    pov "Yes, don't worry. I'll help you even you decide to not help me."
    pov "But I'm glad you decided to this time."
    povi "I hope she \"decides\" to help me again! Haha!"
    jump base10pmniccorend

label base10pmnicbj:
    povi "Let's see what she's got."
    if base10pmnicred == True:
        scene basement 10pm 073cbbj
    else:
        scene basement 10pm 073cabj
    if inc == True:
        pov "Oh yes mom! Pleasure me more!"
    else:
        pov "Oh yes [mother]! Pleasure me more!"
    mom "Hmm... <suck>"
    pov "You enjoy this too, don't you?"
    mom "Hmm... yesh..."
    pov "Then I'm happy, that we can share this dirty secret."
    "She sucks you wilder."
    pov "Oh, oh."
    if inc == True:
        pov "I'm about to cum, mom!"
    else:
        pov "I'm about to cum, [mother]!"
    call screen base10pmnicbjcum

screen base10pmnicbjcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnicbjcum'), Jump('base10pmnicbjm')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnicbjcum'), Jump('base10pmnicbjf')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmnicbjf:
    if inc == True:
        pov "I going to cum on your face, mom!"
    else:
        pov "I going to cum on your face, [mother]!"
    mom "Hm..."
    if base10pmnicred == True:
        scene basement 10pm 074cbbjf
    else:
        scene basement 10pm 074cabjf
    pov "HNG! Oh yes!"
    "You cum on her face."
    if base10pmnicred == True:
        scene basement 10pm 075cbbjf
    else:
        scene basement 10pm 075cabjf
    pov "Wow!"
    mom "You came a lot."
    if inc == True:
        pov "You gave me a great blowjob, mom!"
    else:
        pov "You gave me a great blowjob, [mother]!"
    pov "You gave it your best and that is your reward."
    mom "I can feel it... on my face."
    pov "What you can do with your mouth is just amazing."
    mom "Maybe... but don't forget me."
    pov "Never. Like I said, you choose whether you thank me or not like this. Either way, I'll help you."
    povi "I hope she \"decides\" to thank me again! Haha!"
    jump base10pmniccorend

label base10pmnicbjm:
    if inc == True:
        pov "I need to cum in your mouth, mom!"
    else:
        pov "I need to cum in your mouth, [mother]!"
    mom "Hm..."
    pov "HNG! Oh yes!"
    "You cum in her mouth."
    if base10pmnicred == True:
        scene basement 10pm 074cbbjm
    else:
        scene basement 10pm 074cabjm
    povi "Oh god. She's showing me my cum."
    pov "You see how good you pleasured me? I sure came a lot."
    mom "Hnng..."
    if inc == True:
        pov "Now be a good mom and swallow my cum."
        pov "I want you to taste your son's seed."
    else:
        pov "Now be a good girl and swallow my cum."
        pov "I want you to taste your son's seed."
    if base10pmnicred == True:
        scene basement 10pm 075cbbjm
    else:
        scene basement 10pm 075cabjm
    mom "<gulp> <gulp>"
    povi "It's so much that she can't swallow it all at once."
    povi "And that lewd stare she's giving me. She liked it too, I'm sure."
    mom "<gulp>"
    if base10pmnicred == True:
        scene basement 10pm 076cbbjm
    else:
        scene basement 10pm 076cabjm
    povi "She even opens her mouth to show me that she swallowed it all. Awesome!"
    if inc == True:
        pov "Very good mom. I'm so glad you could taste me."
    else:
        pov "Very good [mother]. I'm so glad you could taste me."
    mom "I did that just for you."
    pov "And I appreciate that very much."
    mom "You came a lot."
    if inc == True:
        pov "You gave me a great blowjob, mom!"
    else:
        pov "You gave me a great blowjob, [mother]!"
    pov "You gave it your best and that is your reward."
    mom "I had to swallow many times."
    pov "What you can do with your mouth is just amazing."
    mom "Maybe... but don't forget me."
    pov "Never. Like I said, you choose whether you thank me or not like this. Either way, I'll help you."
    povi "I hope she \"decides\" to thank me again! Haha!"
    jump base10pmniccorend

label base10pmniccorend:
    scene black
    "Satisfied you leave the basement."
    $ base10pmnicred = False
    $ dtime += 1
    $ mombasementfirst = True
    jump kitchen

label base10pmnicntr:
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene livingroom 10pm 010c
    dad "But first we have to carry the bags away."
    pov "And then we can join them?"
    dad "Yes."
    scene livingroom 10pm 011c
    povi "So let's do this then."
    scene black
    $ base10pmlikentr = False
    call screen checkdarkerpaths_nicole
    if nicole_voyeur == True or nicole_ntr == True:
        $ base10pmlikentr = True
    else:
        $ base10pmlikentr = False
    jump base10pmnicntrpart2

label base10pmnicntrpart2:
    scene black
    "You carry the bags away with Bruce."
    dad "Now it's time to enter the basement."
    scene basement 10pm 012c
    if base10pmlikentr == True:
        mom "Hahaha, you're kidding me! <giggle>"
    else:
        mom "You have to be kidding me!"
    davide "No, I'm serious."
    if inc == True:
        dad "Your mother already drank a little to much again."
    else:
        dad "She already drank a little to much again."
    if momdrugfirst == True:
        povi "At least he didn't drug her."
    else:
        povi "I wonder if he drugged her too."
    dad "You have to stay strong to endure this [pov]."
    pov "Endure what?"
    povi "What is he talking about?"
    scene basement 10pm 013c
    if base10pmlikentr == True:
        mom "I'll go change. Hnnn..."
    else:
        mom "I'll go... change."
    davide "Yes, and don't make us wait!"
    davide "So it's your first time down there with the gang."
    pov "Yes..."
    davide "You'll like it, maybe not today, but soon..."
    pov "What do you mean?"
    scene basement 10pm 014c
    davide "Let's sit together so we can talk."
    pov "Ok."
    scene basement 10pm 016c
    davide "Normally we have the greatest parties in here, with women and and plenty of other fun, haha."
    pov "Other fun?"
    dad "He means the sex drugs."
    davide "Shut up Bruce! I'm talking now!"
    dad "Sorry, boss."
    pov "What you mean with normally?"
    davide "The girls are at our other party locations, you'll see them soon."
    davide "But for this time, I'll just introduce you to the gang rules for the parties."
    davide "You'll need to choose a chick for yourself soon, but you'll also be able to taste others too."
    davide "With the exception of my girl. You're only allowed to have fun with her with my permission."
    dad "Which he almost never gives."
    scene basement 10pm 015c
    davide "I said shut the fuck up!"
    dad "..."
    povi "Why is he just taking this?"
    if inc == True:
        pov "So who did you choose, dad?"
    else:
        pov "So who did you choose, Bruce?"
    davide "Oh he isn't allow to choose. He has the lowest rank so he's only allowed to watch."
    davide "And you love to watch, don't you? Loser, haha!"
    dad "..."
    povi "So he's really that kind of loser? Just watching and never standing up against Davide?"
    pov "And which girl have you chosen, Davide?"
    scene basement 10pm 017c
    davide "Oh there she is! You really take your time, girl!"
    if base10pmlikentr == True:
        mom "Yes, I needed a moment."
    else:
        mom "Sorry..."
    davide "How about you bring us some drinks now, we have to celebrate our newest gang member."
    if base10pmlikentr == True:
        mom "Sure, Davide."
    else:
        mom "Sure."
    scene basement 10pm 018c
    mom "Here, take a glass."
    if inc == True:
        pov "Thank you, mom."
    else:
        pov "Thank you, [mother]."
    pov "You wearing a pretty hot outfit there."
    if base10pmlikentr == True:
        mom "Yes, it was someone's wish."
    else:
        mom "Yes, despite my objections..."
    scene basement 10pm 019c
    mom "Here's a drink for you too."
    davide "Good I need one."
    povi "Holy shit. She isn't wearing panties with that outfit!"
    povi "With that backside open like that... Damn!"
    davide "Now come here, I need more service!"
    if base10pmlikentr == True:
        mom "Yes Davide. Let me just put this down."
    else:
        mom "Oh...ok. Just let me put this down."
    "There was a hint of sadness in her voice, but they just ignored it."
    scene basement 10pm 020c
    davide "Haha, don't look so sad loser! Your slutty wife couldn't resist any longer."
    jump base10pmnicntrhate2

label base10pmnicntrhate2:
    if base10pmlikentr == True:
        povi "He's letting Davide humiliate him."
        if nicole_voyeur == True:
            povi "Maybe that's just what he's into."
        else:
            povi "He really is a loser."
    else:
        if nicole_revenge == True:
            povi "Why doesn't he stand up? Can't we do anything to stop this!"
        else:
            "He's letting Davide humiliate him. He really is a loser."
    mom "<lick> <lick>"
    davide "She's really craving for my big dick!"
    dad "..."
    davide "So you like what I'm doing with your wife?"
    dad "..."
    scene basement 10pm 021c
    if inc == True:
        davide "Like how your slutty mother is working on my dick?"
    else:
        davide "Like how the slutty [mother] is working on my dick?"
    pov "What?"
    davide "She's my slut, you won't find a better one!"
    if nicole_revenge == True:
        povi "Fuck you, and your fucking prick!"
        if momsecret == False:
            povi "She's only doing this only because you drugged her!"
        else:
            povi "She can't even take the the drug to help her get through this!"
    else:
        povi "She's really a slut."
        if momsecret == False:
            povi "She's probably only doing this only because you drugged her anyway!"
    if inc == True:
        povi "And dad is just sitting here trying to get drunk."
    else:
        povi "And Bruce is just sitting here trying to get drunk."
    scene basement 10pm 022c
    davide "It's time for more slut!"
    if base10pmlikentr == True:
        mom "Huh?"
    else:
        mom "No please..."
    davide "What's wrong? I need your slutty pussy now!"
    mom "But you promised me that I would only have to blow you."
    davide "I don't care what I promised. I need to fuck you now!"
    if base10pmlikentr == True:
        if inc == True:
            mom "But not here with my son watching."
        else:
            mom "But not here with [pov] watching."
        if momsecret == False:
            povi "I wonder why she always so focused on not letting me watch? She shouldn't care about that when she's drugged, shouldn't she?"
        else:
            povi "And she won't let me watch that I can't see how much she's loving it to be his slut. She has no more excuses without the drug."
    else:
        if inc == True:
            mom "Please don't make my son watch."
        else:
            mom "Please don't make [pov] watch."
        if momsecret == False:
            povi "I know she doesn't want me watch, but she shouldn't care about that if she's drugged, right?"
        else:
            if nicole_revenge == True:
                if inc == True:
                    povi "Fuck, I need to save her. Drug or no drug she can't help herself. She's trying to help dad."
                else:
                    povi "Fuck, I need to save her. Drug or no drug she can't help herself. She's trying to help Bruce."
            else:
                povi "She doesn't want me to see her humilated like this. She has no idea how much that sort of thing turns me on."
    scene basement 10pm 023c
    davide "Are you kidding me? Come here now, slut!"
    mom "Please, Davide. I'll make it up to you!"
    davide "No! My dick needs a slutty pussy now!"
    scene basement 10pm 024c
    if base10pmlikentr == True:
        mom "No this isn't fair, stop it."
        davide "Is the already wet slut talking!"
        mom "It's just..."
    else:
        mom "No this isn't right, stop it."
        davide "Is the already wet slut talking!"
        mom "That's not true..."
    if nicole_revenge == True:
        povi "Just leave her alone, asshole!"
    else:
        if nicole_voyeur == True:
            povi "She's struggling but it looks like she needs a rough ride."
        else:
            povi "She's struggling but it looks like she wants a rough ride. I didn't know she was such a whore!"
    scene basement 10pm 025c
    if base10pmlikentr == True:
        mom "Hah, you're to rough!"
    else:
        mom "Stop! You're too rough!"
    davide "What you're talking about, slut? You always like it that way!"
    if inc == True:
        davide "Or you just acting because your son is watching?"
    else:
        davide "Or you just acting because [pov] is watching?"
    if base10pmlikentr == True:
        mom "No..."
    else:
        mom "We've never done this before! You fucking liar!"
    davide "Stop bitching around! And now I want you to tell your loser husband how my dick is working in you!"
    if base10pmlikentr == True:
        mom "What?"
    else:
        mom "Fuck you!"
    davide "You heard me!"
    "Davide fucks her even more roughly."
    scene basement 10pm 026c
    if base10pmlikentr == True:
        mom "Hah, hah, wait..."
        davide "Your slutty wife is all wet!"
        mom "I'm... so sorry Bruce..."
        davide "Stop lying! Your pussy is clinging on my dick!"
        mom "Hah... Ahh..."
    else:
        mom "Hah, no..."
        davide "Your slutty wife is all wet!"
        mom "I'm... I'm not!"
        davide "Stop lying! Your pussy is clinging on my dick!"
        mom "Stop... please..."
    if inc == True:
        davide "You're a bad wife and mom. Enjoying getting fucked in front of them!"
    else:
        davide "You're a bad wife. Enjyoing getting fucked in front of your husband and the son of your best friend!"
    if base10pmlikentr == True:
        mom "Hah... Ahh..."
    else:
        mom "No... Hah... ahh..."
    davide "So you need more?"
    scene basement 10pm 027c
    mom "HAH! Are you crazy? You'll tear me apart!"
    davide "I'll only fuck you harder today until you admit it to them!"
    mom "You can't be... hah... serious."
    dad "Argh!"
    if inc == True:
        povi "Is dad crying?"
    else:
        povi "Is Bruce crying?"
    davide "Yes I need to go deeper!"
    if base10pmlikentr == True:
        mom "Aahhh, hah stop. I can't hold your weight too."
    else:
        mom "Aahhh, hah stop. I can't hold your weight too. You're hurting me!"
    scene basement 10pm 028c
    if base10pmlikentr == True:
        mom "AAAHHH... HNNN..."
    else:
        mom "PLEASE... No more..."
    davide "Hah she's cumming. Your bitch wife is cumming from my hard dick!"
    if base10pmlikentr == True:
        mom "Hnng... your big dick... so deep..."
    else:
        mom "Hnng... you sick fucking dick... stop..."
    davide "So I need to reward her and release my spunk in her slutty pussy!"
    mom "Hnng... Hng..."
    scene basement 10pm 029c
    davide "Damn, that was a good rough fuck!"
    davide "And my spunk is already flooding out of her pussy."
    if base10pmlikentr == True:
        mom "Hnng..."
    else:
        mom "Nooo..."
    davide "You liked it! Now I done with her, haha!"
    davide "Stop whining around, loser!"
    davide "Even [pov] is just sitting there and staring."
    pov "..."
    if nicole_revenge == True:
        pov "I'm going to make you eat your own cock Davide."
    scene basement 10pm 030c
    davide "We'll find you a dirty whore you can fuck too, haha."
    davide "Your wife is mine!"
    if base10pmlikentr == True:
        mom "Hnng..."
    else:
        mom "Leave him alone..."
    "Still shocked you walk over to her."
    scene basement 10pm 031c
    mom "Please forgive me... [pov]."
    if base10pmlikentr == True:
        if nicole_voyeur == True:
            pov "Don't worry, I liked it."
        else:
            pov "I don't think so, you're a whore through and through."
        mom "Hnng... I'm so done..."
        scene black
        "You leave her."
    else:
        if nicole_revenge == True:
            pov "It wasn't your fault. David is going to pay."
            mom "Hnng... I'm just so done with this... I hope he dies..."
            mom "Please... go... I'll clean this up."
            scene black
            if inc == True:
                "Confused if she meant Davide or Dad, you leave her."
            else:
                "Confused if she meant Davide or Bruce, you leave her."
        else:
            pov "Don't worry, I liked it."
            mom "Hnng... I'm so done..."
            scene black
            "You leave her."
    $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump mcroom

#----- Edited Scene -----
label base10pmniclove:
    scene basement 10pm 048c
    mom "Hmm..."
    pov "Is something wrong?"
    mom "No, I was just thinking..."
    povi "What is she up to?"
    mom "Wait here, I want to show you something."
    pov "Oh, Ok."
    povi "I wonder what it is?"
    scene basement 10pm 050c
    mom "Hmm... where is it?"
    povi "She's going in the changing room..."
    mom "Just wait a moment [pov]."
    pov "Sure."
    povi "I hope it's something good."
    if momlove >= 80 and bunnyfirst == True and angelfirst == False:
        jump base10pmniclove3
    elif angelfirst == True:
        jump base10pmnicbachoose
    else:
        jump base10pmniclovebunny

label base10pmnicbachoose:
    call screen bunnyangelredschool

#----- Edited Scene -----
screen bunnyangelredschool():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_red_%s.png" action (Hide('base10pmniccoroutfitchoose'), Jump('base10pmniclovered')) hovered tt.Action ("Red Dress") focus_mask True
        imagebutton auto "gui/icons/icon_school_%s.png" action (Hide('base10pmniccoroutfitchoose'), Jump('base10pmnicloveschool')) hovered tt.Action ("School Girl") focus_mask True
        imagebutton auto "gui/icons/icon_angel_%s.png" action (Hide('base10pmniccoroutfitchoose'), Jump('base10pmniclove3')) hovered tt.Action ("Angel") focus_mask True
        imagebutton auto "gui/icons/icon_bunny_%s.png" action (Hide('base10pmniccoroutfitchoose'), Jump('base10pmniclovebunny')) hovered tt.Action ("Bunny") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmniclovebunny:
    scene basement 10pm 051la
    mom "Hey [pov]!"
    pov "Oh my god."
    mom "So you like it?"
    pov "Yes... but why..."
    mom "It's one of my favourite outfits and I wanted you to see it."
    pov "This is... wow."
    scene basement 10pm 052la
    mom "So you like bunnies?"
    pov "Oh yes, you're a very hot bunny."
    mom "<giggle> I knew you'd like it too."
    pov "The hottest Playboy bunny ever."
    mom "You and your flattery. I think nice boys deserve even more."
    scene basement 10pm 053la
    mom "How about this end? Feel free to keep up the complements! <giggle>"
    pov "Wow! You've even got a cute bunny tail."
    povi "What is she's doing? Is she flirting with me?"
    pov "You're really an adorable bunny. But is there a reason you're showing me it now?"
    scene basement 10pm 054la
    mom "I wanted to be a real Playboy bunny in the past."
    mom "And with this outfit I can be one even if I wasn't able to be one when I was young."
    if inc == True:
        pov "Oh mom. You would be the hottest playboy bunny."
    else:
        pov "Oh [mother]. You would be the hottest playboy bunny."
    pov "I bet even Hugh would come back from his grave to have you in his house."
    mom "Haha, you know all the right things to say to me."
    mom "That's why you get a treat now."
    scene basement 10pm 055la
    povi "Wow. Is she going to kiss me now? Must... behave..."
    if inc == True:
        mom "I've been feeling more and more proud of you, my son."
    else:
        mom "I've been feeling more and more proud of you, [pov]."
    mom "You have so much of your father in you."
    pov "Thanks... I'm not him."
    povi "She needs to stop comparing me with him."
    mom "No, you not. You're much better."
    povi "What? Wow."
    scene basement 10pm 056la
    mom "<kiss> I love you [pov]!"
    povi "Well, a kiss on the cheek isn't bad, but not exactly what I was hoping for."
    if inc == True:
        pov "I love you too, mom!"
    else:
        pov "I love you too, [mother]!"
    mom "I feel so free with you. So safe. Just the two of us."
    if inc == True:
        pov "I feel the same, mom."
    else:
        pov "I feel the same [mother]."
    scene basement 10pm 057la
    mom "If you keep it secret, I'll tell you what bunnies really love."
    pov "I can keep any secret you want me to."
    povi "That way she's looking at me... I need to know!"
    mom "Carrots!"
    pov "Carrots?"
    mom "Yes, bunnies loves carrots."
    scene basement 10pm 058la
    mom "And I'd love to see your carrot."
    povi "Wow, she's grabing my dick through my pants!"
    if inc == True:
        pov "Oh mom."
    else:
        pov "Oh [mother]."
    mom "Be a good boy and give your bunny a carrot."
    pov "I'll give you everything you need."
    povi "Is this a dream?"
    scene basement 10pm 059la
    mom "Then follow me!"
    mom "Follow your bunny, [pov]."
    pov "Of course."
    povi "Is she really playing with my carrot... I mean dick! now. Damn it! I don't want to start calling it that now."
    mom "Just sit here and enjoy what your bunny now."
    pov "Hm..."
    scene basement 10pm 060la
    mom "Just relax and enjoy what your bunny wants to do with your carrot."
    pov "Oh, I'm ready!"
    mom "This is our secret right?"
    pov "I promise! I would love to share even more secrets with you."
    mom "Without knowing what I'm going to do with you? You're so sweet."
    pov "It isn't anything bad, right?"
    mom "Well, you could get addicted! <giggle>"
    scene basement 10pm 061la
    pov "I bet it will be worth it!"
    mom "Time to see your carrot."
    "She's unpacking your dick."
    povi "What a hot view. And that cleavage!"
    if inc == True:
        povi "Not to mention the fact that my mom wants to play with my dick."
    else:
        povi "Not to mention the fact [mother] wants to play with my dick."
    scene basement 10pm 062la
    mom "<kiss>"
    pov "Oh yes. Kiss my carrot."
    mom "I need to taste it before... <giggle>"
    pov "Before what? Is there even more?"
    scene basement 10pm 063la
    mom "Before I eat my carrot, <giggle>"
    mom "<lick> <lick>"
    povi "Is she really going to giving me a blowjob?"
    povi "She's even playing with my balls. This is so great."
    pov "I'm glad you like my carrot."
    mom "Yes, <lick> it tastes so good."
    scene basement 10pm 064la
    mom "Hmm... <suck>"
    if inc == True:
        pov "Oh wow mom... That's great!"
        povi "Hell yeah. My mom is playing a naughty roleplay with me and sucking me off. Best day ever!"
    else:
        pov "Oh wow [mother]... That's great!"
        povi "Hell yeah. [mother] is playing a naughty roleplay with me and sucking me off. Best day ever!"
    "Suddenly you feel her teeth on your dick."
    pov "HUH?"
    scene basement 10pm 065la
    mom "Haha... you were scared, weren't you?"
    pov "Haha, you got me there."
    if inc == True:
        mom "I would never hurt my baby boy."
    else:
        mom "I would never hurt you, [pov]."
    pov "Yeah, I should trust you more."
    mom "No worries, it was a little mean. But that's just so you can enjoy your reward even more."
    pov "My reward?"
    mom "This rabbit wants some milk too. Not only a tasty carrot."
    pov "Oh my..."
    povi "She wants to drink my sperm."
    pov "That's a really good reward..."
    scene basement 10pm 066la
    mom "Hm... <suck>"
    pov "Hah, you're doing so good."
    povi "Is she pressing my dick in her cheek? That's so hot."
    "Your penis is twitching like crazy."
    if inc == True:
        pov "Mom, I don't think I can't hold on much longer. You're too good at this!"
    else:
        pov "[mother], I don't think I can't hold on much longer. You're too good at this!"
    scene basement 10pm 067la
    mom "Not yet [pov]. Hold it just a little longer. You'll love the reward even more!"
    "She squeezes your balls."
    pov "Ok... I'll so what I can."
    if inc == True:
        povi "My mom is giving me sex-tips while sucking me!"
    else:
        povi "[mother] is giving me sex-tips while sucking me!"
    povi "And how she's playing with my balls. This is heaven."
    mom "Now be a good boy and give me your milk."
    scene basement 10pm 068la
    "She releases the pressure on your balls."
    pov "HNG! Oh yes!"
    "You spurt your sperm into her mouth."
    povi "I'm cumming!"
    mom "Hnn... hm..."
    scene basement 10pm 069la
    mom "Your milk is so tasty."
    pov "Oh!"
    mom "Time for my treat now!"
    if inc == True:
        pov "I'm so glad that I could give it to you, mom!"
    else:
        pov "I'm so glad that I could give it to you, [mother]!"
    scene basement 10pm 070la
    mom "Hmm... <gulp>"
    povi "She's swalloing it... Oh god yes!"
    if inc == True:
        povi "My mom swallowed my sperm."
    else:
        povi "[mother] swallowed my sperm."
    scene basement 10pm 072la
    povi "That's weird, she was so into this and now she looks a little guilty."
    mom "Oh [pov]! Are you ok with this? You don't think I just attacked you like some whore right? You're probably so confused!"
    if inc == True:
        pov "Of course not mom. Don't worry about that. I liked it very much!"
    else:
        pov "Of course not [pv]. Don't worry about that. I liked it very much!"
    pov "And I'd love to do more things with my personal bunny, haha."
    mom "Hmm..."
    if inc == True:
        pov "Come here, mom!"
    else:
        pov "Come here, [mother]!"
    scene basement 10pm 073la
    pov "Stop worrying over nothing. It's ok that we enjoyed each other's company."
    pov "I love you!"
    if inc == True:
        pov "I love you more than son probably should love his mom."
        pov "But in my heart, I want us to be lovers."
    else:
        pov "And I love you even more than I probably should."
        pov "But in my heart, I want us to be lovers."
    mom "Oh [pov]. I love you so much!"
    "You hold her for a while."
    mom "We should go back now."
    mom "But let me just enjoy this moment a little more."
    mom "I hope you'll have sweet dreams of me. I know I'll be dreaming of you too."
    if inc == True:
        pov "Oh yes I will. Mom."
    else:
        pov "Oh yes I will. [mother]."
    scene black
    "You two leave the basment."
    $ bunnyfirst = True
    $ dtime += 1
    jump droom

label base10pmniclove3:
    scene basement 10pm 051lb
    mom "So...?"
    pov "..."
    mom "Ha! Cat got your tongue?"
    pov "You, you look like an angel."
    mom "Like an angel?"
    pov "Like the lingerie models!"
    scene basement 10pm 052lb
    mom "Oh, that's so sweet."
    pov "Thi... is... so... hot. Why are you... wearing this?"
    mom "It's my present for you being such a sweet gentleman. You're the only one to me in it."
    pov "Than it's a very good present."
    mom "Oh it'll get even better."
    scene basement 10pm 053lb
    pov "Ohh... <gulp>"
    mom "<giggle> So you like it?"
    pov "Wow! That g-string looks so good on you! You ass is amazing!"
    mom "Hm..."
    pov "Oh, sorry. I shouldn't be talking to you like that. You're not some toy for me play with."
    scene basement 10pm 054lb
    mom "Haha, calm down [pov]."
    mom "This sort of lingerie is intended to make men flustered, <giggle>."
    mom "But it makes me happy that you still try to be a gentleman."
    pov "It's very hard right now."
    scene basement 10pm 055lb
    mom "Being a gentleman or something else? <giggle>"
    if inc == True:
        pov "What are you talking about, mom?"
    else:
        pov "What are you talking about, [mother]?"
    mom "I'm not naive. I notice when a young gentleman is giving me special attention."
    if inc == True:
        pov "I... just love you, mom!"
    else:
        pov "I... just love you, [mother]!"
    mom "I know, but your staring tells me that you're loving something else even more."
    pov "I... can't... sorry."
    scene basement 10pm 056lb
    mom "Now you can see them even better!"
    pov "Oh my god! They're so beautiful!"
    pov "But why... why are you showing me all of this?"
    mom "I'm just so proud of you, you've became such a good young man, but I noticed you're also confused around me."
    mom "I've been confused around you too. Thoughts and feelings... naughty things."
    mom "But you've been so strong and stood up for me and girls when no else will. I'm not confused anymore."
    mom "Let's have this special basement time together and forget everything else."
    if inc == True:
        mom "Everything, except you and I. You're my son, that adores me. And I'm you mother, who adores and needs you."
    else:
        mom "Everything, except you and I. You're a young man that adores me. And I'm a woman who adores and needs you."
    scene basement 10pm 057lb
    pov "You are literally the only thing on my mind!"
    mom "Than take you chance."
    pov "My chance?"
    mom "You want to touch them?"
    scene basement 10pm 058lbb
    pov "They're so big and firm, but still so very soft."
    mom "Hehe, you just never stop complimenting me."
    pov "Well, you've just given me two more reasons to not stop now!"
    pov "I wish I could remember sucking milk out of them as a baby."
    mom "Hm..."
    pov "I wish even more I could suck milk out of them now..."
    scene basement 10pm 059lbb
    mom "But I would need to get pregnant first."
    pov "..."
    mom "..."
    pov "..."
    mom "Time for your reward!"
    pov "My... reward..."
    mom "Go over to the table."
    scene basement 10pm 060lb
    mom "It'll be something just for you."
    if inc == True:
        pov "Oh mom. I'm so happy right now. This just gets better and better."
    else:
        pov "Oh [mother]. I'm so happy right. This just gets better and better."
    mom "Relax baby. Let take care of you. And try to endure it for a while. I want to enjoy it as well."
    pov "I... will..."
    scene basement 10pm 061lb
    mom "But first we need to prepare you."
    "She unpacks your dick."
    povi "I'm already so hard right now."
    scene basement 10pm 062lb
    mom "<kiss>"
    if inc == True:
        pov "Oh mom."
    else:
        pov "Oh [mother]."
    mom "You're twitching in anticipation already, try to relax more, [pov]."
    pov "It's so hard when your lips feel so good. But don't worry, I'll last as long as you need me to."
    scene basement 10pm 063lb
    mom "We need to make it nice and wet."
    pov "Oh!"
    "She squeezes your balls."
    mom "Feels good, doesn't it?"
    pov "Oh yes..."
    mom "I you want to try something else as well. I'll let you choose..."
    pov "Choose?"
    mom "Do you want me to continue with my mouth or do you want to feel it between my breasts?"
    povi "Hell yes! But her mouth is so soft and warm."
    call screen base10pmniclove3choose

screen base10pmniclove3choose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmniclove3choose'), Jump('base10pmniclove3bj')) hovered tt.Action ("Let her use her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmniclove3choose'), Jump('base10pmniclove3boobs')) hovered tt.Action ("Let her use her boobs") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmniclove3bj:
    if inc == True:
        pov "Please continue with your mouth, mom."
        mom "As you wish, my lovely son."
    else:
        pov "Please continue with your mouth, [mother]."
        mom "As you wish, lovely [pov],"
    scene basement 10pm 064lb
    mom "<suck>"
    pov "Oh yes!"
    if inc == True:
        povi "Hell yeah. My mom is sucking me off!"
    else:
        povi "Hell yeah. [mother] is sucking me off!"
    pov "Your soft lips and that wet tongue. It's so hard not to just blow everything right now."
    scene basement 10pm 065lb
    "She squeezes your balls harder."
    mom "<giggle> I will have to help you endure a little longer."
    pov "Then... I'll cum so much."
    mom "That's a good way to make my reward unforgetable. Don't you think?"
    if inc == True:
        pov "Oh, I'll never forget this! I can promise you that mom!"
    else:
        pov "Oh, I'll never forget this! I can promise you that [mother]!"
    mom "So sweet!"
    pov "If being a gentleman means I'll get more rewards from you, then I'm official never becoming a bad boy!"
    mom "Haha, I hope I can reward you many more times!"
    scene basement 10pm 066lb
    mom "<suck> <lick>"
    pov "I must be in heaven, having an angel sucking on my dick."
    mom "Hm... hnn..."
    pov "I wish I could do this forever with you."
    mom "<giggle> <suck>"
    scene basement 10pm 067lb
    mom "You're such a charmer. Even when you're at the limit you're polite. I love it!"
    pov "This is a literal dream come true. I plan to enjoy it as much as possible."
    mom "Well I'm ready for you to enjoy it even more. I know you can't hold out much longer, even when I'm holding your balls."
    if inc == True:
        pov "Yes, I'm close. I'm going to cum so hard mom."
    else:
        pov "Yes, I'm close. I'm going to cum so hard [mother]."
    mom "You can choose where to spray it."
    pov "..."
    mom "<giggle>"
    call screen base10pmniclove3bjcum

screen base10pmniclove3bjcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmniclove3bjcum'), Jump('base10pmniclove3bjmouth')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmniclove3bjcum'), Jump('base10pmniclove3bjface')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmniclove3bjmouth:
    pov "I want you to taste my sperm."
    if inc == True:
        mom "As you wish, my son."
    else:
        mom "As you wish, [pov]."
    scene basement 10pm 068lb
    "She releases the pressure on your balls."
    pov "HNG! Oh yes!"
    "You spurt your sperm in her mouth."
    povi "I'm cumming!"
    mom "Hnn... hm..."
    scene basement 10pm 069lb
    mom "You came so much. So you liked my reward?"
    pov "I loved it!"
    mom "And you even taste good."
    scene basement 10pm 070lb
    mom "Hmm... <gulp>"
    povi "She's swallowing it."
    if inc == True:
        povi "My mom swallowed my sperm."
    else:
        povi "[mother] swallowed my sperm."
    scene basement 10pm 072lb
    mom "Tasty!"
    pov "Now you're complimenting me."
    mom "<giggle>"
    jump base10pmniclove3end

label base10pmniclove3bjface:
    pov "I want to paint your beautiful face."
    if inc == True:
        mom "As you wish, my son."
    else:
        mom "As you wish, [pov]."
    scene basement 10pm 068lbf
    "She releases the pressure on your balls."
    pov "HNG! Oh yes!"
    "You spray your sperm on her face."
    povi "I'm cumming in on her face!"
    mom "Hnn... hm..."
    scene basement 10pm 069lbf
    mom "You came so much. So you liked my reward?"
    pov "I loved it!"
    mom "It's so warm and sticky."
    pov "You look so beautiful covered like that."
    mom "I wish I could see your face right now, but you came so much! <giggle>"
    pov "Let me help get cleaned up. That beautiful view is burned in my mind anyways."
    mom "<giggle>"
    jump base10pmniclove3end

label base10pmniclove3boobs:
    if inc == True:
        pov "Please let me feel your breasts around my dick, mom."
        mom "As you wish, my lovely son."
    else:
        pov "Please let me feel your breasts around my dick, [mother]."
        mom "As you wish, lovely [pov],"
    scene basement 10pm 062lbbj
    pov "So... so soft..."
    mom "Your penis likes his new home."
    pov "He's meeting two new friends."
    mom "<giggle>"
    pov "And I hope they'll become friends for life."
    mom "Haha! Save your breath for later, you'll need it to relax, I feel you're very excited already."
    scene basement 10pm 063lbbj
    mom "<kiss>"
    pov "The best view ever."
    if inc == True:
        povi "Getting a boob-job from my mom."
    else:
        povi "Getting a boob-job from [mother]."
    scene basement 10pm 064lbbj
    mom "I see you're enjoying this very much!"
    if inc == True:
        pov "Getting a boob job from my beautiful mom. It's the best thing ever!"
    else:
        pov "Getting a boob job from you. It's the best thing ever!"
    mom "And feeling your warm penis twitching between them is also very nice."
    pov "Then I'm glad you can enjoy my reward too."
    mom "<giggle> Oh yes, I do."
    scene basement 10pm 065lbbj
    mom "How about some more playing?"
    pov "Ohh... ohh... this is so good!"
    mom "I'll squeeze them hard together, just press your cock up while I squeeze. You'll love the way it feels."
    if inc == True:
        pov "I love you giving me tips like that, mom. So sexy!"
    else:
        pov "I love you giving me tips like that, [mother]. So sexy!"
    "She starts squeezing her breasts together."
    scene basement 10pm 066lbbj
    pov "HNG!"
    mom "Good, press more."
    pov "Hah, ahh..."
    mom "Come for me, [pov]!"
    scene basement 10pm 067lbbj
    pov "Haaah..."
    mom "Good!"
    "You spray your sperm out."
    pov "This... hah... is so good!"
    mom "Give it to me baby!"
    pov "Hnn... I love you!"
    mom "I love you too sweet heart!"
    scene basement 10pm 068lbbj
    mom "Good, you sure came a lot."
    if inc == True:
        pov "That was so wonderful, mom."
    else:
        pov "That was so wonderful, [mother]."
    mom "And so much of your warm, sticky sperm is covering me."
    pov "And that is the most amazing view too."
    mom "You won the hard fight. <giggle>"
    jump base10pmniclove3end

label base10pmniclove3end:
    mom "Don't forget, this is just between us."
    pov "I'll rather cut my tongue then tell anyone."
    mom "Come here, my little charmer."
    scene basement 10pm 073lb
    if inc == True:
        pov "I love you so much, mom!"
        mom "I love you too, my son!"
    else:
        pov "I love you so much, [mother]!"
        mom "I love you too, [pov]!"
    mom "And whenever my good boy behaves we can repeat this anytime."
    pov "Oh I'll be looking forward to that."
    "You hold her for a while."
    mom "We should go back now."
    mom "But let me just enjoy this moment a little more."
    mom "I hope you'll have sweet dreams of me. I know I'll be dreaming of you too."
    if inc == True:
        pov "Oh I will. Mom."
    else:
        pov "Oh I will. [mother]."
    scene black
    "You two leave the basment."
    $ angelfirst = True
    $ dtime += 1
    jump droom

#----- Custom Scene -----
#----- Corruptions Scenes for Angel and Bunny outfits -----
label base10pmnicbunnycor:
    scene basement 10pm 050c
    mom "Hmm..."
    pov "Is something wrong?"
    mom "No, I'm just thinking..."
    povi "What is she up to?"
    mom "Wait here, I want to show you something."
    pov "Oh, Ok."
    povi "I wonder what it is?"
    scene basement 10pm 051la
    mom "Hey [pov]!"
    pov "Oh my god."
    mom "So you like it?"
    pov "Yes... suits you very well..."
    mom "It's one of my favourite outfits!"
    pov "I can see why... wow!"
    scene basement 10pm 052la
    mom "So you like bunnies?"
    pov "Oh yes, you're a very hot bunny. Naughty too I bet!"
    mom "<giggle> I knew you'd like it too. And yes, I can be very naughty..."
    pov "The hottest Playboy bunny ever."
    mom "You and your flattery. I just love it!"
    scene basement 10pm 053la
    mom "How about this end? Feel free to keep up the complements! <giggle>"
    pov "Wow! You've even got a fluffy bunny tail."
    povi "What is she's doing? Is she flirting with me?"
    pov "You're really an adorable bunny. With a cute little ass too!"
    mom "Hnnn..."
    scene basement 10pm 054la
    mom "I wanted to be a real Playboy bunny when I was younger."
    mom "And with this outfit I can be one now! Even if it is just for you."
    if inc == True:
        pov "Oh mom, I like having you all to myself. My personal playboy bunny!"
    else:
        pov "Oh [mother], I like having you all to myself. My personal playboy bunny!"
    pov "I bet even Hugh would come back from his grave for the chance to have you in his house."
    mom "Haha, you know all the right things to say to me."
    mom "Did you want to see how naughty this bunny can be?"
    scene basement 10pm 055la
    povi "Wow. Is she going to kiss me now? Yes please..."
    if inc == True:
        mom "I've been feeling excited around you, my son."
    else:
        mom "I've been feeling excited around you, [pov]."
    mom "You have so much of your father in you."
    pov "Thanks... I'm not him."
    povi "She needs to stop comparing me with him."
    mom "No, you not him. You're so much better."
    povi "What? Wow."
    scene basement 10pm 056la
    mom "<kiss> I want you [pov]!"
    povi "Well, a kiss on the cheek isn't bad, but not exactly what I was hoping for."
    if inc == True:
        pov "I want you too, mom!"
    else:
        pov "I want you too, [mother]!"
    mom "I feel so free with you. And being here with just the two of us... alone..."
    if inc == True:
        pov "I feel the same, mom."
    else:
        pov "I feel the same [mother]."
    scene basement 10pm 057la
    mom "I have a secret to share with you. I'm going to tell you what bunnies really love."
    pov "I like the sound of that."
    povi "That way she's looking at me... Damn that's hot!"
    mom "Carrots!"
    pov "Carrots?"
    mom "Yes, bunnies loves carrots."
    scene basement 10pm 058la
    mom "And I'd love to see your carrot."
    povi "Wow, she's grabing my dick through my pants!"
    if inc == True:
        pov "Oh mom. You're an eager bunny aren't you?"
    else:
        pov "Oh [mother]. You're an eager bunny aren't you?"
    mom "Yes, I need it! Be a good boy and give your bunny a carrot."
    pov "I'll give you everything you need."
    scene basement 10pm 059la
    mom "Follow me!"
    mom "Follow your bunny, [pov]."
    pov "Of course."
    povi "Is she really playing with my carrot... I mean dick! now. Damn it! I don't want to start calling it that now."
    mom "Just sit here and enjoy what your bunny does with it's carrot now."
    pov "Hm..."
    scene basement 10pm 060la
    pov "Oh, I'm ready!"
    mom "This is our secret right?"
    pov "I promise! I have a feeling that we'll be sharing many more secrects together."
    mom "Without knowing what I'm going to do with you? You're brave!"
    pov "Well if you did anything bad, you know I would punish you. I think I can handle whatever you have in mind!"
    mom "Oh! I wouldn't want you to punish me! <giggle>"
    mom "I might get addicted to that!"
    scene basement 10pm 061la
    pov "I bet it will be worth it!"
    mom "Time to see your carrot."
    "She's pulls your dick out of your pants."
    povi "What a hot view. And that cleavage, damn that's just perfect!"
    if inc == True:
        povi "Not to mention the fact that my mom wants to play with my dick."
    else:
        povi "Not to mention the fact [mother] wants to play with my dick."
    scene basement 10pm 062la
    mom "<kiss>"
    pov "Oh yes. Kiss my carrot."
    mom "I need to taste it before... <giggle>"
    pov "Oh, does my naughty bunny have even more for me?"
    scene basement 10pm 063la
    mom "Yes, I am going to eat my carrot, <giggle>"
    mom "<lick> <lick>"
    povi "Is she really going to giving me a blowjob?"
    povi "She's even playing with my balls. This is so great."
    pov "I'm glad you like my carrot."
    mom "Yes, <lick> it tastes so good."
    scene basement 10pm 064la
    mom "Hmm... <suck>"
    if inc == True:
        pov "Oh wow mom... That's great! Keep it up!"
        povi "Hell yeah. My mom is playing a naughty roleplay with me and sucking me off. Best day ever!"
    else:
        pov "Oh wow [mother]... That's great! Keep it up!"
        povi "Hell yeah. [mother] is playing a naughty roleplay with me and sucking me off. Best day ever!"
    "Suddenly you feel her teeth on your dick."
    pov "HUH?"
    scene basement 10pm 065la
    mom "Haha... you were scared, weren't you?"
    pov "Haha, you got me there."
    if inc == True:
        mom "I would never hurt my baby boy. Unless you wanted me too..."
    else:
        mom "I would never hurt you, [pov]. Unless you wanted me too..."
    pov "Hmm... That would be something we could explore."
    mom "Hnnn..."
    mom "I think it's time for you to enjoy your reward."
    pov "My reward?"
    mom "This rabbit wants some milk too. Not only a tasty carrot."
    pov "Oh my..."
    povi "She wants to drink my sperm."
    pov "That's a really good reward..."
    scene basement 10pm 066la
    mom "Hm... <suck>"
    pov "Hah, you're doing so good."
    povi "Is she pressing my dick in her cheek? That's so hot."
    "Your penis is twitching like crazy."
    if inc == True:
        pov "Mom, I hope you're ready for my milk. You're too good at this!"
    else:
        pov "[mother], I hope you're ready for my milk. You're too good at this!"
    scene basement 10pm 067la
    mom "Not yet [pov]. Hold it just a little longer. You'll love the reward even more!"
    "She squeezes your balls."
    pov "Ok... I'll so what I can."
    if inc == True:
        povi "My mom is giving me sex-tips while sucking me!"
    else:
        povi "[mother] is giving me sex-tips while sucking me!"
    povi "And how she's playing with my balls. This is heaven."
    mom "Now be a good boy and give me your milk."
    scene basement 10pm 068la
    "She releases the pressure on your balls."
    pov "HNG! Oh yes!"
    "You spurt your sperm into her mouth."
    povi "I'm cumming!"
    mom "Hnn... hm..."
    scene basement 10pm 069la
    mom "Your milk is so tasty."
    pov "Oh!"
    mom "Time for my treat now!"
    if inc == True:
        pov "I'm so glad that I could give it to you, mom!"
    else:
        pov "I'm so glad that I could give it to you, [mother]!"
    scene basement 10pm 070la
    mom "Hmm... <gulp>"
    povi "She's swalloing it... Oh god yes!"
    if inc == True:
        povi "My mom swallowed my sperm."
    else:
        povi "[mother] swallowed my sperm."
    scene basement 10pm 072la
    povi "That's weird, she was so into this and now she looks a little guilty."
    mom "Oh [pov]! Are you ok with this? You don't think I just attacked you like some whore right? You're probably so confused!"
    if inc == True:
        pov "Of course not mom. Don't worry about that. I liked it very much!"
    else:
        pov "Of course not [pv]. Don't worry about that. I liked it very much!"
    pov "And I'd love to do more things with my personal bunny, haha."
    mom "Hmm..."
    if inc == True:
        pov "Come here, mom!"
    else:
        pov "Come here, [mother]!"
    scene basement 10pm 073la
    pov "Stop worrying over nothing. It's ok that we enjoyed each other's company."
    pov "I wanted you to do those things to me."
    mom "Oh [pov]. I wanted you so badly!"
    "You hold her for a while."
    mom "We should go back now."
    mom "But let me just enjoy this moment a little more."
    mom "I hope you'll have naughty dreams of me. I know I'll be dreaming of you too."
    if inc == True:
        pov "Oh yes I will. Mom."
    else:
        pov "Oh yes I will. [mother]."
    scene black
    "You two leave the basement."
    $ bunnyfirst = True
    $ dtime += 1
    jump droom

label base10pmnicangelcor:
    scene basement 10pm 050c
    mom "Hmm..."
    pov "Is something wrong?"
    mom "No, I'm just thinking..."
    povi "What is she up to?"
    mom "Wait here, I want to show you something."
    pov "Oh, Ok."
    povi "I wonder what it is?"
    mom "Hmm... where is it?"
    mom "Just wait a moment [pov]."
    pov "Sure."
    povi "I hope it's something good."
    scene basement 10pm 051lb
    mom "So...?"
    pov "..."
    mom "Ha! Cat got your tongue?"
    pov "You, you look like an angel."
    mom "Like an angel?"
    pov "Like the lingerie models!"
    scene basement 10pm 052lb
    mom "Oh, that's so sweet."
    pov "Thi... is... so... hot. You look amazing!"
    mom "It's my present for you being such a strong man. You're the only one to see me in it."
    pov "Than it's a very good present."
    mom "Oh, it'll get even better."
    scene basement 10pm 053lb
    pov "Ohh... I like that sound of that!"
    mom "<giggle> So you like this end too?"
    pov "Wow! That g-string looks so good on you! Your ass is amazing!"
    mom "Hnng..."
    pov "I just want to reach out and touch you..."
    scene basement 10pm 054lb
    if inc == True:
        mom "Haha, I'm glad you feel that way son."
    else:
        mom "Haha, I'm glad you feel that way [pov]."
    mom "This sort of lingerie is intended to make men want more, <giggle>."
    mom "I'm surprised you didn't just do it."
    pov "I'll admit it was very hard..."
    scene basement 10pm 055lb
    mom "Not touching me or something else? <giggle>"
    if inc == True:
        pov "You're being such a dirty girl, mom!"
    else:
        pov "You're being such a dirty girl, [mother]?"
    mom "I'm not naive. I've noticed that you've been giving me special attention. Protecting me from the other men."
    if inc == True:
        pov "I... just didn't want them to touch you, mom."
    else:
        pov "I... just didn't want them to touch you, [mother]."
    mom "I know, but the way you stare at me tells me that you do want to touch me. Don't you?"
    scene basement 10pm 056lb
    mom "How about now? Is it still hard... for you?"
    pov "Oh my god! Your tits are amazing!"
    pov "Don't take this the wrong way, but... why are you showing me... all of this?"
    mom "I'm just so proud of you, you've became such a good young man, but I noticed you've been different when you're around me."
    mom "I've been different around you too. I've been having thoughts and feelings... thinking about naughty things."
    mom "But you've been so strong and stood up for me and girls when no else will. I want a man like that in my life."
    mom "Let's be ourselves down here together. Fuck the rest of the bastards up there. Forget them, forget everything..."
    if inc == True:
        mom "Everything, except you and I. My son that protects and wants me. And me, your mother, who needs and wants you too."
    else:
        mom "Everything, except you and I. My son that protects and wants me. And me, the woman who needs and wants you too."
    scene basement 10pm 057lb
    pov "You are literally the only thing on my mind!"
    mom "Than take your chance now."
    pov "My chance?"
    mom "You do still want to touch them, right?"
    scene basement 10pm 058lbb
    pov "They're so big and firm, but still so very soft."
    mom "Hehe, you just never stop complimenting me. You don't need to if you don't want to. You already have me!"
    pov "Well, you've just given me two more reasons to not stop now!"
    pov "I wish I could remember sucking milk out of them as a baby."
    mom "Hm..."
    pov "I wish even more I could suck milk out of them now..."
    scene basement 10pm 059lbb
    mom "But I would need to get pregnant first."
    pov "..."
    mom "..."
    pov "..."
    mom "Time for your reward!"
    pov "My... reward..."
    mom "Go over to the table."
    scene basement 10pm 060lb
    mom "It'll be something just for you. My strong protector. My handsome man."
    if inc == True:
        pov "Oh mom. This just gets better and better."
    else:
        pov "Oh [mother]. This just gets better and better."
    mom "Relax baby. Let me take care of you."
    pov "Oh... ok..."
    scene basement 10pm 061lb
    mom "But first thing's first."
    "She pulls your dick out of your pants."
    povi "I'm already so hard right now."
    scene basement 10pm 062lb
    mom "<kiss>"
    if inc == True:
        pov "Oh mom. I want you so badly."
    else:
        pov "Oh [mother]. I want you so badly."
    mom "You're twitching in anticipation already, try to relax more, [pov]. I want plenty of time to show you how much I want you too."
    pov "It's so hard when your lips feel so good. But don't worry, I'll last as long as you need me to."
    scene basement 10pm 063lb
    mom "We need to make it nice and wet."
    pov "Oh!"
    "She squeezes your balls."
    mom "Feels good, doesn't it?"
    pov "Oh god yes..."
    mom "If you want to try something else as well, I'll let you choose..."
    pov "Choose?"
    mom "Do you want me to continue with my mouth or do you want to feel it between my breasts?"
    povi "Hell yes! But her mouth is so soft and warm."
    call screen base10pmnicangelcorchoose

screen base10pmnicangelcorchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnicangelcorchoose'), Jump('base10pmnicangelcorbj')) hovered tt.Action ("Let her use her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnicangelcorchoose'), Jump('base10pmnicangelcorboobs')) hovered tt.Action ("Let her use her boobs") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmnicangelcorbj:
    if inc == True:
        pov "I want you to suck my cock, mom."
        mom "As you wish, my naughty son."
    else:
        pov "I want you to suck my cock, [mother]."
        mom "As you wish, my naughty boy."
    scene basement 10pm 064lb
    mom "<suck>"
    pov "Oh god yes!"
    if inc == True:
        povi "Hell yeah. My mom is sucking me off!"
    else:
        povi "Hell yeah. [mother] is sucking me off!"
    pov "Your soft lips and that wet tongue. It's so hard not to just blow everything right now."
    scene basement 10pm 065lb
    "She squeezes your balls harder."
    mom "<giggle> I will have to help you endure a little longer."
    pov "I'll cum so much..."
    mom "That's a good way to make my reward unforgetable. Don't you think?"
    if inc == True:
        pov "Oh, I'll never forget this! I can promise you that mom!"
    else:
        pov "Oh, I'll never forget this! I can promise you that [mother]!"
    mom "So sweet!"
    pov "Sweet enough that I'll get more rewards from you sometime?"
    mom "Haha, already thinking about next huh? That means I need to get your attention back to here and now!"
    scene basement 10pm 066lb
    mom "<suck> <lick>"
    pov "I must be in heaven, having an angel sucking on my dick."
    mom "Hm... hnn..."
    pov "It feels so good. You much be heavens sluttiest angel!"
    mom "<giggle> <suck>"
    scene basement 10pm 067lb
    mom "You're such a kinky boy. Even when you're at the limit you're thinking about slutty angels in heaven. I love it!"
    pov "This is a literal dream come true. I plan to enjoy it as much as possible."
    mom "Well I'm ready for you to enjoy it even more. I know you can't hold out much longer, even when I'm holding your balls."
    if inc == True:
        pov "Yes, I'm close. I'm going to cum so hard mom."
    else:
        pov "Yes, I'm close. I'm going to cum so hard [mother]."
    mom "You can choose where to spray it."
    pov "..."
    mom "<giggle>"
    call screen base10pmnicangelcorbjcum

screen base10pmnicangelcorbjcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnicangelcorbjcum'), Jump('base10pmnicangelcorbjmouth')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmnicangelcorbjcum'), Jump('base10pmnicangelcorbjface')) hovered tt.Action ("Cum on her face") focus_mask True


    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmnicangelcorbjmouth:
    pov "I want you to taste my sperm."
    if inc == True:
        mom "As you wish, my son."
    else:
        mom "As you wish, [pov]."
    scene basement 10pm 068lb
    "She releases the pressure on your balls."
    pov "HNG! Oh yes!"
    "You spurt your sperm in her mouth."
    povi "I'm cumming!"
    mom "Hnn... hm..."
    scene basement 10pm 069lb
    mom "You came so much. So you liked my reward?"
    pov "I loved it!"
    mom "And you even tasted good."
    scene basement 10pm 070lb
    mom "Hmm... <gulp>"
    povi "She's swallowing it."
    if inc == True:
        povi "My mom swallowed my sperm."
    else:
        povi "[mother] swallowed my sperm."
    scene basement 10pm 072lb
    mom "Tasty!"
    pov "Now you're the kinky one!"
    mom "<giggle>"
    jump base10pmniclove3end

label base10pmnicangelcorbjface:
    pov "I want to paint your slutty angel face."
    if inc == True:
        mom "As you wish, my son."
    else:
        mom "As you wish, [pov]."
    scene basement 10pm 068lbf
    "She releases the pressure on your balls."
    pov "HNG! Oh yes!"
    "You spray your sperm on her face."
    povi "I'm cumming in on her face!"
    mom "Hnn... hm..."
    scene basement 10pm 069lbf
    mom "You came so much. So you liked my reward?"
    pov "I loved it!"
    mom "It's so warm and sticky."
    pov "You look so beautiful covered like that."
    mom "I wish I could see your face right now, but you came so much! I can't see a thing! <giggle>"
    pov "Let me help get cleaned up. That beautiful view is burned in my mind anyways."
    mom "<giggle>"
    jump base10pmnicangelcorend

label base10pmnicangelcorboobs:
    if inc == True:
        pov "I want to feel you breast around my cock, mom."
        mom "As you wish, my naughty son."
    else:
        pov "I want to feel you breast around my cock, [mother]."
        mom "As you wish,  my naughty boy."
    scene basement 10pm 062lbbj
    pov "So... so soft..."
    mom "I think your penis likes his new home."
    pov "I do too. He's meeting his two new best friends."
    mom "<giggle>"
    pov "And I hope they'll become friends for life."
    mom "Haha! Save your breath for later, you'll need it to relax, I feel that you're very excited already."
    scene basement 10pm 063lbbj
    mom "<kiss>"
    pov "The best view ever."
    if inc == True:
        povi "Getting a boob-job from my mom."
    else:
        povi "Getting a boob-job from [mother]."
    scene basement 10pm 064lbbj
    mom "I see you're enjoying this very much!"
    if inc == True:
        pov "Getting a boob job from my beautiful mom. It's the best thing ever!"
    else:
        pov "Getting a boob job from you. It's the best thing ever!"
    mom "And feeling your warm penis twitching between them feels so good!"
    pov "Then I'm glad you can enjoy my reward too."
    mom "<giggle> Oh yes, I do."
    scene basement 10pm 065lbbj
    mom "How about some more playing?"
    pov "Ohh... ohh... this is so good!"
    mom "I'll squeeze them hard together, just press your cock up while I squeeze. You'll love the way it feels."
    if inc == True:
        pov "I love you giving me tips like that, mom. So sexy!"
    else:
        pov "I love you giving me tips like that, [mother]. So sexy!"
    "She starts squeezing her breasts together."
    scene basement 10pm 066lbbj
    pov "HNG!"
    mom "Good, press more. Faster!"
    pov "Hah, ahh..."
    if inc == True:
        mom "Come for your mommy!"
    else:
        mom "Cum for me, [pov]!"
    scene basement 10pm 067lbbj
    pov "Haaah..."
    mom "Good!"
    "You cum releases all over her. Squeezing and spurting out from between her breasts."
    pov "This... hah... is so fucking good!"
    mom "Give it to me baby!"
    pov "Hnn... God you're so good!"
    mom "Keep going [pov]! Cover me in cum!"
    scene basement 10pm 068lbbj
    mom "Good god, you sure came a lot."
    if inc == True:
        pov "That was so wonderful, mom."
    else:
        pov "That was so wonderful, [mother]."
    mom "And so much of your warm, sticky sperm is covering me. I love it so much."
    pov "And that is the most amazing view too."
    mom "Well you worked hard to make it! <giggle>"
    jump base10pmniclove3end

label base10pmnicangelcorend:
    mom "Don't forget, this is just between us."
    pov "I'll rather cut my tongue then tell anyone."
    mom "Come here, my naughty man."
    scene basement 10pm 073lb
    if inc == True:
        pov "I loved that so much, mom! I had no idea you were such a dirty girl!"
        mom "I loved it too, son! And you have no idea how dirty I can be."
    else:
        pov "I loved that so much, [mother]! I had no idea you were such a dirty girl!"
        mom "I loved it too, [pov]! And you have no idea how dirty I can be."
    mom "But I have a feeling you're going to find out! <giggles>"
    pov "Oh I'll be looking forward to that."
    "You hold her for a while."
    mom "We should go back now."
    mom "But let me just enjoy this moment a little more."
    mom "I hope you'll have naughty dreams of me. I know I'll be dreaming of you too."
    if inc == True:
        pov "Oh I will. Mom."
    else:
        pov "Oh I will. [mother]."
    scene black
    "You two leave the basment."
    $ angelfirst = True
    $ dtime += 1
    jump droom

#----- Custom Scene -----
#----- Love Scenes for Red Lingerie and School Girl outfits -----
label base10pmniclovered:
    $ base10pmnicred = True
    jump base10pmniclovestart

label base10pmnicloveschool:
    $ base10pmnicred = False
    jump base10pmniclovestart

label base10pmniclovestart:
    if base10pmnicred == True:
        scene basement 10pm 051cb
        mom "So, what do you think?"
        mom "You don't think that this makes me... look like a slut?"
        if inc == True:
            pov "Of course not mom! You're gorgeous! That dress is so hot!"
        else:
            pov "Of course not [mother]! You're gorgeous! That dress is so hot!"
        mom "Hnng..."
    else:
        scene basement 10pm 051ca
        mom "So, what do you think?"
        mom "You don't think that this makes me... look like a slut?"
        if inc == True:
            pov "Of course not mom! You're gorgeous! That school outfit is so hot!"
        else:
            pov "Of course not [mother]! You're gorgeous! That school outfit is so hot!"
        mom "Hnng..."
    pov "Why don't you come a little closer? I want a better look at you."
    if base10pmnicred == True:
        scene basement 10pm 052cb
    else:
        scene basement 10pm 052ca
    mom "So you like it then? It's not too much?"
    pov "No it's perfect! I really like it. Why are you so worried?"
    mom "Not worried. I guess I'm... just a little nervous."
    pov "Don't worrry, what happens down here, stays down here. I won't tell anyone. This is just between us."
    mom "Ok..."
    pov "Besides, I don't want the other idiots to know about what fun we're going to have here together."
    mom "Fun..."
    "She gives you a sly look."
    if inc == True:
        mom "...what kind of fun do you think you're going to have with your mother down here in a sluttly little outfit like this?"
    else:
        mom "...what kind of fun do you think you're going to have with me down here in a sluttly little outfit like this?"
    pov "Oh I can think of so many things..."
    pov "Besides, you chose the outfit for a reason."
    if inc == True:
        pov "Did my sweet mother want to be a little naughty for her son?"
    else:
        pov "Did you want to be a little naughty for me?"
    pov "I'm pretty sure you did."
    mom "Hmm... maybe. Would that be a bad thing?"
    pov "Not at all."
    if base10pmnicred == True:
        scene basement 10pm 053cb
    else:
        scene basement 10pm 053ca
    "You openly check her out more."
    if base10pmnicred == True:
        pov "Incredible. You look like a model in that dress."
        mom "Hnn..."
    else:
        pov "Incredible. You are the hottest school girl I've seen."
        mom "Hnn..."
    if inc == True:
        pov "Your legs are very beautiful, mom."
    else:
        pov "Your legs are very beautiful, [mother]."
    if base10pmnicred == True:
        scene basement 10pm 054cb
    else:
        scene basement 10pm 054ca
    mom "Hnn..."
    mom "Thank you, sweetie."
    pov "No thank you! Have then other men seen you in this?"
    mom "No... I told them I wouldn't wear it."
    pov "Wow! I'm the first!"
    mom "You're the only one... if you want..."
    pov "Really? I like that these basement adventures are just for me and you."
    mom "Me too."
    pov "Let's sit down."
    if base10pmnicred == True:
        scene basement 10pm 055cb
    else:
        scene basement 10pm 055ca
    pov "You didn't want to sit by me?"
    mom "No... that's not... I do want to sit by you."
    povi "She's acting so shy, submissive even. But I know she was teasing me before. Maybe she wants to play the submissive housewife for me. I'm game for that."
    if inc == True:
        pov "Are you afraid of me, mom?"
    else:
        pov "Are you afraid of me, [mother]?"
    mom "Should I be?"
    povi "There is a hint of a smile behind her expression. She is definitely into this."
    pov "Haha! No, you don't need to be afraid of me. I'm not going to do anything to you without your permission. For now."
    pov "But I'll admit... it's hard not to when you're wearing something so sexy."
    if base10pmnicred == True:
        scene basement 10pm 056cb
    else:
        scene basement 10pm 056ca
    mom "I don't know if you should be saying such things to me..."
    if inc == True:
        mom "You're still my son."
    else:
        mom "You're still the son of my best friend."
    pov "Well, when I'm with someone as beautiful as you are, its hard not to just shout out praises!"
    mom "Hnn..."
    pov "This outfit would even be good for a date sometime."
    mom "Hmm..."
    povi "Is she a bit flustered? Haha, looks like I'm going about this the right way."
    pov "But if it's too much, you could always just take it off..."
    if base10pmnicred == True:
        scene basement 10pm 057cb
    else:
        scene basement 10pm 057ca
    mom "What?"
    pov "Haha, I'm kidding. But I certainly wouldn't argue if you did!"
    if base10pmnicred == True:
        scene basement 10pm 058cb
    else:
        scene basement 10pm 058ca
    mom "Stop that..."
    pov "Haha, see there, you laughed a little! But that did gave me another idea..."
    pov "You could dance a little for me."
    mom "Where?"
    pov "Here on the table. It's the perfect way to showcase how great you look."
    if base10pmnicred == True:
        scene basement 10pm 055cb
    else:
        scene basement 10pm 055ca
    mom "Hnn... of course darling. Anything to make you happy."
    if inc == True:
        pov "That's a good girl, mom."
    else:
        pov "That's a good girl, [mother]."
    povi "Wow, she's really starting to like this. She's just going with things now."
    if base10pmnicred == True:
        scene basement 10pm 059cb
    else:
        scene basement 10pm 059ca
    povi "Oh my god. I can't wait."
    mom "I haven't done a lot of this king of thing. I hope you won't be disappointed."
    pov "There is no way I could be disappointed. You're so beautiful and I'm sure you're better than you think at this. You're so graceful!"
    povi "It's interesting how she asks things like that. Like she expects to be mistreated. I wonder if she's into that kind of thing.?"
    if base10pmnicred == True:
        scene basement 10pm 060cb
    else:
        scene basement 10pm 060ca
    pov "Wow..."
    if inc == True:
        pov "A good start, mom."
    else:
        pov "A good start, [mother]."
    mom "Hnn..."
    povi "Seriously, she's so stacked. And those little panties look great!"
    if base10pmnicred == True:
        scene basement 10pm 061cb
    else:
        scene basement 10pm 061ca
    pov "Wow, that top looks like it's about to burst. Feel free to let somethings loose if you want."
    mom "Hnng..."
    if inc == True:
        pov "You're a natural at this! I know you said you're not a stripper but you could be if you wanted to, mom."
    else:
        pov "You're a natural at this! I know you said you're not a stripper but you could be if you wanted to, [mother]."
    pov "This sort of fun isn't so bad, don't you think so?"
    mom "Hmm..."
    povi "She's really getting into this."
    if base10pmnicred == True:
        scene basement 10pm 062cb
    else:
        scene basement 10pm 062ca
    mom "Hnn..."
    povi "Wow that's sexy."
    pov "Amazing, just amazing."
    if base10pmnicred == True:
        scene basement 10pm 063cb
    else:
        scene basement 10pm 063ca
    pov "I feel really like a real V.I.P. here!"
    mom "You should. I wouldn't do this for just anyone."
    if inc == True:
        pov "You're very important to me too, mom."
    else:
        pov "You're very important to me too, [mother]."
    mom "Thank you [pov]."
    povi "Good, she's getting it now. That should help have much more fun."
    if base10pmnicred == True:
        scene basement 10pm 064cb
    else:
        scene basement 10pm 064ca
    povi "What a delightully lewd view."
    if inc == True:
        pov "I'm so proud of you, mom. Trying new things like this. So much fun!"
    else:
        pov "I'm so proud of you, [mother]. Trying new things like this. So much fun!"
    pov "I'd say you've found a new talent!"
    mom "You really liked it [pov]?"
    pov "You have no idea!"
    povi "Let's see if she wants to take this a little further."
    if base10pmnicred == True:
        scene basement 10pm 065cb
    else:
        scene basement 10pm 065ca
    mom "What are you doing?"
    pov "I wanted show you how much I like your dancing."
    mom "Hnng... you..."
    "You release your dick from the confines of your pants."
    if base10pmnicred == True:
        scene basement 10pm 066cb
    else:
        scene basement 10pm 066ca
    pov "See? I like your dancing very much."
    mom "You... took out your... penis..."
    pov "Yes and the way you're looking at it tells me you don't really mind that I did."
    mom "It's... not... <stare>"
    if base10pmnicred == True:
        scene basement 10pm 067cb
    else:
        scene basement 10pm 067ca
    if inc == True:
        pov "So what's on your mind, mom?"
    else:
        pov "So what's on your mind, [mother]?"
    mom "..."
    pov "You don't have to say it, if you're not ready to. But how about I make you a deal."
    pov "Anything we do down here is our secret. And you can do anythinig you want to me."
    pov "There aren't going to be any judgements here. Just two people that care about each other and want to explore those feelings. Those desires."
    if base10pmnicred == True:
        scene basement 10pm 068cb
    else:
        scene basement 10pm 068ca
    povi "Oh she's thinking..."
    pov "So I'll let you decide what we do next..."
    mom "Hnn..."
    "A few seconds pass, then as if possessed by an animal in heat, [pov] jumps of the table and down to her knees."
    if base10pmnicred == True:
        scene basement 10pm 069cbbj
    else:
        scene basement 10pm 069cabj
    pov "Very good. You're such a good girl."
    mom "Please don't tell anyone. I have just wanted this so much. I've wanted you so much!"
    pov "Of course not. Just as I said, it'll be our dirty little secret."
    povi "Damn, I can't believe she wanted this too."
    if inc == True:
        povi "My own mom is pleasuring me.."
    else:
        povi "My mom's best friend is pleasuring me."
    if base10pmnicred == True:
        scene basement 10pm 070cbbj
    else:
        scene basement 10pm 070cabj
    povi "Such beautiful eyes."
    if inc == True:
        pov "That is so good mom. I love the way you watch me while you play."
    else:
        pov "That is so good [mother]. I love the way you watch me while you play."
    mom "<lick>"
    pov "You're tongue is amazing."
    mom "I really appreciate all you do baby. I really think you'll change things here."
    pov "I'm happy to help out now that I'm home."
    if base10pmnicred == True:
        scene basement 10pm 071cbbj
    else:
        scene basement 10pm 071cabj
    pov "Oh yes!"
    mom "<suck>"
    pov "You're mouth feels so warm and wet."
    mom "Hm... <suck>"
    if base10pmnicred == True:
        scene basement 10pm 072cbbj
    else:
        scene basement 10pm 072cabj
    pov "Ohh..."
    if inc == True:
        pov "You're so good to me, mom!"
    else:
        pov "You're so good to me, [mother]!"
    mom "<suck> <lick>"
    povi "Amazing! I wonder if she would..."
    call screen base10niclovebjchoose

screen base10niclovebjchoose():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_unihand_love_%s.png" action (Hide('base10niclovebjchoose'), Jump('base10pmniclovedp')) hovered tt.Action ("Ask her (deepthroat)") focus_mask True
        imagebutton auto "gui/icons/icon_abort_love_%s.png" action (Hide('base10niclovebjchoose'), Jump('base10pmniclovebj')) hovered tt.Action ("Let her be") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmniclovedp:
    if inc == True:
        pov "Mom, there is something I've always wanted to do."
    else:
        pov "[mother], there is something I've always wanted to do."
    pov "Can you deepthroat my cock?"
    if base10pmnicred == True:
        scene basement 10pm 072cbbjdp
    else:
        scene basement 10pm 072cabjdp
    mom "Hnng?"
    "Her eyes are filled with surprise as you place your hands on her head."
    mom "...yessh."
    "She nods as she tries to say yes with her mouth full of cock."
    if inc == True:
        pov "Really? That's awesome mom!"
    else:
        pov "Really? That's awesome [pov]!"
    pov "I love a woman that can take all of me in her mouth."
    if base10pmnicred == True:
        image dtred_basement = Movie(channel="dtred_basement", play="images/anim/dtred_basement.webm")
        scene dtred_basement with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    else:
        image dt_basement = Movie(channel="dt_basement", play="images/anim/dt_basement.webm")
        scene dt_basement with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    pov "Holy shit! Yopu're taking me deep."
    mom "Hmm... <suck>"
    if inc == True:
        pov "I'm in heaven. My mom is deepthroating me!"
        pov "Youl make me very happy, mom."
        pov "Fulfilling your son's wish."
    else:
        pov "I'm in heaven. [mother] is deepthroating me!"
        pov "You make me very happy, [mother]."
        pov "Fulfilling my wish."
    "Suddenly she impales herself deeper on your cock, invading her throat even deeper."
    if base10pmnicred == True:
        scene basement 10pm 074cbbjdp
    else:
        scene basement 10pm 074cabjdp
    povi "Oh fuck, she can take it even deeper!"
    mom "<suck> <choke>"
    pov "That is so hot. Just a little bit longer. I'm going to cum very soon."
    if inc == True:
        povi "Deep in my mom's throat!"
        pov "Oh yes, HNG!"
        with vpunch
        pov "I'm cumming! I'm cumming in your throat, mom!"
    else:
        povi "Deep in [mother]'s throat!"
        pov "Oh yes, HNG!"
        with vpunch
        pov "I'm cumming! I'm cumming in your throat, [mother]!"
    mom "HNNG! <gulp> <gulp>"
    pov "Good girl. Swallow it all!"
    if base10pmnicred == True:
        scene edited basement 10pm 075red
    else:
        scene edited basement 10pm 075school
    mom "Did you like that baby? I was worried for moment there I wouldn't be able to swallow it all!"
    pov "That was amazing! I didn't expect you to take it so deep!"
    mom "Well... I do have a few secrets you know!"
    pov "That is true. I bet I'm going to find out all your secrets in time."
    if inc == True:
        pov "But seriously, that was amazing, mom."
    else:
        pov "But seriously, that was amazing, [mother]."
    pov "You did so well..."
    mom "Hnn..."
    if inc == True:
        mom "You know I love you so much, right son?"
        pov "Of course I do! I love you too mom."
    else:
        mom "You know I love you so much, right [pov]?"
        pov "Of course I do! I love you too [mother]."
    pov "I'm glad you decided to share this time with me down here."
    mom "Me too, sweetie."
    jump base10pmniccorend

label base10pmniclovebj:
    povi "Let's see what she's got."
    if base10pmnicred == True:
        scene basement 10pm 073cbbj
    else:
        scene basement 10pm 073cabj
    if inc == True:
        pov "Oh yes mom! Please don't stop!"
    else:
        pov "Oh yes [mother]! Please don't stop!"
    mom "Hmm... <suck>"
    pov "You enjoy this too, don't you?"
    mom "Hmm... yesh..."
    pov "Then I'm happy, that we can share this dirty secret."
    "She sucks you wilder."
    pov "Oh, oh."
    if inc == True:
        pov "I'm about to cum, mom!"
    else:
        pov "I'm about to cum, [mother]!"
    call screen base10pmniclovebjcum

screen base10pmniclovebjcum():
    default tt = Tooltip ("")

    hbox xalign .5 yalign .1:

        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmniclovebjcum'), Jump('base10pmniclovebjm')) hovered tt.Action ("Cum in her mouth") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" action (Hide('base10pmniclovebjcum'), Jump('base10pmniclovebjf')) hovered tt.Action ("Cum on her face") focus_mask True

    frame:
        if tt.value == "" or tt.value ==" ":
            background None
        xalign .5
        text tt.value

label base10pmniclovebjf:
    if inc == True:
        pov "I going to cum on your face, mom!"
    else:
        pov "I going to cum on your face, [mother]!"
    mom "Hmm..."
    if base10pmnicred == True:
        scene basement 10pm 074cbbjf
    else:
        scene basement 10pm 074cabjf
    pov "HNG! Oh yes!"
    "You cum on her face."
    if base10pmnicred == True:
        scene basement 10pm 075cbbjf
    else:
        scene basement 10pm 075cabjf
    pov "Wow!"
    mom "You came a lot."
    if inc == True:
        pov "You gave me a great blowjob, mom!"
    else:
        pov "You gave me a great blowjob, [mother]!"
    mom "I can feel it... on my face."
    pov "What you can do with your mouth is just amazing."
    mom "Thank you... I love you sweetie."
    pov "I love you too."
    jump base10pmnicloveend

label base10pmniclovebjm:
    if inc == True:
        pov "I want to cum in your mouth, mom!"
    else:
        pov "I want to cum in your mouth, [mother]!"
    mom "Hmm..."
    pov "HNG! Oh yes!"
    "You cum in her mouth."
    if base10pmnicred == True:
        scene basement 10pm 074cbbjm
    else:
        scene basement 10pm 074cabjm
    povi "Oh god. She's showing me my cum."
    pov "I sure came a lot."
    mom "Hnng..."
    if inc == True:
        pov "Now be a good mom and swallow my cum."
        pov "I want you to taste your son's seed."
    else:
        pov "Now be a good girl and swallow my cum."
        pov "I want you to taste my seed."
    if base10pmnicred == True:
        scene basement 10pm 075cbbjm
    else:
        scene basement 10pm 075cabjm
    mom "<gulp> <gulp>"
    povi "It's so much that she can't swallow it all at once."
    povi "And that lewd stare she's giving me."
    mom "<gulp>"
    if base10pmnicred == True:
        scene basement 10pm 076cbbjm
    else:
        scene basement 10pm 076cabjm
    povi "She even opens her mouth to show me that she swallowed it all. Awesome!"
    if inc == True:
        pov "Very good mom. I'm so glad you could taste me."
    else:
        pov "Very good [mother]. I'm so glad you could taste me."
    mom "I did that just for you."
    pov "And I appreciate that very much."
    mom "You came a lot."
    if inc == True:
        pov "You gave me a great blowjob, mom!"
    else:
        pov "You gave me a great blowjob, [mother]!"
    pov "What you can do with your mouth is just amazing."
    mom "Thank you... I love you sweetie."
    pov "I love you too."
    jump base10pmnicloveend

label base10pmnicloveend:
    scene black
    "Satisfied you two leave the basement."
    $ dtime += 1
    jump kitchen

#----- edited scene -----
label basement23listen:
    hide screen locations
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene main basement door
    povi "Maybe I can hear something?"
    dad "No wait! You shouldn't do that."
    mom "Calm down, honey!"
    davide "I'll do what I want!"
    povi "Whats happening?"
    mom "Oh my god!"
    davide "Nice!"
    call screen checkdarkerpaths_nicole
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Aaah... hah... hah..."
        povi "No, I can't believe it. Are they really doing it?!"
        mom "Hmm... Yes..."
        if inc == True:
            povi "And dad is watching?"
        else:
            povi "And Bruce is watching?"
        mom "Harder!"
    elif nicole_revenge == True or nicole_sadist == True:
        mom "I fucking hate you!"
        if nicole_revenge == True:
            povi "No, I can't believe it. Is Davide raping her?!"
            if inc == True:
                povi "And dad is just watching? Why doesn't he try to stop it?"
                mom "Please, just stop! It hurts!"
            else:
                povi "And Bruce is just watching? Why doesn't he try to stop it?"
                mom "Please, just stop! It hurts!"
            povi "Why is this happening?"
        else:
            povi "Is David raping her?! I wonder if they would let me join?"
            mom "Haah... Ohhh..."
            if inc == True:
                povi "And dad is just watching? I wonder if he's into that shit?"
                mom "Please, just stop! It hurts!"
            else:
                povi "And Bruce is just watching? I wonder if he's into that shit?"
                mom "Please, just stop! It hurts!"
            povi "Doesn't sound like she's into it though! Haha."
        mom "Ugh... Haah..."
    else:
        mom "Aaah... hah... hah..."
        povi "It sounds like people haveing sex?!"
        if inc == True:
            povi "And is dad down there just watching?"
        else:
            povi "And is Bruce down there just watching?"
    povi "I have to find a way to get in the basement."
    $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump basement

#----- edited scene -----
label basement24listen:
    hide screen locations
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene main basement door
    call screen checkdarkerpaths_nicole
    if nicole_voyeur == True or nicole_ntr == True:
        mom "Hah... aahh... please don't stop!"
    elif nicole_revenge == True or nicole_sadist == True:
        mom "Haa... aah... please stop this!"
    else:
        mom "Hah... aahh... hnn...!"
    if nicole_voyeur == True or nicole_ntr == True:
        if nicole_voyeur == True:
            povi "Wow, She's so dirty! Bitch really likes it!"
            povi "I wonder if they are going to keep going."
        else:
            povi "I don't want to hear this anymore! But I can't leave yet."
            povi "Just in case something else happens."
        mom "Harder!"
        povi "They won't do this all night, will they?"
        mom "Hmm..."
    elif nicole_revenge == True or nicole_sadist == True:
        if nicole_revenge == True:
            mom "Please... help me Bruce!"
            povi "This can't go on all night can it?! Please God no!"
            mom "<Sobs quietly>"
        else:
            mom "Please... help me Bruce!"
            povi "This can't go on all night can it?! Please God no!"
            mom "<Sobs quietly>"
    else:
        mom "So deep!"
        povi "Are they seriously going to be doing this all night?"
        mom "Hmm..."
    davide "Move your ass more!"
    povi "That damn asshole!"
    $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump basement

label sellingdrugs1:
    hide screen locations
    scene basement bruce sell1
    povi "What's he doing down here? He seems sad."
    if inc == True:
        pov "Dad?"
    else:
        pov "Bruce?"
    scene basement bruce sell2
    dad "[pov]!"
    dad "I need your help!"
    pov "What's up? What can I do?"
    scene basement bruce sell3
    dad "I promised Davide I would sell some drugs, but I need to meet with someone he can't know."
    pov "From the police?"
    dad "Something like that, yeah."
    pov "You're selling drugs here in the basement?"
    dad "Yes, the people behave when they're here."
    pov "Otherwise they don't get any?"
    dad "Yes, exactly! The people come from in the outside door and wait here."
    dad "We've never had any problems."
    pov "OK, if you say so."
    scene basement bruce sell4
    dad "I know you're a higher-ranked member, so I can only ask you to do it."
    if inc == True:
        pov "No problem dad, I can do it."
    else:
        pov "No problem Bruce, I can do it."
    scene basement bruce sell5
    dad "Thank you so much [pov]."
    dad "And feel free to sell them whenever you want."
    pov "You mean that I should sell them at other times too."
    dad "Yes, that'll be a good training for you how the gang operates."
    dad "You will need to learn much."
    pov "O... OK. What's the price?"
    dad "20 Bucks."
    $ selldrugs = True
    scene black
    "He leaves the basement."
    jump sellingdrugs2

label sellingdrugs2:
    hide screen locations
    $ randomnum = renpy.random.randint(1,2)
    if randomnum == 1:
        scene basement selling drugs male
    elif randomnum == 2:
        scene basement selling drugs female
    if randomnum == 1:
        "Customer" "Four candy please."
        pov "80 Bucks."
        "Customer" "Here."
        $ money += 80
    elif randomnum == 2:
        "Customer" "Five candies please."
        pov "100 Bucks."
        "Customer" "Hm..."
        $ money += 100
    $ selldrugsamount += 1
    scene black
    if selldrugsamount == 1:
        jump sellingdrugs2
    else:
        "No more customers for today."
    $ dtime += 1
    jump kitchen

#----- Custom Scene -----
label dadcasdarkpathlisten:
    hide screen locations
    dad "[bs] are you down here?"
    if inc == True:
        povi "Why is Dad looking for [bs] in the basement? She's not allowed down there..."
    else:
        povi "Why is Bruce looking for [bs] in the basement? She's not allowed down there..."
    jump basement

label dadcasdarkpathopen:
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    hide screen locations
    povi "I better see what's going on down there. I'll be quiet so they don't know I'm there."
    call screen checkdarkerpaths_cassandra
    "You carefully open the door and sneak down the stairs, hiding as soon as you get to the bottom."
    scene edited basement dadcas 01 #Dad hands on head
    dad "[bs] what are you..."
    dad "<gasps>"
    povi "Looks like she came down here after the partying at the club earlier. She's out cold."
    scene edited basement dadcas 02 #Dad overlooking Cassandra
    dad "[bs] are you awake?"
    if cassandra_voyeur == True:
        if inc == True:
            povi "Wow, I'm fairly certain he is checking her out. Good on you Dad!"
        else:
            povi "Wow, I'm fairly certain he is checking her out. Good on you Bruce!"
    elif cassandra_ntr == True:
        povi "That bastard! He's checking her out now! She's your daughter you asshole!"
    elif cassandra_revenge == True:
        povi "After all the shit he's shoveled on this family, he better not be checking her out right now!"
    else:
        povi "Is it just me or is he not staring at her with fatherly love?"
    "You watch as he moves in closer and drops to one need behind her."
    scene edited basement dadcas 03 #Dad lifting up dress
    dad "My god, her pussy looks amazing. I know she's grown up a lot recently, but... damn."
    if cassandra_voyeur == True:
        povi "I know right? Imagine how I feel, being gone for a year and coming back to that!"
    elif cassandra_ntr == True:
        if inc == True:
            povi "I can't believe it! First I have Davide perving on my women and now I have to deal with dad too?!"
        else:
            povi "I can't believe it! First I have Davide perving on my women and now I have to deal with dad too?!"
    elif cassandra_revenge == True:
        povi "Seriously?! I'm going to kick his ass. He has better things to be doing. Instead of perving on your daughter, why don't you work on completing your damn operation?"
    else:
        povi "About time! You have a choice piece of ass sitting right there, just asking to be punished!"
    scene edited basement dadcas 04 #Dad masterbating over Cassandra
    dad "Forgive me [bs]. I just need a release. It will be quick. You won't even remember it."
    if cassandra_voyeur == True:
        povi "Strange flex, but ok. Just go for it! No need to be ashamed."
    elif cassandra_ntr == True:
        povi "Sick prick. She wouldn't want anything to do with you if she wasn't passed the fuck out."
    elif cassandra_revenge == True:
        povi "I should do something. But what is he going to do if he knows I caught him? I mean he is a cop and could cause a lot of trouble."
    else:
        povi "Come on! At least leave a couple marks on her. Just so she wonders what happened to her when she wakes up."
    scene edited basement dadcas 05 #Dad fingering and licking butthole
    bs "Hmmm... Hnnn..."
    if cassandra_voyeur == True:
        povi "He's just digging right in there. She seems to be feeling it at least."
    elif cassandra_ntr == True:
        povi "Get your disgusting hands off her. I'm going to figure out a way to tell [mother] about this!"
    elif cassandra_revenge == True:
        povi "I might not have a choice. He doesn't seem like he's going to hurt her, just use her. If that changes I'm going to have to step in and stop this once and for all."
    else:
        povi "There you go. That's a step in the right direction."
    dad "Do you like that baby? Is daddy making you feel good?"
    bs "Hnng.... Hah..."
    scene edited basement dadcas 06 #Dad fucking Cassandra
    dad "God baby, your pussy is so damn tight!!!"
    if cassandra_voyeur == True:
        povi "I know right?! She's a wonderful girl!"
    elif cassandra_ntr == True:
        povi "You sick freak! She's not even awake, otherwise she'd kick your ass!"
    elif cassandra_revenge == True:
        povi "That fucking asshole is getting into it."
    else:
        povi "That's right, stretch her tight pussy!"
    bs "Hah... Hnng.... Hah..."
    scene edited basement dadcas 07 #Dad fucking Cassandra legs spread
    dad "You like that baby? Do you like that! Daddy's fucking your pussy!"
    bs "Ohhh... Hmmm...."
    if cassandra_voyeur == True:
        povi "I'm sure she would if she were actually awake! Hehe."
    elif cassandra_ntr == True:
        povi "Stop it! Just stop it! She wouldn't want you!"
    elif cassandra_revenge == True:
        povi "She's not going to answer you, dumbass!"
    else:
        povi "Show her who's daddy! Make her whimper!"
    scene edited basement dadcas 08 #Dad fucking Cassandra legs in the air
    dad "Yeah bitch! Take that cock! Take it! Oh fuck you're so wet!"
    if cassandra_voyeur == True:
        povi "Wow, going with the smack talk I see. Whatever helps things along I suppose."
    elif cassandra_ntr == True:
        povi "Talking smack to an unconscious girl, really?!? What a fucking loser! I hate you!"
    elif cassandra_revenge == True:
        povi "Really, you're going to smack talk to an unconscious girl? Your daughter no less?"
    else:
        povi "There you go. Showing the Bitch a good time. Doesn't matter she won't remember it later."
    bs "Haa... Hnng... Huh..."
    scene edited basement dadcas 09 #Dad face fucking Cassandra
    dad "Here slut, take this fat fucking dick!"
    if cassandra_voyeur == True:
        povi "Hehe, he's really really getting down with that whole bad-boy attitude."
    elif cassandra_ntr == True:
        povi "Your tiny dick! You're a worthless piece of shit! I wish I could stop him!"
    elif cassandra_revenge == True:
        povi "Yeah... He really has issues. That worries me."
    else:
        povi "Hell yeah! Stuff it down the slut's throat!"
    bs "Mhmph! Mhmmm..."
    scene edited basement dadcas 10 #Dad cumming in mouth
    dad "HNNNG!!!"
    if cassandra_voyeur == True:
        povi "Nice, fill her up. She likes that."
    elif cassandra_ntr == True:
        povi "Nooooo!"
    elif cassandra_revenge == True:
        povi "Well at least he's finished now. Hopefully he'll leave soon and I can help [bs] get out of here."
    else:
        povi "Fill her stomach!"
    bs "<gulp> <gulp>"
    scene edited basement dadcas 11 #Aftermath
    "Shit! Shit! Shit! What the fuck did I just do?! I'll make this up to you baby. I'm so sorry."
    if cassandra_voyeur == True:
        povi "Relax, relax. No one was hurt. It's ok to have some fun every now and then."
    elif cassandra_ntr == True:
        povi "That's right asshole! You're a horrible person, go crawl into a corner an die!"
    elif cassandra_revenge == True:
        povi "Oh come on! You know exactly what you just did, you sick fuck."
    else:
        povi "Oh come on, don't be such a fucking pussy Bruce! Bitch needed it anyway."
    "You see him start to leave and then he looks back over at [bs] and stops..."
    image dadcas_fuck = Movie(channel="dadcas_fuck", play="images/edited/basement/dadcas mov.webm")
    scene dadcas_fuck with dissolve:
        size (config.screen_width, config.screen_height)
    if cassandra_voyeur == True:
        povi "I guess he decided to continue after all, good for him."
    elif cassandra_ntr == True:
        povi "No! No no no no nooooo! I can't do anything to stop him!"
    elif cassandra_revenge == True:
        povi "Well I guess that piece of shit wasn't that sorry after all. What a fucking loser."
    else:
        povi "Now that's what I'm talking about. Use that pussy until it's raw!"
    pause
    bs "Hunn... Huh... ahh..."
    if dadcasbasementfirst == False:
        $ dadcasbasementfirst = True
    $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump basement

#----- custom scene -----
label basement23and24landing:
    if basement23and24viewed == False:
        jump basement23and24first
    else:
        jump basement23and24repeat

#----- custom scene -----
label basement23and24first:
    hide screen locations
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene main basement door
    "You go to open the door when you hear something inside."
    call screen checkdarkerpaths_nicole
    if nicole_voyeur == True or nicole_ntr == True:
        dad "No wait! You can't do that!"
        mom "Calm down, honey..."
        davide "Shut the fuck up Bruce!"
        povi "Whats happening?"
        mom "Oh my god!"
        davide "Nice!"
        "You slowly open the door and sneak downstairs..."
        scene nicdavntrslow
        with Fade(1, 0.0, 1)
        mom "Aaah... hah... hah..."
        povi "No, I can't believe it. Are they really doing it?!"
        mom "Hmm... Yes..."
        if inc == True:
            povi "And dad is just sitting there watching?"
        else:
            povi "And Bruce is just sitting there watching?"
        mom "Harder! Please fuck me Harder!"
        if nicole_voyeur == True:
            povi "Wow, she's really getting into it!"
        else:
            povi "Why is this happening?!"
        scene nicdavntrfast
        davide "You hear that Bruce? I can't let a bitch down!"
        if nicole_voyeur == True:
            povi "He's right you know. It would be the definition of rude!"
        else:
            povi "I hate him! I hate Bruce... but I can't do anything to stop him either."
        davide "Take this you dirty slut!"
        with vpunch
        dad "..."
        mom "Oh god yes!!!"
        with vpunch
        mom "I'm a... hnng... dirty... hah... slut!"
        if nicole_voyeur == True:
            povi "Yeah you are, I love it!"
        else:
            povi "You are! You're a whore! I'm going to make you regret this!"
        davide "Get ready to take my seed bitch."
        scene edited basement 11pm LikeFinish
        with vpunch
        davide "ARGHHH!"
        mom "HAHhhhng!"
        "The both finish together."
        scene edited basement 11pm LikeEnd
        "Bruce finally comes out of his nearly frozen expression of surprise and slumps down defeated."
        mom "Hnnng... do it again..."
        if nicole_voyeur == True:
            povi "Well I think I'm going to take this as my cue to leave, for now."
        else:
            povi "I'm not going to watch this again..."
    else: #----- revenge and sadist paths -----
        dad "No wait! You can't do that!"
        mom "Help me please, honey!"
        davide "I'll do what I want!"
        povi "Whats happening?"
        mom "Noooo!"
        davide "Nice!"
        mom "I hate you..."
        "You carefully open the door and sneak downstairs..."
        scene nicdavntrslow
        with Fade(1, 0.0, 1)
        if nicole_revenge == True:
            if inc == True:
                povi "No, I can't believe it. Davide is raping her?!"
                povi "And dad is just watching? Why doesn't he try to stop it?"
                mom "Please, just stop! It hurts!"
                povi "Why is this happening?"
            else:
                povi "No, I can't believe it. Davide is raping her?!"
                povi "And Bruce is just watching? Why doesn't he try to stop it?"
                mom "Please, just stop! It hurts!"
                povi "Why is this happening?"
        else:
            povi "Is David raping her?! I wonder if they would let me join?"
            mom "Haah... Ohhh..."
            if inc == True:
                povi "And dad is just watching? I wonder if he's into that shit?"
                mom "Please, just stop! It hurts!"
            else:
                povi "And Bruce is just watching? I wonder if he's into that shit?"
                mom "Please, just stop! It hurts!"
            povi "I don't know why this is this happening, but I like it."
            povi "Doesn't sound like she's into it though! Haha."
        mom "Ugh... Haah..."
        davide "Move your ass more!"
        scene nicdavntrfast
        with vpunch
        mom "GAhhh!"
        davide "Don't worry, I'm not going to last much longer slut!"
        if nicole_revenge == True:
            povi "I'm going to kill that asshole. Seriously, he's not getting away with this."
        else:
            povi "Yeah, I wouldn't either, fucking that bitch in front of her husband, perfect!"
        mom "No! Stop! Hah... don't..."
        davide "Yeah take it, bitch!"
        if nicole_revenge == True:
            povi "Noooo!"
        else:
            povi "Yes! Take it!"
        scene edited basement 11pm DislikeFinish
        with vpunch
        davide "ARGHHH...!"
        mom "..."
        "[mother] is still for a moment and it looks like she has just given up..."
        if nicole_revenge == True:
            povi "She's just stopped trying to fight him. I'm so sorry!"
        else:
            povi "Finally she's accepted this is her life now!"
        scene edited basement 11pm DislikeEnd
        "...when she suddenly screams out and starts hitting and pushing Davide off her."
        mom "Get the hell off of me you asshole! You've had your fun, now just leave us alone!"
        davide "Damn woman, stop hitting me. I'm done with your bitch ass anyway!"
        if nicole_revenge == True:
            povi "That's it! Keep fighting. We'll find a way to stop him for good."
            pov "You decide to leave so you don't get caught and make Nicole embarassed again."
        else:
            povi "God damn she's stubburn. I guess I'll get my turn to break her after all."
            "You decide to leave before they see you down there. It's not time to let them know what you know."
    $ basement23and24viewed == True
    if dtime == 23:
        $ dtime += 2
    else:
        $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump basement

#----- custom scene -----
label basement23and24repeat:
    hide screen locations
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/NTR.mp3"
    scene main basement door
    "You go to open the door when you hear something inside."
    call screen checkdarkerpaths_nicole
    if nicole_voyeur == True or nicole_ntr == True:
        dad "No wait! You can't do that!"
        mom "Calm down, honey..."
        davide "Shut the fuck up Bruce!"
        mom "Oh my god!"
        davide "Nice!"
        "You slowly open the door and sneak downstairs..."
        scene nicdavntrslow
        with Fade(1, 0.0, 1)
        mom "Aaah... hah... hah..."
        povi "They're really doing it again?!"
        mom "Hmm... Yes..."
        if inc == True:
            povi "And dad is still just sitting there watching?"
        else:
            povi "And Bruce is still just sitting there watching?"
        mom "Harder! Please fuck me Harder!"
        if nicole_voyeur == True:
            povi "She's really getting into it again!"
        else:
            povi "Why is this happening again?!"
        scene nicdavntrfast
        davide "You hear that Bruce? I can't let a bitch down!"
        if nicole_voyeur == True:
            povi "He's right you know. It would be the definition of rude!"
        else:
            povi "I hate him! I hate Bruce... but I can't do anything to stop him either."
        davide "Take this you dirty slut!"
        with vpunch
        dad "..."
        mom "Oh god yes!!!"
        with vpunch
        mom "I'm a... hnng... dirty... hah... slut!"
        if nicole_voyeur == True:
            povi "Yeah you are, I love it!"
        else:
            povi "You are! You're a whore! I'm going to make you regret this!"
        davide "Get ready to take my seed bitch."
        scene edited basement 11pm LikeFinish
        with vpunch
        davide "ARGHHH!"
        mom "HAHhhhng!"
        "The both finish together."
        scene edited basement 11pm LikeEnd
        "Bruce finally comes out of his nearly frozen expression of surprise and slumps down defeated."
        mom "Hnnng... do it again..."
        if nicole_voyeur == True:
            povi "Well I think I'm going to take this as my cue to leave, for now."
        else:
            povi "I'm not going to watch this again..."
    else: #----- revenge and sadist paths -----
        dad "No wait! You can't do that!"
        mom "Help me please, honey!"
        davide "I'll do what I want!"
        mom "Noooo!"
        davide "Nice!"
        mom "I hate you..."
        "You carefully open the door and sneak downstairs..."
        scene nicdavntrslow
        with Fade(1, 0.0, 1)
        if nicole_revenge == True:
            if inc == True:
                povi "Davide is raping her again?!"
                povi "And dad is still just watching? Why doesn't he try to stop it?"
                mom "Please, just stop! It hurts!"
                povi "Why is this happening again?"
            else:
                povi "Davide is raping her again?!"
                povi "And Bruce is still just watching? Why doesn't he try to stop it?"
                mom "Please, just stop! It hurts!"
                povi "Why is this happening again?"
        else:
            povi "Is David raping her again?! I wonder if they would let me join this time?"
            mom "Haah... Ohhh..."
            if inc == True:
                povi "And dad is just watching again. He must be into this."
                mom "Please, just stop! It hurts!"
            else:
                povi "And Bruce is just watching again. He must be into this."
                mom "Please, just stop! It hurts!"
            povi "I don't know why this is this happening again, but I like it."
            povi "Doesn't sound like she's into it still! Haha."
        mom "Ugh... Haah..."
        davide "Move your ass more!"
        scene nicdavntrfast
        with vpunch
        mom "GAhhh!"
        davide "Don't worry, I'm not going to last much longer slut!"
        if nicole_revenge == True:
            povi "I'm going to kill that asshole. Seriously, he's not getting away with this."
        else:
            povi "Yeah, I wouldn't either, fucking that bitch in front of her husband again, perfect!"
        mom "No! Stop! Hah... don't..."
        davide "Yeah take it, bitch!"
        if nicole_revenge == True:
            povi "Noooo!"
        else:
            povi "Yes! Take it!"
        scene edited basement 11pm DislikeFinish
        with vpunch
        davide "ARGHHH...!"
        mom "..."
        "[mother] is still for a moment and it looks like she has just given up..."
        if nicole_revenge == True:
            povi "She's just stopped trying to fight him. I'm so sorry!"
        else:
            povi "Finally she's accepted this is her life this time!"
        scene edited basement 11pm DislikeEnd
        "...when she suddenly screams out and starts hitting and pushing Davide off her."
        mom "Get the hell off of me you asshole! You've had your fun, now just leave us alone!"
        davide "Damn woman, stop hitting me. I'm done with your bitch ass anyway!"
        if nicole_revenge == True:
            povi "That's it! Keep fighting. We'll find a way to stop him for good."
            pov "You decide to leave so you don't get caught and make Nicole embarassed again."
        else:
            povi "God damn she's stubburn. I guess I'll get my turn to break her after all."
            "You decide to leave before they see you down there. It's not time to let them know what you know."
    if dtime == 23:
        $ dtime += 2
    else:
        $ dtime += 1
    if gamemusic == True and renpy.music.is_playing("bgm") == False:
        stop music fadeout 2
        play music "music/default.mp3"
    jump basement
