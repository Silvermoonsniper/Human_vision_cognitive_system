# This is an implementation of human vision cognitive system,












 # main entrance
from class_human_vision_cognitor import human_vision_cognitor
from image_data_generation.image_creation_unit import imagdata_creation
from initial_parameters import initialization
from system_start_and_helper_functions.memory_effects_visualize import memory_effects_visualize

if __name__ == '__main__':
        #flag to switch between different functions
        #   "memory_effect_flag": study memory effect
        #   "stroop_effect_flag": stroop effect
        #   # "multiple question": response of cognitive system regarding to one image with multiple questions
        #    "normal mode": response of cognitive system for consecutive images, but each image only processes once
        flag= "normal mode"
        # obtain initiag args
        initial_args=initialization()
        #call the cognitive system class
        C=human_vision_cognitor(initial_args)
        if flag == "normal mode":
            for i in range(initial_args["image_number"]):
            # deliver image data to cognitive system
               image, total_number = imagdata_creation()

        #enable cognitive system
               C.whole_cognitivesystem(total_number,initial_args["object_matrix"],initial_args['time_matrix'],initial_args['image_number'],initial_args['plot_flag'],
                                initial_args["start_congnitivsystem"], initial_args["question"],initial_args["time_limit"],image)

        #if we study stroop effect
        if flag == "stroop_effect_flag":
            C.stroop_effect_simulator()
        # if we want to show response of cognitive system with multiple questions
        if flag == "multiple question":
            # image data with grouping elements
            image = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'gray circle', '_', '_', '_', '_'],
                     ['_', '_', '_', '_', '_', 'red polygon', 'red polygon', 'red polygon', '_', '_', '_', '_', '_',
                      '_', 'gray circle', '_'],
                     ['_', '_', '_', '_', '_', 'red polygon', 'red polygon', 'red polygon', '_', '_', '_', '_', '_',
                      '_', '_', '_'],
                     ['_', '_', '_', '_', '_', 'red polygon', 'red polygon', 'red polygon', '_', '_', '_', '_', '_',
                      '_', '_', '_'],
                     ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
                     ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'red polygon', '_', '_', '_', '_'],
                     ['_', 'gray rectangle', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'gray rectangle', '_',
                      '_', '_'],
                     ['_', '_', '_', '_', '_', 'gray rectangle', 'gray rectangle', '_', '_', '_', '_', '_', '_', '_',
                      '_', '_'],
                     ['_', '_', '_', '_', '_', 'gray rectangle', 'gray rectangle', '_', '_', '_', '_', '_', '_', '_',
                      '_', '_'],
                     ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
                     ['_', 'red circle', '_', '_', '_', '_', '_', '_', 'yellow rectangle', '_', '_', '_', '_', '_', '_',
                      '_'],
                     ['_', '_', '_', '_', 'black circle', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
                     ['_', '_', '_', '_', '_', '_', '_', '_', '_', 'red circle', '_', '_', '_', '_', '_', '_']]

            # deliver image data to cognitive system
            image1, total_number = imagdata_creation()
            final, final1, a= C.example_multiple_function(total_number,image)
            print(final, final1, a)
        #if we study memory effects
        if flag == "memory_effect_flag":
            # question list and word list
            question_list = ['Does the word denote a type of plant', ' Does the word denote a type of animal',
                             'Does the word denote a type of electronic product',
                             ' Does the word denote a type of clothes', 'Is the word in capital letters'
                , 'Is the word in noncapital letters', ' Is the word looking long', ' Is the word looking short']
            word_list = ['tree', 'TREE', 'flower', 'elephant', 'hoodie', 'garment', 'JEANS', 'cellphone', 'headphone',
                         'butterfly']

            #key information of question
            object_information = ['denote', 'Is']
            # vectorial representation of word
            # regarding different aspects: [plant, animal, short word, long word, electronical product, nonelectronic product,captial, noncapital], if
            # one word fulfills one attributes, we assign 1, otherwise assgn 0
            plant = ['tree', 'TREE', 'flower']
            clothes = ['hoodie', 'garment', 'JEANS']
            animal = ['elephant', 'butterfly']
            captial = ['TREE', 'JEANS']
            electronic_product = ['cellphone', 'headphone']
            #visulize results
            memory_effects_visualize(word_list, question_list,object_information)

