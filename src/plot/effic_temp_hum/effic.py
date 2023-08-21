# Plotting file that graphs l/kWh agaisnt time
# Dehumidifier Data -> L/kWh

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

#dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehumidifer_full_data.csv")
dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehumidifier_Full_Data_New.csv")

dehum["Start Date"] = pd.to_datetime(dehum["Start Date"]) # Convert dehum date to datetime

# Filter data to start from 2019
start_date = pd.to_datetime("2023-05-06")
end_date = pd.to_datetime("2023-08-14") 
dehum = dehum[dehum["Start Date"].between(start_date, end_date)]

fig, ax1 = plt.subplots()

ax1.set_ylim(0, 2) 
ax1.plot(dehum["Start Date"],dehum["L/kWh"], label = "Efficiency", color = "tab:blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Efficiency", color = "tab:blue")

# Set the x-axis to show years, you can adjust this as needed
#ax1.xaxis.set_major_locator(mdates.YearLocator())
#ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # Format as year

ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m"))  # Format as year

#Show Legend
ax1.legend(loc = "upper left")

plt.title("Weather Vs. Efficiency (Summer 2023)")
plt.show()