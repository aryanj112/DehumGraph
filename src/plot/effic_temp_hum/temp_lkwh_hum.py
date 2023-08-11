# Plotting file that graphs temperature, l/kWh, and humidity all agaisnt time
# NetZero -> Temperature # Dehumidifier Data -> L/kWh # Ambient Weather -> Humidity

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.ticker import MaxNLocator

# Read data
dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehumidifer_full_data.csv")
weather = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\netzero\weather_file.csv")
ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\ambient_CH1A_combine.csv")

# Convert data to datetime
dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])
weather["date"] = pd.to_datetime(weather["date"])
ambient["Time"] = pd.to_datetime(ambient["Time"])

# Filter data start and end time
start_date = pd.to_datetime("2021-01-01")
end_date = pd.to_datetime("2023-08-08") 
dehum = dehum[dehum["Start Date"].between(start_date, end_date)]
weather = weather[weather["date"].between(start_date, end_date)]
ambient = ambient[ambient["Time"].between(start_date, end_date)]

fig, ax1 = plt.subplots()

# Set the x-axis to show years
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

# Plot first variable
ax1.plot(dehum["Start Date"], dehum["L/kWh"], '-', label="Efficiency", color="tab:blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Efficiency", color="tab:blue")

# Create a second y-axis for temperature
ax2 = ax1.twinx()
ax2.plot(weather["date"], weather["temperature"], 'o', label="Temperature", color="tab:red")
ax2.set_ylabel("Temperature (°C)", color="tab:red")

# Create a third y-axis for humidity
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 80))
ax3.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=15))
ax3.plot(ambient["Time"], ambient["Humidity(%)"], '-', label="Humidity (%)", color="tab:purple")
ax3.plot(ambient["Time"], ambient["Humidity(%)"], '-', label="Humidity (%)", color="tab:purple")
ax3.set_ylabel("Humidity (%)", color="tab:purple")

# Show Legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines + lines2+lines3, labels + labels2 + labels3, loc="upper left")

# Title and end
plt.title("Efficiency, Humidity, and Temperature (BEFORE AVERAGING)")
fig.tight_layout()
plt.show()