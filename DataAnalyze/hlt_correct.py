import csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)

  dates, highs, lows