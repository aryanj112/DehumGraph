import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read data and perform preprocessing
ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Deh(out)\2023CH6A_use.CSV")

# Convert Time column to datetime
ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")
# Clean data
ambient.replace("--", np.nan, inplace=True)  # Replaces '--' with NaN values

# Use regular expression to filter out non-numeric values in Temperature(F) column
ambient = ambient[ambient["Temperature(F)"].str.match(r'\d+\.\d+')]

# Convert Temperature(F) column to numeric
ambient['Temperature(F)'] = pd.to_numeric(ambient['Temperature(F)'])

# Filter data to start from 2023-06-18
start_date = pd.to_datetime("2023-06-19")
end_date = pd.to_datetime("2023-06-20")
ambient = ambient[ambient["Time"].between(start_date, end_date)]

# Set up figure and axes
fig, ax1 = plt.subplots()

# Resample the data for smoother lines
resampled_data = ambient.set_index("Time").resample("10T").mean()  # Resample every 10 minutes

# Plot smoother line
ax1.plot(resampled_data.index, resampled_data["Temperature(F)"], '-', label="Temperature(F)", color="tab:red")

ax1.set_xlabel("Time")
ax1.set_ylabel("Temperature(F)", color="tab:red")

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Show Legend
ax1.legend(loc="upper left")

# Set plot title
plt.title("Smoothed Temperature Line Plot Vs. Time (2023)")

# Display the plot
plt.tight_layout()
plt.show()