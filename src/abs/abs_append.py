import abs.absolutelute as myAbs
import pandas as pd

data_frame = pd.read_csv(r'data\ambient_weather/Base(guest)\CH7A_combine.csv')

# Calculate absolute humidity for each row and add it to a new column
abs_hum_values = []
for index, row in data_frame.iterrows():
    temp = row['Temperature(F)']  # Assuming 'temp' is the column name for temperature
    rel_hum = row['Humidity(%)']  # Assuming 'relhum' is the column name for relative humidity
    abs_hum = myAbs.cal_absHum(temp, rel_hum)
    abs_hum_values.append(abs_hum)

# Add the calculated values to a new column
data_frame['Absolute Humidity(%)'] = abs_hum_values

# Write the updated DataFrame back to a new CSV file
output_csv_path = 'CH7A_Absolute.csv'
data_frame.to_csv(output_csv_path, index=False)