




init -100:
    $ p1 = True


init:
    $ pov = Character("[pov]", color="ffffff", what_color="ffffff")
    $ ls = Character("[ls]", color="#cc00ff", what_color="ffffff")
    $ bs = Character("[bs]", color="007408", what_color="ffffff")
    $ mother = Character("[mother]")
    if p1 == False:
        $ mom = Character("Mom", color="02a9ff", what_color="ffffff")
    else:
        $ mom = Character("[mother]")
    $ father = Character("Bruce")
    $ steve = Character("Steve", color="ffc600", what_color="ffffff")
    $ davide = Character("Davide", color="00fcff", what_color="ffffff")
    $ frank = Character("Frank", color="00fcff", what_color="ffffff")
    if p1 == False:
        $ dad = Character("Dad", color="ff0000", what_color="ffffff")
    else:
        $ dad = Character("Bruce")
    $ martin = Character("Martin", color="ff0000", what_color="ffffff")
    $ irina = Character("[irina]", color="cc00ff", what_color="ffffff")
    $ susan = Character("[susan]", color="cc00ff", what_color="ffffff")
    $ dummy = Character("Dummy", color="cc00ff", what_color="ffffff")
    $ kate = Character("[kate]", color="cc00ff", what_color="ffffff")
    $ vivian = Character("[vivian]", color="cc00ff", what_color="ffffff")
    $ miranda = Character("[miranda]", color="cc00ff", what_color="ffffff")
    $ ruby = Character("[ruby]", color="cc00ff", what_color="ffffff")
    $ n = Character(None, kind=nvl)
    $ cr1 = "{color=ff0000}+Corruption{/color}"
    $ lv1 = "{color=3cff00}+Love{/color}"
    $ bd1 = "{color=ff0000}+Bad{/color}"
    $ gd1 = "{color=3cff00}+Good{/color}"
    if p1 == False:
        $ inc = True
    else:
        $ inc = False




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





    scene black
    window show
    n "This game normally contains NTR (netorare). But if you don't want to see it in your"
    n "game you'll have the option to turn it off and it won't happen in your game."
    n "This option can only be set for the whole game, so if you want to play another game"
    n "with it, you'll need to restart a new game. What is NTR? {a=http://www.urbandictionary.com/define.php?term=NTR}See here.{/a}"
    window hide
    nvl clear     
    window show
    n "Turn NTR on?"

    menu:
        "Yes":
            $ NTR = True
            n "NTR is now set to on."
        "No":

            n "NTR will stay off."



    window hide
    nvl clear       

    "In this game you alone decide how you play. You can try to corrupt characters, fall in love with them or just stay as friends."
    "You can stick with the main story of the game or ignore it and just play for yourself."










    jump intro



    return