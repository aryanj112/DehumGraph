import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Load the data
data = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Main Data\dehum_Avg_Rel_Hum.csv")

# Convert date columns to datetime format
data['Date'] = pd.to_datetime(data['Date'])

filtered_data = data[data['Date'] > '2023-07-22']

internal_color = "blue"
external_color = "red"

data["Date"] = pd.to_datetime(data["Date"], format="%m/%d/%Y")

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





'''

# Linear Regression
internal_data = data[data['Model'] == 'internal']
external_data = data[data['Model'] == 'external']

X_internal = internal_data['Avg Rel Hum Deh(in) - Deh(out)'].values.reshape(-1, 1)
y_internal = internal_data['L/kWh'].values

X_external = external_data['Avg Rel Hum Deh(in) - Deh(out)'].values.reshape(-1, 1)
y_external = external_data['L/kWh'].values

model_internal = LinearRegression().fit(X_internal, y_internal)
model_external = LinearRegression().fit(X_external, y_external)

print('Internal Coefficients:', model_internal.coef_, model_internal.intercept_)
print('External Coefficients:', model_external.coef_, model_external.intercept_)


def perform_linear_regression(data):
    X = data[["Avg Rel Hum Deh(in) - Deh(out)"]]
    y = data["L/kWh"]

    model = LinearRegression()
    model.fit(X, y)

    return model

internal_model = perform_linear_regression(internal_data_run_time)
external_model = perform_linear_regression(external_data_run_time)

internal_slope, internal_intercept = internal_model.coef_[0], internal_model.intercept_
external_slope, external_intercept = external_model.coef_[0], external_model.intercept_

#plt.plot(internal_data_run_time["Avg Abs Hum"], internal_model.predict(internal_data_run_time[["Avg Abs Hum"]]), color=internal_color)
#plt.plot(external_data_run_time["Avg Abs Hum"], external_model.predict(external_data_run_time[["Avg Abs Hum"]]), color=external_color)

# Plot the regression lines
plt.plot(internal_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], internal_model.predict(internal_data_run_time[["Avg Rel Hum Deh(in) - Deh(out)"]]), color=internal_color, label=f"Internal: y = {internal_slope:.2f}x + {internal_intercept:.2f}")
plt.plot(external_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], external_model.predict(external_data_run_time[["Avg Rel Hum Deh(in) - Deh(out)"]]), color=external_color, label=f"External: y = {external_slope:.2f}x + {external_intercept:.2f}")


'''