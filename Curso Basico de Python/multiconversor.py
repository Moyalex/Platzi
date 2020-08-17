def conversor(tipoPesos,valorDolar):
    pesos = input("¿Cuantos pesos "+tipoPesos+" tienes?: ")
    pesos=float(pesos)
    dolares = pesos / valorDolar
    dolares = round(dolares,2)
    dolares=str(dolares)
    print("Tienes $"+dolares+" Dolares")

while 1:
    menu = """
    Bienvenido al conversor de monedas 

    1.- Pesos Colombianos
    2.- Pesos Argentinos
    3.- Pesos Mexicanos

    Elige una opcion:"""

    opcion = int(input(menu))
    valorDolar = 0
    moneda=""
    if opcion==1:
        conversor("Colombianos",3875)
        # valorDolar=3875
        # moneda="Colombianos"
    elif opcion==2:
        conversor("Argentinos",65)
        # valorDolar=65
        # moneda="Argentinos"
    elif opcion==3:
        conversor("Mexicanos",24)
        # valorDolar=24
        # moneda="Mexicanos"
    else:
        print("Ingresa una opcion correcta por favor")