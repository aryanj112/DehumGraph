import matplotlib.pyplot as plt
import pandas as pd

def plot_eff_hum(loc, show, write):
    dtype_options = {
        'Temperature(F)': float,
        'Humidity(%)': float,
        'Dewpoint(F)': float,
        'HeatIndex(F)': float,
        'Absolute Humidity(g/m^3)': float
    }

    if loc == 'guestroom':
        file_path = r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv"
    elif loc == 'frontdoor':
        file_path = r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Out_FR_door\CH1A_Absolute.csv"
    else:
        raise ValueError('Invalid location specified')

    dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehumidifier_Full_Data_New.csv")    
    ambient = pd.read_csv(file_path, dtype=dtype_options, low_memory=False)
    
    dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])
    ambient['Time'] = pd.to_datetime(ambient['Time'], format="%m/%d/%y %H:%M")

    daily_avg_humidity = ambient.groupby(ambient['Time'].dt.date)["Absolute Humidity(g/m^3)"].mean()
    dehum_grouped = dehum.groupby("Start Date")["L/kWh"].mean()
    
    merged_data = pd.merge(dehum_grouped, daily_avg_humidity, left_index=True, right_index=True, how="left")
    
    plt.figure()
    plt.plot(merged_data["Absolute Humidity(g/m^3)"], merged_data["L/kWh"], 'o', label="Efficiency [L/kWh]", color="tab:orange")
    plt.xlabel("Absolute Humidity [g/m^3]")
    plt.ylabel("Efficiency [L/kWh]")
    plt.title(f"Efficiency [L/kWh] Vs. Absolute Humidity [g/m^3] ({loc})")
    plt.legend()
    
    if write == 'Y':
        plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\Effic_Vs_AH ({loc}).png'
        plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
        print(f"Plot saved as '{plot_filename}'")
    
    if show == 'Y':
        print("Plot is being displayed")
        plt.show()

if __name__ == '__main__':
    loc = input("Enter a location to plot Effic Vs. A.H. (guestroom or frontdoor): ")
    show = input('Do you want to show this [Y/N]: ').upper()
    write = input('Do you want to save this [Y/N]: ').upper()

    plot_eff_hum(loc, show, write)
