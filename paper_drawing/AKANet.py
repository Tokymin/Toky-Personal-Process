import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
def box_plot():
    rcParams['font.family'] = 'serif'
    rcParams['font.serif'] = ['Times New Roman']
    # Data from the table
    models = ['Baseline (L2-Net)', 'BF', 'AKANet no pretrained', 'AKANet with pretrained']
    pretrain = ['N', '-', 'N', 'Y']
    finetune = ['N', 'Y', '-', '-']
    ate_mean = [3.60, 2.81, 2.08, 1.26]
    ate_std = [1.60, 1.62, 1.79, 0.79]
    rmse_mean = [4.34, 4.15, 3.97, 3.73]
    rmse_std = [0.90, 1.12, 1.41, 1.48]

    # Plotting
    fig, ax = plt.subplots(2, 1, figsize=(10, 12))

    # ATE Plot
    ax[0].bar(models, ate_mean, yerr=ate_std, capsize=5, color=['blue', 'orange', 'green', 'red'])
    ax[0].set_title('Impact of Pretrain and Fine-tune on ATE')
    ax[0].set_ylabel('ATE (mm)')
    ax[0].set_ylim(0, max(ate_mean) + 2)

    # RMSE Plot
    ax[1].bar(models, rmse_mean, yerr=rmse_std, capsize=5, color=['blue', 'orange', 'green', 'red'])
    ax[1].set_title('Impact of Pretrain and Fine-tune on RMSE')
    ax[1].set_ylabel('RMSE (mm)')
    ax[1].set_ylim(0, max(rmse_mean) + 2)

    # Adding text for pretrain and finetune
    for i in range(len(models)):
        ax[0].text(i, ate_mean[i] + 0.5, f'Pretrain: {pretrain[i]}\nFinetune: {finetune[i]}', ha='center')
        ax[1].text(i, rmse_mean[i] + 0.5, f'Pretrain: {pretrain[i]}\nFinetune: {finetune[i]}', ha='center')

    plt.tight_layout()
    plt.show()


def stacked_bar():
    rcParams['font.family'] = 'serif'
    fontsize=16
    rcParams['font.size'] = 24  # Set the default font size to 16
    rcParams['font.serif'] = ['Times New Roman']
    # Data from the table
    models = ['Baseline', 'BF', 'AKANet-1', 'AKANet-2']
    pretrain = ['×', '-', '×', '√']
    finetune = ['×', '√', '-', '-']
    ate_mean = [3.60, 2.81, 2.08, 1.26]
    ate_std = [1.60, 1.62, 1.79, 0.48]
    rmse_mean = [4.34, 4.15, 3.97, 3.73]
    rmse_std = [0.90, 1.12, 1.41, 1.48]

    x = np.arange(len(models))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(12, 8))

    # Set custom colors
    ate_color = (254 / 255, 194 / 255, 46 / 255)
    rmse_color = (41 / 255, 124 / 255, 246 / 255)

    rects1 = ax.bar(x - width / 2, ate_mean, width, yerr=ate_std, label='ATE', capsize=5, color=ate_color,
                    edgecolor='black')
    rects2 = ax.bar(x + width / 2, rmse_mean, width, yerr=rmse_std, label='RMSE', capsize=5, color=rmse_color,
                    edgecolor='black')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Models')
    ax.set_ylabel('Values')
    ax.set_title('Impact of Pretrain and Fine-tune on ATE and RMSE')
    ax.set_xticks(x)
    ax.set_xticklabels(models)
    ax.legend()  # loc='upper right' Fix the legend to the upper right corner

    # Adding annotations for pretrain and finetune
    for i in range(len(models)):
        ax.text(x[i] - width / 2, ate_mean[i] + 0.3, f'Pretrain: {pretrain[i]}\nFinetune: {finetune[i]}', ha='center',
                va='bottom')
        ax.text(x[i] + width / 2, rmse_mean[i] + 0.3, f'Pretrain: {pretrain[i]}\nFinetune: {finetune[i]}', ha='center',
                va='bottom')

    fig.tight_layout()

    plt.savefig("/Users/mintan/PycharmProjects/Toky-Personal-Process/DataFiles/pdfs/sec5-impact_of_pretrain_and_finetune.pdf", format='pdf')
    plt.show()


def color_bar_plot():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.colors import Normalize

    # New data
    ate_values = np.array([
        [0.2568, 0.4594, 0.3545, 0.3521],
        [0.4895, 0.4521, 0.2649, 0.3215],
        [0.4189, 0.3951, 0.2351, 0.1480],
        [0.3251, 0.4156, 0.4514, 0.4124]
    ])

    # Set up the figure and axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Define the position of the bars
    _x = np.arange(ate_values.shape[1])
    _y = np.arange(ate_values.shape[0])
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    # Define the top and bottom of the bars
    top = ate_values.ravel()
    bottom = np.zeros_like(top)
    width = depth = 1

    # Plot the bars with gradient color
    cmap = plt.get_cmap('viridis')
    norm = Normalize(vmin=np.min(top), vmax=np.max(top))

    for i in range(len(x)):
        rgba = cmap(norm(top[i]))
        ax.bar3d(x[i], y[i], bottom[i], width, depth, top[i], shade=True, color=rgba, edgecolor='k', alpha=0.8)

    # Rotate the view
    ax.view_init(elev=30, azim=210)

    # Labels and ticks
    ax.set_xlabel('Window size')
    ax.set_ylabel('Heads')
    ax.set_zlabel('Mean(cm)')
    ax.set_xticks(_x + width / 2)
    ax.set


def curve3D():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # New data
    ate_values = np.array([
        [0.2568, 0.4594, 0.3545, 0.3521],
        [0.4895, 0.4521, 0.2649, 0.3215],
        [0.4189, 0.3951, 0.2351, 0.1480],
        [0.3251, 0.4156, 0.4514, 0.4124]
    ])

    # Define the grid
    _x = np.arange(1, ate_values.shape[1] + 1)
    _y = np.arange(1, ate_values.shape[0] + 1)
    _xx, _yy = np.meshgrid(_x, _y)

    # Create the figure
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface
    surf = ax.plot_surface(_xx, _yy, ate_values, cmap='viridis', edgecolor='k', alpha=0.8)

    # Find the minimum value and its position
    min_val = np.min(ate_values)
    min_pos = np.unravel_index(np.argmin(ate_values), ate_values.shape)
    min_x, min_y = min_pos[1] + 1, min_pos[0] + 1  # Adjust for 1-based indexing

    # Annotate the minimum point
    ax.scatter(min_x, min_y, min_val, color='red', s=100)
    ax.text(min_x, min_y, min_val, f'({min_x}, {min_y})', color='red', fontsize=12, weight='bold')

    # Labels and ticks
    ax.set_xlabel('Window size')
    ax.set_ylabel('Heads')
    ax.set_zlabel('Mean(cm)')
    ax.set_xticks(_x)
    ax.set_xticklabels([4, 3, 2, 1])
    ax.set_yticks(_y)
    ax.set_yticklabels([4, 3, 2, 1])
    ax.set_title('APE')

    # Color bar which maps values to colors.
    cbar = plt.colorbar(surf, shrink=0.5, aspect=5, ax=ax)
    cbar.set_label('Mean(cm)')

    plt.show()


def smooth_curve_3D():
    # Original data
    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = 24  # Set the default font size to 16
    rcParams['font.serif'] = ['Times New Roman']
    ate_values = np.array([
        [1.411, 2.127, 1.723, 1.715],
        [2.354, 2.097, 1.448, 1.677],
        [2.031, 1.939, 1.381, 1.260],
        [1.621, 1.998, 2.092, 2.079]
    ])

    # Multiply each value by 10
    # ate_values *= 10

    # Define the grid
    x = np.arange(1, ate_values.shape[1] + 1)
    y = np.arange(1, ate_values.shape[0] + 1)
    xx, yy = np.meshgrid(x, y)

    # Interpolate to make the surface smoother
    x_fine = np.linspace(1, ate_values.shape[1], 100)
    y_fine = np.linspace(1, ate_values.shape[0], 100)
    xx_fine, yy_fine = np.meshgrid(x_fine, y_fine)
    ate_values_fine = griddata((xx.ravel(), yy.ravel()), ate_values.ravel(), (xx_fine, yy_fine), method='cubic')

    # Create the figure
    fig = plt.figure(figsize=(13, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface
    surf = ax.plot_surface(xx_fine, yy_fine, ate_values_fine, cmap='viridis', edgecolor='k', alpha=0.8)

    # Annotate the point (4,3)
    annotate_val = ate_values[2, 3]  # Value at (4,3)
    ax.scatter(4, 3, annotate_val, color='red', s=500)
    ax.text(4, 3, annotate_val, f'  (4, 3): {annotate_val}', color='red', fontsize=24, weight='bold')

    # Labels and ticks
    ax.set_xlabel('Window size')
    ax.set_ylabel('Heads')
    ax.set_zlabel('Mean(mm)')
    ax.set_xticks(x)
    ax.set_xticklabels([1, 2, 3, 4])
    ax.set_yticks(y)
    ax.set_yticklabels([1, 2, 3, 4])
    ax.set_title('ATE')

    # Color bar which maps values to colors.
    cbar = plt.colorbar(surf, shrink=0.5, aspect=5, ax=ax)
    cbar.set_label('mm')

    # plt.show()
    plt.savefig("/Users/mintan/PycharmProjects/Toky-Personal-Process/DataFiles/pdfs/sec5-impact_of_windowsize.pdf", format='pdf')



if __name__ == '__main__':
    # box_plot()
    stacked_bar()
    # color_bar_plot()
    # curve3D()
    # smooth_curve_3D()