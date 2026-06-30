init python:
    tmlp_gallery = Gallery()
    tmlp_gallery_page = 0
    tmlp_gallery.transition = fade
    tmlp_gallery.locked_button = TMLP_GUI_PATH + "save_load/main_menu_part_one/save_load_button_idle.png"
    tmlp_gallery.navigation = False

    tmlp_rows = 4
    tmlp_cols = 3
    tmlp_cells  = tmlp_rows * tmlp_cols

    tmlp_gallery_bg_list = [

    ]

    for bg in tmlp_gallery_bg_list:
        tmlp_gallery.button(bg)
        tmlp_gallery.image("bg " + bg)
        tmlp_gallery.unlock("bg " + bg)

screen tmlp_background_gallery():
    tag menu
    modal True

    $ tmlp_gallery_table = []

    if tmlp_gallery_mode == "tmlp_cg":
        $ tmlp_gallery_table = tmlp_part_one_gallery_cg

    else:
        $ tmlp_gallery_table = tmlp_part_one_gallery_bg

    $ tmlp_len_table = len(tmlp_gallery_table)

    frame background "tmlp_part_one_main_menu":
        if tmlp_gallery_mode == "tmlp_cg":
            textbutton "Фоны":
                style "log_button"
                text_style "settings_link"
                xalign 0.98
                yalign 0.02
                action (SetVariable("tmlp_gallery_mode", "tmlp_bg"), SetVariable("tmlp_page", 0), ShowMenu("tmlp_part_one_gallery"))

            hbox xalign 0.5 yalign 0.08:
                text "Иллюстрации":
                    style "settings_link"
                    yalign 0.5
                    color "#ffffff"

        elif tmlp_gallery_mode == "tmlp_bg":
            textbutton "Иллюстрации":
                style "log_button"
                text_style "settings_link"
                xalign 0.02
                yalign 0.02
                action (SetVariable("tmlp_gallery_mode", "tmlp_cg"), SetVariable("tmlp_page", 0), ShowMenu("tmlp_part_one_gallery"))

            hbox xalign 0.5 yalign 0.08:
                text "Фоны":
                    style "settings_link"
                    yalign 0.5
                    color "#ffffff"

        textbutton "НАЗАД":
            style "log_button"
            text_style "settings_link"
            xalign 0.1
            ypos 960
            action [Hide("tmlp_part_one_gallery"), ShowMenu("tmlp_part_one_main_menu")]

        grid tmlp_rows tmlp_cols xpos 0.09 ypos 0.18:
            $ tmlp_cg_displayed = 0
            $ tmlp_next_page = tmlp_page + 1

            if tmlp_next_page > int(tmlp_len_table/tmlp_cells):
                $ tmlp_next_page = 0

            for n in range(0, tmlp_len_table):
                if n < (tmlp_page + 1) * tmlp_cells  and n >= tmlp_page * tmlp_cells :
                    python:
                        if tmlp_gallery_mode == "tmlp_cg":
                            _t = im.Crop("tmlp/images/cg/part1/"+tmlp_gallery_table[n]+".png" , (0, 0, 1920, 1080))

                        elif tmlp_gallery_mode == "tmlp_bg":
                            _t = im.Crop("tmlp/images/bg/part1/"+tmlp_gallery_table[n]+".png" , (0, 0, 1920, 1080))

                        th = im.Scale(_t, 320, 180)

                        tmlp_img = im.Composite((336,196),(8,8),im.Alpha(th, 0.9),(0,0), im.Image("tmlp/images/gui/save_load/main_menu_part_one/save_load_button_idle.png"))
                        tmlp_imgh = im.Composite((336,196),(8,8),th,(0,0),im.Image("tmlp/images/gui/save_load/main_menu_part_one/save_load_button_hover.png"))

                    add tmlp_g.make_button(tmlp_gallery_table[n], get_image("gui/gallery/blank.png"), None, tmlp_imgh , tmlp_img , style = "blank_button", bottom_margin = 50, right_margin = 50)

                    $ tmlp_cg_displayed += 1

                    if n+1 == tmlp_len_table:
                        $ tmlp_next_page = 0

            for j in range(0, tmlp_cells - tmlp_cg_displayed):
                null

        if tmlp_page != 0:
            imagebutton:
                idle "tmlp/images/gui/music_room/previous.png"
                hover "tmlp/images/gui/music_room/previous_part_one.png"
                yalign 0.5
                xalign 0.01
                action (SetVariable("tmlp_page", tmlp_page - 1), ShowMenu("tmlp_part_one_gallery"))

        imagebutton:
            idle "tmlp/images/gui/music_room/next.png"
            hover "tmlp/images/gui/music_room/next_part_one.png"
            yalign 0.5
            xalign 0.99
            action (SetVariable("tmlp_page", tmlp_next_page), ShowMenu("tmlp_part_one_gallery"))

        python:
            def abc(n,k):
                l = float(n)/float(k)
                if l - int(l) > 0:
                    return int(l) + 1

                else:
                    return l

            tmlp_pages = str(tmlp_page + 1) + "/" + str(int(abc(tmlp_len_table, tmlp_cells)))

        text tmlp_pages:
            style "settings_link"
            xalign 0.015
            yalign 0.92
