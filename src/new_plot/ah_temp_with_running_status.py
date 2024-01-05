import pandas as pd
from data_loader import custom_row, merge_time 

baseGuestPath = r"C:\Users\ajayj\DehumGraph\data\Base(guest).csv"
runPath = r"C:\Users\ajayj\DehumGraph\data\Runtime.csv"

# Load data
humidity_temp_df, _ = custom_row('Absolute Humidity(g/m^3)', baseGuestPath)

# Filter data based on specified date ranges
humidity_temp_df = humidity_temp_df[(humidity_temp_df['Time'] >= '6/18/2023') & (humidity_temp_df['Time'] <= '11/4/2023')]
dehumidifier_runtime_df = pd.read_csv(runPath)

# Convert columns to datetime
humidity_temp_df['Time'] = pd.to_datetime(humidity_temp_df['Time'])
dehumidifier_runtime_df['Date'] = pd.to_datetime(dehumidifier_runtime_df['Date'], format="%m/%d/%Y")

# Create a 'Running' column and set default to 'No'
humidity_temp_df['Running'] = 'No'

# Iterate over each row in the runtime DataFrame
for index, row in dehumidifier_runtime_df.iterrows():
    # Iterate over runtime columns (assuming they are labeled as RT1.1, RT1.2, RT2.1, RT2.2, and so on)
    for i in range(1, 3):  # Modify the range to iterate until 2.1
        start_time_col = f"RT{i}.1"
        end_time_col = f"RT{i}.2"
        
        # Extract start and end times for the runtime period
        start_time = row[start_time_col]
        end_time = row[end_time_col]

        # Filter the humidity and temperature DataFrame based on the current runtime period
        mask = (humidity_temp_df['Time'] >= start_time) & (humidity_temp_df['Time'] <= end_time)

        # Set 'Running' column to 'Yes' for the rows within the current runtime period
        humidity_temp_df.loc[mask, 'Running'] = 'Yes'

# Now 'humidity_temp_df' contains a 'Running' column indicating whether the dehumidifier is running at each time point
print(humidity_temp_df)
# Assuming the DataFrame is named 'humidity_temp_df'
humidity_temp_df.to_csv(r"C:\Users\ajayj\DehumGraph\data\humidity_temp_with_running.csv", index=False)
