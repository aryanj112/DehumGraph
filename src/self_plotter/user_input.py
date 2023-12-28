from plotter import basic_plot, show_plot
import time
from data_loader import data_loader, merge_time, custom_row
#from config import FILE_CONFIG, NICK_NAME

NICK_NAME = {
    'FR_DOOR': 'front_door_path',
    'BASE': 'basement_guest_path',
    'Input': 'dehum_input_path', 
    'Output': 'dehum_output_path', 
    'Dehum': 'dehumidifier_path',
}

FILE_CONFIG = {
    'FR_DOOR': r"C:\Users\ajayj\DehumGraph\data\Main Data\Frontdoor.csv",
    'BASE': r"C:\Users\ajayj\DehumGraph\data\Main Data\Base(guest).csv",
    'Input': r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(in).csv",
    'Output': r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(out).csv",
    'Dehum': r"C:\Users\ajayj\DehumGraph\data\Main Data\Dehum.csv",
}

def potential_vars (loc):
    
    ambient_vars = ["Temperature(F)", "Humidity(%)", "Dewpoint(F)", "HeatIndex(F)", "Absolute Humidity(g/m^3)"]
    dehum_vars = ["L/kWh", "Avg Abs Hum", "Avg Rel Hum Deh(in) - Deh(out)"]
    
    type_writer(f"Here are the potential variables you can plot for {loc}:")
    
    if loc in ["FR_DOOR", "BASE", "Input", "Output"]:
        for var in ambient_vars:
            type_writer(f"- [{var}]")

    elif loc == "Dehum":
        for var in dehum_vars:
            type_writer(f"- [{var}]")

    var = input("Select a variable: ")
    return var

def type_writer(text, delay=0.0):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_user_input():
    type_writer("Welcome to the  Dehumidifier Graph program.")
    type_writer("Here, you can visualize data from different sources, including:")
    type_writer("- Front Door [FR_DOOR]")
    type_writer("- Basement [BASE]")
    type_writer("- Dehumidifier Input [Input]")
    type_writer("- Dehumidifier Output [Output]")
    type_writer("- Dehumidifier [Dehum]")
    type_writer("\nExplore and plot various pieces of information with ease!")
    type_writer("\nTo begin, would you prefer to view the trend of a variable over time [var_time] or compare that variable against another variable? [var_var]")
    type_writer("Note: Choices are indicated within square brackets.")
    against = input("[var_time] or [var_var]: ")

    if against == "var_time":
        type_writer("\nWhere would you like to visualize data:")
        type_writer("- Front Door [FR_DOOR]")
        type_writer("- Basement [BASE]")
        type_writer("- Dehumidifier Input [Input]")
        type_writer("- Dehumidifier Output [Output]")
        type_writer("- Dehumidifier [Dehum]")
        loc = input()
        if loc in ["FR_DOOR", "BASE", "Input", "Output"]:
            type_writer("Here are the potential variables you can plot:")
            type_writer("- [Temperature(F)]")
            type_writer("- [Humidity(%)]")
            type_writer("- [Dewpoint(F)]")
            type_writer("- [HeatIndex(F)]")
            type_writer("- [Absolute Humidity(g/m^3)]")
            plot_var = input("Select a variable: ")
            type_writer("Indicate a time zone you would like to plot these on: ")
            #start_date = input()
            #end_date = input()
            
            type_writer("Do you want to add a secondary axis? [Y] or [N]")
            add_secondary = input()
            if add_secondary == "Y":
                type_writer("Do you want to add a tertiary axis? [Y] or [N]")
                add_tertiary = input()
            elif add_secondary == "N":
                x_label = 'Time'
                y_label = plot_var
                file_path = FILE_CONFIG[loc]
                x, y, dataset = data_loader(x_label, y_label, file_path)
                title = f"{y_label} vs. {x_label} at {loc}"
                basic_plot(x, y, x_label, y_label, title)
                show_plot()
            else:
                print('Invalid choice')
        elif loc == "Dehum":
            type_writer("Here are the potential variables you can plot:")
            type_writer("- [L/kWh]")
            type_writer("- [Avg Abs Hum]")
            type_writer("- [Avg Rel Hum Deh(in) - Deh(out)]")
            plot_var = input("Select a variable: ")
            type_writer("Indicate a time zone you would like to plot these on: ")
            #start_date = input()
            #end_date = input()     
            
            type_writer("Do you want to add a secondary axis? [Y] or [N]")
            add_secondary = input()
            if add_secondary == "Y":
                type_writer("Do you want to add a tertiary axis? [Y] or [N]")
                add_tertiary = input()
            elif add_secondary == "N":
                x_label = 'Time'
                y_label = f'{plot_var}'
                file_path = FILE_CONFIG[loc]
                print(file_path)
                x, y, dataset = data_loader(x_label, y_label, file_path)
                title = f"{y_label} vs. {x_label} at {loc}"
                basic_plot(x, y, x_label, y_label, title)
                show_plot()
            else:
                print('Invalid choice')
        else:
            print('Invalid location')

    elif against == "var_var":
        type_writer("\n What is the first location you would like to visualize data:")
        type_writer("- Front Door [FR_DOOR]")
        type_writer("- Basement [BASE]")
        type_writer("- Dehumidifier Input [Input]")
        type_writer("- Dehumidifier Output [Output]")
        type_writer("- Dehumidifier [Dehum]")
        first_loc = input()
        type_writer("\n What is the second location you would like to visualize data:")
        second_loc = input()
        loc = [first_loc, second_loc]
        var_var = []
        for single_loc in loc:
            plot_var = potential_vars(single_loc)
            var_var.append(plot_var)
                
            '''
            type_writer("Indicate a time zone you would like to plot these on: ")
            #start_date = input()
            #end_date = input()
            
            type_writer("Do you want to add a secondary axis? [Y] or [N]")
            add_secondary = input()
            if add_secondary == "Y":
                type_writer("Do you want to add a tertiary axis? [Y] or [N]")
                add_tertiary = input()
            elif add_secondary == "N":                    
                print("TO BE DONE")
            else:
                print('Invalid choice')

            '''
            
                
            '''
            type_writer("Indicate a time zone you would like to plot these on: ")
            #start_date = input()
            #end_date = input()     
            
            type_writer("Do you want to add a secondary axis? [Y] or [N]")
            add_secondary = input()
            if add_secondary == "Y":
                type_writer("Do you want to add a tertiary axis? [Y] or [N]")
                add_tertiary = input()
            elif add_secondary == "N":
                print("TO BE DONE")
            else:
                print('Invalid choice')
            '''
        
        file_path_one = FILE_CONFIG[first_loc]
        file_path_two = FILE_CONFIG[second_loc]
        x_label = var_var[0]
        y_label = var_var[1]
        
        x,data_set1 = custom_row(x_label, file_path_one)
        y,data_set1 = custom_row(y_label, file_path_two)

        title = y_label + " vs. " + x_label

        merge = merge_time(x,y,x_label,y_label)
        print (merge)

        fig, ax1 = basic_plot(merge[x_label + "_x"], merge[y_label + "_y"], x_label, y_label, f"{y_label} vs. {x_label}")

        show_plot()



    else:
        print('Invalid choice')


    return 0 #do the vars and plot all the stuff in main
get_user_input()