init python:
    from random import Random
    from os import path

    tmlp_gui_path = "tmlp/images/gui/"

    tmlp_thumb = tmlp_gui_path + "preferences/thumb.png"

    tmlp_mod_name = "tmlp"
    tmlp_prefix = tmlp_mod_name + "_"

    for file_name in renpy.list_files():
        if tmlp_mod_name in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith(tmlp_mod_name + "/images/bg/"):
                bg_name = "bg " + tmlp_prefix + file_path

                if file_name.endswith(".ogv"):
                    renpy.image(bg_name, Movie(fps=45, play=file_name))

                else:
                    renpy.image(bg_name, file_name)

            elif file_name.startswith(tmlp_mod_name + "/images/sprites/"):
                renpy.image(
                    tmlp_prefix + file_path,
                    ConditionSwitch(
                        "persistent.sprite_time == 'sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)),
                        "persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)),
                        True, file_name
                    )
                )

            elif file_name.startswith(tmlp_mod_name + "/sounds/"):
                globals()[tmlp_prefix + file_path] = file_name

    tmlp_std_set_for_preview = {}
    tmlp_std_set = {}
    store.tmlp_colors = {}
    store.tmlp_names = {}
    store.tmlp_names_list = []
    tmlp_speaker_color = "speaker_color"

    store.tmlp_names_list.append("tmlp_narrator")

    store.tmlp_names_list.append("tmlp_th")

    tmlp_colors["tmlp_din"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_din"] = "Дин"
    store.tmlp_names_list.append("tmlp_din")

    tmlp_colors["tmlp_dinp"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_dinp"] = "Пионер"
    store.tmlp_names_list.append("tmlp_dinp")

    tmlp_colors["tmlp_pyan"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_pyan"] = "Пьяница"
    store.tmlp_names_list.append("tmlp_pyan")

    tmlp_colors["tmlp_pyap"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_pyap"] = "Пионер"
    store.tmlp_names_list.append("tmlp_pyap")

    tmlp_colors["tmlp_plyaj"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_plyaj"] = "Пляжник"
    store.tmlp_names_list.append("tmlp_plyaj")

    tmlp_colors["tmlp_plyajp"] = {"speaker_color": (85, 19, 19, 255)}
    tmlp_names["tmlp_plyajp"] = "Пионер"
    store.tmlp_names_list.append("tmlp_plyajp")

    tmlp_colors["tmlp_voice"] = {"speaker_color": (225, 221, 125, 255)}
    tmlp_names["tmlp_voice"] = "Голос"
    store.tmlp_names_list.append("tmlp_voice")

    tmlp_colors["tmlp_sam"] = {"speaker_color": (225, 221, 125, 255)}
    tmlp_names["tmlp_sam"] = "Семён"
    store.tmlp_names_list.append("tmlp_sam")

    tmlp_colors["tmlp_myself"] = {"speaker_color": (6, 91, 13, 255)}
    tmlp_names["tmlp_myself"] = "Я"
    store.tmlp_names_list.append("tmlp_myself")

    tmlp_colors["tmlp_el"] = {"speaker_color": (205, 205, 0, 255)}
    tmlp_names["tmlp_el"] = "Электроник"
    store.tmlp_names_list.append("tmlp_el")

    tmlp_colors["tmlp_un"] = {"speaker_color": (170, 100, 217, 255)}
    tmlp_names["tmlp_un"] = "Леночка"
    store.tmlp_names_list.append("tmlp_un")

    tmlp_colors["tmlp_dv"] = {"speaker_color": (210, 139, 16, 255)}
    tmlp_names["tmlp_dv"] = "Двачевская"
    store.tmlp_names_list.append("tmlp_dv")

    tmlp_colors["tmlp_sl"] = {"speaker_color": (214, 176, 0, 255)}
    tmlp_names["tmlp_sl"] = "Славяна"
    store.tmlp_names_list.append("tmlp_sl")

    tmlp_colors["tmlp_us"] = {"speaker_color": (234, 55, 0, 255)}
    tmlp_names["tmlp_us"] = "Мелкая"
    store.tmlp_names_list.append("tmlp_us")

    tmlp_colors["tmlp_mt"] = {"speaker_color": (0, 182, 39, 255)}
    tmlp_names["tmlp_mt"] = "Вожатая"
    store.tmlp_names_list.append("tmlp_mt")

    tmlp_colors["tmlp_cs"] = {"speaker_color": (134, 134, 230, 255)}
    tmlp_names["tmlp_cs"] = "Медсестра"
    store.tmlp_names_list.append("tmlp_cs")

    tmlp_colors["tmlp_mz"] = {"speaker_color": (84, 129, 219, 255)}
    tmlp_names["tmlp_mz"] = "Библиотекарша"
    store.tmlp_names_list.append("tmlp_mz")

    tmlp_colors["tmlp_mi"] = {"speaker_color": (0, 180, 207, 255)}
    tmlp_names["tmlp_mi"] = "Мику"
    store.tmlp_names_list.append("tmlp_mi")

    tmlp_colors["tmlp_uv"] = {"speaker_color": (64, 208, 0, 255)}
    tmlp_names["tmlp_uv"] = "Юля"
    store.tmlp_names_list.append("tmlp_uv")

    tmlp_colors["tmlp_sh"] = {"speaker_color": (205, 194, 18, 255)}
    tmlp_names["tmlp_sh"] = "Шурик"
    store.tmlp_names_list.append("tmlp_sh")

    tmlp_colors["tmlp_pi"] = {"speaker_color": (230, 0, 0, 255)}
    tmlp_names["tmlp_pi"] = "Пионер"
    store.tmlp_names_list.append("tmlp_pi")

    tmlp_colors["tmlp_bush"] = {"speaker_color": (192, 192, 192, 255)}
    tmlp_names["tmlp_bush"] = "Голос"
    store.tmlp_names_list.append("tmlp_bush")

    def tmlp_char_define(x, is_nvl = False):
        global DynamicCharacter
        global nvl
        global tmlp_store
        global tmlp_speaker_color
        tmlp_gl = globals()

        if x == "tmlp_narrator":
            if is_nvl:
                tmlp_gl["tmlp_narrator"] = Character(None, kind = nvl, what_style = "tmlp_text_style", ctc = "none", ctc_position = "fixed")

            else:
                tmlp_gl["tmlp_narrator"] = Character(None, what_style = "tmlp_text_style", ctc = "none", ctc_position = "fixed")

            return

        if x == "tmlp_th":
            if  is_nvl:
                tmlp_gl["tmlp_th"] = Character(None, kind = nvl, what_style = "tmlp_text_style", what_prefix = "~ ", what_suffix = " ~", ctc = "none", ctc_position = "fixed")

            else:
                tmlp_gl["tmlp_th"] = Character(None, what_style = "tmlp_text_style", what_prefix = "~ ", what_suffix = " ~", ctc = "none", ctc_position = "fixed")

            return

        if is_nvl:
            tmlp_gl[x] = DynamicCharacter("%s_name" % x, color = store.tmlp_colors[x][tmlp_speaker_color], kind = nvl, what_style = "tmlp_text_style", who_suffix = ":", ctc = "none", ctc_position = "fixed")
            tmlp_gl["%s_name" % x] = store.tmlp_names[x]

        else:
            tmlp_gl[x] = DynamicCharacter("%s_name" % x, color = store.tmlp_colors[x][tmlp_speaker_color], what_style = "tmlp_text_style", ctc = "none", ctc_position = "fixed")
            tmlp_gl["%s_name" % x] = store.tmlp_names[x]

    def tmlp_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global tmlp_store

        for x in store.tmlp_names_list:
            tmlp_char_define(x)

    def tmlp_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global tmlp_narrator
        global tmlp_th
        tmlp_narrator_nvl = tmlp_narrator
        th_nvl = tmlp_th
        
        global tmlp_store
        
        for x in store.tmlp_names_list:
            tmlp_char_define(x, True)

    def tmlp_reload_names():
        global tmlp_store

        for x in store.tmlp_names_list:
            tmlp_char_define(x)

    tmlp_reload_names()

    def tmlp_day_intro(day_numeral, tmlp_save_name, text_output = "adv", tmlp_part = "one"):
        global save_name
        
        tmlp_part_one_introes_path = tmlp_gui_path + "part_one_introes/part_one_day_"
        tmlp_part_two_intro_path = tmlp_gui_path + "part_two_intro/part_two.webm"
        tmlp_part_three_intro_path = tmlp_gui_path + "part_three_intro/part_three.webm"
        
        save_name = tmlp_save_name

        renpy.pause(1, hard = True)

        if tmlp_part == "one":
            renpy.movie_cutscene(tmlp_part_one_introes_path + str(day_numeral) + ".webm")

        elif tmlp_part == "two":
            renpy.movie_cutscene(tmlp_part_two_intro_path)

        elif tmlp_part == "three":
            renpy.movie_cutscene(tmlp_part_three_intro_path)
        
        renpy.pause(1, hard = True)
        
        if text_output == "adv":
            tmlp_set_mode_adv()

        else:
            tmlp_set_mode_nvl()

    def tmlp_set_zone(zone, lbl, reload_dict = False):
        global tmlp_map_zones

        if reload_dict:
            tmlp_map_zones = {}

        tmlp_map_zones[zone] = lbl

    def tmlp_disable_current_zone():
        global tmlp_map_zones

        a = tmlp_map_zones.pop(tmlp_last_zone)

    def tmlp_day():
        persistent.timeofday = "day"
        persistent.sprite_time = "day"

    def tmlp_city_day():
        persistent.timeofday = "city_day"
        persistent.sprite_time = "day"

    def tmlp_night():
        persistent.timeofday = "night"
        persistent.sprite_time = "night"
    
    def tmlp_city_night():
        persistent.timeofday = "city_night"
        persistent.sprite_time = "night"

    def tmlp_nightmare():
        persistent.timeofday = "nightmare"
        persistent.sprite_time = "night"

    def tmlp_old():
        persistent.timeofday = "old"
        persistent.sprite_time = "day"

    def tmlp_prologue():
        persistent.timeofday = "prologue"
        persistent.sprite_time = "night"
    
    def tmlp_city_prologue():
        persistent.timeofday = "city_prologue"
        persistent.sprite_time = "night"

    def tmlp_sunset():
        persistent.timeofday = "sunset"
        persistent.sprite_time = "sunset"
    
    def tmlp_city_sunset():
        persistent.timeofday = "city_sunset"
        persistent.sprite_time = "sunset"

    def tmlp_blink(blink_pause):
        renpy.show("blink")
        renpy.pause(blink_pause, hard = True)

    def tmlp_unblink(scene_name, unblink_pause):
        renpy.hide("blink")
        renpy.scene()
        renpy.show(scene_name)
        renpy.show("unblink")
        renpy.pause(unblink_pause, hard = True)

    def tmlp_frame_animation(image_name, frames_quantity, retention, loop, transition, start = 1, **properties):
        if image_name:
            anim_args = []

            for i in range(start, start + frames_quantity):
                anim_args.append(renpy.display.im.image(image_name + "_" + str(i) + ".png"))

                if loop:
                    anim_args.append(retention)
                    anim_args.append(transition)

            return anim.TransitionAnimation(*anim_args, **properties)
        return None

    class tmlp_particles(renpy.Displayable, Random, NoRollback):   
        def __init__(self, particle):
            super(tmlp_particles, self).__init__()
            self.particle = renpy.displayable(particle)           
            self.parts_cache = []

            if self.parts_cache:
                self.__init__()

            self.max_parts = 125
            self.oldst = None                    
            
        def tmlp_particles_create_cache(self):     
            self.parts_cache = [self.tmlp_particles_get_anim() for i in xrange(self.max_parts)]
            
        def tmlp_particles_get_anim(self):
            part = self.particle
            pos = [random.randint(0, config.screen_width), random.randint(0, config.screen_height)]
            pos2 = [random.randint(0, config.screen_width), random.randint(0, config.screen_height)]
            dist = [pos2[0] - pos[0], pos2[1] - pos[1]]
            speed = random.uniform(45, 55)
            alpha = random.uniform(.25, 1.0)
            zoom = random.uniform(.25, .75)
            time = math.sqrt(dist[0] ** 2 + dist[1] ** 2) / speed
            elapsed_time = time
            birth_time = time - random.uniform(.5, 3.5)
            death_time = random.uniform(.5, 3.5)
            current_zoom = .0
            current_alpha = .0
            return [part, pos, pos2, dist, speed, alpha, zoom, time, elapsed_time, birth_time, death_time, current_zoom, current_alpha]      
        
        def tmlp_particles_visit(self):
            return [i[0] for i in self.parts_cache]
            
        def tmlp_particles_update(self, st):            
            if self.oldst == None:
                self.oldst = st
            
            self.tick = st - self.oldst
            self.oldst = st     
               
            for part in self.parts_cache:   
                if part[8] <= part[7]:
                    part[8] -= self.tick

                else:
                    part[8] = 0
                    self.tick = 0     
                    
                if part[8] <= .0:
                    upd_val = self.tmlp_particles_get_anim()
                    for i in xrange(1, 13):
                        part[i] = upd_val[i]
                try:        
                    path_progress = part[8] / part[7]           
                    xdist_now = part[3][0] * path_progress
                    part[1][0] = part[2][0] - xdist_now
                
                    ydist_now = part[3][1] * path_progress
                    part[1][1] = part[2][1] - ydist_now
                 
                    alpha_time = part[7] - part[9]
                    alpha_el_time = alpha_time
                    alpha_el_time -= self.tick
                    alpha_progress = alpha_el_time / alpha_time
                    alpha_now = part[5] * (1.0 - alpha_progress)
                    zoom_now = part[6] * (1.0 - alpha_progress)
                
                    if part[8] >= part[9]:
                        if part[12] < part[5] and part[11] < part[6]:
                            part[12] += alpha_now
                            part[11] += zoom_now

                        elif part[12] > part[5] and part[11] > part[6]:
                            part[12] = part[5]
                            part[11] = part[6]
                    
                    if part[8] <= part[10]:
                        if part[12] > .0 and part[11] > .0:
                            part[12] -= alpha_now
                            part[11] -= zoom_now

                        elif part[12] <= .001 and part[11] <= .001:
                            part[12] = .0
                            part[11] = .0

                except ZeroDivisionError:
                    pass
           
        def render(self, width, height, st, at):               
            if not self.parts_cache:
                self.tmlp_particles_create_cache()
                           
            renderObj = renpy.Render(config.screen_width, config.screen_height)

            for part in self.parts_cache:
                xpos, ypos = part[1]
                alpha, zoom = part[12], part[11]
                t = Transform(child = part[0], zoom = zoom, alpha = alpha)
                cp_render = renpy.render(t, width, height, st, at)
                renderObj.blit(cp_render, (xpos, ypos))
                        
            self.tmlp_particles_update(st)              
            renpy.redraw(self, 0)
            return renderObj

    # class tmlp_glitches(renpy.Displayable, Random, NoRollback):
    #     def __init__(self, image_name, speed_multipler = .5):
    #         super(tmlp_glitches, self).__init__()
    #         self.image_name = renpy.easy.displayable(image_name)
    #         self.cached_images = []
    #         self.speed_multipler = float(speed_multipler)

    #     def tmlp_glitches_visit(self):
    #         return [i[0] for i in self.cached_images] + [self.image_name]

    #     def tmlp_glitches_create_cache(self):
    #         self.cached_images = [self.tmlp_glitches_get_random_recolor() for i in xrange(500)]

    #     def tmlp_glitches_get_random_crop(self):
    #         width, height = fix_map(lambda x: self.tmlp_glitches_rndInt((self.random() * x * .1)), self.base_size)

    #         width *= 10

    #         x, y = fix_map(lambda x: self.tmlp_glitches_rndInt(self.uniform(.0, (x[1] - x[0]))), zip((width, height), self.base_size))

    #         return(LiveCrop((x, y, width, height), self.image_name), (x, y), (width, height))

    #     def tmlp_glitches_get_random_recolor(self):
    #         crop, pos, size = self.tmlp_glitches_get_random_crop()
    #         return(Transform(LiveComposite(size, (0, 0), crop, (0, 0), AlphaMask(Solid(tuple(self.randint(0, 200) for i in xrange(4))), crop)), xzoom = self.uniform(1., 1.5), yzoom = self.uniform(.5, 1.),), pos, size)

    #     @staticmethod
    #     def tmlp_glitches_rndInt(val):
    #         return int(round(float(val)))

    #     def render(self, width, height, st, at):
    #         pic_rend = renpy.render(self.image_name, width, height, st, at)
    #         w, h = self.base_size = fix_map(self.tmlp_glitches_rndInt, pic_rend.get_size())

    #         if not self.cached_images:
    #             self.tmlp_glitches_create_cache()

    #         renderObj = renpy.Render(w, h)

    #         if self.randint(0, 9):
    #             renderObj.blit(pic_rend, (0, 0))

    #         for i in xrange(self.randint(0, 50)):
    #             image_name, pos, old_size = self.choice(self.cached_images)
    #             oldX, oldY = old_size
    #             surface = renpy.render(image_name, width, height, st, at)
    #             sizeX, sizeY = surface.get_size()
    #             x, y = pos
    #             x -= (float((sizeX - oldX)) / 2.)
    #             y -= (float((sizeY - oldY)) / 2.)
    #             x += (sizeX * self.uniform(-.2, .2))
    #             renderObj.blit(renpy.render(image_name, width, height, st, at), tuple(fix_map(self.tmlp_glitches_rndInt, (x, y))))

    #         renpy.redraw(self, (self.random() * self.speed_multipler))
    #         return renderObj

init:
    image tmlp_part_one_main_menu = Movie(fps = 45, play = tmlp_gui_path + "main_menu_part_one/tmlp_part_one_main_menu.webm")

    image tmlp_part_one_main_menu_1of3 = tmlp_frame_animation(tmlp_gui_path + "main_menu_part_one/1of3_frame_animation/1of3", 20, 1, True, dissolve)
    image tmlp_stars_anim = tmlp_frame_animation("tmlp/images/bg/anim_bg/tmlp_stars/stars", 2, 1.5, True, Dissolve(1.5))
    image bg tmlp_int_catacombs_living_celling_blurred = im.Blur("tmlp/images/bg/part1/tmlp_int_catacombs_living_celling.png", 2)

    # image tmlp_part_one_main_menu_1of3_glitch = tmlp_glitches(tmlp_gui_path + "main_menu/part1/1of3_static.png", 1)
    # image tmlp_text = tmlp_glitches(tmlp_gui_path + "main_menu_part_one/tmlp_text.png")

    $ tmlp_transition = ImageDissolve(tmlp_gui_path + "transitions/glitch.png", 2, 50, reverse = False)
    $ tmlp_glitch_transition = MultipleTransition([True, Dissolve(0.5), "tmlp/images/gui/transitions/glitch/1.png", Pause(1.0), "tmlp/images/gui/transitions/glitch/2.png", dissolve, True])

    if persistent.tmlp_firstrun == None:
        $ persistent.tmlp_firstrun = False

    if persistent.tmlp_part_one_completed == None:
        $ persistent.tmlp_part_one_completed = False

    if persistent.tmlp_part_two_completed == None:
        $ persistent.tmlp_part_two_completed = False

    $ tmlp_pyan_contempt = 0
    $ tmlp_diary_active = False

    transform tmlp_bus_moving():
        subpixel True
        truecenter
        zoom 1.03

        parallel:
            linear 0.2 xoffset -2
            linear 0.3 xoffset 3
            linear 0.2 xoffset -1
            linear 0.3 xoffset 2
            repeat

        parallel:
            linear 0.2 yoffset -1
            linear 0.25 yoffset 2
            linear 0.2 yoffset -1
            repeat