contador = 0
numero = 1
while contador < 5:
    if numero % 3 == 0:
        print(numero)
        contador += 1
    numero += 1

print("***************************")


print(10*'_')
contador = 0


for numero in range(1, 100):
    if numero % 3 == 0:
        print(numero)
        contador += 1


    if contador == 520:
        break
print(10*'_')