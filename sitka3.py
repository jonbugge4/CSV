import csv
from datetime import datetime
open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ',')

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)


#testing to convert date from string
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(type(mydate))

dates = []
high = []
low= []

for row in csv_file:
    high.append(int(row[5]))
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)
    low.append(int(row[6]))

print(high)
print(dates)
print(low)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.title("Daily High Temperature, July 2018", fontsize = 16)
plt.xlabel("",fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis='both',which = 'major', labelsize=12)

plt.plot(dates, high, c= 'red', alpha=0.5)
plt.plot(dates, low, c= 'blue', alpha=0.5)
plt.fill_between(dates, high, low, facecolor = 'blue', alpha = 0.1)


fig.autofmt_xdate()

plt.show()
