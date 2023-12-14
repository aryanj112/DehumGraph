import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Main Data\dehum_Avg_Rel_Hum.csv")

# Convert date columns to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Plotting
plt.scatter(data[data['Model'] == 'internal']['Avg Rel Hum Deh(in) - Deh(out)'],
            data[data['Model'] == 'internal']['Efficiency'],
            color='blue', label='Internal')

plt.scatter(data[data['Model'] == 'external']['Avg Rel Hum Deh(in) - Deh(out)'],
            data[data['Model'] == 'external']['Efficiency'],
            color='red', label='External')

plt.xlabel('Avg Rel Hum Deh(in) - Deh(out)')
plt.ylabel('Efficiency')
plt.legend()
plt.show()

# Linear Regression
internal_data = data[data['Model'] == 'internal']
external_data = data[data['Model'] == 'external']

X_internal = internal_data['Avg Rel Hum Deh(in) - Deh(out)'].values.reshape(-1, 1)
y_internal = internal_data['Efficiency'].values

X_external = external_data['Avg Rel Hum Deh(in) - Deh(out)'].values.reshape(-1, 1)
y_external = external_data['Efficiency'].values

model_internal = LinearRegression().fit(X_internal, y_internal)
model_external = LinearRegression().fit(X_external, y_external)

print('Internal Coefficients:', model_internal.coef_, model_internal.intercept_)
print('External Coefficients:', model_external.coef_, model_external.intercept_)
