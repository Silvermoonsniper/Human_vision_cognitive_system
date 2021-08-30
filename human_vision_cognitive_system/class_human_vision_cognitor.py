# The overall  vision cognitive System starts here,
# Input parameters:
# start_congnitivsystem: start button to activate whole system
# question: user command to look for specific objects
# time_limit： processing time that required for cognitive process
# output parameter:
# object_matrix: array to store number of detected objects for different images
# time_matrix:array to store process time  for different images
#

# start our visual stimuli cognitive system

from cognitors.shape_detection_unit import *
import pandas as pd
from novel_functionality_implementation.stroop_interference_effect import stroop_effect_recognizer
from system_start_and_helper_functions.stroop_effect_visualize import plot_final
from system_start_and_helper_functions.user_activation_unit import check_question


class human_vision_cognitor():
    def __init__(self,initial_args):
        for key in initial_args:
            setattr(self, key, initial_args[key])

# the input paramter are image link and user question, depends on different user question, we identify objects with specific shape and color
    def cognitive_system(self,image, question, total_number, time_limit):
    # do detection depends on user question, all separate detection functions set image data as input and return the number of objects with given
    # shape and color
        if question == 'gray circle':
            gray_circle_number, time = circle_detection_1(image, total_number, time_limit)
            print(gray_circle_number, 'gray circle')
            return gray_circle_number, time

        if question == 'red circle':
           red_circle_number, time = circle_detection_2(image, total_number, time_limit)
           print(red_circle_number, 'red circle')
           return red_circle_number, time
        if question == 'black circle':
           black_circle_number, time = circle_detection_3(image, total_number, time_limit)
           print(black_circle_number, 'black circle')
           return black_circle_number, time
        if question == 'yellow rectangle':
           yellow_rectangle_number, time = rectangle_detection_1(image, total_number, time_limit)

           print(yellow_rectangle_number, 'yellow rectangle')
           return yellow_rectangle_number, time
        if question == 'gray rectangle':
           gray_rectangle_number, time = rectangle_detection_2(image, total_number, time_limit)
           print(gray_rectangle_number, 'gray rectangle')
           return gray_rectangle_number, time
        if question == 'red polygon':
           red_polygon_number, time = polygon_detection(image, total_number, time_limit)
           print(red_polygon_number, 'red polygon')
           return red_polygon_number, time

    def whole_cognitivesystem(self,total_number,object_matrix,time_matrix,image_number,plot_flag,start_congnitivsystem, question, time_limit, image):
        if start_congnitivsystem == 1:
        # question=['black circle','red circle','gray circle','gray rectangle','yellow rectangle','red polygon']

           object_number, time = self.cognitive_system(image, question, total_number, time_limit)

        # store geometric object and detection time information
           object_matrix.append(object_number)
           time_matrix.append(time)
        # plot detected object number in each image
        if plot_flag == 1:
           x = np.linspace(0, image_number - 1, image_number)
           plt.subplot(2, 1, 1)
           plt.scatter(x, object_matrix)
           plt.legend([question], loc='best')
           plt.ylabel(question)
           plt.xlabel('Image No.')
           plt.title('The Number of Detected Colored Geometric Objects for Different Images')
           plt.tight_layout(pad=3.0)
           plt.subplot(2, 1, 2)
           plt.plot(x, time_matrix, 'r')
           plt.legend(['detection time'], loc='best')
           plt.ylabel('detection time')
           plt.xlabel('Image No.')
           plt.title('The total Processing Time for Different Images')

        return object_matrix, time_matrix, image

    # function to extract object information from buffer if the user already asked, otherwise we activate cognitive system to detect

    def multiple_targetdetection(self,total_number,time_limit, question_sequence,  image, start_congnitivsystem):
        # initial question and answer list
        questionlist = []
        answer = []
        # check if there is no visual stimulus
        if start_congnitivsystem == 0:
            # check if the object from user question we haven't ask
            for i in question_sequence:
                if i not in questionlist:
                    return 'Number Unknown'
        objectinformation = []
        for i in question_sequence:
            # if we already have detected one specific object that mentioned in the user question
            if i in questionlist:
                # object information from buffer, not apply visual stimuli
                index = questionlist.index(i)
                answer.append(answer[index])

            # if we detect new objects we have never detected before
            else:
                objectinfo, time, image = self.whole_cognitivesystem(total_number,self.object_matrix,self.time_matrix,self.image_number,self.plot_flag,start_congnitivsystem, i, time_limit, image)

                answer.append(objectinfo[len(objectinfo) - 1])
            questionlist.append(i)
        print(answer)
        # return OBJECTDATA1
        return np.sum(answer), questionlist, answer, image

    #stroop effect simulation main function
    def stroop_effect_simulator(self):
        meaningless = []
        # keyword extraction
        keyword = check_question(self.user_command,self.object_information)
        keyword1 = check_question(self.user_command1,self.object_information)
        # deal with first example of visual stimuli
        process_time, index_stroop, judgement = stroop_effect_recognizer(self.stroop_visual_stimuli, keyword,meaningless,self.target_range)
        # deal with second example of visual stimuli
        process_time1, index_stroop1, judgement1 = stroop_effect_recognizer(self.stroop_visual_stimuli1, keyword,meaningless,self.target_range)
        # deal with task of reading color
        process_time2, index_stroop2, judgement2 = stroop_effect_recognizer(self.stroop_visual_stimuli, keyword1,meaningless,self.target_range)
        # deal with second example of visual stimuli
        process_time3, index_stroop3, judgement3 = stroop_effect_recognizer(self.stroop_visual_stimuli1, keyword1,meaningless,self.target_range)
        #visualize simulation results
        plot_final(process_time,index_stroop)
        plot_final(process_time1,index_stroop1)
        plot_final(process_time2,index_stroop2)
        plot_final(process_time3,index_stroop3)
        plt.show()
        x = np.arange(1, len(judgement) + 1)
        result1 = pd.DataFrame({'The ith visual stimuli': np.array(x), 'Judgement Result': np.array(judgement)})
        # final judgement for example stimuli set 2
        result2 = pd.DataFrame({'The ith visual stimuli': np.array(x), 'Judgement Result': np.array(judgement1)})
        # result
        result3 = pd.DataFrame({'The ith visual stimuli': np.array(x), 'Judgement Result': np.array(judgement2)})
        # final judgement for example stimuli set 2
        result4 = pd.DataFrame({'The ith visual stimuli': np.array(x), 'Judgement Result': np.array(judgement3)})
        print(result1, result2, result3, result4)

    # example of cognition with multiple question
    def example_multiple_function(self,total_number,image):

        # user question read
        user_question = ['How many gray circle are contained in this picture',
                         'How many yellow rectangle are contained in this picture']
        # object information array
        object_information = ['gray circle', 'red circle', 'black circle', 'yellow rectangle', 'gray rectangle',
                              'red polygon']
        question = check_question(user_question,object_information)
        number, questionlist, answer, image = self.multiple_targetdetection(total_number,self.time_limit, question,  image, self.start_congnitivsystem)
        # if user ask information of two or more types of objects simultaneously
        question_large = ['How many gray circle and red polygon (sum) are contained in the picture']

        # extract question information
        question_sequence = check_question(question_large,object_information)

        # obtain number of objects accoriding to this question
        number1, questionlist1, answer1, image = self.multiple_targetdetection(total_number,self.time_limit, question_sequence,  image, self.start_congnitivsystem)
        # final answer of question-question_large
        final = np.sum(answer1[len(answer1) - len(question_sequence):])

        # first question
        question_large1 = ['How many gray rectangle and red polygon (sum) are contained in the picture']

        # extract question information
        question_sequence1 = check_question(question_large1,object_information)

        # obtain number of objects accoriding to this question
        number2, questionlist2, answer2, image = self.multiple_targetdetection(total_number,self.time_limit, question_sequence1,  image, self.start_congnitivsystem)
        # second question
        question_large2 = ['How many black circle and red polygon (sum) are contained in the picture']
        # extract question information
        question_sequence2 = check_question(question_large2,object_information)
        # no visual stimulus applied for it
        start_congnitivsystem = 0
        # obtain number of objects accoriding to this question
        a = self.multiple_targetdetection(total_number,self.time_limit, question_sequence2,  image,
                                     start_congnitivsystem)
        final1 = np.sum(answer2[len(answer2) - len(question_sequence1):])
        return final,final1,a