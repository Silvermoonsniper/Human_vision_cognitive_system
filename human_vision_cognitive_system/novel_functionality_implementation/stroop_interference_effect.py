import  numpy as np
# visual stimuli processor
def visual_stimuli_processor(stroop_visual_stimuli,target_range):
    aa = []
    bb = []
    # array to store matched and unmatched visual stimuli(match means if word matches its printed color)
    correspond_stimuli = []
    noncorrespond_stimuli = []
    meaningless = []
    flag = 1
    for i in stroop_visual_stimuli:
        for j in range(len(i)):
            # read through the information of visual stimuli sequentially, acooridng to human vision mechanisim, we prefer read
            # from left to right

            if i[j] != '_' and flag == 1:
                aa.append(i[j])
            else:
                flag = 0
                if i[j] != '_':
                    bb.append(i[j])
        flag = 1
        # check if they are matched
        # case 1: if word meaning is exactly its printed color
        # case 2: if word meaning has no relation to printed color, clean, dry etc.

        if aa == bb:
            correspond_stimuli.append(i)
        # if not matched
        else:
            noncorrespond_stimuli.append(i)
        if aa != bb and ''.join(aa) not in target_range:
            correspond_stimuli.append(i)
            meaningless.append(i)

        # get rid of existing information in compared array aa and bb, which stores word and printed color for targeted visual stimuli

        aa = []
        bb = []

    return correspond_stimuli, noncorrespond_stimuli


# input parameter:
# stroop_visual_stimuli:visual stimuli with word meaning and its printed color
# output parameters:
# judgement:array for storing recognization result for each visual stimuli
# process_time: process time to recognize printed color of each visual
# index.stroop: index of visual stimuli occurs stroop interference
def stroop_effect_recognizer(stroop_visual_stimuli, keyword,meaningless,target_range):
    # recognize matched and unmatched stimulis:
    correspond_stimuli, noncorrespond_stimuli = visual_stimuli_processor(stroop_visual_stimuli,target_range)
    print(correspond_stimuli, noncorrespond_stimuli)
    # initial processing time(unit:us)
    process_time = []
    # metrc array to store flag indicating if recgonization is correct or not at a given visual stimuli
    judgement = []
    # initial occuring times of stroop effect
    stroop_effect_number = 0
    # initial index array
    index_stroop = []
    # loop over all visual stimulis；
    for i in stroop_visual_stimuli:
        # if we wanna participants to read the word from visual stimulis
        if keyword == ['word meaning']:

            # process faster if there is no interference ocurrs(word meaning matches printed color)
            if i in correspond_stimuli:
                # check if the word is color names
                if i not in meaningless:
                    # human processing time to recognize printed color, usually random
                    process_time.append(np.random.randint(30, 40))
                    # correct recognization, no stroop interference occurs
                    judgement.append('True')
                # if the word is neutral no relation to color, reaction time is increased
                else:
                    # human processing time to recognize printed color, usually random
                    process_time.append(np.random.randint(45, 55))
                    # correct recognization, no stroop interference occurs
                    judgement.append('True')
            else:
                # now there are two possible situations for stroop interference effect, one is prolonged processing time, the other one is
                # wrong recognization
                # record the times occuring stroop effect
                stroop_effect_number += 1

                # correct recognization,stroop interference occurs
                if stroop_effect_number % 4 != 0:
                    judgement.append('True')
                    process_time.append(np.random.randint(60, 70))
                    # record the element index of visual stimuli array that occur stroop interference
                    index_stroop.append(len(process_time) - 1)

                # there is a certain frequency that stroop effect occurs that lead to wrong recognization
                if stroop_effect_number % 4 == 0:
                    judgement.append('False')
                    # append processing time
                    process_time.append(np.random.randint(60, 70))
                    # record the element index of visual stimuli array that occur stroop interference
                    index_stroop.append(len(process_time) - 1)
            # if we wanna participants to read the printed color from visual stimulis
        if keyword == ['printed color']:

            # process faster if there is no interference ocurrs(word meaning matches printed color)
            if i in correspond_stimuli:
                # check if the word is color names
                if i not in meaningless:
                    # human processing time to recognize printed color, usually random,read color needs more attention compared with reading word
                    process_time.append(np.random.randint(40, 50))
                    # correct recognization, no stroop interference occurs
                    judgement.append('True')
                # if the word is neutral no relation to color, reaction time is increased
                else:
                    # human processing time to recognize printed color, usually random
                    process_time.append(np.random.randint(55, 65))
                    # correct recognization, no stroop interference occurs
                    judgement.append('True')
            else:

                # now there are two possible situations for stroop interference effect, one is prolonged processing time, the other one is
                # wrong recognization

                # record the times occuring stroop effect
                stroop_effect_number += 1

                # correct recognization,stroop interference occurs
                if stroop_effect_number % 4 != 0:
                    judgement.append('True')
                    process_time.append(np.random.randint(70, 80))
                    # record the element index of visual stimuli array that occur stroop interference
                    index_stroop.append(len(process_time) - 1)

                # there is a certain frequency that stroop effect occurs that lead to wrong recognization
                if stroop_effect_number % 4 == 0:
                    judgement.append('False')
                    # append processing time
                    process_time.append(np.random.randint(70, 80))
                    # record the element index of visual stimuli array that occur stroop interference
                    index_stroop.append(len(process_time) - 1)
    return process_time, index_stroop, judgement