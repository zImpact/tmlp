init python:
    mods["tmlp_start"] = u"{font=tmlp/images/gui/fonts/gotham_pro_medium.ttf}Петля времени{/font}"

    try:
        modsImages["tmlp_start"] = ("tmlp/images/gui/misc/tmlp_tabular_list_preview.png", False)

    except:
        pass

label tmlp_start:
    $ persistent.timeofday = "prologue"
    $ tmlp_screens_save_act()
    $ tmlp_set_mode_adv()
    #$ tmlp_camera_reset()
    # $ tmlp_layer_move("background_layer", 2000)
    # $ tmlp_layer_move("middle_layer", 1500)
    # $ tmlp_layer_move("forward_layer", 1000)

    # if persistent.tmlp_firstrun == False:
    #     $ renpy.pause(2, hard = True)
    #     $ renpy.movie_cutscene("tmlp/images/gui/part_two_introes/part_two.webm")
    #     jump tmlp_part_one_prologue_day_one

    # else:
    #     pass