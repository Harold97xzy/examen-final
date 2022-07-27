"""3. (3 ptos) Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que medirá el tiempo de
ejecución. Apoyarse importando la librería time
- Crear una función, por ejemplo, división de dos números para decorarla con
la función anterior.
- Usar la propiedad de N parámetros para la función a decorar (*, **) y
visualizar los resultados con un mínimo tres ejemplos.
Sugerencia: Usar sleep para visualizar mejor el tiempo de ejecución
"""

import time


def funcionA(func):

    def calcular(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        total = time.time() - start
        print("Tiempo de ejecución es: {}".format(total))
        return result
    return calcular


@funcionA
def divison(a, b):
    time.sleep(1)
    resultado = a / b
    return resultado


print(divison(90, 10))

# Tiempo 1 = 1.2636020183563232
# Tiempo 2 = 1.0140018463134766
# Tiempo 3 = 1.7940032482147217
