############# EJERCICIO 1 ##############

# contador = 1

# while contador < 100:  # Mientras contador sea menor a 100
#     print(contador)  # Devuelve contador
#     contador *= 2  # Duplica contador en cada Iteración

comando = ""

############# EJERCICIO 2 ##############

# while comando.lower() != "salir":
#     comando = input("$ ")
# print(comando)

############# EJERCICIO 3 ##############

while True:
    comando = input("$ ")
    if comando.lower() == "salir":  # Cuando comando sea el especificado
        break  # Termina la ejecución.

print("Adios!")
