import numpy as np
import matplotlib.pyplot as plt

def ejecutar_tarea3(A, f, phi):
    t0 = 0             
    tf = 5              
    N = 1000           
    t = np.linspace(t0, tf, N)
    A = float(A)
    f = float(f)
    phi = float(phi)
    xt = A * np.sin(2 * np.pi * f * t + phi)
    A_ref = 1
    f_ref = 1
    phi_ref = 0
    x_ref = A_ref * np.sin(2 * np.pi * f_ref * t + phi_ref)
    
    plt.plot(t, xt, label="Señal Modificada")
    plt.plot(t, x_ref, '--', label="Referencia (A=1, f=1Hz, φ=0)")
    plt.title('Comparación de Señales Senoidales')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
