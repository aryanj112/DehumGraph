import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import day_average as da

def dehum_start_end(start_date,end_date,write):

    # Read data
    temperature_data = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Deh(out)\2023CH6ANEW.csv")
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
    plt.title(f"Temperature(F) at Deh(out) Vs. Time (H) ({formatted_date})")
    plt.tight_layout()

    if write == 'Y':
        formatted_date = formatted_date.replace('/', '_')
        plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\dehum_run\{formatted_date}_Temp@Deh_Out_vs_Time.png'
        plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
        print(f"Plot saved as '{plot_filename}'")

    #plt.show()

if __name__ == '__main__':
    #start_date = input("Enter start date (e.g., 4/5/23): ")
    #end_date = input("Enter end date (e.g., 4/6/23): ")
    #write = input('Do you want to save this [Y/N]: ').upper()
    #dehum_start_end(start_date,end_date,write)
    date_ranges = [
        ('6/18/23', '6/19/23'),
        ('6/19/23', '6/20/23'),
        ('6/20/23', '6/21/23'),
        ('6/21/23', '6/22/23'),
        ('6/22/23', '6/23/23'),
        ('6/23/23', '6/24/23'),
        ('6/24/23', '6/25/23'),
        ('6/25/23', '6/26/23'),
        ('6/26/23', '6/27/23'),
        ('6/27/23', '6/28/23'),
        ('6/28/23', '6/29/23'),
        ('6/29/23', '6/30/23'),
        ('6/30/23', '7/1/23'),
        ('7/1/23', '7/2/23'),
        ('7/2/23', '7/3/23'),
        ('7/3/23', '7/4/23'),
        ('7/4/23', '7/5/23'),
        ('7/5/23', '7/6/23'),
        ('7/6/23', '7/7/23'),
        ('7/7/23', '7/8/23'),
        ('7/8/23', '7/9/23'),
        ('7/9/23', '7/10/23'),
        ('7/10/23', '7/11/23'),
        ('7/11/23', '7/12/23'),
        ('7/12/23', '7/13/23'),
        ('7/13/23', '7/14/23'),
        ('7/14/23', '7/15/23'),
        ('7/15/23', '7/16/23'),
        ('7/16/23', '7/17/23'),
        ('7/17/23', '7/18/23'),
        ('7/18/23', '7/19/23'),
        ('7/19/23', '7/20/23'),
        ('7/20/23', '7/21/23'),
        ('7/21/23', '7/22/23'),
        ('7/22/23', '7/23/23'),
        ('7/23/23', '7/24/23'),
        ('7/24/23', '7/25/23'),
        ('7/25/23', '7/26/23'),
        ('7/26/23', '7/27/23'),
        ('7/27/23', '7/28/23'),
        ('7/28/23', '7/29/23'),
        ('7/29/23', '7/30/23'),
        ('7/30/23', '7/31/23'),
        ('7/31/23', '8/1/23'),
        ('8/1/23', '8/2/23'),
        ('8/2/23', '8/3/23'),
        ('8/3/23', '8/4/23'),
        ('8/4/23', '8/5/23'),
        ('8/5/23', '8/6/23'),
        ('8/6/23', '8/7/23'),
        ('8/7/23', '8/8/23'),
        ('8/8/23', '8/9/23'),
        ('8/9/23', '8/10/23'),
        ('8/10/23', '8/11/23'),
        ('8/11/23', '8/12/23'),
        ('8/12/23', '8/13/23'),
        ('8/13/23', '8/14/23'),
        ('8/14/23', '8/15/23')
    ]   

    date_ranges_p2 = [
        ('8/15/23', '8/16/23'),
        ('8/16/23', '8/17/23'),
        ('8/17/23', '8/18/23'),
        ('8/18/23', '8/19/23'),
        ('8/19/23', '8/20/23'),
        ('8/20/23', '8/21/23'),
        ('8/21/23', '8/22/23'),
        ('8/22/23', '8/23/23'),
        ('8/23/23', '8/24/23'),
        ('8/24/23', '8/25/23'),
        ('8/25/23', '8/26/23'),
        ('8/26/23', '8/27/23'),
        ('8/27/23', '8/28/23'),
        ('8/28/23', '8/29/23'),
        ('8/29/23', '8/30/23'),
        ('8/30/23', '8/31/23'),
        ('8/31/23', '9/1/23'),
        ('9/1/23', '9/2/23'),
        ('9/2/23', '9/3/23'),
        ('9/3/23', '9/4/23'),
        ('9/4/23', '9/5/23'),
        ('9/5/23', '9/6/23'),
        ('9/6/23', '9/7/23'),
        ('9/7/23', '9/8/23'),
        ('9/8/23', '9/9/23'),
        ('9/9/23', '9/10/23'),
        ('9/10/23', '9/11/23'),
        ('9/11/23', '9/12/23'),
        ('9/12/23', '9/13/23'),
        ('9/13/23', '9/14/23'),
        ('9/14/23', '9/15/23'),
        ('9/15/23', '9/16/23'),
        ('9/16/23', '9/17/23'),
        ('9/17/23', '9/18/23'),
        ('9/18/23', '9/19/23'),
        ('9/19/23', '9/20/23'),
        ('9/20/23', '9/21/23'),
        ('9/21/23', '9/22/23'),
        ('9/22/23', '9/23/23'),
        ('9/23/23', '9/24/23'),
        ('9/24/23', '9/25/23'),
        ('9/25/23', '9/26/23'),
        ('9/26/23', '9/27/23'),
        ('9/27/23', '9/28/23'),
        ('9/28/23', '9/29/23'),
        ('9/29/23', '9/30/23'),
        ('9/30/23', '10/1/23'),
        ('10/1/23', '10/2/23'),
        ('10/2/23', '10/3/23'),
        ('10/3/23', '10/4/23'),
        ('10/4/23', '10/5/23'),
        ('10/5/23', '10/6/23'),
        ('10/6/23', '10/7/23'),
        ('10/7/23', '10/8/23'),
        ('10/8/23', '10/9/23'),
        ('10/9/23', '10/10/23'),
        ('10/10/23', '10/11/23'),
        ('10/11/23', '10/12/23'),
        ('10/12/23', '10/13/23'),
        ('10/13/23', '10/14/23'),
        ('10/14/23', '10/15/23'),
        ('10/15/23', '10/16/23'),
        ('10/16/23', '10/17/23'),
        ('10/17/23', '10/18/23'),
        ('10/18/23', '10/19/23'),
        ('10/19/23', '10/20/23'),
        ('10/20/23', '10/21/23'),
        ('10/21/23', '10/22/23'),
        ('10/22/23', '10/23/23'),
        ('10/23/23', '10/24/23'),
        ('10/24/23', '10/25/23'),
        ('10/25/23', '10/26/23'),
        ('10/26/23', '10/27/23'),
        ('10/27/23', '10/28/23'),
        ('10/28/23', '10/29/23'),
        ('10/29/23', '10/30/23'),
        ('10/30/23', '10/31/23'),
        ('10/31/23', '11/1/23'),
        ('11/1/23', '11/2/23'),
        ('11/2/23', '11/3/23'),
        ('11/3/23', '11/4/23')
    ]
    last_date = [('11/4/23', '11/5/23')]
    for start_date, end_date in last_date:
        dehum_start_end(start_date, end_date, 'Y')  