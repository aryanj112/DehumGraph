from plotter import basic_plot, show_plot
import time
from data_loader import data_loader, merge_time, custom_row

FILE_CONFIG = {
    'FR_DOOR': r"C:\Users\ajayj\DehumGraph\data\Main Data\Frontdoor.csv",
    'BASE': r"C:\Users\ajayj\DehumGraph\data\Main Data\Base(guest).csv",
    'Input': r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(in).csv",
    'Output': r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(out).csv",
    'Dehum': r"C:\Users\ajayj\DehumGraph\data\Main Data\Dehum.csv",
}

NUM_CONFIG = {
    '1': 'FR_DOOR',
    '2': 'BASE',
    '3': 'Input', 
    '4': 'Output',
    '5': 'Dehum',
    '6': 'Temperature(F)',
    '7': 'Humidity(%)',
    '8': 'Dewpoint(F)',
    '9': 'HeatIndex(F)',
    '10': 'Absolute Humidity(g/m^3)',
    '11': 'L/kWh',
    '12': 'Avg Abs Hum',
    '13': 'Avg Rel Hum Deh(in) - Deh(out)',
}

def type_potential_vars(loc):
    ambient_vars = ["Temperature(F) [6]", "Humidity(%) [7]", "Dewpoint(F) [8]", "HeatIndex(F) [9]", "Absolute Humidity(g/m^3) [10]"]
    dehum_vars = ["L/kWh [11]", "Avg Abs Hum [12]", "Avg Rel Hum Deh(in) - Deh(out) [13]"]
    
    type_writer(f"Here are the potential variables you can plot for {loc}:")
    
    if loc in ["FR_DOOR", "BASE", "Input", "Output"]:
        for var in ambient_vars:
            type_writer(f"- {var}")
    elif loc == "Dehum":
        for var in dehum_vars:
            type_writer(f"- {var}")

    var = input("Select a variable: ")
    return var

def type_data_sources():
    type_writer("- Front Door [1]")
    type_writer("- Basement [2]")
    type_writer("- Dehumidifier Input [3]")
    type_writer("- Dehumidifier Output [4]")
    type_writer("- Dehumidifier [5]")

def type_writer(text, delay=0.0):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_user_input():
    
    # Introduction
    type_writer("Welcome to the Dehumidifier Graph program.")
    type_writer("Here, you can visualize data from different sources, including:")
    type_data_sources()
    type_writer("Explore and plot various pieces of information with ease!")

    # User's choice: var_time or var_var
    type_writer("\nTo begin, would you prefer to view the trend of a variable over time [var_vs_time] or compare that variable against another variable? [var_vs_var]")
    type_writer("Note: Choices are indicated within square brackets.")
    against = input("[var_vs_time] or [var_vs_var]: ")

    if against == "var_vs_time":
        # User selects a single location
        type_writer("\nWhere would you like to visualize data:")
        type_data_sources()
        loc = input()
        plot_var = type_potential_vars(NUM_CONFIG[loc])

        # User decides on secondary and tertiary axes
        type_writer("Do you want to add a secondary axis? [Y] or [N]")
        add_secondary = input()
        if add_secondary == "Y":
            type_writer("Do you want to add a tertiary axis? [Y] or [N]")
            add_tertiary = input()

        # Plot based on user's choices
        elif add_secondary == "N":
            x_label = 'Time'
            y_label = plot_var
            file_path = FILE_CONFIG[NUM_CONFIG[loc]]
            x, y, dataset = data_loader(x_label, y_label, file_path)
            title = f"{y_label} vs. {x_label} at {loc}"
            basic_plot(x, y, x_label, y_label, title)
            show_plot()
        else:
            print('Invalid Choice')

    elif against == "var_vs_var":
        # User selects two locations and their respective variables
        type_writer("\nWhat is the first location you would like to visualize data:")
        type_data_sources()
        first_loc = input("\nFirst Location: ")
        type_writer("\nWhat is the second location you would like to visualize data:")
        second_loc = input("Second Location: ")
        loc = [first_loc, second_loc]
        plot_vars = []

        for single_loc in loc:
            plot_var = type_potential_vars(NUM_CONFIG[single_loc])
            plot_vars.append(NUM_CONFIG[plot_var])

        # TO BE DONE: User input for time zone and additional axes
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

        # Plot based on user's choices

        file_path_one = FILE_CONFIG[NUM_CONFIG[first_loc]]
        file_path_two = FILE_CONFIG[NUM_CONFIG[second_loc]]
        x_label = plot_vars[0]
        y_label = plot_vars[1]

        x, data_set1 = custom_row(x_label, file_path_one)
        y, data_set2 = custom_row(y_label, file_path_two)

        title = f"{y_label} vs. {x_label}"

        if first_loc == "Dehum" or second_loc == "Dehum":
            overlap_bool=True
        else:
            overlap_bool=False

        merge = merge_time(x, y, x_label, y_label,  average_overlapping=overlap_bool)
        fig, ax1 = basic_plot(merge[x_label], merge[y_label], x_label, y_label, title)

        show_plot()

    else:
        print('Invalid choice')
    

    return 0

# Execute the main function
get_user_input()