# Calculate Daily Absolute Humidity based on Dehum Runtimes

# For each day:
#   Get the time the dehumidifier is running
#   Get the absolute humidity for that time
#   Put the absolute humidiity as a meaned value and save it in a data set

import matplotlib as mlt
import pandas as pd
import numpy as np

ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv")
run_times = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehum_runtimes_update.csv")

'''
start_date = pd.to_datetime(f'2023-06-18')
end_date = pd.to_datetime(f'2023-8-14')
ambient = ambient[ambient["Time"].between(start_date, end_date)]
'''

run_times['RT1.1'] = run_times['Run Zone 1'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)
run_times['RT1.2'] = run_times['Run Zone 1'].apply(lambda x: int(x.split('-')[1]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)
run_times['RT2.1'] = run_times['Run Zone 2'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)
run_times['RT2.2'] = run_times['Run Zone 2'].apply(lambda x: int(x.split('-')[1]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)

print(run_times)

#abs_hum_avr_test = run_times[]

'''
run_times['Average Absolute Humidity'] = 

Assuming the 'Time Range' column in the 'time_ranges' DataFrame contains entries like "8-12"
time_ranges['Start Time'] = time_ranges['Time Range'].apply(lambda x: datetime.strptime(x.split('-')[0], '%H:%M'))
time_ranges['End Time'] = time_ranges['Time Range'].apply(lambda x: datetime.strptime(x.split('-')[1], '%H:%M'))


averages = []
for _, row in run_times.iterrows():
    start_time = row['Start Time']
    end_time = row['End Time']
    mask = (data['Timestamp'] >= start_time) & (data['Timestamp'] <= end_time)
    average_time = data.loc[mask, 'Value'].mean()
    averages.append(average_time)

time_ranges['Average Value'] = averages


for x in ambient:
    print(x)

'''
