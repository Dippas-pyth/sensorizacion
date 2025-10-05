#### ARGUMENTOS DEFINIDOS ####


def suma(a, b):
    print(a + b)


suma(2, 5)


def suma(a, b, c):
    print(a + b + c)


suma(2, 5, 3)


#### X.ARGS ### FUNCIONES CON Nº DE ARGUMENTOS INDEFINIDOS ###


def suma(*numeros):  # Convertimos la función en ITERABLE
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(2, 5, 3)
suma(2, 5, 2, 3, 4, 5, 6, 10)
