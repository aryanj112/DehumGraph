import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

dehum = pd.read_csv("data/dehumidifer_full_data.csv")
weather = pd.read_csv("data/netzero/weather_file.csv")

#dehum["Start Date"] = pd.to_datetime(dehum["Start Date"]) # Convert dehum date to datetime
#weather["date"] = pd.to_datetime(weather["date"])  # Convert weather date to datetime

# Filter data to start from 2019
dehum = dehum[dehum["Start Date"] >= "2021-01-01"]
weather = weather[weather["date"] >= "2021-01-01"]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

#Plot First Variable
ax1.plot(dehum["Start Date"],dehum["L/kWh"], label = "Efficiency", color = "tab:blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Efficiency", color = "tab:blue")

#Plot First Variable
ax2.plot(weather["date"],weather["temperature"], 'o',label = "Temperature", color = "tab:red")
ax2.set_ylabel("Temperature", color = "tab:blue")

# Set the x-axis to show years, you can adjust this as needed
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # Format as year

#Show Legend
ax1.legend(loc = "upper left")
ax2.legend(loc = "upper left",bbox_to_anchor=(0,0.93))

plt.title("Weather Vs. Efficiency (2021-2023)")
plt.show()
