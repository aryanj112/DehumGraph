import pandas as pd
import numpy as np

ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute.csv")
ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")
run_times = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehum_runtimes_update.csv")

run_times['RT1.1'] = run_times['Run Zone 1'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)
run_times['RT1.2'] = run_times['Run Zone 1'].apply(lambda x: int(x.split('-')[1]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)
run_times['RT2.1'] = run_times['Run Zone 2'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)
run_times['RT2.2'] = run_times['Run Zone 2'].apply(lambda x: int(x.split('-')[1]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)

start_time = pd.to_datetime('2023-06-18')
end_time = pd.to_datetime('2023-08-15')

run_times['Date'] = pd.to_datetime(run_times['Date'], format='%m/%d/%y %H:%M')
run_times['RT1.1'] = run_times['Date'] + pd.to_timedelta(run_times['RT1.1'], unit='h')
run_times['RT1.2'] = run_times['Date'] + pd.to_timedelta(run_times['RT1.2'], unit='h')

def calculate_mean(row):
    selected_data = ambient[
        (ambient['Time'] >= row['RT1.1']) &
        (ambient['Time'] <= row['RT1.2'])
    ]
    if not selected_data.empty:
        return selected_data['Absolute Humidity(g/m^3)'].mean()
    return np.nan

run_times['Average Absolute Humidity'] = run_times.apply(calculate_mean, axis=1)

mean_absolute_humidity = ambient[(ambient['Time'] >= start_time) & (ambient['Time'] <= end_time)]['Absolute Humidity(g/m^3)']
grouped = mean_absolute_humidity.groupby(ambient['Time']).mean()
print(grouped)
