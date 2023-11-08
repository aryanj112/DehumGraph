import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dehum_run = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehum_runtimes_update.csv")

def avg_time(write):
    dehum_run['Date'] = pd.to_datetime(dehum_run['Date'], format='%m/%d/%Y')

    dehum_run['Dehumidifier Time 1'] = dehum_run['Run Zone 1'].apply(lambda x: int(x.split('-')[1]) - int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan)
    dehum_run['Dehumidifier Time 2'] = dehum_run['Run Zone 2'].apply(lambda x: int(x.split('-')[1]) - int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan)
    dehum_run['Dehumidifier Time 1'] = dehum_run['Dehumidifier Time 1'].fillna(0)
    dehum_run['Dehumidifier Time 2'] = dehum_run['Dehumidifier Time 2'].fillna(0)
    dehum_run['Final'] = dehum_run['Dehumidifier Time 1'] + dehum_run['Dehumidifier Time 2']

    plt.figure(figsize=(12, 6))
    plt.plot(dehum_run['Date'], dehum_run['Final'], marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Added Dehumidifier Time (hours)')
    plt.title('Daily Dehumidifier Run Time')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.ylim(-1, 25)

    if (write == 'Y'):
        plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\others\Daily_Dehum_Run_Time.png'
        plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
        print(f"Plot saved as '{plot_filename}'")

    plt.show()

if __name__ == '__main__':
    write = input('Do you want to save this [Y/N]: ').upper()
    avg_time(write)