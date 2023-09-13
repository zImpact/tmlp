screen timeloop_notebook:
    tag menu
    modal True
    add "timeloop_blank"
    if timeloop_notebook_prologue_day_1 == True:
        add "timeloop_notebook_prologue_day_1"
        
    elif timeloop_notebook_prologue_day_2 == True:
        add "timeloop_notebook_prologue_day_2"
        
    elif timeloop_part_one_main_day1_camp == True:
        add "timeloop_part_one_main_day1_camp"
        
    elif timeloop_part_one_main_day1_catacombs == True:
        add "timeloop_part_one_main_day1_catacombs"