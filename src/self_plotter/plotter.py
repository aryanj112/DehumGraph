import matplotlib.pyplot as plt

def basic_plot(x, y, x_label, y_label, title):
    fig, ax1 = plt.subplots()
    ax1.plot(x,y,"o", label = y_label, color="tab:blue")
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    ax1.set_title(title)
    ax1.legend()
    return fig, ax1

def add_vertical_line():

    return 0

def add_secondary_axis(fig, ax1, x, y, y2_label):
    ax2 = ax1.twinx()
    ax2.plot(x,y,"-", label = y2_label, color="tab:purple")
    return fig, ax1

def add_tertiary_axis(fig, ax1, x, y, y3_label):
    
    ax3 = ax1.twinx()
    ax3.plot(x,y,"-", label = y3_label, color="tab:red")
    return fig, ax1

def save_plot(title):
    plot_filename = fr"C:\Users\ajayj\DehumGraph\plots\plotter\{title}.png"
    plt.savefig(plot_filename, dpi=500, bbox_inches='tight')
    print(f"Plot saved as '{plot_filename}'")

def show_plot():
    plt.tight_layout()
    plt.show()