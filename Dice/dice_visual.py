from dice import Dice
import pygal

dice_1 = Dice()
dice_2 = Dice(10)

results = []

for roll_num in range(50000):
    results.append(dice_1.roll() + dice_2.roll())

frequencies = []

# draw the histogram of the result
hist = pygal.Bar()
hist.title = "Result of rolling two dices 50000times"
hist.x_title = "Result"
hist.y_title = "Frequency of the result"
hist_xlabels = []

for value in range(2, dice_1.num_sides + dice_2.num_sides + 1):
    hist_xlabels.append(str(value))
    frequencies.append(results.count(value))

hist.x_labels = hist_xlabels
hist.add('D' + str(dice_1.num_sides) + '+ D' +
         str(dice_2.num_sides), frequencies)
hist.render_to_file('dice_visual.svg')
