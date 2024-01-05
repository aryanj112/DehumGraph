import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# File path for humidity and temperature data
baseGuestPath = r"C:\Users\ajayj\DehumGraph\data\Base(guest).csv"

combined_data_df = pd.read_csv(baseGuestPath)

# Specify the start and end dates for the desired range
start_date = '2023-06-18'
end_date = '2023-11-04'

# Convert the 'Time' column to datetime format (if not already)
combined_data_df['Time'] = pd.to_datetime(combined_data_df['Time'])

# Filter the DataFrame based on the date range
combined_data_df = combined_data_df[(combined_data_df['Time'] >= start_date) & (combined_data_df['Time'] <= end_date)]

# Assume you have a 'Running' column indicating if the dehumidifier is running at each time point
# Define features and target variable
X = combined_data_df[
    ['Time', 'Temperature(F)', 'Humidity(%)', 'Dewpoint(F)', 'HeatIndex(F)', 'Absolute Humidity(g/m^3)']
]
y = (combined_data_df['Running'] == 'Yes').astype(int)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train.iloc[:, 1:])  # Exclude 'Time' column from scaling
X_test_scaled = scaler.transform(X_test.iloc[:, 1:])

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