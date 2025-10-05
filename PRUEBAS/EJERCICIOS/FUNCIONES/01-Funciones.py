def saludo(nombre):  # Incluimos un PARAMETRO (nombre)
    print("Hello?")
    print(f"How are you {nombre}?")


saludo("DIMAS")  # Le pasamos el ARGUMENTO "Dimas" a la función


def saludos(
    name, surname, age
):  # Incluimos los PARAMETROS necesarios (nombre, apellido, edad)
    print("Hello?")
    print(f"How are you {name} {surname}")
    print(f"{name} is {age} years old")


saludos("DIMAS", "GALLEGO", 46)
saludos("MARIA", "MARTINEZ", 34)


def saludos(name1, surname1="GALLEGO"):  # Incluimos PARAMETROS FIJOS (surname1)
    print(f"How are you {name1} {surname1}")


saludos("DIMAS")  # Se incluirá el PARAMETRO por defecto
saludos("PAU")

saludos("GORKA", "SERRANO")  # Se imprimirá el ARGUMENTO especificado.

saludos(
    name1="AITANA", surname1="RUIZ"
)  # Se puede especificar el ARGUMENTO en cualquier llamada.

saludos(
    surname1="PEREZ", name1="DOLORES"
)  # Especificando el ARGUMENTO la FUNCIÓN ordena según los PARAMETROS establecidos.
