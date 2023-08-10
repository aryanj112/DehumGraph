# Concating file that combines data from the data from CH1A in Ambient weather

import pandas as pd
import numpy as np

# List of CSV file paths
csv_files = [r"C:\Users\ajayj\DehumGraph\data\ambient_weather\2019CH1A_use.CSV",    
             r"C:\Users\ajayj\DehumGraph\data\ambient_weather\2020CH1A_use.CSV",
             r"C:\Users\ajayj\DehumGraph\data\ambient_weather\2021CH1A_use.csv", 
             r"C:\Users\ajayj\DehumGraph\data\ambient_weather\2022CH1A_use.csv", 
             r"C:\Users\ajayj\DehumGraph\data\ambient_weather\2023CH1A_use.csv"]

# Load and concatenate multiple CSV files
data_frames = [pd.read_csv(file) for file in csv_files]
ambient_combine_data = pd.concat(data_frames, ignore_index=True)

# Clean data
ambient_combine_data.replace("--",np.nan,inplace=True) # Replaces -- with nan values
ambient_combine_data['Humidity(%)'] = pd.to_numeric(ambient_combine_data['Humidity(%)'], errors='coerce') # Convert humidity column to numeric values
ambient_combine_data.dropna(inplace=True) # Drops Nan values

# Save the combined data to a new CSV file
ambient_combine_data.to_csv('ambient_combine_data.csv', index=False)

print("CSV files combined and saved to 'ambient_combine_data.csv'")
