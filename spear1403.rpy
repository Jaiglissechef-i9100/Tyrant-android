

init:
    python hide:


        config.gestures ['s']='hide_windows'





        if not persistent.set_skip_unseen:
            persistent.set_skip_unseen = True
            _preferences.skip_unseen = True

init:

    style quick_button is default:

        background None
        xpadding 20

    style quick_button_text is default:

        size 35
        outlines [(2, "#000",0,0)]
        idle_color "#ffff"
        hover_color "#336600"

screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.995
        yalign 1.0
        xanchor 1.0

        if quick_menu:

            textbutton _("Hide") action HideInterface()

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()
            textbutton (">") action [ SetVariable('quick_menu', False ), SetVariable('quick_menu2', True )]

        if quick_menu2:

            textbutton ("<") action [ SetVariable('quick_menu', True ), SetVariable('quick_menu2', False )]