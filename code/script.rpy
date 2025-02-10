init python:
    class timeloop_FunctionCallback(Action):
        def __init__(self, function, *arguments):
            self.function = function
            self.arguments = arguments

        def __call__(self):
            return self.function(self.arguments)
    
    def timeloop_on_load_callback(slot):
        try:
            if persistent.timeloop_on_save_timeofday[slot]:
                persistent.timeofday = persistent.timeloop_on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.timeloop_on_save_timeofday[slot][1]
                persistent.font_size = persistent.timeloop_on_save_timeofday[slot][2]
                _preferences.volumes["music"] = persistent.timeloop_on_save_timeofday[slot][3]
                _preferences.volumes["sfx"] = persistent.timeloop_on_save_timeofday[slot][4]
                _preferences.volumes["voice"] = persistent.timeloop_on_save_timeofday[slot][5]
        
        except:
            pass
    
    def timeloop_on_save_callback(slot):
        if not persistent.timeloop_on_save_timeofday:
            persistent.timeloop_on_save_timeofday = {}

        persistent.timeloop_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes["music"], _preferences.volumes["sfx"], _preferences.volumes["voice"])
        
    def timeloop_screen_save():
        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[("timeloop_old_" + screen_name, None)] = renpy.display.screen.screens[(screen_name, None)]
        
    def timeloop_screen_act():
        config.window_title = u"Петля времени"
        config.name = "Timeloop"
        config.version = "1.0.0."

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("timeloop_" + screen_name, None)]

        renpy.free_memory()
        layout.LOADING = "Потерять несохраненые данные?"
            
        config.mouse = {"default": [(timeloop_gui_path + "misc/tl_cursor.png", 0, 0)]}

        if persistent.timeloop_part_one_completed == False:
            config.main_menu_music = tl_suicidwave_hustler#tl_mega_drive_narc

        if persistent.timeloop_part_one_completed == True:
            config.main_menu_music = tl_stigmata_tanwui

        if persistent.timeloop_part_two_completed == True:
            config.main_menu_music = tl_yoko_kanno_total_eclipse

        config.linear_saves_page_size = None
        persistent._file_page = "timeloop_FilePage_1"  

    def timeloop_screens_diact():
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.2"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("timeloop_old_" + screen_name, None)]

        renpy.free_memory()
        layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
            
        config.mouse = {"default": [("images/misc/mouse/1.png", 0, 0)]}

        config.main_menu_music = "sound/music/blow_with_the_fires.ogg"

        persistent._file_page = 1

        for channel in ["ambience", "music", "sound", "sound_loop"]:
            renpy.music.stop(channel)
            
        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def timeloop_screens_save_act():
        timeloop_screen_save()
        timeloop_screen_act()