#2022 april 22nd
# Make time stamps midnight

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

df = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Master_BE.csv")
df['Bucket Empty'] = pd.to_datetime(df['Bucket Empty'])
bucket_empty_list = []

for index, row in df.iterrows():
    bucket_empty_date = row['Bucket Empty']
    
    one_week_after = bucket_empty_date + pd.DateOffset(7)
    within_one_week = df[(df['Bucket Empty'] >= bucket_empty_date) & (df['Bucket Empty'] <= one_week_after)]['Bucket Empty'].tolist()
    bucket_empty_list.append([bucket_empty_date, one_week_after, within_one_week])

var = "Humidity(%)"
var = "Absolute Humidity(g/m^3)"
var = "Humidity(%)"


def load_data(start_date, end_date):

    # Read the Dataframes
    guestroom = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Base(guest).csv")
    out = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Deh(out).csv")
    front = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Frontdoor.csv")
    inlet = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Deh(in)_ABS.csv")


    # Clean the DataFrames
    guestroom.replace("--", np.nan, inplace=True)
    guestroom[var] = pd.to_numeric(guestroom[var], errors='coerce')   
    
    #out.replace("--", np.nan, inplace=True)
    #out["Temperature(F)"] = pd.to_numeric(out["Temperature(F)"], errors='coerce')   
    print(out)
    inlet.replace("--", np.nan, inplace=True)
    inlet[var] = pd.to_numeric(inlet[var], errors='coerce')   
    
    front.replace("--", np.nan, inplace=True)
    front['Absolute Humidity(g/m^3)'] = pd.to_numeric(front['Absolute Humidity(g/m^3)'], errors='coerce')

    # Convert the 'Time' column to datetime format
    guestroom['Time'] = pd.to_datetime(guestroom['Time'], format="%m/%d/%y %H:%M")
    front['Time'] = pd.to_datetime(front['Time'], format="%m/%d/%y %H:%M")
    inlet['Time'] = pd.to_datetime(inlet['Time'], format="%m/%d/%y %H:%M")
    out['Time'] = pd.to_datetime(front['Time'], format="%m/%d/%y %H:%M")

    # Filter the DataFrames based on the date range
    guestroom = guestroom[guestroom['Time'].between(start_date, end_date)]
    front = front[front['Time'].between(start_date, end_date)]
    inlet = inlet[inlet['Time'].between(start_date, end_date)]
    out = out[out['Time'].between(start_date, end_date)]
    print(out)

    return guestroom, front, inlet, out

def plot(start_date, end_date, write, bucket_lines_jaunt):
    guestroom, front, inlet, out = load_data(start_date, end_date)
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(out["Time"], out["Temperature(F)"], '-', label=f"Out Temperature(F)", color="tab:blue")
    ax1.set_ylabel(f"Temperature(F)", color="tab:blue")
#   ax1.set_yticks(np.linspace(70, 90, 11)) 

    ax2 = ax1.twinx()
    ax2.plot(inlet["Time"], inlet[var], '-', label=f"Guestroom {var}", color="tab:purple")
    ax2.set_ylabel(f"Guestroom {var}", color="tab:purple")
    ax2.spines['right'].set_position(('outward', 0))
    ax2.set_yticks(np.linspace(50, 75,5)) 

    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")

    for line_date in bucket_lines_jaunt:
        ax1.axvline(x=line_date, color='r', linestyle='--', linewidth=1, label='Bucket Empty Date')
        ax1.text(line_date, 23, f'{line_date:%m-%d %H:%M}', color='r', rotation=90, ha='right')

# Set the x-axis format with ticks every midnight and 12 hours before that
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))

    # Set minor ticks every 12 hours
    ax1.xaxis.set_minor_locator(mdates.HourLocator(byhour=[0, 12]))

    ax1.xaxis.set_major_locator(mdates.HourLocator(byhour=[0, 12]))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))

    plt.title(f"Inlet AH & Front AH Vs. Time {start_date} - {end_date}")

    # Rotate the x-axis labels for better visibility
    for tick in ax1.get_xticklabels():
        tick.set_rotation(45)
        tick.set_ha('right')

    fig.tight_layout()

    if write == 'Y':
        start_date_str = pd.to_datetime(start_date, format='%m/%d/%y %H:%M').strftime('%#m/%#d/%y')
        start_date_str = start_date_str.replace('/', '_')
        plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\seventeennew\{start_date_str}_AH(Base & Front)_Temp(Oulet)_vs_Time.png'
        
        # Save the figure directly
        fig.savefig(plot_filename, dpi=300)

        print(f"Plot saved as '{plot_filename}'")
    
    #plt.show()

if __name__ == '__main__':

    chosen_start_date = pd.to_datetime('2023-07-21 00:00')  # Replace with your desired start date

    for start_date, end_date, bucket_lines in bucket_empty_list:
        if start_date >= chosen_start_date:
            print(f"\nPlotting for {start_date} to {end_date}")
            plot(start_date, end_date, 'Y', bucket_lines)
        else:
            print(f"Skipping {start_date} as it is before the chosen start date.")