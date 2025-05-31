import numpy as np
from scipy.signal import square, sawtooth
from src.utils.grapher import continuous_plotter, discrete_plotter, overlay_plotter

def ejecutar_tarea1():
    f = 2
    time = np.linspace(-1, 5, 1000)    
    Ts = 0.01
    n = np.arange(-1, 5, Ts)          

    x_t = np.sin(2 * np.pi * f * time)
    x_n = np.sin(2 * np.pi * f * n)
    continuous_plotter(time, x_t, title="señal senoidal continua", graph_label="continua")
    discrete_plotter(n, x_n, title="señal senoidal discreta", graph_label="discreta")
    overlay_plotter(time, x_t, n, x_n, title="", graph_label1="continua", graph_label2="distreca")

    x_t = np.exp(-2 * time) * (time >= 0)
    x_n = np.exp(-2 * n) * (n >= 0)
    continuous_plotter(time, x_t, title="señal exponencial continua", graph_label="continua")
    discrete_plotter(n, x_n, title="señal exponencial discreta", graph_label="discreta")
    overlay_plotter(time, x_t, n, x_n, title="señal exponencial continua y discreta", graph_label1="continua", graph_label2="distreca")

    x_t = sawtooth(2 * np.pi * f * time, 0.5)
    x_n = sawtooth(2 * np.pi * f * n, 0.5)
    continuous_plotter(time, x_t, title="señal triangular continua", graph_label="continua")
    discrete_plotter(n, x_n, title="señal triangular discreta", graph_label="discreta")
    overlay_plotter(time, x_t, n, x_n, title="señal triangular continua y discreta", graph_label1="continua", graph_label2="distreca")

    x_t = square(2 * np.pi * f * time)
    x_n = square(2 * np.pi * f * n)
    continuous_plotter(time, x_t, title="señal cuadrada continua", graph_label="continua")
    discrete_plotter(n, x_n, title="señal cuadrada discreta", graph_label="discreta")
    overlay_plotter(time, x_t, n, x_n, title="señal cuadrada continua y discreta", graph_label1="continua", graph_label2="distreca")
