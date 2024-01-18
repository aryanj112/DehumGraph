import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

easy_eff_abshum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehum.csv")
internal_color = "blue"
external_color = "red"

easy_eff_abshum["Time"] = pd.to_datetime(easy_eff_abshum["Time"], format="%m/%d/%y %H:%M")

internal_data_run_time = easy_eff_abshum[easy_eff_abshum["Control Setting"] == "internal"]
external_data_run_time = easy_eff_abshum[easy_eff_abshum["Control Setting"] == "external"]

internal_data_run_time = internal_data_run_time.groupby("Time")[["Avg Abs Hum", "L/kWh"]].mean().reset_index()
external_data_run_time = external_data_run_time.groupby("Time")[["Avg Abs Hum", "L/kWh"]].mean().reset_index()

def perform_linear_regression(data):
    X = sm.add_constant(data[["Avg Abs Hum"]])  # Add a constant term to the independent variable
    y = data["L/kWh"]

    model = sm.OLS(y, X).fit()

    return model

internal_model = perform_linear_regression(internal_data_run_time)
external_model = perform_linear_regression(external_data_run_time)

# Print regression summary with statistics including p-values
print("Internal Control Setting Regression Summary:")
print(internal_model.summary())

print("\nExternal Control Setting Regression Summary:")
print(external_model.summary())

# Extracting slope and intercept
internal_slope, internal_intercept = internal_model.params[1], internal_model.params[0]
external_slope, external_intercept = external_model.params[1], external_model.params[0]

# Print p-values
print("\nInternal Control Setting p-values:")
print(internal_model.pvalues)

print("\nExternal Control Setting p-values:")
print(external_model.pvalues)


# Extracting slope and intercept
internal_slope, internal_intercept = internal_model.params[1], internal_model.params[0]
external_slope, external_intercept = external_model.params[1], external_model.params[0]

plt.figure()

plt.plot(internal_data_run_time["Avg Abs Hum"], internal_data_run_time["L/kWh"], 'o', label="internal control setting", color=internal_color)
plt.plot(external_data_run_time["Avg Abs Hum"], external_data_run_time["L/kWh"], 'o', label="external control setting", color=external_color)

# Plot the regression lines
plt.plot(internal_data_run_time["Avg Abs Hum"], internal_model.predict(sm.add_constant(internal_data_run_time[["Avg Abs Hum"]])), color=internal_color, label=f"Internal: y = {internal_slope:.2f}x + {internal_intercept:.2f}")
plt.plot(external_data_run_time["Avg Abs Hum"], external_model.predict(sm.add_constant(external_data_run_time[["Avg Abs Hum"]])), color=external_color, label=f"External: y = {external_slope:.2f}x + {external_intercept:.2f}")

print(f"Internal: y = {internal_slope:.2f}x + {internal_intercept:.2f}")
print(f"External: y = {external_slope:.2f}x + {external_intercept:.2f})")

plt.xlabel("Absolute Humidity [g/m^3]")
plt.ylabel("Efficiency [L/kWh]")
plt.title(f"Efficiency Vs. Absolute Humidity while Dehum. is running (guestroom)")
plt.legend()
plt.tight_layout()
plt.ylim(0, 2)
plt.xlim(10, 15)

plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\eff_vs_hum_runt_linreg.png'
plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
print(f"Plot saved as '{plot_filename}'")

plt.show()