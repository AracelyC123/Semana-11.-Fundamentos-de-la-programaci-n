
#reservas de cine
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


fila = int(input("Ingrese la fila (0 a 2): "))
columna = int(input("Ingrese la columna (0 a 3): "))


asientos[fila][columna] = 1

print("\nEstado de la sala:")

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
