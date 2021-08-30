# obscured object function
validinfo = ['gray circle', 'red circle', 'black circle', 'yellow rectangle', 'gray rectangle', 'red polygon', '_'];


def obscured_object_detection(image, total_number, time_limit):
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])
    # set initial detection time
    detection_time = 0
    a = 1
    b = 1
    obscured_object_line_number = 0
    obscured_obejct_square_number = 0

    if (detection_time <= time_limit):
        for i in range(nums):
            for j in range(rows):
                # judge if the object is obscured object
                if image[i][j] not in validinfo:
                    # judge if the object is line-like
                    # case1 vertical line
                    if image[i + 1][j] not in validinfo and image[i][j + 1] in validinfo and image[i][
                        j - 1] in validinfo and flag == 0:

                        while image[i + a][j] in validinfo and image[i][j + 1] not in validinfo:
                            a += 1

                        obscured_object_line_number += 1
                        # processing time
                        detection_time1 = 5 * a
                        # overall detection time
                        detection_time = detection_time + detection_time1
                        a = 1
                        # set flag to stop counting grouping obstacles that belong to identical grouping
                        flag = 1
                else:
                    flag = 0
                # judge if the object is obscured object
                if image[i][j] not in validinfo:
                    # case2 horizontal line
                    if image[i + 1][j] in validinfo and image[i][j + 1] not in validinfo and image[i - 1][
                        j] in validinfo and flag == 0:

                        while image[i + 1][j] not in validinfo and image[i][j + b] in validinfo:
                            b += 1

                        obscured_object_line_number += 1
                        # processing time
                        detection_time1 = 5 * b
                        # overall detection time
                        detection_time = detection_time + detection_time1
                        # set flag to stop counting grouping obstacles that belong to identical grouping

                        b = 1
                        flag = 1
                else:
                    flag = 0
                # judge if the object is obscured object
                if image[i][j] not in validinfo:
                    # judge if the objects is square-like
                    if image[i + 1][j] not in validinfo and image[i][j + 1] not in validinfo and flag == 0:
                        while image[i + a][j] not in validinfo and image[i][j + b] not in validinfo:
                            a += 1
                            b += 1
                        obscured_obejct_square_number += 1
                        detection_time1 = 5 * (a + b)
                        # overall detection time
                        detection_time = detection_time + detection_time1
                        a = 1
                        b = 1
                        # set flag to stop counting grouping obstacles that belong to identical grouping
                        flag = 1
                else:
                    flag = 0
        # if there is no obscured obejct
        if obscured_object_line_number == 0 and obscured_obejct_square_number == 0:
            detection_time = 30

    else:
        raise('detection time is exceeded')

    return obscured_object_line_number, obscured_obejct_square_number