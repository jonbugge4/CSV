import csv
from datetime import datetime
open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ',')

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)


dates = []
highs = []
lows= []

for row in csv_file:
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

fig = plt.figure()

plt.title("Daily High Temperature, July 2018", fontsize = 16)
plt.xlabel("",fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis='both',which = 'major', labelsize=12)

plt.plot(dates, highs, c= 'red', alpha=0.5)
plt.plot(dates, lows, c= 'blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)


fig.autofmt_xdate()

plt.show()


#subplot lets us usse multiple plots in one figure
#subplot(row, column, index)/(2,1,1) creates two graphs on top of each other 
#index starts at 1, not 0
plt.subplot(2,1,1)
plt.plot(dates, highs, c='red')
plt.title('Highs')

plt.subplot(2,1,2)
plt.plot(dates, lows, c='blue')
plt.title('Lows')


#super title is the title of the page with the plots
plt.suptitle("Highs and lows of Sitka Alaska")

plt.show()
