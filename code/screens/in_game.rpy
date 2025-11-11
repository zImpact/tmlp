screen tmlp_preferences:
    tag menu
    modal True

    $ tmlp_timeofday = persistent.timeofday

    add "save_load_preferences"

    text "{font=[intro_light]}Настройки{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.060
        antialias True
        kerning 2
            
    textbutton ["Режим экрана"]:
        style "tmlp_button_none"
        text_style "tmlp_text_setting_"+tmlp_timeofday+""
        xpos 415
        ypos 190
            
    textbutton ["На весь экран"]:
        style "tmlp_button_none"
        text_style "tmlp_text_small_preference_"+tmlp_timeofday+""
        xpos 270
        ypos 270
        action Preference("display", "fullscreen")
            
    textbutton ["В окне"]:
        style "tmlp_button_none"
        text_style "tmlp_text_small_preference_"+tmlp_timeofday+""
        xpos 730
        ypos 270
            
        if not _preferences.fullscreen:
            text_style "tmlp_text_small_invers_preference_"+tmlp_timeofday+""

        else:
            text_style "tmlp_text_small_preference_"+tmlp_timeofday+""

        action Preference("display", "window")

    textbutton ["Размер шрифта"]:
        style "tmlp_button_none"
        text_style "tmlp_text_setting_"+tmlp_timeofday+""
        xpos 380
        ypos 395
            
    textbutton ["Обычный"]:
        style "tmlp_button_none"
        text_style "tmlp_text_small_setting_"+tmlp_timeofday+""
        xpos 270
        ypos 475
        action SetField(persistent, "font_size", "small")
            
    textbutton ["Большой"]:
        style "tmlp_button_none"
        text_style "tmlp_text_small_setting_"+tmlp_timeofday+""
        xpos 700
        ypos 475
        action SetField(persistent, "font_size", "large")

    textbutton ["Музыка"]:
        style "tmlp_button_none"
        text_style "tmlp_text_setting_"+tmlp_timeofday+""
        xpos 1010
        ypos 270
    bar:
        value Preference("music volume")
        right_bar TMLP_GUI_PATH + "preferences/bar_nofull.png"
        left_bar TMLP_GUI_PATH + "preferences/"+tmlp_timeofday+"/bar_full.png"
        thumb tmlp_thumb
        xpos 1260
        ypos 280
        xmaximum 394
        ymaximum 80
            
    textbutton ["Звуки"]:
        style "tmlp_button_none"
        text_style "tmlp_text_setting_"+tmlp_timeofday+""
        xpos 1010
        ypos 370
    bar:
        value Preference("sound volume")
        right_bar TMLP_GUI_PATH + "preferences/bar_nofull.png"
        left_bar TMLP_GUI_PATH + "preferences/"+tmlp_timeofday+"/bar_full.png"
        thumb tmlp_thumb
        xpos 1260
        ypos 380
        xmaximum 394
        ymaximum 80

    textbutton ["Эмбиент"]:
        style "tmlp_button_none"
        text_style "tmlp_text_setting_"+tmlp_timeofday+""
        xpos 1010
        ypos 470
    bar:
        value Preference("voice volume")
        right_bar TMLP_GUI_PATH + "preferences/bar_nofull.png"
        left_bar TMLP_GUI_PATH + "preferences/"+tmlp_timeofday+"/bar_full.png"
        thumb tmlp_thumb
        xpos 1260
        ypos 480
        xmaximum 394
        ymaximum 80
            
    textbutton ["Пропускать"]:
        style "tmlp_button_none"
        text_style "tmlp_text_setting_"+tmlp_timeofday+""
        xpos 605
        ypos 522

    if not _preferences.skip_unseen:
        textbutton ["Виденное ранее"]:
            style "tmlp_button_none"
            text_style "tmlp_text_setting_"+tmlp_timeofday+""
            xpos 494
            ypos 604
            action Preference("skip", "seen")

        textbutton ["Весь текст"]:
            style "tmlp_button_none"
            text_style "tmlp_text_setting_"+tmlp_timeofday+""
            xpos 763
            ypos 604
            action Preference("skip", "all")
                    
    if _preferences.skip_unseen:
        textbutton ["Виденное ранее"]:
            style "tmlp_button_none"
            text_style "tmlp_text_setting_"+tmlp_timeofday+""
            xpos 494
            ypos 604
            action Preference("skip", "seen")

        textbutton ["Весь текст"]:
            style "tmlp_button_none"
            text_style "tmlp_text_setting_"+tmlp_timeofday+""
            xpos 763
            ypos 604
            action Preference("skip", "all")    

    textbutton ["Автопереход"]:
        style "tmlp_button_none"
        text_style "tmlp_text_setting_"+tmlp_timeofday+""
        xpos 1156
        ypos 622
            
    if _preferences.afm_time != 0:
        textbutton ["Включен"]:
            style "tmlp_button_none"
            text_style "tmlp_text_setting_"+tmlp_timeofday+""
            xpos 1066
            ypos 699
            action Preference("auto-forward after click", "enable")

        textbutton ["Выключен"]:
            style "tmlp_button_none"
            text_style "tmlp_text_setting_"+tmlp_timeofday+""
            xpos 1339
            ypos 699
            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

    elif _preferences.afm_time == 0:
        textbutton ["Включен"]:
            style "tmlp_button_none"
            text_style "tmlp_text_white"
            xpos 1066
            ypos 699
            action Preference("auto-forward after click", "enable")

        textbutton ["Выключен"]:
            style "tmlp_button_none"
            text_style "tmlp_text_setting_"+tmlp_timeofday+""
            xpos 1339
            ypos 699
            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

    textbutton ["Автопереход"]:
        style "tmlp_button_none"
        text_style "tmlp_button_none"
        xpos 1022
        ypos 771

    bar:
        value Preference("auto-forward time")
        right_bar TMLP_GUI_PATH + "preferences/bar_nofull.png"
        left_bar TMLP_GUI_PATH + "preferences/"+tmlp_timeofday+"/bar_full.png"
        thumb tmlp_thumb
        xpos 1210
        ypos 756
        xmaximum 265
        ymaximum 48

    textbutton ["Текст"]:
        style "tmlp_button_none"
        text_style "tmlp_button_none"
        xpos 1022
        ypos 836

    bar:
        value Preference("text speed")
        right_bar TMLP_GUI_PATH + "preferences/bar_nofull.png"
        left_bar TMLP_GUI_PATH + "preferences/"+tmlp_timeofday+"/bar_full.png"
        thumb tmlp_thumb
        xpos 1210
        ypos 821
        xmaximum 265
        ymaximum 48

    textbutton ["Назад"]:
        style "tmlp_button_none"
        text_style "tmlp_text_setting_"+tmlp_timeofday+""
        xalign 0.1
        ypos 960
        action [Hide("tmlp_quit"), Return()]       
            
screen tmlp_save:
    tag menu
    modal True

    $ tmlp_timeofday = persistent.timeofday

    add "save_load_preferences"
                
    text "{font=[intro_light]}Сохранить{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.007
        antialias True
        kerning 2
            
    textbutton ["Сохранить игру"]:
        style "tmlp_button_none"
        text_style "tmlp_text_big_save_load_"+tmlp_timeofday+""
        ypos 960
        xalign 0.5
        action (tmlp_FunctionCallback(tmlp_on_save_callback, selected_slot), FileSave(selected_slot, confirm = False))

    textbutton ["Удалить"]:
        style "tmlp_button_none"
        text_style "tmlp_text_big_save_load_"+tmlp_timeofday+""
        xalign 0.9
        ypos 965
        action FileDelete(selected_slot, confirm = False)

    textbutton ["Назад"]:
        style "tmlp_button_none"
        text_style "tmlp_text_big_save_load_"+tmlp_timeofday+""
        xalign 0.1
        ypos 960
        action [Hide("tmlp_save"), Return()]

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
                    style "tmlp_save_load_button_"+tmlp_timeofday+""
                    fixed:
                        text ("%s." % i + FileTime(i, format = " %d.%m.%y, %H:%M", empty = " "+translation["Empty_slot"][_preferences.language]) + "\n" +FileSaveName(i)):
                            style "tmlp_save_load_button_"+tmlp_timeofday+""
                            xpos 15
                            ypos 15                           

screen tmlp_load:             
    tag menu
    modal True

    $ tmlp_timeofday = persistent.timeofday

    add "save_load_preferences"
                
    text "{font=[intro_light]}Загрузка{/font}":
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.007
        antialias True
        kerning 2       
            
    textbutton ["Загрузить игру"]:
        style "tmlp_button_none"
        text_style "tmlp_text_big_save_load_"+tmlp_timeofday+""
        xalign 0.5
        ypos 960
        action (tmlp_FunctionCallback(tmlp_on_load_callback,selected_slot), FileLoad(selected_slot, confirm = False))

    textbutton ["Удалить"]:
        style "tmlp_button_none"
        text_style "tmlp_text_big_save_load_"+tmlp_timeofday+""
        xalign 0.9
        ypos 965
        action FileDelete(selected_slot, confirm = False)

    textbutton ["Назад"]:
        style "tmlp_button_none"
        text_style "tmlp_text_big_save_load_"+tmlp_timeofday+""
        xalign 0.1
        ypos 960
        action [Hide("tmlp_load"), Return()]

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
                    style "tmlp_save_load_button_"+tmlp_timeofday+""
                    fixed:
                        text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty = " "+translation["Empty_slot"][_preferences.language]) + "\n" +FileSaveName(i)):
                            style "tmlp_save_load_button_"+tmlp_timeofday+""
                            xpos 15
                            ypos 15
                                
screen tmlp_yesno_prompt:
    modal True

    $ tmlp_timeofday = persistent.timeofday

    add TMLP_GUI_PATH + "yesno_prompt/day/yesno_bg.png"

    text _(message):
        text_align 0.5
        yalign 0.45
        xalign 0.5
        color "#ffffff"
        font intro_light
        size 65
            
    textbutton ["Да"]:
        style "tmlp_button_none"
        text_style "tmlp_text_small_save_load_"+tmlp_timeofday+""
        yalign 0.53
        xalign 0.42
        action yes_action

    textbutton ["Нет"]:
        style "tmlp_button_none"
        text_style "tmlp_text_small_save_load_"+tmlp_timeofday+""
        yalign 0.53
        xalign 0.58
        action no_action           

screen tmlp_text_history:
    tag menu

    $ tmlp_timeofday = persistent.timeofday

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
    
    window background Frame((TMLP_GUI_PATH + "save_load_choice_nvl_th.png"),50,50) left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:
        viewport id "text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:
                if h.who:
                    text h.who:
                        font tmlp_gotham_pro_medium
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        
                        if "color" in h.who_args:
                            color h.who_args["color"]
                
                if persistent.timeofday == "day":
                    textbutton h.what style "log_button" text_style "tmlp_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#2bb136" xpos 100
                    
                elif persistent.timeofday == "night":
                    textbutton h.what style "log_button" text_style "tmlp_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#1ba9d0" xpos 100
                    
                elif persistent.timeofday == "nightmare":
                    textbutton h.what style "log_button" text_style "tmlp_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#ee080e" xpos 100
                    
                elif persistent.timeofday == "old":
                    textbutton h.what style "log_button" text_style "tmlp_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#e0511e" xpos 100
                    
                elif persistent.timeofday == "prologue":
                    textbutton h.what style "log_button" text_style "tmlp_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#466db8" xpos 100
                    
                elif persistent.timeofday == "sunset":
                    textbutton h.what style "log_button" text_style "tmlp_button_none" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#e0511e" xpos 100   
                    
        vbar value YScrollValue("text_history_screen") bottom_bar tmlp_thumb top_bar "images/misc/none.png" thumb tmlp_thumb xoffset 1700
        
screen tmlp_choice:
    modal True

    $ tmlp_timeofday = persistent.timeofday

    python:
        tmlp_choice_colors_hover = {
            "day": "#9dcd55",
            "night": "#3ccfa2",
            "nightmare": "#40E0D0",
            "old": "#98d8da",
            "sunset": "#dcd168",
            "prologue": "#98d8da"
                    }

        tmlp_choice_colors = {
            "day": "#466123",
            "night": "#145644",
            "nightmare": "#F0F8FF",
            "old": "#98d8da",
            "sunset": "#69652f",
            "prologue": "#496463"
                    }

        tmlp_choice_colors_selected = {
            "day": "#2a3b15",
            "night": "#0b3027",
            "nightmare": "#ADFFFF",
            "old": "#98d8da",
            "sunset": "#42401e",
            "prologue": "#2d3d3d"
                    }
                        
    window:
        background Frame((TMLP_GUI_PATH + "choice/"+tmlp_timeofday+"/choice_box.png"),50,50)
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
                            font tmlp_gotham_pro_medium
                            size 37
                            hover_size 37
                            color tmlp_choice_colors[persistent.timeofday]
                            hover_color tmlp_choice_colors_hover[persistent.timeofday]
                            selected_color tmlp_choice_colors_selected[persistent.timeofday]
                            xcenter 0.5
                else:
                    button:
                        background None
                        xalign 0.5
                        action action
                        text caption:
                            font tmlp_gotham_pro_medium
                            size 37
                            hover_size 37
                            color tmlp_choice_colors[persistent.timeofday]
                            hover_color tmlp_choice_colors_hover[persistent.timeofday]
                            selected_color tmlp_choice_colors_selected[persistent.timeofday]
                            xcenter 0.5
                              
screen tmlp_say:
    $ tmlp_timeofday = persistent.timeofday

    window:
        background None
        id "window"
        
        if persistent.font_size == "small":
            add TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/dialogue_box.png":
                xpos -6
                ypos 750
                
            imagebutton:
                hover TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/backward_hover.png"
                idle TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/backward_idle.png"
                xpos 38
                ypos 949
                action ShowMenu("tmlp_text_history")                
                
            if not config.skipping:
                imagebutton:
                    hover TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/forward_hover.png"
                    idle TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/forward_idle.png"
                    xpos 1768
                    ypos 949
                    action Skip()

            else:
                imagebutton:
                    hover TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/fast_forward_hover.png"
                    idle TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/fast_forward_idle.png"
                    xpos 1768
                    ypos 949
                    action Skip()

            text what:
                color (255, 255, 255, 255)
                id "what"
                xpos 194
                ypos 964
                xmaximum 1541
                font tmlp_gotham_pro_medium
                size 28
                line_spacing 2

            if who:
                text who:
                    id "who"
                    xalign 0.5
                    text_align 0.5
                    ypos 900
                    font tmlp_gotham_pro_medium
                    size 28
                    line_spacing 2          
                
        elif persistent.font_size == "large":
            add TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/dialogue_box_large.png":
                xpos -6
                ypos 745
                
            imagebutton:
                hover TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/backward_hover.png"
                idle TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/backward_idle.png"
                xpos 38
                ypos 924
                action ShowMenu("tmlp_text_history")                
                
            if not config.skipping:
                imagebutton:
                    hover TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/forward_hover.png"
                    idle TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/forward_idle.png"
                    xpos 1768
                    ypos 924
                    action Skip()

            else:
                imagebutton:
                    hover TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/fast_forward_hover.png"
                    idle TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/fast_forward_idle.png"
                    xpos 1768
                    ypos 924
                    action Skip()
                    
            text what:                
                color (255, 255, 255, 255)
                id "what"
                xpos 194
                ypos 915
                xmaximum 1541
                font tmlp_gotham_pro_medium
                size 35
                line_spacing 1
                
            if who:
                add "tmlp/images/gui/plajka.png" xalign 0.5 ypos 860
                
                text who:
                    id "who"
                    xalign 0.5
                    text_align 0.5
                    ypos 870
                    font tmlp_gotham_pro_medium
                    size 35
                    line_spacing 1

    if tmlp_diary_active == True:
        imagebutton:
            idle TMLP_GUI_PATH + "norm.png"
            hover TMLP_GUI_PATH + "norm.png"
            xpos 350
            ypos 830
            action ShowMenu("tmlp_diary")

    else:
        pass

screen tmlp_nvl:
    $ tmlp_timeofday = persistent.timeofday

    window:
        background Frame((TMLP_GUI_PATH + "choice/"+tmlp_timeofday+"/choice_box.png"),50,50)
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
                                    font tmlp_gotham_pro_medium
                                    size 35
                                    line_spacing 1

                            text what:
                                id what_id
                                color (255, 255, 255, 255) 
                                size 35
                                line_spacing 1
                                font tmlp_gotham_pro_medium
                                
                        elif persistent.font_size == "small":
                            if who is not None:
                                text who:
                                    id who_id
                                    font tmlp_gotham_pro_medium
                                    size 28
                                    line_spacing 1

                            text what:
                                id what_id
                                color (255, 255, 255, 255)   
                                size 28
                                line_spacing 1
                                font tmlp_gotham_pro_medium
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
        auto TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/backward_%s.png"
        xpos 38
        ypos 924
        action ShowMenu("tmlp_text_history")
            
    if not config.skipping:
        imagebutton:
            auto TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()
    else:
        imagebutton:
            auto TMLP_GUI_PATH + "dialogue_box/"+tmlp_timeofday+"/fast_forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()
                
screen tmlp_game_menu_selector:
    tag menu
    modal True

    $ tmlp_timeofday = persistent.timeofday

    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()

    if persistent.timeofday == "nightmare":
        add TMLP_GUI_PATH + "quick_menu/quick_menu_ground_nightmare.png"
    
    else:
        add TMLP_GUI_PATH + "quick_menu/quick_menu_ground.png"

    textbutton ["В ГЛАВНОЕ МЕНЮ"]:
        style "tmlp_button_none"
        text_style "tmlp_text_"+tmlp_timeofday+""
        xalign 0.5
        yalign 0.32
        action MainMenu(confirm = False)

    textbutton ["СОХРАНИТЬ"]:
        style "tmlp_button_none"
        text_style "tmlp_text_"+tmlp_timeofday+""
        xalign 0.5
        yalign 0.41
        action ShowMenu("tmlp_save")

    textbutton ["ЗАГРУЗИТЬ"]:
        style "tmlp_button_none"
        text_style "tmlp_text_"+tmlp_timeofday+""
        xalign 0.5
        yalign 0.5
        action ShowMenu("tmlp_load")

    textbutton ["НАСТРОЙКИ"]:
        style "tmlp_button_none"
        text_style "tmlp_text_"+tmlp_timeofday+""
        xalign 0.5
        yalign 0.59
        action ShowMenu("tmlp_preferences")

    textbutton ["ВЫХОД"]:
        style "tmlp_button_none"
        text_style "tmlp_text_"+tmlp_timeofday+""
        xalign 0.5
        yalign 0.68
        action ShowMenu("tmlp_quit")
        
screen tmlp_quit:
    tag menu
    modal True

    $ tmlp_timeofday = persistent.timeofday

    if persistent.timeofday == "nightmare":
        add TMLP_GUI_PATH + "quit/quit_nightmare.png"
    
    else:
        add TMLP_GUI_PATH + "quit/quit.png"

    text "Вы действительно хотите выйти?":
        font intro_light
        size 100
        text_align 0.5
        xalign 0.5
        yalign 0.35
        antialias True
        kerning 2
        
    textbutton ["Да"]:
        style "tmlp_button_none"
        text_style "tmlp_text_"+tmlp_timeofday+""
        xalign 0.4
        yalign 0.6
        action [
            Function(tmlp_screens_diact),
            ShowMenu("main_menu")
        ]
        
    textbutton ["Нет"]:
        style "tmlp_button_none"
        text_style "tmlp_text_"+tmlp_timeofday+""
        xalign 0.6
        yalign 0.6
        action [
            Hide("tmlp_quit"),
            Return()
        ]

screen tmlp_help:
    tag menu
    modal True

