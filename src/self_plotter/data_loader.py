import numpy as np
import pandas as pd

def data_loader (x, y, file_path):
    data_set = pd.read_csv(file_path)
    data_set.replace("---.-", np.nan, inplace = True)
    data_set.replace("--", np.nan, inplace = True)       
    numeric_columns = data_set.columns.difference(['Time'])
    data_set[numeric_columns] = data_set[numeric_columns].apply(pd.to_numeric, errors='coerce')
    data_set.dropna(inplace=True)
    data_set['Time'] = pd.to_datetime(data_set['Time'], format="%m/%d/%y %H:%M")
    x = data_set[x]
    y = data_set[y]
    return x, y, data_set

def custom_row(var, file_path):
    data_set = pd.read_csv(file_path)
    data_set.replace("---.-", np.nan, inplace = True)
    data_set.replace("--", np.nan, inplace = True)       
    numeric_columns = data_set.columns.difference(['Time'])
    data_set[numeric_columns] = data_set[numeric_columns].apply(pd.to_numeric, errors='coerce')
    data_set.dropna(inplace=True)
    data_set['Time'] = pd.to_datetime(data_set['Time'], format="%m/%d/%y %H:%M")
    var = data_set[var]
    return var, data_set