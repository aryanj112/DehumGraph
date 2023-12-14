import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import statsmodels.api as sm

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

# Print the equation for internal line
internal_equation = f"Equation for internal line: Efficiency = {internal_slope:.4f} * (Avg Rel Hum Deh(in) - Deh(out)) + {internal_intercept:.4f}"
print(internal_equation)


# Fit the model for external data
regressor.fit(external_data_run_time_imputed, external_data_run_time["L/kWh"])
external_slope = regressor.coef_[0]
external_intercept = regressor.intercept_

# Print the equation for external line
external_equation = f"Equation for external line: Efficiency = {external_slope:.4f} * (Avg Rel Hum Deh(in) - Deh(out)) + {external_intercept:.4f}"
print(external_equation)

# Perform statistical tests
internal_X = sm.add_constant(internal_data_run_time_imputed)
internal_model = sm.OLS(internal_data_run_time["L/kWh"], internal_X).fit()

external_X = sm.add_constant(external_data_run_time_imputed)
external_model = sm.OLS(external_data_run_time["L/kWh"], external_X).fit()

# Save the values and regression results to a text document
with open(r'C:\Users\ajayj\DehumGraph\plots\Data\results.txt', 'w') as f:
    f.write(internal_equation + '\n\n')
    f.write(external_equation + '\n\n')
    f.write(internal_model.summary().as_text() + '\n\n')
    f.write(external_model.summary().as_text())

# Save data to a new DataFrame
result_data = pd.DataFrame({
    'Date': internal_data_run_time['Date'].tolist() + external_data_run_time['Date'].tolist(),
    'Control Setting': ['internal'] * len(internal_data_run_time) + ['external'] * len(external_data_run_time),
    'Avg Rel Hum Deh(in) - Deh(out)': internal_data_run_time['Avg Rel Hum Deh(in) - Deh(out)'].tolist() + external_data_run_time['Avg Rel Hum Deh(in) - Deh(out)'].tolist(),
    'L/kWh': internal_data_run_time['L/kWh'].tolist() + external_data_run_time['L/kWh'].tolist(),
    'Predicted Efficiency': internal_model.predict(sm.add_constant(internal_data_run_time_imputed)).tolist() + external_model.predict(sm.add_constant(external_data_run_time_imputed)).tolist()
})

# Save the DataFrame to a CSV file
result_data.to_csv(r'C:\Users\ajayj\DehumGraph\plots\Data\result_data.csv', index=False)

# Plot the scatter plot
plt.figure()
plt.plot(internal_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], internal_data_run_time["L/kWh"], 'o', label="internal control setting", color=internal_color)
plt.plot(external_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], external_data_run_time["L/kWh"], 'o', label="external control setting", color=external_color)

# Plot the linear regression lines
plt.plot(internal_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], internal_slope * internal_data_run_time_imputed + internal_intercept, color=internal_color, label=f"Internal Control Setting: y = {internal_slope:.4f} * x + {internal_intercept:.4f}")
plt.plot(external_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], external_slope * external_data_run_time_imputed + external_intercept, color=external_color, label=f"External Control Setting: y = {external_slope:.4f} * x + {external_intercept:.4f}")

plt.xlabel("Avg Rel Hum Deh(in) - Deh(out)")
plt.ylabel("Efficiency [L/kWh]")
plt.title(f"Efficiency Vs. Avg Rel Hum Deh(in) - Deh(out) (guestroom)")
plt.legend()
plt.tight_layout()
plt.ylim(0, 2)

plot_filename = fr'C:\Users\ajayj\DehumGraph\plots\others\Good graphs\eff_vs_outvin_linreg.png'
plt.savefig(plot_filename, dpi=500, bbox_inches='tight')   
print(f"Plot saved as '{plot_filename}'")

plt.show()