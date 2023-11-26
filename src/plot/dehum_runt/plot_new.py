import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

easy_eff_abshum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\efficiency\Easy_Eff_Avg_AbsHum_New.csv")

internal_color = "blue"
external_color = "red"

easy_eff_abshum["Date"] = pd.to_datetime(easy_eff_abshum["Date"], format="%m/%d/%Y")

internal_data_run_time = easy_eff_abshum[easy_eff_abshum["Control Setting"] == "internal"]
external_data_run_time = easy_eff_abshum[easy_eff_abshum["Control Setting"] == "external"]

# Group by date and calculate the mean of "Avg Abs Hum" and "L/kWh"
internal_data_run_time = internal_data_run_time.groupby("Date")[["Avg Abs Hum", "L/kWh"]].mean().reset_index()
external_data_run_time = external_data_run_time.groupby("Date")[["Avg Abs Hum", "L/kWh"]].mean().reset_index()


plt.figure()

plt.plot(internal_data_run_time["Avg Abs Hum"], internal_data_run_time["L/kWh"], 'o', label="internal control setting", color=internal_color)
plt.plot(external_data_run_time["Avg Abs Hum"], external_data_run_time["L/kWh"], 'o', label="external control setting", color=external_color)

plt.xlabel("Absolute Humidity [g/m^3]")
plt.ylabel("Efficiency [L/kWh]")
plt.title(f"Efficiency Vs. Absolute Humidity while Dehum. is running (guestroom)")
plt.legend()
plt.tight_layout()
plt.ylim(0,2)
plt.xlim(10,15)

plt.show()
