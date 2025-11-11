screen tmlp_main_menu():
    tag menu
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add tmlp_menu_backgrounds[store.tmlp_menu_choice] at tmlp_bus_moving()

    text "Петля времени":
        font tmlp_gotham_pro_medium
        size 85
        text_align 0.5
        xalign 0.5
        ypos 25

    textbutton "Начать игру":
        style "tmlp_button_none"
        text_style "tmlp_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 250
        action [
            Hide("tmlp_main_menu"),
            Start("tmlp_prologue")
        ]
            
    textbutton "Загрузить игру":
        style "tmlp_button_none"
        text_style "tmlp_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 395
        action [
            Hide("tmlp_main_menu"),
            ShowMenu("tmlp_load")
        ]
           
    textbutton "Дополнительно":
        style "tmlp_button_none"
        text_style "tmlp_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 540
        action [
            Hide("tmlp_main_menu"),
            ShowMenu("tmlp_part_one_gallery")
        ]

    textbutton "Настройки":
        style "tmlp_button_none"
        text_style "tmlp_text_main_menu_part_one"
        xalign 0.5
        ypos 685
        action [
            Hide("tmlp_main_menu"),
            ShowMenu("tmlp_preferences")
        ]
            
    textbutton "Выход":
        style "tmlp_button_none"
        text_style "tmlp_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 830
        action [
            Hide("tmlp_main_menu"),
            ShowMenu("tmlp_quit")
        ]

    imagebutton:
        auto tmlp_gui_path + "misc/logowhite_%s.png"
        xpos 1520
        ypos 800
        action OpenURL("https://vk.com/public176281709")