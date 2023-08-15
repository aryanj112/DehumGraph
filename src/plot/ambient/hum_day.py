import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Read data
ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_combine.CSV")

# Convert Time column to datetime
ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")

# Clean data
ambient.replace("--", np.nan, inplace=True)  # Replaces '--' with NaN values
ambient['Humidity(%)'] = pd.to_numeric(ambient['Humidity(%)'], errors='coerce')  # Convert humidity column to numeric values
ambient.dropna(inplace=True)  # Drops NaN values

# Fitlter time 
start_date = pd.to_datetime("2023-07-04")  
end_date = pd.to_datetime("2023-07-05")  
ambient = ambient[ambient["Time"].between(start_date, end_date)]

# Create a figure and plot
fig, ax1 = plt.subplots()

ax1.plot(ambient["Time"], ambient["Humidity(%)"], '-', label="Humidity(%)", color="tab:purple")

vertical_line_time = pd.to_datetime("2023-07-04 12:00") # Add vertical line at 11 o'clock on July 5th, 2023
ax1.axvline(x=vertical_line_time, color='red', linestyle='--')

ax1.set_xlabel("Date and Time")
ax1.set_ylabel("Humidity(%)", color="tab:purple")

ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))  # Show ticks every 6 hour
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))  # Format as month, day, and hour:minute

# Show Legend
ax1.legend(loc="upper left")
plt.xticks(rotation= 45)
plt.title("Humidity(%) Vs. Time (hourly)") # Set plot title

# Display the plot
plt.tight_layout()
plt.show()