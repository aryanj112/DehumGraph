import pandas as pd
from data_loader import data_loader, custom_row, merge_time 


baseGuestPath = r"C:\Users\ajayj\DehumGraph\data\Base(guest).csv"
outPath = r"C:\Users\ajayj\DehumGraph\data\Deh(out).csv"

# Load data
baseGuest, _ = custom_row('Absolute Humidity(g/m^3)', baseGuestPath)

# Filter data based on specified date ranges
baseGuest = baseGuest[(baseGuest['Time'] >= '6/18/2023') & (baseGuest['Time'] <= '11/4/2023')]
humidity_temp_df = baseGuest

# Sample dehumidifier runtime data
dehumidifier_runtime_df = pd.DataFrame({
    'Start Time': ['2023-01-01 00:10:00', '2023-01-01 00:30:00'],
    'End Time': ['2023-01-01 00:15:00', '2023-01-01 00:40:00']
})

# Convert columns to datetime
humidity_temp_df['Time'] = pd.to_datetime(humidity_temp_df['Time'])
dehumidifier_runtime_df['Start Time'] = pd.to_datetime(dehumidifier_runtime_df['Start Time'])
dehumidifier_runtime_df['End Time'] = pd.to_datetime(dehumidifier_runtime_df['End Time'])

# Initialize the "Running" column with 'No'
humidity_temp_df['Running'] = 'No'

# Check if each timestamp is within the runtime intervals
for _, runtime_row in dehumidifier_runtime_df.iterrows():
    mask = (humidity_temp_df['Time'] >= runtime_row['Start Time']) & (humidity_temp_df['Time'] <= runtime_row['End Time'])
    humidity_temp_df.loc[mask, 'Running'] = 'Yes'

# Print the resulting DataFrame
print(humidity_temp_df)
