import numpy as np
import pandas as pd

def data_loader (x_label, y_label, file_path):
    data_set = pd.read_csv(file_path)
    data_set.replace("---.-", np.nan, inplace = True)
    data_set.replace("--", np.nan, inplace = True)       
    numeric_columns = data_set.columns.difference(['Time'])
    data_set[numeric_columns] = data_set[numeric_columns].apply(pd.to_numeric, errors='coerce')
    if(file_path != r"C:\Users\ajayj\DehumGraph\data\Main Data\Dehum.csv"):
        data_set.dropna(inplace=True)
    data_set['Time'] = pd.to_datetime(data_set['Time'], format="%m/%d/%y %H:%M")
    x = data_set[x_label]
    y = data_set[y_label]
    return x, y, data_set

def custom_row(var, file_path):
    data_set = pd.read_csv(file_path)
    data_set.replace("---.-", np.nan, inplace = True)
    data_set.replace("--", np.nan, inplace = True)       
    numeric_columns = data_set.columns.difference(['Time'])
    data_set[numeric_columns] = data_set[numeric_columns].apply(pd.to_numeric, errors='coerce')
    #data_set.dropna(inplace=True)
    if(file_path != r"C:\Users\ajayj\DehumGraph\data\Main Data\Dehum.csv"):
        data_set.dropna(inplace=True)
    data_set["Time"] = pd.to_datetime(data_set['Time'], format="%m/%d/%y %H:%M")
    var = data_set[["Time", var]].copy()
    return var, data_set

def merge_time(x, y, x_label, y_label, average_overlapping=False):

    if average_overlapping:
        # Merge on date and time, and calculate the mean for overlapping values
        daily_avg = x.groupby(x['Time'].dt.date)[x_label].mean()
        y_grouped = y.groupby(y['Time'].dt.date)[y_label].mean()
        merged_data = pd.merge(y_grouped, daily_avg, left_index=True, right_index=True, how="left")
        merged_data.dropna(inplace=True)
    
    else:
        # Merge on date and time without averaging
        merged_data = pd.merge(y, x, on='Time', how='left')
        merged_data = merged_data[['Time', x_label, y_label]].dropna().reset_index(drop=True)
        merged_data.columns = ['Time', x_label, y_label]

    return merged_data