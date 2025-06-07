import matplotlib.pyplot as plt

def continuous_plotter(
        ind_var, dep_var, 
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.plot(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

def discrete_plotter(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.stem(ind_var, dep_var, label=graph_label) 
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

def overlay_plotter(
        ind_var1, dep_var1,
        ind_var2, dep_var2,
        title: str = "",
        graph_label1: str = "", graph_label2: str = "",
        x_label: str = "tiempo", y_label: str = "amplitud"):
    plt.plot(ind_var1, dep_var1, label=graph_label1)
    plt.stem(ind_var2, dep_var2, label=graph_label2) 
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()



