import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import day_average as da

def dehum_start_end(start_date,end_date,write):

    # Read data
    temperature_data = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Deh(out)\2023CH6A_use.csv")
    dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehumidifier_Full_Data_New_Form.csv")

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
    dehum = dehum[dehum["Start Date"].between(formatted_date,formatted_date)]

    # Get the daily average temperature using the 'day_average' module
    day_avg_temperature = da.day_average(formatted_date, formatted_date2)

    # Plot
    fig, ax1 = plt.subplots()
    ax1.plot(temperature_data["Time"], temperature_data["Temperature(F)"], '-', label="Temperature(F)", color="tab:red")
    
    # Iterate through rows in dehum to add vertical lines
    date_is_within_df = dehum['Start Date'].between(formatted_date, formatted_date).any()

    if date_is_within_df:
        for _, row in dehum.iterrows():
            vertical_line_time = pd.to_datetime(formatted_date + ' ' + row["Start Time"])
            ax1.axvline(x=vertical_line_time, color='red', linestyle='--')

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

    if write == 'Y':
        formatted_date = formatted_date.replace('/', '_')
        plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\dehum_run\{formatted_date}_Temp@Deh_Out_vs_Time.png'
        plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
        print(f"Plot saved as '{plot_filename}'")

if __name__ == '__main__':
    start_date = input("Enter start date (e.g., 4/5/23): ")
    end_date = input("Enter end date (e.g., 4/6/23): ")
    write = input('Do you want to save this [Y/N]: ').upper()
    dehum_start_end(start_date,end_date,write)