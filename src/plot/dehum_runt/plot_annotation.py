import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the CSV file
easy_eff_abshum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\efficiency\Easy_Eff_Avg_AbsHum_New.csv")

# Convert the "Date" column to datetime format
easy_eff_abshum["Date"] = pd.to_datetime(easy_eff_abshum["Date"], format="%m/%d/%Y")

# Separate data based on control settings
internal_data_run_time = easy_eff_abshum[easy_eff_abshum["Control Setting"] == "internal"]
external_data_run_time = easy_eff_abshum[easy_eff_abshum["Control Setting"] == "external"]

# Group by date and calculate the mean of "Avg Abs Hum" and "L/kWh"
internal_data_run_time = internal_data_run_time.groupby("Date")[["Avg Abs Hum", "L/kWh"]].mean().reset_index()
external_data_run_time = external_data_run_time.groupby("Date")[["Avg Abs Hum", "L/kWh"]].mean().reset_index()

# Plotting
internal_color = "blue"
external_color = "red"

plt.figure()

# Plot the scatter points
plt.scatter(internal_data_run_time["Avg Abs Hum"], internal_data_run_time["L/kWh"], color=internal_color, label="internal control setting")
plt.scatter(external_data_run_time["Avg Abs Hum"], external_data_run_time["L/kWh"], color=external_color, label="external control setting")

# Annotate each point with the day and month
for i, row in internal_data_run_time.iterrows():
    plt.annotate(row["Date"].strftime("%b %d"), (row["Avg Abs Hum"], row["L/kWh"]), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8, color='black')

for i, row in external_data_run_time.iterrows():
    plt.annotate(row["Date"].strftime("%b %d"), (row["Avg Abs Hum"], row["L/kWh"]), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8, color='black')

plt.xlabel("Average Absolute Humidity")
plt.ylabel("Efficiency [L/kWh]")
plt.title("Efficiency Vs. Absolute Humidity while Dehum. is running (guestroom)")
plt.legend()
#plt.ylim(0,2)
#plt.xlim(10,15)
plt.tight_layout()


plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\others\eff_vs_hum_runt_ann_large.png'
plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
print(f"Plot saved as '{plot_filename}'")


plt.show()
