#----- Edited by S A Z ----- Completed 0.75 Part 1 and 2 Mod A

init: #----- Edited -----
    #----- Custom -----
    define povname = None
    define lsname = None
    define bsname = None
    define nicolename = None
    define brucename = None
    define brucename = None
    define momname = None
    define dadname = None
    define irinaname = None
    define susanname = None
    define katename = None
    define vivianname = None
    define mirandaname = None
    define rubyname = None
    #----- End -----
    define pov = Character("[povname]", who_color="#0066cc", what_color="#ffffff")
    define povi = Character("[povname]", what_italic=True, who_color="#0066cc", what_color="#ff8000") #----- Added -----
    define ls = Character("[lsname]", who_color="#ea9aff", what_color="#ea9aff")
    define bs = Character("[bsname]", who_color="#ea9aff", what_color="#ea9aff")
    define mother = Character("[nicolename]", who_color="#ea9aff", what_color="#ea9aff")
    define father = Character("[brucename]", who_color="#ff3533", what_color="#ff3533") #----- Not Used -----
    define mom = Character("[momname]", who_color="#ea9aff", what_color="#ea9aff")
    define dad = Character("[dadname]", who_color="#ff3533", what_color="#ff3533")
    define irina = Character("[irinaname]", who_color="#ea9aff", what_color="#ea9aff")
    define susan = Character("[susanname]", who_color="#ea9aff", what_color="#ea9aff")
    define kate = Character("[katename]", who_color="#ea9aff", what_color="#ea9aff")
    define vivian = Character("[vivianname]", who_color="#ea9aff", what_color="#ea9aff")
    define miranda = Character("[mirandaname]", who_color="#ea9aff", what_color="#ea9aff")
    define ruby = Character("[rubyname]", who_color="#ea9aff", what_color="#ea9aff")
    define davide = Character("Davide", who_color="#ff3533", what_color="#ff3533")
    define frank = Character("Frank", who_color="#ff3533", what_color="#ff3533")
    define martin = Character("Martin", who_color="#ff3533", what_color="#ff3533")
    define steve = Character("Steve", who_color="#ff3533", what_color="#ff3533")
    define dummy = Character("Dummy", who_color="#0066cc", what_color="#ffffff")
    define n = Character(None, kind=nvl)
    $ cr1 = "{color=ff0000}+Corruption{/color}"
    $ lv1 = "{color=3cff00}+Love{/color}"
    $ bd1 = "{color=ff0000}+Bad{/color}"
    $ gd1 = "{color=3cff00}+Good{/color}"
    $ inc = False
    #----- Custom -----
    $ cr2 = "{color=ff0000}Corruption{/color}"
    $ lv2 = "{color=3cff00}Love{/color}"
    $ rp1 = "{color=0000ff}+Relationship{/color}"
    $ rp2 = "{color=0000ff}Relationship{/color}"
    image novel_back = "gui/game_menu.png"

init python:
    config.empty_window = nvl_show_core

label splashscreen:
    scene black
    with Pause(1)
    show warning with dissolve
    with Pause(7)
    scene black with dissolve
    with Pause(1)
    return

label start:
    scene novel_back
    window show
    n "Hello!"
    n "This is Saz. And you're playing my Expanded Story Mod for The Tyrant."
    n "I made this because I loved the story concept and wanted more content. But I also wanted to differentiate the paths you can choose even more. I have taken the NTR path and split it into four separate paths story wise."
    nvl clear
    n "The NTR content has been seperated into four \"Darker Paths\" for this mod. Voyeur, NTR, Revenge and Sadist."
    n "Voyeur. The MC enjoys the things being done to the girls and frankly so do the girls, they just need to admit it to themselves."
    n "NTR. This and the Voyeur path are the closest to the the original story. In this path, the MC hates what is happening around here, despite the girls secretly, or not so secretly, being into it."
    nvl clear
    n "Revenge. In this path, the girls do not like what is being done to them. They are doing their best in a shitty situation, but often coming up short. The MC wants to help them but can't yet. But when he can, he's going to help them get back at them. Hard."
    n "Sadist. This path, like the Revenge path, follows the girls being forced to do things against their will. But in path, the MC is into it and he's willing to the same to the girls if he gets the chance."
    n "Due to the nature of their stories, both the Revenge and the Sadist paths have aspects of rape/blackmail/threats of violence. I just wanted to give you a heads up just in case."
    nvl clear
    n "The Love and Corruption paths have been extended to help make them more robust. There are corruption scenes written for the love path scenes and vice versa. Essentially doubling the amount of love and corruption content."
    n "I also used some scenes using fan art from the {a=https://f95zone.com/threads/the-tyrant-fan-art-thread.7538/}Fan Art Thread{/a}. This wasn't used with permission, so if any artist wants me to remove their images I would be happy to."
    n "I added a cheat menu in the phone which you can access with the Cheat Menu button. I've boosted how much you make from the cleaning job and selling drugs. So it should be less grindy. You can just give yourself money in the Cheat Menu too."
    nvl clear
    n "This game normally contains NTR (netorare). But if you don't want to see it in your game you have the option to turn it off. It won't happen in your game then. This option is set for the whole game, so if you want to play another game with it on, you'll need to start a new game."
    n "What is NTR? {a=http://www.urbandictionary.com/define.php?term=NTR}See here.{/a}"
    nvl clear

    n "Turn NTR on? These are the Darker Paths in the Mod. This will allow access to the Voyeur, NTR, Sadist, and Revenge Paths."
    window hide
    nvl clear

    menu:
        "Yes - Turn NTR (Darker Paths) On":
            $ NTR = True
            window show
            n "NTR (Darker Paths) is now set to ON."
        "No - Turn NTR (Darker Paths) Off":
            window show
            n "NTR (Darker Paths) is now set to OFF."

    if NTR == True:
        n "Select the initial path you want to play. You will be able to change these settings at various times during the game later on for each of the girls."
        window hide
        nvl clear

        menu:
            "Voyeur - Main Character doesn't care if the women are getting strange D. He'll use it to get what he wants.":
                $ nicole_voyeur = True
                $ nicole_ntr = False
                $ nicole_revenge = False
                $ nicole_sadist = False
                $ alexis_voyeur = True
                $ alexis_ntr = False
                $ alexis_revenge = False
                $ alexis_sadist = False
                $ cassandra_voyeur = True
                $ cassandra_ntr = False
                $ cassandra_revenge = False
                $ cassandra_sadist = False
                $ irina_voyeur = True
                $ irina_ntr = False
                $ irina_revenge = False
                $ irina_sadist = False
                window show
                n "Voyeur path selected."
            "NTR - Main Character doesn't want the women to enjoy the strange D, but they do enjoy it. Sucks to be him.":
                $ nicole_voyeur = False
                $ nicole_ntr = True
                $ nicole_revenge = False
                $ nicole_sadist = False
                $ alexis_voyeur = False
                $ alexis_ntr = True
                $ alexis_revenge = False
                $ alexis_sadist = False
                $ cassandra_voyeur = False
                $ cassandra_ntr = True
                $ cassandra_revenge = False
                $ cassandra_sadist = False
                $ irina_voyeur = False
                $ irina_ntr = True
                $ irina_revenge = False
                $ irina_sadist = False
                window show
                n "NTR path selected."
            "Revenge - Main Character doesn't want this to be happening, neither do the women. They are going to get payback!":
                $ nicole_voyeur = False
                $ nicole_ntr = False
                $ nicole_revenge = True
                $ nicole_sadist = False
                $ alexis_voyeur = False
                $ alexis_ntr = False
                $ alexis_revenge = True
                $ alexis_sadist = False
                $ cassandra_voyeur = False
                $ cassandra_ntr = False
                $ cassandra_revenge = True
                $ cassandra_sadist = False
                $ irina_voyeur = False
                $ irina_ntr = False
                $ irina_revenge = True
                $ irina_sadist = False
                window show
                n "Revenge path selected."
            "Sadist - Main Character doesn't like that the girls are getting strange D against their will... he loves it! Bring on the pain!":
                $ nicole_voyeur = False
                $ nicole_ntr = False
                $ nicole_revenge = False
                $ nicole_sadist = True
                $ alexis_voyeur = False
                $ alexis_ntr = False
                $ alexis_revenge = False
                $ alexis_sadist = True
                $ cassandra_voyeur = False
                $ cassandra_ntr = False
                $ cassandra_revenge = False
                $ cassandra_sadist = True
                $ irina_voyeur = False
                $ irina_ntr = False
                $ irina_revenge = False
                $ irina_sadist = True
                window show
                n "Sadist path selected."

    n "In this game you alone decide how you play. You can try to corrupt characters, fall in love with them or just stay as friends. You can stick with the main story of the game or ignore it and just play for yourself."
    nvl clear

    n "Turn Incest On?"
    window hide
    nvl clear

    menu:
        "Yes - Turn Incest On":
            $ P1 = False
            $ inc = True
            window show
            n "Incest is now set to ON."
        "No - Turn Incest Off":
            $ P1 = True
            $ inc = False
            window show
            n "Incest is now set to OFF."

    if inc == True:
        n "Enjoy fucking your family!"
    else:
        n "Enjoy fucking someone else's family!"
    window hide
    nvl clear

    if inc == True:
        $ momname = "Mom"
    else:
        $ momname = "Nicole"
    if inc == True:
        $ dadname = "Dad"
    else:
        $ dadname = "Bruce"

    jump intro
    return
