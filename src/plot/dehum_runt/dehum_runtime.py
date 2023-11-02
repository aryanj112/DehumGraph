import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import day_average as da

dehum_run = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehum_runtimes_update.csv")

def avg_time(write):
    dehum_run['Date'] = pd.to_datetime(dehum_run['Date'], format='%m/%d/%Y')

    dehum_run['Dehumidifier Time'] = dehum_run['Run Zone 1'].apply(lambda x: int(x.split('-')[1]) - int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan)

    daily_dehumidifier_time = dehum_run.groupby('Date')['Dehumidifier Time'].sum()

    plt.figure(figsize=(12, 6))
    plt.plot(daily_dehumidifier_time.index, daily_dehumidifier_time, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Added Dehumidifier Time (hours)')
    plt.title('Added Dehumidifier Time Each Day')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    avg_time(write)
