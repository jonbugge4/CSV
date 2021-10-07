import csv

from datetime import datetime
open_file = open("sitka_weather_2018_simple.csv", "r")

open_file2 = open("death_valley_2018_simple.csv", 'r')

csv_file = csv.reader(open_file, delimiter = ',')
csv_file2 =csv.reader(open_file2, delimiter = ',')

header_row = next(csv_file)
header_row2 = next(csv_file2)


dates = []
highs = []
lows = []

dates2 = []
highs2 = []
lows2 = []

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
        highs2.append(high)
        lows2.append(low)
        dates2.append(the_date)

print(highs[:5])
print(dates[:5])
print(lows[:5])
print(highs2[:5])
print(dates2[:5])
print(lows2[:5])

import matplotlib.pyplot as plt

fig = plt.figure()

plt.xlabel("",fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis='both',which = 'major', labelsize=12)



plt.subplot(2,1,1)
plt.plot(dates, lows, c='blue', alpha = 0.5)
plt.plot(dates, highs, c='red', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
plt.title('Sitka')

plt.subplot(2,1,2)
plt.plot(dates2, lows2, c='blue', alpha = 0.5)
plt.plot(dates2, highs2, c='red', alpha = 0.5)
plt.fill_between(dates2, highs2, lows2, facecolor = 'blue', alpha = 0.1)
plt.title('Death Valley')

plt.suptitle('Temperatures of Sitka and Death Valley')

fig.autofmt_xdate()
plt.show()
