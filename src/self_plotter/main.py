from data_loader import data_loader
from plotter import basic_plot, show_plot

basement_guest = r"C:\Users\ajayj\DehumGraph\data\Main Data\Base(guest).csv"
dehum_input = r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(in).csv"
dehum_output = r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(out).csv"
dehumdidifier = r"C:\Users\ajayj\DehumGraph\data\Main Data\Dehum.csv"

x_label = "Temperature(F)"
y_label = "Humidity(%)"

x,y,data_set = data_loader(x_label, y_label,dehum_input)

title = x_label + " vs. " + y_label

basic_plot(x, y, x_label, y_label, title)

show_plot()