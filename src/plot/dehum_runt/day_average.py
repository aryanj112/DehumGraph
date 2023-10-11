import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def day_average(input_date, new_date):    
    # Define the date and time format
    print(input_date)
    print(new_date)

    date_time_format = "%m/%d/%y %H:%M"  # Assuming format is "month day year army time"

    # Read data
    ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv")

    # Clean data
    ambient.replace("---.-", np.nan, inplace=True)
    ambient["Temperature(F)"] = pd.to_numeric(ambient["Temperature(F)"], errors='coerce')
    ambient.dropna(inplace=True)

    # Filter time
    ambient["Time"] = pd.to_datetime(ambient["Time"], format=date_time_format)  # Use the specified format
    ambient = ambient[ambient["Time"].between(input_date, new_date)]

    day_avg_temperature = ambient["Temperature(F)"].mean()

    print(day_avg_temperature)
    return day_avg_temperature

if __name__ == '__main__':
    input_date = input("Enter start date (e.g., 04/05/2023 14:49): ")
    new_date = input("Enter end date (e.g., 04/06/2023 14:49): ")
    print(day_average(input_date, new_date))