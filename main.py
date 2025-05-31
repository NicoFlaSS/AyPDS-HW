import sys
from src.tarea1 import ejecutar_tarea1
def main(options):
    if options[1] == "tarea_1":
        ejecutar_tarea1()
    elif options[1] == "tarea_2":
        if len(options) > 2:
            understanding_freq(options[2])
        else:
            print("Please give a frequency. Example: python main.py act_2 2")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run activity 1 ) : python main.py act_1")
        print("Example ( run activity 2 ) : python main.py act_2 1")