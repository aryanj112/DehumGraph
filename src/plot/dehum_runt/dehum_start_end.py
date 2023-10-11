import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def dehum_start_end(month, day, varbool):    
    
    if varbool == 'H':
        var = "Humidity(%)"
    else:
        var = "Temperature(F)"

    #Read data
    ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Deh(out)\2023CH6A_use.csv")
    ambientBase = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv")

    # Clean data
    ambient.replace("---.-", np.nan, inplace=True)
    ambient[var] = pd.to_numeric(ambient[var], errors='coerce')
    ambient.dropna(inplace=True)

    ambientBase.replace("---.-", np.nan, inplace=True)
    ambientBase[var] = pd.to_numeric(ambient[var], errors='coerce')
    ambientBase.dropna(inplace=True)


    # Filter time
    ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")
    month = int(month)
    day = int(day)
    input_date = datetime(year=2023, month=month, day=day)
    new_date = input_date + timedelta(days=1)
    ambient = ambient[ambient["Time"].between(input_date, new_date)]
    ambientBase["Time"] = pd.to_datetime(ambientBase["Time"], format="%m/%d/%y %H:%M")
    ambientBase = ambientBase[ambientBase["Time"].between(input_date, new_date)]
    day_avg_temperature = ambientBase.groupby("Time")[var].mean()
    print(day_avg_temperature)
    #Plot
    fig, ax1 = plt.subplots()
    ax1.plot(ambient["Time"], ambient[var], '-', label={var}, color="tab:red")
    vertical_line_time = pd.to_datetime("2023-07-18 12:00")
    ax1.axvline(x=vertical_line_time, color='red', linestyle='--')
    ax1.set_xlabel("Time")
    ax1.set_ylabel(var, color="tab:red")
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    ax1.legend(loc="upper left")
    #plt.axhline(y=day_avg_temperature, color='tab:blue', linestyle='--')
    plt.xticks(rotation=45)
    plt.title(f"{var} Vs. Time (H)")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    input('You will be prompted to enter a month and day after June 18th, 2023...press enter')
    month = input('Enter month: ')
    day = input('Enter day: ')
    varbool = input ('Enter T or H: (temperature or humidity) ')
    dehum_start_end(month, day, varbool)