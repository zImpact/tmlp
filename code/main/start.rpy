init python:
    mods["tmlp_start"] = u"{font=tmlp/images/gui/fonts/gotham_pro_medium.ttf}Петля времени{/font}"

    try:
        modsImages["tmlp_start"] = (TMLP_GUI_PATH + "misc/tabular_list_preview.png", False)

    except:
        pass

label tmlp_start:
    $ tmlp_random_menu_theme()
    $ tmlp_set_time(OSD_TIMEOFDAY_PROLOGUE)
    $ tmlp_onload("lock")
    $ tmlp_set_dynamic_cursor("main_menu")
    $ tmlp_screens_save_act()
    scene bg black with Dissolve(2)
    $ renpy.pause(0.5, hard=True)
    scene osd_sky_day
    show osd_intro_logo at truecenter
    show osd_blank_skip
    with Dissolve(2)
    $ renpy.pause(0.5, hard=True) 
    play sound osd_intro_sample
    $ renpy.pause(8, hard=True)
    scene bg black with Dissolve(2)
    $ renpy.pause(0.5, hard=True)
    $ tmlp_set_mode_adv()

    label tmlp_after_intro:
        $ tmlp_onload("unlock")
        stop sound
        $ renpy.transition(Dissolve(2))
