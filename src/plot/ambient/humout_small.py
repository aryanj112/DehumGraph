import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Read data and perform preprocessing
ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Deh(out)\2023CH6A_use.CSV")

# Convert Time column to datetime
ambient["Time"] = pd.to_datetime(ambient["Time"])

# Clean data
ambient.replace("--", np.nan, inplace=True)  # Replaces '--' with NaN values
ambient['Temperature(F)'] = pd.to_numeric(ambient['Temperature(F)'], errors='coerce')  # Convert humidity column to numeric values
ambient.dropna(inplace=True)  # Drops NaN values

# Calculate daily average temperature
ambient["Date"] = ambient["Time"].dt.date
daily_avg_temp = ambient.groupby("Date")["Temperature(F)"].mean()

# Filter data to start from 2023-06-18
ambient = ambient[ambient["Time"] >= "2023-06-18"]

# Create a figure and plot
fig, ax1 = plt.subplots()

ax1.plot(daily_avg_temp.index, daily_avg_temp.values, '-', label="Avg Temp", color="tab:red")
ax1.set_xlabel("Date")
ax1.set_ylabel("Temperature(F)", color="tab:red")

# Set the x-axis to show months and days
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7))  # Show ticks every 7 days
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))  # Format as month abbreviation and day

# Show Legend
ax1.legend(loc="upper left")

# Set plot title
plt.title("Average Temperature Vs. Time (2023)")

# Display the plot
plt.tight_layout()
plt.show()