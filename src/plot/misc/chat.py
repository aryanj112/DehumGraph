import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

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

# Polynomial Regression (degree=2)
degree = 2
internal_model = make_pipeline(PolynomialFeatures(degree), regressor)
external_model = make_pipeline(PolynomialFeatures(degree), regressor)

# Split the data into training and testing sets
internal_X_train, internal_X_test, internal_y_train, internal_y_test = train_test_split(internal_data_run_time_imputed, internal_data_run_time["L/kWh"], test_size=0.2, random_state=42)
external_X_train, external_X_test, external_y_train, external_y_test = train_test_split(external_data_run_time_imputed, external_data_run_time["L/kWh"], test_size=0.2, random_state=42)

# Fit the model for internal data
internal_model.fit(internal_X_train, internal_y_train)
internal_predictions_train = internal_model.predict(internal_X_train)
internal_predictions_test = internal_model.predict(internal_X_test)

# Fit the model for external data
external_model.fit(external_X_train, external_y_train)
external_predictions_train = external_model.predict(external_X_train)
external_predictions_test = external_model.predict(external_X_test)

# Print the coefficients
internal_coefficients = internal_model.named_steps['linearregression'].coef_
external_coefficients = external_model.named_steps['linearregression'].coef_
print(f'Internal Coefficients: {internal_coefficients}')
print(f'External Coefficients: {external_coefficients}')

# Evaluate the model
internal_mse_train = mean_squared_error(internal_y_train, internal_predictions_train)
internal_mse_test = mean_squared_error(internal_y_test, internal_predictions_test)
external_mse_train = mean_squared_error(external_y_train, external_predictions_train)
external_mse_test = mean_squared_error(external_y_test, external_predictions_test)

print(f'Internal MSE (Train): {internal_mse_train:.4f}')
print(f'Internal MSE (Test): {internal_mse_test:.4f}')
print(f'External MSE (Train): {external_mse_train:.4f}')
print(f'External MSE (Test): {external_mse_test:.4f}')

# Plot the scatter plot with regression lines
plt.figure()

plt.scatter(internal_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], internal_data_run_time["L/kWh"], label="Internal Control Setting", color=internal_color)
plt.scatter(external_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], external_data_run_time["L/kWh"], label="External Control Setting", color=external_color)

# Plot the linear regression lines
plt.plot(internal_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], internal_model.predict(internal_data_run_time_imputed), color=internal_color, label=f"Internal Control Setting (Degree {degree})")
plt.plot(external_data_run_time["Avg Rel Hum Deh(in) - Deh(out)"], external_model.predict(external_data_run_time_imputed), color=external_color, label=f"External Control Setting (Degree {degree})")

plt.xlabel("Avg Rel Hum Deh(in) - Deh(out)")
plt.ylabel("Efficiency [L/kWh]")
plt.title(f"Efficiency Vs. Avg Rel Hum Deh(in) - Deh(out) (Guestroom)")
plt.legend()
plt.tight_layout()
plt.ylim(0, 2)

plt.show()
