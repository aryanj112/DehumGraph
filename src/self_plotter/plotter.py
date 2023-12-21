import matplotlib.pyplot as plt

def basic_plot(x, y, x_label, y_label, title):
    fig, ax1 = plt.subplots()
    ax1.plot(x,y,"-", label = title, color="tab:blue")
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    ax1.set_title(title)
    ax1.legend()
    
    return fig, ax1

def add_vertical_line():

    return 0

def add_secondary_axis():

    return 0

def add_tertiary_axis():
    return 0

def save_plot():

    return 0

def show_plot():
    return 0 
