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

# Calculate daily average humidity
ambient["Date"] = ambient["Time"].dt.date
daily_avg_humidity = ambient.groupby("Date")["Humidity(%)"].mean()

fig, ax1 = plt.subplots()

# Set the x-axis to show years
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

# Plot first variable (efficiency) on the left y-axis
ax1.plot(dehum["Start Date"], dehum["L/kWh"], '-', label="Efficiency", color="tab:blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Efficiency", color="tab:blue")

# Create a second y-axis for temperature and humidity
ax2 = ax1.twinx()

# Plot temperature on the right y-axis
ax2.plot(weather["date"], weather["temperature"], 'o', label="Temperature", color="tab:red")
ax2.set_ylabel("Temperature (°C)", color="tab:red")

# Plot daily average humidity on the right y-axis
ax2.plot(daily_avg_humidity.index, daily_avg_humidity.values, '-', label="Avg Humidity (%)", color="tab:purple")
ax2.set_ylabel("Avg Humidity (%)", color="tab:purple")

# Show Legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

# Title and end
plt.title("Efficiency, Temperature, and Avg Humidity")
fig.tight_layout()
plt.show()