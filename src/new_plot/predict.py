import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# File path for the original humidity and temperature data
base_guest_path = r"C:\Users\ajayj\DehumGraph\data\Base(guest).csv"

# Load the original data
original_data_df = pd.read_csv(base_guest_path)

# Specify the date range for filtering
start_date = '2019-01-15'
end_date = '2023-06-17'

# Convert the 'Time' column to datetime format
original_data_df['Time'] = pd.to_datetime(original_data_df['Time'])

# Filter the data based on the specified date range
filtered_data_df = original_data_df[(original_data_df['Time'] >= start_date) & (original_data_df['Time'] <= end_date)]

# Load the trained Random Forest model
# model_path = r"C:\Users\ajayj\DehumGraph\models\RandomForestClassifier84.joblib"
model_path = r"C:\Users\ajayj\DehumGraph\models\GirdSearch97.joblib"

loaded_model = joblib.load(model_path)

filtered_data_df['Hour'] = filtered_data_df['Time'].dt.hour
filtered_data_df['DayOfWeek'] = filtered_data_df['Time'].dt.dayofweek

# Define features for the new data
X_new = filtered_data_df[['Temperature(F)', 'Humidity(%)', 'Dewpoint(F)', 'HeatIndex(F)', 'Absolute Humidity(g/m^3)', 'Hour', 'DayOfWeek']]

# Standardize features
scaler = StandardScaler()
X_new_scaled = scaler.fit_transform(X_new)

# Make predictions on the new data
y_pred_new = loaded_model.predict(X_new_scaled)

# Add the predicted running status as a new column
filtered_data_df['Running'] = ['Yes' if pred == 1 else 'No' for pred in y_pred_new]

# Save the updated data to a new CSV file
# output_csv_path = r"C:\Users\ajayj\DehumGraph\data\old_data_with_running_status.csv"
output_csv_path = r"C:\Users\ajayj\DehumGraph\data\PredictedRuntime97.csv"
filtered_data_df.to_csv(output_csv_path, index=False)

print(f"Predictions saved to: {output_csv_path}")