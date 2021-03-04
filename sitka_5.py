import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# enumerate returns both the index item and the value of each
# item as you loop through a list

for index, column_header in enumerate(header_row):
    print("Index: ", index, "Column Name: ", column_header)

highs = []
lows = []
dates = []

# example:
# somedate = "2018-07-01"
# converted_date = datetime.strptime(somedate, "%Y-%m-%d")
# print(converted_date)
for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

open_file2 = open("death_valley_2018_simple.csv", "r")
csv_file2 = csv.reader(open_file2, delimiter=",")

header_row = next(csv_file2)

# enumerate returns both the index item and the value of each
# item as you loop through a list


for index, column_header in enumerate(header_row):
    print("Index: ", index, "Column Name: ", column_header)

highs = []
lows = []
dates = []

# example:
# somedate = "2018-07-01"
# converted_date = datetime.strptime(somedate, "%Y-%m-%d")
# print(converted_date)
for row in csv_file2:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

import matplotlib.pyplot as plt

fig, a = plt.subplots(2)

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily high and low temperatures for 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.show()

fig.autofmt_xdate()

plt.show()


# subplot

# fig2, a = plt.subplots(2)
# a[0].plot(dates, highs, c="red")
# a[1].plot(dates, lows, c="blue")

# plt.show()
