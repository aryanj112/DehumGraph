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
    ax1.set_ylim(bottom=70)  # Set the minimum y-axis limit to 0 for the first subplot

    ax2 = ax1.twinx()
    ax2.plot(guestroom["Time"], guestroom[var], '-', label=f"Guestroom {var}", color="tab:purple")
    ax2.set_ylabel(f"Guestroom {var}", color="tab:purple")
    #ax2.set_ylim(bottom=0)  # Set the minimum y-axis limit to 0 for the second subplot
    ax2.set_ylim(bottom=0, top=15)  # Set both minimum and maximum y-axis limits for the first subplot

    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))  # Place ax3 to the right of ax1
    ax3.plot(front["Time"], front["Absolute Humidity(g/m^3)"], '-', label=f"Front Absolute Humidity(g/m^3)", color="tab:blue")
    ax3.set_ylabel(f"Front Absolute Humidity(g/m^3)", color="tab:blue")
    ax3.set_ylim(bottom=0, top=30) 
    
    plt.title(f"Deh(Out) Temp Guest AH & Front AH Vs. Time {start_date} - {end_date}")

    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=4))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))  # Adjust the format as needed

    # Rotate the x-axis labels for better visibility
    for tick in ax1.get_xticklabels():
        tick.set_rotation(45)
        tick.set_ha('right')

    # Show legends for both axes
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")

    # Manually adjust layout before saving
    fig.tight_layout()

    if write == 'Y':
        start_date_str = pd.to_datetime(start_date, format='%m/%d/%y %H:%M').strftime('%#m/%#d/%y')
        start_date_str = start_date_str.replace('/', '_')
        plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\Guestroom AH Deh(out) Temp & Front AH Vs. Time\Zeroed\{start_date_str}_AH(Base & Front)_Temp(Oulet)_vs_Time.png'
        
        # Save the figure directly
        fig.savefig(plot_filename, dpi=300)

        print(f"Plot saved as '{plot_filename}'")
    #plt.show()

if __name__ == '__main__':

    bucketempty = [
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),

    ]
    
    runtime = [
        ('6/18/23 18:00', '6/22/23 2:00'),
        ('6/22/23 19:00', '6/24/23 5:00'),
        ('6/27/23 10:00', '6/28/23 1:00'),
        ('6/28/23 13:00', '6/29/23 9:00'),
        ('6/29/23 21:00', '7/1/23 3:00'),
        ('7/1/23 10:00', '7/2/23 9:00'),
        ('7/2/23 10:00', '7/3/23 13:00'),
        ('7/3/23 14:00', '7/4/23 7:00'),
        ('7/4/23 12:00', '7/5/23 6:00'),
        ('7/5/23 11:00', '7/6/23 7:00'),
        ('7/6/23 10:00', '7/7/23 11:00'),
        ('7/7/23 21:00', '7/8/23 19:00'),
        ('7/8/23 20:00', '7/9/23 21:00'),
        ('7/10/23 11:00', '7/12/23 5:00'),
        ('7/13/23 20:00', '7/14/23 14:00'),
        ('7/14/23 14:00', '7/15/23 12:00'),
        ('7/15/23 14:00', '7/16/23 5:00'),
        ('7/16/23 10:00', '7/16/23 23:00'),
        ('7/17/23 22:00', '7/18/23 18:00'),
        ('7/18/23 22:00', '7/19/23 19:00')
    ]

    #Come back to work on 7/20/23 12:00

    test = [
        ('6/27/23 10:00', '6/28/23 1:00')]
    
    for start_date, end_date in test:
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