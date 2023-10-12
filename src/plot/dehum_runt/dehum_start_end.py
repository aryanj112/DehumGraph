import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import day_average as da

def dehum_start_end(start_date,end_date):

    # Read data
    temperature_data = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Deh(out)\2023CH6A_use.csv")

    # Clean data
    temperature_data.replace("---.-", np.nan, inplace=True)
    temperature_data["Temperature(F)"] = pd.to_numeric(temperature_data["Temperature(F)"], errors='coerce')
    temperature_data.dropna(inplace=True)

    # Filter time
    datetime1 = pd.to_datetime(start_date, format='%m/%d/%y')
    datetime2 = pd.to_datetime(end_date, format='%m/%d/%y')
    formatted_date = datetime1.strftime('%#m/%d/%y')
    formatted_date2 = datetime2.strftime('%#m/%d/%y')

    temperature_data["Time"] = pd.to_datetime(temperature_data["Time"], format= "%m/%d/%y %H:%M")
    temperature_data = temperature_data[temperature_data["Time"].between(formatted_date, formatted_date2)]

    # Get the daily average temperature using the 'day_average' module
    day_avg_temperature = da.day_average(formatted_date, formatted_date2)

    # Plot
    fig, ax1 = plt.subplots()
    ax1.plot(temperature_data["Time"], temperature_data["Temperature(F)"], '-', label="Temperature(F)", color="tab:red")
    #vertical_line_time = pd.to_datetime("2023-06-13 12:00")
    #ax1.axvline(x=vertical_line_time, color='red', linestyle='--')
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature(F)", color="tab:red")
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d %H:%M"))

    # Plot the daily average temperature as a horizontal line
    ax1.axhline(y=day_avg_temperature, color='tab:blue', linestyle='--', label="Daily Avg Temperature")

    ax1.legend(loc="upper left")
    plt.xticks(rotation=45)
    plt.title("Temperature(F) at Deh(out) Vs. Time (H)")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    start_date = input("Enter start date (e.g., 4/5/23): ")
    end_date = input("Enter end date (e.g., 4/6/23): ")
    print(dehum_start_end(start_date,end_date))