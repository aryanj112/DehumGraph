import matplotlib.pyplot as plt
import pandas as pd

run_time = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehum_rt_avg_AH_new.csv")
dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehumidifier_Full_Data_New_Form.csv")    

run_time["Date_Only"] = pd.to_datetime(run_time["Date_Only"])
dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])

start_date = pd.to_datetime('2023-06-14')
end_date = pd.to_datetime('2023-8-18') 
dehum = dehum[dehum["Start Date"].between(start_date, end_date)]
dehum_grouped = dehum.groupby("Start Date")["L/kWh"].mean()
runtime_grouped = run_time.groupby("Date_Only")["Average Absolute Humidity Zone 1"].mean()

print(dehum_grouped)
print(runtime_grouped)

plt.figure()
#plt.plot(runtime_grouped.index, dehum_grouped, 'o', label="Efficiency [L/kWh]", color="tab:orange")66
#plt.plot(runtime_grouped["Average Absolute Humidity Zone 1"], dehum_grouped["L/kWh"], 'o', label="Efficiency [L/kWh]", color="tab:orange")
plt.xlabel("Run Time Absolute Humidity (g/m^3)")
plt.ylabel("Efficiency [L/kWh]")
plt.title(f"Efficiency [L/kWh] Vs. Dehum. Running Absolute Humidity (g/m^3) (guestroom)")
plt.legend()
plt.show()

