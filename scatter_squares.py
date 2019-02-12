import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# delete the edge of the data points, using a color map with the y values
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=40)
# set title, add tag to the axis
plt.title("Square numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of the value", fontsize=14)
# set the tick params
plt.tick_params(axis="both", which="major", labelsize=14)
# set the range of every axis
plt.axis([0, 1100, 0, 1100000])
plt.show()
# save the figure and crop the blank area
plt.savefig("scatter_square_numbers.png")
