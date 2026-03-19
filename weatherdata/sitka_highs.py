
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the CSV file
filename = os.path.join(script_dir, 'sitka_weather_2021_full.csv')

with open(filename) as f:
    # rest of your code remains the same
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # Get dates and high and low  temperatures from this file.
    dates, highs, lows = [], [], []
    rainfall = []


    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[7])
            low = int(row[8])
            prcp = float(row[5])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            rainfall.append(prcp)
         


# Plot the high  and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(dates , highs, c='red' , alpha = 0.5)
ax1.plot(dates , lows, c='blue', alpha = 0.5)
ax2.plot(dates , rainfall, c='green', alpha = 0.5)
# Format plot.

plt.title("Daily high and low temperatures and rainfall - 2021", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
ax1.set_ylim(0,130)
plt.show()

    
  