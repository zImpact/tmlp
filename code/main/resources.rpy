init python:
    from random import Random
    from os import path

    tmlp_mod_name = "tmlp"
    tmlp_prefix = tmlp_mod_name + "_"

    for file_name in renpy.list_files():
        if tmlp_mod_name in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith(tmlp_mod_name + "/images/bg/"):
                bg_name = "bg " + tmlp_prefix + file_path

                if file_name.endswith(".ogv"):
                    renpy.image(bg_name, Movie(fps=45, play=file_name))

                else:
                    renpy.image(bg_name, file_name)

            elif file_name.startswith(tmlp_mod_name + "/images/sprites/"):
                renpy.image(
                    tmlp_prefix + file_path,
                    ConditionSwitch(
                        "persistent.sprite_time == 'sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)),
                        "persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)),
                        True, file_name
                    )
                )

            elif file_name.startswith(tmlp_mod_name + "/sounds/"):
                globals()[tmlp_prefix + file_path] = file_name

    tmlp_std_set_for_preview = {}
    tmlp_std_set = {}
    store.tmlp_colors = {}
    store.tmlp_names = {}
    store.tmlp_names_list = []
    tmlp_speaker_color = "speaker_color"

    store.tmlp_names_list.append("tmlp_narrator")

    store.tmlp_names_list.append("tmlp_th")

    tmlp_colors["tmlp_din"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_din"] = "Дин"
    store.tmlp_names_list.append("tmlp_din")

    tmlp_colors["tmlp_dinp"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_dinp"] = "Пионер"
    store.tmlp_names_list.append("tmlp_dinp")

    tmlp_colors["tmlp_pyan"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_pyan"] = "Пьяница"
    store.tmlp_names_list.append("tmlp_pyan")

    tmlp_colors["tmlp_pyap"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_pyap"] = "Пионер"
    store.tmlp_names_list.append("tmlp_pyap")

    tmlp_colors["tmlp_plyaj"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_plyaj"] = "Пляжник"
    store.tmlp_names_list.append("tmlp_plyaj")

    tmlp_colors["tmlp_plyajp"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_plyajp"] = "Пионер"
    store.tmlp_names_list.append("tmlp_plyajp")

    tmlp_colors["tmlp_voice"] = {"speaker_color": (225, 221, 125, 255)}
    tmlp_names["tmlp_voice"] = "Голос"
    store.tmlp_names_list.append("tmlp_voice")

    tmlp_colors["tmlp_sam"] = {"speaker_color": (225, 221, 125, 255)}
    tmlp_names["tmlp_sam"] = "Семён"
    store.tmlp_names_list.append("tmlp_sam")

    tmlp_colors["tmlp_myself"] = {"speaker_color": (6, 91, 13, 255)}
    tmlp_names["tmlp_myself"] = "Я"
    store.tmlp_names_list.append("tmlp_myself")

    tmlp_colors["tmlp_el"] = {"speaker_color": (205, 205, 0, 255)}
    tmlp_names["tmlp_el"] = "Электроник"
    store.tmlp_names_list.append("tmlp_el")

    tmlp_colors["tmlp_un"] = {"speaker_color": (170, 100, 217, 255)}
    tmlp_names["tmlp_un"] = "Леночка"
    store.tmlp_names_list.append("tmlp_un")

    tmlp_colors["tmlp_dv"] = {"speaker_color": (210, 139, 16, 255)}
    tmlp_names["tmlp_dv"] = "Двачевская"
    store.tmlp_names_list.append("tmlp_dv")

    tmlp_colors["tmlp_sl"] = {"speaker_color": (214, 176, 0, 255)}
    tmlp_names["tmlp_sl"] = "Славяна"
    store.tmlp_names_list.append("tmlp_sl")

    tmlp_colors["tmlp_us"] = {"speaker_color": (234, 55, 0, 255)}
    tmlp_names["tmlp_us"] = "Мелкая"
    store.tmlp_names_list.append("tmlp_us")

    tmlp_colors["tmlp_mt"] = {"speaker_color": (0, 182, 39, 255)}
    tmlp_names["tmlp_mt"] = "Вожатая"
    store.tmlp_names_list.append("tmlp_mt")

    tmlp_colors["tmlp_cs"] = {"speaker_color": (134, 134, 230, 255)}
    tmlp_names["tmlp_cs"] = "Медсестра"
    store.tmlp_names_list.append("tmlp_cs")

    tmlp_colors["tmlp_mz"] = {"speaker_color": (84, 129, 219, 255)}
    tmlp_names["tmlp_mz"] = "Библиотекарша"
    store.tmlp_names_list.append("tmlp_mz")

    tmlp_colors["tmlp_mi"] = {"speaker_color": (0, 180, 207, 255)}
    tmlp_names["tmlp_mi"] = "Мику"
    store.tmlp_names_list.append("tmlp_mi")

    tmlp_colors["tmlp_uv"] = {"speaker_color": (64, 208, 0, 255)}
    tmlp_names["tmlp_uv"] = "Юля"
    store.tmlp_names_list.append("tmlp_uv")

    tmlp_colors["tmlp_sh"] = {"speaker_color": (205, 194, 18, 255)}
    tmlp_names["tmlp_sh"] = "Шурик"
    store.tmlp_names_list.append("tmlp_sh")

    tmlp_colors["tmlp_pi"] = {"speaker_color": (230, 0, 0, 255)}
    tmlp_names["tmlp_pi"] = "Пионер"
    store.tmlp_names_list.append("tmlp_pi")

    tmlp_colors["tmlp_bush"] = {"speaker_color": (192, 192, 192, 255)}
    tmlp_names["tmlp_bush"] = "Голос"
    store.tmlp_names_list.append("tmlp_bush")

    def tmlp_char_define(x, is_nvl=False):
        global DynamicCharacter
        global nvl
        global tmlp_store
        global tmlp_speaker_color
        tmlp_gl = globals()

        if x == "tmlp_narrator":
            if is_nvl:
                tmlp_gl["tmlp_narrator"] = Character(None, kind=nvl, what_style="tmlp_text_style", ctc="none", ctc_position="fixed")

            else:
                tmlp_gl["tmlp_narrator"] = Character(None, what_style="tmlp_text_style", ctc="none", ctc_position="fixed")

            return

        if x == "tmlp_th":
            if  is_nvl:
                tmlp_gl["tmlp_th"] = Character(None, kind=nvl, what_style="tmlp_text_style", what_prefix="~ ", what_suffix=" ~", ctc="none", ctc_position="fixed")

            else:
                tmlp_gl["tmlp_th"] = Character(None, what_style="tmlp_text_style", what_prefix="~ ", what_suffix=" ~", ctc="none", ctc_position="fixed")

            return

        if is_nvl:
            tmlp_gl[x] = DynamicCharacter("%s_name" % x, color=store.tmlp_colors[x][tmlp_speaker_color], kind=nvl, what_style="tmlp_text_style", who_suffix=":", ctc="none", ctc_position="fixed")
            tmlp_gl["%s_name" % x] = store.tmlp_names[x]

        else:
            tmlp_gl[x] = DynamicCharacter("%s_name" % x, color=store.tmlp_colors[x][tmlp_speaker_color], what_style="tmlp_text_style", ctc="none", ctc_position="fixed")
            tmlp_gl["%s_name" % x] = store.tmlp_names[x]

    def tmlp_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global tmlp_store

        for x in store.tmlp_names_list:
            tmlp_char_define(x)

    def tmlp_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global tmlp_narrator
        global tmlp_th
        tmlp_narrator_nvl = tmlp_narrator
        th_nvl = tmlp_th
        
        global tmlp_store
        
        for x in store.tmlp_names_list:
            tmlp_char_define(x, True)

    def tmlp_reload_names():
        global tmlp_store

        for x in store.tmlp_names_list:
            tmlp_char_define(x)

    tmlp_reload_names()

    def tmlp_day_intro(day_numeral, tmlp_save_name, text_output = "adv", tmlp_part = "one"):
        global save_name
        
        tmlp_part_one_introes_path = tmlp_gui_path + "part_one_introes/part_one_day_"
        tmlp_part_two_intro_path = tmlp_gui_path + "part_two_intro/part_two.webm"
        tmlp_part_three_intro_path = tmlp_gui_path + "part_three_intro/part_three.webm"
        
        save_name = tmlp_save_name

        renpy.pause(1, hard = True)

        if tmlp_part == "one":
            renpy.movie_cutscene(tmlp_part_one_introes_path + str(day_numeral) + ".webm")

        elif tmlp_part == "two":
            renpy.movie_cutscene(tmlp_part_two_intro_path)

        elif tmlp_part == "three":
            renpy.movie_cutscene(tmlp_part_three_intro_path)
        
        renpy.pause(1, hard = True)
        
        if text_output == "adv":
            tmlp_set_mode_adv()

        else:
            tmlp_set_mode_nvl()

    def tmlp_blink(blink_pause):
        renpy.show("blink")
        renpy.pause(blink_pause, hard=True)

    def tmlp_unblink(scene_name, unblink_pause):
        renpy.hide("blink")
        renpy.scene()
        renpy.show(scene_name)
        renpy.show("unblink")
        renpy.pause(unblink_pause, hard=True)

    def tmlp_frame_animation(image_name, frames_quantity, retention, loop, transition, start=1, **properties):
        if image_name:
            anim_args = []

            for i in range(start, start + frames_quantity):
                anim_args.append(renpy.display.im.image(image_name + "_" + str(i) + ".png"))

                if loop:
                    anim_args.append(retention)
                    anim_args.append(transition)

            return anim.TransitionAnimation(*anim_args, **properties)
        return None

init:
    image tmlp_part_one_main_menu = Movie(fps = 45, play = tmlp_gui_path + "main_menu_part_one/tmlp_part_one_main_menu.webm")

    image tmlp_part_one_main_menu_1of3 = tmlp_frame_animation(tmlp_gui_path + "main_menu_part_one/1of3_frame_animation/1of3", 20, 1, True, dissolve)
    image tmlp_stars_anim = tmlp_frame_animation("tmlp/images/bg/anim_bg/tmlp_stars/stars", 2, 1.5, True, Dissolve(1.5))
    image bg tmlp_int_catacombs_living_celling_blurred = im.Blur("tmlp/images/bg/part1/tmlp_int_catacombs_living_celling.png", 2)

    # image tmlp_part_one_main_menu_1of3_glitch = tmlp_glitches(tmlp_gui_path + "main_menu/part1/1of3_static.png", 1)
    # image tmlp_text = tmlp_glitches(tmlp_gui_path + "main_menu_part_one/tmlp_text.png")

    $ tmlp_transition = ImageDissolve(tmlp_gui_path + "transitions/glitch.png", 2, 50, reverse = False)
    $ tmlp_glitch_transition = MultipleTransition([True, Dissolve(0.5), "tmlp/images/gui/transitions/glitch/1.png", Pause(1.0), "tmlp/images/gui/transitions/glitch/2.png", dissolve, True])

    if persistent.tmlp_firstrun == None:
        $ persistent.tmlp_firstrun = False

    if persistent.tmlp_part_one_completed == None:
        $ persistent.tmlp_part_one_completed = False

    if persistent.tmlp_part_two_completed == None:
        $ persistent.tmlp_part_two_completed = False

    $ tmlp_pyan_contempt = 0
    $ tmlp_diary_active = False

    transform tmlp_bus_moving():
        subpixel True
        truecenter
        zoom 1.03

        parallel:
            linear 0.2 xoffset -2
            linear 0.3 xoffset 3
            linear 0.2 xoffset -1
            linear 0.3 xoffset 2
            repeat

        parallel:
            linear 0.2 yoffset -1
            linear 0.25 yoffset 2
            linear 0.2 yoffset -1
            repeat