import pandas as pd
import numpy as np

# Assuming '2023CH1A.CSV' and 'Training.csv' are the file paths for your datasets
ch1_path = r"C:\Users\ajayj\DehumGraph\data\Training2.CSV"
training2_path = r"C:\Users\ajayj\DehumGraph\data\Training.csv"

# Load datasets
ch1_df = pd.read_csv(ch1_path)
training2_df = pd.read_csv(training2_path)


# Merge on the 'Time' column
merged_df = pd.merge(ch1_df, training2_df, on='Time', how='left', suffixes=('_front', '_base'))

# Save the merged dataframe to a new CSV file
merged_path = r"C:\Users\ajayj\DehumGraph\data\TrainingMerge.csv"
merged_df.to_csv(merged_path, index=False)

print(f"Merged data saved to: {merged_path}")
