for i in range(13):
    print("voy a repasar python al menos una hora al dia")
for num in range(10):
    if num == 5:
        continue
    print(f"el numero actual es {num}")
print("continuamos con el bucle")
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