import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline

# Read data
ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.CSV")

# Convert Time column to datetime
ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")

# Clean data
ambient.replace("--", np.nan, inplace=True)
ambient['Absolute Humidity(%)'] = pd.to_numeric(ambient['Absolute Humidity(%)'], errors='coerce')
ambient.dropna(inplace=True)

# Filter time
start_date = pd.to_datetime("2023-07-04")
end_date = pd.to_datetime("2023-07-05")
ambient = ambient[ambient["Time"].between(start_date, end_date)]

# Create a figure and plot
fig, ax1 = plt.subplots()

#cubic_interp = CubicSpline(ambient["Time"], ambient["Absolute Humidity(%)"])
#x_interp = pd.date_range(start=min(ambient["Time"]), end=max(ambient["Time"]), periods=100)
#y_interp = cubic_interp(x_interp)

#ax1.plot(x_interp, y_interp, '-', label="Absolute Humidity [g/m^3]", color="tab:purple")

ax1.plot(ambient["Time"], ambient["Absolute Humidity(%)"], '-', label="Absolute Humidity [g/m^3]", color="tab:purple")
#ax1.plot(ambient["Time"], ambient["Humidity(%)"], '-', label="Humidity(%)", color="tab:purple")

vertical_line_time = pd.to_datetime("2023-07-04 12:00")
ax1.axvline(x=vertical_line_time, color='red', linestyle='--')

ax1.set_xlabel("Date and Time")
ax1.set_ylabel("Absolute Humidity[g/m^3]", color="tab:purple")

ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

ax1.legend(loc="upper left")
plt.xticks(rotation=45)
plt.title("Absolute Humidity[g/m^3] Vs. Time (hourly)")

plt.tight_layout()
plt.show()