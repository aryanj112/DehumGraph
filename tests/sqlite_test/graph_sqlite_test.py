import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
from dateutil import parser
import sqlite3

#styling
from matplotlib import style
style.use('fivethirtyeight')
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
mpl.rcParams['lines.markersize'] = 2

def graph_data(df_file,table_name,col_x,col_y):
    conn = sqlite3.connect(df_file)
    c = conn.cursor()
    c.execute(f"SELECT {col_x}, {col_y} FROM {table_name}")    
    data = c.fetchall()

    dates = []
    temp = []

    for row in data:
        dates.append(parser.parse(row[0]))
        temp.append(row[1])

    plt.plot_date(dates,temp,'-')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    
    plt.xlabel("Time")
    plt.ylabel("Watt hrs")
    plt.title("Time vs. Watt hrs (Solaredge)") #Pepco

    #plt.xlabel("Date")
    #plt.ylabel("Temperature")
    #plt.title("Date vs. Temperature")

    plt.show()
    
    conn.close()
    c.close()

if __name__ == "__main__":
    df_file = r"C:\Users\ajayj\DehumGraph\database.sqlite3"
    table_name = "solaredge"
    col_x = "time"
    col_y = "watt_hrs"
    graph_data(df_file,table_name,col_x,col_y)