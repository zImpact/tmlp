init python:
    from random import Random
    from os import path

    for file_name in renpy.list_files():
        if TMLP_MOD_NAME in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith(TMLP_MOD_NAME + "/images/bg/"):
                bg_name = "bg " + TMLP_PREFIX + file_path

                if file_name.endswith(".ogv"):
                    renpy.image(bg_name, Movie(fps=45, play=file_name))

                else:
                    renpy.image(bg_name, file_name)

            elif file_name.startswith(TMLP_MOD_NAME + "/images/sprites/"):
                renpy.image(
                    TMLP_PREFIX + file_path,
                    ConditionSwitch(
                        "persistent.sprite_time == 'sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)),
                        "persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)),
                        True, file_name
                    )
                )

            elif file_name.startswith(TMLP_MOD_NAME + "/sounds/"):
                globals()[TMLP_PREFIX + file_path] = file_name

    store.tmlp_colors = {}
    store.tmlp_names = {}
    store.tmlp_names_list = []
    tmlp_speaker_color = "speaker_color"

    store.tmlp_names_list.append("tmlp_narrator")

    store.tmlp_names_list.append("tmlp_th")

    tmlp_colors["tmlp_din"] = {"speaker_color": "#551313"}
    tmlp_names["tmlp_din"] = "Дин"
    store.tmlp_names_list.append("tmlp_din")

    tmlp_colors["tmlp_pi_pyan"] = {"speaker_color": "#551313"} # TODO: цвет поменять
    tmlp_names["tmlp_pi_pyan"] = "Пионер"
    store.tmlp_names_list.append("tmlp_pi_pyan")

    tmlp_colors["tmlp_pyan"] = {"speaker_color": "#551313"} # TODO: цвет поменять
    tmlp_names["tmlp_pyan"] = "Пьяница"
    store.tmlp_names_list.append("tmlp_pyan")

    tmlp_colors["tmlp_pacifist"] = {"speaker_color": "#088010"}
    tmlp_names["tmlp_pacifist"] = "Пацифист"
    store.tmlp_names_list.append("tmlp_pacifist")

    tmlp_colors["tmlp_un"] = {"speaker_color": "#aa64d9"}
    tmlp_names["tmlp_un"] = "Лена"
    store.tmlp_names_list.append("tmlp_un")

    tmlp_colors["tmlp_dv"] = {"speaker_color": "#ffaa00"}
    tmlp_names["tmlp_dv"] = "Двачевская"
    store.tmlp_names_list.append("tmlp_dv")

    tmlp_colors["tmlp_sl"] = {"speaker_color": "#ffd200"}
    tmlp_names["tmlp_sl"] = "Славяна"
    store.tmlp_names_list.append("tmlp_sl")

    def tmlp_char_define(character_name, is_nvl=False):
        global DynamicCharacter
        global nvl
        global tmlp_store
        global tmlp_speaker_color
        tmlp_gl = globals()

        if character_name == "tmlp_narrator":
            if is_nvl:
                tmlp_gl["tmlp_narrator"] = Character(
                    None,
                    kind=nvl,
                    what_style="tmlp_text_style"
                )

            else:
                tmlp_gl["tmlp_narrator"] = Character(
                    None,
                    what_style="tmlp_text_style"
                )

            return

        if character_name == "tmlp_th":
            if  is_nvl:
                tmlp_gl["tmlp_th"] = Character(
                    None,
                    kind=nvl,
                    what_style="tmlp_text_style",
                    what_prefix="~ ",
                    what_suffix=" ~"
                )

            else:
                tmlp_gl["tmlp_th"] = Character(
                    None,
                    what_style="tmlp_text_style",
                    what_prefix="~ ",
                    what_suffix=" ~"
                )

            return

        if is_nvl:
            tmlp_gl[character_name] = DynamicCharacter(
                "%s_name" % character_name,
                color=store.tmlp_colors[character_name][tmlp_speaker_color],
                kind=nvl,
                what_style="tmlp_text_style",
                who_suffix=":"
            )
            tmlp_gl["%s_name" % character_name] = store.tmlp_names[character_name]

        else:
            tmlp_gl[character_name] = DynamicCharacter(
                "%s_name" % character_name,
                color=store.tmlp_colors[character_name][tmlp_speaker_color],
                what_style="tmlp_text_style"
            )
            tmlp_gl["%s_name" % character_name] = store.tmlp_names[character_name]

    def tmlp_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global tmlp_store

        for character_name in store.tmlp_names_list:
            tmlp_char_define(character_name)

    def tmlp_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global tmlp_narrator
        global tmlp_th
        tmlp_narrator_nvl = tmlp_narrator
        th_nvl = tmlp_th
        
        global tmlp_store
        
        for character_name in store.tmlp_names_list:
            tmlp_char_define(character_name, True)

    def tmlp_reload_names():
        global tmlp_store

        for character_name in store.tmlp_names_list:
            tmlp_char_define(character_name)


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

    def tmlp_set_time(timeofday, sprite_time=None):
        if sprite_time is None:
            sprite_time = timeofday
        
        renpy.block_rollback()
        persistent.timeofday = timeofday
        persistent.sprite_time = sprite_time

init:
    image tmlp_part_one_main_menu = Movie(fps = 45, play = TMLP_GUI_PATH + "main_menu_part_one/tmlp_part_one_main_menu.webm")

    image tmlp_part_one_main_menu_1of3 = tmlp_frame_animation(TMLP_GUI_PATH + "main_menu_part_one/1of3_frame_animation/1of3", 20, 1, True, dissolve)
    image tmlp_stars_anim = tmlp_frame_animation("tmlp/images/bg/anim_bg/tmlp_stars/stars", 2, 1.5, True, Dissolve(1.5))
    image bg tmlp_int_catacombs_living_celling_blurred = im.Blur("tmlp/images/bg/part1/tmlp_int_catacombs_living_celling.png", 2)


    $ tmlp_transition = ImageDissolve(TMLP_GUI_PATH + "transitions/glitch.png", 2, 50, reverse = False)
    $ tmlp_glitch_transition = MultipleTransition([True, Dissolve(0.5), "tmlp/images/gui/transitions/glitch/1.png", Pause(1.0), "tmlp/images/gui/transitions/glitch/2.png", dissolve, True])

    if persistent.tmlp_firstrun == None:
        $ persistent.tmlp_firstrun = False

    if persistent.tmlp_part_one_completed == None:
        $ persistent.tmlp_part_one_completed = False

    if persistent.tmlp_part_two_completed == None:
        $ persistent.tmlp_part_two_completed = False

    # Списки для рандомизации главного меню
    $ tmlp_menu_backgrounds = [
        "tmlp_part_one_main_menu",
        "tmlp_part_one_main_menu_1of3",
        "tmlp_part2_main_menu_bg"
    ]

    $ tmlp_menu_music = [
        tmlp_mega_drive_narc,
        tmlp_stigmata_tanwui,
        tmlp_yoko_kanno_total_eclipse
    ]

    # Инициализируем глобальные переменные для рандомизации
    if not hasattr(store, 'tmlp_menu_choice'):
        $ store.tmlp_menu_choice = 0
    if not hasattr(store, 'tmlp_music_choice'):
        $ store.tmlp_music_choice = 0

    # Рандомизация выбора меню и музыки при каждом запуске
    $ store.tmlp_menu_choice = renpy.random.choice(range(len(tmlp_menu_backgrounds)))
    $ store.tmlp_music_choice = renpy.random.choice(range(len(tmlp_menu_music)))

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