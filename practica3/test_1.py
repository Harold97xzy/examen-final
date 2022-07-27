"""
1. Escribir un programa para el manejo de listas el cuál cumplirá los siguientes
requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 número aleatorios e
imprimirlos por consola.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará lista para ordenar de mayor a menor la
lista que se creará en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlo por
consola.
- Crear una función para indicar cuál es mayor número de la lista (lista del
ítem 2), retornar este valor e imprimirlo por consola.
"""

lista = []

"""Usando iteración con for"""

def almacenar():
    for item in range(10):
        lista.append(item)

    print("El valor de mi lista es: {}".format(lista))

def norepetir():

    lista.count()
    print("Mi lista no repetida es: {}".format(lista))

def ordenar():
    lista.sort()
    print("Mi lista ordenado de menor a mayor es: {}".format(lista))
    lista.reverse()
    print("Mi lista de mayor a menor es: {}".format(lista))

#def cualesmayor():


almacenar()
norepetir()
ordenar()

