import csv
import matplotlib.pyplot as plt
from datetime import datetime

#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# for index, column_header in enumerate(header_row):
#    print(index, column_header)

    # get the datas
    dates = []
    highs = []
    lows = []
    for row in reader:
      try:
        date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])
        low = int(row[3])
      except ValueError:
        print(date, 'missing data')
      else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

    # draw a figure to show the daily high and low temperatures
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')

    # some settings of the figure
    plt.title("Daily high and low temperatures 2014", fontsize=24)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)
    plt.show()
