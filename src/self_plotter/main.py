from data_loader import data_loader, custom_row, merge_time
from plotter import basic_plot, show_plot, add_secondary_axis, save_plot
#from user_input import user_input

front_door = r"C:\Users\ajayj\DehumGraph\data\Main Data\Frontdoor.csv"
basement_guest = r"C:\Users\ajayj\DehumGraph\data\Main Data\Base(guest).csv"
dehum_input = r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(in).csv"
dehum_output = r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(out).csv"
dehumdidifier = r"C:\Users\ajayj\DehumGraph\data\Main Data\Dehum.csv"

x_label = "Time"
y_label= "L/kWh"

#x,data_set1 = custom_row(x_label, dehum_output)

#x,data_set1 = custom_row(x_label, basement_guest)
#x,data_set1 = custom_row(x_label, front_door)


#merge = merge_time(x,y,x_label,y_label)

#fig, ax1 = basic_plot(merge[x_label], merge[y_label], x_label, y_label, f"{y_label} vs. {x_label}")
#title = y_label + " vs. " + x_label

#x,y,dataset = data_loader(x_label, y_label,dehumdidifier)

x,y,dataset = data_loader(x_label, y_label,dehumdidifier)
fig, ax1 = basic_plot(x, y, x_label, y_label, f"{y_label} vs. {x_label}")

#y,data_set2 = custom_row(y_label, dehumdidifier)
#merge = merge_time(x,y,x_label,y_label)
#print(merge)

#fig, ax1 = basic_plot(y[x_label], y[y_label], x_label, y_label, f"{y_label} vs. {x_label}")


#print(merge)



#y2_label = "Temperature(F)"
#x,y,data_set = data_loader(x_label, y2_label,dehum_input)
#add_secondary_axis(fig, ax1, x, y, y2_label)
#save_plot(title)

show_plot()