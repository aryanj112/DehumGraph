import matplotlib.pyplot as plt
import pandas as pd

run_time = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\runtimes\dehum_rt_avg_AH_new.csv")
dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\efficiency\Dehumidifier_Full_Data_New - dehumidifer_full_data.csv")    

run_time["Date"] = pd.to_datetime(run_time["Date"], format="%Y-%m-%d")
dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])

start_date = pd.to_datetime('2022-10-14')
end_date = pd.to_datetime('2023-10-30') 
dehum = dehum[dehum["Start Date"].between(start_date, end_date)]

runtime_grouped = run_time.groupby(run_time["Date"].dt.date)["Average Absolute Humidity Zone 1"].mean()
dehum_grouped = dehum.groupby("Start Date")["L/kWh"].mean()
merged_data = pd.merge(dehum_grouped, runtime_grouped, left_index=True, right_index=True, how="left")

plt.figure()
plt.plot(merged_data["Average Absolute Humidity Zone 1"], merged_data["L/kWh"], 'o', label="Efficiency [L/kWh]", color="tab:blue")
plt.xlabel("Run Time Absolute Humidity [g/m^3]")
plt.ylabel("Efficiency [L/kWh]")
plt.title(f"Efficiency [L/kWh] Vs. Dehum. Running Absolute Humidity [g/m^3] (guestroom)")
plt.legend()
plt.tight_layout()
plt.ylim(0,2)
plt.xlim(10,15)
plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\others\eff_vs_hum_runt.png'
plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
print(f"Plot saved as '{plot_filename}'")

plt.show()


