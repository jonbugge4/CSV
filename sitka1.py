import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ',')

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

high = []

for row in csv_file:
    high.append(int(row[5]))

print(high)

import matplotlib.pyplot as plt

plt.title("Daily High Temperature, July 2018", fontsize = 16)
plt.xlabel("",fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis='both',which = 'major', labelsize=12)

plt.plot(high, c= 'red')
plt.show()