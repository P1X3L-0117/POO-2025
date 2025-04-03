import random

numr = random.randint(1, 850)

numrf = round(random.uniform(1, 10), 2)

#   1. Ejercicio:
#   Escribir un programa en Java que imprima por pantalla la frase “Hola, ya se
#   imprimir frases”.

print("Hola, ya se imprimir frases")

#    2. Ejercicio    Escribir un programa en Java que imprima por pantalla un número entero, por
#    ejemplo el 273, o el 597.

print(numr)

#    3. Ejercicio:
#    Escribir un programa en Java que imprima por pantalla un número decimal, por
#    ejemplo el 5’3, ó el 7’5."

print(numrf)

# 4. Ejercicio:
# Escribir un programa en Java que imprima por pantalla la suma de 1234 y 532.


def suma(a, b):
    a = 1234
    b = 532
    return a + b


resultado = suma(1234, 532)

print(f"La suma de 1234 y 532 es: {resultado}")


# 5. Ejercicio:
# Escribir un programa en Java que imprima por pantalla la resta de 1234 y 532.\


def resta(a, b):
    a = 1234
    b = 532
    return a - b


resultadores = resta(1234, 532)
print(f"La resta de 1234 y 532 es: {resultadores}")


# 7. Ejercicio:
# Escribir un programa en Java que imprima por pantalla la división de 1234 entre
# 532.


def division(a, b):
    a = 1234
    b = 532
    return a / b


resultadod = division(1234, 532)
print(f"La división de 1234 entre 532 es: {resultadod}")


# 8. Ejercicio:
# Escribir un programa en Java que imprima por pantalla los números del 1 al 3.


def imprimir_num():
    for i in range(1, 4):
        print(i)


imprimir_num()


# 9. Ejercicio:
# Escribir un programa en Java que imprima por pantalla los números del 1 al 9.


def imprimir_num():
    for i in range(1, 10):
        print(i)


imprimir_num()


# 10. Ejercicio:
# Escribir un programa en Java que imprima por pantalla los números del 1 al 10.000.
# Conveniente usar bucles.


def imprimir_num():
    n = 1
    while n <= 10000:
        print(n)
        n += 1


imprimir_num()
