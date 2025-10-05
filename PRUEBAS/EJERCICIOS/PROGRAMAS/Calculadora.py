######### BIENVENIDA E INSTRUCCIONES ########

print("Bienvenido a la calculadora.")
print("Para salir escriba salir")
print("Las operaciones son suma, resta, mult, div y pot.")

####### VARIABLES GLOBALES ########
resultado = ""

########### ENTRADA AL BUCLE #############
while True:
    if not resultado:
        resultado = input("Ingrese N1 o Salir: ")
        if resultado.lower() == "salir":
            print("Adiós!")
            break
        resultado = int(resultado)
        op = input("Ingrese operación:  ")
        if op.lower() == "salir":
            break
        b = input("Introduzca N2 o Salir: ")
        if b.lower() == "salir":
            break
        b = int(b)

        ####### ELEGIMOS EL OPERANDO ###########

        if op.lower() == "suma" or op == "+":
            resultado += b
        elif op.lower() == "resta" or op == "-":
            resultado -= b
        elif op.lower() == "mult" or op == "*":
            resultado *= b
        elif op.lower() == "div" or op == "/":
            resultado /= b
        elif op.lower() == "pot" or op == "^":
            resultado **= b
        else:
            print("OPERACIÓN NO VÁLIDA!!")
            break
        print(f"El resultado es: {resultado}")

        ####### DECIDIMOS SI REINICIAMOS EL BUCLE DE NUEVO ########

        continuar = input("Quiere continuar? S/N: ")

        if continuar.lower() == "n" or continuar.lower() == "no":
            print("Adiós!")
            break
        else:
            resultado = ""
