# EJEMPLO DE RANGOS range()

# range(n) - Genera números desde 0 hasta n-1
rango1 = range(4)
print(list(rango1))

# range(inicio, fin) - Genera números desde 'inicio' hasta 'fin-1'
rango2 = range(1, 11)
print(list(rango2))

# range(inicio, fin, paso) - Genera números
rango3 = range(0, 21, 5)
print(list(rango3))

# range(inicio, fin, paso) - Genera números desde 'inicio' hasta 'fin-1' con un 'paso' específico (paso negativo)
rango4 = range(20, 0, -3)
print(list(rango4))
