import dp_conversion as dp
import pandas as pd

data_frame = pd.read_csv(r'data\ambient_weather\Out_FR_door\CH1A_new.csv')

# Calculate absolute humidity for each row and add it to a new column
dp_values = []
for index, row in data_frame.iterrows():
    temp = row['Temperature(F)']  # Assuming 'temp' is the column name for temperature
    rel_hum = row['Humidity(%)']  # Assuming 'relhum' is the column name for relative humidity
    dp = dp.cal_dewPnt(temp, rel_hum)
    dp_values.append(dp)

# Add the calculated values to a new column
data_frame['Calculated Dewpoint (F)'] = dp_values