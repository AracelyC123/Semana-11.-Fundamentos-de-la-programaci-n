
# Crear una matriz vacía de 5 x 5

matriz = []

# Crear las 5 filas
for fila in range(5):
    fila = []

# Crear las 5 columnas
    for columna in range(5):
        valor = int(input("Ingrese un número: "))
        fila.append(valor)

# Agregar la fila a la matriz
    matriz.append(fila)

# Mostrar la matriz
# \n ayuda a separar los valores como una especie de tabla

print("\nMatriz ingresada:")

for fila in range(5):
    for columna in range(5):
        print(matriz[fila][columna], end="\t")
    print()