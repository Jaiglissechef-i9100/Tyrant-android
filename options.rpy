













define config.name = _("The Tyrant")





define gui.show_name = False




define config.version = "0.8.2-android"





define gui.about = _("")






define build.name = "TheTyrant"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "TheTyrant-1504059355"






define config.window_icon = "gui/window_icon.png"

init python:

    config.automatic_images = [ ' ', '_', '-', '/' ]

    config.automatic_images_strip = [ 'images', 'update71', 'update75p1', 'update75p2' ]






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("game/**.rpy", None)








    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("update71", "all")
    build.archive("update75p1", "all")
    build.archive("update75p2", "all")




    build.classify("game/**.rpyc", "scripts")



    build.classify('game/images/**.jpg', 'images')
    build.classify('game/images/**.png', 'images')    
    build.classify('game/images/**.webm', 'images')
    build.classify('game/images/**.webp', 'images')
    build.classify('game/gui/**.jpg', 'images')
    build.classify('game/gui/**.png', 'images')    
    build.classify('game/gui/**.webm', 'images')



    build.classify('game/update71/**.jpg', 'update71')
    build.classify('game/update71/**.png', 'update71')    
    build.classify('game/update71/**.webm', 'update71')
    build.classify('game/update75p1/**.jpg', 'update75p1')
    build.classify('game/update75p1/**.png', 'update75p1')    
    build.classify('game/update75p1/**.webm', 'update75p1')
    build.classify('game/update75p2/**.jpg', 'update75p2')
    build.classify('game/update75p2/**.png', 'update75p2')    
    build.classify('game/update75p2/**.webp', 'update75p2')   
    build.classify('game/update75p2/**.webm', 'update75p2')





    build.documentation('*.html')
    build.documentation('*.txt')