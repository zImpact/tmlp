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