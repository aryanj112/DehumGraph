import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import day_average as da

def dehum_start_end(month, day):

    # Read data
    temperature_data = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Deh(out)\2023CH6A_use.csv")

    # Clean data
    temperature_data.replace("---.-", np.nan, inplace=True)
    temperature_data["Temperature(F)"] = pd.to_numeric(temperature_data["Temperature(F)"], errors='coerce')
    temperature_data.dropna(inplace=True)

    # Filter time

    year = 2023  
    month = int(month)  
    day = int(day)  
    hour = 0
    minute = 0
    input_date = datetime(year, month, day, hour, minute)
    #input_date = input_date.strftime("%m/%d/%y %H:%M")
    new_date = input_date + timedelta(days=1)
    input_date = pd.to_datetime(input_date, format= "%m/%d/%y %H:%M")
    new_date = pd.to_datetime(new_date, format= "%m/%d/%y %H:%M")


    temperature_data["Time"] = pd.to_datetime(temperature_data["Time"], format= "%m/%d/%y %H:%M")
    temperature_data = temperature_data[temperature_data["Time"].between(input_date, new_date)]

    # Get the daily average temperature using the 'day_average' module
    print('error')
    day_avg_temperature = da.day_average(input_date, new_date)

    # Plot
    fig, ax1 = plt.subplots()
    ax1.plot(temperature_data["Time"], temperature_data["Temperature(F)"], '-', label="Temperature(F)", color="tab:red")
    vertical_line_time = pd.to_datetime("2023-07-18 12:00")
    ax1.axvline(x=vertical_line_time, color='red', linestyle='--')
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature(F)", color="tab:red")
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

    # Plot the daily average temperature as a horizontal line
    print("get")
    print(day_avg_temperature)
    if not pd.isna(day_avg_temperature):
        ax1.axhline(y=day_avg_temperature, color='tab:blue', linestyle='--', label="Daily Avg Temperature")

    ax1.legend(loc="upper left")
    plt.xticks(rotation=45)
    plt.title("Temperature(F) Vs. Time (H)")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    print('You will enter a month and day after June 18th, 2023')
    month = input('Enter month: ')
    day = input('Enter day: ')
    dehum_start_end(month, day)