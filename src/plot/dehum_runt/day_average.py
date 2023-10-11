import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def day_average(input_date, new_date):    
    
    # Read data
    ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Combine.csv")

    # Clean data
    ambient.replace("---.-", np.nan, inplace=True)
    ambient["Temperature(F)"] = pd.to_numeric(ambient["Temperature(F)"], errors='coerce')
    ambient.dropna(inplace=True)

    # Filter time
    ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")
    ambient = ambient[ambient["Time"].between(input_date, new_date)]

    day_avg_temperature = ambient["Temperature(F)"].mean()

    return day_avg_temperature

if __name__ == '__main__':
    input_date = input("input date:")
    new_date = input("new_date: ")
    print(day_average(input_date, new_date))