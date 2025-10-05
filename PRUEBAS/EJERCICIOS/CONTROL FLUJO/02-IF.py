edad = int(input("Cuántos años tiene? "))

if edad > 65:
    print("Puede entrar gratis al cine.")
    print("Gracias por venir!")
elif edad > 54:

    print("Puede ver la película con descuento.")
    print("Bienvenido!")

elif edad >= 18:
    print("Puede ver la película.")

else:
    print("No puede entrar.")
    print("Ve a otro lado.")

print("Listo!")
