# Plotting file that graphs avg temperature, l/kWh, and avg humidity all agaisnt time but in a 4 graph plot
# NetZero -> Avg Temperature # Dehumidifier Data -> L/kWh # Ambient Weather -> Avg Humidity

# Imports
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

def plot_1():
    fig, ax1 = plt.subplots()

    # Set the x-axis to show years
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    # Plot first variable (efficiency) on the left y-axis
    ax1.plot(dehum["Start Date"], dehum["L/kWh"], '-', label="Efficiency", color="tab:blue")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Efficiency", color="tab:blue")
    #ax1.set_ylim(0, 2)

    # Create a second y-axis for temperature and humidity
    ax2 = ax1.twinx()

    # Plot daily average temperature on the right y-axis
    ax2.plot(daily_avg_temp.index, daily_avg_temp.values, '-', label="Avg Temperature", color="tab:red")
    ax2.set_ylabel("Avg Temperature (°C)", color="tab:red")

    # Create a third y-axis for average humidity
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 80))
    ax3.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=15))
    ax3.plot(daily_avg_humidity.index, daily_avg_humidity.values, '-', label="Avg Humidity (%)", color="tab:purple")
    ax3.set_ylabel("Avg Humidity (%)", color="tab:purple")

    # Show Legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    lines3, labels3 = ax3.get_legend_handles_labels()
    ax1.legend(lines + lines2+lines3, labels + labels2 + labels3, loc="upper left")

    # Title and end
    plt.title("Efficiency, Avg Humidity, and Avg Temperature (AFTER AVERAGING)")
    fig.tight_layout()

def plot_2():
    fig, ax1 = plt.subplots()

    #ax1.set_ylim(0, 2) 
    ax1.plot(dehum["Start Date"],dehum["L/kWh"], label = "Efficiency", color = "tab:blue")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Efficiency", color = "tab:blue")

    # Set the x-axis to show years, you can adjust this as needed
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # Format as year

    #Show Legend
    ax1.legend(loc = "upper left")

    plt.title("Weather Vs. Efficiency (2019-2023)")

def plot_3():
    fig, ax1 = plt.subplots()

    # Calculate daily average temperature
    daily_avg_temp = weather.groupby(weather["date"].dt.date)["temperature"].mean()

    ax1.set_xlabel("Date")
    ax1.set_ylabel("Average Temperature", color = "tab:blue")

    ax1.plot(weather["date"], weather["temperature"], 'o', label="Temperature", color="tab:red")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Average Temperature (°C)", color="tab:red")


    # Set the x-axis to show years, you can adjust this as needed
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # Format as year

    #Show Legend
    ax1.legend(loc = "upper left")

    plt.title("Average Temperature Vs. Time (2019-2023)")

def plot_4():
    fig, ax1 = plt.subplots()

    # Calculate daily average humidity
    ambient["Date"] = ambient["Time"].dt.date
    daily_avg_humidity = ambient.groupby("Date")["Humidity(%)"].mean()
    
    ax1.plot(daily_avg_humidity.index, daily_avg_humidity.values, '-', label="Avg Humidity (%)", color="tab:purple")
    ax1.set_ylabel("Avg Humidity (%)", color="tab:purple")
    ax1.set_xlabel("Date")

    # Set the x-axis to show years, you can adjust this as needed
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # Format as year

    #Show Legend
    ax1.legend(loc = "upper left")

    plt.title("Average Humidity(%) Vs. Time (2019-2023)")

plot_1()
plot_2()
plot_3()
plot_4()

plt.show()