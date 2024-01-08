import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

var = "Absolute Humidity(g/m^3)"
var2 = "Humidity(%)"

def load_data(start_date, end_date):

    # Read the Dataframes
    guestroom = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Base(guest).csv")
    out = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Deh(out).csv")
    front = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Frontdoor.csv")

    # Clean the DataFrames
    guestroom.replace("--", np.nan, inplace=True)
    guestroom[var] = pd.to_numeric(guestroom[var], errors='coerce')
    guestroom.dropna(inplace=True)
    
    out.replace("--", np.nan, inplace=True)
    out['Temperature(F)'] = pd.to_numeric(out['Temperature(F)'], errors='coerce')
    out.dropna(inplace=True)    
    
    front.replace("--", np.nan, inplace=True)
    front['Absolute Humidity(g/m^3)'] = pd.to_numeric(front['Absolute Humidity(g/m^3)'], errors='coerce')
    #front.dropna(inplace=True)   

    # Convert the 'Time' column to datetime format
    guestroom['Time'] = pd.to_datetime(guestroom['Time'], format="%m/%d/%y %H:%M")
    out['Time'] = pd.to_datetime(out['Time'], format="%m/%d/%y %H:%M")
    front['Time'] = pd.to_datetime(front['Time'], format="%m/%d/%y %H:%M")

    # Filter the DataFrames based on the date range
    guestroom = guestroom[guestroom['Time'].between(start_date, end_date)]
    out = out[out['Time'].between(start_date, end_date)]
    front = front[front['Time'].between(start_date, end_date)]
    print (front)
    return guestroom, out, front

def plot(start_date, end_date, write):
    
    guestroom, out, front = load_data(start_date, end_date)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(out["Time"], out["Temperature(F)"], '-', label="Deh(out) Temperature [F]", color="tab:orange")
    ax1.set_ylabel("Deh(out) Temperature [F]", color="tab:orange")
    ax1.set_xlabel("Date and Time")

    ax2 = ax1.twinx()
    ax2.plot(guestroom["Time"], guestroom[var], '-', label=f"Guestroom {var}", color="tab:purple")
    ax2.set_ylabel(f"Guestroom {var}", color="tab:purple")

    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))  # Place ax3 to the right of ax1
    ax3.plot(front["Time"], front["Absolute Humidity(g/m^3)"], '-', label=f"Front Absolute Humidity(g/m^3)", color="tab:blue")
    ax3.set_ylabel(f"Front Absolute Humidity(g/m^3)", color="tab:blue")

    plt.title(f"Deh(Out) Temp Guest AH & Front AH Vs. Time (hourly)  {start_date}")

    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    plt.xticks(rotation=45, ha='right')

    # Show legends for both axes
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")

    # Manually adjust layout before saving
    fig.tight_layout()

    if write == 'Y':
        start_date_str = pd.to_datetime(start_date, format='%m/%d/%y').strftime('%#m/%#d/%y')
        start_date_str = start_date_str.replace('/', '_')
        plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\Guestroom AH Deh(out) Temp & Front AH Vs. Time\{start_date_str}_GuestHum_n_Temp@Deh_Out_vs_Time.png'
        
        # Save the figure directly
        fig.savefig(plot_filename, dpi=300)

        print(f"Plot saved as '{plot_filename}'")

    #plt.show()

if __name__ == '__main__':
    
    date_ranges1 = [
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
        ('7/13/23', '7/14/23')
    ]

    test = [
        ('5/23/20', '5/24/20')]
    
    for start_date, end_date in date_ranges1:
        print(f"\nPlotting for {start_date} to {end_date}")
        plot(start_date, end_date, 'Y')

    '''
    date_ranges2 = pd.date_range(start='1/15/19', end='1/18/19', freq='D')
    date_ranges3 = pd.date_range(start='10/9/19', end='11/4/23', freq='D')
    
    for date in date_ranges3:
        start_date = date.strftime('%m/%d/%y')
        end_date = (date + pd.Timedelta(days=1)).strftime('%m/%d/%y')
        
        print(f"\nPlotting for {start_date} to {end_date}")
        plot(start_date, end_date, 'N')
    
    '''