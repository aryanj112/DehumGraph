import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Read data and perform preprocessing
ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Deh(out)\2023CH6A_use.CSV")

# Convert Time column to datetime
ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")

# Clean data
ambient.replace("--", np.nan, inplace=True)  # Replaces '--' with NaN values
ambient['Temperature(F)'] = pd.to_numeric(ambient['Temperature(F)'], errors='coerce')  # Convert humidity column to numeric values
ambient.dropna(inplace=True)  # Drops NaN values

# Calculate daily average temperature
#ambient["Date"] = ambient["Time"].dt.date
#daily_avg_temp = ambient.groupby("Date")["Temperature(F)"].mean()

# Filter data to start from 2023-06-18
start_date = pd.to_datetime("2023-06-25")  # Convert to datetime.date
end_date = pd.to_datetime("2023-06-26")  # Convert to datetime.date
#daily_avg_temp = daily_avg_temp.loc[start_date:end_date]
ambient = ambient[ambient["Time"].between(start_date, end_date)]

# Create a figure and plot
fig, ax1 = plt.subplots()

#ax1.plot(daily_avg_temp.index, daily_avg_temp.values, '-', label="Avg Temp", color="tab:red")
ax1.plot(ambient["Time"], ambient["Temperature(F)"], '-', label="Temperature(F)", color="tab:red")

ax1.set_xlabel("Date and Time")
ax1.set_ylabel("Temperature(F)", color="tab:red")

# Set the x-axis to show hours
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))  # Show ticks every 6 hour
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))  # Format as month, day, and hour:minute

# Show Legend
ax1.legend(loc="upper left")

plt.xticks(rotation= 45)

# Set plot title
plt.title("Temperature Vs. Time (hourly)")

# Display the plot
plt.tight_layout()
plt.show()