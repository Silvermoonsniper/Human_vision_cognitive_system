# construct image data creation function to generate image data for cognitive system processing
import numpy as np


def imagdata_creation():

    # set image size randomly

    image = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
    red_polygon_number = np.random.randint(0, len(image[0]))
    gray_circle_number = np.random.randint(0, len(image[0]))
    red_circle_number = np.random.randint(0, len(image[0]))
    black_circle_number = np.random.randint(0, len(image[0]))
    gray_rectangle_number = np.random.randint(0, len(image[0]))
    yellow_rectangle_number = np.random.randint(0, len(image[0]))
    # total objects number
    total_number = red_polygon_number + gray_circle_number + red_circle_number + black_circle_number + gray_rectangle_number + yellow_rectangle_number
    # arbitraryly place colored geometric objects
    for i in range(red_polygon_number):
        l, k = np.random.randint(1, len(image[0])-1), np.random.randint(1, len(image)-1)
        image[k][l] = 'red ploygon'
        red_polygon_number -= 1
    for i in range(red_circle_number):
        # arbitraryly place colored geometric objects
        l, k = np.random.randint(1, len(image[0])-1), np.random.randint(1, len(image)-1)
        image[k][l] = 'red circle'
        red_circle_number -= 1
    for i in range(black_circle_number):
        # arbitraryly place colored geometric objects
        l, k = np.random.randint(1, len(image[0])-1), np.random.randint(1, len(image)-1)
        image[k][l] = 'black circle'
        black_circle_number -= 1
    for i in range(gray_circle_number):
        # arbitraryly place colored geometric objects
        l, k = np.random.randint(1, len(image[0])-1), np.random.randint(1, len(image)-1)
        image[k][l] = 'gray circle'
        gray_circle_number -= 1
    for i in range(gray_rectangle_number):
        # arbitraryly place colored geometric objects
        l, k = np.random.randint(1, len(image[0])-1), np.random.randint(1, len(image)-1)
        image[k][l] = 'gray rectangle'
        gray_rectangle_number -= 1
    for i in range(yellow_rectangle_number):
        # arbitraryly place colored geometric objects
        l, k = np.random.randint(1, len(image[0])-1), np.random.randint(1, len(image)-1)
        image[k][l] = 'yellow rectangle'
        yellow_rectangle_number -= 1

    return image, total_number