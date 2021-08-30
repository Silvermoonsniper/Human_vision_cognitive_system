# plot result function
import numpy as np
import matplotlib.pyplot as plt
def plot_final(process_time,index_stroop):
    x = np.arange(1, len(process_time) + 1)
    legend_array = ['No Stroop Effect', 'Stroop Effect Occurs']
    fig, ax = plt.subplots()

    for i in range(len(process_time)):
        if i not in index_stroop:

            plt.scatter(x[i], process_time[i], label='No Stroop Effect', color='red')

        else:
            plt.scatter(x[i], process_time[i], label='Stroop Effect Occurs', color='blue')
    ax.legend(loc='right', bbox_to_anchor=(1, 0.25, 0.5, 0.5))
    plt.title('Processing time of Each Visual Stimuli')
    plt.xlabel('The number of visual stimuli')
    plt.ylabel('processing time (us)')