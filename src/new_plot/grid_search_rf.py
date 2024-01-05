import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# File path for humidity and temperature data
baseGuestPath = r"C:\Users\ajayj\DehumGraph\data\Base(guest).csv"

# Load data
print("Loading data...")
humidity_temp_df = pd.read_csv(baseGuestPath)

# Specify the start and end dates for the desired range
start_date = '2023-06-18'
end_date = '2023-11-04'

# Convert the 'Time' column to datetime format (if not already)
print("Converting 'Time' to datetime format...")
humidity_temp_df['Time'] = pd.to_datetime(humidity_temp_df['Time'])

# Filter the DataFrame based on the date range
print("Filtering data based on date range...")
humidity_temp_df = humidity_temp_df[(humidity_temp_df['Time'] >= start_date) & (humidity_temp_df['Time'] <= end_date)]

# Feature Engineering: Create additional features or transformations
print("Performing feature engineering...")
humidity_temp_df['Hour'] = humidity_temp_df['Time'].dt.hour
humidity_temp_df['DayOfWeek'] = humidity_temp_df['Time'].dt.dayofweek

# Define features and target variable
X = humidity_temp_df[
    ['Temperature(F)', 'Humidity(%)', 'Dewpoint(F)', 'HeatIndex(F)', 'Absolute Humidity(g/m^3)', 'Hour', 'DayOfWeek']
]
y = (humidity_temp_df['Running'] == 'Yes').astype(int)

# Split the data into training and testing sets
print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
print("Standardizing features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Perform GridSearchCV for hyperparameter tuning
print("Performing GridSearchCV for hyperparameter tuning...")
rf_model = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(rf_model, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

# Print the best parameters and corresponding accuracy
best_params = grid_search.best_params_
best_accuracy = grid_search.best_score_
print(f"Best Parameters: {best_params}")
print(f"Best Accuracy: {best_accuracy}")

# Get the best model from the grid search
best_rf_model = grid_search.best_estimator_

# Make predictions on the test set
print("Making predictions on the test set...")
y_pred = best_rf_model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Final results
print("\nFinal Results:")
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)