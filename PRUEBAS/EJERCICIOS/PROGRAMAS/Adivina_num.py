import random

while True:
    n_usuario = int(input("Adivina el número (1-5): "))
    n_secreto = random.randint(1, 5)
    intentos = 1

    while n_usuario != n_secreto:

        if n_usuario < n_secreto:
            print("El número es mayor")
            intentos += 1

        elif n_usuario > n_secreto:
            print("El número es menor")
            intentos += 1
        n_usuario = int(input("Inténtalo de nuevo: "))

    print(f"¡Felicidades! Has adivinado el número {n_secreto}.")
    print(f"Has realizado un total de  {intentos} intentos!")
    seguir = input("¿Quieres jugar de nuevo? (s/n): ").lower()

    if seguir != "s":
        print("Gracias por jugar. ¡Hasta luego!")
        break
    else:
        print("¡Vamos a jugar de nuevo!")
