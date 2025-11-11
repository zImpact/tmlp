init python: 
    tmlp_gallery = Gallery() 
    tmlp_gallery_page = 0
    tmlp_gallery.transition = fade
    tmlp_gallery.locked_button = TMLP_GUI_PATH + "save_load/main_menu_part_one/save_load_button_idle.png"
    tmlp_gallery.navigation = False

    tmlp_rows = 4
    tmlp_cols = 3
    tmlp_cells  = tmlp_rows * tmlp_cols

    tmlp_part_one_gallery_bg = [
    "tmlp_ext_aidpost_sunset", "tmlp_ext_boathouse_sunset", "tmlp_ext_booth_day",
    "tmlp_ext_booth_night", "tmlp_int_catacombs_living", "tmlp_int_catacombs_living_celling"
    ]

    tmlp_part_one_gallery_cg = [
    "tmlp_protagonist_end_of_day", "tmlp_protagonist_scene", "tmlp_protagonist_mirror_edited"
    ]

    tmlp_part_two_gallery_bg = [
    "tmlp_int_nigtclub", "tmlp_int_semen_room_clean"
    ]

    tmlp_part_two_gallery_cg = [

    ]

    tmlp_part_three_gallery_bg = [

    ]

    tmlp_part_three_gallery_cg = [

    ]

    tmlp_part_one_music_box = {
        "Mega Drive — Narc": tmlp_mega_drive_narc,
        "Reef — Inevitability": tmlp_reef_inevitability,
        "Reef — Last Night": tmlp_reef_last_night,
        "Yoko Kanno — Total Eclipse (DTB OST)": tmlp_yoko_kanno_total_eclipse,
        }

    tmlp_part_two_music_box = {

        }

    tmlp_part_three_music_box = {

        }

    tmlp_mr = MusicRoom(fadeout = 1.0)

    for name in tmlp_part_one_music_box.values():
        tmlp_mr.add(name)
    
    for bg in tmlp_part_one_gallery_bg:
        tmlp_g.button(bg)
        tmlp_g.image(im.Crop("tmlp/images/bg/part1/" + bg + ".png", (0, 0, 1920, 1080)))
        tmlp_g.unlock(bg)

    for cg in tmlp_part_one_gallery_cg:
        tmlp_g.button(cg)
        tmlp_g.image(im.Crop("tmlp/images/cg/part1/" + cg + ".png", (0, 0, 1920, 1080)))
        tmlp_g.unlock(cg)

    for bg in tmlp_part_two_gallery_bg:
        tmlp_g.button(bg)
        tmlp_g.image(im.Crop("tmlp/images/bg/part2/" + bg + ".png", (0, 0, 1920, 1080)))
        tmlp_g.unlock(bg)

    for cg in tmlp_part_two_gallery_cg:
        tmlp_g.button(cg)
        tmlp_g.image(im.Crop("tmlp/images/cg/part2/" + cg + ".png", (0, 0, 1920, 1080)))
        tmlp_g.unlock(cg)

    for bg in tmlp_part_three_gallery_bg:
        tmlp_g.button(bg)
        tmlp_g.image(im.Crop("tmlp/images/bg/part3/" + bg + ".png", (0, 0, 1920, 1080)))
        tmlp_g.unlock(bg)

    for cg in tmlp_part_three_gallery_cg:
        tmlp_g.button(cg)
        tmlp_g.image(im.Crop("tmlp/images/cg/part3/" + cg + ".png", (0, 0, 1920, 1080)))
        tmlp_g.unlock(cg)
