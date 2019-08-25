

label baseorgyaoamirchoose:
    scene basement 10pm 128mm
    pov "Any ideas how I can punish my slut?"
    miranda "Oh, I have a wonderful idea. She'll love it, haha."
    miranda "I always wanted her to lick me! That'd be wonderful!"
    scene basement 10pm 130mm
    mom "No, [pov]! Anything, but not that..."
    pov "It's not your choice, slut!"
    pov "{i}But it's a tempting offer. Seeing some lesbian stuff and maybe having my own fun too.{/i}"
    call screen baseorgyniclosemirchoose

screen baseorgyniclosemirchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 548 ypos 316 action (Hide('baseorgyniclosemirchoose'), Jump('baseorgyaoamirchooseyes')) hovered tt.Action ("You'll please [miranda], slut!") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 1155 ypos 316 action (Hide('baseorgyniclosemirchoose'), Jump('baseorgyaoamirchooseno')) hovered tt.Action ("I'll punish you myself, slut!") focus_mask True


        frame:
            xalign .5
            text tt.value

label baseorgyaoamirchooseyes:
    pov "You can have her and she'll give her best to please you!"
    mom "Hnn..."
    scene basement 10pm 133mmnl
    miranda "Did you hear that slut? We're going to have fun!"
    mom "Hnn..."
    miranda "Make sure you please me good, I'm so wet I want to feel your tongue!"
    mom "Please [miranda]..."
    miranda "Oh no! You need to know your place, slut! <giggle>"
    scene basement 10pm 134mmnl
    miranda "Stop beeing mad!"
    if inc == True:
        miranda "I chose you to please me, so I won't touch your son. And this is something you want too."
    else:
        miranda "I chose you to please me, so I won't touch [pov]. And this is something you want too."
    mom "Hmm?"
    miranda "Protect him from me, wanting to do really perverted things with him!"
    pov "{i}Haha, she knows how to press [mother]'s buttons.{/i}"
    miranda "I show some good will, so you need to show some too."
    mom "O... okay..."
    scene basement 10pm 135mmnl
    miranda "Hurry, my pussy is waiting. <giggle>"
    mom "Hmm..."
    davide "Oh yes, this'll be so hot!"
    pov "Make me proud, slut!"
    mom "Hm..."
    scene basement 10pm 136mmnl
    miranda "Isn't that a nice position for your slut. So someone else can have fun too, haha."
    miranda "You want someone special to use you too, slut?"
    mom "..."
    miranda "What a good slut she is, demanding nothing."
    scene basement 10pm 137mmnl
    miranda "Oh yes, your sluts tongue is the best."
    mom "Hnn... <lick>"
    miranda "And look how she's showing off her ass. She need a hard dick, hah..."
    pov "Yes, very hot, haha..."
    scene basement 10pm 138mmnl
    miranda "Oh YES! Right there!"
    mom "Hnn... <lick> <lick>"
    miranda "So good..."
    pov "{i}This is the best!{/i}"
    if inc == True:
        pov "{i}And mom is \"protecting\" me.{/i}"
    else:
        pov "{i}And [mother] is \"protecting\" me.{/i}"
    scene basement 10pm 139mmnl
    pov "And her hot ass, ready to get fucked."
    miranda "Hah... hmm..."
    pov "{i}Should I take care of her? Or just watch the show?{/i}"
    pov "{i}Or maybe make Davide a present? He's so happy about seeing this?{/i}"
    scene basement 10pm 140mmnl
    pov "{i}And [bs] could need some attention too... hmm...{/i}"
    call screen baseorgyniclosemirniclesbchoose

screen baseorgyniclosemirniclesbchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 248 ypos 916 action (Hide('baseorgyniclosemirniclesbchoose'), Jump('baseorgyniclosemirniclesbpfnic')) hovered tt.Action ("{i}I'll fuck her myself, they can watch{/i}") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 455 ypos 916 action (Hide('baseorgyniclosemirniclesbchoose'), Jump('baseorgyniclosemirniclesbpfnicdcas')) hovered tt.Action ("{i}I'll fuck her myself, Davide can have fun with [bs]{/i}") focus_mask True




        frame:
            xalign .5
            text tt.value

label baseorgyniclosemirniclesbpfnicdcas:
    $ basement10nicolelesbiandavidecas = True
    jump baseorgyniclosemirniclesbpfnic

label baseorgyniclosemirniclesbpfnic:
    if basement10nicolelesbiandavidecas == True:
        pov "I need to punish my slut now, but you can have fun with my other slut, haha."
        bs "Eh...?"
        scene basement 10pm 140mmnlsh
        davide "Oh yes, I'll watch a hot lesbian show and fuck your brains out, hot slut!"
        bs "Hnng..."
    else:
        pov "I need to punish my slut now, enjoy the show, haha."
        bs "Eh...?"
        davide "Oh yes, we will, haha."
    pov "{i}Now I have to choose which hole I'll stuff with my dick.{/i}"
    pov "{i}So many choices, haha.{/i}"
    scene basement 10pm 139mmnl
    call screen baseorgyniclosemirniclesbpfnicchoose

screen baseorgyniclosemirniclesbpfnicchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 348 ypos 550 action (Hide('baseorgyniclosemirniclesbpfnicchoose'), Jump('baseorgyniclosemirniclesbpfnicp')) hovered tt.Action ("I'll fuck your pussy, slut!") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 348 ypos 750 action (Hide('baseorgyniclosemirniclesbpfnicchoose'), Jump('baseorgyniclosemirniclesbpfnica')) hovered tt.Action ("I'll fuck your ass, slut!") focus_mask True



        frame:
            xalign .5
            text tt.value

label baseorgyniclosemirniclesbpfnica:
    $ basement10pmnicolelesbianass = True
    jump baseorgyniclosemirniclesbpfnicp

label baseorgyniclosemirniclesbpfnicp:
    if basement10pmnicolelesbianass == True:
        scene basement 10pm 141mmnla
    else:
        scene basement 10pm 141mmnlp
    mom "Hmm... <lick>"
    miranda "Oh, your slut is getting wilder. She's happy to get punished by you, hah."
    pov "Oh, so you want my dick so badly, slut?"
    mom "Hmm... hmm... <lick>"
    pov "I can't hear you, slut!"
    mom "Y... yes... <lick>, please fuck... <lick> me..."
    pov "As you wish!"
    if basement10nicolelesbiandavidecas == True:
        scene basement 10pm 144mmnlsh
        bs "Hmm... <kiss>"
        pov "Huh, Davide is gentle? Did I missed something?"
        miranda "Haha, don't worry about that. I know exactly what he's doing, you'll see."
        mom "Hnng... hnng..."
        pov "So [mother] knows it too?"
        miranda "Haha, yes..."
    scene basement 10pm 142mmnl
    mom "Hnng...! <lick>"
    miranda "Oh hah... hah... she's doing even better now!"
    if basement10pmnicolelesbianass == True:
        pov "And her ass is thighten up too, hah."
    else:
        pov "And her pussy is tighten up too, hah."
    miranda "It's a new thing for her and she's getting so excited, hah..."
    if basement10nicolelesbiandavidecas == True:
        scene basement 10pm 145mmnlsh
        bs "What's with that pill? My body is getting so hot!"
        davide "Oh you'll know it soon, slut!"
        pov "Oh I understand. He gave her the sex drug."
        miranda "Yes, that is he doing when he's kissing someone, haha."
        pov "That'll be a surprise for [bs], haha."
    scene basement 10pm 143mmnl
    if inc == True:
        miranda "Getting fucked from her beloved son while she's licking her enemy, ha... ahh... hah..."
    else:
        miranda "Getting fucked from her beloved [pov] while she's licking her enemy, ha... ahh... hah..."
    mom "<licks faster>"
    pov "Yes, she seems to like it a little too much, haha."
    miranda "Maybe she lost on purpose, haha... hah... hahn..."
    pov "Haha..."
    mom "Hah... hnng... <lick>"
    if basement10nicolelesbiandavidecas == True:
        scene basement 10pm 146mmnlsh
        bs "His hard... hah... dick... hnng..."
        davide "I'll make you scream, bitch!"
        bs "Hnng! Hah... hah..."
        pov "{i}She's piercing me with her eyes. Does she wish I would take her like that?{/i}"
    scene basement 10pm 144mmnl
    miranda "Yes, fuck her harder! She licks even wilder and I'm so close."
    "You fuck [mother] harder."
    mom "Hnng... <lick> <lick>"
    miranda "Oh yes, Yes!"
    scene basement 10pm 145mmnl
    miranda "More slut, don't stop! Hah... hah..."
    mom "Hnn... hnn <lick>"
    miranda "Hah, hah... I'm so close!"
    mom "<choke> <lick>"
    pov "Ahh... she's getting so damn tight!"
    if basement10nicolelesbiandavidecas == True:
        scene basement 10pm 147mmnlsh
        bs "AAAHHH... HAAAHH... HNNG!"
        davide "Yes now you feel real good!"
        bs "Hnng... hnn... MORE!"
        miranda "Hah... see what the drug made with her... hah..."
        pov "{i}Maybe I'll use the drug also when I have fun with her next time.{/i}"
    scene basement 10pm 147mmnl
    miranda "YES! AHH! AHHHH!"
    "[miranda]'s body shakes wildly."
    miranda "So good slut! I'm cumming!"
    pov "{i}Oh shit. [mom]'s trembling so hard, it makes me cum too.{/i}"
    call screen baseorgyniclosemirniclesbpfnicpcum

screen baseorgyniclosemirniclesbpfnicpcum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 348 ypos 550 action (Hide('baseorgyniclosemirniclesbpfnicpcum'), Jump('baseorgyniclosemirniclesbpfnicpin')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 348 ypos 750 action (Hide('baseorgyniclosemirniclesbpfnicpcum'), Jump('baseorgyniclosemirniclesbpfnicpout')) hovered tt.Action ("Cum on her") focus_mask True



        frame:
            xalign .5
            text tt.value

label baseorgyniclosemirniclesbpfnicpin:
    scene basement 10pm 142mmnl
    pov "I'll cum inside you, slut!"
    mom "Hmm... hah..."
    pov "Ahh..."
    if basement10pmnicolelesbianass == True:
        "You cum inside her ass."
    else:
        "You cum inside her pussy."
    pov "{i}Oh, she's shaking. So she came too.{/i}"
    if basement10pmnicolelesbianass == True:
        scene basement 10pm 146mmnlcia
    else:
        scene basement 10pm 146mmnlcip
    mom "Hnng... hah... <lick>"
    miranda "Yes, be a good slut and continue licking. I want to cum more often."
    pov "That was an interesting fuck, haha."
    pov "And my slut will lick you as long as you want. As her punishment."
    mom "Hnng... <lick>"
    miranda "Oh yes!"
    $ basement10pmnicolelesbianass = False
    $ basement10nicolelesbiandavidecas = False
    jump baseorgyend


label baseorgyniclosemirniclesbpfnicpout:
    scene basement 10pm 146mmnlco
    pov "I'll cum on you, slut!"
    mom "Hmm... hah..."
    pov "Ahh..."
    "You cum on her ass."
    pov "{i}Oh, she's shaking. So she came too.{/i}"
    scene basement 10pm 147mmnlco
    mom "Hnng... hah... <lick>"
    miranda "Yes, be a good slut and continue licking. I want to cum more often."
    pov "That was an interesting fuck, haha."
    pov "And my slut will lick you as long as you want. As her punishment."
    mom "Hnng... <lick>"
    miranda "Oh yes!"
    $ basement10pmnicolelesbianass = False
    $ basement10nicolelesbiandavidecas = False
    jump baseorgyend


label baseorgyaoamirchooseno:
    scene basement 10pm 128mm
    pov "I need to punish my slut by myself!"
    miranda "Hmm... then I'll find something to have fun."
    pov "I already know something, I'll punish my slut and I'm sure Davide can help you out!"
    miranda "Ohh... hmm..."
    jump baseorgyniclosepunnicdavmir


label baseorgyaoamirfuck:
    pov "I think I'll have fun with [miranda]."
    mom "Nooo..."
    scene basement 10pm 129mmms
    miranda "What a good choice! I want to feel your young, hard dick inside me!"
    pov "{i}She's so damn horny, she can't wait much longer!{/i}"
    miranda "Please fuck me hard, [pov]!"
    scene basement 10pm 130mmms
    miranda "I'll give you a good time, when your big dick ravage my wet pussy."
    pov "Hmm..."
    miranda "I can feel you moving there, your dick has already decided."
    scene basement 10pm 131mmms
    if inc == True:
        miranda "I'll prove you that I'm a much better slut than your mother!"
    else:
        miranda "I'll prove you that I'm a much better slut than [mother]!"
    mom "[miranda]!"
    miranda "See? She's already jealous."
    scene basement 10pm 132mmms
    miranda "My pussy is so wet! Don't let me wait any longer, [pov]."
    miranda "Please use me as you wish and ravage my body!"
    pov "{i}Damn, her dirty talk is so hot!{/i}"
    scene basement 10pm 133mmms
    davide "Just do it [pov]! Her pussy is so magnificent, you won't regret it."
    mom "Davide!"
    miranda "He's right. And [mother]'s jealousy proves it."
    pov "So it'll be, haha. Get ready, slut!"
    miranda "Yes... yes!"
    scene basement 10pm 135mmms
    pov "{i}She teased me all the time, so she'll get a payback.{/i}"
    "You rub your dick over her pussy lips."
    miranda "Hmm... yes..."
    mom "Hnng..."
    pov "{i}This is also a good punishment for [mother], she'll be more submissive after that.{/i}"
    scene basement 10pm 136mmms
    miranda "Please stop teasing, [pov]. Make me your slut!"
    pov "Haha, relax. You'll go even crazier on my dick then."
    pov "{i}Wow, she so horny. She tries to suck my dick in.{/i}"
    scene basement 10pm 137mmms
    davide "Haha, you're serious? You're so near to the ultimate pleasure."
    pov "Yes and I want to taste every second."
    davide "Just do it, everyone is waiting. Even [bs] is dying from expectation."
    davide "Let her see this big tits shaking, she's staring all the time at them."
    scene basement 10pm 138mmms
    pov "Really? I didn't notice."
    bs "Eh?"
    miranda "It's like Davide said. I bet she want to have also big tits like me!"
    pov "You want to have such big tits as [miranda], slut?"
    bs "I... eh... I don't know..."
    scene basement 10pm 136mmms
    pov "{i}These big udders on [bs]? I don't know...{/i}"
    miranda "And your other slut could need a better place to view us. I want her to see everything close."
    miranda "Don't you think so, [pov]?"
    pov "Yes, you're right. It's her punishment."
    pov "Come here slut!"
    scene basement 10pm 139mmms
    mom "Please [pov]..."
    pov "No more whining! You'll watch us closely and keep your mouth shut!"
    mom "..."
    pov "You disappointed one time, don't do it again."
    mom "Y- yes, you're right [pov]. I'll be a good slut and watch you."
    pov "Good."
    if inc == True:
        pov "{i}Haha, [bs] is so confused. Seeing mom being so submissive towards me.{/i}"
    else:
        pov "{i}Haha, [bs] is so confused. Seeing her mother being so submissive towards me.{/i}"
    scene basement 10pm 140mmms
    "You ram your dick all in [miranda]'s pussy."
    miranda "AAAAHHH..."
    pov "This is what you needed!"
    miranda "Haaah... so big..."
    "You start to fuck her fast and rough!"
    scene basement 10pm 141mmms
    miranda "Yes! Hah... hah... you stud!"
    pov "{i}That pussy is sucking me in. Really a fine fuck.{/i}"
    mom "..."
    miranda "Look [mother]!"
    if inc == True:
        miranda "Your son is drilling me! Hah... hah..."
    else:
        miranda "[pov] is drilling me! Hah... hah..."
    pov "{i}What's with [bs]? She's biting her finger. Does she want also such a hard fuck?{/i}"
    pov "{i}Or is she admiring [miranda], with her big udders?{/i}"
    miranda "Hah... hah... ahhh... more!"
    pov "{i}Maybe I can spice this up?{/i}"
    pov "Do you want to join us [bs]? You look so excited, haha."
    scene basement 10pm 142mmms
    bs "Eh?"
    pov "You staring like a bitch in heat at us."
    miranda "Does she?"
    davide "Oh yes, haha."
    miranda "Come here [bs], closer to me."
    pov "Go to her, slut."
    bs "O...ok."
    scene basement 10pm 143mmms
    bs "HNNG...?"
    miranda "<kiss> <lick>"
    davide "Two sluts making out, while you fuck one of them. So hot!"
    pov "Oh yes, enjoy it, [bs]!"
    scene basement 10pm 144mmms
    bs "Hmm... <kiss> <lick>"
    miranda "Hah... <kiss> hah..."
    pov "{i}This is so hot. [bs] enjoy the kissing and even have fun with [miranda]'s tits.{/i}"
    pov "{i}Her pussy is squeezing my dick even more, since [bs] joined. I'm about to cum.{/i}"
    call screen baseorgyaoamircum

screen baseorgyaoamircum():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 348 ypos 550 action (Hide('baseorgyaoamircum'), Jump('baseorgyaoamircumin')) hovered tt.Action ("Cum inside her") focus_mask True
        imagebutton auto "gui/icons/icon_unihand_%s.png" xpos 348 ypos 750 action (Hide('baseorgyaoamircum'), Jump('baseorgyaoamircumout')) hovered tt.Action ("Cum on her") focus_mask True



        frame:
            xalign .5
            text tt.value

label baseorgyaoamircumin:
    $ basement10nicolemirfuckinside = True
    jump baseorgyaoamircumout

label baseorgyaoamircumout:
    pov "I'm cumming!"
    if basement10nicolemirfuckinside == True:
        scene basement 10pm 140mmms
        "You cum inside her pussy."
    else:
        scene basement 10pm 146mmmso
        "You cum on her."
    pov "Hnng..."
    "You feel her body shaking."
    miranda "Aaahh... yes...!"
    if basement10nicolemirfuckinside == True:
        scene basement 10pm 147mmmsi
    else:
        scene basement 10pm 147mmmso
    miranda "Hah... hah... that was amazing..."
    pov "Oh yes, your pussy drenched me out."
    pov "And see [bs] joining pushed me over the edge."
    miranda "Yes, that slut can learn fast, hah..."
    pov "So you'll have much more fun with [miranda]!"
    bs "Hmm..."
    scene basement 10pm 148mmms
    davide "Damn, that was a hot show."
    pov "Haha, oh yes."
    davide "And I bet your slut is also wet."
    pov "[mother]?"
    scene basement 10pm 149mmms
    pov "So you had your fun too?"
    mom "N... no..."
    pov "Then we need to repeat it more often to get you used to it."
    mom "I... I got wet... I'm sorry [pov]."
    pov "Good girl, maybe you'll get my dick next."
    $ basement10nicolemirfuckinside = False
    jump baseorgyend




























































label casweekendNTR:
    hide screen locations
    scene weekend 4pm 001n
    irina "[pov]! What are you doing here?"
    pov "[bs] invited me."
    irina "Why did she...? Oh maybe..."
    pov "Can I come in?"
    irina "Y- yes..."
    scene weekend 4pm 002n
    irina "Follow me."
    pov "{i}Oh yes, I can't wait to have fun with them again.{/i}"
    scene weekend 4pm 003n
    irina "Maybe this will surprise you, but you must know that [bs] wanted this."
    pov "What are you talking about?"
    irina "You'll see, but don't freak out."
    scene weekend 4pm 004n
    if gamemusic == True:
        stop music fadeout 2
        play music "music/NTR.mp3"
    bs "I love your gift very much daddy!"
    pov "..."
    pov "{i}What the hell? [bs] and Frank, that old geezer?{/i}"
    scene weekend 4pm 005n
    bs "It's so beautiful, I feel really good having it."
    frank "So you're grateful?"
    bs "I'm very grateful. You earned yourself a reward, daddy. <giggle>"
    if irinadatetemplentr == True:
        pov "{i}That reminds me of something. The conversation [irina] had with him. So she helped him to get [bs] finally...{/i}"
        pov "{i}She must have drugged her, maybe the sex-drug. She would be never be so happy with that old fart.{/i}"
    scene weekend 4pm 006n
    irina "Don't be jealous [pov]. She's happy now."
    irina "Someone who adore her and take care of her, especially financially."
    pov "Financially?"
    irina "He's the one who paid for her boobs. And now he reep the rewards for his investition."
    pov "I see..."
    if irinadatetemplentr == True:
        pov "But you're his dirty little helper."
        irina "So you know that I hadn't a choice, life wasn't sometime easy on me."
        pov "But with Frank?"
        irina "She's really happy, you'll see. And you don't need to be alone too. <giggle>"
        pov "{i}So she removed a rival...{/i}"
    scene weekend 4pm 007n
    bs "Oh hi [pov]! You're here too."
    pov "{i}She doesn't even know that she invited me...{/i}"
    frank "Hey [pov]."
    pov "Frank..."
    bs "Look what beautiful things Daddy gifted me... <giggle>"
    pov "{i}So weird...{/i}"
    scene weekend 4pm 008n
    irina "See her happiness. She's fallen for him."
    pov "You tricked her."
    irina "She just needed a little push in the right direction."
    irina "And you don't need to be jealous. I'll fit better on your side."
    pov "{i}Damn, like a headhunter. Hunting for men, literally me.{/i}"
    scene weekend 4pm 009n
    frank "You're so cute, babygirl, I can't await my reward."
    bs "I got so wet when I'm with you, help me, daddy. <giggle>"
    pov "{i}I can't believe this. That [bs] could act like this. But maybe she's really after his money?{/i}"
    pov "Huh?"
    scene weekend 4pm 010n
    pov "What...?"
    irina "No need to hide it, your dick shows how horny you are."
    "She starts to rub your dick slowly."
    irina "I'll give you a good time so you can say goodbye to her with happiness."
    pov "But..."
    scene weekend 4pm 011n
    irina "They're about to get sexual now. It's his first time to have fun with her."
    bs "Your hands are so big, it feels so good."
    frank "Your tits were worth the money. So firm!"
    pov "{i}Do I really want to see this...?{/i}"
    scene weekend 4pm 012n
    irina "Your dick is rock hard. I'm a little jealous that [bs] naked body has this effect on you."
    irina "But I'll let you have this last fun, soon you'll get this hard from my naked body."
    pov "{i}Does she really think she her plan would work?{/i}"
    pov "{i}Maybe I can't stop this now, but I can still ruin her plan and reassure [bs] later.{/i}"
    pov "{i}Or should I let her win and enjoy the new attention of [irina] for me? She'll give her best to be my favourite.{/i}"
    call screen casweekendntrchoose

screen casweekendntrchoose():
    default tt = Tooltip (" ")

    fixed:
        imagebutton auto "gui/icons/icon_approve_%s.png" xpos 567 ypos 123 action (Hide ('casweekendntrchoose'), Jump('casweekendntrchooseyes')) hovered tt.Action ("Let [irina] continue") focus_mask True
        imagebutton auto "gui/icons/icon_disapprove_%s.png" xpos 1275 ypos 123 action (Hide ('casweekendntrchoose'), Jump('casweekendntrchooseno')) hovered tt.Action ("Ruin her plan") focus_mask True


    frame:
        xalign .5
        text tt.value

label casweekendntrchooseno:
    pov "No, I won't play in your little game!"
    scene weekend 4pm 012nn
    irina "What?"
    pov "Maybe you won this round, but I'll get [bs] back to me."
    irina "You... you refuse me... but I can be a better girl for you."
    pov "No, you're evil."
    scene black
    "You leave them. You'll think of something to reassure [bs] and punish [irina] for this."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    $ weekendactivities += 1
    $ casweekendntrno = True
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose

label casweekendntrchooseyes:
    pov "Don't stop rubbing on my dick and it'll play out for you."
    irina "I knew you'd love my kinky side."
    scene weekend 4pm 013n
    bs "Look daddy, [pov] will be our witness, when you do me for our first time."
    frank "That's good. So he can see how I'll make you my girl."
    bs "I'm excited how you'll do that... <giggle>"
    frank "Hard and good, haha..."
    scene weekend 4pm 014n
    irina "Your dick is trembling, you like that [pov], don't you."
    "She grips your dick harder."
    if inc == True:
        irina "Watching your sister getting screwed."
    else:
        irina "Watching [bs] getting screwed."
    irina "Or maybe you're in that \"daddy game\" too?"
    irina "Will you take care of me too and raise me like you want to, daddy? <giggle>"
    irina "We could make our own porn movie, like they do."
    pov "Eh?"
    scene weekend 4pm 018n
    pov "They're filming themselves?"
    irina "Yes, her first time taped and I'm sure they'll do many more movies after that. <giggle>"
    irina "But you don't need to watch it, I'll take care that you won't need porns ever again."
    "She rubs your dick faster."
    scene weekend 4pm 015n
    bs "Haah, daddy... Your dick is so thick, I didn't know..."
    frank "Enjoy it and get used to it, haha!"
    irina "Yes, his thick rod can be a surprise, but don't worry [pov]..."
    irina "I don't want it, it's also small. But yours instead... <giggle>"
    bs "Hah... hnng..."
    scene weekend 4pm 017n
    bs "Hah... hah... ohhh...!"
    frank "You accepted my dick, very good babygirl."
    bs "Yes, hah... more daddy..."
    frank "We'll have much more fun together and I'll mark your insides with my seed very soon."
    bs "Yes, cum inside me, daddy."
    irina "Oh, you're close to cum too, [pov]."
    "She rubs your dick wildly."
    scene weekend 4pm 016n
    pov "Hah... HNNG!"
    "You cum from [irina]'s hand on your dick."
    irina "Yes, show me how much you like it!"
    pov "Hah... hah..."
    scene weekend 4pm 019n
    frank "Do you see this?"
    if inc == True:
        frank "Your brother is cumming from watching us fuck."
    else:
        frank "[pov] is cumming from watching us fuck."
    bs "Hnng... hah, oh yes daddy... AHHH AHHH"
    frank "Yes, cum with me, babygirl."
    bs "AHHH... HAAAH... HAAAHHH!"
    irina "They're such a happy couple. <giggle>"
    scene weekend 4pm 020n
    "[irina] joined them."
    irina "I'll get my reward from [bs]s tongue now, you can leave now [pov]."
    irina "You'll get your reward another time, hah..."
    bs "Daddy promised me to take me to a vacation when I'll lick you good."
    bs "I'll do my best. <giggle>"
    frank "Yes we'll go and I'll take care to fill all your holes with my sperm, babygirl."
    scene black
    "You leave them alone."
    if gamemusic == True:
        stop music fadeout 2
        play music "music/default.mp3"
    $ casweekendntrfirst = True
    $ weekendactivities += 1
    if weekendactivities == 3:
        jump weekendskip
    else:
        jump weekendacchoose
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
