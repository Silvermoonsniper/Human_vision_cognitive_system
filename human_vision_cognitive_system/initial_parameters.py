#initial parameters setting

def initialization():
   initial_args ={
           # start our visual stimuli cognitive system
           "start_congnitivsystem" : 1,
       # array to store geometric object information
           "object_matrix": [],
       # array to store processing time
           "time_matrix": [],
   # user question activate system
            "question" : 'black circle',
   # set time limitation for cognitive system ,unit:ms
            "time_limit" : 2000,
   # here we set number of image
            "image_number" : 10,
   #flag for plot
             "plot_flag" : 0,
       # basically we have two arrays one for word, one for printed color, thus we spilt visual stimuli in two groups, one is word corresponds
       # to its printed color, another one not corresponds
             "stroop_visual_stimuli" : ['red_red', 'green_red', 'yellow_blue', 'blue_blue', 'blue_green', 'green_yellow',
                                'green_green',
                                'purple_yellow', 'purple_purple', 'purple_green', 'gray_gray', 'gray_blue',
                                'gray_yellow', 'gray_purple', 'gray_green'],
   # second example of visual stimuli
             "stroop_visual_stimuli1" : ['clean_red', 'green_red', 'yellow_blue', 'blue_blue', 'blue_green', 'green_yellow',
                             'green_green',
                             'purple_yellow', 'dry_purple', 'pop_green', 'gray_gray', 'gray_blue', 'gray_yellow',
                             'gray_purple', 'gray_green'],
   # array to store words whose word meaning are colors
              "target_range" : ['red', 'purple', 'green', 'yellow', 'gray', 'blue'],
       # user activate cognitive system to tackle stroop interference effect
              "user_command" : ['Please read the word meaning of each visual stimuli'],
              "user_command1" : ['Please read the printed color of each visual stimuli'],
   # keywords for targeted recognized object:color or word meaning
              "object_information" : ['word meaning', 'printed color']










      }
   return initial_args
