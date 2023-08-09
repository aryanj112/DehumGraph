import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.ticker import MaxNLocator

#Read data
dehum = pd.read_csv("data/dehumidifer_full_data.csv")
weather = pd.read_csv("data/netzero/weather_file.csv")
ambient = pd.read_csv("data/ambient_weather/ambient_CH1A_combine.csv")
#2021CH1A_use
#ambient_combine_data

#Convert data to datetime
dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])
weather["date"] = pd.to_datetime(weather["date"])
ambient["Time"] = pd.to_datetime(ambient["Time"])

# Filter data to start from 2019
dehum = dehum[dehum["Start Date"] >= "2021-01-01"]
weather = weather[weather["date"] >= "2021-01-01"]
ambient = ambient[ambient["Time"] >= "2021-01-01"]

fig, ax1 = plt.subplots()

# Set the x-axis to show years
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # Format as year

#Plot first variable
ax1.plot(dehum["Start Date"],dehum["L/kWh"], '-', label = "Efficiency", color = "tab:blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Efficiency", color = "tab:blue")

#Plot second Variable
ax2 = ax1.twinx()
ax2.plot(weather["date"],weather["temperature"], '-',label = "Temperature", color = "tab:red")
ax2.set_ylabel("Temperature", color = "tab:blue")

#Plot third Variable
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 50))
ax3.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=15))  # Adjust nbins as needed
ax3.plot(ambient["Time"],ambient["Humidity(%)"], '-',label = "Humidity(%)", color = "tab:purple")
ax3.set_ylabel("Humidity(%)", color = "tab:purple")


#Show Legend
ax1.legend(loc = "upper left")
ax2.legend(loc = "upper left",bbox_to_anchor=(0,0.96))
ax3.legend(loc = "upper left",bbox_to_anchor=(0,.92))

#Title and end
plt.title("Efficiency, Humidity, and Temperature")
fig.tight_layout()
plt.show()