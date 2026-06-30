init python:
    tmlp_music_box = {
        "Mega Drive — Narc": tmlp_mega_drive_narc,
        "Reef — Inevitability": tmlp_reef_inevitability,
        "Reef — Last Night": tmlp_reef_last_night,
        "Yoko Kanno — Total Eclipse (DTB OST)": tmlp_yoko_kanno_total_eclipse,
    }

    tmlp_music_room = MusicRoom(fadeout=1.0)

    for music_name in tmlp_music_box.values():
        tmlp_music_room.add(name)

screen tmlp_music_room():
    modal True

    frame background "tmlp_part_one_main_menu":
        textbutton "Назад":
            style "log_button"
            text_style "settings_link"
            xalign 0.1
            ypos 960
            action Return()

        hbox xalign 0.5 yalign 0.06:
            text "{font=[gotham_pro_medium]}Музыка{/font}":
                yalign 0.5

        side "c b r":
            area (0.23, 0.15, 0.61, 0.75)

            viewport:
                id "tmlp_part_one_music_box"
                draggable True
                mousewheel True
                scrollbars None

                grid 1 len(tmlp_part_one_music_box):
                    for name, track in sorted(tmlp_part_one_music_box.iteritems()):
                        textbutton name:
                            style "log_button"
                            text_style "music_link"
                            xalign 0.5
                            action tmlp_mr.Play(track)
                            ##text_font "tl/menu/fonts/Morpheus.ttf"

            ##$ vbar_null = Frame("tl/gui/mus_gal/divider.png", 0, 0)
            $ vbar_null = Frame("images/misc/none.png", 0, 0)

            bar:
                value XScrollValue("tmlp_part_one_music_box")
                left_bar "images/misc/none.png"
                right_bar "images/misc/none.png"
                thumb "images/misc/none.png"
                hover_thumb "images/misc/none.png"

            vbar:
                value YScrollValue("tmlp_part_one_music_box")
                bottom_bar vbar_null
                top_bar vbar_null
                ##thumb "tl/gui/mus_gal/polzynok.png"
                thumb "images/misc/none.png"
                #ymaximum 1920
                xmaximum 52
                #thumb_offset 104
                #ypos -0.55

    on "replaced" action Play("music", tmlp_mega_drive_narc)
