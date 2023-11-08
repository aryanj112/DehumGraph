import matplotlib.pyplot as plt
import pandas as pd

run_time = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\runtimes\dehum_rt_avg_AH_new.csv")
dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\efficiency\Dehumidifier_Full_Data_New - dehumidifer_full_data.csv")    

internal_color = "blue"
external_color = "red"


run_time["Date"] = pd.to_datetime(run_time["Date"], format="%Y-%m-%d")
dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])


start_date = pd.to_datetime('2022-10-14')
end_date = pd.to_datetime('2023-10-30') 

internal_data_run_time = run_time[run_time["Control Setting"] == "internal"]
external_data_run_time = run_time[run_time["Control Setting"] == "external"]

internal_data_run_time = internal_data_run_time.groupby(run_time["Date"].dt.date)["Average Absolute Humidity Zone 1"].mean()
external_data_run_time = external_data_run_time.groupby(run_time["Date"].dt.date)["Average Absolute Humidity Zone 1"].mean()

dehum_grouped = dehum.groupby("Start Date")["L/kWh"].mean()

internal_merged_data = pd.merge(dehum_grouped, internal_data_run_time, left_index=True, right_index=True, how="left")
external_merged_data = pd.merge(dehum_grouped, external_data_run_time, left_index=True, right_index=True, how="left")

#internal_merged_data = internal_merged_data[internal_merged_data["Start Date"].between(start_date, end_date)]
#external_merged_data = external_merged_data[external_merged_data["Start Date"].between(start_date, end_date)]

plt.figure()

plt.plot(internal_merged_data["Average Absolute Humidity Zone 1"], internal_merged_data["L/kWh"], 'o', label="internal control setting", color=internal_color)
plt.plot(external_merged_data["Average Absolute Humidity Zone 1"], external_merged_data["L/kWh"], 'o', label="external control setting", color=external_color)

plt.xlabel("Absolute Humidity [g/m^3]")
plt.ylabel("Efficiency [L/kWh]")
plt.title(f"Efficiency Vs. Absolute Humidity while Dehum. is running (guestroom)")
plt.legend()
plt.tight_layout()
plt.ylim(0,2)
plt.xlim(10,15)

plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\others\eff_vs_hum_runt_controls.png'
plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
print(f"Plot saved as '{plot_filename}'")

plt.show()

