#### return - NOS DEVUELVE VALORES DE DENTRO DE LA FUNCION ####


# Definición de la función 'suma' que recibe dos parámetros
def suma(a, b):
    # Realiza la operación de suma entre los dos parámetros
    resultado = a + b
    # Retorna el resultado de la suma
    return resultado


###### LLAMADAS A LA FUNCIÓN: ######

# Primera llamada: suma los números 1 y 2
# El resultado (3) se almacena en la variable 'c'
c = suma(1, 2)

# Segunda llamada: usa el resultado anterior 'c' (que vale 3) y lo suma con 2
# El resultado (5) se almacena en la variable 'd'
d = suma(c, 2)

# Imprime el resultado final almacenado en 'd'
print(d)  # Output: 5
