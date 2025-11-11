init python:
    mods["tmlp_start"] = u"{font=tmlp/images/gui/fonts/gotham_pro_medium.ttf}Петля времени{/font}"

    try:
        modsImages["tmlp_start"] = (TMLP_GUI_PATH + "misc/tabular_list_preview.png", False)

    except:
        pass

label tmlp_start:
    $ tmlp_set_dynamic_cursor("null")
    $ renpy.pause(3, hard=True)
    $ din_onload("lock")
    $ tmlp_random_menu_theme()
    $ tmlp_screens_save_act()
    $ tmlp_set_dynamic_cursor("main_menu")
    $ tmlp_set_time("day")
    $ tmlp_set_mode_adv()
