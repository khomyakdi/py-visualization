import csv
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.plot(highs, c='red')

plt.title("Daily high temperature, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis="both", which='major', labelsize=16)

plt.show()
