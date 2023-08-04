import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
import pandas as pd


dehum = pd.read_csv("data/dehumidifer_full_data.csv")
weather = pd.read_csv("data/result/weather.csv")

# Convert "Start Date" to datetime objects
dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

#Plot First Variable
ax1.plot(dehum["Start Date"],dehum["L/kWh"], label = "Efficiency", color = "tab:blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Efficiency", color = "tab:blue")

#Plot First Variable
ax2.plot(weather["date"],weather["temperature"], 'o',label = "Temperature", color = "tab:red")
ax2.set_ylabel("Temperature", color = "tab:blue")

#Set the x-axis to show months
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter(""))

#Show Legend
ax1.legend(loc = "upper left")
ax2.legend(loc = "upper left",bbox_to_anchor=(0,0.93))

plt.title("Weather Vs. Efficiency")
plt.show()
