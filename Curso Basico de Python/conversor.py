pesos = input("¿Cuantos pesos tienes?: ")
pesos=float(pesos)
valorDolar= 22.75
dolares = pesos / valorDolar
dolares = round(dolares,2)
dolares=str(dolares)
print("Tienes $"+dolares+" Dolares")