import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Read data and perform preprocessing
ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_combine.CSV")

# Convert Time column to datetime
ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")

# Clean data
ambient.replace("--", np.nan, inplace=True)  # Replaces '--' with NaN values
ambient['Humidity(%)'] = pd.to_numeric(ambient['Humidity(%)'], errors='coerce')  # Convert humidity column to numeric values
ambient.dropna(inplace=True)  # Drops NaN values

# Calculate daily average temperature
#ambient["Date"] = ambient["Time"].dt.date
#daily_avg_temp = ambient.groupby("Date")["Temperature(F)"].mean()

# Filter data to start from 2023-06-18
start_date = pd.to_datetime("2023-07-04")  # Convert to datetime.date
end_date = pd.to_datetime("2023-07-05")  # Convert to datetime.date
#daily_avg_temp = daily_avg_temp.loc[start_date:end_date]
ambient = ambient[ambient["Time"].between(start_date, end_date)]

# Create a figure and plot
fig, ax1 = plt.subplots()

#ax1.plot(daily_avg_temp.index, daily_avg_temp.values, '-', label="Avg Temp", color="tab:red")
ax1.plot(ambient["Time"], ambient["Humidity(%)"], '-', label="Humidity(%)", color="tab:purple")

ax1.set_xlabel("Date and Time")
ax1.set_ylabel("Humidity(%)", color="tab:purple")

# Set the x-axis to show hours
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))  # Show ticks every 6 hour
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))  # Format as month, day, and hour:minute

# Show Legend
ax1.legend(loc="upper left")

plt.xticks(rotation= 45)

# Set plot title
plt.title("Humidity(%) Vs. Time (hourly)")

# Display the plot
plt.tight_layout()
plt.show()