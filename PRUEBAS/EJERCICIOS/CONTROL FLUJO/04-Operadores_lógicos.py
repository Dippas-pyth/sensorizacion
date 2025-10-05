def pedir_bool(mensaje):
    # Muestra el mensaje al usuario y recoge la respuesta, quitando espacios y pasando a minúsculas
    respuesta = input(mensaje).strip().lower()
    # Devuelve True si la respuesta es "s" o "si", False en cualquier otro caso
    return respuesta in ("s", "si")


def pedir_edad(mensaje):
    # Bucle infinito hasta que el usuario introduzca un valor válido
    while True:
        try:
            # Intenta convertir la entrada del usuario a entero y la retorna si es correcto
            return int(input(mensaje))
        except ValueError:
            # Si la conversión falla (por ejemplo, si el usuario escribe letras), muestra un mensaje y repite
            print("Por favor, introduce un número válido.")


gas = pedir_bool("Hay bombona?(S/N): ")
encendido = pedir_bool("Sale gas?(S/N): ")
edad = pedir_edad("Introduce edad: ")

# AND, OR, NOT

if edad > 17:
    print("Puedes cocinar")
else:
    print("No puedes cocinar")
    exit()

if gas and encendido:
    print("Bienvenido Chef!")
elif gas and not encendido:
    print("Enciende los fogones!")
else:
    print("Fallo en el suministro")


# if gas AND encendido:  # 2 Variables a TRUE ejecuta el código
#     print("Puedes cocinar")

# if gas OR encendido:  # Una u otra variable a TRUE ejecuta el código
#     print("Ten cuidado")

# if (
#    NOT AND NOT encendido ORS
# edad < 17
# ):  # Las 2 Variables a FALSE o edad menor a 17 ejecutan el código
#     print("NO Puedes cocinar")

# if gas and encendido and edad > 17:
#     print("A cocinar!")
