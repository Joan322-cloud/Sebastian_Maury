import os
os.system('cls')
# tabla de multiplicar n número
numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 13):
    print(f"{numero} x {i} = {numero * i}")