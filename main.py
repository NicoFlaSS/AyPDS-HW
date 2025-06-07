import sys
from src.tarea1 import ejecutar_tarea1
from src.tarea2 import understanding_freq
from src.tarea3 import ejecutar_tarea3  
from src.tarea4 import ejecutar_tarea4

def main(options):
    if options[1] == "tarea_1":
        ejecutar_tarea1()

    elif options[1] == "tarea_2":
        if len(options) > 2:
            understanding_freq(options[2])
        else:
            print("Please give a frequency. Example: python main.py tarea_2 2")

    elif options[1] == "tarea_3":
        if len(options) == 5:
            A = float(options[2])
            f = float(options[3])
            phi = float(options[4])
            ejecutar_tarea3(A, f, phi)
        else:
            print("Please provide the 3 parameters: Amplitude, Frequency, and Phase.")
            print("Example: python main.py tarea_3 1 2 0.785")

        
    elif options[1] == "tarea_4":
        if len(options) > 2:
            ejecutar_tarea4(options[2])
        else:
            print("Usage: python main.py tarea_4 <número_de_bits>")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run activity 1 ) : python main.py tarea_1")
        print("Example ( run activity 2 ) : python main.py tarea_2 1")
        print("Example ( run activity 3 ) : python main.py tarea_3 1 2 0.785")
        print("Example ( run activity 4 ) : python main.py tarea_4 3")
    


  
