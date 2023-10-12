import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil import parser

def day_average(start_date,end_date):
    # Read data
    ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv")

    # Convert the date strings to datetime objects
    datetime1 = pd.to_datetime(start_date, format='%m/%d/%y')
    datetime2 = pd.to_datetime(end_date, format='%m/%d/%y')
    formatted_date = datetime1.strftime('%#m/%d/%y')
    formatted_date2 = datetime2.strftime('%#m/%d/%y')

    # Clean data
    ambient.replace("---.-", np.nan, inplace=True)
    ambient["Temperature(F)"] = pd.to_numeric(ambient["Temperature(F)"], errors='coerce')
    ambient.dropna(inplace=True)
    ambient = ambient[ambient["Time"].between(formatted_date, formatted_date2)]
    day_avg_temperature = ambient["Temperature(F)"].mean()

    return day_avg_temperature

if __name__ == '__main__':
    start_date = input("Enter start date (e.g., 4/5/23): ")
    end_date = input("Enter end date (e.g., 4/6/23): ")
    print(day_average(start_date,end_date))