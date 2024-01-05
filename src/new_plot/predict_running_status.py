import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib


baseGuestPath = r"C:\Users\ajayj\DehumGraph\data\Base(guest).csv"

new_data_df = pd.read_csv(baseGuestPath)


start_date = '2019-01-15'
end_date = '2023-06-17'

new_data_df['Time'] = pd.to_datetime(new_data_df['Time'])

new_data_df = new_data_df[(new_data_df['Time'] >= start_date) & (new_data_df['Time'] <= end_date)]


# Load the trained Random Forest model
model_path = r"C:\Users\ajayj\DehumGraph\models\RandomForestClassifier84.joblib"  # Replace with the path to your trained model
loaded_model = joblib.load(model_path)

# Define features for the new data
X_new = new_data_df[['Temperature(F)', 'Humidity(%)', 'Dewpoint(F)', 'HeatIndex(F)', 'Absolute Humidity(g/m^3)']]

# Standardize features
scaler = StandardScaler()
X_new_scaled = scaler.fit_transform(X_new)

# Make predictions on the new data
y_pred_new = loaded_model.predict(X_new_scaled)

# Add the predicted running status as a new column
new_data_df['Running'] = ['Yes' if pred == 1 else 'No' for pred in y_pred_new]

# Save the updated data to a new CSV file
output_csv_path = r"C:\Users\ajayj\DehumGraph\data\old_data_with_running_status.csv"  # Replace with the desired output path
new_data_df.to_csv(output_csv_path, index=False)

print(f"Predictions saved to: {output_csv_path}")
