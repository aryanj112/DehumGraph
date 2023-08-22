import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load your CSV data into pandas DataFrames
    weather = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\netzero\weather_file_new.csv")
    weather["date"] = pd.to_datetime(weather["date"])
    ambient_FR = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Out_FR_door\CH1A_Absolute.csv")
    ambient_BASE = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv")

    ambient_FR['Time'] = pd.to_datetime(ambient_FR['Time'], format="%m/%d/%y %H:%M")
    ambient_BASE['Time'] = pd.to_datetime(ambient_BASE['Time'], format="%m/%d/%y %H:%M")

    # Split the data into separate DataFrames for each station
    station_a_data = weather[weather['station'] == 'GHCND:USW00093721']
    station_b_data = weather[weather['station'] == 'GHCND:USW00093738']

    # Ask user if they want overlayed plots or separate plots
    overlay_choice = input("Do you want overlayed plots (Y/N)? ").strip().lower()

    if overlay_choice == 'y':
        plot_overlayed(station_a_data, station_b_data, ambient_FR, ambient_BASE)
    else:
        plot_separate(station_a_data, station_b_data, ambient_FR, ambient_BASE)

def plot_overlayed(station_a_data, station_b_data, ambient_FR, ambient_BASE):
    fig, ax = plt.subplots(figsize=(10, 8))
    
    ax.plot(station_a_data['date'], station_a_data['temperature'], '-', label='BALTIMORE WASHINGTON INTERNATIONAL AIRPORT, MD US')
    ax.plot(station_b_data['date'], station_b_data['temperature'], '-', label='WASHINGTON DULLES INTERNATIONAL AIRPORT, VA US', color="tab:orange")
    ax.plot(ambient_FR['Time'], ambient_FR['Temperature(F)'], '-', label='Front Door', color="tab:red")
    ax.plot(ambient_BASE['Time'], ambient_BASE['Temperature(F)'], '-', label='Basement Guest Room', color="tab:pink")
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature(F)')
    ax.legend()
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.title("Temperature(F) Vs. Time (Overlayed)")

    plt.show()

def plot_separate(station_a_data, station_b_data, ambient_FR, ambient_BASE):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8), sharex=True)

    ax1.plot(station_a_data['date'], station_a_data['temperature'], '-', label='BALTIMORE WASHINGTON INTERNATIONAL AIRPORT, MD US')
    ax1.set_ylabel('Temperature(F)')
    ax1.legend()

    ax2.plot(station_b_data['date'], station_b_data['temperature'], '-', label='WASHINGTON DULLES INTERNATIONAL AIRPORT, VA US', color="tab:orange")
    ax2.set_ylabel('Temperature(F)')
    ax2.legend()

    ax3.plot(ambient_FR['Time'], ambient_FR['Temperature(F)'], '-', label='Front Door', color="tab:red")
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Temperature(F)')
    ax3.legend()

    ax4.plot(ambient_BASE['Time'], ambient_BASE['Temperature(F)'], '-', label='Basement Guest Room', color="tab:pink")
    ax4.set_xlabel('Date')
    ax4.set_ylabel('Temperature(F)')
    ax4.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.suptitle("Temperature(F) Vs. Time (Separate Locations)")
    plt.subplots_adjust(top=0.9)

    plt.show()

if __name__ == "__main__":
    main()