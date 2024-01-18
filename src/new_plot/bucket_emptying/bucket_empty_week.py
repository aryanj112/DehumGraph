import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Assuming your dataset is stored in a DataFrame called df
df = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Master_BE.csv")

# Convert 'Bucket Empty' column to datetime format
df['Bucket Empty'] = pd.to_datetime(df['Bucket Empty'])

# Create an empty list to store the result
bucket_empty_list = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    bucket_empty_date = row['Bucket Empty']
    
    # Calculate the date exactly one week after the "Bucket Empty" date
    one_week_after = bucket_empty_date + pd.DateOffset(7)
    
    # Filter the DataFrame for "Bucket Empty" dates within the one-week period
    within_one_week = df[(df['Bucket Empty'] >= bucket_empty_date) & (df['Bucket Empty'] <= one_week_after)]['Bucket Empty'].tolist()
    
    # Append the result to the list
    bucket_empty_list.append([bucket_empty_date, one_week_after, within_one_week])

# Display the result
for item in bucket_empty_list:
    print(item)
    print("")

#var = "Humidity(%)"
var = "Absolute Humidity(g/m^3)"

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
    plt.show()

if __name__ == '__main__':

    for start_date, end_date, bucket_lines in bucket_empty_list:
        print(f"\nPlotting for {start_date} to {end_date}")
        plot(start_date, end_date, 'N')