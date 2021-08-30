# image array processing to get only one attribute for each object, which is essential to further processing with respect to form and
# color criteria
def image_arraytocolor(image):
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])

    # a flag to let system only recognize grouping objects once
    repeat = 0
    # initial number of groupings in terms of color criteria
    # only uniform shape of grouping objects are of consideration

    for i in range(nums):
        for j in range(rows):
            if image[i][j] == 'black circle':
                image[i][j] = 'black'
            if image[i][j] == 'red circle' or image[i][j] == 'red polygon':
                image[i][j] = 'red'
            if image[i][j] == 'gray rectangle' or image[i][j] == 'gray circle':
                image[i][j] = 'gray'
            if image[i][j] == 'yellow rectangle':
                image[i][j] = 'yellow'

    return image
# image array processing to get only one attribute for each object, which is essential to further processing with respect to form and
# color criteria
def image_arraytoform(image):
    # calculate the number of rows and columns of detected image
    nums, rows = len(image), len(image[0])

    # a flag to let system only recognize grouping objects once
    repeat = 0
    # initial number of groupings in terms of proximity criteria
    # only uniform shape of grouping objects are of consideration
    grouping_number = 0
    grouping_numberfinal = 0
    for i in range(nums):
        for j in range(rows):
            if image[i][j] == 'black circle' or image[i][j] == 'red circle' or image[i][j] == 'gray circle':
                image[i][j] = 'circle'

            if image[i][j] == 'gray rectangle' or image[i][j] == 'yellow rectangle':
                image[i][j] = 'rectangle'

            if image[i][j] == 'red polygon':
                image[i][j] = 'polygon'

    return image