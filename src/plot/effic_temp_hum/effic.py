import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def plot_effic(year, write):    
    dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\Dehumidifier_Full_Data_New.csv")
    dehum["Start Date"] = pd.to_datetime(dehum["Start Date"])

    start_date = pd.to_datetime(f'{year}-05-01')
    end_date = pd.to_datetime(f'{year}-11-30') 
    dehum = dehum[dehum["Start Date"].between(start_date, end_date)]

    fig, ax1 = plt.subplots()

    ax1.set_ylim(0, 2) 
    ax1.plot(dehum["Start Date"],dehum["L/kWh"], label = "Efficiency [L/kWh]", color = "tab:blue")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Efficiency [L/kWh]", color = "tab:blue")

    ax1.xaxis.set_major_locator(mdates.MonthLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m"))

    ax1.legend(loc = "upper left")

    plt.title(f"Time Vs. Efficiency [L/kWh] (May To November {year})")
    plt.show()

    # Save the plot as an image
    if write == 'Y':
        plot_filename = f"Time_Vs_Effic(May_Nov_{year})"  
        print(f"Plot saved as '{plot_filename}'")

if __name__ == '__main__':
    year = input("Enter a year: ")
    write = input('Do you want to save this [Y/N]: ')
    plot_effic(year, write)