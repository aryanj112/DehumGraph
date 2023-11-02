import pandas as pd
import numpy as np

dehum_run = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehum_runtimes_update.csv")
dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehumidifier_Full_Data_New_Form.csv")
dehum_BEST = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehumidifer_Full_Data_Form_Runtime.csv")

def runtime_write(write):
    dehum_run['Date'] = pd.to_datetime(dehum_run['Date'], format='%m/%d/%Y')

    dehum_run['Dehumidifier Time 1'] = dehum_run['Run Zone 1'].apply(lambda x: int(x.split('-')[1]) - int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan)
    dehum_run['Dehumidifier Time 2'] = dehum_run['Run Zone 2'].apply(lambda x: int(x.split('-')[1]) - int(x.split('-')[0]) if isinstance(x, str) and '-' in x else np.nan)
    dehum_run['Dehumidifier Time 1'] = dehum_run['Dehumidifier Time 1'].fillna(0)
    dehum_run['Dehumidifier Time 2'] = dehum_run['Dehumidifier Time 2'].fillna(0)
    dehum["Runtime (hours)"] = dehum_run['Dehumidifier Time 1'] + dehum_run['Dehumidifier Time 2']

    if (write == 'Y'):
        plot_filename = fr'C:\Users\ajayj\DehumGraph\data\Dehumidifer_Full_Data_Form_Runtime.csv'
        dehum.to_csv(plot_filename, index=False)
        print(f"Plot saved as '{plot_filename}'")

if __name__ == '__main__':
    write = input('Do you want to save this [Y/N]: ').upper()
    runtime_write(write)