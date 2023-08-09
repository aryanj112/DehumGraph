import pandas as pd

# Load CSV data from 2021
ambient_2021 = pd.read_csv("data/ambient_weather/2021CH1A_use.csv")

# Load CSV data from 2023
ambient_2023 = pd.read_csv("data/ambient_weather/2023CH1A_use.csv")


# Concatenate the two dataframes vertically
ambient_combine_data = pd.concat([ambient_2021, ambient_2023], ignore_index=True)

# Save the combined data to a new CSV file
ambient_combine_data.to_csv('ambient_combine_data.csv', index=False)

print("CSV files combined and saved to 'ambient_combine_data.csv'")
