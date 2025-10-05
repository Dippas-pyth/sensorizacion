buscar = int(input("Introduzca número a buscar: "))

for numero in range(11):
    print(numero)

    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontrado.")

# ITERACION SOBRE UNA LISTA.
usuarios = ["Alberto", "Diana", "Marcos", "Sara", "Roberto", "Lucas"]
for usuario in usuarios:
    print(usuario)

# ITERACION SOBRE UN STRING
for char in "Hola Mundo":
    print(char)
