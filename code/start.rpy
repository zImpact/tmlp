init python:
    mods["timeloop_start"] = u"{font=timeloop/images/gui/fonts/gotham_pro_medium.ttf}Петля времени{/font}"

    try:
        modsImages["timeloop_start"] = ("timeloop/images/gui/misc/tl_tabular_list_preview.png", False)

    except:
        pass

label timeloop_start:
    $ persistent.timeofday = "prologue"
    $ timeloop_screens_save_act()
    $ timeloop_set_mode_adv()
    #$ timeloop_camera_reset()
    # $ timeloop_layer_move("background_layer", 2000)
    # $ timeloop_layer_move("middle_layer", 1500)
    # $ timeloop_layer_move("forward_layer", 1000)

    # if persistent.timeloop_firstrun == False:
    #     $ renpy.pause(2, hard = True)
    #     $ renpy.movie_cutscene("timeloop/images/gui/part_two_introes/part_two.webm")
    #     jump timeloop_part_one_prologue_day_one

    # else:
    #     pass