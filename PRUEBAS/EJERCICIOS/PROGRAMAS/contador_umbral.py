import random

while True:
    N_objetivo = int(input(f"Introduce tu número del (1 - 20): "))
    N_random = random.randint(1, 20)
    intentos = 1

    while N_random != N_objetivo:

        if N_random > N_objetivo:
            print("Mayor!")
            intentos += 1

        elif N_random < N_objetivo:
            print("Menor!")
            intentos += 1

        N_objetivo = int(input("Introduce número: "))

    print(f"Felicidades! {N_random} es el número!!")
    print(f"Has necesitado {intentos} intentos! Enhorabuena!!")

    seguir = input("Quieres seguir? (s/n): ").lower()
    if seguir != "s":
        print("Adios!!")
        break
    else:
        print("Sigamos jugando!!")
