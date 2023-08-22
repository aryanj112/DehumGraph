import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV data into a pandas DataFrame
weather = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\netzero\weather_file_new.csv")
weather["date"] = pd.to_datetime(weather["date"])

# Split the data into separate DataFrames for each station
station_a_data = weather[weather['station'] == 'GHCND:USW00093721']
station_b_data = weather[weather['station'] == 'GHCND:USW00093738']

# Create a plot with two subplots (one for each station)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot data for Station A on the first subplot
ax1.plot(station_a_data['date'], station_a_data['temperature'],'-', label='BALTIMORE WASHINGTON INTERNATIONAL AIRPORT, MD US')
ax1.set_ylabel('Temperature')
ax1.legend()

# Plot data for Station B on the second subplot
ax2.plot(station_b_data['date'], station_b_data['temperature'], '-',label='WASHINGTON DULLES INTERNATIONAL AIRPORT, VA US', color="tab:orange")
ax2.set_xlabel('Date')
ax2.set_ylabel('Temperature')
ax2.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent overlapping labels
plt.tight_layout()

plt.show()  # Display the plot