vocabulario = {
    "hello": "hola",
    "goodbye": "adios",
    "please": "por favor",
    "thank you": "gracias",
    "water": "agua",
    "food": "comida",
    "house": "casa",
    "friend": "amigo",
    "time": "tiempo",
    "love": "amor",
}


def traducir(palabra):
    traducción = vocabulario.get(palabra.lower())
    if traducción:
        print(f"{palabra} en Español es {traducción}")
    else:
        print(f"No se encontró traducción para {palabra}")


while True:

    palabra_usuario = input("Introduzca palabra para traducir o exit para salir: ")
    if palabra_usuario.lower() == "exit":
        break
    traducir(palabra_usuario)
