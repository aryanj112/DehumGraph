import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Load the data
data = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Main Data\dehum_Avg_Rel_Hum.csv")

# Convert date columns to datetime format
data["Date"] = pd.to_datetime(data["Date"], format="%m/%d/%Y")
filtered_data = data[data['Date'] > '2023-07-22']

internal_color = "blue"
external_color = "red"
internal_data_run_time = data[data["Control Setting"] == "internal"]
external_data_run_time = data[data["Control Setting"] == "external"]

# Group by Date and compute the mean
internal_data_run_time = internal_data_run_time.groupby("Date")[["Avg Rel Hum Deh(in) - Deh(out)", "L/kWh"]].mean().reset_index()
external_data_run_time = external_data_run_time.groupby("Date")[["Avg Rel Hum Deh(in) - Deh(out)", "L/kWh"]].mean().reset_index()

# Handle missing values
imputer = SimpleImputer(strategy='mean')
internal_data_run_time_imputed = imputer.fit_transform(internal_data_run_time[["Avg Rel Hum Deh(in) - Deh(out)"]])
external_data_run_time_imputed = imputer.fit_transform(external_data_run_time[["Avg Rel Hum Deh(in) - Deh(out)"]])

# Create a linear regression model
regressor = LinearRegression()

# Fit the model for internal data
regressor.fit(internal_data_run_time_imputed, internal_data_run_time["L/kWh"])
internal_slope = regressor.coef_[0]
internal_intercept = regressor.intercept_

# Fit the model for external data
regressor.fit(external_data_run_time_imputed, external_data_run_time["L/kWh"])
external_slope = regressor.coef_[0]
external_intercept = regressor.intercept_

# Plot the scatter plot
plt.figure()
plt.plot(internal_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], internal_data_run_time["L/kWh"], 'o', label="internal control setting", color=internal_color)
plt.plot(external_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], external_data_run_time["L/kWh"], 'o', label="external control setting", color=external_color)

# Plot the linear regression lines
plt.plot(internal_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], internal_slope * internal_data_run_time_imputed + internal_intercept, color=internal_color)
plt.plot(external_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], external_slope * external_data_run_time_imputed + external_intercept, color=external_color)

plt.xlabel("Avg Rel Hum Deh(in) - Deh(out)")
plt.ylabel("Efficiency [L/kWh]")
plt.title(f"Efficiency Vs. Avg Rel Hum Deh(in) - Deh(out) (guestroom)")
plt.legend()
plt.tight_layout()
plt.ylim(0,2)

plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\others\Good graphs\eff_vs_outvin_linreg.png'
plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
print(f"Plot saved as '{plot_filename}'")

plt.show()