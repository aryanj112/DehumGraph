import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV data into a pandas DataFrame
weather = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\netzero\weather_file_new.csv")
weather["date"] = pd.to_datetime(weather["date"])
ambient_FR = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Out_FR_door\CH1A_Absolute.csv")
ambient_BASE = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv")

ambient_FR['Time'] = pd.to_datetime(ambient_FR['Time'], format="%m/%d/%y %H:%M")
ambient_BASE['Time'] = pd.to_datetime(ambient_BASE['Time'], format="%m/%d/%y %H:%M")

# Split the data into separate DataFrames for each station
station_a_data = weather[weather['station'] == 'GHCND:USW00093721']
station_b_data = weather[weather['station'] == 'GHCND:USW00093738']

# Create a plot with two subplots (one for each station)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

# Plot data for Station A on the first subplot
ax1.plot(station_a_data['date'], station_a_data['temperature'],'-', label='BALTIMORE WASHINGTON INTERNATIONAL AIRPORT, MD US')
ax1.set_ylabel('Temperature(F)')
ax1.legend()

# Plot data for Station B on the second subplot
ax2.plot(station_b_data['date'], station_b_data['temperature'], '-',label='WASHINGTON DULLES INTERNATIONAL AIRPORT, VA US', color="tab:orange")
ax2.set_ylabel('Temperature(F)')
ax2.legend()

ax3.plot(ambient_FR['Time'], ambient_FR['Temperature(F)'], '-',label='Front Door', color="tab:red")
ax3.set_ylabel('Temperature(F)')
ax3.legend()

ax4.plot(ambient_BASE['Time'], ambient_BASE['Temperature(F)'], '-',label='Basement Guest Room', color="tab:pink")
ax4.set_xlabel('Date')
ax4.set_ylabel('Temperature(F)')
ax4.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent overlapping labels
plt.tight_layout()
plt.title("Temperature(F) Vs. Time (Multiple Locations)")

plt.show()  # Display the plot