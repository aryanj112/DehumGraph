import time

def type_writer(text, delay=0.0):
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
    type_writer("[var_time] or [var_var]: ")
    against = input()

    if (against == "var_time"):
        type_writer("\nWhere would you like to visualize data:")
        type_writer("- Front Door [FR_DOOR]")
        type_writer("- Basement [BASE]")
        type_writer("- Dehumidifier Input [Input]")
        type_writer("- Dehumidifier Output [Output]")
        type_writer("- Dehumidifier [Dehum]")
        loc = input()
        if loc in ["FR_DOOR", "BASE", "Input", "Output"]:
            type_writer("Here are the potential variables you can plot:")
            type_writer("- Front Door [FR_DOOR]")
            type_writer("- Basement [BASE]")
            type_writer("- Dehumidifier Input [Input]")
            type_writer("- Dehumidifier Output [Output]")
            type_writer("- Dehumidifier [Dehum]")
        elif (loc == "Dehum"):
            type_writer("Here are the potential variables you can plot:")

        else:
            print('Invalid location')
    
    elif (against == "var_var"):
        print("hey")
    
    
    else:
        print('Invalid location')

    return 0

get_user_input()