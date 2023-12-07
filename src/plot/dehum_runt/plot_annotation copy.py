import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the CSV file
easy_eff_abshum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\efficiency\Easy_Eff_Avg_AbsHum_New.csv")

# Convert the "Date" column to datetime format
easy_eff_abshum["Date"] = pd.to_datetime(easy_eff_abshum["Date"], format="%m/%d/%Y")

# Separate data based on control settings (only external)
external_data_run_time = easy_eff_abshum[easy_eff_abshum["Control Setting"] == "external"]

# Extract month information from the "Date" column
external_data_run_time["Month"] = external_data_run_time["Date"].dt.month_name()

# Create a dictionary to map months to colors
month_color_mapping = {
    "July": "blue",
    "August": "green",
    "September": "orange",
    "October": "red"
}

# Plotting External Control Setting
plt.figure()

for month, color in month_color_mapping.items():
    month_data = external_data_run_time[external_data_run_time["Month"] == month]
    plt.scatter(month_data["Avg Abs Hum"], month_data["L/kWh"], color=color, label=f"{month} external control setting")

# Annotate each point with the day and month
for i, row in external_data_run_time.iterrows():
    plt.annotate(row["Date"].strftime("%b %d"), (row["Avg Abs Hum"], row["L/kWh"]), textcoords="offset points", xytext=(5, 5), ha='center', fontsize=8, color='black')

plt.xlabel("Average Absolute Humidity")
plt.ylabel("Efficiency [L/kWh]")
plt.title("Efficiency Vs. Absolute Humidity while Dehum. is running (external control sensor) (guestroom)")
plt.legend()
plt.ylim(0, 2)
plt.xlim(10, 15)
plt.tight_layout()

plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\others\eff_vs_hum_runt_ann_large_external_anno.png'
plt.savefig(plot_filename, dpi=500, bbox_inches='tight')
print(f"Plot saved as '{plot_filename}'")

plt.show()