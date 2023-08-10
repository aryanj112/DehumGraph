import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.ticker import MaxNLocator

# Read data and perform preprocessing (you can keep this as it is)
# Read data
dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehumidifer_full_data.csv")
weather = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\netzero\weather_file.csv")
ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\ambient_CH1A_combine.csv")

# Convert data to datetime
dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])
weather["date"] = pd.to_datetime(weather["date"])
ambient["Time"] = pd.to_datetime(ambient["Time"])

# Filter data start and end time
start_date = pd.to_datetime("2019-01-01")
end_date = pd.to_datetime("2023-08-08") 
dehum = dehum[dehum["Start Date"].between(start_date, end_date)]
weather = weather[weather["date"].between(start_date, end_date)]
ambient = ambient[ambient["Time"].between(start_date, end_date)]

# Calculate daily average humidity
ambient["Date"] = ambient["Time"].dt.date
daily_avg_humidity = ambient.groupby("Date")["Humidity(%)"].mean()

# Calculate daily average temperature
daily_avg_temp = weather.groupby(weather["date"].dt.date)["temperature"].mean()

# Create a figure with four subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Plot 1
ax1 = axes[0, 0]
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax1.set_ylim(0, 2) 
ax1.plot(dehum["Start Date"], dehum["L/kWh"], '-', label="Efficiency", color="tab:blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Efficiency", color="tab:blue")

# Create a second y-axis for temperature and humidity
ax2 = ax1.twinx()
ax2.plot(daily_avg_temp.index, daily_avg_temp.values, '-', label="Avg Temperature", color="tab:red")
ax2.set_ylabel("Avg Temperature (°C)", color="tab:red")

# Create a third y-axis for average humidity
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 50))
ax3.plot(daily_avg_humidity.index, daily_avg_humidity.values, '-', label="Avg Humidity (%)", color="tab:purple")
ax3.set_ylabel("Avg Humidity (%)", color="tab:purple")

# End and title
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc="upper left")
ax1.set_title("Efficiency, Avg Humidity, and Avg Temperature (AFTER AVERAGING)")

# Plot 2
ax2 = axes[0, 1]
ax2.set_ylim(0, 2) 
ax2.plot(dehum["Start Date"], dehum["L/kWh"], label="Efficiency", color="tab:blue")
ax2.set_xlabel("Date")
ax2.set_ylabel("Efficiency", color="tab:blue")
ax2.xaxis.set_major_locator(mdates.YearLocator())
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax2.legend(loc="upper left")
ax2.set_title("Weather Vs. Efficiency")

# Plot 3
ax3 = axes[1, 0]
ax3.plot(daily_avg_temp.index, daily_avg_temp.values, '-', label="Avg Temperature", color="tab:red")
ax3.set_xlabel("Date")
ax3.set_ylabel("Average Temperature (°F)", color="tab:red")
ax3.xaxis.set_major_locator(mdates.YearLocator())
ax3.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax3.legend(loc="upper left")
ax3.set_title("Average Temperature Vs. Time")

# Plot 4
ax4 = axes[1, 1]
ax4.plot(daily_avg_humidity.index, daily_avg_humidity.values, '-', label="Avg Humidity (%)", color="tab:purple")
ax4.set_ylabel("Avg Humidity (%)", color="tab:purple")
ax4.set_xlabel("Date")
ax4.xaxis.set_major_locator(mdates.YearLocator())
ax4.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax4.legend(loc="upper left")
ax4.set_title("Average Humidity(%) Vs. Time")


# Adjust layout
plt.title("Efficiency, Weather, and Temperature (2019-2023)")
plt.tight_layout()

# Display all plots together
plt.show()