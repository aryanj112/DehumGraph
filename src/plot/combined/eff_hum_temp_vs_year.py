import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from matplotlib.ticker import MaxNLocator

def plot_eff_hum_temp(year, loc, show, write, avg):
    dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehumidifier_Full_Data_New.csv")
    weather = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\netzero\weather_file.csv")
    
    dtype_options = {'Temperature(F)': float, 'Humidity(%)': float, 'Dewpoint(F)': float, 'HeatIndex(F)': float, 'Absolute Humidity(g/m^3)': float}
    if loc == 'guestroom':
        file_path = r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv"
    elif loc == 'frontdoor':
        file_path = r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Out_FR_door\CH1A_Absolute.csv"
    else:
        raise ValueError('Invalid location specified')

    # Read and preprocess ambient data
    ambient = pd.read_csv(file_path, dtype=dtype_options, low_memory=False)
    ambient.replace("'---.-'", np.nan, inplace=True)
    ambient['Absolute Humidity(g/m^3)'] = pd.to_numeric(ambient['Absolute Humidity(g/m^3)'], errors='coerce')
    ambient.dropna(inplace=True)
    
    dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])
    weather["date"] = pd.to_datetime(weather["date"])
    ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")
    
    # Filter data start and end time
    start_date = pd.to_datetime(f"{year}-05-01")
    end_date = pd.to_datetime(f"{year}-11-30") 
    dehum = dehum[dehum["Start Date"].between(start_date, end_date)]
    weather = weather[weather["date"].between(start_date, end_date)]
    ambient = ambient[ambient["Time"].between(start_date, end_date)]
    
    ambient["Date"] = ambient["Time"].dt.date
    daily_avg_humidity = ambient.groupby("Date")["Humidity(%)"].mean()
    daily_avg_temp = weather.groupby(weather["date"].dt.date)["temperature"].mean()

    fig, ax1 = plt.subplots()

    # Set the x-axis to show years
    ax1.xaxis.set_major_locator(mdates.MonthLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m"))

    ax1.set_ylim(0, 2)
    ax1.plot(dehum["Start Date"], dehum["L/kWh"], '-', label="Efficiency [L/kWh]", color="tab:blue")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Efficiency [L/kWh]", color="tab:blue")
    
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()

    temp_label = 'Temperature [°F]'
    hum_label = 'Absolute Humidity [g/m^3]'

    if avg == 'N':
        ax2.plot(weather["date"],weather["temperature"], '-',label = temp_label, color = "tab:red")
        ax3.plot(ambient["Time"], ambient["Absolute Humidity(g/m^3)"], '-', label= hum_label, color="tab:purple")
    else:
        temp_label = "Avg " + temp_label
        hum_label = "Avg " + hum_label
        ax2.plot(daily_avg_temp.index, daily_avg_temp.values, '-', label=temp_label, color="tab:red")
        ax3.plot(daily_avg_humidity.index, daily_avg_humidity.values, '-', label= hum_label, color="tab:purple")

    ax3.spines['right'].set_position(('outward', 80))
    ax3.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=15))
    
    ax2.set_ylabel(temp_label, color="tab:red")
    ax3.set_ylabel(hum_label, color="tab:purple")

    # Show Legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    lines3, labels3 = ax3.get_legend_handles_labels()
    ax1.legend(lines + lines2+lines3, labels + labels2 + labels3, loc="upper left")

    # Title and end
    plt.title(f"Efficiency [L/kWh], {temp_label}, {hum_label} ({loc}) (May To November {year})")
    fig.tight_layout()
    
    # Save the plot if requested
    if write == 'Y':
        plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\Effic_Vs_AH ({loc}) (May_Nov_{year}).png'
        plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
        print(f"Plot saved as '{plot_filename}'")
    
    # Show the plot if requested
    if show == 'Y':
        print("Plot is being dsiplayed")
        plt.show()

if __name__ == '__main__':
    year = input("Enter a year: ")
    loc = input("Enter a location to plot Effic Vs. A.H. [guestroom or frontdoor]: ")
    avg = input('Do you want to average the temperature and absolute humidity [Y/N]: ').upper()
    show = input('Do you want to show this [Y/N]: ').upper() 
    write = input('Do you want to save this [Y/N]: ').upper()

    plot_eff_hum_temp(year, loc, show, write, avg)
