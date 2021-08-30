# Third assignement a more complicated version of visual cognitive system is constructed
# function to detect number of groupings according to criteria of proximity
# input parameter: image visual stimulis
def proximity_judge(image, total_number, time_limit):
    # regardless of form and color of objects and therefore visual recognition should be put to every object
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0
    a = 1
    b = 1
    # a flag to let system only recognize grouping objects once
    repeat = 0
    grouping_numberfinal = 0
    # initial number of groupings in terms of proximity criteria
    # only uniform shape of grouping objects are of consideration
    grouping_number = 0
    already_check = []
    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                # if visual sensor focus on one object

                if image[i][j] != '_':
                    already_check.append([i, j])
                    # search rightwards and downwards to determine number of grouping objects
                    # if we focus on objects on the edge of picture
                    if image[i + 1][j] != '_' or image[i - 1][j] != '_' or image[i][j - 1] != '_' or image[i][
                        j + 1] != '_':
                        # search by edge to determine number of grouping objects
                        if [i + 1, j] not in already_check and [i - 1, j] not in already_check and [i,
                                                                                                    j + 1] not in already_check and [
                            i, j - 1] not in already_check:
                            if i + a <= nums - 1 and j + b <= rows - 1 and repeat == 0:
                                while (image[i + a][j] != '_' or image[i][j + b] != '_'):
                                    if image[i + a][j] != '_':
                                        a += 1
                                        # update number of groupings and proceed to recognize next groupings
                                        grouping_number = 1
                                        repeat += 1
                                    if image[i][j + b] != '_':
                                        b += 1
                                        # update number of groupings and proceed to recognize next groupings
                                        grouping_number = 1
                                        repeat += 1

                                grouping_numberfinal = grouping_numberfinal + grouping_number
                                # calculate number of grouping elements
                                grouping_objects = a * b

                                # calculate processing time
                                detection_time = 5 * (a + b)


                # it means we move to cell without object
                else:
                    repeat = 0
                    a = 1
                    b = 1
        # if there is no grouping objects, add a basic cognitive processing time(ms)
        if grouping_number == 0:
            detection_time = 30
    # if we exceeds time limitation
    else:
        raise('detection time is exceeded')
    return grouping_numberfinal





# function to judge the number of groupings according to criteria of form similarity
def form_judge(image, total_number, time_limit):
    # firstly we need to check whether two objects are in distance 1 that fulfills criteria of proximity similarity
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0
    a = 1
    b = 1
    # a flag to let system only recognize grouping objects once
    repeat = 0
    # initial number of groupings in terms of form criteria
    # only uniform shape of grouping objects are of consideration
    grouping_number = 0
    number = []
    grouping_numberfinal = 0
    already_check = []
    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                # if visual sensor focus on one object

                if image[i][j] != '_':
                    # search rightwards and downwards to determine number of grouping objects
                    # if we focus on objects on the edge of picture
                    already_check.append([i, j])
                    # print(i,j)
                    if image[i + 1][j] != '_' or image[i - 1][j] != '_' or image[i][j - 1] != '_' or image[i][
                        j + 1] != '_':

                        # if [i+1,j] not in already_check and [i-1,j] not in already_check and [i,j+1] not in already_check and [i,j-1] not in already_check:
                        # judge if these neighbour objects are with same form

                        if i + a <= nums - 1 and j + b <= rows - 1:
                            k = 1
                            while image[i + a][j] == image[i][j] or image[i][j + b] == image[i][j]:

                                # array to append first detected position of grouping elements
                                if k == 1:
                                    number.append([i, j])
                                k -= 1

                                if image[i + a][j] == image[i][j] or image[i][j + b] == image[i][j]:
                                    # update number of groupings and proceed to recognize next groupings
                                    grouping_number = 1
                                    repeat += 1
                                if image[i + a][j] == image[i][j]:
                                    a += 1
                                # print(a,image[i][j])

                                if image[i][j + b] == image[i][j]:
                                    b += 1
                                    # print(b,image[i][j])

                        grouping_numberfinal = grouping_numberfinal + grouping_number

                        # print(grouping_number,image[i][j])

                        detection_time = 5 * (a + b)




                # it means we move to cell without object
                else:
                    repeat = 0
                    a = 1
                    b = 1

    return len(number)


# function to judge according to the criteria of color similarity







# function to judge the number of groupings according to criteria of form similarity
def color_judge(image, total_number, time_limit):
    # firstly we need to check whether two objects are in distance 1 that fulfills criteria of proximity similarity
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0
    a = 1
    b = 1
    # a flag to let system only recognize grouping objects once
    repeat = 0
    # initial number of groupings in terms of proximity criteria
    # only uniform shape of grouping objects are of consideration
    grouping_number = 0
    grouping_numberfinal = 0
    number = []
    already_check = []
    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                # if visual sensor focus on one object

                if image[i][j] != '_':
                    # search rightwards and downwards to determine number of grouping objects
                    # if we focus on objects on the edge of picture
                    already_check.append([i, j])
                    # check if its grouping objects

                    # if we focus on objects on the edge of picture
                    if image[i + 1][j] != '_' or image[i - 1][j] != '_' or image[i][j - 1] != '_' or image[i][
                        j + 1] != '_':
                        # search by edge to determine number of grouping objects
                        # if [i+1,j] not in already_check and [i-1,j] not in already_check and [i,j+1] not in already_check and [i,j-1] not in already_check:

                        # search rightwards and downwards to determine number of grouping objects

                        # check it we already look at the boundary of image
                        if i + a <= nums - 1 and j + b <= rows - 1:
                            k = 1
                            while image[i + a][j] == image[i][j] or image[i][j + b] == image[i][j]:

                                # array to append first detected position of grouping elements
                                if k == 1:
                                    number.append([i, j])
                                k -= 1
                                if image[i + a][j] == image[i][j] or image[i][j + b] == image[i][j]:
                                    # update number of groupings and proceed to recognize next groupings
                                    grouping_number = 1
                                    repeat += 1
                                if image[i + a][j] == image[i][j]:
                                    a += 1
                                # print(a,image[i][j])

                                if image[i][j + b] == image[i][j]:
                                    b += 1
                                    # print(b,image[i][j])
                            a = 1
                            b = 1

                            grouping_numberfinal = len(number)

                            detection_time = 5 * (a + b)
                # it means we move to cell without object
                else:
                    repeat = 0
                    a = 1
                    b = 1

    return grouping_numberfinal