import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_nums = list(range(rw.num_points))
    # show the order of the coloring
    plt.scatter(rw.x_values, rw.y_values, c=point_nums,
                cmap=plt.cm.Blues, edgecolors='none', s=15)
    # hightlight the start and the end point
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolors='none', s=100)

    # hide the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # set the window size of the figure
    # plt.figure(figsize=(72, 50))
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
