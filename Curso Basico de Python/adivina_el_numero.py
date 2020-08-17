import random


def run():
    numeroRandom = random.randint(1,100)
    numeroChoice = int(input("Elige un numero del 1 al 100 : "))
    while numeroChoice != numeroRandom:
        if numeroChoice<numeroRandom:
            print("Busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        numeroChoice=int(input("Elige otro numero: "))
    print("Ganaste")


if __name__ == '__main__':
    run()