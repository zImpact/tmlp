init -10 python:
    tmlp_gui_path = "tmlp/images/gui/"

    tmlp_intro_light = tmlp_gui_path + "fonts/intro_light.ttf"
    tmlp_gotham_pro_medium = tmlp_gui_path + "fonts/gotham_pro_medium.ttf"

    style.tmlp_button_none = Style(style.button)
    style.tmlp_button_none.background = None
    style.tmlp_button_none.hover_background = None
    style.tmlp_button_none.selected_background = None
    style.tmlp_button_none.selected_hover_background = None
    style.tmlp_button_none.selected_idle_background = None

    style.tmlp_text_style = Style(style.default)
    style.tmlp_text_style.drop_shadow = (2, 2)
    style.tmlp_text_style.drop_shadow_color = "#000"

    style.tmlp_style_default = Style(style.default)
    style.tmlp_style_default.font = intro_light
    style.tmlp_style_default.size = 65

    style.tmlp_text_day = Style(style.tmlp_style_default)
    style.tmlp_text_day.color = "#ffffff"
    style.tmlp_text_day.hover_color = "#2bb136"
    style.tmlp_text_day.selected_color = "#ffffff"
    style.tmlp_text_day.selected_idle_color = "#ffffff"
    style.tmlp_text_day.selected_hover_color = "#ffffff"
    style.tmlp_text_day.insensitive_color = "#ffffff"
    
    style.tmlp_history_button_text_day = Style(style.tmlp_style_default)
    style.tmlp_history_button_text_day.selected_color = "#2bb136"
    style.tmlp_history_button_text_day.hover_color = "#2bb136"
    style.tmlp_history_button_text_day.selected_color = "#2bb136"
    style.tmlp_history_button_text_day.hover_color = "#2bb136"
    
    style.tmlp_text_setting_day = Style(style.tmlp_style_default)
    style.tmlp_text_setting_day.color = "#ffffff"
    style.tmlp_text_setting_day.hover_color = "#2bb136"
    style.tmlp_text_setting_day.selected_color = "#2bb136"
    
    style.tmlp_text_small_setting_day = Style(style.tmlp_style_default)
    style.tmlp_text_small_setting_day.color = "#ffffff"
    style.tmlp_text_small_setting_day.hover_color = "#2bb136"
    style.tmlp_text_small_setting_day.selected_color = "#2bb136"
    
    style.tmlp_text_big_setting_day = Style(style.tmlp_style_default)
    style.tmlp_text_big_setting_day.color = "#ffffff"
    style.tmlp_text_big_setting_day.hover_color = "#2bb136"
    style.tmlp_text_big_setting_day.selected_color = "#2bb136"
    
    style.tmlp_text_small_invers_setting_day = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_setting_day.color = "#ffffff"
    style.tmlp_text_small_invers_setting_day.hover_color = "#2bb136"
    style.tmlp_text_small_invers_setting_day.selected_color = "#2bb136"
    
    style.tmlp_text_big_save_load_day = Style(style.tmlp_style_default)
    style.tmlp_text_big_save_load_day.color = "#ffffff"
    style.tmlp_text_big_save_load_day.hover_color = "#2bb136"
    style.tmlp_text_big_save_load_day.selected_color = "#ffffff"
    style.tmlp_text_big_save_load_day.selected_idle_color = "#ffffff"
    style.tmlp_text_big_save_load_day.selected_hover_color = "#2bb136"
    style.tmlp_text_big_save_load_day.insensitive_color = "#ffffff"
    
    style.tmlp_text_small_save_load_day = Style(style.tmlp_style_default)
    style.tmlp_text_small_save_load_day.color = "#ffffff"
    style.tmlp_text_small_save_load_day.hover_color = "#2bb136"
    style.tmlp_text_small_save_load_day.selected_color = "#ffffff"
    style.tmlp_text_small_save_load_day.selected_idle_color = "#ffffff"
    style.tmlp_text_small_save_load_day.selected_hover_color = "#2bb136"
    style.tmlp_text_small_save_load_day.insensitive_color = "#ffffff"

    style.tmlp_save_load_button_day = Style(style.button)
    style.tmlp_save_load_button_day.background = tmlp_gui_path + "save_load/day/save_load_button_idle.png"
    style.tmlp_save_load_button_day.hover_background = tmlp_gui_path + "save_load/day/save_load_button_hover.png"
    style.tmlp_save_load_button_day.selected_background = tmlp_gui_path + "save_load/day/save_load_button_selected.png"
    style.tmlp_save_load_button_day.selected_hover_background = tmlp_gui_path + "save_load/day/save_load_button_selected.png"
    style.tmlp_save_load_button_day.selected_idle_background = tmlp_gui_path + "save_load/day/save_load_button_selected.png"

    style.tmlp_text_small_preference_day = Style(style.tmlp_style_default)
    style.tmlp_text_small_preference_day.color = "#ffffff"
    style.tmlp_text_small_preference_day.hover_color = "#2bb136"
    style.tmlp_text_small_preference_day.selected_color = "#2bb136"
    
    style.tmlp_text_small_invers_preference_day = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_preference_day.color = "#2bb136"
    style.tmlp_text_small_invers_preference_day.hover_color = "#2bb136"
    style.tmlp_text_small_invers_preference_day.selected_color = "#2bb136"

    style.tmlp_text_night = Style(style.tmlp_style_default)
    style.tmlp_text_night.color = "#ffffff"
    style.tmlp_text_night.hover_color = "#1ba9d0"
    style.tmlp_text_night.selected_color = "#ffffff"
    style.tmlp_text_night.selected_idle_color = "#ffffff"
    style.tmlp_text_night.selected_hover_color = "#ffffff"
    style.tmlp_text_night.insensitive_color = "#ffffff"
    
    style.tmlp_history_button_text_night = Style(style.tmlp_style_default)
    style.tmlp_history_button_text_night.selected_color = "#1ba9d0"
    style.tmlp_history_button_text_night.hover_color = "#1ba9d0"
    style.tmlp_history_button_text_night.selected_color = "#1ba9d0"
    style.tmlp_history_button_text_night.hover_color = "#1ba9d0"
    
    style.tmlp_text_setting_night = Style(style.tmlp_style_default)
    style.tmlp_text_setting_night.color = "#ffffff"
    style.tmlp_text_setting_night.hover_color = "#1ba9d0"
    style.tmlp_text_setting_night.selected_color = "#1ba9d0"
    
    style.tmlp_text_small_setting_night = Style(style.tmlp_style_default)
    style.tmlp_text_small_setting_night.color = "#ffffff"
    style.tmlp_text_small_setting_night.hover_color = "#1ba9d0"
    style.tmlp_text_small_setting_night.selected_color = "#1ba9d0"
    
    style.tmlp_text_big_setting_night = Style(style.tmlp_style_default)
    style.tmlp_text_big_setting_night.color = "#ffffff"
    style.tmlp_text_big_setting_night.hover_color = "#1ba9d0"
    style.tmlp_text_big_setting_night.selected_color = "#1ba9d0"
    
    style.tmlp_text_small_invers_setting_night = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_setting_night.color = "#ffffff"
    style.tmlp_text_small_invers_setting_night.hover_color = "#1ba9d0"
    style.tmlp_text_small_invers_setting_night.selected_color = "#1ba9d0"
    
    style.tmlp_text_big_save_load_night = Style(style.tmlp_style_default)
    style.tmlp_text_big_save_load_night.color = "#ffffff"
    style.tmlp_text_big_save_load_night.hover_color = "#1ba9d0"
    style.tmlp_text_big_save_load_night.selected_color = "#ffffff"
    style.tmlp_text_big_save_load_night.selected_idle_color = "#ffffff"
    style.tmlp_text_big_save_load_night.selected_hover_color = "#1ba9d0"
    style.tmlp_text_big_save_load_night.insensitive_color = "#ffffff"
    
    style.tmlp_text_small_save_load_night = Style(style.tmlp_style_default)
    style.tmlp_text_small_save_load_night.color = "#ffffff"
    style.tmlp_text_small_save_load_night.hover_color = "#1ba9d0"
    style.tmlp_text_small_save_load_night.selected_color = "#ffffff"
    style.tmlp_text_small_save_load_night.selected_idle_color = "#ffffff"
    style.tmlp_text_small_save_load_night.selected_hover_color = "#1ba9d0"
    style.tmlp_text_small_save_load_night.insensitive_color = "#ffffff"

    style.tmlp_save_load_button_night = Style(style.button)
    style.tmlp_save_load_button_night.background = tmlp_gui_path + "save_load/night/save_load_button_idle.png"
    style.tmlp_save_load_button_night.hover_background = tmlp_gui_path + "save_load/night/save_load_button_hover.png"
    style.tmlp_save_load_button_night.selected_background = tmlp_gui_path + "save_load/night/save_load_button_selected.png"
    style.tmlp_save_load_button_night.selected_hover_background = tmlp_gui_path + "save_load/night/save_load_button_selected.png"
    style.tmlp_save_load_button_night.selected_idle_background = tmlp_gui_path + "save_load/night/save_load_button_selected.png"

    style.tmlp_text_small_preference_night = Style(style.tmlp_style_default)
    style.tmlp_text_small_preference_night.color = "#ffffff"
    style.tmlp_text_small_preference_night.hover_color = "#1ba9d0"
    style.tmlp_text_small_preference_night.selected_color = "#1ba9d0"
    
    style.tmlp_text_small_invers_preference_night = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_preference_night.color = "#1ba9d0"
    style.tmlp_text_small_invers_preference_night.hover_color = "#1ba9d0"
    style.tmlp_text_small_invers_preference_night.selected_color = "#1ba9d0"

    style.tmlp_text_quit_nightmare = Style(style.tmlp_style_default)
    style.tmlp_text_quit_nightmare.color = "#ffffff"
    style.tmlp_text_quit_nightmare.hover_color = "#ee080e"
    style.tmlp_text_quit_nightmare.selected_color = "#ffffff"
    style.tmlp_text_quit_nightmare.selected_idle_color = "#ffffff"
    style.tmlp_text_quit_nightmare.selected_hover_color = "#ffffff"
    style.tmlp_text_quit_nightmare.insensitive_color = "#ffffff"
    
    style.tmlp_history_button_text_nightmare = Style(style.tmlp_style_default)
    style.tmlp_history_button_text_nightmare.selected_color = "#ee080e"
    style.tmlp_history_button_text_nightmare.hover_color = "#ee080e"
    style.tmlp_history_button_text_nightmare.selected_color = "#ee080e"
    style.tmlp_history_button_text_nightmare.hover_color = "#ee080e"
    
    style.tmlp_text_setting_nightmare = Style(style.tmlp_style_default)
    style.tmlp_text_setting_nightmare.color = "#ffffff"
    style.tmlp_text_setting_nightmare.hover_color = "#ee080e"
    style.tmlp_text_setting_nightmare.selected_color = "#ee080e"
    
    style.tmlp_text_small_setting_nightmare = Style(style.tmlp_style_default)
    style.tmlp_text_small_setting_nightmare.color = "#ffffff"
    style.tmlp_text_small_setting_nightmare.hover_color = "#ee080e"
    style.tmlp_text_small_setting_nightmare.selected_color  = "#ee080e"
    
    style.tmlp_text_big_setting_nightmare = Style(style.tmlp_style_default)
    style.tmlp_text_big_setting_nightmare.color = "#ffffff"
    style.tmlp_text_big_setting_nightmare.hover_color = "#ee080e"
    style.tmlp_text_big_setting_nightmare.selected_color = "#ee080e"
    
    style.tmlp_text_small_invers_setting_nightmare = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_setting_nightmare.color = "#ffffff"
    style.tmlp_text_small_invers_setting_nightmare.hover_color = "#ee080e"
    style.tmlp_text_small_invers_setting_nightmare.selected_color = "#ee080e"
    
    style.tmlp_text_big_save_load_nightmare = Style(style.tmlp_style_default)
    style.tmlp_text_big_save_load_nightmare.color = "#ffffff"
    style.tmlp_text_big_save_load_nightmare.hover_color = "#ee080e"
    style.tmlp_text_big_save_load_nightmare.selected_color = "#ffffff"
    style.tmlp_text_big_save_load_nightmare.selected_idle_color = "#ffffff"
    style.tmlp_text_big_save_load_nightmare.selected_hover_color = "#ee080e"
    style.tmlp_text_big_save_load_nightmare.insensitive_color = "#ffffff"
    
    style.tmlp_text_small_save_load_nightmare = Style(style.tmlp_style_default)
    style.tmlp_text_small_save_load_nightmare.color = "#ffffff"
    style.tmlp_text_small_save_load_nightmare.hover_color = "#ee080e"
    style.tmlp_text_small_save_load_nightmare.selected_color = "#ffffff"
    style.tmlp_text_small_save_load_nightmare.selected_idle_color = "#ffffff"
    style.tmlp_text_small_save_load_nightmare.selected_hover_color = "#ee080e"
    style.tmlp_text_small_save_load_nightmare.insensitive_color = "#ffffff"

    style.tmlp_save_load_button_nightmare = Style(style.button)
    style.tmlp_save_load_button_nightmare.background = tmlp_gui_path + "save_load/nightmare/save_load_button_idle.png"
    style.tmlp_save_load_button_nightmare.hover_background = tmlp_gui_path + "save_load/nightmare/save_load_button_hover.png"
    style.tmlp_save_load_button_nightmare.selected_background = tmlp_gui_path + "save_load/nightmare/save_load_button_selected.png"
    style.tmlp_save_load_button_nightmare.selected_hover_background = tmlp_gui_path + "save_load/nightmare/save_load_button_selected.png"
    style.tmlp_save_load_button_nightmare.selected_idle_background = tmlp_gui_path + "save_load/nightmare/save_load_button_selected.png"

    style.tmlp_text_small_preference_nightmare = Style(style.tmlp_style_default)
    style.tmlp_text_small_preference_nightmare.color = "#ffffff"
    style.tmlp_text_small_preference_nightmare.hover_color = "#ee080e"
    style.tmlp_text_small_preference_nightmare.selected_color = "#ee080e"
    
    style.tmlp_text_small_invers_preference_nightmare = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_preference_nightmare.color = "#ee080e"
    style.tmlp_text_small_invers_preference_nightmare.hover_color = "#ee080e"
    style.tmlp_text_small_invers_preference_nightmare.selected_color = "#ee080e"

    style.tmlp_text_old = Style(style.tmlp_style_default)
    style.tmlp_text_old.color = "#ffffff"
    style.tmlp_text_old.hover_color = "#e0511e"
    style.tmlp_text_old.selected_color = "#ffffff"
    style.tmlp_text_old.selected_idle_color = "#ffffff"
    style.tmlp_text_old.selected_hover_color = "#ffffff"
    style.tmlp_text_old.insensitive_color = "#ffffff"
    
    style.tmlp_history_button_text_old  = Style(style.tmlp_style_default)
    style.tmlp_history_button_text_old.selected_color = "#e0511e"
    style.tmlp_history_button_text_old.hover_color = "#e0511e"
    style.tmlp_history_button_text_old.selected_color = "#e0511e"
    style.tmlp_history_button_text_old.hover_color = "#e0511e"
    
    style.tmlp_text_setting_old = Style(style.tmlp_style_default)
    style.tmlp_text_setting_old.color = "#ffffff"
    style.tmlp_text_setting_old.hover_color = "#e0511e"
    style.tmlp_text_setting_old.selected_color = "#e0511e"
    
    style.tmlp_text_small_setting_old = Style(style.tmlp_style_default)
    style.tmlp_text_small_setting_old.color = "#ffffff"
    style.tmlp_text_small_setting_old.hover_color = "#e0511e"
    style.tmlp_text_small_setting_old.selected_color = "#e0511e"
    
    style.tmlp_text_big_setting_old = Style(style.tmlp_style_default)
    style.tmlp_text_big_setting_old.color = "#ffffff"
    style.tmlp_text_big_setting_old.hover_color = "#e0511e"
    style.tmlp_text_big_setting_old.selected_color = "#e0511e"
    
    style.tmlp_text_small_invers_setting_old = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_setting_old.color = "#ffffff"
    style.tmlp_text_small_invers_setting_old.hover_color = "#e0511e"
    style.tmlp_text_small_invers_setting_old.selected_color = "#e0511e"
    
    style.tmlp_text_big_save_load_old = Style(style.tmlp_style_default)
    style.tmlp_text_big_save_load_old.color = "#ffffff"
    style.tmlp_text_big_save_load_old.hover_color = "#e0511e"
    style.tmlp_text_big_save_load_old.selected_color = "#ffffff"
    style.tmlp_text_big_save_load_old.selected_idle_color = "#ffffff"
    style.tmlp_text_big_save_load_old.selected_hover_color = "#e0511e"
    style.tmlp_text_big_save_load_old.insensitive_color  = "#ffffff"
    
    style.tmlp_text_small_save_load_old = Style(style.tmlp_style_default)
    style.tmlp_text_small_save_load_old.color = "#ffffff"
    style.tmlp_text_small_save_load_old.hover_color = "#e0511e"
    style.tmlp_text_small_save_load_old.selected_color = "#ffffff"
    style.tmlp_text_small_save_load_old.selected_idle_color = "#ffffff"
    style.tmlp_text_small_save_load_old.selected_hover_color = "#e0511e"
    style.tmlp_text_small_save_load_old.insensitive_color = "#ffffff"

    style.tmlp_save_load_button_old = Style(style.button)
    style.tmlp_save_load_button_old.background = tmlp_gui_path + "save_load/old/save_load_button_idle.png"
    style.tmlp_save_load_button_old.hover_background = tmlp_gui_path + "save_load/old/save_load_button_hover.png"
    style.tmlp_save_load_button_old.selected_background = tmlp_gui_path + "save_load/old/save_load_button_selected.png"
    style.tmlp_save_load_button_old.selected_hover_background = tmlp_gui_path + "save_load/old/save_load_button_selected.png"
    style.tmlp_save_load_button_old.selected_idle_background = tmlp_gui_path + "save_load/old/save_load_button_selected.png"

    style.tmlp_text_small_preference_old = Style(style.tmlp_style_default)
    style.tmlp_text_small_preference_old.color = "#ffffff"
    style.tmlp_text_small_preference_old.hover_color = "#e0511e"
    style.tmlp_text_small_preference_old.selected_color = "#e0511e"
    
    style.tmlp_text_small_invers_preference_old = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_preference_old.color = "#e0511e"
    style.tmlp_text_small_invers_preference_old.hover_color = "#e0511e"
    style.tmlp_text_small_invers_preference_old.selected_color = "#e0511e"

    style.tmlp_text_prologue = Style(style.tmlp_style_default)
    style.tmlp_text_prologue.color = "#ffffff"
    style.tmlp_text_prologue.hover_color = "#286ebc"
    style.tmlp_text_prologue.selected_color = "#ffffff"
    style.tmlp_text_prologue.selected_idle_color = "#ffffff"
    style.tmlp_text_prologue.selected_hover_color = "#ffffff"
    style.tmlp_text_prologue.insensitive_color = "#ffffff"
    
    style.tmlp_history_button_text_prologue = Style(style.tmlp_style_default)
    style.tmlp_history_button_text_prologue.selected_color = "#286ebc"
    style.tmlp_history_button_text_prologue.hover_color = "#286ebc"
    style.tmlp_history_button_text_prologue.selected_color = "#286ebc"
    style.tmlp_history_button_text_prologue.hover_color = "#286ebc"

    style.tmlp_text_setting_prologue = Style(style.tmlp_style_default)
    style.tmlp_text_setting_prologue.color = "#ffffff"
    style.tmlp_text_setting_prologue.hover_color = "#286ebc"
    style.tmlp_text_setting_prologue.selected_color = "#286ebc"
    
    style.tmlp_text_small_setting_prologue = Style(style.tmlp_style_default)
    style.tmlp_text_small_setting_prologue.color = "#ffffff"
    style.tmlp_text_small_setting_prologue.hover_color = "#286ebc"
    style.tmlp_text_small_setting_prologue.selected_color = "#286ebc"
    
    style.tmlp_text_big_setting_prologue = Style(style.tmlp_style_default)
    style.tmlp_text_big_setting_prologue.color = "#ffffff"
    style.tmlp_text_big_setting_prologue.hover_color = "#286ebc"
    style.tmlp_text_big_setting_prologue.selected_color = "#286ebc"
    
    style.tmlp_text_small_invers_setting_prologue = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_setting_prologue.color = "#ffffff"
    style.tmlp_text_small_invers_setting_prologue.hover_color = "#286ebc"
    style.tmlp_text_small_invers_setting_prologue.selected_color = "#286ebc"
    
    style.tmlp_text_big_save_load_prologue = Style(style.tmlp_style_default)
    style.tmlp_text_big_save_load_prologue.color = "#ffffff"
    style.tmlp_text_big_save_load_prologue.hover_color = "#286ebc"
    style.tmlp_text_big_save_load_prologue.selected_color = "#ffffff"
    style.tmlp_text_big_save_load_prologue.selected_idle_color = "#ffffff"
    style.tmlp_text_big_save_load_prologue.selected_hover_color = "#286ebc"
    style.tmlp_text_big_save_load_prologue.insensitive_color = "#ffffff"
    
    style.tmlp_text_small_save_load_prologue = Style(style.tmlp_style_default)
    style.tmlp_text_small_save_load_prologue.color = "#ffffff"
    style.tmlp_text_small_save_load_prologue.hover_color = "#286ebc"
    style.tmlp_text_small_save_load_prologue.selected_color = "#ffffff"
    style.tmlp_text_small_save_load_prologue.selected_idle_color = "#ffffff"
    style.tmlp_text_small_save_load_prologue.selected_hover_color = "#286ebc"
    style.tmlp_text_small_save_load_prologue.insensitive_color = "#ffffff"

    style.tmlp_save_load_button_prologue = Style(style.button)
    style.tmlp_save_load_button_prologue.background = tmlp_gui_path + "save_load/prologue/save_load_button_idle.png"
    style.tmlp_save_load_button_prologue.hover_background = tmlp_gui_path + "save_load/prologue/save_load_button_hover.png"
    style.tmlp_save_load_button_prologue.selected_background = tmlp_gui_path + "save_load/prologue/save_load_button_selected.png"
    style.tmlp_save_load_button_prologue.selected_hover_background = tmlp_gui_path + "save_load/prologue/save_load_button_selected.png"
    style.tmlp_save_load_button_prologue.selected_idle_background = tmlp_gui_path + "save_load/prologue/save_load_button_selected.png"

    style.tmlp_text_small_preference_prologue = Style(style.tmlp_style_default)
    style.tmlp_text_small_preference_prologue.color = "#ffffff"
    style.tmlp_text_small_preference_prologue.hover_color = "#286ebc"
    style.tmlp_text_small_preference_prologue.selected_color = "#286ebc"
    
    style.tmlp_text_small_preference_prologue_quit_button = Style(style.tmlp_style_default)
    style.tmlp_text_small_preference_prologue_quit_button.color = "#ffffff"
    style.tmlp_text_small_preference_prologue_quit_button.hover_color = "#286ebc"
    style.tmlp_text_small_preference_prologue_quit_button.selected_color = "#ffffff"
    
    style.tmlp_text_small_invers_preference_prologue = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_preference_prologue.color = "#286ebc"
    style.tmlp_text_small_invers_preference_prologue.hover_color = "#286ebc"
    style.tmlp_text_small_invers_preference_prologue.selected_color = "#286ebc"

    style.tmlp_text_quit_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_quit_main_menu_part_one.color = "#ffffff"
    style.tmlp_text_quit_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_quit_main_menu_part_one.selected_color = "#ffffff"
    style.tmlp_text_quit_main_menu_part_one.selected_idle_color = "#ffffff"
    style.tmlp_text_quit_main_menu_part_one.selected_hover_color = "#ffffff"
    style.tmlp_text_quit_main_menu_part_one.insensitive_color = "#ffffff"
    
    style.tmlp_history_button_text_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_history_button_text_main_menu_part_one.selected_color = "#466db8"
    style.tmlp_history_button_text_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_history_button_text_main_menu_part_one.selected_color = "#466db8"
    style.tmlp_history_button_text_main_menu_part_one.hover_color = "#466db8"
    
    style.tmlp_text_setting_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_setting_main_menu_part_one.color = "#ffffff"
    style.tmlp_text_setting_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_setting_main_menu_part_one.selected_color = "#466db8"
    
    style.tmlp_text_small_setting_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_small_setting_main_menu_part_one.color = "#ffffff"
    style.tmlp_text_small_setting_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_small_setting_main_menu_part_one.selected_color = "#466db8"
    
    style.tmlp_text_big_setting_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_big_setting_main_menu_part_one.color = "#ffffff"
    style.tmlp_text_big_setting_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_big_setting_main_menu_part_one.selected_color = "#466db8"
    
    style.tmlp_text_small_invers_setting_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_setting_main_menu_part_one.color = "#ffffff"
    style.tmlp_text_small_invers_setting_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_small_invers_setting_main_menu_part_one.selected_color = "#466db8"
    
    style.tmlp_text_big_save_load_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_big_save_load_main_menu_part_one.color = "#ffffff"
    style.tmlp_text_big_save_load_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_big_save_load_main_menu_part_one.selected_color = "#ffffff"
    style.tmlp_text_big_save_load_main_menu_part_one.selected_idle_color = "#ffffff"
    style.tmlp_text_big_save_load_main_menu_part_one.selected_hover_color = "#466db8"
    style.tmlp_text_big_save_load_main_menu_part_one.insensitive_color = "#ffffff"
    
    style.tmlp_text_small_save_load_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_small_save_load_main_menu_part_one.color = "#ffffff"
    style.tmlp_text_small_save_load_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_small_save_load_main_menu_part_one.selected_color = "#ffffff"
    style.tmlp_text_small_save_load_main_menu_part_one.selected_idle_color = "#ffffff"
    style.tmlp_text_small_save_load_main_menu_part_one.selected_hover_color = "#466db8"
    style.tmlp_text_small_save_load_main_menu_part_one.insensitive_color = "#ffffff"

    style.tmlp_save_load_button_main_menu_part_one = Style(style.button)
    style.tmlp_save_load_button_main_menu_part_one.background = tmlp_gui_path + "save_load/main_menu_part_one/save_load_button_idle.png"
    style.tmlp_save_load_button_main_menu_part_one.hover_background = tmlp_gui_path + "save_load/main_menu_part_one/save_load_button_hover.png"
    style.tmlp_save_load_button_main_menu_part_one.selected_background = tmlp_gui_path + "save_load/main_menu_part_one/save_load_button_selected.png"
    style.tmlp_save_load_button_main_menu_part_one.selected_hover_background = tmlp_gui_path + "save_load/main_menu_part_one/save_load_button_selected.png"
    style.tmlp_save_load_button_main_menu_part_one.selected_idle_background = tmlp_gui_path + "save_load/main_menu_part_one/save_load_button_selected.png"

    style.tmlp_text_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_main_menu_part_one.color = "#ffffff"
    style.tmlp_text_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_main_menu_part_one.selected_color = "#466db8"
    
    style.tmlp_text_main_menu_part_one_quit_button = Style(style.tmlp_style_default)
    style.tmlp_text_main_menu_part_one_quit_button.color = "#ffffff"
    style.tmlp_text_main_menu_part_one_quit_button.hover_color = "#466db8"
    style.tmlp_text_main_menu_part_one_quit_button.selected_color = "#ffffff"
    
    style.tmlp_text_small_invers_preference_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_preference_main_menu_part_one.color = "#466db8"
    style.tmlp_text_small_invers_preference_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_small_invers_preference_main_menu_part_one.selected_color = "#466db8"

    style.tmlp_text_small_preference_main_menu_part_one = Style(style.tmlp_style_default)
    style.tmlp_text_small_preference_main_menu_part_one.color = "#ffffff"
    style.tmlp_text_small_preference_main_menu_part_one.hover_color = "#466db8"
    style.tmlp_text_small_preference_main_menu_part_one.selected_color = "#466db8"

    style.tmlp_text_quit_sunset = Style(style.tmlp_style_default)
    style.tmlp_text_quit_sunset.color = "#ffffff"
    style.tmlp_text_quit_sunset.hover_color = "#e0511e"
    style.tmlp_text_quit_sunset.selected_color = "#ffffff"
    style.tmlp_text_quit_sunset.selected_idle_color = "#ffffff"
    style.tmlp_text_quit_sunset.selected_hover_color = "#ffffff"
    style.tmlp_text_quit_sunset.insensitive_color = "#ffffff"
    
    style.tmlp_history_button_text_sunset = Style(style.tmlp_style_default)
    style.tmlp_history_button_text_sunset.selected_color = "#e0511e"
    style.tmlp_history_button_text_sunset.hover_color = "#e0511e"
    style.tmlp_history_button_text_sunset.selected_color = "#e0511e"
    style.tmlp_history_button_text_sunset.hover_color = "#e0511e"
    
    style.tmlp_text_setting_sunset = Style(style.tmlp_style_default)
    style.tmlp_text_setting_sunset.color = "#ffffff"
    style.tmlp_text_setting_sunset.hover_color = "#e0511e"
    style.tmlp_text_setting_sunset.selected_color = "#e0511e"
    
    style.tmlp_text_small_setting_sunset = Style(style.tmlp_style_default)
    style.tmlp_text_small_setting_sunset.color = "#ffffff"
    style.tmlp_text_small_setting_sunset.hover_color = "#e0511e"
    style.tmlp_text_small_setting_sunset.selected_color = "#e0511e"
    
    style.tmlp_text_big_setting_sunset = Style(style.tmlp_style_default)
    style.tmlp_text_big_setting_sunset.color = "#ffffff"
    style.tmlp_text_big_setting_sunset.hover_color = "#e0511e"
    style.tmlp_text_big_setting_sunset.selected_color = "#e0511e"
    
    style.tmlp_text_small_invers_setting_sunset = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_setting_sunset.color = "#ffffff"
    style.tmlp_text_small_invers_setting_sunset.hover_color = "#e0511e"
    style.tmlp_text_small_invers_setting_sunset.selected_color = "#e0511e"
    
    style.tmlp_text_big_save_load_sunset = Style(style.tmlp_style_default)
    style.tmlp_text_big_save_load_sunset.color = "#ffffff"
    style.tmlp_text_big_save_load_sunset.hover_color = "#e0511e"
    style.tmlp_text_big_save_load_sunset.selected_color = "#ffffff"
    style.tmlp_text_big_save_load_sunset.selected_idle_color = "#ffffff"
    style.tmlp_text_big_save_load_sunset.selected_hover_color = "#e0511e"
    style.tmlp_text_big_save_load_sunset.insensitive_color = "#ffffff"
    
    style.tmlp_text_small_save_load_sunset = Style(style.tmlp_style_default)
    style.tmlp_text_small_save_load_sunset.color = "#ffffff"
    style.tmlp_text_small_save_load_sunset.hover_color = "#e0511e"
    style.tmlp_text_small_save_load_sunset.selected_color = "#ffffff"
    style.tmlp_text_small_save_load_sunset.selected_idle_color = "#ffffff"
    style.tmlp_text_small_save_load_sunset.selected_hover_color = "#e0511e"
    style.tmlp_text_small_save_load_sunset.insensitive_color = "#ffffff"

    style.tmlp_save_load_button_sunset = Style(style.button)
    style.tmlp_save_load_button_sunset.background = tmlp_gui_path + "save_load/sunset/save_load_button_idle.png"
    style.tmlp_save_load_button_sunset.hover_background = tmlp_gui_path + "save_load/sunset/save_load_button_hover.png"
    style.tmlp_save_load_button_sunset.selected_background = tmlp_gui_path + "save_load/sunset/save_load_button_selected.png"
    style.tmlp_save_load_button_sunset.selected_hover_background = tmlp_gui_path + "save_load/sunset/save_load_button_selected.png"
    style.tmlp_save_load_button_sunset.selected_idle_background = tmlp_gui_path + "save_load/sunset/save_load_button_selected.png"

    style.tmlp_text_small_preference_sunset = Style(style.tmlp_style_default)
    style.tmlp_text_small_preference_sunset.color = "#ffffff"
    style.tmlp_text_small_preference_sunset.hover_color = "#e0511e"
    style.tmlp_text_small_preference_sunset.selected_color = "#e0511e"
    
    style.tmlp_text_small_invers_preference_sunset = Style(style.tmlp_style_default)
    style.tmlp_text_small_invers_preference_sunset.color = "#e0511e"
    style.tmlp_text_small_invers_preference_sunset.hover_color = "#e0511e"
    style.tmlp_text_small_invers_preference_sunset.selected_color = "#e0511e"
    
    style.tmlp_text_white = Style(style.tmlp_style_default)
    style.tmlp_text_white.color = "#ffffff"
    style.tmlp_text_white.hover_color = "#ffffff"
    style.tmlp_text_white.selected_color = "#ffffff"