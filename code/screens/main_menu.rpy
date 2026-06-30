screen tmlp_main_menu():
    tag menu
    modal True

    key "game_menu":
        action NullAction()

    key "K_F1":
        action NullAction()

    add persistent.tmlp_main_menu_background

    if tmlp_main_menu_var:
        text "Петля времени":
            font tmlp_gotham_pro_medium
            size 105
            xalign 0.5
            ypos 45

        textbutton "Начать":
            style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            text_style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            xalign 0.5
            ypos 250
            action [
                Hide("tmlp_main_menu", Dissolve(1.5)),
                SetVariable("tmlp_lock_quit_game_main_menu_var", False),
                Start("tmpl_main_scenario")
            ]

        textbutton "Загрузить":
            style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            text_style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            xalign 0.5
            ypos 395
            action [
                SetVariable("tmlp_main_menu_var", False),
                ShowMenu("tmlp_load_main_menu")
            ]

        textbutton "Дополнительно":
            style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            text_style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            xalign 0.5
            ypos 540
            action [
                SetVariable("tmlp_main_menu_var", False),
                ShowMenu("tmlp_extra")
            ]

        textbutton "Настройки":
            style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            text_style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            xalign 0.5
            ypos 685
            action [
                SetVariable("tmlp_main_menu_var", False),
                ShowMenu("tmlp_preferences_main_menu")
            ]

        textbutton "Выход":
            style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            text_style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
            xalign 0.5
            ypos 830
            action [
                SetVariable("tmlp_main_menu_var", False),
                ShowMenu("tmlp_quit_main_menu")
            ]

        imagebutton:
            auto TMLP_GUI_PATH + "misc/logowhite_%s.png"
            xpos 1520
            ypos 800
            action OpenURL("https://vk.com/public176281709")

screen tmlp_extra():
    modal True

    key "K_F1":
        action NullAction()
    
    if not tmlp_main_menu_var: 
        add "tmlp_main_menu_options_frame" xalign 0.5 yalign 0.5
        
        text "[TMLP_EXTRA_TEXT]":
            font tmlp_gotham_pro_medium
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "Музыка":
            xalign 0.5
            yalign 0.3
            action [
                Hide("tmlp_extra"),
                ShowMenu("tmlp_music_room")
            ]

        textbutton "Галерея":
            xalign 0.5
            yalign 0.5
            action [
                Hide("tmlp_extra"),
                ShowMenu("tmlp_background_gallery")
            ]

        textbutton "НАЧАЛО КОНЦА":
            xalign 0.5
            yalign 0.7
            action [
                Hide("osd_extra"),
                ShowMenu("osd_achievements")
            ]

        textbutton "[TMLP_RETURN_TEXT]":
            xalign 0.1
            ypos 970
            action [
                SetVariable("tmlp_main_menu_var", True),
                Hide("tmlp_extra"),
                ShowMenu("tmlp_main_menu")
            ]
