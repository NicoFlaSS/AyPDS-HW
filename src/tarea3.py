import numpy as np
import matplotlib.pyplot as plt

def ejecutar_tarea3(A, f, phi):
    t0 = 0
    tf = 5
    N = 1000
    Ts = 0.01 
    A = float(A)
    f = float(f)
    phi = float(phi)
    t = np.linspace(t0, tf, N)
    xt = A * np.sin(2 * np.pi * f * t + phi)

    A_ref = 1
    f_ref = 1
    phi_ref = 0
    x_ref = A_ref * np.sin(2 * np.pi * f_ref * t + phi_ref)

    n = np.arange(0, int(tf / Ts))
    td = n * Ts
    xd = A * np.sin(2 * np.pi * f * td + phi)
    x_ref_d = A_ref * np.sin(2 * np.pi * f_ref * td + phi_ref)

    plt.figure(figsize=(10, 4))
    plt.plot(t, xt, label="Señal continua modificada")
    plt.plot(t, x_ref, '--', label="Referencia continua (A=1, f=1Hz, φ=0)")
    plt.title("Señal Senoidal en Tiempo Continuo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.tight_layout()

    plt.figure(figsize=(10, 4))
    plt.stem(td, xd, linefmt='b-', markerfmt='bo', basefmt='k-', label='Señal discreta modificada')
    plt.stem(td, x_ref_d, linefmt='r--', markerfmt='ro', basefmt='k-', label='Referencia discreta (A=1, f=1Hz, φ=0)')
    plt.title("Señal Senoidal en Tiempo Discreto")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.tight_layout()

    plt.show()
