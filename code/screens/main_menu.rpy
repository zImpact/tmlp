screen tmlp_main_menu():
    tag menu
    modal True

    key "game_menu":
        action NullAction()

    key "K_F1":
        action NullAction()

    add persistent.tmlp_main_menu_background

    text "Петля времени":
        font tmlp_gotham_pro_medium
        size 85
        xalign 0.5
        ypos 25

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
            Hide("tmlp_main_menu"),
            ShowMenu("tmlp_load_main_menu")
        ]

    textbutton "Дополнительно":
        style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
        text_style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
        xalign 0.5
        ypos 540
        action [
            Hide("tmlp_main_menu"),
            ShowMenu("tmlp_extra_main_menu")
        ]

    textbutton "Настройки":
        style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
        text_style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
        xalign 0.5
        ypos 685
        action [
            Hide("tmlp_main_menu"),
            ShowMenu("tmlp_preferences_main_menu")
        ]

    textbutton "Выход":
        style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
        text_style "tmlp_main_menu_theme_" + persistent.tmlp_theme_number + "_style"
        xalign 0.5
        ypos 830
        action [
            Hide("tmlp_main_menu"),
            ShowMenu("tmlp_quit_main_menu")
        ]

    imagebutton:
        auto TMLP_GUI_PATH + "misc/logowhite_%s.png"
        xpos 1520
        ypos 800
        action OpenURL("https://vk.com/public176281709")
