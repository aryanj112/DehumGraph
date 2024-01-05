import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def plot(start_date, end_date, write):

    var = "Humidity(%)"
    var = 'Absolute Humidity(g/m^3)'

    df = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\PredictedRuntime.csv")
    
    # Remove rows with missing or invalid values
    df.replace("--", np.nan, inplace=True)
    df[var] = pd.to_numeric(df[var], errors='coerce')
    df.dropna(subset=[var], inplace=True)
    
    # Convert the 'Time' column to datetime format
    df['Time'] = pd.to_datetime(df['Time'], format="%m/%d/%Y %H:%M")
    
    # Filter data based on date range
    df = df[df['Time'].between(start_date, end_date)]

    # Plot humidity
    fig, ax1 = plt.subplots()

    ax1.plot(df["Time"], df[var], '-', label=var, color="tab:purple")
    ax1.set_ylabel(var, color="tab:purple")
    ax1.tick_params('y', colors='tab:purple')
    
    min_humidity = df[var].min()
    max_humidity = df[var].max()

    # Adding the prediction plot for Running 84
    colors_84 = {'Yes': 'green', 'No': 'red'}
    ax1.scatter(df["Time"], [min_humidity-.5]*len(df), color=[colors_84[status] for status in df['Running 84']], alpha=0.5, marker='s')

    # Adding the prediction plot for Running 97
    colors_97 = {'Yes': 'green', 'No': 'red'}
    ax1.scatter(df["Time"], [max_humidity+.5]*len(df), color=[colors_97[status] for status in df['Running 97']], alpha=0.5, marker='s')

    # Adjust x-axis ticks
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    plt.xticks(rotation=45, ha='right')

    # Set lower limit of y-axis for humidity to 4
    ax1.set_ylim(min_humidity-.55, max_humidity+.55)

    plt.title(f"{var} Vs. Time (hourly) {start_date}")

    plt.tight_layout()

    if write == 'Y':
        # Convert start_date to datetime and then to the desired string format
        start_date_str = pd.to_datetime(start_date, format='%m/%d/%y').strftime('%#m/%#d/%y')
        start_date_str = start_date_str.replace('/', '_')
        plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\oldrunahguest\{start_date_str}_AH_vs_Time_Guest_Daily_modeldata.png'
        plt.savefig(plot_filename, dpi=500, bbox_inches='tight')
        print(f"Plot saved as '{plot_filename}'")
    
    #plt.show()

if __name__ == '__main__':

    date_ranges1 = pd.date_range(start='1/15/19', end='1/18/19', freq='D')
    date_ranges2 = pd.date_range(start='10/9/19', end='11/4/23', freq='D')
    
    for date in date_ranges2:
        start_date = date.strftime('%m/%d/%y')
        end_date = (date + pd.Timedelta(days=1)).strftime('%m/%d/%y')
        
        print(f"\nPlotting for {start_date} to {end_date}")
        plot(start_date, end_date, 'Y')
