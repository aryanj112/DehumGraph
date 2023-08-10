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

# Filter data to start from 2021
start_date = pd.to_datetime("2021-01-01")
dehum = dehum[dehum["Start Date"] >= start_date]
weather = weather[weather["date"] >= start_date]
ambient = ambient[ambient["Time"] >= start_date]

fig, ax1 = plt.subplots()

# Set the x-axis to show years
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # Format as year

# Plot first variable
ax1.plot(dehum["Start Date"], dehum["L/kWh"], '-', label="Efficiency", color="tab:blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Efficiency", color="tab:blue")

# Create a second y-axis for temperature
ax2 = ax1.twinx()
ax2.plot(weather["date"], weather["temperature"], 'o', label="Temperature", color="tab:red")
ax2.set_ylabel("Temperature (°C)", color="tab:red")

# Plot humidity data directly on the primary y-axis (ax1)
ax1.plot(ambient["Time"], ambient["Humidity(%)"], '-', label="Humidity (%)", color="tab:purple")
ax1.set_ylabel("Humidity (%)", color="tab:purple")

# Combine the legends from all y-axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
all_lines = lines1 + lines2
all_labels = labels1 + labels2
ax1.legend(all_lines, all_labels, loc="upper left", bbox_to_anchor=(0, 1.0))

# Title and end
plt.title("Efficiency, Humidity, and Temperature")
fig.tight_layout()
plt.show()