import sys
from src.tarea1 import ejecutar_tarea1
def main(options):
    if options[1] == "tarea_1":
        ejecutar_tarea1()
    elif options[1] == "tarea_2":
        if len(options) > 2:
            understanding_freq(options[2])
        else:
            print("Por favor proporciona una frecuencia. Ejemplo: python main.py tarea_2 2")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Por favor proporciona un argumento.")
        print("Ejemplo (ejecutar tarea 1): python main.py tarea_1")
        print("Ejemplo (ejecutar tarea 2): python main.py tarea_2 2")
