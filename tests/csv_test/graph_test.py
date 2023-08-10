import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

dehum = pd.read_csv(r"C:\Users\ajayj\DehumGraph\data\dehumidifer_full_data.csv")

#Converting to date
'''
try:
    dehum['Start Date'] = pd.to_datetime(dehum['Start Date'], format=r'%m/%d/%y')
except ValueError:
    dehum['Start Date'] = pd.NaT
'''

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
mpl.rcParams['lines.markersize'] = 2

plt.plot(dehum['Start Date'], dehum['L/kWh'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('L/kWh')
plt.title('Efficiency Over Time')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.grid(True)
plt.show()