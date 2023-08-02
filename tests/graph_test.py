import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
import sqlite3

#Used to make the graph look better
from matplotlib import style
style.use('fivethirtyeight')

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
    plt.show()
    
    conn.close()
    c.close()

if __name__ == "__main__":
    df_file = r"C:\Users\ajayj\DehumGraph\database.sqlite3"
    table_name = "solaredge"
    col_x = "time"
    col_y = "watt_hrs"
    graph_data(df_file,table_name,col_x,col_y)