# This is a simple cognitive visual system, as it sets colored-geometric image time limitation and user question as input and realize the function of
# distinguishing specific geometic objects in the image.
# the individual results can be added up and therefore we can retriveal information from buffer to get answer to new question, if user
# mentions it. The grouping objects can be detccted and processed fasstly, instead of counting them individually.


import numpy as np

import matplotlib.pyplot as plt
from PIL import Image

# second part, improved detector for grouping elements
image = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'gray circle', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', 'red polygon', 'red polygon', 'red polygon', '_', '_', '_', '_', '_', '_',
          'gray circle', '_'],
         ['_', '_', '_', '_', '_', 'red polygon', 'red polygon', 'red polygon', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', 'red polygon', 'red polygon', 'red polygon', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'red polygon', '_', '_', '_', '_'],
         ['_', 'gray rectangle', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'gray rectangle', '_', '_', '_'],
         ['_', '_', '_', '_', '_', 'gray rectangle', 'gray rectangle', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', 'gray rectangle', 'gray rectangle', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', 'red circle', '_', '_', '_', '_', '_', '_', 'yellow rectangle', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', 'black circle', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', 'red circle', '_', '_', '_', '_', '_', '_']]
# Shape detection unit that distinguish shape of object

# rectangle_detection function
def rectangle_detection_1(image, total_number, time_limit):
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0
    a = 1
    b = 1
    # initial rectangle number
    rectangle_number = 0
    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                if image[i][j] == 'yellow rectangle':
                    # judge whther it belongs to grouping elements
                    if image[i + 1][j] == 'yellow rectangle' or image[i - 1][j] == 'yellow rectangle' or image[i][
                        j - 1] == 'yellow rectangle' or image[i][j + 1] == 'yellow rectangle':
                        # search by edge to determine number of grouping objects

                        while (image[i + a][j] == 'yellow rectangle' or image[i][j + b] == 'yellow rectangle'):

                            if image[i + a][j] == 'yellow rectangle':
                                a += 1
                            if image[i][j + b] == 'yellow rectangle':
                                b += 1
                        # calculate number of grouping elements
                        grouping_number = a * b

                        rectangle_number = grouping_number
                        # calculate processing time
                        detection_time = 5 * (a + b)
                        # update i and j

                    # if not belongs to grouping elements
                    else:
                        rectangle_number += 1
                        # add detection basis time,unit；ms
                        detection_time += 50 + 2 * total_number
                else:

                    # add detection basis time,unit；ms
                    detection_time += 0
        # if there is no detected objects, add a basic cognitive processing time(ms)
        if rectangle_number == 0:
            detection_time = 30
    else:
        raise('detection time is exceeded')

    return rectangle_number, detection_time


# rectangle_detection function
def rectangle_detection_2(image, total_number, time_limit):
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0
    a = 1
    b = 1
    rectangle_number = 0
    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                if image[i][j] == 'gray rectangle':
                    # judge whther it belongs to grouping elements
                    if image[i + 1][j] == 'gray rectangle' or image[i - 1][j] == 'gray rectangle' or image[i][
                        j - 1] == 'gray rectangle' or image[i][j + 1] == 'gray rectangle':
                        # search by edge to determine number of grouping objects

                        while (image[i + a][j] == 'gray rectangle' or image[i][j + b] == 'gray rectangle'):

                            if image[i + a][j] == 'gray rectangle':
                                a += 1
                            if image[i][j + b] == 'gray rectangle':
                                b += 1
                        # calculate number of grouping elements
                        grouping_number = a * b

                        rectangle_number = grouping_number
                        # calculate processing time
                        detection_time = 5 * (a + b)
                        # update i and j

                    # if not belongs to grouping elements
                    else:
                        rectangle_number += 1
                        # add detection basis time,unit；ms
                        detection_time += 50 + 2 * total_number
                else:

                    # add detection basis time,unit；ms
                    detection_time += 0
        # if there is no detected objects, add a basic cognitive processing time(ms)
        if rectangle_number == 0:
            detection_time = 30
    else:
        raise('detection time is exceeded')

    return rectangle_number, detection_time


# circle_detection function
def circle_detection_1(image, total_number, time_limit):
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0
    a = 1
    b = 1
    # initial circle number
    circle_number = 0
    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                if image[i][j] == 'gray circle':
                    # judge whther it belongs to grouping elements
                    if image[i + 1][j] == 'gray circle' or image[i - 1][j] == 'gray circle' or image[i][
                        j - 1] == 'gray circle' or image[i][j + 1] == 'gray circle':
                        # search by edge to determine number of grouping objects

                        while (image[i + a][j] == 'gray circle' or image[i][j + b] == 'gray circle'):

                            if image[i + a][j] == 'gray circle':
                                a += 1
                            if image[i][j + b] == 'gray circle':
                                b += 1
                        # calculate number of grouping elements
                        grouping_number = a * b

                        circle_number = grouping_number
                        # calculate processing time
                        detection_time = 5 * (a + b)
                        # update i and j

                    # if not belongs to grouping elements
                    else:
                        circle_number += 1
                        # add detection basis time,unit；ms
                        detection_time += 50 + 2 * total_number

                else:
                    # add detection basis time,unit；ms
                    detection_time += 0
                    # if there is no detected objects, add a basic cognitive processing time(ms)
        if circle_number == 0:
            detection_time = 30
    else:
        raise('detection time is exceeded')

    return circle_number, detection_time


# circle_detection function
def circle_detection_2(image, total_number, time_limit):
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0
    a = 1
    b = 1
    # initial circle number
    circle_number = 0
    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                if image[i][j] == 'red circle':
                    # judge whther it belongs to grouping elements
                    if image[i + 1][j] == 'red circle' or image[i - 1][j] == 'red circle' or image[i][
                        j - 1] == 'red circle' or image[i][j + 1] == 'red circle':
                        # search by edge to determine number of grouping objects

                        while (image[i + a][j] == 'red circle' or image[i][j + b] == 'red circle'):

                            if image[i + a][j] == 'red circle':
                                a += 1
                            if image[i][j + b] == 'red circle':
                                b += 1
                        # calculate number of grouping elements
                        grouping_number = a * b

                        circle_number = grouping_number
                        # calculate processing time
                        detection_time = 5 * (a + b)
                        # update i and j

                    # if not belongs to grouping elements
                    else:

                        circle_number += 1
                        # add detection basis time,unit；ms
                        detection_time += 50 + 2 * total_number
                else:

                    # add detection basis time,unit；ms
                    detection_time += 0
                    # #if there is no detected objects, add a basic cognitive processing time(ms)
        if circle_number == 0:
            detection_time = 30
    else:
        raise('detection time is exceeded')
    return circle_number, detection_time


# circle_detection function
def circle_detection_3(image, total_number, time_limit):
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0
    a = 1
    b = 1
    # initial circle number
    circle_number = 0
    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                if image[i][j] == 'black circle':

                    # judge whther it belongs to grouping elements
                    if image[i + 1][j] == 'black circle' or image[i - 1][j] == 'black circle' or image[i][
                        j - 1] == 'black circle' or image[i][j + 1] == 'black circle':
                        # search by edge to determine number of grouping objects

                        while (image[i + a][j] == 'black circle' or image[i][j + b] == 'black circle'):

                            if image[i + a][j] == 'black circle':
                                a += 1
                            if image[i][j + b] == 'black circle':
                                b += 1
                        # calculate number of grouping elements
                        grouping_number = a * b

                        circle_number = grouping_number
                        # calculate processing time
                        detection_time = 5 * (a + b)
                        # update i and j

                    # if not belongs to grouping elements
                    else:
                        circle_number += 1
                        # add detection basis time,unit；ms
                        detection_time += 50 + 2 * total_number
                else:

                    # add detection basis time,unit；ms
                    detection_time += 0
        # if there is no detected objects, add a basic cognitive processing time(ms)
        if circle_number == 0:
            detection_time = 30
    else:
        raise('detection time is exceeded')

    return circle_number, detection_time


# circle_detection function
def polygon_detection(image, total_number, time_limit):
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0

    # initial polygon number
    polygon_number = 0
    a = 1
    b = 1
    group_flag = 1
    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                if image[i][j] == 'red polygon':
                    # judge whther it belongs to grouping elements
                    if image[i + 1][j] == 'red polygon' or image[i - 1][j] == 'red polygon' or image[i][
                        j - 1] == 'red polygon' or image[i][j + 1] == 'red polygon':
                        # search by edge to determine number of grouping objects

                        while (image[i + a][j] == 'red polygon' or image[i][j + b] == 'red polygon'):

                            if image[i + a][j] == 'red polygon':
                                a += 1
                            if image[i][j + b] == 'red polygon':
                                b += 1
                            group_flag = 0
                        # calculate number of grouping elements
                        grouping_number = a * b

                        polygon_number = grouping_number
                        # calculate processing time
                        detection_time = 5 * (a + b)
                        # update i and j

                    # if not belongs to grouping elements
                    else:
                        polygon_number += 1
                        # add detection basis time,unit；ms
                        detection_time += 50 + 2 * total_number
                else:

                    # add detection basis time,unit；ms
                    detection_time += 0
        # if there is no detected objects, add a basic cognitive processing time(ms)
        if polygon_number == 0:
            detection_time = 30
    else:
        raise('detection time is exceeded')

    return (polygon_number, detection_time)