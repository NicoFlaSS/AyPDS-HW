import numpy as np
from src.utils.grapher import continuous_plotter

def ejecutar_tarea4(num_bits):
    num_bits = int(num_bits)
    Vfs = 5.0  
    niveles = 2 ** num_bits
    paso = Vfs / (niveles - 1)
    resolucion_pct = (paso / Vfs) * 100

    print(f"Bits: {num_bits}")
    print(f"Niveles: {niveles}")
    print(f"Tamaño del paso: {paso:.6f} V")
    print(f"Resolución porcentual: {resolucion_pct:.6f} %")

    entradas_digitales = np.arange(niveles)
    salidas_analogicas = entradas_digitales * paso
    continuous_plotter(
        entradas_digitales, salidas_analogicas,
        title=f'DAC de {num_bits} bits',
        graph_label='Salida analógica',
        x_label='Entrada digital',
        y_label='Voltaje [V]'
    )
