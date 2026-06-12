# Iniciamos un bucle que recorrerá una secuencia de números generada de 0 a 4.
# En cada vuelta (iteración), el número actual se guardará automáticamente en 'i'.
for i in range(0, 5):
    
    # Imprime en la consola el valor numérico que tiene la variable 'i' en la vuelta actual.
    # Al igual que antes, después de imprimir, hace un salto de línea automático.
    print(i)


print(40*'-')
for i in range(5):# Un argumento: fin
    print(i)
print(40*'-')
for i in range(2,6):# Dos argumentos: inicio, fin
    print(i)
print(40*'-')
for i in range(1,10,2):# Tres argumentos: inicio, fin, paso
    print(i)
print(40*'-')



for num in range(10):
    if num == 5:
        print("Se cumple la condición que finaliza el bucle")
        break
    print(f"El número actual es {num}")
print("Continuamos tras el bucle")


print(40*'-')
for i in range(5):
    if i == 3:
        break
    print(i)
print(40*'-')


for num in range(10):
    if num == 5:
        continue
    print(f"El número actual es {num}")
print("Continuamos tras el bucle")


print(40*'-')
for i in range(5):
    if i == 2:
        continue
    print(i)
print(40*'-')

for num in range(10):
    if num == 5:
        pass
    print(f"El número actual es {num}")
print("Continuamos tras el bucle")


print(40*'-')
for i in range(5):
    if i == 3:
        pass  # No hace nada, simplemente pasa
    print(i)
print(40*'-')