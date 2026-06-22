fila = 0 # Variable que controla las filas
while fila < 3: # Mientras fila sea menor que 3
    columna = 0    # Variable que controla las columnas
    while columna < 4:     # Mientras columna sea menor que 4
        print("*", end=" ")  # Imprime un asterisco sin cambiar de línea
        columna += 1       # Avanza a la siguiente columna
    print()     # Salto de línea al terminar una fila
    fila += 1    # Avanza a la siguiente fila



print(8*'_')
for i in range(3):
    for j in range(4):
        print("*",end=" ")
    print()
print(8*'_')


print(8*'_')
n = int(input("Ingresar un número: "))


for fila in range(n):
    for columna in range(n):
        print("*", end=" ")
    print()
print(8*'_')