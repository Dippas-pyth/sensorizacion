## VARIABLES ## Son contenedores de información
cadena_texto_string = "Hola Mundo"  # Variable que contiene texto entre comillas

# INT() - Variable que contiene un número
numero = 34
numero2 = int("34")  # Convertir string a entero

# FLOAT() - Variable que contiene un número con decimales
decimal = 3.14  # Variable que contiene un número decimal
decimal2 = float(decimal * 2)  # El resultado es un número decimal
decimal3 = float("3.14")  # Convertir string a decimal

# BOOLEANO - Variable que contiene un valor verdadero o falso
booleano = True  # Variable que contiene un valor booleano verdadero
booleano2 = False  # Variable que contiene un valor booleano falso

# NONE - Variable que no contiene ningún valor
nada = None  # Variable que no tiene valor asignado

# OPERADORES DE CONVERSIÓN - int(), float(), str(), list(), tuple(), set(), dict()
numero_convertido = int("123")  # Convierte string a entero
texto_convertido = str(123)  # Convierte entero a string
decimal_convertido = float("3.14")  # Convierte string a float
lista_convertida = list((1, 2, 3))  # Convierte tupla a lista
tupla_convertida = tuple([1, 2, 3])  # Convierte lista a tupla
conjunto_convertido = set(
    [1, 2, 2, 3]
)  # Convierte lista a conjunto (elimina duplicados)
diccionario_convertido = dict(
    [("clave1", "valor1"), ("clave2", "valor2")]
)  # Convierte lista de tuplas a diccionario

# COMPLEJO - Variable que puede contener múltiples tipos de datos
complejo = 3 + 5j  # Variable que contiene un número complejo
complejo2 = complex(2, 4)  # Otra forma de definir un número complejo

# RANGO - Variable que contiene una secuencia de números (MUTABLE)
rango = range(0, 10)  # Variable que contiene un rango de números del 0 al 9

# INPUT - Función para recibir datos del usuario
entrada = input("Introduce un dato: ")
print(f"El dato introducido es: {entrada}")  # f-strings para formatear cadenas

# F-strings - Formateo de cadenas entre llaves {}
# Se puede usar f-strings para incluir variables dentro de cadenas de texto
# FORMAT - Modificar la presentación de los datos
# Se usa format() para formatear cadenas de texto
nombre = "Juan"
edad = 30
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")  # Ejemplo de f-string
print(
    "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
)  # Ejemplo de format()

# --------------------------CONJUNTOS--------------------------------------#

# CONJUNTO - Variable que contiene un conjunto de elementos únicos (MUTABLE)
conjunto = {1, 2, 3, 4, 5}

# --------------------------LISTAS--------------------------------------#

# LISTA VACÍA - Variable que contiene una lista vacía (MUTABLE)
lista_vacia = []
# LISTA - Variable que contiene una lista de elementos (MUTABLE)
lista = [1, 2, 3, 4, 5]
# LISTA DE LISTAS - Variable que contiene una lista de listas (MUTABLE)
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# --------------------------DICCIONARIOS--------------------------------------#

# DICCIONARIO - Variable que contiene un conjunto de pares clave-valor (MUTABLE)
diccionario = {"clave1": "valor1", "clave2": "valor2"}

traductor = {"dog": "perro", "cat": "gato", "bird": "pájaro", "snake": "serpiente"}

print(traductor["cat"])

traductor["fish"] = "pez"  # AÑADIR UNA NUEVA DUPLA AL DICCIONARIO.

print(traductor.keys())  # IMPRIMIMOS TODAS LAS CLAVES
print(traductor.values())  # IMPRIMIMOS TODOS LOS VALORES
print(traductor)  # IMPRIMIMOS TODO EL DICCIONARIO

# TUPLA - Variable que contiene datos relacionados y fijos (INMUTABLE)
tupla = (1, 2, 3)


# --------------------------ESTRUCTURA DE CONTROL-------------------------#


# IF - Estructura CONDICIONAL
edad = 18
if edad >= 18:  # Si la edad es mayor o igual a 18
    print("Eres mayor de edad")  # Imprime este mensaje
else:
    print("Eres menor de edad")  # Imprime este mensaje si la condición es falsa
    print("No puedes acceder al contenido")

# FOR - Estructura de REPETICION
for i in range(11):  # Repite 11 veces, desde 0 hasta 10
    print(i)  # Imprime el valor de i en cada iteración

# WHILE - Estructura de REPETICION CON CONDICIÓN
contador = 0
while contador < 5:  # Mientras el contador sea menor que 5
    print(contador)  # Imprime el valor del contador
    contador += 1  # Incrementa el contador en 1
    if contador == 3:  # Si el contador es igual a 3
        break  # Sale del bucle
    if contador == 1:  # Si el contador es igual a 1
        continue  # Salta a la siguiente iteración
    print("Este mensaje no se imprimirá cuando contador sea 1")
print("Bucle terminado")  # Imprime este mensaje al finalizar el bucle


# FUNCIONES - Bloques de código reutilizables
def saludar(nombre):  # Definición de la función con un parámetro
    """Función que saluda a la persona cuyo nombre se pasa como argumento."""
    print(f"Hola, {nombre}!")  # Imprime un saludo personalizado


saludar("Juan")  # Llamada a la función con el argumento "Juan"
saludar("María")  # Llamada a la función con el argumento "María
saludar("Ana")  # Llamada a la función con el argumento "Ana"
saludar("Luis")  # Llamada a la función con el argumento "Luis"

# IMPORTAR MÓDULOS - Reutilización de código externo
import math  # Importa el módulo matemático

resultado = math.sqrt(16)  # Usa la función sqrt del módulo math
print(f"La raíz cuadrada de 16 es {resultado}")  # Imprime el resultado
# IMPORTAR FUNCIONES ESPECIFICAS de un módulo:
# from ... import ... -
from math import pi, pow  # Importa solo pi y pow del módulo math

print(f"El valor de pi es {pi}")  # Imprime el valor de pi
print(f"2 elevado a la 3 es {pow(2, 3)}")  # Imprime 2 elevado a la 3

# OPERADORES - Realizan operaciones sobre variables y valores:

# ARITMÉTICOS: +, -, *, /, %, //, **
a = 10
b = 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
division_entera = a // b
potencia = a**b

# COMPARACIÓN: ==, !=, >, <, >=, <=
igual = a == b
diferente = a != b
mayor = a > b
menor = a < b
mayor_igual = a >= b
menor_igual = a <= b

# LÓGICOS: and, or, not
logico_and = (a > 5) and (b < 5)  # True si ambas condiciones son verdaderas
logico_or = (a > 5) or (b > 5)  # True si al menos una de las condiciones es verdadera
logico_not = not (a > 5)  # True si la condición es falsa

# ASIGNACIÓN: =, +=, -=, *=, /=, %=, //=, **=
a += 5  # Equivalente a a = a + 5
b *= 2  # Equivalente a b = b * 2
a //= 3  # Equivalente a a = a // 3
b **= 2  # Equivalente a b = b ** 2
# IDENTIDAD: is, is not
c = a  # c es una referencia al mismo objeto que a
identico = a is c  # True si a y c son el mismo objeto
diferente = a is not c  # True si a y c no son el mismo objeto
# PERTENENCIA: in, not in
lista = [1, 2, 3, 4, 5]
pertenece = 3 in lista  # True si 3 está en la lista
no_pertenece = 6 not in lista  # True si 6 no está en la lista
# BIT A BIT: &, |, ^, ~, <<, >>
x = 5  # En binario: 0101
y = 3  # En binario: 0011
and_result = x & y  # Resultado: 0001
or_result = x | y  # Resultado: 0111
xor_result = x ^ y  # Resultado: 0110
not_result = ~x  # Resultado: 1010 (en 2's complement)
left_shift = x << 1  # Resultado: 1010
right_shift = x >> 1  # Resultado: 0010
# OPERADORES DE SLICING (rebanado) - Acceder a partes de secuencias
texto = "Hola Mundo"
subcadena = texto[0:4]  # Extrae "Hola"
subcadena2 = texto[5:]  # Extrae "Mundo"
subcadena3 = texto[-5:]  # Extrae "Mundo" usando índice negativo
reversa = texto[::-1]  # Invierte la cadena, resultado "odnuM aloH"
# OPERADORES DE TIPO - type(), isinstance()
tipo_numero = type(numero)  # Devuelve <class 'int'>
tipo_texto = type(texto)  # Devuelve <class 'str'>
es_numero = isinstance(numero, int)  # True si numero es un entero
es_texto = isinstance(texto, str)  # True si texto es una cadena
