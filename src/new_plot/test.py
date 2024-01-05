import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from data_loader import data_loader, custom_row, merge_time 

baseGuestPath = r"C:\Users\ajayj\DehumGraph\data\Base(guest).csv"
outPath = r"C:\Users\ajayj\DehumGraph\data\Deh(out).csv"

# Load data
baseGuest, _ = custom_row('Absolute Humidity(g/m^3)', baseGuestPath)
out, _ = custom_row('Temperature(F)', outPath)
new_data, _ = custom_row('Absolute Humidity(g/m^3)', baseGuestPath)

# Filter data based on specified date ranges
baseGuest = baseGuest[(baseGuest['Time'] >= '6/18/2023') & (baseGuest['Time'] <= '11/4/2023')]
out = out[(out['Time'] >= '6/18/2023') & (out['Time'] <= '11/4/2023')]
new_data = new_data[(new_data['Time'] >= '1/15/2019') & (new_data['Time'] <= '6/17/2023')]

merged_data = merge_time(baseGuest, out, 'Absolute Humidity(g/m^3)', 'Temperature(F)')

# Define features and target variable
X = merged_data[['Absolute Humidity(g/m^3)', 'Temperature(F)']]
y = (merged_data['Temperature(F)'] > 80).astype(int)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a logistic regression model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)

# Clean and preprocess the new data
new_data.replace("--", np.nan, inplace=True)
new_data['Absolute Humidity(g/m^3)'] = pd.to_numeric(new_data['Absolute Humidity(g/m^3)'], errors='coerce')
new_data.dropna(inplace=True)

# Ensure the features match the columns used during training
X_new = new_data[['Absolute Humidity(g/m^3)']]
X_new_scaled = scaler.transform(X_new)

# Make predictions on the new data
y_pred_new = model.predict(X_new_scaled)

# Now 'y_pred_new' contains the predicted labels for the new data
# You can use these predictions as needed for your application