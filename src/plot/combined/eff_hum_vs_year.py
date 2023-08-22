import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

def plot_eff_hum_vs_time(year, loc, show, write):
    # Load humidity and dehumidifier data
    dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehumidifier_Full_Data_New.csv")
    dtype_options = {'Temperature(F)': float, 'Humidity(%)': float, 'Dewpoint(F)': float, 'HeatIndex(F)': float, 'Absolute Humidity(g/m^3)': float}

    # Determine file path based on location
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

    # Filter data by date range
    dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])
    ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")
    start_date = pd.to_datetime(f'{year}-05-01')
    end_date = pd.to_datetime(f'{year}-11-30') 
    dehum = dehum[dehum["Start Date"].between(start_date, end_date)]
    ambient = ambient[ambient["Time"].between(start_date, end_date)]

    # Create a dual-axis plot
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # Plot efficiency on the first axis
    ax1.plot(ambient["Time"], ambient["Absolute Humidity(g/m^3)"], '-', label="Absolute Humidity [g/m^3]", color="tab:purple")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Absolute Humidity[g/m^3]", color="tab:blue")

    # Plot absolute humidity on the second axis
    ax2.set_ylim(0,2)
    ax2.plot(dehum["Start Date"], dehum["L/kWh"], label="Efficiency [L/kWh]", color="tab:blue")
    ax2.set_ylabel("Efficiency [L/kWh]", color="tab:blue")

    # Customize x-axis formatting
    ax1.xaxis.set_major_locator(mdates.MonthLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m"))

    # Combine legends
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc="upper left")

    # Set plot title
    plt.title(f"Absolute Humidity [g/m^3] Vs. Efficiency [L/kWh] ({loc}) (May To November {year})")
    
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
    loc = input("Enter a location to plot Effic Vs. A.H. (guestroom or frontdoor): ")
    show = input('Do you want to show this [Y/N]: ').upper() # Convert to uppercase for comparison
    write = input('Do you want to save this [Y/N]: ').upper()  # Convert to uppercase for comparison

    plot_eff_hum_vs_time(year, loc, show, write)