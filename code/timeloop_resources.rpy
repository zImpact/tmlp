init python:
    from random import Random
    from renpy.loader import transfn
    from __builtin__ import map as fix_map
    from os import path

    timeloop_gui_path = "timeloop/images/gui/"

    timeloop_thumb = timeloop_gui_path + "preferences/thumb.png"

    for file_name in renpy.list_files():
        if "timeloop" in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith("timeloop/images/bg/"):
                if file_name.endswith(".ogv"):
                    renpy.image("bg " + file_path, Movie(fps = 45, play = file_name))

                else:
                    renpy.image("bg " + file_path, file_name)

            elif file_name.startswith("timeloop/images/gui/"):
                renpy.image(file_path, file_name)

            elif file_name.startswith("timeloop/images/sprites/"):
                renpy.image(file_path, ConditionSwitch("persistent.sprite_time == 'sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), True, file_name))

            elif file_name.startswith("timeloop/sounds/"):
                globals()[file_path] = file_name

    timeloop_std_set_for_preview = {}
    timeloop_std_set = {}
    store.timeloop_colors = {}
    store.timeloop_names = {}
    store.timeloop_names_list = []
    timeloop_speaker_color = "speaker_color"

    store.timeloop_names_list.append("tl_narrator")

    store.timeloop_names_list.append("tl_th")

    timeloop_colors["tl_din"] = {"speaker_color": (85, 19, 19, 255)}
    timeloop_names["tl_din"] = "Дин"
    store.timeloop_names_list.append("tl_din")

    timeloop_colors["tl_dinp"] = {"speaker_color": (85, 19, 19, 255)}
    timeloop_names["tl_dinp"] = "Пионер"
    store.timeloop_names_list.append("tl_dinp")

    timeloop_colors["tl_pyan"] = {"speaker_color": (85, 19, 19, 255)}
    timeloop_names["tl_pyan"] = "Пьяница"
    store.timeloop_names_list.append("tl_pyan")

    timeloop_colors["tl_pyap"] = {"speaker_color": (85, 19, 19, 255)}
    timeloop_names["tl_pyap"] = "Пионер"
    store.timeloop_names_list.append("tl_pyap")

    timeloop_colors["tl_plyaj"] = {"speaker_color": (85, 19, 19, 255)}
    timeloop_names["tl_plyaj"] = "Пляжник"
    store.timeloop_names_list.append("tl_plyaj")

    timeloop_colors["tl_plyajp"] = {"speaker_color": (85, 19, 19, 255)}
    timeloop_names["tl_plyajp"] = "Пионер"
    store.timeloop_names_list.append("tl_plyajp")

    timeloop_colors["tl_voice"] = {"speaker_color": (225, 221, 125, 255)}
    timeloop_names["tl_voice"] = "Голос"
    store.timeloop_names_list.append("tl_voice")

    timeloop_colors["tl_sam"] = {"speaker_color": (225, 221, 125, 255)}
    timeloop_names["tl_sam"] = "Семён"
    store.timeloop_names_list.append("tl_sam")

    timeloop_colors["tl_myself"] = {"speaker_color": (6, 91, 13, 255)}
    timeloop_names["tl_myself"] = "Я"
    store.timeloop_names_list.append("tl_myself")

    timeloop_colors["tl_el"] = {"speaker_color": (205, 205, 0, 255)}
    timeloop_names["tl_el"] = "Электроник"
    store.timeloop_names_list.append("tl_el")

    timeloop_colors["tl_un"] = {"speaker_color": (170, 100, 217, 255)}
    timeloop_names["tl_un"] = "Леночка"
    store.timeloop_names_list.append("tl_un")

    timeloop_colors["tl_dv"] = {"speaker_color": (210, 139, 16, 255)}
    timeloop_names["tl_dv"] = "Двачевская"
    store.timeloop_names_list.append("tl_dv")

    timeloop_colors["tl_sl"] = {"speaker_color": (214, 176, 0, 255)}
    timeloop_names["tl_sl"] = "Славяна"
    store.timeloop_names_list.append("tl_sl")

    timeloop_colors["tl_us"] = {"speaker_color": (234, 55, 0, 255)}
    timeloop_names["tl_us"] = "Мелкая"
    store.timeloop_names_list.append("tl_us")

    timeloop_colors["tl_mt"] = {"speaker_color": (0, 182, 39, 255)}
    timeloop_names["tl_mt"] = "Вожатая"
    store.timeloop_names_list.append("tl_mt")

    timeloop_colors["tl_cs"] = {"speaker_color": (134, 134, 230, 255)}
    timeloop_names["tl_cs"] = "Медсестра"
    store.timeloop_names_list.append("tl_cs")

    timeloop_colors["tl_mz"] = {"speaker_color": (84, 129, 219, 255)}
    timeloop_names["tl_mz"] = "Библиотекарша"
    store.timeloop_names_list.append("tl_mz")

    timeloop_colors["tl_mi"] = {"speaker_color": (0, 180, 207, 255)}
    timeloop_names["tl_mi"] = "Мику"
    store.timeloop_names_list.append("tl_mi")

    timeloop_colors["tl_uv"] = {"speaker_color": (64, 208, 0, 255)}
    timeloop_names["tl_uv"] = "Юля"
    store.timeloop_names_list.append("tl_uv")

    timeloop_colors["tl_sh"] = {"speaker_color": (205, 194, 18, 255)}
    timeloop_names["tl_sh"] = "Шурик"
    store.timeloop_names_list.append("tl_sh")

    timeloop_colors["tl_pi"] = {"speaker_color": (230, 0, 0, 255)}
    timeloop_names["tl_pi"] = "Пионер"
    store.timeloop_names_list.append("tl_pi")

    timeloop_colors["tl_bush"] = {"speaker_color": (192, 192, 192, 255)}
    timeloop_names["tl_bush"] = "Голос"
    store.timeloop_names_list.append("tl_bush")

    def timeloop_char_define(x, is_nvl = False):
        global DynamicCharacter
        global nvl
        global timeloop_store
        global timeloop_speaker_color
        timeloop_gl = globals()

        if x == "tl_narrator":
            if is_nvl:
                timeloop_gl["tl_narrator"] = Character(None, kind = nvl, what_style = "timeloop_text_style", ctc = "none", ctc_position = "fixed")

            else:
                timeloop_gl["tl_narrator"] = Character(None, what_style = "timeloop_text_style", ctc = "none", ctc_position = "fixed")

            return

        if x == "tl_th":
            if  is_nvl:
                timeloop_gl["tl_th"] = Character(None, kind = nvl, what_style = "timeloop_text_style", what_prefix = "~ ", what_suffix = " ~", ctc = "none", ctc_position = "fixed")

            else:
                timeloop_gl["tl_th"] = Character(None, what_style = "timeloop_text_style", what_prefix = "~ ", what_suffix = " ~", ctc = "none", ctc_position = "fixed")

            return

        if is_nvl:
            timeloop_gl[x] = DynamicCharacter("%s_name" % x, color = store.timeloop_colors[x][timeloop_speaker_color], kind = nvl, what_style = "timeloop_text_style", who_suffix = ":", ctc = "none", ctc_position = "fixed")
            timeloop_gl["%s_name" % x] = store.timeloop_names[x]

        else:
            timeloop_gl[x] = DynamicCharacter("%s_name" % x, color = store.timeloop_colors[x][timeloop_speaker_color], what_style = "timeloop_text_style", ctc = "none", ctc_position = "fixed")
            timeloop_gl["%s_name" % x] = store.timeloop_names[x]

    def timeloop_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global timeloop_store

        for x in store.timeloop_names_list:
            timeloop_char_define(x)

    def timeloop_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global tl_narrator
        global tl_th
        tl_narrator_nvl = tl_narrator
        th_nvl = tl_th
        
        global timeloop_store
        
        for x in store.timeloop_names_list:
            timeloop_char_define(x, True)

    def timeloop_reload_names():
        global timeloop_store

        for x in store.timeloop_names_list:
            timeloop_char_define(x)

    timeloop_reload_names()

    def timeloop_day_intro(day_numeral, tl_save_name, text_output = "adv", tl_part = "one"):
        global save_name
        
        tl_part_one_introes_path = timeloop_gui_path + "part_one_introes/part_one_day_"
        tl_part_two_intro_path = timeloop_gui_path + "part_two_intro/part_two.webm"
        tl_part_three_intro_path = timeloop_gui_path + "part_three_intro/part_three.webm"
        
        save_name = tl_save_name

        renpy.pause(1, hard = True)

        if tl_part == "one":
            renpy.movie_cutscene(tl_part_one_introes_path + str(day_numeral) + ".webm")

        elif tl_part == "two":
            renpy.movie_cutscene(tl_part_two_intro_path)

        elif tl_part == "three":
            renpy.movie_cutscene(tl_part_three_intro_path)
        
        renpy.pause(1, hard = True)
        
        if text_output == "adv":
            timeloop_set_mode_adv()

        else:
            timeloop_set_mode_nvl()

    def timeloop_set_zone(zone, lbl, reload_dict = False):
        global timeloop_map_zones

        if reload_dict:
            timeloop_map_zones = {}

        timeloop_map_zones[zone] = lbl

    def timeloop_disable_current_zone():
        global timeloop_map_zones

        a = timeloop_map_zones.pop(timeloop_last_zone)

    def timeloop_day():
        persistent.timeofday = "day"
        persistent.sprite_time = "day"

    def timeloop_city_day():
        persistent.timeofday = "city_day"
        persistent.sprite_time = "day"

    def timeloop_night():
        persistent.timeofday = "night"
        persistent.sprite_time = "night"
    
    def timeloop_city_night():
        persistent.timeofday = "city_night"
        persistent.sprite_time = "night"

    def timeloop_nightmare():
        persistent.timeofday = "nightmare"
        persistent.sprite_time = "night"

    def timeloop_old():
        persistent.timeofday = "old"
        persistent.sprite_time = "day"

    def timeloop_prologue():
        persistent.timeofday = "prologue"
        persistent.sprite_time = "night"
    
    def timeloop_city_prologue():
        persistent.timeofday = "city_prologue"
        persistent.sprite_time = "night"

    def timeloop_sunset():
        persistent.timeofday = "sunset"
        persistent.sprite_time = "sunset"
    
    def timeloop_city_sunset():
        persistent.timeofday = "city_sunset"
        persistent.sprite_time = "sunset"

    def timeloop_blink(blink_pause):
        renpy.show("blink")
        renpy.pause(blink_pause, hard = True)

    def timeloop_unblink(scene_name, unblink_pause):
        renpy.hide("blink")
        renpy.scene()
        renpy.show(scene_name)
        renpy.show("unblink")
        renpy.pause(unblink_pause, hard = True)

    def timeloop_frame_animation(image_name, frames_quantity, retention, loop, transition, start = 1, **properties):
        if image_name:
            anim_args = []

            for i in range(start, start + frames_quantity):
                anim_args.append(renpy.display.im.image(image_name + "_" + str(i) + ".png"))

                if loop:
                    anim_args.append(retention)
                    anim_args.append(transition)

            return anim.TransitionAnimation(*anim_args, **properties)
        return None

    class timeloop_particles(renpy.Displayable, Random, NoRollback):   
        def __init__(self, particle):
            super(timeloop_particles, self).__init__()
            self.particle = renpy.displayable(particle)           
            self.parts_cache = []

            if self.parts_cache:
                self.__init__()

            self.max_parts = 125
            self.oldst = None                    
            
        def timeloop_particles_create_cache(self):     
            self.parts_cache = [self.timeloop_particles_get_anim() for i in xrange(self.max_parts)]
            
        def timeloop_particles_get_anim(self):
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
        
        def timeloop_particles_visit(self):
            return [i[0] for i in self.parts_cache]
            
        def timeloop_particles_update(self, st):            
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
                    upd_val = self.timeloop_particles_get_anim()
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
                self.timeloop_particles_create_cache()
                           
            renderObj = renpy.Render(config.screen_width, config.screen_height)

            for part in self.parts_cache:
                xpos, ypos = part[1]
                alpha, zoom = part[12], part[11]
                t = Transform(child = part[0], zoom = zoom, alpha = alpha)
                cp_render = renpy.render(t, width, height, st, at)
                renderObj.blit(cp_render, (xpos, ypos))
                        
            self.timeloop_particles_update(st)              
            renpy.redraw(self, 0)
            return renderObj

    class timeloop_glitches(renpy.Displayable, Random, NoRollback):
        def __init__(self, image_name, speed_multipler = .5):
            super(timeloop_glitches, self).__init__()
            self.image_name = renpy.easy.displayable(image_name)
            self.cached_images = []
            self.speed_multipler = float(speed_multipler)

        def timeloop_glitches_visit(self):
            return [i[0] for i in self.cached_images] + [self.image_name]

        def timeloop_glitches_create_cache(self):
            self.cached_images = [self.timeloop_glitches_get_random_recolor() for i in xrange(500)]

        def timeloop_glitches_get_random_crop(self):
            width, height = fix_map(lambda x: self.timeloop_glitches_rndInt((self.random() * x * .1)), self.base_size)

            width *= 10

            x, y = fix_map(lambda x: self.timeloop_glitches_rndInt(self.uniform(.0, (x[1] - x[0]))), zip((width, height), self.base_size))

            return(LiveCrop((x, y, width, height), self.image_name), (x, y), (width, height))

        def timeloop_glitches_get_random_recolor(self):
            crop, pos, size = self.timeloop_glitches_get_random_crop()
            return(Transform(LiveComposite(size, (0, 0), crop, (0, 0), AlphaMask(Solid(tuple(self.randint(0, 200) for i in xrange(4))), crop)), xzoom = self.uniform(1., 1.5), yzoom = self.uniform(.5, 1.),), pos, size)

        @staticmethod
        def timeloop_glitches_rndInt(val):
            return int(round(float(val)))

        def render(self, width, height, st, at):
            pic_rend = renpy.render(self.image_name, width, height, st, at)
            w, h = self.base_size = fix_map(self.timeloop_glitches_rndInt, pic_rend.get_size())

            if not self.cached_images:
                self.timeloop_glitches_create_cache()

            renderObj = renpy.Render(w, h)

            if self.randint(0, 9):
                renderObj.blit(pic_rend, (0, 0))

            for i in xrange(self.randint(0, 50)):
                image_name, pos, old_size = self.choice(self.cached_images)
                oldX, oldY = old_size
                surface = renpy.render(image_name, width, height, st, at)
                sizeX, sizeY = surface.get_size()
                x, y = pos
                x -= (float((sizeX - oldX)) / 2.)
                y -= (float((sizeY - oldY)) / 2.)
                x += (sizeX * self.uniform(-.2, .2))
                renderObj.blit(renpy.render(image_name, width, height, st, at), tuple(fix_map(self.timeloop_glitches_rndInt, (x, y))))

            renpy.redraw(self, (self.random() * self.speed_multipler))
            return renderObj

init:
    image timeloop_part_one_main_menu = Movie(fps = 45, play = timeloop_gui_path + "main_menu_part_one/timeloop_part_one_main_menu.webm")

    image timeloop_part_one_main_menu_1of3 = timeloop_frame_animation(timeloop_gui_path + "main_menu_part_one/1of3_frame_animation/1of3", 20, 1, True, dissolve)
    image tl_stars_anim = timeloop_frame_animation("timeloop/images/bg/anim_bg/tl_stars/stars", 2, 1.5, True, Dissolve(1.5))
    image bg tl_int_catacombs_living_celling_blurred = im.Blur("timeloop/images/bg/part1/tl_int_catacombs_living_celling.png", 2)

    image timeloop_part_one_main_menu_1of3_glitch = timeloop_glitches(timeloop_gui_path + "main_menu/part1/1of3_static.png", 1)
    image timeloop_text = timeloop_glitches(timeloop_gui_path + "main_menu_part_one/timeloop_text.png")

    $ tl_transition = ImageDissolve(timeloop_gui_path + "transitions/glitch.png", 2, 50, reverse = False)
    $ tl_glitch_transition = MultipleTransition([True, Dissolve(0.5), "timeloop/images/gui/transitions/glitch/1.png", Pause(1.0), "timeloop/images/gui/transitions/glitch/2.png", dissolve, True])

    if persistent.timeloop_firstrun == None:
        $ persistent.timeloop_firstrun = False

    if persistent.timeloop_part_one_completed == None:
        $ persistent.timeloop_part_one_completed = False

    if persistent.timeloop_part_two_completed == None:
        $ persistent.timeloop_part_two_completed = False

    $ timeloop_pyan_contempt = 0
    $ timeloop_diary_active = False

    transform tl_bus_moving():
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