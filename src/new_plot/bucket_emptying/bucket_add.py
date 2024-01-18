import pandas as pd

# Assuming your dataset is stored in a DataFrame called df
df = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Master_BE.csv")

# Convert 'Bucket Empty' column to datetime format
df['Bucket Empty'] = pd.to_datetime(df['Bucket Empty'])

# Create an empty list to store the result
bucket_empty_list = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    bucket_empty_date = row['Bucket Empty']
    
    # Calculate the date exactly one week after the "Bucket Empty" date
    one_week_after = bucket_empty_date + pd.DateOffset(7)
    
    # Filter the DataFrame for "Bucket Empty" dates within the one-week period
    within_one_week = df[(df['Bucket Empty'] >= bucket_empty_date) & (df['Bucket Empty'] <= one_week_after)]['Bucket Empty'].tolist()
    
    # Append the result to the list
    bucket_empty_list.append([bucket_empty_date, one_week_after, within_one_week])

# Display the result
for item in bucket_empty_list:
    print(item)
    print("")


