import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil import parser

def day_average(input_date, new_date):
    # Read data
    ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv")

    # Clean data
    ambient.replace("---.-", np.nan, inplace=True)
    ambient["Temperature(F)"] = pd.to_numeric(ambient["Temperature(F)"], errors='coerce')
    ambient.dropna(inplace=True)

    # Filter time
    ambient["Time"] = ambient["Time"].apply(lambda x: parser.parse(x))  # Parse various date and time formats

    input_date = parser.parse(input_date)
    new_date = parser.parse(new_date)

    ambient = ambient[(ambient["Time"] >= input_date) & (ambient["Time"] <= new_date)]

    day_avg_temperature = ambient["Temperature(F)"].mean()

    print(day_avg_temperature)
    return day_avg_temperature

if __name__ == '__main__':
    input_date = input("Enter start date (e.g., 04/05/2023 14:49): ")
    new_date = input("Enter end date (e.g., 04/06/2023 14:49): ")
    print(day_average(input_date, new_date))