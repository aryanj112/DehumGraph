from plotter import basic_plot, show_plot
import time
from data_loader import data_loader

NICK_NAME = {
    'FR_DOOR': 'front_door_path',
    'BASE': 'basement_guest_path',
    'Input': 'dehum_input_path', 
    'Output': 'dehum_output_path', 
    'Dehum': 'dehumidifier_path',
}

FILE_CONFIG = {
    'front_door_path': r"C:\Users\ajayj\DehumGraph\data\Main Data\Frontdoor.csv",
    'basement_guest_path': r"C:\Users\ajayj\DehumGraph\data\Main Data\Base(guest).csv",
    'dehum_input_path': r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(in).csv",
    'dehum_output_path': r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(out).csv",
    'dehumidifier_path': r"C:\Users\ajayj\DehumGraph\data\Main Data\Dehum.csv",
}

def type_writer(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_user_input():
    type_writer("Welcome to the Dehumidifier Graph program.")
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
                key_in_file_config = NICK_NAME[loc]
                file_path = FILE_CONFIG[key_in_file_config]
                x, y, dataset = data_loader(x_label, y_label, file_path)
                title = f"{y_label} vs. {x_label} at {loc}"
                basic_plot(x, y, x_label, y_label, title)
                show_plot()
            else:
                print('Invalid choice')
        elif loc == "Dehum":
            type_writer("Here are the potential variables you can plot:")
        else:
            print('Invalid location')
    elif against == "var_var":
        print("Not implemented yet")
    else:
        print('Invalid choice')

    return 0

get_user_input()
