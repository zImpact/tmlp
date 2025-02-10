init python: 
    tl_g = Gallery() 
    tl_page = 0
    tl_gallery_mode = "tl_bg"

    tl_g.locked_button = "timeloop/images/gui/save_load/main_menu_part_one/save_load_button_idle.png"
    tl_g.navigation = False

    tl_rows = 4
    tl_cols = 3
    tl_cells  = tl_rows * tl_cols

    tl_part_one_gallery_bg = [
    "tl_ext_aidpost_sunset", "tl_ext_boathouse_sunset", "tl_ext_booth_day",
    "tl_ext_booth_night", "tl_int_catacombs_living", "tl_int_catacombs_living_celling"
    ]

    tl_part_one_gallery_cg = [
    "tl_protagonist_end_of_day", "tl_protagonist_scene", "tl_protagonist_mirror_edited"
    ]

    tl_part_two_gallery_bg = [
    "tl_int_nigtclub", "tl_int_semen_room_clean"
    ]

    tl_part_two_gallery_cg = [

    ]

    tl_part_three_gallery_bg = [

    ]

    tl_part_three_gallery_cg = [

    ]

    tl_part_one_music_box = {
        "Mega Drive — Narc": tl_mega_drive_narc,
        "Reef — Inevitability": tl_reef_inevitability,
        "Reef — Last Night": tl_reef_last_night,
        "Yoko Kanno — Total Eclipse (DTB OST)": tl_yoko_kanno_total_eclipse,
        }

    tl_part_two_music_box = {

        }

    tl_part_three_music_box = {

        }

    tl_mr = MusicRoom(fadeout = 1.0)

    for name in tl_part_one_music_box.values():
        tl_mr.add(name)
    
    for bg in tl_part_one_gallery_bg:
        tl_g.button(bg)
        tl_g.image(im.Crop("timeloop/images/bg/part1/" + bg + ".png", (0, 0, 1920, 1080)))
        tl_g.unlock(bg)

    for cg in tl_part_one_gallery_cg:
        tl_g.button(cg)
        tl_g.image(im.Crop("timeloop/images/cg/part1/" + cg + ".png", (0, 0, 1920, 1080)))
        tl_g.unlock(cg)

    for bg in tl_part_two_gallery_bg:
        tl_g.button(bg)
        tl_g.image(im.Crop("timeloop/images/bg/part2/" + bg + ".png", (0, 0, 1920, 1080)))
        tl_g.unlock(bg)

    for cg in tl_part_two_gallery_cg:
        tl_g.button(cg)
        tl_g.image(im.Crop("timeloop/images/cg/part2/" + cg + ".png", (0, 0, 1920, 1080)))
        tl_g.unlock(cg)

    for bg in tl_part_three_gallery_bg:
        tl_g.button(bg)
        tl_g.image(im.Crop("timeloop/images/bg/part3/" + bg + ".png", (0, 0, 1920, 1080)))
        tl_g.unlock(bg)

    for cg in tl_part_three_gallery_cg:
        tl_g.button(cg)
        tl_g.image(im.Crop("timeloop/images/cg/part3/" + cg + ".png", (0, 0, 1920, 1080)))
        tl_g.unlock(cg)

    tl_g.transition = fade

    def timeloop_show_achievement(img):
        renpy.play(sfx_achievement)
        renpy.show(ach_table[img][_preferences.language], [achievement_trans], layer = "overlay")
        renpy.pause(3.5)
        renpy.hide(ach_table[img][_preferences.language])

    if persistent.tl_part_one_achievements == None:
        persistent.tl_part_one_achievements = {
                "tl1": False,
                }

    if persistent.tl_part_two_achievements == None:
        persistent.tl_part_two_achievements = {
                "tl2": False,
                }

    if persistent.tl_part_three_achievements == None:
        persistent.tl_part_three_achievements = {
                "tl3": False,
                }

    tl_part_one_achievments = {
        "tl1": persistent.tl_part_one_achievements["tl1"]
    }

    tl_part_two_achievments = {
        "tl2": persistent.tl_part_two_achievements["tl2"]
    }

    tl_part_three_achievments = {
        "tl3": persistent.tl_part_three_achievements["tl3"]
    }

screen timeloop_main_menu():
    tag menu
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    #add "timeloop_part_one_main_menu"

    add "tl_part2_main_menu_bg" at tl_bus_moving()

    ##add "timeloop_part_one_main_menu_1of3" xalign 0.5 ypos 115
    add "timeloop_part_one_main_menu_1of3_glitch" xalign 0.5 ypos 115
    #add "timeloop_text" xalign 0.5 ypos 25
    text "{font=[gotham_pro_medium]}Петля времени{/font}":
        size 85
        text_align 0.5
        xalign 0.5
        ypos 25

    textbutton ["Начать игру"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 250
        action [Hide("timeloop_part_one_main_menu"), Start("timeloop_part_one_prologue_day_one")]
            
    textbutton ["Загрузить игру"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 395
        action [Hide("timeloop_part_one_main_menu"), ShowMenu("timeloop_part_one_load_main_menu")]
           
    textbutton ["Дополнительно"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 540
        action [Hide("timeloop_part_one_main_menu"), ShowMenu("timeloop_part_one_extra_main_menu")]

    textbutton ["Настройки"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.5
        ypos 685
        action [Hide("timeloop_part_one_main_menu"), ShowMenu("timeloop_part_one_preferences_main_menu")]
            
    textbutton ["Выход"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 830
        action [Hide("timeloop_part_one_main_menu"), ShowMenu("timeloop_part_one_quit_main_menu")]

    imagebutton:
        auto timeloop_gui_path + "misc/tl_logowhite_%s.png"
        xpos 1520
        ypos 800
        action OpenURL("https://vk.com/public176281709")

screen timeloop_part_one_extra_main_menu:
    tag menu
    modal True    
    
    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "timeloop_part_one_main_menu"
    
    textbutton ["Спрайты"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 295
        action [Hide("timeloop_part_one_main_menu"), ShowMenu("timeloop_load")]
            
    textbutton ["Фоны"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 463
        action [Hide("timeloop_part_one_extra_main_menu"), ShowMenu("timeloop_part_one_gallery")]
            
    textbutton ["Музыка"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.5
        text_align 0.5
        ypos 623
        ##action [Hide("timeloop_part_one_extra_main_menu"), (SetVariable("tl_page", 0), ShowMenu("timeloop_part_one_music_room"))]
        action [Hide("timeloop_part_one_extra_main_menu"), ShowMenu("timeloop_part_one_music_room")]
        
    textbutton ["Назад"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.1
        ypos 960
        action [Hide("timeloop_part_one_extra_main_menu"), ShowMenu("timeloop_part_one_main_menu")]

screen timeloop_part_one_quit_main_menu:
    tag menu
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()
        
    add "timeloop_part_one_main_menu"

    text "{font=[intro_light]}Вы действительно хотите выйти?{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.35
        antialias True
        kerning 2
        
    textbutton ["Да"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.4
        yalign 0.6
        action [(Function(timeloop_screens_diact)), Quit(confirm = False)]
        
    textbutton ["Нет"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.6
        yalign 0.6
        action [Hide("timeloop_part_one_quit_main_menu"), Return()]

screen timeloop_part_one_load_main_menu:
    tag menu
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()
        
    add "timeloop_part_one_main_menu"

    text "{font=[intro_light]}Загрузка{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.007
        antialias True
        kerning 2
            
    textbutton ["Загрузить игру"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.5
        ypos 960
        action (timeloop_FunctionCallback(timeloop_on_load_callback,selected_slot), FileLoad(selected_slot, confirm = False))

    textbutton ["Удалить"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.9
        ypos 965
        action FileDelete(selected_slot, confirm = False)

    textbutton ["Назад"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.1
        ypos 960
        action [Hide("timeloop_load"), Return()]

    grid 4 3:
        xpos 0.11
        ypos 0.2
        xmaximum 0.81
        ymaximum 0.65
        transpose False
        xfill True
        yfill True
        for i in range(1, 13):
            fixed:
                add FileScreenshot(i):
                    xpos 10
                    ypos 10
                button:
                    action SetVariable("selected_slot", i)
                    xfill False
                    yfill False
                    style "timeloop_save_load_button_main_menu_part_one"
                    fixed:
                        text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" "+translation["Empty_slot"][_preferences.language]) + "\n" +FileSaveName(i)):
                            style "timeloop_save_load_button_main_menu_part_one"
                            xpos 15
                            ypos 15

screen timeloop_part_one_preferences_main_menu:
    tag menu
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "timeloop_part_one_main_menu"

    text "{font=[intro_light]}Настройки{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.007
        antialias True
        kerning 2  
            
    textbutton ["Режим экрана"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.3
        ypos 190
            
    textbutton ["На весь экран"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xpos 250
        ypos 270
        action Preference("display", "fullscreen")
            
    textbutton ["В окне"]:
        style "timeloop_button_none"
        text_style "timeloop_text_small_preference_main_menu_part_one"
        xpos 770
        ypos 275
            
        if not _preferences.fullscreen:
            text_style "timeloop_text_small_invers_preference_main_menu_part_one"

        else:
            text_style "timeloop_text_small_preference_main_menu_part_one"

        action Preference("display", "window")

    textbutton ["Размер шрифта"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.3
        ypos 395
          
    textbutton ["Обычный"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xpos 300
        ypos 475
        action SetField(persistent, "font_size", "small")
            
    textbutton ["Большой"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xpos 750
        ypos 475
        action SetField(persistent, "font_size", "large")
            
    textbutton ["Пропускать"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.3
        ypos 600

    if not _preferences.skip_unseen:
        textbutton ["Виденное ранее"]:
            style "timeloop_button_none"
            text_style "timeloop_text_main_menu_part_one"
            xpos 160
            ypos 680
            action Preference("skip", "seen")

        textbutton ["Весь текст"]:
            style "timeloop_button_none"
            text_style "timeloop_text_main_menu_part_one"
            xpos 750
            ypos 685
            action Preference("skip", "all")
                    
    if _preferences.skip_unseen:
        textbutton ["Виденное ранее"]:
            style "timeloop_button_none"
            text_style "timeloop_text_main_menu_part_one"
            xpos 160
            ypos 680
            action Preference("skip", "seen")

        textbutton ["Весь текст"]:
            style "timeloop_button_none"
            text_style "timeloop_text_main_menu_part_one"
            xpos 750
            ypos 685
            action Preference("skip", "all")

    textbutton ["Музыка"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xpos 900
        ypos 190
    bar:
        value Preference("music volume")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/main_menu/bar_full.png"
        thumb timeloop_thumb
        xpos 1260
        ypos 280
        xmaximum 394
        ymaximum 80
            
    textbutton ["Звуки"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.7
        ypos 390
    bar:
        value Preference("sound volume")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/main_menu/bar_full.png"
        thumb timeloop_thumb
        xpos 1260
        ypos 380
        xmaximum 394
        ymaximum 80

    textbutton ["Эмбиент"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.7
        ypos 590
    bar:
        value Preference("voice volume")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/main_menu/bar_full.png"
        thumb timeloop_thumb
        xpos 1260
        ypos 480
        xmaximum 394
        ymaximum 80

    textbutton ["Автопереход"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xpos 1156
        ypos 622
            
    if _preferences.afm_time != 0:
        textbutton ["Включен"]:
            style "timeloop_button_none"
            text_style "timeloop_text_main_menu_part_one"
            xpos 1066
            ypos 699
            action Preference("auto-forward after click", "enable")

        textbutton ["Выключен"]:
            style "timeloop_button_none"
            text_style "timeloop_text_main_menu_part_one"
            xpos 1339
            ypos 699
            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

    elif _preferences.afm_time == 0:
        textbutton ["Включен"]:
            style "timeloop_button_none"
            text_style "timeloop_text_white"
            xpos 1066
            ypos 699
            action Preference("auto-forward after click", "enable")

        textbutton ["Выключен"]:
            style "timeloop_button_none"
            text_style "timeloop_text_main_menu_part_one"
            xpos 1339
            ypos 699
            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

    textbutton ["Автопереход"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xpos 1022
        ypos 771
    bar:
        value Preference("auto-forward time")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/main_menu/bar_full.png"
        thumb timeloop_thumb
        xpos 1210
        ypos 756
        xmaximum 265
        ymaximum 48

    textbutton ["Текст"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xpos 1022
        ypos 836
    bar:
        value Preference("text speed")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/main_menu/bar_full.png"
        thumb timeloop_thumb
        xpos 1210
        ypos 821
        xmaximum 265
        ymaximum 48

    textbutton ["Назад"]:
        style "timeloop_button_none"
        text_style "timeloop_text_main_menu_part_one"
        xalign 0.1
        ypos 960
        action [Hide("timeloop_part_one_preferences_main_menu"), Return()]
            
screen timeloop_preferences:
    tag menu
    modal True

    $ timeloop_timeofday = persistent.timeofday

    add "save_load_preferences"

    text "{font=[intro_light]}Настройки{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.060
        antialias True
        kerning 2
            
    textbutton ["Режим экрана"]:
        style "timeloop_button_none"
        text_style "timeloop_text_setting_"+timeloop_timeofday+""
        xpos 415
        ypos 190
            
    textbutton ["На весь экран"]:
        style "timeloop_button_none"
        text_style "timeloop_text_small_preference_"+timeloop_timeofday+""
        xpos 270
        ypos 270
        action Preference("display", "fullscreen")
            
    textbutton ["В окне"]:
        style "timeloop_button_none"
        text_style "timeloop_text_small_preference_"+timeloop_timeofday+""
        xpos 730
        ypos 270
            
        if not _preferences.fullscreen:
            text_style "timeloop_text_small_invers_preference_"+timeloop_timeofday+""

        else:
            text_style "timeloop_text_small_preference_"+timeloop_timeofday+""

        action Preference("display", "window")

    textbutton ["Размер шрифта"]:
        style "timeloop_button_none"
        text_style "timeloop_text_setting_"+timeloop_timeofday+""
        xpos 380
        ypos 395
            
    textbutton ["Обычный"]:
        style "timeloop_button_none"
        text_style "timeloop_text_small_setting_"+timeloop_timeofday+""
        xpos 270
        ypos 475
        action SetField(persistent, "font_size", "small")
            
    textbutton ["Большой"]:
        style "timeloop_button_none"
        text_style "timeloop_text_small_setting_"+timeloop_timeofday+""
        xpos 700
        ypos 475
        action SetField(persistent, "font_size", "large")

    textbutton ["Музыка"]:
        style "timeloop_button_none"
        text_style "timeloop_text_setting_"+timeloop_timeofday+""
        xpos 1010
        ypos 270
    bar:
        value Preference("music volume")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/"+timeloop_timeofday+"/bar_full.png"
        thumb timeloop_thumb
        xpos 1260
        ypos 280
        xmaximum 394
        ymaximum 80
            
    textbutton ["Звуки"]:
        style "timeloop_button_none"
        text_style "timeloop_text_setting_"+timeloop_timeofday+""
        xpos 1010
        ypos 370
    bar:
        value Preference("sound volume")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/"+timeloop_timeofday+"/bar_full.png"
        thumb timeloop_thumb
        xpos 1260
        ypos 380
        xmaximum 394
        ymaximum 80

    textbutton ["Эмбиент"]:
        style "timeloop_button_none"
        text_style "timeloop_text_setting_"+timeloop_timeofday+""
        xpos 1010
        ypos 470
    bar:
        value Preference("voice volume")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/"+timeloop_timeofday+"/bar_full.png"
        thumb timeloop_thumb
        xpos 1260
        ypos 480
        xmaximum 394
        ymaximum 80
            
    textbutton ["Пропускать"]:
        style "timeloop_button_none"
        text_style "timeloop_text_setting_"+timeloop_timeofday+""
        xpos 605
        ypos 522

    if not _preferences.skip_unseen:
        textbutton ["Виденное ранее"]:
            style "timeloop_button_none"
            text_style "timeloop_text_setting_"+timeloop_timeofday+""
            xpos 494
            ypos 604
            action Preference("skip", "seen")

        textbutton ["Весь текст"]:
            style "timeloop_button_none"
            text_style "timeloop_text_setting_"+timeloop_timeofday+""
            xpos 763
            ypos 604
            action Preference("skip", "all")
                    
    if _preferences.skip_unseen:
        textbutton ["Виденное ранее"]:
            style "timeloop_button_none"
            text_style "timeloop_text_setting_"+timeloop_timeofday+""
            xpos 494
            ypos 604
            action Preference("skip", "seen")

        textbutton ["Весь текст"]:
            style "timeloop_button_none"
            text_style "timeloop_text_setting_"+timeloop_timeofday+""
            xpos 763
            ypos 604
            action Preference("skip", "all")    

    textbutton ["Автопереход"]:
        style "timeloop_button_none"
        text_style "timeloop_text_setting_"+timeloop_timeofday+""
        xpos 1156
        ypos 622
            
    if _preferences.afm_time != 0:
        textbutton ["Включен"]:
            style "timeloop_button_none"
            text_style "timeloop_text_setting_"+timeloop_timeofday+""
            xpos 1066
            ypos 699
            action Preference("auto-forward after click", "enable")

        textbutton ["Выключен"]:
            style "timeloop_button_none"
            text_style "timeloop_text_setting_"+timeloop_timeofday+""
            xpos 1339
            ypos 699
            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

    elif _preferences.afm_time == 0:
        textbutton ["Включен"]:
            style "timeloop_button_none"
            text_style "timeloop_text_white"
            xpos 1066
            ypos 699
            action Preference("auto-forward after click", "enable")

        textbutton ["Выключен"]:
            style "timeloop_button_none"
            text_style "timeloop_text_setting_"+timeloop_timeofday+""
            xpos 1339
            ypos 699
            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

    textbutton ["Автопереход"]:
        style "timeloop_button_none"
        text_style "timeloop_button_none"
        xpos 1022
        ypos 771

    bar:
        value Preference("auto-forward time")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/"+timeloop_timeofday+"/bar_full.png"
        thumb timeloop_thumb
        xpos 1210
        ypos 756
        xmaximum 265
        ymaximum 48

    textbutton ["Текст"]:
        style "timeloop_button_none"
        text_style "timeloop_button_none"
        xpos 1022
        ypos 836

    bar:
        value Preference("text speed")
        right_bar timeloop_gui_path + "preferences/bar_nofull.png"
        left_bar timeloop_gui_path + "preferences/"+timeloop_timeofday+"/bar_full.png"
        thumb timeloop_thumb
        xpos 1210
        ypos 821
        xmaximum 265
        ymaximum 48

    textbutton ["Назад"]:
        style "timeloop_button_none"
        text_style "timeloop_text_setting_"+timeloop_timeofday+""
        xalign 0.1
        ypos 960
        action [Hide("timeloop_quit"), Return()]       
            
screen timeloop_save:
    tag menu
    modal True

    $ timeloop_timeofday = persistent.timeofday

    add "save_load_preferences"
                
    text "{font=[intro_light]}Сохранить{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.007
        antialias True
        kerning 2
            
    textbutton ["Сохранить игру"]:
        style "timeloop_button_none"
        text_style "timeloop_text_big_save_load_"+timeloop_timeofday+""
        ypos 960
        xalign 0.5
        action (timeloop_FunctionCallback(timeloop_on_save_callback, selected_slot), FileSave(selected_slot, confirm = False))

    textbutton ["Удалить"]:
        style "timeloop_button_none"
        text_style "timeloop_text_big_save_load_"+timeloop_timeofday+""
        xalign 0.9
        ypos 965
        action FileDelete(selected_slot, confirm = False)

    textbutton ["Назад"]:
        style "timeloop_button_none"
        text_style "timeloop_text_big_save_load_"+timeloop_timeofday+""
        xalign 0.1
        ypos 960
        action [Hide("timeloop_save"), Return()]

    grid 4 3:
        xpos 0.11
        ypos 0.2
        xmaximum 0.81
        ymaximum 0.65
        transpose False
        xfill True
        yfill True
        for i in range(1, 13):
            fixed:
                add FileScreenshot(i):
                    xpos 10
                    ypos 10
                button:
                    action SetVariable("selected_slot", i)
                    xfill False
                    yfill False
                    style "timeloop_save_load_button_"+timeloop_timeofday+""
                    fixed:
                        text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " "+translation["Empty_slot"][_preferences.language]) + "\n" +FileSaveName(i)):
                            style "timeloop_save_load_button_"+timeloop_timeofday+""
                            xpos 15
                            ypos 15                           

screen timeloop_load:             
    tag menu
    modal True

    $ timeloop_timeofday = persistent.timeofday

    add "save_load_preferences"
                
    text "{font=[intro_light]}Загрузка{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.007
        antialias True
        kerning 2       
            
    textbutton ["Загрузить игру"]:
        style "timeloop_button_none"
        text_style "timeloop_text_big_save_load_"+timeloop_timeofday+""
        xalign 0.5
        ypos 960
        action (timeloop_FunctionCallback(timeloop_on_load_callback,selected_slot), FileLoad(selected_slot, confirm = False))

    textbutton ["Удалить"]:
        style "timeloop_button_none"
        text_style "timeloop_text_big_save_load_"+timeloop_timeofday+""
        xalign 0.9
        ypos 965
        action FileDelete(selected_slot, confirm = False)

    textbutton ["Назад"]:
        style "timeloop_button_none"
        text_style "timeloop_text_big_save_load_"+timeloop_timeofday+""
        xalign 0.1
        ypos 960
        action [Hide("timeloop_load"), Return()]

    grid 4 3:
        xpos 0.11
        ypos 0.2
        xmaximum 0.81
        ymaximum 0.65
        transpose False
        xfill True
        yfill True
        for i in range(1, 13):
            fixed:
                add FileScreenshot(i):
                    xpos 10
                    ypos 10
                button:
                    action SetVariable("selected_slot", i)
                    xfill False
                    yfill False
                    style "timeloop_save_load_button_"+timeloop_timeofday+""
                    fixed:
                        text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty = " "+translation["Empty_slot"][_preferences.language]) + "\n" +FileSaveName(i)):
                            style "timeloop_save_load_button_"+timeloop_timeofday+""
                            xpos 15
                            ypos 15
                                
screen timeloop_yesno_prompt:
    modal True

    $ timeloop_timeofday = persistent.timeofday

    add timeloop_gui_path + "yesno_prompt/day/yesno_bg.png"

    text _(message):
        text_align 0.5
        yalign 0.45
        xalign 0.5
        color "#ffffff"
        font intro_light
        size 65
            
    textbutton ["Да"]:
        style "timeloop_button_none"
        text_style "timeloop_text_small_save_load_"+timeloop_timeofday+""
        yalign 0.53
        xalign 0.42
        action yes_action

    textbutton ["Нет"]:
        style "timeloop_button_none"
        text_style "timeloop_text_small_save_load_"+timeloop_timeofday+""
        yalign 0.53
        xalign 0.58
        action no_action           

screen timeloop_text_history:
    tag menu

    $ timeloop_timeofday = persistent.timeofday

    predict False

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    if persistent.font_size == "small": 
        $ history_text_size = 28
        $ history_name_size = 29

    elif persistent.font_size == "large":
        $ history_text_size = 36
        $ history_name_size = 37

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()
    
    window background Frame((timeloop_gui_path + "save_load_choice_nvl_th.png"),50,50) left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:
        viewport id "text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:
                if h.who:
                    text h.who:
                        font gotham_pro_medium
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        
                        if "color" in h.who_args:
                            color h.who_args["color"]
                
                if persistent.timeofday == "day":
                    textbutton h.what style "log_button" text_style "timeloop_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#2bb136" xpos 100
                    
                elif persistent.timeofday == "night":
                    textbutton h.what style "log_button" text_style "timeloop_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#1ba9d0" xpos 100
                    
                elif persistent.timeofday == "nightmare":
                    textbutton h.what style "log_button" text_style "timeloop_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#ee080e" xpos 100
                    
                elif persistent.timeofday == "old":
                    textbutton h.what style "log_button" text_style "timeloop_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#e0511e" xpos 100
                    
                elif persistent.timeofday == "prologue":
                    textbutton h.what style "log_button" text_style "timeloop_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#466db8" xpos 100
                    
                elif persistent.timeofday == "sunset":
                    textbutton h.what style "log_button" text_style "timeloop_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#e0511e" xpos 100   
                    
        vbar value YScrollValue("text_history_screen") bottom_bar timeloop_thumb top_bar "images/misc/none.png" thumb timeloop_thumb xoffset 1700
        
screen timeloop_choice:
    modal True

    $ timeloop_timeofday = persistent.timeofday

    python:
        timeloop_choice_colors_hover = {
            "day": "#9dcd55",
            "night": "#3ccfa2",
            "nightmare": "#40E0D0",
            "old": "#98d8da",
            "sunset": "#dcd168",
            "prologue": "#98d8da"
                    }

        timeloop_choice_colors = {
            "day": "#466123",
            "night": "#145644",
            "nightmare": "#F0F8FF",
            "old": "#98d8da",
            "sunset": "#69652f",
            "prologue": "#496463"
                    }

        timeloop_choice_colors_selected = {
            "day": "#2a3b15",
            "night": "#0b3027",
            "nightmare": "#ADFFFF",
            "old": "#98d8da",
            "sunset": "#42401e",
            "prologue": "#2d3d3d"
                    }
                        
    window:
        background Frame((timeloop_gui_path + "choice/"+timeloop_timeofday+"/choice_box.png"),50,50)
        xfill True
        yalign 0.5
        left_padding 50
        right_padding 50
        bottom_padding 60
        top_padding 60
        vbox:
            xalign 0.5
            for caption, action, chosen  in items:
                if action and caption:
                    button:
                        background None
                        xalign 0.5
                        action action
                        text caption:
                            font gotham_pro_medium
                            size 37
                            hover_size 37
                            color timeloop_choice_colors[persistent.timeofday]
                            hover_color timeloop_choice_colors_hover[persistent.timeofday]
                            selected_color timeloop_choice_colors_selected[persistent.timeofday]
                            xcenter 0.5
                else:
                    button:
                        background None
                        xalign 0.5
                        action action
                        text caption:
                            font gotham_pro_medium
                            size 37
                            hover_size 37
                            color timeloop_choice_colors[persistent.timeofday]
                            hover_color timeloop_choice_colors_hover[persistent.timeofday]
                            selected_color timeloop_choice_colors_selected[persistent.timeofday]
                            xcenter 0.5
                              
screen timeloop_say:
    $ timeloop_timeofday = persistent.timeofday

    window:
        background None
        id "window"
        
        if persistent.font_size == "small":
            add timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/dialogue_box.png":
                xpos -6
                ypos 750
                
            imagebutton:
                hover timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/backward_hover.png"
                idle timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/backward_idle.png"
                xpos 38
                ypos 949
                action ShowMenu("timeloop_text_history")                
                
            if not config.skipping:
                imagebutton:
                    hover timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/forward_hover.png"
                    idle timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/forward_idle.png"
                    xpos 1768
                    ypos 949
                    action Skip()

            else:
                imagebutton:
                    hover timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/fast_forward_hover.png"
                    idle timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/fast_forward_idle.png"
                    xpos 1768
                    ypos 949
                    action Skip()

            text what:
                color (255, 255, 255, 255)
                id "what"
                xpos 194
                ypos 964
                xmaximum 1541
                font gotham_pro_medium
                size 28
                line_spacing 2

            if who:
                text who:
                    id "who"
                    xalign 0.5
                    text_align 0.5
                    ypos 900
                    font gotham_pro_medium
                    size 28
                    line_spacing 2          
                
        elif persistent.font_size == "large":
            add timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/dialogue_box_large.png":
                xpos -6
                ypos 745
                
            imagebutton:
                hover timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/backward_hover.png"
                idle timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/backward_idle.png"
                xpos 38
                ypos 924
                action ShowMenu("timeloop_text_history")                
                
            if not config.skipping:
                imagebutton:
                    hover timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/forward_hover.png"
                    idle timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/forward_idle.png"
                    xpos 1768
                    ypos 924
                    action Skip()

            else:
                imagebutton:
                    hover timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/fast_forward_hover.png"
                    idle timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/fast_forward_idle.png"
                    xpos 1768
                    ypos 924
                    action Skip()
                    
            text what:                
                color (255, 255, 255, 255)
                id "what"
                xpos 194
                ypos 915
                xmaximum 1541
                font gotham_pro_medium
                size 35
                line_spacing 1
                
            if who:
                add "timeloop/images/gui/plajka.png" xalign 0.5 ypos 860
                
                text who:
                    id "who"
                    xalign 0.5
                    text_align 0.5
                    ypos 870
                    font gotham_pro_medium
                    size 35
                    line_spacing 1

    if timeloop_diary_active == True:
        imagebutton:
            idle timeloop_gui_path + "norm.png"
            hover timeloop_gui_path + "norm.png"
            xpos 350
            ypos 830
            action ShowMenu("timeloop_diary")

    else:
        pass

screen timeloop_nvl:
    $ timeloop_timeofday = persistent.timeofday

    window:
        background Frame((timeloop_gui_path + "choice/"+timeloop_timeofday+"/choice_box.png"),50,50)
        xfill True
        yfill True
        yalign 0.5
        left_padding 175
        right_padding 175
        bottom_padding 150
        top_padding 150
        vbox:
            for who, what, who_id, what_id, window_id in dialogue:
                window:
                    id window_id
                    hbox:
                        spacing 10
                        if persistent.font_size == "large":
                            if who is not None:
                                text who:
                                    id who_id
                                    font gotham_pro_medium
                                    size 35
                                    line_spacing 1

                            text what:
                                id what_id
                                color (255, 255, 255, 255) 
                                size 35
                                line_spacing 1
                                font gotham_pro_medium
                                
                        elif persistent.font_size == "small":
                            if who is not None:
                                text who:
                                    id who_id
                                    font gotham_pro_medium
                                    size 28
                                    line_spacing 1

                            text what:
                                id what_id
                                color (255, 255, 255, 255)   
                                size 28
                                line_spacing 1
                                font gotham_pro_medium
            if items:
                vbox:
                    id "menu"
                    for caption, action, chosen  in items:
                        if action:
                            button:
                                style "nvl_menu_choice_button"
                                action action
                                text caption:
                                    style "nvl_menu_choice"
                        else:
                            text caption:
                                style "nvl_dialogue"
                                
    imagebutton:
        auto timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/backward_%s.png"
        xpos 38
        ypos 924
        action ShowMenu("timeloop_text_history")
            
    if not config.skipping:
        imagebutton:
            auto timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()
    else:
        imagebutton:
            auto timeloop_gui_path + "dialogue_box/"+timeloop_timeofday+"/fast_forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()
                
screen timeloop_game_menu_selector:
    tag menu
    modal True

    $ timeloop_timeofday = persistent.timeofday

    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()

    if persistent.timeofday == "nightmare":
        add timeloop_gui_path + "quick_menu/quick_menu_ground_nightmare.png"
    
    else:
        add timeloop_gui_path + "quick_menu/quick_menu_ground.png"

    textbutton ["В ГЛАВНОЕ МЕНЮ"]:
        style "timeloop_button_none"
        text_style "timeloop_text_"+timeloop_timeofday+""
        xalign 0.5
        yalign 0.32
        action MainMenu(confirm = False)

    textbutton ["СОХРАНИТЬ"]:
        style "timeloop_button_none"
        text_style "timeloop_text_"+timeloop_timeofday+""
        xalign 0.5
        yalign 0.41
        action ShowMenu("timeloop_save")

    textbutton ["ЗАГРУЗИТЬ"]:
        style "timeloop_button_none"
        text_style "timeloop_text_"+timeloop_timeofday+""
        xalign 0.5
        yalign 0.5
        action ShowMenu("timeloop_load")

    textbutton ["НАСТРОЙКИ"]:
        style "timeloop_button_none"
        text_style "timeloop_text_"+timeloop_timeofday+""
        xalign 0.5
        yalign 0.59
        action ShowMenu("timeloop_preferences")

    textbutton ["ВЫХОД"]:
        style "timeloop_button_none"
        text_style "timeloop_text_"+timeloop_timeofday+""
        xalign 0.5
        yalign 0.68
        action ShowMenu("timeloop_quit")
        
screen timeloop_quit:
    tag menu
    modal True

    $ timeloop_timeofday = persistent.timeofday

    if persistent.timeofday == "nightmare":
        add timeloop_gui_path + "quit/quit_nightmare.png"
    
    else:
        add timeloop_gui_path + "quit/quit.png"

    text "{font=[intro_light]}Вы действительно хотите выйти?{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.35
        antialias True
        kerning 2
        
    textbutton ["Да"]:
        style "timeloop_button_none"
        text_style "timeloop_text_"+timeloop_timeofday+""
        xalign 0.4
        yalign 0.6
        action [(Function(timeloop_screens_diact)), Quit(confirm = False)]
        
    textbutton ["Нет"]:
        style "timeloop_button_none"
        text_style "timeloop_text_"+timeloop_timeofday+""
        xalign 0.6
        yalign 0.6
        action [Hide("timeloop_quit"), Return()]

screen timeloop_help:
    tag menu
    modal True

screen minigame(ai_mode):
    default chess = timeloop_chess(chess_ai=ai_mode)
    add "chessboard"
    add chess
    
    if chess.winner:
        timer 6.0 action Return(chess.winner)

screen timeloop_part_one_gallery:
    tag menu
    modal True

    $ tl_gallery_table = []

    if tl_gallery_mode == "tl_cg":
        $ tl_gallery_table = tl_part_one_gallery_cg

    else:
        $ tl_gallery_table = tl_part_one_gallery_bg

    $ tl_len_table = len(tl_gallery_table)

    frame background "timeloop_part_one_main_menu":

        if tl_gallery_mode == "tl_cg":
            textbutton "Фоны": 
                style "log_button" 
                text_style "settings_link"
                xalign 0.98 
                yalign 0.02 
                action (SetVariable("tl_gallery_mode", "tl_bg"), SetVariable("tl_page", 0), ShowMenu("timeloop_part_one_gallery"))

            hbox xalign 0.5 yalign 0.08:
                text "Иллюстрации": 
                    style "settings_link" 
                    yalign 0.5 
                    color "#ffffff"

        elif tl_gallery_mode == "tl_bg":
            textbutton "Иллюстрации": 
                style "log_button" 
                text_style "settings_link" 
                xalign 0.02 
                yalign 0.02 
                action (SetVariable("tl_gallery_mode", "tl_cg"), SetVariable("tl_page", 0), ShowMenu("timeloop_part_one_gallery"))

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
            action [Hide("timeloop_part_one_gallery"), ShowMenu("timeloop_part_one_main_menu")]

        grid tl_rows tl_cols xpos 0.09 ypos 0.18:
            $ tl_cg_displayed = 0
            $ tl_next_page = tl_page + 1

            if tl_next_page > int(tl_len_table/tl_cells):
                $ tl_next_page = 0

            for n in range(0, tl_len_table):
                if n < (tl_page + 1) * tl_cells  and n >= tl_page * tl_cells :
                    python:
                        if tl_gallery_mode == "tl_cg":
                            _t = im.Crop("timeloop/images/cg/part1/"+tl_gallery_table[n]+".png" , (0, 0, 1920, 1080))

                        elif tl_gallery_mode == "tl_bg":
                            _t = im.Crop("timeloop/images/bg/part1/"+tl_gallery_table[n]+".png" , (0, 0, 1920, 1080))
                            
                        th = im.Scale(_t, 320, 180)

                        tl_img = im.Composite((336,196),(8,8),im.Alpha(th, 0.9),(0,0), im.Image("timeloop/images/gui/save_load/main_menu_part_one/save_load_button_idle.png"))
                        tl_imgh = im.Composite((336,196),(8,8),th,(0,0),im.Image("timeloop/images/gui/save_load/main_menu_part_one/save_load_button_hover.png"))

                    add tl_g.make_button(tl_gallery_table[n], get_image("gui/gallery/blank.png"), None, tl_imgh , tl_img , style = "blank_button", bottom_margin = 50, right_margin = 50)

                    $ tl_cg_displayed += 1

                    if n+1 == tl_len_table:
                        $ tl_next_page = 0

            for j in range(0, tl_cells - tl_cg_displayed):
                null

        if tl_page != 0:
            imagebutton:
                idle "timeloop/images/gui/music_room/previous.png"
                hover "timeloop/images/gui/music_room/previous_part_one.png"
                yalign 0.5 
                xalign 0.01 
                action (SetVariable("tl_page", tl_page - 1), ShowMenu("timeloop_part_one_gallery"))

        imagebutton: 
            idle "timeloop/images/gui/music_room/next.png"
            hover "timeloop/images/gui/music_room/next_part_one.png"
            yalign 0.5 
            xalign 0.99 
            action (SetVariable("tl_page", tl_next_page), ShowMenu("timeloop_part_one_gallery"))

        python:
            def abc(n,k):
                l = float(n)/float(k)
                if l - int(l) > 0:
                    return int(l) + 1

                else:
                    return l

            tl_pages = str(tl_page + 1) + "/" + str(int(abc(tl_len_table, tl_cells)))

        text tl_pages: 
            style "settings_link" 
            xalign 0.015 
            yalign 0.92

screen timeloop_part_one_music_room:
    tag menu
    modal True

    frame background "timeloop_part_one_main_menu":
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
                id "tl_part_one_music_box"
                draggable True
                mousewheel True
                scrollbars None
                
                grid 1 len(tl_part_one_music_box):
                    for name, track in sorted(tl_part_one_music_box.iteritems()):
                        textbutton name:
                            style "log_button"
                            text_style "music_link"
                            xalign 0.5
                            action tl_mr.Play(track)
                            ##text_font "tl/menu/fonts/Morpheus.ttf"

            ##$ vbar_null = Frame("tl/gui/mus_gal/divider.png", 0, 0)
            $ vbar_null = Frame("images/misc/none.png", 0, 0)

            bar:
                value XScrollValue("tl_part_one_music_box")
                left_bar "images/misc/none.png"
                right_bar "images/misc/none.png"
                thumb "images/misc/none.png"
                hover_thumb "images/misc/none.png"

            vbar:
                value YScrollValue("tl_part_one_music_box")
                bottom_bar vbar_null
                top_bar vbar_null
                ##thumb "tl/gui/mus_gal/polzynok.png"
                thumb "images/misc/none.png"
                #ymaximum 1920
                xmaximum 52
                #thumb_offset 104
                #ypos -0.55

    on "replaced" action Play("music", tl_mega_drive_narc)