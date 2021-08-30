from numpy import linalg as LA
import numpy as np
#vectorial representation of word
#regarding different aspects: [plant, animal, short word, long word, electronical product, nonelectronic product,captial, noncapital], if
#one word fulfills one attributes, we assign 1, otherwise assgn 0
plant=['tree','TREE','flower']
clothes=['hoodie','garment','JEANS']
animal=['elephant','butterfly']
captial=['TREE','JEANS']
electronic_product=['cellphone','headphone']
def vectorial_transformer(word_list):
    #loop over all words
    a=[]
    for i in word_list:
        if i in plant:
            a.append(np.random.uniform(0,1))
        else:
            a.append(0)
        if i in clothes:
            a.append(np.random.uniform(0,1))
        else:
            a.append(0)
        if i in electronic_product:
            a.append(np.random.uniform(0,1))
        else:
            a.append(0)
        if i in animal:
            a.append(np.random.uniform(0,1))
        else:
            a.append(0)
        if i in captial:
            a.append(np.random.uniform(0,1))
        else:
            a.append(0)
        if len(i)>=5:
            a.append(np.random.uniform(0,1))
        else:
            a.append(0)
    a=np.reshape(a,[6,len(word_list)])
    return a


# function to calculate similarity of word or question
def similarity_check(input_sample1, input_sample2):
    decay_parameter = 0.21
    # calculate norm of vector difference
    vector_distance = LA.norm(input_sample1 - input_sample2)

    # similarity representation between two word vector
    similarity = np.exp(-decay_parameter * vector_distance)
    return similarity


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
# function to simulate memory effect
# input parameter: word list and question list
def memory_effect_simulator(word_list, question_list,object_information):
    a = vectorial_transformer(word_list)
    b = question_recognizer(question_list,object_information)
    reaction_time = []
    similar = []
    answer = []
    answer1 = []
    sum_similarities = []
    sum_similarities1 = []
    print(len(question_list), len(word_list))
    for i in b:
        # it's a semantic question
        if i == 1:
            # one question is asked for different words

            for j in range(len(word_list)):
                # process first word, no memory
                if j < 1:
                    reaction_time.append(np.random.uniform(70, 75))
                    if j % 4 == 0:
                        answer.append(1)
                    else:
                        answer.append(0)
                # retrivel memory
                if j >= 1:
                    for k in range(j):
                        # sum up all similarities with respect to all words that have been asked
                        # single_similar=similarity_check(a[:,j],a[:,k])
                        sum_similarities.append(np.array(similarity_check(a[:, j], a[:, k])))
                    if j % 2 == 0:
                        answer.append(1)
                    else:
                        answer.append(0)
                    # append reaction time
                    reaction_time.append(np.random.uniform(70, 75) / np.array(np.sum(sum_similarities)))
            sum_similarities = []
            # it's a physical aspect question
        elif i == 0:
            # one question is asked for different words
            for j in range(len(word_list)):
                # process first word, no memory
                if j < 1:
                    reaction_time.append(np.random.uniform(40, 45))
                    if j % 2 == 0:
                        answer1.append(1)
                    else:
                        answer1.append(0)
                # retrivel memory
                if j >= 1:
                    for k in range(j):
                        # sum up all similarities with respect to all words that have been asked
                        sum_similarities1.append(np.array(similarity_check(a[:, j], a[:, k])))
                    # append reaction time

                    reaction_time.append(np.random.uniform(40, 45) / np.array(np.sum(sum_similarities1)))
                if j % 2 == 0:
                    answer1.append(1)
                else:
                    answer1.append(0)
            sum_similarities1 = []

    return reaction_time, answer, answer1