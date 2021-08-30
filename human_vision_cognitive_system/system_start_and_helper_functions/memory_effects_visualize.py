import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from novel_functionality_implementation.memory_effects import memory_effect_simulator


def memory_effects_visualize(word_list, question_list,object_information):
    results, answer, answer1 = memory_effect_simulator(word_list, question_list,object_information)
    results = np.reshape(results, [len(question_list), len(word_list)])
    x = np.arange(1, len(word_list) + 1)
    df = pd.DataFrame({'x': range(1, 11), 'question 1': results[0], 'question 2': results[1], 'question 3': results[2],
                       'question 4': results[3], 'question 5': results[4], 'question 6': results[5],
                       'question 7': results[6], 'question 8': results[7]})

    # multiple line plot
    plt.plot('x', 'question 1', data=df, marker='o', linewidth=2)
    plt.plot('x', 'question 2', data=df, marker='o', linewidth=2)
    plt.plot('x', 'question 3', data=df, marker='o', linewidth=2)
    plt.plot('x', 'question 4', data=df, marker='o', linewidth=2)
    plt.plot('x', 'question 5', data=df, marker='o', linewidth=2)
    plt.plot('x', 'question 6', data=df, marker='o', linewidth=2)
    plt.plot('x', 'question 7', data=df, marker='o', linewidth=2)
    plt.plot('x', 'question 8', data=df, marker='o', linewidth=2)
    plt.xlabel('The ith Word')
    plt.ylabel('Reaction Time')
    plt.legend()
    # Data
    plt.title('reaction time for each question with words(unit:us)')
    plt.show()