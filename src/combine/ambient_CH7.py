import pandas as pd
import numpy as np

# List of CSV file paths
csv_files = [
    r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\2019CH7A.CSV",    
    r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\2020CH7A.CSV",
    r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\2021CH7A.csv", 
    r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\2022CH7A.csv", 
    r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\2023CH7A.csv"
]

# Load and concatenate multiple CSV files
data_frames = [pd.read_csv(file, encoding='ISO-8859-1') for file in csv_files]
ambient_combine_data = pd.concat(data_frames, ignore_index=True)

# Clean data
ambient_combine_data.replace("--", np.nan, inplace=True) # Replaces -- with nan values
ambient_combine_data['Humidity(%)'] = pd.to_numeric(ambient_combine_data['Humidity(%)'], errors='coerce') # Convert humidity column to numeric values
ambient_combine_data.dropna(inplace=True) # Drops Nan values

# Save the combined data to a new CSV file
output_file_path = r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_combine.csv"
ambient_combine_data.to_csv(output_file_path, index=False)

print("CSV files combined and saved to 'CH7A_combine.csv'")