animal = "  igüanA goMEz  "

print(animal.upper())  # Mayúsculas.
print(animal.lower())  # Minúsculas.
print(animal.capitalize())  # Primera letra en mayúscula resto en minúsculas.
print(
    animal.title()
)  # Cambia a mayúsculas las primeras letras del string y el resto a minúsculas.

print(animal.strip())  # Elimina los espacios en blanco a la izquierda del string.
print(animal.lstrip())  # Elimina espacios a IZQUIERDA.
print(animal.rstrip())  # Elimina espacios a DERECHA.

print(animal.find("go"))  # Busca "" en el argumento. -1 NO ENCONTRADO.
print(animal.replace("gü", "Ju"))  # Sustituir partes.

print("me" in animal)  # Comprueba que EXISTA "" en STRING.
print("me" not in animal)  # Comprueba que NO EXISTA "" en el STRING.

#### ENCADENAR MÉTODOS ####
print(animal.strip().capitalize())
