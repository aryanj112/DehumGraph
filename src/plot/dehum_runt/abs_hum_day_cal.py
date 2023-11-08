#Averages abs hum per day based on the runtime

import pandas as pd
import numpy as np
import re

ambient = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\ambient_weather\Base(guest)\CH7A_Absolute_NEW.csv")
ambient["Time"] = pd.to_datetime(ambient["Time"], format="%m/%d/%y %H:%M")
#run_times = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehum_runtimes_update.csv")
run_times = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\runtimes\fin_dehum_runtimes.csv")

run_times['RT1.1'] = run_times['Run Zone 1'].apply(lambda x: float(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan).fillna(0.0)
run_times['RT1.2'] = run_times['Run Zone 1'].apply(lambda x: float(x.split('-')[1]) if isinstance(x, str) and '-' in x else np.nan).fillna(0.0)

#run_times['RT1.1'] = run_times['Run Zone 1'].apply(lambda x: int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)
#run_times['RT1.2'] = run_times['Run Zone 1'].apply(lambda x: int(x.split('-')[1]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)
run_times['RT2.1'] = run_times['Run Zone 2'].apply(lambda x: float(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)
run_times['RT2.2'] = run_times['Run Zone 2'].apply(lambda x: float(x.split('-')[1]) if isinstance(x, str) and '-' in x else np.nan).fillna(0)

run_times['Date'] = pd.to_datetime(run_times['Date'], format='%m/%d/%y')
run_times['RT1.1'] = run_times['Date'] + pd.to_timedelta(run_times['RT1.1'], unit='h')
run_times['RT1.2'] = run_times['Date'] + pd.to_timedelta(run_times['RT1.2'], unit='h')
run_times['RT2.1'] = run_times['Date'] + pd.to_timedelta(run_times['RT2.1'], unit='h')
run_times['RT2.2'] = run_times['Date'] + pd.to_timedelta(run_times['RT2.2'], unit='h')

def calculate_mean(row, zone):
    selected_data = ambient[
        (ambient['Time'] >= row[f'RT{zone}.1']) &
        (ambient['Time'] <= row[f'RT{zone}.2'])
    ]
    if not selected_data.empty:
        return selected_data['Absolute Humidity(g/m^3)'].mean()
    return np.nan

run_times['Average Absolute Humidity Zone 1'] = run_times.apply(lambda row: calculate_mean(row, 1), axis=1)
run_times['Average Absolute Humidity Zone 2'] = run_times.apply(lambda row: calculate_mean(row, 2), axis=1)

run_times['Date_Only'] = run_times['Date'].dt.date
grouped = run_times.set_index('Date_Only')
grouped.fillna(0)
plot_filename = fr'dehum_rt_avg_AH_new.csv'
grouped.to_csv(plot_filename, index=False)
print(f"Plot saved as '{plot_filename}'")