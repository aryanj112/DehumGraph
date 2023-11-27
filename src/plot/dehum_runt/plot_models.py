import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

easy_eff_abshum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\efficiency\Fit Data Set - Sheet1.csv")

internal_color = "blue"
external_color = "red"

easy_eff_abshum["Date"] = pd.to_datetime(easy_eff_abshum["Date"], format="%m/%d/%Y")

internal_data_run_time = easy_eff_abshum[easy_eff_abshum["Control Setting"] == "internal"]
external_data_run_time = easy_eff_abshum[easy_eff_abshum["Control Setting"] == "external"]

internal_data_run_time = internal_data_run_time.groupby("Date")[["Avg Abs Hum", "L/kWh"]].mean().reset_index()
external_data_run_time = external_data_run_time.groupby("Date")[["Avg Abs Hum", "L/kWh"]].mean().reset_index()

def perform_linear_regression(data):
    X = data[["Avg Abs Hum"]]
    y = data["L/kWh"]

    model = LinearRegression()
    model.fit(X, y)

    return model

internal_model = perform_linear_regression(internal_data_run_time)
external_model = perform_linear_regression(external_data_run_time)

internal_slope, internal_intercept = internal_model.coef_[0], internal_model.intercept_
external_slope, external_intercept = external_model.coef_[0], external_model.intercept_


plt.figure()

plt.plot(internal_data_run_time["Avg Abs Hum"], internal_data_run_time["L/kWh"], 'o', label="internal control setting", color=internal_color)
plt.plot(external_data_run_time["Avg Abs Hum"], external_data_run_time["L/kWh"], 'o', label="external control setting", color=external_color)

#plt.plot(internal_data_run_time["Avg Abs Hum"], internal_model.predict(internal_data_run_time[["Avg Abs Hum"]]), color=internal_color)
#plt.plot(external_data_run_time["Avg Abs Hum"], external_model.predict(external_data_run_time[["Avg Abs Hum"]]), color=external_color)

# Plot the regression lines
plt.plot(internal_data_run_time["Avg Abs Hum"], internal_model.predict(internal_data_run_time[["Avg Abs Hum"]]), color=internal_color, label=f"Internal: y = {internal_slope:.2f}x + {internal_intercept:.2f}")
plt.plot(external_data_run_time["Avg Abs Hum"], external_model.predict(external_data_run_time[["Avg Abs Hum"]]), color=external_color, label=f"External: y = {external_slope:.2f}x + {external_intercept:.2f}")


plt.xlabel("Absolute Humidity [g/m^3]")
plt.ylabel("Efficiency [L/kWh]")
plt.title(f"Efficiency Vs. Absolute Humidity while Dehum. is running (guestroom)")
plt.legend()
plt.tight_layout()
plt.ylim(0,2)
plt.xlim(10,15)

plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\others\eff_vs_hum_runt_linreg.png'
plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
print(f"Plot saved as '{plot_filename}'")

plt.show()
