import pandas as pd
import numpy as np

dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Main Data\Dehum.csv")
outlet = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(out).csv")
inlet = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(in).csv")

dehum["Date"] = pd.to_datetime(dehum["Date"], format="%m/%d/%Y")
outlet["Time"] = pd.to_datetime(outlet["Time"], format="%m/%d/%y %H:%M")
inlet["Time"] = pd.to_datetime(inlet["Time"], format="%m/%d/%y %H:%M")

outlet.replace("---.-", np.nan, inplace=True)
inlet.replace("---.-", np.nan, inplace=True)

outlet["Humidity(%)"] = pd.to_numeric(outlet["Humidity(%)"], errors='coerce')
inlet["Humidity(%)"] = pd.to_numeric(inlet["Humidity(%)"], errors='coerce')

outlet.dropna(inplace=True)
inlet.dropna(inplace=True)

def day_average(input_date):
    input_date = pd.to_datetime(input_date, format="%m/%d/%Y")
    
    # Filter dehum data for the given date
    dehum_subset = dehum[dehum["Date"] == input_date]
    
    if dehum_subset.empty:
        return "No data available for the given date."
    
    # Extract R1.1, R1.2, R2.1, and R2.2 values
    r1_1 = dehum_subset["R 1.1"].values[0]
    r1_2 = dehum_subset["R 1.2"].values[0]
    r2_1 = dehum_subset["R 2.1"].values[0]
    r2_2 = dehum_subset["R 2.2"].values[0]
    
    # Filter outlet data based on R1.1, R1.2, R2.1, and R2.2 values
    outlet_subset_r1 = outlet[(outlet["Time"] >= r1_1) & (outlet["Time"] <= r1_2)]
    outlet_subset_r2 = outlet[(outlet["Time"] >= r2_1) & (outlet["Time"] <= r2_2)]

    if outlet_subset_r1.empty and outlet_subset_r2.empty:
        return "No outlet humidity data available for the given date."
    
    inlet_subset_r1 = inlet[(inlet["Time"] >= r1_1) & (inlet["Time"] <= r1_2)]
    inlet_subset_r2 = inlet[(inlet["Time"] >= r2_1) & (inlet["Time"] <= r2_2)]

    if inlet_subset_r1.empty and inlet_subset_r2.empty:
        return "No outlet humidity data available for the given date."

    # Calculate average humidity for the filtered outlet data
    day_avg_outlet_r1 = outlet_subset_r1["Humidity(%)"].mean()
    day_avg_outlet_r2 = outlet_subset_r2["Humidity(%)"].mean()
    
    # Calculate average humidity for the filtered inlet data
    day_avg_inlet_r1 = inlet_subset_r1["Humidity(%)"].mean()
    day_avg_inlet_r2 = inlet_subset_r2["Humidity(%)"].mean()

    # Calculate the overall average humidity for both cycles

    nancheck = [day_avg_outlet_r1, day_avg_outlet_r2, day_avg_inlet_r1, day_avg_inlet_r2]

    # Check for NaN values and set them to 0
    nancheck = [0 if pd.isna(val) else val for val in nancheck]

    # Check if both values are not 0 before averaging
    if nancheck[0] != 0 and nancheck[1] != 0:
        overall_avg_outlet = (nancheck[0] + nancheck[1]) / 2
    else:
        overall_avg_outlet = nancheck[0]  # Set to the non-zero value or 0 if both are 0

    # Check if both values are not 0 before averaging
    if nancheck[2] != 0 and nancheck[3] != 0:
        overall_avg_inlet = (nancheck[2] + nancheck[3]) / 2
    else:
        overall_avg_inlet = nancheck[2]  # Set to the non-zero value or 0 if both are 0



    return overall_avg_inlet - overall_avg_outlet

if __name__ == '__main__':
    input_date = input("Enter date (e.g., 7/18/2023): ")
    print("Average Humidity(%) of the Deh(in) - Deh(out): ")
    print(day_average(input_date))
