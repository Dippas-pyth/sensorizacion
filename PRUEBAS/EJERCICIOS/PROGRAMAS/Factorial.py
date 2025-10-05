n = int(input("Número para calculo: "))


def factorial(n):
    n_usados = []

    for i in range(1, n):
        n *= i  # n = n * i
        n_usados.append(i)  # Almacena los números usados en una lista
        print(
            f" Multiplicando por {i}: {n_usados}, Resultado: {n}"
        )  # Muestra el proceso de cálculo

    return n


print(f"factorial de {n} es {factorial(n)}")  # Muestra el resultado final
