import numpy as np
# deal with user questions sequentially



def check_question(user_question,object_information):
    aa = []
    for i in user_question:
        for j in range(len(i)):
            # extract specific object information from user question
            for a in range(len(i)):
                if i[j:j + a] in object_information:
                    aa.append(i[j:j + a])
    return aa


# apply viusal stimuli
questionlist = []
answer = []
plot_flag = 0
#function to distinguish different level of questions
#input parameter: questionlist
#output paramter: binary sequence to indicate different level of questions

def question_recognizer(question_list,object_information):
    aa=[]
    for i in question_list:
        for j in range(len(i)):
        #extract specific object information from user question
             for a in range(len(i)):
                #check if it is semantic question
                 if i[j:j+a] ==object_information[0]:
                        aa.append(1)
                #else its a physical aspect question
                 elif i[j:j+a] ==object_information[1]:
                        aa.append(0)
    return aa

