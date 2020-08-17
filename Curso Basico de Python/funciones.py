# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# def conversacion(numero):
#     print("Hola")
#     print("Como estas")
#     print("Elegiste la opcion "+str(numero))
#     print("Adios")

# while 1:
#     opcion = int(input("Elige una opcion (1,2,3): "))
#     if opcion==1:
#         conversacion(opcion)
#     elif opcion==2:
#         conversacion(opcion)
#     elif opcion==3:
#         conversacion(opcion)
#     else:
#         print("Escribe la opcion correcta")

def suma(a,b):
    print("Se suman dos numeros")
    resultado = a+b
    return resultado

sumatoria = suma(1,4)
print(sumatoria)