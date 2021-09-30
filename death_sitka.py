import csv

from datetime import datetime
open_file = open("sitka_weather_2018_simple.csv", "r")

open_file2 = open("death_valley_2018_simple.csv", 'r')

csv_file = csv.reader(open_file, delimiter = ',')
csv_file2 =csv.reader(open_file, delimiter = ',')

header_row = next(csv_file)
header_row2 = next(csv_file2)


dates = []
highs = []
lows = []

for row in csv_file:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high =int(row[5])
        low =int(row[6])
    except ValueError:
        print(f'missing data for {the_date}')
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)

for row in csv_file2:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"missing data for {the_date}")
        #allows us to incorporate variables directly into statements^^ "f string method"
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)

print(high)
print(dates)
print(low)

import matplotlib.pyplot as plt

plt.subplot(2,1,1)
plt.plot(dates, low, c='blue')
plt.plot(dates, high, c='red')
plt.title('Sitka')

plt.subplot(2,1,2)
plt.plot(dates, low, c='blue')
plt.plot(dates, high, c='red')
plt.title('Death Valley')

plt.suptitle('Temperatures of Sitka and Death Valley')

plt.show()
